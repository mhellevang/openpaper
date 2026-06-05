# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx"]
# ///
"""
Throwaway spike: can Gemma 4 (E2B/E4B) drive OpenPaper's two LLM jobs locally?

Tasks:
  A1  per-article relevance scoring (map-reduce style), run twice for consistency
  A2  whole-pool editorial selection (exploits the 128K context window)
  B   Norwegian (bokmål) summarisation across roles: lead / lg / md / brief

Material: the real corpus in .openpaper/saved/2026-06-05-morning/ plus
preferences.md. The edition Claude actually produced (editions/draft.yaml) is the
reference to eyeball outputs against. Nothing here touches production code.

Usage:
  uv run spike/local_model_spike.py                # default model gemma4:e4b
  uv run spike/local_model_spike.py --model gemma4:e2b
"""
from __future__ import annotations

import argparse
import json
import pathlib
import time

import httpx

ROOT = pathlib.Path(__file__).resolve().parent.parent
CORPUS = ROOT / ".openpaper" / "saved" / "2026-06-05-morning"
PREFS = ROOT / ".openpaper" / "preferences.md"
OUT = pathlib.Path(__file__).resolve().parent / "out"
OLLAMA = "http://localhost:11434/api/generate"
NUM_CTX = 32768

# Articles chosen for the summarisation test: one per role, mixing
# English sources (translation test) with a native Norwegian source.
SUMMARY_TARGETS = [
    ("lead", "world-first-vaccine-designed-by-ai-could-protect-against-whole-families-of-virus.json"),
    ("lg", "when-ai-builds-itself-our-progress-toward-recursive-self-improvement.json"),
    ("md", "after-11-years-at-mars-nasas-maven-spacecraft-went-out-with-a-whisper.json"),
    ("brief", "isolerer-suicidale-barn-i-fengsel-svært-urovekkende.json"),
]

ROLE_SPEC = {
    "lead": "3-4 avsnitt. Narrativ bue: scene → utvikling → betydning → hva nå. "
            "Returner JSON {\"kicker\",\"deck\",\"paragraphs\":[..],\"photo_caption\"}.",
    "lg": "Nøyaktig 2 avsnitt: nøkkelfakta først, ett sitat/talende detalj i andre. "
          "Returner JSON {\"kicker\",\"deck\",\"paragraphs\":[..]}.",
    "md": "Ett stramt avsnitt: hvem, hva, hvorfor det betyr noe. "
          "Returner JSON {\"kicker\",\"paragraphs\":[\"...\"]}.",
    "brief": "Én setning, maks 15 ord. "
             "Returner JSON {\"bold\":\"tema/kilde\",\"text\":\"én setning.\"}.",
}

BOKMAL_RULES = (
    "Skriv alt på norsk (bokmål). Oversett engelske kilder til naturlig, "
    "journalistisk bokmål; behold egennavn. Fornorsk faste engelske uttrykk "
    "(f.eks. «game changer» → «et gjennombrudd»). Ikke behold engelsk «The» "
    "foran organisasjonsnavn. Svar KUN med gyldig JSON, ingen forklaring."
)


def call(model: str, prompt: str, *, system: str = "", temperature: float = 0.0) -> tuple[str, float]:
    body = {
        "model": model,
        "prompt": prompt,
        "system": system,
        "stream": False,
        "format": "json",
        "options": {"num_ctx": NUM_CTX, "temperature": temperature},
    }
    t0 = time.monotonic()
    r = httpx.post(OLLAMA, json=body, timeout=600.0)
    r.raise_for_status()
    dt = time.monotonic() - t0
    return r.json()["response"], dt


def load_corpus() -> list[dict]:
    arts = []
    for p in sorted(CORPUS.glob("*.json")):
        d = json.loads(p.read_text())
        d["_file"] = p.name
        arts.append(d)
    return arts


def parse_json(s: str) -> dict | list | None:
    try:
        return json.loads(s)
    except Exception:
        return None


# ---------------------------------------------------------------- Task A1
def task_a1(model: str, prefs: str, arts: list[dict], run: int) -> list[dict]:
    rubric = (
        "Du er ansvarlig redaktør for en personlig avis. Gi artikkelen en "
        "relevansscore mellom 0.0 og 1.0 ut fra leserens preferanser nedenfor. "
        "Returner KUN JSON: {\"score\": <0-1>, \"topic\": \"<kort emne>\", "
        "\"reason\": \"<kort begrunnelse på norsk>\"}.\n\nPREFERANSER:\n" + prefs
    )
    results = []
    for a in arts:
        content = (a.get("content") or "")[:800]
        prompt = (
            f"TITTEL: {a['title']}\nKILDE: {a['source']}\n"
            f"SAMMENDRAG: {a.get('summary', '')}\nUTDRAG: {content}"
        )
        resp, dt = call(model, prompt, system=rubric, temperature=0.3)
        j = parse_json(resp) or {}
        results.append({
            "file": a["_file"], "title": a["title"], "source": a["source"],
            "score": j.get("score"), "topic": j.get("topic"),
            "reason": j.get("reason"), "secs": round(dt, 1),
        })
        print(f"  [A1 r{run}] {a['source']:12} {str(j.get('score')):>5}  {a['title'][:55]}")
    return results


# ---------------------------------------------------------------- Task A2
def task_a2(model: str, prefs: str, arts: list[dict]) -> tuple[dict | None, float]:
    listing = "\n".join(
        f"{i}. [{a['source']}] {a['title']} — {a.get('summary', '')[:160]}"
        for i, a in enumerate(arts)
    )
    system = (
        "Du er ansvarlig redaktør. Velg og ranger artikler til en 14-saks avis "
        "ut fra leserens preferanser. Tildel redaksjonelle roller. Regler: maks "
        "30% per emne; lead bør være tech/KI eller viktig norsk sak; balanser "
        "kilder. Returner KUN JSON: {\"lead\": <id>, \"majors\": [<id>..], "
        "\"mids\": [<id>..], \"briefs\": [<id>..], \"reasoning\": \"<kort>\"}.\n\n"
        "PREFERANSER:\n" + prefs
    )
    resp, dt = call(model, "ARTIKLER:\n" + listing, system=system, temperature=0.3)
    return parse_json(resp), dt


# ---------------------------------------------------------------- Task B
def task_b(model: str, arts_by_file: dict[str, dict]) -> list[dict]:
    out = []
    for role, fname in SUMMARY_TARGETS:
        a = arts_by_file[fname]
        system = (
            f"Du skriver en avissak i rollen «{role}». {ROLE_SPEC[role]}\n"
            + BOKMAL_RULES
        )
        prompt = (
            f"TITTEL: {a['title']}\nKILDE: {a['source']}\n"
            f"FORFATTER: {a.get('author', '')}\n\nARTIKKELTEKST:\n{a.get('content', '')}"
        )
        resp, dt = call(model, prompt, system=system, temperature=0.6)
        out.append({"role": role, "file": fname, "title": a["title"],
                    "source": a["source"], "json": parse_json(resp),
                    "raw": resp, "secs": round(dt, 1)})
        print(f"  [B] {role:6} {dt:5.1f}s  {a['title'][:55]}")
    return out


# ---------------------------------------------------------------- runner
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="gemma4:e4b")
    args = ap.parse_args()
    model = args.model

    OUT.mkdir(exist_ok=True)
    prefs = PREFS.read_text()
    arts = load_corpus()
    by_file = {a["_file"]: a for a in arts}
    print(f"Model: {model} | {len(arts)} articles | num_ctx={NUM_CTX}\n")

    print("== Task A1: per-article scoring (2 runs) ==")
    a1_r1 = task_a1(model, prefs, arts, 1)
    a1_r2 = task_a1(model, prefs, arts, 2)

    print("\n== Task A2: whole-pool editorial selection ==")
    a2, a2_secs = task_a2(model, prefs, arts)

    print("\n== Task B: bokmål summaries (lead/lg/md/brief) ==")
    b = task_b(model, by_file)

    tag = model.replace(":", "_")
    (OUT / f"results_{tag}.json").write_text(json.dumps(
        {"model": model, "a1_run1": a1_r1, "a1_run2": a1_r2,
         "a2": a2, "a2_secs": a2_secs, "b": b}, ensure_ascii=False, indent=2))
    write_report(model, tag, arts, a1_r1, a1_r2, a2, a2_secs, b)
    print(f"\nWrote spike/out/results_{tag}.json and report_{tag}.md")


def write_report(model, tag, arts, r1, r2, a2, a2_secs, b) -> None:
    L = [f"# Spike report — {model}\n"]

    L.append("## A1 — per-article scoring (consistency between 2 runs)\n")
    L.append("| source | title | run1 | run2 | Δ | topic |")
    L.append("|---|---|---|---|---|---|")
    deltas = []
    for x, y in zip(r1, r2):
        s1, s2 = x["score"], y["score"]
        try:
            d = abs(float(s1) - float(s2)); deltas.append(d); d = f"{d:.2f}"
        except Exception:
            d = "?"
        L.append(f"| {x['source']} | {x['title'][:45]} | {s1} | {s2} | {d} | {x['topic']} |")
    if deltas:
        L.append(f"\n_Mean |Δ| across runs: {sum(deltas)/len(deltas):.3f} "
                 f"(max {max(deltas):.2f})_\n")
    rank = sorted(r1, key=lambda z: (float(z["score"]) if z["score"] is not None else -1), reverse=True)
    L.append("\n**Run-1 ranking (top→bottom):**\n")
    for z in rank:
        L.append(f"- {z['score']} · [{z['source']}] {z['title'][:60]}")

    L.append("\n## A2 — whole-pool editorial selection\n")
    if a2:
        def titles(ids):
            return [f"{i}:{arts[i]['title'][:50]}" for i in ids if isinstance(i, int) and i < len(arts)]
        lead = a2.get("lead")
        lead_t = arts[lead]["title"][:60] if isinstance(lead, int) and lead < len(arts) else lead
        L.append(f"- **lead:** {lead_t}")
        L.append(f"- **majors:** {titles(a2.get('majors', []))}")
        L.append(f"- **mids:** {titles(a2.get('mids', []))}")
        L.append(f"- **briefs:** {titles(a2.get('briefs', []))}")
        L.append(f"- _reasoning:_ {a2.get('reasoning', '')}")
        L.append(f"- _({a2_secs:.1f}s)_")
    else:
        L.append("_(failed to parse JSON)_")
    L.append("\n_Fasit (Claude): lead=AI-vaksine; majors=Mette-Marit, Anthropic "
             "selvforbedring, havvind; mids=Trump AI, NASA MAVEN, VoidZero, flyktning-flytterett._\n")

    L.append("\n## B — bokmål summaries by role\n")
    for item in b:
        L.append(f"### {item['role'].upper()} · {item['title'][:60]} ({item['source']}, {item['secs']}s)\n")
        j = item["json"]
        if isinstance(j, dict):
            if j.get("kicker"):
                L.append(f"**Kicker:** {j['kicker']}  ")
            if j.get("deck"):
                L.append(f"**Deck:** {j['deck']}\n")
            for p in j.get("paragraphs", []):
                L.append(f"{p}\n")
            if j.get("photo_caption"):
                L.append(f"_Bildetekst: {j['photo_caption']}_\n")
            if item["role"] == "brief":
                L.append(f"**{j.get('bold','')}** — {j.get('text','')}\n")
        else:
            L.append(f"```\n{item['raw'][:800]}\n```\n")

    secs = [x["secs"] for x in b]
    L.append(f"\n_Summary throughput: {sum(secs):.1f}s for {len(b)} articles "
             f"→ ~{sum(secs)/len(b):.1f}s each; a 14-article edition ≈ "
             f"{14*sum(secs)/len(b)/60:.1f} min sequential._\n")

    OUT.joinpath(f"report_{tag}.md").write_text("\n".join(L))


if __name__ == "__main__":
    main()

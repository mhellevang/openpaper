# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "pyyaml"]
# ///
"""
End-to-end standalone OpenPaper prototype — no Claude, no cloud.

  hybrid curation (curate_sketch)  →  E4B summaries (bokmål)  →  edition.yaml  →  render.py

Run:
  uv run spike/standalone.py
Opens nothing; prints the path to the rendered HTML.

Weather/markets are static placeholders here (in production they come from the
existing weather.py / markets.py fetchers). Everything else is real: the model
does per-article semantic matching (curate_sketch) and per-article summarisation;
all editorial arithmetic and role-length enforcement is plain Python.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

import httpx
import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import curate_sketch as cs  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_YAML = pathlib.Path(__file__).resolve().parent / "out" / "edition_local.yaml"
RENDER = ROOT / "skills" / "openpaper" / "scripts" / "render.py"
TEMPLATES = ROOT / ".openpaper" / "templates"
MODEL = "gemma4:e4b"

# role → (max paragraphs enforced in CODE, prompt spec). The max-paragraph cap is
# the fix for the calibration bug the spike found (E4B wrote 4 paragraphs for md).
# Each role also returns a bokmål "title" (used for English sources). brief keeps bold+text.
ROLE = {
    "lead": (4, "3-4 avsnitt, narrativ bue. JSON {\"title\",\"kicker\",\"deck\",\"paragraphs\":[..],\"photo_caption\"}."),
    "lg": (2, "Nøyaktig 2 avsnitt. JSON {\"title\",\"kicker\",\"deck\",\"paragraphs\":[..]}."),
    "md": (1, "Ett stramt avsnitt. JSON {\"title\",\"kicker\",\"paragraphs\":[\"...\"]}."),
    "brief": (0, "Én setning, maks 15 ord. JSON {\"bold\":\"tema\",\"text\":\"setning.\"}."),
}
BOKMAL = ("Skriv på naturlig norsk BOKMÅL — IKKE svensk eller dansk (bruk «og/å/sjø», "
          "aldri «och/att/ö/ä»). Oversett engelske kilder, behold egennavn. Hold "
          "«kicker» kort (maks 5 ord). «miles» → kilometer (ikke «mil»). Fornorsk "
          "faste uttrykk. Svar KUN med gyldig JSON.")
NORWEGIAN_SOURCES = {"nrk", "aftenposten"}


def _looks_swedish(j: dict) -> bool:
    text = " ".join(str(v) for v in j.values() if isinstance(v, str))
    text += " " + " ".join(p for p in j.get("paragraphs", []) if isinstance(p, str))
    low = text.lower()
    return any(c in text for c in "äö") or any(
        m in low for m in (" och ", " för ", " är ", "möte", "kriget", " att "))


def _call(art: cs.Article, system: str, temperature: float = 0.5) -> dict:
    prompt = f"TITTEL: {art.title}\nKILDE: {art.source}\n\nARTIKKEL:\n{art.content[:12000]}"
    r = httpx.post(cs.OLLAMA, json={
        "model": MODEL, "system": system, "prompt": prompt, "stream": False,
        "format": "json", "options": {"num_ctx": 32768, "temperature": temperature},
    }, timeout=300.0)
    try:
        return json.loads(r.json()["response"])
    except Exception:
        return {}


def summarise(art: cs.Article) -> dict:
    cap, spec = ROLE[art.role]
    system = f"Du skriver en avissak i rollen «{art.role}». {spec}\n{BOKMAL}"
    j = _call(art, system)
    needs_title = art.role != "brief" and art.source not in NORWEGIAN_SOURCES
    if _looks_swedish(j) or (needs_title and not (j.get("title") or "").strip()):
        note = ("\nVIKTIG: Skriv NORSK BOKMÅL (ikke svensk/dansk), vær tro mot kilden, "
                "og ta med ALLE JSON-felt – også \"title\" oversatt til norsk.")
        j = _call(art, system + note, temperature=0.2)  # lower temp = more faithful
    return j


def annotation(art: cs.Article) -> str:
    return f"fordi du følger {art.primary_topic}"


def headline(art: cs.Article, j: dict) -> str:
    """Keep native Norwegian titles; use the model's bokmål title for English sources."""
    if art.source in NORWEGIAN_SOURCES:
        return art.title
    return (j.get("title") or "").strip() or art.title


def short_kicker(text: str, topic: str, max_words: int = 5) -> str:
    words = (text or topic).strip().rstrip(".:–-").split()
    s = " ".join(words[:max_words])
    return s[:1].upper() + s[1:] if s else topic


def build_story(art: cs.Article, j: dict, section: str) -> dict:
    cap, _ = ROLE[art.role]
    paras = [p for p in j.get("paragraphs", []) if p][:cap]   # ← code enforces length
    story = {
        "kicker": short_kicker(j.get("kicker"), art.primary_topic),
        "title": headline(art, j),
        "size": "lg" if art.role == "lg" else "md",
        "section": section,
        "url": art.url,
        "paragraphs": paras,
        "annotation": annotation(art),
    }
    if j.get("deck"):
        story["deck"] = j["deck"]
    if art.role == "lg" and art.match:                 # lg gets an image if available
        img = getattr(art, "image_url", None)
        if img:
            story["image_url"], story["has_thumb"] = img, True
    return story


def main() -> None:
    print(">> Curating (model does per-article matching; code does the rest)…")
    plan = cs.curate()
    for a in plan:                                     # carry image_url onto Article
        d = json.loads((cs.CORPUS / a.file).read_text())
        a.image_url = d.get("image_url")

    lead_art = plan[0]
    print(f">> Summarising {len(plan)} articles with {MODEL} (bokmål)…")
    summaries = {a.file: summarise(a) for a in plan}

    lj = summaries[lead_art.file]
    lead = {
        "kicker": "Hovedsak · " + short_kicker(lj.get("kicker"), lead_art.primary_topic),
        "title": headline(lead_art, lj),
        "deck": lj.get("deck", ""),
        "byline": "Av OpenPaper-redaksjonen · Skrevet 06:30 i Oslo",
        "url": lead_art.url,
        "image_url": lead_art.image_url,
        "paragraphs": [p for p in lj.get("paragraphs", []) if p][:4],
        "annotation": annotation(lead_art),
        "photo_caption": lj.get("photo_caption", ""),
    }

    cols = ["col2", "col3", "col4", "col1", "col5", "col2", "col3", "col4"]
    stories, briefs, ci, seen = [], [], 0, set()
    for a in plan[1:]:
        j = summaries[a.file]
        if a.role == "brief":
            text = j.get("text", "")
            key = " ".join(text.lower().split()[:4])     # drop near-duplicate briefs
            if not text or key in seen:
                continue
            seen.add(key)
            briefs.append({"bold": j.get("bold") or a.primary_topic.capitalize(),
                           "text": text, "url": a.url})
        else:
            stories.append(build_story(a, j, cols[ci % len(cols)])); ci += 1

    edition = {
        "template": "broadsheet", "edition_name": "morning",
        "date": "Fredag 5. juni 2026",
        "date_formal": "Fredag den femte juni MMXXVI",
        "volume": "auto", "number": "auto",
        "location": "Oslo, Norge", "reading_time": "20 min",
        "article_count": 1 + len(stories) + len(briefs),
        "tagline": "Alle nyhetene som passer dagen du har foran deg.",
        "printed_time": "06:30 CET",
        # placeholder weather/markets — production: weather.py / markets.py fetchers
        "weather": {"icon": "rain", "temp": 15, "description": "Lett regn, gir seg snart",
                    "high": 17, "low": 14, "wind": "S 20 km/t",
                    "forecast": [{"day": "LØR", "temp": 19}, {"day": "SØN", "temp": 20},
                                 {"day": "MAN", "temp": 20}, {"day": "TIR", "temp": 17}]},
        "markets": [{"name": "Oslo Børs", "value": "1,017", "change": "+1.0%", "direction": "up"},
                    {"name": "USD/NOK", "value": "9.32", "change": "−0.1%", "direction": "down"},
                    {"name": "S&P 500", "value": "7,584", "change": "+0.4%", "direction": "up"},
                    {"name": "Bitcoin", "value": "62,842", "change": "−1.5%", "direction": "down"}],
        "lead": lead, "stories": stories, "briefs": briefs,
        "sections_index": [{"name": "Norge", "page": "A1"}, {"name": "Vitenskap & KI", "page": "A3"},
                           {"name": "Verden", "page": "B1"}],
        "word_of_day": {"word": "Eolisk", "definition": "formet eller ført av vinden"},
    }

    OUT_YAML.parent.mkdir(exist_ok=True)
    OUT_YAML.write_text(yaml.safe_dump(edition, allow_unicode=True, sort_keys=False))
    print(f">> Wrote {OUT_YAML.relative_to(ROOT)}")

    out_html = OUT_YAML.parent / "edition_local.html"
    print(">> Rendering with render.py + localised template…")
    subprocess.run(["uv", "run", str(RENDER), "--data-dir", str(ROOT / ".openpaper"),
                    "--edition", str(OUT_YAML), "--templates-dir", str(TEMPLATES),
                    "--output", str(out_html)], check=True, cwd=ROOT)
    print(f"\n✓ Local newspaper: {out_html}")


if __name__ == "__main__":
    main()

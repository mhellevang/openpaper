# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx"]
# ///
"""
Sketch: hybrid curation for a standalone OpenPaper.

The point of this file is to show how SMALL the model's job is. Everything that
curation-guide.md describes as an "algorithm" — weights, bonuses, recency, the
30%/40%/20% rules, role assignment — is just deterministic Python. The ONLY thing
that genuinely needs a language model is one narrow question per article:
"how strongly does this text relate to each of the reader's interests?"
That single function (semantic_match) is boxed off below. Swap it for embeddings
and you remove the generative model from selection entirely.

Run against the real corpus:
  uv run spike/curate_sketch.py
"""
from __future__ import annotations

import datetime as dt
import json
import math
import pathlib
from dataclasses import dataclass, field

import httpx

ROOT = pathlib.Path(__file__).resolve().parent.parent
CORPUS = ROOT / ".openpaper" / "saved" / "2026-06-05-morning"
TODAY = dt.date(2026, 6, 5)  # passed in for real; hardcoded for the sketch
OLLAMA = "http://localhost:11434/api/generate"


# ────────────────────────────────────────────────────────────────────────
# CONFIG — this is preferences.md, parsed once into structured data.
# (Parsing the freeform markdown into this shape is the *other*, one-time,
#  model seam — or you just hand-write this block. Either way it is not part
#  of the per-edition hot path.)
# ────────────────────────────────────────────────────────────────────────
INTERESTS: dict[str, float] = {        # natural language → weight (guide §1)
    "teknologi og KI": 0.9,            # "very interested"
    "Norge og Oslo": 0.9,              # "very interested"
    "vitenskap og klima": 0.7,         # "interested"
    "verden og politikk": 0.5,         # "some interest"
}
SOURCE_PRIORITY = ["hackernews", "arstechnica", "bbc", "bbc_business",
                   "theguardian", "nrk", "aftenposten"]
SOURCE_BONUS = [0.15, 0.10, 0.05, 0.02]        # positions 1-4; 4+ → 0.02
FEEDBACK: list[dict] = []                       # empty for now
MAX_ARTICLES = 14
READING_MINUTES = 20


@dataclass
class Article:
    title: str
    source: str
    date: dt.date | None
    summary: str
    content: str
    url: str
    file: str
    match: dict[str, float] = field(default_factory=dict)   # filled by model
    score: float = 0.0
    primary_topic: str = ""
    role: str = ""


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  THE ONLY MODEL-DEPENDENT STEP IN SELECTION.                          ║
# ║  Narrow, bounded, per-article. Returns one number per interest.      ║
# ║  Replace the body with an embeddings dot-product and the generative  ║
# ║  model disappears from curation entirely.                            ║
# ╚══════════════════════════════════════════════════════════════════════╝
def semantic_match(art: Article, model: str = "gemma4:e4b") -> dict[str, float]:
    interests = list(INTERESTS)
    system = (
        "Vurder hvor sterkt artikkelen handler om hvert av disse temaene, "
        "fra 0.0 (ikke i det hele tatt) til 1.0 (helt sentralt). Returner KUN "
        'JSON: {"' + '": <0-1>, "'.join(interests) + '": <0-1>}.'
    )
    prompt = f"TITTEL: {art.title}\nSAMMENDRAG: {art.summary}\nUTDRAG: {art.content[:600]}"
    r = httpx.post(OLLAMA, json={
        "model": model, "system": system, "prompt": prompt, "stream": False,
        "format": "json", "options": {"num_ctx": 8192, "temperature": 0.0},
    }, timeout=120.0)
    r.raise_for_status()
    try:
        raw = json.loads(r.json()["response"])
    except Exception:
        raw = {}
    # clamp + default missing interests to 0
    return {k: max(0.0, min(1.0, float(raw.get(k, 0.0) or 0.0))) for k in interests}


# ────────────────────────── pure deterministic code below ──────────────────
def source_bonus(source: str) -> float:
    if source in SOURCE_PRIORITY:
        i = SOURCE_PRIORITY.index(source)
        return SOURCE_BONUS[i] if i < len(SOURCE_BONUS) else 0.02
    return 0.0                                   # unlisted: no bonus, no penalty


def recency_bonus(date: dt.date | None) -> float:
    if date is None:
        return 0.0
    days = (TODAY - date).days
    return 0.1 if days <= 0 else 0.05 if days == 1 else 0.0


def feedback_multiplier(art: Article) -> float:
    """Apply love/more/less/hide with 30/90-day decay (guide §1.4, §1.6)."""
    mult = 1.0
    for fb in FEEDBACK:
        if fb["topic"] not in art.match or art.match[fb["topic"]] < 0.3:
            continue
        age = (TODAY - fb["date"]).days
        decay = 1.0 if age <= 30 else 0.5 if age <= 90 else 0.25
        signal = {"love": 1.5, "more": 1.2, "less": 0.5, "hide": -999}[fb["signal"]]
        mult *= signal if signal > 0 else signal
    return mult


def score(art: Article) -> float:
    base = sum(art.match[i] * w for i, w in INTERESTS.items())   # weighted sum
    s = (base + source_bonus(art.source) + recency_bonus(art.date))
    s *= feedback_multiplier(art)
    art.primary_topic = max(art.match, key=art.match.get)        # top interest
    return -1.0 if s < -100 else round(s, 3)                     # hide → exclude


def diversify(arts: list[Article]) -> list[Article]:
    """Topic cap: no topic > 30% of MAX_ARTICLES (guide §2)."""
    cap = math.ceil(0.3 * MAX_ARTICLES)
    kept, per_topic = [], {}
    for a in sorted(arts, key=lambda x: x.score, reverse=True):
        n = per_topic.get(a.primary_topic, 0)
        if n < cap:
            kept.append(a); per_topic[a.primary_topic] = n + 1
    return kept


def balance_sources(arts: list[Article]) -> list[Article]:
    """≤40% from one source; reserve ≥20% for non-priority sources (guide §3)."""
    src_cap = math.floor(0.4 * MAX_ARTICLES)
    serendipity_min = math.ceil(0.2 * MAX_ARTICLES)
    chosen, per_src = [], {}
    pool = sorted(arts, key=lambda x: x.score, reverse=True)
    for a in pool:
        if len(chosen) >= MAX_ARTICLES:
            break
        if per_src.get(a.source, 0) < src_cap:
            chosen.append(a); per_src[a.source] = per_src.get(a.source, 0) + 1
    # ensure serendipity quota from sources outside SOURCE_PRIORITY[:3]
    outsiders = [a for a in chosen if a.source not in SOURCE_PRIORITY[:3]]
    if len(outsiders) < serendipity_min:
        extra = [a for a in pool if a not in chosen
                 and a.source not in SOURCE_PRIORITY[:3]]
        chosen += extra[: serendipity_min - len(outsiders)]
    return chosen[:MAX_ARTICLES]


def assign_roles(arts: list[Article]) -> list[Article]:
    """1 lead, 2-3 lg, 3-5 md, rest briefs; tilt by reading time (guide §4)."""
    n_lg, n_md = (2, 3) if READING_MINUTES < 15 else (3, 4)
    ranked = sorted(arts, key=lambda x: x.score, reverse=True)
    for i, a in enumerate(ranked):
        a.role = ("lead" if i == 0 else "lg" if i <= n_lg
                  else "md" if i <= n_lg + n_md else "brief")
    return ranked


def load_corpus() -> list[Article]:
    out = []
    for p in sorted(CORPUS.glob("*.json")):
        d = json.loads(p.read_text())
        try:
            date = dt.datetime.fromisoformat(d["date"]).date() if d.get("date") else None
        except Exception:
            date = None
        out.append(Article(d["title"], d["source"], date, d.get("summary", ""),
                           d.get("content") or "", d["url"], p.name))
    return out


def curate() -> list[Article]:
    arts = load_corpus()
    for a in arts:                       # ── model: one narrow call per article
        a.match = semantic_match(a)
        a.score = score(a)               # ── code from here down
    selected = balance_sources(diversify(arts))
    return assign_roles(selected)


if __name__ == "__main__":
    plan = curate()
    print(f"{'ROLLE':6} {'SCORE':>6}  {'EMNE':22} {'KILDE':7} TITTEL")
    print("─" * 100)
    for a in plan:
        print(f"{a.role:6} {a.score:6.2f}  {a.primary_topic[:22]:22} "
              f"{a.source:7} {a.title[:42]}")
    lead = plan[0]
    print(f"\nLEAD → {lead.title}\n  (matches: " +
          ", ".join(f"{k} {v:.1f}" for k, v in lead.match.items() if v >= 0.3) + ")")

# Spike-funn: Gemma 4 E2B/E4B lokalt for OpenPaper

**Dato:** 2026-06-05 · **Maskinvare:** lokal Mac via Ollama 0.20.6, `num_ctx=32768`
**Materiale:** 14 ekte artikler fra `.openpaper/saved/2026-06-05-morning/` (norske +
engelske kilder), målt mot utgaven Claude faktisk lagde (`editions/draft.yaml`).
Rådata i `spike/out/results_*.json`, fulle utdrag i `report_gemma4_e4b.md` /
`report_gemma4_e2b.md`.

## Kortversjon
- **E4B er brukbar; E2B er det ikke.** E2B oversatte lange artikler *ordrett* i
  stedet for å oppsummere, og produserte tekstkorrupsjon («kanviruss», «rompet,
  menesker»). E4B oppsummerer faktisk, på flytende, naturlig bokmål.
- **Faktatroskap er overraskende god** på E4B — ingen oppdiktede fakta funnet.
  (To tall jeg først mistenkte som hallusinasjon — «8× kode per kvartal» og «200
  millioner mil» — sto begge ordrett i kildene.) Dette var det største a-priori-
  risikomomentet, og det holdt ikke stikk.
- **Den virkelige svakheten er redaktørskjønn**, ikke språk eller fakta.

## Funn i detalj

### 1. Bokmål-kvalitet
- **E4B:** flytende, idiomatisk journalistisk bokmål. Lesbart rett inn i avisen.
- **E2B:** korrupsjonsartefakter og halvferdige setninger → under terskel.
- **Felles feil (begge):** engelsk «miles» oversatt til norsk «mil» (1 mil = 10 km)
  — klassisk falsk venn, faktisk enhetsfeil. E4B lot også «(game changer)» stå i
  parentes, tross eksplisitt instruks om å fornorske slike uttrykk.

### 2. Rolle-kalibrering (lengdestyring)
| Rolle | E4B | E2B |
|---|---|---|
| lead (3–4 avsnitt) | ✅ 4 avsnitt | ❌ oversatte hele artikkelen |
| lg (2 avsnitt) | ✅ 2 avsnitt | ✅ 2 (men «deck: hackernews») |
| md (1 avsnitt) | ❌ 4 avsnitt | ❌ oversatte hele artikkelen |
| brief (1 setning) | ✅ | ✅ |

Avgrensede oppgaver (brief) er rocksolide; lengre roller glipper. Dette er
**styrbart i kode** (max_tokens per rolle, few-shot-eksempler, hard avkorting),
ikke et fundamentalt modellproblem.

### 3. Redaktørskjønn — den egentlige flaskehalsen
Per-artikkel-scoring (A1) er **konsistent** (E4B snitt |Δ|=0.043 mellom to
kjøringer), men *skjev*:
- Over-belønner overflate-tech: VoidZero (nisje JS-verktøy) ble toppscoret (0.9),
  mens Claude la den som en mid.
- Under-belønner menneske-interesse og store norske saker: **kronprinsesse
  Mette-Marit på venteliste for lungetransplantasjon** fikk 0.5–0.6 på E4B og
  **0.1** på E2B — tross «Norge/Oslo (svært interessert)». Begge modeller ville i
  praksis begravd eller droppet en av dagens viktigste norske nyheter.
- Ingen av modellene valgte AI-vaksinen (Claudes lead) som lead.

Whole-pool-utvelgelse (A2, utnytter 128K): mekanisk fungerer det, men begge
modeller laget **feil kobling mellom JSON-indekser og sin egen begrunnelse**
(reliabilitetsbugg), valgte svak lead, og leverte litt for få saker.

### 4. Gjennomstrømning (E4B)
~12 s per sammendrag → en 14-saks utgave ≈ **3 min sekvensielt**. Scoring ~2–3 s
per artikkel. Fullt akseptabelt for en daglig avis. («Parallelt» gir lite lokalt
— maskinen er compute-bundet; design for sekvensiell/batchet kjøring.)

## Anbefaling
1. **Bruk E4B, ikke E2B.** E2B er under kvalitetsterskel for prosa.
2. **«Alt lokalt» er realistisk for språk-/oppsummeringshalvdelen** med E4B —
   forutsatt at rolle-lengde håndheves i kode, og to prompt-fikser (enhets-
   oversettelse «miles»→km, og fornorsknings-regelen for faste uttrykk).
3. **Ikke overlat redaktørskjønnet til modellen.** Empirien bekrefter at en liten
   modell scorer mot leserens faktiske interesser på en skjev måte. Best
   arkitektur er **hybrid**: behold den dokumenterte deterministiske scoringen
   (vekter/bonus/recency fra `curation-guide.md`) i Python, bruk evt. E4B kun til
   per-artikkel emne-tagging, og la kode håndheve diversitet, kildebalanse og
   norsk-signifikans. Dvs. *lokal modell for prosa, kode for skjønn* — ikke lokal
   modell for alt.

## Oppfølging hvis vi bygger videre
- Few-shot + max_tokens per rolle; valider md-lengde i kode.
- Fiks enhets-/idiomregler i system-prompten; legg til en etterkontroll som
  fanger «mil» og gjenværende engelske uttrykk.
- For A2: be om artikkel-URL/slug i stedet for indeks for å unngå indeksforvirring.
- (Valgfritt) test `gemma4:26b` / `gemma4-claude` som allerede ligger lokalt, for å
  se hvor mye redaktørskjønnet bedres med en større lokal modell.

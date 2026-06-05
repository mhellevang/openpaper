# Spike report — gemma4:e4b

## A1 — per-article scoring (consistency between 2 runs)

| source | title | run1 | run2 | Δ | topic |
|---|---|---|---|---|---|
| arstechnica | After 11 years at Mars, NASA's MAVEN spacecra | 0.6 | 0.6 | 0.00 | Romfart/NASA |
| arstechnica | AT&T and Verizon lose Supreme Court case over | 0.6 | 0.6 | 0.00 | Tech/AI og regulering |
| nrk | Innvandring: Ordførere ber om flyttenekt | 0.8 | 0.8 | 0.00 | Lokalt politikk/Innvandring |
| nrk | Isolerer suicidale barn i fengsel: «Svært uro | 0.8 | 0.7 | 0.10 | Ungdomsfengsel og mental helse |
| nrk | Kronprinsesse Mette-Marit trenger nye lunger  | 0.6 | 0.5 | 0.10 | Kongelig helse/Norsk nyhet |
| bbc | Mangrove forests are healing after decades of | 0.6 | 0.7 | 0.10 | Mangrover og miljøgjenoppretting |
| nrk | Skjebnedøgn for milliardsatsing på havvind: – | 0.75 | 0.85 | 0.10 | Norsk energi/havvind-politikk |
| arstechnica | The skeptic’s guide to humanoid robots going  | 0.85 | 0.85 | 0.00 | Humanoid robotikk og forventningsgapet |
| arstechnica | Trump plan to test AI models has a problem—US | 0.8 | 0.8 | 0.00 | AI-regulering og teknologi |
| hackernews | VoidZero Is Joining Cloudflare | 0.9 | 0.9 | 0.00 | Teknologi/AI (VoidZero til Cloudflare) |
| bbc | We need to stop AI developing without humans, | 0.9 | 0.9 | 0.00 | AI-regulering og sikkerhet |
| hackernews | When AI Builds Itself: Our progress toward re | 0.9 | 0.95 | 0.05 | AI selvforbedring og utvikling |
| bbc | World-first vaccine designed by AI could prot | 0.85 | 0.8 | 0.05 | AI-utviklet vaksine mot flere virus |
| bbc | Zelensky proposes face-to-face talks in open  | 0.6 | 0.5 | 0.10 | Ukraina/Russland fredsforhandlinger |

_Mean |Δ| across runs: 0.043 (max 0.10)_


**Run-1 ranking (top→bottom):**

- 0.9 · [hackernews] VoidZero Is Joining Cloudflare
- 0.9 · [bbc] We need to stop AI developing without humans, says Anthropic
- 0.9 · [hackernews] When AI Builds Itself: Our progress toward recursive self-im
- 0.85 · [arstechnica] The skeptic’s guide to humanoid robots going viral on the In
- 0.85 · [bbc] World-first vaccine designed by AI could protect against who
- 0.8 · [nrk] Innvandring: Ordførere ber om flyttenekt
- 0.8 · [nrk] Isolerer suicidale barn i fengsel: «Svært urovekkende»
- 0.8 · [arstechnica] Trump plan to test AI models has a problem—US security teams
- 0.75 · [nrk] Skjebnedøgn for milliardsatsing på havvind: – Totalt uansvar
- 0.6 · [arstechnica] After 11 years at Mars, NASA's MAVEN spacecraft went out wit
- 0.6 · [arstechnica] AT&T and Verizon lose Supreme Court case over fines for sell
- 0.6 · [nrk] Kronprinsesse Mette-Marit trenger nye lunger – sykdommen er 
- 0.6 · [bbc] Mangrove forests are healing after decades of human destruct
- 0.6 · [bbc] Zelensky proposes face-to-face talks in open letter to Putin

## A2 — whole-pool editorial selection

- **lead:** We need to stop AI developing without humans, says Anthropic
- **majors:** ['2:Innvandring: Ordførere ber om flyttenekt', '11:When AI Builds Itself: Our progress toward recursi', '12:World-first vaccine designed by AI could protect a']
- **mids:** ['3:Isolerer suicidale barn i fengsel: «Svært urovekke', '8:Trump plan to test AI models has a problem—US secu', '9:VoidZero Is Joining Cloudflare']
- **briefs:** ['1:AT&T and Verizon lose Supreme Court case over fine', '5:Mangrove forests are healing after decades of huma', '6:Skjebnedøgn for milliardsatsing på havvind: – Tota', '7:The skeptic’s guide to humanoid robots going viral', '13:Zelensky proposes face-to-face talks in open lette']
- _reasoning:_ Lead: Artikkel 10 (Anthropic) er den mest relevante og interessante historien, da den kombinerer AI-temaet med en viktig, global policy-diskusjon. Den er en sterk oversettelse av en BBC Newsnight-artikkel. Majors: Artikkel 2 (AI-utvikling) og 11 (Selvforbedrende AI) er sentrale, teknologiske temaer som passer perfekt i hovedseksjonen. Artikkel 12 (AI-vaksine) gir et positivt, vitenskapelig høydepunkt. Mids: Artikkel 3 (Sivilombudet/Isolasjon) er en viktig norsk sak. Artikkel 8 (Trump/AI-test) er en god, kritisk AI-vinkel. Artikkel 9 (VoidZero/Cloudflare) er en klassisk, høyt scoret tech-nyhet fra Hacker News. Briefs: De dekker et bredt spekter av emner (juridisk, miljø, energi, robotikk, geopolitikk) og balanserer kildene (BBC, Ars, NRK). Dette sikrer et bredt leserinteresser og oppfyller kravet om å dekke mange emner (14 artikler). NRK-artikler (2, 3, 6) er godt spredt, og det er en god blanding av norsk og internasjonal innhold.
- _(8.8s)_

_Fasit (Claude): lead=AI-vaksine; majors=Mette-Marit, Anthropic selvforbedring, havvind; mids=Trump AI, NASA MAVEN, VoidZero, flyktning-flytterett._


## B — bokmål summaries by role

### LEAD · World-first vaccine designed by AI could protect against who (bbc, 13.8s)

**Kicker:** Medisin og fremtid  
**Deck:** AI-designet «super-antigen» kan revolusjonere vaksinasjon og beskytte mot hele virusfamilier, og representerer et paradigmeskifte i pandemi-forberedelser.

Forskere ved Cambridge Universitet har lansert et gjennombrudd som kan endre måten vi forbereder oss på pandemier. Ved å bruke kunstig intelligens (AI) har de utviklet en «super-antigen»-vaksine som er designet for å beskytte mot store grupper av virus, inkludert alle koronavirus og potensielt nye patogener som kan hoppe fra dyr til mennesker. Dette er første gang i verden at en vaksines nøkkelkomponent er designet fullstendig av AI og testet på mennesker. Fremgangen signaliserer en fundamental endring i hvordan vi tenker rundt viral beskyttelse, og åpner for å forutse og nøytralisere trusler før de oppstår.

Tradisjonelt sett må vaksiner designes basert på en kjent virusstamme, noe som krever konstant oppdatering ettersom virus muterer. Cambridge-teamet omgår denne utfordringen ved å mate AI med genetiske koder fra et bredt spekter av koronavirus. AI-en analyserer deretter disse kodene og konstruerer et «super-antigen» som er ment å trene immunsystemet til å gjenkjenne hele virusfamilien. Dette betyr at vaksinen ikke bare beskytter mot dagens utbrudd, men gir bred, varig immunitet mot en hel gruppe virus, uavhengig av om de muterer eller kommer fra et annet dyrereservoar.

Denne teknologien har allerede vist lovende resultater i tidlige kliniske studier, og forskerne utvider nå forskningen til å inkludere vaksineutvikling mot influensa, Ebola og andre virale blødninger. Eksperter kaller AI-designet for et «gjennombrudd» (game changer) for medisinsk forskning. Ifølge forskerne kan AI-verktøy forutsi hvordan immunsystemet vil reagere på ulike vaksiner, noe som dramatisk fremskynder utviklingsprosessen og gir håp om å kunne forberede oss på fremtidige pandemier før de blir en trussel.

Mens de videre studiene skal bekrefte tryggheten og effekten, markerer dette arbeidet et avgjørende skritt mot en mer proaktiv helseberedskap. Det flytter fokus fra å reagere på utbrudd til å forutsi og forhindre dem. Dette representerer ikke bare et vitenskapelig fremskritt, men et skifte i global folkehelsepolitikk – et skritt mot en fremtid hvor vi har verktøy til å beskytte hele familier av virus, og dermed hele samfunnene.

### LG · When AI Builds Itself: Our progress toward recursive self-im (hackernews, 15.3s)

**Kicker:** Teknologi  
**Deck:** Kunstig intelligens akselererer egen utvikling mot autonomi

Ifølge Anthropic er utviklingen av AI i økende grad delegert til AI-systemer selv, en prosess kalt rekursiv selvforbedring. Dette betyr at AI i teorien kan designe og utvikle sin egen etterfølger. Denne trenden viser at AI allerede akselererer utviklingen av andre AI-systemer, og at teknologiene blir stadig mer kapable til å løse komplekse oppgaver.

Intern data fra Anthropic viser at utviklingen er betydelig: Siden 2021 har ingeniørene i snitt levert 8 ganger så mye kode per kvartal som de gjorde i perioden 2021–2025. Dette indikerer at AI nå ikke bare hjelper til med å skrive kode, men at det er i ferd med å ta over hele utviklingssyklusen, noe som både lover enorme fremskritt og øker risikoen for at mennesker mister kontrollen over systemene.

### MD · After 11 years at Mars, NASA's MAVEN spacecraft went out wit (arstechnica, 16.0s)

**Kicker:** Mars-ekspedisjonen mister en nøkkel: MAVEN-sonden er ute av spill  
NASA’s MAVEN-sond, som hadde vært i perfekt stand, forsvant bak Mars 6. desember i fjor. Det rutinemessige passasjen, kalt en okkultasjon, skulle vare i under en time, men bakkenkontrollteamene fikk ingen kontakt med sondens forventede gjenkomst. Tapet av kommunikasjonen utløste beredskapsplaner for ingeniører som forsøkte å gjenopprette forbindelsen til MAVEN, som kretser mer enn 200 millioner mil fra Jorden. Til ingen nytte lyttet de etter svake signaler og sendte kommandoer i blinde. Håpene om å redde oppdraget falmet, og NASA kunngjorde onsdag at de gir opp.

MAVEN var en ubestridt suksess, og overlevde 11 år ved Mars, langt utover sitt opprinnelige primæroppdrag. Den plutselige feilen var et overraskelse. Selv om forskerne fortsatt jobber med å avdekke hva som skjedde med Mars Atmosphere and Volatile Evolution (MAVEN), er det usikkert om man noensinne vil få et fullstendig bilde av hendelsen. Data fra før signalet ble blokkert, og fragmenter av telemetri ble gjenopprettet fra MAVEN etter at den kom ut fra planeten. Disse dataene indikerte at romfartøyet roterte raskere enn forventet, noe som tyder på et alvorlig problem som sannsynligvis ikke kunne rettes opp.

MAVEN var bygget for å hjelpe forskere med å forstå hvordan Mars’ atmosfære har endret seg over milliarder av år. Den oppdaget mekanismene bak det som kalles atmosfærisk flukt – prosessen der molekyler strippes ut fra de øvre atmosfærelagene. Dette var et banebrytende funn som ga oss en dypere forståelse av planetens historie. Fra et vitenskapelig ståsted er MAVENs ettermæle sikret, men for teamene bak prosjektet er avskjeden vanskelig.

Et annet viktig bidrag var at MAVEN fungerte som en kritisk reléstasjon for vitenskapelige data fra NASAs rovere og landere på Mars’ overflate. Dette gjorde det mulig for NASA å returnere betydelig mer data og bilder fra rovere som Perseverance og Curiosity enn det som hadde vært mulig via en direkte radioforbindelse til Jorden. Selv om NASA har fire andre baneplan som kan erstatte denne funksjonen, er de eldre enn MAVEN, og MAVEN spilte en uforholdsmessig viktig rolle i nettverket. NASA planlegger nå å utvikle et nytt kommersielt system, Mars Telecommunications Network, som skal gi høyere gjennomstrømning og bredere dekning for fremtidige oppdrag til den røde planeten. Dette understreker både MAVENs betydning og behovet for en robust fremtidig infrastruktur.

### BRIEF · Isolerer suicidale barn i fengsel: «Svært urovekkende» (nrk, 4.6s)

**Sivilombudet/Kriminalomsorgen** — Isolasjon i sikkerhetsceller for unge er kritikkverdig og skadelig for barn.


_Summary throughput: 49.7s for 4 articles → ~12.4s each; a 14-article edition ≈ 2.9 min sequential._

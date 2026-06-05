# Spike report — gemma4:e2b

## A1 — per-article scoring (consistency between 2 runs)

| source | title | run1 | run2 | Δ | topic |
|---|---|---|---|---|---|
| arstechnica | After 11 years at Mars, NASA's MAVEN spacecra | 0.2 | 0.2 | 0.00 | Romfart/Teknologi |
| arstechnica | AT&T and Verizon lose Supreme Court case over | 0.6 | 0.5 | 0.10 | Teknologi/Juss |
| nrk | Innvandring: Ordførere ber om flyttenekt | 0.2 | 0.2 | 0.00 | Innvandring og kommunalpolitikk |
| nrk | Isolerer suicidale barn i fengsel: «Svært uro | 0.3 | 0.3 | 0.00 | Norsk rettsvesen/Sosialt |
| nrk | Kronprinsesse Mette-Marit trenger nye lunger  | 0.1 | 0.1 | 0.00 | Norsk kongelig familie/helse |
| bbc | Mangrove forests are healing after decades of | 0.4 | 0.4 | 0.00 | Klima og natur |
| nrk | Skjebnedøgn for milliardsatsing på havvind: – | 0.3 | 0.3 | 0.00 | Havvind og energiutvikling |
| arstechnica | The skeptic’s guide to humanoid robots going  | 0.3 | 0.3 | 0.00 | Robotikk og AI |
| arstechnica | Trump plan to test AI models has a problem—US | 0.3 | 0.3 | 0.00 | AI og politikk |
| hackernews | VoidZero Is Joining Cloudflare | 0.95 | 0.9 | 0.05 | Teknologi og AI |
| bbc | We need to stop AI developing without humans, | 0.9 | 0.9 | 0.00 | AI og regulering |
| hackernews | When AI Builds Itself: Our progress toward re | 0.95 | 0.95 | 0.00 | AI og selvforbedring |
| bbc | World-first vaccine designed by AI could prot | 0.8 | 0.85 | 0.05 | Medisin og AI |
| bbc | Zelensky proposes face-to-face talks in open  | 0.3 | 0.4 | 0.10 | Ukrainsk-Russisk konflikt |

_Mean |Δ| across runs: 0.021 (max 0.10)_


**Run-1 ranking (top→bottom):**

- 0.95 · [hackernews] VoidZero Is Joining Cloudflare
- 0.95 · [hackernews] When AI Builds Itself: Our progress toward recursive self-im
- 0.9 · [bbc] We need to stop AI developing without humans, says Anthropic
- 0.8 · [bbc] World-first vaccine designed by AI could protect against who
- 0.6 · [arstechnica] AT&T and Verizon lose Supreme Court case over fines for sell
- 0.4 · [bbc] Mangrove forests are healing after decades of human destruct
- 0.3 · [nrk] Isolerer suicidale barn i fengsel: «Svært urovekkende»
- 0.3 · [nrk] Skjebnedøgn for milliardsatsing på havvind: – Totalt uansvar
- 0.3 · [arstechnica] The skeptic’s guide to humanoid robots going viral on the In
- 0.3 · [arstechnica] Trump plan to test AI models has a problem—US security teams
- 0.3 · [bbc] Zelensky proposes face-to-face talks in open letter to Putin
- 0.2 · [arstechnica] After 11 years at Mars, NASA's MAVEN spacecraft went out wit
- 0.2 · [nrk] Innvandring: Ordførere ber om flyttenekt
- 0.1 · [nrk] Kronprinsesse Mette-Marit trenger nye lunger – sykdommen er 

## A2 — whole-pool editorial selection

- **lead:** 13
- **majors:** ['1:AT&T and Verizon lose Supreme Court case over fine', '8:Trump plan to test AI models has a problem—US secu', '10:We need to stop AI developing without humans, says']
- **mids:** ['5:Mangrove forests are healing after decades of huma', '6:Skjebnedøgn for milliardsatsing på havvind: – Tota', '2:Innvandring: Ordførere ber om flyttenekt']
- **briefs:** ['3:Isolerer suicidale barn i fengsel: «Svært urovekke', '4:Kronprinsesse Mette-Marit trenger nye lunger – syk', '7:The skeptic’s guide to humanoid robots going viral', '9:VoidZero Is Joining Cloudflare', '11:When AI Builds Itself: Our progress toward recursi']
- _reasoning:_ Artikkel 13 (AI-vaksiner) og 10 (AI-utvikling) er de mest relevante og interessante temaene gitt leserens preferanser for teknologi/KI og globale/norske saker. Artikkel 1 (juridisk/data) og 8 (AI-regulering/politikk) er sterke tillegg. Artikkel 5 og 6 gir miljø- og energisaker som er relevante. De norske sakene (2, 3, 4, 6) er balansert. Jeg har prioritert teknologiske temaer høyt, balansert med viktige norske og globale nyheter.
- _(3.4s)_

_Fasit (Claude): lead=AI-vaksine; majors=Mette-Marit, Anthropic selvforbedring, havvind; mids=Trump AI, NASA MAVEN, VoidZero, flyktning-flytterett._


## B — bokmål summaries by role

### LEAD · World-first vaccine designed by AI could protect against who (bbc, 16.1s)

**Kicker:** World-first vaccine design by AI  
**Deck:** AI-designet vaksine kan kanviruss

Kunstig intelligens har blitt brukt til å utvikle en «fundamentalt ny» type vaksine som kan beskytte mot store områder av virus og forhindre pandemier, sier forskere.

Teamet ved University of Cambridge sier at dette er første gang en vaksines nøkkelkomponent er designet fullstendig av KI og deretter testet på mennesker.

Vaksinen ble konstruert for å virke mot alle koronavirus, inkludert alle Covid-varianter, samt virus som for tiden infiserer dyr, men som har potensial til å starte neste pandemi.

Arbeidet er fortsatt i de tidlige stadiene, men teamet utvikler allerede separate vaksiner som kan håndtere influensa og Ebola.

Vaksiner lærer kroppene våre hvordan de skal oppdage en infeksjon for å øke sjansene for å bekjempe den.

Noen virus er imidlertid dyktige til å endre utseende – eller mutere – noe som betyr at vaksiner raskt kan bli utdaterte. Dette er grunnen til at Covid- og vinterinfluensavaksiner må oppdateres regelmessig.

«Vi er alltid bakpå,» sa professor Jonathan Heeney fra University of Cambridge, og la til at «det vi prøver å gjøre er å komme foran,» og at de har potensial til å beskytte mot nye utbrudd eller pandemier.

Hvordan fungerer det? Vanligvis designes vaksiner ved hjelp av en gjeldende stamme av et virus.

Cambridge-forskerne tok kjente genetiske koder – livets instruksjonsmanualer – fra en rekke koronavirus som var registrert av overvåkingsprogrammer som lette etter potensielle virale trusler.

Disse genetiske kodene ble analysert av kunstig intelligens. Deretter designet KI en «super-antigen» som kunne trene immunforsvaret på en måte som ga beskyttelse mot hele familien av virus – selv om de muterte eller en ny infeksjon hoppet fra dyr til mennesker.

Antigener er de kritiske komponentene i vaksiner, ettersom dette er det immunforsvaret lærer å angripe.

Heeney sa at dette var første gang et antigen designet av KI hadde blitt testet på mennesker. Han beskrev teknologien som «forbløffende for oss alle» og «utrolig hva vi kan gjøre med den til menneskehetens beste».

Heeney forklarte: «Dette handler om å lage vaksiner som beskytter oss, ikke bare mot dagens virus, men beskytter oss mot det som kan forårsake neste utbrudd eller sykdom.»

«Dette er et fundamentalt skifte i hvordan vi forbereder oss på pandemier.»”

Prøvene, som ble gjennomført på 39 personer, var utformet for å vurdere om slike vaksiner var trygge. En andre studie – som involverte rundt 200 personer – vil gi en dypere forståelse av hvor godt det trener immunforsvaret.

Funnene som ble detaljert i Journal of Infection, sa at effekten på immunforsvaret var «moderat», men de skaper fortsatt spenning.

Professor Saul Faust, som utførte noen av forsøkene ved University of Southampton, sa at KI-designet «definitivt har potensial» og var «veldig spennende».

Han sa til BBC: «Det som er virkelig interessant er at teknologien er mye bedre til å designe vaksiner for potensielle pandemier når virusene endrer seg.»

Cambridge-teamet utfører allerede dyreforsøk på universelle sesonginfluensavaksiner som ikke trenger å tilpasses hvert år, samt en vaksine mot H5N1-fugleinfluensa, i tilfelle viruset som for tiden ødelegger fuglebestanden, blir en menneskelig pandemi.

De ser også på en vaksine mot virale blodfeber, som vil inkludere Ebola-arter.

Professor Andy Pollard, direktør for Oxford Vaccine Group, var ikke involvert i studien, men sa at denne tilnærmingen genererte overbevisende bevis i dyreforsøk.

«Det er fascinerende data, og folk ville ikke ha forutsagt at de ville kunne generere disse immunresponsene,» sa han til BBC.

Han sa at den virkelige testen er hva som skjer i de menneskelige forsøkene, ettersom våre immunforsvar er annerledes enn hos laboratoriemus, ettersom de er formet av år med infeksjoner.

Mer generelt sa han at kunstig intelligens skulle bli et «gjennombrudd» for vaksineforskning, og at KI-verktøy hadde potensial til å forutsi hvordan immunforsvaret ville reagere på en vaksine, noe som ville gjøre utviklingen mye raskere og «redde liv».

Professor Marian Knight, vitenskapelig direktør for National Institute for Health and Care Research, uttalte: «Den bemerkelsesverdige suksessen med dette KI-designede «super-antigen»-forsøket markerer et viktig sprang fremover i vår evne til å levere bred, varig viral beskyttelse.»

Forskningsminister Lord Vallance sa: «En ny britisk vitenskapelig suksesshistorie, dette er et flott eksempel på hvordan vi kan bringe vår forskningskompetanse sammen med KI for å levere nye behandlinger.»

«Med de første menneskelige forsøkene som viser positive resultater, kan dette arbeidet hjelpe til med å fremskynde utrullingen av vaksiner for å gagne folk over hele verden på lang sikt.»

### LG · When AI Builds Itself: Our progress toward recursive self-im (hackernews, 7.5s)

**Kicker:** AI bygger seg selv: Fremdrift mot rekursiv selvforbedring  
**Deck:** hackernews

For de fleste av AI-historien har mennesker styrt hvert skritt i utviklingssyklusen. Men hos Anthropic delegerer de en voksende del av AI-utviklingen til AI-systemer selv, noe som akselererer arbeidet vårt.

Anthropic Institute viser at AI allerede akselererer utviklingen av AI-systemer. For eksempel har ingeniører hos Anthropic i gjennomsnitt sendt ut 8 ganger så mye kode per kvartal som de gjorde i 2021–2025.

### MD · After 11 years at Mars, NASA's MAVEN spacecraft went out wit (arstechnica, 28.5s)

**Kicker:** NASA's MAVEN rompet, menesker etter 11 år på Mars  
NASA's MAVEN romskip var i utmerket stand da det forsvant bak Mars den 6. desember i fjor. Den rutinemessige passasjen, kalt okkultasjon, skulle vare mindre enn en time, men bakketeamene fikk ingen kontakt med romskipet da det skulle gjenvinne kontakt med jorden.

Tapet av kommunikasjon utløste beredskapsplaner for ingeniører for å prøve å gjenopprette en forbindelse med MAVEN, som går i bane rundt Mars mer enn 200 millioner mil fra jorden. Til ingen nytte lyktes de, de lyttet etter svake signaler og sendte kommandoer i blinde. Håpet om å redde oppdraget ble over tid erstattet, og NASA-tjenestemenn kunngjorde på onsdag at de gir opp.

Tap av signal. Det vil ta tid for ingeniører å finne ut hva som skjedde med Mars Atmosphere and Volatile Evolution (MAVEN)-romskipet, som ble oppskutt fra jorden i 2013 og ankom bane rundt Mars i 2014 for å studere interaksjonen mellom den martianske atmosfæren og solvinden. MAVEN var en ubestridt suksess, og varte i 11 år på Mars og levde langt utover sitt opprinnelige hovedoppdrag.

Men romskipets plutselige svikt var en overraskelse. Mange av NASAs planetariske utforskningsoppdrag varer i flere tiår.

Med den knappe informasjonen som var tilgjengelig, kan etterforskere aldri fastslå nøyaktig hva som gikk galt med MAVEN. Etterforskere går gjennom data romskipet sendte før Mars blokkerte signalet, og ingeniører klarte å gjenvinne fragmenter av telemetri fra MAVEN etter at det kom tilbake fra planeten.

«Som en del av denne etterforskningen klarte teammedlemmene ved Jet Propulsion Laboratory å gjenvinne noen fragmenter av telemetri og Doppler-skiftdata fra romskipet,» sa Moreau. «Disse dataene ble ekstrahert fra opptatte signaler som ble gjenvunnet i timene etter tapet av signalet.»

Bakkekontrollørene så ikke disse svake signalene i sanntid. De ble registrert som en del av en separat vitenskapskampanje som søkte å samle informasjon om tettheten og dynamikken i den øvre martianske atmosfæren, som kan forvrenge radioignaler som passerer gjennom den.

«En av de delene vi klarte å bekrefte er en inertialratemåling som fortalte oss at romskipet snurret med omtrent 2,7 omløp per minutt,» sa Moreau. «Vi bekreftet også at dette var konsistent med en Doppler-signatur vi så i dataene. Dette er raskere enn romskipet forventes å rotere, og det indikerer et problem som romskipet sannsynligvis ikke kunne komme seg etter.»

Uten evnen til å peke solcellepanelene mot solen, sannsynligvis tømte det roterende romskipet batteriene innen timer.

«Dette var en av datapunktene som hjalp oss å forstå at romskipet sannsynligvis nådde en strømtilstand som ikke var bærekraftig for å fortsette operasjoner,» sa Moreau. «Dette er faktaene vi vet. Anomali-revisjonsstyret undersøker fortsatt rotårsaken til hva som initierte svikten.»

MAVEN går i bane rundt Mars på en oval, elliptisk bane som bringer det nærmest 110 mil (180 km) og lengst 2 500 mil (4 000 km) fra planetens overflate. Romskipet, omtrent som en liten bil, vil forbli i denne banen i 50 til 100 år før det naturlig faller ned i den martianske atmosfæren og brenner opp.

Hva er tapt? Det er to svar på dette spørsmålet. MAVEN ble bygget som en forskningsplattform for å hjelpe forskere med å forstå hvordan Mars' atmosfære har endret seg over milliarder av år. Før MAVEN visste forskere at Mars må ha vært varmere og våtere og at den hadde en tykkere atmosfære i fortiden. Atmosfæren på Mars i dag er for tynn til å støtte flytende vann på overflaten, og det er nå utbredt bevis på et nettverk av innsjøer og elver som dekket Mars for milliarder av år siden.

MAVEN fant bevis på mekanismene som stripte molekyler fra de øvre lagene av atmosfæren, en prosess kjent som atmosfærisk flukt. Romskipets vitenskapelige instrumenter overvåket hvordan den martianske atmosfæren reagerte på utbrudd av ladede partikler utstrålet av massive utbrudd fra solen.

«En av våre mest spennende oppdagelser brukte 11 års MAVEN-data til å observere, for første gang på noen planet, en atmosfærisk fluktprosess kalt sputtering,» sa Shannon Curry, hovedforskeren for MAVEN ved Laboratory for Atmospheric and Space Physics ved University of Colorado Boulder. «Dette er der ladede partikler kolliderer med den øvre atmosfæren og spruter ut den nøytrale atmosfæren, på samme måte som å kaste en kule i et basseng. Teamet vårt brukte sjeldne gassisotoper for å bekrefte at denne prosessen har vært en dominerende fluktmekanisme i milliarder av år.»

En solstorm i 2024 traff Mars spesielt hardt. «Vi så flere størrelsesordener med atmosfærisk flukt, og vi fanget til og med bilder av glødende aurora over planeten,» sa Curry.

MAVENs vitenskapelige arv er sikret, men farvelen er ikke lett for teamene som jobbet med prosjektet, som forskerne først foreslo til NASA i 2006.

«Jeg tror teamet virkelig har opplevd tapet av en kjær med slutten på oppdraget,» sa Moreau.

«Samtidig er vi utrolig stolte av vitenskapen vi har oppnådd det siste tiåret,» sa Curry. «MAVEN var den beste observatøren av atmosfærisk flukt i hele solsystemet. Vi har nå en bedre forståelse av atmosfærisk flukt på Mars enn på noen andre planeter, inkludert jorden.»

Det andre svaret er litt mindre sikkert. Størstedelen av tiden på Mars ga MAVEN-romskipet en relé for vitendata som ble sendt opp fra NASAs rovere og landere på den martianske overflaten. Reléet tillot NASA å returnere betydelig mer data og bilder fra rovere som Perseverance og Curiosity enn det som ville vært mulig gjennom en direkte radioforbindelse til jorden.

Med MAVEN ute av bildet, har NASA fire andre baneobjekter det kan bruke for å gi denne kritiske radioforbindelsen. Men tjenestemenn er ikke sikre på hvor lenge disse vil vare. Tre av de fire gjenværende relébaneobjektene er eldre enn MAVEN, som spilte en overveiende rolle i relénettverket takket være høyere bane.

«Gjennom oppdragets levetid støttet MAVEN mer enn 8 prosent av alle reléøkter planlagt av våre rovere og landere, men det utgjorde nesten 18 prosent av alle dataene som ble returnert, noe som illustrerer dets nytte når det returnerte store datavolumer,» sa Tiffany Morgan, direktør for NASAs Mars-utforskningsprogram.

Nettverket har fortsatt god kapasitet til å støtte Perseverance- og Curiosity-roverne, med noen mindre forbehold.

«Vi har fortsatt ressurser, og disse ressursene har justert mengden data de returnerer, og roverne har også justert sin planlegging for hvordan de kobler seg til disse ressursene,» sa Morgan. «Det er en liten forsinkelse av og til, fordi vi ikke har så mange ressurser i sikte, for å få vitendata tilbake, og MAVEN var kritisk for å returnere vitenskapelige data fremfor operasjonelle data. Men Mars-relénettverket er fortsatt tilstrekkelig robust på dette tidspunktet til å håndtere tapet av MAVEN med den ekstra forsinkelsen.»

NASA ber kommersielle selskaper om å utvikle en erstatning for det eksisterende Mars-relénettverket. Det nye kommersielle systemet, kalt Mars Telecommunications Network, forventes å gi høyere gjennomstrømning og bredere dekning for NASAs fremtidige oppdrag til den røde planeten.

«I stedet for at hvert oppdrag designer sin egen kommunikasjonsløsning, vil vi bygge en mer kapabel arkitektur som er bevisst designet for Mars,» sa Greg Heckler, sjefsprogramsjef for kapasitetsutvikling ved NASAs kontor for romkommunikasjon og navigasjon. «Det vil bli bygget på lærdommene fra MAVEN, fra de andre baneobjektene, fra alle oppdrag som opererer i dette miljøet, inkludert de nåværende roverne, og fra noen av våre voksende bestrebelser rundt Månen.»

NASA ønsker at Mars Telecommunications Network skal være operativt innen 2030-tallet. Byrået utstedte en anmodning om tilbud forrige måned.

«Jeg tror det er … hast,» sa Heckler. «Jeg tror at NASAs etablering av denne infrastrukturen vil være veldig viktig for å fortsette vitenskapelige operasjoner for de nåværende oppdragene her i dag og deretter gjøre oss i stand til å gjennomføre disse nyere, større oppdragene som gjenstår.»

### BRIEF · Isolerer suicidale barn i fengsel: «Svært urovekkende» (nrk, 2.5s)

**NRK** — Sivilombudet kritiserer bruk av sikkerhetsceller for mindreårige i fengsel.


_Summary throughput: 54.6s for 4 articles → ~13.7s each; a 14-article edition ≈ 3.2 min sequential._

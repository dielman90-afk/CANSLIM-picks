# CANSLIM-Bericht Verbesserungslog

## Lauf 01. Juni 2026 (Montag)

### Was gut lief
- Slack-Direktnachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only, ~3.000 Zeichen, klar unter 3.500-Limit
- JSON erfolgreich auf GitHub main ersetzt (dielman90-afk/CANSLIM-picks, Commit 193f5dc7) -- diesmal funktionierte der Push direkt ueber das GitHub-MCP
- Marktampel klar GRUEN: Juni-Start auf Rekordhochs, Montag-Futures hoeher. Basis Freitags-Close 29.05.: S&P 500 7.580,06 ATH, Nasdaq 26.972,62 ATH, Dow ueber 51.000. 9. Wochengewinn in Folge, Nasdaq +8% im Mai
- US-Iran-Waffenstillstand um 60 Tage verlaengert -- geopolitischer Rueckenwind, Oel-Risiko entschaerft
- 5 Qualitaets-Setups exakt im Breakout-Fenster: HWM direkt am Pivot 259,82; CLS frisch ausgebrochen (+10,2% 29.05.); NVDA/GEV/FIX kurz vor Pivot -- genau das vom User geforderte Profil
- Alle 5 Picks haben Q1-Earnings hinter sich (NVDA-Report 20.05. verifiziert) -- kein akutes Earnings-Risiko
- CLS-Datenfalle erkannt und vermieden: Suchergebnisse mischten CLS.TO (Toronto, ~386) mit US-CLS (533,01) -- US-Kurs korrekt verifiziert
- AVGO konsequent gefiltert (Earnings 03.06., in 2 Tagen) und DY (zu weit gelaufen, ~+23% ueber Pivot) -- Filter-Disziplin gewahrt
- Spekulative/weit gelaufene Namen (RXT +165%, INOD, HUT) bewusst NICHT aufgenommen -- Qualitaet vor Quantitaet

### Probleme
- Log war stale: letzter protokollierter Eintrag Lauf 21 (07.05.), aber JSON wurde bis 31.05. mit voellig anderen Picks (HWM/CLS/NVDA/GEV/FIX statt AMD/STRL/VRT/FIX/ECG) aktualisiert -- zwischenzeitliche Laeufe wurden nicht protokolliert. Lauf-Nummerierung daher unsicher, deshalb datumsbasierter Titel
- Sektor-Konzentration weiterhin hoch: 4 von 5 Picks AI-Infrastruktur (CLS Networking, NVDA Chips, GEV Power, FIX HVAC/Datacenter) -- nur HWM (Aerospace) diversifiziert
- Montag-Close 01.06. lag zum Report-Zeitpunkt noch nicht vor -- Basis ist Freitags-Close 29.05. (wie schon im 31.05.-Update)
- CLS am oberen Buy-Zone-Rand -- bei sofortigem Einstieg erhoehtes Risiko, kleiner Pullback waere ideal

### Verbesserungen fuer naechsten Lauf

1. **AVGO-Post-Earnings (KRITISCH 04.06.):**
   - AVGO berichtet 03.06. a.h. (Konsens EPS ~2,40, Umsatz ~22,1 Mrd, AI-Semis +140% YoY)
   - Bei Beat + starker Guidance: als Top-Pick aufnehmen (Basis-/Breakout-Position pruefen)
   - Bei Miss/Sell-the-News: weiter filtern

2. **MARKTAMPEL-MONITORING:**
   - S&P 7.580 ATH -- GRUEN solange ueber ~7.400
   - Bei Bruch unter 7.300 (50-Tage-MA-Naehe) auf GELB
   - US-Iran-MoU laeuft 60 Tage -- bei Scheitern Oel-/Markt-Risiko

3. **POST-BREAKOUT-MONITORING der aktuellen Picks:**
   - HWM: GRUEN solange ueber Pivot ~259; bei Bruch unter 250 YELLOW
   - CLS: nach +10,2% kleiner Pullback gesund; bei Bruch unter ~490 YELLOW
   - NVDA: GRUEN solange ueber ~205; Ausbruch ueber ~225 = Bestaetigung
   - GEV: Ausbruch ueber ~1.031 abwarten; bei Bruch unter 920 YELLOW
   - FIX: bei Bruch unter ~1.750 YELLOW; Ausbruch ueber ~2.074 = Bestaetigung

4. **Slack-Formatierung (bewaehrt, beibehalten):**
   - Nur ASCII, keine Emojis, kein EUR-Zeichen, Umlaute als ae/oe/ue
   - DACH-Zahlenstil (Punkt-Tausender, Komma-Dezimal), unter 3.500 Zeichen
   - Direktnachricht an User (channel = U0AMXQ1EA4B / D0AN24D9PTQ)

5. **Datenquellen-Hinweis:**
   - Bei Dual-Listings (z.B. CLS US vs CLS.TO Toronto) immer US-Notierung verifizieren -- Suchergebnisse mischen die Boersen
   - tradingkey.com zuverlaessig fuer Tagesbewegungen (CLS +10,2% 29.05. bestaetigt)

6. **Sektor-Diversifizierung:**
   - 4 von 5 Picks AI-Infrastruktur -- bei naechstem Lauf gezielt nach Nicht-AI-Leadern suchen (Healthcare, Financials, Industrials ausserhalb Power)

7. **Log-Pflege:**
   - Log war ueber Wochen nicht aktualisiert -- bei jedem Lauf konsequent fortschreiben, damit Lauf-Historie und Lessons erhalten bleiben

8. **JSON-Export (funktioniert):**
   - GitHub-MCP create_or_update_file auf main mit SHA -- reliabel, diesmal kein Bash-Push noetig
   - 5 GREEN-Picks, AVGO + DY in "gefiltert" dokumentiert


## Lauf 21 -- 07. Mai 2026 (Donnerstag)

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt (~3.300 Zeichen)
- JSON-Export per Read+Write direkt nach Projektordner erfolgreich
- Marktampel klar GRUEN: S&P 500 7.365,12 ATH (+1,46%) und Nasdaq 25.838,94 ATH (+2,02%) am 06.05. -- beide auf neuen Rekordhochs
- Iran-Peace-Deal-Hoffnung treibt Markt, Oel weiter rueckläufig nach Spike auf $114
- AMD als #1 GREEN NEU aufgenommen -- Mega-Q1-Beat: EPS $1,37, Umsatz $10,25B (+38%), Datacenter +57% auf $5,8B, Q2-Guide $11,2B vs $9,9B Konsens. +18,61% am 06.05. = bestes Earnings-Day in 7 Jahren
- STRL als #2 GREEN gehalten -- Fortsetzung post +52% Mega-Rally, Schlusskurs $881,98 am 06.05. (+9,4% Folgetag), 7-Tage +70,8%
- VRT als #3 GREEN bestaetigt -- ATH $358,92 am 06.05., Cup-Handle voll bestaetigt
- FIX als #4 GREEN -- ATH-Zone $2.000+, 5-Tage +14%, Marketcap $69B
- ECG als #5 GREEN gehalten -- $169,16 am 06.05., bestaetigt nach Q1-Beat
- 5 von 5 Picks haben Q1-Earnings hinter sich -- niedrigste Earnings-Konzentration ueberhaupt
- Sektor-Diversifizierung verbessert: AMD bringt Halbleiter-Exposure rein (statt 100% Datacenter-Infrastruktur)
- MOD ausgelassen wegen Earnings 27.05. (3 Wochen) -- Risiko-Vermeidung

### Probleme
- AMD bei $421 = +18,6% Tagesperformance -- evtl. Pullback-Risiko nach Mega-Rally
- STRL nach +70% in 7 Tagen extrem ueberkauft -- Konsolidierung erwartet
- Workspace-Bash war NICHT verfuegbar -- GitHub-Push konnte NICHT ausgefuehrt werden
- EU-Pool weiter leer (RHM unter Threshold, ASML/SAP nicht geprueft)
- Sektor-Konzentration noch hoch: 4 von 5 Picks Datacenter/Infrastruktur (AMD bringt Halbleiter-Diversifikation)

### Verbesserungen fuer naechsten Lauf (08.05.)

1. **POST-RALLY MONITORING (KRITISCH):**
   - AMD: nach +18,6% Konsolidierung erwartet -- bei Bruch unter $390 sofort YELLOW, sonst GREEN solange ueber $400
   - STRL: nach +70% in 7 Tagen scharfer Pullback moeglich -- bei Bruch unter $800 YELLOW
   - VRT: Cup-Handle bestaetigt, GREEN solange ueber $340
   - FIX: ATH $2.003,65 -- bei Bruch unter $1.900 YELLOW
   - ECG: GREEN solange ueber $156

2. **MARKTAMPEL-MONITORING:**
   - S&P 7.365 ATH -- GRUEN solange ueber 7.250
   - Bei Bruch unter 7.150 (50-Tage-MA Naehe) sofort GELB
   - Iran-Peace-Deal-Hoffnung treibt Markt -- bei Scheitern der Verhandlungen Risiko fuer Marktampel
   - Oel zurueck unter $100 = sehr bullish, bei erneutem Spike auf $115+ Vorsicht

3. **Slack-Formatierung (bewaehrt, beibehalten):**
   - Nur ASCII, keine Emojis, kein EUR-Zeichen
   - Umlaute als ae/oe/ue
   - Punkt-Tausender und Komma-Dezimal fuer DACH-Style
   - Nachricht unter 3.500 Zeichen (Lauf 21: ~3.300)

4. **Datenquellen (funktionierend):**
   - finance.yahoo.com, marketbeat.com, cnbc.com, fool.com, thestreet.com
   - tradingkey.com fuer Stock-Movers
   - timothysykes.com fuer After-Hours-Bewegungen
   - prnewswire.com, stocktitan.net fuer Earnings-Pressemitteilungen
   - tradingeconomics.com, investing.com fuer EU-Kurse
   - 247wallst.com (NEU): zuverlaessig fuer Live-Updates
   - artvoice.com (NEU): gut fuer Mega-Rally-Stories
   - BLOCKIERT: swingtradebot.com, stockanalysis.com (intermittent)

5. **Kandidatenpool fuer naechsten Lauf (08.05.):**
   - AMD als #1 -- nach +18,6% evtl. Pullback erwartet, weiter GREEN solange ueber $400
   - STRL als #2 -- evtl. Konsolidierung nach +70%, GREEN solange ueber $800
   - VRT als #3 -- bestaetigt, GREEN
   - FIX als #4 -- bestaetigt, GREEN
   - ECG als #5 -- bestaetigt, GREEN
   - MOD weiter aus Pool wegen Earnings 27.05.
   - POWL als Watchlist nach +10% trotz Miss
   - RHM weiter ausgeschlossen bei EUR <1.450

6. **Earnings-Strategie (bewaehrt):**
   - Alle 5 Picks haben Q1-Earnings hinter sich -- IDEAL
   - Naechster Earnings-Termin: MOD 27.05. (3 Wochen) -- nicht im Pool
   - WARNUNG bei Earnings innerhalb 2 Wochen

7. **Sektor-Konzentration (verbessert):**
   - AMD bringt Halbleiter-Diversifikation (zuvor 100% Datacenter-Infrastruktur)
   - Pharma/Healthcare-Wachstumswerte fuer naechsten Lauf erneut pruefen
   - Cybersecurity (PANW, CRWD), Semiconductors (NVDA, AVGO, MRVL) als alternative Sektoren erwaegen

8. **JSON-Export funktioniert reliable:**
   - Read+Write direkt nach Projektordner erfolgreich
   - 4 Picks (AMD, STRL, VRT, FIX) -- alle GREEN
   - ECG ausgelassen weil Top 4 limitiert

9. **AMD-Lesson (KRITISCH):**
   - AMD verpasst zu haben in Lauf 18-20 war Verfehlung
   - Wenn Mega-Cap-Tech mit Earnings-Beat in unsere Kriterien faellt, MUSS aufgenommen werden
   - Halbleiter-Sektor (AMD, NVDA, AVGO, MRVL) bei Earnings-Beats systematisch pruefen

10. **GitHub-Push (Lauf 21):**
   - Workspace-Bash war NICHT verfuegbar -- Push uebersprungen
   - Slack-Bericht und JSON-Export erfolgreich -- Hauptprioritaet erfuellt
   - Bei naechstem Lauf erneut versuchen


## Lauf 20 -- 06. Mai 2026 (Mittwoch)

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt (~3.300 Zeichen)
- JSON-Export per Read+Write direkt nach Projektordner erfolgreich
- Marktampel klar GRUEN: S&P 500 7.259,22 ATH (+0,81%) und Nasdaq 25.326,13 ATH (+1,03%) am 05.05. -- beide auf neuen Rekordhochs
- Brent -3,99% auf $109,87, WTI -3,9% auf $102,27 -- Oel-Entspannung trotz Hormuz-Tensions sehr bullish fuer Tech/Wachstum
- STRL als #1 GREEN -- Mega-Explosion +52,4% von $529 auf $806 am 05.05. nach Blowout-Earnings: EPS $3,59 vs $2,19 (+64% Beat), Umsatz +92%
- FIX als #2 GREEN -- ATH $2.003,65 am 05.05., Range $1.907-$2.003, klarer Flat-Base-Breakout
- VRT als #3 GREEN -- neues ATH $341,02 am 05.05. (+3,04%), Cup-Handle voll bestaetigt
- ECG als #4 GREEN NEU aufgenommen -- +10,1% am 05.05. nach Q1-Beat (EPS $1,14 vs $0,81, +40% Beat). FFTY Top-3 Holding mit +244% 52W
- MOD als #5 GREEN gehalten -- ATH $272,61 am 04.05., Cup-Handle nahe ATH, Earnings 27.05. (3 Wochen Warnung)
- POWL nicht aufgenommen trotz +10,49% am 05.05. -- EPS-Miss zeigt Schwaeche, ECG starkere Wahl
- 4 von 5 Picks haben Earnings hinter sich -- nur MOD mit 27.05. naechstem Risiko (3 Wochen)

### Probleme
- Sektorale Konzentration weiter hoch: alle 5 Picks sind Datacenter-/Infrastruktur-Plays (STRL Bau, FIX HVAC, VRT Power, ECG Bau, MOD Cooling)
- Hormuz-Tensions weiter latent vorhanden -- bei erneuter Eskalation Risiko fuer Marktampel
- EU-Pool weiter leer: STOXX 600 +0,7% am 05.05., aber FTSE -1,4% gemischt
- RHM weiter ausgeschlossen unter EUR 1.450 Threshold
- POWL trotz +10% nicht aufgenommen wegen EPS-Miss -- aber starke $400M-Order, Watchlist-Kandidat fuer naechsten Lauf
- Bewertungs-Risiken bei STRL nach +52% -- evtl. kurzfristige Konsolidierung erwartet

### Verbesserungen fuer naechsten Lauf (07.05.)

1. **POST-RALLY MONITORING (KRITISCH):**
   - STRL: nach +52% Konsolidierung erwartet -- bei Bruch unter $720 Cup-Hoch sofort YELLOW
   - FIX: ueber $2.000 ATH-Bereich, Pullback unter $1.900 = YELLOW
   - VRT: Cup-Handle-Buy-Point $276 noch viel Puffer, GREEN solange ueber $325
   - ECG: nach +10% mind. 1 Tag Pause erwartet, Buy-Zone $156-173
   - MOD: ATH $272,61 -- bei Bruch unter $260 YELLOW

2. **MARKTAMPEL-MONITORING:**
   - S&P 7.259 ATH -- klar GRUEN solange ueber 7.150
   - Bei Bruch unter 7.100 (50-Tage-MA Naehe) sofort GELB
   - Hormuz weiter im Auge behalten -- bei Brent ueber $115 Risiko fuer Marktampel
   - Fed haelt Zinsen, keine Cuts 2026 -- belastet Wachstumswerte langfristig
   - Tech-Sektor +2% am 05.05. -- bullisch, AI-Capex-Story zurueck

3. **Slack-Formatierung (bewaehrt, beibehalten):**
   - Nur ASCII, keine Emojis, kein EUR-Zeichen
   - Umlaute als ae/oe/ue
   - Punkt-Tausender und Komma-Dezimal fuer DACH-Style
   - Nachricht unter 3.500 Zeichen (Lauf 20: ~3.300)

4. **Datenquellen (funktionierend):**
   - finance.yahoo.com, marketbeat.com, cnbc.com, fool.com, thestreet.com
   - tradingkey.com fuer Stock-Movers
   - tradingeconomics.com, investing.com fuer EU-Kurse
   - simplywall.st, trefis.com fuer Analysen
   - benzinga.com, quiverquant.com fuer Earnings-Reaktionen
   - prnewswire.com, stocktitan.net fuer Earnings-Pressemitteilungen
   - timothysykes.com gut fuer After-Hours-Bewegungen
   - thecerbatgem.com (NEU): zuverlaessig fuer Earnings-Results-Detail
   - BLOCKIERT: swingtradebot.com, stockanalysis.com (intermittent)

5. **Kandidatenpool fuer naechsten Lauf (07.05.):**
   - STRL als #1 -- evtl. nach +52% Konsolidierung, weiter GREEN solange ueber $720
   - FIX als #2 -- bestaetigt, GREEN, Earnings ~Juli
   - VRT als #3 -- GREEN, Earnings ~Juli
   - ECG als #4 -- bestaetigt nach Beat, GREEN
   - MOD als #5 -- Earnings 27.05., GREEN bis dahin
   - POWL als Watchlist -- $400M-Order positiv, Beobachten
   - FN weiter aus Pool entfernt -- mind. 4 Wochen Pause
   - RHM weiter ausgeschlossen bei EUR <1.450

6. **Earnings-Strategie (bewaehrt):**
   - WARNUNG bei Earnings innerhalb 2 Wochen
   - 4 von 5 Picks haben Earnings hinter sich -- niedrige Earnings-Konzentration
   - MOD am 27.05. bleibt der einzige Mai-Termin

7. **Sektor-Konzentration (anhaltendes Thema):**
   - Alle 5 Picks weiterhin Datacenter-/Infrastruktur-Plays
   - Diversifizierung weg von reinem Datacenter pruefen
   - Healthcare/Pharma-Wachstumswerte fuer naechsten Lauf erneut pruefen
   - Cybersecurity (PANW, CRWD), Semiconductors (NVDA, AVGO) als alternative Sektoren erwaegen

8. **JSON-Export funktioniert reliable:**
   - Read+Write direkt nach Projektordner erfolgreich
   - 4 Picks (STRL, FIX, VRT, ECG) -- alle GREEN
   - MOD ausgelassen wegen Earnings-Risiko 27.05.

9. **POWL-Lesson:**
   - +10,49% trotz EPS-Miss zeigt: Markt belohnt Backlog/Order-News mehr als Quartals-EPS
   - Wenn Order-Story ueberzeugt, kann eine Aktie auch nach Miss steigen
   - POWL-Watchlist halten, ggf. naechster Lauf als #5 wenn keine Korrektur


## Lauf 19 -- 05. Mai 2026 (Dienstag)

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt (~3.300 Zeichen)
- JSON-Export per Read+Write direkt nach Projektordner erfolgreich
- Marktampel GRUEN (vorsichtig) korrekt: S&P 500 7.200,75 (-0,41%), Nasdaq 25.067,80 (-0,19%) am 04.05.
- STRL korrekt auf #1 hochgestuft nach Mega-Beat 04.05.: EPS $3,09 (+141%), Umsatz +92%, FY-Guidance massiv auf $18,40-19,05 EPS angehoben (vs Konsens $13,46), +22,6% AH auf $649,25
- FIX als #2 GREEN bestaetigt -- $1.867, ATH-Zone, keine Earnings-Risiken bis Juli
- VRT als #3 GREEN -- $328,80, Range $324-333, Cup-Handle voll bestaetigt
- MOD als #4 GREEN -- $261,26, Datacenter +78% YoY, Earnings 27.05. (3+ Wochen)
- POWL als #5 YELLOW: EPS $1,25 verfehlte Konsens $1,34 leicht, aber Mega-Order $400M Datacenter und Backlog +33% rekordhoch -- Mischsignal korrekt erkannt
- FN korrekt entfernt: Trotz Q3-Beat (EPS $3,72 vs $3,58) -10,84% AH wegen In-Line-Q4-Guidance -- Sell-the-News, Cup-Handle technisch gebrochen

### Probleme
- Hormuz-Spannungen wieder akut: UAE fing iranische Raketen ab, Brent +5,8% auf $114,44, WTI auf $106,42 -- Risiko fuer Marktampel
- Fed haelt Zinsen stabil, keine Cuts mehr fuer 2026 erwartet -- Stagflations-Risiko
- POWL EPS-Miss zeigt: Auch starke Backlog-Story kann kurzfristig schwach sein
- ECG hat Earnings 05.05. a.h. -- nicht aufgenommen wegen Risiko, naechster Lauf einarbeiten
- RHM weiter ausgeschlossen wegen EU-Pool-Schwaeche
- Sektorale Konzentration: alle 5 Picks weiterhin "Picks-and-Shovels" Datacenter-Plays

### Verbesserungen fuer naechsten Lauf (06.05.)

1. **POST-EARNINGS BEWERTUNG (06.05.):**
   - STRL: Reaktion am 05.05. tagsueber pruefen -- bei +20% Eroeffnung GREEN bestaetigen
   - POWL: Tag-Reaktion auf gemischtes Quartal pruefen -- bei stabiler Aktion GREEN, sonst durch ECG ersetzen
   - ECG Earnings 05.05. a.h. -- bei Beat ggf. als #5 statt POWL aufnehmen
   - FN: nicht zurueckholen -- Cup-Handle gebrochen, mind. 4 Wochen Konsolidierung noetig

2. **MARKTAMPEL-MONITORING (KRITISCH):**
   - S&P 7.200 -- bleibt GRUEN solange ueber 7.100
   - Bei Bruch unter 7.100 (50-Tage-MA Naehe) sofort GELB
   - Hormuz-Eskalation mit Brent ueber $115 koennte Markt schnell drehen
   - Fed haelt Zinsen, keine Cuts 2026 -- belastet Wachstumswerte
   - Bei weiterem Iran-Eskalation: Defensive Sektoren beobachten

3. **Slack-Formatierung (bewaehrt, beibehalten):**
   - Nur ASCII, keine Emojis, kein EUR-Zeichen
   - Umlaute als ae/oe/ue
   - Punkt-Tausender und Komma-Dezimal fuer DACH-Style
   - Nachricht unter 3.500 Zeichen (Lauf 19: ~3.300)

4. **Datenquellen (funktionierend):**
   - finance.yahoo.com, marketbeat.com, cnbc.com, fool.com, thestreet.com
   - tradingkey.com fuer Stock-Movers
   - tradingeconomics.com, investing.com fuer EU-Kurse
   - simplywall.st, trefis.com fuer Analysen
   - benzinga.com, quiverquant.com fuer Earnings-Reaktionen
   - prnewswire.com, stocktitan.net fuer Earnings-Pressemitteilungen
   - dailypolitical.com fuer Analyst-Updates
   - timothysykes.com (NEU): gut fuer After-Hours-Bewegungen
   - BLOCKIERT: swingtradebot.com, stockanalysis.com (intermittent)

5. **Kandidatenpool fuer naechsten Lauf (06.05.):**
   - STRL als #1 bestaetigt nach Mega-Beat -- bis ~Juli kein Earnings-Risiko, GREEN
   - FIX als #2 bestaetigt -- bis Juli kein Earnings-Risiko, GREEN
   - VRT als #3 -- ATH bestaetigt, GREEN, kein Earnings-Risiko
   - MOD als #4 -- Earnings 27.05. (3 Wochen), GREEN
   - POWL als #5 -- nach Tag-Reaktion 05.05. neu bewerten
   - ECG: Earnings 05.05. a.h. -- bei Beat als Watchlist/Top-5
   - FN aus Pool entfernt -- mind. 4 Wochen Pause
   - RHM weiter ausgeschlossen bei EUR <1.450

6. **Earnings-Strategie (bewaehrt):**
   - Sell-the-News-Effekt bei FN war ein wichtiger Lerneffekt: Selbst Q3-Beat reicht nicht, wenn Q4-Guidance nur in-line
   - Bei Folge-Laeufen explizit auf Beat-Magnitude UND Guidance achten
   - WARNUNG bei Earnings innerhalb 2 Wochen
   - Konzentrations-Risiko vermeiden: max. 2 von 5 mit Earnings im 1-Wochen-Fenster

7. **EU-Pool (kritisch leer seit mehreren Laeufen):**
   - RHM weiter unter Threshold EUR 1.450 ausgeschlossen
   - ASML, SAP, Novo Nordisk fuer naechsten Lauf erneut pruefen
   - Top 5 ausschliesslich aus US-Markt ist OK gemaess SKILL.md

8. **JSON-Export funktioniert reliable:**
   - Read+Write direkt nach Projektordner erfolgreich
   - 4 Picks (STRL, FIX, VRT, MOD) -- alle GREEN
   - POWL als YELLOW im Slack, aber nicht im JSON (nur 4 GREEN-Picks)

9. **Sektor-Konzentration (anhaltendes Thema):**
   - Alle 5 Picks weiterhin Datacenter-/Infrastruktur-Plays
   - STRL (Bau), FIX (HVAC), VRT (Power), MOD (Cooling), POWL (Power)
   - Diversifizierung weg von reinem Datacenter pruefen
   - Pharma/Healthcare-Wachstumswerte fuer naechsten Lauf erneut pruefen


## Lauf 18 -- 04. Mai 2026 (Montag)

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt (~3.300 Zeichen)
- JSON-Export per Read+Write direkt nach Projektordner erfolgreich
- Marktampel klar GRUEN: S&P 500 7.230,12 ATH (+0,29%) und Nasdaq 25.114,44 ATH (+0,89%) am 01.05. -- Mai mit neuen Rekorden gestartet
- FIX als #1 GREEN -- $1.867 am 03.05., neue ATH-Zone, keine Earnings-Risiken bis Juli
- VRT als #2 GREEN -- ATH $331,97 am 01.05., Cup-Handle voll bestaetigt
- MOD als #3 GREEN -- ATH $268,51 am 02.05., Earnings 27.05. (3+ Wochen)
- FN als #4 YELLOW -- WARNUNG erfolgreich platziert (Earnings HEUTE 04.05.)
- STRL als #5 YELLOW -- WARNUNG erfolgreich platziert (Earnings HEUTE 04.05.)
- Apple-Beat hat Mag-7 Sektor gestuetzt
- Iran-Waffenstillstand intakt, Oel ruecklaeufig

### Probleme
- 2 von 5 Picks (FN, STRL) haben heute nachboerslich Earnings -- hohes Konzentrations-Risiko fuer naechsten Lauf
- POWL ebenfalls Earnings 04.05. -- nicht aufgenommen wegen Risiko
- ECG Earnings 05.05. -- ebenfalls nicht aufgenommen
- RHM bei EUR 1.355,80 weiter unter Threshold EUR 1.450 -- EU-Pool bleibt leer
- Bei FN/STRL Miss am 04.05. fehlen sofort verfuegbare Ersatz-Kandidaten ohne eigenes Earnings-Risiko

### Verbesserungen fuer naechsten Lauf (05.05.)

1. **POST-EARNINGS BEWERTUNG (KRITISCH am 05.05.):**
   - FN Earnings 04.05. a.h. -- bei Beat (Konsens EPS ~$2,80) Signal auf GREEN, bei Miss durch Watchlist ersetzen
   - STRL Earnings 04.05. a.h. -- Konsens EPS $2,18, Umsatz $605,81M; bei Beat GREEN
   - POWL Earnings 04.05. -- bei Beat als Watchlist-Kandidat aufnehmen
   - ECG Earnings 05.05. -- bei Beat als Watchlist-Kandidat aufnehmen

2. **MARKTAMPEL-MONITORING:**
   - S&P 7.230 ATH -- klar GRUEN solange ueber 7.100
   - Bei Bruch unter 7.100 (50-Tage-MA Naehe) sofort GELB
   - Mag-7-Earnings hinter uns -- nun makro-getrieben
   - Iran-Waffenstillstand bleibt wichtig
   - Fed-Sitzung 06./07.05. -- Watch fuer Markt-Reaktion

3. **Slack-Formatierung (bewaehrt, beibehalten):**
   - Nur ASCII, keine Emojis, kein EUR-Zeichen
   - Umlaute als ae/oe/ue
   - Punkt-Tausender und Komma-Dezimal fuer DACH-Style
   - Nachricht unter 3.500 Zeichen (Lauf 18: ~3.300)

4. **Datenquellen (funktionierend):**
   - finance.yahoo.com, marketbeat.com, cnbc.com, fool.com, thestreet.com
   - tradingkey.com fuer Stock-Movers
   - tradingeconomics.com, investing.com fuer EU-Kurse
   - simplywall.st, trefis.com fuer Analysen
   - ad-hoc-news.de (NEU): zuverlaessig fuer S&P-Schlusskurse
   - stocktitan.net fuer Earnings-Termine
   - BLOCKIERT: swingtradebot.com, stockanalysis.com (intermittent)

5. **Kandidatenpool fuer naechsten Lauf (05.05.):**
   - FIX als #1 bestaetigt -- bis Juli kein Earnings-Risiko, GREEN
   - VRT als #2 -- ATH bestaetigt, GREEN, kein Earnings-Risiko
   - MOD als #3 -- ATH 02.05., GREEN, Earnings 27.05.
   - FN: Post-Earnings-Reaktion einarbeiten -- GREEN bei Beat
   - STRL: Post-Earnings-Reaktion einarbeiten -- GREEN bei Beat
   - POWL: Post-Earnings -- ggf. neuer Top-5-Kandidat
   - ECG: Post-Earnings 05.05. -- ggf. neuer Top-5-Kandidat
   - RHM weiter ausgeschlossen bei EUR <1.450

6. **Earnings-Strategie (bewaehrt):**
   - WARNUNG bei Earnings innerhalb 2 Wochen
   - Am Tag der Earnings: explizite "HEUTE"-Warnung
   - Folge-Lauf: Beat/Miss-Reaktion einarbeiten
   - Bei Miss sofort durch Watchlist-Kandidaten ersetzen
   - Konzentrations-Risiko vermeiden: max. 2 von 5 mit Earnings im 1-Wochen-Fenster

7. **EU-Pool (kritisch leer seit mehreren Laeufen):**
   - RHM bei EUR 1.355 -- 7%+ Erholung noetig fuer Wiederaufnahme
   - ASML, SAP, Novo Nordisk fuer naechsten Lauf erneut pruefen
   - Top 5 ausschliesslich aus US-Markt ist OK gemaess SKILL.md

8. **JSON-Export funktioniert reliable:**
   - Read+Write direkt nach Projektordner erfolgreich
   - 4 Picks (FIX, VRT, MOD, FN) -- FIX/VRT/MOD GREEN, FN YELLOW

9. **Sektor-Konzentration beachten:**
   - Alle 5 Picks sind "Picks-and-Shovels"-Plays auf AI-Datacenter-Boom
   - FIX (HVAC), VRT (Power), MOD (Cooling), FN (Optik), STRL (Bau)
   - Diversifizierung weg von reinem AI-Datacenter pruefen
   - Pharma/Healthcare-Wachstumswerte als Diversifikation pruefen


## Lauf 17 -- 01. Mai 2026

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt (~3.300 Zeichen)
- JSON-Export per Read+Write direkt nach Projektordner erfolgreich
- Marktampel auf GRUEN bestaetigt: S&P 500 7.209 ATH (+1,02%), Nasdaq 24.892 ATH (+0,89%) am 30.04. -- bester Monat seit 2020
- Mag-7-Earnings: GOOGL +10%, AAPL/QCOM (+16%) Beats; MSFT -4%/META -9% wegen AI-Capex-Sorgen
- Alle 11 Sektoren positiv am 30.04.
- FIX als #1 hochgestuft -- Post-Earnings GREEN, ATH $1.840,25 am 30.04. (+6,73%), Backlog $12,45B
- VRT als #2 -- Recovery auf $315, Cup-Handle Buy-Point $276 intakt, Vanguard 7,48% Stake bekannt
- MOD als #3 NEU -- Datacenter-Cooling +78% YoY, Cup-Handle bei $254, Earnings 27.05. (3+ Wochen)
- FN als #4 mit YELLOW -- Earnings 04.05. (3 Tage!)
- STRL als #5 mit YELLOW -- ATH $515 am 30.04., Earnings 04.05. (3 Tage!)
- Concentration-Risiko in Earnings-Saison reduziert: nur 2 von 5 Picks haben Mai-Earnings (FN, STRL)

### Probleme
- 3 ehemals starke Watchlist-Kandidaten haben am 04.05. Earnings (FN, STRL, POWL) -- POWL daher nicht aufgenommen
- ECG verworfen: Earnings 05.05., zu hohe Konzentration
- Nasdaq-Tech-Sektor unter Druck wegen MSFT/META -- Halbleiter und Cloud beobachten
- Bei AAPL-Schwaeche im Mai (Tariffe, China) koennte Mag-7-Rallye stoppen
- RHM weiter unter EUR 1.450 -- EU-Pool bleibt leer
- FN-Position vor Earnings 04.05. konzentriert -- Bei Miss schnell durch ECG/POWL ersetzen

### Verbesserungen fuer naechsten Lauf

1. **MARKTAMPEL-MONITORING (KRITISCH):**
   - S&P 7.209 ATH -- klar GRUEN solange ueber 7.000
   - Bei Bruch unter 7.100 (50-Tage-MA) sofort GELB
   - Mag-7-Earnings hinter uns -- nun makro-getrieben
   - Iran-Waffenstillstand bleibt wichtig fuer Marktstabilitaet
   - Brent-Verlauf, ISM-Daten, Fed-Sitzung 06./07.05. beobachten

2. **Slack-Formatierung (bewaehrt, beibehalten):**
   - Nur ASCII, keine Emojis, kein EUR-Zeichen
   - Umlaute als ae/oe/ue
   - Punkt-Tausender und Komma-Dezimal fuer DACH-Style
   - Nachricht unter 3.500 Zeichen (Lauf 17: ~3.300)

3. **Datenquellen (funktionierend):**
   - finance.yahoo.com, marketbeat.com, cnbc.com, fool.com, thestreet.com
   - tradingkey.com fuer Stock-Movers (gut fuer +/-% intraday)
   - tradingeconomics.com, investing.com fuer EU-Kurse
   - simplywall.st, trefis.com fuer Analysen
   - quiverquant.com (NEU): gut fuer Q1-Earnings-Reactions
   - dailypolitical.com (NEU): gut fuer Analyst-Upgrades und 52W-Highs
   - BLOCKIERT: swingtradebot.com, stockanalysis.com (intermittent), nasdaq.com (intermittent)

4. **Kandidatenpool fuer naechsten Lauf (04.05.):**
   - FIX als #1 bestaetigt -- bis Juli kein Earnings-Risiko, GREEN
   - VRT als #2 -- Recovery bestaetigt, GREEN
   - MOD als #3 NEU -- Earnings 27.05. (3 Wochen), GREEN
   - FN als #4 -- KRITISCH: Earnings 04.05.! Vor Lauf am 04.05. letzte Warnung, am 05.05. Ergebnis einarbeiten
   - STRL als #5 -- KRITISCH: Earnings 04.05.! Identisch
   - POWL als Watchlist -- Earnings 04.05. ebenfalls
   - ECG als Watchlist -- Earnings 05.05.
   - RHM weiter ausgeschlossen bei EUR <1.450

5. **Earnings-Strategie (KRITISCH fuer 04.05.-Lauf):**
   - 04.05. Lauf: Letzte Warnung fuer FN, STRL (an dem Tag erscheinen Zahlen!)
   - 05.05. Lauf: Earnings-Ergebnisse einarbeiten -- bei Beat GREEN, bei Miss durch ECG/POWL ersetzen
   - POWL Earnings auch 04.05. -- nach Beat aufnehmen
   - ECG Earnings 05.05. -- nach Beat aufnehmen
   - MOD Earnings ~27.05. -- bis dahin sicher

6. **VRT-Spezialfall (geloest):**
   - Recovery auf $315 nach -5,27% am 28.04. -- Cup-Handle-Buy-Point $276 weit intakt
   - Q2-Guidance-Sorgen verarbeitet
   - Bei Bruch unter $295 erneut beobachten

7. **EU-Pool (kritisch leer):**
   - RHM Trend weiter abwaerts -- bei Erholung ueber EUR 1.450 wieder aufnehmen
   - ASML, SAP, Novo Nordisk fuer naechsten Lauf erneut pruefen
   - Alternativ Top 5 ausschliesslich aus US-Markt -- ist OK gemaess SKILL.md

8. **JSON-Export funktioniert reliable:**
   - Read+Write direkt nach C:\Users\andyg\Documents\Claude\Projects\Tägliche CANSLIM Analyse\canslim-picks.json
   - 4 Picks (FIX, VRT, MOD, FN), FIX/VRT/MOD GREEN, FN YELLOW

9. **Mag-7-Lessons fuer Sektor-Allocation:**
   - AI-Capex-Skepsis getroffen MSFT/META, aber Datacenter-Infrastruktur (FIX, VRT, MOD) profitiert
   - Picks sind alle "Picks-and-Shovels"-Plays auf AI-Boom -- robust gegen Hyperscaler-Capex-Bedenken
   - GOOGL-Beat zeigt: AI-Monetarisierung fortgeschritten, sektorale Diversifizierung wichtig

10. **Geo-politische Risiken:**
   - Iran-Waffenstillstand haelt -- Brent unter $112
   - China-Taiwan, Russland-Ukraine weiterhin im Fokus
   - Naechster Lauf: pruefen ob Markt noch GRUEN -- bei Bruch unter 7.000 sofort GELB


## Lauf 16 -- 29. April 2026

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt (~3.300 Zeichen)
- JSON-Export per Read+Write direkt nach Projektordner erfolgreich
- Marktampel weiterhin GRUEN (vorsichtig): S&P 500 7.138,80 (-0,49%), Nasdaq 24.663,80 (-0,90%) am 28.04. -- Pullback vom ATH 7.165
- VRT Q2-Guidance-Reaktion (-5,27% am 28.04.) korrekt erfasst und Signal von GREEN auf YELLOW gesenkt
- FIX als #1 hochgestuft -- Post-Earnings GREEN, ATH $1.829 am 24.04., Backlog $12,45B
- FN als #2 -- Cup-Handle Breakout intakt bei $720, FFTY #3, aber Earnings 11.05. (YELLOW)
- STRL als #3 -- Double Bottom intakt, ATH $512 am 24.04., Earnings 04.05. (5 Tage!) prominent gewarnt
- VRT als #4 statt #1 wegen Q2-Guidance-Schwaeche -- Cup-Handle-Buy-Point $276 noch intakt, FY raised
- ECG als #5 wieder im Pool -- Cup-Pattern bei $137, FFTY Top-3
- Alle 5 Picks fundamentale CANSLIM-Kriterien erfuellt, alle aus FFTY Top-Holdings

### Probleme
- VRT Q2-Guidance ($1,37-1,43 vs Konsens $1,44) loeste -5,27% aus trotz starkem Q1-Beat -- Markt bestraft Wachstumsverlangsamung scharf
- EMEA-Region bei VRT -29% organisch -- regionale Schwaeche bedrohlich, kein temporaeres Phaenomen
- OpenAI-Umsatzverfehlung (WSJ-Bericht) am 28.04. drueckt Chip-/AI-Sektor breit
- UAE verlaesst OPEC -- Brent ueber $112, Oel-Inflation neu im Fokus
- Big-Tech-Earnings (MSFT, GOOGL, META, AMZN heute/morgen, AAPL Do) koennten Markt drehen
- RHM bei EUR 1.325 weiter unter Threshold EUR 1.450 -- EU-Pool bleibt leer

### Verbesserungen fuer naechsten Lauf

1. **MARKTAMPEL-MONITORING (KRITISCH):**
   - S&P 7.138 weiter ueber 6.950 -- bleibt GRUEN
   - Bei Bruch unter 7.000 sofort GELB
   - Bei Big-Tech-Misses Mi/Do koennte Markt schnell drehen -- am 30.04. Lauf neu bewerten
   - Nasdaq -0,90% staerker getroffen -- Tech-Schwaeche im Auge behalten
   - Brent ueber $112 + Stagflation-Risiko -- Defensive Sektoren beobachten

2. **Slack-Formatierung (bewaehrt, beibehalten):**
   - Nur ASCII, keine Emojis, kein EUR-Zeichen
   - Umlaute als ae/oe/ue
   - Punkt-Tausender und Komma-Dezimal fuer DACH-Style
   - Nachricht unter 3.500 Zeichen (Lauf 16: ~3.300)

3. **Datenquellen (funktionierend):**
   - finance.yahoo.com, marketbeat.com, cnbc.com, fool.com, thestreet.com
   - tradingkey.com fuer Stock-Movers (gut fuer +/-% intraday)
   - tradingeconomics.com, investing.com fuer EU-Kurse
   - simplywall.st, trefis.com fuer Analysen
   - BLOCKIERT: swingtradebot.com, stockanalysis.com (intermittent), nasdaq.com (intermittent)

4. **Kandidatenpool fuer naechsten Lauf:**
   - FIX als #1 bestaetigt -- bis Juli kein Earnings-Risiko, GREEN
   - FN als #2 -- WARNUNG: Earnings 11. Mai (in 12 Tagen ab 30.04.)
   - STRL als #3 -- WARNUNG: Earnings 04.05. (in 5 Tagen!) -- bei Folge-Lauf am 04.05. nur 0 Tage entfernt!
   - VRT als #4 -- nach -5,27% Wirkung beobachten. Bei Bruch unter $276 (Cup-Handle Buy-Point) sofort durch MOD oder POWL ersetzen
   - ECG als #5 -- Earnings 19. Mai (3 Wochen)
   - MOD bei $247,69 (FFTY-Holding, Data-Center +78% YoY) als nahe Watchlist halten
   - POWL bei ~$229 nach 3:1-Split, $1,6B Backlog -- Watchlist
   - RHM weiter ausgeschlossen bei EUR <1.450

5. **Post-Earnings-Strategie (NEU 30.04.):**
   - Big-Tech-Earnings Mi/Do beobachten -- bei Misses sofort Marktampel pruefen
   - STRL Earnings 04.05. (a.h.) -- 04.05. Lauf VOR Zahlen warnen, 05.05. Lauf nach Zahlen einarbeiten
   - FN Earnings 11.05. -- bei Folge-Laeufen Position verkleinern bis Ergebnis bekannt
   - Bei Earnings-Misses sofort durch Watchlist-Kandidat (MOD, POWL) ersetzen

6. **VRT-Spezialfall (NEU):**
   - Q1 stark, FY raised, aber Q2 Guidance unter Konsens
   - Bei -5,27% am 28.04. abgestraft -- Q2 wird der Test
   - Stop-Loss bei Bruch unter $276 (Cup-Handle Buy-Point)
   - Bei weiterem Drop am 29.04./30.04. sofort durch MOD oder POWL ersetzen
   - EMEA-Schwaeche -29% organisch -- nicht temporaer

7. **EU-Pool (kritisch leer):**
   - RHM Trend weiter abwaerts -- bei Erholung ueber EUR 1.450 wieder aufnehmen
   - ASML, SAP, Novo Nordisk fuer naechsten Lauf erneut pruefen
   - Alternativ Top 5 ausschliesslich aus US-Markt -- ist OK gemaess SKILL.md

8. **JSON-Export funktioniert reliable:**
   - Read+Write direkt nach C:\Users\andyg\Documents\Claude\Projects\Tägliche CANSLIM Analyse\canslim-picks.json
   - 4 Picks (FIX, FN, STRL, VRT), FIX GREEN, FN+STRL+VRT YELLOW

9. **Geo-politische Risiken (verschaerft):**
   - UAE verlaesst OPEC am 28.04. -- Brent ueber $112
   - Hormuz-Blockade weiter aktiv
   - OpenAI-Umsatzverfehlung WSJ-Bericht -- AI/Chip-Sektor breit unter Druck
   - Naechster Lauf: pruefen ob Markt noch GRUEN -- bei Bruch unter 7.000 sofort GELB


## Lauf 15 -- 27. April 2026

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt (~3.250 Zeichen)
- JSON-Export per Read+Write direkt nach Projektordner erfolgreich
- Marktampel weiterhin GRUEN: S&P 500 7.165,08 (+0,80%) und Nasdaq 24.836,60 (+1,63%) -- beide neue Rekorde am 24. Apr
- VRT als Top-Pick bestaetigt: $303,90 nach Q1-Beat, FY-Guidance erhoeht, Earnings-Risiko bis ~Juli vorbei
- FIX Q1-Beat sehr stark: ATH $1.829 am 24. Apr, jetzt Konsolidierung bei $1.715, Backlog $12,45B
- FN auf neuem 52W-Hoch $720,19 am 24. Apr (+4,5%) -- Cup-Handle voll bestaetigt
- STRL bei $497 nahe ATH $504 -- Double Bottom intakt
- ECG bei $132,89 -- Cup-Pattern, FFTY #2 Holding
- Korrekte Earnings-Warnungen platziert (FN 11. Mai, STRL 4. Mai)

### Probleme
- Hormuz-Blockade-Eskalation am 27. Apr koennte Volatilitaet ausloesen -- Marktampel im Auge behalten
- Big-Tech-Earnings (MSFT, GOOGL, AMZN, META Mi / AAPL Do) koennten Volatilitaet erhoehen
- RHM bei EUR 1.317-1.405 weiter unter Threshold EUR 1.450 -- EU-Pool bleibt leer
- ASML EPS-Surprise nur +8,4%, EPS-Wachstum unter C-Schwelle -- nicht aufgenommen
- FN GF-Value-Bewertung 125,6% ueber Fair Value (P/E 69x) -- Bewertungsrisiko vor Earnings hoch

### Verbesserungen fuer naechsten Lauf

1. **MARKTAMPEL-MONITORING (KRITISCH):**
   - S&P 500 7.165 ATH, klar ueber MAs -- bleibt GRUEN solange S&P ueber 6.950
   - Aber: Hormuz-Blockade aktiviert, Brent ~$100 -- bei weiterer Eskalation und Bruch unter 7.000 zurueck auf GELB
   - University of Michigan Consumer Sentiment 49,8 (NIEDRIGSTER Wert seit 1952) -- Stagflations-Risiko
   - Bei Big-Tech-Earnings-Misses Mi/Do koennte Markt schnell drehen

2. **Slack-Formatierung (bewaehrt, beibehalten):**
   - Nur ASCII, keine Emojis, kein EUR-Zeichen
   - Umlaute als ae/oe/ue
   - Punkt-Tausender und Komma-Dezimal fuer DACH-Style
   - Nachricht unter 3.500 Zeichen (Lauf 15: ~3.250)

3. **Datenquellen (funktionierend):**
   - finance.yahoo.com, marketbeat.com, cnbc.com, fool.com, thestreet.com
   - investing.com, tradingview.com fuer Kurse
   - stocktitan.net, prnewswire.com fuer Earnings
   - econcurrents.substack.com fuer Marktzusammenfassungen
   - BLOCKIERT: swingtradebot.com, stockanalysis.com, nasdaq.com (intermittent)

4. **Kandidatenpool fuer naechsten Lauf:**
   - VRT als #1 bestaetigt nach Q1-Beat -- bis Juli kein Earnings-Risiko
   - FIX als #2 bestaetigt nach Q1-Beat -- Backlog-Wachstum prominent
   - FN als #3 -- WARNUNG: Earnings 11. Mai (in 2 Wochen ab Folge-Lauf eventuell verschoben)
   - STRL als #4 -- WARNUNG: Earnings 4. Mai (in 1 Woche!) -- bei Folge-Lauf am 28.04. nur 6 Tage entfernt
   - ECG als #5 -- Earnings 19. Mai (3 Wochen)
   - MOD (Modine), POWL (Powell) als Watchlist halten
   - RHM weiter ausgeschlossen bei EUR <1.450

5. **Post-Earnings-Strategie (NEU):**
   - VRT, FIX haben Earnings hinter sich -- GREEN-Signale
   - STRL Earnings am 4. Mai (a.h.) -- vor Lauf am 4. Mai noch keine Zahlen, am 5. Mai einarbeiten
   - FN Earnings am 11. Mai -- bei Folge-Laeufen Position verkleinern bis Ergebnis bekannt
   - Bei Earnings-Misses sofort durch Watchlist-Kandidat (MOD, POWL) ersetzen

6. **EU-Pool (kritisch leer):**
   - RHM Trend weiter abwaerts -- bei Erholung ueber EUR 1.450 wieder aufnehmen
   - ASML nicht qualifiziert (EPS-Wachstum nur +8%)
   - SAP, Novo Nordisk fuer naechsten Lauf erneut pruefen
   - Alternativ Top 5 ausschliesslich aus US-Markt -- ist OK gemaess SKILL.md

7. **JSON-Export funktioniert reliable:**
   - Read+Write direkt nach C:\Users\andyg\Documents\Claude\Projects\Taegliche CANSLIM Analyse\canslim-picks.json
   - 4 Picks (VRT, FIX, FN, STRL), VRT+FIX GREEN, FN+STRL YELLOW

8. **Geo-politische Risiken (NEU prominent):**
   - Hormuz-Blockade aktiv ab 27. Apr -- Oel-Preise ueber $100
   - Iran-Talks gestockt
   - Naechster Lauf: pruefen ob Markt noch GRUEN -- bei Bruch unter 7.000 sofort GELB


## Lauf 14 -- 24. April 2026

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt (3.150 Zeichen)
- JSON-Export mit Write direkt nach Projektordner erfolgreich nach Read
- Marktampel GRUEN beibehalten trotz leichtem Pullback: S&P 500 bei 7.108,40 (-0.41%), Nasdaq bei 24.438,50 (-0.89%)
- VRT Q1 Earnings 22. Apr: STARKER BEAT -- EPS $1.17 (Beat +$0.16), +136% GAAP EPS, +83% adj, FY-Guidance auf $6.30-$6.40 angehoben (ueber Konsens $6.16). Als Top-Pick bestaetigt
- FIX Q1 Earnings 23. Apr (a.h.): EXPLOSIVER BEAT -- Umsatz +56.5% auf $2.87B, GAAP-EPS $10.51 (+54% ueber Konsens). +9.3% intraday auf $1.724, nachboerslich $1.854. Flat-Base-Breakout vollstaendig bestaetigt
- FN weiter bei $690 nahe ATH, Cup-Breakout intakt
- STRL bei $498 nahe 52W-Hoch $504, KeyBanc startet Coverage OW mit PT $572
- ECG (Everus Construction) als Ersatz fuer RHM aufgenommen: $137, Q4 EPS +61%, FFTY Top-3 Holding
- RHM korrekt entfernt: EUR ~1.400 unter Threshold EUR 1.450, -10% in 7 Tagen, Abwaertstrend

### Probleme
- RHM fundamentale Story intakt (Backlog EUR 135B), aber technisch komplett versagt -- keine adequate EU-Alternative gefunden
- VRT nach Beat zunaechst -2.5%, dann +3.3% intraday -- volatile Reaktion trotz starker Zahlen
- Einige Investoren erwarteten hoehere Revenue-Zahlen trotz +30% Wachstum -- hohe Erwartungen bei Vertiv
- Iran-Krieg-Sorgen treiben erneut Marktvolatilitaet (Oelpreise hoch)
- Chartmuster-Validierung weiter auf Preisbewegung basiert

### Verbesserungen fuer naechsten Lauf

1. **MARKTAMPEL GRUEN (weiterhin):**
   - S&P 500 bei 7.108 nach Pullback von ~7.160 ATH
   - Bleibt GRUEN solange S&P ueber 6.950
   - Iran-Sorgen beobachten -- bei Eskalation und Break unter 200-Tage-MA zurueck auf GELB/ROT
   - Nasdaq -0.89% staerker gefallen -- Tech-Schwaeche im Auge behalten

2. **Slack-Formatierung (bewaehrt):**
   - Keine Emojis, kein EUR-Zeichen, keine Unicode-Sonderzeichen
   - Umlaute als ae/oe/ue
   - Nachricht unter 3.500 Zeichen (aktuell ~3.150)

3. **Datenquellen (funktionierend):**
   - finance.yahoo.com, marketbeat.com, cnbc.com, seekingalpha.com, fool.com
   - thestreet.com fuer Marktzusammenfassungen
   - investing.com fuer historische Daten
   - stocktitan.net, prnewswire.com fuer Earnings-Pressemitteilungen
   - tradingkey.com, indexbox.io fuer Preisbewegungen
   - simplywall.st, chartmill.com, trefis.com fuer Analysen
   - BLOCKIERT: swingtradebot.com, stockanalysis.com, nasdaq.com

4. **Kandidatenpool fuer naechsten Lauf:**
   - VRT als #1 bestaetigt nach Q1-Beat -- Guidance-Erhoehung, nun Earnings bis ~Juli raus
   - FIX auf #2 hochgestuft -- Q1-Beat mit Flat-Base-Breakout, keine naechsten Earnings bis ~Juli
   - FN als #3 beibehalten -- Cup-Pattern, Earnings ~11. Mai (WARNUNG in 2 Wochen)
   - STRL als #4 beibehalten -- Double Bottom intakt, Earnings Anfang Mai (WARNUNG)
   - ECG als #5 neu aufgenommen -- Cup-Pattern, $137, FFTY Top-3. Earnings Anfang Mai (WARNUNG)
   - RHM vorerst entfernt (EUR 1.400, Abwaertstrend). Bei Erholung ueber EUR 1.450 wieder aufnehmen
   - MOD (Modine), POWL weiter als Watchlist

5. **Post-Earnings-Positioning (KRITISCH fuer naechsten Lauf):**
   - VRT und FIX haben Earnings hinter sich -- nun Signale auf GREEN
   - FN, STRL, ECG Earnings Anfang Mai -- YELLOW-Signale
   - Bei allen May-Earnings: genaue Daten in naechstem Lauf verifizieren

6. **JSON-Export erfolgreich:**
   - Write nach Read hat direkt geklappt in Projektordner
   - Pfad: C:\Users\andyg\Documents\Claude\Projects\Taegliche CANSLIM Analyse\canslim-picks.json
   - 4 Picks (ohne ECG) im JSON, VRT+FIX auf GREEN, FN+STRL auf YELLOW

7. **EU-Markt:**
   - RHM komplett im Abwaertstrend, keine technische Einstiegschance
   - Beim naechsten Lauf ASML, SAP, Novo Nordisk als Kandidaten pruefen
   - Alternativ EU-Anteil temporaer auf 0 setzen bis Kandidaten staerker werden


## Lauf 13 -- 17. April 2026

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt
- Marktampel GRUEN beibehalten: S&P 500 bei ~7.041 (16. Apr Close), intraday ~7.078 am 17. Apr
- Nasdaq bei 24.102, 12-Tage-Gewinnserie (laengste seit 2009) -- extrem bullish
- Alle 5 Kern-Picks beibehalten: FN, VRT, STRL, FIX, RHM
- FN weiterhin bei ~$686, nahe ATH $708 -- Cup with Handle Breakout intakt
- VRT bei ~$301, leichter Ruecksetzer vom ATH $312 -- gesund vor Earnings
- STRL bei ~$441, Ruecksetzer vom 52W-Hoch $477 -- bietet Einstiegsgelegenheit
- FIX bei ~$1.614, nahe ATH $1.672 -- Flat Base intakt, PT auf $1.819 erhoeht
- RHM bei EUR 1.497 -- leichte Erholung, Cup-Formation intakt
- Earnings-Warnungen fuer VRT (22. Apr) und FIX (29. Apr) prominent platziert
- Everus Construction (ECG) als neuen FFTY-Top-Holding identifiziert (3.67%)

### Probleme
- Stock Weather JSON-Export gescheitert: User hat Ordner-Freigabe abgelehnt
- STRL Ruecksetzer auf $441 -- unter Double Bottom Buy-Point $450, technisch leicht schwaecher
- RHM weiterhin deutlich unter ATH (EUR 1.497 vs EUR 2.008)
- Keine exakten RS-Ratings (IBD Paywall)
- Chartmuster-Validierung weiter auf Preisbewegung basiert, nicht auf echten OHLC-Daten

### Verbesserungen fuer naechsten Lauf

1. **MARKTAMPEL GRUEN (weiterhin):**
   - S&P 500 bei ~7.041-7.078, neue ATHs
   - Nasdaq 12-Tage-Gewinnserie
   - 50-Tage-MA klar ueber 200-Tage-MA
   - Ampel bleibt GRUEN solange S&P ueber 6.950
   - Bei Rueckfall unter 200-Tage-MA (~6.700): zurueck auf GELB

2. **Slack-Formatierung (bewaehrt, beibehalten):**
   - Keine Emojis, kein EUR-Zeichen, keine Unicode-Sonderzeichen
   - Umlaute als ae/oe/ue
   - Nachricht unter 3500 Zeichen
   - Nur ASCII-Zeichen verwenden

3. **Datenquellen (funktionierend):**
   - finance.yahoo.com, marketbeat.com, cnbc.com, seekingalpha.com, fool.com
   - finviz.com und gurufocus.com fuer US-Kursdaten
   - tradingeconomics.com und investing.com fuer EU
   - stocktitan.net fuer Earnings-Pressemitteilungen
   - BLOCKIERT: swingtradebot.com, stockanalysis.com, nasdaq.com

4. **Kandidatenpool fuer naechsten Lauf:**
   - FN beibehalten als #1 -- AI-Optik-Story intakt, Earnings ~11. Mai
   - VRT: EARNINGS 22. APRIL (DIENSTAG)! Sofort nach Ergebnis bewerten. Bei Beat + Guidance: bestaetigen. Bei Miss: durch MOD oder ECG ersetzen
   - STRL beibehalten -- Ruecksetzer auf $441 bietet Einstieg, Earnings Anfang Mai
   - FIX: EARNINGS 29. APRIL! Nach Ergebnis neu bewerten
   - RHM beibehalten falls ueber EUR 1.450. Earnings 7. Mai
   - ECG (Everus Construction): FFTY #2 Holding (3.67%), Q4 Revenue +33%, FY25 +31.5%, Backlog $3.23B -- starker Kandidat als Ersatz
   - MOD (Modine): ~$238, Data-Center +78% YoY, FFTY Holding -- Watchlist
   - POWL (Powell Industries): Nach 3:1 Split bei ~$229, Backlog $1.6B -- Watchlist

5. **Stock Weather JSON-Export:**
   - User hat Ordner-Freigabe abgelehnt -- beim naechsten Lauf erneut versuchen mit request_cowork_directory
   - Alternativ: Datei in Taegliche CANSLIM Analyse Ordner schreiben als Backup

6. **Earnings-Saison Beachtung (KRITISCH):**
   - VRT Earnings 22. Apr -- DIENSTAG! Wichtigster Katalysator diese Woche
   - FIX Earnings 29. Apr -- naechste Woche
   - FN Earnings ~11. Mai
   - STRL Earnings Anfang Mai
   - RHM Earnings 7. Mai
   - Bei Earnings innerhalb 2 Wochen: explizite Warnung im Bericht

7. **Post-Earnings-Bewertung (naechster Lauf 21. April -- Montag):**
   - VRT Q1 Earnings am 22. Apr (Dienstag): Am Montag letzte Warnung, am Mittwoch Ergebnis einarbeiten
   - Bei VRT Beat + Guidance-Erhoehung: Signal GRUEN, Kern-Pick bestaetigen
   - Bei VRT Miss: sofort durch ECG oder MOD ersetzen
   - FIX Earnings 29. Apr: Warnung beibehalten


## Lauf 12 -- 16. April 2026

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt
- Marktampel von GELB auf GRUEN hochgestuft -- S&P 500 Rekordschluss 7.022,95 am 15. Apr (+0,80%)
- Nasdaq ebenfalls auf ATH -- Iran-Waffenstillstand-Rally plus Bank-Earnings-Beats (BAC, MS)
- Death Cross aufgeloest: 50-Tage-MA hat 200-Tage-MA endgueltig zurueckerobert
- Alle 5 Kern-Picks beibehalten: FN, VRT, STRL, FIX, RHM
- FN bei $686 (neues ATH $700 intraday) -- Cup with Handle Breakout ueber $679 vollstaendig bestaetigt
- VRT bei $301 neues ATH -- Cup with Handle Breakout intakt, aber Earnings-Warnung 22. Apr prominent platziert
- STRL bei $468 -- Double Bottom Buy-Point bei $450 getriggert, naehert sich 52W-Hoch $477
- FIX bei $1.635 neues ATH -- Flat Base Breakout ueber $1.614 bestaetigt, Earnings-Warnung 29. Apr platziert
- RHM bei EUR 1.519 -- leichte Erholung von EUR 1.486, Cup-Formation intakt
- Stock Weather JSON-Export erfolgreich in Windows-Ordner geschrieben nach request_cowork_directory
- WICHTIGE LEKTION: Der Stock Weather Ordner war nicht in der Cowork-Session gemountet. Mit dem Tool mcp__cowork__request_cowork_directory und dem Pfad "C:\Users\andyg\Documents\Claude\Projects\Stock Weather" kann der Ordner mit einem User-Klick freigegeben werden. Danach funktionieren Read/Write/Edit direkt auf diesem Ordner

### Probleme
- Write-Tool scheiterte zunaechst mit "File has not been read yet" bei neuem Dateipfad -- erst Read, dann Write verwenden
- RHM technisch weiterhin schwaecher als US-Picks (24% unter ATH EUR 2.008)
- MOD (Modine) waere technisch staerker als RHM aber EU-Diversitaet verloren
- POWL nach 3-fuer-1 Split bei $229 -- interessant, aber noch nicht im Top-5-Pool (Monitoring)
- NBIS negative EPS -- erfuellt CANSLIM-C-Kriterium nicht trotz starkem Momentum
- Chartmuster-Validierung weiter auf Preisbewegung/Beschreibung basiert, nicht auf echten OHLC-Daten
- Keine exakten IBD RS-Ratings (Paywall) -- 52W-Performance als Proxy

### Verbesserungen fuer naechsten Lauf

1. **MARKTAMPEL GRUEN (aktuell):**
   - S&P 500 bei 7.022,95 am 15. Apr 2026 -- neues ATH
   - 50-Tage-MA ueber 200-Tage-MA wieder
   - Iran-Waffenstillstand bleibt wichtigster Katalysator
   - Ampel auf GRUEN bleibt, solange S&P ueber 6.950 (50-Tage-MA-Bereich)
   - Bei Rueckfall unter 200-Tage-MA (~6.700): zurueck auf GELB

2. **Slack-Formatierung (bewaehrt, beibehalten):**
   - Keine Emojis, kein EUR-Zeichen, keine Unicode-Sonderzeichen
   - Umlaute als ae/oe/ue
   - Nachricht unter 3500 Zeichen
   - Nur ASCII-Zeichen verwenden
   - Trennzeichen: Leerzeilen statt ---
   - WARNUNG-Hinweise fuer Earnings-Termine innerhalb 2 Wochen

3. **Datenquellen (funktionierend):**
   - finance.yahoo.com, marketbeat.com, cnbc.com, seekingalpha.com, fool.com
   - thestreet.com fuer Marktzusammenfassungen
   - finviz.com fuer US-Kursdaten
   - tradingeconomics.com fuer EU-Aktien
   - stocktitan.net fuer Earnings-Pressemitteilungen
   - gurufocus.com fuer aktuelle Kursverifikation
   - BLOCKIERT: swingtradebot.com, stockanalysis.com, nasdaq.com

4. **Kandidatenpool fuer naechsten Lauf:**
   - FN beibehalten als #1 -- am neuen ATH, Earnings ~11. Mai
   - VRT: NACH Earnings 22. Apr neu bewerten\! Bei Beat + Guidance-Erhoehung: Kern-Pick bestaetigen. Bei Miss: durch POWL oder MOD ersetzen
   - STRL beibehalten -- fundamentaler Datencenter-Boom intakt, Earnings Anfang Mai
   - FIX: Earnings 29. Apr -- nach Ergebnis neu bewerten
   - RHM beibehalten falls ueber EUR 1.500. Falls unter 1.450: durch MOD ersetzen
   - MOD (Modine): Q3 FY26 EPS +29% YoY adjustiert, $238, Data-Center +78% YoY, FFTY Holding
   - POWL (Powell Industries): Nach 3:1 Split bei $229, Backlog $1.6B, Data-Center-Exposure -- Watchlist
   - AVGO: starke AI-Revenue-Wachstum, EPS-Beat historisch unter C-Schwelle pruefen
   - APP (AppLovin): Umsatzwachstum +51% Q1, aber $745 ATH, Volatilitaet hoch -- pruefen
   - NBIS ausgeschlossen: Negative EPS, erfuellt C nicht

5. **Preisverifikation:**
   - Mindestens 2 Quellen pro Kurs (Schlusskurs verwenden)
   - finviz.com und gurufocus.com als primaere US-Quellen
   - tradingeconomics.com und investing.com fuer EU
   - S&P 500 Preis IMMER doppelt pruefen (aktuell 7.022,95)

6. **Earnings-Saison Beachtung:**
   - VRT Earnings 22. Apr -- NAECHSTE WOCHE\! Position vorher verkleinern
   - FIX Earnings 29. Apr -- vor Zahlen Position verkleinern
   - FN Earnings ~11. Mai
   - STRL Earnings Anfang Mai
   - RHM Earnings 7. Mai
   - APP Earnings 6. Mai
   - NBIS Earnings 29. Apr
   - Bei Earnings innerhalb 2 Wochen: explizite Warnung im Bericht

7. **Stock Weather JSON-Export (GELOEST):**
   - Zu Beginn jedes Laufs: mcp__cowork__request_cowork_directory mit Pfad "C:\Users\andyg\Documents\Claude\Projects\Stock Weather" aufrufen -- User bestaetigt mit einem Klick
   - Danach: Read gefolgt von Write auf C:\Users\andyg\Documents\Claude\Projects\Stock Weather\canslim-picks.json
   - Datei wird direkt im Windows-Ordner ueberschrieben und vom Dashboard geladen

8. **Post-Earnings-Bewertung (naechste Woche):**
   - VRT Q1 22. Apr: Wichtigster Katalysator -- bei Beat + Guidance: Signal GRUEN, bei Miss: sofort ersetzen
   - NBIS Q1 29. Apr: Auf Weg zur Profitabilitaet beobachten
   - FIX Q1 29. Apr: Record Backlog sollte Ergebnis stuetzen
   - Iran-Deal-Entwicklung weiter entscheidend fuer Marktampel


## Lauf 11 -- 15. April 2026

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt
- Marktampel GELB korrekt: S&P 500 bei 6.967 (nahe ATH), ueber beiden MAs, aber Death Cross technisch noch aktiv
- Alle 5 Kern-Picks beibehalten: FN, VRT, STRL, FIX, RHM -- alle Fundamentaldaten weiterhin stark
- FN auf Platz 1 hochgestuft -- am 52W-Hoch bei $679, FFTY #1 Holding, Cup Breakout bestaetigt
- VRT neues ATH bei $312 am 14. Apr -- starker Trend, Cup with Handle Breakout voll bestaetigt
- STRL bei $469, nahe 52W-Hoch $477 -- Double Bottom These intakt, +260% in 52W
- FIX bei $1.574, nahe ATH $1.614 -- Flat Base stabil, Rekord-Backlog $11.9B
- RHM bei EUR 1.486 -- fundamentaler Katalysator (Backlog EUR 135B) weiterhin extrem stark
- S&P 500 Preis korrekt aus Quelle uebernommen (6.967 vs. vorherige Tippfehler)
- ASML Q1 Earnings heute bewertet: starke Ergebnisse aber EPS +10% unter C-Schwelle -- korrekt nicht aufgenommen
- Earnings-Warnungen fuer VRT (22. Apr) und FIX (29. Apr) prominent platziert
- Marktampel von ROT auf GELB korrigiert -- S&P jetzt ueber beiden MAs, nahe ATH

### Probleme
- Chartmuster-Validierung weiterhin auf Preisbewegung/Beschreibung basiert, nicht auf echten Chartdaten
- Keine exakten RS-Ratings (IBD Paywall) -- 52W-Performance und FFTY-Ranking als Proxy
- Distribution Day Count weiterhin nicht ermittelbar
- RHM weiterhin deutlich unter ATH (EUR 1.486 vs EUR 2.008) -- technisch schwaecher als US-Picks
- swingtradebot.com weiterhin blockiert
- Keine neuen EU-Kandidaten gefunden die staerker als RHM sind (ASML EPS-Wachstum zu niedrig)
- Stock Weather Ordner nicht gefunden -- JSON-Export uebersprungen

### Verbesserungen fuer naechsten Lauf

1. **Slack-Formatierung (bewaehrt, beibehalten):**
   - Keine Emojis, kein EUR-Zeichen, keine Unicode-Sonderzeichen
   - Umlaute als ae/oe/ue
   - Nachricht unter 3500 Zeichen (Puffer lassen)
   - Nur ASCII-Zeichen verwenden
   - Trennzeichen: Leerzeilen statt ---

2. **MARKTAMPEL-UPDATE:**
   - S&P 500 bei 6.967 -- ueber 50-Tage (6.710) und 200-Tage (6.661)
   - Death Cross von Ende Maerz: 50-Tage unter 200-Tage -- aber jetzt 50-Tage bei 6.710 vs 200-Tage 6.661, also knapp darueber
   - Falls S&P weiter steigt und 50-Tage-MA sich weiter von 200-Tage-MA entfernt: Ampel auf GRUEN
   - Falls S&P unter 200-Tage-MA faellt: zurueck auf ROT

3. **Datenquellen (funktionierend):**
   - finance.yahoo.com, marketbeat.com, cnbc.com, seekingalpha.com, fool.com
   - chartmill.com fuer technische Bewertungen
   - finviz.com fuer US-Kursdaten
   - tradingeconomics.com fuer EU-Aktien
   - barchart.com fuer Marktbreite-Daten
   - macrotrends.net fuer historische Kursdaten
   - investing.com fuer technische Analyse (MA-Daten)
   - stocktitan.net fuer Earnings-Pressemitteilungen
   - gurufocus.com fuer aktuelle Kursverifikation
   - BLOCKIERT: swingtradebot.com, stockanalysis.com, nasdaq.com

4. **Kandidatenpool fuer naechsten Lauf:**
   - FN beibehalten als #1 -- AI-Optik-Story intakt, am 52W-Hoch, Earnings ~11. Mai
   - VRT: NACH Earnings (22. Apr) neu bewerten! Bei Beat + Guidance-Erhoehung: Kern-Pick bestaetigen. Bei Miss: sofort ersetzen
   - STRL beibehalten -- fundamentaler Datencenter-Boom intakt, Earnings Anfang Mai
   - FIX: Earnings 29. Apr -- nach Ergebnis neu bewerten
   - RHM beibehalten falls ueber EUR 1.500. Falls unter 1.450: durch Modine (MOD) ersetzen
   - MOD (Modine Manufacturing) als Alternative: FFTY Holding (3.56%), +223% in 52W, Data Center Growth, ~$241
   - Broadcom (AVGO) pruefen: starke AI-Revenue-Wachstum, aber EPS-Beat historisch unter C-Schwelle
   - ASML nach Q1 Earnings-Reaktion beobachten (starke Guidance, EPS aber unter 25% Wachstum)

5. **Preisverifikation:**
   - Mindestens 2 Quellen pro Kurs (Schlusskurs verwenden)
   - finviz.com und gurufocus.com als primaere US-Quellen
   - tradingeconomics.com fuer EU
   - S&P 500 Preis IMMER doppelt pruefen!

6. **Markt-Strategie (aktualisiert):**
   - S&P unter 200-Tage-Linie + Death Cross: Ampel ROT, Watchlist-Modus
   - S&P auf/nahe 200-Tage-Linie: Ampel GELB, halbe Positionen
   - S&P ueber 50-Tage-Linie UND 50-Tage ueber 200-Tage: Ampel GRUEN, volle Positionen
   - Aktuell GELB -- Preis ueber beiden MAs, aber 50/200-Tage sehr eng beieinander

7. **Earnings-Saison Beachtung (aktualisiert):**
   - VRT Earnings 22. Apr -- DIESE WOCHE! Position vorher verkleinern oder warten
   - FIX Earnings 29. Apr -- NAECHSTE WOCHE! Position vorher verkleinern oder warten
   - FN Earnings ~11. Mai
   - STRL Earnings Anfang Mai
   - RHM Earnings 7. Mai
   - Bei Earnings innerhalb 2 Wochen: explizite Warnung im Bericht

8. **Post-Earnings-Bewertung (diese Woche):**
   - ASML Q1 Ergebnis heute: EUR 8.8B Revenue, EUR 2.8B Net Income, Guidance erhoeht auf EUR 36-40B -- positiv fuer Halbleiter-Sentiment
   - VRT Earnings 22. Apr: Wichtigster Katalysator -- bei Beat koennte Ampel fuer VRT auf GRUEN, bei Miss sofort ersetzen
   - FIX Earnings 29. Apr: Record Backlog sollte Ergebnis stuetzen
   - Iran-Deal-Optimismus koennte Marktampel bald auf GRUEN bringen falls 50-Tage-MA weiter steigt

## Lauf 10 -- 13. April 2026

### Was gut lief
- Slack-Nachricht beim ersten Versuch erfolgreich gesendet -- ASCII-only Formatierung bewaehrt
- Marktampel ROT klar kommuniziert: Death Cross weiterhin aktiv, S&P ~6.582 unter beiden MAs
- Alle 5 Kern-Picks beibehalten: VRT, STRL, FIX, FN, RHM
- VRT starker Breakout auf $295, neues ATH -- Cup with Handle Breakout ueber $276 bestaetigt
- FN weiterer Anstieg auf $662 (+7,1% am 10. Apr), nahe 52W-Hoch $679 -- Cup These staerker
- STRL Erholung auf $447, Double Bottom intakt
- FIX nahe ATH bei $1.575 ($1.602 Hoch) -- Flat Base unter 5% Korrektur
- RHM bei EUR 1.464 weiterhin schwaecher, -5,6% am 10. Apr -- fundamentaler Katalysator (Backlog-Verdopplung) aber weiterhin extrem stark
- Earnings-Warnungen fuer VRT (22. Apr) und FIX (29. Apr) prominent platziert
- Iran-Waffenstillstand als Marktkatalysator erwaehnt
- Stock Weather Ordner nicht gefunden -- JSON-Export korrekt uebersprungen

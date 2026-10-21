# Datenvertrag `canslim-picks.json`

Diese Datei ist die **einzige Schnittstelle** zwischen der taeglichen
CANSLIM-Analyse und dem Stock-Weather-Dashboard. Wer eines der drei
Projekte anfasst, haelt sich an dieses Dokument.

```
  canslim_new                CANSLIM-picks               dashboard_new
  (Analyse-Routine)   ---->  (dieses Repo)      ---->    (Anzeige)
  schreibt + pusht           haelt den Stand             holt per raw.githubusercontent
```

Formal beschrieben in `canslim-picks.schema.json` (JSON Schema Draft-07).
Die CI dieses Repos validiert jeden Push dagegen — ein Lauf, der das Schema
verletzt, faellt sofort auf und nicht erst als leeres Widget.

## Warum das existiert

Das Format war nirgends festgeschrieben. Producer und Consumer sind
auseinandergelaufen: die Routine lieferte `company`/`status`/`setup`/
`buy_trigger` und eine deutsche Marktampel (`GRUEN`), das Dashboard las
`name`/`price`/`signal` und kannte nur `GREEN`. Ergebnis: graue Ampel,
keine Firmennamen, dauerhaft rotes M-Kriterium und die komplette
Analyse (Setup, Kauf-Trigger, Watchlist) unsichtbar. Niemand hat es
gemerkt, weil nichts geprueft wurde.

## Aufbau

```json
{
  "updated": "2026-08-17",
  "run": 95,
  "market_signal": "GRUEN",
  "market_summary": "Ein Satz zur Marktlage ...",
  "picks_summary": "Ein Satz zur Auswahl ...",
  "market_note": "Begruendung der Marktampel ...",
  "picks_note": "Einordnung der Auswahl insgesamt ...",
  "picks":       [ /* Eintraege, max. 8 */ ],
  "watchlist":   [ /* Eintraege, max. 8 */ ],
  "filtered_out": [ "EARNINGS-REGEL (Bericht innerhalb 14 Tagen): HEI (25.08.) ..." ]
}
```

### Kopffelder

| Feld | Pflicht | Bedeutung im Dashboard |
|---|---|---|
| `updated` | ja | `JJJJ-MM-TT`. Steht im Footer. Aelter als **4 Tage** → gelbe Warnpille „veraltet“. |
| `run` | nein | Lauf-Nummer, Footer. |
| `market_signal` | ja | Ampelpille oben rechts **und** das M-Kriterium jeder Karte. `GRUEN`/`GELB`/`ROT` (deutsch bevorzugt), englische Werte weiter erlaubt. |
| `market_summary` | empfohlen | **Ein Satz** (Ziel ≤ 140 Zeichen), steht im Widget-Kopf. Fehlt er, nimmt das Dashboard den `FAZIT:`-Abschnitt bzw. den ersten Satz von `market_note`. |
| `picks_summary` | empfohlen | **Ein Satz** (Ziel ≤ 140 Zeichen), zweite Zeile im Kopf. |
| `market_note` | nein | Langtext, eingeklappt unter „Marktlage & Auswahl“. |
| `picks_note` | nein | Langtext, ebenfalls dort. |
| `filtered_out` | nein | Eingeklappter Block „Aussortiert (N)“ am Ende. |

Die Langtexte (`market_note`, `picks_note`) zerlegt das Dashboard an Labels
in Grossbuchstaben mit Doppelpunkt (`FAZIT:`, `BSVN ENTFERNT:`,
`DATENHINWEIS:` — mindestens vier Zeichen) in Stichpunkte. Bei
`filtered_out` wird der Text vor dem ersten `: ` fett als Label gezeigt.

### Eintrag (`picks` und `watchlist`)

| Feld | Pflicht | Darstellung |
|---|---|---|
| `ticker` | ja | Grosse Mono-Schrift oben links |
| `company` | empfohlen | Zeile darunter |
| `sector` | empfohlen | Chip |
| `status` | empfohlen | farbiges Badge oben rechts — siehe unten |
| `canslim` | ja | **Hauptinhalt der Karte:** Liste mit sieben Zeilen (Buchstabe, Bedeutung, Text) — siehe unten |
| `earnings_date` | empfohlen | `JJJJ-MM-TT` des naechsten Quartalsberichts. Chip „Zahlen TT.MM. · in N T.“, gelb ab 14 Tagen vorher. Unbekannt → weglassen. |
| `setup` | empfohlen | eingeklappt unter „Details“, Block **SETUP** |
| `buy_trigger` | empfohlen | eingeklappt unter „Details“, Block **KAUF-TRIGGER** |
| `note` / `reason` | empfohlen | eingeklappt unter „Details“, Block **NOTIZ** bzw. **GRUND** |
| `price` | optional | Kurs oben rechts; fehlt er, bleibt das Feld leer statt „—“ |
| `pct_from_ath` | optional | Watchlist-Badge |

### `status` — Format `STUFE -- Fliesstext`

Das Dashboard wertet **nur den Teil vor `--`** aus. Erkannt werden:

| Stufe enthaelt | Badge | Farbe |
|---|---|---|
| `UEBERDEHNT`, `ZU WEIT GELAUFEN` | Überdehnt | rot |
| `KURZ VOR`, `VOR DEM AUSBRUCH`, `NAHE AM PIVOT` | Kurz vor Pivot | gelb |
| `AUSGEBROCH…`, `BREAKOUT ERFOLGT` | Ausgebrochen | gruen |
| `AM BREAKOUT`, `AM PIVOT`, `BREAKOUT-PUNKT` | Am Pivot | gruen |

Die Reihenfolge ist bewusst so: `KURZ VOR DEM AUSBRUCH` enthaelt selbst das
Wort *Ausbruch* und darf nicht als vollzogener Ausbruch gewertet werden.
Aus demselben Grund wird der Fliesstext hinter `--` ignoriert — dort steht
regelmaessig „(Ausbruch laeuft)“ o. ae.

### `canslim`

Alle sieben Buchstaben `C A N S L I M` muessen vorhanden sein. Je Buchstabe
**ein kurzer Satz, Ziel ≤ 80 Zeichen** — sichtbar ist eine Zeile, der Rest
erst nach Antippen (`validate_picks.py` warnt ab 120 Zeichen). Booleans
funktionieren weiterhin.

Einstufung (Farbe des Buchstabens):

| Text beginnt mit | Farbe | Angezeigt wird |
|---|---|---|
| — (kein Praefix) | gruen, erfuellt | der ganze Text |
| `SCHWACH -- ` oder `TEILWEISE -- ` | gelb | Text hinter `--` |
| `NICHT ERFUELLT -- ` | rot | Text hinter `--` |

`M` folgt immer der Marktampel (GRUEN gruen, GELB gelb, ROT rot).

Beispiel: `"S": "SCHWACH -- hohe Nettoverschuldung (12,9 Mrd. USD)"`

## Regeln fuer Aenderungen

1. **Feld umbenennen = Breaking Change.** Neues Feld additiv einfuehren, das
   alte weiterlesen — so wie es das Dashboard heute mit `name`/`company` tut.
2. **Schema zuerst.** Erst `canslim-picks.schema.json` anpassen, dann die
   Routine, dann das Dashboard.
3. **Nie ohne Validierung pushen.** `push_to_github.py` in `canslim_new`
   prueft Schema **und** Frische vor jedem Push und verweigert einen aelteren
   Stand, damit ein Leerlauf der Routine den guten Stand nicht ueberschreibt.
4. **Sprache:** Deutsch, ASCII-Umschrift (`ae/oe/ue`) wie im Slack-Bericht.

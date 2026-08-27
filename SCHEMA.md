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
| `market_note` | nein | Aufklappbarer Text unter dem Titel. |
| `picks_note` | nein | Zweite aufklappbare Zeile. |
| `filtered_out` | nein | Eigener Block „Aussortiert (N)“ am Ende. |

### Eintrag (`picks` und `watchlist`)

| Feld | Pflicht | Darstellung |
|---|---|---|
| `ticker` | ja | Grosse Mono-Schrift oben links |
| `company` | empfohlen | Zeile darunter |
| `sector` | empfohlen | Chip |
| `status` | empfohlen | farbiges Badge oben rechts — siehe unten |
| `setup` | empfohlen | Block **SETUP** (3 Zeilen, klickbar aufklappbar) |
| `buy_trigger` | empfohlen | Block **KAUF-TRIGGER** |
| `note` / `reason` | empfohlen | Block **NOTIZ** bzw. **GRUND** |
| `canslim` | ja | sieben Buchstaben-Chips, Volltext als Tooltip |
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

Alle sieben Buchstaben `C A N S L I M` muessen vorhanden sein. Bevorzugt je
ein erklaerender Satz (erscheint als Tooltip). Booleans funktionieren
weiterhin. Bei Text gelten `C`–`I` als erfuellt; `M` folgt der Marktampel.

## Regeln fuer Aenderungen

1. **Feld umbenennen = Breaking Change.** Neues Feld additiv einfuehren, das
   alte weiterlesen — so wie es das Dashboard heute mit `name`/`company` tut.
2. **Schema zuerst.** Erst `canslim-picks.schema.json` anpassen, dann die
   Routine, dann das Dashboard.
3. **Nie ohne Validierung pushen.** `push_to_github.py` in `canslim_new`
   prueft Schema **und** Frische vor jedem Push und verweigert einen aelteren
   Stand, damit ein Leerlauf der Routine den guten Stand nicht ueberschreibt.
4. **Sprache:** Deutsch, ASCII-Umschrift (`ae/oe/ue`) wie im Slack-Bericht.

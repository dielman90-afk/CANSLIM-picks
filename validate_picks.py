#!/usr/bin/env python3
"""
validate_picks.py

Prueft canslim-picks.json gegen den Datenvertrag (siehe SCHEMA.md).

Laeuft an zwei Stellen:
  * CI dieses Repos, nach jedem Push
  * push_to_github.py in `canslim_new`, VOR dem Push

Zwei Stufen:
  1. Strukturpruefung ohne Fremdbibliotheken (laeuft immer)
  2. zusaetzlich JSON-Schema, falls `jsonschema` installiert und
     canslim-picks.schema.json auffindbar ist

Verwendung:
    python3 validate_picks.py canslim-picks.json
    python3 validate_picks.py canslim-picks.json --min-datum 2026-08-17

Exit-Code 0 = in Ordnung, 1 = Vertragsverletzung.
"""

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

LETTERS = ["C", "A", "N", "S", "L", "I", "M"]
SIGNALE = {"GRUEN", "GRÜN", "GRUN", "GELB", "ROT", "GREEN", "YELLOW", "RED"}
DATUM = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# Stufen, die das Dashboard aus dem Teil vor "--" erkennt
STUFEN = re.compile(
    r"UEBERDEHNT|ÜBERDEHNT|ZU WEIT GELAUFEN"
    r"|KURZ (VOR|DAVOR)|VOR DEM AUSBRUCH|NAHE (AM|DEM) PIVOT"
    r"|AUSGEBROCH|BREAKOUT ERFOLGT|AUSBRUCH (VOLLZOGEN|BESTAETIGT|LAEUFT)"
    r"|AM (BREAKOUT|PIVOT|PUNKT|AUSBRUCHSPUNKT)|BREAKOUT-PUNKT"
)


def pruefe_eintrag(eintrag, wo, fehler, warnungen):
    if not isinstance(eintrag, dict):
        fehler.append(f"{wo}: ist kein Objekt")
        return

    ticker = eintrag.get("ticker")
    if not isinstance(ticker, str) or not ticker.strip():
        fehler.append(f"{wo}: `ticker` fehlt oder ist leer")
        return
    wo = f"{wo} ({ticker})"

    canslim = eintrag.get("canslim")
    if not isinstance(canslim, dict):
        fehler.append(f"{wo}: `canslim` fehlt oder ist kein Objekt")
    else:
        fehlend = [l for l in LETTERS if l not in canslim]
        if fehlend:
            fehler.append(f"{wo}: `canslim` ohne {', '.join(fehlend)}")
        for l in LETTERS:
            v = canslim.get(l)
            if l in canslim and not isinstance(v, (str, bool)):
                fehler.append(f"{wo}: canslim.{l} ist weder Text noch Boolean ({type(v).__name__})")
            elif isinstance(v, str) and not v.strip():
                fehler.append(f"{wo}: canslim.{l} ist leer")
        unbekannt = [k for k in canslim if k not in LETTERS]
        if unbekannt:
            warnungen.append(f"{wo}: unbekannte canslim-Schluessel {unbekannt} — werden nicht angezeigt")

    if not (eintrag.get("company") or eintrag.get("name")):
        warnungen.append(f"{wo}: weder `company` noch `name` — die Karte bleibt ohne Firmenname")
    if not eintrag.get("sector"):
        warnungen.append(f"{wo}: kein `sector` — kein Chip auf der Karte")

    status = eintrag.get("status")
    if status is not None:
        if not isinstance(status, str):
            fehler.append(f"{wo}: `status` ist kein Text")
        elif not STUFEN.search(status.split("--")[0].upper()):
            warnungen.append(
                f"{wo}: Stufe in `status` nicht erkannt "
                f"({status.split('--')[0].strip()!r}) — die Karte bekommt kein Badge. "
                "Erkannte Stufen siehe SCHEMA.md."
            )

    for feld in ("setup", "buy_trigger", "note", "reason", "company", "name", "sector"):
        if feld in eintrag and eintrag[feld] is not None and not isinstance(eintrag[feld], str):
            fehler.append(f"{wo}: `{feld}` ist kein Text")
    for feld in ("price", "pct_from_ath"):
        if feld in eintrag and eintrag[feld] is not None and not isinstance(eintrag[feld], (int, float)):
            fehler.append(f"{wo}: `{feld}` ist keine Zahl")


def pruefe(daten, min_datum=None):
    fehler, warnungen = [], []

    if not isinstance(daten, dict):
        return ["Wurzelelement ist kein Objekt"], []

    updated = daten.get("updated")
    if not isinstance(updated, str) or not DATUM.match(updated):
        fehler.append("`updated` fehlt oder ist nicht JJJJ-MM-TT")
    else:
        try:
            stand = datetime.strptime(updated, "%Y-%m-%d").date()
        except ValueError:
            fehler.append(f"`updated` ist kein gueltiges Datum: {updated}")
            stand = None
        if stand:
            if stand > date.today():
                fehler.append(f"`updated` liegt in der Zukunft: {updated}")
            if min_datum and stand < min_datum:
                fehler.append(
                    f"RUECKSCHRITT: `updated` {updated} ist aelter als der bereits "
                    f"veroeffentlichte Stand {min_datum.isoformat()}. Push wuerde gute "
                    "Daten mit alten ueberschreiben."
                )
            alter = (date.today() - stand).days
            if alter > 4:
                warnungen.append(f"Stand ist {alter} Tage alt — das Dashboard zeigt die Warnpille 'veraltet'")

    signal = daten.get("market_signal")
    if not isinstance(signal, str) or signal.strip().upper() not in SIGNALE:
        fehler.append(f"`market_signal` fehlt oder ist unbekannt: {signal!r} (erlaubt: {', '.join(sorted(SIGNALE))})")

    if "run" in daten and daten["run"] is not None and not isinstance(daten["run"], int):
        fehler.append("`run` ist keine Ganzzahl")
    for feld in ("market_note", "picks_note"):
        if feld in daten and daten[feld] is not None and not isinstance(daten[feld], str):
            fehler.append(f"`{feld}` ist kein Text")

    picks = daten.get("picks")
    watchlist = daten.get("watchlist")
    for name, wert in (("picks", picks), ("watchlist", watchlist)):
        if wert is not None and not isinstance(wert, list):
            fehler.append(f"`{name}` ist keine Liste")
        elif isinstance(wert, list):
            if len(wert) > 8:
                warnungen.append(f"`{name}` hat {len(wert)} Eintraege — das Dashboard zeigt nur die ersten 8")
            for i, e in enumerate(wert):
                pruefe_eintrag(e, f"{name}[{i}]", fehler, warnungen)

    if not (picks or watchlist):
        fehler.append("weder `picks` noch `watchlist` enthalten Eintraege — das Widget bliebe leer")

    fo = daten.get("filtered_out")
    if fo is not None and not isinstance(fo, list):
        fehler.append("`filtered_out` ist keine Liste")

    return fehler, warnungen


def pruefe_mit_schema(daten, schema_pfad):
    """Optionale Zusatzpruefung. Fehlt jsonschema oder die Datei, wird still uebersprungen."""
    try:
        import jsonschema
    except ImportError:
        return None
    if not schema_pfad or not Path(schema_pfad).is_file():
        return None
    schema = json.loads(Path(schema_pfad).read_text(encoding="utf-8"))
    validator = jsonschema.Draft7Validator(schema)
    return [
        f"{'/'.join(str(p) for p in e.absolute_path) or '(Wurzel)'}: {e.message}"
        for e in sorted(validator.iter_errors(daten), key=lambda e: list(e.absolute_path))
    ]


def main():
    ap = argparse.ArgumentParser(description="canslim-picks.json gegen den Datenvertrag pruefen")
    ap.add_argument("datei", nargs="?", default="canslim-picks.json")
    ap.add_argument("--schema", default=None, help="Pfad zu canslim-picks.schema.json (Standard: neben der Datei bzw. neben diesem Skript)")
    ap.add_argument("--min-datum", default=None, help="JJJJ-MM-TT: `updated` darf nicht aelter sein (Rueckschritt-Schutz)")
    ap.add_argument("--strict", action="store_true", help="Warnungen wie Fehler behandeln")
    args = ap.parse_args()

    pfad = Path(args.datei)
    if not pfad.is_file():
        print(f"FEHLER: {pfad} existiert nicht.")
        return 1
    try:
        daten = json.loads(pfad.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"FEHLER: {pfad} ist kein gueltiges JSON — {e}")
        return 1

    min_datum = None
    if args.min_datum:
        try:
            min_datum = datetime.strptime(args.min_datum, "%Y-%m-%d").date()
        except ValueError:
            print(f"FEHLER: --min-datum {args.min_datum!r} ist kein JJJJ-MM-TT-Datum.")
            return 1

    fehler, warnungen = pruefe(daten, min_datum)

    schema_pfad = args.schema
    if not schema_pfad:
        for kandidat in (pfad.parent / "canslim-picks.schema.json",
                         Path(__file__).parent / "canslim-picks.schema.json"):
            if kandidat.is_file():
                schema_pfad = kandidat
                break
    schema_fehler = pruefe_mit_schema(daten, schema_pfad)
    if schema_fehler:
        fehler.extend(f"Schema — {m}" for m in schema_fehler)

    print(f"Pruefe {pfad}  (Stand {daten.get('updated')}, Lauf {daten.get('run')}, "
          f"{len(daten.get('picks') or [])} Picks / {len(daten.get('watchlist') or [])} Watchlist)")
    if schema_fehler is None:
        print("  Hinweis: JSON-Schema-Pruefung uebersprungen (jsonschema oder Schemadatei nicht verfuegbar).")

    for w in warnungen:
        print(f"  WARNUNG: {w}")
    for f in fehler:
        print(f"  FEHLER:  {f}")

    if fehler:
        print(f"\nNICHT IN ORDNUNG — {len(fehler)} Fehler. Siehe SCHEMA.md.")
        return 1
    if warnungen and args.strict:
        print(f"\nNICHT IN ORDNUNG — {len(warnungen)} Warnungen (--strict).")
        return 1
    print(f"\nIn Ordnung{f' ({len(warnungen)} Warnungen)' if warnungen else ''}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

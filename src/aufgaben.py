"""Einfache Aufgabenverwaltung für die Kommandozeile."""

import argparse
import sys

from aufgaben_speicher import AufgabenFehler, AufgabenSpeicher


def positive_nummer(wert):
    try:
        nummer = int(wert)
    except ValueError:
        raise argparse.ArgumentTypeError("Die Aufgaben-ID muss eine positive ganze Zahl sein.")
    if nummer < 1:
        raise argparse.ArgumentTypeError("Die Aufgaben-ID muss eine positive ganze Zahl sein.")
    return nummer


def main(argv=None):
    parser = argparse.ArgumentParser(description="Aufgaben verwalten")
    befehle = parser.add_subparsers(dest="befehl", required=True)
    add = befehle.add_parser("add", help="Aufgabe hinzufügen")
    add.add_argument("titel", help="Titel der Aufgabe")
    befehle.add_parser("list", help="Aufgaben auflisten")
    done = befehle.add_parser("done", help="Aufgabe als erledigt markieren")
    done.add_argument("id", type=positive_nummer, help="ID der Aufgabe")
    args = parser.parse_args(argv)

    speicher = AufgabenSpeicher("data/aufgaben.json")
    try:
        if args.befehl == "add":
            aufgabe = speicher.hinzufuegen(args.titel)
            print(f"Aufgabe {aufgabe['id']} hinzugefügt: {aufgabe['titel']}")
        elif args.befehl == "list":
            aufgaben = speicher.laden()
            if not aufgaben:
                print("Keine Aufgaben vorhanden.")
            for aufgabe in aufgaben:
                status = "x" if aufgabe["erledigt"] else " "
                print(f"{aufgabe['id']}. [{status}] {aufgabe['titel']}")
        elif args.befehl == "done":
            aufgabe = speicher.erledigen(args.id)
            print(f"Aufgabe {aufgabe['id']} ist erledigt: {aufgabe['titel']}")
    except AufgabenFehler as fehler:
        print(f"Fehler: {fehler}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

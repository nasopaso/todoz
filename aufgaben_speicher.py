"""Speicherung und Verwaltung der Aufgaben."""

import json
from pathlib import Path


class AufgabenFehler(Exception):
    """Ein Fehler, der der Benutzerin oder dem Benutzer angezeigt werden kann."""


class AufgabenSpeicher:
    def __init__(self, datei):
        self.datei = Path(datei)

    def laden(self):
        try:
            with self.datei.open(encoding="utf-8") as datei:
                aufgaben = json.load(datei)
        except FileNotFoundError:
            return []
        except (json.JSONDecodeError, UnicodeError) as fehler:
            raise AufgabenFehler(f"Die Datendatei '{self.datei}' enthält kein gültiges JSON.") from fehler
        except OSError as fehler:
            raise AufgabenFehler(f"Die Datendatei '{self.datei}' konnte nicht gelesen werden: {fehler}") from fehler

        if not self._gueltig(aufgaben):
            raise AufgabenFehler(f"Die Datendatei '{self.datei}' enthält ungültige Aufgabendaten.")
        return aufgaben

    @staticmethod
    def _gueltig(aufgaben):
        if not isinstance(aufgaben, list):
            return False
        ids = set()
        for aufgabe in aufgaben:
            if not isinstance(aufgabe, dict):
                return False
            nummer = aufgabe.get("id")
            titel = aufgabe.get("titel")
            if (type(nummer) is not int or nummer < 1 or nummer in ids
                    or not isinstance(titel, str) or not titel.strip()
                    or not isinstance(aufgabe.get("erledigt"), bool)):
                return False
            ids.add(nummer)
        return True

    def speichern(self, aufgaben):
        try:
            with self.datei.open("w", encoding="utf-8") as datei:
                json.dump(aufgaben, datei, ensure_ascii=False, indent=2)
                datei.write("\n")
        except OSError as fehler:
            raise AufgabenFehler(f"Die Datendatei '{self.datei}' konnte nicht gespeichert werden: {fehler}") from fehler

    def hinzufuegen(self, titel):
        titel = titel.strip()
        if not titel:
            raise AufgabenFehler("Der Aufgabentitel darf nicht leer sein.")
        aufgaben = self.laden()
        nummer = max((aufgabe["id"] for aufgabe in aufgaben), default=0) + 1
        aufgabe = {"id": nummer, "titel": titel, "erledigt": False}
        aufgaben.append(aufgabe)
        self.speichern(aufgaben)
        return aufgabe

    def erledigen(self, nummer):
        aufgaben = self.laden()
        for aufgabe in aufgaben:
            if aufgabe["id"] == nummer:
                if not aufgabe["erledigt"]:
                    aufgabe["erledigt"] = True
                    self.speichern(aufgaben)
                return aufgabe
        raise AufgabenFehler(f"Aufgabe {nummer} existiert nicht.")

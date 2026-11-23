## Technsiche Anweisungen
- Python-Abhängigkeiten mit `uv` verwalten
- Tests mit `uv run pytest` ausführen.
- Bei Änderungen am Skill-Log auch `node --test .opencode/tests/skill-usage-log.test.js` ausführen. Das lokale Protokoll liegt in `.opencode/skill-usage.csv`.
- `data/aufgaben.json` enthält lokale Nutzerdaten; Tests müssen isolierte Daten verwenden.

## Dokumentations-Anweisungen
- Wenn Texte in `docs/` oder der `README.md` angelegt oder bearbeitet werden, müssen sie abschließend mit dem Humanizer-Skill auf natürliche, klare Sprache geprüft werden
- fachliche Aussagen und Vorlagen beibehalten.

## Frontmatter-Schema
- `title`: Titel der Notiz
- `tags`: Liste, lowercase, 5 Stück, ohne Umlaute (`ae`/`oe`/`ue`/`ss`), Bindestriche statt Leerzeichen.
- `created`: `YYYY-MM-DD`.
- `description`: Unter 200 Zeichen, Klartext ohne Markdown und Zeilenumbrüche, immer in `"..."` eingeschlossen


## Dateinamen
- Meeting-Notizen: `YYYY-MM-DD-meeting-<kurzbeschreibung>.md`.
- Alles andere: `<kurzbeschreibung>.md` ohne Datum, es sei denn, das Datum ist inhaltlich relevant.
- Nur Kleinbuchstaben, Bindestriche statt Leerzeichen, keine Umlaute (`ae`/`oe`/`ue`/`ss`).

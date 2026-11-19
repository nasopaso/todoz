# Hinweise für Agents

- Python-Abhängigkeiten mit `uv` verwalten
- Tests mit `uv run pytest` ausführen.
- Bei Änderungen am Skill-Log auch `node --test .opencode/tests/skill-usage-log.test.js` ausführen. Das lokale Protokoll liegt in `.opencode/skill-usage.csv`.
- `data/aufgaben.json` enthält lokale Nutzerdaten; Tests müssen isolierte Daten verwenden.
- Wenn Texte in `docs/` oder der `README.md` angelegt oder bearbeitet werden, müssen sie abschließend mit dem Humanizer-Skill auf natürliche, klare Sprache geprüft werden
- fachliche Aussagen und Vorlagen beibehalten.

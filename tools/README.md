# Generatore caroselli coolbio·360

- `data/*.json`: un oggetto per carosello (slug, vol, tag, accent, emoji, title max ~13 caratteri, single, sub, next, people con rank/h/score/emoji/cat/str/v e congrats sul No.1)
- `shots/<handle>.png`: screenshot ritagliato dell'intestazione del profilo (ritaglio con `crop.py`, sopra il pulsante Follow)
- Render: `DATA=data3.json python3 tools/gen.py [slug ...]` (Playwright + Chromium, font Google). Output in `tools/out/`, poi copiare in `posts/<slug>/`
- Calendario: `calendario_coolbio360.json` con `user_tags` (per immagine) e `collaboratori` (il No.1)

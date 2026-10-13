# Generatore caroselli coolbio·360

- `data/*.json`: un oggetto per carosello (slug, vol, tag, accent, emoji, title max ~13 caratteri, single, sub, next, people con rank/h/score/emoji/cat/str/v e congrats sul No.1)
- `shots/<handle>.png`: screenshot ritagliato dell'intestazione del profilo (ritaglio con `crop.py`, sopra il pulsante Follow)
- Render: `DATA=data3.json python3 tools/gen.py [slug ...]` (Playwright + Chromium, font Google). Output in `tools/out/`, poi copiare in `posts/<slug>/`
- Calendario: `calendario_coolbio360.json` con `user_tags` (per immagine) e `collaboratori` (il No.1)

## Regole di selezione profili (dal 13/10/2026, decise con Matteo)
1. **Attività (filtro, prima del punteggio):** ultimo post (esclusi i fissati) negli ultimi 30 giorni. Profili più fermi non entrano in lista. Controllo: data nell'og:description dei primi 12 post.
2. **Cool Score 10 punti:** Personality 3, Clarity 2, Call to action 2, Details 1, **Feed 2** (foto nitide e ben illuminate del proprio lavoro, griglia coerente, pubblicazione regolare).
3. Restano valide: profili pubblici professionali, sotto 600 follower, niente email o telefono personali in chiaro, niente refusi.

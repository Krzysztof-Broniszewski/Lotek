# Lotto 6/49 — Draw Simulator & Hit Checker (PL grammar)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nByh-cJusPUEpIv9X7p3EYXtEtwbkq6m?usp=sharing)  
**Direct link:** https://colab.research.google.com/drive/1nByh-cJusPUEpIv9X7p3EYXtEtwbkq6m?usp=sharing

A clean, dependency-free Python script that simulates a **6/49 lottery draw** (draws 6 unique numbers from 1..49), compares results against your picks, and prints correctly pluralized Polish output (_liczbę / liczby / liczb_). Optional `seed` enables reproducible draws.

---

## Features
- Draws **6 unique numbers** from **1..49** via `random.sample`.
- Compares against your set and shows the **hit count** and **hit values**.
- Correct Polish pluralization: _liczbę_, _liczby_, _liczb_.
- Optional `seed` for reproducible runs.
- Input validation (exactly 6 unique numbers in range 1..49).
- **Pure standard library**, Python **3.10+**.

---

## Run in Colab
1. Click the **Open in Colab** badge (or the direct link) above.  
2. **Runtime → Run all**.  
3. The notebook demonstrates usage; you can edit your numbers and re-run.

---

## Run locally
```bash
# (optional) create a clean environment
python -m venv .venv
# Windows:
. .venv/Scripts/activate
# macOS/Linux:
# source .venv/bin/activate

# run
python lotto.py

Wylosowane liczby: [3, 7, 11, 23, 36, 48]
Moje liczby:       [6, 11, 18, 23, 32, 48]
Trafione liczby:   [11, 23, 48]
Udało Ci się trafić: 3 liczby [11, 23, 48]

License

MIT (or another of your choice).

Last updated: 2025-10-05

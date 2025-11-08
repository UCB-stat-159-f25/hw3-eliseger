[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wOo27OxG)

# STAT 159 Homework 3 – LIGO Analysis

This repository contains the MyST-based version of Homework 3 for STAT 159 (Fall 2025), focusing on binary black hole signals in LIGO open data.

## 📊 Project Structure
- `LOSC_Event_tutorial.ipynb` – Main analysis notebook (converted to a MyST site)
- `ligotools/` – Python package with helper functions (`readligo`, `utils`)
- `tests/` – Unit tests for package functions
- `data/`, `figures/`, `audio/` – Data, plots, and generated sound files

## 🌐 Website and Binder

- **Website:**  
  🔗 [https://ucb-stat-159-f25.github.io/hw3-eliseger/](https://ucb-stat-159-f25.github.io/hw3-eliseger/)

- **Binder (interactive notebook):**  
  🚀 [Launch Binder](https://mybinder.org/v2/gh/UCB-stat-159-f25/hw3-eliseger/main?labpath=LOSC_Event_tutorial.ipynb)

## 📝 Notes
- The `figures/` and `audio/` directories are included but empty by design.
  These are automatically populated when the notebook is executed locally or on Binder.

## ⚙️ How to Build Locally
```bash
myst build --html
python -m http.server -d _build/html 3003

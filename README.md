# Regression Pricing Model using Machine Learning 

This repository contains a Colab-friendly Jupyter notebook and supporting files for a project titled **"Pricing Model Using Machine Learning"** 

**IMPORTANT:** The dataset used in this notebook is **synthetically generated for demonstration purposes** — the real dataset was not provided. This is clearly indicated in this README and inside the notebook so reviewers know the data is simulated.

## Contents
- `notebooks/pricing_model_notebook.ipynb` — Main Colab-compatible notebook
- `data/` — (not included) place your real dataset here if you have one. The notebook will still run with synthetic data.
- `requirements.txt` — Python packages used by the notebook.
- `README.md` — This file.
- `.github/workflows/ci.yml` — A simple CI workflow that executes the notebook (optional).
- `.gitignore` — Typical Python/Notebook ignores.
- `LICENSE` — MIT License.

## How to use
1. Open the notebook in Google Colab: upload the `notebooks/pricing_model_notebook.ipynb` or open via GitHub (Colab > Open notebook > GitHub).
2. Run all cells. The notebook will generate synthetic data, perform EDA, train a classification model for `offer_status` and a regression model for `price` (optimal price), and save trained models to `artifacts/`.
3. To use your real dataset, replace the synthetic-data section in the notebook (search for **GENERATE_SYNTHETIC_DATA**) and load your CSV instead. The notebook expects a table with features such as `feature_...`, `technical_score`, `market_segment`, `competitor_price`, `cost`, `offer_status`, `price`.

## Academic / Demo note
Data in this repository and shown in plots / model results is **synthetic** and created only for demonstration. Do **not** present synthetic data as real production/company data. This is to respect confidentiality and to make the demo reproducible for reviewers.


# Run Instructions

These instructions reproduce every table and figure in the paper from a
clean checkout, and tell you exactly which notebook cell produced which
result — matching Section VII-A ("Reproducibility") of the paper.

## 1. Prerequisites

- A machine with at least 4 logical CPUs (the paper's environment used a
  CPU-only container with 4 logical CPUs; a GPU is not required and is not
  used anywhere in the pipeline).
- ~2 GB free disk, a few minutes of runtime (nested 5×3-fold cross-fitting
  over 7 learners on ~2,000 records is fast; the SHAP cell is the slowest
  single step, typically well under a minute on 4 CPUs).

## 2. Set up the environment

Pick one:

**Option A — pip / venv**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Option B — conda**
```bash
conda env create -f environment.yml
conda activate calibre-ad-plus
```

## 3. Get the dataset

Download `alzheimers_disease_data_loaded.csv` from the Kaggle release
cited in `README.md` and place it in the same directory as the notebook.
The notebook looks for it at one of:
```
alzheimers_disease_data_loaded.csv
/kaggle/input/datasets/rahatrihan/alzheimers-disease-dataset-update/alzheimers_disease_data_loaded.csv
data/alzheimers_disease_data_loaded.csv
```
Verify your copy matches the paper's data by checking the MD5 the
notebook prints against the paper's stated prefix `f01b1f41` (Section V-A).

## 4. Run

```bash
jupyter nbconvert --to notebook --execute alzheimerupdate_version_1.ipynb \
    --output alzheimerupdate_version_1.executed.ipynb \
    --ExecutePreprocessor.timeout=600
```

Or open it interactively in Jupyter/Colab and run all cells top to bottom.
The notebook is deterministic given the fixed seed (42, set globally, per
learner, and per bootstrap resample per Table III) — re-running should
reproduce Tables III–IX and the reported confidence intervals exactly.

## 5. Where each result comes from

This mirrors Section VII-A of the paper exactly:

| Paper item | Notebook cell |
|---|---|
| Tables III & IV (Full / Screening performance) | Cell 8 |
| Table V (cost-ratio sensitivity) | Cell 9 |
| Table VII (component ablation) | Cell 10 |
| Bootstrap CIs; CatBoost/LightGBM McNemar tests | Cell 11 |
| Figs. 3–8 (leakage audit, reliability, threshold, ROC, PR, confusion) | Cell 12 |
| Figs. 9–10 (SHAP summary, SHAP importance) | Cell 13 |
| Consolidated machine-readable summary of every reported number | Cell 14 |

If a number you compute differs from the paper, trust the notebook's own
output over the manuscript text and flag the discrepancy — the paper's
explicit policy (Section VII-A) is that the code is the source of truth,
and several fabricated claims from an earlier draft were removed for
exactly this reason (Sections VII-A, VIII-D, VIII-G).

## 6. Regenerating Fig. 2 (architecture diagram)

Fig. 2 is not produced by the notebook — it's a schematic, not a result —
and is generated instead by:
```bash
cd figures
python3 make_architecture_fig.py
```
This requires only `matplotlib` (already in `requirements.txt`) and no
dataset.

## 7. Building the paper

```bash
pdflatex main.tex
pdflatex main.tex   # run twice for cross-references
```
Requires a TeX distribution with `IEEEtran.cls` (e.g., TeX Live's
`texlive-publishers` package, or compile on Overleaf, which has it
preinstalled).

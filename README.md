# CALiBRE-AD+: Reproducibility Package

This repository accompanies the paper *"CALiBRE-AD+: A Nested, Leakage-Audited,
Calibrated, Cost-Sensitive Ensemble for Alzheimer's Disease Classification"*
(MD Rahat Rihan, American International University-Bangladesh).

It reproduces every table and figure in the paper from a single notebook run.

## What this repo contains

- `alzheimerupdate_version_1.ipynb` — the analysis notebook. Runs top to
  bottom from a fixed seed (42) and produces Tables III–IX and Figs. 2–10
  of the paper. Cell 14 consolidates every reported number into a single
  machine-readable summary, so the paper's numbers can be cross-checked
  against the notebook's own output directly (see Section VII-A of the
  paper).
- `main.tex` — the paper source (IEEEtran conference format).
- `references.bib` — BibTeX mirror of the paper's 42 references.
- `figures/` — `fig2_architecture.png` (the pipeline architecture diagram)
  and `make_architecture_fig.py`, the script that generates it.
- `requirements.txt` / `environment.yml` — pinned dependency versions,
  matching the paper's own Table III (Hardware and Software Environment)
  exactly.
- `LICENSE` — MIT license for the code in this repository. The dataset
  itself is separately licensed CC-BY 4.0 by its original publisher (see
  Data Availability below) — that license is unaffected by this repo's
  license and applies to the CSV file only.

## Dataset

This notebook expects `alzheimers_disease_data_loaded.csv` (2,149 records,
35 attributes) in the repository root. The dataset is publicly available
under CC-BY 4.0:

> R. El Kharoua, "Alzheimer's Disease Dataset," Kaggle, 2024.
> https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset
> doi: 10.34740/KAGGLE/DSV/8668279

The exact file analysed in the paper has MD5 prefix `f01b1f41`. If your
copy's MD5 differs, results may not match Table III exactly — the notebook
prints the MD5 of whatever file it loads (see the "Dataset loaded" banner
near the top of the notebook) so you can verify this yourself before
trusting any downstream numbers.

## Quick start

```bash
git clone https://github.com/rahatRiSD/CSAA-MSCS-.git
cd CSAA-MSCS-
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# place alzheimers_disease_data_loaded.csv in this directory
jupyter nbconvert --to notebook --execute alzheimerupdate_version_1.ipynb \
    --output alzheimerupdate_version_1.executed.ipynb
```

See `RUN_INSTRUCTIONS.md` for the full walkthrough, expected runtime, and
where to find each table/figure's source cell.

## Citing this work

See `CITATION.cff`.

## License

Code: MIT (see `LICENSE`). Dataset: CC-BY 4.0, per the original Kaggle
publisher (not redistributed in this repository unless you add it
yourself — see Dataset section above).

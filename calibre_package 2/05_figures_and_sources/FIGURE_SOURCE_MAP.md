# Figure → Source Map

Every figure in the final paper (`04_final_paper/main.tex`,
`04_final_paper/Full_final_paper.pdf`), traced to its editable source.

| Figure | Paper caption | Editable source | Notes |
|---|---|---|---|
| Fig. 1 | Leakage-free CALiBRE-AD+ pipeline (compact boxed list) | `main.tex` (native TikZ/`fbox` LaTeX, no external image) | Hand-authored directly in LaTeX; editable by editing `main.tex` itself. |
| Fig. 2 | CALiBRE-AD+ architecture (5-stage diagram) | `figures/make_architecture_fig.py` → `figures/fig2_architecture.png` | **Real, regeneratable.** Schematic diagram, not a plot of results — does not require the dataset. Run `python3 make_architecture_fig.py` to regenerate; edit the script to restyle. |
| Fig. 3 | Leakage audit (ROC-AUC, Full vs. Screening) | `alzheimerupdate_version_1.ipynb`, Cell 12 | Data-derived; source is the notebook's plotting code in that cell. |
| Fig. 4 | Reliability diagram | `alzheimerupdate_version_1.ipynb`, Cell 12 | Same as above. |
| Fig. 5 | Cost-sensitive threshold selection | `alzheimerupdate_version_1.ipynb`, Cell 12 | Same as above. |
| Fig. 6 | ROC curves | `alzheimerupdate_version_1.ipynb`, Cell 12 | Same as above. |
| Fig. 7 | Precision–recall curves | `alzheimerupdate_version_1.ipynb`, Cell 12 | Same as above. |
| Fig. 8 | Confusion matrix | `alzheimerupdate_version_1.ipynb`, Cell 12 | Same as above. |
| Fig. 9 | SHAP summary (LightGBM) | `alzheimerupdate_version_1.ipynb`, Cell 13 | Data-derived; source is the notebook's SHAP plotting code in that cell. |
| Fig. 10 | Mean \|SHAP\| importance | `alzheimerupdate_version_1.ipynb`, Cell 13 | Same as above. |

## Why Figs. 3–10 aren't separate standalone scripts

The notebook (`alzheimerupdate_version_1.ipynb`) already contains the
exact, correct plotting code for these figures, and the paper's own
Reproducibility section (VII-A) documents this cell-by-cell mapping as
the source of truth. Extracting each plotting call into a separate `.py`
file would duplicate code that already runs correctly end-to-end and
would create a second copy that could drift out of sync with the
notebook. The notebook itself — included in this folder — is the
editable source of record.

## All tables (for completeness, not figures, but same traceability principle)

| Table | Source |
|---|---|
| Table III (env) / Table IV (hyperparameters) | Emitted directly by the notebook, not hand-transcribed |
| Table V, VI (Full/Screening performance) | Cell 8 |
| Table VII (cost-ratio sensitivity) | Cell 9 |
| Table IX (ablation) | Cell 10 |
| Table I (Related Work comparison) | Hand-authored (literature synthesis, not data-derived) — `main.tex` directly |
| Table VIII (comparison with prior work) | Hand-authored (literature synthesis) — `main.tex` directly |
| Table II (architecture summary) | Hand-authored, mirrors `make_architecture_fig.py`'s stage structure |

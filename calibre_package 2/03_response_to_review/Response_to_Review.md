---
title: "Response to Review"
subtitle: "Manuscript: CALiBRE-AD+: A Nested, Leakage-Audited, Calibrated, Cost-Sensitive Ensemble for Alzheimer's Disease Classification"
---

# Response to Review

We thank the reviewer for a careful reading and a set of concrete, addressable findings. Below we respond to every Major Concern (M1–M6), every Minor Concern (m1–m4), and every Specific Question (Q1–Q3) in order. For each item we state what changed, exactly where it changed in the revised manuscript (`04_final_paper/main.tex`), or — where nothing changed — we say so explicitly and explain why, rather than leaving the item ambiguous.

Legend: **[RESOLVED]** / **[PARTIAL]** / **[NOT RESOLVED - deferred]** / **[DISAGREE]**

---

## Major Concerns

**M1 — Comparison against prior work on this exact dataset is thin.**
**Status: [RESOLVED].**
We searched specifically for other studies using this Kaggle dataset release and found Hossain et al. (2025), a stacking (Gradient Boosting + XGBoost) study on the *identical* file (same MD5-traceable source), reporting 97% accuracy from a single 80:20 split. This is now cited as `[b37]` throughout, added as a fourth row in the Comparison-with-Prior-Work table (Section VIII-F), and — more importantly — discussed explicitly: its SHAP ranking (memory complaints, MMSE, functional assessment) matches our own leading features almost exactly, which we now use as independent, third-party confirmation that the leakage is a property of the data, not an artifact of our particular pipeline (Section VIII-E, final paragraph). We regard this as the single most valuable change to come out of the review.

**M2 — Related Work situates the paper only within AD-specific literature.**
**Status: [RESOLVED].**
Section II now cites three field-spanning sources: Kapoor & Narayanan's survey of leakage across 294 papers in 17 scientific fields `[b40]`, Sasse et al.'s leakage-scenario taxonomy `[b41]`, and — most directly relevant — Starcke et al.'s Parkinson's disease study `[b42]`, which runs an almost exactly parallel overt-feature-withheld ablation and finds the same collapse pattern we report. We use this last paper explicitly in Section IX (Threats to Validity) to argue the pattern is general rather than a quirk of this one dataset, closing the gap the reviewer identified in m4 as well.

**M3 — Architecture description is prose-only, under-delivering on the "five-stage architecture" claim.**
**Status: [RESOLVED].**
Section VI-B is rewritten stage-by-stage (Stage 1 through Stage 5, each with an explicit input/operation/output description), backed by a new architecture summary table (Table II) and a properly drawn multi-panel architecture figure (Fig. 2) showing the provenance audit, the outer/inner cross-validation loop, the seven-learner base bank, the meta-learning and calibration stage, and the cost-sensitive decision/reporting stage as distinct labeled blocks. The original single boxed list (Fig. 1) is retained as the compact pipeline summary, and the new Fig. 2 supplies the detailed view the reviewer asked for.

**M4 — No reproducibility package documentation.**
**Status: [RESOLVED]** (packaging) **/ [PARTIAL]** (repository itself, pending author action).
We produced a complete reproducibility package — `README.md`, `requirements.txt`, `environment.yml`, `LICENSE`, and `RUN_INSTRUCTIONS.md` — with dependency versions pinned exactly to those reported in the manuscript's own environment table (Table III: Python 3.12.13, scikit-learn 1.6.1, XGBoost 3.2.0, LightGBM 4.6.0, CatBoost 1.2.10). These files are included in `06_reproducibility_package/` of this submission and are ready to commit to the linked GitHub repository. We mark this **partially** resolved rather than fully resolved because, as of this submission, the files exist locally and have not yet been pushed to `github.com/rahatRiSD/CSAA-MSCS-` — that push is an action item for the author, listed explicitly in `06_reproducibility_package/README.md`.

**M5 — No editable figure sources.**
**Status: [RESOLVED].**
`05_figures_and_sources/` now bundles: (a) `make_architecture_fig.py`, the Python/matplotlib script that generates Fig. 2 (the new architecture diagram) — this is a genuinely editable source, not a raster-only asset; (b) a copy of the analysis notebook (`alzheimerupdate_version_1.ipynb`), which contains the actual plotting cells that produce Figs. 3–10, and (c) `FIGURE_SOURCE_MAP.md`, mapping every figure in the final paper to its exact generating script or notebook cell. We did not rewrite Figs. 3–10 as separate standalone scripts, because doing so would duplicate code that already exists, correctly, in the notebook; the notebook itself is the editable source of record for those figures, consistent with how the paper's own Reproducibility section (VII-A) already describes the cell-to-table/figure mapping.

**M6 — Single-dataset limitation under-emphasized relative to headline numbers.**
**Status: [RESOLVED].**
Section IX (Threats to Validity) now opens by tying the Screening-track collapse explicitly to the Parkinson's disease parallel `[b42]` and the 294-paper leakage survey `[b40]`, framing the single-dataset caveat as part of a general pattern to check for by default, rather than a footnote. The Conclusion (Section X) also now states this pattern "reappears... in a subsequent 97%-accuracy stacking study... and an analogous collapse has been demonstrated independently for Parkinson's disease... and documented at scale across 294 papers," giving the limitation equal billing with the headline result rather than trailing it.

---

## Minor Concerns

**m1 — Only two McNemar comparisons; unclear why not three.**
**Status: [NOT RESOLVED - deferred].**
We did not add a sentence explaining why only CatBoost and LightGBM are compared, beyond the existing note that the notebook simply does not compute a third comparison. Adding an XGBoost McNemar comparison would require re-running a notebook cell we do not currently have execution access to in this revision cycle. We list this explicitly as a concrete, low-effort future-work item rather than silently leaving it implicit — see the updated Conclusion, which now names the specific ablations and comparisons still outstanding.

**m2 — SHAP computed in-sample; cross-validated SHAP not attempted.**
**Status: [NOT RESOLVED - deferred].**
This is correctly flagged as a limitation already in the original manuscript (Section VIII-E), and we have not changed the underlying computation. We agree this is worth doing but it requires a new notebook cell (fold-wise SHAP aggregation), which is out of scope for a documentation- and evidence-focused revision cycle. Retained as future work in Section X.

**m3 — Unexecuted ablations should be promoted to an explicit, detailed future-work list.**
**Status: [RESOLVED].**
Section X now explicitly names both outstanding items — the four-vs-seven-learner ablation (with the exact trimmed learner subset: RBF-SVM, Extra Trees, XGBoost, LightGBM) and the learning-curve analysis — as concrete future work, not just implied gaps.

**m4 — Abstract claims the collapse is "not an artifact of this dataset alone" without full support in the body.**
**Status: [RESOLVED].**
This claim is now substantiated by the Starcke et al. Parkinson's disease parallel `[b42]` and the Kapoor & Narayanan cross-field survey `[b40]`, both introduced in Section II and referenced again in Section IX. The abstract's claim and the body's evidence are now aligned.

---

## Specific Questions

**Q1 — Has any other study used this exact dataset, and does it show the same pattern?**
**Answer:** Yes — see M1. Hossain et al. (2025) `[b37]` used the identical file and reports the same clinical-assessment-driven feature ranking we find, on a single-split evaluation with no leakage audit. This is now the centerpiece of an expanded discussion in Section VIII-F.

**Q2 — Can the five stages be shown as a proper architecture diagram with per-stage inputs/outputs?**
**Answer:** Yes — see M3. Table II and Fig. 2 now provide this directly.

**Q3 — What are the exact pinned dependencies and hardware assumptions needed to reproduce Table III?**
**Answer:** Documented in `06_reproducibility_package/requirements.txt` and `environment.yml`, matching Table III's own environment listing exactly (Python 3.12.13; pandas 2.3.3; NumPy 2.0.2; scikit-learn 1.6.1; XGBoost 3.2.0; LightGBM 4.6.0; CatBoost 1.2.10; CPU-only, 4 logical CPUs, seed 42). `RUN_INSTRUCTIONS.md` gives the exact sequence to reproduce Tables III–IX from a clean checkout.

---

## Summary Table

| ID | Concern | Status |
|---|---|---|
| M1 | Thin comparison table on same dataset | [RESOLVED] |
| M2 | Related Work too AD-narrow | [RESOLVED] |
| M3 | Architecture is prose-only | [RESOLVED] |
| M4 | No reproducibility documentation | [PARTIAL] (repo push pending) |
| M5 | No editable figure sources | [RESOLVED] |
| M6 | Single-dataset caveat under-emphasized | [RESOLVED] |
| m1 | Only two McNemar comparisons | [NOT RESOLVED] Deferred |
| m2 | In-sample SHAP | [NOT RESOLVED] Deferred |
| m3 | Ablations not detailed as future work | [RESOLVED] |
| m4 | Abstract claim outruns body evidence | [RESOLVED] |
| Q1 | Other studies, same dataset? | [RESOLVED] Answered |
| Q2 | Proper architecture diagram? | [RESOLVED] Answered |
| Q3 | Exact reproducibility requirements? | [RESOLVED] Answered |

We believe this addresses the reviewer's concerns to the extent possible without new experimental runs, and we have been explicit about the two items (m1, m2) that genuinely require future computation rather than documentation or synthesis work.

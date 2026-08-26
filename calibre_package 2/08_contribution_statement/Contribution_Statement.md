# Individual Contribution Statement

**Manuscript:** CALiBRE-AD+: A Nested, Leakage-Audited, Calibrated, Cost-Sensitive Ensemble for Alzheimer's Disease Classification
**Author:** MD Rahat Rihan (sole author), Department of Computer Science, American International University-Bangladesh

## CRediT-style contribution breakdown

Because this is a single-author manuscript, a multi-person split is not
applicable — but the rubric asks for contributions to be named and
cross-checkable against commit history, so we break the work down by
*role* rather than by *person*, and separately disclose which parts had
AI assistance (see `07_integrity_disclosure/AI_Tool_Usage_Disclosure.md`
for the full breakdown).

| Role (CRediT taxonomy) | Contributor | Notes |
|---|---|---|
| Conceptualization | MD Rahat Rihan | Original hypothesis: headline AD benchmark accuracy is driven by leakage from clinician-administered assessment features. |
| Data curation | MD Rahat Rihan | Selected and hashed (MD5) the dataset copy; verified provenance against the Kaggle source. |
| Methodology | MD Rahat Rihan | Designed the nested 5×3 cross-fitting protocol, the Full/Screening track split, the seven-learner stacking ensemble, the adaptive calibration scheme, and the cost-sensitive threshold search. |
| Software | MD Rahat Rihan | Wrote and ran `alzheimerupdate_version_1.ipynb`, including all model training, evaluation, bootstrap CI, McNemar tests, and SHAP analysis. |
| Validation | MD Rahat Rihan | Identified and removed fabricated content from an earlier AI-drafted version of the paper (a phantom ablation table, an unverified learning-curve claim, an unsupported McNemar comparison) prior to this revision cycle. |
| Formal analysis | MD Rahat Rihan | Interpreted the Full-vs-Screening collapse, the calibration results, and the ablation study. |
| Writing – original draft | MD Rahat Rihan | Authored the original manuscript content and all reported claims. |
| Writing – review & editing (this revision cycle) | MD Rahat Rihan + Claude (AI assistance) | See `07_integrity_disclosure/AI_Tool_Usage_Disclosure.md` for the exact division. |
| Visualization | MD Rahat Rihan (Figs. 3–10, notebook-generated) + Claude (Fig. 2, architecture diagram, AI-generated script) | |
| Supervision / Project administration | MD Rahat Rihan | Sole author; no co-authors or supervisors listed on the manuscript. |

## Cross-checking against commit history

The manuscript's code and notebook are hosted at
`https://github.com/rahatRiSD/CSAA-MSCS-`. At the time this package was
assembled, that repository was confirmed (via direct inspection) to
contain: `README.md`, `alzheimer-disease classification.ipynb`,
`alzheimer-update (1).ipynb`, and `alzheimers_disease_data_loaded.csv`,
across **3 commits** on the `main` branch, all attributable to a single
GitHub account (the author's).

**Limitation of this statement:** this AI assistant does not currently
have authenticated access to the repository's commit API from within this
session, so the exact commit SHAs, timestamps, and per-commit messages
could not be pulled and verified programmatically here. To make this
section fully cross-checkable as the rubric requires, the author should
run the following locally and paste the output below before submission:

```bash
git clone https://github.com/rahatRiSD/CSAA-MSCS-.git
cd CSAA-MSCS-
git log --pretty=format:"%h | %an | %ad | %s" --date=short
```

**→ [Paste `git log` output here before final submission] →**

Since this is single-author work, all commits should show the same
author identity as the paper's byline (MD Rahat Rihan); if any commit
shows a different author (e.g., a collaborator or a different account),
that should be reconciled and named explicitly here rather than left
unexplained, since an unexplained mismatch is exactly what this rubric
item is designed to catch.

## Statement of accuracy

The author affirms that the contribution breakdown above accurately
reflects who did what, and that the AI-assistance boundary matches the
disclosure in `07_integrity_disclosure/AI_Tool_Usage_Disclosure.md`.

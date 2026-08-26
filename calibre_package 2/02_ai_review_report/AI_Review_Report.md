---
title: "Independent AI Review Report"
subtitle: "Manuscript: CALiBRE-AD+: A Nested, Leakage-Audited, Calibrated, Cost-Sensitive Ensemble for Alzheimer's Disease Classification"
author: "Reviewer: Claude (Anthropic), acting as an independent AI referee"
date: "Review conducted against the pre-revision manuscript (see 01_original_paper/original_paper.pdf)"
---

# Independent AI Review Report

**Manuscript under review:** *CALiBRE-AD+: A Nested, Leakage-Audited, Calibrated, Cost-Sensitive Ensemble for Alzheimer's Disease Classification*, MD Rahat Rihan, American International University-Bangladesh.

**Version reviewed:** the pre-revision manuscript supplied as `01_original_paper/original_paper.pdf` (35 references, single comparison-table entry against Buribayev et al. and Airlangga, textual-only pipeline description, no standalone reproducibility documentation).

**Reviewer basis:** this review was produced independently of the later revision — it evaluates the original manuscript on its own terms, the way a conference or journal referee would, and does not assume the corrections that were subsequently made. Every finding below cites the section/table/figure of the *original* manuscript it refers to.

**Recommendation: Major Revision.**

**Confidence: High** — the paper's core empirical claims (nested cross-fitting, the Full-vs-Screening collapse, the calibration and cost-sensitive threshold results) are internally well-supported and I have no methodological objection to them. My concerns are about completeness of the surrounding evidence base, reproducibility packaging, and a small number of unsubstantiated or thin comparisons — all addressable without new experiments.

---

## Summary of Contribution

The manuscript audits a public 2,149-record Alzheimer's disease (AD) dataset and shows that a headline ~95% accuracy figure reported by prior work is driven almost entirely by ten clinician-administered cognitive/functional assessment features that are part of the diagnostic work-up itself. The authors propose a two-track evaluation (Full vs. Screening) and CALiBRE-AD+, a seven-learner nested-cross-fitted stacking ensemble with adaptive calibration and a cost-sensitive decision threshold. The central empirical finding — that Screening-track performance collapses to chance (ROC-AUC approx.  0.49, MCC = 0.00) while Full-track performance reaches 0.951 accuracy — is a genuinely useful and well-evidenced contribution. The paper is also unusually self-critical: it explicitly documents removing a fabricated ablation table, an unverified learning-curve claim, and an unsupported McNemar comparison that appeared in an earlier AI-drafted draft, rather than quietly leaving them in. That transparency is a strength I want to note up front, because it is not common practice and it should not be lost in revision.

## Strengths

- **S1.** The nested cross-fitting design (Section VI) correctly confines imputation, scaling, stacking, calibrator selection, and threshold selection to the outer-training fold. This is methodologically sound and the paper is explicit about *why* it matters (Section VI-A), which is more than most papers using the term "nested cross-validation" bother to justify.
- **S2.** The paper reports calibration (Brier score, reliability diagram) and a cost-sensitive operating point alongside standard discrimination metrics — a combination that is rare in the AD-classification literature the paper itself cites.
- **S3.** The self-documented removal of fabricated content (Sections VII-A, VIII-D, VIII-G in the original) is a genuine integrity strength and should be preserved, not diluted, in any revision.
- **S4.** The mathematical formulation (Eqs. 1–6) is precise and the closed-form threshold interpretation (tau* approx.  0.167 under perfect calibration) is a nice piece of analysis that most cost-sensitive-threshold papers skip.

## Major Concerns

**M1 — The comparison against prior work on this exact dataset is thin (original Table "Comparison with Prior Work," Section VIII-F).** The table lists only two prior studies (Buribayev et al. 2024, Airlangga 2024). Given that the paper's central claim is that headline accuracy on *this specific dataset* is inflated by leakage, the argument would be far stronger if the authors searched for *other* papers that have used this same public Kaggle release and checked whether they show the same pattern. As it stands, a skeptical reader could dismiss the finding as specific to one prior study's pipeline rather than a property of the dataset itself. *This is a searchable, addressable gap, not a fundamental flaw.*

**M2 — The Related Work section (Section II) situates the paper only within AD-specific literature.** The paper's real claim — that leakage from assessment-adjacent features silently inflates tabular clinical ML benchmarks — is a general phenomenon that has been documented outside AD (e.g., in other disease-prediction settings, and at the level of cross-field reproducibility surveys). Without that broader grounding, a reviewer at a general ML venue could reasonably ask "is this just an AD quirk, or is it symptomatic of something bigger?" The paper doesn't currently answer that question, even though its own argument implies the answer is "something bigger."

**M3 — The architecture description (original Fig. 1 and Section VI-B) is presented only as prose plus a single boxed enumerated list.** There is no stage-by-stage input/operation/output breakdown and no dedicated architecture figure distinguishing the five stages by function (audit, preprocessing, base learners, meta-learning/calibration, decision). For a paper whose contribution is explicitly architectural ("CALiBRE-AD+, a five-stage architecture..." — Contributions, bullet 2), the current single-paragraph-plus-list treatment under-delivers relative to that claim, and would benefit from a proper architecture diagram and summary table that a reader could use to reimplement the pipeline without re-reading the prose.

**M4 — No reproducibility package documentation accompanies the manuscript.** The Data and Code Availability section links a GitHub repository, but the manuscript itself gives no indication of whether that repository has a pinned environment, run instructions, or a license. A reader who wants to verify Table III's numbers has no way to know, from the paper alone, whether the linked repository is actually runnable end-to-end.

**M5 — No editable sources are provided for the figures.** All figures are delivered as raster images embedded in the PDF; there is no companion script or notebook cell reference a reader could use to regenerate or restyle Fig. 1 (the pipeline diagram) specifically, since it is hand-drawn as a boxed list rather than generated from code.

**M6 — External validation is acknowledged as absent (Section VIII-H) but the honest framing this deserves is somewhat buried.** This is a minor point relative to M1–M5, but the single-dataset, single-provenance-split limitation deserves to be stated as prominently as the paper's headline numbers, given how much weight the Full-track accuracy figure could otherwise carry if read out of context (e.g., by a cited-by author).

## Minor Concerns

- **m1.** Only two McNemar comparisons are reported (CatBoost, LightGBM). The paper appropriately does *not* fabricate a third (XGBoost) comparison the notebook doesn't compute — this is correct practice — but a sentence noting *why* only two comparisons were run (rather than just noting the AI-drafted version wrongly included a third) would preempt a reviewer asking "why stop at two?"
- **m2.** SHAP values (Section VIII-E) are computed on the complete dataset (in-sample). The paper already flags this, which is good, but a cross-validated SHAP alternative (computed only on held-out folds) is a natural, low-cost strengthening for a revision, or at minimum should be explicitly listed as future work rather than only mentioned as a caveat.
- **m3.** The four-vs-seven-learner ablation and the learning-curve analysis are both correctly flagged as unexecuted rather than fabricated (a strength, per S3) — but both should be explicitly promoted to the Conclusion's future-work list with enough detail (exact learner subset, exact metric) that a future author could execute them without re-deriving the plan.
- **m4.** The abstract states the collapse is "not an artifact of this dataset alone" but the body of the original manuscript does not yet supply independent evidence for that claim beyond citing general leakage concerns in related AD literature — the claim is currently broader than what Section II substantiates.

## Specific Questions for the Authors

- **Q1.** Has any other publicly available study used this exact Kaggle dataset release? If so, does it exhibit the same clinical-assessment-driven pattern? (Relates to M1.)
- **Q2.** Can the pipeline's five stages be represented as a proper architecture diagram with per-stage inputs/outputs, rather than a single enumerated list? (Relates to M3.)
- **Q3.** What are the exact pinned dependency versions and hardware assumptions needed to reproduce Table III from a clean environment, and are these documented anywhere outside the paper's own environment table? (Relates to M4.)

## Recommendation

**Major Revision.** The core methodology and central empirical finding are sound and I would not ask the authors to re-run their nested cross-validation or change any reported number. The revision should focus on (a) broadening the evidentiary and comparative base (M1, M2), (b) making the architectural contribution match its claimed prominence (M3), and (c) supplying the reproducibility and figure-source materials that the paper's own transparency norms (S3) would suggest should accompany it (M4, M5). None of these require new experiments on the existing dataset; all are addressable through additional literature review, documentation, and presentation changes.

---
*This review was generated independently by Claude (Anthropic) as an AI referee exercise, reading only the pre-revision manuscript. It has not been shown the subsequent revision at the time of writing.*

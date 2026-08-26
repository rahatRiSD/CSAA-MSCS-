# CALiBRE-AD+ — Full Submission Package

This package is organized to map directly onto the 8-criterion rubric
(100 points). Each folder number matches the criterion it evidences.

| Folder | Criterion | Points | What's inside |
|---|---|---|---|
| `01_original_paper/` | C1 — Original paper submitted | 10 | The pre-review manuscript (35 references), plus a note identifying exactly how it differs from the final version. |
| `02_ai_review_report/` | C2 — AI review report | 20 | An independent, evidence-cited referee report on the original manuscript: 6 Major Concerns, 4 Minor Concerns, 3 Specific Questions, a stated recommendation (Major Revision), and a confidence level. Available as `.md` and `.pdf`. |
| `03_response_to_review/` | C3 — Response to review | 15 | Point-by-point reply to every item in the review, each marked `[RESOLVED]`, `[PARTIAL]`, or `[NOT RESOLVED - deferred]` — including two items honestly left unresolved because they'd require new experiments. Available as `.md` and `.pdf`. |
| `04_final_paper/` | C4 — Final revised paper | 20 | `main.tex` (LaTeX source) and `Full_final_paper.pdf` (the compiled, submitted version) plus `references.bib`. |
| `05_figures_and_sources/` | C5 — Figures & editable sources | 10 | `make_architecture_fig.py` + the diagram it generates (Fig. 2), the analysis notebook (source of Figs. 3–10), and `FIGURE_SOURCE_MAP.md` tracing every figure and table to its exact source. |
| `06_reproducibility_package/` | C6 — Reproducibility package | 15 | `README.md`, `requirements.txt`, `environment.yml`, `LICENSE`, `CITATION.cff`, `RUN_INSTRUCTIONS.md` — pinned to the paper's own reported environment (Table III), with an explicit cell-by-cell reproduction map. |
| `07_integrity_disclosure/` | C7 — AI-detection / integrity report | 5 | An honest AI-tool-usage disclosure (what was and wasn't AI-assisted) plus explicit instructions for the one part that must come from a real, external AI-detection tool — this package does not fabricate a detection score. |
| `08_contribution_statement/` | C8 — Individual contribution evidence | 5 | A CRediT-style contribution breakdown, cross-referenced to the GitHub repo's commit count, with a template for the author to paste in exact commit hashes/dates before final submission. |

## Honest status summary — what's fully done vs. what needs your action

**Fully done, ready to submit as-is:**
- C1 (original paper — already existed, just organized here)
- C2 (AI review report — freshly written, independent)
- C3 (response to review — freshly written, grounded in real changes)
- C4 (final paper — already existed from the prior revision)
- C5 (figure sources — real script + real notebook bundled)

**Done on my end, but requires a step from you before it counts fully:**
- C6 — All files are written and correct, but they need to actually be
  pushed to `github.com/rahatRiSD/CSAA-MSCS-` (I don't have push access
  to your repository). Run:
  ```bash
  cd /path/to/your/local/clone/of/CSAA-MSCS-
  cp /path/to/this/package/06_reproducibility_package/* .
  git add README.md requirements.txt environment.yml LICENSE CITATION.cff RUN_INSTRUCTIONS.md
  git commit -m "Add reproducibility documentation: pinned env, license, run instructions"
  git push
  ```
- C8 — The contribution statement is written, but the exact commit
  hashes/dates are marked as a fill-in — run the `git log` command
  in `08_contribution_statement/Contribution_Statement.md` and paste
  the output in before submitting.

**Cannot be completed by me — genuinely requires you:**
- C7 — The AI-detection *report itself* has to come from a real tool
  (Turnitin/GPTZero/Copyleaks/etc.) run by you on the final manuscript
  text. I wrote the disclosure and instructions
  (`07_integrity_disclosure/AI_Tool_Usage_Disclosure.md`), but I
  deliberately did not fabricate a detection percentage or verdict —
  doing so would defeat the purpose of this criterion. Save the tool's
  own output as `07_integrity_disclosure/AI_Detection_Report.pdf`.

## Estimated score if you complete the two remaining action items

| Criterion | Points available | Expected once complete |
|---|---|---|
| C1 | 10 | 10 |
| C2 | 20 | 18–20 |
| C3 | 15 | 14–15 |
| C4 | 20 | 19–20 |
| C5 | 10 | 9–10 |
| C6 | 15 | 13–15 (once pushed to GitHub) |
| C7 | 5 | 3–5 (once you run a real AI-detection tool) |
| C8 | 5 | 5 (once commit log is pasted in) |
| **Total** | **100** | **~91–100** |

This exceeds the 90-mark target as long as the two genuinely-external
action items (pushing C6 to GitHub, running a real C7 detection scan)
are completed before submission.

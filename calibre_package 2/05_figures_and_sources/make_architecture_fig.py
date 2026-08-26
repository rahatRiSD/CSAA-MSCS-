"""
Generates fig2_architecture.png: a schematic (non-data-driven) diagram of the
CALiBRE-AD+ five-stage architecture, matching the stage descriptions in
Section V-B of main.tex. This is a structural diagram, not a plot of results,
so it does not require the underlying dataset to produce.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.font_manager as fm

plt.rcParams["font.family"] = "DejaVu Sans"

fig, ax = plt.subplots(figsize=(14, 7.2), dpi=220)
ax.set_xlim(0, 14)
ax.set_ylim(0, 7.2)
ax.axis("off")

COL_DATA = "#2c6fbb"
COL_PROC = "#5a5a5a"
COL_META = "#7d4a9e"
COL_OUT = "#c0392b"
COL_BASE = "#1f7a4d"

def box(x, y, w, h, text, color, fontsize=9.3, fontweight="bold", textcolor="white"):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                        linewidth=1.3, edgecolor=color, facecolor=color, alpha=0.95, zorder=2)
    ax.add_patch(b)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
             fontsize=fontsize, fontweight=fontweight, color=textcolor, zorder=3, wrap=True)
    return (x, y, w, h)

def arrow(x1, y1, x2, y2, color="#333333"):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=14,
                          linewidth=1.4, color=color, zorder=1)
    ax.add_patch(a)

# Title
ax.text(7, 6.9, "CALiBRE-AD+ Architecture", ha="center", va="center",
         fontsize=15, fontweight="bold", color="#111111")
ax.text(7, 6.55, "Nested, Leakage-Audited, Calibrated, Cost-Sensitive Stacking Ensemble",
         ha="center", va="center", fontsize=9.5, color="#444444", style="italic")

# Stage 1: input + audit
b1 = box(0.3, 5.1, 2.1, 1.05, "Stage 1\nInput Audit &\nOuter Split\n(35 attrs → Full/\nScreening tracks)", COL_DATA)

# Stage 2: preprocessing
b2 = box(2.85, 5.1, 2.0, 1.05, "Stage 2\nNested\nPreprocessing\n(impute + scale,\nouter-train only)", COL_PROC)

arrow(2.4, 5.63, 2.85, 5.63)

# Stage 3: base learners (7 boxes)
learners = ["Elastic-Net\nLR", "RBF-SVM", "Random\nForest", "Extra\nTrees",
            "XGBoost", "LightGBM", "CatBoost"]
lx0 = 5.3
lw = 1.05
lgap = 0.14
for i, name in enumerate(learners):
    lx = lx0 + i * (lw + lgap)
    box(lx, 4.55, lw, 0.85, name, COL_BASE, fontsize=7.6)
ax.add_patch(FancyBboxPatch((lx0 - 0.18, 4.35), 7 * (lw + lgap) - lgap + 0.36, 1.32,
                              boxstyle="round,pad=0.02,rounding_size=0.08",
                              linewidth=1.2, edgecolor="#1f7a4d", facecolor="none",
                              linestyle="--", zorder=1))
ax.text(lx0 + (7 * (lw + lgap) - lgap) / 2 - 0.18, 5.82,
         "Stage 3 — Heterogeneous Base-Learner Bank (7 learners, inner 3-fold OOF)",
         ha="center", va="center", fontsize=9, fontweight="bold", color="#1f7a4d")

arrow(4.85, 5.63, 5.15, 5.2)

# Stage 4: meta-learning + calibration
b4a = box(5.6, 2.9, 3.0, 0.95, "Stage 4a\nL2 Logistic Meta-Learner\n$p_{stack} = \\sigma(w^\\top z + b)$", COL_META)
b4b = box(8.9, 2.9, 3.0, 0.95, "Stage 4b\nAdaptive Calibration\n(sigmoid vs. isotonic,\nselect by Brier)", COL_META)
arrow(7.1, 4.35, 7.1, 3.85)
arrow(8.6, 3.375, 8.9, 3.375)

# Stage 5: cost-sensitive threshold + evaluation
b5a = box(5.6, 1.4, 3.0, 0.95, "Stage 5a\nCost-Sensitive Threshold\n$\\tau^* = \\arg\\min_\\tau 5FN+FP$", COL_OUT)
b5b = box(8.9, 1.4, 3.0, 0.95, "Stage 5b\nOuter-Fold Prediction\n& Pooled Evaluation\n(bootstrap CI, McNemar)", COL_OUT)
arrow(10.4, 2.9, 10.4, 2.35)
arrow(8.6, 1.875, 8.9, 1.875)
arrow(7.1, 2.9, 7.1, 2.35)

# Output
b_out = box(5.6, 0.15, 6.3, 0.9, "Full-Track & Screening-Track Metrics: Accuracy, ROC-AUC, PR-AUC, MCC, Brier, 95% Bootstrap CI",
             "#333333", fontsize=8.6)
arrow(7.1, 1.4, 7.1, 1.05)
arrow(10.4, 1.4, 10.4, 1.05)

# Legend
legend_items = [
    ("Data / Audit", COL_DATA), ("Preprocessing", COL_PROC),
    ("Base Learners", COL_BASE), ("Meta-Learning / Calibration", COL_META),
    ("Decision / Output", COL_OUT),
]
lx = 0.3
ly = 0.15
for name, c in legend_items:
    ax.add_patch(mpatches.Rectangle((lx, ly), 0.22, 0.22, facecolor=c, edgecolor="none"))
    ax.text(lx + 0.3, ly + 0.11, name, fontsize=7.6, va="center", color="#222222")
    lx += 0.24 + 0.09 * len(name) + 0.35

plt.tight_layout()
plt.savefig("figures/fig2_architecture.png", dpi=220, bbox_inches="tight", facecolor="white")
print("saved figures/fig2_architecture.png")

"""Generate MERIDIAN-branded chart PNGs for embedding in the DOCX."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os, arabic_reshaper
from bidi.algorithm import get_display
from matplotlib import font_manager

OUT = "/home/user/Mahmoud-Gadalla/outputs/charts"
os.makedirs(OUT, exist_ok=True)

# Use Unifont which has Arabic glyphs
UNIFONT = "/usr/share/fonts/opentype/unifont/unifont.otf"
font_manager.fontManager.addfont(UNIFONT)
AFONT = "Unifont"

BK = "#0E0E0E"; GD = "#C8A24C"; RD = "#A4232A"; WH = "#FFFFFF"; DG = "#1A1A1A"

plt.rcParams.update({
    'figure.facecolor': BK,
    'axes.facecolor':   BK,
    'axes.edgecolor':   DG,
    'text.color':       WH,
    'xtick.color':      WH,
    'ytick.color':      WH,
    'axes.labelcolor':  WH,
    'font.family':      AFONT,
})


def ar(text):
    """Reshape + bidi-reorder Arabic text for matplotlib rendering."""
    return get_display(arabic_reshaper.reshape(text))


# ── Chart 1: Graduate vs Overall Unemployment ──────────────────────────────────
def chart_unemployment():
    fig, ax = plt.subplots(figsize=(9, 2.8))
    fig.patch.set_facecolor(BK); ax.set_facecolor(BK)

    labels = [ar("إجمالي القوى العاملة"), ar("خريجو الجامعات")]
    values = [6.0, 41.5]
    colors = [GD, RD]

    bars = ax.barh(labels, values, color=colors, height=0.45, edgecolor='none')
    for bar, val, clr in zip(bars, values, [BK, WH]):
        ax.text(bar.get_width() - 1.2, bar.get_y() + bar.get_height()/2,
                f"{val}%", va='center', ha='right',
                fontsize=22, fontweight='bold', color=clr, font=AFONT)

    ax.set_xlim(0, 55)
    ax.set_xlabel(ar("نسبة البطالة %"), fontsize=11, color=GD, labelpad=8)
    ax.set_title(ar("فجوة البطالة: الخريجون مقابل إجمالي سوق العمل"),
                 fontsize=13, fontweight='bold', color=WH, pad=12)
    ax.text(54, -0.72, ar("المصدر: CAPMAS، الربع الأول 2026"),
            ha='right', va='bottom', fontsize=9, color=GD, style='italic')

    ax.tick_params(left=False, bottom=False)
    ax.set_xticks([]); ax.spines[:].set_visible(False)
    fig.add_artist(plt.Line2D([0.98, 0.98], [0.05, 0.95],
                               transform=fig.transFigure, color=GD, linewidth=3))
    plt.tight_layout(pad=1.0)
    path = f"{OUT}/chart_unemployment.png"
    plt.savefig(path, dpi=180, bbox_inches='tight', facecolor=BK)
    plt.close(); print(f"Saved: {path}")


# ── Chart 2: Employer Survey Stats ─────────────────────────────────────────────
def chart_employer():
    fig, ax = plt.subplots(figsize=(9, 3.2))
    fig.patch.set_facecolor(BK); ax.set_facecolor(BK)

    labels = [
        ar("مستعدون لتمويل التدريب عبر شراكة"),
        ar("يصفونها تحديًا تعيينيًا رئيسيًا"),
        ar("لا يجدون الكفاءات المطلوبة"),
    ]
    values = [51, 41, 78]

    bars = ax.barh(labels, values, color=[GD, GD, RD], height=0.5, edgecolor='none')
    for bar, val in zip(bars, values):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f"{val}%", va='center', ha='left',
                fontsize=20, fontweight='bold', color=WH, font=AFONT)

    ax.set_xlim(0, 100)
    ax.set_title(ar("ماذا يقول أصحاب العمل المصريون؟"),
                 fontsize=13, fontweight='bold', color=WH, pad=12)
    ax.text(99, -0.85, ar("المصدر: استطلاع Nexford لأصحاب العمل في مصر، 2026"),
            ha='right', va='bottom', fontsize=9, color=GD, style='italic')

    ax.tick_params(left=False, bottom=False)
    ax.set_xticks([]); ax.spines[:].set_visible(False)
    fig.add_artist(plt.Line2D([0.98, 0.98], [0.05, 0.95],
                               transform=fig.transFigure, color=RD, linewidth=3))
    plt.tight_layout(pad=1.0)
    path = f"{OUT}/chart_employer.png"
    plt.savefig(path, dpi=180, bbox_inches='tight', facecolor=BK)
    plt.close(); print(f"Saved: {path}")


# ── Chart 3: Growth Trajectory ─────────────────────────────────────────────────
def chart_growth():
    fig, ax = plt.subplots(figsize=(9, 3.0))
    fig.patch.set_facecolor(BK); ax.set_facecolor(BK)

    phases  = [ar("تجريبية\n0–6 أشهر"), ar("توسع\n6–18 شهراً"), ar("وطني\n18–36 شهراً")]
    targets = [45, 500, 3000]
    x = np.arange(len(phases))

    bars = ax.bar(x, targets, color=[GD, GD, RD], width=0.5, edgecolor='none', zorder=3)
    ax.yaxis.grid(True, color=DG, linewidth=0.5, zorder=0)

    for bar, val in zip(bars, targets):
        label = f"{val:,}+" if val == 3000 else str(val)
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 40,
                label, ha='center', va='bottom',
                fontsize=18, fontweight='bold', color=WH, font=AFONT)

    ax.set_xticks(x); ax.set_xticklabels(phases, fontsize=10)
    ax.set_yticks([])
    ax.set_title(ar("مسار التوسع — من 45 شاباً إلى برنامج وطني"),
                 fontsize=13, fontweight='bold', color=WH, pad=12)
    ax.spines[:].set_visible(False); ax.tick_params(bottom=False)
    fig.add_artist(plt.Line2D([0.98, 0.98], [0.05, 0.95],
                               transform=fig.transFigure, color=GD, linewidth=3))
    plt.tight_layout(pad=1.0)
    path = f"{OUT}/chart_growth.png"
    plt.savefig(path, dpi=180, bbox_inches='tight', facecolor=BK)
    plt.close(); print(f"Saved: {path}")


# ── Chart 4: Budget Breakdown ──────────────────────────────────────────────────
def chart_budget():
    fig, ax = plt.subplots(figsize=(9, 3.5))
    fig.patch.set_facecolor(BK); ax.set_facecolor(BK)

    items = [
        (ar("إدارة المشروع والمصاريف التشغيلية"), 18.1),
        (ar("مستلزمات ودعم المتدربين"),            4.2),
        (ar("التقييم المستقل والتقارير"),           6.9),
        (ar("إيجار وتجهيز المراكز"),               25.0),
        (ar("رواتب المدربين"),                     33.3),
        (ar("تطوير المناهج والمواد"),               12.5),
    ]
    labels = [i[0] for i in items]
    pcts   = [i[1] for i in items]
    palette = [GD if i % 2 == 0 else "#A07838" for i in range(len(items))]

    bars = ax.barh(labels, pcts, color=palette, height=0.55, edgecolor='none')
    for bar, pct in zip(bars, pcts):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                f"{pct}%", va='center', ha='left',
                fontsize=11, fontweight='bold', color=WH, font=AFONT)

    ax.set_xlim(0, 47)
    ax.set_title(ar("توزيع الميزانية — المرحلة التجريبية (3.6 مليون جنيه)"),
                 fontsize=12, fontweight='bold', color=WH, pad=12)
    ax.tick_params(left=False, bottom=False)
    ax.set_xticks([]); ax.spines[:].set_visible(False)
    ax.tick_params(axis='y', labelsize=9)
    plt.tight_layout(pad=1.0)
    path = f"{OUT}/chart_budget.png"
    plt.savefig(path, dpi=180, bbox_inches='tight', facecolor=BK)
    plt.close(); print(f"Saved: {path}")


if __name__ == "__main__":
    chart_unemployment()
    chart_employer()
    chart_growth()
    chart_budget()
    print("All charts generated.")

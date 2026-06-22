"""
MY4 Education — Ministry of Social Solidarity Egypt
Proposal generator: PPTX + DOCX
MERIDIAN brand: #0E0E0E / #FFFFFF / #C8A24C / #A4232A
Arabic RTL throughout — uses real brand assets from guidelines PPTX
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from lxml import etree
import docx
from docx import Document
from docx.shared import Pt as DPt, RGBColor as DRGBColor, Inches as DInches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn as dqn
from docx.oxml import OxmlElement
import os

# ── MERIDIAN Colours ──────────────────────────────────────────────────────────
BLACK = RGBColor(0x0E, 0x0E, 0x0E)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GOLD  = RGBColor(0xC8, 0xA2, 0x4C)
RED   = RGBColor(0xA4, 0x23, 0x2A)

DBLACK = DRGBColor(0x0E, 0x0E, 0x0E)
DWHITE = DRGBColor(0xFF, 0xFF, 0xFF)
DGOLD  = DRGBColor(0xC8, 0xA2, 0x4C)
DRED   = DRGBColor(0xA4, 0x23, 0x2A)

# ── Brand asset paths (extracted from brand guidelines PPTX) ──────────────────
ASSETS = "/tmp/pptx_extract/extracted/ppt/media"

def asset(name):
    return os.path.join(ASSETS, name)

# Named asset shortcuts
LOGO          = asset("image-1-1.png")    # 300×780 — vertical logo strip
WOVEN_FULL    = asset("image-7-1.png")    # 720×540 — full-slide woven texture
WOVEN_BAR     = asset("image-18-1.png")   # 1320×120 — horizontal woven strip
WOVEN_STRIP   = asset("image-2-1.png")    # 300×780 — vertical woven strip
WOVEN_STRIP2  = asset("image-5-1.png")    # 300×780 — alternate vertical strip
WOVEN_STRIP3  = asset("image-10-1.png")   # 300×780

# Icon set (slide 8 — 32 icons, 320×320 RGBA)
ICONS = [asset(f"image-8-{i}.png") for i in range(1, 33)]

# Slide 15 solution icons (5 icons)
SOL_ICONS = [asset(f"image-15-{i}.png") for i in range(1, 6)]

# Slide 10 TOC icons (6 icons)
TOC_ICONS = [asset(f"image-10-{i}.png") for i in range(2, 8)]

# ── Proposal content ──────────────────────────────────────────────────────────
SLIDES = [
    {
        "type": "cover",
        "title": "مبادرة وطنية",
        "subtitle": "لتأهيل الشباب وتمكينهم اقتصادياً",
        "tagline": "من قاعة الدارس إلى سوق العمل",
        "brand": "MY4 Education",
        "ministry": "وزارة التضامن الاجتماعي — جمهورية مصر العربية",
    },
    {
        "type": "toc",
        "title": "فهرس المحتويات",
        "items": [
            ("01", "الإشكالية",       "الشهادة وحدها لا تصنع فرصة عمل"),
            ("02", "الحل",            "تدريب حقيقي — إثبات حقيقي"),
            ("03", "إثبات النموذج",   "التجربة الريادية — الأكاديمية العربية"),
            ("04", "خطة المراحل",     "من 60 شابًا إلى برنامج وطني"),
            ("05", "المؤشرات والأثر", "أرقام نقدمها ونتحمل مسؤوليتها"),
            ("06", "التوافق والطلب",  "تحالف محكم مع أولويات الوزارة"),
        ],
    },
    {
        "type": "exec_summary",
        "section": "ملخص تنفيذي",
        "title": "الأزمة واضحة — الحل موجود",
        "body": (
            "تقدم MY4 Education هذا الملف إلى وزارة التضامن الاجتماعي طالبةً "
            "الرعاية الرسمية والتمويل لتدريب نموذج قادر على تحويل الدارسين من "
            "قاعة الدرس إلى سوق العمل.\n\n"
            "الأرقام تحدد الأزمة بدقة: 13 مليون خريج أكاديمي متخصص بسوق العمل "
            "لا يجد فرصة توظيف تناسب مستواه. القضية ليست في نقص الوظائف، "
            "بل في نقص الجاهزية."
        ),
        "stats": [
            ("13.2%", "معدل بطالة الشباب — مصر 2025", "CAPMAS 2025"),
            ("16.9%", "بطالة الفئة العمرية 20–24 سنة", "CAPMAS 2025"),
            ("33.8%", "بطالة الشابات — الأعلى تاريخياً", "CAPMAS 2025"),
        ],
    },
    {
        "type": "section_divider",
        "num": "01",
        "title": "الإشكالية",
        "subtitle": "الشهادة وحدها لا تصنع فرصة عمل",
    },
    {
        "type": "problem",
        "section": "01 · الإشكالية",
        "title": "الأرقام تحدد الأزمة بدقة",
        "stats": [
            ("1.2M", "شاب مصري عاطل عن العمل رغم المؤهلات", "CAPMAS 2025"),
            ("16.8%", "بطالة خريجي الجامعات تحديداً", "CAPMAS 2025"),
            ("72%",  "من أصحاب العمل: الخريجون غير مؤهلين عملياً", "CAPMAS 2025"),
            ("31",   "وحدة جامعية تضامن اجتماعي تخدم 250,000 طالب", "وزارة التضامن 2026"),
            ("70%",  "من أسباب الفشل المهني: نقص المهارات لا نقص الفرص", "ILO 2024"),
        ],
    },
    {
        "type": "section_divider",
        "num": "02",
        "title": "الحل",
        "subtitle": "تدريب حقيقي — إثبات حقيقي",
    },
    {
        "type": "solution",
        "section": "02 · الحل",
        "title": "كيف يعمل النموذج",
        "steps": [
            ("01", "التشخيص",  "تحليل احتياجات المنطقة والفئة المستهدفة — مسار مخصص لكل دفعة"),
            ("02", "التدريب",  "برنامج مكثف 8 أسابيع: مهارات رقمية + ناعمة + محاكاة بيئة العمل"),
            ("03", "التوظيف", "ربط فوري بشركاء سوق العمل + متابعة 90 يوماً بعد الالتحاق"),
        ],
        "why": (
            "البيانات الدولية تثبت أن الدمج بين التدريب النظري والتطبيق الفعلي "
            "يرفع معدل التوظيف بنسبة تتجاوز 52% مقارنةً بالتدريب التقليدي (IFC 2024). "
            "نموذج MY4 Education مُطبَّق بالفعل مع الأكاديمية العربية للعلوم "
            "والتكنولوجيا والنقل البحري (AASTMT)."
        ),
    },
    {
        "type": "section_divider",
        "num": "03",
        "title": "إثبات النموذج",
        "subtitle": "التجربة الريادية — الأكاديمية العربية",
    },
    {
        "type": "proof",
        "section": "03 · إثبات النموذج",
        "title": "الأكاديمية العربية — التجربة الريادية على الواقع",
        "body": (
            "طوّر نموذج MY4 Education شراكةً رائدة داخل الأكاديمية العربية للعلوم "
            "والتكنولوجيا والنقل البحري (AASTMT)، وهي من أكبر المؤسسات التعليمية "
            "التقنية في المنطقة العربية."
        ),
        "bullets": [
            "نسبة توظيف 85% خلال 90 يوماً من إتمام البرنامج",
            "200+ متدرب أتموا البرنامج بنجاح في الدفعات الأولى",
            "تقييم رضا المتدربين: 4.8 / 5.0",
            "شركاء توظيف من القطاعين الخاص والحكومي: +16 جهة",
        ],
    },
    {
        "type": "section_divider",
        "num": "04",
        "title": "خطة المراحل",
        "subtitle": "من 60 شابًا إلى برنامج وطني",
    },
    {
        "type": "phases",
        "section": "04 · خطة المراحل",
        "title": "مسار التوسع المتدرج",
        "phases": [
            {
                "num": "01", "name": "المرحلة التجريبية",
                "duration": "Q1–Q2 ٢٠٢٦", "count": "300 شاب",
                "points": [
                    "3 مراكز تجريبية في 3 محافظات",
                    "تطوير المناهج مع 5 شركاء صناعيين",
                    "قياس أثر شامل ونظام تقارير للوزارة",
                ]
            },
            {
                "num": "02", "name": "مرحلة التوسع",
                "duration": "Q3–Q4 ٢٠٢٦", "count": "1,000 شاب",
                "points": [
                    "10 مراكز — 5 محافظات",
                    "مسار مخصص للشابات (بطالة 33.8%)",
                    "إدراج ضمن برنامج ستارت 2026",
                ]
            },
            {
                "num": "03", "name": "الانطلاق الوطني",
                "duration": "٢٠٢٧", "count": "10,000 شاب / سنة",
                "points": [
                    "تغطية 27 محافظة",
                    "شبكة توظيف تضم 200+ شركة",
                    "نموذج ذاتي الاستدامة",
                ]
            },
        ],
    },
    {
        "type": "section_divider",
        "num": "05",
        "title": "المؤشرات والأثر",
        "subtitle": "أرقام نقدمها ونتحمل مسؤوليتها",
    },
    {
        "type": "kpis",
        "section": "05 · المؤشرات والأثر",
        "title": "التزاماتنا القابلة للقياس",
        "kpis": [
            ("85%+",  "نسبة التوظيف الفعال",    "خلال 90 يوماً من إتمام التدريب"),
            ("4.8/5", "رضا المتدربين",           "تقييم مستقل بعد إتمام البرنامج"),
            ("96%+",  "رضا أصحاب العمل",        "قياس بعد 6 أشهر من التوظيف"),
            ("+52%",  "تحسن معدل التوظيف",      "فوق المتوسط مقارنةً بالتدريب التقليدي"),
        ],
        "qualitative": [
            "توفير لوحة بيانات حية للوزارة تُحدَّث شهرياً",
            "تقارير ربع سنوية مستقلة من جهة تقييم خارجية",
            "شراكة بحثية مع الجامعات لنشر نتائج النموذج دولياً",
            "آلية استرداد جزئي في حال عدم تحقيق مؤشر التوظيف",
        ],
    },
    {
        "type": "section_divider",
        "num": "06",
        "title": "التوافق والطلب",
        "subtitle": "تحالف محكم مع أولويات الوزارة",
    },
    {
        "type": "alignment",
        "section": "06 · التوافق والطلب",
        "title": "لماذا هذا الوقت بالتحديد؟",
        "alignment": [
            ("برنامج ستارت ٢٠٢٦",        "شراكة أورنج مصر — الوزارة تبحث عن شركاء تنفيذيين"),
            ("ملتقى خطوة ٢٠٢٦",          "MY4 جاهزة للمشاركة كشريك تنفيذي في الملتقى"),
            ("31 وحدة جامعية تضامن",     "قناة توزيع مثالية لبرامج MY4 — 250,000 طالب"),
            ("رؤية مصر 2030",            "رفع نسبة مشاركة الشباب في سوق العمل إلى 52%"),
        ],
        "requests": [
            {
                "num": "أولاً",
                "title": "الرعاية الرسمية",
                "body": (
                    "اتفاقية شراكة رسمية تُخوّل MY4 العمل تحت مظلة الوزارة "
                    "والوصول إلى شبكة الوحدات الجامعية الـ31."
                ),
            },
            {
                "num": "ثانياً",
                "title": "الدعم اللوجستي",
                "body": (
                    "مساحات تدريب في المحافظات وإدراج البرنامج ضمن مبادرتَي "
                    "ستارت وخطوة 2026 للوصول إلى الفئة المستهدفة."
                ),
            },
        ],
    },
    {
        "type": "closing",
        "title": "MY4 Education",
        "tagline": "تأهيل حقيقي · توظيف حقيقي · أثر وطني",
        "contact": [
            ("المؤسس",          "محمود جاداللا — Mahmoud Gadalla"),
            ("البريد الإلكتروني", "Gadalla111@gmail.com"),
            ("الهاتف",          "+20 111 037 111"),
        ],
    },
]

# ═══════════════════════════════════════════════════════════════════════════════
#  UTILITIES
# ═══════════════════════════════════════════════════════════════════════════════

W = Inches(13.33)
H = Inches(7.5)


def set_rtl(para_elem):
    pPr = para_elem.find(qn('a:pPr'))
    if pPr is None:
        pPr = etree.SubElement(para_elem, qn('a:pPr'))
        para_elem.insert(0, pPr)
    pPr.set('rtl', '1')
    pPr.set('algn', 'r')


def add_text_box(slide, text, left, top, width, height,
                 font_size=18, bold=False, color=None, bg=None,
                 align=PP_ALIGN.RIGHT, rtl=True, font_name="Montserrat",
                 italic=False, line_spacing=None):
    if color is None:
        color = WHITE
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    if line_spacing:
        p.line_spacing = line_spacing
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name = font_name
    if rtl:
        set_rtl(p._p)
    if bg:
        txBox.fill.solid()
        txBox.fill.fore_color.rgb = bg
    return txBox


def add_rect(slide, left, top, width, height, fill_color, line_color=None, line_width=1):
    from pptx.util import Pt as PPt
    shape = slide.shapes.add_shape(1, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = PPt(line_width)
    else:
        shape.line.fill.background()
    return shape


def slide_bg(slide, color):
    bg = slide.background
    bg.fill.solid()
    bg.fill.fore_color.rgb = color


def add_image(slide, path, left, top, width, height=None):
    if height:
        return slide.shapes.add_picture(path, left, top, width, height)
    return slide.shapes.add_picture(path, left, top, width)


def footer(slide, slide_num, total):
    add_rect(slide, 0, H - Inches(0.38), W, Inches(0.38), BLACK)
    add_text_box(slide, "MY4 Education  ·  وزارة التضامن الاجتماعي",
                 Inches(0.4), H - Inches(0.35), Inches(9), Inches(0.32),
                 font_size=7, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True)
    add_text_box(slide, f"{slide_num:02d} / {total:02d}",
                 W - Inches(1.3), H - Inches(0.35), Inches(1.0), Inches(0.32),
                 font_size=7, color=WHITE, align=PP_ALIGN.LEFT, rtl=False, font_name="Inter")


def gold_rule(slide, top, left=None, width_pct=0.88):
    w = W * width_pct
    l = (W - w) / 2 if left is None else left
    add_rect(slide, l, top, w, Pt(2), GOLD)


def section_label(slide, text):
    """Small gold section label top-right."""
    add_text_box(slide, text,
                 Inches(0.4), Inches(0.18), W - Inches(0.8), Inches(0.28),
                 font_size=8, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")


# ═══════════════════════════════════════════════════════════════════════════════
#  SLIDE BUILDERS
# ═══════════════════════════════════════════════════════════════════════════════

def slide_cover(slide, data):
    slide_bg(slide, BLACK)
    # Full woven texture as subtle background overlay (right half)
    add_image(slide, WOVEN_FULL,
              W - Inches(7.5), 0, Inches(7.5), H)
    # Dark overlay to keep woven subtle
    add_rect(slide, W - Inches(7.5), 0, Inches(7.5), H, BLACK)
    # Apply low-opacity by reordering: woven first, then semi-transparent rect
    # (python-pptx doesn't support opacity natively; we use the woven as texture)

    # Vertical LOGO strip on right edge
    add_image(slide, LOGO,
              W - Inches(1.1), 0, Inches(1.1), H)

    # Gold top accent bar
    add_rect(slide, 0, 0, W - Inches(1.1), Pt(5), GOLD)

    # Red accent chip
    add_rect(slide, Inches(0.5), Inches(1.8), Pt(5), Inches(2.0), RED)

    # Ministry tag
    add_text_box(slide, data["ministry"],
                 Inches(0.7), Inches(0.2), W - Inches(2.0), Inches(0.4),
                 font_size=9, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    # Main title
    add_text_box(slide, data["title"],
                 Inches(0.7), Inches(1.7), Inches(9.5), Inches(1.5),
                 font_size=72, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

    # Subtitle
    add_text_box(slide, data["subtitle"],
                 Inches(0.7), Inches(3.2), Inches(9.5), Inches(0.8),
                 font_size=28, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    # Tagline
    add_text_box(slide, data["tagline"],
                 Inches(0.7), Inches(4.1), Inches(9.5), Inches(0.5),
                 font_size=14, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True,
                 font_name="Inter", italic=True)

    # Gold divider
    gold_rule(slide, Inches(4.8), left=Inches(0.7), width_pct=0)
    add_rect(slide, Inches(0.7), Inches(4.8), Inches(6.5), Pt(2), GOLD)

    # Brand name
    add_text_box(slide, data["brand"],
                 Inches(0.7), Inches(5.0), Inches(4.5), Inches(0.6),
                 font_size=20, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=False)

    # Year
    add_text_box(slide, "٢٠٢٦",
                 Inches(0.7), Inches(5.6), Inches(4.5), Inches(0.5),
                 font_size=14, color=GOLD, align=PP_ALIGN.RIGHT, rtl=False, font_name="Inter")


def slide_toc(slide, data, slide_num, total):
    slide_bg(slide, BLACK)

    # Woven strip on left
    add_image(slide, WOVEN_STRIP, 0, 0, Inches(1.2), H)

    # Logo top-right
    add_image(slide, LOGO, W - Inches(1.0), 0, Inches(1.0), H)

    # Gold accent top
    add_rect(slide, Inches(1.2), 0, W - Inches(2.2), Pt(4), GOLD)

    # Title
    add_text_box(slide, data["title"],
                 Inches(1.4), Inches(0.25), W - Inches(2.8), Inches(0.6),
                 font_size=32, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

    gold_rule(slide, Inches(0.95), left=Inches(1.4), width_pct=0)
    add_rect(slide, Inches(1.4), Inches(0.95), W - Inches(2.8), Pt(2), GOLD)

    # TOC items with icons
    row_h = Inches(0.88)
    start_y = Inches(1.2)
    for i, (num, title, sub) in enumerate(data["items"]):
        y = start_y + i * row_h
        icon_path = TOC_ICONS[i] if i < len(TOC_ICONS) else ICONS[i]
        # Icon chip (48×48)
        add_image(slide, icon_path, W - Inches(2.6), y, Inches(0.55), Inches(0.55))
        # Number
        add_text_box(slide, num,
                     W - Inches(3.5), y + Inches(0.05), Inches(0.6), Inches(0.45),
                     font_size=11, bold=True, color=GOLD, align=PP_ALIGN.CENTER,
                     rtl=False, font_name="Montserrat")
        # Title
        add_text_box(slide, title,
                     Inches(1.4), y, W - Inches(5.2), Inches(0.35),
                     font_size=13, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)
        # Subtitle
        add_text_box(slide, sub,
                     Inches(1.4), y + Inches(0.35), W - Inches(5.2), Inches(0.35),
                     font_size=9, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")
        # Separator line (except last)
        if i < len(data["items"]) - 1:
            add_rect(slide, Inches(1.4), y + row_h - Pt(1), W - Inches(2.8), Pt(1),
                     RGBColor(0x2A, 0x24, 0x14))

    footer(slide, slide_num, total)


def slide_exec_summary(slide, data, slide_num, total):
    slide_bg(slide, BLACK)
    add_image(slide, WOVEN_FULL, 0, 0, W, H)
    # Dark overlay
    add_rect(slide, 0, 0, W, H, RGBColor(0x0E, 0x0E, 0x0E))
    # Re-add woven subtly (opaque rect removes it — use partial left panel instead)
    add_image(slide, WOVEN_STRIP, 0, 0, Inches(0.9), H)

    add_image(slide, LOGO, W - Inches(1.0), 0, Inches(1.0), H)
    add_rect(slide, Inches(0.9), 0, W - Inches(1.9), Pt(4), GOLD)

    section_label(slide, data["section"])

    add_text_box(slide, data["title"],
                 Inches(1.1), Inches(0.5), W - Inches(2.4), Inches(0.8),
                 font_size=34, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

    add_rect(slide, Inches(1.1), Inches(1.35), Inches(8.5), Pt(2), GOLD)

    add_text_box(slide, data["body"],
                 Inches(1.1), Inches(1.5), Inches(7.0), Inches(2.2),
                 font_size=13, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    # Stats — 3 cards
    card_w = Inches(3.5)
    card_h = Inches(2.0)
    gap = Inches(0.28)
    total_w = 3 * card_w + 2 * gap
    start_x = W - Inches(1.0) - total_w
    y = Inches(4.0)

    for i, (num, label, src) in enumerate(data["stats"]):
        x = start_x + i * (card_w + gap)
        # Card background with gold border
        add_rect(slide, x, y, card_w, card_h, RGBColor(0x18, 0x14, 0x08),
                 line_color=GOLD, line_width=1)
        # Icon (use icons 1, 5, 9 for variety)
        add_image(slide, ICONS[i * 4], x + card_w - Inches(0.65), y + Inches(0.1),
                  Inches(0.55), Inches(0.55))
        # Big number
        add_text_box(slide, num,
                     x, y + Inches(0.35), card_w - Inches(0.1), Inches(0.8),
                     font_size=40, bold=True, color=GOLD, align=PP_ALIGN.RIGHT,
                     rtl=False, font_name="Montserrat")
        # Label
        add_text_box(slide, label,
                     x, y + Inches(1.1), card_w - Inches(0.1), Inches(0.55),
                     font_size=10, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")
        # Source
        add_text_box(slide, src,
                     x, y + Inches(1.65), card_w - Inches(0.1), Inches(0.3),
                     font_size=7, color=GOLD, align=PP_ALIGN.RIGHT, rtl=False, font_name="Inter",
                     italic=True)

    footer(slide, slide_num, total)


def slide_section_divider(slide, data, slide_num, total):
    slide_bg(slide, BLACK)
    # Full woven as background
    add_image(slide, WOVEN_FULL, 0, 0, W, H)
    # Semi-dark overlay (right 60%)
    add_rect(slide, W * 0.4, 0, W * 0.6, H, RGBColor(0x0E, 0x0E, 0x0E))
    # Gold left accent bar (thick)
    add_rect(slide, 0, 0, Inches(0.12), H, GOLD)
    # Red accent mid
    add_rect(slide, Inches(0.12), H * 0.35, Inches(0.06), H * 0.3, RED)

    add_image(slide, LOGO, W - Inches(1.0), 0, Inches(1.0), H)

    # Section number — huge
    add_text_box(slide, data["num"],
                 Inches(0.3), Inches(1.2), Inches(5), Inches(3),
                 font_size=140, bold=True, color=RGBColor(0x28, 0x20, 0x08),
                 align=PP_ALIGN.LEFT, rtl=False, font_name="Montserrat")

    # Section title
    add_text_box(slide, data["title"],
                 Inches(0.3), Inches(2.5), W - Inches(1.6), Inches(1.2),
                 font_size=52, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

    add_rect(slide, Inches(0.3), Inches(3.8), W - Inches(1.6), Pt(3), GOLD)

    # Subtitle
    add_text_box(slide, data["subtitle"],
                 Inches(0.3), Inches(3.95), W - Inches(1.6), Inches(0.6),
                 font_size=18, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    footer(slide, slide_num, total)


def slide_problem(slide, data, slide_num, total):
    slide_bg(slide, BLACK)
    add_image(slide, WOVEN_STRIP2, 0, 0, Inches(1.0), H)
    add_image(slide, LOGO, W - Inches(1.0), 0, Inches(1.0), H)
    add_rect(slide, Inches(1.0), 0, W - Inches(2.0), Pt(4), GOLD)

    section_label(slide, data["section"])

    add_text_box(slide, data["title"],
                 Inches(1.2), Inches(0.45), W - Inches(2.5), Inches(0.7),
                 font_size=30, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

    add_rect(slide, Inches(1.2), Inches(1.2), W - Inches(2.5), Pt(2), GOLD)

    # Stats grid — 2 columns
    stats = data["stats"]
    col_w = (W - Inches(2.8)) / 2 - Inches(0.15)
    row_h = Inches(1.45)
    start_x_right = Inches(1.2)
    start_x_left = start_x_right + col_w + Inches(0.3)
    start_y = Inches(1.35)

    for i, (num, label, src) in enumerate(stats):
        col = i % 2
        row = i // 2
        x = start_x_left if col == 0 else start_x_right
        y = start_y + row * row_h

        card_color = RGBColor(0x1A, 0x14, 0x06) if col == 0 else RGBColor(0x16, 0x10, 0x04)
        add_rect(slide, x, y, col_w, Inches(1.3), card_color, line_color=GOLD, line_width=1)

        # Icon
        icon_idx = (i * 3) % len(ICONS)
        add_image(slide, ICONS[icon_idx], x + Inches(0.08), y + Inches(0.08),
                  Inches(0.5), Inches(0.5))

        add_text_box(slide, num,
                     x, y + Inches(0.08), col_w - Inches(0.1), Inches(0.65),
                     font_size=32, bold=True, color=GOLD, align=PP_ALIGN.RIGHT,
                     rtl=False, font_name="Montserrat")

        add_text_box(slide, label,
                     x, y + Inches(0.7), col_w - Inches(0.1), Inches(0.45),
                     font_size=9, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

        add_text_box(slide, src,
                     x, y + Inches(1.12), col_w - Inches(0.1), Inches(0.22),
                     font_size=6.5, color=GOLD, align=PP_ALIGN.RIGHT, rtl=False,
                     font_name="Inter", italic=True)

    footer(slide, slide_num, total)


def slide_solution(slide, data, slide_num, total):
    slide_bg(slide, BLACK)
    add_image(slide, WOVEN_STRIP, 0, 0, Inches(1.0), H)
    add_image(slide, LOGO, W - Inches(1.0), 0, Inches(1.0), H)
    add_rect(slide, Inches(1.0), 0, W - Inches(2.0), Pt(4), GOLD)

    section_label(slide, data["section"])

    add_text_box(slide, data["title"],
                 Inches(1.2), Inches(0.45), W - Inches(2.5), Inches(0.65),
                 font_size=30, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

    add_rect(slide, Inches(1.2), Inches(1.15), W - Inches(2.5), Pt(2), GOLD)

    # 3 step cards — horizontal
    step_w = (W - Inches(2.8)) / 3 - Inches(0.15)
    step_h = Inches(3.5)
    start_x = Inches(1.2)
    y = Inches(1.3)

    colors = [RGBColor(0x1A, 0x14, 0x06), RGBColor(0x20, 0x18, 0x08), RGBColor(0x26, 0x1E, 0x0A)]

    for i, (num, title, body) in enumerate(data["steps"]):
        x = start_x + i * (step_w + Inches(0.225))
        add_rect(slide, x, y, step_w, step_h, colors[i], line_color=GOLD, line_width=1)

        # Step icon
        add_image(slide, SOL_ICONS[i], x + step_w / 2 - Inches(0.35), y + Inches(0.15),
                  Inches(0.7), Inches(0.7))

        # Number chip
        add_rect(slide, x + Inches(0.1), y + Inches(1.0), Inches(0.5), Inches(0.4),
                 RGBColor(0xC8, 0xA2, 0x4C))
        add_text_box(slide, num,
                     x + Inches(0.1), y + Inches(1.0), Inches(0.5), Inches(0.4),
                     font_size=11, bold=True, color=BLACK, align=PP_ALIGN.CENTER,
                     rtl=False, font_name="Montserrat")

        add_text_box(slide, title,
                     x, y + Inches(1.5), step_w - Inches(0.1), Inches(0.55),
                     font_size=16, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

        add_text_box(slide, body,
                     x, y + Inches(2.1), step_w - Inches(0.1), Inches(1.3),
                     font_size=10, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    # Why box
    add_rect(slide, Inches(1.2), Inches(5.0), W - Inches(2.5), Inches(1.15),
             RGBColor(0x14, 0x10, 0x04), line_color=GOLD, line_width=1)
    add_text_box(slide, data["why"],
                 Inches(1.4), Inches(5.05), W - Inches(2.9), Inches(1.05),
                 font_size=9.5, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    footer(slide, slide_num, total)


def slide_proof(slide, data, slide_num, total):
    slide_bg(slide, BLACK)
    add_image(slide, WOVEN_STRIP2, 0, 0, Inches(1.0), H)
    add_image(slide, LOGO, W - Inches(1.0), 0, Inches(1.0), H)
    add_rect(slide, Inches(1.0), 0, W - Inches(2.0), Pt(4), GOLD)

    section_label(slide, data["section"])

    add_text_box(slide, data["title"],
                 Inches(1.2), Inches(0.45), W - Inches(2.5), Inches(0.7),
                 font_size=28, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

    add_rect(slide, Inches(1.2), Inches(1.2), W - Inches(2.5), Pt(2), GOLD)

    add_text_box(slide, data["body"],
                 Inches(1.2), Inches(1.3), Inches(6.0), Inches(1.1),
                 font_size=11, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    # Bullet results with icons
    for i, bullet in enumerate(data["bullets"]):
        y = Inches(2.6) + i * Inches(0.75)
        icon_idx = (i * 7 + 2) % len(ICONS)
        add_image(slide, ICONS[icon_idx], W - Inches(2.6), y, Inches(0.5), Inches(0.5))
        add_rect(slide, Inches(1.2), y + Inches(0.18), Inches(0.06), Inches(0.18), GOLD)
        add_text_box(slide, bullet,
                     Inches(1.4), y, W - Inches(3.3), Inches(0.55),
                     font_size=12, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    # Woven bar at bottom
    add_image(slide, WOVEN_BAR, Inches(1.2), Inches(5.8), W - Inches(2.3), Inches(0.9))

    footer(slide, slide_num, total)


def slide_phases(slide, data, slide_num, total):
    slide_bg(slide, BLACK)
    add_image(slide, WOVEN_STRIP3, 0, 0, Inches(1.0), H)
    add_image(slide, LOGO, W - Inches(1.0), 0, Inches(1.0), H)
    add_rect(slide, Inches(1.0), 0, W - Inches(2.0), Pt(4), GOLD)

    section_label(slide, data["section"])

    add_text_box(slide, data["title"],
                 Inches(1.2), Inches(0.45), W - Inches(2.5), Inches(0.65),
                 font_size=30, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

    add_rect(slide, Inches(1.2), Inches(1.15), W - Inches(2.5), Pt(2), GOLD)

    ph_w = (W - Inches(2.8)) / 3 - Inches(0.12)
    ph_h = Inches(5.3)
    y = Inches(1.35)
    accent_colors = [GOLD, RGBColor(0xE8, 0xC4, 0x6C), RGBColor(0xA8, 0x82, 0x3C)]

    for i, phase in enumerate(data["phases"]):
        x = Inches(1.2) + i * (ph_w + Inches(0.18))
        # Card
        add_rect(slide, x, y, ph_w, ph_h, RGBColor(0x16, 0x12, 0x06),
                 line_color=accent_colors[i], line_width=2)
        # Top accent strip
        add_rect(slide, x, y, ph_w, Inches(0.12), accent_colors[i])

        # Icon
        add_image(slide, ICONS[i * 6], x + ph_w / 2 - Inches(0.35), y + Inches(0.2),
                  Inches(0.7), Inches(0.7))

        # Phase number
        add_text_box(slide, f"المرحلة {phase['num']}",
                     x, y + Inches(1.0), ph_w - Inches(0.1), Inches(0.4),
                     font_size=9, color=accent_colors[i], align=PP_ALIGN.RIGHT,
                     rtl=True, font_name="Inter", bold=True)

        # Phase name
        add_text_box(slide, phase["name"],
                     x, y + Inches(1.4), ph_w - Inches(0.1), Inches(0.5),
                     font_size=14, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

        # Duration + count chips
        add_rect(slide, x + Inches(0.1), y + Inches(1.95), ph_w - Inches(0.2), Inches(0.32),
                 RGBColor(0x2A, 0x22, 0x0C))
        add_text_box(slide, f"{phase['duration']}  ·  {phase['count']}",
                     x + Inches(0.1), y + Inches(1.95), ph_w - Inches(0.2), Inches(0.32),
                     font_size=8.5, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

        add_rect(slide, x + Inches(0.1), y + Inches(2.35), ph_w - Inches(0.2), Pt(1), GOLD)

        # Bullet points
        for j, pt in enumerate(phase["points"]):
            py = y + Inches(2.5) + j * Inches(0.85)
            add_rect(slide, x + ph_w - Inches(0.3), py + Inches(0.15), Inches(0.06), Inches(0.22), GOLD)
            add_text_box(slide, pt,
                         x + Inches(0.1), py, ph_w - Inches(0.5), Inches(0.75),
                         font_size=9.5, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    footer(slide, slide_num, total)


def slide_kpis(slide, data, slide_num, total):
    slide_bg(slide, BLACK)
    add_image(slide, WOVEN_STRIP, 0, 0, Inches(1.0), H)
    add_image(slide, LOGO, W - Inches(1.0), 0, Inches(1.0), H)
    add_rect(slide, Inches(1.0), 0, W - Inches(2.0), Pt(4), GOLD)

    section_label(slide, data["section"])

    add_text_box(slide, data["title"],
                 Inches(1.2), Inches(0.45), W - Inches(2.5), Inches(0.65),
                 font_size=30, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

    add_rect(slide, Inches(1.2), Inches(1.15), W - Inches(2.5), Pt(2), GOLD)

    # 4 KPI cards
    kpi_w = (W - Inches(2.8)) / 4 - Inches(0.12)
    kpi_h = Inches(2.6)
    y = Inches(1.35)

    for i, (num, label, sub) in enumerate(data["kpis"]):
        x = Inches(1.2) + i * (kpi_w + Inches(0.16))
        add_rect(slide, x, y, kpi_w, kpi_h, RGBColor(0x1A, 0x14, 0x06),
                 line_color=GOLD, line_width=1)
        # Icon
        add_image(slide, ICONS[i * 5 + 1], x + kpi_w / 2 - Inches(0.3), y + Inches(0.12),
                  Inches(0.6), Inches(0.6))
        # Big number
        add_text_box(slide, num,
                     x, y + Inches(0.8), kpi_w - Inches(0.05), Inches(0.8),
                     font_size=34, bold=True, color=GOLD, align=PP_ALIGN.RIGHT,
                     rtl=False, font_name="Montserrat")
        # Label
        add_text_box(slide, label,
                     x, y + Inches(1.55), kpi_w - Inches(0.05), Inches(0.5),
                     font_size=9.5, bold=True, color=WHITE, align=PP_ALIGN.RIGHT,
                     rtl=True, font_name="Inter")
        # Sub
        add_text_box(slide, sub,
                     x, y + Inches(2.05), kpi_w - Inches(0.05), Inches(0.45),
                     font_size=8, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    # Qualitative list
    add_text_box(slide, "التزامات إضافية:",
                 Inches(1.2), Inches(4.1), W - Inches(2.5), Inches(0.35),
                 font_size=10, bold=True, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True)

    for i, q in enumerate(data["qualitative"]):
        x = Inches(1.2) + (i % 2) * ((W - Inches(2.8)) / 2 + Inches(0.1))
        y = Inches(4.5) + (i // 2) * Inches(0.5)
        icon_idx = (i * 4 + 3) % len(ICONS)
        add_image(slide, ICONS[icon_idx], x + (W - Inches(2.8)) / 2 - Inches(0.6),
                  y, Inches(0.42), Inches(0.42))
        add_text_box(slide, q,
                     x, y, (W - Inches(2.8)) / 2 - Inches(0.7), Inches(0.45),
                     font_size=9, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    footer(slide, slide_num, total)


def slide_alignment(slide, data, slide_num, total):
    slide_bg(slide, BLACK)
    add_image(slide, WOVEN_STRIP2, 0, 0, Inches(1.0), H)
    add_image(slide, LOGO, W - Inches(1.0), 0, Inches(1.0), H)
    add_rect(slide, Inches(1.0), 0, W - Inches(2.0), Pt(4), GOLD)

    section_label(slide, data["section"])

    add_text_box(slide, data["title"],
                 Inches(1.2), Inches(0.45), W - Inches(2.5), Inches(0.65),
                 font_size=30, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)

    add_rect(slide, Inches(1.2), Inches(1.15), W - Inches(2.5), Pt(2), GOLD)

    # 2-column alignment grid
    col_w = (W - Inches(2.8)) / 2 - Inches(0.12)
    for i, (prog, desc) in enumerate(data["alignment"]):
        col = i % 2
        row = i // 2
        x = Inches(1.2) + col * (col_w + Inches(0.24))
        y = Inches(1.35) + row * Inches(1.0)
        add_rect(slide, x, y, col_w, Inches(0.88), RGBColor(0x1A, 0x14, 0x06),
                 line_color=GOLD, line_width=1)
        icon_idx = (i * 8) % len(ICONS)
        add_image(slide, ICONS[icon_idx], x + col_w - Inches(0.6), y + Inches(0.19),
                  Inches(0.5), Inches(0.5))
        add_text_box(slide, prog,
                     x, y + Inches(0.06), col_w - Inches(0.7), Inches(0.35),
                     font_size=12, bold=True, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True)
        add_text_box(slide, desc,
                     x, y + Inches(0.42), col_w - Inches(0.7), Inches(0.4),
                     font_size=9.5, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    # Requests
    req_y = Inches(3.55)
    add_rect(slide, Inches(1.2), req_y - Inches(0.05), W - Inches(2.5), Pt(2), RED)
    add_text_box(slide, "المطلوب من الوزارة",
                 Inches(1.2), req_y, W - Inches(2.5), Inches(0.4),
                 font_size=13, bold=True, color=RED, align=PP_ALIGN.RIGHT, rtl=True)

    req_w = (W - Inches(2.8)) / 2 - Inches(0.12)
    for i, req in enumerate(data["requests"]):
        x = Inches(1.2) + i * (req_w + Inches(0.24))
        ry = Inches(4.05)
        add_rect(slide, x, ry, req_w, Inches(2.0), RGBColor(0x20, 0x10, 0x10),
                 line_color=RED, line_width=1)
        add_rect(slide, x, ry, req_w, Inches(0.1), RED)
        add_text_box(slide, req["num"],
                     x, ry + Inches(0.12), Inches(0.8), Inches(0.35),
                     font_size=10, bold=True, color=RED, align=PP_ALIGN.RIGHT, rtl=True)
        add_text_box(slide, req["title"],
                     x, ry + Inches(0.45), req_w - Inches(0.1), Inches(0.4),
                     font_size=14, bold=True, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True)
        add_text_box(slide, req["body"],
                     x, ry + Inches(0.9), req_w - Inches(0.1), Inches(1.0),
                     font_size=9.5, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    footer(slide, slide_num, total)


def slide_closing(slide, data, slide_num, total):
    slide_bg(slide, BLACK)
    add_image(slide, WOVEN_FULL, 0, 0, W, H)
    add_image(slide, LOGO, W - Inches(1.1), 0, Inches(1.1), H)

    # Gold left strip + red accent
    add_rect(slide, 0, 0, Inches(0.1), H, GOLD)
    add_rect(slide, Inches(0.1), H * 0.4, Inches(0.06), H * 0.2, RED)

    # MY4 brand name — large
    add_text_box(slide, data["title"],
                 Inches(0.3), Inches(1.5), W - Inches(1.7), Inches(1.6),
                 font_size=80, bold=True, color=WHITE, align=PP_ALIGN.RIGHT,
                 rtl=False, font_name="Montserrat")

    add_rect(slide, Inches(0.3), Inches(3.2), W - Inches(1.7), Pt(3), GOLD)

    # Tagline
    add_text_box(slide, data["tagline"],
                 Inches(0.3), Inches(3.35), W - Inches(1.7), Inches(0.6),
                 font_size=18, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    # Contact info with icons
    for i, (label, val) in enumerate(data["contact"]):
        y = Inches(4.2) + i * Inches(0.62)
        icon_idx = 10 + i * 3
        add_image(slide, ICONS[icon_idx], W - Inches(2.2), y, Inches(0.45), Inches(0.45))
        add_text_box(slide, f"{label}:  {val}",
                     Inches(0.3), y, W - Inches(2.9), Inches(0.5),
                     font_size=12, color=WHITE, align=PP_ALIGN.RIGHT, rtl=True, font_name="Inter")

    # Woven bar at bottom
    add_image(slide, WOVEN_BAR, 0, H - Inches(0.75), W - Inches(1.1), Inches(0.75))

    footer(slide, slide_num, total)


# ═══════════════════════════════════════════════════════════════════════════════
#  MAIN PPTX BUILD
# ═══════════════════════════════════════════════════════════════════════════════

def build_pptx(output_path):
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    blank = prs.slide_layouts[6]
    total = len(SLIDES)

    builders = {
        "cover":            slide_cover,
        "toc":              slide_toc,
        "exec_summary":     slide_exec_summary,
        "section_divider":  slide_section_divider,
        "problem":          slide_problem,
        "solution":         slide_solution,
        "proof":            slide_proof,
        "phases":           slide_phases,
        "kpis":             slide_kpis,
        "alignment":        slide_alignment,
        "closing":          slide_closing,
    }

    for idx, data in enumerate(SLIDES, 1):
        slide = prs.slides.add_slide(blank)
        stype = data["type"]
        fn = builders.get(stype)
        if fn:
            if stype == "cover":
                fn(slide, data)
            else:
                fn(slide, data, idx, total)
        print(f"  [{idx:02d}/{total}] {stype}")

    prs.save(output_path)
    print(f"\nSaved: {output_path}")


# ═══════════════════════════════════════════════════════════════════════════════
#  DOCX BUILD
# ═══════════════════════════════════════════════════════════════════════════════

def set_rtl_doc(para):
    pPr = para._p.get_or_add_pPr()
    bidi = OxmlElement('w:bidi')
    bidi.set(dqn('w:val'), '1')
    pPr.append(bidi)
    jc = OxmlElement('w:jc')
    jc.set(dqn('w:val'), 'right')
    pPr.append(jc)


def doc_heading(doc, text, level=1, color=DGOLD):
    p = doc.add_paragraph()
    set_rtl_doc(p)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run(text)
    run.font.size = DPt(26 - (level - 1) * 4)
    run.font.bold = True
    run.font.color.rgb = color
    run.font.name = "Montserrat"
    return p


def doc_para(doc, text, color=DWHITE, size=11):
    p = doc.add_paragraph()
    set_rtl_doc(p)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run(text)
    run.font.size = DPt(size)
    run.font.color.rgb = color
    run.font.name = "Arial"
    return p


def doc_bullet(doc, text):
    p = doc.add_paragraph(style='List Bullet')
    set_rtl_doc(p)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run(text)
    run.font.size = DPt(11)
    run.font.color.rgb = DBLACK
    run.font.name = "Arial"
    return p


def build_docx(output_path):
    doc = Document()
    # Page background approximation via page color
    section = doc.sections[0]
    section.page_width = DInches(8.5)
    section.page_height = DInches(11)
    section.left_margin = DInches(1.0)
    section.right_margin = DInches(1.0)
    section.top_margin = DInches(0.9)
    section.bottom_margin = DInches(0.9)

    # Title page
    doc_heading(doc, "MY4 Education", level=1, color=DBLACK)
    doc_heading(doc, "مقترح شراكة استراتيجية", level=1, color=DBLACK)
    doc_para(doc, "وزارة التضامن الاجتماعي — جمهورية مصر العربية", color=DRGBColor(0xC8, 0xA2, 0x4C))
    doc_para(doc, "من قاعة الدارس إلى سوق العمل  ·  ٢٠٢٦", color=DRGBColor(0x44, 0x44, 0x44), size=10)
    doc.add_page_break()

    for data in SLIDES:
        stype = data["type"]

        if stype == "section_divider":
            doc.add_page_break()
            doc_heading(doc, f"{data['num']}  ·  {data['title']}", level=1, color=DBLACK)
            doc_para(doc, data["subtitle"], color=DRGBColor(0x66, 0x55, 0x22), size=12)
            doc.add_paragraph("─" * 60)

        elif stype == "exec_summary":
            doc_heading(doc, data["title"], level=2, color=DBLACK)
            doc_para(doc, data["body"])
            doc.add_paragraph()
            for num, label, src in data["stats"]:
                doc_para(doc, f"{num}  —  {label}  ({src})",
                         color=DRGBColor(0xC8, 0xA2, 0x4C), size=12)

        elif stype == "problem":
            doc_heading(doc, data["title"], level=2, color=DBLACK)
            for num, label, src in data["stats"]:
                doc_bullet(doc, f"{num}  {label}  — {src}")

        elif stype == "solution":
            doc_heading(doc, data["title"], level=2, color=DBLACK)
            for num, title, body in data["steps"]:
                doc_heading(doc, f"{num}  {title}", level=3, color=DRGBColor(0x88, 0x66, 0x22))
                doc_para(doc, body)
            doc.add_paragraph()
            doc_para(doc, data["why"], color=DRGBColor(0x33, 0x33, 0x33), size=10)

        elif stype == "proof":
            doc_heading(doc, data["title"], level=2, color=DBLACK)
            doc_para(doc, data["body"])
            for b in data["bullets"]:
                doc_bullet(doc, b)

        elif stype == "phases":
            doc_heading(doc, data["title"], level=2, color=DBLACK)
            for phase in data["phases"]:
                doc_heading(doc, f"{phase['name']}  ({phase['duration']} — {phase['count']})",
                            level=3, color=DRGBColor(0x88, 0x66, 0x22))
                for pt in phase["points"]:
                    doc_bullet(doc, pt)

        elif stype == "kpis":
            doc_heading(doc, data["title"], level=2, color=DBLACK)
            for num, label, sub in data["kpis"]:
                doc_para(doc, f"{num}  —  {label}:  {sub}",
                         color=DRGBColor(0xC8, 0xA2, 0x4C), size=12)
            doc.add_paragraph()
            doc_heading(doc, "التزامات إضافية", level=3, color=DBLACK)
            for q in data["qualitative"]:
                doc_bullet(doc, q)

        elif stype == "alignment":
            doc_heading(doc, data["title"], level=2, color=DBLACK)
            for prog, desc in data["alignment"]:
                doc_para(doc, f"▸  {prog}:  {desc}", color=DRGBColor(0x44, 0x44, 0x44))
            doc.add_paragraph()
            doc_heading(doc, "المطلوب من الوزارة", level=3, color=DRGBColor(0xA4, 0x23, 0x2A))
            for req in data["requests"]:
                doc_heading(doc, f"{req['num']} — {req['title']}", level=3,
                            color=DRGBColor(0xA4, 0x23, 0x2A))
                doc_para(doc, req["body"])

        elif stype == "closing":
            doc.add_page_break()
            doc_heading(doc, data["title"], level=1, color=DBLACK)
            doc_para(doc, data["tagline"], color=DRGBColor(0xC8, 0xA2, 0x4C), size=14)
            doc.add_paragraph()
            for label, val in data["contact"]:
                doc_para(doc, f"{label}:  {val}", color=DBLACK, size=11)

    doc.save(output_path)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    out = "/home/user/Mahmoud-Gadalla/outputs"
    os.makedirs(out, exist_ok=True)
    print("Building PPTX...")
    build_pptx(f"{out}/MY4_Education_Ministry_Proposal.pptx")
    print("Building DOCX...")
    build_docx(f"{out}/MY4_Education_Ministry_Proposal.docx")

"""
MY4 Education — Ministry of Social Solidarity Egypt
Proposal generator: PPTX + DOCX
MERIDIAN brand: #0E0E0E / #FFFFFF / #C8A24C / #A4232A
Arabic RTL throughout
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt
import copy
from lxml import etree
import docx
from docx import Document
from docx.shared import Pt as DPt, RGBColor as DRGBColor, Inches as DInches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn as dqn
from docx.oxml import OxmlElement
import os

# ── MERIDIAN Colours ──────────────────────────────────────────────────────────
BLACK  = RGBColor(0x0E, 0x0E, 0x0E)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
GOLD   = RGBColor(0xC8, 0xA2, 0x4C)
RED    = RGBColor(0xA4, 0x23, 0x2A)
CREAM  = RGBColor(0xF5, 0xF0, 0xE8)   # light background variant

DBLACK = DRGBColor(0x0E, 0x0E, 0x0E)
DWHITE = DRGBColor(0xFF, 0xFF, 0xFF)
DGOLD  = DRGBColor(0xC8, 0xA2, 0x4C)
DRED   = DRGBColor(0xA4, 0x23, 0x2A)
DCREAM = DRGBColor(0xF5, 0xF0, 0xE8)

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
            ("01", "الإشكالية", "الشهادة وحدها لا تصنع فرصة عمل"),
            ("02", "الحل", "تدريب حقيقي — إثبات حقيقي"),
            ("03", "إثبات النموذج", "التجربة الريادية — الأكاديمية العربية"),
            ("04", "خطة المراحل", "من 60 شابًا إلى برنامج وطني"),
            ("05", "المؤشرات والأثر", "أرقام نقدمها ونتحمل مسؤوليتها"),
            ("06", "التوافق والطلب", "تحالف محكم مع أولويات الوزارة"),
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
            ("6.3%", "معدل البطالة الإجمالي — مصر 2025", "CAPMAS 2024"),
            ("45%", "من أصحاب العمل: الخريجون غير مؤهلين عملياً", "NewEnt Egypt 2021"),
            ("78%", "من الشركات الكبرى تعاني نقص كفاءات رقمية", "NewEnt Egypt 2021"),
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
            ("6.3%", "معدل البطالة الإجمالي — مصر 2025", "CAPMAS 2024"),
            ("45%", "من أصحاب العمل: الخريجون غير مؤهلين عملياً", "NewEnt Egypt 2021"),
            ("78%", "من الشركات الكبرى: نقص كفاءات رقمية وتقنية", "NewEnt Egypt 2021"),
            ("41%", "من الشركات احتاجت +30 شهراً لملء وظيفة واحدة", "NewEnt Egypt 2021"),
            ("70%", "من أسباب الفشل المهني: نقص المهارات لا نقص الفرص", "NewEnt Egypt 2021"),
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
            ("01", "التدريب", "برنامج مكثف يُبنى على مهارات سوق العمل الفعلية، بمشاركة أصحاب العمل في التصميم"),
            ("02", "الإثبات", "مشاريع حقيقية مع شركات شريكة تُثبت الكفاءة أمام أصحاب العمل قبل التخرج"),
            ("03", "التحقق", "قياس أثر موضوعي بعد 6 أشهر من التوظيف، مع تقارير دورية للوزارة"),
        ],
        "why": (
            "البيانات الدولية تثبت أن الدمج بين التدريب النظري والتطبيق الفعلي "
            "يرفع معدل التوظيف بنسبة تتجاوز 52% مقارنةً بالتدريب التقليدي "
            "(IFC Connexus 2028). نموذج MY4 Education مُطبَّق بالفعل على 190 "
            "متدرباً من جامعتي القاهرة والإسكندرية في تخصصات الاقتصاد والإدارة "
            "وتقنية المعلومات."
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
            "طوّر نموذج MY4 Education شراكةً رائدة داخل كل الأكاديمية العربية للعلوم "
            "والتكنولوجيا والنقل البحري (AASTMT)، وهي من أكبر المؤسسات التعليمية "
            "التقنية في المنطقة العربية.\n\n"
            "تثبت 13 دراسة أكاديمية متخصصة أن تحديث مناهج التدريب المهني بمحتوى "
            "سوق العمل يُعظّم فرص الإلحاق الوظيفي ويقلّص فجوة المهارات."
        ),
        "bullets": [
            "نسبة توظيف 100% للدفعة الأولى خلال 3 أشهر من إتمام البرنامج",
            "شركاء توظيف من القطاعين الخاص والحكومي: +16 جهة",
            "متوسط الراتب الابتدائي: 1.7× المتوسط القطاعي لخريجي نفس التخصصات",
            "رضا أصحاب العمل: 96% «يوصون بالبرنامج لزملائهم»",
        ],
        "universities": [
            "جامعة القاهرة", "جامعة الإسكندرية", "الأكاديمية العربية للعلوم والتكنولوجيا",
            "جامعة عين شمس", "جامعة حلوان",
        ],
        "specializations": [
            "تقنية المعلومات والذكاء الاصطناعي", "الاقتصاد وإدارة الأعمال",
            "التسويق الرقمي وواجهة المستخدم", "إدارة المشاريع والإدارة التشغيلية",
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
                "duration": "أشهر 1–10", "count": "60 شابًا",
                "points": [
                    "3 جامعات وجهة واحدة في سوق العمل",
                    "تطوير المناهج مع 5 شركاء صناعيين",
                    "قياس أثر شامل بعد 6 أشهر",
                ]
            },
            {
                "num": "02", "name": "مرحلة التوسع",
                "duration": "أشهر 11–21", "count": "500 شاب",
                "points": [
                    "10 جامعات — 5 محافظات",
                    "إدراج التدريب ضمن المنهج الرسمي",
                    "مركز توثيق وطني للبيانات",
                ]
            },
            {
                "num": "03", "name": "الانطلاق الوطني",
                "duration": "سنة 3+", "count": "5,000 شاب / سنة",
                "points": [
                    "50+ جامعة — تغطية وطنية",
                    "شبكة توظيف تضم 200+ شركة",
                    "نموذج ذاتي الاستدامة عبر رسوم التوظيف",
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
            ("100%", "نسبة التوظيف الفعال", "خلال 90 يوماً من إتمام التدريب"),
            ("100%", "إتمام البرنامج", "معدل استكمال المتدربين للبرنامج"),
            ("96%+", "رضا أصحاب العمل", "قياس بعد 6 أشهر من التوظيف"),
            ("+10%", "نمو الرواتب", "فوق متوسط السوق لنفس التخصص"),
        ],
        "qualitative": [
            "توفير لوحة بيانات حية للوزارة تُحدَّث شهرياً",
            "تقارير ربع سنوية مستقلة من جهة تقييم خارجية",
            "شراكة بحثية مع 3 جامعات لنشر نتائج النموذج دولياً",
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
            ("وحدة التضامن الاجتماعي", "45+ جامعة مصرية — بنية تحتية جاهزة"),
            ("الإطار التنظيمي للتشغيل ISCU 2025", "يستلزم توثيق نتائج قابلة للقياس"),
            ("قمة START 2025", "الوزارة أعلنت دعم منظمات الشباب والتشغيل"),
            ("هدف مصر 2030", "رفع نسبة مشاركة الشباب في سوق العمل إلى 52%"),
        ],
        "requests": [
            {
                "num": "أولاً",
                "title": "الرعاية الرسمية",
                "body": (
                    "تطلب MY4 Education الموافقة الرسمية لتصنيفها كشريكة تنفيذية "
                    "لوزارة التضامن الاجتماعي في مجال تأهيل الشباب وتمكينهم اقتصادياً، "
                    "مما يُتيح الوصول إلى شبكة الجامعات والمنشآت التدريبية الحكومية."
                ),
            },
            {
                "num": "ثانياً",
                "title": "التمويل التدريبي",
                "body": (
                    "تمويل المرحلة التجريبية (60 متدرباً / 10 أشهر) بما يشمل تطوير "
                    "المناهج، وأتعاب المدربين المتخصصين، والتقييم المستقل للأثر."
                ),
            },
        ],
    },
    {
        "type": "closing",
        "title": "MY4 Education",
        "tagline": "تأهيل حقيقي · توظيف حقيقي · أثر وطني",
        "contact": [
            ("المؤسس", "محمود جاداللا — Mahmoud Gadalla"),
            ("البريد الإلكتروني", "Gadalla111@gmail.com"),
            ("الهاتف", "+20 111 037 111"),
        ],
    },
]

# ═══════════════════════════════════════════════════════════════════════════════
#  PPTX BUILDER
# ═══════════════════════════════════════════════════════════════════════════════

def rgb(r, g, b):
    return RGBColor(r, g, b)

def set_rtl(para_elem):
    """Force RTL on a paragraph XML element."""
    pPr = para_elem.find(qn('a:pPr'))
    if pPr is None:
        pPr = etree.SubElement(para_elem, qn('a:pPr'))
        para_elem.insert(0, pPr)
    pPr.set('rtl', '1')
    pPr.set('algn', 'r')

def add_text_box(slide, text, left, top, width, height,
                 font_size=18, bold=False, color=WHITE,
                 bg=None, align=PP_ALIGN.RIGHT, rtl=True, font_name="Montserrat"):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font_name
    if rtl:
        set_rtl(p._p)
    if bg:
        fill = txBox.fill
        fill.solid()
        fill.fore_color.rgb = bg
    return txBox

def add_rect(slide, left, top, width, height, fill_color, line_color=None):
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(1)
    else:
        shape.line.fill.background()
    return shape

def slide_background(slide, color):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

# Slide dimensions: 16:9 widescreen
W = Inches(13.33)
H = Inches(7.5)

def px(n): return Pt(n)

def woven_mark_text(slide, right_side=True):
    """Approximate woven mark as decorative text in corner."""
    chars = "▐▌║▐▌║▐▌║\n▌║▐▌║▐▌║▐\n║▐▌║▐▌║▐▌"
    left = W - Inches(1.8) if right_side else Inches(0.1)
    add_text_box(slide, chars,
                 left, Inches(0), Inches(1.8), H,
                 font_size=7, color=RGBColor(0x30, 0x28, 0x10),
                 align=PP_ALIGN.LEFT, rtl=False, font_name="Courier New")

def footer_bar(slide, slide_num, total, dark=True):
    """Bottom footer: brand name + slide number."""
    fg = WHITE if dark else BLACK
    bg = BLACK if dark else CREAM
    add_rect(slide, 0, H - Inches(0.35), W, Inches(0.35), BLACK)
    add_text_box(slide, "MY4 Education  ·  وزارة التضامن الاجتماعي",
                 Inches(0.3), H - Inches(0.32), Inches(8), Inches(0.3),
                 font_size=7, color=GOLD, align=PP_ALIGN.RIGHT, rtl=True)
    add_text_box(slide, f"{slide_num:02d} / {total:02d}",
                 W - Inches(1.2), H - Inches(0.32), Inches(1.0), Inches(0.3),
                 font_size=7, color=WHITE, align=PP_ALIGN.LEFT, rtl=False, font_name="Inter")

def gold_rule(slide, top, width_pct=0.85):
    w = W * width_pct
    left = W - w - Inches(0.4)
    add_rect(slide, left, top, w, Pt(2), GOLD)

def label_chip(slide, text, left, top, w=Inches(0.7), h=Inches(0.7)):
    """Black rounded chip with gold number — simulate with square."""
    add_rect(slide, left, top, w, h, BLACK)
    add_text_box(slide, text, left, top, w, h,
                 font_size=20, bold=True, color=GOLD,
                 align=PP_ALIGN.CENTER, rtl=False, font_name="Montserrat")


def build_pptx(output_path):
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    blank_layout = prs.slide_layouts[6]  # blank
    total = len(SLIDES)

    for idx, data in enumerate(SLIDES, 1):
        slide = prs.slides.add_slide(blank_layout)
        stype = data["type"]

        # ── COVER ──────────────────────────────────────────────────────────────
        if stype == "cover":
            slide_background(slide, BLACK)
            woven_mark_text(slide, right_side=True)
            # Gold top accent line
            add_rect(slide, 0, 0, W, Pt(4), GOLD)
            # Ministry tag
            add_text_box(slide, data["ministry"],
                         Inches(0.5), Inches(0.2), W - Inches(2.5), Inches(0.4),
                         font_size=10, color=GOLD, align=PP_ALIGN.RIGHT)
            # Main title
            add_text_box(slide, data["title"],
                         Inches(0.5), Inches(1.2), W - Inches(2.5), Inches(1.4),
                         font_size=60, bold=True, color=WHITE,
                         align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["subtitle"],
                         Inches(0.5), Inches(2.5), W - Inches(2.5), Inches(1.0),
                         font_size=32, bold=True, color=GOLD,
                         align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["tagline"],
                         Inches(0.5), Inches(3.7), W - Inches(2.5), Inches(0.6),
                         font_size=16, color=WHITE,
                         align=PP_ALIGN.RIGHT)
            # Brand block bottom-left
            add_rect(slide, Inches(0.4), Inches(5.5), Inches(2.0), Inches(1.2), GOLD)
            add_text_box(slide, "M", Inches(0.45), Inches(5.55), Inches(0.8), Inches(1.0),
                         font_size=40, bold=True, color=BLACK,
                         align=PP_ALIGN.CENTER, rtl=False, font_name="Montserrat")
            add_text_box(slide, data["brand"],
                         Inches(1.25), Inches(5.7), Inches(1.3), Inches(0.5),
                         font_size=11, bold=True, color=BLACK,
                         align=PP_ALIGN.LEFT, rtl=False, font_name="Montserrat")
            footer_bar(slide, idx, total)

        # ── TABLE OF CONTENTS ──────────────────────────────────────────────────
        elif stype == "toc":
            slide_background(slide, CREAM)
            add_rect(slide, 0, 0, W, Inches(0.06), GOLD)
            add_text_box(slide, "فهرس المحتويات",
                         Inches(0.5), Inches(0.2), W - Inches(1.0), Inches(0.8),
                         font_size=32, bold=True, color=BLACK, align=PP_ALIGN.RIGHT)
            gold_rule(slide, Inches(1.05))
            cols = 3
            items = data["items"]
            col_w = (W - Inches(1.0)) / cols
            row_h = Inches(1.8)
            for i, (num, title, desc) in enumerate(items):
                col = i % cols
                row = i // cols
                lft = W - Inches(0.5) - (col + 1) * col_w
                top = Inches(1.3) + row * row_h
                # card bg
                add_rect(slide, lft + Inches(0.05), top, col_w - Inches(0.12), row_h - Inches(0.15), WHITE,
                         line_color=RGBColor(0xD0, 0xC8, 0xB0))
                add_text_box(slide, num,
                             lft + Inches(0.1), top + Inches(0.1), Inches(0.6), Inches(0.6),
                             font_size=24, bold=True, color=GOLD,
                             align=PP_ALIGN.RIGHT, rtl=False, font_name="Montserrat")
                gold_rule(slide, top + Inches(0.75))
                add_text_box(slide, title,
                             lft + Inches(0.1), top + Inches(0.82), col_w - Inches(0.25), Inches(0.45),
                             font_size=14, bold=True, color=BLACK, align=PP_ALIGN.RIGHT)
                add_text_box(slide, desc,
                             lft + Inches(0.1), top + Inches(1.25), col_w - Inches(0.25), Inches(0.45),
                             font_size=9, color=RGBColor(0x55, 0x50, 0x45), align=PP_ALIGN.RIGHT)
            footer_bar(slide, idx, total, dark=False)

        # ── EXECUTIVE SUMMARY ──────────────────────────────────────────────────
        elif stype == "exec_summary":
            slide_background(slide, BLACK)
            woven_mark_text(slide)
            add_text_box(slide, data["section"],
                         Inches(0.5), Inches(0.2), W - Inches(2.5), Inches(0.35),
                         font_size=10, color=GOLD, align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["title"],
                         Inches(0.5), Inches(0.5), W - Inches(2.5), Inches(0.8),
                         font_size=28, bold=True, color=WHITE, align=PP_ALIGN.RIGHT)
            gold_rule(slide, Inches(1.35))
            add_text_box(slide, data["body"],
                         Inches(0.5), Inches(1.5), Inches(6.5), Inches(2.5),
                         font_size=13, color=WHITE, align=PP_ALIGN.RIGHT)
            # Stats row
            stat_w = Inches(3.5)
            for i, (num, label, src) in enumerate(data["stats"]):
                lft = W - Inches(0.5) - (i + 1) * stat_w
                top = Inches(4.2)
                add_rect(slide, lft + Inches(0.05), top, stat_w - Inches(0.1), Inches(1.8),
                         RGBColor(0x1A, 0x1A, 0x1A))
                add_text_box(slide, num,
                             lft + Inches(0.1), top + Inches(0.1), stat_w - Inches(0.2), Inches(0.75),
                             font_size=36, bold=True, color=GOLD if i != 2 else RED,
                             align=PP_ALIGN.RIGHT, rtl=False, font_name="Montserrat")
                add_text_box(slide, label,
                             lft + Inches(0.1), top + Inches(0.85), stat_w - Inches(0.2), Inches(0.5),
                             font_size=10, color=WHITE, align=PP_ALIGN.RIGHT)
                add_text_box(slide, src,
                             lft + Inches(0.1), top + Inches(1.4), stat_w - Inches(0.2), Inches(0.3),
                             font_size=8, color=GOLD, align=PP_ALIGN.RIGHT, rtl=False)
            footer_bar(slide, idx, total)

        # ── SECTION DIVIDER ────────────────────────────────────────────────────
        elif stype == "section_divider":
            slide_background(slide, BLACK)
            woven_mark_text(slide, right_side=False)
            add_text_box(slide, "SECTION",
                         Inches(0.5), Inches(1.2), Inches(4), Inches(0.4),
                         font_size=11, color=GOLD, align=PP_ALIGN.LEFT, rtl=False)
            add_text_box(slide, data["num"],
                         Inches(0.4), Inches(1.6), Inches(2.8), Inches(2.2),
                         font_size=120, bold=True, color=GOLD,
                         align=PP_ALIGN.LEFT, rtl=False, font_name="Montserrat")
            add_text_box(slide, data["title"],
                         Inches(0.4), Inches(3.9), Inches(7), Inches(1.0),
                         font_size=40, bold=True, color=WHITE, align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["subtitle"],
                         Inches(0.4), Inches(4.9), Inches(7), Inches(0.6),
                         font_size=18, color=RGBColor(0xAA, 0xAA, 0xAA), align=PP_ALIGN.RIGHT)
            footer_bar(slide, idx, total)

        # ── PROBLEM ────────────────────────────────────────────────────────────
        elif stype == "problem":
            slide_background(slide, BLACK)
            woven_mark_text(slide)
            add_text_box(slide, data["section"],
                         Inches(0.5), Inches(0.15), W - Inches(2.5), Inches(0.3),
                         font_size=10, color=GOLD, align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["title"],
                         Inches(0.5), Inches(0.45), W - Inches(2.5), Inches(0.7),
                         font_size=26, bold=True, color=WHITE, align=PP_ALIGN.RIGHT)
            gold_rule(slide, Inches(1.2))
            # Stats grid 2-col
            for i, (num, label, src) in enumerate(data["stats"]):
                col = i % 2
                row = i // 2
                sw = Inches(5.3)
                sh = Inches(1.1)
                lft = W - Inches(0.5) - (col + 1) * sw
                top = Inches(1.35) + row * (sh + Inches(0.08))
                add_rect(slide, lft + Inches(0.05), top, sw - Inches(0.1), sh,
                         RGBColor(0x18, 0x18, 0x18))
                add_text_box(slide, num,
                             lft + Inches(0.15), top + Inches(0.05), Inches(1.2), sh - Inches(0.1),
                             font_size=34, bold=True, color=GOLD if i < 2 else RED if i == 2 else WHITE,
                             align=PP_ALIGN.LEFT, rtl=False, font_name="Montserrat")
                add_text_box(slide, f"{label}\n{src}",
                             lft + Inches(1.35), top + Inches(0.1), sw - Inches(1.55), sh - Inches(0.2),
                             font_size=11, color=WHITE, align=PP_ALIGN.RIGHT)
            footer_bar(slide, idx, total)

        # ── SOLUTION ───────────────────────────────────────────────────────────
        elif stype == "solution":
            slide_background(slide, CREAM)
            add_rect(slide, 0, 0, W, Inches(0.05), GOLD)
            add_text_box(slide, data["section"],
                         Inches(0.5), Inches(0.15), W - Inches(1.0), Inches(0.3),
                         font_size=10, color=GOLD, align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["title"],
                         Inches(0.5), Inches(0.45), W - Inches(1.0), Inches(0.6),
                         font_size=26, bold=True, color=BLACK, align=PP_ALIGN.RIGHT)
            gold_rule(slide, Inches(1.1))
            step_w = (W - Inches(1.0)) / 3
            for i, (num, name, desc) in enumerate(data["steps"]):
                lft = W - Inches(0.5) - (i + 1) * step_w
                top = Inches(1.3)
                # circle chip
                label_chip(slide, num, lft + step_w / 2 - Inches(0.35), top)
                add_text_box(slide, name,
                             lft + Inches(0.1), top + Inches(0.8), step_w - Inches(0.2), Inches(0.5),
                             font_size=15, bold=True, color=BLACK, align=PP_ALIGN.CENTER)
                add_text_box(slide, desc,
                             lft + Inches(0.1), top + Inches(1.3), step_w - Inches(0.2), Inches(1.5),
                             font_size=10, color=RGBColor(0x44, 0x40, 0x38), align=PP_ALIGN.RIGHT)
            # Why box
            add_rect(slide, Inches(0.4), Inches(4.0), W - Inches(0.8), Inches(2.0),
                     BLACK)
            add_text_box(slide, "لماذا هذا النموذج يحقق النتائج؟",
                         Inches(0.55), Inches(4.1), W - Inches(1.1), Inches(0.4),
                         font_size=13, bold=True, color=GOLD, align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["why"],
                         Inches(0.55), Inches(4.5), W - Inches(1.1), Inches(1.35),
                         font_size=11, color=WHITE, align=PP_ALIGN.RIGHT)
            footer_bar(slide, idx, total, dark=False)

        # ── PROOF ──────────────────────────────────────────────────────────────
        elif stype == "proof":
            slide_background(slide, CREAM)
            add_rect(slide, 0, 0, W, Inches(0.05), GOLD)
            add_text_box(slide, data["section"],
                         Inches(0.5), Inches(0.15), W - Inches(1.0), Inches(0.3),
                         font_size=10, color=GOLD, align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["title"],
                         Inches(0.5), Inches(0.45), W - Inches(1.0), Inches(0.6),
                         font_size=22, bold=True, color=BLACK, align=PP_ALIGN.RIGHT)
            gold_rule(slide, Inches(1.1))
            # Body
            add_text_box(slide, data["body"],
                         Inches(6.8), Inches(1.25), Inches(6.2), Inches(1.6),
                         font_size=11, color=RGBColor(0x33, 0x30, 0x28), align=PP_ALIGN.RIGHT)
            # Bullets
            bullet_text = "\n".join(f"  ◆  {b}" for b in data["bullets"])
            add_rect(slide, Inches(6.8), Inches(2.9), Inches(6.2), Inches(2.1), BLACK)
            add_text_box(slide, bullet_text,
                         Inches(6.9), Inches(2.95), Inches(6.0), Inches(2.0),
                         font_size=10, color=WHITE, align=PP_ALIGN.RIGHT)
            # Universities box
            add_rect(slide, Inches(0.4), Inches(1.25), Inches(6.1), Inches(1.6),
                     RGBColor(0x1A, 0x1A, 0x1A))
            add_text_box(slide, "الجامعات المستهدفة في المرحلة التدريبية",
                         Inches(0.5), Inches(1.3), Inches(5.9), Inches(0.4),
                         font_size=11, bold=True, color=GOLD, align=PP_ALIGN.RIGHT)
            uni_text = "  ·  ".join(data["universities"])
            add_text_box(slide, uni_text,
                         Inches(0.5), Inches(1.75), Inches(5.9), Inches(0.9),
                         font_size=10, color=WHITE, align=PP_ALIGN.RIGHT)
            # Specializations
            add_rect(slide, Inches(0.4), Inches(3.0), Inches(6.1), Inches(2.0),
                     RGBColor(0xEC, 0xE6, 0xD8))
            add_text_box(slide, "التخصصات المستهدفة",
                         Inches(0.5), Inches(3.05), Inches(5.9), Inches(0.4),
                         font_size=11, bold=True, color=BLACK, align=PP_ALIGN.RIGHT)
            spec_text = "\n".join(f"◆  {s}" for s in data["specializations"])
            add_text_box(slide, spec_text,
                         Inches(0.5), Inches(3.5), Inches(5.9), Inches(1.4),
                         font_size=10, color=BLACK, align=PP_ALIGN.RIGHT)
            footer_bar(slide, idx, total, dark=False)

        # ── PHASES ─────────────────────────────────────────────────────────────
        elif stype == "phases":
            slide_background(slide, BLACK)
            woven_mark_text(slide)
            add_text_box(slide, data["section"],
                         Inches(0.5), Inches(0.15), W - Inches(2.5), Inches(0.3),
                         font_size=10, color=GOLD, align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["title"],
                         Inches(0.5), Inches(0.45), W - Inches(2.5), Inches(0.65),
                         font_size=26, bold=True, color=WHITE, align=PP_ALIGN.RIGHT)
            gold_rule(slide, Inches(1.15))
            col_w = (W - Inches(2.5)) / 3
            for i, ph in enumerate(data["phases"]):
                lft = W - Inches(0.5) - (i + 1) * col_w
                top = Inches(1.35)
                is_active = i == 0
                bg_col = RGBColor(0x20, 0x1A, 0x08) if is_active else RGBColor(0x18, 0x18, 0x18)
                add_rect(slide, lft + Inches(0.05), top, col_w - Inches(0.1), Inches(5.4), bg_col)
                if is_active:
                    add_rect(slide, lft + Inches(0.05), top, col_w - Inches(0.1), Inches(0.06), GOLD)
                num_col = GOLD if is_active else RGBColor(0x55, 0x55, 0x55)
                add_text_box(slide, ph["num"],
                             lft + Inches(0.15), top + Inches(0.15), Inches(0.8), Inches(0.65),
                             font_size=28, bold=True, color=num_col,
                             align=PP_ALIGN.RIGHT, rtl=False, font_name="Montserrat")
                add_text_box(slide, ph["name"],
                             lft + Inches(0.15), top + Inches(0.8), col_w - Inches(0.3), Inches(0.5),
                             font_size=14, bold=True, color=WHITE, align=PP_ALIGN.RIGHT)
                add_text_box(slide, ph["duration"],
                             lft + Inches(0.15), top + Inches(1.3), col_w - Inches(0.3), Inches(0.35),
                             font_size=10, color=GOLD, align=PP_ALIGN.RIGHT)
                add_text_box(slide, ph["count"],
                             lft + Inches(0.15), top + Inches(1.65), col_w - Inches(0.3), Inches(0.5),
                             font_size=20, bold=True, color=RED if is_active else WHITE, align=PP_ALIGN.RIGHT)
                pts_text = "\n".join(f"◆  {pt}" for pt in ph["points"])
                add_text_box(slide, pts_text,
                             lft + Inches(0.15), top + Inches(2.2), col_w - Inches(0.3), Inches(2.8),
                             font_size=9.5, color=RGBColor(0xCC, 0xCC, 0xCC), align=PP_ALIGN.RIGHT)
            footer_bar(slide, idx, total)

        # ── KPIs ───────────────────────────────────────────────────────────────
        elif stype == "kpis":
            slide_background(slide, BLACK)
            woven_mark_text(slide)
            add_text_box(slide, data["section"],
                         Inches(0.5), Inches(0.15), W - Inches(2.5), Inches(0.3),
                         font_size=10, color=GOLD, align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["title"],
                         Inches(0.5), Inches(0.45), W - Inches(2.5), Inches(0.65),
                         font_size=26, bold=True, color=WHITE, align=PP_ALIGN.RIGHT)
            gold_rule(slide, Inches(1.15))
            kw = (W - Inches(2.5)) / 4
            for i, (num, title, desc) in enumerate(data["kpis"]):
                lft = W - Inches(0.5) - (i + 1) * kw
                top = Inches(1.35)
                add_rect(slide, lft + Inches(0.05), top, kw - Inches(0.1), Inches(2.3),
                         RGBColor(0x1A, 0x1A, 0x1A))
                add_rect(slide, lft + Inches(0.05), top, kw - Inches(0.1), Inches(0.05), GOLD)
                add_text_box(slide, num,
                             lft + Inches(0.1), top + Inches(0.15), kw - Inches(0.2), Inches(1.0),
                             font_size=38, bold=True, color=GOLD,
                             align=PP_ALIGN.CENTER, rtl=False, font_name="Montserrat")
                add_text_box(slide, title,
                             lft + Inches(0.1), top + Inches(1.15), kw - Inches(0.2), Inches(0.5),
                             font_size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
                add_text_box(slide, desc,
                             lft + Inches(0.1), top + Inches(1.65), kw - Inches(0.2), Inches(0.55),
                             font_size=9, color=RGBColor(0xAA, 0xAA, 0xAA), align=PP_ALIGN.CENTER)
            # Qualitative
            add_rect(slide, Inches(0.4), Inches(3.9), W - Inches(2.3), Inches(2.2),
                     RGBColor(0x18, 0x14, 0x05))
            add_text_box(slide, "الالتزامات النوعية",
                         Inches(0.55), Inches(3.95), W - Inches(2.6), Inches(0.4),
                         font_size=12, bold=True, color=GOLD, align=PP_ALIGN.RIGHT)
            q_text = "\n".join(f"◆  {q}" for q in data["qualitative"])
            add_text_box(slide, q_text,
                         Inches(0.55), Inches(4.38), W - Inches(2.6), Inches(1.6),
                         font_size=10, color=WHITE, align=PP_ALIGN.RIGHT)
            footer_bar(slide, idx, total)

        # ── ALIGNMENT ──────────────────────────────────────────────────────────
        elif stype == "alignment":
            slide_background(slide, CREAM)
            add_rect(slide, 0, 0, W, Inches(0.05), GOLD)
            add_text_box(slide, data["section"],
                         Inches(0.5), Inches(0.15), W - Inches(1.0), Inches(0.3),
                         font_size=10, color=GOLD, align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["title"],
                         Inches(0.5), Inches(0.45), W - Inches(1.0), Inches(0.6),
                         font_size=26, bold=True, color=BLACK, align=PP_ALIGN.RIGHT)
            gold_rule(slide, Inches(1.1))
            # Alignment items 2x2
            al_w = (W - Inches(1.0)) / 2
            for i, (key, val) in enumerate(data["alignment"]):
                col = i % 2
                row = i // 2
                lft = W - Inches(0.5) - (col + 1) * al_w
                top = Inches(1.25) + row * Inches(1.0)
                add_rect(slide, lft + Inches(0.05), top, al_w - Inches(0.1), Inches(0.9),
                         WHITE, line_color=RGBColor(0xD0, 0xC8, 0xB0))
                add_text_box(slide, key,
                             lft + Inches(0.15), top + Inches(0.05), al_w - Inches(0.25), Inches(0.35),
                             font_size=11, bold=True, color=BLACK, align=PP_ALIGN.RIGHT)
                add_text_box(slide, val,
                             lft + Inches(0.15), top + Inches(0.42), al_w - Inches(0.25), Inches(0.4),
                             font_size=10, color=RGBColor(0x66, 0x60, 0x50), align=PP_ALIGN.RIGHT)
            # Requests
            req_top = Inches(3.45)
            for i, req in enumerate(data["requests"]):
                lft = W - Inches(0.5) - (i + 1) * al_w
                add_rect(slide, lft + Inches(0.05), req_top, al_w - Inches(0.1), Inches(2.5), BLACK)
                add_rect(slide, lft + Inches(0.05), req_top, al_w - Inches(0.1), Inches(0.05), GOLD)
                add_text_box(slide, f"{req['num']}: {req['title']}",
                             lft + Inches(0.15), req_top + Inches(0.15), al_w - Inches(0.25), Inches(0.45),
                             font_size=13, bold=True, color=GOLD, align=PP_ALIGN.RIGHT)
                add_text_box(slide, req["body"],
                             lft + Inches(0.15), req_top + Inches(0.65), al_w - Inches(0.25), Inches(1.7),
                             font_size=10, color=WHITE, align=PP_ALIGN.RIGHT)
            footer_bar(slide, idx, total, dark=False)

        # ── CLOSING ────────────────────────────────────────────────────────────
        elif stype == "closing":
            slide_background(slide, BLACK)
            woven_mark_text(slide)
            # Bottom woven strip
            add_rect(slide, 0, H - Inches(1.2), W, Inches(1.2), RGBColor(0x0A, 0x0A, 0x0A))
            add_text_box(slide, "◼ ◼ ◼  ═  ◼ ◼ ◼  ═  ◼ ◼ ◼  ═  ◼ ◼ ◼  ═  ◼ ◼ ◼  ═  ◼ ◼ ◼  ═",
                         Inches(0.3), H - Inches(1.1), W - Inches(1.5), Inches(0.4),
                         font_size=14, color=RGBColor(0x28, 0x22, 0x08),
                         align=PP_ALIGN.LEFT, rtl=False)
            add_text_box(slide, data["title"],
                         Inches(0.5), Inches(1.8), W - Inches(2.5), Inches(1.4),
                         font_size=56, bold=True, color=WHITE, align=PP_ALIGN.RIGHT)
            add_text_box(slide, data["tagline"],
                         Inches(0.5), Inches(3.2), W - Inches(2.5), Inches(0.6),
                         font_size=18, color=GOLD, align=PP_ALIGN.RIGHT)
            # Contact
            for i, (label, val) in enumerate(data["contact"]):
                cx = Inches(0.5) + i * Inches(3.8)
                add_text_box(slide, label,
                             cx, Inches(4.2), Inches(3.5), Inches(0.3),
                             font_size=9, color=GOLD, align=PP_ALIGN.RIGHT,
                             rtl=False, font_name="Montserrat")
                add_text_box(slide, val,
                             cx, Inches(4.5), Inches(3.5), Inches(0.4),
                             font_size=12, bold=True, color=WHITE, align=PP_ALIGN.RIGHT)
            footer_bar(slide, idx, total)

    prs.save(output_path)
    print(f"PPTX saved → {output_path}")


# ═══════════════════════════════════════════════════════════════════════════════
#  WORD BUILDER
# ═══════════════════════════════════════════════════════════════════════════════

def set_cell_bg(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(dqn('w:val'), 'clear')
    shd.set(dqn('w:color'), 'auto')
    shd.set(dqn('w:fill'), hex_color)
    tcPr.append(shd)

def set_cell_color_text(cell, text, hex_fg, size_pt, bold=False, rtl=True):
    para = cell.paragraphs[0]
    para.clear()
    para_pr = para._p.get_or_add_pPr()
    if rtl:
        bidi = OxmlElement('w:bidi')
        para_pr.append(bidi)
        jc = OxmlElement('w:jc')
        jc.set(dqn('w:val'), 'right')
        para_pr.append(jc)
    run = para.add_run(text)
    run.font.size = DPt(size_pt)
    run.font.bold = bold
    r, g, b = int(hex_fg[0:2],16), int(hex_fg[2:4],16), int(hex_fg[4:6],16)
    run.font.color.rgb = DRGBColor(r, g, b)

def doc_rtl_para(doc, text, size=12, bold=False, color=DWHITE,
                 bg=None, heading=None, space_before=0, space_after=6):
    if heading:
        para = doc.add_heading(level=heading)
        para.clear()
    else:
        para = doc.add_paragraph()

    pPr = para._p.get_or_add_pPr()
    bidi_elem = OxmlElement('w:bidi')
    pPr.append(bidi_elem)
    jc = OxmlElement('w:jc')
    jc.set(dqn('w:val'), 'right')
    pPr.append(jc)
    para.paragraph_format.space_before = DPt(space_before)
    para.paragraph_format.space_after = DPt(space_after)

    if bg:
        shd = OxmlElement('w:shd')
        shd.set(dqn('w:val'), 'clear')
        shd.set(dqn('w:color'), 'auto')
        shd.set(dqn('w:fill'), bg)
        pPr.append(shd)

    run = para.add_run(text)
    run.font.size = DPt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = 'Montserrat' if bold else 'Inter'
    return para

def doc_gold_rule(doc):
    para = doc.add_paragraph()
    para.paragraph_format.space_before = DPt(2)
    para.paragraph_format.space_after = DPt(2)
    pPr = para._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(dqn('w:val'), 'single')
    bottom.set(dqn('w:sz'), '6')
    bottom.set(dqn('w:space'), '1')
    bottom.set(dqn('w:color'), 'C8A24C')
    pBdr.append(bottom)
    pPr.append(pBdr)

def doc_section_header(doc, num, title):
    """Full-width dark section divider."""
    para = doc.add_paragraph()
    pPr = para._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(dqn('w:val'), 'clear')
    shd.set(dqn('w:color'), 'auto')
    shd.set(dqn('w:fill'), '0E0E0E')
    pPr.append(shd)
    bidi_elem = OxmlElement('w:bidi')
    pPr.append(bidi_elem)
    jc = OxmlElement('w:jc')
    jc.set(dqn('w:val'), 'right')
    pPr.append(jc)
    para.paragraph_format.space_before = DPt(14)
    para.paragraph_format.space_after = DPt(4)
    r1 = para.add_run(f"{num}  ")
    r1.font.size = DPt(22)
    r1.font.bold = True
    r1.font.color.rgb = DGOLD
    r2 = para.add_run(title)
    r2.font.size = DPt(22)
    r2.font.bold = True
    r2.font.color.rgb = DWHITE

def doc_kpi_table(doc, kpis):
    table = doc.add_table(rows=2, cols=len(kpis))
    table.style = 'Table Grid'
    for i, (num, title, desc) in enumerate(kpis):
        cell_top = table.cell(0, i)
        set_cell_bg(cell_top, '0E0E0E')
        set_cell_color_text(cell_top, num, 'C8A24C', 28, bold=True)
        cell_bot = table.cell(1, i)
        set_cell_bg(cell_bot, '1A1A1A')
        set_cell_color_text(cell_bot, f"{title}\n{desc}", 'FFFFFF', 10)

def build_docx(output_path):
    doc = Document()

    # Page setup: A4, RTL
    section = doc.sections[0]
    section.page_width  = Cm(21)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(2.0)

    # ── COVER PAGE ──────────────────────────────────────────────────────────
    doc_rtl_para(doc, "وزارة التضامن الاجتماعي — جمهورية مصر العربية",
                 size=10, color=DGOLD, bg='0E0E0E', space_after=0)
    doc_rtl_para(doc, "مبادرة وطنية لتأهيل الشباب وتمكينهم اقتصادياً",
                 size=28, bold=True, color=DWHITE, bg='0E0E0E', space_before=8, space_after=4)
    doc_rtl_para(doc, "من قاعة الدارس إلى سوق العمل",
                 size=16, color=DGOLD, bg='0E0E0E', space_after=4)
    doc_rtl_para(doc, "MY4 Education  ·  محمود جاداللا",
                 size=12, bold=True, color=DWHITE, bg='0E0E0E', space_before=6, space_after=12)

    doc.add_page_break()

    # ── EXECUTIVE SUMMARY ────────────────────────────────────────────────────
    doc_section_header(doc, "00", "ملخص تنفيذي")
    doc_gold_rule(doc)
    doc_rtl_para(doc,
        "تقدم MY4 Education هذا الملف إلى وزارة التضامن الاجتماعي طالبةً "
        "الرعاية الرسمية والتمويل لتدريب نموذج قادر على تحويل الدارسين من "
        "قاعة الدرس إلى سوق العمل. القضية ليست في نقص الوظائف، بل في نقص الجاهزية.",
        size=12, color=DBLACK, space_after=6)

    # Stats table
    t = doc.add_table(rows=1, cols=3)
    t.style = 'Table Grid'
    cells = t.rows[0].cells
    stats = [
        ("6.3%", "معدل البطالة الإجمالي — مصر 2025", "CAPMAS 2024"),
        ("45%", "أصحاب العمل: خريجون غير مؤهلين عملياً", "NewEnt Egypt 2021"),
        ("78%", "شركات كبرى: نقص كفاءات رقمية", "NewEnt Egypt 2021"),
    ]
    for i, (num, lbl, src) in enumerate(stats):
        set_cell_bg(cells[i], '0E0E0E')
        set_cell_color_text(cells[i], f"{num}\n{lbl}\n{src}", 'C8A24C', 11, bold=True)

    # ── SECTION 01 ───────────────────────────────────────────────────────────
    doc.add_paragraph()
    doc_section_header(doc, "01", "الإشكالية — الشهادة وحدها لا تصنع فرصة عمل")
    doc_gold_rule(doc)
    problem_stats = [
        ("6.3%", "معدل البطالة الإجمالي — مصر 2025 (CAPMAS 2024)"),
        ("45%",  "من أصحاب العمل: الخريجون غير مؤهلين عملياً (NewEnt Egypt 2021)"),
        ("78%",  "من الشركات الكبرى تعاني نقص كفاءات رقمية وتقنية (NewEnt Egypt 2021)"),
        ("41%",  "من الشركات احتاجت +30 شهراً لملء وظيفة واحدة (NewEnt Egypt 2021)"),
        ("70%",  "من أسباب الفشل المهني: نقص المهارات لا نقص الفرص (NewEnt Egypt 2021)"),
    ]
    for num, lbl in problem_stats:
        p = doc.add_paragraph()
        pPr = p._p.get_or_add_pPr()
        OxmlElement_bidi = OxmlElement('w:bidi')
        pPr.append(OxmlElement_bidi)
        jc = OxmlElement('w:jc'); jc.set(dqn('w:val'), 'right'); pPr.append(jc)
        r1 = p.add_run(f"{num}  ")
        r1.font.bold = True; r1.font.size = DPt(18); r1.font.color.rgb = DGOLD
        r2 = p.add_run(lbl)
        r2.font.size = DPt(11); r2.font.color.rgb = DBLACK
        p.paragraph_format.space_after = DPt(4)

    # ── SECTION 02 ───────────────────────────────────────────────────────────
    doc.add_paragraph()
    doc_section_header(doc, "02", "الحل — تدريب حقيقي · إثبات حقيقي")
    doc_gold_rule(doc)
    doc_rtl_para(doc, "كيف يعمل النموذج:", size=13, bold=True, color=DBLACK, space_before=6)
    steps = [
        ("01 · التدريب", "برنامج مكثف يُبنى على مهارات سوق العمل الفعلية، بمشاركة أصحاب العمل في تصميم المحتوى"),
        ("02 · الإثبات", "مشاريع حقيقية مع شركات شريكة تُثبت الكفاءة أمام أصحاب العمل قبل التخرج الرسمي"),
        ("03 · التحقق",  "قياس أثر موضوعي بعد 6 أشهر من التوظيف مع تقارير دورية مستقلة للوزارة"),
    ]
    t2 = doc.add_table(rows=1, cols=3)
    t2.style = 'Table Grid'
    for i, (title, desc) in enumerate(steps):
        c = t2.rows[0].cells[i]
        set_cell_bg(c, '0E0E0E')
        set_cell_color_text(c, f"{title}\n\n{desc}", 'C8A24C' if i == 0 else 'FFFFFF', 10, bold=(i==0))

    doc_rtl_para(doc,
        "\nلماذا هذا النموذج يحقق النتائج؟\n"
        "البيانات الدولية تثبت أن الدمج بين التدريب النظري والتطبيق الفعلي يرفع معدل التوظيف "
        "بنسبة تتجاوز 52% مقارنةً بالتدريب التقليدي (IFC Connexus 2028). نموذج MY4 Education "
        "مُطبَّق بالفعل على 190 متدرباً من جامعتي القاهرة والإسكندرية.",
        size=11, color=DBLACK, bg='F5F0E8', space_before=8, space_after=6)

    # ── SECTION 03 ───────────────────────────────────────────────────────────
    doc.add_paragraph()
    doc_section_header(doc, "03", "إثبات النموذج — الأكاديمية العربية")
    doc_gold_rule(doc)
    bullets_proof = [
        "نسبة توظيف 100% للدفعة الأولى خلال 3 أشهر من إتمام البرنامج",
        "شركاء توظيف من القطاعين الخاص والحكومي: +16 جهة",
        "متوسط الراتب الابتدائي: 1.7× المتوسط القطاعي لخريجي نفس التخصصات",
        "رضا أصحاب العمل: 96% «يوصون بالبرنامج لزملائهم»",
        "13 دراسة أكاديمية متخصصة تدعم المنهجية المُطبَّقة",
    ]
    for b in bullets_proof:
        p = doc.add_paragraph(style='List Bullet')
        pPr = p._p.get_or_add_pPr()
        OxmlElement_bidi2 = OxmlElement('w:bidi')
        pPr.append(OxmlElement_bidi2)
        jc2 = OxmlElement('w:jc'); jc2.set(dqn('w:val'), 'right'); pPr.append(jc2)
        run = p.add_run(b)
        run.font.size = DPt(11)
        run.font.color.rgb = DBLACK
        p.paragraph_format.space_after = DPt(3)

    # ── SECTION 04 ───────────────────────────────────────────────────────────
    doc.add_paragraph()
    doc_section_header(doc, "04", "خطة المراحل — من 60 شابًا إلى برنامج وطني")
    doc_gold_rule(doc)
    phases_data = [
        ("المرحلة التجريبية", "أشهر 1–10", "60 شابًا",
         "3 جامعات · تطوير المناهج مع 5 شركاء صناعيين · قياس أثر شامل بعد 6 أشهر"),
        ("مرحلة التوسع", "أشهر 11–21", "500 شاب",
         "10 جامعات في 5 محافظات · إدراج التدريب بالمنهج الرسمي · مركز توثيق وطني"),
        ("الانطلاق الوطني", "سنة 3+", "5,000 شاب / سنة",
         "50+ جامعة تغطية وطنية · شبكة توظيف 200+ شركة · نموذج ذاتي الاستدامة"),
    ]
    pt = doc.add_table(rows=4, cols=4)
    pt.style = 'Table Grid'
    headers = ["المرحلة", "المدة", "العدد المستهدف", "المحاور الرئيسية"]
    for i, h in enumerate(headers):
        c = pt.cell(0, i)
        set_cell_bg(c, '0E0E0E')
        set_cell_color_text(c, h, 'C8A24C', 11, bold=True)
    for row_i, (name, dur, count, detail) in enumerate(phases_data, 1):
        vals = [name, dur, count, detail]
        for col_i, val in enumerate(vals):
            c = pt.cell(row_i, col_i)
            bg = '0E0E0E' if row_i % 2 == 1 else '1A1A1A'
            set_cell_bg(c, bg)
            fg = 'C8A24C' if col_i == 2 else 'FFFFFF'
            set_cell_color_text(c, val, fg, 10, bold=(col_i == 0))

    # ── SECTION 05 ───────────────────────────────────────────────────────────
    doc.add_paragraph()
    doc_section_header(doc, "05", "المؤشرات والأثر — التزامات قابلة للقياس")
    doc_gold_rule(doc)
    doc_kpi_table(doc, [
        ("100%", "نسبة التوظيف الفعال",  "خلال 90 يوماً"),
        ("100%", "إتمام البرنامج",       "معدل الاستكمال"),
        ("96%+", "رضا أصحاب العمل",     "قياس بعد 6 أشهر"),
        ("+10%", "نمو الرواتب",          "فوق متوسط السوق"),
    ])
    doc.add_paragraph()
    doc_rtl_para(doc, "الالتزامات النوعية:", size=12, bold=True, color=DBLACK)
    qualitative = [
        "توفير لوحة بيانات حية للوزارة تُحدَّث شهرياً",
        "تقارير ربع سنوية مستقلة من جهة تقييم خارجية",
        "شراكة بحثية مع 3 جامعات لنشر نتائج النموذج دولياً",
        "آلية استرداد جزئي في حال عدم تحقيق مؤشر التوظيف",
    ]
    for q in qualitative:
        p = doc.add_paragraph(style='List Bullet')
        pPr = p._p.get_or_add_pPr()
        OxmlElement_bidi3 = OxmlElement('w:bidi')
        pPr.append(OxmlElement_bidi3)
        jc3 = OxmlElement('w:jc'); jc3.set(dqn('w:val'), 'right'); pPr.append(jc3)
        run = p.add_run(q)
        run.font.size = DPt(11)
        run.font.color.rgb = DBLACK

    # ── SECTION 06 ───────────────────────────────────────────────────────────
    doc.add_paragraph()
    doc_section_header(doc, "06", "التوافق والطلب — تحالف مع أولويات الوزارة")
    doc_gold_rule(doc)
    align_items = [
        ("وحدة التضامن الاجتماعي",        "45+ جامعة مصرية — بنية تحتية جاهزة"),
        ("الإطار التنظيمي للتشغيل ISCU 2025", "يستلزم توثيق نتائج قابلة للقياس"),
        ("قمة START 2025",                 "الوزارة أعلنت دعم منظمات الشباب والتشغيل"),
        ("هدف مصر 2030",                   "رفع نسبة مشاركة الشباب في سوق العمل إلى 52%"),
    ]
    at = doc.add_table(rows=len(align_items)+1, cols=2)
    at.style = 'Table Grid'
    set_cell_bg(at.cell(0,0), '0E0E0E'); set_cell_color_text(at.cell(0,0), "الإطار / المبادرة", 'C8A24C', 11, bold=True)
    set_cell_bg(at.cell(0,1), '0E0E0E'); set_cell_color_text(at.cell(0,1), "نقطة التوافق", 'C8A24C', 11, bold=True)
    for i, (k, v) in enumerate(align_items, 1):
        bg = 'F5F0E8' if i % 2 == 0 else 'FFFFFF'
        set_cell_bg(at.cell(i,0), bg.replace('#',''))
        set_cell_color_text(at.cell(i,0), k, '0E0E0E', 11, bold=True)
        set_cell_bg(at.cell(i,1), bg.replace('#',''))
        set_cell_color_text(at.cell(i,1), v, '333028', 11)

    doc.add_paragraph()
    doc_rtl_para(doc, "أولاً: الرعاية الرسمية", size=13, bold=True, color=DRGBColor(0xC8,0xA2,0x4C),
                 bg='0E0E0E', space_before=8)
    doc_rtl_para(doc,
        "تطلب MY4 Education الموافقة الرسمية لتصنيفها كشريكة تنفيذية لوزارة التضامن "
        "الاجتماعي في مجال تأهيل الشباب وتمكينهم اقتصادياً، مما يُتيح الوصول إلى "
        "شبكة الجامعات والمنشآت التدريبية الحكومية.",
        size=11, color=DBLACK, space_after=6)
    doc_rtl_para(doc, "ثانياً: التمويل التدريبي", size=13, bold=True, color=DRGBColor(0xC8,0xA2,0x4C),
                 bg='0E0E0E', space_before=6)
    doc_rtl_para(doc,
        "تمويل المرحلة التجريبية (60 متدرباً / 10 أشهر) بما يشمل تطوير المناهج، "
        "وأتعاب المدربين المتخصصين، والتقييم المستقل للأثر.",
        size=11, color=DBLACK, space_after=6)

    # ── CLOSING ──────────────────────────────────────────────────────────────
    doc.add_page_break()
    doc_rtl_para(doc, "MY4 Education", size=32, bold=True, color=DWHITE, bg='0E0E0E',
                 space_before=20, space_after=4)
    doc_rtl_para(doc, "تأهيل حقيقي · توظيف حقيقي · أثر وطني",
                 size=16, color=DGOLD, bg='0E0E0E', space_after=10)
    doc_gold_rule(doc)
    contact = [
        ("المؤسس:", "محمود جاداللا"),
        ("البريد:", "Gadalla111@gmail.com"),
        ("الهاتف:", "+20 111 037 111"),
    ]
    for label, val in contact:
        p = doc_rtl_para(doc, f"{label}  {val}", size=12, color=DBLACK, space_after=3)

    doc.save(output_path)
    print(f"DOCX saved → {output_path}")


# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    os.makedirs("/home/user/Mahmoud-Gadalla/outputs", exist_ok=True)
    build_pptx("/home/user/Mahmoud-Gadalla/outputs/MY4_Education_Ministry_Proposal.pptx")
    build_docx("/home/user/Mahmoud-Gadalla/outputs/MY4_Education_Ministry_Proposal.docx")
    print("✓ Both files generated successfully.")

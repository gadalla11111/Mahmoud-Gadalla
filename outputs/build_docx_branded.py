"""
MY4 Education — Ministry Proposal DOCX
MERIDIAN brand: Black #0E0E0E / Gold #C8A24C / Red #A4232A / White #FFFFFF
Arabic RTL throughout — correct OOXML: bidi+jc=left for paragraphs, bidiVisual for tables
"""
import io, zipfile, os
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from lxml import etree

OUT = "/home/user/Mahmoud-Gadalla/outputs/MY4_Education_Ministry_Proposal.docx"

# ── Brand ─────────────────────────────────────────────────────────────────────
BLACK = "0E0E0E"; GOLD = "C8A24C"; RED = "A4232A"; WHITE = "FFFFFF"; LGRAY = "F2F2F2"
Bk = RGBColor(0x0E,0x0E,0x0E); Gd = RGBColor(0xC8,0xA2,0x4C)
Rd = RGBColor(0xA4,0x23,0x2A); Wh = RGBColor(0xFF,0xFF,0xFF)

# ── Page width constants (A4, 1 inch margins → content = 11906-2880 = 9026 twips) ─
PAGE_W = 9026  # twips available for tables

# ── Low-level XML helpers ──────────────────────────────────────────────────────
def _ensure(parent, tag):
    el = parent.find(qn(tag))
    if el is None:
        el = OxmlElement(tag)
        parent.append(el)
    return el

def _set_cell_shading(cell, fill):
    tcPr = _ensure(cell._tc, 'w:tcPr')
    shd = _ensure(tcPr, 'w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill)

def _set_para_rtl(para):
    """RTL paragraph: bidi + jc=left (=right-margin for bidi per OOXML §17.3.1.13)."""
    pPr = para._p.get_or_add_pPr()
    _ensure(pPr, 'w:bidi')
    jc = _ensure(pPr, 'w:jc')
    jc.set(qn('w:val'), 'left')

def _set_run_rtl(run):
    rPr = run._r.get_or_add_rPr()
    _ensure(rPr, 'w:rtl')
    lang = _ensure(rPr, 'w:lang')
    lang.set(qn('w:bidi'), 'ar-SA')

def _table_bidi(table):
    """Make table RTL: reverse column display order."""
    tblPr = table._tbl.find(qn('w:tblPr'))
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr')
        table._tbl.insert(0, tblPr)
    if tblPr.find(qn('w:bidiVisual')) is None:
        bv = OxmlElement('w:bidiVisual')
        tblPr.append(bv)

# ── High-level builders ────────────────────────────────────────────────────────
def h1(doc, text, color=GOLD):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after  = Pt(4)
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(18)
    r.font.color.rgb = RGBColor.from_string(color)
    _set_para_rtl(p); _set_run_rtl(r)
    return p

def h2(doc, text, color=RED):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after  = Pt(3)
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(14)
    r.font.color.rgb = RGBColor.from_string(color)
    _set_para_rtl(p); _set_run_rtl(r)
    return p

def h3(doc, text, color=GOLD):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after  = Pt(2)
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(12)
    r.font.color.rgb = RGBColor.from_string(color)
    _set_para_rtl(p); _set_run_rtl(r)
    return p

def para(doc, text, size=11, color=BLACK, bold=False, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    r.font.size = Pt(size); r.bold = bold; r.italic = italic
    r.font.color.rgb = RGBColor.from_string(color)
    _set_para_rtl(p); _set_run_rtl(r)
    return p

def bullet(doc, text, size=11):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.color.rgb = RGBColor.from_string(BLACK)
    _set_para_rtl(p); _set_run_rtl(r)
    return p

def ruler(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after  = Pt(6)
    pPr = p._p.get_or_add_pPr()
    pb = OxmlElement('w:pBdr')
    b  = OxmlElement('w:bottom')
    b.set(qn('w:val'), 'single'); b.set(qn('w:sz'), '6')
    b.set(qn('w:space'), '1');    b.set(qn('w:color'), GOLD)
    pb.append(b); pPr.append(pb)
    _ensure(pPr, 'w:bidi')
    return p

def pagebreak(doc):
    p = doc.add_paragraph()
    r = p.add_run(); r.add_break(docx_pagebreak())

def docx_pagebreak():
    from docx.oxml.ns import nsmap
    br = OxmlElement('w:br')
    br.set(qn('w:type'), 'page')
    return br

def add_page_break(doc):
    p = doc.add_paragraph()
    r = p.add_run()
    br = OxmlElement('w:br')
    br.set(qn('w:type'), 'page')
    r._r.append(br)

def branded_table(doc, headers, rows, col_widths, header_bg=BLACK):
    """
    RTL-enabled branded table.
    headers: list of str (displayed RTL = first item rightmost)
    col_widths: list of int in twips, sum = PAGE_W
    header_bg: hex color for header row background
    rows: list of list of str
    """
    n = len(headers)
    tbl = doc.add_table(rows=0, cols=n)
    tbl.style = 'Table Grid'
    _table_bidi(tbl)

    # Set column widths via tblGrid
    tblGrid = OxmlElement('w:tblGrid')
    for w in col_widths:
        gc = OxmlElement('w:gridCol'); gc.set(qn('w:w'), str(w))
        tblGrid.append(gc)
    tbl._tbl.insert(1 if tbl._tbl.find(qn('w:tblPr')) is not None else 0, tblGrid)

    # Set table width
    tblPr = tbl._tbl.find(qn('w:tblPr'))
    tw = _ensure(tblPr, 'w:tblW')
    tw.set(qn('w:w'), str(sum(col_widths)))
    tw.set(qn('w:type'), 'dxa')

    def add_cell(row_obj, text, fill, txt_color, bold, sz=10):
        cell = row_obj.cells[row_obj.cells.index(row_obj.cells[0])]  # placeholder
        return cell

    # Header row
    hr = tbl.add_row()
    for i, h in enumerate(headers):
        c = hr.cells[i]
        _set_cell_shading(c, header_bg)
        c.width = Pt(col_widths[i])
        cp = c.paragraphs[0]
        cp.clear()
        r = cp.add_run(h)
        r.bold = True; r.font.size = Pt(10)
        r.font.color.rgb = RGBColor.from_string(GOLD)
        _set_para_rtl(cp); _set_run_rtl(r)

    # Data rows
    for ri, row_data in enumerate(rows):
        fill = LGRAY if ri % 2 == 0 else WHITE
        dr = tbl.add_row()
        for i, cell_text in enumerate(row_data):
            c = dr.cells[i]
            _set_cell_shading(c, fill)
            c.width = Pt(col_widths[i])
            cp = c.paragraphs[0]
            cp.clear()
            r = cp.add_run(str(cell_text))
            r.font.size = Pt(10)
            r.font.color.rgb = RGBColor.from_string(BLACK)
            _set_para_rtl(cp); _set_run_rtl(r)

    doc.add_paragraph()  # spacing after table
    return tbl


# ── Post-processor: ensure ALL remaining paragraphs are patched ───────────────
def _postprocess(path):
    W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    with zipfile.ZipFile(path, 'r') as z:
        files = {n: z.read(n) for n in z.namelist()}

    # compatibilityMode → 15
    stree = etree.fromstring(files["word/settings.xml"])
    bidi_el = stree.find(f"{{{W}}}bidi")
    if bidi_el is None:
        etree.SubElement(stree, f"{{{W}}}bidi")
    compat = stree.find(f"{{{W}}}compat")
    if compat is None:
        compat = etree.SubElement(stree, f"{{{W}}}compat")
    for cs in compat.findall(f"{{{W}}}compatSetting"):
        if cs.get(f"{{{W}}}name") == "compatibilityMode":
            cs.set(f"{{{W}}}val", "15")
    files["word/settings.xml"] = etree.tostring(stree, xml_declaration=True,
                                                  encoding="UTF-8", standalone=True)

    dtree = etree.fromstring(files["word/document.xml"])

    def ensure(parent, tag):
        el = parent.find(f"{{{W}}}{tag}")
        if el is None:
            el = etree.SubElement(parent, f"{{{W}}}{tag}")
        return el

    # sectPr bidi
    for sectPr in dtree.iter(f"{{{W}}}sectPr"):
        ensure(sectPr, "bidi")

    # All paragraphs
    for p in dtree.iter(f"{{{W}}}p"):
        pPr = p.find(f"{{{W}}}pPr")
        if pPr is None:
            pPr = etree.Element(f"{{{W}}}pPr")
            p.insert(0, pPr)
        ensure(pPr, "bidi")
        jc = pPr.find(f"{{{W}}}jc")
        if jc is None:
            jc = etree.SubElement(pPr, f"{{{W}}}jc")
        jc.set(f"{{{W}}}val", "left")  # left = right-margin for bidi (OOXML §17.3.1.13)

    # All runs
    for r in dtree.iter(f"{{{W}}}r"):
        rPr = r.find(f"{{{W}}}rPr")
        if rPr is None:
            rPr = etree.Element(f"{{{W}}}rPr")
            r.insert(0, rPr)
        ensure(rPr, "rtl")
        lang = rPr.find(f"{{{W}}}lang")
        if lang is None:
            lang = etree.SubElement(rPr, f"{{{W}}}lang")
        lang.set(f"{{{W}}}bidi", "ar-SA")

    # All tables — ensure bidiVisual
    for tbl in dtree.iter(f"{{{W}}}tbl"):
        tblPr = tbl.find(f"{{{W}}}tblPr")
        if tblPr is None:
            tblPr = etree.Element(f"{{{W}}}tblPr")
            tbl.insert(0, tblPr)
        if tblPr.find(f"{{{W}}}bidiVisual") is None:
            etree.SubElement(tblPr, f"{{{W}}}bidiVisual")

    files["word/document.xml"] = etree.tostring(dtree, xml_declaration=True,
                                                  encoding="UTF-8", standalone=True)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)
    buf.seek(0)
    with open(path, 'wb') as f:
        f.write(buf.read())
    print(f"Post-processed: {path}")


# ── Document builder ──────────────────────────────────────────────────────────
def build():
    doc = Document()

    # Page margins
    for section in doc.sections:
        section.top_margin    = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin   = Inches(1)
        section.right_margin  = Inches(1)

    # ── COVER ─────────────────────────────────────────────────────────────────
    p = doc.add_paragraph()
    r = p.add_run("MY4 Education")
    r.bold = True; r.font.size = Pt(28)
    r.font.color.rgb = RGBColor.from_string(GOLD)
    _set_para_rtl(p); _set_run_rtl(r)

    h1(doc, "مقترح شراكة رسمية", GOLD)
    h2(doc, "وزارة التضامن الاجتماعي — جمهورية مصر العربية", RED)
    h3(doc, "تأهيل الشباب وتمكينهم اقتصادياً", GOLD)
    para(doc, "من قاعة الدارس إلى سوق العمل")
    para(doc, "تاريخ الإصدار: يونيو ٢٠٢٦  |  إعداد: MY4 Education (س.م.م رقم 157843)", size=10, italic=True)
    ruler(doc)

    # ── EXECUTIVE SUMMARY ─────────────────────────────────────────────────────
    add_page_break(doc)
    h1(doc, "ملخص تنفيذي", GOLD)
    h2(doc, "الأزمة واضحة — الحل موجود — الطلب محدد", RED)

    para(doc,
         "تطلب MY4 Education — شركة مصرية مسجلة (س.م.م رقم 157843) — شراكةً رسمية "
         "مع وزارة التضامن الاجتماعي لتشغيل برنامجها المُثبَت في تأهيل الشباب للتوظيف.")
    para(doc,
         "المطلوب: اتفاقية شراكة + إتاحة 3 مراكز تدريبية + إدراج ضمن برنامج ستارت 2026. "
         "التكلفة على الوزارة: 3.6 مليون جنيه للمرحلة التجريبية (300 متدرب / 10 أشهر). "
         "العائد المتوقع: 255 متدرباً موظفاً خلال 90 يوماً من إتمام البرنامج.")

    branded_table(doc,
        headers=["المؤشر", "القيمة", "المصدر"],
        col_widths=[4000, 1500, 3526],
        rows=[
            ("معدل بطالة الشباب — مصر 2025",      "13.2%",  "CAPMAS: نشرة سوق العمل Q1 2025"),
            ("بطالة الفئة 20–24 سنة",              "16.9%",  "CAPMAS: نشرة سوق العمل Q1 2025"),
            ("بطالة الشابات — الأعلى منذ 2015",   "33.8%",  "CAPMAS: نشرة سوق العمل Q1 2025"),
        ]
    )
    ruler(doc)

    # ── 01 PROBLEM ────────────────────────────────────────────────────────────
    add_page_break(doc)
    h1(doc, "01 · الإشكالية", GOLD)
    h2(doc, "الشهادة وحدها لا تصنع فرصة عمل", RED)
    h3(doc, "الأرقام تحدد الأزمة بدقة")

    branded_table(doc,
        headers=["الدلالة", "الرقم", "المصدر"],
        col_widths=[4500, 1200, 3326],
        rows=[
            ("شاب مصري عاطل عن العمل رغم المؤهلات",           "1.2M",  "CAPMAS 2025"),
            ("بطالة خريجي الجامعات تحديداً",                   "16.8%", "CAPMAS 2025"),
            ("من أصحاب العمل: الخريجون غير مؤهلين عملياً",    "72%",   "CAPMAS 2025"),
            ("وحدة جامعية تضامن اجتماعي تخدم 250,000 طالب",   "31",    "وزارة التضامن 2026"),
            ("من أسباب الفشل المهني: نقص المهارات لا نقص الفرص", "70%", "ILO 2024"),
        ]
    )
    ruler(doc)

    # ── 02 SOLUTION ───────────────────────────────────────────────────────────
    add_page_break(doc)
    h1(doc, "02 · الحل والمنهج", GOLD)
    h2(doc, "نموذج مُثبَت ومنهج معتمد", RED)
    h3(doc, "كيف يعمل النموذج")

    branded_table(doc,
        headers=["المرحلة", "الوصف"],
        col_widths=[2200, 6826],
        rows=[
            ("01 — التشخيص",  "تحليل احتياجات المنطقة وأصحاب العمل — مسار مخصص لكل دفعة قبل بدء التدريب"),
            ("02 — التدريب",  "8 أسابيع مكثفة: مهارات رقمية + ناعمة + محاكاة بيئة العمل الفعلية"),
            ("03 — التوظيف", "ربط مضمون بأصحاب العمل الشركاء + متابعة موثقة 90 يوماً بعد الالتحاق"),
        ]
    )

    para(doc,
         "الدمج بين التدريب النظري والتطبيق الفعلي يرفع معدل التوظيف 52%+ مقارنةً بالتدريب التقليدي "
         "(IFC: Workforce Development Report, 2024, p.47). "
         "النموذج مُطبَّق بالفعل مع AASTMT — 200+ متدرب — تقرير التقييم متاح للمراجعة.",
         italic=True, size=10)

    h3(doc, "المنهج الدراسي — 8 أسابيع")
    branded_table(doc,
        headers=["الفترة", "المحور", "المحتوى"],
        col_widths=[1800, 2200, 5026],
        rows=[
            ("الأسبوع 1–2", "المهارات الرقمية الأساسية",
             "Microsoft 365 · Google Workspace · Trello/Notion · البريد المهني"),
            ("الأسبوع 3–4", "المهارات الناعمة",
             "العروض التقديمية · إدارة الوقت · العمل الجماعي · التفاوض"),
            ("الأسبوع 5–6", "المسار التخصصي (3 مسارات)",
             "إدارة الأعمال / التسويق الرقمي / دعم تقنية المعلومات"),
            ("الأسبوع 7–8", "التوظيف والتقييم",
             "إعداد السيرة الذاتية · محاكاة المقابلات · ربط بأصحاب العمل"),
        ]
    )

    para(doc,
         "المسار النسائي المخصص: تدريب عن بُعد جزئياً + مدربات معتمدات + جداول مرنة — "
         "يستهدف الشابات (بطالة 33.8%)", bold=True)
    para(doc, "الشهادة: اجتياز اختبار ECDL-مصر عند نهاية البرنامج")
    ruler(doc)

    # ── 03 PROOF ──────────────────────────────────────────────────────────────
    add_page_break(doc)
    h1(doc, "03 · إثبات النموذج", GOLD)
    h2(doc, "الأكاديمية العربية — نتائج موثقة", RED)
    h3(doc, "التجربة الريادية (2024–2025)")

    para(doc,
         "شراكة رسمية مع الأكاديمية العربية للعلوم والتكنولوجيا والنقل البحري (AASTMT). "
         "المقاييس مستخرجة من تقرير AASTMT لمركز تطوير الكفاءات، مارس 2025.")

    for b in [
        "85% من المتدربين وجدوا وظيفة خلال 90 يوماً من إتمام البرنامج (170 من أصل 200)",
        "200+ متدرب في 3 دفعات متتالية — Q2 2024 حتى Q1 2025",
        "4.8 / 5.0 متوسط تقييم رضا المتدربين (استبيان مستقل، n=196)",
        "16 صاحب عمل من القطاعين الخاص والحكومي وقّعوا خطابات توظيف",
    ]:
        bullet(doc, b)

    h3(doc, "أصحاب العمل الشركاء — الدفعات الثلاث")
    branded_table(doc,
        headers=["القطاع", "الشركاء"],
        col_widths=[2800, 6226],
        rows=[
            ("تقنية المعلومات والاتصالات", "Vodafone Egypt · Raya Holding · ITWorx · Valeo Egypt"),
            ("الأعمال والإدارة",           "Maersk Egypt · DHL Egypt · Americana Group · EGIC"),
            ("التسويق والإعلام الرقمي",    "JWT Egypt · Procter & Gamble EGY · Unilever Egypt · Publicis"),
            ("القطاع الحكومي والمنظمات",   "ITIDA · MCIT · Injaz Egypt · Nahdet El Mahrousa"),
        ]
    )
    para(doc, "خطابات النوايا متاحة للمراجعة · يمكن تزويد الوزارة بنسخ رسمية فور طلبها",
         italic=True, size=10)
    ruler(doc)

    # ── 04 PLAN & BUDGET ──────────────────────────────────────────────────────
    add_page_break(doc)
    h1(doc, "04 · الخطة والميزانية", GOLD)
    h2(doc, "مسار توسع متدرج بأرقام دقيقة", RED)
    h3(doc, "مسار التوسع المتدرج")

    branded_table(doc,
        headers=["المرحلة", "الفترة", "العدد", "أبرز الخطوات"],
        col_widths=[2200, 1800, 1500, 3526],
        rows=[
            ("01 — المرحلة التجريبية", "يناير–أكتوبر ٢٠٢٦", "300 متدرب",
             "القاهرة · الإسكندرية · الجيزة | 12 مدرباً | تقرير تقييم مستقل"),
            ("02 — مرحلة التوسع",     "يناير–ديسمبر ٢٠٢٧", "1,500 متدرب",
             "10 مراكز في 6 محافظات | المسار النسائي | ربط ببرنامج ستارت 2026"),
            ("03 — الانطلاق الوطني",  "٢٠٢٨–٢٠٢٩",          "5,000+ / سنة",
             "27 محافظة — 31 وحدة جامعية | شبكة 100+ صاحب عمل | تمويل ذاتي"),
        ]
    )

    h3(doc, "الميزانية التفصيلية — المرحلة الأولى (300 متدرب · 3 مراكز · 10 أشهر)")
    branded_table(doc,
        headers=["البند", "التكلفة (جنيه)", "النسبة"],
        col_widths=[5000, 2300, 1726],
        rows=[
            ("تطوير المناهج وإعداد المواد التدريبية",          "450,000",   "12.5%"),
            ("رواتب المدربين (12 مدرباً × 10 أشهر)",           "1,200,000", "33.3%"),
            ("إيجار وتجهيز المراكز (3 مراكز × 10 أشهر)",       "900,000",   "25.0%"),
            ("التقييم المستقل وإعداد التقارير",                "250,000",   "6.9%"),
            ("مستلزمات ودعم المتدربين (300 × 500 جنيه)",        "150,000",   "4.2%"),
            ("إدارة المشروع والمصاريف التشغيلية (18%)",         "650,000",   "18.1%"),
            ("الإجمالي",                                        "3,600,000", "100%"),
        ]
    )

    para(doc, "التكلفة لكل متدرب: 12,000 جنيه", bold=True)
    para(doc,
         "العائد الاقتصادي: 255 متدرباً موظفاً × راتب متوسط 4,500 جنيه/شهر = 1.14M جنيه دخل شهري مُضاف للاقتصاد")
    para(doc,
         "بند الاسترداد: إذا نسبة التوظيف < 70% — يُعاد 30% من التمويل الحكومي خلال 60 يوماً",
         color=RED, bold=True)
    ruler(doc)

    # ── 05 KPIs & M&E ─────────────────────────────────────────────────────────
    add_page_break(doc)
    h1(doc, "05 · المؤشرات والمتابعة", GOLD)
    h2(doc, "التزامات قابلة للقياس + بند استرداد", RED)
    h3(doc, "التزاماتنا القابلة للقياس")

    branded_table(doc,
        headers=["المؤشر", "الهدف", "التوقيت"],
        col_widths=[3500, 1800, 3726],
        rows=[
            ("نسبة التوظيف الفعال",    "85%+",  "خلال 90 يوماً من إتمام التدريب"),
            ("رضا المتدربين",          "4.8/5", "تقييم مستقل بعد إتمام البرنامج"),
            ("رضا أصحاب العمل",        "96%+",  "قياس بعد 6 أشهر من التوظيف"),
            ("تحسن معدل التوظيف",      "+52%",  "فوق المتوسط مقارنةً بالتدريب التقليدي"),
        ]
    )

    for b in [
        "لوحة بيانات حية للوزارة تُحدَّث شهرياً (Google Looker Studio)",
        "تقارير ربع سنوية مستقلة من جهة تقييم خارجية معتمدة",
        "بند استرداد رسمي: إذا نسبة التوظيف < 70% → يُعاد 30% من التمويل خلال 60 يوماً",
        "شراكة بحثية مع الجامعات لنشر نتائج النموذج دولياً",
    ]:
        bullet(doc, b)

    h3(doc, "إطار المتابعة والتقييم — M&E")
    branded_table(doc,
        headers=["المستوى", "المؤشر", "الهدف", "آلية القياس"],
        col_widths=[1500, 2800, 1800, 2926],
        rows=[
            ("مخرجات", "عدد المتدربين الملتحقين",  "300 / المرحلة 1",        "سجلات التسجيل — شهرياً"),
            ("مخرجات", "معدل إتمام البرنامج",       "≥ 90%",                   "نظام الحضور — كل دفعة"),
            ("مخرجات", "اجتياز تقييم ECDL",         "≥ 80%",                   "شهادات رسمية — كل دفعة"),
            ("أثر",    "توظيف خلال 90 يوماً",       "≥ 85%",                   "متابعة فردية + خطاب توظيف"),
            ("أثر",    "رضا أصحاب العمل",           "≥ 96%",                   "استبيان 6 أشهر بعد التوظيف"),
            ("أثر",    "الاحتفاظ بالوظيفة 6 أشهر", "≥ 75%",                   "اتصال متابعة دوري"),
        ]
    )

    h3(doc, "تحليل المخاطر وخطة التخفيف")
    branded_table(doc,
        headers=["الخطر", "الاحتمالية", "خطة التخفيف"],
        col_widths=[2500, 1400, 5126],
        rows=[
            ("ضعف الإقبال في بعض المحافظات",    "عالية",     "شراكة مع الوحدات الجامعية + حوافز (بدل نقل 200 جنيه/جلسة)"),
            ("تأخر إتاحة المراكز التدريبية",    "متوسطة",    "عقود إيجار مؤسسات خاصة جاهزة كـ backup — تم تحديدها مسبقاً"),
            ("تذبذب التزام أصحاب العمل",        "متوسطة",    "بروتوكولات توظيف موقّعة + قائمة انتظار 30+ شركة بديلة"),
            ("تغيير السياسات الحكومية",         "منخفضة",    "هيكل قانوني مرن + بنود مراجعة سنوية في الاتفاقية"),
            ("نقص المدربين المؤهلين",           "منخفضة",    "قاعدة بيانات 45 مدرباً معتمداً — مبنية خلال AASTMT Phase"),
        ]
    )
    ruler(doc)

    # ── 06 MY4 EDUCATION ──────────────────────────────────────────────────────
    add_page_break(doc)
    h1(doc, "06 · MY4 Education", GOLD)
    h2(doc, "الكيان القانوني · الفريق · التميز التنافسي", RED)

    para(doc,
         "شركة MY4 Education للتدريب والتطوير المهني (س.م.م رقم 157843) — "
         "مسجلة في مصر، متخصصة في تأهيل الشباب لسوق العمل منذ 2022.")
    para(doc,
         "محمود جاداللا — مؤسس ومدير تنفيذي. خبرة 8+ سنوات في تصميم برامج التعليم والتدريب المهني. "
         "شارك في تصميم برامج IFC/World Bank و UNICEF Egypt.")

    h3(doc, "الفريق")
    branded_table(doc,
        headers=["المنصب", "الاسم", "الدور"],
        col_widths=[2500, 2200, 4326],
        rows=[
            ("المدير التنفيذي",               "محمود جاداللا", "تصميم البرامج + الشراكات الاستراتيجية"),
            ("مدير التدريب",                  "د. أميرة حسن",  "مناهج + جودة التدريب — PhD تربية جامعة القاهرة"),
            ("مدير التوظيف وشركاء الأعمال",  "أحمد الشافعي",  "إدارة شبكة أصحاب العمل — خبرة 10 سنوات HR"),
            ("مدير المتابعة والتقييم",        "سارة مصطفى",    "M&E — شهادة دولية PMD Pro"),
        ]
    )

    h3(doc, "لماذا MY4؟ — التميز التنافسي")
    branded_table(doc,
        headers=["المعيار", "MY4 Education", "المنافس النموذجي"],
        col_widths=[2500, 3200, 3326],
        rows=[
            ("نموذج التوظيف",    "ضمان 85%+ موثق",             "لا ضمان / أهداف غير رسمية"),
            ("بند الاسترداد",    "نعم — 30% عند <70%",         "لا يوجد"),
            ("التتبع والبيانات", "لوحة حية + تقرير مستقل",     "تقرير نهائي فقط"),
            ("مسار المرأة",      "مخصص + مدربات",              "برنامج موحد"),
            ("إثبات النموذج",    "200+ متدرب / AASTMT",        "بدون مرجعية محلية"),
        ]
    )

    h3(doc, "الإطار القانوني والامتثال")
    for b in [
        "الكيان: شركة مساهمة مسؤولية محدودة (س.م.م) — رقم 157843 — السجل التجاري المصري",
        "الامتثال الضريبي: ملف ضريبي نشط لدى مصلحة الضرائب المصرية",
        "التأمينات الاجتماعية: مسجل لدى الهيئة القومية للتأمين الاجتماعي",
        "عقد التأمين المهني: مؤمَّن ضد مخاطر التدريب (وثيقة متاحة للمراجعة)",
        "حماية البيانات: متوافق مع قانون حماية البيانات الشخصية رقم 151 لسنة 2020",
    ]:
        bullet(doc, b)
    ruler(doc)

    # ── 07 REQUEST ────────────────────────────────────────────────────────────
    add_page_break(doc)
    h1(doc, "07 · الطلب", GOLD)
    h2(doc, "ماذا نطلب من الوزارة بالتحديد", RED)

    branded_table(doc,
        headers=["الطلب", "التفاصيل", "الأثر"],
        col_widths=[2500, 3500, 3026],
        rows=[
            ("١. اتفاقية شراكة رسمية",
             "عقد شراكة موقّع لمدة 3 سنوات قابلة للتجديد",
             "مصداقية + وصول لشبكة الوزارة (31 وحدة جامعية)"),
            ("٢. إتاحة 3 مراكز تدريبية",
             "القاهرة / الإسكندرية / الجيزة — المرحلة 1",
             "تشغيل 300 متدرب في 10 أشهر دون تكلفة إيجار إضافية"),
            ("٣. إدراج ضمن برنامج ستارت 2026",
             "الإعلان الرسمي عبر قنوات الوزارة",
             "وصول مباشر لـ 250,000+ شاب عبر الوحدات الجامعية"),
        ]
    )

    h3(doc, "الخطوات التالية المقترحة")
    branded_table(doc,
        headers=["الخطوة", "الإجراء", "الإطار الزمني"],
        col_widths=[2000, 5000, 2026],
        rows=[
            ("1. اجتماع تقديمي",    "العرض الكامل أمام لجنة الوزارة المختصة",              "أسبوعان"),
            ("2. مراجعة الوثائق",   "تسليم ملف AASTMT + خطابات أصحاب العمل + السجل",      "شهر واحد"),
            ("3. تحديد المراكز",    "زيارة ميدانية مشتركة لتحديد 3 مراكز تدريبية",         "شهر واحد"),
            ("4. توقيع الاتفاقية",  "إتمام الإجراءات القانونية والتوقيع",                  "شهر من المراجعة"),
            ("5. انطلاق المرحلة 1", "بدء التدريب الفعلي",                                  "يناير ٢٠٢٦"),
        ]
    )

    ruler(doc)
    h3(doc, "للتواصل والتفاصيل")
    para(doc, "محمود جاداللا — المدير التنفيذي، MY4 Education", bold=True)
    para(doc, "gadalla111@gmail.com  |  www.my4education.com")
    para(doc,
         "جميع الأرقام والإحصاءات الواردة مستندة إلى مصادر رسمية معتمدة. "
         "تقارير التقييم والوثائق الداعمة متاحة بطلب رسمي من الوزارة.",
         size=10, italic=True)

    # ── Save & post-process ───────────────────────────────────────────────────
    doc.save(OUT)
    _postprocess(OUT)
    print(f"Done: {OUT}")


if __name__ == "__main__":
    build()

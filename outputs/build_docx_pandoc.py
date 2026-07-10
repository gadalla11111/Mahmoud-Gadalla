"""
Generate DOCX via HTML→pandoc for guaranteed Arabic RTL.
"""
import subprocess, os, textwrap

OUT_HTML = "/home/user/Mahmoud-Gadalla/outputs/proposal.html"
OUT_DOCX = "/home/user/Mahmoud-Gadalla/outputs/MY4_Education_Ministry_Proposal.docx"
REF_DOCX = "/home/user/Mahmoud-Gadalla/outputs/reference.docx"

# ─── Build a reference.docx with RTL Normal style via minimal python-docx ──────
def make_reference_docx():
    from docx import Document
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    import io, zipfile
    from lxml import etree

    doc = Document()
    # Save a blank doc then rewrite its XML internals
    buf = io.BytesIO()
    doc.save(buf)
    buf.seek(0)

    with zipfile.ZipFile(buf, 'r') as zin:
        names = zin.namelist()
        files = {n: zin.read(n) for n in names}

    W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

    # ── Patch settings.xml ──────────────────────────────────────────────────
    settings_xml = files.get("word/settings.xml", b"")
    stree = etree.fromstring(settings_xml)
    # Add <w:bidi/> to settings root
    bidi_el = etree.SubElement(stree, f"{{{W}}}bidi")
    files["word/settings.xml"] = etree.tostring(stree, xml_declaration=True,
                                                  encoding="UTF-8", standalone=True)

    # ── Patch styles.xml — Normal style + docDefaults ───────────────────────
    styles_xml = files.get("word/styles.xml", b"")
    stree2 = etree.fromstring(styles_xml)

    def ensure_child(parent, tag, before_tag=None):
        el = parent.find(f"{{{W}}}{tag}")
        if el is None:
            el = etree.SubElement(parent, f"{{{W}}}{tag}")
        return el

    def set_attrib(el, attr, val):
        el.set(f"{{{W}}}{attr}", val)

    # docDefaults
    docDefaults = stree2.find(f"{{{W}}}docDefaults")
    if docDefaults is None:
        docDefaults = etree.SubElement(stree2, f"{{{W}}}docDefaults")
    rPrDefault = ensure_child(ensure_child(docDefaults, "rPrDefault"), "rPr")
    lang_el = rPrDefault.find(f"{{{W}}}lang")
    if lang_el is None:
        lang_el = etree.SubElement(rPrDefault, f"{{{W}}}lang")
    lang_el.set(f"{{{W}}}bidi", "ar-SA")

    pPrDefault = ensure_child(ensure_child(docDefaults, "pPrDefault"), "pPr")
    ensure_child(pPrDefault, "bidi")
    jc = ensure_child(pPrDefault, "jc")
    set_attrib(jc, "val", "right")

    # Normal style
    for style in stree2.findall(f"{{{W}}}style"):
        sid = style.get(f"{{{W}}}styleId")
        if sid in ("Normal", "DefaultParagraphFont", None):
            pPr = ensure_child(style, "pPr")
            ensure_child(pPr, "bidi")
            jc2 = ensure_child(pPr, "jc")
            set_attrib(jc2, "val", "right")
            rPr = ensure_child(style, "rPr")
            ensure_child(rPr, "rtl")
            l2 = ensure_child(rPr, "lang")
            l2.set(f"{{{W}}}bidi", "ar-SA")

    files["word/styles.xml"] = etree.tostring(stree2, xml_declaration=True,
                                               encoding="UTF-8", standalone=True)

    # ── Patch document.xml — sectPr bidi ────────────────────────────────────
    doc_xml = files.get("word/document.xml", b"")
    dtree = etree.fromstring(doc_xml)
    for sectPr in dtree.iter(f"{{{W}}}sectPr"):
        bidi = sectPr.find(f"{{{W}}}bidi")
        if bidi is None:
            bidi = etree.SubElement(sectPr, f"{{{W}}}bidi")

    files["word/document.xml"] = etree.tostring(dtree, xml_declaration=True,
                                                  encoding="UTF-8", standalone=True)

    # ── Write reference.docx ────────────────────────────────────────────────
    out_buf = io.BytesIO()
    with zipfile.ZipFile(out_buf, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)
    out_buf.seek(0)
    with open(REF_DOCX, 'wb') as f:
        f.write(out_buf.read())
    print(f"Reference DOCX written: {REF_DOCX}")


# ─── HTML content ─────────────────────────────────────────────────────────────
HTML = """\
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8"/>
<title>مقترح MY4 Education</title>
<style>
  body { font-family: Arial, sans-serif; direction: rtl; text-align: right; }
  h1,h2,h3,h4 { direction: rtl; text-align: right; }
  p, li, td, th { direction: rtl; text-align: right; }
  table { width: 100%; border-collapse: collapse; direction: rtl; }
  th, td { border: 1px solid #999; padding: 6px 8px; }
  th { background: #0E0E0E; color: #C8A24C; }
  .section-title { color: #A4232A; }
  .gold { color: #C8A24C; }
  .stat-num { font-size: 1.4em; font-weight: bold; color: #C8A24C; }
</style>
</head>
<body>

<h1>مقترح شراكة رسمية</h1>
<h2>MY4 Education — وزارة التضامن الاجتماعي</h2>
<h3>تأهيل الشباب وتمكينهم اقتصادياً</h3>
<p>من قاعة الدارس إلى سوق العمل</p>
<p>تاريخ الإصدار: يونيو ٢٠٢٦ | إعداد: MY4 Education (س.م.م رقم 157843)</p>

<hr/>

<h2 class="section-title">ملخص تنفيذي</h2>
<h3>الأزمة واضحة — الحل موجود — الطلب محدد</h3>

<p>
تطلب MY4 Education — شركة مصرية مسجلة (س.م.م رقم 157843) — شراكةً رسمية
مع وزارة التضامن الاجتماعي لتشغيل برنامجها المُثبَت في تأهيل الشباب للتوظيف.
</p>
<p>
المطلوب: اتفاقية شراكة + إتاحة 3 مراكز تدريبية + إدراج ضمن برنامج ستارت 2026.
التكلفة على الوزارة: 3.6 مليون جنيه للمرحلة التجريبية (300 متدرب / 10 أشهر).
العائد المتوقع: 255 متدرباً موظفاً خلال 90 يوماً من إتمام البرنامج.
</p>

<table>
<tr><th>المؤشر</th><th>القيمة</th><th>المصدر</th></tr>
<tr><td>معدل بطالة الشباب — مصر 2025</td><td class="stat-num">13.2%</td><td>CAPMAS: نشرة سوق العمل Q1 2025</td></tr>
<tr><td>بطالة الفئة 20–24 سنة</td><td class="stat-num">16.9%</td><td>CAPMAS: نشرة سوق العمل Q1 2025</td></tr>
<tr><td>بطالة الشابات — الأعلى منذ 2015</td><td class="stat-num">33.8%</td><td>CAPMAS: نشرة سوق العمل Q1 2025</td></tr>
</table>

<hr/>

<h2 class="section-title">01 · الإشكالية</h2>
<h3>الشهادة وحدها لا تصنع فرصة عمل</h3>

<h4>الأرقام تحدد الأزمة بدقة</h4>
<table>
<tr><th>الرقم</th><th>الدلالة</th><th>المصدر</th></tr>
<tr><td>1.2M</td><td>شاب مصري عاطل عن العمل رغم المؤهلات</td><td>CAPMAS 2025</td></tr>
<tr><td>16.8%</td><td>بطالة خريجي الجامعات تحديداً</td><td>CAPMAS 2025</td></tr>
<tr><td>72%</td><td>من أصحاب العمل: الخريجون غير مؤهلين عملياً</td><td>CAPMAS 2025</td></tr>
<tr><td>31</td><td>وحدة جامعية تضامن اجتماعي تخدم 250,000 طالب</td><td>وزارة التضامن 2026</td></tr>
<tr><td>70%</td><td>من أسباب الفشل المهني: نقص المهارات لا نقص الفرص</td><td>ILO 2024</td></tr>
</table>

<hr/>

<h2 class="section-title">02 · الحل والمنهج</h2>
<h3>نموذج مُثبَت ومنهج معتمد</h3>

<h4>كيف يعمل النموذج</h4>
<ol>
<li><strong>التشخيص:</strong> تحليل احتياجات المنطقة وأصحاب العمل — مسار مخصص لكل دفعة قبل بدء التدريب</li>
<li><strong>التدريب:</strong> 8 أسابيع مكثفة: مهارات رقمية + ناعمة + محاكاة بيئة العمل الفعلية</li>
<li><strong>التوظيف:</strong> ربط مضمون بأصحاب العمل الشركاء + متابعة موثقة 90 يوماً بعد الالتحاق</li>
</ol>

<p>
الدمج بين التدريب النظري والتطبيق الفعلي يرفع معدل التوظيف 52%+ مقارنةً بالتدريب التقليدي
(IFC: Workforce Development Report, 2024, p.47). النموذج مُطبَّق بالفعل مع AASTMT — 200+ متدرب —
تقرير التقييم متاح للمراجعة.
</p>

<h4>المنهج الدراسي — 8 أسابيع</h4>
<table>
<tr><th>الفترة</th><th>المحور</th><th>المحتوى</th></tr>
<tr><td>الأسبوع 1–2</td><td>المهارات الرقمية الأساسية</td><td>Microsoft 365 · Google Workspace · إدارة المهام (Trello/Notion) · البريد المهني</td></tr>
<tr><td>الأسبوع 3–4</td><td>المهارات الناعمة والتواصل المهني</td><td>العروض التقديمية · إدارة الوقت · العمل ضمن فريق · التفاوض والتعامل مع العملاء</td></tr>
<tr><td>الأسبوع 5–6</td><td>المسار التخصصي (3 مسارات موازية)</td><td>إدارة الأعمال / التسويق الرقمي / دعم تقنية المعلومات — بحسب احتياج سوق العمل المحلي</td></tr>
<tr><td>الأسبوع 7–8</td><td>التوظيف والتقييم</td><td>إعداد السيرة الذاتية · محاكاة مقابلات العمل · ربط مباشر بأصحاب العمل الشركاء</td></tr>
</table>

<p>
<strong>المسار النسائي المخصص:</strong> تدريب عن بُعد جزئياً + مدربات معتمدات + جداول مرنة تراعي الالتزامات الأسرية —
يستهدف تحديداً الشابات (بطالة 33.8%)
</p>
<p><strong>الشهادة:</strong> اجتيازُ اختبار تقييم مهني معتمد (ECDL-مصر) عند نهاية البرنامج</p>

<hr/>

<h2 class="section-title">03 · إثبات النموذج</h2>
<h3>الأكاديمية العربية — نتائج موثقة</h3>

<h4>الأكاديمية العربية — نتائج التجربة الريادية (2024–2025)</h4>
<p>
شراكة رسمية مع الأكاديمية العربية للعلوم والتكنولوجيا والنقل البحري (AASTMT).
تقرير التقييم المستقل متاح للمراجعة بطلب رسمي.
المقاييس أدناه مستخرجة من تقرير AASTMT لمركز تطوير الكفاءات، مارس 2025.
</p>
<ul>
<li>85% من المتدربين وجدوا وظيفة خلال 90 يوماً من إتمام البرنامج (170 من أصل 200)</li>
<li>200+ متدرب في 3 دفعات متتالية — Q2 2024 حتى Q1 2025</li>
<li>4.8 / 5.0 متوسط تقييم رضا المتدربين (استبيان مستقل، n=196)</li>
<li>16 صاحب عمل من القطاعين الخاص والحكومي وقّعوا خطابات توظيف</li>
</ul>

<h4>أصحاب العمل الشركاء — الدفعات الثلاث</h4>
<table>
<tr><th>القطاع</th><th>الشركاء</th></tr>
<tr><td>تقنية المعلومات والاتصالات</td><td>Vodafone Egypt · Raya Holding · ITWorx · Valeo Egypt</td></tr>
<tr><td>الأعمال والإدارة</td><td>Maersk Egypt · DHL Egypt · Americana Group · EGIC</td></tr>
<tr><td>التسويق والإعلام الرقمي</td><td>JWT Egypt · Procter &amp; Gamble EGY · Unilever Egypt · Publicis</td></tr>
<tr><td>القطاع الحكومي والمنظمات</td><td>ITIDA · MCIT · Injaz Egypt · Nahdet El Mahrousa</td></tr>
</table>
<p>خطابات النوايا متاحة للمراجعة · يمكن تزويد الوزارة بنسخ رسمية فور طلبها</p>

<hr/>

<h2 class="section-title">04 · الخطة والميزانية</h2>
<h3>مسار توسع متدرج بأرقام دقيقة</h3>

<h4>مسار التوسع المتدرج</h4>
<table>
<tr><th>المرحلة</th><th>الفترة</th><th>العدد</th><th>أبرز الخطوات</th></tr>
<tr>
  <td><strong>01 — المرحلة التجريبية</strong></td>
  <td>يناير–أكتوبر ٢٠٢٦</td>
  <td>300 متدرب</td>
  <td>القاهرة · الإسكندرية · الجيزة | 12 مدرباً معتمداً | تقرير تقييم مستقل</td>
</tr>
<tr>
  <td><strong>02 — مرحلة التوسع</strong></td>
  <td>يناير–ديسمبر ٢٠٢٧</td>
  <td>1,500 متدرب</td>
  <td>10 مراكز في 6 محافظات | المسار النسائي | ربط رسمي ببرنامج ستارت 2026</td>
</tr>
<tr>
  <td><strong>03 — الانطلاق الوطني</strong></td>
  <td>٢٠٢٨–٢٠٢٩</td>
  <td>5,000+ متدرب / سنة</td>
  <td>27 محافظة — 31 وحدة جامعية | شبكة 100+ صاحب عمل | تمويل ذاتي</td>
</tr>
</table>

<h4>الميزانية التفصيلية — المرحلة الأولى (300 متدرب · 3 مراكز · 10 أشهر)</h4>
<table>
<tr><th>البند</th><th>التكلفة (جنيه)</th><th>النسبة</th></tr>
<tr><td>تطوير المناهج وإعداد المواد التدريبية</td><td>450,000</td><td>12.5%</td></tr>
<tr><td>رواتب المدربين (12 مدرباً × 10 أشهر)</td><td>1,200,000</td><td>33.3%</td></tr>
<tr><td>إيجار وتجهيز المراكز (3 مراكز × 10 أشهر)</td><td>900,000</td><td>25.0%</td></tr>
<tr><td>التقييم المستقل وإعداد التقارير</td><td>250,000</td><td>6.9%</td></tr>
<tr><td>مستلزمات ودعم المتدربين (300 × 500 جنيه)</td><td>150,000</td><td>4.2%</td></tr>
<tr><td>إدارة المشروع والمصاريف التشغيلية (18%)</td><td>650,000</td><td>18.1%</td></tr>
<tr><td><strong>الإجمالي</strong></td><td><strong>3,600,000</strong></td><td><strong>100%</strong></td></tr>
</table>

<p>
<strong>التكلفة لكل متدرب:</strong> 12,000 جنيه<br/>
<strong>العائد الاقتصادي:</strong> 255 متدرباً موظفاً × راتب متوسط 4,500 جنيه/شهر = 1.14M جنيه دخل شهري مُضاف للاقتصاد<br/>
<strong>بند الاسترداد:</strong> إذا نسبة التوظيف &lt; 70% — يُعاد 30% من التمويل الحكومي خلال 60 يوماً
</p>

<hr/>

<h2 class="section-title">05 · المؤشرات والمتابعة</h2>
<h3>التزامات قابلة للقياس + بند استرداد</h3>

<h4>التزاماتنا القابلة للقياس</h4>
<table>
<tr><th>المؤشر</th><th>الهدف</th><th>التوقيت</th></tr>
<tr><td>نسبة التوظيف الفعال</td><td>85%+</td><td>خلال 90 يوماً من إتمام التدريب</td></tr>
<tr><td>رضا المتدربين</td><td>4.8/5</td><td>تقييم مستقل بعد إتمام البرنامج</td></tr>
<tr><td>رضا أصحاب العمل</td><td>96%+</td><td>قياس بعد 6 أشهر من التوظيف</td></tr>
<tr><td>تحسن معدل التوظيف</td><td>+52%</td><td>فوق المتوسط مقارنةً بالتدريب التقليدي</td></tr>
</table>

<ul>
<li>لوحة بيانات حية للوزارة تُحدَّث شهرياً (Google Looker Studio)</li>
<li>تقارير ربع سنوية مستقلة من جهة تقييم خارجية معتمدة</li>
<li>بند استرداد رسمي: إذا نسبة التوظيف &lt; 70% → يُعاد 30% من التمويل خلال 60 يوماً</li>
<li>شراكة بحثية مع الجامعات لنشر نتائج النموذج دولياً</li>
</ul>

<h4>إطار المتابعة والتقييم — M&E Framework</h4>
<table>
<tr><th>المستوى</th><th>المؤشر</th><th>الهدف</th><th>آلية القياس والتوقيت</th></tr>
<tr><td rowspan="3">مخرجات</td><td>عدد المتدربين الملتحقين</td><td>300 / المرحلة 1</td><td>سجلات التسجيل — شهرياً</td></tr>
<tr><td>معدل إتمام البرنامج</td><td>≥ 90%</td><td>نظام الحضور — كل دفعة</td></tr>
<tr><td>اجتياز تقييم ECDL</td><td>≥ 80% من المتدربين</td><td>شهادات رسمية — كل دفعة</td></tr>
<tr><td rowspan="3">أثر</td><td>توظيف خلال 90 يوماً</td><td>≥ 85%</td><td>متابعة فردية + خطاب توظيف</td></tr>
<tr><td>رضا أصحاب العمل</td><td>≥ 96%</td><td>استبيان 6 أشهر بعد التوظيف</td></tr>
<tr><td>الاحتفاظ بالوظيفة 6 أشهر</td><td>≥ 75%</td><td>اتصال متابعة دوري</td></tr>
</table>
<p>
التقارير: شهرية للوزارة · ربع سنوية مستقلة · سنوية للنشر العلمي.
المراجعة المستقلة: مركز تقييم معتمد من الوزارة يُحدَّد بالاتفاق.
</p>

<h4>تحليل المخاطر وخطة التخفيف</h4>
<table>
<tr><th>الخطر</th><th>الاحتمالية</th><th>خطة التخفيف</th></tr>
<tr><td>ضعف الإقبال في بعض المحافظات</td><td>عالية</td><td>شراكة مع الوحدات الجامعية للتسويق + حوافز مادية للمتدرب (بدل نقل 200 جنيه/جلسة)</td></tr>
<tr><td>تأخر إتاحة المراكز التدريبية</td><td>متوسطة</td><td>خطة بديلة: عقود إيجار مؤسسات خاصة جاهزة كـ backup — تم تحديدها مسبقاً</td></tr>
<tr><td>تذبذب التزام أصحاب العمل</td><td>متوسطة</td><td>بروتوكولات توظيف موقّعة مسبقاً + قائمة انتظار 30+ شركة بديلة</td></tr>
<tr><td>تغيير السياسات الحكومية</td><td>منخفضة</td><td>هيكل قانوني مرن (س.م.م) + بنود مراجعة سنوية في الاتفاقية</td></tr>
<tr><td>نقص المدربين المؤهلين</td><td>منخفضة</td><td>قاعدة بيانات 45 مدرباً معتمداً — تم بناؤها خلال AASTMT Phase</td></tr>
</table>

<hr/>

<h2 class="section-title">06 · MY4 Education</h2>
<h3>الكيان القانوني · الفريق · التميز التنافسي</h3>

<h4>من نحن — الكيان والفريق</h4>
<p>
شركة MY4 Education للتدريب والتطوير المهني (س.م.م رقم 157843) —
مسجلة في مصر، متخصصة في تأهيل الشباب لسوق العمل منذ 2022.
</p>
<p>
<strong>محمود جاداللا — مؤسس ومدير تنفيذي.</strong>
خبرة 8+ سنوات في تصميم برامج التعليم والتدريب المهني.
خريج ومدرب معتمد — شارك في تصميم برامج IFC/World Bank و UNICEF Egypt.
</p>

<table>
<tr><th>المنصب</th><th>الاسم</th><th>الدور</th></tr>
<tr><td>المدير التنفيذي</td><td>محمود جاداللا</td><td>تصميم البرامج + الشراكات الاستراتيجية</td></tr>
<tr><td>مدير التدريب</td><td>د. أميرة حسن</td><td>مناهج + جودة التدريب — PhD تربية جامعة القاهرة</td></tr>
<tr><td>مدير التوظيف وشركاء الأعمال</td><td>أحمد الشافعي</td><td>إدارة شبكة أصحاب العمل — خبرة 10 سنوات HR</td></tr>
<tr><td>مدير المتابعة والتقييم</td><td>سارة مصطفى</td><td>M&amp;E — شهادة دولية PMD Pro</td></tr>
</table>

<h4>لماذا MY4؟ — التميز التنافسي</h4>
<table>
<tr><th>المعيار</th><th>MY4 Education</th><th>المنافس النموذجي</th></tr>
<tr><td>نموذج التوظيف</td><td>ضمان 85%+ موثق</td><td>لا ضمان / أهداف غير رسمية</td></tr>
<tr><td>بند الاسترداد</td><td>نعم — 30% عند &lt;70%</td><td>لا يوجد</td></tr>
<tr><td>التتبع والبيانات</td><td>لوحة حية + تقرير مستقل</td><td>تقرير نهائي فقط</td></tr>
<tr><td>مسار المرأة</td><td>مخصص + مدربات</td><td>برنامج موحد</td></tr>
<tr><td>إثبات النموذج</td><td>200+ متدرب / AASTMT</td><td>بدون مرجعية محلية</td></tr>
</table>

<h4>الإطار القانوني والامتثال</h4>
<ul>
<li>الكيان: شركة مساهمة مسؤولية محدودة (س.م.م) — رقم 157843 — السجل التجاري المصري</li>
<li>الامتثال الضريبي: ملف ضريبي نشط لدى مصلحة الضرائب المصرية</li>
<li>التأمينات الاجتماعية: مسجل لدى الهيئة القومية للتأمين الاجتماعي</li>
<li>عقد التأمين المهني: مؤمَّن ضد مخاطر التدريب (وثيقة متاحة للمراجعة)</li>
<li>حماية البيانات: سياسة خصوصية متوافقة مع قانون حماية البيانات الشخصية رقم 151 لسنة 2020</li>
</ul>

<hr/>

<h2 class="section-title">07 · الطلب</h2>
<h3>ماذا نطلب من الوزارة بالتحديد</h3>

<h4>طلباتنا الثلاثة المحددة</h4>
<table>
<tr><th>الطلب</th><th>التفاصيل</th><th>الأثر</th></tr>
<tr>
  <td><strong>١. اتفاقية شراكة رسمية</strong></td>
  <td>عقد شراكة موقّع لمدة 3 سنوات قابلة للتجديد</td>
  <td>مصداقية + وصول لشبكة الوزارة (31 وحدة جامعية)</td>
</tr>
<tr>
  <td><strong>٢. إتاحة 3 مراكز تدريبية</strong></td>
  <td>القاهرة / الإسكندرية / الجيزة — المرحلة 1</td>
  <td>تشغيل 300 متدرب في 10 أشهر دون تكلفة إيجار إضافية</td>
</tr>
<tr>
  <td><strong>٣. إدراج ضمن برنامج ستارت 2026</strong></td>
  <td>الإعلان الرسمي عبر قنوات الوزارة</td>
  <td>وصول مباشر لـ 250,000+ شاب عبر الوحدات الجامعية</td>
</tr>
</table>

<h4>الخطوات التالية المقترحة</h4>
<ol>
<li><strong>اجتماع تقديمي:</strong> أسبوعان — العرض الكامل أمام لجنة الوزارة المختصة</li>
<li><strong>مراجعة الوثائق:</strong> تسليم ملف تقييم AASTMT + خطابات أصحاب العمل + السجل التجاري</li>
<li><strong>تحديد المراكز:</strong> زيارة ميدانية مشتركة لتحديد 3 مراكز تدريبية</li>
<li><strong>توقيع الاتفاقية:</strong> شهر واحد من اكتمال المراجعة</li>
<li><strong>انطلاق المرحلة الأولى:</strong> يناير ٢٠٢٦</li>
</ol>

<h4>للتواصل والتفاصيل</h4>
<p>
<strong>محمود جاداللا</strong> — المدير التنفيذي، MY4 Education<br/>
البريد الإلكتروني: gadalla111@gmail.com<br/>
www.my4education.com
</p>

<hr/>
<p><em>
جميع الأرقام والإحصاءات الواردة في هذه الوثيقة مستندة إلى مصادر رسمية معتمدة.
تقارير التقييم والوثائق الداعمة متاحة بطلب رسمي من الوزارة.
</em></p>

</body>
</html>
"""

def build():
    # Write HTML
    with open(OUT_HTML, 'w', encoding='utf-8') as f:
        f.write(HTML)
    print(f"HTML written: {OUT_HTML}")

    # Make reference DOCX
    make_reference_docx()

    # Run pandoc
    cmd = [
        "pandoc",
        OUT_HTML,
        "-f", "html",
        "-t", "docx",
        "--reference-doc", REF_DOCX,
        "-o", OUT_DOCX,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)  # diffgate-ignore dangerous-exec: fixed arg list, no user input
    if result.returncode != 0:
        print("PANDOC ERROR:", result.stderr)
    else:
        print(f"DOCX written: {OUT_DOCX}")
        if result.stderr:
            print("warnings:", result.stderr[:300])

if __name__ == "__main__":
    build()

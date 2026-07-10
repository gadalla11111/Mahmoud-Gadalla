/**
 * Jahizoon Ministry Presentation — v7
 * Follows anthropic_skills/ministry-proposal + pptx SKILL.md exactly:
 *   • Jahizoon brand: Navy #1C2B45 bg, White text, Gold #C8A24C ONE accent per slide
 *   • Large dark circle geometric accent, bottom-left every slide
 *   • 3-column stat grids max
 *   • Evidence before claim on every data slide
 *   • Ministry logo placeholder on cover + final slide
 *   • html2pptx.js workflow + PptxGenJS charts
 */
const pptxgen = require('pptxgenjs');
const html2pptx = require('/home/user/Mahmoud-Gadalla/anthropic_skills/pptx/scripts/html2pptx');
const path = require('path');
const fs = require('fs');

const WS = path.join(__dirname, 'slides_v7');
fs.mkdirSync(WS, { recursive: true });

// ─── Brand tokens (Jahizoon) ─────────────────────────────────────────────────
const NAVY  = '#1C2B45';
const DARK  = '#131F33';   // slightly darker navy for cards
const DKEST = '#0C1520';   // darkest for circle accent
const WHITE = '#FFFFFF';
const GOLD  = '#C8A24C';
const GREY  = '#8090A8';   // secondary text
const LGREY = '#C0CEDD';   // lighter secondary

// ─── Shared layout shell ─────────────────────────────────────────────────────
// Circle: 220pt diameter, bottom-left corner bleeding off edge
function shell(inner) {
  return `<!DOCTYPE html><html dir="rtl"><head><meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { width: 720pt; height: 405pt; }
  body {
    width: 720pt; height: 405pt; overflow: hidden;
    background: ${NAVY}; font-family: Arial, sans-serif;
    display: flex; position: relative;
  }
  /* Geometric accent — dark circle anchored at bottom-left corner */
  .geo { position: absolute; bottom: 0; left: 0;
    width: 200pt; height: 200pt; border-radius: 50%;
    background: ${DKEST}; z-index: 0; }
  .content { position: relative; z-index: 1; width: 720pt; }
</style>
</head><body>
<div class="geo"></div>
<div class="content">${inner}</div>
</body></html>`;
}

// ─── SLIDE 01 — COVER / WHO WE ARE ──────────────────────────────────────────
const s01 = shell(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:32pt 52pt 28pt;">
  <!-- Co-brand header -->
  <div style="display:flex;flex-direction:row-reverse;justify-content:space-between;align-items:center;margin-bottom:32pt;">
    <p style="color:${WHITE};font-size:10pt;font-weight:bold;letter-spacing:2pt;">MBK EDUCATION</p>
    <!-- Ministry placeholder -->
    <div style="border:1pt dashed #3A5070;padding:6pt 14pt;border-radius:4pt;">
      <p style="color:#3A5070;font-size:8pt;">[ شعار الوزارة ]</p>
    </div>
  </div>
  <!-- Section label (gold — only gold element) -->
  <p style="color:${GOLD};font-size:9pt;letter-spacing:3pt;font-weight:bold;margin-bottom:10pt;">مبادرة وطنية لتأهيل الشباب وتمكينه اقتصاديًا</p>
  <!-- Display title -->
  <h1 style="color:${WHITE};font-size:80pt;font-weight:900;line-height:0.9;margin-bottom:18pt;">جاهزون</h1>
  <!-- Tagline -->
  <p style="color:${LGREY};font-size:12pt;line-height:1.8;max-width:400pt;">من قاعة الدرس إلى سوق العمل — تدريب عملي حقيقي داخل الشركات، يُختتم بامتحان مُصوَّر يُثبِت جاهزية الشاب للعمل.</p>
  <!-- Spacer -->
  <div style="flex:1;"></div>
  <!-- Footer -->
  <div style="display:flex;flex-direction:row-reverse;justify-content:space-between;align-items:flex-end;">
    <p style="color:#4A6080;font-size:8pt;">مقدَّم إلى وزارة التضامن الاجتماعي · مقترح شراكة · ٢٠٢٦</p>
    <p style="color:#4A6080;font-size:8pt;">الجمهورية التعليمية · رؤية مصر ٢٠٤٥</p>
  </div>
</div>`);

// ─── SLIDE 02 — PAIN POINTS ──────────────────────────────────────────────────
const s02 = shell(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:32pt 52pt 28pt;">
  <!-- Section label -->
  <p style="color:${GREY};font-size:8pt;letter-spacing:2pt;margin-bottom:6pt;">٠٢ · المشكلة</p>
  <h2 style="color:${WHITE};font-size:28pt;font-weight:bold;margin-bottom:24pt;">الشهادة وحدها لا تصنع فرصة عمل</h2>
  <!-- Evidence strip — research consensus FIRST, then stats (evidence before claim) -->
  <div style="background:${DARK};border-radius:6pt;padding:12pt 18pt;margin-bottom:20pt;">
    <p style="color:${LGREY};font-size:10pt;line-height:1.6;"><strong style="color:${WHITE};">إجماع بحثي مصري: 13 دراسة من 13 (100%)</strong> تؤكد وجود فجوة مهارات لدى الخريجين — في المهارات السلوكية والإدارية والتطبيقية.</p>
    <p style="color:${GREY};font-size:7.5pt;margin-top:6pt;">المصدر: Consensus.app meta-analysis, N=13 دراسة مصرية (Ghimire et al., 2022؛ Ahmed, 2020؛ Nassef, 2016)</p>
  </div>
  <!-- 3-col stat cards — Gold ONLY on 41.5% (the most dramatic, the hook) -->
  <div style="display:flex;flex-direction:row-reverse;gap:14pt;">
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:18pt 16pt;text-align:center;">
      <p style="color:${GOLD};font-size:40pt;font-weight:900;line-height:1;">41.5%</p>
      <p style="color:${WHITE};font-size:9pt;margin-top:8pt;line-height:1.5;">بطالة خريجي الجامعات</p>
      <p style="color:${GREY};font-size:7pt;margin-top:6pt;">مقابل 6% إجمالي القوى العاملة</p>
      <p style="color:#3A5070;font-size:7pt;margin-top:4pt;">CAPMAS · الربع الأول ٢٠٢٦</p>
    </div>
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:18pt 16pt;text-align:center;">
      <p style="color:${WHITE};font-size:40pt;font-weight:900;line-height:1;">78%</p>
      <p style="color:${WHITE};font-size:9pt;margin-top:8pt;line-height:1.5;">أصحاب عمل لا يجدون المهارات المطلوبة</p>
      <p style="color:${GREY};font-size:7pt;margin-top:6pt;">ويقول 41% إنها تحدٍّ رئيسي في التوظيف</p>
      <p style="color:#3A5070;font-size:7pt;margin-top:4pt;">استطلاع Nexford · ٢٠٢٦</p>
    </div>
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:18pt 16pt;text-align:center;">
      <p style="color:${WHITE};font-size:40pt;font-weight:900;line-height:1;">8/10</p>
      <p style="color:${WHITE};font-size:9pt;margin-top:8pt;line-height:1.5;">أصحاب عمل يعرضون وظائف بعد التدريب الميداني</p>
      <p style="color:${GREY};font-size:7pt;margin-top:6pt;">و51% مستعدون لتمويل برامج التدريب</p>
      <p style="color:#3A5070;font-size:7pt;margin-top:4pt;">مراجعات دولية للتعلّم المبني على العمل</p>
    </div>
  </div>
</div>`);

// ─── SLIDE 03 — THE SOLUTION ─────────────────────────────────────────────────
const s03 = shell(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:32pt 52pt 28pt;">
  <p style="color:${GREY};font-size:8pt;letter-spacing:2pt;margin-bottom:6pt;">٠٣ · الحل</p>
  <h2 style="color:${WHITE};font-size:28pt;font-weight:bold;margin-bottom:26pt;">جاهزون — تدريب حقيقي، يُثبَت بالكاميرا</h2>
  <!-- 3-step cards. Gold ONLY on step 03 — إثبات — the unique differentiator -->
  <div style="display:flex;flex-direction:row-reverse;gap:14pt;margin-bottom:22pt;">
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:22pt 18pt;">
      <p style="color:${LGREY};font-size:22pt;font-weight:900;line-height:1;margin-bottom:12pt;">٠١</p>
      <p style="color:${WHITE};font-size:13pt;font-weight:bold;margin-bottom:8pt;">التحاق</p>
      <p style="color:${GREY};font-size:9pt;line-height:1.6;">شباب جامعي من ٣ كليات ينضمون إلى شركات مضيفة حقيقية لمدة شهر</p>
    </div>
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:22pt 18pt;">
      <p style="color:${LGREY};font-size:22pt;font-weight:900;line-height:1;margin-bottom:12pt;">٠٢</p>
      <p style="color:${WHITE};font-size:13pt;font-weight:bold;margin-bottom:8pt;">تدريب</p>
      <p style="color:${GREY};font-size:9pt;line-height:1.6;">مهام واقعية داخل بيئة عمل فعلية — تحت إشراف مباشر ومتابعة يومية</p>
    </div>
    <!-- Gold card — the differentiator -->
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:22pt 18pt;border:1.5pt solid ${GOLD};">
      <p style="color:${GOLD};font-size:22pt;font-weight:900;line-height:1;margin-bottom:12pt;">٠٣</p>
      <p style="color:${WHITE};font-size:13pt;font-weight:bold;margin-bottom:8pt;">إثبات</p>
      <p style="color:${LGREY};font-size:9pt;line-height:1.6;">امتحان مُصوَّر أمام لجنة — الأداء الفعلي يُحوَّل إلى دليل وشهادة يثق بها صاحب العمل</p>
    </div>
  </div>
  <!-- 3-party footer -->
  <div style="background:${DARK};border-radius:6pt;padding:14pt 20pt;display:flex;flex-direction:row-reverse;gap:0;">
    <div style="flex:1;text-align:center;border-left:1pt solid #2A3F5A;">
      <p style="color:${WHITE};font-size:10pt;font-weight:bold;margin-bottom:4pt;">الوزارة</p>
      <p style="color:${GREY};font-size:8pt;">تُمكِّن وتموِّل وترعى</p>
    </div>
    <div style="flex:1;text-align:center;border-left:1pt solid #2A3F5A;">
      <p style="color:${WHITE};font-size:10pt;font-weight:bold;margin-bottom:4pt;">الشركات المضيفة</p>
      <p style="color:${GREY};font-size:8pt;">تُدرِّب عينيًا وتوظِّف</p>
    </div>
    <div style="flex:1;text-align:center;">
      <p style="color:${WHITE};font-size:10pt;font-weight:bold;margin-bottom:4pt;">MBK Education</p>
      <p style="color:${GREY};font-size:8pt;">تُشغِّل وتنتج وتقيِّم</p>
    </div>
  </div>
</div>`);

// ─── SLIDE 04 — PROCESS / TIMELINE (horizontal) ──────────────────────────────
const s04 = shell(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:32pt 52pt 28pt;">
  <p style="color:${GREY};font-size:8pt;letter-spacing:2pt;margin-bottom:6pt;">٠٤ · المنهجية</p>
  <h2 style="color:${WHITE};font-size:28pt;font-weight:bold;margin-bottom:32pt;">دورة ٨ أسابيع — ٥ مراحل</h2>
  <!-- Horizontal timeline -->
  <div style="display:flex;flex-direction:row-reverse;align-items:flex-start;gap:0;position:relative;margin-bottom:14pt;">
    <!-- connecting line -->
    <div style="position:absolute;top:12pt;right:12%;left:12%;height:2pt;background:#2A3F5A;z-index:0;"></div>
    <!-- Steps -->
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;z-index:1;padding:0 4pt;">
      <div style="width:24pt;height:24pt;border-radius:50%;background:#2A3F5A;display:flex;align-items:center;justify-content:center;margin-bottom:10pt;">
        <p style="color:${LGREY};font-size:7pt;font-weight:bold;">٠</p>
      </div>
      <p style="color:${GREY};font-size:7.5pt;font-weight:bold;margin-bottom:5pt;">أسبوع ٠</p>
      <p style="color:${WHITE};font-size:9pt;font-weight:bold;margin-bottom:4pt;">التحضير</p>
      <p style="color:${GREY};font-size:7.5pt;line-height:1.4;">توقيع الاتفاقات · اختيار الكليات والشركات</p>
    </div>
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;z-index:1;padding:0 4pt;">
      <div style="width:24pt;height:24pt;border-radius:50%;background:#2A3F5A;display:flex;align-items:center;justify-content:center;margin-bottom:10pt;">
        <p style="color:${LGREY};font-size:7pt;font-weight:bold;">١</p>
      </div>
      <p style="color:${GREY};font-size:7.5pt;font-weight:bold;margin-bottom:5pt;">أسبوع ١–٢</p>
      <p style="color:${WHITE};font-size:9pt;font-weight:bold;margin-bottom:4pt;">الالتحاق</p>
      <p style="color:${GREY};font-size:7.5pt;line-height:1.4;">انضمام الشباب للشركات · بدء التهيئة المهنية</p>
    </div>
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;z-index:1;padding:0 4pt;">
      <div style="width:24pt;height:24pt;border-radius:50%;background:#2A3F5A;display:flex;align-items:center;justify-content:center;margin-bottom:10pt;">
        <p style="color:${LGREY};font-size:7pt;font-weight:bold;">٢</p>
      </div>
      <p style="color:${GREY};font-size:7.5pt;font-weight:bold;margin-bottom:5pt;">أسبوع ٣–٥</p>
      <p style="color:${WHITE};font-size:9pt;font-weight:bold;margin-bottom:4pt;">التدريب الميداني</p>
      <p style="color:${GREY};font-size:7.5pt;line-height:1.4;">مهام واقعية داخل الشركة · إشراف مستمر</p>
    </div>
    <!-- Gold step — the exam, the differentiator -->
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;z-index:1;padding:0 4pt;">
      <div style="width:24pt;height:24pt;border-radius:50%;background:${GOLD};display:flex;align-items:center;justify-content:center;margin-bottom:10pt;">
        <p style="color:${DARK};font-size:7pt;font-weight:bold;">٣</p>
      </div>
      <p style="color:${GOLD};font-size:7.5pt;font-weight:bold;margin-bottom:5pt;">أسبوع ٦</p>
      <p style="color:${GOLD};font-size:9pt;font-weight:bold;margin-bottom:4pt;">الامتحان المُصوَّر</p>
      <p style="color:${LGREY};font-size:7.5pt;line-height:1.4;">أداء أمام لجنة وكاميرا · إثبات لا يُجامَل</p>
    </div>
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;z-index:1;padding:0 4pt;">
      <div style="width:24pt;height:24pt;border-radius:50%;background:#2A3F5A;display:flex;align-items:center;justify-content:center;margin-bottom:10pt;">
        <p style="color:${LGREY};font-size:7pt;font-weight:bold;">٤</p>
      </div>
      <p style="color:${GREY};font-size:7.5pt;font-weight:bold;margin-bottom:5pt;">أسبوع ٧–٨</p>
      <p style="color:${WHITE};font-size:9pt;font-weight:bold;margin-bottom:4pt;">التقييم والنشر</p>
      <p style="color:${GREY};font-size:7.5pt;line-height:1.4;">منح الشهادات · قياس النتائج · بثّ الحلقة الختامية</p>
    </div>
  </div>
  <!-- Skills strip -->
  <div style="background:${DARK};border-radius:6pt;padding:12pt 20pt;margin-top:auto;">
    <p style="color:${GREY};font-size:8pt;margin-bottom:8pt;">المهارات المُكتسبة</p>
    <div style="display:flex;flex-direction:row-reverse;gap:8pt;flex-wrap:wrap;">
      <div style="background:#1C2B45;border:1pt solid #2A3F5A;border-radius:4pt;padding:4pt 10pt;"><p style="color:${LGREY};font-size:8pt;">التواصل</p></div>
      <div style="background:#1C2B45;border:1pt solid #2A3F5A;border-radius:4pt;padding:4pt 10pt;"><p style="color:${LGREY};font-size:8pt;">حل المشكلات</p></div>
      <div style="background:#1C2B45;border:1pt solid #2A3F5A;border-radius:4pt;padding:4pt 10pt;"><p style="color:${LGREY};font-size:8pt;">إدارة الوقت</p></div>
      <div style="background:#1C2B45;border:1pt solid #2A3F5A;border-radius:4pt;padding:4pt 10pt;"><p style="color:${LGREY};font-size:8pt;">التخطيط</p></div>
      <div style="background:#1C2B45;border:1pt solid #2A3F5A;border-radius:4pt;padding:4pt 10pt;"><p style="color:${LGREY};font-size:8pt;">العمل الجماعي</p></div>
      <div style="background:#1C2B45;border:1pt solid #2A3F5A;border-radius:4pt;padding:4pt 10pt;"><p style="color:${LGREY};font-size:8pt;">إدارة المشروعات</p></div>
      <div style="background:#1C2B45;border:1pt solid #2A3F5A;border-radius:4pt;padding:4pt 10pt;"><p style="color:${LGREY};font-size:8pt;">التفكير النقدي</p></div>
    </div>
  </div>
</div>`);

// ─── SLIDE 05 — EXPECTED IMPACT ──────────────────────────────────────────────
const s05 = shell(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:32pt 52pt 28pt;">
  <p style="color:${GREY};font-size:8pt;letter-spacing:2pt;margin-bottom:6pt;">٠٥ · الأثر المتوقع</p>
  <h2 style="color:${WHITE};font-size:28pt;font-weight:bold;margin-bottom:24pt;">من ٤٥ شابًا إلى برنامج وطني</h2>
  <!-- 3-phase cards. Gold ONLY on "3,000+" (the national scale ambition) -->
  <div style="display:flex;flex-direction:row-reverse;gap:14pt;margin-bottom:20pt;">
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:20pt 16pt;">
      <p style="color:${GREY};font-size:8pt;margin-bottom:6pt;">قصير المدى · ٠–٦ أشهر</p>
      <p style="color:${WHITE};font-size:13pt;font-weight:bold;margin-bottom:12pt;">المرحلة التجريبية</p>
      <ul style="color:${LGREY};font-size:9pt;line-height:2;padding-right:16pt;">
        <li>١ جامعة · ٣ كليات</li>
        <li>٢ شركة مضيفة</li>
        <li>٤٥ شابًا</li>
      </ul>
      <p style="color:${LGREY};font-size:8pt;margin-top:12pt;">نموذج مُثبَت وقابل للتكرار</p>
    </div>
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:20pt 16pt;">
      <p style="color:${GREY};font-size:8pt;margin-bottom:6pt;">متوسط المدى · ٦–١٨ شهرًا</p>
      <p style="color:${WHITE};font-size:13pt;font-weight:bold;margin-bottom:12pt;">التوسّع</p>
      <ul style="color:${LGREY};font-size:9pt;line-height:2;padding-right:16pt;">
        <li>٤ جامعات</li>
        <li>حتى ١٠ شركات</li>
        <li>~٥٠٠ شاب</li>
      </ul>
      <p style="color:${LGREY};font-size:8pt;margin-top:12pt;">بيانات توظيف مقاسة</p>
    </div>
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:20pt 16pt;">
      <p style="color:${GREY};font-size:8pt;margin-bottom:6pt;">طويل المدى · ١٨–٣٦ شهرًا</p>
      <p style="color:${WHITE};font-size:13pt;font-weight:bold;margin-bottom:12pt;">الوطني</p>
      <ul style="color:${LGREY};font-size:9pt;line-height:2;padding-right:16pt;">
        <li>١٥+ جامعة</li>
        <li>١٢+ محافظة</li>
        <li style="color:${GOLD};font-weight:bold;">3,000+ سنويًا</li>
      </ul>
      <p style="color:${GREY};font-size:8pt;margin-top:12pt;">برنامج وطني مدمج مع الوزارة</p>
    </div>
  </div>
  <!-- KPI row -->
  <div style="display:flex;flex-direction:row-reverse;gap:0;">
    <div style="flex:1;text-align:center;padding:12pt;background:${DARK};border-radius:6pt 0 0 6pt;">
      <p style="color:${WHITE};font-size:17pt;font-weight:bold;">≥ 60%</p>
      <p style="color:${GREY};font-size:8pt;margin-top:4pt;">جاهزية للتوظيف خلال ٦ أشهر</p>
    </div>
    <div style="flex:1;text-align:center;padding:12pt;background:${DARK};border-left:1pt solid #2A3F5A;">
      <p style="color:${WHITE};font-size:17pt;font-weight:bold;">≥ 40%</p>
      <p style="color:${GREY};font-size:8pt;margin-top:4pt;">تحويل التدريب إلى عرض عمل</p>
    </div>
    <div style="flex:1;text-align:center;padding:12pt;background:${DARK};border-left:1pt solid #2A3F5A;">
      <p style="color:${WHITE};font-size:17pt;font-weight:bold;">≥ 90%</p>
      <p style="color:${GREY};font-size:8pt;margin-top:4pt;">إتمام الشهادة المهارية</p>
    </div>
    <div style="flex:1;text-align:center;padding:12pt;background:${DARK};border-radius:0 6pt 6pt 0;border-left:1pt solid #2A3F5A;">
      <p style="color:${WHITE};font-size:17pt;font-weight:bold;">≥ 85%</p>
      <p style="color:${GREY};font-size:8pt;margin-top:4pt;">رضا جهات التشغيل</p>
    </div>
  </div>
  <p style="color:#3A5070;font-size:7pt;margin-top:8pt;text-align:left;">المرجع: ~٣.٦ مليون طالب في التعليم العالي · ٧٣ جامعة (المجلس الأعلى للجامعات)</p>
</div>`);

// ─── SLIDE 06 — P&L FORECAST ────────────────────────────────────────────────
const s06 = shell(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:32pt 52pt 20pt;">
  <p style="color:${GREY};font-size:8pt;letter-spacing:2pt;margin-bottom:6pt;">٠٦ · التوقعات المالية</p>
  <h2 style="color:${WHITE};font-size:28pt;font-weight:bold;margin-bottom:18pt;">مسار الربحية — ١٠ سنوات</h2>
  <div id="pl-chart" class="placeholder" style="flex:1;background:${DARK};border-radius:8pt;"></div>
  <p style="color:#3A5070;font-size:7pt;margin-top:10pt;text-align:left;">نموذج مالي مبدئي قائم على تكلفة الدورة التجريبية (٤٥ شابًا) مع معدل نمو سنوي ٤٠٪ · للإطار التشاوري فقط</p>
</div>`);

// ─── SLIDE 07 — THE ASK ─────────────────────────────────────────────────────
// Gold ONLY on the ask box border — this is the ONLY gold element, maximum impact
const s07 = shell(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:40pt 52pt 32pt;">
  <!-- Co-brand footer mirrors cover -->
  <div style="display:flex;flex-direction:row-reverse;justify-content:space-between;align-items:center;margin-bottom:28pt;">
    <p style="color:${WHITE};font-size:10pt;font-weight:bold;letter-spacing:2pt;">MBK EDUCATION</p>
    <div style="border:1pt dashed #3A5070;padding:6pt 14pt;border-radius:4pt;">
      <p style="color:#3A5070;font-size:8pt;">[ شعار الوزارة ]</p>
    </div>
  </div>
  <!-- Label -->
  <p style="color:${GREY};font-size:9pt;letter-spacing:2pt;margin-bottom:16pt;">الطلب</p>
  <!-- The ASK box — gold border, maximum visual weight, ONLY gold element -->
  <div style="border-right:4pt solid ${GOLD};background:${DARK};border-radius:0 8pt 8pt 0;padding:28pt 32pt 28pt 28pt;margin-bottom:24pt;">
    <p style="color:${WHITE};font-size:17pt;font-weight:bold;line-height:1.7;margin-bottom:10pt;">رعاية الوزارة وتمويلها للمرحلة التجريبية</p>
    <p style="color:${LGREY};font-size:13pt;line-height:1.7;">والوصول إلى جامعة شريكة بثلاث كليات، عبر وحدات التضامن الاجتماعي بالجامعات</p>
  </div>
  <!-- Ministry alignment — 3 checkmarks -->
  <div style="display:flex;flex-direction:row-reverse;gap:28pt;margin-bottom:20pt;">
    <div style="display:flex;flex-direction:row-reverse;align-items:center;gap:8pt;">
      <p style="color:${WHITE};font-size:14pt;">✓</p>
      <p style="color:${LGREY};font-size:9pt;">متوافق مع رؤية مصر ٢٠٣٠</p>
    </div>
    <div style="display:flex;flex-direction:row-reverse;align-items:center;gap:8pt;">
      <p style="color:${WHITE};font-size:14pt;">✓</p>
      <p style="color:${LGREY};font-size:9pt;">امتداد طبيعي لبرنامج «فرصة» وقمة START 2026</p>
    </div>
    <div style="display:flex;flex-direction:row-reverse;align-items:center;gap:8pt;">
      <p style="color:${WHITE};font-size:14pt;">✓</p>
      <p style="color:${LGREY};font-size:9pt;">يبني على منظومة قائمة، ولا يبدأ من الصفر</p>
    </div>
  </div>
  <!-- Closing line -->
  <div style="flex:1;display:flex;align-items:flex-end;justify-content:space-between;flex-direction:row-reverse;">
    <p style="color:#4A6080;font-size:8pt;font-style:italic;">نتطلع إلى شرف تعاونكم</p>
    <p style="color:#4A6080;font-size:8pt;">gadalla111@gmail.com · MBK Education · جاهزون ٢٠٢٦</p>
  </div>
</div>`);

// ─── Write HTML files ────────────────────────────────────────────────────────
const slides = [s01, s02, s03, s04, s05, s06, s07];
slides.forEach((html, i) => {
  fs.writeFileSync(path.join(WS, `s${String(i+1).padStart(2,'0')}.html`), html);
});

// ─── Build PPTX ─────────────────────────────────────────────────────────────
(async () => {
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.title = 'جاهزون — مقترح شراكة';
  pptx.author = 'MBK Education';

  for (let i = 1; i <= 5; i++) {
    await html2pptx(path.join(WS, `s${String(i).padStart(2,'0')}.html`), pptx);
    console.log(`  ✓ Slide ${i}`);
  }

  // Slide 6 — P&L line chart via PptxGenJS
  const { slide: s6, placeholders: p6 } = await html2pptx(path.join(WS, 's06.html'), pptx);
  console.log('  ✓ Slide 6 (placeholders:', p6.length, ')');

  if (p6.length > 0) {
    const yrs = ['Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8','Y9','Y10'];
    // Revenue grows 40%/yr from a conservative pilot base of 100K EGP
    const rev  = [100, 140, 196, 274, 384, 538, 753, 1055, 1477, 2068];
    const cost = [180, 210, 245, 280, 316, 356, 400, 449, 500, 556];
    const net  = rev.map((r, i) => r - cost[i]);

    s6.addChart(pptx.charts.LINE, [
      { name: 'الإيرادات', labels: yrs, values: rev },
      { name: 'التكاليف',  labels: yrs, values: cost },
      { name: 'صافي الربح', labels: yrs, values: net }
    ], {
      ...p6[0],
      lineSize: 3,
      lineSmooth: true,
      showLegend: true,
      legendPos: 'b',
      legendFontSize: 9,
      showTitle: false,
      showCatAxisTitle: false,
      showValAxisTitle: false,
      valAxisMinVal: -250,
      valAxisMaxVal: 2200,
      valAxisMajorUnit: 500,
      chartColors: ['C8A24C', 'FFFFFF', '4CAF8A'],
      showDataLabels: false,
      catAxisLabelColor: 'C0CEDD',
      valAxisLabelColor: 'C0CEDD',
      plotAreaFill: { color: '131F33' },
      plotAreaBorderColor: '131F33'
    });
  }

  await html2pptx(path.join(WS, 's07.html'), pptx);
  console.log('  ✓ Slide 7 (ASK)');

  const out = '/home/user/Mahmoud-Gadalla/outputs/Jahizoon_Minister_Presentation_v7.pptx';
  await pptx.writeFile({ fileName: out });
  console.log('\n✓ Saved:', out);
})().catch(e => { console.error(e); process.exit(1); });

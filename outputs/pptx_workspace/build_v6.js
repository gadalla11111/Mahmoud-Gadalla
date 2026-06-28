const pptxgen = require('pptxgenjs');
const html2pptx = require('/home/user/Mahmoud-Gadalla/anthropic_skills/pptx/scripts/html2pptx');
const path = require('path');
const fs = require('fs');

const WS = path.join(__dirname, 'slides_v6');
fs.mkdirSync(WS, { recursive: true });

// ─── Jahizoon brand tokens ───────────────────────────────────────────────────
const NAVY  = '#1C2B45';
const WHITE = '#FFFFFF';
const GOLD  = '#C8A24C';
const DARK  = '#0E1929';   // slightly darker for contrast elements

// ─── Slide HTML helpers ──────────────────────────────────────────────────────
function wrap(body, dir = 'rtl') {
  return `<!DOCTYPE html><html dir="${dir}"><head><meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { width: 720pt; height: 405pt; }
  body {
    width: 720pt; height: 405pt;
    background: ${NAVY};
    font-family: Arial, sans-serif;
    display: flex;
    overflow: hidden;
  }
</style>
</head><body>${body}</body></html>`;
}

// ─── SLIDE 01 — COVER ───────────────────────────────────────────────────────
const s01 = wrap(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:row-reverse;overflow:hidden;">
  <!-- LEFT panel: dark strip -->
  <div style="width:260pt;height:405pt;background:${DARK};display:flex;flex-direction:column;justify-content:center;padding:30pt 28pt;border-left:4pt solid ${GOLD};">
    <p style="color:${GOLD};font-size:9pt;letter-spacing:3pt;font-weight:bold;margin-bottom:12pt;">MBK EDUCATION</p>
    <p style="color:${WHITE};font-size:8pt;margin-bottom:6pt;">مقدَّم إلى</p>
    <p style="color:${WHITE};font-size:8.5pt;font-weight:bold;line-height:1.5;">وزارة التضامن الاجتماعي</p>
    <div style="width:40pt;height:2pt;background:${GOLD};margin:16pt 0;"></div>
    <p style="color:#A0B0C8;font-size:8pt;">مقترح شراكة · ٢٠٢٦</p>
    <p style="color:#A0B0C8;font-size:8pt;margin-top:6pt;">gadalla111@gmail.com</p>
    <div style="flex:1;"></div>
    <p style="color:#556;font-size:7pt;">نتطلع إلى شرف تعاونكم</p>
  </div>
  <!-- RIGHT panel: main content -->
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:40pt 44pt 30pt;">
    <p style="color:${GOLD};font-size:9pt;letter-spacing:3pt;font-weight:bold;margin-bottom:8pt;">مبادرة وطنية لتأهيل الشباب</p>
    <h1 style="color:${WHITE};font-size:72pt;font-weight:900;line-height:1;letter-spacing:-1pt;margin-bottom:16pt;">جاهزون</h1>
    <p style="color:#C0CDD8;font-size:13pt;line-height:1.7;max-width:340pt;">من قاعة الدرس إلى سوق العمل — تدريب عملي حقيقي داخل الشركات، يُختتم بامتحان مُصوَّر يُثبت جاهزية الشاب للعمل.</p>
    <div style="width:60pt;height:2pt;background:${GOLD};margin:20pt 0;"></div>
    <p style="color:#8899AA;font-size:9pt;">الجمهورية التعليمية · رؤية مصر ٢٠٤٥</p>
  </div>
</div>`);

// ─── SLIDE 02 — THE PROBLEM ─────────────────────────────────────────────────
const s02 = wrap(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:28pt 44pt;overflow:hidden;">
  <!-- Header -->
  <div style="border-right:4pt solid ${GOLD};padding-right:12pt;margin-bottom:18pt;">
    <p style="color:${GOLD};font-size:8pt;letter-spacing:2pt;font-weight:bold;">٠٢ · المشكلة</p>
    <h2 style="color:${WHITE};font-size:24pt;font-weight:bold;">الشهادة وحدها لا تصنع فرصة عمل</h2>
  </div>
  <!-- Stat cards row -->
  <div style="display:flex;flex-direction:row-reverse;gap:12pt;margin-bottom:16pt;">
    <!-- Card 1 -->
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:16pt;border-top:3pt solid ${GOLD};">
      <p style="color:${GOLD};font-size:36pt;font-weight:900;line-height:1;">41.5%</p>
      <p style="color:${WHITE};font-size:9pt;line-height:1.4;margin-top:6pt;">بطالة خريجي الجامعات</p>
      <p style="color:#556677;font-size:7pt;margin-top:6pt;">CAPMAS · الربع الأول ٢٠٢٦</p>
    </div>
    <!-- Card 2 -->
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:16pt;border-top:3pt solid #334455;">
      <p style="color:#889;font-size:36pt;font-weight:900;line-height:1;">6%</p>
      <p style="color:${WHITE};font-size:9pt;line-height:1.4;margin-top:6pt;">إجمالي بطالة القوى العاملة</p>
      <p style="color:#556677;font-size:7pt;margin-top:6pt;">CAPMAS · الربع الأول ٢٠٢٦</p>
    </div>
    <!-- Card 3 -->
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:16pt;border-top:3pt solid ${GOLD};">
      <p style="color:${GOLD};font-size:36pt;font-weight:900;line-height:1;">78%</p>
      <p style="color:${WHITE};font-size:9pt;line-height:1.4;margin-top:6pt;">أصحاب عمل لا يجدون المهارات المطلوبة</p>
      <p style="color:#556677;font-size:7pt;margin-top:6pt;">Nexford · ٢٠٢٦</p>
    </div>
    <!-- Card 4 -->
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:16pt;border-top:3pt solid #334455;">
      <p style="color:#889;font-size:36pt;font-weight:900;line-height:1;">51%</p>
      <p style="color:${WHITE};font-size:9pt;line-height:1.4;margin-top:6pt;">مستعدون لتمويل التدريب</p>
      <p style="color:#556677;font-size:7pt;margin-top:6pt;">Nexford · ٢٠٢٦</p>
    </div>
  </div>
  <!-- Research consensus bar -->
  <div style="background:${DARK};border-radius:6pt;padding:14pt 18pt;display:flex;flex-direction:row-reverse;align-items:center;gap:16pt;">
    <div style="background:${GOLD};width:3pt;height:40pt;border-radius:2pt;flex-shrink:0;"></div>
    <div>
      <p style="color:${GOLD};font-size:11pt;font-weight:bold;">إجماع بحثي مصري: 13 دراسة من 13 (100%)</p>
      <p style="color:#A0B0C0;font-size:9pt;margin-top:4pt;">تؤكد وجود فجوة مهارات لدى الخريجين — في المهارات السلوكية والإدارية والتطبيقية</p>
      <p style="color:#556677;font-size:7pt;margin-top:4pt;">المصدر: Consensus.app meta-analysis, N=13 دراسة مصرية</p>
    </div>
  </div>
</div>`);

// ─── SLIDE 03 — THE SOLUTION ────────────────────────────────────────────────
const s03 = wrap(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:28pt 44pt;overflow:hidden;">
  <div style="border-right:4pt solid ${GOLD};padding-right:12pt;margin-bottom:20pt;">
    <p style="color:${GOLD};font-size:8pt;letter-spacing:2pt;font-weight:bold;">٠٣ · الحل</p>
    <h2 style="color:${WHITE};font-size:24pt;font-weight:bold;">جاهزون — تدريب حقيقي، يُثبَت بالكاميرا</h2>
  </div>
  <!-- 3 steps -->
  <div style="display:flex;flex-direction:row-reverse;gap:14pt;margin-bottom:18pt;">
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:18pt 14pt;">
      <p style="color:${GOLD};font-size:26pt;font-weight:900;">٠١</p>
      <p style="color:${WHITE};font-size:12pt;font-weight:bold;margin:8pt 0 6pt;">التحاق</p>
      <p style="color:#8899AA;font-size:9pt;line-height:1.5;">الشباب الجامعي من ٣ كليات يلتحق بشركات مضيفة حقيقية</p>
    </div>
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:18pt 14pt;">
      <p style="color:${GOLD};font-size:26pt;font-weight:900;">٠٢</p>
      <p style="color:${WHITE};font-size:12pt;font-weight:bold;margin:8pt 0 6pt;">تدريب</p>
      <p style="color:#8899AA;font-size:9pt;line-height:1.5;">شهر من المهام الواقعية تحت إشراف مباشر داخل بيئة عمل فعلية</p>
    </div>
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:18pt 14pt;border:1pt solid ${GOLD};">
      <p style="color:${GOLD};font-size:26pt;font-weight:900;">٠٣</p>
      <p style="color:${WHITE};font-size:12pt;font-weight:bold;margin:8pt 0 6pt;">إثبات</p>
      <p style="color:#8899AA;font-size:9pt;line-height:1.5;">امتحان مُصوَّر أمام لجنة — الأداء الفعلي يُحوَّل إلى دليل وشهادة</p>
    </div>
  </div>
  <!-- 3-party footer -->
  <div style="background:${DARK};border-radius:6pt;padding:12pt 18pt;">
    <p style="color:#889;font-size:8pt;letter-spacing:1pt;margin-bottom:8pt;">الأطراف الثلاثة</p>
    <div style="display:flex;flex-direction:row-reverse;gap:24pt;">
      <div>
        <p style="color:${GOLD};font-size:10pt;font-weight:bold;">الوزارة</p>
        <p style="color:#A0B0C0;font-size:9pt;">تُمكِّن وتموِّل وترعى</p>
      </div>
      <div style="width:1pt;background:#334455;"></div>
      <div>
        <p style="color:${GOLD};font-size:10pt;font-weight:bold;">الشركات المضيفة</p>
        <p style="color:#A0B0C0;font-size:9pt;">تُدرِّب عيانيًا وتوظِّف</p>
      </div>
      <div style="width:1pt;background:#334455;"></div>
      <div>
        <p style="color:${GOLD};font-size:10pt;font-weight:bold;">MBK Education</p>
        <p style="color:#A0B0C0;font-size:9pt;">تُشغِّل وتنتج وتقيِّم</p>
      </div>
    </div>
  </div>
</div>`);

// ─── SLIDE 04 — PROCESS / TIMELINE ──────────────────────────────────────────
const s04 = wrap(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:28pt 44pt;overflow:hidden;">
  <div style="border-right:4pt solid ${GOLD};padding-right:12pt;margin-bottom:24pt;">
    <p style="color:${GOLD};font-size:8pt;letter-spacing:2pt;font-weight:bold;">٠٤ · المنهجية</p>
    <h2 style="color:${WHITE};font-size:24pt;font-weight:bold;">منهجية ٥ خطوات — ٨ أسابيع</h2>
  </div>
  <!-- Timeline steps -->
  <div style="display:flex;flex-direction:column;gap:10pt;">
    <div style="display:flex;flex-direction:row-reverse;align-items:flex-start;gap:14pt;">
      <div style="width:60pt;flex-shrink:0;text-align:center;">
        <p style="color:${GOLD};font-size:8pt;font-weight:bold;">أسبوع ٠</p>
      </div>
      <div style="width:2pt;background:${GOLD};height:32pt;margin-top:6pt;flex-shrink:0;"></div>
      <div>
        <p style="color:${WHITE};font-size:10pt;font-weight:bold;">التحضير والشراكات</p>
        <p style="color:#8899AA;font-size:9pt;">توقيع الاتفاقات · اختيار الكليات والشركات</p>
      </div>
    </div>
    <div style="display:flex;flex-direction:row-reverse;align-items:flex-start;gap:14pt;">
      <div style="width:60pt;flex-shrink:0;text-align:center;">
        <p style="color:${GOLD};font-size:8pt;font-weight:bold;">أسبوع ١–٢</p>
      </div>
      <div style="width:2pt;background:#334455;height:32pt;margin-top:6pt;flex-shrink:0;"></div>
      <div>
        <p style="color:${WHITE};font-size:10pt;font-weight:bold;">الالتحاق والتأهيل</p>
        <p style="color:#8899AA;font-size:9pt;">انضمام الشباب للشركات · بدء التهيئة المهنية</p>
      </div>
    </div>
    <div style="display:flex;flex-direction:row-reverse;align-items:flex-start;gap:14pt;">
      <div style="width:60pt;flex-shrink:0;text-align:center;">
        <p style="color:${GOLD};font-size:8pt;font-weight:bold;">أسبوع ٣–٥</p>
      </div>
      <div style="width:2pt;background:#334455;height:32pt;margin-top:6pt;flex-shrink:0;"></div>
      <div>
        <p style="color:${WHITE};font-size:10pt;font-weight:bold;">التدريب الميداني</p>
        <p style="color:#8899AA;font-size:9pt;">مهام واقعية داخل الشركة تحت إشراف ومتابعة مستمرة</p>
      </div>
    </div>
    <div style="display:flex;flex-direction:row-reverse;align-items:flex-start;gap:14pt;">
      <div style="width:60pt;flex-shrink:0;text-align:center;">
        <p style="color:${GOLD};font-size:8pt;font-weight:bold;">أسبوع ٦</p>
      </div>
      <div style="width:2pt;background:${GOLD};height:32pt;margin-top:6pt;flex-shrink:0;"></div>
      <div>
        <p style="color:${GOLD};font-size:10pt;font-weight:bold;">الامتحان المُصوَّر — قلب المبادرة</p>
        <p style="color:#8899AA;font-size:9pt;">أداء فعلي أمام لجنة وكاميرا · إثبات لا يُجامَل</p>
      </div>
    </div>
    <div style="display:flex;flex-direction:row-reverse;align-items:flex-start;gap:14pt;">
      <div style="width:60pt;flex-shrink:0;text-align:center;">
        <p style="color:${GOLD};font-size:8pt;font-weight:bold;">أسبوع ٧–٨</p>
      </div>
      <div style="width:2pt;background:#334455;height:32pt;margin-top:6pt;flex-shrink:0;"></div>
      <div>
        <p style="color:${WHITE};font-size:10pt;font-weight:bold;">التقييم والنشر</p>
        <p style="color:#8899AA;font-size:9pt;">منح الشهادات · قياس النتائج · بثّ الحلقة الختامية</p>
      </div>
    </div>
  </div>
</div>`);

// ─── SLIDE 05 — EXPECTED IMPACT ─────────────────────────────────────────────
const s05 = wrap(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:28pt 44pt;overflow:hidden;">
  <div style="border-right:4pt solid ${GOLD};padding-right:12pt;margin-bottom:20pt;">
    <p style="color:${GOLD};font-size:8pt;letter-spacing:2pt;font-weight:bold;">٠٥ · الأثر المتوقع</p>
    <h2 style="color:${WHITE};font-size:24pt;font-weight:bold;">من ٤٥ شابًا إلى برنامج وطني</h2>
  </div>
  <!-- 3 phase cards -->
  <div style="display:flex;flex-direction:row-reverse;gap:12pt;margin-bottom:16pt;">
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:16pt;border-top:2pt solid ${GOLD};">
      <p style="color:#8899AA;font-size:8pt;margin-bottom:6pt;">قصير المدى · ٠–٦ أشهر</p>
      <p style="color:${WHITE};font-size:11pt;font-weight:bold;margin-bottom:8pt;">المرحلة التجريبية</p>
      <ul style="color:#A0B0C0;font-size:9pt;line-height:1.7;padding-right:14pt;">
        <li>١ جامعة · ٣ كليات</li>
        <li>٢ شركة مضيفة</li>
        <li>٤٥ شابًا</li>
      </ul>
      <p style="color:${GOLD};font-size:8pt;margin-top:10pt;">نموذج مُثبَت وقابل للتكرار</p>
    </div>
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:16pt;border-top:2pt solid #334455;">
      <p style="color:#8899AA;font-size:8pt;margin-bottom:6pt;">متوسط المدى · ٦–١٨ شهرًا</p>
      <p style="color:${WHITE};font-size:11pt;font-weight:bold;margin-bottom:8pt;">التوسّع</p>
      <ul style="color:#A0B0C0;font-size:9pt;line-height:1.7;padding-right:14pt;">
        <li>٤ جامعات</li>
        <li>١٠ شركات</li>
        <li>~٥٠٠ شاب</li>
      </ul>
      <p style="color:#8899AA;font-size:8pt;margin-top:10pt;">بيانات توظيف مقاسة</p>
    </div>
    <div style="flex:1;background:${DARK};border-radius:8pt;padding:16pt;border-top:2pt solid #334455;">
      <p style="color:#8899AA;font-size:8pt;margin-bottom:6pt;">طويل المدى · ١٨–٣٦ شهرًا</p>
      <p style="color:${WHITE};font-size:11pt;font-weight:bold;margin-bottom:8pt;">الوطني</p>
      <ul style="color:#A0B0C0;font-size:9pt;line-height:1.7;padding-right:14pt;">
        <li>١٥+ جامعة</li>
        <li>١٢+ محافظة</li>
        <li>٣٠٠٠+ سنويًا</li>
      </ul>
      <p style="color:#8899AA;font-size:8pt;margin-top:10pt;">برنامج وطني مدمج مع الوزارة</p>
    </div>
  </div>
  <!-- KPI strip -->
  <div style="background:${DARK};border-radius:6pt;padding:12pt 18pt;display:flex;flex-direction:row-reverse;gap:28pt;">
    <div style="text-align:center;">
      <p style="color:${GOLD};font-size:18pt;font-weight:900;">≥ 60%</p>
      <p style="color:#889;font-size:8pt;">جاهزية للتوظيف</p>
    </div>
    <div style="width:1pt;background:#334455;"></div>
    <div style="text-align:center;">
      <p style="color:${GOLD};font-size:18pt;font-weight:900;">≥ 40%</p>
      <p style="color:#889;font-size:8pt;">عروض عمل فعلية</p>
    </div>
    <div style="width:1pt;background:#334455;"></div>
    <div style="text-align:center;">
      <p style="color:${GOLD};font-size:18pt;font-weight:900;">≥ 90%</p>
      <p style="color:#889;font-size:8pt;">إتمام الشهادة</p>
    </div>
    <div style="width:1pt;background:#334455;"></div>
    <div style="text-align:center;">
      <p style="color:${GOLD};font-size:18pt;font-weight:900;">≥ 85%</p>
      <p style="color:#889;font-size:8pt;">رضا جهات التشغيل</p>
    </div>
    <div style="flex:1;text-align:left;">
      <p style="color:#556677;font-size:7pt;margin-top:8pt;">~٣.٦ مليون طالب في التعليم العالي · ٧٣ جامعة (المجلس الأعلى للجامعات)</p>
    </div>
  </div>
</div>`);

// ─── SLIDE 06 — P&L FORECAST (placeholder for chart) ────────────────────────
const s06 = wrap(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;padding:28pt 44pt 20pt;overflow:hidden;">
  <div style="border-right:4pt solid ${GOLD};padding-right:12pt;margin-bottom:18pt;">
    <p style="color:${GOLD};font-size:8pt;letter-spacing:2pt;font-weight:bold;">٠٦ · التوقعات المالية</p>
    <h2 style="color:${WHITE};font-size:24pt;font-weight:bold;">مسار الربحية — ١٠ سنوات</h2>
  </div>
  <!-- chart placeholder -->
  <div id="pl-chart" class="placeholder" style="flex:1;background:#0E1929;border-radius:8pt;"></div>
  <!-- footnote -->
  <p style="color:#445566;font-size:7pt;margin-top:10pt;text-align:right;">التوقعات قائمة على نموذج المرحلة التجريبية (٤٥ شابًا) مع معدل نمو سنوي ٤٠٪ حتى العام العاشر</p>
</div>`);

// ─── SLIDE 07 — THE ASK ─────────────────────────────────────────────────────
const s07 = wrap(`
<div style="width:720pt;height:405pt;display:flex;flex-direction:column;justify-content:center;padding:40pt 44pt;overflow:hidden;">
  <!-- top label -->
  <p style="color:${GOLD};font-size:9pt;letter-spacing:3pt;font-weight:bold;margin-bottom:20pt;">الطلب</p>
  <!-- Main ask box -->
  <div style="background:${DARK};border-radius:10pt;border-right:5pt solid ${GOLD};padding:28pt 32pt;margin-bottom:20pt;">
    <p style="color:${WHITE};font-size:16pt;font-weight:bold;line-height:1.7;margin-bottom:12pt;">رعاية الوزارة وتمويلها للمرحلة التجريبية</p>
    <p style="color:#A0B0C0;font-size:12pt;line-height:1.6;">والوصول إلى جامعة شريكة بثلاث كليات، عبر وحدات التضامن الاجتماعي بالجامعات</p>
  </div>
  <!-- Ministry alignment bullets -->
  <div style="display:flex;flex-direction:row-reverse;gap:12pt;">
    <div style="flex:1;display:flex;flex-direction:row-reverse;align-items:center;gap:8pt;">
      <div style="width:8pt;height:8pt;background:${GOLD};border-radius:50%;flex-shrink:0;"></div>
      <p style="color:#A0B0C0;font-size:9pt;">متوافق مع رؤية مصر ٢٠٣٠ والتمكين الاقتصادي</p>
    </div>
    <div style="flex:1;display:flex;flex-direction:row-reverse;align-items:center;gap:8pt;">
      <div style="width:8pt;height:8pt;background:${GOLD};border-radius:50%;flex-shrink:0;"></div>
      <p style="color:#A0B0C0;font-size:9pt;">امتداد طبيعي لبرنامج «فرصة» وقمة START 2026</p>
    </div>
    <div style="flex:1;display:flex;flex-direction:row-reverse;align-items:center;gap:8pt;">
      <div style="width:8pt;height:8pt;background:${GOLD};border-radius:50%;flex-shrink:0;"></div>
      <p style="color:#A0B0C0;font-size:9pt;">يبني على منظومة قائمة ولا يبدأ من الصفر</p>
    </div>
  </div>
  <!-- footer -->
  <div style="margin-top:20pt;padding-top:16pt;border-top:1pt solid #1E3050;display:flex;flex-direction:row-reverse;justify-content:space-between;align-items:center;">
    <p style="color:#8899AA;font-size:8pt;">MBK EDUCATION · جاهزون</p>
    <p style="color:#556677;font-size:8pt;">gadalla111@gmail.com</p>
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

  const htmlDir = WS;

  // Slides 1–5 (no charts)
  for (let i = 1; i <= 5; i++) {
    const f = path.join(htmlDir, `s${String(i).padStart(2,'0')}.html`);
    await html2pptx(f, pptx);
    console.log(`  ✓ Slide ${i}`);
  }

  // Slide 6 — P&L chart
  const { slide: s6, placeholders: p6 } = await html2pptx(path.join(htmlDir, 's06.html'), pptx);
  console.log('  ✓ Slide 6 (placeholder found:', p6.length, ')');

  if (p6.length > 0) {
    // 10-year P&L: Revenue, Costs, Net Profit
    const years = ['Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8','Y9','Y10'];
    const revenue = [120, 170, 238, 333, 467, 654, 916, 1282, 1794, 2512];
    const costs   = [200, 230, 264, 290, 320, 360, 410, 470, 540, 620];
    const profit  = revenue.map((r, i) => r - costs[i]);

    s6.addChart(pptx.charts.LINE, [
      { name: 'الإيرادات (ألف جنيه)', labels: years, values: revenue },
      { name: 'التكاليف (ألف جنيه)',  labels: years, values: costs },
      { name: 'صافي الربح (ألف جنيه)', labels: years, values: profit }
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
      valAxisMinVal: -300,
      valAxisMaxVal: 2600,
      valAxisMajorUnit: 500,
      chartColors: ['C8A24C', 'FFFFFF', '2ECC71'],
      plotAreaBorderColor: '1C2B45',
      plotAreaFill: { color: '0E1929' }
    });
  }

  // Slide 7 — ASK (no charts)
  await html2pptx(path.join(htmlDir, 's07.html'), pptx);
  console.log('  ✓ Slide 7');

  const outPath = '/home/user/Mahmoud-Gadalla/outputs/Jahizoon_Minister_Presentation_v6.pptx';
  await pptx.writeFile({ fileName: outPath });
  console.log('\n✓ Saved:', outPath);
})().catch(e => { console.error(e); process.exit(1); });

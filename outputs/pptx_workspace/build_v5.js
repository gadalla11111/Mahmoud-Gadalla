/**
 * JAHIZOON — Minister Deck v5
 * 6 slides · inline SVG charts · zero CDN · every slide checked
 */
const { chromium } = require('playwright');
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const OUT = path.join(__dirname, 'slides_v5');
fs.mkdirSync(OUT, { recursive: true });

const GD = '#C8A24C', RD = '#A4232A', WH = '#FFFFFF';

const HEAD = `<!DOCTYPE html><html dir="rtl"><head><meta charset="UTF-8">
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{width:960px;height:540px;overflow:hidden;background:#0C0C0C;font-family:'Segoe UI',Tahoma,Arial,sans-serif;position:relative;}
</style></head><body>`;

// helper: gold top bar + red bottom bar
const BARS = `<div style="position:absolute;top:0;left:0;width:960px;height:4px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>`;

const LABEL = (txt, extra='') =>
  `<p style="position:absolute;top:20px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;${extra}">${txt}</p>`;

const H1 = (txt, top=44) =>
  `<h1 style="position:absolute;top:${top}px;right:32px;left:32px;color:${WH};font-size:26px;font-weight:800;direction:rtl;text-align:right;">${txt}</h1>`;

// ─── SLIDE 01: WHO WE ARE ────────────────────────────────────────────────────
const s01 = HEAD + `
<!-- Left brand panel -->
<div style="position:absolute;top:0;left:0;width:520px;height:540px;background:#080808;border-right:5px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:56px 52px;">
  <p style="color:${GD};font-size:10px;letter-spacing:6px;direction:ltr;margin-bottom:20px;">THE REPUBLIC EDUCATION</p>
  <h1 style="color:${GD};font-size:80px;font-weight:900;line-height:1;direction:ltr;">JAHIZOON</h1>
  <h2 style="color:${WH};font-size:42px;font-weight:700;margin-top:10px;direction:rtl;">جاهزون</h2>
  <div style="width:64px;height:3px;background:${GD};margin:24px 0;"></div>
  <p style="color:#777;font-size:14px;line-height:1.8;direction:rtl;">برنامج التأهيل الوظيفي الوطني</p>
</div>
<!-- Right vision panel -->
<div style="position:absolute;top:0;left:525px;right:0;height:540px;background:#0C0C0C;display:flex;flex-direction:column;justify-content:space-between;padding:40px 40px 32px;">
  <p style="color:#333;font-size:10px;letter-spacing:4px;direction:ltr;">VISION · 2045</p>
  <!-- Vision sentence -->
  <div>
    <p style="color:#444;font-size:11px;letter-spacing:3px;direction:ltr;margin-bottom:20px;">OUR MISSION</p>
    <p style="color:${WH};font-size:20px;font-weight:700;direction:rtl;line-height:1.65;">بناء الكوادر البشرية التي ستجعل مصر الحضارة الرائدة في العالم بحلول 2045</p>
    <div style="width:40px;height:2px;background:${RD};margin:20px 0;"></div>
    <p style="color:#555;font-size:13px;direction:rtl;line-height:1.7;">جواز السفر الأقوى · العملة الاحتياطية العالمية · القوة الناعمة الأولى</p>
  </div>
  <!-- Three pillars mini -->
  <div style="display:flex;gap:8px;direction:ltr;">
    <div style="flex:1;background:#111;border-top:3px solid ${GD};padding:12px;text-align:right;direction:rtl;">
      <p style="color:${GD};font-size:11px;font-weight:700;">تدريب</p>
      <p style="color:#444;font-size:11px;margin-top:2px;">12 أسبوعاً</p>
    </div>
    <div style="flex:1;background:#111;border-top:3px solid ${RD};padding:12px;text-align:right;direction:rtl;">
      <p style="color:${RD};font-size:11px;font-weight:700;">تقييم</p>
      <p style="color:#444;font-size:11px;margin-top:2px;">امتحان مصوّر</p>
    </div>
    <div style="flex:1;background:#111;border-top:3px solid ${GD};padding:12px;text-align:right;direction:rtl;">
      <p style="color:${GD};font-size:11px;font-weight:700;">توظيف</p>
      <p style="color:#444;font-size:11px;margin-top:2px;">مضمون</p>
    </div>
  </div>
  <p style="color:#222;font-size:11px;direction:ltr;">June 2026 · Presented to Ministry of Social Solidarity</p>
</div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
</body></html>`;

// ─── SLIDE 02: THE PROBLEM ───────────────────────────────────────────────────
// Bar chart via inline SVG (no CDN)
// 4 bars: مؤهل متوسط 18%, دبلوم 29%, بكالوريوس 41.5%, إجمالي 6%
// SVG: 600×320px, bars drawn manually
function barSVG() {
  const labels = ['إجمالي سوق العمل','مؤهل متوسط','دبلوم فني','بكالوريوس فأعلى'];
  const vals   = [6, 18, 29, 41.5];
  const colors = [GD, '#555', '#777', RD];
  const W = 580, H = 280, padL = 20, padB = 36, padT = 10;
  const barH = 44, gap = 14;
  const maxV = 50;
  let svg = `<svg width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg">`;
  // grid lines
  for (let v of [0,10,20,30,40,50]) {
    const x = padL + (v/maxV)*(W - padL - 10);
    svg += `<line x1="${x}" y1="${padT}" x2="${x}" y2="${H-padB}" stroke="#1A1A1A" stroke-width="1"/>`;
    svg += `<text x="${x}" y="${H-padB+14}" fill="#444" font-size="10" text-anchor="middle" font-family="Arial">${v}%</text>`;
  }
  vals.forEach((v, i) => {
    const y = padT + i*(barH+gap);
    const bW = (v/maxV)*(W - padL - 10);
    svg += `<rect x="${padL}" y="${y}" width="${bW}" height="${barH}" fill="${colors[i]}" rx="2"/>`;
    svg += `<text x="${padL+bW+8}" y="${y+barH/2+5}" fill="${WH}" font-size="15" font-weight="bold" font-family="Arial">${v}%</text>`;
    // label (RTL text via textLength trick - use dir attribute on foreignObject is complex, just use english positions)
    svg += `<text x="${padL}" y="${y-6}" fill="#888" font-size="12" font-family="Arial,Segoe UI">${labels[i]}</text>`;
  });
  svg += `</svg>`;
  return svg;
}

const s02 = HEAD + BARS + LABEL('THE PROBLEM') +
`<h1 style="position:absolute;top:28px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;text-align:right;">500,000 خريج · 41.5% عاطل · النظام مكسور</h1>
<!-- 3 KPI blocks top -->
<div style="position:absolute;top:72px;left:0;right:0;height:140px;display:flex;gap:0;">
  <div style="flex:1;background:#1A0000;border-top:5px solid ${RD};display:flex;flex-direction:column;justify-content:center;padding:20px 28px;">
    <p style="color:#553333;font-size:10px;letter-spacing:3px;direction:ltr;">GRAD UNEMPLOYMENT</p>
    <p style="color:${RD};font-size:72px;font-weight:900;line-height:1;direction:ltr;">41.5%</p>
    <p style="color:#664444;font-size:12px;margin-top:4px;direction:rtl;">بطالة خريجي الجامعات · CAPMAS 2026</p>
  </div>
  <div style="flex:1;background:#111;border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:20px 28px;">
    <p style="color:#555;font-size:10px;letter-spacing:3px;direction:ltr;">NEW GRADUATES / YEAR</p>
    <p style="color:${GD};font-size:72px;font-weight:900;line-height:1;direction:ltr;">500K</p>
    <p style="color:#555;font-size:12px;margin-top:4px;direction:rtl;">خريج جديد سنوياً · وزارة التعليم العالي 2025</p>
  </div>
  <div style="flex:1;background:#111;border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:20px 28px;">
    <p style="color:#555;font-size:10px;letter-spacing:3px;direction:ltr;">VS. MARKET AVERAGE</p>
    <p style="color:${GD};font-size:72px;font-weight:900;line-height:1;direction:ltr;">×6.9</p>
    <p style="color:#555;font-size:12px;margin-top:4px;direction:rtl;">أعلى من البطالة العامة (6%) · الفجوة تتسع</p>
  </div>
</div>
<!-- Bar chart bottom -->
<div style="position:absolute;top:220px;left:32px;bottom:16px;right:32px;background:#0A0A0A;padding:16px 20px;">
  <p style="color:#333;font-size:10px;letter-spacing:3px;direction:ltr;margin-bottom:8px;">UNEMPLOYMENT BY EDUCATION LEVEL · CAPMAS Q1 2026</p>
  ${barSVG()}
</div>
</body></html>`;

// ─── SLIDE 03: OUR SOLUTION ──────────────────────────────────────────────────
const s03 = HEAD + BARS + LABEL('OUR SOLUTION') +
`<h1 style="position:absolute;top:28px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;text-align:right;">جاهزون · من الفجوة إلى التوظيف في 12 أسبوعاً</h1>
<!-- 3 full-height pillars -->
<div style="position:absolute;top:72px;left:0;right:0;bottom:8px;display:flex;gap:0;">

  <!-- TRAIN -->
  <div style="flex:1;background:#0A0A0A;border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;border-right:2px solid #141414;">
    <div>
      <p style="color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;margin-bottom:16px;">01 · TRAIN</p>
      <p style="color:${WH};font-size:30px;font-weight:800;direction:rtl;">تدريب</p>
      <div style="width:36px;height:2px;background:${GD};margin:16px 0;"></div>
      <p style="color:#555;font-size:14px;direction:rtl;line-height:1.9;">12 أسبوعاً مكثفاً<br>مهارات ناعمة + تقنية<br>مدربون معتمدون<br>مشاريع حقيقية</p>
    </div>
    <p style="color:#C8A24C33;font-size:80px;font-weight:900;direction:ltr;line-height:1;">12W</p>
  </div>

  <!-- ASSESS -->
  <div style="flex:1;background:#100000;border-top:5px solid ${RD};display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;border-right:2px solid #1A0000;">
    <div>
      <p style="color:${RD};font-size:10px;letter-spacing:5px;direction:ltr;margin-bottom:16px;">02 · ASSESS</p>
      <p style="color:${WH};font-size:30px;font-weight:800;direction:rtl;">تقييم مصوّر</p>
      <div style="width:36px;height:2px;background:${RD};margin:16px 0;"></div>
      <p style="color:#553333;font-size:14px;direction:rtl;line-height:1.9;">امتحان أداء مسجّل بالفيديو<br>توثيق رقمي معتمد<br>يُرسَل لأصحاب العمل مباشرةً<br>لا تزوير · لا تخمين</p>
    </div>
    <div style="display:flex;align-items:center;gap:10px;">
      <div style="width:14px;height:14px;border-radius:50%;background:${RD};"></div>
      <p style="color:#A4232A55;font-size:28px;font-weight:900;direction:ltr;">● REC</p>
    </div>
  </div>

  <!-- PLACE -->
  <div style="flex:1;background:#0A0A0A;border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;">
    <div>
      <p style="color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;margin-bottom:16px;">03 · PLACE</p>
      <p style="color:${WH};font-size:30px;font-weight:800;direction:rtl;">توظيف</p>
      <div style="width:36px;height:2px;background:${GD};margin:16px 0;"></div>
      <p style="color:#555;font-size:14px;direction:rtl;line-height:1.9;">شبكة 40+ شريك مؤسسي<br>ربط مباشر بعروض العمل<br>75% توظيف خلال 90 يوماً<br>6 أشهر دعم ما بعد التعيين</p>
    </div>
    <p style="color:#C8A24C33;font-size:52px;font-weight:900;direction:rtl;line-height:1;">75%</p>
  </div>

</div>
</body></html>`;

// ─── SLIDE 04: OUR PROCESS (5 steps) ────────────────────────────────────────
const steps = [
  { n:'01', color: GD,   bg:'#0A0A0A', title:'تشخيص',         body:'تحديد الفجوات الفردية عبر أداة رقمية · نتيجة فورية' },
  { n:'02', color: GD,   bg:'#0A0A0A', title:'تدريب مكثف',    body:'12 أسبوعاً · مناهج مُصمَّمة بالتعاون مع أصحاب العمل' },
  { n:'03', color: RD,   bg:'#100000', title:'امتحان مصوّر',   body:'أداء حقيقي · مسجّل · موثّق رقمياً لا يمكن تزويره' },
  { n:'04', color: GD,   bg:'#0A0A0A', title:'ربط وظيفي',      body:'منصة رقمية + شركاء مؤسسيون + عروض عمل حقيقية' },
  { n:'05', color:'#3A7A3A', bg:'#0A100A', title:'متابعة',     body:'6 أشهر بعد التعيين · ضمان استمرار النجاح' },
];

const s04 = HEAD + BARS + LABEL('OUR PROCESS') +
`<h1 style="position:absolute;top:28px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;text-align:right;">منهجية جاهزون · 5 خطوات من الفجوة إلى التوظيف</h1>
<div style="position:absolute;top:72px;left:0;right:0;bottom:8px;display:flex;gap:0;">
${steps.map((s,i) => `
  <div style="flex:1;background:${s.bg};border-top:5px solid ${s.color};display:flex;flex-direction:column;justify-content:space-between;padding:28px 18px;${i<4?'border-right:2px solid #141414;':''}">
    <div>
      <p style="color:${s.color};font-size:10px;letter-spacing:4px;direction:ltr;margin-bottom:12px;">STEP ${s.n}</p>
      <p style="color:${WH};font-size:18px;font-weight:700;direction:rtl;">${s.title}</p>
      <div style="width:28px;height:2px;background:${s.color};margin:12px 0;"></div>
      <p style="color:#555;font-size:12px;direction:rtl;line-height:1.8;">${s.body}</p>
    </div>
    <p style="color:${s.color}22;font-size:52px;font-weight:900;direction:ltr;line-height:1;">${s.n}</p>
  </div>`).join('')}
</div>
<p style="position:absolute;bottom:14px;left:0;right:0;text-align:center;color:#333;font-size:11px;direction:rtl;">هدف: 75% من المتدربين يحصلون على وظيفة خلال 90 يوماً من انتهاء البرنامج</p>
</body></html>`;

// ─── SLIDE 05: EXPECTED IMPACT ───────────────────────────────────────────────
const s05 = HEAD + BARS + LABEL('EXPECTED IMPACT') +
`<h1 style="position:absolute;top:28px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;text-align:right;">الأثر المتوقع · قصير · متوسط · طويل المدى</h1>
<div style="position:absolute;top:72px;left:0;right:0;bottom:8px;display:flex;gap:0;">

  <!-- Short term -->
  <div style="flex:1;background:#0A0A1A;border-top:5px solid #4466AA;display:flex;flex-direction:column;justify-content:space-between;padding:32px 24px;border-right:2px solid #111;">
    <div>
      <p style="color:#4466AA;font-size:10px;letter-spacing:4px;direction:ltr;margin-bottom:8px;">SHORT TERM · 2025–2026</p>
      <p style="color:${WH};font-size:20px;font-weight:700;direction:rtl;">التأسيس</p>
      <div style="width:28px;height:2px;background:#4466AA;margin:14px 0;"></div>
      <div style="display:flex;flex-direction:column;gap:10px;direction:rtl;">
        <div><p style="color:#4466AA;font-size:32px;font-weight:900;direction:ltr;">300</p><p style="color:#555;font-size:12px;">متدرب · القاهرة</p></div>
        <div><p style="color:#4466AA;font-size:32px;font-weight:900;direction:ltr;">225</p><p style="color:#555;font-size:12px;">موظف (75%)</p></div>
        <div><p style="color:#4466AA;font-size:32px;font-weight:900;direction:ltr;">5+</p><p style="color:#555;font-size:12px;">شركاء مؤسسيين</p></div>
      </div>
    </div>
    <p style="color:#22335566;font-size:11px;direction:rtl;">إثبات النموذج · جمع البيانات</p>
  </div>

  <!-- Medium term -->
  <div style="flex:1;background:#111;border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:space-between;padding:32px 24px;border-right:2px solid #1A1A1A;">
    <div>
      <p style="color:${GD};font-size:10px;letter-spacing:4px;direction:ltr;margin-bottom:8px;">MEDIUM TERM · 2027–2029</p>
      <p style="color:${WH};font-size:20px;font-weight:700;direction:rtl;">التوسع</p>
      <div style="width:28px;height:2px;background:${GD};margin:14px 0;"></div>
      <div style="display:flex;flex-direction:column;gap:10px;direction:rtl;">
        <div><p style="color:${GD};font-size:32px;font-weight:900;direction:ltr;">5,000</p><p style="color:#555;font-size:12px;">متدرب / سنة · 4 مدن</p></div>
        <div><p style="color:${GD};font-size:32px;font-weight:900;direction:ltr;">20+</p><p style="color:#555;font-size:12px;">شريك مؤسسي</p></div>
        <div><p style="color:${GD};font-size:32px;font-weight:900;direction:ltr;">2027</p><p style="color:#555;font-size:12px;">نقطة التعادل المالي</p></div>
      </div>
    </div>
    <p style="color:#C8A24C33;font-size:11px;direction:rtl;">رؤية مصر 2030 · محور التوظيف والكفاءة</p>
  </div>

  <!-- Long term -->
  <div style="flex:1;background:#0A100A;border-top:5px solid #3A8A3A;display:flex;flex-direction:column;justify-content:space-between;padding:32px 24px;">
    <div>
      <p style="color:#3A8A3A;font-size:10px;letter-spacing:4px;direction:ltr;margin-bottom:8px;">LONG TERM · 2030–2035</p>
      <p style="color:${WH};font-size:20px;font-weight:700;direction:rtl;">الانتشار الوطني</p>
      <div style="width:28px;height:2px;background:#3A8A3A;margin:14px 0;"></div>
      <div style="display:flex;flex-direction:column;gap:10px;direction:rtl;">
        <div><p style="color:#3A8A3A;font-size:32px;font-weight:900;direction:ltr;">30,000</p><p style="color:#555;font-size:12px;">خريج موظف بحلول 2035</p></div>
        <div><p style="color:#3A8A3A;font-size:32px;font-weight:900;direction:ltr;">↓5%</p><p style="color:#555;font-size:12px;">هدف بطالة رؤية 2030</p></div>
        <div><p style="color:#3A8A3A;font-size:32px;font-weight:900;direction:ltr;">#1</p><p style="color:#555;font-size:12px;">نموذج وطني قابل للتصدير</p></div>
      </div>
    </div>
    <p style="color:#1A441A;font-size:11px;direction:rtl;">رؤية مصر 2030 · خفض البطالة + رأس المال البشري</p>
  </div>

</div>
</body></html>`;

// ─── SLIDE 06: P&L FORECAST (inline SVG) ─────────────────────────────────────
function plSVG() {
  const W = 700, H = 260;
  const years = [2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035];
  const rev   = [2.5,5.5,11,19,29,42,57,74,92,110,132];
  const ebit  = [-1.2,-0.8,0.5,3.2,7.8,14,22,33,44,56,68.6];
  const n = years.length;
  const padL=40, padR=10, padT=10, padB=40;
  const cW = W-padL-padR, cH = H-padT-padB;
  const minY=-10, maxY=145;

  function px(i){ return padL + (i/(n-1))*cW; }
  function py(v){ return padT + cH - ((v-minY)/(maxY-minY))*cH; }

  // build polyline points
  const revPts = rev.map((v,i)=>`${px(i)},${py(v)}`).join(' ');
  const ebitPts = ebit.map((v,i)=>`${px(i)},${py(v)}`).join(' ');

  // filled area for revenue
  const revArea = `${padL},${py(0)} ` + rev.map((v,i)=>`${px(i)},${py(v)}`).join(' ') + ` ${padL+cW},${py(0)}`;

  // zero line y
  const zeroY = py(0);

  let svg = `<svg width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg">`;

  // grid
  for(let v of [-10,0,20,40,60,80,100,120,140]){
    const y = py(v);
    if(y<padT||y>padT+cH) continue;
    svg += `<line x1="${padL}" y1="${y}" x2="${W-padR}" y2="${y}" stroke="${v===0?'#333':'#1A1A1A'}" stroke-width="${v===0?1.5:1}"/>`;
    svg += `<text x="${padL-6}" y="${y+4}" fill="#444" font-size="10" text-anchor="end" font-family="Arial">${v}M</text>`;
  }
  // year labels
  years.forEach((yr,i)=>{
    if(i%2===0||i===n-1)
      svg += `<text x="${px(i)}" y="${H-8}" fill="#555" font-size="10" text-anchor="middle" font-family="Arial">${yr}</text>`;
  });

  // revenue fill
  svg += `<polygon points="${revArea}" fill="${GD}18"/>`;
  // revenue line
  svg += `<polyline points="${revPts}" fill="none" stroke="${GD}" stroke-width="2.5"/>`;
  // ebitda fill below zero (red)
  const ebitAreaBelow = ebit.map((v,i)=>`${px(i)},${py(Math.min(v,0))}`).reverse().map((p,i,a)=>p).join(' ');
  // ebitda line
  svg += `<polyline points="${ebitPts}" fill="none" stroke="${RD}" stroke-width="2" stroke-dasharray="6,3"/>`;

  // break-even marker (2027 = index 2)
  const bx = px(2), by2 = py(0.5);
  svg += `<line x1="${bx}" y1="${padT}" x2="${bx}" y2="${padT+cH}" stroke="#333" stroke-width="1" stroke-dasharray="4,3"/>`;
  svg += `<text x="${bx+4}" y="${padT+14}" fill="#555" font-size="10" font-family="Arial">break-even</text>`;

  // dots at key points
  rev.forEach((v,i)=>{
    svg += `<circle cx="${px(i)}" cy="${py(v)}" r="3" fill="${GD}"/>`;
  });
  ebit.forEach((v,i)=>{
    svg += `<circle cx="${px(i)}" cy="${py(v)}" r="2.5" fill="${RD}"/>`;
  });

  // legend
  svg += `<line x1="${W-160}" y1="14" x2="${W-130}" y2="14" stroke="${GD}" stroke-width="2.5"/>
    <text x="${W-125}" y="18" fill="${GD}" font-size="11" font-family="Arial">الإيراد</text>
    <line x1="${W-160}" y1="30" x2="${W-130}" y2="30" stroke="${RD}" stroke-width="2" stroke-dasharray="6,3"/>
    <text x="${W-125}" y="34" fill="${RD}" font-size="11" font-family="Arial">EBITDA</text>`;

  svg += `</svg>`;
  return svg;
}

const s06 = HEAD + BARS + LABEL('P&L FORECAST · 10 YEARS') +
`<h1 style="position:absolute;top:28px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;text-align:right;">توقعات الأداء المالي 2025–2035 · مليون جنيه مصري</h1>
<!-- KPI strip -->
<div style="position:absolute;top:72px;left:0;right:0;height:68px;display:flex;gap:0;">
  <div style="flex:1;background:#1A0000;border-top:3px solid ${RD};display:flex;flex-direction:column;justify-content:center;padding:0 24px;border-right:1px solid #2A0000;">
    <p style="color:#553333;font-size:9px;letter-spacing:2px;direction:ltr;">REVENUE · 2035</p>
    <p style="color:${RD};font-size:28px;font-weight:900;direction:ltr;">132M <span style="font-size:16px;font-weight:400;">EGP</span></p>
  </div>
  <div style="flex:1;background:#111;border-top:3px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:0 24px;border-right:1px solid #1A1A1A;">
    <p style="color:#444;font-size:9px;letter-spacing:2px;direction:ltr;">EBITDA · 2035</p>
    <p style="color:${GD};font-size:28px;font-weight:900;direction:ltr;">68.6M <span style="font-size:16px;font-weight:400;">EGP</span></p>
  </div>
  <div style="flex:1;background:#111;border-top:3px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:0 24px;border-right:1px solid #1A1A1A;">
    <p style="color:#444;font-size:9px;letter-spacing:2px;direction:ltr;">TRAINEES · 2035</p>
    <p style="color:${GD};font-size:28px;font-weight:900;direction:ltr;">30,000</p>
  </div>
  <div style="flex:1;background:#0A0A14;border-top:3px solid #4466AA;display:flex;flex-direction:column;justify-content:center;padding:0 24px;">
    <p style="color:#334466;font-size:9px;letter-spacing:2px;direction:ltr;">BREAK-EVEN</p>
    <p style="color:#4466AA;font-size:28px;font-weight:900;direction:ltr;">2027</p>
  </div>
</div>
<!-- SVG Chart -->
<div style="position:absolute;top:148px;left:20px;right:240px;bottom:12px;background:#0A0A0A;">
  ${plSVG()}
</div>
<!-- Right data table -->
<div style="position:absolute;top:148px;right:0;width:228px;bottom:12px;background:#0A0A0A;border-left:2px solid #141414;padding:16px 16px;overflow:hidden;">
  <p style="color:#333;font-size:9px;letter-spacing:2px;direction:ltr;margin-bottom:10px;">KEY MILESTONES</p>
  <table style="width:100%;border-collapse:collapse;direction:ltr;">
    <tr><td style="color:#444;font-size:11px;padding:5px 0;border-bottom:1px solid #141414;">Year</td><td style="color:#444;font-size:11px;padding:5px 0;border-bottom:1px solid #141414;text-align:right;">Rev</td><td style="color:#444;font-size:11px;padding:5px 0;border-bottom:1px solid #141414;text-align:right;">EBITDA</td></tr>
    ${[[2025,'2.5M','-1.2M'],[2026,'5.5M','-0.8M'],[2027,'11M','0.5M'],[2028,'19M','3.2M'],[2030,'42M','14M'],[2035,'132M','68.6M']].map(([y,r,e])=>`
    <tr><td style="color:#555;font-size:11px;padding:5px 0;border-bottom:1px solid #0F0F0F;">${y}</td><td style="color:${GD};font-size:11px;padding:5px 0;border-bottom:1px solid #0F0F0F;text-align:right;">${r}</td><td style="color:${RD};font-size:11px;padding:5px 0;border-bottom:1px solid #0F0F0F;text-align:right;">${e}</td></tr>`).join('')}
  </table>
</div>
</body></html>`;

// ─── MAIN ────────────────────────────────────────────────────────────────────
(async () => {
  const slides = { '01':s01,'02':s02,'03':s03,'04':s04,'05':s05,'06':s06 };
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });

  for(const [num, html] of Object.entries(slides)){
    const page = await browser.newPage();
    await page.setViewportSize({ width:960, height:540 });
    await page.setContent(html, { waitUntil:'domcontentloaded' });
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.join(OUT,`${num}.png`), clip:{x:0,y:0,width:960,height:540} });
    await page.close();
    console.log(`  ✓ Slide ${num}`);
  }
  await browser.close();

  // assemble
  execSync(`python3 -c "
from pptx import Presentation
from pptx.util import Emu
import os
OUT='${OUT}'
prs=Presentation()
prs.slide_width=Emu(9144000)
prs.slide_height=Emu(5143500)
blank=prs.slide_layouts[6]
for i in range(1,7):
    num=str(i).zfill(2)
    s=prs.slides.add_slide(blank)
    s.shapes.add_picture(os.path.join(OUT,num+'.png'),0,0,width=prs.slide_width,height=prs.slide_height)
    print(f'  Added slide {num}')
prs.save('/home/user/Mahmoud-Gadalla/outputs/Jahizoon_Minister_Presentation.pptx')
print('PPTX saved.')
"`, { stdio:'inherit' });
})();

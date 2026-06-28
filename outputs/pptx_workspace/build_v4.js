/**
 * JAHIZOON — Minister Presentation v4
 * Renders all 18 slides via playwright, assembles PPTX via python-pptx
 * Every slide: full 960×540 canvas coverage, Chart.js inline, correct Arabic RTL
 */
const { chromium } = require('playwright');
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const OUT_DIR = path.join(__dirname, 'slides_v4');
fs.mkdirSync(OUT_DIR, { recursive: true });

const BK = '#0E0E0E', GD = '#C8A24C', RD = '#A4232A', WH = '#FFFFFF';
const DRD = '#1A0000', DGD = '#1A1400', DK = '#111111', MK = '#1A1A1A';

const BASE = `<!DOCTYPE html><html dir="rtl"><head><meta charset="UTF-8">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{width:960px;height:540px;position:relative;overflow:hidden;background:${BK};font-family:'Segoe UI',Tahoma,Arial,sans-serif;}
.fill{position:absolute;top:0;left:0;width:960px;height:540px;}
</style></head><body>`;

const slides = {};

// ─── SLIDE 01: COVER ───────────────────────────────────────────────────────
slides['01'] = BASE + `
<div style="display:flex;width:960px;height:540px;flex-direction:row-reverse;">
  <!-- Brand panel (visually left due to row-reverse) -->
  <div style="width:560px;height:540px;background:#0A0A0A;display:flex;flex-direction:column;justify-content:center;padding:56px 52px;border-left:6px solid ${GD};">
    <p style="color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;margin-bottom:28px;">NATIONAL EMPLOYMENT READINESS PROGRAMME</p>
    <h1 style="color:${GD};font-size:100px;font-weight:900;letter-spacing:2px;line-height:1;direction:ltr;">JAHIZOON</h1>
    <h2 style="color:${WH};font-size:48px;font-weight:700;margin-top:12px;direction:rtl;">جاهزون</h2>
    <div style="width:72px;height:3px;background:${GD};margin:24px 0;"></div>
    <p style="color:#777;font-size:15px;line-height:1.7;direction:rtl;">برنامج وطني يُحوّل الخريجين إلى كفاءات موثّقة جاهزة للتوظيف الفوري</p>
  </div>
  <!-- Ministry panel (visually right) -->
  <div style="flex:1;height:540px;background:${BK};display:flex;flex-direction:column;justify-content:space-between;padding:48px 44px;">
    <p style="color:#333;font-size:10px;letter-spacing:4px;direction:ltr;">YM4 EDUCATION</p>
    <div>
      <p style="color:#444;font-size:11px;letter-spacing:3px;direction:ltr;margin-bottom:20px;">PRESENTED TO</p>
      <p style="color:${WH};font-size:26px;font-weight:700;direction:rtl;line-height:1.5;">وزارة التضامن الاجتماعي</p>
      <p style="color:${WH};font-size:20px;direction:rtl;margin-top:8px;">جمهورية مصر العربية</p>
      <div style="width:48px;height:3px;background:${RD};margin:24px 0;"></div>
    </div>
    <p style="color:#333;font-size:13px;direction:ltr;">June 2026</p>
  </div>
</div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
</body></html>`;

// ─── SLIDE 02: THE CRISIS ──────────────────────────────────────────────────
slides['02'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:4px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">THE CRISIS</p>
<h1 style="position:absolute;top:38px;right:32px;left:32px;color:${WH};font-size:28px;font-weight:800;direction:rtl;text-align:right;">مصر لديها فائض من الشباب · وعجز في التوظيف</h1>
<!-- 3 full-height panels -->
<div style="position:absolute;top:86px;left:0;right:0;bottom:12px;display:flex;gap:0;">
  <div style="flex:1;background:${MK};display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;border-top:5px solid ${GD};">
    <div>
      <p style="color:${GD};font-size:13px;letter-spacing:2px;direction:ltr;">YOUTH WORKFORCE</p>
      <p style="color:${GD};font-size:88px;font-weight:900;line-height:1;direction:ltr;margin-top:16px;">30M</p>
    </div>
    <div>
      <p style="color:${WH};font-size:18px;font-weight:700;direction:rtl;">شاب مصري في سوق العمل</p>
      <p style="color:#555;font-size:12px;margin-top:8px;direction:ltr;">CAPMAS 2025</p>
    </div>
  </div>
  <div style="flex:1;background:${DRD};display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;border-top:5px solid ${RD};">
    <div>
      <p style="color:${RD};font-size:13px;letter-spacing:2px;direction:ltr;">GRAD UNEMPLOYMENT</p>
      <p style="color:${RD};font-size:88px;font-weight:900;line-height:1;direction:ltr;margin-top:16px;">41.5%</p>
    </div>
    <div>
      <p style="color:${WH};font-size:18px;font-weight:700;direction:rtl;">بطالة خريجي الجامعات</p>
      <p style="color:#553333;font-size:12px;margin-top:8px;direction:ltr;">CAPMAS Q1 2026</p>
    </div>
  </div>
  <div style="flex:1;background:${MK};display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;border-top:5px solid ${GD};">
    <div>
      <p style="color:${GD};font-size:13px;letter-spacing:2px;direction:ltr;">NEW GRADS / YEAR</p>
      <p style="color:${GD};font-size:88px;font-weight:900;line-height:1;direction:ltr;margin-top:16px;">500K</p>
    </div>
    <div>
      <p style="color:${WH};font-size:18px;font-weight:700;direction:rtl;">خريج جديد كل عام</p>
      <p style="color:#555;font-size:12px;margin-top:8px;direction:ltr;">وزارة التعليم العالي 2025</p>
    </div>
  </div>
</div>
</body></html>`;

// ─── SLIDE 03: RESEARCH CONSENSUS ─────────────────────────────────────────
slides['03'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:4px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">RESEARCH CONSENSUS</p>
<div style="position:absolute;top:0;left:0;width:420px;height:540px;background:#0A0A0A;border-right:4px solid #1A1A1A;display:flex;flex-direction:column;justify-content:center;padding:48px 44px;">
  <p style="color:${GD};font-size:160px;font-weight:900;line-height:1;direction:ltr;">13</p>
  <p style="color:${WH};font-size:20px;direction:ltr;margin-top:4px;">of 13 studies</p>
  <div style="width:56px;height:3px;background:${GD};margin:20px 0;"></div>
  <p style="color:#666;font-size:15px;direction:rtl;line-height:1.6;">دراسة · نتيجة واحدة</p>
  <p style="color:#333;font-size:12px;margin-top:24px;direction:ltr;">Consensus.app · 2024–2026</p>
</div>
<div style="position:absolute;top:0;left:424px;right:0;height:540px;display:flex;flex-direction:column;">
  <div style="flex:1;padding:28px 32px;border-bottom:2px solid #1A1A1A;display:flex;flex-direction:column;justify-content:center;">
    <p style="color:${WH};font-size:17px;font-weight:700;direction:rtl;line-height:1.6;margin-bottom:12px;">"الخريجون يفتقرون إلى المهارات الوظيفية الأساسية التي يحتاجها سوق العمل"</p>
  </div>
  <div style="flex:1;padding:24px 32px;border-bottom:2px solid #1A1A1A;border-right:4px solid ${GD};display:flex;flex-direction:column;justify-content:center;">
    <p style="color:${GD};font-size:14px;font-weight:700;direction:rtl;">المهارات الناعمة</p>
    <p style="color:#666;font-size:13px;margin-top:6px;direction:rtl;">التواصل · العمل الجماعي · إدارة الضغط</p>
  </div>
  <div style="flex:1;padding:24px 32px;border-bottom:2px solid #1A1A1A;border-right:4px solid ${RD};background:${DRD};display:flex;flex-direction:column;justify-content:center;">
    <p style="color:${WH};font-size:14px;font-weight:700;direction:rtl;">الفجوة التقنية</p>
    <p style="color:#664444;font-size:13px;margin-top:6px;direction:rtl;">Excel · العرض · الكتابة المهنية</p>
  </div>
  <div style="flex:1;padding:24px 32px;border-right:4px solid ${GD};display:flex;flex-direction:column;justify-content:center;">
    <p style="color:${GD};font-size:14px;font-weight:700;direction:rtl;">غياب الشبكات</p>
    <p style="color:#666;font-size:13px;margin-top:6px;direction:rtl;">80% من الوظائف تُشغَل عبر المعارف</p>
  </div>
</div>
</body></html>`;

// ─── SLIDE 04: DATA GAP (Chart.js bar) ────────────────────────────────────
slides['04'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:4px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">THE DATA GAP</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;">فجوة البطالة: خريجو الجامعات مقابل سوق العمل</h1>
<!-- stats top row -->
<div style="position:absolute;top:80px;right:32px;display:flex;gap:12px;direction:ltr;">
  <div style="background:${DRD};border-top:4px solid ${RD};padding:16px 24px;text-align:center;">
    <p style="color:${RD};font-size:36px;font-weight:900;">41.5%</p>
    <p style="color:#888;font-size:11px;direction:rtl;margin-top:4px;">بطالة الخريجين</p>
  </div>
  <div style="background:${MK};border-top:4px solid ${GD};padding:16px 24px;text-align:center;">
    <p style="color:${GD};font-size:36px;font-weight:900;">6%</p>
    <p style="color:#888;font-size:11px;direction:rtl;margin-top:4px;">البطالة العامة</p>
  </div>
  <div style="background:${DGD};border-top:4px solid ${GD};padding:16px 24px;text-align:center;">
    <p style="color:${GD};font-size:36px;font-weight:900;">×6.9</p>
    <p style="color:#888;font-size:11px;direction:rtl;margin-top:4px;">الفجوة</p>
  </div>
</div>
<!-- chart -->
<canvas id="ch" style="position:absolute;top:168px;left:32px;right:32px;bottom:20px;width:896px;height:348px;"></canvas>
<script>
const ctx = document.getElementById('ch');
ctx.width=896; ctx.height=348;
new Chart(ctx,{type:'bar',data:{
  labels:['مؤهل متوسط','دبلوم','بكالوريوس','دراسات عليا'],
  datasets:[{
    label:'نسبة البطالة %',
    data:[18,29,41.5,35],
    backgroundColor:['${MK}','${MK}','${RD}','${MK}'],
    borderColor:['${GD}','${GD}','${RD}','${GD}'],
    borderWidth:2,borderRadius:4
  }]
},options:{
  responsive:false,animation:false,
  plugins:{legend:{display:false},tooltip:{enabled:false}},
  scales:{
    x:{ticks:{color:'#AAA',font:{size:13}},grid:{color:'#222'}},
    y:{ticks:{color:'#AAA',font:{size:12},callback:v=>v+'%'},grid:{color:'#222'},max:50}
  }
}});
</script>
</body></html>`;

// ─── SLIDE 05: EMPLOYER VOICE ──────────────────────────────────────────────
slides['05'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:4px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">EMPLOYER VOICE</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;">ماذا يقول أصحاب العمل؟</h1>
<p style="position:absolute;top:72px;left:32px;color:#444;font-size:11px;direction:ltr;">Nexford Employer Survey — Egypt 2026 · N=1,200</p>
<div style="position:absolute;top:96px;left:0;right:0;bottom:12px;display:flex;">
  <div style="flex:1;background:${DRD};border-top:5px solid ${RD};display:flex;flex-direction:column;justify-content:space-between;padding:36px 32px;">
    <p style="color:${RD};font-size:13px;letter-spacing:2px;direction:ltr;">SKILL GAP</p>
    <p style="color:${RD};font-size:100px;font-weight:900;line-height:1;direction:ltr;">78%</p>
    <p style="color:${WH};font-size:17px;font-weight:600;direction:rtl;line-height:1.5;">يرون نقص الكفاءات تحدياً رئيسياً للتعيين</p>
  </div>
  <div style="flex:1;background:${MK};border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:space-between;padding:36px 32px;">
    <p style="color:${GD};font-size:13px;letter-spacing:2px;direction:ltr;">BELOW STANDARD</p>
    <p style="color:${GD};font-size:100px;font-weight:900;line-height:1;direction:ltr;">41%</p>
    <p style="color:${WH};font-size:17px;font-weight:600;direction:rtl;line-height:1.5;">يصفون جاهزية الخريجين بـ"دون المستوى"</p>
  </div>
  <div style="flex:1;background:${MK};border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:space-between;padding:36px 32px;">
    <p style="color:${GD};font-size:13px;letter-spacing:2px;direction:ltr;">WILLING TO FUND</p>
    <p style="color:${GD};font-size:100px;font-weight:900;line-height:1;direction:ltr;">51%</p>
    <p style="color:${WH};font-size:17px;font-weight:600;direction:rtl;line-height:1.5;">مستعدون لتمويل التدريب عبر شراكة مؤسسية</p>
  </div>
</div>
</body></html>`;

// ─── SLIDE 06: ROOT CAUSES ─────────────────────────────────────────────────
slides['06'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:4px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">ROOT CAUSES</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;">لماذا يفشل الخريجون في الحصول على وظائف؟</h1>
<div style="position:absolute;top:86px;left:0;right:0;bottom:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:4px;">
  <div style="background:${MK};border-right:5px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:32px 28px;">
    <p style="color:${GD};font-size:48px;font-weight:900;direction:ltr;">01</p>
    <p style="color:${WH};font-size:20px;font-weight:700;margin-top:8px;direction:rtl;">فجوة المهارات الناعمة</p>
    <p style="color:#666;font-size:14px;margin-top:10px;direction:rtl;">التواصل · ضبط الوقت · الذكاء العاطفي</p>
  </div>
  <div style="background:${DRD};border-right:5px solid ${RD};display:flex;flex-direction:column;justify-content:center;padding:32px 28px;">
    <p style="color:${RD};font-size:48px;font-weight:900;direction:ltr;">02</p>
    <p style="color:${WH};font-size:20px;font-weight:700;margin-top:8px;direction:rtl;">غياب الخبرة العملية</p>
    <p style="color:#664444;font-size:14px;margin-top:10px;direction:rtl;">مناهج نظرية · لا مشاريع حقيقية</p>
  </div>
  <div style="background:${MK};border-right:5px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:32px 28px;">
    <p style="color:${GD};font-size:48px;font-weight:900;direction:ltr;">03</p>
    <p style="color:${WH};font-size:20px;font-weight:700;margin-top:8px;direction:rtl;">ضعف إمكانية التحقق</p>
    <p style="color:#666;font-size:14px;margin-top:10px;direction:rtl;">أصحاب العمل لا يثقون في شهادات التدريب</p>
  </div>
  <div style="background:${DRD};border-right:5px solid ${RD};display:flex;flex-direction:column;justify-content:center;padding:32px 28px;">
    <p style="color:${RD};font-size:48px;font-weight:900;direction:ltr;">04</p>
    <p style="color:${WH};font-size:20px;font-weight:700;margin-top:8px;direction:rtl;">انعدام الشبكات المهنية</p>
    <p style="color:#664444;font-size:14px;margin-top:10px;direction:rtl;">80% من الوظائف تُشغَل عبر المعارف</p>
  </div>
</div>
</body></html>`;

// ─── SLIDE 07: TRAJECTORY (Chart.js line) ─────────────────────────────────
slides['07'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:4px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">THE TRAJECTORY</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:22px;font-weight:800;direction:rtl;">المشكلة تتفاقم · كل عام يُضاف نصف مليون خريج</h1>
<!-- right stats -->
<div style="position:absolute;top:80px;right:32px;width:240px;bottom:20px;display:flex;flex-direction:column;gap:8px;">
  <div style="flex:1;background:${DRD};border-top:5px solid ${RD};padding:20px;display:flex;flex-direction:column;justify-content:center;">
    <p style="color:${RD};font-size:13px;letter-spacing:2px;direction:ltr;">BY 2035</p>
    <p style="color:${RD};font-size:56px;font-weight:900;direction:ltr;line-height:1;margin-top:8px;">800K</p>
    <p style="color:${WH};font-size:14px;margin-top:8px;direction:rtl;">داخل جديد سنوياً</p>
  </div>
  <div style="flex:1;background:${MK};border-top:5px solid ${GD};padding:20px;display:flex;flex-direction:column;justify-content:center;">
    <p style="color:${GD};font-size:13px;letter-spacing:2px;direction:ltr;">SINCE 2000</p>
    <p style="color:${GD};font-size:56px;font-weight:900;direction:ltr;line-height:1;margin-top:8px;">+110%</p>
    <p style="color:${WH};font-size:14px;margin-top:8px;direction:rtl;">نمو الضغط على سوق العمل</p>
  </div>
</div>
<!-- chart -->
<canvas id="ch" style="position:absolute;top:80px;left:32px;bottom:20px;" width="668" height="436"></canvas>
<script>
new Chart(document.getElementById('ch'),{type:'line',data:{
  labels:['2015','2017','2019','2021','2023','2025','2027','2030','2035'],
  datasets:[
    {label:'خريجون جدد (ألف)',data:[320,360,400,440,480,500,560,640,800],borderColor:'${RD}',backgroundColor:'rgba(164,35,42,0.15)',tension:0.4,fill:true,pointRadius:4,pointBackgroundColor:'${RD}'},
    {label:'وظائف متاحة (ألف)',data:[280,290,300,295,310,320,330,350,380],borderColor:'${GD}',backgroundColor:'rgba(200,162,76,0.08)',tension:0.4,fill:true,pointRadius:4,pointBackgroundColor:'${GD}'}
  ]
},options:{responsive:false,animation:false,
  plugins:{legend:{labels:{color:'#AAA',font:{size:12}}}},
  scales:{x:{ticks:{color:'#888'},grid:{color:'#222'}},y:{ticks:{color:'#888',callback:v=>v+'K'},grid:{color:'#222'}}}
}});
</script>
</body></html>`;

// ─── SLIDE 08: THE SOLUTION ────────────────────────────────────────────────
slides['08'] = BASE + `
<div style="position:absolute;top:0;left:0;width:6px;height:540px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<!-- Left brand panel -->
<div style="position:absolute;top:0;left:6px;width:320px;height:540px;background:#060606;display:flex;flex-direction:column;justify-content:center;padding:48px 40px;">
  <p style="color:${GD};font-size:10px;letter-spacing:5px;margin-bottom:24px;direction:ltr;">THE ANSWER</p>
  <h1 style="color:${GD};font-size:64px;font-weight:900;letter-spacing:2px;line-height:1;direction:ltr;">JAHIZOON</h1>
  <h2 style="color:${WH};font-size:36px;font-weight:700;margin-top:12px;direction:rtl;">جاهزون</h2>
  <div style="width:56px;height:3px;background:${GD};margin:24px 0;"></div>
  <p style="color:#555;font-size:14px;line-height:1.7;direction:rtl;">برنامج وطني يُحوّل الخريجين إلى كفاءات موثّقة جاهزة للتوظيف الفوري</p>
</div>
<!-- 3 pillars -->
<div style="position:absolute;top:0;left:326px;right:0;height:540px;display:flex;flex-direction:column;gap:0;">
  <div style="flex:1;background:${MK};border-right:5px solid ${GD};padding:32px 28px;display:flex;flex-direction:column;justify-content:center;border-bottom:2px solid #1A1A1A;">
    <p style="color:${GD};font-size:11px;letter-spacing:4px;direction:ltr;margin-bottom:10px;">TRAIN</p>
    <p style="color:${WH};font-size:22px;font-weight:700;direction:rtl;">تدريب مكثف · 12 أسبوعاً</p>
    <p style="color:#555;font-size:14px;margin-top:8px;direction:rtl;">مهارات العمل الفعلية · مدربون معتمدون</p>
  </div>
  <div style="flex:1;background:${DRD};border-right:5px solid ${RD};padding:32px 28px;display:flex;flex-direction:column;justify-content:center;border-bottom:2px solid #2A0000;">
    <p style="color:${RD};font-size:11px;letter-spacing:4px;direction:ltr;margin-bottom:10px;">ASSESS</p>
    <p style="color:${WH};font-size:22px;font-weight:700;direction:rtl;">تقييم مصوّر · موثّق</p>
    <p style="color:#664444;font-size:14px;margin-top:8px;direction:rtl;">امتحان نهائي مسجّل يراه أصحاب العمل</p>
  </div>
  <div style="flex:1;background:${MK};border-right:5px solid ${GD};padding:32px 28px;display:flex;flex-direction:column;justify-content:center;">
    <p style="color:${GD};font-size:11px;letter-spacing:4px;direction:ltr;margin-bottom:10px;">PLACE</p>
    <p style="color:${WH};font-size:22px;font-weight:700;direction:rtl;">توظيف مضمون</p>
    <p style="color:#555;font-size:14px;margin-top:8px;direction:rtl;">شبكة شركاء مؤسسيين · ربط مباشر</p>
  </div>
</div>
</body></html>`;

// ─── SLIDE 09: THE PROGRAMME (5 steps) ────────────────────────────────────
slides['09'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:5px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">THE PROGRAMME</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;">منهجية جاهزون: من الفجوة إلى التوظيف</h1>
<!-- 5 columns full height -->
<div style="position:absolute;top:86px;left:0;right:0;bottom:12px;display:flex;gap:0;">
  <div style="flex:1;background:${MK};border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:space-between;padding:28px 18px;border-left:2px solid #1A1A1A;">
    <p style="color:${GD};font-size:40px;font-weight:900;direction:ltr;">01</p>
    <div>
      <p style="color:${WH};font-size:16px;font-weight:700;direction:rtl;">التقييم</p>
      <p style="color:#555;font-size:12px;margin-top:8px;direction:rtl;line-height:1.5;">تحديد الفجوات الفردية عبر أداة تشخيص رقمية</p>
    </div>
  </div>
  <div style="flex:1;background:${MK};border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:space-between;padding:28px 18px;border-left:2px solid #1A1A1A;">
    <p style="color:${GD};font-size:40px;font-weight:900;direction:ltr;">02</p>
    <div>
      <p style="color:${WH};font-size:16px;font-weight:700;direction:rtl;">التدريب</p>
      <p style="color:#555;font-size:12px;margin-top:8px;direction:rtl;line-height:1.5;">12 أسبوعاً مكثفاً · مهارات ناعمة وتقنية</p>
    </div>
  </div>
  <div style="flex:1;background:${DRD};border-top:5px solid ${RD};display:flex;flex-direction:column;justify-content:space-between;padding:28px 18px;border-left:2px solid #2A0000;">
    <p style="color:${RD};font-size:40px;font-weight:900;direction:ltr;">03</p>
    <div>
      <p style="color:${WH};font-size:16px;font-weight:700;direction:rtl;">الامتحان المصوّر</p>
      <p style="color:#664444;font-size:12px;margin-top:8px;direction:rtl;line-height:1.5;">تقييم أداء مسجّل · معتمد من أصحاب العمل</p>
    </div>
  </div>
  <div style="flex:1;background:${MK};border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:space-between;padding:28px 18px;border-left:2px solid #1A1A1A;">
    <p style="color:${GD};font-size:40px;font-weight:900;direction:ltr;">04</p>
    <div>
      <p style="color:${WH};font-size:16px;font-weight:700;direction:rtl;">التوظيف</p>
      <p style="color:#555;font-size:12px;margin-top:8px;direction:rtl;line-height:1.5;">ربط مع شركاء مؤسسيين وفرص وظيفية حقيقية</p>
    </div>
  </div>
  <div style="flex:1;background:#0A1A0A;border-top:5px solid #3A7A3A;display:flex;flex-direction:column;justify-content:space-between;padding:28px 18px;">
    <p style="color:#3A7A3A;font-size:40px;font-weight:900;direction:ltr;">05</p>
    <div>
      <p style="color:${WH};font-size:16px;font-weight:700;direction:rtl;">المتابعة</p>
      <p style="color:#335533;font-size:12px;margin-top:8px;direction:rtl;line-height:1.5;">6 أشهر دعم بعد التوظيف</p>
    </div>
  </div>
</div>
<div style="position:absolute;bottom:20px;left:32px;right:32px;display:flex;justify-content:center;">
  <p style="color:#333;font-size:12px;direction:rtl;">هدف التوظيف: 75% من المتدربين خلال 90 يوماً من إتمام البرنامج</p>
</div>
</body></html>`;

// ─── SLIDE 10: FILMED EXAM ─────────────────────────────────────────────────
slides['10'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:5px;background:${RD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${GD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${RD};font-size:10px;letter-spacing:5px;direction:ltr;">THE DIFFERENTIATOR</p>
<!-- Left: big visual -->
<div style="position:absolute;top:0;left:0;width:480px;height:540px;background:#0A0000;display:flex;flex-direction:column;justify-content:center;align-items:center;border-right:4px solid #1A0000;">
  <div style="width:200px;height:140px;border:3px solid ${RD};display:flex;align-items:center;justify-content:center;position:relative;">
    <div style="width:16px;height:16px;border-radius:50%;background:${RD};position:absolute;top:12px;left:12px;"></div>
    <p style="color:${RD};font-size:13px;letter-spacing:3px;direction:ltr;">● REC</p>
  </div>
  <p style="color:${RD};font-size:52px;font-weight:900;direction:ltr;margin-top:32px;line-height:1;">الامتحان</p>
  <p style="color:${WH};font-size:32px;font-weight:700;direction:rtl;margin-top:8px;">المصوّر</p>
</div>
<!-- Right: 3 features -->
<div style="position:absolute;top:0;left:484px;right:0;height:540px;display:flex;flex-direction:column;">
  <div style="flex:1;padding:28px 32px;border-bottom:2px solid #1A1A1A;display:flex;flex-direction:column;justify-content:center;">
    <p style="color:${GD};font-size:11px;letter-spacing:3px;direction:ltr;margin-bottom:8px;">RECORDED</p>
    <p style="color:${WH};font-size:18px;font-weight:700;direction:rtl;">امتحان أداء مسجّل بالفيديو</p>
    <p style="color:#555;font-size:13px;margin-top:8px;direction:rtl;">يُرسَل لأصحاب العمل مباشرةً</p>
  </div>
  <div style="flex:1;padding:28px 32px;border-bottom:2px solid #1A1A1A;background:#0A0A0A;display:flex;flex-direction:column;justify-content:center;">
    <p style="color:${RD};font-size:11px;letter-spacing:3px;direction:ltr;margin-bottom:8px;">VERIFIED</p>
    <p style="color:${WH};font-size:18px;font-weight:700;direction:rtl;">توثيق رقمي معتمد</p>
    <p style="color:#555;font-size:13px;margin-top:8px;direction:rtl;">شهادة قابلة للتحقق · لا تزوير ممكن</p>
  </div>
  <div style="flex:1;padding:28px 32px;display:flex;flex-direction:column;justify-content:center;">
    <p style="color:${GD};font-size:11px;letter-spacing:3px;direction:ltr;margin-bottom:8px;">TRUSTED</p>
    <p style="color:${WH};font-size:18px;font-weight:700;direction:rtl;">ثقة أصحاب العمل</p>
    <p style="color:#555;font-size:13px;margin-top:8px;direction:rtl;">93% من الشركاء يفضّلون هذا النموذج على المقابلة التقليدية</p>
  </div>
</div>
</body></html>`;

// ─── SLIDE 11: ECOSYSTEM ──────────────────────────────────────────────────
slides['11'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:5px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">THE ECOSYSTEM</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;">المنظومة المتكاملة · ثلاثة محاور</h1>
<div style="position:absolute;top:86px;left:0;right:0;bottom:0;display:flex;gap:0;">
  <div style="flex:1;background:#0A0A1A;border-top:5px solid #4444AA;display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;border-left:2px solid #111;">
    <div>
      <p style="color:#6666CC;font-size:11px;letter-spacing:4px;direction:ltr;margin-bottom:16px;">ACADEMIA</p>
      <p style="color:${WH};font-size:22px;font-weight:700;direction:rtl;">الجامعات</p>
      <div style="width:40px;height:2px;background:#4444AA;margin:16px 0;"></div>
      <p style="color:#555;font-size:13px;direction:rtl;line-height:1.7;">اتفاقيات مع 12 جامعة<br>مسار مدمج في الفصل الأخير<br>اعتماد أكاديمي مشترك</p>
    </div>
    <p style="color:#333;font-size:12px;direction:ltr;">12 Universities</p>
  </div>
  <div style="flex:1;background:#0A0A0A;border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;border-left:2px solid #111;">
    <div>
      <p style="color:${GD};font-size:11px;letter-spacing:4px;direction:ltr;margin-bottom:16px;">JAHIZOON CORE</p>
      <p style="color:${WH};font-size:22px;font-weight:700;direction:rtl;">جاهزون</p>
      <div style="width:40px;height:2px;background:${GD};margin:16px 0;"></div>
      <p style="color:#666;font-size:13px;direction:rtl;line-height:1.7;">منهج مكثف 12 أسبوعاً<br>امتحان أداء مصوّر<br>منصة توظيف رقمية</p>
    </div>
    <p style="color:#444;font-size:12px;direction:ltr;">Hub — Cairo + 3 Cities</p>
  </div>
  <div style="flex:1;background:#0A1A0A;border-top:5px solid #3A7A3A;display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;">
    <div>
      <p style="color:#3A7A3A;font-size:11px;letter-spacing:4px;direction:ltr;margin-bottom:16px;">EMPLOYERS</p>
      <p style="color:${WH};font-size:22px;font-weight:700;direction:rtl;">أصحاب العمل</p>
      <div style="width:40px;height:2px;background:#3A7A3A;margin:16px 0;"></div>
      <p style="color:#335533;font-size:13px;direction:rtl;line-height:1.7;">40+ شريك مؤسسي<br>تعيين مباشر خلال 90 يوماً<br>تمويل مشترك للتدريب</p>
    </div>
    <p style="color:#223322;font-size:12px;direction:ltr;">40+ Corporate Partners</p>
  </div>
</div>
</body></html>`;

// ─── SLIDE 12: BUSINESS MODEL ──────────────────────────────────────────────
slides['12'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:5px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">BUSINESS MODEL</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;">مصادر الإيراد · نموذج مستدام</h1>
<div style="position:absolute;top:86px;left:0;right:0;bottom:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:4px;">
  <div style="background:${MK};border-right:5px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:32px 28px;">
    <p style="color:${GD};font-size:11px;letter-spacing:3px;direction:ltr;margin-bottom:8px;">STREAM 01</p>
    <p style="color:${WH};font-size:20px;font-weight:700;direction:rtl;">رسوم التدريب</p>
    <p style="color:${GD};font-size:36px;font-weight:900;direction:ltr;margin-top:8px;">3,500 EGP</p>
    <p style="color:#555;font-size:13px;margin-top:8px;direction:rtl;">للمتدرب · قابل للتقسيط · دعم حكومي ممكن</p>
  </div>
  <div style="background:${DRD};border-right:5px solid ${RD};display:flex;flex-direction:column;justify-content:center;padding:32px 28px;">
    <p style="color:${RD};font-size:11px;letter-spacing:3px;direction:ltr;margin-bottom:8px;">STREAM 02</p>
    <p style="color:${WH};font-size:20px;font-weight:700;direction:rtl;">رسوم التوظيف</p>
    <p style="color:${RD};font-size:36px;font-weight:900;direction:ltr;margin-top:8px;">8,000 EGP</p>
    <p style="color:#664444;font-size:13px;margin-top:8px;direction:rtl;">تدفعها الشركة عند التعيين الناجح</p>
  </div>
  <div style="background:${MK};border-right:5px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:32px 28px;">
    <p style="color:${GD};font-size:11px;letter-spacing:3px;direction:ltr;margin-bottom:8px;">STREAM 03</p>
    <p style="color:${WH};font-size:20px;font-weight:700;direction:rtl;">رسوم الشراكة المؤسسية</p>
    <p style="color:${GD};font-size:36px;font-weight:900;direction:ltr;margin-top:8px;">50K EGP</p>
    <p style="color:#555;font-size:13px;margin-top:8px;direction:rtl;">سنوياً / شريك · برامج تدريب مخصصة</p>
  </div>
  <div style="background:#0A1A0A;border-right:5px solid #3A7A3A;display:flex;flex-direction:column;justify-content:center;padding:32px 28px;">
    <p style="color:#3A7A3A;font-size:11px;letter-spacing:3px;direction:ltr;margin-bottom:8px;">STREAM 04</p>
    <p style="color:${WH};font-size:20px;font-weight:700;direction:rtl;">دعم حكومي ومنح</p>
    <p style="color:#3A7A3A;font-size:36px;font-weight:900;direction:ltr;margin-top:8px;">20M EGP</p>
    <p style="color:#335533;font-size:13px;margin-top:8px;direction:rtl;">مرحلة أولى · وزارة التضامن الاجتماعي</p>
  </div>
</div>
</body></html>`;

// ─── SLIDE 13: REVENUE MIX (Chart.js doughnut) ────────────────────────────
slides['13'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:5px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">REVENUE MIX · YEAR 5</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;">توزيع الإيرادات · العام الخامس</h1>
<canvas id="ch" style="position:absolute;top:80px;left:32px;bottom:20px;" width="460" height="436"></canvas>
<!-- Legend right -->
<div style="position:absolute;top:80px;left:520px;right:32px;bottom:20px;display:flex;flex-direction:column;justify-content:center;gap:20px;">
  <div style="display:flex;align-items:center;gap:16px;direction:rtl;">
    <div style="width:16px;height:16px;background:${GD};flex-shrink:0;"></div>
    <div>
      <p style="color:${WH};font-size:16px;font-weight:700;direction:rtl;">رسوم التدريب</p>
      <p style="color:${GD};font-size:28px;font-weight:900;direction:ltr;">45%</p>
      <p style="color:#555;font-size:12px;direction:rtl;">~22.5M EGP</p>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:16px;direction:rtl;">
    <div style="width:16px;height:16px;background:${RD};flex-shrink:0;"></div>
    <div>
      <p style="color:${WH};font-size:16px;font-weight:700;direction:rtl;">رسوم التوظيف</p>
      <p style="color:${RD};font-size:28px;font-weight:900;direction:ltr;">30%</p>
      <p style="color:#555;font-size:12px;direction:rtl;">~15M EGP</p>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:16px;direction:rtl;">
    <div style="width:16px;height:16px;background:#4444AA;flex-shrink:0;"></div>
    <div>
      <p style="color:${WH};font-size:16px;font-weight:700;direction:rtl;">شراكات مؤسسية</p>
      <p style="color:#6666CC;font-size:28px;font-weight:900;direction:ltr;">15%</p>
      <p style="color:#555;font-size:12px;direction:rtl;">~7.5M EGP</p>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:16px;direction:rtl;">
    <div style="width:16px;height:16px;background:#3A7A3A;flex-shrink:0;"></div>
    <div>
      <p style="color:${WH};font-size:16px;font-weight:700;direction:rtl;">دعم حكومي</p>
      <p style="color:#3A7A3A;font-size:28px;font-weight:900;direction:ltr;">10%</p>
      <p style="color:#555;font-size:12px;direction:rtl;">~5M EGP</p>
    </div>
  </div>
</div>
<script>
new Chart(document.getElementById('ch'),{type:'doughnut',data:{
  labels:['رسوم التدريب','رسوم التوظيف','شراكات مؤسسية','دعم حكومي'],
  datasets:[{data:[45,30,15,10],backgroundColor:['${GD}','${RD}','#4444AA','#3A7A3A'],borderWidth:0,hoverOffset:4}]
},options:{responsive:false,animation:false,cutout:'65%',
  plugins:{legend:{display:false},tooltip:{enabled:false}}
}});
</script>
</body></html>`;

// ─── SLIDE 14: P&L DASHBOARD (Chart.js line) ──────────────────────────────
slides['14'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:5px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">10-YEAR P&L DASHBOARD</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:22px;font-weight:800;direction:rtl;">توقعات الأداء المالي 2025–2035 (مليون جنيه مصري)</h1>
<!-- KPI strip -->
<div style="position:absolute;top:78px;left:32px;right:32px;height:56px;display:flex;gap:8px;direction:ltr;">
  <div style="flex:1;background:${DRD};border-top:3px solid ${RD};display:flex;flex-direction:column;justify-content:center;padding:0 16px;">
    <p style="color:#664444;font-size:10px;direction:ltr;">إيراد 2035</p>
    <p style="color:${RD};font-size:22px;font-weight:900;direction:ltr;">132M EGP</p>
  </div>
  <div style="flex:1;background:${MK};border-top:3px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:0 16px;">
    <p style="color:#444;font-size:10px;direction:ltr;">EBITDA 2035</p>
    <p style="color:${GD};font-size:22px;font-weight:900;direction:ltr;">68.6M EGP</p>
  </div>
  <div style="flex:1;background:${MK};border-top:3px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:0 16px;">
    <p style="color:#444;font-size:10px;direction:ltr;">متدربون 2035</p>
    <p style="color:${GD};font-size:22px;font-weight:900;direction:ltr;">30,000</p>
  </div>
  <div style="flex:1;background:${DRD};border-top:3px solid ${RD};display:flex;flex-direction:column;justify-content:center;padding:0 16px;">
    <p style="color:#664444;font-size:10px;direction:ltr;">التعادل</p>
    <p style="color:${RD};font-size:22px;font-weight:900;direction:ltr;">2027</p>
  </div>
</div>
<!-- chart -->
<canvas id="ch" style="position:absolute;top:148px;left:32px;right:32px;bottom:20px;" width="896" height="368"></canvas>
<script>
const yrs=['2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035'];
const rev=[2.5,5.5,11,19,29,42,57,74,92,110,132];
const ebitda=[-1.2,-0.8,0.5,3.2,7.8,14,22,33,44,56,68.6];
const stud=[300,650,1300,2200,3400,5000,7000,9500,12500,16000,20000];
new Chart(document.getElementById('ch'),{type:'line',data:{
  labels:yrs,
  datasets:[
    {label:'الإيراد (مليون جنيه)',data:rev,borderColor:'${GD}',backgroundColor:'rgba(200,162,76,0.1)',tension:0.4,fill:true,pointRadius:4,pointBackgroundColor:'${GD}',yAxisID:'y'},
    {label:'EBITDA (مليون جنيه)',data:ebitda,borderColor:'${RD}',backgroundColor:'rgba(164,35,42,0.08)',tension:0.4,fill:true,pointRadius:4,pointBackgroundColor:'${RD}',yAxisID:'y'}
  ]
},options:{responsive:false,animation:false,
  plugins:{legend:{labels:{color:'#AAA',font:{size:12}}}},
  scales:{
    y:{ticks:{color:'#888',callback:v=>v+'M'},grid:{color:'#222'},title:{display:true,text:'مليون جنيه',color:'#555'}},
    x:{ticks:{color:'#888'},grid:{color:'#222'}}
  }
}});
</script>
</body></html>`;

// ─── SLIDE 15: SCALE PLAN ──────────────────────────────────────────────────
slides['15'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:5px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">SCALE PLAN</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;">خطة التوسع · ثلاث مراحل</h1>
<div style="position:absolute;top:86px;left:0;right:0;bottom:0;display:flex;gap:0;">
  <div style="flex:1;background:#0A0A1A;border-top:5px solid #4444AA;display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;border-left:2px solid #111;">
    <div>
      <p style="color:#4444AA;font-size:11px;letter-spacing:4px;direction:ltr;margin-bottom:8px;">PHASE 01 · 2025–2026</p>
      <p style="color:${WH};font-size:24px;font-weight:700;direction:rtl;">التأسيس</p>
      <div style="width:40px;height:2px;background:#4444AA;margin:16px 0;"></div>
      <p style="color:#444;font-size:13px;direction:rtl;line-height:1.8;">300 متدرب · القاهرة<br>3 دفعات تجريبية<br>5 شركاء مؤسسيين<br>إثبات النموذج</p>
    </div>
    <div>
      <p style="color:#4444AA;font-size:36px;font-weight:900;direction:ltr;">300</p>
      <p style="color:#333;font-size:12px;direction:rtl;">متدرب في العام الأول</p>
    </div>
  </div>
  <div style="flex:1;background:${MK};border-top:5px solid ${GD};display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;border-left:2px solid #1A1A1A;">
    <div>
      <p style="color:${GD};font-size:11px;letter-spacing:4px;direction:ltr;margin-bottom:8px;">PHASE 02 · 2027–2028</p>
      <p style="color:${WH};font-size:24px;font-weight:700;direction:rtl;">التوسع</p>
      <div style="width:40px;height:2px;background:${GD};margin:16px 0;"></div>
      <p style="color:#555;font-size:13px;direction:rtl;line-height:1.8;">2,200 متدرب / سنة<br>4 مدن رئيسية<br>20 شريك مؤسسي<br>التعادل المالي</p>
    </div>
    <div>
      <p style="color:${GD};font-size:36px;font-weight:900;direction:ltr;">2,200</p>
      <p style="color:#444;font-size:12px;direction:rtl;">متدرب سنوياً</p>
    </div>
  </div>
  <div style="flex:1;background:#0A1A0A;border-top:5px solid #3A7A3A;display:flex;flex-direction:column;justify-content:space-between;padding:36px 28px;">
    <div>
      <p style="color:#3A7A3A;font-size:11px;letter-spacing:4px;direction:ltr;margin-bottom:8px;">PHASE 03 · 2029–2030</p>
      <p style="color:${WH};font-size:24px;font-weight:700;direction:rtl;">الانتشار الوطني</p>
      <div style="width:40px;height:2px;background:#3A7A3A;margin:16px 0;"></div>
      <p style="color:#335533;font-size:13px;direction:rtl;line-height:1.8;">5,000+ متدرب / سنة<br>جميع المحافظات<br>40+ شريك مؤسسي<br>نقطة مرجعية وطنية</p>
    </div>
    <div>
      <p style="color:#3A7A3A;font-size:36px;font-weight:900;direction:ltr;">5,000+</p>
      <p style="color:#223322;font-size:12px;direction:rtl;">متدرب سنوياً بحلول 2030</p>
    </div>
  </div>
</div>
</body></html>`;

// ─── SLIDE 16: VISION 2030 ─────────────────────────────────────────────────
slides['16'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:5px;background:${GD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
<!-- Big watermark -->
<p style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:#111;font-size:240px;font-weight:900;direction:ltr;white-space:nowrap;pointer-events:none;user-select:none;">2030</p>
<p style="position:absolute;top:18px;left:32px;color:${GD};font-size:10px;letter-spacing:5px;direction:ltr;">EGYPT VISION ALIGNMENT</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;">جاهزون · ركيزة رؤية مصر 2030</h1>
<!-- 5 alignment points -->
<div style="position:absolute;top:86px;left:32px;right:32px;bottom:20px;display:flex;flex-direction:column;justify-content:space-between;gap:8px;">
  <div style="flex:1;background:rgba(10,10,10,0.9);border-right:4px solid ${GD};padding:14px 20px;display:flex;align-items:center;gap:20px;">
    <p style="color:${GD};font-size:28px;font-weight:900;direction:ltr;min-width:48px;">01</p>
    <div style="direction:rtl;">
      <p style="color:${WH};font-size:16px;font-weight:700;">خفض البطالة إلى 5%</p>
      <p style="color:#555;font-size:12px;margin-top:2px;">جاهزون يوظّف 75% من خريجيه خلال 90 يوماً</p>
    </div>
  </div>
  <div style="flex:1;background:rgba(10,10,10,0.9);border-right:4px solid ${RD};padding:14px 20px;display:flex;align-items:center;gap:20px;">
    <p style="color:${RD};font-size:28px;font-weight:900;direction:ltr;min-width:48px;">02</p>
    <div style="direction:rtl;">
      <p style="color:${WH};font-size:16px;font-weight:700;">تطوير رأس المال البشري</p>
      <p style="color:#555;font-size:12px;margin-top:2px;">كفاءات موثّقة قابلة للقياس · معيار وطني للجاهزية المهنية</p>
    </div>
  </div>
  <div style="flex:1;background:rgba(10,10,10,0.9);border-right:4px solid ${GD};padding:14px 20px;display:flex;align-items:center;gap:20px;">
    <p style="color:${GD};font-size:28px;font-weight:900;direction:ltr;min-width:48px;">03</p>
    <div style="direction:rtl;">
      <p style="color:${WH};font-size:16px;font-weight:700;">تمكين الشباب اقتصادياً</p>
      <p style="color:#555;font-size:12px;margin-top:2px;">30,000 خريج موظف بحلول 2035 · دخل منتج مستدام</p>
    </div>
  </div>
  <div style="flex:1;background:rgba(10,10,10,0.9);border-right:4px solid ${RD};padding:14px 20px;display:flex;align-items:center;gap:20px;">
    <p style="color:${RD};font-size:28px;font-weight:900;direction:ltr;min-width:48px;">04</p>
    <div style="direction:rtl;">
      <p style="color:${WH};font-size:16px;font-weight:700;">الشراكة بين القطاعين</p>
      <p style="color:#555;font-size:12px;margin-top:2px;">نموذج حكومي-خاص · تمويل مشترك · مسؤولية مشتركة</p>
    </div>
  </div>
  <div style="flex:1;background:rgba(10,10,10,0.9);border-right:4px solid ${GD};padding:14px 20px;display:flex;align-items:center;gap:20px;">
    <p style="color:${GD};font-size:28px;font-weight:900;direction:ltr;min-width:48px;">05</p>
    <div style="direction:rtl;">
      <p style="color:${WH};font-size:16px;font-weight:700;">التحول الرقمي في التدريب</p>
      <p style="color:#555;font-size:12px;margin-top:2px;">توثيق رقمي · منصة بيانات وطنية · قياس الأثر في الوقت الفعلي</p>
    </div>
  </div>
</div>
</body></html>`;

// ─── SLIDE 17: THE ASK ─────────────────────────────────────────────────────
slides['17'] = BASE + `
<div style="position:absolute;top:0;left:0;width:960px;height:5px;background:${RD};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${GD};"></div>
<p style="position:absolute;top:18px;left:32px;color:${RD};font-size:10px;letter-spacing:5px;direction:ltr;">THE ASK</p>
<h1 style="position:absolute;top:38px;right:32px;color:${WH};font-size:24px;font-weight:800;direction:rtl;">ما نطلبه من وزارة التضامن الاجتماعي</h1>
<div style="position:absolute;top:86px;left:0;right:0;bottom:0;display:flex;gap:0;">
  <!-- Left: big number -->
  <div style="width:380px;height:454px;background:${DRD};border-top:5px solid ${RD};display:flex;flex-direction:column;justify-content:center;padding:48px 40px;border-left:4px solid #2A0000;">
    <p style="color:${RD};font-size:13px;letter-spacing:3px;direction:ltr;margin-bottom:12px;">TOTAL INVESTMENT</p>
    <p style="color:${RD};font-size:72px;font-weight:900;line-height:1;direction:ltr;">20M</p>
    <p style="color:${WH};font-size:24px;font-weight:700;direction:ltr;margin-top:4px;">EGP</p>
    <div style="width:48px;height:2px;background:${RD};margin:20px 0;"></div>
    <p style="color:#664444;font-size:14px;direction:rtl;line-height:1.7;">المرحلة الأولى · 18 شهراً<br>300 متدرب في الدفعة الأولى</p>
  </div>
  <!-- Right: 4 items -->
  <div style="flex:1;height:454px;display:flex;flex-direction:column;">
    <div style="flex:1;padding:22px 28px;border-bottom:2px solid #1A1A1A;border-right:4px solid ${GD};display:flex;align-items:center;gap:20px;">
      <p style="color:${GD};font-size:32px;font-weight:900;direction:ltr;min-width:44px;">01</p>
      <div style="direction:rtl;">
        <p style="color:${WH};font-size:16px;font-weight:700;">دعم مالي للمرحلة التجريبية</p>
        <p style="color:#555;font-size:13px;margin-top:4px;">20 مليون جنيه · 18 شهراً · 300 خريج</p>
      </div>
    </div>
    <div style="flex:1;padding:22px 28px;border-bottom:2px solid #1A1A1A;border-right:4px solid ${RD};background:#0A0A0A;display:flex;align-items:center;gap:20px;">
      <p style="color:${RD};font-size:32px;font-weight:900;direction:ltr;min-width:44px;">02</p>
      <div style="direction:rtl;">
        <p style="color:${WH};font-size:16px;font-weight:700;">تسهيل الوصول للخريجين</p>
        <p style="color:#555;font-size:13px;margin-top:4px;">قواعد بيانات الخريجين · قنوات التواصل الرسمية</p>
      </div>
    </div>
    <div style="flex:1;padding:22px 28px;border-bottom:2px solid #1A1A1A;border-right:4px solid ${GD};display:flex;align-items:center;gap:20px;">
      <p style="color:${GD};font-size:32px;font-weight:900;direction:ltr;min-width:44px;">03</p>
      <div style="direction:rtl;">
        <p style="color:${WH};font-size:16px;font-weight:700;">اعتماد شهادة جاهزون</p>
        <p style="color:#555;font-size:13px;margin-top:4px;">توثيق رسمي من الوزارة · يرفع ثقة أصحاب العمل</p>
      </div>
    </div>
    <div style="flex:1;padding:22px 28px;border-right:4px solid ${RD};background:#0A0A0A;display:flex;align-items:center;gap:20px;">
      <p style="color:${RD};font-size:32px;font-weight:900;direction:ltr;min-width:44px;">04</p>
      <div style="direction:rtl;">
        <p style="color:${WH};font-size:16px;font-weight:700;">ربط بشبكة أصحاب العمل الحكومية</p>
        <p style="color:#555;font-size:13px;margin-top:4px;">الشركات الحكومية والهيئات · فرص توظيف مضمونة</p>
      </div>
    </div>
  </div>
</div>
</body></html>`;

// ─── SLIDE 18: CLOSING ─────────────────────────────────────────────────────
slides['18'] = BASE + `
<div style="display:flex;width:960px;height:540px;">
  <!-- Full left panel -->
  <div style="width:580px;height:540px;background:#060606;border-right:6px solid ${GD};display:flex;flex-direction:column;justify-content:center;padding:64px 56px;">
    <p style="color:${GD};font-size:10px;letter-spacing:6px;direction:ltr;margin-bottom:28px;">THE OPPORTUNITY</p>
    <h1 style="color:${WH};font-size:40px;font-weight:900;direction:rtl;line-height:1.4;">500,000 خريج ينتظرون<br>فرصة واحدة عادلة.</h1>
    <div style="width:72px;height:3px;background:${RD};margin:28px 0;"></div>
    <p style="color:${GD};font-size:28px;font-weight:700;direction:rtl;line-height:1.5;">جاهزون هي تلك الفرصة.</p>
  </div>
  <!-- Right panel -->
  <div style="flex:1;height:540px;background:${BK};display:flex;flex-direction:column;justify-content:space-between;padding:48px 44px;">
    <div style="text-align:right;">
      <p style="color:#333;font-size:11px;letter-spacing:3px;direction:ltr;margin-bottom:16px;">CONTACT</p>
      <p style="color:${GD};font-size:20px;font-weight:700;direction:ltr;">YM4 Education</p>
      <p style="color:#555;font-size:14px;margin-top:8px;direction:ltr;">info@ym4education.com</p>
    </div>
    <div style="text-align:right;">
      <p style="color:#222;font-size:11px;letter-spacing:3px;direction:ltr;margin-bottom:12px;">IMPACT TARGET</p>
      <p style="color:${GD};font-size:44px;font-weight:900;direction:ltr;line-height:1;">30,000</p>
      <p style="color:#555;font-size:14px;direction:rtl;margin-top:4px;">خريج موظف بحلول 2035</p>
    </div>
    <p style="color:#222;font-size:11px;direction:ltr;text-align:right;">JAHIZOON · جاهزون · June 2026</p>
  </div>
</div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:4px;background:${RD};"></div>
</body></html>`;

// ─── SCREENSHOT ────────────────────────────────────────────────────────────
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });

  for (const [num, html] of Object.entries(slides).sort()) {
    const page = await browser.newPage();
    await page.setViewportSize({ width: 960, height: 540 });
    await page.setContent(html, { waitUntil: 'networkidle' });
    // wait for Chart.js canvas renders
    if (html.includes('Chart(')) {
      await page.waitForTimeout(800);
    }
    const pngPath = path.join(OUT_DIR, `${num}.png`);
    await page.screenshot({ path: pngPath, clip: { x: 0, y: 0, width: 960, height: 540 } });
    await page.close();
    console.log(`  ✓ Slide ${num}`);
  }

  await browser.close();
  console.log('\nScreenshots done. Assembling PPTX...');

  // assemble
  execSync(`python3 -c "
from pptx import Presentation
from pptx.util import Emu
import os
OUT='${OUT_DIR}'
prs=Presentation()
prs.slide_width=Emu(9144000)
prs.slide_height=Emu(5143500)
blank=prs.slide_layouts[6]
for i in range(1,19):
    num=str(i).zfill(2)
    png=os.path.join(OUT,num+'.png')
    s=prs.slides.add_slide(blank)
    s.shapes.add_picture(png,0,0,width=prs.slide_width,height=prs.slide_height)
prs.save('/home/user/Mahmoud-Gadalla/outputs/Jahizoon_Minister_Presentation.pptx')
print('PPTX saved.')
"`, { stdio: 'inherit' });
})();

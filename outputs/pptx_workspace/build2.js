/**
 * JAHIZOON — Screenshot-based build
 * Each HTML slide is rendered by playwright → PNG → PPTX slide background
 * This preserves perfect Arabic RTL rendering from the browser.
 * Charts are overlaid via pptxgenjs on top of the background images.
 */
const path = require('path');
process.env.NODE_PATH = '/opt/node22/lib/node_modules';
require('module').Module._initPaths();

const pptxgen = require('pptxgenjs');
const { chromium } = require('playwright');
const fs = require('fs');

const SLIDES_DIR = path.join(__dirname, 'slides');
const OUT = '/home/user/Mahmoud-Gadalla/outputs/Jahizoon_Minister_Presentation.pptx';

const BK = '0E0E0E', GD = 'C8A24C', RD = 'A4232A', WH = 'FFFFFF';
const DG = '1A1A1A', MG = '2A2A2A';

const YEARS  = ['2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035'];
const REV    = [2.5,   5.0,   9.2,   15.8,  24.0,  36.5,  52.0,  71.0,  93.0, 115.0, 132.0];
const EBITDA = [-1.2, -0.5,   0.8,   4.2,   8.5,  16.0,  26.0,  38.5,  52.0,  68.0,  68.6];

// px → inches (at 96dpi)
const px = n => n / 96;

async function build() {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.author = 'YM4 Education';
  pptx.title  = 'JAHIZOON — Egypt National Youth Work-Readiness Programme';

  for (let i = 1; i <= 18; i++) {
    const num = String(i).padStart(2, '0');
    const htmlFile = path.join(SLIDES_DIR, `${num}.html`);
    const pngFile  = path.join(SLIDES_DIR, `${num}.png`);

    console.log(`Screenshotting slide ${i}...`);
    const page = await browser.newPage();
    await page.setViewportSize({ width: 960, height: 540 });
    await page.goto(`file://${htmlFile}`, { waitUntil: 'networkidle' });
    await page.screenshot({ path: pngFile, clip: { x: 0, y: 0, width: 960, height: 540 } });
    await page.close();

    const slide = pptx.addSlide();
    slide.background = { path: pngFile };

    // ── Chart overlays ──────────────────────────────────────────────────────
    if (i === 4) {
      // Unemployment gap bar — placeholder: left:48 top:132 w:580 h:270
      slide.addChart(pptx.charts.BAR, [
        { name: 'معدل البطالة %',
          labels: ['إجمالي سوق العمل', 'خريجو الجامعات'],
          values: [6.0, 41.5] }
      ], {
        x: px(48), y: px(132), w: px(580), h: px(270),
        barDir: 'bar', barGrouping: 'clustered',
        chartColors: [GD, RD],
        showLegend: false,
        showValue: true,
        dataLabelFontSize: 16, dataLabelFontBold: true, dataLabelColor: WH,
        dataLabelPosition: 'inEnd',
        valAxisHidden: true,
        catAxisLabelColor: WH, catAxisLabelFontSize: 13,
        plotAreaBkgndColor: BK, chartAreaBkgndColor: BK,
        valGridLine: { style: 'none' },
      });
    }

    if (i === 7) {
      // Trajectory bar — placeholder: left:48 top:108 w:560 h:290
      slide.addChart(pptx.charts.BAR, [
        { name: 'داخل جديد سنوياً (ألف)',
          labels: ['2000','2005','2010','2015','2020','2025','2030','2035'],
          values: [380, 420, 470, 510, 575, 620, 750, 800] }
      ], {
        x: px(48), y: px(108), w: px(560), h: px(290),
        barDir: 'col',
        chartColors: [RD],
        showLegend: false,
        showValue: true,
        dataLabelFontSize: 10, dataLabelFontBold: true, dataLabelColor: WH,
        valAxisHidden: true,
        catAxisLabelColor: WH, catAxisLabelFontSize: 11,
        plotAreaBkgndColor: BK, chartAreaBkgndColor: BK,
        valGridLine: { style: 'none' },
      });
    }

    if (i === 13) {
      // Revenue mix donut — placeholder: left:48 top:108 w:500 h:340
      slide.addChart(pptx.charts.DOUGHNUT, [
        { name: 'توزيع الإيرادات',
          labels: ['شراكات مؤسسية 40%', 'إنتاج إعلامي 35%', 'عقود حكومية 25%'],
          values: [40, 35, 25] }
      ], {
        x: px(48), y: px(108), w: px(500), h: px(340),
        chartColors: [GD, RD, '555555'],
        showLegend: true, legendPos: 'b', legendColor: WH, legendFontSize: 12,
        showTitle: false,
        holeSize: 55,
        dataLabelFontSize: 14, dataLabelFontBold: true, dataLabelColor: WH,
        showPercent: true,
        chartAreaBkgndColor: BK, plotAreaBkgndColor: BK,
      });
    }

    if (i === 14) {
      // 10-year P&L line — placeholder: left:48 top:168 w:864 h:280
      slide.addChart(pptx.charts.LINE, [
        { name: 'الإيراد (مليون ج.م.)', labels: YEARS, values: REV },
        { name: 'EBITDA (مليون ج.م.)', labels: YEARS, values: EBITDA },
      ], {
        x: px(48), y: px(168), w: px(864), h: px(280),
        chartColors: [GD, RD],
        showLegend: true, legendPos: 'b', legendColor: WH, legendFontSize: 11,
        showValue: false,
        lineDataSymbol: 'circle', lineDataSymbolSize: 6, lineSize: 3,
        valAxisLabelColor: WH, valAxisLabelFontSize: 11,
        catAxisLabelColor: WH, catAxisLabelFontSize: 11,
        valGridLine: { color: MG, style: 'solid', size: 1 },
        catGridLine: { style: 'none' },
        chartAreaBkgndColor: BK, plotAreaBkgndColor: BK,
      });
    }
  }

  await browser.close();
  await pptx.writeFile({ fileName: OUT });
  console.log(`\n✓ Saved: ${OUT}`);
}

build().catch(e => { console.error(e); process.exit(1); });

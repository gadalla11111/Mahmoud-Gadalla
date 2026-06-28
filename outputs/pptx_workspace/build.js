/**
 * JAHIZOON — Minister-Ready Presentation Builder
 * MERIDIAN brand: Black #0E0E0E / Gold #C8A24C / Red #A4232A / White #FFFFFF
 * 18 slides · 16:9 · PptxGenJS + html2pptx
 */
const path = require('path');
process.env.NODE_PATH = '/opt/node22/lib/node_modules';
require('module').Module._initPaths();

const pptxgen = require('pptxgenjs');
const html2pptx = require('/home/user/Mahmoud-Gadalla/anthropic_skills/pptx/scripts/html2pptx.js');
const fs = require('fs');

const SLIDES_DIR = path.join(__dirname, 'slides');
const OUT = '/home/user/Mahmoud-Gadalla/outputs/Jahizoon_Minister_Presentation.pptx';

// ── Brand ─────────────────────────────────────────────────────────────────────
const BK = '0E0E0E', GD = 'C8A24C', RD = 'A4232A', WH = 'FFFFFF';
const DG = '1A1A1A', MG = '2A2A2A';

// ── P&L data ──────────────────────────────────────────────────────────────────
const YEARS  = ['2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035'];
const REV    = [2.5,   5.0,   9.2,   15.8,  24.0,  36.5,  52.0,  71.0,  93.0, 115.0, 132.0];
const EBITDA = [-1.2, -0.5,   0.8,   4.2,   8.5,  16.0,  26.0,  38.5,  52.0,  68.0,  68.6];
const STUD   = [300,  900,  2200,  4500,  7000, 10000, 14000, 18000, 22000, 26000, 30000];

async function build() {
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.author = 'YM4 Education';
  pptx.title  = 'JAHIZOON — Egypt National Youth Work-Readiness Programme';

  for (let i = 1; i <= 18; i++) {
    const htmlFile = path.join(SLIDES_DIR, `${String(i).padStart(2,'0')}.html`);
    console.log(`Processing slide ${i}...`);
    const { slide, placeholders } = await html2pptx(htmlFile, pptx);

    // ── Slides with charts ──────────────────────────────────────────────────
    if (i === 4) {
      // Bar chart: Graduate vs Overall unemployment
      slide.addChart(pptx.charts.BAR, [
        { name: 'Unemployment Rate (%)', labels: ['Total Labour Force','Graduate (University)'], values: [6.0, 41.5] }
      ], {
        ...placeholders[0],
        barDir: 'bar',
        barGrouping: 'clustered',
        chartColors: [GD, RD],
        showLegend: false,
        showValue: true,
        dataLabelFontSize: 14,
        dataLabelFontBold: true,
        dataLabelColor: WH,
        dataLabelPosition: 'inEnd',
        valAxisHidden: true,
        catAxisLabelColor: WH,
        catAxisLabelFontSize: 13,
        plotAreaBkgndColor: BK,
        chartAreaBkgndColor: BK,
        valGridLine: { style: 'none' },
      });
    }

    if (i === 13) {
      // Donut chart: Revenue mix
      slide.addChart(pptx.charts.DOUGHNUT, [
        { name: 'Revenue Mix', labels: ['Corporate\nPartnership 40%','Media &\nProduction 35%','Government &\nInstitutional 25%'], values: [40, 35, 25] }
      ], {
        ...placeholders[0],
        chartColors: [GD, RD, '555555'],
        showLegend: true,
        legendPos: 'r',
        legendColor: WH,
        legendFontSize: 13,
        showTitle: false,
        holeSize: 55,
        dataLabelFontSize: 14,
        dataLabelFontBold: true,
        dataLabelColor: WH,
        showPercent: true,
        chartAreaBkgndColor: BK,
        plotAreaBkgndColor: BK,
      });
    }

    if (i === 14) {
      // Line chart: 10-year P&L
      slide.addChart(pptx.charts.LINE, [
        { name: 'Revenue (EGP M)', labels: YEARS, values: REV },
        { name: 'EBITDA (EGP M)',  labels: YEARS, values: EBITDA },
      ], {
        ...placeholders[0],
        chartColors: [GD, RD],
        showLegend: true,
        legendPos: 'b',
        legendColor: WH,
        legendFontSize: 11,
        showValue: false,
        lineDataSymbol: 'circle',
        lineDataSymbolSize: 6,
        lineSize: 3,
        valAxisLabelColor: WH,
        valAxisLabelFontSize: 11,
        catAxisLabelColor: WH,
        catAxisLabelFontSize: 11,
        valGridLine: { color: MG, style: 'solid', size: 1 },
        catGridLine: { style: 'none' },
        chartAreaBkgndColor: BK,
        plotAreaBkgndColor: BK,
      });
    }

    if (i === 7) {
      // Bar chart: trajectory — students needing jobs
      slide.addChart(pptx.charts.BAR, [
        { name: 'New Entrants/Year (thousands)',
          labels: ['2000','2005','2010','2015','2020','2025','2030','2035'],
          values: [380, 420, 470, 510, 575, 620, 750, 800] }
      ], {
        ...placeholders[0],
        barDir: 'col',
        chartColors: [RD],
        showLegend: false,
        showValue: true,
        dataLabelFontSize: 10,
        dataLabelFontBold: true,
        dataLabelColor: WH,
        valAxisHidden: true,
        catAxisLabelColor: WH,
        catAxisLabelFontSize: 11,
        plotAreaBkgndColor: BK,
        chartAreaBkgndColor: BK,
        valGridLine: { style: 'none' },
      });
    }
  }

  await pptx.writeFile({ fileName: OUT });
  console.log(`\n✓ Saved: ${OUT}`);
}

build().catch(e => { console.error(e); process.exit(1); });

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const slideDir = path.join(__dirname, 'slides');
  const outDir = path.join(__dirname, 'slides_browser');
  fs.mkdirSync(outDir, { recursive: true });

  for (let i = 1; i <= 18; i++) {
    const num = String(i).padStart(2, '0');
    const htmlPath = path.join(slideDir, `${num}.html`);
    const pngPath = path.join(outDir, `${num}.png`);

    const page = await browser.newPage();
    await page.setViewportSize({ width: 960, height: 540 });
    await page.goto(`file://${htmlPath}`);
    await page.waitForTimeout(200);
    await page.screenshot({ path: pngPath, clip: { x: 0, y: 0, width: 960, height: 540 } });
    await page.close();
    console.log(`  ✓ Slide ${num}`);
  }

  await browser.close();
  console.log('Done screenshotting.');
})();

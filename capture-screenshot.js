#!/usr/bin/env node
/* eslint-disable no-console */

/**
 * Capture screenshot of local website using Playwright
 * Usage: node capture-screenshot.js <url> <output-path>
 */

import { chromium } from 'playwright';

const url = process.argv[2] || 'http://localhost:4322';
const outputPath = process.argv[3] || 'screenshot.png';

(async () => {
  console.log(`Capturing screenshot of ${url}...`);

  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1920, height: 1080 }
  });

  await page.goto(url, { waitUntil: 'networkidle' });

  // Wait a bit for animations
  await page.waitForTimeout(2000);

  await page.screenshot({
    path: outputPath,
    fullPage: true
  });

  console.log(`Screenshot saved to ${outputPath}`);

  await browser.close();
})();

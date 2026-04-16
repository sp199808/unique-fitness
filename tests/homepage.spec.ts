import { test, expect } from '@playwright/test';
import { Homepage } from '../pages/Homepage';

test.describe('Unique Fitness Template Deployment Tests', () => {
    test.beforeEach(async ({ page }) => {
        await page.goto("http://localhost:3000/index.html");
    });

    test('Homepage logo Tests', async ({ page }) => {
        const homepage = new Homepage(page);
        await homepage.checkLogoVisibility();
    });

    test('Desktop Menu Tests', async ({ page }) => {
        const homepage = new Homepage(page);
        await homepage.checkDesktopMenuLinkVisibility();
    });
});

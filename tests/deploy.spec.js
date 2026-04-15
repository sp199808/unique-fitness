const { test, expect } = require('@playwright/test');
const path = require('path');

test.describe('Unique Fitness Template Deployment Tests', () => {

    test.beforeEach(async ({ page }) => {
        // Load the local HTML file
        const filePath = `file://${path.resolve(__dirname, '../index.html')}`;
        await page.goto(filePath);
    });

    // test('should have the correct document title', async ({ page }) => {
    //     await expect(page).toHaveTitle(/Unique Fitness/);
    // });

    // test('hero section should be visible and contain call to action', async ({ page }) => {
    //     const heroHeading = page.locator('h1');
    //     await expect(heroHeading).toContainText('Transform Your Life');

    //     // Desktop CTA
    //     const ctas = page.getByText('Claim 1-Day Free Pass');
    //     await expect(ctas.first()).toBeVisible();
    // });

    // test('services section renders correctly', async ({ page }) => {
    //     const servicesHeading = page.locator('#services h2');
    //     await expect(servicesHeading).toBeVisible();
    //     await expect(servicesHeading).toContainText('Elite Classes');

    //     // Wait for image cards to be registered
    //     const weightTrainingCard = page.getByText('Weight Training', { exact: true });
    //     await expect(weightTrainingCard).toBeVisible();
    // });

    // test('lead capture form exists and has required fields', async ({ page }) => {
    //     const formHeading = page.locator('#contact h2');
    //     await expect(formHeading).toBeVisible();

    //     // Form Elements
    //     const nameInput = page.locator('input#name');
    //     const phoneInput = page.locator('input#phone');
    //     const emailInput = page.locator('input#email');
    //     const submitBtn = page.locator('button#submit-btn');

    //     await expect(nameInput).toHaveAttribute('required', '');
    //     await expect(phoneInput).toHaveAttribute('required', '');
    //     await expect(submitBtn).toBeVisible();
    // });

    // test('mobile sticky bottom navigation is visible on mobile viewport', async ({ page, isMobile }) => {
    //     if (isMobile) {
    //         // Check if bottom nav links are present
    //         const callNav = page.locator('div.md\\:hidden.fixed.bottom-0').getByText('Call Now');
    //         const whatsappNav = page.locator('div.md\\:hidden.fixed.bottom-0').getByText('WhatsApp');

    //         await expect(callNav).toBeVisible();
    //         await expect(whatsappNav).toBeVisible();
    //     }
    // });

    test('booking modal opens when CTA is clicked', async ({ page }) => {
        const modal = page.locator('div[x-show="modalOpen"]').filter({ hasText: 'Claim Free Pass' }).first();
        const viewportWidth = page.viewportSize()?.width ?? 1280;
        const isMobileViewport = viewportWidth < 768;

        if (isMobileViewport) {
            // On mobile the desktop nav is hidden — open hamburger menu first
            const hamburgerBtn = page.locator('div.flex.md\\:hidden button').first();
            await hamburgerBtn.click();

            // Click the CTA inside the mobile menu overlay
            const mobileMenuCTA = page.locator('div[x-show="mobileMenuOpen"] button').filter({ hasText: 'Book Free Trial' });
            await mobileMenuCTA.click();
        } else {
            // On desktop the nav is visible — click its CTA button directly
            const desktopNavCTA = page.locator('nav.hidden.md\\:flex button').first();
            await desktopNavCTA.click();
        }

        // Modal should now be visible
        await expect(modal).toBeVisible();
    });
});

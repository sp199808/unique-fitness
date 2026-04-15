import { Page, Locator, expect } from '@playwright/test';

export class Homepage {
    readonly page: Page;
    readonly headerLogo: Locator;
    readonly classesLink: Locator;
    readonly facilitiesLink: Locator;
    readonly reviewsLink: Locator;
    readonly bookFreeTrialButton: Locator;

    constructor(page: Page) {
        this.page = page;
        this.headerLogo = page.getByRole('img', { name: 'Unique Fitness Logo' }).first();
        this.classesLink = page.getByRole('link', { name: 'Classes' }).first();
        this.facilitiesLink = page.getByRole('link', { name: 'Facilities' }).first();
        this.reviewsLink = page.getByRole('link', { name: 'Reviews' }).first();
        this.bookFreeTrialButton = page.getByRole('button', { name: 'Book Free Trial' }).first();
    }

    async checkLogoVisibility() {
        await expect(this.headerLogo).toBeVisible();
    }

    async checkDesktopMenuLinkVisibility() {
        await expect(this.headerLogo).toBeVisible();
        await expect(this.classesLink).toBeVisible();
        await expect(this.facilitiesLink).toBeVisible();
        await expect(this.reviewsLink).toBeVisible();
    }

}
import re
import time

import password
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_tz9(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1680,"height":1050})
    page = context.new_page()
    page.goto("https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home")
    page.locator('//*[@id="email"]').fill("evgeniykilochek@gmail.com")
    time.sleep(1)
    page.locator('//*[@id="email-container"]/div[2]/button').click()

    expect(page.locator("#password"))



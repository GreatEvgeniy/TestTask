import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_tz39(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1680, "height": 1050})
    page = context.new_page()
    page.goto("https://github.com/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_role("link", name="Do not share my personal information").click()




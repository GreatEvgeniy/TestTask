import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_tz34(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1680, "height": 1050})
    page = context.new_page()
    page.goto("https://github.com/")
    page.get_by_role("link", name="Manage cookies").click()


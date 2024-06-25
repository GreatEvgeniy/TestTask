import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_tz31(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1680,"height":1050})
    page = context.new_page()
    page.goto("https://github.com/")
    page.get_by_role("link", name="Sign up").click()
    time.sleep(2)
    page.get_by_role("contentinfo").get_by_label("Homepage").click()
    time.sleep(2)
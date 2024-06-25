import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_tz30(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1680,"height":1050})
    page = context.new_page()
    page.goto("https://github.com/")
    page.get_by_role("link", name="Sign up").click()
    time.sleep(3)
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="GitHub Privacy Statement").click()
    page1 = page1_info.value
    time.sleep(2)

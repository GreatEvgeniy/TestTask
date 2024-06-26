import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_tz29(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1680, "height": 1050})
    page = context.new_page()
    page.goto("https://github.com/")
    page.get_by_role("link", name="Sign up").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Terms of Service").click()
    page1 = page1_info.value

    expect(page).to_have_url("https://docs.github.com/ru/site-policy/")
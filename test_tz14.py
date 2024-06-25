import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_tz14(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1680,"height":1050})
    page = context.new_page()
    page.goto("https://github.com/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Enter your email*").click()
    page.get_by_label("Enter your email*").fill("evgeniykilochek@gmail.com")
    page.get_by_role("button", name="Continue").click()
    page.get_by_label("Create a password*").click()
    page.get_by_label("Create a password*").fill("😒😔🤗😳😭👍😏😆👌😊")
    time.sleep(2)



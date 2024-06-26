import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_tz27(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1680,"height":1050})
    page = context.new_page()
    page.goto("https://github.com/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Enter your email*").fill("умпутшн")
    page.get_by_label("Enter your email*").press("ControlOrMeta+a")
    page.get_by_label("Enter your email*").fill("evgeniykilochek@gmail.com")
    page.get_by_role("button", name="Continue").click()
    page.get_by_label("Create a password*").fill("Ww_06111991")
    page.get_by_role("button", name="Continue").click()
    page.get_by_label("Enter a username*").fill("Great-Evgeniy")
    page.get_by_role("button", name="Continue").click()
    page.get_by_label("Receive occasional product").check()
    time.sleep(2)
    page.get_by_role("button", name="Continue").click()

    expect(page.locator(".js-continue-button"))


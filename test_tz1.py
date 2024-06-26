import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_tz1(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1680,"height":1050})
    page = context.new_page()
    page.goto("https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home")
    page.get_by_role("banner").get_by_label("Homepage").click()
    time.sleep(2)

    expect(page).to_have_url("https://github.com/")





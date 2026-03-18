"""
Simple step definitions for BrowserStack + Playwright + Behave
"""

from behave import given, when, then
from playwright.sync_api import sync_playwright


@given('I launch the browser')
def step_launch_browser(context):
    """Launch Playwright browser - SDK patches this to use BrowserStack cloud"""
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch()
    context.page = context.browser.new_page()
    assert context.browser.is_connected(), "Browser should be connected"


@when('I navigate to "{url}"')
def step_navigate(context, url):
    """Navigate to a webpage"""
    context.page.goto(url, timeout=60000)


@then('the page title should contain "{text}"')
def step_verify_title(context, text):
    """Verify page title"""
    title = context.page.title()
    assert text in title, f"Expected '{text}' in title but got '{title}'"


@then('I close the browser')
def step_close_browser(context):
    """Close the browser and cleanup"""
    if hasattr(context, 'page') and context.page:
        context.page.close()
    if hasattr(context, 'browser') and context.browser:
        context.browser.close()
    if hasattr(context, 'playwright') and context.playwright:
        context.playwright.stop()


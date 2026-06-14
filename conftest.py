import allure
import pytest
from playwright.sync_api import Page
from pages.todo_page import TodoPage
import os
import platform

def pytest_configure(config):
    os.makedirs("allure-results", exist_ok=True)
    with open("allure-results/environment.properties", "w") as f:
        f.write(f"Environment=LOCAL\n")
        f.write(f"Browser=Chromium\n")
        f.write(f"Base.URL=https://demo.playwright.dev/todomvc\n")
        f.write(f"Python.Version={platform.python_version()}\n")
        f.write(f"Framework=Playwright + pytest\n")
        f.write(f"OS={platform.system()}\n")


@pytest.fixture()
def todo_page(page: Page) -> TodoPage:
    todo = TodoPage(page)
    todo.open()
    return todo


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page: Page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
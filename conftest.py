import allure
import pytest
from playwright.sync_api import Page
from pages.todo_page import TodoPage


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
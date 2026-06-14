from playwright.sync_api import Page
from pages.base_page import BasePage

class TodoPage(BasePage):
    URL = "https://demo.playwright.dev/todomvc"

    # Locators
    INPUT = ".new-todo"
    TODO_ITEMS = ".todo-list li"
    TODO_LABEL = ".todo-list li .view label"
    CHECKBOX = ".todo-list li .toggle"
    DELETE_BTN = ".todo-list li .destroy"
    FOOTER_COUNT = ".todo-count"
    FILTER_ACTIVE = "a[href='#/active']"
    FILTER_COMPLETED = "a[href='#/completed']"
    FILTER_ALL = "a[href='#/']"
    COMPLETED_ITEM = ".todo-list li.completed"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.navigate(self.URL)

    def add_todo(self, text: str):
        self.fill(self.INPUT, text)
        self.page.keyboard.press("Enter")

    def complete_todo(self, index: int = 0):
        self.page.locator(self.CHECKBOX).nth(index).click()

    def delete_todo(self, index: int = 0):
        item = self.page.locator(self.TODO_ITEMS).nth(index)
        item.hover()
        self.page.locator(self.DELETE_BTN).nth(index).click()

    def get_todo_count(self) -> int:
        return self.count(self.TODO_ITEMS)

    def get_todo_text(self, index: int = 0) -> str:
        return self.page.locator(self.TODO_LABEL).nth(index).inner_text()

    def get_footer_count_text(self) -> str:
        return self.get_text(self.FOOTER_COUNT)

    def filter_active(self):
        self.click(self.FILTER_ACTIVE)
        self.page.wait_for_timeout(500)

    def filter_completed(self):
        self.click(self.FILTER_COMPLETED)
        self.page.wait_for_timeout(500)

    def filter_all(self):
        self.click(self.FILTER_ALL)
        self.page.wait_for_timeout(500)

    def get_completed_count(self) -> int:
        return self.count(self.COMPLETED_ITEM)

    def edit_todo(self, index: int, new_text: str):
        item = self.page.locator(self.TODO_LABEL).nth(index)
        item.dblclick()
        edit_input = self.page.locator(".todo-list li.editing .edit")
        edit_input.fill(new_text)
        self.page.keyboard.press("Enter")
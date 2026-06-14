import allure
import pytest
from allure import severity_level
from pages.todo_page import TodoPage


@allure.epic("Todo Application")
@allure.feature("Todo Management")
class TestTodo:

    @allure.title("User can add a single todo item")
    @allure.description("Verify that a user can add a todo item and it appears in the list with correct count")
    @allure.severity(severity_level.CRITICAL)
    @allure.story("Add Todo")
    def test_add_single_todo(self, todo_page: TodoPage):
        with allure.step("Add a todo item - Buy groceries"):
            todo_page.add_todo("Buy groceries")

        with allure.step("Verify todo count is 1"):
            assert todo_page.get_todo_count() == 1

        with allure.step("Verify todo text is correct"):
            assert todo_page.get_todo_text(0) == "Buy groceries"

        with allure.step("Verify footer shows 1 item left"):
            assert "1 item left" in todo_page.get_footer_count_text()

    @allure.title("User can complete a todo item")
    @allure.description("Verify that clicking the checkbox marks a todo as completed and updates the footer count")
    @allure.severity(severity_level.CRITICAL)
    @allure.story("Complete Todo")
    def test_complete_a_todo(self, todo_page: TodoPage):
        with allure.step("Add a todo item - Read a book"):
            todo_page.add_todo("Read a book")

        with allure.step("Complete the todo item"):
            todo_page.complete_todo(0)

        with allure.step("Verify item is marked as completed"):
            assert todo_page.get_completed_count() == 1

        with allure.step("Verify footer shows 0 items left"):
            assert "0 items left" in todo_page.get_footer_count_text()

    @allure.title("User can delete a todo item")
    @allure.description("Verify that hovering and clicking delete removes the todo item from the list")
    @allure.severity(severity_level.NORMAL)
    @allure.story("Delete Todo")
    def test_delete_a_todo(self, todo_page: TodoPage):
        with allure.step("Add a todo item - Watch a movie"):
            todo_page.add_todo("Watch a movie")

        with allure.step("Verify todo was added successfully"):
            assert todo_page.get_todo_count() == 1

        with allure.step("Delete the todo item"):
            todo_page.delete_todo(0)

        with allure.step("Verify todo list is now empty"):
            assert todo_page.get_todo_count() == 0

    @allure.title("User can filter todos by Active and Completed")
    @allure.description("Verify that Active filter shows incomplete todos and Completed filter shows done todos")
    @allure.severity(severity_level.NORMAL)
    @allure.story("Filter Todo")
    def test_filter_active_and_completed(self, todo_page: TodoPage):
        with allure.step("Add 3 todo items"):
            todo_page.add_todo("Task One")
            todo_page.add_todo("Task Two")
            todo_page.add_todo("Task Three")

        with allure.step("Complete the first todo item"):
            todo_page.complete_todo(0)

        with allure.step("Apply Active filter and verify 2 items visible"):
            todo_page.filter_active()
            assert todo_page.get_todo_count() == 1 #failing it delibrately to check allure report for failed test case

        with allure.step("Apply Completed filter and verify 1 item visible"):
            todo_page.filter_completed()
            assert todo_page.get_todo_count() == 1

        with allure.step("Apply All filter and verify all 3 items visible"):
            todo_page.filter_all()
            assert todo_page.get_todo_count() == 3

    @allure.title("User can edit an existing todo item")
    @allure.description("Verify that double clicking a todo allows editing and saves the updated text")
    @allure.severity(severity_level.MINOR)
    @allure.story("Edit Todo")
    def test_edit_a_todo(self, todo_page: TodoPage):
        with allure.step("Add a todo item - Original Text"):
            todo_page.add_todo("Original Text")

        with allure.step("Verify original text is displayed"):
            assert todo_page.get_todo_text(0) == "Original Text"

        with allure.step("Double click to edit and type new text"):
            todo_page.edit_todo(0, "Updated Text")

        with allure.step("Verify updated text is saved correctly"):
            assert todo_page.get_todo_text(0) == "Updated Text"
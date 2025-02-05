from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from behave import when

@when('I select "{option}" from the dropdown')
def select_dropdown_option(context, option):
    dropdown = Select(context.driver.find_element(By.NAME, "my-select"))
    dropdown.select_by_visible_text(option)

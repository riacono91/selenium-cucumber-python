from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then

@when('I enter "{text}" in the text field')
def enter_text(context, text):
    text_field = context.driver.find_element(By.ID, "my-text-id")
    text_field.clear()
    text_field.send_keys(text)

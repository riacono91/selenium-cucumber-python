from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('I open the login page')
def open_login_page(context):
    context.driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    context.driver.maximize_window()

@when('I enter valid credentials')
def enter_valid_credentials(context):
    context.driver.find_element(By.ID, "my-text-id").send_keys("testuser")
    context.driver.find_element(By.NAME, "my-password").send_keys("password123")

@when("I submit the form")
def submit_form(context):
    context.driver.find_element(By.CSS_SELECTOR, "button").click()

@then('I should see the confirmation message "{expected_message}"')
def verify_confirmation_message(context, expected_message):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    actual_message = context.driver.find_element(By.TAG_NAME, "h1").text
    assert actual_message == expected_message, f"Expected '{expected_message}', but got '{actual_message}'"

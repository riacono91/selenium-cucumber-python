from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from features.utils import fill_input

@given('I open the login page of a new link')
def open_login_page2(context):
    context.driver.get("https://the-internet.herokuapp.com/login")

@when('I enter valid credentials of a new link')
def enter_valid_credentials2(context):
    fill_input(context.driver, By.ID, "username", "tomsmith")
    fill_input(context.driver, By.ID, "password", "SuperSecretPassword!")

@when('I submit the login form')
def submit_form2(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
  
@then('I should see the alert with the message "{expected_message}"')
def verify_alert_message(context, expected_message):
    # Aspetta che il messaggio sia visibile
    flash = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    actual_message = flash.text.strip()
    assert expected_message in actual_message, f"Expected '{expected_message}', but got '{actual_message}'"

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "username").clear()
    context.driver.find_element(By.ID, "username").send_keys(username)
    context.driver.find_element(By.NAME, "password").clear()
    context.driver.find_element(By.NAME, "password").send_keys(password)

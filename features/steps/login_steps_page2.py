from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('I open the login page of a new link')
def open_login_page2(context):
    print("[STEP] Opening login page")
    context.driver.get("https://the-internet.herokuapp.com/login")

@when('I enter valid credentials of a new link')
def enter_valid_credentials2(context):
    print("[STEP] Entering username and password")
    context.driver.find_element(By.ID, "username").send_keys("tomsmith")
    context.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    print("[INFO] Credentials entered")

@when('I submit the login form')
def submit_form2(context):
    print("[STEP] Submitting login form")
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print("[INFO] Form submitted")

@then('I should see the alert with the message "{expected_message}"')
def verify_alert_message(context, expected_message):
    print("[STEP] Verifying message on page instead of alert")
    # Aspetta che il messaggio sia visibile
    flash = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    actual_message = flash.text.strip()
    print(f"[INFO] Flash message: '{actual_message}'")
    assert expected_message in actual_message, f"Expected '{expected_message}', but got '{actual_message}'"

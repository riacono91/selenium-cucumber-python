from selenium.webdriver.common.by import By
from behave import when

@when('I select the radio button "{radio_option}"')
def select_radio_button(context, radio_option):
    radios = context.driver.find_elements(By.NAME, "my-radio")
    for radio in radios:
        if radio.get_attribute("value") == radio_option:
            radio.click()
            break

from selenium.webdriver.common.by import By

def fill_input(driver, locator_type, locator, value):
    element = driver.find_element(locator_type, locator)
    element.clear()
    element.send_keys(value)

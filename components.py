from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

def wait_and_click(driver, timeout, ui_selector_str):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
        )
    )
    element.click()
    return element

def wait_until_present(driver, timeout, ui_selector_str):
    wait = WebDriverWait(driver, timeout)
    return wait.until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
        )
    )

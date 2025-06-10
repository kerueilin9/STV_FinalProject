from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

def _get_locator_strategy(selector_str):
    """自動判斷選擇器類型並返回對應的定位策略"""
    if selector_str.startswith('//') or selector_str.startswith('/'):
        # XPath 選擇器
        return AppiumBy.XPATH, selector_str
    else:
        # UiSelector 選擇器
        return AppiumBy.ANDROID_UIAUTOMATOR, selector_str

def wait_and_click(driver, timeout, selector_str):
    """支援 UiSelector 和 XPath 的點擊函數"""
    wait = WebDriverWait(driver, timeout)
    locator_by, locator_value = _get_locator_strategy(selector_str)
    element = wait.until(
        EC.element_to_be_clickable(
            (locator_by, locator_value)
        )
    )
    element.click()
    return element

def wait_until_present(driver, timeout, selector_str):
    """支援 UiSelector 和 XPath 的元素等待函數"""
    wait = WebDriverWait(driver, timeout)
    locator_by, locator_value = _get_locator_strategy(selector_str)
    return wait.until(
        EC.presence_of_element_located(
            (locator_by, locator_value)
        )
    )

# coding: utf-8
# ATC33.py

import unittest


from appium import webdriver
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# with open("capabilities.json", "r", encoding="utf-8") as f:
#     capabilities = eval(f.read())
#     capabilities = dict((k if k[:7] != "appium:" else k[7:], v)
#                         for (k, v) in capabilities.items())
#     capabilities["deviceName"] = "Android"

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.money.smoney_android',
    appActivity='com.money.smoney_android.ui.splash.SplashActivity',
    language='zh',
    locale='TW'
)
appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_zeroValue(self):
        def wait_and_click(ui_selector_str, timeout=5) -> WebElement:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
                    )
                )
                element.click()
                return element
            except Exception as e:
                print(e)

        def wait_until_present(ui_selector_str, timeout=5) -> WebElement:
            try:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(
                        (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
                    )
                )
            except Exception as e:
                print(e)

        # 等待應用程式啟動
        wait_and_click('new UiSelector().text("簡單記帳")')

        # 點擊「不用同步，直接開始」
        wait_and_click('new UiSelector().text("不用同步，直接開始")')

        # 如果有 Cancel 按鈕就點掉
        wait_and_click('new UiSelector().text("Cancel")')

        # 如果有開啟通知
        wait_and_click('new UiSelector().description("向上瀏覽")')

        # 點擊「新增」按鈕
        wait_and_click(
            'new UiSelector().className("android.widget.Button").instance(0)')
        wait_and_click(
            'new UiSelector().className("android.widget.Button").instance(4)')

        # 點擊輸入備註
        if e := wait_until_present('new UiSelector().className("android.widget.EditText")'):
            e.send_keys("")

        # 再點 OK
        wait_and_click(
            'new UiSelector().className("android.view.View").instance(22)')

    def test_extremelyLargeValue(self):
        def wait_and_click(ui_selector_str, timeout=5) -> WebElement:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
                    )
                )
                element.click()
                return element
            except Exception as e:
                print(e)

        def wait_until_present(ui_selector_str, timeout=5) -> WebElement:
            try:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(
                        (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
                    )
                )
            except Exception as e:
                print(e)

        # 等待應用程式啟動
        wait_and_click('new UiSelector().text("簡單記帳")')

        # 點擊「不用同步，直接開始」
        wait_and_click('new UiSelector().text("不用同步，直接開始")')

        # 如果有 Cancel 按鈕就點掉
        wait_and_click('new UiSelector().text("Cancel")')

        # 如果有開啟通知
        wait_and_click('new UiSelector().description("向上瀏覽")')

        # 點擊「新增」按鈕
        wait_and_click(
            'new UiSelector().className("android.widget.Button").instance(0)')
        wait_and_click(
            'new UiSelector().className("android.widget.Button").instance(4)')

        # 點擊輸入備註
        if e := wait_until_present('new UiSelector().className("android.widget.EditText")'):
            e.send_keys("")

        # 再點 OK
        wait_and_click(
            'new UiSelector().className("android.view.View").instance(22)')

    def test_excessiveDecimalPlaces(self):
        def wait_and_click(ui_selector_str, timeout=5) -> WebElement:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
                    )
                )
                element.click()
                return element
            except Exception as e:
                print(e)

        def wait_until_present(ui_selector_str, timeout=5) -> WebElement:
            try:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(
                        (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
                    )
                )
            except Exception as e:
                print(e)

        # 等待應用程式啟動
        wait_and_click('new UiSelector().text("簡單記帳")')

        # 點擊「不用同步，直接開始」
        wait_and_click('new UiSelector().text("不用同步，直接開始")')

        # 如果有 Cancel 按鈕就點掉
        wait_and_click('new UiSelector().text("Cancel")')

        # 如果有開啟通知
        wait_and_click('new UiSelector().description("向上瀏覽")')

        # 點擊「新增」按鈕
        wait_and_click(
            'new UiSelector().className("android.widget.Button").instance(0)')
        wait_and_click(
            'new UiSelector().className("android.widget.Button").instance(4)')

        # 點擊輸入備註
        if e := wait_until_present('new UiSelector().className("android.widget.EditText")'):
            e.send_keys("")

        # 再點 OK
        wait_and_click(
            'new UiSelector().className("android.view.View").instance(22)')

    def test_blankInput(self):
        def wait_and_click(ui_selector_str, timeout=5) -> WebElement:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
                    )
                )
                element.click()
                return element
            except Exception as e:
                print(e)

        def wait_until_present(ui_selector_str, timeout=5) -> WebElement:
            try:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(
                        (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
                    )
                )
            except Exception as e:
                print(e)

        # 等待應用程式啟動
        wait_and_click('new UiSelector().text("簡單記帳")')

        # 點擊「不用同步，直接開始」
        wait_and_click('new UiSelector().text("不用同步，直接開始")')

        # 如果有 Cancel 按鈕就點掉
        wait_and_click('new UiSelector().text("Cancel")')

        # 如果有開啟通知
        wait_and_click('new UiSelector().description("向上瀏覽")')

        # 點擊「新增」按鈕
        wait_and_click(
            'new UiSelector().className("android.widget.Button").instance(0)')
        wait_and_click(
            'new UiSelector().className("android.widget.Button").instance(4)')

        # 點擊輸入備註
        if e := wait_until_present('new UiSelector().className("android.widget.EditText")'):
            e.send_keys("")

        # 再點 OK
        wait_and_click(
            'new UiSelector().className("android.view.View").instance(22)')

    def test_overlyLongInput(self):
        def wait_and_click(ui_selector_str, timeout=5) -> WebElement:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
                    )
                )
                element.click()
                return element
            except Exception as e:
                print(e)

        def wait_until_present(ui_selector_str, timeout=5) -> WebElement:
            try:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(
                        (AppiumBy.ANDROID_UIAUTOMATOR, ui_selector_str)
                    )
                )
            except Exception as e:
                print(e)

        # 等待應用程式啟動
        wait_and_click('new UiSelector().text("簡單記帳")')

        # 點擊「不用同步，直接開始」
        wait_and_click('new UiSelector().text("不用同步，直接開始")')

        # 如果有 Cancel 按鈕就點掉
        wait_and_click('new UiSelector().text("Cancel")')

        # 如果有開啟通知
        wait_and_click('new UiSelector().description("向上瀏覽")')

        # 點擊「新增」按鈕
        wait_and_click(
            'new UiSelector().className("android.widget.Button").instance(0)')
        wait_and_click(
            'new UiSelector().className("android.widget.Button").instance(4)')

        # 點擊輸入備註
        if e := wait_until_present('new UiSelector().className("android.widget.EditText")'):
            e.send_keys("a"*10**4)

        # 再點 OK
        wait_and_click(
            'new UiSelector().className("android.view.View").instance(22)')


if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        print(e)

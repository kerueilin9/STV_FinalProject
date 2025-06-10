# test_add_button.py
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

from components import wait_and_click, wait_until_present

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.money.smoney_android',
    appActivity='com.money.smoney_android.ui.splash.SplashActivity',
    language='zh',
    locale='CN'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_click_add_button(self):
        # 點擊「不用同步，直接開始」
        wait_and_click(self.driver, 20, 'new UiSelector().text("不用同步，直接開始")')

        # 如果有 Cancel 按鈕就點掉
        try:
            wait_and_click(self.driver, 5, 'new UiSelector().text("Cancel")')   
        except Exception:
            print("Cancel button not found")

        # 點擊「新增」按鈕
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.widget.Button").instance(0)')

        time.sleep(0.5)

        # 點擊 OK 鈕
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.view.View").instance(22)')

        # 點擊 Zoom out 鈕
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.widget.Button").instance(2)')
        
        # 輸入數字
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.view.View").instance(12)')  # 9
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.view.View").instance(11)')  # 0

        # 再點 OK
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.view.View").instance(22)')
        
        time.sleep(0.5)
        wait_and_click(self.driver, 5, 'new UiSelector().text("早餐")')
        wait_and_click(self.driver, 5, 'new UiSelector().text("交通")')
        # 再點 OK
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.view.View").instance(22)')

if __name__ == '__main__':
    unittest.main()

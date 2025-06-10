import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from appium.webdriver.common.appiumby import AppiumBy

from components import wait_and_click, wait_until_present

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.money.smoney_android',
    appActivity='com.money.smoney_android.ui.splash.SplashActivity',
    language='zh',
    locale='CN',
)

appium_server_url = 'http://localhost:4723'

class TestUpdateCategory(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_update_category(self):
        # 點擊「不用同步，直接開始」
        wait_and_click(self.driver, 20, 'new UiSelector().text("不用同步，直接開始")')

        # 如果有 Cancel 按鈕就點掉
        try:
            wait_and_click(self.driver, 5, 'new UiSelector().text("取消")')
        except Exception:
            print("Cancel button not found")

        # 點擊「新增」按鈕
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.widget.Button").instance(0)')

        time.sleep(0.5)

        # 點擊 OK 鈕
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.view.View").instance(22)')

        # 點擊 Zoom out 鈕
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.widget.Button").instance(2)')
        time.sleep(0.5)
        time.sleep(0.5)
        # 輸入數字
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.view.View").instance(12)')  # 9
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.view.View").instance(11)')  # 0

        # 再點 OK
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.view.View").instance(22)')
        time.sleep(0.5)

        # 點擊第一筆帳務
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.view.View").instance(2)')
        
        # 點擊「刪除」按鈕
        self.driver.find_element("xpath", '//*[@bounds="[1124,168][1268,312]"]').click()

        

        # 再點 確認刪除
        wait_and_click(self.driver, 20, 'new UiSelector().text("確認刪除")')

        time.sleep(1)  # 等待變更生效

if __name__ == '__main__':
    unittest.main()
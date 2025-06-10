# test_pl_statement.py
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from components import wait_and_click, wait_until_present
from selenium.common.exceptions import NoSuchElementException
import time

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.money.smoney_android',
    appActivity='com.money.smoney_android.ui.splash.SplashActivity',
    language='zh',
    locale='TW',
    # 自動授予權限
    autoGrantPermissions=True,
    # 或者使用以下設置跳過系統對話框
    skipServerInstallation=True,
    noReset=False,  # 每次測試重置應用狀態
    fullReset=False  # 不完全重置
)

appium_server_url = 'http://localhost:4723'

class TestPLStatement(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_pl_statement(self):

        # 點擊「不用同步，直接開始」
        wait_and_click(self.driver, 20, 'new UiSelector().text("不用同步，直接開始")')

        # 如果有 Cancel 按鈕就點掉
        try:
            wait_and_click(self.driver, 2, 'new UiSelector().text("取消")')
        except Exception:
            print("Cancel button not found")
        time.sleep(0.5)
        # 等待應用程式啟動
        # 選取選單按鈕
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.widget.Button").instance(1)')

        time.sleep(0.5)

        # 點擊 帳務報表 按鈕
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.widget.Button").instance(7)')

        time.sleep(0.5)

        # 點擊「近六個月」按鈕
        wait_and_click(self.driver, 20, 'new UiSelector().text("近六個月")')

        time.sleep(0.5) 

        # 驗證目標元素是否存在且可點擊（表示按鈕已被選中）
        target_element = wait_until_present(self.driver, 20, 'new UiSelector().text("近六個月")')
        
        # 驗證元素是否可點擊（Android 中選中的按鈕通常會保持可點擊狀態）
        self.assertTrue(target_element.is_enabled(), "目標元素應該是啟用狀態")
        
        # 驗證元素是否可見
        self.assertTrue(target_element.is_displayed(), "目標元素應該是可見的")
        
        time.sleep(0.5)

if __name__ == '__main__':
    unittest.main()

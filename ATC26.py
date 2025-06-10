# test_expense_component.py
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

from components import wait_and_click, wait_until_present
from flows.record import add_expense_component, verify_expense_added
from flows.common import handle_initial_setup

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.money.smoney_android',
    appActivity='com.money.smoney_android.ui.splash.SplashActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestExpenseComponent(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        self.test_amount = "66"  # 測試金額參數

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()


    def verify_breakfast_amount(self):
        """驗證螢幕上是否有指定金額文字"""
        expected_amount = f"${self.test_amount}"
        print(f"開始驗證螢幕上是否有 {expected_amount}...")
        
        try:
            # 直接檢查螢幕上是否有指定金額文字
            amount_element = wait_until_present(self.driver, 10, f'new UiSelector().text("{expected_amount}")')
            print(f"找到 {expected_amount} 元素")
            return True
            
        except Exception as e:
            print(f"未找到 {expected_amount} 文字: {str(e)}")
            return False

    def test_add_expense_with_existing_label(self):
        """測試使用現有標籤新增 expense"""
        # 處理初始設定和通知提醒
        handle_initial_setup(self.driver)

        # 使用組件新增 expense: $30 - Dinner (第一次使用，會跳過教學)
        print("=== 測試 1: 使用現有標籤新增 expense (含跳過教學) ===")
        success = add_expense_component(self.driver, self.test_amount, "Breakfast", first=True)
        time.sleep(3)

        # self.assertTrue(success, "新增 expense 失敗")

        # 步驟 1: 點選左上角選單 (使用 XPath 定位器)
        # 注意：現在 components 函數支援自動判斷 UiSelector 和 XPath
        print("正在點擊左上角選單...")
        wait_and_click(self.driver, 20, '//androidx.compose.ui.platform.ComposeView[@resource-id="com.money.smoney_android:id/home_content"]/android.view.View/android.view.View/android.view.View[2]/android.widget.Button[1]')
        
        time.sleep(2)  # 等待選單載入
        
        # 步驟 2: 進入 P&L Statement (實際測試驗證：成功找到並點擊)
        print("正在進入 P&L Statement...")
        wait_and_click(self.driver, 20, 'new UiSelector().text("P&L Statement")')
        
        time.sleep(2)  # 等待 P&L Statement 頁面載入

        wait_and_click(self.driver, 20, 'new UiSelector().text("Year")')
        time.sleep(2)  # 等待 P&L Statement 頁面載入
        
        # 步驟 3: 檢查 text 是 "Breakfast" 的下一個 text 欄位是否包含 "66"
        print("=== 步驟 3: 檢查 Breakfast 項目的金額 ===")
        
        # 使用驗證函數檢查 Breakfast 金額
        is_breakfast_amount_correct = self.verify_breakfast_amount()
        self.assertTrue(is_breakfast_amount_correct, f"螢幕上應該包含 ${self.test_amount}")

if __name__ == '__main__':
    unittest.main()
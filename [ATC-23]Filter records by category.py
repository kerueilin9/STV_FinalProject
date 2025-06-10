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
    locale='CN',
    # 自動授予權限
    autoGrantPermissions=True,
    # 或者使用以下設置跳過系統對話框
    skipServerInstallation=True,
    noReset=False,  # 每次測試重置應用狀態
    fullReset=False  # 不完全重置
)

appium_server_url = 'http://127.0.0.1:4723'

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
            wait_and_click(self.driver, 5, 'new UiSelector().text("取消")')
        except Exception:
            print("Cancel button not found")
        time.sleep(0.5)

        # 等待應用程式啟動
        # 選取選單按鈕
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.widget.Button").instance(1)')
        time.sleep(0.5)

        # 點擊 搜尋圖示 按鈕
        wait_and_click(self.driver, 20, 'new UiSelector().className("android.widget.Button").instance(5)')
        time.sleep(0.5)

        # 點擊 篩選工具
        wait_and_click(self.driver, 20, 'com.money.smoney_android:id/iv_coolicon')
        time.sleep(0.5)

        # 點擊 篩選工具
        wait_and_click(self.driver, 20, 'com.money.smoney_android:id/iv_coolicon')
        time.sleep(0.5)

        # 點擊 支出分類 
        wait_and_click(self.driver, 20, 'com.money.smoney_android:id/tv_expense_category_choose')
        time.sleep(0.5)

        # 選擇 支出分類 
        # 點擊「午餐」
        wait_and_click(self.driver, 20, 'new UiSelector().text("午餐")')
        time.sleep(0.5)
        # 點擊「晚餐」
        wait_and_click(self.driver, 20, 'new UiSelector().resourceId("com.money.smoney_android:id/iv_bg").instance(2)')
        time.sleep(0.5)

        # 點擊 收入分類
        wait_and_click(self.driver, 20, 'com.money.smoney_android:id/tv_income_category_choose')
        time.sleep(0.5)
        
        # 選擇 收入分類
        # 點擊「薪水」
        wait_and_click(self.driver, 20, 'new UiSelector().resourceId("com.money.smoney_android:id/iv_bg").instance(0)')
        time.sleep(0.5)

        # 驗證目標圖示變換
        target_element = wait_until_present(self.driver, 20, 'com.money.smoney_android:id/ivNotFind')
        
        # 驗證目標圖示不是未搜尋的圖示
        self.assertNotEqual(target_element, 'com.money.smoney_android:id/ivNoSearch')
        time.sleep(0.5)

if __name__ == '__main__':
    unittest.main()

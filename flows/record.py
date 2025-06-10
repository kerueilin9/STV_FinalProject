# expense_component.py
import time
from components import wait_and_click, wait_until_present

def add_expense_component(driver, amount, label, first=False, timeout=20):
    """
    新增 expense 組件
    
    參數:
    - driver: Appium webdriver 實例
    - amount: 要輸入的金額數字 (字串格式，例如 "25" 或 "100")
    - label: 標籤名稱 (字串格式，例如 "Lunch" 或 "Coffee")
    - first: 是否為第一次使用 (True 時會跳過教學)
    - timeout: 等待超時時間
    
    功能:
    1. 如果 first=True，在畫面中間按兩下跳過教學
    2. 輸入數字 (使用按鈕輸入數字)
    3. 選擇標籤 (先尋找該標籤有沒有在螢幕上，有則點擊，沒有則在標籤欄位輸入文字)
    4. 按下 OK 按鍵
    """
    
    print(f"開始新增 expense: 金額=${amount}, 標籤={label}, 第一次使用={first}")
    
    # 點擊新增按鈕 (根據實際測試，使用座標定位更可靠)
    print("正在點擊新增按鈕...")
    try:
        # 先嘗試用常見的新增按鈕定位方式
        wait_and_click(driver, 5, 'new UiSelector().className("android.widget.Button").instance(0)')
    except Exception:
        # 如果找不到，使用座標點擊 (540, 2220 為實際測試驗證的新增按鈕位置)
        print("使用座標點擊新增按鈕")
        driver.tap([(540, 2220)], 500)
    time.sleep(1)

    # 如果是第一次使用，先跳過教學
    if first:
        time.sleep(5)
        print("正在跳過教學...")
        # 獲取螢幕尺寸來計算中心點
        screen_size = driver.get_window_size()
        center_x = screen_size['width'] // 2
        center_y = screen_size['height'] // 2
        
        print(f"螢幕尺寸: {screen_size['width']}x{screen_size['height']}, 中心點: ({center_x}, {center_y})")
        
        # 在畫面中間按兩下，間隔2秒
        print("第一次點擊螢幕中間...")
        driver.tap([(center_x, center_y)], 500)
        time.sleep(2)
        
        print("第二次點擊螢幕中間...")
        driver.tap([(center_x, center_y)], 500)
        time.sleep(1)
        
        print("教學跳過完成")
    
    # 步驟 1: 輸入數字 (使用按鈕輸入數字)
    print(f"正在輸入金額: {amount}")
    
    # 數字按鈕的座標對應
    number_coordinates = {
        '0': (313, 2189),
        '1': (102, 1998),
        '2': (313, 1998),
        '3': (524, 1998),
        '4': (102, 1807),
        '5': (313, 1807),
        '6': (524, 1807),
        '7': (102, 1616),
        '8': (313, 1616),
        '9': (524, 1616),
        '.': (532, 2189)
    }
    
    # 逐個點擊數字按鈕
    for digit in amount:
        if digit in number_coordinates:
            # x, y = number_coordinates[digit]
            wait_and_click(driver, timeout, f'new UiSelector().text("{digit}")')
            time.sleep(0.5)  # 短暫延遲確保輸入被識別
    
    print(f"金額輸入完成: ${amount}")
    
    # 步驟 2: 選擇標籤
    # print(f"正在尋找標籤: {label}")
    
    # # 先檢查標籤是否在螢幕上的預設標籤中
    # try:
    #     # 嘗試找到並點擊現有的標籤
    #     label_element = wait_until_present(driver, 5, f'new UiSelector().text("{label}")')
    #     label_element.click()
    #     print(f" 找到並選擇了現有標籤: {label}")
        
    # except Exception:
    #     print(f" 未找到現有標籤 '{label}'，將新增自定義標籤")
        
    #     # 如果找不到現有標籤，點擊 "Add" 按鈕新增自定義標籤
    #     try:
    #         wait_and_click(driver, timeout, 'new UiSelector().text("Add")')
    #         time.sleep(1)
            
    #         # 在輸入欄位中輸入標籤名稱
    #         input_field = wait_until_present(driver, timeout, 'new UiSelector().className("android.widget.EditText")')
    #         input_field.clear()
    #         input_field.send_keys(label)
            
    #         # 選擇分類 (預設選擇 "Food & drink")
    #         wait_and_click(driver, timeout, 'new UiSelector().text("Food & drink")')
            
    #         # 點擊 Confirm 確認新增標籤
    #         wait_and_click(driver, timeout, 'new UiSelector().text("Confirm")')
    #         time.sleep(1)
            
    #         print(f" 成功新增自定義標籤: {label}")
            
    #     except Exception as e:
    #         print(f" 新增自定義標籤失敗: {str(e)}")
    #         # 如果新增失敗，使用預設標籤 "Breakfast"
    #         wait_and_click(driver, timeout, 'new UiSelector().text("Breakfast")')
    #         print(" 使用預設標籤: Breakfast")
    
    # 步驟 3: 按下 OK 按鍵
    print("正在確認新增...")
    wait_and_click(driver, timeout, 'new UiSelector().text("OK")')
    time.sleep(2)  # 等待頁面返回主畫面
    
    print(f"成功新增 expense: ${amount} - {label}")
    return True

def verify_expense_added(driver, amount, label, timeout=10):
    """
    驗證 expense 是否成功新增
    
    參數:
    - driver: Appium webdriver 實例
    - amount: 預期的金額
    - label: 預期的標籤
    - timeout: 等待超時時間
    
    回傳:
    - True: 如果找到對應的 expense 記錄
    - False: 如果未找到
    """
    try:
        # 尋找標籤文字
        label_element = wait_until_present(driver, timeout, f'new UiSelector().text("{label}")')
        
        # 尋找金額文字 (可能是 $-amount 格式)
        amount_text = f"$-{amount}"
        amount_element = wait_until_present(driver, timeout, f'new UiSelector().text("{amount_text}")')
        
        print(f" 驗證成功: 找到 expense 記錄 {label} - {amount_text}")
        return True
        
    except Exception as e:
        print(f" 驗證失敗: 未找到 expense 記錄 {label} - ${amount}")
        print(f"錯誤詳情: {str(e)}")
        return False

# 使用範例
if __name__ == "__main__":
    # 這裡需要有 driver 實例
    
    # 第一次使用 (會跳過教學)
    # add_expense_component(driver, "25", "Lunch", first=True)
    
    # 一般使用
    # add_expense_component(driver, "25", "Lunch")
    # add_expense_component(driver, "30", "Coffee", first=False)
    
    # 驗證記錄
    # verify_expense_added(driver, "25", "Lunch")
    pass
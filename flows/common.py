"""
共用的測試流程函數模組
包含可重複使用的設定和工具函數
"""
import time
import base64
from PIL import Image
import io
from components import wait_and_click, wait_until_present


def handle_initial_setup(driver):
    """處理應用初始設定和各種彈窗提醒"""
    print("正在處理應用初始設定...")
    
    # 1. 處理「不用同步，直接開始」
    try:
        wait_and_click(driver, 10, 'new UiSelector().text("不用同步，直接開始")')
        print("點擊了「不用同步，直接開始」")
    except Exception:
        print("未找到同步提示，可能已跳過")

    time.sleep(1)

    # 2. 處理通知權限提醒 - 點擊 Navigate up 按鈕
    try:
        wait_and_click(driver, 5, 'new UiSelector().className("android.widget.ImageButton").description("Navigate up")')
        print("點擊了 Navigate up 按鈕，關閉權限設定")
        time.sleep(1)
                
    except Exception:
        print("未找到 Navigate up 按鈕，嘗試其他方式處理通知提醒")

    time.sleep(1)

    # 3. 處理 Cancel 按鈕
    try:
        wait_and_click(driver, 5, 'new UiSelector().text("Cancel")')
        print("點擊了 Cancel 按鈕")
    except Exception:
        print("未找到 Cancel 按鈕")

    time.sleep(1)

    print("初始設定處理完成")


def get_pixel_color_at_coordinates(driver, x, y):
    """取得指定座標點的顏色值"""
    try:
        # 取得螢幕截圖
        screenshot_base64 = driver.get_screenshot_as_base64()
        
        # 將 base64 轉換為 PIL Image
        screenshot_data = base64.b64decode(screenshot_base64)
        image = Image.open(io.BytesIO(screenshot_data))
        
        # 取得指定座標的顏色 (RGB)
        pixel_color = image.getpixel((x, y))
        
        return pixel_color
        
    except Exception as e:
        print(f"取得座標 ({x}, {y}) 顏色時發生錯誤: {str(e)}")
        return None
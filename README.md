# Appium 自動化測試專案

這是一個使用 Python 和 Appium 框架針對 Android 應用程式進行自動化測試的專案。

## 專案概述

本專案主要測試「Smoney Android」應用程式的功能，包括：

- 應用程式啟動流程
- 新增按鈕功能測試
- UI 元素互動測試

## 專案結構

```
├── ATC01.py              # 主要測試案例 - 新增按鈕功能測試
├── ATC02.py              # 次要測試案例 - 應用程式互動測試
├── test.py               # 基礎測試檔案 - Android 設定應用測試
├── components.py         # 共用元件函數庫
├── test.json            # Appium 配置檔案
├── requirements.txt     # Python 依賴套件清單
└── README.md           # 專案說明文件
```

## 環境需求

### 軟體需求

- Python 3.8 或更高版本
- Node.js 14 或更高版本
- Android SDK
- Appium Server 2.0+
- Android 模擬器或實體裝置

### Python 依賴套件

- `appium-python-client >= 3.0.0`
- `selenium >= 4.15.0`
- `websocket-client >= 1.6.4`

## 安裝步驟

### 1. 安裝 Python 依賴套件

```bash
pip install -r requirements.txt
```

### 2. 安裝 Appium Server

```bash
npm install -g appium
appium driver install uiautomator2
```

### 3. 設定 Android 環境

- 確保 Android SDK 已安裝
- 設定 ANDROID_HOME 環境變數
- 啟動 Android 模擬器或連接實體裝置

## 使用方法

### 1. 啟動 Appium Server

```bash
appium --port 4723
appium --use-plugins=inspector --allow-cors
```

### 2. 執行測試

#### 執行主要測試案例 (ATC01)

```bash
python ATC01.py

```

#### 執行次要測試案例 (ATC02)

```bash
python ATC02.py
```

#### 執行基礎測試

```bash
python test.py
```

## 測試案例說明

### ATC01.py - 新增按鈕功能測試

此測試案例模擬使用者在 Smoney 應用程式中執行以下操作：

1. 點擊「不用同步，直接開始」按鈕
2. 處理可能出現的取消對話框
3. 點擊新增按鈕
4. 確認操作並輸入數據
5. 完成新增流程

### ATC02.py - 應用程式互動測試

此測試案例執行類似的互動流程，用於驗證應用程式的穩定性。

### test.py - Android 設定應用測試

基礎測試案例，用於測試 Android 系統設定應用程式的基本功能。

## 配置檔案

### test.json

包含 Appium 的基本配置設定：

```json
{
  "platformName": "Android",
  "automationName": "UiAutomator2",
  "deviceName": "Android",
  "appPackage": "com.money.smoney_android",
  "appActivity": "com.money.smoney_android.ui.splash.SplashActivity",
  "noReset": true
}
```

## 共用函數庫 (components.py)

提供兩個主要的輔助函數：

### `wait_and_click(driver, timeout, ui_selector_str)`

- 等待元素可點擊後執行點擊操作
- 參數：
  - `driver`: WebDriver 實例
  - `timeout`: 等待超時時間（秒）
  - `ui_selector_str`: Android UiSelector 字串

### `wait_until_present(driver, timeout, ui_selector_str)`

- 等待元素出現在頁面上
- 參數同上

## 故障排除

### 常見問題

1. **ImportError: module 'selectors' has no attribute 'DefaultSelector'**

   - 確保 websocket-client 版本 >= 1.6.4
   - 檢查專案目錄中是否有名為 `selectors.py` 的檔案並重新命名

2. **Appium Server 連接失敗**

   - 確認 Appium Server 已啟動且運行在 http://localhost:4723
   - 檢查防火牆設定

3. **找不到 Android 裝置**

   - 使用 `adb devices` 確認裝置連接狀態
   - 確保 USB 偵錯已啟用

4. **應用程式無法啟動**
   - 確認應用程式套件名稱和活動名稱正確
   - 檢查應用程式是否已安裝在測試裝置上

## 開發建議

1. 使用明確的等待條件而非固定延遲時間
2. 為每個測試案例添加適當的錯誤處理
3. 使用 Page Object Model 模式組織測試程式碼
4. 定期更新依賴套件版本

## 貢獻

歡迎提交 Pull Request 或回報問題。請確保：

- 程式碼符合 PEP 8 標準
- 添加適當的註解和文件
- 測試新功能的穩定性

## 授權

此專案僅供學術研究使用。

---

**注意：** 確保在執行測試前已正確設定所有環境和依賴套件。

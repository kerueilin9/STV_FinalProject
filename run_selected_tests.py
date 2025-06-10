#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
執行指定的測試檔案
"""

import subprocess
import time
from datetime import datetime

def run_test(test_file):
    """執行單一測試檔案"""
    print(f"\n{'='*60}")
    print(f"執行測試: {test_file}")
    print(f"{'='*60}")
    
    start_time = datetime.now()
    
    try:
        # 執行測試
        result = subprocess.run(
            ['python', test_file],
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=300
        )
        
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        print(f"執行時間: {execution_time:.2f} 秒")
        print(f"返回碼: {result.returncode}")
        
        if result.stdout:
            print(f"輸出:\n{result.stdout}")
        if result.stderr:
            print(f"錯誤:\n{result.stderr}")
            
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("測試執行超時")
        return False
    except Exception as e:
        print(f"執行錯誤: {e}")
        return False

def main():
    """主函數"""
    test_files = [
        'ATC25.py',
        'ATC26.py', 
        'ATC27.py',
        'ATC28.py',
        # 'ATC15.py',
        # 'ATC16.py',
        # 'ATC07.py',
        # 'ATC08.py'
    ]
    
    print("開始執行選定的測試檔案...")
    print(f"總共 {len(test_files)} 個檔案")
    
    results = []
    
    for i, test_file in enumerate(test_files, 1):
        print(f"\n進度: {i}/{len(test_files)}")
        success = run_test(test_file)
        results.append((test_file, success))
        
        # 測試間隔
        if i < len(test_files):
            print("等待 2 秒後執行下一個測試...")
            time.sleep(2)
    
    # 顯示總結
    print(f"\n{'='*60}")
    print("測試執行總結")
    print(f"{'='*60}")
    
    success_count = sum(1 for _, success in results if success)
    
    print(f"總測試: {len(results)}")
    print(f"成功: {success_count}")
    print(f"失敗: {len(results) - success_count}")
    print(f"成功率: {success_count/len(results)*100:.1f}%")
    
    print(f"\n詳細結果:")
    for test_file, success in results:
        status = "✓ 成功" if success else "✗ 失敗"
        print(f"  {test_file:<15} {status}")

if __name__ == "__main__":
    main()

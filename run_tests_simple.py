import os
import subprocess
import time
from datetime import datetime
import json

def get_test_files():
    """獲取所有測試檔案"""
    test_files = []
    
    # 獲取當前目錄下的所有 Python 檔案
    for file in os.listdir('.'):
        if file.endswith('.py') and ('ATC' in file or file == 'test.py'):
            test_files.append(file)
    
    # 排序檔案名稱
    test_files.sort()
    return test_files

def run_single_test(test_file):
    """執行單一測試檔案"""
    print(f"\n{'='*60}")
    print(f"執行測試: {test_file}")
    print(f"{'='*60}")
    
    start_time = datetime.now()
    
    try:
        # 使用 subprocess 執行測試
        result = subprocess.run(
            [r'C:\Users\kerueilin9\AppData\Local\Programs\Python\Python312\python.exe', test_file],
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=300  # 5分鐘超時
        )
        
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        print(f"執行時間: {execution_time:.2f} 秒")
        print(f"返回碼: {result.returncode}")
        
        # 分析輸出
        stdout = result.stdout
        stderr = result.stderr
        
        if stdout:
            print(f"標準輸出:\n{stdout}")
        if stderr:
            print(f"標準錯誤:\n{stderr}")
        
        # 判斷測試結果
        if result.returncode == 0:
            if "OK" in stdout or "." in stdout:
                status = "SUCCESS"
            else:
                status = "UNKNOWN"
        else:
            status = "FAILED"
            
        return {
            "file": test_file,
            "status": status,
            "execution_time": execution_time,
            "return_code": result.returncode,
            "stdout": stdout,
            "stderr": stderr,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat()
        }
        
    except subprocess.TimeoutExpired:
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        print(f"測試超時 ({execution_time:.2f} 秒)")
        
        return {
            "file": test_file,
            "status": "TIMEOUT",
            "execution_time": execution_time,
            "return_code": -1,
            "stdout": "",
            "stderr": "測試執行超時",
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat()
        }
        
    except Exception as e:
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        print(f"執行錯誤: {str(e)}")
        
        return {
            "file": test_file,
            "status": "ERROR",
            "execution_time": execution_time,
            "return_code": -1,
            "stdout": "",
            "stderr": str(e),
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat()
        }

def generate_report(results):
    """產生測試報表"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print(f"\n{'='*80}")
    print("測試執行報表")
    print(f"{'='*80}")
    
    total_tests = len(results)
    success_count = len([r for r in results if r['status'] == 'SUCCESS'])
    failed_count = len([r for r in results if r['status'] == 'FAILED'])
    error_count = len([r for r in results if r['status'] == 'ERROR'])
    timeout_count = len([r for r in results if r['status'] == 'TIMEOUT'])
    unknown_count = len([r for r in results if r['status'] == 'UNKNOWN'])
    
    total_time = sum(r['execution_time'] for r in results)
    
    print(f"執行時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"總執行時間: {total_time:.2f} 秒")
    print(f"測試檔案數量: {total_tests}")
    print(f"\n結果統計:")
    print(f"  成功: {success_count} ({success_count/total_tests*100:.1f}%)")
    print(f"  失敗: {failed_count} ({failed_count/total_tests*100:.1f}%)")
    print(f"  錯誤: {error_count} ({error_count/total_tests*100:.1f}%)")
    print(f"  超時: {timeout_count} ({timeout_count/total_tests*100:.1f}%)")
    print(f"  未知: {unknown_count} ({unknown_count/total_tests*100:.1f}%)")
    
    print(f"\n詳細結果:")
    print(f"{'檔案名稱':<50} {'狀態':<10} {'執行時間(秒)':<15}")
    print(f"{'-'*80}")
    
    for result in results:
        status_symbol = {
            'SUCCESS': '✓',
            'FAILED': '✗', 
            'ERROR': '❌',
            'TIMEOUT': '⏰',
            'UNKNOWN': '?'
        }.get(result['status'], '?')
        
        print(f"{result['file']:<50} {status_symbol} {result['status']:<9} {result['execution_time']:<15.2f}")
    
    # 失敗和錯誤詳情
    failed_tests = [r for r in results if r['status'] in ['FAILED', 'ERROR', 'TIMEOUT']]
    if failed_tests:
        print(f"\n失敗測試詳情:")
        print(f"{'-'*80}")
        for result in failed_tests:
            print(f"\n{result['file']} ({result['status']}):")
            if result['stderr']:
                print(f"錯誤: {result['stderr'][:300]}...")
            if result['stdout']:
                print(f"輸出: {result['stdout'][:300]}...")
    
    # 儲存 JSON 報表
    json_filename = f"test_report_{timestamp}.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": timestamp,
            "summary": {
                "total_tests": total_tests,
                "success": success_count,
                "failed": failed_count,
                "error": error_count,
                "timeout": timeout_count,
                "unknown": unknown_count,
                "total_time": total_time
            },
            "results": results
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n報表已儲存到: {json_filename}")
    
    return json_filename

def main():
    """主函數"""
    print("Appium 自動化測試批次執行器")
    print("="*50)
    
    # 獲取測試檔案
    test_files = get_test_files()
    
    print(f"找到 {len(test_files)} 個測試檔案:")
    for i, test_file in enumerate(test_files, 1):
        print(f"  {i}. {test_file}")
    
    print(f"\n請確保:")
    print("1. Appium Server 已啟動 (http://localhost:4723)")
    print("2. Android 模擬器或實體裝置已連接")
    print("3. 測試應用程式已安裝在裝置上")
    
    input("\n按 Enter 鍵開始執行測試...")
    
    # 執行所有測試
    results = []
    overall_start_time = datetime.now()
    
    for i, test_file in enumerate(test_files, 1):
        print(f"\n進度: {i}/{len(test_files)}")
        result = run_single_test(test_file)
        results.append(result)
        
        # 測試間隔，避免資源衝突
        if i < len(test_files):
            print("等待 3 秒後執行下一個測試...")
            time.sleep(3)
    
    overall_end_time = datetime.now()
    overall_time = (overall_end_time - overall_start_time).total_seconds()
    
    print(f"\n{'='*50}")
    print(f"所有測試執行完成! 總時間: {overall_time:.2f} 秒")
    
    # 產生報表
    report_file = generate_report(results)
    
    print(f"\n測試報表已產生: {report_file}")

if __name__ == "__main__":
    main()

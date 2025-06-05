# Stock Pilot - 台股爬蟲工具

這是一個簡單的台股條件式選股爬蟲，使用 Selenium + BeautifulSoup 自動抓取 MoneyDJ 的篩選條件股票，並輸出 Excel 報表。

## 執行方式

1. 建立虛擬環境：
```bash
python -m venv stock-env
```
2. 安裝套件：
```bash
pip install -r requirements.txt
```
3. 測試套件：
```bash
python package_test.py
```
## 套件需求
```text
- selenium
- beautifulsoup4
- openpyxl
```

```plaintext
stock-pilot/
├── stock-env/               # 虛擬環境（不要放上 GitHub）
├── package_test.py          # 測試套件
├── requirements.txt         # 套件清單
└── README.md                # 說明文件
```

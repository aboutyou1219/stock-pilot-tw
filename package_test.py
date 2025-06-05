from selenium import webdriver
from bs4 import BeautifulSoup
import openpyxl
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://concords.moneydj.com/z/zk/zk5/zkparse_320_30.djhtm")
soup = BeautifulSoup(driver.page_source, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")

for row in rows[:5]:  # 先印前幾行看看
    print(row.get_text())

driver.quit()
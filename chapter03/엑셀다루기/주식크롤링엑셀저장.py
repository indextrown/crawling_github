import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'C:\Users\Index\PycharmProjects\startproject\chapter03\엑셀다루기\참가자_data.xlsx'

#1 엑셀 불러오기
wb = openpyxl.load_workbook(fpath)

ws = wb.active #현재 활성화된 시트를 선택


## 종목 코드 리스트
codes = {
    '005930',
    '028260',
    '066570'
}


row = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',', '')
    alpha = 0
    alpha+=1
    print(price)
    ws[f'B{row}'] = int(price)
    row = row + 1
wb.save(fpath)








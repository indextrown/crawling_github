# 키워드 별로 순위, 브랜드명, 가격, 상세페이지링크 엑셀 저장

# 1~100위까지

#len([])

#게이밍 마우스, 기계식 키보드, 27인치 모니터

import requests
from bs4 import BeautifulSoup
import pyautogui
#import time
##import pyautogui
#from openpyxl import Workbook
#from openpyxl.styles import Alignment  #엑셀 자동 줄바꿈

#select 는 한 페이지에 여러개
#select_one는 각 페이지의 이름 과 같이

# 헤더에 User-Agent, Accept-Language 를 추가하지 않으면 멈춥니다
header = {
    'Host': 'www.coupang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
}

keyword = pyautogui.prompt("검색어를 입력하시오:")
main_url = f"https://www.coupang.com/np/search?rocketAll=false&q={keyword}&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page=1&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=595564&component=&rating=0&sorter=scoreDesc&listSize=36"
#headers={'user-agent':'Mozila/5.0'} 봇으로 접근 가능하게 함 headers={'user-agent':'Mozila/5.0'}
response = requests.get(main_url, headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# select의 결과는 리스트 자료형
links = soup.select("a.search-product-link")


for link in links:
    # 광고 상품 제거

    if len(link.select("span.ad-badge-text"))>0:
        print("광고 상품 입니다")
    else:
        sub_url = "https://www.coupang.com/" + link.attrs['href']

        # 상세 페이지 링크
        response = requests.get(sub_url, headers=header)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # 브랜드명 추출     , Text요소만 출력
        # 브랜드명은 있을 수도 없을 수도 있음
        # 중고 상품일 때는 태그가 달라짐
        # try -except로 예외처리
        # 예외가 났을 때 브랜드명 비워줌
        try:
            brand_name = soup.select_one("a.prod-brand-name").text
            # print(brand_name)
        except:
            brand_name = ""

        # 상품명 추출
        name = soup.select_one("h2.prod-buy-header__title").text
        # print(name)

        # 가격 추출
        # 만약 와우 할인가가 있으면 와우 할인가 출력
        # 그렇지 않으면 쿠팡 판매가 출력

        # 쿠팡 판매가
        price = soup.select_one("span.total-price > strong").text
        print(brand_name, name, price)













        '''#와우 할인가
        price = soup.select_one("div.prod-coupon-price.prod-major-price > span.total-price").text
        print("와우할인가:", price)'''

        '''if "div.prod-coupon-price.prod-major-price" in soup:
            price = soup.select_one("div.prod-coupon-price.prod-major-price > span.total-price").text
            print("와우할인가:", price)
        else:
            price = soup.select_one("span.total-price > strong").text
            print("쿠팡판매가:", price)'''

        # 상세 페이지로 가는 링크 추출
        # print(sub_url)







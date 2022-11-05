import requests
from bs4 import BeautifulSoup
import time

response = requests.get(
    "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC&oquery=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&tqi=h2U9%2FlprvhGssLD%2BKvZssssstQ4-489077&nso=so%3Ar%2Cp%3Aall%2Ca%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=0")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# 뉴스 기사 div 10개 추출
articles = soup.select("div.news_info")

num = 0
for article in articles:
    # 리스트
    links = article.select("a.info")
    num = num + 1

    # 링크가 2개 이상이면
    if len(links) >= 2:
        # 두번째 링크의 href를 추출한다
        url = links[1].attrs['href']
        ##print(num, url)

        # headers={'user-agent':'Mozila/5.0'} 봇으로 접근 가능하게 함
        response = requests.get(url, headers={'user-agent': 'Mozila/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        #content = soup.select_one("#dic_area")
        #title = soup.select_one(".media_end_head_title")


        #만약 연애 뉴스 라면 //response => 링크가 리다이렉션인지(사이트 주소가 바뀌는지) 확인하기 위해 response.url 로 만듬
        if "entertain" in response.url:
            title = soup.select_one(".end_tit")
            content = soup.select_one("#articeBody")
        #연애 뉴스가 아니라면
        else:
            title = soup.select_one(".media_end_head_headline")
            content = soup.select_one("#dic_area")

        print("=======링크======= \n", url)
        #공백 제거 .text.strip()
        print("=======제목======= \n", title.text.strip())

        print("=======본문======= \n", content.text.strip())
        # time.sleep(0.3)

# arrtibure arror:'nonetype object has no arrtibure text 객체에 네가 원하는 속성이 없다
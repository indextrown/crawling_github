import requests
from bs4 import BeautifulSoup
import time

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=104&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

#뉴스 기사 div 10개 추출
articles = soup.select("div.news_info")

num = 0
for article in articles:
    #리스트
    links = article.select("a.info")
    num = num + 1

    #링크가 2개 이상이면
    if len(links) >= 2:
        #두번째 링크의 href를 추출한다
        url = links[1].attrs['href']
        #print(num, url)
        #headers={'user-agent':'Mozila/5.0'} 봇으로 접근 가능하게 함
        response = requests.get(url, headers={'user-agent':'Mozila/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        content = soup.select_one("#dic_area")
        title = soup.select_one(".media_end_head_title")

        print("============링크============>\n", url)
        print("============제목============>", title.text)
        print(content.text)
        #time.sleep(0.3)
        
#arrtibure arror:'nonetype object has no arrtibure text 객체에 네가 원하는 속성이 없다
import requests
from bs4 import BeautifulSoup
import time
response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC")
html = response.text
##naver에서 html을 준것임
##response.text파일의 내용을 html 변수에 담는다
soup = BeautifulSoup(html, 'html.parser')  ##번역선생님
articles = soup.select("div.info_group") #뉴스 기사 div 10개 추출

for article in articles:
    links = article.select("a.info") #리스트
    if len(links) >= 2:              #링크가 2개 이상이면
        url = links[1].attrs['href'] #두번째 링크의 href를 추출
        #print(url)
        response = requests.get(url, headers={'User-agent':'Mozila/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')  ##번역선생님


        #만약 연예 뉴스 라면
        if "entertain" in response.url: #리다이렉션 방지 response.
            title = soup.select_one("h2.end_tit")
            content = soup.select_one("#articeBody")
        else:
            title = soup.select_one("h2.media_end_head_headline")
            content = soup.select_one("#newsct_article")
        print("==========링크==========\n", url)
        print("==========제목==========\n", title.text)
        print("==========본문==========\n", content.text)

        time.sleep(0.3)  #0.3 딜레이
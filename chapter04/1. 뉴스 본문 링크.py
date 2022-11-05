import requests
from bs4 import BeautifulSoup
import time

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
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
        content = soup.select_one("#newsct_article")
        print(content.text)
        time.sleep(0.3)  #0.3 딜레이
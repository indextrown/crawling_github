import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
##naver에서 html을 준것임
##response.text파일의 내용을 html 변수에 담는다
soup = BeautifulSoup(html, 'html.parser')  ##번역선생님
links = soup.select(".news_tit")  ##결과는 리스트
i=1

for link in links:
    title = link.text  ##태그 안에 텍스트 요소만 가져와서 변수에 저장
    url =  link.attrs['href'] ## href의 속성 값을 가져와서 변수에 저장
    print(i)
    i = i + 1
    print(title, url)


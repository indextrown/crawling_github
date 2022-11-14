import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하시오")
lastpage = pyautogui.prompt("마지막 페이지 번호를 입력하시오")
num=1
pageNum=1
for i in range(1, int(lastpage)*10, 10):
    print(f"{pageNum}페이지 입니다==============================================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')  ##번역선생님
    links = soup.select(".news_tit")  ##결과는 리스트
    pageNum = pageNum+1
    for link in links:
        title = link.text  ##태그 안에 텍스트 요소만 가져와서 변수에 저장
        url =  link.attrs['href'] ## href의 속성 값을 가져와서 변수에 저장
        print(num, title, url)
        num = num + 1

import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하시오")

response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')  ##번역선생님
links = soup.select(".news_tit")  ##결과는 리스트



num=1
for link in links:
    title = link.text  ##태그 안에 텍스트 요소만 가져와서 변수에 저장
    url =  link.attrs['href'] ## href의 속성 값을 가져와서 변수에 저장


    print(num, title, url)
    num = num + 1

import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.naver.com/")
##response는 네이버 서버에 대화를 시도
##주소를 요청해서 응답을 받자

html = response.text
##naver에서 html을 준것임
##response.text파일의 내용을 html 변수에 담는다

soup = BeautifulSoup(html, 'html.parser')
##html 번역선생님으로 아름다운 수프 완성

word = soup.select_one('#NM_set_home_btn')
##id 값이 NM_set_home_btn인 놈 한개를 찾아냄
#soup.select로  원하는 태그 선택 가능 word 변수에 저장

print(word.text)
##텍스트 요소만 출력
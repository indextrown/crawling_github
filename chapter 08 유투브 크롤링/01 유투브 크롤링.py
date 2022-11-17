from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 엔터키 관련
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  #크롬 드라이버 자동 업데이트

from selenium.webdriver.common.by import By
import time
import openpyxl

# 입력부분
keyword = input("검색어를 입력하시오")

#1 엑셀 만들기
wb = openpyxl.Workbook()

# 입력한 키워드 명으로 엑셀 시트 생성
ws = wb.create_sheet(keyword)

# 처음 새로운 엑셀파일이 생성될 때 존재하는 "Sheet" 시트 삭제
wb.remove(wb['Sheet'])

#열 너비 조절
ws.column_dimensions['A'].width = 5.0
ws.column_dimensions['B'].width = 10.0
ws.column_dimensions['C'].width = 70.0
ws.column_dimensions['D'].width = 10.0
ws.column_dimensions['E'].width = 120

# 리스트 형태로 맨위의 칸 추가
ws.append(['제목', '조회수', 'test1', 'test2', 'link'])



keyword = "아두이노"
#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

#서비스 객체를 만들어서 service에 저장
service = Service(executable_path=ChromeDriverManager().install())

##크롬 브라우저를 생성
#셀레니움 웹드라이버 => chrome을 만들어냄 서비스는 service 집어넣음
driver = webdriver.Chrome(service=service, options=chrome_options)


#웹페이지 해당 주소 이동
driver.implicitly_wait(5) #웹페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window()  #화면 최대화
driver.get(f"https://www.youtube.com/results?search_query={keyword}")


# 스크롤 전 높이  자바스크립트 실행 가능 함수
before_h = driver.execute_script("return window.scrollY")


# 특정 횟수만큼 스크롤 내리기 1~11이면 1 ~ 10을 의미

for i in range(1, 11):
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(1)
att = 10
html = driver.page_source
import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml') #html.parser

title = soup.select('#video-title > yt-formatted-string')

for i in title:
    print(i.text.strip())


# 엑셀 저장하기
wb.save(f"./{keyword}.xlsx")


driver.close()
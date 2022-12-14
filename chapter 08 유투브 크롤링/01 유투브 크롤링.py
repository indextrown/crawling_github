from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 엔터키 관련
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  #크롬 드라이버 자동 업데이트

from selenium.webdriver.common.by import By
import time
import openpyxl

# 헤더에 User-Agent, Accept-Language 를 추가하지 않으면 멈춥니다
header = {
    'Host': 'www.coupang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
}


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
ws.column_dimensions['B'].width = 70.0
ws.column_dimensions['C'].width = 10.0
ws.column_dimensions['D'].width = 10.0
ws.column_dimensions['E'].width = 70.0

# 리스트 형태로 맨위의 칸 추가
ws.append(['번호', '제목', '조회수', '날짜' ,'링크'])



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

    html = driver.page_source
import requests

from bs4 import BeautifulSoup
main_url = f"https://www.youtube.com/results?search_query={keyword}"

# headers={'user-agent':'Mozila/5.0'} 봇으로 접근 가능하게 함 headers={'user-agent':'Mozila/5.0'}
response = requests.get(main_url, headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')


num = 1
# soup.select는 리스트 형태로 출력하기 때문에 for문을 통해 변수를 입력받아야 함.
links = soup.select("a#video-title")
for link in links:
    sub_url = "https://www.youtube.com/" + link.attrs['href']
    print(num, sub_url)
    num += 1

    title_Name = soup.select_one("#title > h1 > yt-formatted-string")



















    ''' #리스트가 아닌 그냥 변수 형식
     links = soup.select_one("a.yt-simple-endpoint.style-scope.ytd-video-renderer").attrs['href']
    print(links)
    
    '''













    '''title = soup.select('#video-title > yt-formatted-string')

    # 제목 여러개 출력하기

    print(i.text.strip())
    ws.append(['1','2','3','4','5'])

    # 엑셀 저장하기
    wb.save(f"./{keyword}.xlsx")'''


    #driver.close()
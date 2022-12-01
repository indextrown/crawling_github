import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager



#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

#서비스 객체를 만들어서 service에 저장
# ChromeDriverManager를 통해서 ChromeDriver 를 최신버전으로 자동 설치 후 서비스 객체를 만들어서 service 변수에 저장
service = Service(executable_path=ChromeDriverManager().install())

#셀레니움 웹드라이버 => chrome을 만들어냄 서비스는 service 집어넣음
driver = webdriver.Chrome(service=service, options=chrome_options)

#웹페이지 해당 주소 이동
driver.implicitly_wait(5) #웹페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window()  #화면 최대화
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

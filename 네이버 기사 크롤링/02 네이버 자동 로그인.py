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

#크롬 드라이버 매니저를 통해 크롬 드라이버를 최신 버전으로 자동으로 설치
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

#웹 페이지가 로딩 될때 까지 5초는 기다린다
driver.implicitly_wait(5)

#화면 최대화
driver.maximize_window()

#웹 페이지 주소 이동
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

#아이디 입력창
#크롬 드라이버를 통해 해당 css선택자에 맞는 태그를 자동으로 찾아줌
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
id.send_keys("d2131")

#pw 입력창
#크롬 드라이버를 통해 해당 css선택자에 맞는 태그를 자동으로 찾아줌
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pw.send_keys("improve@!3")

#로그인 버튼 클릭
login = driver.find_element(By.CSS_SELECTOR, "#log\.login")
login.click()

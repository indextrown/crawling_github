import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  #크롬 드라이버 자동 업데이트



#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

#서비스 객체를 만들어서 service에 저장
service = Service(executable_path=ChromeDriverManager().install())

#셀레니움 웹드라이버 => chrome을 만들어냄 서비스는 service 집어넣음
driver = webdriver.Chrome(service=service, options=chrome_options)

#웹페이지 해당 주소 이동
driver.implicitly_wait(5) #웹페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window()  #화면 최대화
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
#id.send_keys("d2131")
pyperclip.copy("d2131")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
#pw.send_keys("improve@!3")
pyperclip.copy("improve@!3")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

#로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()

#메일함 버튼
mail = driver.find_element(By.CSS_SELECTOR, "a.nav")
mail.click()

#메일쓰기 버튼
sendmail = driver.find_element(By.CSS_SELECTOR, "a.item.button_write")
sendmail.click()

#메일 수신자 입력
mailaddress = driver.find_element(By.CSS_SELECTOR, "#user_input_1")
mailaddress.click()
pyperclip.copy("lghan00020@nate.com")
pyautogui.hotkey("ctrl", "v")


#메일 제목 입력
mailaddress = driver.find_element(By.CSS_SELECTOR, "#subject_title")
mailaddress.click()
pyperclip.copy("테스트메일 입니다")
pyautogui.hotkey("ctrl", "v")



#메일 내용
word_mail = driver.find_element(By.CSS_SELECTOR, "#content > div.contents_area > div > div.editor_area > div > div.editor_body")
word_mail.click()
pyperclip.copy("테스트 메일 입니다")
pyautogui.hotkey("ctrl", "v")

#메일 보내기
send_mail = driver.find_element(By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task")
send_mail.click()


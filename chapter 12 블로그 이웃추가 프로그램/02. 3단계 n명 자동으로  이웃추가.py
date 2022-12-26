import requests
import pyperclip
import pyautogui
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 엔터키 관련
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  #크롬 드라이버 자동 업데이트

n = int(input("이웃추가 횟수를 입력하시오"))
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
driver.get("https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/")


# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
#id.send_keys("d2131")
pyperclip.copy("d2131")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
#pw.send_keys("improve@!3")
pyperclip.copy("improve@!3")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)


#로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()


# 키워드 : 제태그
# 정렬 : 블로그, 최신순
search_url = "https://m.search.naver.com/search.naver?where=m_blog&query=%EC%A0%9C%ED%85%8C%ED%81%AC&sm=mtb_org&nso=so%3Add%2Cp%3Aall&qvt=0"
driver.get(search_url)


#n = 10    # 총 이웃 신청 개수
count = 0 # 현재 이웃 신청 개수
index = 0 # 현재 블로그 글 번호

while count < n:


    # 첫 블로그 사용자 프로필 클릭( element는 1개 elements 는 여러개)
    ids = driver.find_elements(By.CSS_SELECTOR, ".sub_txt.sub_name")

    # 현재 블로그 글 번호에 맞는 아이디 찾기
    id = ids[index]


    # 블로그 아이디 클릭
    # 새창으로 열기
    id.send_keys(Keys.CONTROL + '\n')


    # 새창으로 드라이버 전환
    ## 드라이버가 열린 모든 창을 가지고 옴
    all_windows = driver.window_handles

    ## 드라이버가 제어하고 있는 윈도우를 바꾸겠다  [0]은 기존 [1]은 새로운 창
    driver.switch_to.window(all_windows[1])
    time.sleep(2)
    try:
        # 이웃추가 버튼
        make_friends = driver.find_element(By.CSS_SELECTOR, ".link__RsHMX.add_buddy_btn__oGR_B")
        time.sleep(2)
        make_friends.click()

        # 서로 이웃 추가
        each_friends = driver.find_element(By.CSS_SELECTOR, "#bothBuddyRadio")
        each_friends.click()

        input_message = "제태크에 관심있는 블로거 입니다. 반갑습니다"

        # 이웃추가 멘트 박스
        ment_box = driver.find_element(By.CSS_SELECTOR, ".textarea_t1.ng-pristine.ng-untouched.ng-valid.ng-not-empty")
        time.sleep(1)
        ment_box.click()

        ment_box.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        ment_box.send_keys(Keys.DELETE)
        time.sleep(1)

        ment_box.send_keys(input_message)

        '''pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("esc")
        pyperclip.copy("안녕하세요 재테크에 관심있는 청년입니다 소통하고 싶습니다!")
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)'''

        # 확인
        ok = driver.find_element(By.CSS_SELECTOR, ".btn_ok")
        ok.click()
        count += 1  # 현재 이웃 신청 개수 증가
        time.sleep(2)


    except:
        print("이웃추가 버튼이 비활성화 되어 있습니다")
        time.sleep(3)
        pass  # 그냥 넘어감


    # 새창 닫기
    driver.close()
    # driver.quit();


    # 기존 창으로 드라이버 전환
    driver.switch_to.window(all_windows[0])
    index += 1 # 현재 블로그 글 번호 증가






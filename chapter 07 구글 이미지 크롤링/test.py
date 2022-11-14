from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  #크롬 드라이버 자동 업데이트
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib.request # url로 이미지를 다운받기 위한 라이브러리
from selenium.webdriver.common.keys import Keys # 엔터키 관련
import time
import os
import urllib.request # url로 이미지를 다운받기 위한 라이브러리
import pyautogui

# 크롤링 하다보면 주로 발생하는 오류
    # 403 forbidden error 서버가 연결을 거부 하는것
    # 해결법 header 를 추가히준다 어떤 header => useragent(브라우저 생김새)
    # 보통 mozila 5.0을 추가해줌
    # 밑에 참고





# step1+2: 입력부분
searchimage = pyautogui.prompt("검색어를 입력하시오:")
searchnum = pyautogui.prompt("이미지 개수를 입력하시오:")


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
driver.get(f"https://www.google.com/search?q={searchimage}&sxsrf=ALiCzsZMaT6NfdknzaS5PHsAeoO8pbBCMw:1668433179078&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiruOH35a37AhXIaN4KHRfsDOkQ_AUoAXoECAEQAw&biw=788&bih=746&dpr=1.25")

# 스크롤 전 높이  자바스크립트 실행 가능 함수
before_h = driver.execute_script("return window.scrollY")


# 무한 스크롤  반복문(맨 아래로 스크롤을 내린다)
while True:
    '''맨 아래로 스크롤을 내린다'''
    '''body 태그를 찾아서 end키를 누른다'''

    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    '''스크롤 사이 페이지 로딩 시간'''
    time.sleep(1)

    '''스크롤 후 높이'''
    after_h = driver.execute_script("return window.scrollY")

    if after_h == before_h:
        break

    before_h = after_h
# 썸내일 이미지 추출
small_imges = driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")

count = 1
for i, image in enumerate(small_imges, 1):
    # 이미지를 클릭해서 큰 사이즈를 찾아요
    image.click()
    time.sleep(1)

    # 큰 이미지 주소 추출
    img = driver.find_element(By.CSS_SELECTOR, "img.n3VNCb")
    img_src = img.get_attribute('src')
    print(img_src)

    # 폴더 만들기
    img_folder = f'./{searchimage}.사진폴더'
    if not os.path.isdir(f'{searchimage}.사진폴더'):  # img폴더가 없으면 생성한다
        os.mkdir(img_folder)

    # 이미지를 url로 다운받는다.

    # 크롤링 하다보면 주로 발생하는 오류
    # 403 forbidden error 서버가 연결을 거부 하는것
    # 해결법 header 를 추가히준다 어떤 header => useragent(브라우저 생김새)
    # 보통 mozila 5.0을 추가해줌
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]
    urllib.request.install_opener(opener)

    urllib.request.urlretrieve(img_src, f'./{searchimage}.사진폴더/{i}' + ".png")

    if count >= int(searchnum):
        break
    count+=1
driver.close()
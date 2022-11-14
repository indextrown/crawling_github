from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys # 엔터키 관련
#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import urllib.request # url로 이미지를 다운받기 위한 라이브러리

#입력부분
searchimage=input("입력하시오")

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
driver.get(f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={searchimage}")

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

images = driver.find_elements(By.CSS_SELECTOR, "img._image._listImage")


#enumerate 리스트에 번호 붙임 (, 1부터시작)
for i, image in enumerate(images, 1):
    # get_attribute 속성값 얻기 ex) images에 대해서 _image
    # 각 이미지 태그의 주소
    img_src = image.get_attribute('src')
    print(i, img_src)

    img_folder = f'./{searchimage}.사진폴더'
    if not os.path.isdir(f'{searchimage}.사진폴더'):  # img폴더가 없으면 생성한다
        os.mkdir(img_folder)

        # 이미지를 url로 다운받는다.
    urllib.request.urlretrieve(img_src, f'./{searchimage}.사진폴더/{i}' + ".png")

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 엔터키 관련
##크롬 브라우저를 생성
browser = webdriver.Chrome('c:/chromedriver.exe')  
#웹 사이트 열기
browser.get('https://www.naver.com/')

#로딩이 끝날 때까지 10초까지는 기다려줌
browser.implicitly_wait(10)

#쇼핑 메뉴 클릭
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

#검색창 클릭
search = browser.find_element_by_css_selector('input._searchInput_search_text_3CUDs')
search.click()

#검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

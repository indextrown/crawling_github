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

#스크롤 전 높이  자바스크립트 실행 가능 함수
before_h = browser.execute_script("return window.scrollY")

#무한 스크롤  반복문(맨 아래로 스크롤을 내린다)
while True:
    '''맨 아래로 스크롤을 내린다'''
    '''body 태그를 찾아서 end키를 누른다'''
    browser.find_element_by_css_selector("body").send_keys(Keys.END)
    
    '''스크롤 사이 페이지 로딩 시간'''
    time.sleep(1)

    '''스크롤 후 높이'''
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break

    before_h = after_h

#상품 정보 div  해당되는 element(s) 여러개 가져옴=> 리스트 형태로 반환
items = browser.find_elements_by_css_selector(".basicList_info_area__TWvzp")

for item in items:
    name = item.find_element_by_css_selector(".basicList_title__VfX3c").text
    
    try: ##오류처리 ex)판매중단처럼 판매가격이 안나올때
        price = item.find_element_by_css_selector(".price_num__S2p_v").text
    except:
        price = "판매중단"
    link = item.find_element_by_css_selector(".basicList_title__VfX3c > a").get_attribute('href')
    print(name, price, link)
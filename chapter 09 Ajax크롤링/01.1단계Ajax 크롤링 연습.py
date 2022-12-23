## ajax(=비동기 크롤링)
#네이버 검색창에 단어를 칠때 자동으로 연관 검색어를 서버로 부터 받아와 실시간 업데이트를 해줌
# 비동기 통신

# 필요한 지식
# 파이썬 딕셔너리 자료형 key value
# ex) 딕셔너리 = {key : value, key : value}


import requests
import json
response = requests.get("https://ac.search.naver.com/nx/ac?q=%EC%A3%BC%EC%8B%9D%20%E3%84%B1&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_4")

# response 객체에 text 객체가 존재하는데 이텍스트를 origin_data 변수로 저장
origin_data = response.text

# 출력
#print(origin_data)

# # split 문자열을 자르겠다 ""안의 것으로
print(origin_data.split("_jsonp_4("))

#딕셔너리의 두번째 값 = 1
print(origin_data.split("_jsonp_4(")[1])

# 깔끔한 딕셔너리 필요 맨마지막 ) 지우는법
# 문자열의 마지막 문자 없애기 => 슬라이싱   [:-1] : 0부터 마지막 번호까지 제외
print(origin_data.split("_jsonp_4(")[1][:-1])

str_data = origin_data.split("_jsonp_4(")[1][:-1]



#!!!!!!!!!중요
# 자료형 확인하기
print(type(str_data))

# str(문자열)자료형을 가진 딕셔너리는 key값을 뽑아오기 어렵다=> 딕셔너리 자료형으로 바꿀 필요 있음
# import json모듈 필요
dic_data = json.loads(str_data)
print(type(dic_data))
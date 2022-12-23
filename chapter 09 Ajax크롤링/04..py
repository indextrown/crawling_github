## ajax(=비동기 크롤링)
#네이버 검색창에 단어를 칠때 자동으로 연관 검색어를 서버로 부터 받아와 실시간 업데이트를 해줌
# 비동기 통신


# 필요한 지식
# 파이썬 딕셔너리 자료형 key value
# ex) 딕셔너리 = {key : value, key : value}


# 딕셔너리 값 접근하기
# data = {"name" : "김동현", "age": "27"}
# data["name"] ==> 홍길동 가져옴


# ajax 크롤링 방법
# 네이버 기준으로 f12창을 누르고 network창을 누르고 네이버 화면으로 돌아와서 검색어를 친다 ex) 주식 ㄱ


# 하면 network 칸에서 새로 여러 name이 뜨는데 맨 밑에꺼 클릭하고 resp
# onse 칸에서 이상한 데이터가 들어있음(딕셔너리 자료형태)
# header 탭에서 url을 request 요청을 하면 response 딕셔너리가 뜬다!


import requests
response = requests.get("https://ac.search.naver.com/nx/ac?q=%EC%A3%BC%EC%8B%9D%20%E3%84%B1&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_3")


# .string 태그 하위에 문자열을 객체화 한다 문자열이 없으면 None 을 반환
# .text는 하위 자식태그의 텍스트까지 문자열로 반환합니다. (유니코드 형식)
origin_data = response.text


# split 하고 index 1번 data만 가져오고 슬라이싱을 이용해 0부터 마지막 번호까지 제외
str_data = origin_data.split("_jsonp_3(")[1][:-1]
print(type(str_data))

# 문자열 자료형은 key값들만 뽑아오기 힘들기 때문에 딕셔너리 자료형 형태로 바꿔줄 것임
import json
dic_data = json.loads(str_data)
print(type(dic_data))














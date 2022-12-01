import requests

# get명령어: 서버에 요청을 보낸다 url
# 서버는 요청을 받으면 응답(response을 돌려준다)
# response는 객체이다 -> 속성+명령어(메서드)
response = requests.get("https://www.naver.com/")

# 응답코드출력: 요청에 대한 응답상태를 나타냄
print(response.status_code)

# 200 통신 정상
# 404 페이지를 찾을 수 없음

# response 객체에 text 객체가 존재한다.
html = response.text
# text 객체를 html 변수 안에 담는다
print(html)




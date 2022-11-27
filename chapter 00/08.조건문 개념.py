# 조건문
# : 조건에 따라 실행할 명령이 달라 지는 것

origin_pass = "1234"
input_pass = input("패스워드를 입력하시오: ")

if input_pass == origin_pass:   # 조건 A
    print("로그인 성공")
    print("반갑습니다")
elif input_pass == "" : # 조건 A 가 거짓이면서 조건 B 참
    print("아무것도 입력하지 않았습니다")
else:                   # 조건 A가 거짓이면서 조건 B 가 거짓
    print("로그인 실패")
    print("비밀번호를 확인하세요")
    
# if else  / if    
# 조건 여려개 만드는 경우 elif 추가
'''x = input(" 숫자를 입력하시오 ")
print("입력된 값은", x, "입니다")

'''

# 문제 1. 사용자로부터 두 개의 숫자를 입력 받고 
# 더한 결과를 출력하기

'''a = int(input("첫 번째 숫자를 입력하시오"))
b = int(input("두 번째 숫자를 입력하시오"))
c = a+b;
print(c)
'''
# 문제 2. 사용자로부터 크롤링할 페이지 개수를 입력 받으면
# 메시지를 출력하기
# 자료형변환  int(), str()
a = input("크롤링할 페이지 개수를 입력하시오: ")
# 콤마가 있으면 띄어쓰기 1칸이 추가된다
print("크롤링할 페이지 개수는" , a, "개 입니다.")
print("크롤링할 페이지 개수는 " + a + "개 입니다.")

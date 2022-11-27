# while문
# 조건이 false가 될 때 까지 반복

i = 1
while i<= 10:
    print(f"{i}번째 자동화 작업")
    i = i + 1

while True:
    x = input("종료하려면 exit를 입력하시오 >>>")
    if x == "exit":
        break
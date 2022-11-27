# 1~ 100까지 중 랜덤으로 하나의 번호를 고른다
import random
rn = random.randrange(1, 101, 1)
num = -1
count = 0
while ( rn != num ):
    num = int(input("1 ~ 100 사이의 숫자를 입력하세요 : "))

    if (num > rn):
        print("내리세요")
    elif (num < rn):
        print("올리세요")
    else:
        print("정답")
    count = count + 1


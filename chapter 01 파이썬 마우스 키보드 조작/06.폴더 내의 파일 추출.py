import os

# 현재 폴더 내 모든 파일 출력
file_list = os.listdir('C:/Users/Index/Downloads')

# 반복문 통해 각 파일의 확장자 확인하기
for file in file_list:
    #splittext: 확장자를 추출/잘라낸다

    #name, ext => 언패킹
    # splitext 결과는 tuple 자료형(데이터가 변하지 않음)
    # 언패킹 기능: 각 원소들을 변수에 하나씩 담는다
    name, ext = os.path.splitext(file)
    print(name, ext)


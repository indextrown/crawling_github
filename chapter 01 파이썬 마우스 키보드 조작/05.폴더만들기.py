import os

# 상대 경로
#os.mkdir("테스트000")

# 상대 경로 이용
#os.mkdir('../chapter 00/테스트2')

# 절대 경로 이용
#os.mkdir('c:/Users/Index/PycharmProjects/startproject/000000000')

# 절대 경로 찾기
# 특정 파일 클릭 후 우측클릭 속성 눌러서 위치 복사
# 역슬래시 = 문자열에서 사용하면 이스케이프 문자로 취급됨
# 해결방안1 역슬래시 2번써서 역슬래시를 문자열 취급을 해주던가
#        2 슬래시(/)로 다 바꿔줘야함
#os.mkdir("C:/Users/Index/Downloads/이미징")

# 이스케이프 문자
# \n 한줄 띄우기 \t 탭 \\ 역슬래시 \"큰따옴표

# 폴더가 없을 때만 만들기

#1
if not os.path.exists('C:/Users/Index/Downloads/이미징'):
    os.mkdir("C:/Users/Index/Downloads/이미징")


'''
#2
try:
    os.mkdir("C:/Users/Index/Downloads/이미징")
except:
    print("이미 존재")'''
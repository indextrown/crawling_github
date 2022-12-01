import os
from PIL import Image

# 정리할 확장자
extension_list = ['.jpg', '.png', 'jpeg' ,'gif']

# 정리할 폴더
target = '../chapter 01 파이썬 마우스 키보드 조작/랜덤이미지'

# 만들 폴더
destination = os.path.join(target, '크기변경')

# 폴더가 없다면 만들기
if not os.path.exists(destination):
    os.mkdir(destination)

# 현재 폴더 내 모든 파일 출력
file_list = os.listdir("랜덤이미지")

# 반복문을 통해 각 파일의 확장자를 확인해준다
# splitext 파일 이름이랑 확장자 분리해줌
for file in file_list:
    name, ext = os.path.splitext(file)
    if ext in extension_list:
        # 이미지 열기
        img_path = os.path.join(target, file)
        # 이미지 열기
        img = Image.open(img_path)
        
        # 이미지 크기 수정  0.5 곱하면 50프로 줄어듬
        # 이미지 크기 자체는 소수점 불가하기 때문에 int형으로 강제형변환
        width = int(img.width * 0.5)
        height = int(img.height * 0.5)
        # resize 함수는 튜플 형태로 data를 넘겨줘야함
        # 괄호 너비만큼 resize를 한 후 resize 변수에 담겠다
        resize = img.resize((width, height))
        
        # 이미지 저장
        save_path = os.path.join(destination, file)
        resize.save(save_path)

        


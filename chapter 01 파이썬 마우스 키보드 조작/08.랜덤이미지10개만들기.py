import numpy
from PIL import Image
import os

# PIL 라이브러리에서 Image만 import 하겠다는 뜻
# import PIL이라고 하면
# PIL.Image 이렇게 써야하지만
# from PIL import Image 로 사용하면
# Image로 바로 사용 가능 ==> 가독성

# 만들 폴더 경로(일단 상대경로)
target = "../chapter 01 파이썬 마우스 키보드 조작/랜덤이미지"

# 폴더 만들기
# 만약 해당 경로가 존재하지 않는다면
if not os.path.exists(target):
    os.mkdir(target)
# 총 100번 동안 반복
for i in range (1, 11):
    filename = f"{i}.jpg"

    # 3차원 rgb 랜덤 배열 생성       세로 , 가로 픽셀 개수, 3은 고정
    # red green blue 색상 조합을 만들 때 0 ~ 255숫자가 있음
    rgb_array = numpy.random.rand(720, 1080, 3)* 255
    
    # 이미지 생성
    image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')
    
    # 이미지 저장
    # path.join은 문자와 문자를 / 로 이어준다
    image.save(os.path.join(target, filename))












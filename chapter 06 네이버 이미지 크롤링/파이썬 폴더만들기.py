import os
'''name = input("입력")
img_folder = f'./{name}.사진폴더'

if not os.path.isdir(img_folder): # img폴더가 없으면 생성한다
    os.mkdir(img_folder)
    # 이미지를 url로 다운받는다.
'''
# 폴더 만들기
os.mkdir('img_folder')

#해당 경로에 파일이 있으면 true
print(os.path.exists('img_folder'))

#
if not os.path.isdir('img_folder'):  # img폴더가 없으면 생성한다
    os.mkdir('img_folder')
    # 이미지를 url로 다운받는다.
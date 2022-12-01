import os

# 정리할 확장자 리스트
extension_list = ['.jpg', 'png', '.gif', '.jpg', '.pdf', '.mp4']

# 정리할 폴더
target = "C:/Users/Index/Downloads"

# 만들 폴더
destination = target + "/pdf"

# 폴더가 없다면 만들기
if not os.path.exists(destination):
    os.mkdir(destination)

# 현재 폴더 내 모든 파일 출력
file_list = os.listdir(target)

# 반복문을 통해 각 파일의 확장자를 확인
for file in file_list:
    name, ext = os.path.splitext(file)
    print(name, ext)
    #if ext == 'jpg' or ext =='png':
    if ext in extension_list:
        # join은 /로 이어주는 역할
        source = os.path.join(target, file)
        '''# 파일 이동'''
        os.rename(source, os.path.join(destination, file))
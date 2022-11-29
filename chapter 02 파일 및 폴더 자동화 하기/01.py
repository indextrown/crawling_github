'''import os
path = "C:/Users/Index/Downloads/"
file_lst = os.listdir(path)
category = [] #분류 데이터 저장을 위해 빈 리스트 생성
for file in file_lst:
    #filepath = path + '/' + file
    # print(filepath)
    temp_list = file.split(".")  # 파일명중 "_"로 분리하여 리스트화
    # 분류 리스트
    category.append(temp_list[-1])  # 리스트의 -2 인덱싱 데이터를 category에 추가
    #print(category)

for cat in category:
    try:
        path = "C:/Users/Index/Downloads"
        os.makedirs(path+"/"+cat)
    except:
        pass
folderlist = os.listdir(path)
filelist = os.listdir(path) #이동시킬 파일명들을 리스트화
dict = {}

for file in filelist:

'''





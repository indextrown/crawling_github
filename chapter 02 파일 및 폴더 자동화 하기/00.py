import os


try:
    path1 = "C:/Users/Index/Downloads/이미지 파일"
    path2 = "C:/Users/Index/Downloads/문서 파일"
    path3 = "C:/Users/Index/Downloads/동영상 파일"
    path4 = "C:/Users/Index/Downloads/음악 파일"
    os.mkdir(path1)
    os.mkdir(path2)
    os.mkdir(path3)
    os.mkdir(path4)
except:
    print("이미 파일 존재") # test
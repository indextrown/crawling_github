import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        # 도화지 코드의 이 위치에 아래 코드 한 줄을 추가할 것
        self.setWindowTitle("코딩테스트 GUI")

        # 도화지 코드의 이 위치에 아래 코드 한 줄을 추가할 것
        self.setGeometry(300, 300, 400, 400)  # 차례대로 창위치 x,y, 창크기 x,y

        # 해당 위치에 아래 코드 추가
        self.setWindowIcon(QIcon('icon-0013-sale_102755.png'))


app = QApplication(sys.argv)

window = MyWindow()
# 위의 기본 코드와 다른 점
# QMainWindow 클래스를 상속받은 MyWindow 클래스를 선언
# 그 후 부모클래스를 의미하는 super()메소드와 그 클래스의 속성을 불러오는 __init__ 초기화 메소드 사용
# QMainWindow의 속성이 무엇인지는 모르겠음

window.show()

app.exec_()
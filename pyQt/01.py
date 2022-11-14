# sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈입니다
import sys
# pyqt5 패키지의 qtwidgets 모듈에서 전체를 가져오는 코드
from PyQt5.QtWidgets import *

# QApplication( ) 클래스로 app이란 이름의 객체를 생성하는 코드
# QApplication는 QtWidgets 모듈 안에 존재하는 여러 메소드(함수) 중의 하나이며, PyQt를 사용하면 무조건 써야하는 클래스입니다.
app = QApplication(sys.argv)


# 기능없는 창(window) 만들어보기
# Qwidget( )은 실제로 화면에 보여지는 윈도우를 생성하는 클래스입니다.
# window라는 이름으로 객체를 생성한 후에 show 메소드로 창을 띄워줌
window = QWidget()
window.show( )

# 닫기 버튼을 누를때 까지 계속 실행하는 코드
app.exec_()

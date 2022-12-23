from PyQt5.QtWidgets import *
from  PyQt5 import uic
import sys

UI_PATH = "practice.ui"

# 클래스 정의
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self) # ui 파일 로드

        # 1) 버튼 클릭 이벤트
        # self.객체이름.clicked.connect(self.실행함수이름)
        self.login_btn.clicked.connect(self.login_start)

    def login_start(self):
        print("로그인 버튼 클릭됨")
        # 2) 입력창 텍스트 값 추출
        # self. 객체이름.text()
        input_id = self.id.text()
        input_pw = self.pw.text()
        print("아이디", input_id)
        print("비밀번호", input_pw)

# 좀더 이쁜 형태로 바꿔줌
QApplication.setStyle("fusion")
app = QApplication(sys.argv)

# MainDialog 클래스로부터 main_Dialog만듬
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())



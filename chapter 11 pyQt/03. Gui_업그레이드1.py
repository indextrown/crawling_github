from PyQt5.QtWidgets import *
from  PyQt5 import uic
import sys

UI_PATH = "design.ui"

# 클래스 정의
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self) # ui 파일 로드

# 좀더 이쁜 형태로 바꿔줌
QApplication.setStyle("fusion")
app = QApplication(sys.argv)

# MainDialog 클래스로부터 main_Dialog만듬
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())



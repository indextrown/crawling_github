from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import requests
import json
import os # 경로 관련 모듈

# 절대경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_PATH = "design.ui"
sub_list = ['ㄱ', 'ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ', 'ㅈ' ,'ㅊ','ㅋ','ㅌ','ㅍ','ㅁ']

# 클래스 정의
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(os.path.join(BASE_DIR, UI_PATH), self) # ui 파일 로드
        self.pushButton.clicked.connect(self.search_start)
        self.pushButton_2.clicked.connect(self.search_reset)
        self.pushButton_3.clicked.connect(self.save)
        self.pushButton_4.clicked.connect(self.end)
    def search_start(self):
        self.label_3.setText("자동완성 키워드 추출을 시작합니다...")
        QApplication.processEvents()
        main_keyword = self.lineEdit.text()
        for sub in sub_list:
            keyword = main_keyword + '' + sub
            response = requests.get(f"https://ac.search.naver.com/nx/ac?q={keyword}&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_1")

            str_data = response.text.split("_jsonp_1(")[1][:-1]

            # str_data를 dic_data로 바꿈
            dic_data = json.loads(str_data)

            # dic_data['items'] 는 items키의 값 불러오기
            # print(dic_data['items'][0])

            # 리스트 한칸 없애기(3차원의 0번째 요소 가져오기)
            first_dic_data = dic_data['items'][0]

            for data in first_dic_data:
                self.textBrowser.append(data[0])
        self.label_3.setText("자동완성 키워드 추출이 완료되었습니다...")

    def search_reset(self):
        self.textBrowser.setText("")
        self.lineEdit.setText("")
        self.label_3.setText("리셋되었습니다")

    def save(self):
        result = self.textBrowser.toPlainText()
        f = open(f"{self.lineEdit.text()}_연관검색어.txt", 'w', encoding = 'utf-8')
        f.write(result)
        f.close()
        self.label_3.setText(os.getcwd() + f"\{self.lineEdit.text()}_연관검색어.txt에 저장 되었습니다")

    def end(self):
        sys.exit()

# 좀더 이쁜 형태로 바꿔줌
QApplication.setStyle("fusion")
app = QApplication(sys.argv)

# MainDialog 클래스로부터 main_Dialog만듬
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())



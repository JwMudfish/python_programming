# -*- coding: utf-8 -*-

import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

CalUI = '../_uiFiles/calculator.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(CalUI, self)

        #self.num_pushButton_1.clicked.connect(self.NumClicked)   # 클릭 이벤트 - 함수 연동
        #self.num_pushButton_1.clicked.connect(lambda button=self.num_pushButton_1 : self.NumClicked(button))
        
        # 숫자버튼 - lineedit에 연동
        self.num_pushButton_1.clicked.connect(lambda state, button=self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_2.clicked.connect(lambda state, button=self.num_pushButton_2 : self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button=self.num_pushButton_3 : self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button=self.num_pushButton_4 : self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button=self.num_pushButton_5 : self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button=self.num_pushButton_6 : self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button=self.num_pushButton_7 : self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button=self.num_pushButton_8 : self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button=self.num_pushButton_9 : self.NumClicked(state, button))
        self.num_pushButton_0.clicked.connect(lambda state, button=self.num_pushButton_0 : self.NumClicked(state, button))


        self.sign_pushButton_1.clicked.connect(lambda state, button=self.sign_pushButton_1 : self.NumClicked(state, button))
        self.sign_pushButton_2.clicked.connect(lambda state, button=self.sign_pushButton_2 : self.NumClicked(state, button))
        self.sign_pushButton_3.clicked.connect(lambda state, button=self.sign_pushButton_3 : self.NumClicked(state, button))
        self.sign_pushButton_4.clicked.connect(lambda state, button=self.sign_pushButton_4 : self.NumClicked(state, button))

        self.result_pushButton.clicked.connect(self.MakeResult)
        self.reset_pushButton.clicked.connect(self.Reset)
        self.del_pushButton.clicked.connect(self.Delete)
        self.del_pushButton.setStyleSheet('image:url(../image/delete.png);')
        self.del_pushButton.setStyleSheet(
            '''
            QPushButton{image:url(../image/delete.png); border:0px;}
            QPushButton:hover{image:url(../image/delete_red.png); border:0px;}
            ''')

        self.p_open_pushButton.clicked.connect(lambda state, button=self.p_open_pushButton : self.NumClicked(state, button))
        self.p_close_pushButton.clicked.connect(lambda state, button=self.p_open_pushButton : self.NumClicked(state, button))
        self.dot_pushButton.clicked.connect(lambda state, button=self.dot_pushButton : self.NumClicked(state, button))
        self.per_pushButton.clicked.connect(lambda state, button=self.per_pushButton : self.NumClicked(state, button))

        # del 버튼에 이미지 적용시키기
        #self.del_pushButton.setStyleSheet('image:url(../image/delete.png);')
        #self.del_pushButton.setStyleSheet('image:url(../image/delete.png);')

        #self.setFixedSize(300,300)  # 고정된 사이즈로 크기조절
        #self.lineEdit = QLineEdit(self)   # 글 쓸수있는 칸
        #self.pushButton = QPushButton(self)  # 버튼
        #self.pushButton.move(0,100)

    def NumClicked(self, state, button):  # state라는 깍두기 인자를 넣어줌, 원래는 함수 10개 선언해야 하지만 하나만 선언하고 button 인자를 줌
        #print(self.num_pushButton_1.text())   # text()는 위젯에 적혀있는 문자를 가지고 오는 메서드
        if button == self.per_pushButton:
            now_num_text = '*0.01'
        
        else:
            now_num_text = button.text()
        # lineEdit에 문자 입력시키기
        exist_line_text = self.q_lineEdit.text()
        #now_num_text = button.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text)  # setText - 위젯에 글자 넣는 메서드

    def MakeResult(self):
        try:
            result = eval(self.q_lineEdit.text())   # eval - 문자열로 된 수식을 계산하여 int로 반환
            self.a_lineEdit.setText(str(result))      # lineEdit.text()는 문자열 형식만 받아들이기 때문에 str로 변경해줘야 한다.
        except Exception as e:
            print(e)

    def Reset(self):  # q_lineEdit는 초기화, a_lineEdit 는 초기화 후 0
        self.q_lineEdit.clear()
        self.a_lineEdit.setText('0')

    def Delete(self):
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)


app = QApplication(sys.argv)   # Qapplication - 컴퓨터에 실행시키는 역할
main_dialog = MainDialog()
main_dialog.show()

app.exec_()   # 이벤트 루프로 진입

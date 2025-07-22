from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QPushButton, QLabel, QLineEdit)

from instr import *
from exp import *
from final_win import Final_win

class Test_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
        self.lbl_name = QLabel(txt_name)
        self.input_name = QLineEdit()
        self.lbl_age = QLabel()
        self.input_age = QLineEdit()
        self.input_name.setPlaceholderText(txt_hintname)
        self.input_age.setPlaceholderText(txt_hintage)
        self.lbl_instr1 = QLabel(txt_test1)
        self.btn_start = QPushButton(txt_starttest1)
        self.input_puls1 = QLineEdit()
        self.input_puls1.setPlaceholderText(txt_hintage)
        self.lbl_instr2 = QLabel(txt_test2)
        self.btn_sits = QPushButton(txt_starttest2)
        self.lbl_instr3 = QLabel(txt_test3)
        self.btn_final = QPushButton(txt_starttest3)
        self.input_puls2 = QLineEdit()
        self.input_puls2.setPlaceholderText(txt_hintage)
        self.input_puls3 = QLineEdit()
        self.input_puls3.setPlaceholderText(txt_hintage)
        self.btn_result = QPushButton(txt_sendresults)
        self.lbl_timer = QLabel(txt_timer)
        self.lbl_timer.setFont(QFont('Arial', 36, QFont.Bold))
        self.btn_sits.setDisabled(True)
        self.btn_final.setDisabled(True)
        self.btn_result.setDisabled(True)
        self.input_puls1.setDisabled(True)
        self.input_puls2.setDisabled(True)
        self.input_puls3.setDisabled(True)
        
        self.layout_main = QHBoxLayout()
        self.layout1 = QVBoxLayout()
        self.layout2 = QVBoxLayout()
        self.layout1.addWidget(self.lbl_name, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.input_name, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.lbl_age, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.input_age, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.lbl_instr1, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.btn_start, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.input_puls1, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.lbl_instr2, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.btn_sits, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.lbl_instr3, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.btn_final, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.input_puls2, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.input_puls3, alignment = Qt.AlignLeft)
        self.layout1.addWidget(self.btn_result, alignment = Qt.AlignCenter)
        self.layout2.addWidget(self.lbl_timer, alignment = Qt.AlignCenter)
        self.layout_main.addLayout(self.layout1)
        self.layout_main.addLayout(self.layout2)
        self.setLayout(self.layout_main)
        
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.input_name.text(), self.input_age.text(), self.input_puls1.text(), self.input_puls2.text(), self.input_puls3.text())
        self.fw = Final_win(self.exp)

    def timerTest1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1event)
        self.timer.start(100)

    def timer1event(self):
        global time
        time = time.addSecs(-1)
        self.lbl_timer.setText(time.toString('hh:mm:ss'))
        self.lbl_timer.setFont(QFont('Arial', 36, QFont.Bold))
        self.lbl_timer.setStyleSheet('color: rgb(70, 15, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
            self.btn_sits.setDisabled(False)
            self.input_puls1.setDisabled(False)

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2event)
        self.timer.start(100)

    def timer2event(self):
        global time
        time = time.addSecs(-1)
        self.lbl_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.lbl_timer.setFont(QFont('Arial', 36, QFont.Bold))
        self.lbl_timer.setStyleSheet('color: rgb(70, 15, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
            self.btn_final.setDisabled(False)
            
    def timer_final(self):
        global time
        time = QTime(0, 1, 00)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3event)
        self.timer.start(100)

    def timer3event(self):
        global time
        time = time.addSecs(-1)
        self.lbl_timer.setText(time.toString('hh:mm:ss'))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.lbl_timer.setStyleSheet('color: rgb(0, 255, 0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.lbl_timer.setStyleSheet('color: rgb(0, 0, 255)')
        else:
            self.lbl_timer.setStyleSheet('color: rgb(0, 0, 0)')
        self.lbl_timer.setFont(QFont('Arial', 36, QFont.Bold))
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
            self.btn_result.setDisabled(False)
            self.input_puls2.setDisabled(False)
            self.input_puls3.setDisabled(False)


    def connects(self):
        self.btn_result.clicked.connect(self.next_click)
        self.btn_start.clicked.connect(self.timerTest1)
        self.btn_sits.clicked.connect(self.timer_sits)
        self.btn_final.clicked.connect(self.timer_final)

    
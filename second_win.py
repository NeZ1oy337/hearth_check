from PyQt5.QtCore import Qt
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
    def connects(self):
        self.btn_result.clicked.connect(self.next_click)

    
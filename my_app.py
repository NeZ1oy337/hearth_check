from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QPushButton, QLabel, QLineEdit)

from instr import *
from second_win import *

class Main_win(QWidget):
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
        self.layout_main = QVBoxLayout()
        self.btn = QPushButton(txt_next)
        self.lbl_hi = QLabel(txt_hello)
        self.lbl_inst = QLabel(txt_instruction)
        self.layout_main.addWidget(self.lbl_hi, alignment = Qt.AlignLeft)
        self.layout_main.addWidget(self.lbl_inst, alignment = Qt.AlignLeft)
        self.layout_main.addWidget(self.btn, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_main)


    def connects(self):
        pass

    
app = QApplication([])
main_win = Main_win()

app.exec_()


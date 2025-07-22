from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QPushButton, QLabel)

from instr import *

class Final_win(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
        self.index_text = QLabel(txt_index + str(self.exp.index))
        self.workh_text = QLabel(txt_workheart + results[self.exp.result()])

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)

    def connects(self):
        pass

    
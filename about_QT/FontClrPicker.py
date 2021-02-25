#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore 

class FontClrPicker(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        vbox = QtGui.QVBoxLayout()
        self.setGeometry(300, 300, 250, 220)
        self.setWindowTitle('Font Color Check Dialog')
        button = QtGui.QPushButton('Select Font', self)
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20, 20)
        vbox.addWidget(button)
        button_clr = QtGui.QPushButton('Pick Color')
        button_clr.setFocusPolicy(QtCore.Qt.NoFocus)
        button_clr.move(20,40)
        vbox.addWidget(button_clr)
        self.connect(button, QtCore.SIGNAL('clicked()'), self.showDialog)
        self.connect(button_clr,QtCore.SIGNAL("clicked()"),self.showColor)
        self.f_hbox = QtGui.QHBoxLayout()
        # self.name_l = QtGui.QTextEdit(self)
        self.f_l = QtGui.QLabel("font:  ",self)
        self.f_res_l = QtGui.QLabel('',self)
        self.f_res_l.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.f_hbox.addWidget(self.f_l)
        self.f_hbox.addWidget(self.f_res_l)
        vbox.addLayout(self.f_hbox)
        self.c_hbox = QtGui.QHBoxLayout()
        # self.name_l = QtGui.QTextEdit(self)
        self.c_l = QtGui.QLabel("color:  ", self)
        self.c_res_l = QtGui.QLabel('', self)
        self.c_res_l.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.c_hbox.addWidget(self.c_l)
        self.c_hbox.addWidget(self.c_res_l)
        vbox.addLayout(self.c_hbox)
        # self.name_l.setInputMethodHints()
        self.label = QtGui.QLabel('When you are feeling work hard!\nDon not complain! Just Resign!!', self)
        self.label.setFont(QtGui.QFont("Times",15))
        # self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        # self.label.move(130, 20)

        # self.name_l.move(20,75)
        vbox.addWidget(self.label, 1)
        self.setLayout(vbox)
        
    def showDialog(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            font.setPointSize(15)
            self.label.setFont(font)
            fontInf = QtGui.QFontInfo(font)
            self.f_res_l.setText(fontInf.family())
    def showColor(self):
        color = QtGui.QColorDialog.getColor()
        clr_nm = color.name()
        self.c_res_l.setText(clr_nm)
        self.label.setStyleSheet('color: {}'.format(clr_nm))

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    fd = FontClrPicker()
    fd.show()
    sys.exit(app.exec_())
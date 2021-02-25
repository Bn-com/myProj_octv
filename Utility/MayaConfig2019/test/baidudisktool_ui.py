# -*- coding: utf-8 -*-

# Form implementation generated from reading myuis file 'baidudisktool_ui.myuis'
#
# Created: Mon Feb 25 20:22:01 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(731, 114)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 40, 151, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.AdressTE = QtGui.QTextEdit(Form)
        self.AdressTE.setGeometry(QtCore.QRect(220, 40, 251, 31))
        self.AdressTE.setObjectName(_fromUtf8("AdressTE"))
        self.OPbt = QtGui.QPushButton(Form)
        self.OPbt.setGeometry(QtCore.QRect(500, 40, 75, 23))
        self.OPbt.setObjectName(_fromUtf8("OPbt"))
        self.CPbt = QtGui.QPushButton(Form)
        self.CPbt.setGeometry(QtCore.QRect(610, 40, 75, 23))
        self.CPbt.setObjectName(_fromUtf8("CPbt"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "http://pan.baidu.com/s/", None))
        self.OPbt.setText(_translate("Form", "Open", None))
        self.CPbt.setText(_translate("Form", "Copy", None))


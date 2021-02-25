# -*- coding: utf-8 -*-

# Form implementation generated from reading myuis file 'abcSingleWidget.myuis'
#
# Created: Tue Mar 26 09:22:55 2019
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
        Form.resize(413, 286)
        self.MainFrame = QtGui.QFrame(Form)
        self.MainFrame.setGeometry(QtCore.QRect(0, 20, 401, 251))
        self.MainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.MainFrame.setObjectName(_fromUtf8("MainFrame"))
        self.line = QtGui.QFrame(self.MainFrame)
        self.line.setGeometry(QtCore.QRect(20, 160, 369, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.widget = QtGui.QWidget(self.MainFrame)
        self.widget.setGeometry(QtCore.QRect(20, 180, 371, 61))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.ccPth_bt = QtGui.QPushButton(self.widget)
        self.ccPth_bt.setObjectName(_fromUtf8("ccPth_bt"))
        self.horizontalLayout_2.addWidget(self.ccPth_bt)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.im_cc_bt = QtGui.QPushButton(self.widget)
        self.im_cc_bt.setObjectName(_fromUtf8("im_cc_bt"))
        self.horizontalLayout_3.addWidget(self.im_cc_bt)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.widget1 = QtGui.QWidget(self.MainFrame)
        self.widget1.setGeometry(QtCore.QRect(21, 11, 180, 22))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.widget2 = QtGui.QWidget(self.MainFrame)
        self.widget2.setGeometry(QtCore.QRect(21, 83, 361, 25))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pth_line = QtGui.QLineEdit(self.widget2)
        self.pth_line.setObjectName(_fromUtf8("pth_line"))
        self.horizontalLayout.addWidget(self.pth_line)
        self.cc_pth_bt = QtGui.QPushButton(self.widget2)
        self.cc_pth_bt.setIconSize(QtCore.QSize(16, 16))
        self.cc_pth_bt.setObjectName(_fromUtf8("cc_pth_bt"))
        self.horizontalLayout.addWidget(self.cc_pth_bt)
        self.widget3 = QtGui.QWidget(self.MainFrame)
        self.widget3.setGeometry(QtCore.QRect(21, 41, 367, 22))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.splitter = QtGui.QSplitter(self.widget3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.st_line = QtGui.QLineEdit(self.splitter)
        self.st_line.setObjectName(_fromUtf8("st_line"))
        self.horizontalLayout_4.addWidget(self.splitter)
        self.splitter_2 = QtGui.QSplitter(self.widget3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_3 = QtGui.QLabel(self.splitter_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.end_line = QtGui.QLineEdit(self.splitter_2)
        self.end_line.setObjectName(_fromUtf8("end_line"))
        self.horizontalLayout_4.addWidget(self.splitter_2)
        self.widget4 = QtGui.QWidget(self.MainFrame)
        self.widget4.setGeometry(QtCore.QRect(21, 124, 361, 25))
        self.widget4.setObjectName(_fromUtf8("widget4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.ex_cc_bt = QtGui.QPushButton(self.widget4)
        self.ex_cc_bt.setObjectName(_fromUtf8("ex_cc_bt"))
        self.horizontalLayout_5.addWidget(self.ex_cc_bt)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.ccPth_bt.setText(_translate("Form", "PushButton", None))
        self.im_cc_bt.setText(_translate("Form", "PushButton", None))
        self.label.setText(_translate("Form", "选择要输出缓存的模型：", None))
        self.cc_pth_bt.setText(_translate("Form", "path", None))
        self.label_2.setText(_translate("Form", "start frame", None))
        self.label_3.setText(_translate("Form", "end   frame", None))
        self.ex_cc_bt.setText(_translate("Form", "Export Cache & record file", None))


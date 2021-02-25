# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abcSingleWidget.ui'
#
# Created: Wed Mar 27 16:27:22 2019
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

class Ui_abcS_form(object):
    def setupUi(self, abcS_form):
        abcS_form.setObjectName(_fromUtf8("abcS_form"))
        abcS_form.resize(436, 368)
        self.abcFrm = QtGui.QFrame(abcS_form)
        self.abcFrm.setGeometry(QtCore.QRect(10, 20, 410, 300))
        self.abcFrm.setMinimumSize(QtCore.QSize(410, 300))
        self.abcFrm.setMaximumSize(QtCore.QSize(410, 300))
        self.abcFrm.setFrameShape(QtGui.QFrame.Panel)
        self.abcFrm.setFrameShadow(QtGui.QFrame.Raised)
        self.abcFrm.setObjectName(_fromUtf8("abcFrm"))
        self.line = QtGui.QFrame(self.abcFrm)
        self.line.setGeometry(QtCore.QRect(20, 160, 369, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.layoutWidget = QtGui.QWidget(self.abcFrm)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 180, 371, 106))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.im_lst_tx = QtGui.QTextEdit(self.layoutWidget)
        self.im_lst_tx.setMaximumSize(QtCore.QSize(16777215, 50))
        self.im_lst_tx.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.im_lst_tx.setReadOnly(False)
        self.im_lst_tx.setObjectName(_fromUtf8("im_lst_tx"))
        self.horizontalLayout_2.addWidget(self.im_lst_tx)
        self.sel_cc_bt = QtGui.QPushButton(self.layoutWidget)
        self.sel_cc_bt.setObjectName(_fromUtf8("sel_cc_bt"))
        self.horizontalLayout_2.addWidget(self.sel_cc_bt)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.im_cc_bt = QtGui.QPushButton(self.layoutWidget)
        self.im_cc_bt.setObjectName(_fromUtf8("im_cc_bt"))
        self.horizontalLayout_3.addWidget(self.im_cc_bt)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.layoutWidget1 = QtGui.QWidget(self.abcFrm)
        self.layoutWidget1.setGeometry(QtCore.QRect(21, 11, 180, 22))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.layoutWidget2 = QtGui.QWidget(self.abcFrm)
        self.layoutWidget2.setGeometry(QtCore.QRect(21, 83, 361, 25))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pth_line = QtGui.QLineEdit(self.layoutWidget2)
        self.pth_line.setObjectName(_fromUtf8("pth_line"))
        self.horizontalLayout.addWidget(self.pth_line)
        self.cc_pth_bt = QtGui.QPushButton(self.layoutWidget2)
        self.cc_pth_bt.setIconSize(QtCore.QSize(16, 16))
        self.cc_pth_bt.setObjectName(_fromUtf8("cc_pth_bt"))
        self.horizontalLayout.addWidget(self.cc_pth_bt)
        self.layoutWidget3 = QtGui.QWidget(self.abcFrm)
        self.layoutWidget3.setGeometry(QtCore.QRect(21, 41, 367, 22))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.splitter = QtGui.QSplitter(self.layoutWidget3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.st_line = QtGui.QLineEdit(self.splitter)
        self.st_line.setObjectName(_fromUtf8("st_line"))
        self.horizontalLayout_4.addWidget(self.splitter)
        self.splitter_2 = QtGui.QSplitter(self.layoutWidget3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_3 = QtGui.QLabel(self.splitter_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.end_line = QtGui.QLineEdit(self.splitter_2)
        self.end_line.setObjectName(_fromUtf8("end_line"))
        self.horizontalLayout_4.addWidget(self.splitter_2)
        self.layoutWidget4 = QtGui.QWidget(self.abcFrm)
        self.layoutWidget4.setGeometry(QtCore.QRect(21, 124, 361, 25))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.rc_bt = QtGui.QPushButton(self.layoutWidget4)
        self.rc_bt.setObjectName(_fromUtf8("rc_bt"))
        self.horizontalLayout_5.addWidget(self.rc_bt)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.ex_cc_bt = QtGui.QPushButton(self.layoutWidget4)
        self.ex_cc_bt.setObjectName(_fromUtf8("ex_cc_bt"))
        self.horizontalLayout_5.addWidget(self.ex_cc_bt)

        self.retranslateUi(abcS_form)
        QtCore.QMetaObject.connectSlotsByName(abcS_form)

    def retranslateUi(self, abcS_form):
        abcS_form.setWindowTitle(_translate("abcS_form", "Form", None))
        self.sel_cc_bt.setText(_translate("abcS_form", "选择：缓存 及\n"
"记录物体的文件", None))
        self.im_cc_bt.setText(_translate("abcS_form", "importCache", None))
        self.label.setText(_translate("abcS_form", "选择要输出缓存的模型：", None))
        self.cc_pth_bt.setText(_translate("abcS_form", "path", None))
        self.label_2.setText(_translate("abcS_form", "start frame", None))
        self.label_3.setText(_translate("abcS_form", "end   frame", None))
        self.rc_bt.setText(_translate("abcS_form", "只记录缓存物体", None))
        self.ex_cc_bt.setText(_translate("abcS_form", "Export Cache & record file", None))


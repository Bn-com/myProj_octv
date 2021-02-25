# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doWin.ui'
#
# Created: Wed Mar 27 18:24:23 2019
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

class Ui_doWin(object):
    def setupUi(self, doWin):
        doWin.setObjectName(_fromUtf8("doWin"))
        doWin.resize(382, 240)
        self.centralwidget = QtGui.QWidget(doWin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.add_bt = QtGui.QPushButton(self.centralwidget)
        self.add_bt.setGeometry(QtCore.QRect(270, 60, 75, 23))
        self.add_bt.setObjectName(_fromUtf8("add_bt"))
        self.cmdStr_l = QtGui.QTextEdit(self.centralwidget)
        self.cmdStr_l.setGeometry(QtCore.QRect(40, 10, 301, 41))
        self.cmdStr_l.setObjectName(_fromUtf8("cmdStr_l"))
        self.ref_rb = QtGui.QRadioButton(self.centralwidget)
        self.ref_rb.setGeometry(QtCore.QRect(160, 170, 89, 16))
        self.ref_rb.setObjectName(_fromUtf8("ref_rb"))
        self.mod_grp = QtGui.QButtonGroup(doWin)
        self.mod_grp.setObjectName(_fromUtf8("mod_grp"))
        self.mod_grp.addButton(self.ref_rb)
        self.im_rb = QtGui.QRadioButton(self.centralwidget)
        self.im_rb.setGeometry(QtCore.QRect(60, 170, 89, 16))
        self.im_rb.setObjectName(_fromUtf8("im_rb"))
        self.mod_grp.addButton(self.im_rb)
        self.hold_bx = QtGui.QScrollArea(self.centralwidget)
        self.hold_bx.setGeometry(QtCore.QRect(40, 110, 261, 21))
        self.hold_bx.setWidgetResizable(True)
        self.hold_bx.setObjectName(_fromUtf8("hold_bx"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 19))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.bx_rf_rb = QtGui.QRadioButton(self.scrollAreaWidgetContents)
        self.bx_rf_rb.setGeometry(QtCore.QRect(0, 0, 89, 16))
        self.bx_rf_rb.setObjectName(_fromUtf8("bx_rf_rb"))
        self.bx_im_rb = QtGui.QRadioButton(self.scrollAreaWidgetContents)
        self.bx_im_rb.setGeometry(QtCore.QRect(120, 0, 89, 16))
        self.bx_im_rb.setObjectName(_fromUtf8("bx_im_rb"))
        self.hold_bx.setWidget(self.scrollAreaWidgetContents)
        doWin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(doWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        doWin.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(doWin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        doWin.setStatusBar(self.statusbar)

        self.retranslateUi(doWin)
        QtCore.QMetaObject.connectSlotsByName(doWin)

    def retranslateUi(self, doWin):
        doWin.setWindowTitle(_translate("doWin", "MainWindow", None))
        self.add_bt.setText(_translate("doWin", "add", None))
        self.ref_rb.setText(_translate("doWin", "reference", None))
        self.im_rb.setText(_translate("doWin", "import", None))
        self.bx_rf_rb.setText(_translate("doWin", "reference", None))
        self.bx_im_rb.setText(_translate("doWin", "import", None))


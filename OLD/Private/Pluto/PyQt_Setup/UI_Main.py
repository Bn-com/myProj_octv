# -*- coding: utf-8 -*-

# Form implementation generated from reading myuis file 'UI_Main.myuis'
#
# Created: Thu Jul 16 14:31:31 2015
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.centralLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.centralLayout.setSpacing(3)
        self.centralLayout.setMargin(3)
        self.centralLayout.setObjectName(_fromUtf8("centralLayout"))
        self.frame_left = QtGui.QFrame(self.centralwidget)
        self.frame_left.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_left.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_left.setObjectName(_fromUtf8("frame_left"))
        self.Layout_left = QtGui.QVBoxLayout(self.frame_left)
        self.Layout_left.setSpacing(3)
        self.Layout_left.setMargin(3)
        self.Layout_left.setObjectName(_fromUtf8("Layout_left"))
        self.label = QtGui.QLabel(self.frame_left)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.Layout_left.addWidget(self.label)
        self.centralLayout.addWidget(self.frame_left)
        self.frame_right = QtGui.QFrame(self.centralwidget)
        self.frame_right.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_right.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_right.setObjectName(_fromUtf8("frame_right"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_right)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setMargin(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.QDoubleSpinBox_tx = QtGui.QDoubleSpinBox(self.frame_right)
        self.QDoubleSpinBox_tx.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.QDoubleSpinBox_tx.setDecimals(2)
        self.QDoubleSpinBox_tx.setMinimum(-999999999.0)
        self.QDoubleSpinBox_tx.setMaximum(999999999.0)
        self.QDoubleSpinBox_tx.setObjectName(_fromUtf8("QDoubleSpinBox_tx"))
        self.gridLayout.addWidget(self.QDoubleSpinBox_tx, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_right)
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame_right)
        self.label_3.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame_right)
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.QDoubleSpinBox_ty = QtGui.QDoubleSpinBox(self.frame_right)
        self.QDoubleSpinBox_ty.setMinimum(-999999999.0)
        self.QDoubleSpinBox_ty.setMaximum(999999999.0)
        self.QDoubleSpinBox_ty.setObjectName(_fromUtf8("QDoubleSpinBox_ty"))
        self.gridLayout.addWidget(self.QDoubleSpinBox_ty, 2, 2, 1, 1)
        self.QDoubleSpinBox_tz = QtGui.QDoubleSpinBox(self.frame_right)
        self.QDoubleSpinBox_tz.setMinimum(-999999999.0)
        self.QDoubleSpinBox_tz.setMaximum(999999999.0)
        self.QDoubleSpinBox_tz.setObjectName(_fromUtf8("QDoubleSpinBox_tz"))
        self.gridLayout.addWidget(self.QDoubleSpinBox_tz, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.QCheckBox_autocam = QtGui.QCheckBox(self.frame_right)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QCheckBox_autocam.setFont(font)
        self.QCheckBox_autocam.setChecked(True)
        self.QCheckBox_autocam.setObjectName(_fromUtf8("QCheckBox_autocam"))
        self.verticalLayout_2.addWidget(self.QCheckBox_autocam)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.QPushButton_CMD = QtGui.QPushButton(self.frame_right)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QPushButton_CMD.setFont(font)
        self.QPushButton_CMD.setObjectName(_fromUtf8("QPushButton_CMD"))
        self.verticalLayout_2.addWidget(self.QPushButton_CMD)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.centralLayout.addWidget(self.frame_right)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "测试表情面板", None))
        self.label.setText(_translate("MainWindow", "---------------------------标题---------------------------", None))
        self.label_2.setText(_translate("MainWindow", " TX:", None))
        self.label_3.setText(_translate("MainWindow", " TY: ", None))
        self.label_4.setText(_translate("MainWindow", " TZ: ", None))
        self.QCheckBox_autocam.setText(_translate("MainWindow", "自动切换摄像机", None))
        self.QPushButton_CMD.setText(_translate("MainWindow", "按钮", None))


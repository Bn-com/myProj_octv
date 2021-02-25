# -*- coding: utf-8 -*-

# Form implementation generated from reading myuis file 'UI.myuis'
#
# Created: Thu Mar 17 09:13:25 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_batch_playblast_MainWindow(object):
    def setupUi(self, batch_playblast_MainWindow):
        batch_playblast_MainWindow.setObjectName("batch_playblast_MainWindow")
        batch_playblast_MainWindow.resize(568, 291)
        self.centralwidget = QtGui.QWidget(batch_playblast_MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.QL_list = QtGui.QListWidget(self.centralwidget)
        self.QL_list.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.QL_list.setObjectName("QL_list")
        self.horizontalLayout.addWidget(self.QL_list)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.QB_add = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.QB_add.setFont(font)
        self.QB_add.setObjectName("QB_add")
        self.verticalLayout.addWidget(self.QB_add)
        self.QB_del = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.QB_del.setFont(font)
        self.QB_del.setObjectName("QB_del")
        self.verticalLayout.addWidget(self.QB_del)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.QB_start = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.QB_start.setFont(font)
        self.QB_start.setObjectName("QB_start")
        self.verticalLayout.addWidget(self.QB_start)
        self.horizontalLayout.addLayout(self.verticalLayout)
        batch_playblast_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(batch_playblast_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(batch_playblast_MainWindow)

    def retranslateUi(self, batch_playblast_MainWindow):
        batch_playblast_MainWindow.setWindowTitle(QtGui.QApplication.translate("batch_playblast_MainWindow", "批量PlayBlast", None, QtGui.QApplication.UnicodeUTF8))
        self.QB_add.setText(QtGui.QApplication.translate("batch_playblast_MainWindow", "添加", None, QtGui.QApplication.UnicodeUTF8))
        self.QB_del.setText(QtGui.QApplication.translate("batch_playblast_MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.QB_start.setText(QtGui.QApplication.translate("batch_playblast_MainWindow", "开始", None, QtGui.QApplication.UnicodeUTF8))


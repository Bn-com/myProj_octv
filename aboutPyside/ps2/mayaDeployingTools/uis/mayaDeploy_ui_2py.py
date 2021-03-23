# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mayaDeploy_ui.ui'
#
# Created: Tue Mar 23 11:24:13 2021
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 465)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_new = QtGui.QRadioButton(self.frame_2)
        self.rb_new.setChecked(True)
        self.rb_new.setObjectName("rb_new")
        self.verticalLayout.addWidget(self.rb_new)
        self.rb_old = QtGui.QRadioButton(self.frame_2)
        self.rb_old.setObjectName("rb_old")
        self.verticalLayout.addWidget(self.rb_old)
        self.rb_def = QtGui.QRadioButton(self.frame_2)
        self.rb_def.setObjectName("rb_def")
        self.verticalLayout.addWidget(self.rb_def)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 3)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chbx_16 = QtGui.QCheckBox(self.frame)
        self.chbx_16.setChecked(True)
        self.chbx_16.setObjectName("chbx_16")
        self.horizontalLayout.addWidget(self.chbx_16)
        self.chbx_oth = QtGui.QCheckBox(self.frame)
        self.chbx_oth.setChecked(True)
        self.chbx_oth.setObjectName("chbx_oth")
        self.horizontalLayout.addWidget(self.chbx_oth)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 3)

        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.pb_run = QtGui.QPushButton(self.centralwidget)
        self.pb_run.setObjectName("pb_run")
        self.gridLayout.addWidget(self.pb_run, 2, 2, 1, 1)


        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")

        self.gridLayout.addWidget(self.frame_3, 3, 0, 1, 3)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.rb_old, QtCore.SIGNAL("toggled(bool)"), self.chbx_oth.setChecked)
        QtCore.QObject.connect(self.chbx_oth, QtCore.SIGNAL("toggled(bool)"), self.rb_new.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Maya Deploying", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_new.setText(QtGui.QApplication.translate("MainWindow", "新配置方式（所有版本maya)", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_old.setText(QtGui.QApplication.translate("MainWindow", "旧配置方式(只适用于2016)", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_def.setText(QtGui.QApplication.translate("MainWindow", "maya 默认配置\n"
"备份当前maya配置文件夹\n"
"并配置为默认环境）", None, QtGui.QApplication.UnicodeUTF8))
        self.chbx_16.setText(QtGui.QApplication.translate("MainWindow", "Maya2106", None, QtGui.QApplication.UnicodeUTF8))
        self.chbx_oth.setText(QtGui.QApplication.translate("MainWindow", "其他版本", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_run.setText(QtGui.QApplication.translate("MainWindow", "配置", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))


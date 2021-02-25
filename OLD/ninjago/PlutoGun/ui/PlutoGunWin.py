# -*- coding: utf-8 -*-

# Form implementation generated from reading myuis file 'PlutoGunWin.myuis'
#
# Created: Fri Oct 30 19:06:16 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PlutoGun(object):
    def setupUi(self, PlutoGun):
        PlutoGun.setObjectName("PlutoGun")
        PlutoGun.setEnabled(True)
        PlutoGun.resize(1017, 599)
        PlutoGun.setMinimumSize(QtCore.QSize(0, 0))
        PlutoGun.setStyleSheet("QMainWindow{\n"
"background: url(:/myuis/StarWar.png);\n"
"\n"
"}\n"
"")
        self.CenterWidget = QtGui.QWidget(PlutoGun)
        self.CenterWidget.setAutoFillBackground(False)
        self.CenterWidget.setStyleSheet("background-color:transparent;\n"
"border-style: solid;")
        self.CenterWidget.setObjectName("CenterWidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.CenterWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtGui.QSplitter(self.CenterWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget_left = QtGui.QWidget(self.splitter)
        self.widget_left.setObjectName("widget_left")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_left)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Left_Layout = QtGui.QVBoxLayout()
        self.Left_Layout.setObjectName("Left_Layout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Low_High = QtGui.QPushButton(self.widget_left)
        self.Low_High.setStyleSheet("border-width: 1px;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-radius: 2px;")
        self.Low_High.setObjectName("Low_High")
        self.gridLayout.addWidget(self.Low_High, 1, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.widget_left)
        self.comboBox.setStyleSheet("border-width: 1px;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-radius: 2px;\n"
"background-color:rgb(27,27, 27);")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.Refresh = QtGui.QPushButton(self.widget_left)
        self.Refresh.setStyleSheet("border-width: 1px;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-radius: 2px;")
        self.Refresh.setObjectName("Refresh")
        self.gridLayout.addWidget(self.Refresh, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 4)
        self.Left_Layout.addLayout(self.gridLayout)
        self.tmp_label = QtGui.QLabel(self.widget_left)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setUnderline(False)
        font.setBold(True)
        self.tmp_label.setFont(font)
        self.tmp_label.setStyleSheet("color:rgb(255, 255, 0);")
        self.tmp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tmp_label.setObjectName("tmp_label")
        self.Left_Layout.addWidget(self.tmp_label)
        self.Left_Layout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.Left_Layout)
        self.widget_right = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_right.sizePolicy().hasHeightForWidth())
        self.widget_right.setSizePolicy(sizePolicy)
        self.widget_right.setStyleSheet("border-width: 1px;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-radius: 6px;")
        self.widget_right.setObjectName("widget_right")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableView = My_TableView(self.widget_right)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalSlider = QtGui.QSlider(self.widget_right)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 60))
        self.horizontalSlider.setStyleSheet("            QSlider::groove:horizontal {\n"
"                 border: 1px inset qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #565656, stop:1 #848484);\n"
"                 border-radius: 6px;\n"
"                 height: 10px;\n"
"                 background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #848484, stop:1 #919191);\n"
"                 margin: 2px 6px;\n"
"             }\n"
"\n"
"             QSlider::handle:horizontal {\n"
"                 background-color: rgba(0,0,0,0);\n"
"                 image: url(:/myuis/slider_knob.png);\n"
"                 border: 0px;\n"
"                 width: 40px;\n"
"                 margin: -10px; \n"
"                 border-radius:10px;\n"
"             }")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(9)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setProperty("value", 5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.widget_right)
        self.groupBox.setMinimumSize(QtCore.QSize(65, 80))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.RedButton = QtGui.QRadioButton(self.groupBox)
        self.RedButton.setGeometry(QtCore.QRect(7, 16, 51, 17))
        self.RedButton.setStyleSheet("color:rgb(255, 0, 0);background:rgb(150, 150, 150);")
        self.RedButton.setChecked(True)
        self.RedButton.setObjectName("RedButton")
        self.BlueButton = QtGui.QRadioButton(self.groupBox)
        self.BlueButton.setGeometry(QtCore.QRect(7, 56, 51, 17))
        self.BlueButton.setStyleSheet("color:rgb(0, 0, 255);\n"
"background:rgb(150, 150, 150);")
        self.BlueButton.setObjectName("BlueButton")
        self.GreenButton = QtGui.QRadioButton(self.groupBox)
        self.GreenButton.setGeometry(QtCore.QRect(7, 36, 51, 17))
        self.GreenButton.setStyleSheet("color:rgb(0, 255, 0);\n"
"background:rgb(150, 150, 150);")
        self.GreenButton.setObjectName("GreenButton")
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.widget_right)
        self.lcdNumber.setMinimumSize(QtCore.QSize(40, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setMode(QtGui.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 5)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 0, 2, 1, 1)
        self.Shoot_Gun = QtGui.QToolButton(self.widget_right)
        self.Shoot_Gun.setMinimumSize(QtCore.QSize(60, 60))
        self.Shoot_Gun.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.Shoot_Gun.setFont(font)
        self.Shoot_Gun.setStyleSheet("color:rgb(255, 0, 0);\n"
"border-image: url(:/myuis/slider_knob.png);\n"
"")
        self.Shoot_Gun.setObjectName("Shoot_Gun")
        self.gridLayout_2.addWidget(self.Shoot_Gun, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.splitter)
        PlutoGun.setCentralWidget(self.CenterWidget)

        self.retranslateUi(PlutoGun)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL("valueChanged(int)"), self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(PlutoGun)

    def retranslateUi(self, PlutoGun):
        PlutoGun.setWindowTitle(QtGui.QApplication.translate("PlutoGun", "PlutoGun", None, QtGui.QApplication.UnicodeUTF8))
        self.Low_High.setText(QtGui.QApplication.translate("PlutoGun", "LOW  /  HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.Refresh.setText(QtGui.QApplication.translate("PlutoGun", "REFRESH", None, QtGui.QApplication.UnicodeUTF8))
        self.Refresh.setProperty("-command", QtGui.QApplication.translate("PlutoGun", "\"print \\\"s\\\"\"", None, QtGui.QApplication.UnicodeUTF8))
        self.tmp_label.setText(QtGui.QApplication.translate("PlutoGun", "No PlutoGun System\'s Machine", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("PlutoGun", "Laser Color", None, QtGui.QApplication.UnicodeUTF8))
        self.RedButton.setText(QtGui.QApplication.translate("PlutoGun", "Red", None, QtGui.QApplication.UnicodeUTF8))
        self.BlueButton.setText(QtGui.QApplication.translate("PlutoGun", "Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.GreenButton.setText(QtGui.QApplication.translate("PlutoGun", "Green", None, QtGui.QApplication.UnicodeUTF8))
        self.Shoot_Gun.setText(QtGui.QApplication.translate("PlutoGun", "Shoot", None, QtGui.QApplication.UnicodeUTF8))

from My_TableView import My_TableView
import resources_rc

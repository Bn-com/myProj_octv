# -*- coding: utf-8 -*-

# Form implementation generated from reading myuis file 'CameraShakeLibrary_MW.myuis'
#
# Created: Wed Jul 05 14:44:01 2017
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
        MainWindow.resize(714, 576)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tb_disaster = QtGui.QWidget()
        self.tb_disaster.setObjectName(_fromUtf8("tb_disaster"))
        self.listView = QtGui.QListView(self.tb_disaster)
        self.listView.setGeometry(QtCore.QRect(210, 20, 451, 471))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        self.listView.setFont(font)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.scrollArea = QtGui.QScrollArea(self.tb_disaster)
        self.scrollArea.setGeometry(QtCore.QRect(20, 40, 171, 401))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 169, 399))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.pb_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pb_2.setGeometry(QtCore.QRect(30, 200, 101, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        self.pb_2.setFont(font)
        self.pb_2.setObjectName(_fromUtf8("pb_2"))
        self.pb_3 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pb_3.setGeometry(QtCore.QRect(30, 290, 101, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        self.pb_3.setFont(font)
        self.pb_3.setObjectName(_fromUtf8("pb_3"))
        self.pb_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pb_1.setGeometry(QtCore.QRect(30, 110, 101, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        self.pb_1.setFont(font)
        self.pb_1.setObjectName(_fromUtf8("pb_1"))
        self.pb_0 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pb_0.setGeometry(QtCore.QRect(30, 20, 101, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        self.pb_0.setFont(font)
        self.pb_0.setObjectName(_fromUtf8("pb_0"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtGui.QLabel(self.tb_disaster)
        self.label.setGeometry(QtCore.QRect(270, 70, 361, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tb_disaster, _fromUtf8(""))
        self.tb_chase = QtGui.QWidget()
        self.tb_chase.setObjectName(_fromUtf8("tb_chase"))
        self.listView_2 = QtGui.QListView(self.tb_chase)
        self.listView_2.setGeometry(QtCore.QRect(210, 10, 441, 471))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.tabWidget.addTab(self.tb_chase, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.menuFile.addAction(self.actionImport)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pb_2.setText(_translate("MainWindow", "爆炸", None))
        self.pb_3.setText(_translate("MainWindow", "碰撞", None))
        self.pb_1.setText(_translate("MainWindow", "崩塌", None))
        self.pb_0.setText(_translate("MainWindow", "洪水", None))
        self.label.setText(_translate("MainWindow", "The camera shaked in the deluge", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_disaster), _translate("MainWindow", " 灾难", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_chase), _translate("MainWindow", "追逐", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.actionImport.setText(_translate("MainWindow", "import...", None))


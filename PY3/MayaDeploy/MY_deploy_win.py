# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mayaDeploy_win.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys,os,re,glob,subprocess
import qdarkstyle
# class MainWindow(QMainWindow):
#
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(250, 171)
        # MainWindow.setWindowTitle("Deploy Maya")
        # self.mwin = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.font = QFont()
        self.font.setPointSize(10)
        # f_sz = self.font.pointSize()
        # print(f_sz)
        self.comboBox.setFont(self.font)
        self.comboBox.setFixedSize(200,35)

        self.verticalLayout_2.addWidget(self.comboBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(120, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70,110,75,23))
        # self.pushButton.setMaximumSize(200,30)
        # self.pushButton.setMinimumSize(150,25)
        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(120, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 70, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

        # MainWindow.setStyleSheet("""
        #         # color: rgba(237,174,28,100%);
        #         background-color: rgba(0,0,0,100%);
        #         text-align: center;
        #         border-radius: 150px;
        #         border: 1px solid rgba(237,174,28,100%);
        #         padding: 0px;
        #         """)
        self.btnStylSheet = 'border:0.5px solid gray;border-radius:4px'
        tstStyle1 = 'border:0.8px solid gray;border-radius:4px;max-width:69px;max-height:20px;min-width:65px;min-height:20px'
        self.pushButton.setStyleSheet(tstStyle1)
        MainWindow.setFixedSize(MainWindow.size())
        self.retranslateUi(MainWindow)
        self.config_combox()
        self.pushButton.clicked.connect(lambda :self.bt_cmd(MainWindow))
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def config_combox(self):
        # file_path = __file__
        file_path = os.path.abspath(sys.argv[0])
        self.file_dir = os.path.dirname(file_path)
        # self.file_dir = r"F:\development\myProj\Utility\MayaDeploy\dist"
        # print(self.file_dir)
        my_folds = glob.glob("{}/maya*".format(self.file_dir))
        for e_f in my_folds:
            folder_nm = os.path.basename(e_f)
            self.comboBox.addItem(folder_nm)
    def bt_cmd(self,MainWindow):
        get_vs = self.comboBox.currentText()
        vs_fold = os.path.normpath(os.path.join(self.file_dir,get_vs))
        ex_bat_f = glob.glob("{}/*.bat".format(vs_fold))[0]
        # print(ex_bat_f)
        subprocess.call(ex_bat_f)
        # self.comboBox
        # self.mwin.close()
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Maya Deply", u"Maya Deploy", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
    # retranslateUi


class ControlMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(ControlMainWindow,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet('QMainWindow{border; 1px solid black;}')
    win = ControlMainWindow()
    # win.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
    # win.hide()
    # win.setFixedSize(win.size())
    win.show()
    sys.exit(app.exec_())
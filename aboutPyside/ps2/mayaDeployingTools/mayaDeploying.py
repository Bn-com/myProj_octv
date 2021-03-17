#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = mayaDeploying
__author__ = zhangben 
__mtime__ = 2021/3/15 : 16:55
__description__: 

THEOREM: A good programmer should wipe the butts of his predecessors in an amicable way,
    instead of reinventing a new butt.
        As long as this , code is far away from bugs, and with the god animal protecting
            I love animals. They taste delicious.
"""
import re,os,sys
try:
    from PySide.QtGui import *
    from PySide.QtCore import *
    from PySide.QtUiTools import QUiLoader
    import pysideuic as uic

except:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtUiTools import QUiLoader
    import pyside2uic as uic
# from PySide.QtGui import *
# from PySide.QtCore import *
# from PySide.QtUiTools import QUiLoader
# import pysideuic as uic
import deployProc,resultDialog


#  ============= ===live template require variables =====================
#  m  ayaDeploying M MayaDeploying || MayaDeploying  ayadeploying
class MayaDeploying_Ui(QMainWindow):
    def __init__(self,parent=None):
        super(MayaDeploying_Ui,self).__init__(parent)
        self.setObjectName("MayaDeploying_mainWin")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_run = QPushButton(self.centralwidget)
        self.pb_run.setObjectName("pb_run")
        self.gridLayout.addWidget(self.pb_run, 2, 1, 1, 1)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chbx_16 = QCheckBox(self.frame)
        self.chbx_16.setChecked(True)
        self.chbx_16.setObjectName("chbx_16")
        self.horizontalLayout.addWidget(self.chbx_16)
        self.chbx_oth = QCheckBox(self.frame)
        self.chbx_oth.setChecked(True)
        self.chbx_oth.setObjectName("chbx_oth")
        self.horizontalLayout.addWidget(self.chbx_oth)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btgrp = QButtonGroup(self.frame_2)
        self.rb_new = QRadioButton()
        self.rb_new.setChecked(True)
        self.rb_new.setObjectName("rb_new")
        self.verticalLayout.addWidget(self.rb_new)
        self.rb_old = QRadioButton()
        self.rb_old.setObjectName("rb_old")
        self.verticalLayout.addWidget(self.rb_old)
        self.rb_def = QRadioButton()
        self.rb_def.setObjectName("rb_def")
        self.verticalLayout.addWidget(self.rb_def)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 2)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout.addWidget(self.frame_3, 3, 0, 1, 2)


        self.btgrp.addButton(self.rb_new)
        self.btgrp.addButton(self.rb_old)
        self.btgrp.addButton(self.rb_def)


        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 211, 23))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QObject.connect(self.chbx_oth, SIGNAL("toggled(bool)"), self.rb_old.setDisabled)
        QObject.connect(self.rb_old, SIGNAL("toggled(bool)"), self.chbx_oth.setDisabled)
        QObject.connect(self.rb_old,SIGNAL("toggled(bool)"),self.chbx_oth.setChecked(False))
        QMetaObject.connectSlotsByName(self)
        #==setup ui
        self.setupUI()
        #=============================
        self.resDia = None
    def retranslateUi(self):
        self.pb_run.setText(u"配置")
        self.chbx_16.setText("Maya2106")
        self.chbx_oth.setText(u"其他版本")
        self.rb_new.setText(u"新配置方式（所有版本maya)")
        self.rb_old.setText(u"旧配置方式(只适用于2016)")
        self.rb_def.setText(u"maya 默认配置\n备份当前maya配置文件夹\n并配置为默认环境")
        self.setWindowTitle(u"Maya 配置")
    def setupUI(self):
        self.pb_run.clicked.connect(self.cmd_bt_run)
        self._setPlatter()
    def _setPlatter(self):
        # self.setStyle("Windows")
        # self.setStyle(QStyleFactory.create('Windows'))
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(1, 22, 39))
        # palette.setColor(QPalette.Window, QColor(33, 33, 33))
        palette.setColor(QPalette.WindowText, QColor(255, 128, 0))
        # palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.Base, QColor(33, 50, 63))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.black)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, QColor(255, 128, 0))
        # palette.setColor(QPalette.Button, QColor(0, 0, 0))
        palette.setColor(QPalette.ButtonText, QColor(88, 155, 122))
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(127, 235, 255))
        self.setPalette(palette)
    def cmd_bt_run(self):
        self._show_resDialog()
        mode_dict = {-2:'new',-3:'obsolete',-4:'default'}
        mode = mode_dict[self.btgrp.checkedId()]
        if self.chbx_16.isChecked():
            mayaversion = '2016'
            dpl = deployProc.DeployProc(mayaversion)
            dpl.mode = mode
            dpl.run()
        print("??")
    def _show_resDialog(self,redirect=True,close=None,clear=None):
        if not self.resDia:
            self.resDia =resultDialog.ResultDialog(self.frame_3)
            if redirect:
                if isinstance(redirect,int):
                    self.resDia.redirectOPT()
                elif isinstance(redirect,(str)):
                    self.resDia.opt2txt(redirect)
            self.resDia.resize(500,400)
            self.resDia.move(600,300)
            self.resDia.show()
        else:
            if clear:
                self.resDia.txtedit.clear()
                return
            if close:
                self.resDia.close()
                self.resDia.deleteLater()
                self.resDia = None
            else:
                if self.resDia.isClosed: self.resDia._showing()
                if redirect:
                    if isinstance(redirect, int):
                        self.resDia.redirectOPT()
                    elif isinstance(redirect, (str, unicode)):
                        # self.resDia.txtedit.clear()
                        self.resDia.opt2txt(redirect)
def main_ui():
    # for widget in qApp.allWidgets():
    #     if hasattr(widget, "objectName"):
    #         # if widget.objectName() == '****':
    #         if widget.objectName() == "MayaDeploying_mainWin": #'Ui_self'
    #             widget.close()
    view = MayaDeploying_Ui()
    view.show()

def main():
    app = QApplication(sys.argv)
    ex = MayaDeploying_Ui()
    ex.show()
    sys.exit(app.exec_())
# Client code

if __name__ == "__main__":
    """ 
        #===========================================dereict invoke main_ui================================
        from  import mayaDeploying
        mayaDeploying.main_ui()
        #=================================================================================================
        import sys,os
        from PySide2.QtWidgets import *
        sys.path.append(os.path.dirname(r'F:\Development\myProj\aboutPyside\ps2\mayaDeploying.py'))
        for win in qApp.allWidgets():
            if hasattr(win, "objectName"):
                # if win.objectName() == '****':
                if win.objectName() == "MayaDeploying_mainWin": 
                    win.close()
        import mayaDeploying as xxx;reload(xxx)
        myui = xxx.MayaDeploying_Ui()
        myui.show()
        #xxx.main_ui()
    """
    app = QApplication(sys.argv)
    # view = UI()
    view = MayaDeploying_Ui()
    view.show()
    sys.exit(app.exec_())
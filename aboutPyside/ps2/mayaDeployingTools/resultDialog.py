#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = resultDialog
__author__ = zhangben 
__mtime__ = 2020/12/31 : 11:52
__description__: 

    code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import re,os,sys

if str(sys.executable).endswith("maya.exe"):
    import pymel.core as pm
    import maya.OpenMayaUI as mui
    import maya.utils
    try:
        import shiboken as sbk
    except:
        import shiboken2 as sbk
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



class Stream(QObject):
    newText = Signal(str)
    # def __init__(self):
    #     super(Stream,self).__init__()
    def write(self, text):
        self.newText.emit(str(text))

class ResultDialog(QDialog):
    # animStart = Signal(bool)
    readyPrint = Signal(bool)
    def __init__(self, *args, **kwargs):
        super(ResultDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("RESULT DIALOG...")
        self.txtedit = QTextEdit(self)
        font = self.txtedit.font()
        font.setPointSize(10)
        self.txtedit.setFont(font)
        hlay = QHBoxLayout()
        spcr = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hlay.addItem(spcr)
        self.btn_clr = QPushButton("clear.")
        hlay.addWidget(self.btn_clr)
        lay = QVBoxLayout(self)
        lay.addWidget(self.txtedit)
        lay.addLayout(hlay)
        self.btn_clr.clicked.connect(self.txtedit.clear)
        # lay.addWidget(self.btn)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        # ==================call anlibe==================================
        # self.btn.clicked.connect(self.redirectOPT)
        # self.redirectOPT()
        #self.setFixedSize(300,400)
        self.isClosed = False
    def _showing(self):
        self._emitSG()
        self.isClosed = False
        self.show()

    def _emitSG(self):
        self.readyPrint.emit(True)
        self.READY = True
    def redirectOPT(self):
        # sys.stdout = Log(self.txtedit)
        sys.stdout = Stream()
        sys.stdout.newText.connect(self.opt2txt)
        sys.stderr = Stream()
        sys.stderr.newText.connect(self.opt2txt)
    def opt2txt(self, text,color=None):
        # print("get Message ....{}".format(text))
        cursor = self.txtedit.textCursor()
        cursor.movePosition(QTextCursor.End)
        if color or text.startswith('#'):
            text = self.richTxt(text)
            cursor.insertHtml(text)
            cursor.insertText(os.linesep)
        else:
            cursor.insertText(text)
        self.txtedit.setTextCursor(cursor)
        self.txtedit.ensureCursorVisible()
    def closeEvent(self,event):
        # sys.stdout = sys.__stdout__
        # sys.stdin = maya.app.baseUI.StandardInput()
        sys.stdout = maya.utils.Output()
        sys.stderr = maya.utils.Output(error=1)
        super(ResultDialog,self).closeEvent(event)
        self.isClosed = True
    @staticmethod
    def richTxt(txt,color = '#ff710b'):
        retText = "<span style=\" font-size:10pt; font-weight:600; color:{};\" >".format(color)
        retText += txt
        retText += "</span>"
        return retText

def main():
    optUI = ResultDialog()
    optUI.show()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    c = ResultDialog()
    c.redirectOPT()
    c.show()
    print("hhhh")
    # raise("an error!!")
    sys.exit(app.exec_())

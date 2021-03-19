#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = outputTxtplan
__author__ = zhangben 
__mtime__ = 2021/3/17 : 18:07
__description__: 

THEOREM: A good programmer should wipe the butts of his predecessors in an amicable way,
    instead of reinventing a new butt.
        As long as this , code is far away from bugs, and with the god animal protecting
            I love animals. They taste delicious.
"""

import sys
import re,os,sys
from PySide.QtGui import *
from PySide.QtCore import *
from PySide import QtXml
from PySide.QtUiTools import QUiLoader
import pysideuic as uic

#  ============= ===live template require variables =====================
#  o  utputTxtplan O OutputTxtplan || OutputTxtplan  utputtxtplan


class OptTxEdt(QWidget):
    executeObject = Signal(str)
    def __init__(self,*args,**kwargs):
        super(OptTxEdt, self).__init__(*args,**kwargs)
        self.output = QTextEdit(self)
        self.layout = QVBoxLayout()
        self.bt_clr = QPushButton(self)
        self.bt_clr.setText("clear...")
        self.bt_run = QPushButton(self)
        self.bt_run.setText("run bat")
        self.layout.addWidget(self.output)
        self.layout.addWidget(self.bt_clr)
        self.layout.addWidget(self.bt_run)
        self.setLayout(self.layout)
        # self.initUI()
        self.executeBat = None
        self.bt_clr.clicked.connect(self.output.clear)
        self.bt_run.clicked.connect(self.internalCalling)
        self.setAcceptDrops(True)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle(">>>bat debug")
    def initUI_process(self):
        # Layout are better for placing widgets
        # QProcess object for external app
        self.process = QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyRead.connect(self.dataReady)
        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        # self.process.started.connect(lambda: self.runButton.setEnabled(False))
        # self.process.finished.connect(lambda: self.runButton.setEnabled(True))
    @Slot()
    def dataReady(self):
        cursor = self.output.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(unicode(self.process.readAll(),'gbk'))
        self.output.ensureCursorVisible()


    def callProgram(self,cmd):
        # run the process
        # `start` takes the exec and a list of arguments
        self.process.start(cmd)

    def dragEnterEvent(self, event):
        print('drag-enter')
        if event.mimeData().hasUrls():
            print('has urls')
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        url = event.mimeData().urls()[-1]
        self.executeBat  = url.toLocalFile()
        if self.executeBat .endswith('.bat'):
            self.executeObject.emit(self.executeBat )
            self.output.setText(self.executeBat )
    def internalCalling(self):
        self.initUI_process()
        if self.executeBat:
            self.callProgram(self.executeBat)
        else:
            print("......")
#Function Main Start
def main():
    app = QApplication(sys.argv)
    ui=OptTxEdt()
    ui.show()
    bat = os.path.join(os.path.dirname(os.path.realpath(__file__)),'exec','maya2016.bat')
    print(bat)
    # ui.callProgram(bat)
    sys.exit(app.exec_())
#Function Main END

if __name__ == '__main__':
    main() 
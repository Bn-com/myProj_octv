# -*- coding: utf-8 -*-

# Copyright (C) 2000-2012 IDMT. All rights reserved.
'''
Album Tool:
此工具用来把py文件编译成pyc文件
'''
__author__ = 'zhaozhongjie'
__date__ = '2012-12-13'

import time 
start = time.clock() 

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
import os
import sys
sys.path.append(r'Z:\Resource\Support\Python\2.6-x64\Lib\site-packages')
import PyQt4.uic as pyuic
import PyQt4

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

class DropArea(QtGui.QLabel):
    changed = QtCore.pyqtSignal(QtCore.QMimeData)

    def __init__(self, parent=None):
        super(DropArea, self).__init__(parent)
        self.setFrameStyle(QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)
        self.clear()

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        mimeData = event.mimeData()

        if mimeData.hasUrls():
            path = []
            for url in mimeData.urls():
                path.append(url.toLocalFile())

            self.setText('\n'.join(path))

        else:
            self.setText("Cannot display data")

    def clear(self):
        self.setText(u"---请拖拽文件到这里---")
        self.setBackgroundRole(QtGui.QPalette.Dark)


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

#    1.拖拽窗口
        self.dropArea = DropArea()
        
#    2.输入窗口
        self.textEdit = QtGui.QTextEdit()
        
#    3.反馈窗口
        self.outPut = QtGui.QPlainTextEdit()
        self.outPut.setStyleSheet("background:rgb(200, 200, 200)")
        self.outPut.setReadOnly(1)
        
#    4.确认，退出按钮
        self.goButton = QtGui.QPushButton("Go")
        self.quitButton = QtGui.QPushButton("Quit")

        self.buttonBox = QtGui.QDialogButtonBox()
        self.buttonBox.addButton(
            self.goButton, QtGui.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(
            self.quitButton, QtGui.QDialogButtonBox.RejectRole)
        self.quitButton.clicked.connect(self.close)

#    =====Layout
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(QLabel(u'反馈信息：'))
        mainLayout.addWidget(self.outPut)
        mainLayout.addWidget(QLabel(u'拖拽区域：'))
        mainLayout.addWidget(self.dropArea)
        mainLayout.addWidget(QLabel(u'路径粘贴：'))
        mainLayout.addWidget(self.textEdit)
        mainLayout.addWidget(self.buttonBox)
        mainLayout.setStretch(0,0)
        mainLayout.setStretch(1,1)
        mainLayout.setStretch(2,0)
        mainLayout.setStretch(3,1)
        mainLayout.setStretch(4,0)
        mainLayout.setStretch(5,1)
        self.setLayout(mainLayout)
      
#    =====Connect
        self.goButton.clicked.connect(self.go)
        self.textEdit.textChanged.connect(self.MyFilter_ExistFilePath)

        self.setWindowTitle(u"TD同步文件")
        self.resize(550, 800)

    end = time.clock() 
    print 'ini'
    print end-start 

    def MyFilter_ExistFilePath(self):
        self.textEdit.textChanged.disconnect(self.MyFilter_ExistFilePath)
        
        text = self.textEdit.document().toPlainText()
        text_split = text.split('\n')
        
        exist_Paths=[]
        
        for t in text_split:
            tt = t.strip(' ')
            if os.path.isfile(tt):
                exist_Paths.append(tt)
        exist_Path = '\n'.join(exist_Paths)
                
        
        self.textEdit.setText(exist_Path)
        
        self.textEdit.textChanged.connect(self.MyFilter_ExistFilePath)
        
    def go(self):
#    1.拖拽区域
        content = self.dropArea.text()
#         content = content.encode('utf-8')
        c_split = content.split('\n')
 
        for cs in c_split:
            try:
                if os.path.exists(cs):
                    self.outPut.appendPlainText(u'开始上传------->>>   '+cs)
                    cmd = r"\\file-cluster\GDC\Resource\Support\bin\tdSync.exe " + cs
                    feedback =  os.popen(cmd).read()
                    if len(feedback):
                        if feedback[-1]=='\n':          #    删除换行符
                            feedback =feedback[:-1]
                        self.outPut.appendPlainText(feedback)
                        self.outPut.appendPlainText(u'成功')
                    else:
                        self.outPut.appendPlainText(u'失败')
                    self.outPut.appendPlainText(u'')
            except:
                continue        

#    2.路径粘贴：
        content = self.textEdit.document().toPlainText()
        c_split = content.split('\n')

        for cs in c_split:
            try:
                if os.path.exists(cs):
                    self.outPut.appendPlainText(u'开始上传------->>>   '+cs)
                    cmd = r"\\file-cluster\GDC\Resource\Support\bin\tdSync.exe " + cs
                    feedback =  os.popen(cmd).read()
                    if len(feedback):
                        if feedback[-1]=='\n':          #    删除换行符
                            feedback =feedback[:-1]
                        self.outPut.appendPlainText(feedback)
                        self.outPut.appendPlainText(u'成功')
                    else:
                        self.outPut.appendPlainText(u'失败')
                    self.outPut.appendPlainText(u'')
            except:
                continue              
        

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    end = time.clock() 
    print 'show'
    print end-start 

    
    sys.exit(app.exec_())

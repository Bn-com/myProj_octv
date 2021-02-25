# -*- coding: utf-8 -*-

# Copyright (C) 2000-2012 IDMT. All rights reserved.
'''
Album Tool:
此工具用来把QTdesigner设计出来的.ui文件，批量转换成.py文件。
另外可以把qrc文件，转换成.py文件。
'''
__author__ = 'zhaozhongjie'
__date__ = '2012-12-13'


import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
import os
import sys
import PyQt4.uic as pyuic
import PyQt4

from PyQt4 import QtCore, QtGui


class DropArea(QtGui.QLabel):

    changed = QtCore.pyqtSignal(QtCore.QMimeData)

    def __init__(self, parent=None):
        super(DropArea, self).__init__(parent)
        self.setMinimumSize(200, 200)
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
        self.setText(u"---请拖拽 \"*.myuis\" 或者 \"*.qrc\"  文件到这里---")
        self.setBackgroundRole(QtGui.QPalette.Dark)

    def go(self):
        content = self.text()
        content = content.encode('utf-8')

        c_split = content.split('\n')

        for cs in c_split:

            cs_split = cs.split('.')
            cs_pre = '.'.join(cs_split[:-1])

            try:
                f_py = cs_pre + '.py'
                f_ui = cs_pre + '.myuis'
                f_qrc = cs_pre + '.qrc'

                if os.path.exists(f_ui):
                    cmd = os.path.join(pyuic.__path__[0], "pyuic.py")
                    cmd += " -o "
                    cmd += "\""
                    cmd += f_py
                    cmd += "\""
                    cmd += " "
                    cmd += "\""
                    cmd += f_ui
                    cmd += "\""

                    cmd = sys.executable + " " + cmd
                    os.system(cmd)

                elif os.path.exists(f_qrc):
                    output_py = cs_pre + '_rc.py'
                    cmd = os.path.join(PyQt4.__path__[0], "pyrcc4.exe")
                    cmd += " -o "
                    cmd += "\""
                    cmd += output_py
                    cmd += "\""
                    cmd += " "
                    cmd += "\""
                    cmd += f_qrc
                    cmd += "\""

                    os.system(cmd)

            except:
                pass


class DropSiteWindow(QtGui.QWidget):

    def __init__(self):
        super(DropSiteWindow, self).__init__()

        self.dropArea = DropArea()
        self.goButton = QtGui.QPushButton("Go")
        self.quitButton = QtGui.QPushButton("Quit")

        self.buttonBox = QtGui.QDialogButtonBox()
        self.buttonBox.addButton(
            self.goButton, QtGui.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(
            self.quitButton, QtGui.QDialogButtonBox.RejectRole)

        self.quitButton.clicked.connect(self.close)
        self.goButton.clicked.connect(self.dropArea.go)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.dropArea)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle(u"UI转换成PY")
        self.setMinimumSize(350, 500)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = DropSiteWindow()
    window.show()
    sys.exit(app.exec_())

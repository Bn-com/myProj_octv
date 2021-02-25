#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = Ui_mayaConfigWin.py
__author__ = zhangben
__mtime__ = 2019/2/25 : 11:04
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
from PyQt4 import QtGui,QtCore
from haha import Ui_MainWindow
import sys

class MyForm(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.AddButton,QtCore.SIGNAL("clicked()"),self.func_buttonAdd)


    def func_buttonAdd(self):
        num1 = int(self.ui.Num1Edit.text())
        num2 = int(self.ui.Num2Edit.text())
        self.ui.SumEdit.setText(str(num1+num2))



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())



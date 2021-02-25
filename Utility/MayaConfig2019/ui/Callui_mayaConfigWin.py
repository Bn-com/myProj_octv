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
from Ui_mayaConfigWin import Ui_MainWindow
import sys,os,re
import subprocess
class MyForm(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.func_buttonAdd)


    def func_buttonAdd(self):
        curDir = os.path.abspath(r"\\octvision.com\cg\TD\MayaConfig2018")
        print curDir
        mayaVersion = str(self.ui.comboBox.currentText())
        # print type(mayaVersion)
        batFileDir = os.path.join(curDir,mayaVersion)
        # fils = os.listdir(batFileDir)
        for root,dir,files in os.walk(batFileDir):
            for eaf in files:
                if not re.search("test",eaf):
                    bat_path = os.path.join(root, eaf)
                    # os.system('start'+bat_path)
                    # subprocess.Popen(os.path.join(root,eaf))
                    # os.system(os.path.join(root,eaf))

                    # p = subprocess.Popen("cmd.exe/c" + bat_path,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                    # curline = p.stdout.readline()
                    # while(curDir != b''):
                    #     print(curDir)
                    #     curline = p.stdout.readline()
                    #
                    # p.wait()
                    # print(p.returncode)
                    subprocess.call(bat_path)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())



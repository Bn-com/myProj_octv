#-*- coding: utf-8 -*-
'''
Created on 2014-1-13
@contact:     66372484@qq.com
@deffield    updated: Updated
@author: zhaozhongjie
'''
import os
import sys
from PyQt4.uic import loadUi
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Win_CreateLayer(QMainWindow):
    '''
    classdocs
    '''


    def __init__(self, parent=None):
        super(Win_CreateLayer, self).__init__(parent)
        self.resize(850, 600)
        path_split = __file__.split('\\')
        path = '\\'.join(path_split[:-1])
        win = os.path.join(path, 'Win_CreateLayer.myuis')

        self.win = loadUi(win, QMainWindow())
        self.setCentralWidget(self.win)

        
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    aa = Win_CreateLayer()
    aa.show()
    app.exec_()

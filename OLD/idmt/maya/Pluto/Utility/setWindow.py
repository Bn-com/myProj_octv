#-*- coding: gbk -*-
'''
Created on 2013-9-10

@author: zhaozhongjie
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class setQMainWindow():
    def __init__(self):
        pass
    def aaa(self):
        pass

#===============================================================================
# 
#===============================================================================
    def setCenter(self,window):
        '''
        把window设置到屏幕的中心
        '''
        screen = QDesktopWidget().screenGeometry()
        size = window.geometry()
        window.move(
                          (screen.width()-size.width())/2 + screen.left()  ,
                          (screen.height()-size.height())/2 + screen.top()
                          )
        
#===============================================================================
# 
#===============================================================================
    def setCenterFollowMouse(self,window):
        '''
        把window设置到鼠标所在屏幕的中间位置
        '''
        count = QDesktopWidget().screenCount()
        mPos = QCursor.pos()
        for i in range(count):
            s = QDesktopWidget().screenGeometry(screen = i)
            if s.contains(mPos):
                screen = QDesktopWidget().screenGeometry(screen = i)
                size = window.geometry()
                window.move(
                          (screen.width()-size.width())/2 + screen.left()  ,
                          (screen.height()-size.height())/2 + screen.top()
                          )
                
#===============================================================================
# 
#===============================================================================
    def setFollowMouse(self,window):
        '''
        把window设置到鼠标的位置
        '''
        pos = QCursor.pos()
        window.move(pos)



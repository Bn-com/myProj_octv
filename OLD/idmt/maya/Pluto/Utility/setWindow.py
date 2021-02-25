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
        ��window���õ���Ļ������
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
        ��window���õ����������Ļ���м�λ��
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
        ��window���õ�����λ��
        '''
        pos = QCursor.pos()
        window.move(pos)



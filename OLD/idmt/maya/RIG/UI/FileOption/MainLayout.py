#-*- coding: utf-8 -*-
import maya.cmds as rig

class FileOption():
    def __init__(self, parentLayout):
        self.parent = parentLayout
        self.returnLayout = ''
        self.createLayout()

    
    def createLayout(self):
        rig.setParent(self.parent)
        self.returnLayout = self.runLayout()
        rig.setParent(self.parent)
        return self.returnLayout      
    
    
    def runLayout(self):
        rig.menu( label='File',tearOff=True)
        rig.menuItem( label='New')
        rig.menuItem( label='Open')
        rig.menuItem( label='Save')
        rig.menuItem( divider=True)
        rig.menuItem( label='Quit')
        rig.menu(label='Help',helpMenu=True)
        rig.menuItem( 'Application..."',label= u'帮助文档',c='from RIG.Help.helpUI import *;SK_helptUI()' )


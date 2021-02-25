#-*- coding: utf-8 -*-
import maya.cmds as rig

class Assemblage():
    def __init__(self, parentLayout):
        self.parent = parentLayout
        self.returnLayout = ''
        self.createLayout()

    
    def createLayout(self):
        rig.setParent(self.parent)
        self.runLayout()
        rig.setParent(self.parent)
    
    def getLayout(self):
        return self.returnLayout      
    
    def runLayout(self):
        self.returnLayout = rig.columnLayout(w =300,h=355)
         
        rig.text(u'1:->选择你要复制的部件2:->在下面的输入复制的数量\n3:->完成复制4:->完成镜像')
        rig.rowColumnLayout('skinningLayout',numberOfColumns = 3,columnWidth=[(1, 109), (2,  109),(3,109)],columnAttach=(2,'both',0) )
        rig.intField('numOfduplicate' , min = 1 , max = 100 , value=1 ,step=1 )
        rig.button(label= u' 完成复制 ', c = 'SK_duplicateJnt()')
        rig.button(label= u' 完成镜像 ',c='SK_mirrorDupJoint ()')
        rig.setParent('..')
        rig.separator(w = 332,h=15,style='in')
        
        return self.returnLayout
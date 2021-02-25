#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.face.controlers import CreateControler

class SM_controller(object):
    def __init__(self,ployName,col,row,conPre,size,shape,color,start):
        self.start = start
        self.ployName = ployName
        self.col = col
        self.row = row
        self.conPre = conPre
        self.size = size
        self.shape = shape
        self.color = color
        
    def createController(self):
        if not rig.attributeQuery('sign',node = self.ployName,ex =True):
            rig.addAttr(self.ployName,ln = 'sign',at = 'long',dv = 7648)
#----------------------------------------------------------------------- 得到控制器颜色
        conColor = 13
        if 1 == self.color:
            conColor = 13
        if 2 == self.color:
            conColor = 17
        if 3 == self.color:
            conColor = 15
        
        SMCON = CreateControler(conColor,(self.size,self.size,self.size))
        for i in range(self.start,self.start+self.col*self.row):
            if 1 == self.shape:
                con = SMCON.SK_b03(self.conPre+'_'+str(i)+'_P')
            if 2 == self.shape:
                con = SMCON.SK_b01(self.conPre+'_'+str(i)+'_P')
            if 3 == self.shape:
                con = SMCON.SK_b05(self.conPre+'_'+str(i)+'_P')
                
            rig.connectAttr(self.ployName+'.sign',con+'.sign')
   
     
        
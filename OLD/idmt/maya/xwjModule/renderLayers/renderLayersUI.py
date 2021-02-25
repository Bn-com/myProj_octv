__author__ = 'xuweijian'
# -*- coding: utf-8 -*-
import maya.cmds as mc
from functools import partial

class renderLayersUI():
    def creatRGBUI(self,UI):
        if mc.window('IDP',ex=1):
            mc.deleteUI('IDP')
        RGBwindow=mc.window('IDP')
        c1=mc.columnLayout('mainCLayout')
        mc.textFieldButtonGrp('tfbR', cw=(1,50),cal=(1,'center'),label='R',text='', buttonLabel='<<<',bc=partial(self.setTextField,'textFieldButtonGrp','tfbR') )
        mc.textFieldButtonGrp('tfbG', cw=(1,50),cal=(1,'center'),label='G', text='', buttonLabel='<<<',bc=partial(self.setTextField,'textFieldButtonGrp','tfbG') )
        mc.textFieldButtonGrp('tfbB', cw=(1,50),cal=(1,'center'),label='B', text='', buttonLabel='<<<',bc=partial(self.setTextField,'textFieldButtonGrp','tfbB') )
        mc.textFieldGrp('tfN',cw2=(100,200),cal=(1,'center'),l='avo name:')
        mc.button(w=330,l='creat IDP',c=partial(self.creatIDP))
        mc.setParent(c1)
        mc.showWindow(RGBwindow)


    def creatMainUI(self):
        if mc.window('main',ex=1):
            mc.deleteUI('main')
        mc.window('main')
        mc.columnLayout()
        mc.button(l='IDP',w=200,h=50,c=partial(self.creatRGBUI))
        mc.setParent('..')
        mc.showWindow('main')


    def setTextField(self,tfType,tfName):
        obj=mc.ls(sl=1)
        str=','.join(obj)
        #mc.textFieldButtonGrp(tfName,e=1,text=str)
        eval('mc.%s(\'%s\',e=1,text=\'%s\')'%(tfType,tfName,str))

    def getObjFromTextField(self,tfType,tfName):
        #str=mc.textFieldButtonGrp(tfName,q=1,text=1)
        str=eval('mc.%s(\'%s\',q=1,text=1)'%(tfType,tfName))
        obj=str.split(',')
        return obj

    def creatIDP(self,UI=''):
        meshR=self.getObjFromTextField('textFieldButtonGrp','tfbR')
        meshG=self.getObjFromTextField('textFieldButtonGrp','tfbG')
        meshB=self.getObjFromTextField('textFieldButtonGrp','tfbB')
        aovName=self.getObjFromTextField('textFieldGrp','tfN')
        from idmt.maya.xwjModule.renderLayers import AOV
        reload(AOV)
        AOV1=AOV.AOV('test')
        AOV1.creatAOV(aovName[0])
        AOV1.RGB(meshR,meshG,meshB)

# -*- coding: utf-8 -*-
'''
Created on 2017-3-31

@author: hanhong
'''
import maya.cmds as mc
import os
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class Yak_ArnoldDis():
    def __init__(self):
        
        pass
    def Yak_ArnoldDisWin(self):
        if mc.window('Yak_ArnoldDisWin',exists = True):
            mc.deleteUI('Yak_ArnoldDisWin')
        mc.window('Yak_ArnoldDisWin', title = u'Yak -- Arnold StandIn Display', width = 700, height = 180, sizeable = True,menuBar=1)
        mc.columnLayout(rowSpacing=2, columnAttach = ['both',5],columnWidth = 700, columnAlign = 'left')
        mc.text(label = '')
        mc.radioButtonGrp('Yak_mode', label='Mode:', labelArray4=['Box','Wireframe', 'Polywire','shaded'], select = 4, numberOfRadioButtons = 4 )
        mc.radioButtonGrp('Yak_selType', label='Selected:', labelArray2=['By Selected', 'All'], select = 1, numberOfRadioButtons = 2 )
        mc.button( label=u'Apply',bgc=[0.13, 0.15, 0.25],c = 'from idmt.maya.py_common import Yak_ArnoldDis\nreload(Yak_ArnoldDis)\nYak_ArnoldDis.Yak_ArnoldDis().Yak_ArnoldDisCreat()' )
        mc.showWindow('Yak_ArnoldDisWin')
    def Yak_ArnoldDisCreat(self):
        mode = ''
        modeInt = mc.radioButtonGrp('Yak_mode', q = True, select = True )
        selType = mc.radioButtonGrp('Yak_selType', q = True, select = True )
        if modeInt == 1:
            mode = 0
        if modeInt == 2:
            mode = 3
        elif modeInt == 3:
            mode = 2
        elif modeInt == 4:
            mode = 6
        StandIns=[]
        if selType==1:
           objs=mc.ls(sl=1,l=1,type='transform')
           if not objs:
               mc.error(u'=====未选择物体，请选择======')
           for obj in objs:
               shapes=mc.listRelatives(obj,s=1,f=1)
               for shape in shapes:
                   if mc.nodeType(shape)=='aiStandIn' and mc.objExists(shape+'.dso') and mc.getAttr(shape+'.dso')!='':
                       StandIns.append(shape)
        else:
            objs=mc.ls(type='aiStandIn',l=1)
            if not objs:
                mc.error(u'=====文件中没有【aiStandIn】物体======')
            for obj in objs:
                if mc.objExists(obj+'.dso') and mc.getAttr(obj+'.dso')!='':
                    StandIns.append(obj)
        if not StandIns:
            mc.error(u'======未选择【aiStandIn】物体，请选择======')
        for sta in StandIns:
            if modeInt==1:
                mc.setAttr((sta+'.standInDrawOverride'),4)
                mc.setAttr((sta+'.mode'),int(mode))
            else:
                mc.setAttr((sta+'.standInDrawOverride'),0)
                mc.setAttr((sta+'.mode'),int(mode))
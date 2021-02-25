# -*- coding: utf-8 -*-
# 【乐高】【鬼魂模型选择工具】
#  Author : 韩虹
#  Data   : 2014_08
# import sys
# sys.path.append('D:\\food\pyp\common')

import maya.cmds as mc
import maya.mel as mel


class nj_mobSelect(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    def nj_mobSelectUI(self):
    # 窗口
        if mc.window('nj_mobSelectWin', exists=True):
            mc.deleteUI('nj_mobSelectWin')
        mc.window('nj_mobSelectWin', title=u'NJ 鬼魂模型选择',width=240, height=120, sizeable=True)
        mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label=u'鬼魂模型选择', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=3)
        mc.button(l=u'尾巴',bgc=[0.13, 0.15, 0.25],width=80,c='from idmt.maya.Ninjago import nj_mobSelect\nreload(nj_mobSelect)\nnj_mobSelect.nj_mobSelect().nj_mobSelect(tail=1,qib=0,dress=0)')
        mc.button(l=u'短裙',bgc=[0.13, 0.15, 0.25],width=80,c='from idmt.maya.Ninjago import nj_mobSelect\nreload(nj_mobSelect)\nnj_mobSelect.nj_mobSelect().nj_mobSelect(tail=0,qib=1,dress=0)')
        mc.button(l=u'衣服',bgc=[0.13, 0.15, 0.25],width=80,c='from idmt.maya.Ninjago import nj_mobSelect\nreload(nj_mobSelect)\nnj_mobSelect.nj_mobSelect().nj_mobSelect(tail=0,qib=0,dress=1)')
        mc.setParent('..')
        mc.setParent('..')
       
        mc.showWindow('nj_mobSelectWin')   
#============================================
# 鬼魂模型选择(韩虹)
#    tail,qib,dress 只有一个为真
#=====================================			               

    def nj_mobSelect(self,tail=1,qib=0,dress=0):
        objInfo=[]
        chas=['nj_c410001GhostBackgroundCharactersTwo','nj_c409001GhostBackgroundCharacters','nj_c411001GhostBackgroundCharactersWide']        
        tais=['tail1_','tail2_','tail3_']
        objs=mc.ls(type='transform',l=1)
        qibs=['tail5_','tail6_']
        dres=['dress']
        objtype=[]
        if tail==1:
            objtype=tais
        if qib==1:
             objtype=qibs
        if dress==1:
             objtype=dres                
        if objs:
            for obj in objs:
                if mc.objExists(obj) and mc.listRelatives(obj,s = 1) and mc.nodeType(mc.listRelatives(obj,s = 1,f=1)[0])=='mesh':
                    for i in range(len(chas)):
                        if chas[i] in obj:                       
                            for j in range(len(objtype)):
                                if objtype[j] in obj :
                                    objInfo.append(obj)
        if objInfo:
            mc.select(objInfo)
        else:
            print u'-------------------没有该类型模型-------------------' 
        return objInfo                                                          
                                	                                                                                                                                                                                                                                                       
            

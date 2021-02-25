# -*- coding: utf-8 -*-
# 【通用】【植物分布工具】
#  Author : 韩虹
#  Data   : 2018_01_22

import maya.cmds as mc
import maya.mel as mel
import random
class GA_TreeScatter(object):
    def __init__(self):

        pass
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【植物分布工具】【随机选择工具】
    #  Author  : 韩虹
    #  Data    : 2018_01
    #------------------------------#
    def GA_SelectScatter(self,par):
        objs=mc.ls(sl=1,l=1)
        if not objs:
            mc.error('select,please')
        nums=len(objs)
        numN=int(nums*int(par)*0.01)
        print numN
        if numN==0:
            mc.warning(u'选择物体数量过少，请重新选择')
            mc.error(u'选择物体数量过少，请重新选择')
        objsList=[]
        for i in range(numN):
            k=int(random.uniform(0,(nums-1)))
            while objs[k] in objsList:
                k=int(random.uniform(0,(nums-1)))
            objsList.append(objs[k])
        if not objsList:
            mc.warning(u'选择物体数量过少，请重新选择')
            mc.error(u'选择物体数量过少，请重新选择')
        mc.select(objsList)
        result=objsList
        return result
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【植物分布工具】【分布工具】
    #  Author  : 韩虹
    #  Data    : 2018_01
    #------------------------------#
    def GA_ScatterInfos(self):
        ActiveList=[]
        Actives=mc.columnLayout('ActiveColumn',q=1,childArray=1)
        ActiveObjsList=[]
        ActiveWeight=[]
        ActiveWeightNew=[]
        for act in Actives:
            if 'ScatterItemRow_' in act and act not in ActiveList:
                ActiveList.append(act)
        if not ActiveList:
            mc.error(u'没有active物体，请检查')

        for i in range(len(ActiveList)):
            box=mc.checkBox('ScatterCheckBox'+str(i),q=1,v=1)
            if box==True:
                obj=mc.checkBox('ScatterCheckBox'+str(i),q=1,label=1)
                weight=mc.floatSliderGrp(("Scatter_"+obj),q=1,v=1)
                ActiveObjsList.append(obj)
                ActiveWeight.append(weight)
        if not 	ActiveObjsList:
            mc.error(u'未激活物体，请检查')
        sumNum=sum(ActiveWeight)
        for i in range(len(ActiveWeight)):
            weightNew=ActiveWeight[i]/sumNum
            ActiveWeightNew.append(weightNew)
        result=dict(zip(ActiveObjsList,ActiveWeightNew))
        return result
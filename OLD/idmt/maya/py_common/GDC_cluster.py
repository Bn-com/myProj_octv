# -*- coding: utf-8 -*-

'''
Created on 2016

GDC 群组工具【通用】

@author: hanhong
'''
import maya.cmds as mc
import random
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
#群组工具
#@author: hanhong
#Data：2016/3/24
#----------------------------------------------------------------------------------------------------------#
class GDC_cluster(object):
    def __init__(self):
        pass
#面板
    def yd_clusterWin(self):
        if mc.window('yd_clusterWin', exists=True):
            mc.deleteUI('yd_clusterWin')
        mc.window('yd_clusterWin', title=u'yd_clusterWin',
                  width=90, height=80, sizeable=True)
        mc.columnLayout( adjustableColumn=True )

        mc.button(label=u'cluster', bgc=[
                  0, 0, 0.0], width=30, height=30, command='from idmt.maya.py_common import GDC_cluster\nreload(GDC_cluster)\nGDC_cluster.GDC_cluster().yd_clusterRef()')
        mc.button(label=u'bake', bgc=[
                  0.13, 0.15, 0.25], width=30, height=30, command='from idmt.maya.py_common import GDC_cluster\nreload(GDC_cluster)\nGDC_cluster.GDC_cluster().yd_bakeMast()')
        mc.showWindow('yd_clusterWin')
#删除鱼群参考【辅】
#@author: hanhong
#Data：2016/3/24
#----------------------------------------------------------------------------------------------------------#
    def yd_clusterRemove(self):
        fish01='//file-cluster/GDC/Projects/YODA/Project/scenes/props/E0109/pe0109034001NingothFishSmallAnimA/master/yd_pe0109034001NingothFishSmallAnimA_h_ms_anim.mb'
        fish02='//file-cluster/GDC/Projects/YODA/Project/scenes/props/E0109/pe0109035001NingothFishSmallAnimB/master/yd_pe0109035001NingothFishSmallAnimB_h_ms_anim.mb'
        fish03='//file-cluster/GDC/Projects/YODA/Project/scenes/props/E0109/pe0109036001NingothFishSmallAnimC/master/yd_pe0109036001NingothFishSmallAnimC_h_ms_anim.mb'
        clusterRefs=[fish01,fish02,fish03]
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        clusterList=[]
        for i in range(len(refInfos[1][0])):
            if refInfos[1][0][i] in clusterRefs:
                clusterList.append(refInfos[0][0][i])
        if clusterList:
            for refNode in clusterList:
                try:
                    mc.file(rfn=refNode , removeReference=1)
                except:
                    mc.lockNode(refNode, l=0)
                    mc.delete(refNode)
        return 0
#随机鱼群参考，并跟随【主】
#@author: hanhong
#Data：2016/3/24
#----------------------------------------------------------------------------------------------------------#
    def yd_clusterRef(self):
        self.yd_clusterRemove()
        objs=mc.ls(tr=1,l=1)
        fish01=['yd_pe0109034001NingothFishSmallAnimA_h','//file-cluster/GDC/Projects/YODA/Project/scenes/props/E0109/pe0109034001NingothFishSmallAnimA/master/yd_pe0109034001NingothFishSmallAnimA_h_ms_anim.mb']
        fish02=['yd_pe0109035001NingothFishSmallAnimB_h','//file-cluster/GDC/Projects/YODA/Project/scenes/props/E0109/pe0109035001NingothFishSmallAnimB/master/yd_pe0109035001NingothFishSmallAnimB_h_ms_anim.mb']
        fish03=['yd_pe0109036001NingothFishSmallAnimC_h','//file-cluster/GDC/Projects/YODA/Project/scenes/props/E0109/pe0109036001NingothFishSmallAnimC/master/yd_pe0109036001NingothFishSmallAnimC_h_ms_anim.mb']
        meshList=[]
        if objs:
            for obj in objs:
                if mc.objExists(obj+'.cluster'):
                    meshList.append(obj)
        if meshList:
            for i in range(len(meshList)):
                p=[fish01,fish02,fish03]
                fishRef=random.sample(p,1)
                if i==0:
                    ns=fishRef[0][0]
                else:
                    ns=fishRef[0][0]+'_'+str(i)
                fishAn=mc.file(fishRef[0][1],r=1,namespace=ns)
                master=ns+':Master'
                point=mc.pointConstraint(meshList[i],master)
                poino=mc.orientConstraint(meshList[i],master)
        return 0
#bake动动【主】
#@author: hanhong
#Data：2016/3/24
#----------------------------------------------------------------------------------------------------------#
    def yd_bakeMast(self):
        fish01='//file-cluster/GDC/Projects/YODA/Project/scenes/props/E0109/pe0109034001NingothFishSmallAnimA/master/yd_pe0109034001NingothFishSmallAnimA_h_ms_anim.mb'
        fish02='//file-cluster/GDC/Projects/YODA/Project/scenes/props/E0109/pe0109035001NingothFishSmallAnimB/master/yd_pe0109035001NingothFishSmallAnimB_h_ms_anim.mb'
        fish03='//file-cluster/GDC/Projects/YODA/Project/scenes/props/E0109/pe0109036001NingothFishSmallAnimC/master/yd_pe0109036001NingothFishSmallAnimC_h_ms_anim.mb'
        clusterRefs=[fish01,fish02,fish03]
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        timeR =(mc.playbackOptions(q=1, minTime=1)-12, mc.playbackOptions(q=1, maxTime=1)+12)
        clusterList=[]
        if refInfos:
            for i in range(len(refInfos[1][0])):
                if refInfos[1][0][i] in clusterRefs:
                    clusterList.append(refInfos[-1][0][i])
        masterList=[]
        if clusterList:
            for ns in clusterList:
                master=ns+':Master'
                if mc.objExists(master):
                    masterList.append(master)
        if masterList:
            mc.select(masterList)
            try:
                mc.bakeResults(masterList,t=timeR,simulation=1,sampleBy=1,disableImplicitControl=1,preserveOutsideKeys=1,sparseAnimCurveBake=0,removeBakedAttributeFromLayer=0,bakeOnOverrideLayer=0,controlPoints=0,shape=0)
            except:
                pass
        return u'==============已bake================='


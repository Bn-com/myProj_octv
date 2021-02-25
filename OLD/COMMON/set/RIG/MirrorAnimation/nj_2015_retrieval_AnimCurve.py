# -*- coding: utf-8 -*-
'''
Script Name: retrieval_AnimCurve
Created: 2015-07-03
@Author: Justin.CHan
@Update_Change: 
@LastUpdated:
@Description: 在镜头文件里控制器动画曲线丢失，是由于maya自动自动连接时出错，但动画曲线节点还存在在文件里，这时可用此插件根据命名重新连接上.

'''
import maya.cmds as mc
import re
def CJW_retrieval_AnimCurve():
    objs = mc.ls(sl=1)
    if objs==None or objs==[]:
        mc.error(u'=====请选择相关物体=====')
    for obj in objs:
        reNode = mc.referenceQuery(obj, referenceNode=1)
        refNamespace = mc.referenceQuery(obj , namespace = 1)
    animCurves = mc.listConnections ( reNode,s = 1,d=0,type = 'animCurve')
    if not animCurves ==None:
        for animCurve in animCurves:
            prefix = refNamespace+':'
            Ctrl = prefix + re.sub('_[^_]+$', '', animCurve)
            AttrXX = animCurve.split('_')[-1]
            Attr = re.sub(r'\d+$', '', AttrXX)
            CtrlAttr = Ctrl+'.'+Attr
            if mc.objExists(CtrlAttr):         
                mc.connectAttr(animCurve+'.output',CtrlAttr)           
    AnimLayerDL = mc.listConnections ( reNode,s = 1,d=0,type = 'animBlendNodeAdditiveDL')
    AnimLayerRotation = mc.listConnections ( reNode,s = 1,d=0,type = 'animBlendNodeAdditiveRotation')
    AnimLayerF = mc.listConnections ( reNode,s = 1,d=0,type = 'animBlendNodeAdditiveF')
    AnimLayerScale = mc.listConnections ( reNode,s = 1,d=0,type = 'animBlendNodeAdditiveScale')
    AnimLayers = [AnimLayerDL,AnimLayerRotation,AnimLayerF,AnimLayerScale]
    AnimLayerGRP = []
    for AnimLayer in AnimLayers:
        if not AnimLayer == None:
            for AnimLayerPP in AnimLayer:
                if not AnimLayerPP in AnimLayerGRP:
                    AnimLayerGRP.append(AnimLayerPP)
    for AnimLayerPer in AnimLayerGRP:
        prefix = refNamespace+':'
        animCurve = re.sub('_[^_]+$', '', AnimLayerPer)
        AttrXX = animCurve.split('_')[-1]
        Attr = re.sub(r'\d+$', '', AttrXX)    
        Ctrl = prefix + re.sub('_[^_]+$', '', animCurve)
        CtrlAttr = Ctrl+'.'+Attr
        if mc.objExists(CtrlAttr): 
            mc.connectAttr(AnimLayerPer+'.output',CtrlAttr)  
    print u'=====完成====='
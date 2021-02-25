# -*- coding: utf-8 -*-

'''
Created on

@author: 黄帅

'''
import maya.cmds as mc
import maya.mel as mel
import os
import re
import sys
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.setdefaultencoding('utf8')
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
class GA_animFixTool(object):
    def __init__(self):
        pass

    def GA_animFixTool(self):
        if mc.window('animFixWin',ex=1):
            mc.deleteUI('animFixWin')
        mc.window('animFixWin',t=u'动画修型工具',h=102,w=302)
        mc.columnLayout()
        mc.text('helpText',l=u'输入一个属性名称，记住不要重名！',ww=1,h=40,w=300,font='fixedWidthFont')
        mc.textField('attrNameField',h=20,w=300)
        mc.button('animFixButton',h=40,w=300,c='GA_animFixTool().animFixButtonCmd()')
        mc.showWindow('animFixWin')
    def animFixButtonCmd(self):
        fixShape=mc.textField('attrNameField',q=1,tx=1)
        self.animFixShape(fixShape)
    def animFixShape(self,fixShape):
        objs=mc.ls(sl=1)
        numVtx=mc.polyEvaluate(objs[1],v=1)
        skinMeshShapes=mc.listRelatives(objs[1],s=1,pa=1)
        skinMeshShapes1=mc.listRelatives(objs[1],s=1,ni=1,pa=1)
        fixMeshShape=mc.listRelatives(objs[0],s=1,ni=1,pa=1)[0]
        inputs=mc.listHistory(objs[1])
        for i in skinMeshShapes:
            if not i in skinMeshShapes1:
                intermediateShape=i
        if not 'animFixBS*' in inputs:
            BSNode=mc.blendShape(objs[1],parallel=1,n='animFixBS')[0]
        else:
            for n in inputs:
                if n=='animFixBS*':
                    BSNode=n
        if not mc.objExists('animFixCtrl'):
            self.createCtrl()

        mc.addAttr('animFixCtrl',ln=fixShape,at='double',min=0,max=1,dv=0,k=1)

        weightListNum=mc.blendShape(BSNode,q=1,wc=1)
        mc.blendShape(BSNode,e=1,t=[objs[1],weightListNum,objs[0],1])

        BSTargets=mc.listAttr(BSNode+'.weight',m=1)
        mc.connectAttr('animFixCtrl.'+fixShape,BSNode+'.'+BSTargets[-1])

        for i in range(0,numVtx):
            ipos=mc.xform(intermediateShape+'.vtx[%d]'%i,q=1,os=1,t=1)
            tpos=mc.xform(objs[0]+'.vtx[%d]'%i,q=1,os=1,t=1)
            bpos=mc.xform(objs[1]+'.vtx[%d]'%i,q=1,os=1,t=1)
            mc.xform(objs[0]+'.vtx[%d]'%i,os=1,t=[(ipos[0]+tpos[0]-bpos[0]),(ipos[1]+tpos[1]-bpos[1]),(ipos[2]+tpos[2]-bpos[2])])
        mc.setAttr('animFixCtrl.'+fixShape,1)
        mc.delete(objs[0])
        mc.deleteUI('animFixWin')
    def createCtrl(self):
        animFixCtrl=mc.textCurves(ch=0,o=1,f='Times New Roman|w400|h-1',t='AnimFixCtrl',n='Ctrl_AnimFix')
        curveShapes=mc.listRelatives(animFixCtrl,allDescendents=1,type='nurbsCurve')
        children=mc.listRelatives(animFixCtrl,children=1)
        makeCurve=mc.listConnections(children[0],s=1)
        mc.delete(makeCurve)
        mc.makeIdentity(animFixCtrl,apply=1)
        for i in curveShapes:
            mc.parent(i,animFixCtrl,s=1,add=1)
        mc.delete(children)
        animFixCtrl=mc.rename(animFixCtrl,'animFixCtrl')
        mc.setAttr(animFixCtrl+".overrideEnabled",1)
        mc.setAttr(animFixCtrl+".overrideColor",17)
        mc.setAttr("animFixCtrl.tx",keyable=0,channelBox=1)
        mc.setAttr("animFixCtrl.ty",keyable=0,channelBox=1)
        mc.setAttr("animFixCtrl.tz",keyable=0,channelBox=1)
        mc.setAttr("animFixCtrl.rx",keyable=0,channelBox=1)
        mc.setAttr("animFixCtrl.ry",keyable=0,channelBox=1)
        mc.setAttr("animFixCtrl.rz",keyable=0,channelBox=1)
        mc.setAttr("animFixCtrl.sx",keyable=0,channelBox=1)
        mc.setAttr("animFixCtrl.sy",keyable=0,channelBox=1)
        mc.setAttr("animFixCtrl.sz",keyable=0,channelBox=1)
        mc.setAttr("animFixCtrl.v",keyable=0,channelBox=1)
        activeCam=mc.lookThru(q=1)
        ctrlGrp=mc.group(animFixCtrl,n='animFixCtrlGRP')
        mc.parent(ctrlGrp,activeCam)
        mc.xform(ctrlGrp,a=1,os=1,t=[0.3,0.7,-5],ro=[0,0,0])
        mc.parent(ctrlGrp,w=1)
        mc.parentConstraint(activeCam,ctrlGrp,mo=1)
        mc.select(animFixCtrl,r=1)

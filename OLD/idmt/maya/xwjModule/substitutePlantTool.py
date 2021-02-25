#-*- coding: utf-8 -*-
__author__ = 'xuweijian'


import maya.cmds as mc
from functools import partial


class substitutePlantTool():
    def creatUI(self):
        winName='substitutePlant'
        if mc.window(winName, q = True, ex = True):
                mc.deleteUI(winName)
        mc.window(winName,h=100,w=300)
        mc.columnLayout('c1')
        mc.textFieldGrp('tfSource',l=u'原物体',cw2=(50,250),pht=u'此处填需要替换植物的组')
        mc.textFieldGrp('tfNewPath',l=u'新物体',cw2=(50,250),pht=u'此处填替换新植物的路径')
        mc.button(w=300,l=u'替换',c=partial(self.replacePlant))
        mc.showWindow(winName)


    def replacePlant(self,UI=''):
        sourceObjGrp=mc.textFieldGrp('tfSource',q=1,tx=1)
        newObjPath=mc.textFieldGrp('tfNewPath',q=1,tx=1)
        if newObjPath:
            newObjPath=newObjPath.replace('\\','/')
            sourceObjs=mc.listRelatives(sourceObjGrp,c=1,f=1,type='transform')
            for sourceObj in sourceObjs:
                dictAttr=self.getObjAttr(sourceObj)
                mc.file(newObjPath,i=1,ns='temp')
                newObj=mc.ls('temp:**',assemblies=1)
                for one in newObj:
                    mc.parent(newObj,sourceObjGrp)
                    self.setObjAttr(one,dictAttr)
                    mc.namespace(rm='temp',mnp=1,f=1)
                mc.delete(sourceObj)




    def getObjAttr(self,obj):
        Attrdict={}
        Attrdict['sourceTX']=mc.getAttr('%s.tx'%obj)
        Attrdict['sourceTY']=mc.getAttr('%s.ty'%obj)
        Attrdict['sourceTZ']=mc.getAttr('%s.tz'%obj)
        Attrdict['sourceRX']=mc.getAttr('%s.rx'%obj)
        Attrdict['sourceRY']=mc.getAttr('%s.ry'%obj)
        Attrdict['sourceRZ']=mc.getAttr('%s.rz'%obj)
        Attrdict['sourceSX']=mc.getAttr('%s.sx'%obj)
        Attrdict['sourceSY']=mc.getAttr('%s.sy'%obj)
        Attrdict['sourceSZ']=mc.getAttr('%s.sz'%obj)
        return Attrdict


    def setObjAttr(self,obj,dict):
        mc.setAttr('%s.tx'%obj,dict['sourceTX'])
        mc.setAttr('%s.ty'%obj,dict['sourceTY'])
        mc.setAttr('%s.tz'%obj,dict['sourceTZ'])
        mc.setAttr('%s.rx'%obj,dict['sourceRX'])
        mc.setAttr('%s.ry'%obj,dict['sourceRY'])
        mc.setAttr('%s.rz'%obj,dict['sourceRZ'])
        mc.setAttr('%s.sx'%obj,dict['sourceSX'])
        mc.setAttr('%s.sy'%obj,dict['sourceSY'])
        mc.setAttr('%s.sz'%obj,dict['sourceSZ'])





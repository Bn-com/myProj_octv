# -*- coding: utf-8 -*-


import maya.cmds as mc
import maya.mel as mel
from functools import partial


class groupConstrain():
    def creatUI(self):
        if mc.window ('groupConstrainWindow', ex=1):
            mc.deleteUI('groupConstrainWindow', window=True)
        mc.window('groupConstrainWindow', title="LightConstrain", widthHeight=(50, 300), menuBar=0)
        mc.columnLayout(w=300,adj=1,h=100)
        mc.textFieldButtonGrp('tfgGrp',l='Group',bl=u'<<<',adj=2,cw3=[50,50,50],bc=partial(self.setGrpTextField),ann=u'填入灯光组')
        mc.textFieldButtonGrp('tfVtx',l='Vertex',bl=u'<<<',adj=2,cw3=[50,50,50],bc=partial(self.setVtxTextField),ann=u'填入约束灯光的点')
        mc.button(l='constrain',c=partial(self.groupConstrain))
        mc.setParent('..')
        mc.showWindow('groupConstrainWindow')

    def setGrpTextField(self):
        groupName=mc.ls(sl=1,type='transform')
        #selObj=mc.listRelatives(selObj,type=DestinationNote)
        GrpStr=','.join(groupName)
        mc.textFieldButtonGrp('tfgGrp',e=1,text=GrpStr)

    def setVtxTextField(self):
        #groupName=mc.ls(sl=1,type='transform')
        vtxName=mc.ls(sl=1)[0]
        #GrpStr=','.join(groupName)
        if '.vtx' in vtxName:
            vtxId=vtxName.split('.vtx[')[1][:-1]
            mc.textFieldButtonGrp('tfVtx',e=1,text=vtxId)

    def groupConstrain(self,UI=''):
        groupName=mc.textFieldButtonGrp('tfgGrp',q=1,tx=1)
        print groupName
        vtxId=mc.textFieldButtonGrp('tfVtx',q=1,tx=1)
        print vtxId
        checkGrps = mc.listRelatives(groupName,c=1)
        print checkGrps
        #attrKey = '.deng'
        #consPre = 'foodCons_'
        needObjs = []
        for checkGrp in checkGrps:
            mesh = mc.listRelatives(checkGrp,s=1)
            if not mesh:
                continue
            if not mc.getAttr(checkGrp+'.v'):
                continue
            needObjs.append(checkGrp)
        if not needObjs:
            print needObjs
            return
        # 准备
        pLClr = [0.696,0.880,0]
        pLPos = [0,0,0]
        lightRoot = 'Light_Grp'
        if mc.ls(lightRoot,type = 'transform'):
            mc.delete(lightRoot)
        mc.group(n=lightRoot,em=1)
        for needObj in needObjs:
            # 初始情况
            realName = needObj.split('|')[-1]
            locName = '%s_Loc'%realName
            locName = mc.spaceLocator(n = locName)[0]
            pLightName = '%s_pLight'%realName
            mc.pointLight(n = pLightName,position =pLPos)
            mc.setAttr(pLightName+'.color',pLClr[0],pLClr[1],pLClr[2],type = 'double3')
            mc.setAttr(pLightName+'.decayRate',2)
            mc.setAttr(pLightName+'.aiDecayType',1)
            mc.setAttr(pLightName+'.aiExposure',7.05)
            mc.setAttr(pLightName+'.aiSamples',3)
            mc.setAttr(pLightName+'.aiRadius',3)
            mc.parent(pLightName,locName)
            # 约束
            mc.select('%s.vtx[%s]'%(needObj,vtxId))
            mc.select(locName,add = 1)
            mel.eval('doCreatePointOnPolyConstraintArgList 2 {   "0" ,"0" ,"0" ,"1" ,"" ,"1" ,"0" ,"0" ,"0" ,"0" };')
            #consNode = mc.pointOnPolyConstraint(needObj+'.vtx[281]',locName,mo=0)[0]
            #mc.rename(consNode,consPre+consNode)
            mc.parent(locName,lightRoot)
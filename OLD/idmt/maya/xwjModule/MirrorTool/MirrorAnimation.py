# -*- coding: utf-8 -*-
__author__ = 'xuweijian'
import maya.cmds as mc
import maya.mel as mel
import re
from idmt.maya.xwjModule.xwjProcessWindow import xwjProcessWindow
from idmt.maya.xwjModule.MirrorTool.MirrorPose import MirrorPose

class MirrorAnimation(MirrorPose):

    #--------------------获取对象的动画曲线生成字典------------------------
    def getAnimCurveDict(self,obj):
        nodes=mc.keyframe(obj,q=1,n=1)
        if nodes==None:
            return None
        else:
            nodeDict={}
            for oneNode in nodes:
                keylist=[]
                keys=mc.keyframe(oneNode,q=1,keyframeCount=1)
                i=0
                while(i<=keys-1):
                    detailDict={}
                    detailDict['time']=mc.keyframe(oneNode,q=1,timeChange=1)[i]
                    detailDict['value']=mc.keyframe(oneNode,q=1,valueChange=1)[i]
                    detailDict['angle']=mc.keyTangent(oneNode,q=1,inAngle=1)[i]
                    detailDict['wt']=mc.keyTangent(oneNode,q=1,weightedTangents=1)[0]
                    detailDict['weight']=mc.keyTangent(oneNode,q=1,inWeight=1)[i]
                    detailDict['outangle']=mc.keyTangent(oneNode,q=1,outAngle=1)[i]
                    detailDict['outweight']=mc.keyTangent(oneNode,q=1,outWeight=1)[i]
                    i=i+1
                    keylist.append(detailDict)
                nodeDict[oneNode]=keylist
            return nodeDict



    #-----------------------把字典里的值赋值给对象------------------------------
    def setAnimCurveDict(self,obj,dict,type):
        nodeNames=dict.keys()
        for nodeName in nodeNames:
            #print nodeName
            attrName=self.getAttrNameInNode(nodeName)
            i=0

            while(i<=len(dict[nodeName])-1):
                if type=='IKType':
                    if attrName=='translateX' or attrName=='rotateY' or attrName=='rotateZ':
                        mc.setKeyframe(obj,at=attrName,time=dict[nodeName][i]['time'],value=dict[nodeName][i]['value']*-1)
                        mc.keyTangent(obj,at=attrName,weightedTangents=dict[nodeName][i]['wt'])
                        mc.keyTangent(obj,at=attrName,index=(i,i),inAngle=dict[nodeName][i]['angle']*-1,inWeight=dict[nodeName][i]['weight'],outAngle=dict[nodeName][i]['outangle']*-1,outWeight=dict[nodeName][i]['outweight'])
                    else:
                        mc.setKeyframe(obj,at=attrName,time=dict[nodeName][i]['time'],value=dict[nodeName][i]['value'])
                        mc.keyTangent(obj,at=attrName,weightedTangents=dict[nodeName][i]['wt'])
                        mc.keyTangent(obj,at=attrName,index=(i,i),inAngle=dict[nodeName][i]['angle'],inWeight=dict[nodeName][i]['weight'],outAngle=dict[nodeName][i]['outangle'],outWeight=dict[nodeName][i]['outweight'])
                elif type=='fingerType':
                    if attrName=='translateX':
                        mc.setKeyframe(obj,at=attrName,time=dict[nodeName][i]['time'],value=dict[nodeName][i]['value']*-1)
                        mc.keyTangent(obj,at=attrName,weightedTangents=dict[nodeName][i]['wt'])
                        mc.keyTangent(obj,at=attrName,index=(i,i),inAngle=dict[nodeName][i]['angle']*-1,inWeight=dict[nodeName][i]['weight'],outAngle=dict[nodeName][i]['outangle']*-1,outWeight=dict[nodeName][i]['outweight'])
                    else:
                        mc.setKeyframe(obj,at=attrName,time=dict[nodeName][i]['time'],value=dict[nodeName][i]['value'])
                        mc.keyTangent(obj,at=attrName,weightedTangents=dict[nodeName][i]['wt'])
                        mc.keyTangent(obj,at=attrName,index=(i,i),inAngle=dict[nodeName][i]['angle'],inWeight=dict[nodeName][i]['weight'],outAngle=dict[nodeName][i]['outangle'],outWeight=dict[nodeName][i]['outweight'])
                elif type=='bodyType':
                    if attrName=='rotateY' or attrName=='rotateZ' or attrName=='translateX':
                        mc.setKeyframe(obj,at=attrName,time=dict[nodeName][i]['time'],value=dict[nodeName][i]['value']*-1)
                        mc.keyTangent(obj,at=attrName,weightedTangents=dict[nodeName][i]['wt'])
                        mc.keyTangent(obj,at=attrName,index=(i,i),inAngle=dict[nodeName][i]['angle']*-1,inWeight=dict[nodeName][i]['weight'],outAngle=dict[nodeName][i]['outangle']*-1,outWeight=dict[nodeName][i]['outweight'])
                    else:
                        mc.setKeyframe(obj,at=attrName,time=dict[nodeName][i]['time'],value=dict[nodeName][i]['value'])
                        mc.keyTangent(obj,at=attrName,weightedTangents=dict[nodeName][i]['wt'])
                        mc.keyTangent(obj,at=attrName,index=(i,i),inAngle=dict[nodeName][i]['angle'],inWeight=dict[nodeName][i]['weight'],outAngle=dict[nodeName][i]['outangle'],outWeight=dict[nodeName][i]['outweight'])
                else:
                    mc.setKeyframe(obj,at=attrName,time=dict[nodeName][i]['time'],value=dict[nodeName][i]['value'])
                    mc.keyTangent(obj,at=attrName,weightedTangents=dict[nodeName][i]['wt'])
                    mc.keyTangent(obj,at=attrName,index=(i,i),inAngle=dict[nodeName][i]['angle'],inWeight=dict[nodeName][i]['weight'],outAngle=dict[nodeName][i]['outangle'],outWeight=dict[nodeName][i]['outweight'])
                i=i+1

    #-------------------根据节点名获取对应属性--------------------------
    def getAttrNameInNode(self,node):
        attrX=node.split('_')[-1]
        attr=re.sub(r'\d+$', '', attrX)
        return attr



    #---------------镜前前删除所有节点初始化--------------------
    def clearAllKeyNode(self,obj):
        nodes=mc.keyframe(obj,q=1,n=1)
        if nodes!=None:
            for node in nodes:
                mc.delete(node)
            #attr=self.getAttrNameInNode(node)

            '''
            if attr=='scaleX' or attr=='scaleY' or attr=='scaleZ' or attr=='visibility':
                mc.setAttr(obj+'.'+attr,1)
            else:
                mc.setAttr(obj+'.'+attr,0)
            '''

    #-----------------镜像方法---------------------------
    def mirrorAnim(self,sourceCtrl):
        #sourceCtrl=self.getSelect()
        type=self.checkCtrlType(sourceCtrl)
        mirrorCtrl=self.getMirrorCtrl(sourceCtrl)
        sourceDict=self.getAnimCurveDict(sourceCtrl)
        mirrorDict=self.getAnimCurveDict(mirrorCtrl)
        self.clearAllKeyNode(sourceCtrl)
        self.clearAllKeyNode(mirrorCtrl)
        self.mirrorPose(sourceCtrl,1)
        if mirrorDict:
            self.setAnimCurveDict(sourceCtrl,mirrorDict,type)
        if sourceDict:
            self.setAnimCurveDict(mirrorCtrl,sourceDict,type)


    def wholeMirror(self,obj):
        #slCtrl=self.getSelect()
        theNamespace=self.divNamespace(obj,0)
        BodySet = mc.sets((theNamespace+'BodySet'),q=True)
        ArmSet = mc.sets((theNamespace+'Lf_ArmSet'),q=True)
        FingerSet = mc.sets((theNamespace+'Lf_FingerSet'),q=True)
        LegSet = mc.sets((theNamespace+'Lf_LegSet'),q=True)
        ToesSet = mc.sets((theNamespace+'Lf_ToesSet'),q=True)
        AllSet=[]
        #print BodySet

        if BodySet:
            AllSet=AllSet+BodySet
        if ArmSet:
            AllSet=AllSet+ArmSet
        if FingerSet:
            AllSet=AllSet+FingerSet
        if LegSet:
            AllSet=AllSet+LegSet
        if ToesSet:
            print ToesSet
            AllSet=AllSet+ToesSet

        if AllSet:
            AllSet=list(set(AllSet))
            AllSet=mc.ls(AllSet,type='transform')
            i=1
            xwjProcessWindow().makeProcessWindow()
            for oneSet in AllSet:
                self.mirrorAnim(oneSet)
                xwjProcessWindow().stateProcessWindow(i,len(AllSet))
                i=i+1



#------------------------废弃的方法----------------------------------
"""
    def getMirrorNode(self,ctrl='',node=''):
        mirrorCtrl=self.getMirrorCtrl(ctrl)
        shortCtrl=self.divNamespace(mirrorCtrl,1)
        print node
        attrX=node.split('_')[-1]
        attr=re.sub(r'\d+$', '', attrX)
        mirrorAttr=mirrorCtrl + '.' + attr
        mirrorNode=''
        if mc.connectionInfo(mirrorAttr,isDestination=True):
            print u'纯在对应节点'
            mirrorNode=mc.listConnections(mirrorAttr)[0]
        else:
            print u'没有对应节点'
            myNodeType =mc.nodeType(node)
            mirrorNode=mc.createNode(myNodeType,n=shortCtrl+'_'+attr)
            mc.connectAttr(mirrorNode+'.output',mirrorAttr)
            print 'mirrorNode success'
        print mirrorNode
        return mirrorNode

    #---------------获得两边控制器属性,各k一帧------------------------
    def keyBothObj(self,obj,mirrorObj):
        nodes=mc.keyframe(obj,q=1,n=1)
        mirrorNodes=mc.keyframe(mirrorObj,q=1,n=1)
        for node in nodes:
            attr=self.getAttrNameInNode(node)
            mc.setKeyframe(mirrorObj+'.'+attr)
        for mirrorNode in mirrorNodes:
            mirrorAttr=self.getAttrNameInNode(mirrorNode)
            mc.setKeyframe(obj+'.'+mirrorAttr)

        #把字典的值付给对应的控制器
    def setAnimCurveDict(self,obj,dict):
        nodeNames=dict.keys()
        mirrorNodeNames=[]
        for nodeName in nodeNames:
            mirrorNodeName=self.getMirrorNode(obj,nodeName)
            i=0
            while(i<=len(dict[nodeName])-1):
                mc.setKeyframe(mirrorNodeName,time=dict[nodeName][i]['time'],value=dict[nodeName][i]['value'])
                #mc.keyTangent(mirrorNodeName,index=(i,i),inAngle=dict[nodeName][i]['angle'])
                #mc.keyTangent(mirrorNodeName,index=(i,i),iWeight=dict[nodeName][i]['weight'])
                #mc.keyTangent(mirrorNodeName,index=(i,i),outAngle=dict[nodeName][i]['outangle'])
                mc.keyTangent(mirrorNodeName,index=(i,i),inAngle=dict[nodeName][i]['angle'],inWeight=dict[nodeName][i]['weight'],outAngle=dict[nodeName][i]['outangle'],outWeight=dict[nodeName][i]['outweight'])
                #mc.keyframe(mirrorNodeName,index=(i,i),timeChange=dict[mirrorNodeName][i]['time'],valueChange=dict[mirrorNodeName][i]['value'])
                i=i+1
"""
__author__ = 'xuweijian'
# -*- coding: utf-8 -*-


import maya.cmds as mc
from functools import partial
from idmt.maya.xwjModule.commonModule import animationModule
reload(animationModule)
animIns=animationModule.animationModule()


class copyDrivenKeyTool():
    def creatUI(self):
        if mc.window('mirrorDrivenKey',ex=1):
            mc.deleteUI('mirrorDrivenKey')
        mc.window('mirrorDrivenKey')
        mc.columnLayout('colMain',ca=2)
        mc.rowColumnLayout('rColOrg',ca=2,nr=2)
        mc.textFieldButtonGrp('tfOrgDriverObj',l=u'原驱动物体',bl='<<<',cw3=[100,200,50],bc=partial(self.setGrpTextField,'tfOrgDriverObj'))
        mc.textFieldButtonGrp('tfOrgDrivenObj',l=u'原被驱动物体',bl='<<<',cw3=[100,200,50],bc=partial(self.setGrpTextField,'tfOrgDrivenObj'))
        mc.textFieldButtonGrp('tfTgaDriverObj',l=u'目标驱动物体',bl='<<<',cw3=[100,200,50],bc=partial(self.setGrpTextField,'tfTgaDriverObj'))
        mc.textFieldButtonGrp('tfTgaDrivenObj',l=u'目标被驱动物体',bl='<<<',cw3=[100,200,50],bc=partial(self.setGrpTextField,'tfTgaDrivenObj'))
        mc.setParent('rColOrg')
        mc.setParent('colMain')
        mc.rowColumnLayout('rColInvertAttr',ca=9,nr=3)
        mc.checkBox( 'cbtx',label='tx' ,w=100)
        mc.checkBox( 'cbty',label='ty',w=100 )
        mc.checkBox( 'cbtz',label='tz',w=100)
        mc.checkBox( 'cbrx',label='rx' ,w=100)
        mc.checkBox( 'cbry',label='ry',w=100 )
        mc.checkBox( 'cbrz',label='rz',w=100 )
        mc.checkBox( 'cbsx',label='sx',w=100)
        mc.checkBox( 'cbsy',label='sy' ,w=100)
        mc.checkBox( 'cbsz',label='sz',w=100 )
        mc.setParent('rColInvertAttr')

        #cmds.checkBoxGrp( numberOfCheckBoxes=9, label=u'需要取反的属性', labelArray9=['tx', 'ty', 'tz','rx','ry','rz','sx','sy','sz'] )
        mc.setParent('colMain')
        mc.button(l='copy',w=700,c=partial(self.copyDrivenKey))
        mc.setParent('colMain')
        mc.showWindow('mirrorDrivenKey')

    def getCBinfo(self):
        listAtr=[]
        if mc.checkBox('cbtx',q=1 ,v=1):
            listAtr.append('translateX')
        if mc.checkBox('cbty' ,q=1 ,v=1):
            listAtr.append('translateY')
        if mc.checkBox('cbtz' ,q=1 ,v=1):
            listAtr.append('translateZ')


        if mc.checkBox('cbrx' ,q=1 ,v=1):
            listAtr.append('rotateX')
        if mc.checkBox('cbry' ,q=1 ,v=1):
            listAtr.append('rotateY')
        if mc.checkBox('cbrz' ,q=1 ,v=1):
            listAtr.append('rotateZ')


        if mc.checkBox('cbsx' ,q=1 ,v=1):
            listAtr.append('scaleX')
        if mc.checkBox('cbsy' ,q=1 ,v=1):
            listAtr.append('scaleY')
        if mc.checkBox('cbsz' ,q=1 ,v=1):
            listAtr.append('scaleZ')
        print listAtr
        return listAtr



    def setGrpTextField(self,tfgName):
        groupName=mc.ls(sl=1,type='transform')
        #selObj=mc.listRelatives(selObj,type=DestinationNote)
        GrpStr=','.join(groupName)
        mc.textFieldButtonGrp(tfgName,e=1,text=GrpStr)


    def getConnectInfo(self,obj):
        connectInfo=[]
        crtlToCurveInfo= mc.listConnections(obj,c=1,t='animCurve',p=1)
        for i in range(len(crtlToCurveInfo)/2):
            i=i*2
            #print crtlToCurveInfo[i+1]
            drivenObjAttr=mc.listConnections(crtlToCurveInfo[i+1].replace('input','output'),s=0,p=1)[0]
            connectDetailInfo=[crtlToCurveInfo[i],crtlToCurveInfo[i+1],drivenObjAttr]
            connectInfo.append(connectDetailInfo)
        return connectInfo



    #self.copyDrivenKey()
    #self.connectInfo=getConnectInfo(ctrl)
    #self.targetCtrl=getMirrorObj(ctrl)


    def copyDrivenKey(self,UI=''):
        sourceDriver=mc.textFieldButtonGrp('tfOrgDriverObj',q=1,tx=1)
        sourceDriven=mc.textFieldButtonGrp('tfOrgDrivenObj',q=1,tx=1)
        targetDriver=mc.textFieldButtonGrp('tfTgaDriverObj',q=1,tx=1)
        targetDriven=mc.textFieldButtonGrp('tfTgaDrivenObj',q=1,tx=1)
        connectInfo=self.getConnectInfo(sourceDriver)
        #sourceDriverAnimDict=animIns.getAnimCurveDict(sourceDriver,drvkey=1)
        sourceDrivenAnimDict=animIns.getAnimCurveDict(sourceDriven,drvKey=1)
        attrList=self.getCBinfo()
        print attrList
        newDrivenAnimDict=animIns.getMirrorDict(sourceDrivenAnimDict,attrList)
        print sourceDriver
        print sourceDriven
        print targetDriver
        print targetDriven
        print connectInfo
        print newDrivenAnimDict
        animIns.setAnimCurveDict(targetDriven,newDrivenAnimDict,drvKey=1)
        for one in connectInfo:
            curveNode=mc.listConnections(one,d=0,p=1)
            mc.connectAttr(one[0].replace(sourceDriver,targetDriver),one[1].replace(sourceDriven,targetDriven),f=1)
        #sourceDriverAttr=one[0].split('.')[1]

    def findAnimCurve(self,attr):
        mc.listConnections(attr,d=0,p=1)



'''
    def getMirrorObj(self,sourceObj):
        if 'Rt' in sourceObj:
            targetObj=sourceObj.replace('Rt','Lf')
        elif 'Lf' in sourceObj:
            targetObj=sourceObj.replace('Lf','Rt')
        else:
            mc.error('NO sign of right or left')
        return targetObj
'''




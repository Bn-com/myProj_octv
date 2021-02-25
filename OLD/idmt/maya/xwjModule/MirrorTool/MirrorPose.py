# -*- coding: utf-8 -*-
__author__ = 'xuweijian'
import maya.cmds as mc
import maya.mel as mel
import sys


class MirrorPose():
    thisClass = 'idmt.maya.xwjModule.MirrorTool.MirrorTool()'

    def getSelect(self):
        if len(mc.ls(sl=1))==0:
            mc.confirmDialog( title='Confirm', message=u'请选择一个角色控制器', button=['OK'], cancelButton='No')
            print u'脚本准备结束'
            sys.exit()
        elif len(mc.ls(sl=1))==1:
            selectObj=(mc.ls(sl=1)[0])
            print selectObj
        elif len(mc.ls(sl=1))>1:
            selectObj=(mc.ls(sl=1)[0])
            print selectObj
        return selectObj




    def getMirrorCtrl(self,Ctrl=''):
        prefixCtrl = self.divNamespace(Ctrl,1)
        if 'Lf' == prefixCtrl[0:2]:
            LRCtrl = prefixCtrl.replace('Lf','Rt')
        elif 'Rt' == prefixCtrl[0:2]:
            LRCtrl = prefixCtrl.replace('Rt','Lf')
        else:
            LRCtrl=prefixCtrl
        newCtrl = Ctrl.replace(prefixCtrl,LRCtrl)
        return newCtrl


    #------------把namespace和物体名分开，0返回namespace，1返回物体名------------------
    def divNamespace(self,obj,arg=False):
        objName=''
        if arg==0:
            namearr=obj.split(':')[0:-1]
            if len(namearr)>0:
                for i in range(len(namearr)):
                    objName=objName+namearr[i]+":"
        elif arg==1:
            objName=obj.split(':')[-1]
        return objName


    #-----------获取单个对象的所有属性和值返回一个字典-----------------
    def getAllAttrDict(self,obj=''):
        dict={}
        #print obj
        allAttr=mc.listAttr(obj,r=True,visible=True,keyable=True,unlocked=1)
        for oneAttr in allAttr:
            attrValue=mc.getAttr(obj + '.' + oneAttr)
            if not oneAttr in  dict.keys():
                dict[oneAttr]=attrValue
        return dict
        '''allAttr=mc.listAnimatable(obj)
        for oneAttr in allAttr:
            attrValue=mc.getAttr(oneAttr)
            if not oneAttr in  dict.keys():
                dict[oneAttr]=attrValue
        return dict'''



    #-------------检查控制器类型属于哪种类型的Set-----------------------
    def checkCtrlType(self,Ctrl):
        TheNameSpace=self.divNamespace(Ctrl,0)
        fingerType = mc.sets((TheNameSpace+'Lf_FingerSet'),(TheNameSpace+'Rt_FingerSet'),
                             (TheNameSpace+'Lf_ToesSet'),(TheNameSpace+'Rt_ToesSet'),q=True)
        BodySet = mc.sets((TheNameSpace+'BodySet'),q=True)
        IKType = mc.ls(TheNameSpace+'*Arm_Wrist_IK',TheNameSpace+'*Arm_Pole_ctrl',
                       TheNameSpace+'*Leg_Leg_IK',TheNameSpace+'*Leg_Pole_ctrl')
        bendType = mc.ls((TheNameSpace+'Lf*upArm1_bend'),(TheNameSpace+'Lf*upArm2_bend'),(TheNameSpace+'Lf*elbow1_bend'),
                     (TheNameSpace+'Rt*upArm1_bend'),(TheNameSpace+'Rt*upArm2_bend'),(TheNameSpace+'Rt*elbow1_bend'),
                     (TheNameSpace+'Lf*leg1_bend'),(TheNameSpace+'Lf*leg2_bend'),(TheNameSpace+'Lf*knee1_bend'),
                     (TheNameSpace+'Rt*leg1_bend'),(TheNameSpace+'Rt*leg2_bend'),(TheNameSpace+'Rt*knee1_bend'))
        if Ctrl in fingerType:
            return 'fingerType'
        elif Ctrl in IKType:
            return 'IKType'
        elif Ctrl in BodySet:
            return 'bodyType'
        elif Ctrl in bendType:
            return 'bendType'
        else:
            return 'FKType'



    #-------------镜像一个控制器，type为0时是单向复制，为1是镜像----------------
    def mirrorPose(self,Ctrl,type=False):
        try:
            ctrlType=self.checkCtrlType(Ctrl)
            mirrorCtrl=self.getMirrorCtrl(Ctrl)
            #print 'run sourceAttrDict'
            sourceAttrDict=self.getAllAttrDict(Ctrl)
            #print 'sourceAttrDict:'
            #print sourceAttrDict
            #print 'run targetAttrDict'
            targetAttrDict=self.getAllAttrDict(mirrorCtrl)
            #print 'targetAttrDict:'
            #print targetAttrDict
            if ctrlType=='IKType':
                for  oneattr in targetAttrDict:
                    try:
                        if oneattr=='translateX' or oneattr=='rotateY' or oneattr=='rotateZ':
                            mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr]*-1)
                            if type==1:
                                mc.setAttr((mirrorCtrl+'.'+oneattr),sourceAttrDict[oneattr]*-1)
                        else:
                            mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr])
                            if type==1:
                                mc.setAttr((mirrorCtrl+'.'+oneattr),sourceAttrDict[oneattr])
                    except:
                        continue
                    #print oneattr
            elif ctrlType=='fingerType':
                for  oneattr in targetAttrDict:
                    try:
                        if oneattr=='translateX':
                            mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr]*-1)
                            if type==1:
                                mc.setAttr((mirrorCtrl+'.'+oneattr),sourceAttrDict[oneattr]*-1)
                        else:
                            mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr])
                            if type==1:
                                mc.setAttr((mirrorCtrl+'.'+oneattr),sourceAttrDict[oneattr])
                    except:
                        continue
                    #print oneattr
            elif ctrlType=='bodyType':
                for  oneattr in targetAttrDict:
                    try:
                        if oneattr=='rotateY' or oneattr=='rotateZ' or oneattr=='translateX':
                            mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr]*-1)
                        else:
                            mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr])
                    except:
                        print 'error in '+oneattr
                        continue
            elif ctrlType=='FKType':
                for  oneattr in targetAttrDict:
                    try:
                        mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr])
                        if type==1:
                            mc.setAttr((mirrorCtrl+'.'+oneattr),sourceAttrDict[oneattr])
                    except:
                        continue
        except Exception,e:
            print Exception,":",e

    #——————————————选择所有set整体镜像——————————————
    def wholeMirror(self,obj):
        #slCtrl=self.getSelect()
        theNamespace=self.divNamespace(obj,0)
        BodySet = mc.sets((theNamespace+'BodySet'),q=True)
        ArmSet = mc.sets((theNamespace+'Lf_ArmSet'),q=True)
        FingerSet = mc.sets((theNamespace+'Lf_FingerSet'),q=True)
        LegSet = mc.sets((theNamespace+'Lf_LegSet'),q=True)
        ToesSet = mc.sets((theNamespace+'Lf_ToesSet'),q=True)
        allCtrl=[]
        if BodySet:
            for oneSet in BodySet:
                allCtrl.append(oneSet)
                #print oneSet
                #self.mirrorPose(oneSet,1)
        if ArmSet:
            for oneSet in ArmSet:
                allCtrl.append(oneSet)
                #print oneSet
                #self.mirrorPose(oneSet,1)
        if FingerSet:
            for oneSet in FingerSet:
                allCtrl.append(oneSet)
                #print oneSet
                #self.mirrorPose(oneSet,1)
        if LegSet:
            for oneSet in LegSet:
                allCtrl.append(oneSet)
                #print oneSet
                #self.mirrorPose(oneSet,1)
        print ToesSet
        if ToesSet:
            for oneSet in ToesSet:
                allCtrl.append(oneSet)
                #print oneSet
                #self.mirrorPose(oneSet,1)


        if allCtrl:
            allCtrl=list(set(allCtrl))
            for oneSet in allCtrl:
                self.mirrorPose(oneSet,1)




    def showToolwindow(self):
        if (mc.window('MirrorAnimCurveWindow', ex = 1 ) ) : mc.deleteUI('MirrorAnimCurveWindow', window = 1)
        if(mc.windowPref('MirrorAnimCurveWindow', ex = 1) ) : mc.windowPref('MirrorAnimCurveWindow', remove = 1)
        #mc.window( 'MirrorAnimCurveWindow',title = 'IDMT MirrorAnimCurveTool',width = 400,height = 300,menuBar = 1,rtf = 0)
        mc.window( 'MirrorAnimCurveWindow',title = 'IDMT MirrorAnimCurveTool')
        base = mc.columnLayout()
        commond=self.thisClass+'.wholeMirror()'
        mc.button(c=commond,l=u'全身Pose镜像')


        mc.showWindow('MirrorAnimCurveWindow')



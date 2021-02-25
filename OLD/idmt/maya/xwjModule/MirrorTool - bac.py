# -*- coding: utf-8 -*-
__author__ = 'xuweijian'
import maya.cmds as mc
import maya.mel as mel


class MirrorTool():
    try:
        thisClass = 'idmt.maya.xwjModule.MirrorTool.MirrorTool()'
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
    except Exception,e:
            print Exception,":",e

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
                    if oneattr=='translateX' or oneattr=='rotateY' or oneattr=='rotateZ':
                        mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr]*-1)
                        if type==1:
                            mc.setAttr((mirrorCtrl+'.'+oneattr),sourceAttrDict[oneattr]*-1)
                    else:
                        mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr])
                        if type==1:
                            mc.setAttr((mirrorCtrl+'.'+oneattr),sourceAttrDict[oneattr])
                    #print oneattr
            elif ctrlType=='fingerType':
                for  oneattr in targetAttrDict:
                    if oneattr=='translateX':
                        mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr]*-1)
                        if type==1:
                            mc.setAttr((mirrorCtrl+'.'+oneattr),sourceAttrDict[oneattr]*-1)
                    else:
                        mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr])
                        if type==1:
                            mc.setAttr((mirrorCtrl+'.'+oneattr),sourceAttrDict[oneattr])
                    #print oneattr
            elif ctrlType=='bodyType':
                for  oneattr in targetAttrDict:
                    try:
                        if oneattr=='rotateY' or oneattr=='rotateZ':
                            mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr]*-1)
                        else:
                            mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr])
                    except:
                        print 'error in '+oneattr
                        continue
            elif ctrlType=='FKType':
                for  oneattr in targetAttrDict:
                    mc.setAttr((Ctrl+'.'+oneattr),targetAttrDict[oneattr])
                    if type==1:
                        mc.setAttr((mirrorCtrl+'.'+oneattr),sourceAttrDict[oneattr])
        except Exception,e:
            print Exception,":",e

    #——————————————选择所有set整体镜像——————————————
    def wholeMirror(self):
        slCtrl=mc.ls(sl=1)[0]
        theNamespace=self.divNamespace(slCtrl,0)
        BodySet = mc.sets((theNamespace+'BodySet'),q=True)
        ArmSet = mc.sets((theNamespace+'Lf_ArmSet'),q=True)
        FingerSet = mc.sets((theNamespace+'Lf_FingerSet'),q=True)
        LegSet = mc.sets((theNamespace+'Lf_LegSet'),q=True)
        ToesSet = mc.sets((theNamespace+'Lf_ToesSet'),q=True)
        print(BodySet)
        if BodySet != None:
            for oneSet in BodySet:
                print oneSet
                self.mirrorPose(oneSet,1)
        if ArmSet!=None:
            for oneSet in ArmSet:
                print oneSet
                self.mirrorPose(oneSet,1)
        if FingerSet!=None:
            for oneSet in FingerSet:
                print oneSet
                self.mirrorPose(oneSet,1)
        if LegSet!=None:
            for oneSet in LegSet:
                print oneSet
                self.mirrorPose(oneSet,1)
        print ToesSet
        if ToesSet!=None:
            for oneSet in ToesSet:
                print oneSet
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



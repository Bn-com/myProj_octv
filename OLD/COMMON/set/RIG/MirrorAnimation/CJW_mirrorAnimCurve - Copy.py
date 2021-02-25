#***************************************************************************
# Script Name: MirrorAnimCurve
# Author: Justin.CHan
# Created: 2016-01-04
# Description: ##镜像动画曲线
# 
#***************************************************************************
# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
import re

class CJW_MirrorAnimCurveTool_Class():
    def __init__(self):
        pass
    def CJW_nameSpacTool(self,SelectOBJs):
        #SelectOBJs = mc.ls(sl=1)
        if SelectOBJs == None or SelectOBJs == []:
            mc.error(u'=====请选择相关物体=====')
        prefix = SelectOBJs[-1].split(':')
        TheNameSpace=""                       
        if len(prefix)>1:
            for i in range(len(prefix)-1):
                TheNameSpace=TheNameSpace+prefix[i]+":"            
        if len(prefix)==1:
            TheNameSpace=""    
        return TheNameSpace

    # LR 等于1为左右交换，等于2为右左交换
    def CJW_replaceLRTool(self, Ctrls, LR=0):
        NewCtrls = []
        if LR == 1:
            for ctrl in Ctrls:
                prefixCtrl = ctrl.split(':')
                if 'Lf' == prefixCtrl[-1][0:2]:
                    LRCtrl = prefixCtrl[-1].replace('Lf','Rt')
                    newCtrl = ctrl.replace(prefixCtrl[-1],LRCtrl)
                    if newCtrl not in NewCtrls:
                        NewCtrls.append(newCtrl)
        if LR == 2:
            for ctrl in Ctrls:
                prefixCtrl = ctrl.split(':')
                if 'Rt' == prefixCtrl[-1][0:2]:
                    LRCtrl = prefixCtrl[-1].replace('Rt','Lf')
                    newCtrl = ctrl.replace(prefixCtrl[-1],LRCtrl)
                    if newCtrl not in NewCtrls:
                        NewCtrls.append(newCtrl)            
        return NewCtrls

    def CJW_mirrorAnimCurve(self,Sets):
        SelectOBJs = mc.ls(sl=1)
        prefix = SelectOBJs[-1].split(':')
        TheNameSpace=""                       
        if len(prefix)>1:
            for i in range(len(prefix)-1):
                TheNameSpace=TheNameSpace+prefix[i]+":"            
        if len(prefix)==1:
            TheNameSpace=""
        '''
        Sets = [TheNameSpace+'Lf_ArmSet',TheNameSpace+'Lf_FingerSet',TheNameSpace+'Lf_LegSet',TheNameSpace+'Lf_ToesSet',
    TheNameSpace+'Rt_ArmSet',TheNameSpace+'Rt_FingerSet',TheNameSpace+'Rt_LegSet',TheNameSpace+'Rt_ToesSet']
        '''
        Sets = TheNameSpace + 'Lf_ArmSet'
        Ctrls = mc.sets(Sets, q=True )    
        naimCurveLists = dict({})
        for Ctrl in Ctrls:
            keyNodes = mc.keyframe(Ctrl,query=1,name=1)
            if keyNodes:
                naimCurveLists[Ctrl] = keyNodes    
        for Ctrl in Ctrls:
            #Lf==>Rt
            if 'Rt' in Ctrl:
                RtCtrl = Ctrl
                key = RtCtrl.replace('Rt','Lf')
                if key in naimCurveLists.keys():
                    animCruves = naimCurveLists[key]
                    for animCruve in animCruves:
                        AttrXX = animCruve.split('_')[-1]
                        Attr = re.sub(r'\d+$', '', AttrXX) #如果最后一位是数字，把数字去掉
                        RtCtrlAttr = RtCtrl+'.'+Attr
                        try:
                            oldRtCtrlConnection = mc.listConnections(RtCtrlAttr,d=0,s=1,connections=1)
                            if len(oldRtCtrlConnection)>0:
                                mc.disconnectAttr(oldRtCtrlConnection[1]+'.output',oldRtCtrlConnection[0])
                        except:
                            pass
                        try:
                            mc.connectAttr(animCruve+'.output',RtCtrlAttr)
                        except:
                            pass     
            #Rt==>Lf
            if 'Lf' in Ctrl:
                LfCtrl = Ctrl
                key = LfCtrl.replace('Lf','Rt')
                if key in naimCurveLists.keys():
                    animCruves = naimCurveLists[key]
                    for animCruve in animCruves:
                        AttrXX = animCruve.split('_')[-1]
                        Attr = re.sub(r'\d+$', '', AttrXX)
                        LfCtrlAttr = LfCtrl+'.'+Attr
                        try:
                            oldRtCtrlConnection = mc.listConnections(LfCtrlAttr,d=0,s=1,connections=1)
                            if len(oldRtCtrlConnection)>0:
                                mc.disconnectAttr(oldRtCtrlConnection[1]+'.output',oldRtCtrlConnection[0])
                        except:
                            pass
                        try:
                            mc.connectAttr(animCruve+'.output',LfCtrlAttr)
                        except:
                            pass    

    def CJW_allCtrlValueList(self,TheNameSpace,setName):
        ctrlAttyibutyValueLists = dict({})
        #LfCtrlAttyibutyValueLists = dict({})
        #RtCtrlAttyibutyValueLists = dict({})               
        LRset = ''
        Sets = (TheNameSpace+setName)
        if 'Lf' == setName[0:2]:
            LRset = setName.replace('Lf','Rt')
            Sets = (TheNameSpace+setName),(TheNameSpace+LRset)
            '''
            Ctrls = mc.sets(Sets, q=True)
            for Ctrl in Ctrls:
                CtrlAttributes = mc.listAttr( Ctrl,r=True, visible=True ,keyable=True)
                CtrlAttrValues = []            
                for CtrlAttribute in CtrlAttributes:
                    attributeValue = mc.getAttr(Ctrl+'.'+CtrlAttribute)
                    CtrlAttrValue = CtrlAttribute,attributeValue            
                    if not CtrlAttrValue in CtrlAttrValues:
                        CtrlAttrValues.append(CtrlAttrValue)            
                LfCtrlAttyibutyValueLists[Ctrl] = CtrlAttrValues
            '''
        if 'Rt' == setName[0:2]:
            LRset = setName.replace('Rt','Lf')
            Sets = (TheNameSpace+setName),(TheNameSpace+LRset)
            '''
            Ctrls = mc.sets(Sets, q=True)
            for Ctrl in Ctrls:
                CtrlAttributes = mc.listAttr( Ctrl,r=True, visible=True ,keyable=True)
                CtrlAttrValues = []            
                for CtrlAttribute in CtrlAttributes:
                    attributeValue = mc.getAttr(Ctrl+'.'+CtrlAttribute)
                    CtrlAttrValue = CtrlAttribute,attributeValue            
                    if not CtrlAttrValue in CtrlAttrValues:
                        CtrlAttrValues.append(CtrlAttrValue)            
                RtCtrlAttyibutyValueLists[Ctrl] = CtrlAttrValues
            '''
        Ctrls = mc.sets(Sets, q=True)
        for Ctrl in Ctrls:
            CtrlAttributes = mc.listAttr( Ctrl,r=True, visible=True ,keyable=True)
            CtrlAttrValues = []
            for CtrlAttribute in CtrlAttributes:
                attributeValue = mc.getAttr(Ctrl+'.'+CtrlAttribute)
                CtrlAttrValue = CtrlAttribute,attributeValue
                if not CtrlAttrValue in CtrlAttrValues:
                    CtrlAttrValues.append(CtrlAttrValue)
            ctrlAttyibutyValueLists[Ctrl] = CtrlAttrValues
        #return ctrlAttyibutyValueLists,LfCtrlAttyibutyValueLists,RtCtrlAttyibutyValueLists   
        return ctrlAttyibutyValueLists

    def CJW_mirrorPose(self,rb1,rb2,rb3,rb4,selectObjs,selectSet):
        rb1num = mc.radioButtonGrp(rb1, q=1, sl = 1)
        rb2num = mc.radioButtonGrp(rb2, q=1, sl = 1)    
        rb3num = mc.radioButtonGrp(rb3, q=1, sl = 1)   
        rb4num = mc.radioButtonGrp(rb4, q=1, sl = 1)
        selectCtrls =  mc.textFieldButtonGrp(selectObjs, q=1, text= 1) 
        CtrlSet = selectSet
        Ctrls = mc.ls(sl=1)
        TheNameSpace = self.CJW_nameSpacTool(Ctrls)
        AllctrlAttyibutyValueLists = self.CJW_allCtrlValueList(TheNameSpace,CtrlSet)
        MiCtrlAttyibutyValueLists = AllctrlAttyibutyValueLists[0]
        LfCtrlAttyibutyValueLists = AllctrlAttyibutyValueLists[1]        
        RtCtrlAttyibutyValueLists = AllctrlAttyibutyValueLists[2]        
        MiCtrls = MiCtrlAttyibutyValueLists.keys()
        LfCtrls = LfCtrlAttyibutyValueLists.keys()
        RTCtrls = RtCtrlAttyibutyValueLists.keys()        
        if rb3num == 1:
            for LfCtrl in LfCtrls:
                try:
                    CtrlAttrValues = LfCtrlAttyibutyValueLists[LfCtrl]
                    CtrlType = self.CJW_mirrorAnimCtrlType(TheNameSpace,LfCtrl)
                    if CtrlType == 'fingerType':
                        for CtrlAttrValue in CtrlAttrValues:
                            if 'translate' in CtrlAttrValue[0]:
                                mc.setAttr((Ctrl+'.'+CtrlAttrValue[0]),(CtrlAttrValue[1]*-1))
                            else:
                                mc.setAttr((Ctrl+'.'+CtrlAttrValue[0]),(CtrlAttrValue[1]))                 
                    if CtrlType == 'IKType':
                       for CtrlAttrValue in CtrlAttrValues:
                           if 'translateX' in CtrlAttrValue[0] or 'rotateY' in CtrlAttrValue[0] or 'rotateZ' in CtrlAttrValue[0]:
                               mc.setAttr((Ctrl+'.'+CtrlAttrValue[0]),(CtrlAttrValue[1]*-1))
                           else:
                               mc.setAttr((Ctrl+'.'+CtrlAttrValue[0]),(CtrlAttrValue[1]))               
                    if CtrlType == 'bendType':
                        for CtrlAttrValue in CtrlAttrValues:
                            if 'translateY' in CtrlAttrValue[0] or 'translateZ' in CtrlAttrValue[0]:
                                mc.setAttr((Ctrl+'.'+CtrlAttrValue[0]),(CtrlAttrValue[1]*-1))
                            else:
                                mc.setAttr((Ctrl+'.'+CtrlAttrValue[0]),(CtrlAttrValue[1])) 
                    if CtrlType == 'FKType':
                        for CtrlAttrValue in CtrlAttrValues:
                            mc.setAttr((RtCtrl+'.'+CtrlAttrValue[0]),(CtrlAttrValue[1]))
                except:
                    mc.error(u'=====控制器【%s】不在CtrlSet里，请通知设置更新=====')%(Ctrl)
                    pass

    def CJW_mirrorAnimCtrlType(self,TheNameSpace,Ctrl):  
        fingerType = mc.sets((TheNameSpace+'Lf_FingerSet'),(TheNameSpace+'Rt_FingerSet'),
                             (TheNameSpace+'Lf_ToesSet'),(TheNameSpace+'Rt_ToesSet'),q=True)
        if Ctrl in fingerType:
            return 'fingerType'   
        BodySet = mc.sets((TheNameSpace+'BodySet'),q=True)
        IKType = mc.ls(TheNameSpace+'*Arm_Wrist_IK',TheNameSpace+'*Arm_Pole_ctrl',
                       TheNameSpace+'*Leg_Leg_IK',TheNameSpace+'*Leg_Pole_ctrl')
        if Ctrl in BodySet or Ctrl in IKType:
            return 'IKType'  
        bendType = mc.ls((TheNameSpace+'Lf*upArm1_bend'),(TheNameSpace+'Lf*upArm2_bend'),(TheNameSpace+'Lf*elbow1_bend'),
                         (TheNameSpace+'Rt*upArm1_bend'),(TheNameSpace+'Rt*upArm2_bend'),(TheNameSpace+'Rt*elbow1_bend'),
                         (TheNameSpace+'Lf*leg1_bend'),(TheNameSpace+'Lf*leg2_bend'),(TheNameSpace+'Lf*knee1_bend'),
                         (TheNameSpace+'Rt*leg1_bend'),(TheNameSpace+'Rt*leg2_bend'),(TheNameSpace+'Rt*knee1_bend'))
        if Ctrl in bendType:
            return 'bendType'
    
        else:
            return 'FKType'
    
    def CJW_MirrorAnimCurveWindowTool(self):
        if (mc.window('MirrorAnimCurveWindow', ex = 1 ) ) : mc.deleteUI('MirrorAnimCurveWindow', window = 1) 
        if(mc.windowPref('MirrorAnimCurveWindow', ex = 1) ) : mc.windowPref('MirrorAnimCurveWindow', remove = 1)  
        mc.window ( 'MirrorAnimCurveWindow',title = 'IDMT MirrorAnimCurveTool',width = 400,height = 300,menuBar = 1,rtf = 0)    
        base = mc.formLayout(numberOfDivisions = 100)
        rb1 = mc.radioButtonGrp  ('CJW_MirrorAnimCurveWindowToolRB1',numberOfRadioButtons = 3,
                                  l = u"镜像中心 : ",
                                  labelArray3 = (u"以世界坐标", u"以角色Master", u"以角色腰部"),
                                  sl = 2,
                                  cw4 = (85,85,95,85),
                                  ct4 = ("left", "left", "left", "left"),
                                  editable = 0
                                  )
        mc.formLayout (base,
                    e = 1,
                    attachForm = [(rb1, "top", 20),(rb1, "left", 5)],
                    attachPosition = (rb1, "right", 0, 75)    
                    ) 
        rb2 = mc.radioButtonGrp  ('CJW_MirrorAnimCurveWindowToolRB2',numberOfRadioButtons = 3,
                                  l = u"镜像轴向 : ",
                                  labelArray3 = (u"X轴", u"Y轴", u"Z轴"),
                                  sl = 1,
                                  cw4 = (85,85,95,85),
                                  ct4 = ("left", "left", "left", "left"),
                                  editable = 0
                                  )    
        mc.formLayout (base,
                    e = 1,
                    attachForm = [(rb2, "top", 45),(rb2, "left", 5)],
                    attachPosition = (rb2, "right", 0, 75)    
                    )
        
        rb3 = mc.radioButtonGrp  ('CJW_MirrorAnimCurveWindowToolRB3',numberOfRadioButtons = 3,
                                  l = u"镜像方向 : ",
                                  labelArray3 = (u"两边镜像", u"左边==>右边", u"右边==>左边"),
                                  sl = 1,
                                  cw4 = (85,85,95,85),
                                  ct4 = ("left", "left", "left", "left") 
                                  )    
        mc.formLayout (base,
                    e = 1,
                    attachForm = [(rb3, "top", 70),(rb3, "left", 5)],
                    attachPosition = (rb3, "right", 0, 75)    
                    )
          
        rb4 = mc.radioButtonGrp  ('CJW_MirrorAnimCurveWindowToolRB4',numberOfRadioButtons = 2,
                                  l = u"相关控制器 : ",
                                  labelArray2 = (u"所有控制器", u"选中的控制器"),
                                  sl = 1,
                                  cw3 = (85,85,95),
                                  ct3 = ("left", "left", "left") 
                                  )    
        mc.formLayout (base,
                    e = 1,
                    attachForm = [(rb4, "top", 95),(rb4, "left", 5)],
                    attachPosition = (rb4, "right", 0, 75)    
                    ) 
        
        selectObjs = mc.textFieldButtonGrp(
                            label = u'选中角色控制器', 
                            cw3 = (90, 230, 50), 
                            buttonLabel = "<<<"
                            ) 
        mc.textFieldButtonGrp(selectObjs,
                    e=1,
                    buttonCommand = ''
                    )
        mc.formLayout (base,
                    e = 1, 
                    attachForm  =  [(selectObjs, "top", 125),(selectObjs, "left", 5) ],
                    attachPosition = (selectObjs, "right", 0, 75)             
                )
        parentLabel = mc.text (label = u"镜像POSE:")
        mc.formLayout (base,
            e = 1, 
            attachForm  = [(parentLabel, "top", 160),(parentLabel,"left", 5)],
            attachPosition  = (parentLabel,"right", 0, 100))
        mirrorFPoseButton = mc.button  (label = u"镜像手指Pose",
            command = "from RIG.MirrorAnimation import CJW_mirrorAnimCurve;reload(CJW_mirrorAnimCurve);CJW_mirrorAnimCurve.CJW_MirrorAnimCurveTool_Class().CJW_mirrorPose('"+rb1+"','"+rb2+"','"+rb3+"','"+rb4+"','"+selectObjs+"','Lf_FingerSet')",
            width = 80,
            height = 32,
            al = "center")
        mc.formLayout(base,e = 1, attachForm  = [(mirrorFPoseButton, "top", 180),(mirrorFPoseButton, "left", 50)])
        mirrorAPoseButton = mc.button  (label = u"镜像手臂Pose",
            command = '',
            width = 80,
            height = 32,
            al = "center")
        mc.formLayout(base,e = 1, attachForm  = [(mirrorAPoseButton, "top", 180),(mirrorAPoseButton, "left", 130)])
        mirrorTPoseButton = mc.button  (label = u"镜像脚趾Pose",
            command = '',
            width = 80,
            height = 32,
            al = "center")
        mc.formLayout(base,e = 1, attachForm  = [(mirrorTPoseButton, "top", 180),(mirrorTPoseButton, "left", 210)])
        mirrorLPoseButton = mc.button  (label = u"镜像腿部Pose",
            command = '',
            width = 80,
            height = 32,
            al = "center")
        mc.formLayout(base,e = 1, attachForm  = [(mirrorLPoseButton, "top", 180),(mirrorLPoseButton, "left", 290)])
        mirrorPoseButton = mc.button  (label = u"镜像全身POSE",
            command = '',
            width = 300,
            height = 32,
            al = "center")
        mc.formLayout(base,e = 1, attachForm  = [(mirrorPoseButton, "top", 220),(mirrorPoseButton, "left", 50)])   
        parentLabe2 = mc.text (label = u"镜像动画曲线:")
        mc.formLayout (base,
            e = 1, 
            attachForm  = [(parentLabe2, "top", 260),(parentLabe2,"left", 5)],
            attachPosition  = (parentLabe2,"right", 0, 100))
        mirrorPoseButton2 = mc.button  (label = u"镜像动画曲线",
            command = '',
            width = 300,
            height = 32,
            al = "center")  
        mc.formLayout(base,e = 1, attachForm  = [(mirrorPoseButton2, "top", 260),(mirrorPoseButton2, "left", 50)])                  
        mc.showWindow('MirrorAnimCurveWindow')
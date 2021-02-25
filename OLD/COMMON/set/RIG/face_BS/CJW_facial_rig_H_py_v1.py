# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
import re
import os
import headfile
AutoRigPath = headfile.__file__.replace('headfile.py','RIG/').replace('\\','/')
execfile(AutoRigPath+'edo_ikfkSwitch.py')
class CJW_facial_rig_H_py_v1_Class():
    def __init__(self):
        pass
    def CJW_H_Facial_Animation_Action_Tool(self):
        ui = AutoRigPath+'face_BS/CJW_facial_rig_H_ui_Action.myuis'
        if mc.window('CJW_facial_Action_win', ex=1):
            mc.deleteUI('CJW_facial_Action_win')
        mui = mc.loadUI(f=ui)
        mc.showWindow(mui)

    def CJW_H_Facial_GUI(self):
        SelectOBJs = mc.ls(sl=1)
        if SelectOBJs==None or SelectOBJs==[]:
            mc.warning(u'====请选择相关物体====')
        else:
            TheNameSpace = self.CJW_ReferenceNamespace(SelectOBJs)
            if len(TheNameSpace)>1:
                characterName = TheNameSpace
            else:
                characterName = ''

            #CJW_FacialGUI = TheNameSpace+'CJW_H_FacialGUI'
            CJW_FacialGUI = 'CJW_H_v1_UI'
            if mc.window(CJW_FacialGUI,exists=True):
                mc.deleteUI(CJW_FacialGUI)
            if mc.windowPref(CJW_FacialGUI,exists=True):
                mc.windowPref(CJW_FacialGUI,remove=True)
            MainWindow = mc.window(CJW_FacialGUI,title=characterName,menuBar=True,wh=(600,700),sizeable =True ,minimizeButton=True,maximizeButton=False,resizeToFitChildren = True)
            FormLayOut = mc.formLayout(numberOfDivisions=100)
            FACIAL_GUI_Camera = mc.ls(TheNameSpace+'FM_FACIAL_CAM',r=1)
            mc.select(cl=1)
            mc.select(TheNameSpace+'FM_Cam_FACIAL_gui_guides_grp',TheNameSpace+'CHR_Pier_Lips_Neutre_CTRL_GRP')
            CAM_View = mc.modelEditor(displayAppearance='smoothShaded',viewSelected=1,ignorePanZoom=1,grid=0,wireframeOnShaded=1,headsUpDisplay=1,displayTextures=1,textures=1,camera=FACIAL_GUI_Camera[0])
            KEY_LOOK = mc.button(label=u'表情\n归零',annotation=u'表情控制器归零',backgroundColor = (0.5,0,0),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_initialPose(\'%s\',\'All_FacialSet\')'%(TheNameSpace))
            KEY_FLIP = mc.button(label='LOOK\nKEY',annotation=u'眼球控制器K帧',backgroundColor = (0.5,0.8,0.9),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'LookSet\')'%(TheNameSpace))
            KEY_BROWS = mc.button(label='BROWS\nKEY',annotation=u'眉毛控制器K帧',backgroundColor = (0.5,0.8,0.9),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'BrowsSet\')'%(TheNameSpace))
            KEY_LIPS = mc.button(label='LIPS\nKEY',annotation=u'嘴唇控制器K帧',backgroundColor = (0.5,0.8,0.9),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'LipsSet\')'%(TheNameSpace))
            KEY_MOUTH = mc.button(label='MOUTH\nKEY',annotation=u'嘴部控制器K帧',backgroundColor = (0.5,0.8,0.9 ),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'MouthSet\')'%(TheNameSpace))
            KEY_ALLBODY = mc.button(label='ALL\nKEY',annotation=u'全部面部控制器K帧',backgroundColor = (0.5,0.8,0.9),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'All_FacialSet\')'%(TheNameSpace))
            CheckBox01 = mc.checkBox( 'KeyADD',label=u'自动K帧',backgroundColor = (0.6,0.6,0.6),value=0 )
            CheckBox02 = mc.checkBox( 'CtrlADD',label=u'加选',backgroundColor = (0.6,0.6,0.6),value=0 )
            mc.select(cl=1)
            mc.formLayout(FormLayOut,edit=1,
attachForm=[(CAM_View,'top',4), (CAM_View, 'left', 4),(KEY_LOOK,'top',4),(KEY_LOOK,'right',4),(KEY_FLIP,'right',4),(KEY_BROWS,'right',4),
(KEY_LIPS,'right',4),(KEY_MOUTH,'right',4),(KEY_ALLBODY,'left',4),(KEY_ALLBODY,'right',4),(KEY_ALLBODY,'bottom',4),
(CheckBox01,'top',12),(CheckBox02,'top',30)],
attachControl =[(CAM_View,'bottom',4,KEY_ALLBODY),(KEY_LOOK,'left',4,CAM_View),(KEY_FLIP,'top',4,KEY_LOOK),(KEY_FLIP,'left',4,CAM_View),(KEY_BROWS,'top',4,KEY_FLIP),(KEY_BROWS,'left',4,CAM_View),
(KEY_LIPS,'top',4,KEY_BROWS),(KEY_LIPS,'left',4,CAM_View),(KEY_MOUTH,'top',4,KEY_LIPS),(KEY_MOUTH,'left',4,CAM_View),(KEY_MOUTH,'bottom',4,KEY_ALLBODY),
(CheckBox01,'right',12,KEY_LOOK),(CheckBox02,'right',12,KEY_LOOK)],
attachPosition=[(CAM_View,'right',4,92),(KEY_LOOK,'bottom',4,9),(KEY_FLIP,'bottom',4,29),(KEY_BROWS,'bottom',4,49),(KEY_LIPS,'bottom',4,71)])
            mc.showWindow(CJW_FacialGUI)
            self.CJW_TextureReset()
            self.CJW_CheckLocalInfoPath()
            mel.eval('setObjectPickMask "Surface" 1;')
            ScriptJobSCIndex = mc.scriptJob(event = ('SelectionChanged',self.CJW_SelectonRIGCtrlTool),parent = CJW_FacialGUI,compressUndo=1)
            try:
                mc.setAttr(TheNameSpace+'show_Ctrl.AUOFVEEESZMBP',1)
            except:
                pass

    def CJW_H_Body_GUI(self):
        SelectOBJs = mc.ls(sl=1)
        if SelectOBJs==None or SelectOBJs==[]:
            mc.warning(u'====请选择相关物体====')
        else:
            TheNameSpace = self.CJW_ReferenceNamespace(SelectOBJs)
            if len(TheNameSpace)>1:
                characterName = TheNameSpace
            else:
                characterName = ''

            #CJW_BodyGUI = TheNameSpace+'CJW_H_BodyGUI'
            CJW_BodyGUI = 'CJW_H_v1_UI'
            if mc.window(CJW_BodyGUI,exists=True):
                mc.deleteUI(CJW_BodyGUI)
            if mc.windowPref(CJW_BodyGUI,exists=True):
                mc.windowPref(CJW_BodyGUI,remove=True)
            MainWindow = mc.window(CJW_BodyGUI,title=characterName,menuBar=True,wh=(700,670),sizeable =True ,minimizeButton=True,maximizeButton=False,resizeToFitChildren = True)
            FormLayOut = mc.formLayout(numberOfDivisions=100)
            BODY_GUI_Camera = mc.ls(TheNameSpace+'FM_BODY_CAM',r=1)
            mc.select(cl=1)
            mc.select(TheNameSpace+'FM_Cam_BODY_gui_guides_grp')
            CAM_View = mc.modelEditor(displayAppearance='smoothShaded',viewSelected=1,ignorePanZoom=1,grid=0,wireframeOnShaded=1,headsUpDisplay=1,displayTextures=1,textures=1,camera=BODY_GUI_Camera[0])
            KEY_LfArm = mc.button(label='Lf Arm\nKEY',annotation=u'左臂控制器K帧',backgroundColor = (0.5,0.8,0.9),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'Lf_ArmSet\')'%(TheNameSpace))
            KEY_RtArm = mc.button(label='Rt Arm\nKEY',annotation=u'右臂控制器K帧',backgroundColor = (0.5,0.8,0.9),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'Rt_ArmSet\')'%(TheNameSpace))
            KEY_LfFinger = mc.button(label='LF Finger\nKEY',annotation=u'左手指K帧',backgroundColor = (0.25,0.5,0.25),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'Lf_FingerSet\')'%(TheNameSpace))
            KEY_RtFinger = mc.button(label='Rt Finger\nKEY',annotation=u'右手指K帧',backgroundColor = (0.25,0.5,0.25),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'Rt_FingerSet\')'%(TheNameSpace))
            KEY_BODY1 = mc.button(label='Body\nKEY',annotation=u'躯干控制器K帧',backgroundColor = (0.75,0.6,0.35),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'BodySet\')'%(TheNameSpace))
            KEY_BODY2 = mc.button(label=u'初始\nT-POSE',annotation=u'恢复全身初始Pose',backgroundColor = (0.671,0.671,0.671),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_initialPose(\'%s\',\'All_BodySet\')'%(TheNameSpace))
            KEY_LfLeg = mc.button(label='Le Leg\nKEY',annotation=u'左腿控制器K帧',backgroundColor = (0.5,0.8,0.9),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'Lf_LegSet\')'%(TheNameSpace))
            KEY_RtLeg = mc.button(label='Rt Leg\nKEY',annotation=u'右腿控制器K帧',backgroundColor = (0.5,0.8,0.9),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'Rt_LegSet\')'%(TheNameSpace))
            KEY_LfToes = mc.button(label='Lf Toes\nKEY',annotation=u'左脚趾控制器K帧',backgroundColor = (0.25,0.5,0.25),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'Lf_ToesSet\')'%(TheNameSpace))
            KEY_RtToes = mc.button(label='Rt Toes\nKEY',annotation=u'右脚趾控制器K帧',backgroundColor = (0.25,0.5,0.25),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'Rt_ToesSet\')'%(TheNameSpace))
            KEY_ALLBODY = mc.button(label='ALL BODY\nKEY',annotation=u'全部身体控制器K帧',backgroundColor = (0.5,0.8,0.9),command='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_KeyCtrlTool(\'%s\',\'All_BodySet\')'%(TheNameSpace))
            IKFK_Switch = mc.button(label=u'IK/FK\n无缝切换',annotation=u'选中控制器IKFK无缝切换',backgroundColor = (0.941,0.332,0.332),command='from RIG import edo_ikfkSwitch\nreload(edo_ikfkSwitch)\nedo_ikfkSwitch.edo_ikfkSwitch()')
            CheckBox01 = mc.checkBox( 'KeyADD',label=u'自动K帧',backgroundColor = (0.6,0.6,0.6),value=0 )
            CheckBox02 = mc.checkBox( 'CtrlADD',label=u'加选',backgroundColor = (0.6,0.6,0.6),value=0 )
            mc.select(cl=1)
            mc.formLayout(FormLayOut,edit=1,
attachForm=[(CAM_View,'top',4),(KEY_LfArm,'top',4),(KEY_LfArm,'right',4),(KEY_LfFinger,'right',4),(KEY_BODY1,'right',4),(KEY_LfLeg,'right',4),(KEY_LfToes,'right',4),(KEY_ALLBODY,'left',4),(KEY_ALLBODY,'right',4),(KEY_ALLBODY,'bottom',4),
(KEY_RtArm,'top',4),(KEY_RtArm,'left',4),(KEY_RtFinger,'left',4),(KEY_BODY2,'left',4),(KEY_RtLeg,'left',4),(KEY_RtToes,'left',4),
(IKFK_Switch,'top',12),(CheckBox01,'top',12),(CheckBox02,'top',30)],
attachControl =[(CAM_View,'bottom',4,KEY_ALLBODY),(KEY_LfArm,'left',4,CAM_View),(KEY_LfFinger,'top',4,KEY_LfArm),(KEY_LfFinger,'left',4,CAM_View),(KEY_BODY1,'top',4,KEY_LfFinger),(KEY_BODY1,'left',4,CAM_View),
(KEY_LfLeg,'top',4,KEY_BODY1),(KEY_LfLeg,'left',4,CAM_View),(KEY_LfToes,'top',4,KEY_LfLeg),(KEY_LfToes,'left',4,CAM_View),(KEY_LfToes,'bottom',4,KEY_ALLBODY),
(KEY_RtArm,'right',4,CAM_View),(KEY_RtFinger,'top',4,KEY_RtArm),(KEY_RtFinger,'right',4,CAM_View),(KEY_BODY2,'top',4,KEY_RtFinger),(KEY_BODY2,'right',4,CAM_View),(KEY_RtLeg,'top',4,KEY_BODY2),(KEY_RtLeg,'right',4,CAM_View),(KEY_RtToes,'top',4,KEY_RtLeg),(KEY_RtToes,'right',4,CAM_View),(KEY_RtToes,'bottom',4,KEY_ALLBODY),
(IKFK_Switch,'right',12,KEY_LfArm),(CheckBox01,'right',70,KEY_LfArm),(CheckBox02,'right',70,KEY_LfArm)],
attachPosition=[(CAM_View,'right',4,92),(KEY_LfArm,'bottom',4,20),(KEY_LfFinger,'bottom',4,32),(KEY_BODY1,'bottom',4,59),(KEY_LfLeg,'bottom',4,82),
(CAM_View,'left',4,9),(KEY_RtArm,'bottom',4,20),(KEY_RtFinger,'bottom',4,32),(KEY_BODY2,'bottom',4,59),(KEY_RtLeg,'bottom',4,82)])
            mc.showWindow(CJW_BodyGUI)
            self.CJW_TextureReset()
            self.CJW_CheckLocalInfoPath()
            mel.eval('setObjectPickMask "Surface" 1;')
            ScriptJobSCIndex = mc.scriptJob(event = ('SelectionChanged',self.CJW_SelectonRIGCtrlTool),parent = CJW_BodyGUI,compressUndo=1)


    def CJW_ReferenceNamespace(self,SelectOBJs):
        prefix = SelectOBJs[-1].split(':')
        TheNameSpace=""
        if len(prefix)>1:
            for i in range(len(prefix)-1):
                TheNameSpace=TheNameSpace+prefix[i]+":"
                #characterName = TheNameSpace.split('_')[1]
        if len(prefix)==1:
            TheNameSpace=""
            #characterName = u'试试'
        return TheNameSpace

    def CJW_SelectonRIGCtrlTool(self):
        SelectOBJs = mc.ls(sl=True)
        if len(SelectOBJs)==0:
            self.CJW_TextureReset()
        if len(SelectOBJs)>0:
            if SelectOBJs[-1].split('_')[-1] == 'guide':
                for SelectOBJ in SelectOBJs:
                    if mc.nodeType(SelectOBJ) == 'transform':
                        if SelectOBJ.split('_')[-1] == 'guide':
                            SelectCtrl =  re.sub('_[^_]+$', '',SelectOBJ)
                            if mc.objExists(SelectCtrl):
                                mc.select(SelectOBJ,deselect=1)
                                mc.select(SelectCtrl,tgl=1)
                            else:
                                mc.warning(u'====无【%s】控制器对应===='%(SelectCtrl))
            self.CJW_TextureReset()
            self.CJW_TextureWire()

    def CJW_TextureReset(self):
        #ico_IK = ['RtArm_Wrist_IK_guide','RtArm_Pole_ctrl_guide','LfArm_Pole_ctrl_guide','LfArm_Wrist_IK_guide','top_waist_ikCtrl_guide','mid_waist_ikCtrl_guide','root_waist_ikCtrl_guide','RtLeg_Pole_ctrl_guide','LfLeg_Pole_ctrl_guide','RtLeg_Leg_IK_guide','LfLeg_Leg_IK_guide','RtLeg_foot_guide','LfLeg_foot_guide']
        #ico_FK = ['Rt_shoulder_guide','waist_Ctrl_guide','Rt_hip_ctrl_guide','Lf_hip_ctrl_guide','Lf_shoulder_guide']
        TheNameSpace = mc.window('CJW_H_v1_UI',q=1,title=1)
        characterNumber = TheNameSpace[0:10]
        projectServerPath = '//file-cluster/GDC/Resource/Support/Maya/GDC/2013/RIG/Projects/MiniTiger/%s.txt' % (characterNumber)
        if os.path.exists(projectServerPath):
            try:
                ConnectionNodes = self.CJW_CheckLocalInfoRead(projectServerPath)
                for ConnectionNode in ConnectionNodes:
                    info = ConnectionNode.split('\'')
                    SelectGuideShape = info[1].split('.')[0]
                    if TheNameSpace + 'CJW_selectPannel_selectDefaultSurfaceShaderSG' in mc.listConnections(TheNameSpace + SelectGuideShape,s=0,d=1,connections=1):
                        mc.sets(TheNameSpace + SelectGuideShape,forceElement= TheNameSpace + info[3])
            except:
                pass
        else:
            TXTName = 'CJW_H_v1'
            localTXTpath = 'D:/Info_Temp/JustinCHan_temp/%s.txt' % (TXTName)
            if os.path.exists(localTXTpath):
                try:
                    ConnectionNodes = self.CJW_CheckLocalInfoRead(localTXTpath)
                    for ConnectionNode in ConnectionNodes:
                        info = ConnectionNode.split('\'')
                        SelectGuideShape = info[1].split('.')[0]
                        if TheNameSpace + 'CJW_selectPannel_selectDefaultSurfaceShaderSG' in mc.listConnections(SelectGuideShape,s=0,d=1,connections=1):
                            mc.sets(SelectGuideShape,forceElement= info[3])
                except:
                    pass

    def CJW_TextureWire(self):
        TheNameSpace = mc.window('CJW_H_v1_UI',q=1,title=1)
        characterNumber = TheNameSpace[0:10]
        projectServerPath = '//file-cluster/GDC/Resource/Support/Maya/GDC/2013/RIG/Projects/MiniTiger/%s.txt' % (characterNumber)
        if os.path.exists(projectServerPath):
            AllSelectCtrls = mc.ls(sl=1)
            for SelectCtrl in AllSelectCtrls:
                SelectGuide = SelectCtrl+'_guide'
                if mc.objExists(SelectGuide):
                    SelectGuideShape = mc.listRelatives(SelectGuide,type = 'mesh')[0]
                    PreConnections = mc.listConnections(SelectGuideShape,s=0,d=1,connections=1)
                    if not TheNameSpace + 'CJW_selectPannel_selectDefaultSurfaceShaderSG' in PreConnections:
                        mc.sets(SelectGuideShape,forceElement = TheNameSpace + 'CJW_selectPannel_selectDefaultSurfaceShaderSG')
        else:
            TXTName = 'CJW_H_v1'
            TXTpath = 'D:/Info_Temp/JustinCHan_temp/%s.txt' % (TXTName)
            OldConnectionNodes = self.CJW_CheckLocalInfoRead(TXTpath)
            ConnectionNodes =[]
            AllSelectCtrls = mc.ls(sl=1)
            for SelectCtrl in AllSelectCtrls:
                SelectGuide = SelectCtrl+'_guide'
                if mc.objExists(SelectGuide):
                    SelectGuideShape = mc.listRelatives(SelectGuide,type = 'mesh')[0]
                    PreConnections = mc.listConnections(SelectGuideShape,s=0,d=1,connections=1)
                    if not TheNameSpace + 'CJW_selectPannel_selectDefaultSurfaceShaderSG' in PreConnections:
                        if not OldConnectionNodes == []:
                            PassNu = 0
                            for OldConnectionNode in OldConnectionNodes:
                                if PreConnections[0] in OldConnectionNode:
                                    PassNu = 1
                            if PassNu == 0:
                                ConnectionNodes.append(PreConnections)
                        else:
                            ConnectionNodes.append(PreConnections)
                    mc.sets(SelectGuideShape,forceElement = TheNameSpace + 'CJW_selectPannel_selectDefaultSurfaceShaderSG')
            self.CJW_CheckLocalInfoWirte(TXTpath,ConnectionNodes,1)

    def CJW_KeyCtrlTool(self,TheNameSpace,CtrlType):
        KeyADD=mc.checkBox("KeyADD",q=1,v=1)
        CtrlADD=mc.checkBox("CtrlADD",q=1,v=1)
        if  CtrlADD==0:
            mc.select(cl=1)
        setName = TheNameSpace + CtrlType
        selectCtrls = mc.ls(sl=1)
        setsCtrls = mc.sets( setName, q=True )
        Ctrls = selectCtrls + setsCtrls
        #Ctrls = mc.sets( setName, q=True )
        mc.select(Ctrls)
        if  KeyADD==1:
            mc.setKeyframe(Ctrls,breakdown=0 ,hierarchy= 'none', controlPoints=0 ,shape= 0)
            print ((u'====\'%s\'角色\'%s\'部位【成功】--【K帧】====')%(TheNameSpace,CtrlType))
            #mc.warning((u'====\'%s\'角色\'%s\'部位【成功】--【K帧】====')%(TheNameSpace,CtrlType))

    def CJW_initialPose(self,TheNameSpace,CtrlType):
        KeyADD=mc.checkBox("KeyADD",q=1,v=1)
        AllCtrlsAttrs = ['translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ',
'swivelToe','raiseBall','raiseToeTip','side','swivel','roll','raiseToe','Stretch']
        setName = TheNameSpace + CtrlType
        Ctrls = mc.sets( setName, q=True )
        mc.select(Ctrls)
        AllSelectCtrls = mc.ls(sl=1)
        for AC in AllSelectCtrls:
            if AC == (TheNameSpace + 'Master'):
                pass
            else:
                for ACA in AllCtrlsAttrs:
                    CtrlAttr = AC+'.'+ACA
                    if mc.objExists(CtrlAttr):
                        if '.scale' in CtrlAttr:
                            try:
                                mc.setAttr(CtrlAttr,1)
                            except:
                                pass
                        else:
                            if 'c_Rt_up_eyelids_Ctrl.rotateX' in CtrlAttr or 'c_Lf_up_eyelids_Ctrl.rotateX' in CtrlAttr:
                                mc.setAttr(CtrlAttr,-45)
                            elif 'c_Rt_dn_eyelids_Ctrl.rotateX' in CtrlAttr or 'c_Lf_dn_eyelids_Ctrl.rotateX' in CtrlAttr:
                                mc.setAttr(CtrlAttr,30)
                            else:
                                try:
                                    mc.setAttr(CtrlAttr,0)
                                except:
                                    pass
        if  KeyADD==1:
            mc.setKeyframe(Ctrls,breakdown=0 ,hierarchy= 'none', controlPoints=0 ,shape= 0)

    def CJW_CheckLocalInfoPath(self):
        localInfoPath = ('D:/Info_Temp/JustinCHan_temp/')
        mc.sysFile(localInfoPath, makeDir=True)
        TXTName = 'CJW_H_v1'
        TXTpath = 'D:/Info_Temp/JustinCHan_temp/%s.txt' % (TXTName)
        txt = open(TXTpath, 'w')
        try:
            txt.writelines('')
        finally:
            txt.close()

    def CJW_CheckLocalInfoWirte(self,path,info,addtion=0):
        if addtion ==1 and os.path.exists(path):
            info = self.CJW_CheckLocalInfoRead(path)+info
        txt = open(path, 'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
        finally:
            txt.close()

    def CJW_CheckLocalInfoRead(self,path):
        if not os.path.exists(path):
            print u'Error:    临时文件不存在'
            mc.error(u'Error:    临时文件不存在')
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result

    #设置收集材质连接列表自动生成
    def CJW_characterTextureWire(self):
        fileName = (mc.file(query=1, exn=1)).split('/')[-1]
        characterNumber = fileName[0:10]
        projectServerPath = '//file-cluster/GDC/Resource/Support/Maya/GDC/2013/RIG/Projects/MiniTiger/%s.txt' % (characterNumber)
        ConnectionNodes = []
        FMMs = mc.listRelatives('FM_Caml_gui_guides_grp',allDescendents=1,type='mesh')
        for mesh in FMMs:
            if mesh.split('_')[-1] == 'guideShape':
                PreConnections = mc.listConnections(mesh,s=0,d=1,connections=1)
                ConnectionNodes.append(PreConnections)
        self.CJW_CheckLocalInfoWirte(projectServerPath,ConnectionNodes,1)
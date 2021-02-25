#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_Template as WDTemplate
import RIG.WDface.WD_Main as WDMain
import RIG.WDface.WD_MainClass as WDBase
import RIG.WDface.WD_MainToHead as MTH
import re
import RIG.WDface.WD_SeparateTemplate as ST
import RIG.tools.importExputCurveShape as InportExport
import RIG.WDface.WD_BackupData as BD
import RIG.WDface.WD_ControlInitPose as CIP


class WD_SelectUI(object):
    def __init__(self):
        WD_WDFaceUI('Woodlies')
#        self.displayUI()
        
    def displayUI(self):
        self.IDMTRigGUI='WDselectFaceUI'
        if rig.window(self.IDMTRigGUI,exists=True):
            rig.deleteUI(self.IDMTRigGUI)
        self.CurveSign = 'OFF'
        self.mainUI = rig.window(self.IDMTRigGUI,title= u'请选择项目',menuBar=True,minimizeButton=True,maximizeButton=True)
        self.mainFLY = rig.formLayout()
        self.mainSRL = rig.scrollLayout(cr = True)
        self.mainCLM = rig.columnLayout(adj = True)
       
        self.mainBT = rig.button(l = u'初始版本',c = lambda x:self.Base())
        
        rig.separator(st = 'out')
        self.mainBT = rig.button(l = u'Woodlies',c = lambda x:self.Woodlies())
        
        rig.separator(st = 'out')
        self.mainBT = rig.button(l = u'WinxTV',c = lambda x:self.WinxTV())
        
        rig.setParent(self.mainFLY)
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'top', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'left', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'bottom', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'right', 2))
        
        rig.showWindow(self.IDMTRigGUI)#显示界面  
        rig.window(self.mainUI,e=True,wh=(300,300))
        
    def Base(self):
        WD_WDFaceUI('Base')
        if rig.window(self.IDMTRigGUI,exists=True):
            rig.deleteUI(self.IDMTRigGUI)        

    def Woodlies(self):
        WD_WDFaceUI('Woodlies')
        if rig.window(self.IDMTRigGUI,exists=True):
            rig.deleteUI(self.IDMTRigGUI)  
            
    def WinxTV(self):
        WD_WDFaceUI('WinxTV')
        if rig.window(self.IDMTRigGUI,exists=True):
            rig.deleteUI(self.IDMTRigGUI)  


class WD_WDFaceUI(object):
    def __init__(self,project):
        self.project = project
        self.displayUI()
        
    def displayUI(self):
        IDMTRigGUI='WDFaceUI'
        if rig.window(IDMTRigGUI,exists=True):
            rig.deleteUI(IDMTRigGUI)
        self.CurveSign = 'OFF'
        self.mainUI = rig.window(IDMTRigGUI,title= u'当前项目:'+self.project,menuBar=True,minimizeButton=True,maximizeButton=True)
        self.mainFLY = rig.formLayout()
        self.mainSRL = rig.scrollLayout(cr = True)
        self.mainCLM = rig.columnLayout(adj = True)

        #------------------------------------------------------------------ 部件选择
        rig.rowColumnLayout(nc = 6,columnWidth = [(1,60),(2,60),(3,60),(4,60),(5,60),(6,60)])
        self.mainCB = rig.checkBox(l = u'主体',v = True,changeCommand = lambda i:self.changeOptionVars())
        self.eyeCB = rig.checkBox(l = u'眼睛',v = True,changeCommand = lambda i:self.changeOptionVars())
        self.tongueCB = rig.checkBox(l = u'舌头',v = True,changeCommand = lambda i:self.changeOptionVars())
        self.earCB = rig.checkBox(l = u'耳朵',v = True,changeCommand = lambda i:self.changeOptionVars())
        self.eyebrowCB = rig.checkBox(l = u'眉毛',v = True,changeCommand = lambda i:self.changeOptionVars())
        self.toothCB = rig.checkBox(l = u'牙床',v = True,changeCommand = lambda i:self.changeOptionVars())
        self.jointCB = rig.checkBox(l = u'骨骼',v = True,changeCommand = lambda i:self.changeOptionVars())
#        self.eyeCB = rig.checkBox(l = u'眼睛',v = True,changeCommand = lambda i:self.changeOptionVars())
#        self.tongueCB = rig.checkBox(l = u'舌头',v = True,changeCommand = lambda i:self.changeOptionVars())
#        self.earCB = rig.checkBox(l = u'耳朵',v = True,changeCommand = lambda i:self.changeOptionVars())
#        self.eyebrowCB = rig.checkBox(l = u'眉毛',v = True,changeCommand = lambda i:self.changeOptionVars())
#        self.toothCB = rig.checkBox(l = u'牙床',v = True,changeCommand = lambda i:self.changeOptionVars())
        self.allCB = ['mainCB','eyeCB','tongueCB','earCB','eyebrowCB','toothCB','jointCB']
        self.allBt = ['SkinBT','BlendShapeBT','LfEyeBT','RtEyeBT','LfToothBT','RtToothBT','LfEyebrowBT','RtEyebrowBT','TongueBT']
        self.dictData = {'mainCB':['SkinBT','BlendShapeBT'],'eyeCB':['LfEyeBT','RtEyeBT'],'tongueCB':['TongueBT'],'earCB':[],'eyebrowCB':['LfEyebrowBT','RtEyebrowBT'],'toothCB':['LfToothBT','RtToothBT'],'jointCB':[]}
        rig.setParent(self.mainCLM)
        
        #------------------------------------------------------------------ 参数设置
        self.eyebrowISG = rig.intSliderGrp(field=True, label=u'眉弓控制器个数:',minValue=3, maxValue=20, fieldMinValue=3, fieldMaxValue=10000, value=17,columnAttach=[(1,'left',5),(2,'left',0),(3,'both',0)],columnWidth3 = (100,30,150))
        self.mouthISG = rig.intSliderGrp(field=True, label=u'嘴巴控制器个数:',minValue=3, maxValue=20, fieldMinValue=3, fieldMaxValue=10000, value=7,columnAttach=[(1,'left',5),(2,'left',0),(3,'both',0)],columnWidth3 = (100,30,150))
        self.cheefISG = rig.intSliderGrp(field=True, label=u'鼻唇沟控制器个数:',minValue=3, maxValue=20, fieldMinValue=3, fieldMaxValue=10000, value=6,columnAttach=[(1,'left',5),(2,'left',0),(3,'both',0)],columnWidth3 = (100,30,150))
        
        rig.button(l = u'生成定位控制器',c = lambda x:self.buildPosController())#生成控制器
        rig.button(l = u'刷新模版',c = lambda x:self.refreshTemplate())#刷新模版
        self.sizeFSG = rig.floatSliderGrp(field=True, label=u'调整控制器大小:',minValue=0.0001, maxValue=2, fieldMinValue=0.0001, fieldMaxValue=10000, value=1,columnAttach=[(1,'left',5),(2,'left',0),(3,'both',0)],columnWidth3 = (100,30,150),cc  = lambda x:self.changeConSize())#调整控制器大小
        rig.separator(st = 'out')        

        #------------------------------------------------------------------ 载入模型
        rig.text(u'头部模型:') 
        rig.rowColumnLayout(nc = 2, cal = [(1, 'left'),(2, 'right')])
        self.SkinBT = rig.button(l = u'载入头部模型',c = lambda x:self.loadObj('SkinBT'))
        self.BlendShapeBT = rig.button(l = u'载入蒙皮头部模型',c = lambda x:self.loadObj('BlendShapeBT'))
        rig.setParent(self.mainCLM)
        rig.rowColumnLayout(nc = 2)
        self.SkinTF = rig.textField(enable = False)
        self.BlendShapeTF = rig.textField(enable = False)
        rig.setParent(self.mainCLM)
        
        rig.text(u'眼睛模型:') 
        rig.rowColumnLayout(nc = 2)
        self.LfEyeBT = rig.button(l = u'载入左眼',c = lambda x:self.loadObj('LfEyeBT'))
        self.RtEyeBT = rig.button(l = u'载入右眼',c = lambda x:self.loadObj('RtEyeBT'))
        rig.setParent(self.mainCLM)
        rig.rowColumnLayout(nc = 2)
        self.LfEyeTF = rig.textField(enable = False)
        self.RtEyeTF = rig.textField(enable = False)
        rig.setParent(self.mainCLM)
        
        rig.text(u'牙床模型:') 
        rig.rowColumnLayout(nc = 2)
        self.LfToothBT = rig.button(l = u'载入上牙床',c = lambda x:self.loadObj('LfToothBT'))
        self.RtToothBT = rig.button(l = u'载入下牙床',c = lambda x:self.loadObj('RtToothBT'))
        rig.setParent('..')
        rig.rowColumnLayout(nc = 2)
        self.LfToothTF = rig.textField(enable = False)
        self.RtToothTF = rig.textField(enable = False)
        rig.setParent(self.mainCLM)

        rig.text(u'眉毛模型:') 
        rig.rowColumnLayout(nc = 2)
        self.LfEyebrowBT = rig.button(l = u'载入左边眉毛',c = lambda x:self.loadObj('LfEyebrowBT'))
        self.RtEyebrowBT = rig.button(l = u'载入右边眉毛',c = lambda x:self.loadObj('RtEyebrowBT'))
        rig.setParent('..')
        rig.rowColumnLayout(nc = 2)
        self.LfEyebrowTF = rig.textField(enable = False)
        self.RtEyebrowTF = rig.textField(enable = False)
        rig.setParent(self.mainCLM)
                
        rig.text(u'舌头模型:') 
        self.TongueBT = rig.button(l = u'载入舌头',w = 300,c = lambda x:self.loadObj('TongueBT'))
        self.TongueTF = rig.textField(w = 300,enable = False)  
        rig.setParent(self.mainCLM)
        
        rig.separator(st = 'out')        
        #----------------------------------------------------------------- 镜像控制器
        rig.rowColumnLayout(nc = 3,cw = (1,100))
        rig.text(l = u'镜像控制器：')
        rig.button(l = u'左 ——>右',c = lambda x:self.mirrorCon('X', True))
        rig.button(l = u'右——>左 ',c = lambda x:self.mirrorCon('X', False))
        rig.setParent(self.mainCLM)
        
        rig.button(l = u'生成设置',c = lambda x:self.startSetup())#生成控制器
        rig.separator(st = 'out') 
        

              
        #----------------------------------------------------------------- 镜像blendShape曲线
        rig.rowColumnLayout(nc = 3)
        rig.button(l = u'修改blendShape',c = lambda x:self.mirrorBlendShape('X', True, False))
        rig.button(l = u'镜像到右',c = lambda x:self.mirrorBlendShape('X', True, True))
        rig.button(l = u'镜像到左',c = lambda x:self.mirrorBlendShape('X', False, True))
        rig.setParent(self.mainCLM)  
        
        
#        #----------------------------------------------------------------- 调整范围
#        rig.rowColumnLayout(nc = 3,cw = (1,100))
#        rig.text(l = u'调整范围：')
#        rig.button(l = u'限定位移范围', c = lambda x:rig.setToolTo(self.limitTransformMP))
#        rig.button(l = u'限定旋转范围', c = lambda x:rig.setToolTo(self.move))
#        rig.setParent(self.mainCLM)  
#       
#        #----------------------------------------------------------------- 恢复blendShape曲线
#        rig.rowColumnLayout(nc = 3,cw = (1,100))
#        rig.text(l = u'恢复BS曲线：')
#        rig.button(l = u'恢复Belndshape曲线')
#        rig.button(l = u'恢复所有Belndshape曲线')
#        rig.setParent(self.mainCLM)  
        
        #----------------------------------------------------------------- 隐藏控制器
        rig.rowColumnLayout(nc = 4)
        rig.button(l = u'隐藏small控制器',c = lambda x:self.displayConntroller('small','hide'))
        rig.button(l = u'隐藏macro控制器',c = lambda x:self.displayConntroller('macro','hide'))
        rig.button(l = u'隐藏main控制器',c = lambda x:self.displayConntroller('main','hide'))
        rig.button(l = u'隐藏十字控制器',c = lambda x:self.displayConntroller('cross','hide'))
        rig.setParent(self.mainCLM) 
        
        #----------------------------------------------------------------- 显示控制器
        rig.rowColumnLayout(nc = 4)
        rig.button(l = u'显示small控制器',c = lambda x:self.displayConntroller('small','show'))
        rig.button(l = u'显示macro控制器',c = lambda x:self.displayConntroller('macro','show'))
        rig.button(l = u'显示main控制器',c = lambda x:self.displayConntroller('main','show'))
        rig.button(l = u'显示十字控制器',c = lambda x:self.displayConntroller('cross','show'))
        rig.setParent(self.mainCLM) 

        #----------------------------------------------------------------- 导入导出曲线
        rig.separator(st = 'out')
        rig.separator(st = 'out')
        rig.rowColumnLayout(nc = 3)
        rig.button(l = u'导入导出blendShape曲线',c = lambda x:self.importExportBlendShapeCurve())
        rig.button(l = u'导入导出控制器形状',c = lambda x:self.importExportControlCurve())
        rig.button(l = u'导入导出模版信息',c = lambda x:self.importExportTemplateInfo())
        rig.setParent(self.mainCLM) 

        rig.button(l = u'恢复选择的控制器到初始POSE',c = lambda x:self.restorySelectCon())
        rig.button(l = u'恢复模版',c = lambda x:self.restoryTemplate())
        rig.button(l = u'对blendShape节点进行标识',c = lambda x:self.AddMarker())
        
        rig.setParent(self.mainFLY)
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'top', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'left', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'bottom', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'right', 2))
        
        #设置OptionVars
        self.getOptionVars()
        self.setOptionVars()
        self.getSkinObj()#得到蒙皮物体
        rig.showWindow(IDMTRigGUI)#显示界面  
        rig.window(self.mainUI,e=True,wh=(400,800))
    
    #-------------------------------------------------------- 将窗口信息写入parameter属性
    def getWindowInfo(self):
        main = rig.checkBox(self.mainCB,q = True,v = True)
        ear = rig.checkBox(self.earCB,q = True,v = True)
        eye = rig.checkBox(self.eyeCB,q = True,v = True)
        eyebrow = rig.checkBox(self.eyebrowCB,q = True,v = True)
        tongue = rig.checkBox(self.tongueCB,q = True,v = True)
        tooth = rig.checkBox(self.toothCB,q = True,v = True)
        joints = rig.checkBox(self.jointCB,q = True,v = True)


        eyebrowNum = rig.intSliderGrp(self.eyebrowISG,q = True,v = True)
        mouthNum = rig.intSliderGrp(self.mouthISG,q = True,v = True)
        nasolabialGrooveNum = rig.intSliderGrp(self.cheefISG,q = True,v = True)
        
        WD_buildPostionData = [main,ear,eye,eyebrow,tongue,tooth,joints,eyebrowNum,mouthNum,nasolabialGrooveNum]
        BD.backupData([],[],[], WD_buildPostionData).done()#备份数据        
        
    #-------------------------------------------------------- 将窗口信息写入parameter属性
    def setWindowInfo(self):
        parameter = WDBase.convertData().getAttrData('Head_FaceRig_Control_GRP.parameter')
        main = rig.checkBox(self.mainCB,e = True,v = parameter[0])
        ear = rig.checkBox(self.earCB,e = True,v = parameter[1])
        eye = rig.checkBox(self.eyeCB,e = True,v = parameter[2])
        eyebrow = rig.checkBox(self.eyebrowCB,e = True,v = parameter[3])
        tongue = rig.checkBox(self.tongueCB,e = True,v = parameter[4])
        tooth = rig.checkBox(self.toothCB,e = True,v = parameter[5])
        joints = rig.checkBox(self.jointCB,e = True,v = parameter[6])


        eyebrowNum = rig.intSliderGrp(self.eyebrowISG,e = True,v = parameter[7])
        mouthNum = rig.intSliderGrp(self.mouthISG,e = True,v = parameter[8])
        nasolabialGrooveNum = rig.intSliderGrp(self.cheefISG,e = True,v = parameter[9])
          
        
    #---------------------------------------------------------------------- 生成模版
    def buildPosController(self):
        self.getWindowInfo()
        parameter = WDBase.convertData().getAttrData('Head_FaceRig_Control_GRP.parameter')
        WDTemplate.WD_buildPostion(parameter[0], parameter[1], parameter[2], parameter[3], parameter[4], parameter[5], parameter[6], parameter[7], parameter[8], parameter[9])

     
    #-------------------------------------------------------------------- 开始生成设置
    def startSetup(self):
        checkBoxData = dict([(CB,rig.checkBox(self.__dict__[CB],q = True,v = True)) for CB in self.allCB])
        textFieldData = dict([(TF,rig.textField(self.__dict__[TF.replace('BT','TF')],q = True,tx = True)) for TF in self.allBt])
        StartSetup = WDMain.combineComponent(checkBoxData,textFieldData,self.dictData)
        
        self.getWindowInfo()
        parameter = WDBase.convertData().getAttrData('Head_FaceRig_Control_GRP.parameter')
        print parameter
        BD.backupData(checkBoxData,textFieldData,self.dictData, parameter).done()#备份数据
        StartSetup.done()
        
    #-------------------------------------------------------------------- 对blendShape增加标识
    def AddMarker(self):
        slobjs = rig.ls(sl = True, type = 'blendShape')  
        if slobjs:
            rig.addAttr(slobjs, at = 'long', ln = 'BS_WD_A')
    
    
    #---------------------------------------------------------------------- 载入模型
    def loadObj(self,clickBT):
        slObjs = rig.ls(sl = True)
        if slObjs:
            TX = str(slObjs).replace('[','').replace(']','')
            rig.textField(self.__dict__[clickBT.replace('BT','TF')],e = True,text = TX)
            self.setSkinObj()
                
        else:
            rig.textField(self.__dict__[clickBT.replace('BT','TF')],e = True,text = '')
            self.setSkinObj()

    
    def changeOptionVars(self):#改变OptionVars
        self.OptionVarsData = []
        for CB in self.allCB:
            self.OptionVarsData.append(int(rig.checkBox(self.__dict__[CB],q = True,v = True)))
        self.setOptionVars()
        
    def getOptionVars(self):#获得OptionVars
        self.OptionVarsData = []
        for i,CB in  enumerate(self.allCB):
            if rig.optionVar( exists = 'RIG_WDFace_'+CB):#如果OptionVars已经存在
                getID = rig.optionVar(q = 'RIG_WDFace_'+CB)
                self.OptionVarsData.append(getID)
                rig.checkBox(self.__dict__[CB],e = True,v = getID)
            else:#增加OptionVars默认值设为1
                rig.optionVar(iv = ('RIG_WDFace_'+CB,1))
                self.OptionVarsData.append(1)
                
    
    def setOptionVars(self):#设置OptionVars
        for i,CB in enumerate(self.allCB):
            rig.optionVar(iv = ('RIG_WDFace_'+CB,self.OptionVarsData[i]))
            
            #设置按钮是否激活
            TFs = self.dictData[CB]
            if TFs:
                for TF in TFs:
                    rig.button(self.__dict__[TF],e = True, en = self.OptionVarsData[i])
            else:
                pass
            
    #镜像控制器        
    def mirrorCon(self,axis,direction):
        MirrorCon  = WDBase.BlendShapeController()
        
        if rig.objExists('Main_Control_GRP'):
            rigging = rig.attributeQuery('rigging', node = 'Main_Control_GRP', ex = True) 
            MirrorCon.grp = 'Main_Control_GRP'
            MirrorCon.axis = axis
            MirrorCon.direction = direction
            MirrorCon.conType = 'small'
            MirrorCon.select = False
            MirrorCon.rigging = rigging
            MirrorCon.Mirror()
            
        if rig.objExists('Head_Control_GRP'):  
            rigging = rig.attributeQuery('rigging', node = 'Head_Control_GRP', ex = True)      
            MirrorCon.grp = 'Head_Control_GRP'
            MirrorCon.axis = axis
            MirrorCon.direction = direction
            MirrorCon.conType = 'macro'
            MirrorCon.select = False
            MirrorCon.rigging = rigging
            MirrorCon.Mirror()
            
        if rig.objExists('Eye_Control_GRP'):  
            rigging = rig.attributeQuery('rigging', node = 'Eye_Control_GRP', ex = True)       
            MirrorCon.grp = 'Eye_Control_GRP'
            MirrorCon.axis = axis
            MirrorCon.direction = direction
            MirrorCon.conType = 'eye'
            MirrorCon.select = False
            MirrorCon.rigging = rigging
            MirrorCon.Mirror()
            
        if rig.objExists('Ear_Control_GRP'):  
            rigging = rig.attributeQuery('rigging', node = 'Ear_Control_GRP', ex = True)       
            MirrorCon.grp = 'Ear_Control_GRP'
            MirrorCon.axis = axis
            MirrorCon.direction = direction
            MirrorCon.conType = 'ear'
            MirrorCon.select = False
            MirrorCon.rigging = rigging
            MirrorCon.Mirror()
            
    #镜像blendShape曲线    
    def mirrorBlendShape(self,axis,direction, Msign):
        if Msign:
            MirrorCon  = WDBase.BlendShapeController()
            if rig.objExists('Main_Control_GRP'):
                MirrorCon.grp = 'Main_Control_GRP'
                MirrorCon.axis = axis
                MirrorCon.direction = direction
                MirrorCon.conType = 'blendShape'
                MirrorCon.select = False
                MirrorCon.Mirror()
        else:
            Mth = MTH.createBlendShape()
            Mth.auto = False
            Mth.addBlendShapeControl()
        
        
    def displayConntroller(self,conType,hd):
        Con = WDBase.changeController()
        hideSign = Con.operate
        Con.operate = hd
        Con.selectTypes(conType)
        
    #改变控制器大小   
    def changeConSize(self):
        size = rig.floatSliderGrp(self.sizeFSG,q = True, v = True)
        rig.floatSliderGrp(self.sizeFSG,e = True, v = 1)
        Con = WDBase.changeController()
        objs = rig.ls(sl = True)
        if objs:
            obj = objs[0]
            if re.match('\ALf[A-Z]+|\ARt[A-Z]+', obj):
                Con.size = size
                Con.operate = 'changeSize'
                Con.selectTypes('small')
            elif re.match('\ALf_.+Macro_M\Z|\ARt_.+Macro_M\Z', obj):
                Con.size = size
                Con.operate = 'changeSize'
                Con.selectTypes('macro')        
            elif re.match('\ALf_.+_M\Z|\ARt_.+_M\Z', obj):
                Con.size = size
                Con.operate = 'changeSize'
                Con.selectTypes('main')
       
        
    #得到蒙皮物体
    def getSkinObj(self):
        if rig.objExists('Head_FaceRig_Control_GRP'):
            nodeInfo = 'Head_FaceRig_Control_GRP'
        
            for bt in self.allBt:
                btName = bt.replace('BT','TF')
                if not rig.attributeQuery( btName, node = nodeInfo,ex = True):#如果属性不存在
                    rig.addAttr(nodeInfo,dt = 'string',ln = btName)
                else:
                    attrInfo = rig.getAttr(nodeInfo+'.'+btName)
                    rig.textField(self.__dict__[btName], e = True, tx = attrInfo)
    
    #设置蒙皮物体
    def setSkinObj(self):
        if rig.objExists('Head_FaceRig_Control_GRP'):
            nodeInfo = 'Head_FaceRig_Control_GRP'
            
            for bt in self.allBt:
                btName = bt.replace('BT','TF')
                tx = rig.textField(self.__dict__[btName], q = True, tx = True)
                
                if not rig.attributeQuery( btName, node = nodeInfo,ex = True):#如果属性不存在
                    rig.addAttr(nodeInfo,dt = 'string',ln = btName)
                
                rig.setAttr(nodeInfo+'.'+btName, tx, type = "string")
        
        
    #刷新模版
    def refreshTemplate(self):
        ST.separateTemplate().done()
        
        
        
    #恢复blendShape曲线
    def restorBlendShapeCurve(self):
        Mth = MTH.createBlendShape()
        Mth.auto = False
        Mth.addBlendShapeControl()
        
    #导入导出控制器形状    
    def importExportControlCurve(self):
        cons = []
        if rig.objExists('face_controls_Sets'):
            cons = WDBase.getSetElements().getEle()
            
        TempIE = InportExport.SK_ImportExportUI()
        TempIE.guiName = 'IEControl_UI'
        TempIE.guiTitle = u'导入导出控制器'
        TempIE.guiImport = u'导入控制器'
        TempIE.guiExport = u'导出控制器'
        TempIE.allCons = cons
        TempIE.relativesSet = False
        TempIE.displayUI()
        
    #导入导出blendShape    
    def importExportBlendShapeCurve(self):
        bs = []
        if rig.objExists('Main_Control_GRP_BSCurve'):
            AllBlendShape = rig.listRelatives('Main_Control_GRP_BSCurve', c = True, ad = True)
            bs = rig.ls(AllBlendShape, type = 'transform')
        
        TempIE = InportExport.SK_ImportExportUI()
        TempIE.guiName = 'IEBlendShape_UI'
        TempIE.guiTitle = u'导入导出blendShape曲线'
        TempIE.guiImport = u'导入曲线'
        TempIE.guiExport = u'导出曲线'
        TempIE.allCons = bs
        TempIE.relativesSet = False
        TempIE.displayUI()    
 
    #导入导出模版信息      
    def importExportTemplateInfo(self):
        AllTrans = []
        if rig.objExists('Head_FaceRig_Control_GRP'):
            AllTransforms = rig.listRelatives('Head_FaceRig_Control_GRP', c = True, ad = True)
            AllTrans = rig.ls(AllTransforms, type = 'transform')
            AllTrans.extend(AllTrans)
                
                
        if rig.objExists('Head_FaceDeformers_GRP'):
            Head_FaceDeformers_GRPs = rig.listRelatives('Head_FaceDeformers_GRP', c = True, ad = True)
            FaceDeformers_GRP = rig.ls(Head_FaceDeformers_GRPs, type = 'transform')
            AllTrans.extend(FaceDeformers_GRP)
                
        TempIE = InportExport.SK_ImportExportUI()
        TempIE.guiName = 'IETemplateInfo_UI'
        TempIE.guiTitle = u'导入导出模版信息'
        TempIE.guiImport = u'导入信息'
        TempIE.guiExport = u'导出信息'
        TempIE.allCons = AllTrans
        TempIE.relativesSet = False
        TempIE.shapeSign = False
        TempIE.conSpace = False
        TempIE.displayUI()         

#===============================================================================
# 恢复模版文件        
#===============================================================================
    def restoryTemplate(self):
        #获得控制器形状
        ShpaeIE = InportExport.SK_ImportExportUI()
        cons = []
        if rig.objExists('face_controls_Sets'):
            cons = WDBase.getSetElements().getEle()
        ShpaeIE.allCons = cons
        ShpaeIE.relativesSet = False
#        ShpaeIE.conSpace = True
        ShapeInfo = ShpaeIE.SK_getCurveShape()
        
        parameter = WDBase.convertData().getAttrData('Head_FaceRig_Control_GRP.parameter')
        templateInfo = WDBase.convertData().getAttrData('Head_FaceRig_Control_GRP.templateInfo')
        
        rig.file(f = True, new = True)
        WDTemplate.WD_buildPostion(parameter[0], parameter[1], parameter[2], parameter[3], parameter[4], parameter[5], parameter[6], parameter[7], parameter[8], parameter[9])
        
        BD.backupData([],[],[], parameter).done()#备份数据     
        self.setWindowInfo()
        
        positinIE = InportExport.SK_ImportExportUI()
        positinIE.relativesSet = False
        positinIE.shapeSign = False
        positinIE.conSpace = False
        positinIE.SK_setCurveShape(templateInfo) 
        ShpaeIE.SK_setCurveShape(ShapeInfo)
        
#===============================================================================
# 恢复选择的控制器        
#===============================================================================
    def restorySelectCon(self):
        CIP.restoryControlInit().done()
        
        
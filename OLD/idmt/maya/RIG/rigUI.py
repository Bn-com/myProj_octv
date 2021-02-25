#-*- coding: utf-8 -*-
import maya.cmds as rig
import maya.mel as MEL
from RIG.selectJoint import SK_selectSkinJnt
from RIG.commonly.bodyTemplate import SK_BodyJointPosition
from RIG.commonly.restoreJoint import *
from RIG.fingerPose import *
from RIG.commonly.base import *
from RIG.combine import SK_combinationFinal
from RIG.commonly.mirrorCurve import SK_MirrorCurveControlCmd
from RIG.commonly.resetControllerDefaultPose import SK_creatConDefaultPos
from RIG.commonly.addFingerJoint import SK_createFingers 
from RIG.IKFK import SK_IKFKSwitchCommand
from RIG.tools.skeletoneToController import buildSKTOCON
from RIG.tools.deformerConvert import softModToCluster
from RIG.tools.base import *
from RIG.selectProject import SK_SelectProject

class SK_IDMTRigUI(object):
    def __init__(self):
        self.displayUI()
        
    def displayUI(self):
        IDMTRigGUI='autoRigging'
        if rig.window(IDMTRigGUI,exists=True):
            rig.deleteUI(IDMTRigGUI)
        rig.window(IDMTRigGUI,title='IDMT 2009 AutoRig',menuBar=True,wh=  (400,500),minimizeButton=True,maximizeButton=True)
        
        #===============================================================================
        # 开始菜单
        #===============================================================================
        rig.menu( label='File',tearOff=True )
        rig.menuItem( label='New')
        rig.menuItem( label='Open')
        rig.menuItem( label='Save')
        rig.menuItem( divider=True)
        rig.menuItem( label='Quit')
        rig.menu(label='Help',helpMenu=True)
        rig.menuItem( 'Application..."',label= u'帮助文档',c='from RIG.Help.helpUI import *;SK_helptUI()' )
     
        self.tabs = rig.tabLayout(innerMarginWidth=5,innerMarginHeight=5)
        #===============================================================================
        # 开始"AutoRiggingLayout"     
        #===============================================================================
        self.AutoRiggingLayout = rig.columnLayout(w =100,h=600,columnAlign='center')
    
        
        rig.button(label = u'     导入模版     ',w=322 ,  c='SK_BodyJointPosition()')
        rig.separator(w = 322,h=15,style='in')
        rig.setParent(self.AutoRiggingLayout)
        
        rig.intSliderGrp('fingerNumsField',field=True, label=u'手指个数:',minValue=0, maxValue=5, fieldMinValue=0, fieldMaxValue=100, value=5,columnAttach=[(1,'left',0),(2,'left',0),(3,'both',0)],columnWidth3 = (55,50,222))
        rig.intSliderGrp('toesNumsField', field=True, label=u'脚趾个数:',minValue=0, maxValue=5, fieldMinValue=0, fieldMaxValue=100, value=5,columnAttach=[(1,'left',0),(2,'left',0),(3,'both',0)],columnWidth3 = (55,50,222))
        rig.intSliderGrp('neckSegsField', field=True, label=u'脖子段数:',minValue=2, maxValue=5, fieldMinValue=2, fieldMaxValue=100, value=2,columnAttach=[(1,'left',0),(2,'left',0),(3,'both',0)],columnWidth3 = (55,50,222))
        rig.intSliderGrp('waistSegsField', field=True, label=u'腰部段数:',minValue=3, maxValue=10, fieldMinValue=4, fieldMaxValue=100, value=0,columnAttach=[(1,'left',0),(2,'left',0),(3,'both',0)],columnWidth3 = (55,50,222))
        rig.setParent(self.AutoRiggingLayout)
        
        rig.separator(w = 322,h=15,style='in')
        
        rig.rowColumnLayout(numberOfColumns = 2,columnWidth=[(1, 161), (2,  161)],columnAttach=(2,'both',0) )
        rig.button(label=u' 刷新模版  ',w = 130,c='SK_refreshTemp()')
        rig.button(label=u' 镜像骨骼 ',w=130,c='orientAndMirrorJoint ()')
        rig.setParent(self.AutoRiggingLayout)
    
        rig.separator(w = 322,h=15,style='in')
        
        rig.text(l = u'选择项目')#选择项目
        rig.radioCollection()
        rig.rowColumnLayout(nc = 4,columnWidth = [(1,85),(2,85),(3,85),(4,85)])
        self.OrigenRB = rig.radioButton( label= u'初始版本',sl = 1)
        self.WoodliesRB = rig.radioButton( label='Woodlies' )
        self.motionBuilder = rig.radioButton( label='MotionBuilder')
        self.WinxTVRB = rig.radioButton( label='WinxTV',vis = False)
        rig.setParent(self.AutoRiggingLayout)
    
        rig.button(label=u' 生成身体设置  ',w = 322,h = 40, c = lambda x:self.buildSetup())
        
        rig.separator(w = 322,h=15,style='in')
        
        rig.columnLayout('MeshListLayout')
        rig.textScrollList('meshList',w=322,h=100,allowMultiSelection=True,deleteKeyCommand='SK_delMeshList() ')
        rig.setParent(self.AutoRiggingLayout)
        
        rig.separator(w = 322,h=15,style='in')
        
        rig.rowColumnLayout(numberOfColumns = 2,columnWidth=[(1, 161), (2,  161)],columnAttach=(2,'both',0) )
        rig.button(label= u' 添加绑定模型 ',w = 130,c='SK_addMeshList()')
        rig.button(label= u' 对绑定模型蒙皮 ',w=130,c='SK_rigSkin()')
        rig.setParent(self.AutoRiggingLayout)
        
        rig.separator(w = 322,h=15,style='in')
        rig.button(l= u'IK<-->FK',w=322,h=40,c = 'SK_IKFKSwitchCommand()')
        
        rig.separator(w = 322,h=15,style='in')
        rig.button(l= u'恢复初始POSE',w=322,h=40,c = 'SK_creatConDefaultPos(0)')
        
        rig.setParent( self.tabs )
        #===============================================================================
        # 开始"assemblageLayout"    
        #===============================================================================
        self.assemblageLayout = rig.columnLayout(w =300,h=355)
         
        rig.text(u'1:->选择你要复制的部件2:->在下面的输入复制的数量\n3:->完成复制4:->完成镜像')
        rig.rowColumnLayout('skinningLayout',numberOfColumns = 3,columnWidth=[(1, 109), (2,  109),(3,109)],columnAttach=(2,'both',0) )
        rig.intField('numOfduplicate' , min = 1 , max = 100 , value=1 ,step=1 )
        rig.button(label= u' 完成复制 ', c = 'SK_duplicateJnt()')
        rig.button(label= u' 完成镜像 ',c='SK_mirrorDupJoint ()')
        rig.setParent('..')
        rig.separator(w = 332,h=15,style='in')
    
        rig.setParent(self.tabs)
        #===============================================================================
        # 开始"RiggingToolsLayout"    
        #===============================================================================
        self.RiggingToolsLayout = rig.columnLayout(w =300,h=355)
        
        #------------------------------------------------------------------------------ 
        modelFL = rig.frameLayout(w=327,label= u"模型工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(modelFL,edit=True,expandCommand="rig.frameLayout(\""+modelFL+"\" ,edit=True,h=200)")
        rig.frameLayout(modelFL,edit=True,collapseCommand="rig.frameLayout(\""+modelFL+"\" ,edit=True,h=20)")
        rig.columnLayout()
    
        rig.separator(w = 312,h=5,style='in')
        rig.button(label = u' 打开模型工具窗口 ' ,w=312 ,c = 'from RIG.tools.modelTools.modelUI import *; SK_modelUI()')
        
        rig.setParent(self.RiggingToolsLayout)    
        #------------------------------------------------------------------------------ 
        simulationFL = rig.frameLayout(w=327,label= u"解算设置工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(simulationFL,edit=True,expandCommand="rig.frameLayout(\""+simulationFL+"\" ,edit=True,h=200)")
        rig.frameLayout(simulationFL,edit=True,collapseCommand="rig.frameLayout(\""+simulationFL+"\" ,edit=True,h=20)")
        rig.columnLayout()
    
        rig.separator(w = 312,h=5,style='in')
        rig.text(u'增加布料设置')
        rig.button(label = u' 打开布料设置窗口 ' ,w=312 ,c = 'from RIG.simulation.simulationUI import *; SK_simulationUI()')
        
        rig.separator(w = 312,h=5,style='in')
        rig.text(u'增加动力学IK设置')
        rig.button(label = u' 打开动力学IK设置设置窗口 ' ,w=312 ,c = 'from RIG.tools.dynamicCurve.DC_dynamicCurveUI import *; SK_dynamicIKUI()')
           
        rig.setParent(self.RiggingToolsLayout)
        #------------------------------------------------------------------------------ 
        fingerFL = rig.frameLayout(w=327,label= u"手指工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(fingerFL,edit=True,expandCommand="rig.frameLayout(\""+fingerFL+"\" ,edit=True,h=200)")
        rig.frameLayout(fingerFL,edit=True,collapseCommand="rig.frameLayout(\""+fingerFL+"\" ,edit=True,h=20)")
        rig.scrollLayout()
        fingerMoLayout = rig.columnLayout()
    
        rig.separator(w = 312,h=5,style='in')
        rig.text(u' 增加手指工具')
        rig.button(label = u' 打开窗口 ' ,w=312 ,c = 'SK_fingerAnimUI()')
        rig.setParent(self.RiggingToolsLayout)
        #------------------------------------------------------------------------------ 
        resetFL = rig.frameLayout(w=327,label= u"恢复工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(resetFL,edit=True,expandCommand="rig.frameLayout(\""+resetFL+"\" ,edit=True,h=200)")
        rig.frameLayout(resetFL,edit=True,collapseCommand="rig.frameLayout(\""+resetFL+"\" ,edit=True,h=20)")
        rig.scrollLayout()
        resetMoLayout = rig.columnLayout()
        
        rig.text(u"重新恢复到模版文件")
        rig.button( label = u' 恢复 ' ,w=312 ,c = 'SK_restoreJoint(True)')
        rig.setParent(self.RiggingToolsLayout)
        #------------------------------------------------------------------------------ 
        curveFL = rig.frameLayout(w=327,label= u"曲线工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(curveFL,edit=True,expandCommand="rig.frameLayout(\""+curveFL+"\" ,edit=True,h=200)")
        rig.frameLayout(curveFL,edit=True,collapseCommand="rig.frameLayout(\""+curveFL+"\" ,edit=True,h=20)")
        curveMoScr = rig.scrollLayout()
        rig.columnLayout()
    
        rig.text(u" 导入-导出控制器形状 ")
        rig.button(label = u' 打开窗口' ,w=312 ,c =  'from RIG.tools.importExputCurveShape import *\nSK_ImportExportUI().displayUI()')
        rig.separator(w = 312,h=15,style='in')
        
        rig.text(u"镜像控制器形状")
        rig.rowColumnLayout('curveMirrorLayout' , numberOfColumns=2,columnWidth = [(1,156),(2,156)],columnAttach = (2,'both',0))
        rig.button(l= u'左 ——>右',c='SK_MirrorCurveControlCmd(1)')
        rig.button(l= u'右 ——>左',c='SK_MirrorCurveControlCmd(0)')
        rig.separator(w = 312,h=15,style='in')
        rig.setParent( '..' )
        
        rig.text(u" 增加控制器到bodySet ")
        rig.button(label = u' 增加' ,w=312 ,c =  'from RIG.tools.addSet import *\nSK_AddToSet("bodySet",rig.ls(sl = True),True)')
        rig.separator(w = 312,h=15,style='in')
        rig.setParent(self.RiggingToolsLayout) 
        #------------------------------------------------------------------------------ 
        extraFL = rig.frameLayout('extraFrame',w=327,label= u"附加工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(extraFL,edit=True,expandCommand="rig.frameLayout(\""+extraFL+"\" ,edit=True,h=300)")
        rig.frameLayout(extraFL,edit=True,collapseCommand="rig.frameLayout(\""+extraFL+"\" ,edit=True,h=20)")
        rig.columnLayout()
    
        #   选择骨骼增加控制器
        rig.text(u'为选择的骨骼添加控制器:')
        rig.button(label = u'确定' ,w=312 ,c =  'buildSKTOCON()')
        rig.separator(w = 312,h=15,style='in')
        
        #   将软选择变形器转为CLUSTER
        rig.text(u'将softMod转为cluster:')
        rig.button(label = u'确定' ,w=312 ,c =  'softModToCluster()')
        rig.separator(w = 312,h=15,style='in')
            
        rig.text(u'重设簇的形节点位置:')
        rig.button(label = u'确定' ,w=312 ,c =  'resetClusterPos()')
        rig.separator(w = 312,h=15,style='in')

        rig.text(u'关闭场景中局部旋转轴向显示:')
        rig.button(label = u'确定' ,w=312 ,c =  'TL_CloseDisplayLocalAxis()')
        rig.separator(w = 312,h=15,style='in')
                    
        rig.text(u'创建线性IK:')
        rig.button(label = u'打开窗口' ,w=312 ,c =  'from RIG.tools.IKsplineTool.ikSpline import * \nIKSplineUI()')
        rig.setParent(self.RiggingToolsLayout)
        #------------------------------------------------------------------------------ 
        skinFL = rig.frameLayout('skinTools',w=327,label= u"权重工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(skinFL,edit=True,expandCommand="rig.frameLayout(\""+skinFL+"\" ,edit=True,h=200)")
        rig.frameLayout(skinFL,edit=True,collapseCommand="rig.frameLayout(\""+skinFL+"\" ,edit=True,h=20)")
        rig.columnLayout()
    
        rig.separator(w = 312,h=5,style='in')
        rig.text(u' 将一个物体的权重拷给多个物体')
        rig.button(label = u' 确定 ' ,w = 312 ,c = 'from RIG.tools.copyWeigths import *\nSK_copyWeightToOtherObj()')
        
        rig.separator(w = 312,h=5,style='in')
        rig.text(u'检测是否有影响物体重叠')
        rig.button(label = u' 确定 ' ,w = 312 ,c = 'from RIG.tools.detectInfluence import *\ndetectInfluenceObj()')
        
        rig.separator(w = 312,h=5,style='in')
        rig.text(u'导入导出权重')
        rig.button(label = u' 打开工具窗口 ' ,w = 312 ,c = 'from RIG.tools.IOWeights.IOWeightsUI import *\nSK_IOWeightsUI()')
        
        rig.setParent(self.RiggingToolsLayout)
        rig.setParent(self.tabs)
        #===============================================================================
        # 开始"faceRiggingLayout"        
        #===============================================================================
        self.faceRiggingLayout = rig.columnLayout(w =300,h=355)
        
        rig.button(l= u'打开面部设置窗口',c='from RIG.face.faceUI import *\nOpenFaceUI()',w = 325)
    
        rig.separator(w = 325,h=5,style='in')
        rig.button(l= u'打开最新面部设置窗口',c='import RIG.WDface.WD_FaceUI as face;face.WD_SelectUI()',w = 325)

        rig.separator(w = 325,h=5,style='in')
        rig.text(u' 增加下颚设置')
        rig.rowColumnLayout(numberOfColumns=2,columnWidth = [(1,162),(2,162)])
        rig.button(label = u' 确定 ' ,c = 'from RIG.tools.AddJawSetup import *\nSK_AddJawSetup()')
        rig.button(l= u'移除设置',c = 'from RIG.tools.AddJawSetup import *\nSK_removeJawSetup()')
        rig.setParent('..')
            
        rig.separator(w = 325,h=5,style='in')
        rig.text(u' 增加眼睛设置')    
        rig.rowColumnLayout(numberOfColumns=3,columnWidth = [(1,108),(2,108),(3,108)],columnAttach = (3,'both',0))
        rig.button(l= u'导入控制器',c= 'from RIG.tools.AddEyeSetup import SK_AddEyeSetup\nSK_AddEyeSetup(True)')
        rig.button(l= u'完成设置',c= 'from RIG.tools.AddEyeSetup import SK_AddEyeSetup\nSK_AddEyeSetup(False)')
        rig.button(l= u'移除设置',c= 'from RIG.tools.AddEyeSetup import SK_removeEyeSetup\nSK_removeEyeSetup()')
        
        rig.setParent(self.tabs )
        rig.tabLayout( self.tabs,edit=True,tabLabel=((self.AutoRiggingLayout,'AutoRigging'), (self.assemblageLayout,'assemblage'),  (self.RiggingToolsLayout,'RiggingTools'),(self.faceRiggingLayout,'faceRigging')),\
                       selectTabIndex = self.getOptionVar(),changeCommand = lambda x = 0:self.setOptionVar())
        
        rig.showWindow(IDMTRigGUI)    
        rig.window(IDMTRigGUI,e=True,wh=(344,680))
        #-------------------------------------------------------------------------- 界面结束
    
    #===============================================================================
    # 增加OptionVar
    #===============================================================================
    def setOptionVar(self):
        RIG_Tab_Var = 'RIG_Tab_Var'
        selectID = rig.tabLayout(self.tabs,q = True,selectTabIndex = True)
        rig.optionVar(iv = (RIG_Tab_Var,selectID))
                
    def getOptionVar(self):
        RIG_Tab_Var = 'RIG_Tab_Var'
        if rig.optionVar( exists= RIG_Tab_Var):
            getID = rig.optionVar(q = RIG_Tab_Var)
        else:
            getID = 1
            
        return getID
    #------------------------------------------------------------- 结束OptionVar设置
    
    #===========================================================================
    # 生成设置
    #===========================================================================
    def buildSetup(self):
        SK_combinationFinal()
        SK_SelectProject(self.OrigenRB,self.WoodliesRB,self.WinxTVRB,self.MotionBuilder)#选择项目

def SK_fillTextField():
    name = rig.optionMenuGrp('nameListField',q=True,value=True)
    rig.textField('aTF',e= True , text =name )     


def SK_fingerAnimUI(): 

    GUI='fingerAnimUI'
    if rig.window(GUI,exists=True):
        rig.deleteUI(GUI)
    rig.window(GUI,title='FingerAnim',menuBar=True,wh=(180,150),minimizeButton=True,maximizeButton=True)
    MCL=rig.columnLayout()
    rig.text('**-- fill in the name--**')
    
    MRL=rig.rowColumnLayout(numberOfColumns = 3 , columnAttach=(1, 'left', 1),columnWidth=[(1, 70),(2, 100),(3, 120)] )
    rig.text('  FingerAnim :')
    rig.textField('aTF',text = 'curl',width=80)
    
    rig.optionMenuGrp('nameListField',label='  default:',columnWidth =[(1,55),(2,150)],changeCommand = 'SK_fillTextField()')
    rig.menuItem( label='curl' )
    rig.menuItem( label='relax' )
    rig.menuItem( label='spread' )
    rig.menuItem( label='scrunch' )
    rig.menuItem( label='cup' )
    rig.menuItem( label='twist' )
    rig.menuItem( label='lean' )

    rig.setParent( '..' )
    rig.separator(height =30,w=300)
    
    MBL=rig.rowColumnLayout(numberOfColumns = 3 )
    rig.button('AddButton',label='Add',width=50,command='SK_fingerAdd()')
    rig.button('ResetButton',label='Reset',width=50,command='SK_fingerCopy()')
    rig.button('EditButton',label='Edit',width=50,en = False,command='SK_fingerEdit()')
    
    rig.setParent( '..' )    

    rig.text('''------------------------
       hope you enjoy that''')
    
    rig.window(GUI,e=True,wh=(315,165))

    rig.showWindow(GUI)


def SK_fillTextField():
    name = rig.optionMenuGrp('nameListField',q=True,value=True)
    rig.textField('aTF',e= True , text =name )     


def SK_loadJoint():
    objs = rig.ls(sl = True)[0]
    if('joint' == rig.nodeType(objs)):
        rig.textFieldButtonGrp('SK_BT_textFieldButtonGrpLoadJnt',e = True,tx = objs)
        rig.textFieldGrp('SK_BT_textFieldGrpJointName',e = True,tx = objs)

     
def SK_addMeshList():
    listSel = rig.textScrollList('meshList',q= True,allItems=True )
    if (str(type(listSel)) == "<type 'NoneType'>"):
        listSel = []
    else:
        pass
    meshSel = rig.ls(sl=True)


    for eachMesh in meshSel:
        if eachMesh in listSel:
            pass
        else:
            rig.textScrollList('meshList',e= True,append=eachMesh )
    
def SK_getFilePath():
    getFilePath =  __file__
    fixPath = getFilePath.replace('rigUI.pyc','')
    fixPath = fixPath.replace('rigUI.py','')
    getPath = fixPath.replace('\\','/')
    return getPath

def SK_delMeshList():
    listSel = rig.textScrollList('meshList',q= True,selectItem=True )
    for eachListSel in listSel:
        rig.textScrollList('meshList',e= True,removeItem=eachListSel)


def SK_rigSkin():
    jnts = SK_selectSkinJnt()
    rig.select(cl = True)
    skinMeshList = rig.textScrollList('meshList',q=True,allItems=True)
    for eachSelMesh in skinMeshList:
        if rig.listRelatives(eachSelMesh,s = True):
            rig.skinCluster(jnts,eachSelMesh,toSelectedBones=True,maximumInfluences=2,dropoffRate=4,removeUnusedInfluence=False)
        else:
            try:
                skinObjs = [rig.listRelatives(obj,p = True)[0] for obj in rig.listRelatives(eachSelMesh,ad = True,c = True,type = 'shape')]
                if skinObjs:
                    for obj in skinObjs:
                        rig.skinCluster(jnts,obj,toSelectedBones=True,maximumInfluences=2,dropoffRate=4,removeUnusedInfluence=False)
                       
            except:
                pass

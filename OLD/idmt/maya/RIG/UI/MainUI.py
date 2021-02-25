#-*- coding: utf-8 -*-
import maya.cmds as rig
import maya.mel as MEL
from RIG.selectJoint import SK_selectSkinJnt
from RIG.commonly.bodyTemplate import SK_BodyJointPosition
from RIG.commonly.restoreJoint import *
from RIG.fingerPose import *
from RIG.commonly.base import *

from RIG.commonly.mirrorCurve import SK_MirrorCurveControlCmd
from RIG.commonly.resetControllerDefaultPose import SK_creatConDefaultPos
from RIG.commonly.addFingerJoint import SK_createFingers 
from RIG.IKFK import SK_IKFKSwitchCommand
from RIG.tools.skeletoneToController import buildSKTOCON
from RIG.tools.deformerConvert import softModToCluster
from RIG.tools.base import *
from RIG.selectProject import SK_SelectProject

import RIG.UI.FileOption.MainLayout as UIFile
import RIG.UI.AutoRigging.MainLayout as UIAutoRigging
import RIG.UI.Assemblage.MainLayout as UIAssemblage
import RIG.UI.RiggingTools.MainLayout as UIRiggingTools
import RIG.UI.FaceRigging.MainLayout as UIFaceRigging


class SK_IDMTRigUI(object):
    def __init__(self):
        self.displayUI()
        
    def displayUI(self):
        IDMTRigGUI='autoRigging'
        if rig.window(IDMTRigGUI,exists=True):
            rig.deleteUI(IDMTRigGUI)
        self.MainWindow = rig.window(IDMTRigGUI,title='IDMT 2009 AutoRig',menuBar=True,wh=  (400,780),minimizeButton=True,maximizeButton=True)

        UIFile.FileOption(self.MainWindow)
        
        self.tabs = rig.tabLayout(innerMarginWidth=5,innerMarginHeight=5)
        CAutoRigging = UIAutoRigging.AutoRigging( self.tabs )
        self.AutoRiggingLayout = CAutoRigging.getLayout()
        
        CUIAssemblage = UIAssemblage.Assemblage( self.tabs )
        self.assemblageLayout = CUIAssemblage.getLayout()
        
        CUIRiggingTools = UIRiggingTools.RiggingTools( self.tabs )
        self.RiggingToolsLayout = CUIRiggingTools.getLayout()

        CUIFaceRigging = UIFaceRigging.FaceRigging( self.tabs )
        self.faceRiggingLayout = CUIFaceRigging.getLayout()

        rig.tabLayout( self.tabs,edit=True,tabLabel=((self.AutoRiggingLayout,'AutoRigging'), (self.assemblageLayout,'assemblage'),  (self.RiggingToolsLayout,'RiggingTools'),(self.faceRiggingLayout,'faceRigging')),\
                       selectTabIndex = self.getOptionVar(),changeCommand = lambda x = 0:self.setOptionVar())
        
        rig.showWindow(IDMTRigGUI)    
        rig.window(IDMTRigGUI,e=True,wh=(344,780))
    
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

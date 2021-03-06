import maya.cmds as cmds

global edo_facialCtrlModePanle
global edo_facialViewModePanle
global edo_bodyCtrlModePlane

def edo_listTheChar():
    chars=[]
    try:
        cmds.select(cmds.ls('*:CHR'),r=1)
    except:
        print "this scene has not the characterGroup named CHR!"
        chars.append('NONE')
        return chars
    allRef=cmds.ls(sl=1)
    for char in allRef:
        #char = allRef[0]
        nameSpace=char.replace("CHR","");
        chars.append(nameSpace)
    cmds.select(cl=1)
    return chars


def edo_ccCamButtonCmd():
    global edo_facialCtrlModePanle
    global edo_facialViewModePanle
    global edo_bodyCtrlModePlane
    selectButton=cmds.optionMenu('nameSpaceOptionMenu',q=1,v=1)
    lookCtrlCam=selectButton+'FM_facialCtrl_cam'
    lookCtrlCamShape=selectButton+'FM_facialCtrl_camShape'
    lookViewCam=selectButton+'FM_faceMapCam'
    lookViewCamShape=selectButton+'FM_faceMapCamShape'
    if cmds.objExists(lookCtrlCam):
        cmds.frameLayout('edo_facialCtrlFrameLayout',e=1,vis=1)
        if not cmds.panel(edo_facialCtrlModePanle,exists=1):
            cmds.setParent('edo_facialCtrlPanel1')
            edo_facialCtrlModePanle=cmds.modelPanel(l='edo_facialCtrlModePanle')
        cmds.modelPanel(edo_facialCtrlModePanle,edit=True, camera=lookCtrlCam)
        cmds.modelEditor(edo_facialCtrlModePanle,e=1,alo=0,gr=0,hud=0,nc=1)
        ##cmds.setAttr((lookCtrlCam+'.tx'),0)
        ##cmds.setAttr((lookCtrlCam+'.ty'),0)
        ##cmds.setAttr((lookCtrlCamShape+'.orthographicWidth'),20)
    else:
        cmds.frameLayout('edo_facialCtrlFrameLayout',e=1,vis=0)
    if cmds.objExists(lookViewCam):
        cmds.frameLayout('edo_facialViewFrameLayout',e=1,vis=1)
        if not cmds.panel(edo_facialViewModePanle,exists=1):
            cmds.setParent('edo_facialViewPanel1')
            edo_facialViewModePanle=cmds.modelPanel(l='edo_facialViewModePanle')
        cmds.modelPanel(edo_facialViewModePanle,edit=True, camera=lookViewCam)
        cmds.modelEditor(edo_facialViewModePanle,e=1,alo=0,gr=0,hud=0,ns=1,pm=1);
        cmds.modelEditor(edo_facialViewModePanle,e=1,displayAppearance='smoothShaded')
        ##cmds.setAttr((lookViewCam+'.tx'),0)
        ##cmds.setAttr((lookViewCam+'.ty'),0)
        ##cmds.setAttr((lookViewCamShape+'.orthographicWidth'),20)
    else:
        cmds.frameLayout('edo_facialViewFrameLayout',e=1,vis=0)
        
    if cmds.objExists('re_bodyCtrl_cam'):
        cmds.button('referenceQKSbutton',e=1,vis=0)
        cmds.frameLayout('edo_bodyCtrlFrameLayout',e=1,vis=1)
        if not cmds.panel(edo_bodyCtrlModePlane,exists=1):
            cmds.setParent('edo_bodyCtrlPanel1')
            edo_bodyCtrlModePlane=cmds.modelPanel(l='edo_bodyCtrlModePlane')
        cmds.modelPanel(edo_bodyCtrlModePlane,edit=True, camera='re_bodyCtrl_cam')
        cmds.modelEditor(edo_bodyCtrlModePlane,e=1,alo=1,gr=0,hud=0,lc=1,m=0,displayAppearance='smoothShaded')
        
        if (cmds.checkBox('reSelectSwithcCheckBox',q=1,v=1)==1):
            reSelectionOn()
        else:
            reSelectionOff()
        
        edo_changeNameSpace(selectButton)
    else:
        cmds.button('referenceQKSbutton',e=1,vis=1)
        cmds.frameLayout('edo_bodyCtrlFrameLayout',e=1,vis=0)
        
 
def edo_changeNameSpace(nameSpace):
    allrsls=cmds.ls(type='reSelectLocator')
    for rsl in allrsls:
        #rsl=allrsls[0]
        cmds.setAttr(rsl+'.nameSpace',nameSpace,type='string')

def edo_changeEasyCtrlPlaneWindowSize():
    index=cmds.tabLayout('edo_EasyCtrlPlaneTab',q=1,sti=1)
    if (index==1):
        cmds.window('edo_EasyCtrlPlane',e=1,w=1050,h=600)
        cmds.columnLayout('edo_facialCtrlColum1',e=1,columnWidth=1050)
    if (index==2):
        cmds.window('edo_EasyCtrlPlane',e=1,w=480,h=600)
        cmds.columnLayout('edo_facialCtrlColum1',e=1,columnWidth=480)

def edo_upDataCharacter():
    chars=edo_listTheChar()
    if cmds.optionMenu('nameSpaceOptionMenu',ex=1):
        cmds.deleteUI('nameSpaceOptionMenu')
    cmds.setParent('edo_facialCtrlColum2')
    nameSpaceOptionMenu=cmds.optionMenu('nameSpaceOptionMenu',label='nameSpace:',w=230,changeCommand='edo_ccCamButtonCmd()')
    for char in chars:
        cmds.menuItem(char,label=char)
    edo_ccCamButtonCmd()
    
        
def edo_restoreTheViewCamera():
    selectButton=cmds.optionMenu('nameSpaceOptionMenu',q=1,v=1)
    lookCtrlCam=selectButton+'FM_faceMapCam'
    lookCtrlCamShape=cmds.listRelatives(lookCtrlCam,s=1)
    cmds.setAttr(lookCtrlCam+'.tx',0)
    cmds.setAttr(lookCtrlCam+'.ty',-1)
    cmds.setAttr(lookCtrlCam+'.tz',2)
    cmds.setAttr(lookCtrlCam+'.rx',10)
    cmds.setAttr(lookCtrlCam+'.ry',0)
    cmds.setAttr(lookCtrlCam+'.rz',0)
    cmds.setAttr(lookCtrlCamShape[0]+'.centerOfInterest',5)
    
def edo_restoreTheCtrlCamera():
    selectButton=cmds.optionMenu('nameSpaceOptionMenu',q=1,v=1)
    lookCtrlCam=selectButton+'FM_facialCtrl_cam'
    lookCtrlCamShape=cmds.listRelatives(lookCtrlCam,s=1)
    cmds.setAttr(lookCtrlCam+'.tx',0)
    cmds.setAttr(lookCtrlCam+'.ty',28)
    cmds.setAttr(lookCtrlCam+'.tz',18)
    cmds.setAttr(lookCtrlCam+'.rx',0)
    cmds.setAttr(lookCtrlCam+'.ry',0)
    cmds.setAttr(lookCtrlCam+'.rz',0)
    cmds.setAttr(lookCtrlCamShape[0]+'.centerOfInterest',5)


def reSelectionOn():
    #print "reSelection is on!"
    allrsls=cmds.ls(type='reSelectLocator')
    for i in allrsls:
        cmds.setAttr(i+'.reSelectSwitch',1)

def reSelectionOff():
    #print "reSelection is off!"
    allrsls=cmds.ls(type='reSelectLocator')
    for i in allrsls:
        cmds.setAttr(i+'.reSelectSwitch',0)
        
        
def edo_iniBodyCtrlPanel():
    #print "edo_iniBodyCtrlPanel()"
    cmds.button('referenceQKSbutton',e=1,vis=0)
    ##cmds.file('E:/program/python/ninjago/QSK_panel.ma',r=1,dns=1)
    if not cmds.objExists('re_bodyCtrl_cam'):
        cmds.file('//file-cluster/gdc/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/QSK_panel.ma',r=1,dns=1)
    edo_ccCamButtonCmd()

        
def edo_EasyCtrlPlaneUI():
    global edo_facialCtrlModePanle
    global edo_facialViewModePanle
    global edo_bodyCtrlModePlane
    if cmds.window('edo_EasyCtrlPlane',ex=1):
        cmds.deleteUI('edo_EasyCtrlPlane')
    cmds.window('edo_EasyCtrlPlane',t='edo_EasyCtrlPlane',w=1050,h=600)
    cmds.columnLayout('edo_facialCtrlColum1',columnAttach=('both', 5), rowSpacing=5, columnWidth=1050)
    cmds.rowLayout('edo_facialCtrlRow2',numberOfColumns=3,nch=3,columnWidth3=(250,200,600),ct3=('left','left','left'),co3=(0,10,0))
    cmds.frameLayout( label='charName', borderStyle='in',w=250,h=140)
    cmds.columnLayout('edo_facialCtrlColum2',columnAttach=('both', 5), rowSpacing=10, columnWidth=150)
    cmds.button('edo_upDataCharButton',l='updata the reference character',w=230,c='edo_upDataCharacter()')

    cmds.setParent('edo_facialCtrlRow2')
    cmds.frameLayout( label='facialChannelBox', borderStyle='in',w=200,h=140)
    cmds.channelBox('facialChannelBox',sol=0,hol=0,ool=0,mnp='standard',w=200,h=140,tf=1)

    cmds.setParent('edo_facialCtrlColum1')
    cmds.tabLayout('edo_EasyCtrlPlaneTab',innerMarginWidth=5, innerMarginHeight=5,cc='edo_changeEasyCtrlPlaneWindowSize()')
    cmds.rowLayout('edo_facialCtrlRow1',numberOfColumns=2,nch=2,columnWidth2=(500,500),ct2=('left','left'),co2=(5,25))
    cmds.frameLayout('edo_facialViewFrameLayout',label='facialView---[right click to restore cam position]', borderStyle='in',w=500,h=400)
    cmds.popupMenu('facialViewPopupMenu',button=3)
    cmds.menuItem('facialViewPopupMenuItem1',l='restore the camera pos!',c='edo_restoreTheViewCamera()')
    cmds.paneLayout('edo_facialViewPanel1')
    edo_facialViewModePanle=cmds.modelPanel(l='edo_facialViewModePanle')

    cmds.setParent('edo_facialCtrlRow1')
    cmds.frameLayout('edo_facialCtrlFrameLayout',label='facialCtrl---[right click to restore cam position]', borderStyle='in',w=500,h=400)
    cmds.popupMenu('facialCtrlPopupMenu',button=3)
    cmds.menuItem('facialCtrlPopupMenuItem1',l='restore the camera pos!',c='edo_restoreTheCtrlCamera()')
    cmds.paneLayout('edo_facialCtrlPanel1')
    edo_facialCtrlModePanle=cmds.modelPanel(l='edo_facialCtrlModePanle')

    cmds.setParent('edo_EasyCtrlPlaneTab')
    cmds.columnLayout('edo_bodyCtrlColum1',columnAttach=('both', 5), rowSpacing=5, columnWidth=480)
    cmds.button('referenceQKSbutton',l='initialize the bodyCtrlPanel',w=400,h=100,c='edo_iniBodyCtrlPanel()')
    
    cmds.frameLayout('edo_bodyCtrlFrameLayout',label='bodyCtrl',borderStyle='in',w=500,h=400)
    cmds.checkBox('reSelectSwithcCheckBox',label='reSelectionOn/Off',onc='reSelectionOn()',v=1,ofc='reSelectionOff()');
    
    cmds.paneLayout('edo_bodyCtrlPanel1')
    edo_bodyCtrlModePlane=cmds.modelPanel(l='edo_bodyCtrlModePlane')
    if cmds.objExists('re_bodyCtrl_cam'):
        cmds.button('referenceQKSbutton',e=1,vis=0)
        cmds.frameLayout('edo_bodyCtrlFrameLayout',e=1,vis=1)
        cmds.modelPanel(edo_bodyCtrlModePlane,edit=True, camera='re_bodyCtrl_cam')
        cmds.modelEditor(edo_bodyCtrlModePlane,e=1,alo=1,gr=0,hud=0,lc=1,m=0,displayAppearance='smoothShaded')
    else:
        cmds.button('referenceQKSbutton',e=1,vis=1)
        cmds.frameLayout('edo_bodyCtrlFrameLayout',e=1,vis=0)
    
    cmds.tabLayout('edo_EasyCtrlPlaneTab',e=1,tabLabel=(('edo_facialCtrlRow1','facialCtrlPlane'),('edo_bodyCtrlColum1','bodyCtrlPlane')))
    
    edo_upDataCharacter()
    edo_ccCamButtonCmd()
 
    cmds.window('edo_EasyCtrlPlane',e=1,w=1050,h=600)
    cmds.showWindow('edo_EasyCtrlPlane')
edo_EasyCtrlPlaneUI()
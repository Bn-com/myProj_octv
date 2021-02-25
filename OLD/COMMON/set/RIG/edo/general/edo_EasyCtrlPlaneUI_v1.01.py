import maya.cmds as cmds
import maya.OpenMaya as om

global edo_facialCtrlModePanle
global edo_facialViewModePanle
global edo_bodyCtrlModePlane


def edo_listTheChar():
    chars=[]
    cmds.select(cl=1)
    try:
        cmds.select(cmds.ls('*:CHR'),r=1)
    except:
        print "this scene has not the characterGroup named :CHR!"
    try:
        cmds.select(cmds.ls('CHR'),add=1)
    except:
        print "this scene has not the characterGroup named CHR!"
    #for_vicky_vicky
    try:
        cmds.select(cmds.ls('*:m_spineA_neck_03_ctrlPri'),add=1)
    except:
        print "this scene has not the characterGroup named m_spineA_torso_ctrl!"
    try:
        cmds.select(cmds.ls('m_spineA_neck_03_ctrlPri'),add=1)
    except:
        print "this scene has not the characterGroup named m_spineA_torso_ctrl!"
    try:
        cmds.select(cmds.ls('c_waist_Ctrl'),add=1)
    except:
        print "this scene has not the characterGroup named c_waist_Ctrl!"
    try:
        cmds.select(cmds.ls('*:c_waist_Ctrl'),add=1)
    except:
        print "this scene has not the characterGroup named c_waist_Ctrl!"
    allRef=cmds.ls(sl=1)
    if not allRef:
        chars.append('NONE')
        return chars
    for char in allRef:
        #char = allRef[0]
        nameSpace=char.replace("CHR","").replace('m_spineA_neck_03_ctrlPri','').replace('c_waist_Ctrl','')
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
        print 'there is no FM_facialCtrl_cam'
        #cmds.frameLayout('edo_facialCtrlFrameLayout',e=1,vis=0)
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
        print 'there is no FM_faceMapCam'
        #cmds.frameLayout('edo_facialViewFrameLayout',e=1,vis=0)
    #for_vicky
    vlookCtrlCam=selectButton+'FM_002'
    vlookCtrlCamShape=selectButton+'FM_002Shape'
    vlookViewCam=selectButton+'FM_001'
    vlookViewCamShape=selectButton+'FM_001Shape'
    if cmds.objExists(vlookCtrlCam):
        edo_setorthographicCamera(vlookCtrlCam)
        cmds.frameLayout('edo_facialCtrlFrameLayout',e=1,vis=1)
        if not cmds.panel(edo_facialCtrlModePanle,exists=1):
            cmds.setParent('edo_facialCtrlPanel1')
            edo_facialCtrlModePanle=cmds.modelPanel(l='edo_facialCtrlModePanle')
        cmds.modelPanel(edo_facialCtrlModePanle,edit=True, camera=vlookCtrlCam)
        cmds.modelEditor(edo_facialCtrlModePanle,e=1,alo=0,gr=0,hud=0,nc=1)
        ##cmds.setAttr((lookCtrlCam+'.tx'),0)
        ##cmds.setAttr((lookCtrlCam+'.ty'),0)
        ##cmds.setAttr((lookCtrlCamShape+'.orthographicWidth'),20)
    else:
        print 'there is no FM_002'
        #cmds.frameLayout('edo_facialCtrlFrameLayout',e=1,vis=0)
    if cmds.objExists(vlookViewCam):
        edo_setorthographicCamera(vlookViewCam)
        cmds.frameLayout('edo_facialViewFrameLayout',e=1,vis=1)
        if not cmds.panel(edo_facialViewModePanle,exists=1):
            cmds.setParent('edo_facialViewPanel1')
            edo_facialViewModePanle=cmds.modelPanel(l='edo_facialViewModePanle')
        cmds.modelPanel(edo_facialViewModePanle,edit=True, camera=vlookViewCam)
        cmds.modelEditor(edo_facialViewModePanle,e=1,alo=0,gr=0,hud=0,ns=1,pm=1);
        cmds.modelEditor(edo_facialViewModePanle,e=1,displayAppearance='smoothShaded')
        ##cmds.setAttr((lookViewCam+'.tx'),0)
        ##cmds.setAttr((lookViewCam+'.ty'),0)
        ##cmds.setAttr((lookViewCamShape+'.orthographicWidth'),20)
    else:
        print 'there is no FM_001'
        #cmds.frameLayout('edo_facialViewFrameLayout',e=1,vis=0)
    
        
    if cmds.objExists('re_bodyCtrl_cam'):
        cmds.button('referenceQKSbutton',e=1,vis=0)
        cmds.optionMenu('qskOptionMenu',e=1,vis=1)
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
        cmds.optionMenu('qskOptionMenu',e=1,vis=0)
        cmds.frameLayout('edo_bodyCtrlFrameLayout',e=1,vis=0)

def edo_setorthographicCamera(cname):
    #cname='faxe_original:FM_002'
    cmds.setAttr(cname+'.orthographic',1)
    cmds.transformLimits(cname,etx=[0,0])
    cmds.transformLimits(cname,ety=[0,0])
    cmds.transformLimits(cname,etz=[0,0])
    connect=cmds.listConnections(cname+'.orthographicWidth',s=1,d=0,p=1)
    if connect:
        cmds.disconnectAttr(connect[0],cname+'.orthographicWidth')
        

        
 
def edo_changeNameSpace(nameSpace):
    allrsls=cmds.ls(type='reSelectLocator')
    for rsl in allrsls:
        #rsl=allrsls[0]
        try:
            cmds.setAttr(rsl+'.nameSpace',nameSpace,type='string')
        except:
            print 'attribute has already locked,pass...'

def edo_upDataCharacter():
    chars=edo_listTheChar()
    if cmds.optionMenu('nameSpaceOptionMenu',ex=1):
        cmds.deleteUI('nameSpaceOptionMenu')
    cmds.setParent('edo_facialCtrlColum2')
    nameSpaceOptionMenu=cmds.optionMenu('nameSpaceOptionMenu',label='nameSpace:',w=230,changeCommand='edo_ccCamButtonCmd()')
    #cmds.setParent('nameSpaceOptionMenu')
    #cmds.menuItem(char,label=char)
    for char in chars:
        cmds.menuItem(char,label=char)
    edo_ccCamButtonCmd()
    edo_refreshQSKplane()
    
        
def edo_restoreTheViewCamera():
    selectButton=cmds.optionMenu('nameSpaceOptionMenu',q=1,v=1)
    lookCtrlCam=selectButton+'FM_faceMapCam'
    if cmds.objExists(lookCtrlCam):
        lookCtrlCamShape=cmds.listRelatives(lookCtrlCam,s=1)
        cmds.xform(lookCtrlCam,os=1,t=[0,0,10])
        cmds.setAttr(lookCtrlCam+'.orthographicWidth',30)
        cmds.setAttr(lookCtrlCam+'.centerOfInterest',5)
    #for_vicky
    vlookCtrlCam=selectButton+'FM_001'
    if cmds.objExists(vlookCtrlCam):
        lookCtrlCamShape=cmds.listRelatives(vlookCtrlCam,s=1)
        cmds.xform(vlookCtrlCam,os=1,t=[0,0,10])
        cmds.setAttr(vlookCtrlCam+'.orthographicWidth',30)
        cmds.setAttr(vlookCtrlCam+'.centerOfInterest',5)
        
def edo_restoreTheCtrlCamera():
    selectButton=cmds.optionMenu('nameSpaceOptionMenu',q=1,v=1)
    lookCtrlCam=selectButton+'FM_facialCtrl_cam'
    if cmds.objExists(lookCtrlCam):
        lookCtrlCamShape=cmds.listRelatives(lookCtrlCam,s=1)
        cmds.xform(lookCtrlCam,os=1,t=[0,0,10])
        cmds.setAttr(lookCtrlCam+'.orthographicWidth',30)
        cmds.setAttr(lookCtrlCam+'.centerOfInterest',5)
    #for_vicky
    vlookCtrlCam=selectButton+'FM_002'
    if cmds.objExists(vlookCtrlCam):
        vlookCtrlCamShape=cmds.listRelatives(vlookCtrlCam,s=1)
        cmds.xform(vlookCtrlCam,os=1,t=[0,0,10])
        cmds.setAttr(vlookCtrlCam+'.orthographicWidth',30)
        cmds.setAttr(vlookCtrlCam+'.centerOfInterest',5)


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
    ##print "edo_iniBodyCtrlPanel()"
    ##cmds.button('referenceQKSbutton',e=1,vis=0)
    ##cmds.file('E:/program/python/ninjago/QSK_panel.ma',r=1,dns=1)
    mg=om.MGlobal()
    version=mg.mayaVersion()
    if not cmds.objExists('re_bodyCtrl_cam'):
        if '2014' in version:
            cmds.file('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/QSK_lib/QSK_model_2014.ma',r=1,dns=1)
        else:
            cmds.file('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/QSK_lib/QSK_model.ma',r=1,dns=1)
    edo_findTheVersion()
    edo_ccCamButtonCmd()
    edo_saveAndLoadOptionVar()
    edo_changeVersionCmd()

def edo_findTheVersion():
    if cmds.objExists('re_bodyCtrl_cam'):
        versionString=cmds.listRelatives('QSK_bodyCtrlPlane',type='transform')
        versionString.remove('re_bodyCtrl_cam')
        for version in versionString:
            if cmds.menuItem(version,ex=1):
                cmds.deleteUI(version)
            cmds.menuItem(version,label=version,p='qskOptionMenu')

def edo_changeVersionCmd():
    versionid=cmds.optionMenu('qskOptionMenu',q=1,sl=1)-1
    if cmds.objExists('re_bodyCtrl_cam'):
        cmds.setAttr('QSK_bodyCtrlPlane.version',versionid)
        cmds.optionVar(iv=('edo_EasyCtrlPlane_qskOptionMenu',versionid))

def edo_saveAndLoadOptionVar():
    if not cmds.optionVar(exists='edo_EasyCtrlPlane_qskOptionMenu'):
        cmds.optionVar(iv=('edo_EasyCtrlPlane_qskOptionMenu',0))
    else:
        versionid=cmds.optionVar(q='edo_EasyCtrlPlane_qskOptionMenu')
        try:
            cmds.optionMenu('qskOptionMenu',e=1,sl=versionid+1)
        except:
            print 'qskOptionMenu is empty!'

def edo_refreshQSKplane():
    sels=cmds.ls('vickyl_vicky')
    if sels:
        cmds.setAttr(sels[0]+'.view',cmds.getAttr(sels[0]+'.view'))
        
def edo_changeQSKplane(value):
    #value=1
    sels=cmds.ls(sl=1)
    if not len(sels)==1:
        return False
    cmds.select(cl=1)
    if sels==[]:
        return False
    obj=sels[0]
    buffer=obj.split(':')
    if not buffer==None:
        if len(buffer)==1:
            cmds.setAttr('normal_people.view',value)
            cmds.setAttr('vickyl_vicky.view',value)
            cmds.setAttr('calimero.view',value)
            return True
        else:
            cmds.setAttr(buffer[0]+':normal_people.view',value)
            cmds.setAttr(buffer[0]+':vickyl_vicky.view',value)
            cmds.setAttr('calimero.view',value)
            return True
    
    
######2013_01_08_for_vicky_vicky_ikfk_switch######        
#vv_iffk_switch('LfLeg','globalIk')
#vv_iffk_switch('LfLeg','localIk')
#vv_iffk_switch('LfLeg','localFk')
#vv_iffk_switch('RtLeg','globalIk')
#vv_iffk_switch('RtLeg','localIk')
#vv_iffk_switch('LfArm','localFk')
#vv_iffk_switch('LfArm','globalIk')
#vv_iffk_switch('LfArm','localIk')
#vv_iffk_switch('LfArm','localFk')
#vv_iffk_switch('RtArm','globalIk')
#vv_iffk_switch('RtArm','localIk')
#vv_iffk_switch('RtArm','localFk')
def vv_iffk_switch(part,model):
    sels=cmds.ls(sl=1)
    if not sels:
        return False
    sel=sels[0]
    namespacestr=cmds.getAttr(sel+'.nameSpace')
    cmds.select(cl=1)
    if part=='LfLeg':
        if model=='globalIk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.FK_2_IK"),1)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.globalIK_2_localIK") ,0)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.FK_vis" ),0)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.globalIK_vis" ),1)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.localIK_vis" ),0)
        if model=='localIk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.FK_2_IK"),1)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.globalIK_2_localIK") ,1)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.FK_vis" ),0)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.globalIK_vis" ),0)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.localIK_vis" ),1)
        if model=='localFk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.FK_2_IK"),0)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.globalIK_2_localIK") ,0)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.FK_vis" ),1)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.globalIK_vis" ),0)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.localIK_vis" ),0)
    if part=='RtLeg':
        if model=='globalIk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.FK_2_IK"),1)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.globalIK_2_localIK") ,0)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.FK_vis" ),0)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.globalIK_vis" ),1)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.localIK_vis" ),0)
        if model=='localIk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.FK_2_IK"),1)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.globalIK_2_localIK") ,1)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.FK_vis" ),0)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.globalIK_vis" ),0)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.localIK_vis" ),1)
        if model=='localFk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.FK_2_IK"),0)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.globalIK_2_localIK") ,0)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.FK_vis" ),1)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.globalIK_vis" ),0)
            cmds.setAttr ((namespacestr+"r_legA_ankle_ctrl.localIK_vis" ),0)
    if part=='LfArm':
        if model=='globalIk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.FK_2_IK"),1)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.globalIK_2_localIK") ,0)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.FK_vis" ),0)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.globalIK_vis" ),1)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.localIK_vis" ),0) 
        if model=='localIk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.FK_2_IK"),1)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.globalIK_2_localIK") ,1)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.FK_vis" ),0)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.globalIK_vis" ),0)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.localIK_vis" ),1)
        if model=='localFk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.FK_2_IK"),0)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.globalIK_2_localIK") ,0)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.FK_vis" ),1)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.globalIK_vis" ),0)
            cmds.setAttr ((namespacestr+"l_armA_wrist_ctrl.localIK_vis" ),0) 
    if part=='RtArm':
        if model=='globalIk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.FK_2_IK"),1)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.globalIK_2_localIK") ,0)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.FK_vis" ),0)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.globalIK_vis" ),1)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.localIK_vis" ),0) 
        if model=='localIk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.FK_2_IK"),1)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.globalIK_2_localIK") ,1)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.FK_vis" ),0)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.globalIK_vis" ),0)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.localIK_vis" ),1)
        if model=='localFk':
            #namespacestr=''  
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.FK_2_IK"),0)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.globalIK_2_localIK") ,0)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.FK_vis" ),1)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.globalIK_vis" ),0)
            cmds.setAttr ((namespacestr+"r_armA_wrist_ctrl.localIK_vis" ),0)
            cmds.setAttr ((namespacestr+"l_legA_ankle_ctrl.localIK_vis" ),1)
            
            

def edo_loadQSKplugin():
    path='\\\\file-cluster\\GDC\\Resource\\Support\\Maya\\extra\\Rigging_Simulation\\mll'
    mg=om.MGlobal()
    version=mg.mayaVersion()
    version='maya'+str(version[:4])
    print version
    if cmds.pluginInfo('reSelectLocator.mll',query=True,l=True):
        try:
            cmds.unloadPlugin('reSelectLocator.mll')
        except:
            print 'this plugin was using in this scene!'
    try:
        cmds.loadPlugin(path+'\\'+version+'\\x64\\reSelectLocator.mll')
    except:
        cmds.loadPlugin(path+'\\'+version+'\\x32\\reSelectLocator.mll')


#edo_selectFacialSetCtrls(cmds.optionMenu('nameSpaceOptionMenu',q=1,v=1))
def edo_selectFacialSetCtrls(nameSpace=''):
    #nameSpace=cmds.optionMenu('nameSpaceOptionMenu',q=1,v=1)
    sn='facialSet'
    if not nameSpace=='':    
        if not nameSpace[-1]==':':
            nameSpace=nameSpace+':'
        sn=nameSpace+'facialSet'
    if cmds.objExists(sn):
        cmds.select(sn,add=1)

#edo_unselectFacialSetCtrls(cmds.optionMenu('nameSpaceOptionMenu',q=1,v=1))   
def edo_unselectFacialSetCtrls(nameSpace=''):
    #nameSpace='do4_c402001Peach:'
    sn='facialSet'
    if not nameSpace=='':    
        if not nameSpace[-1]==':':
            nameSpace=nameSpace+':'
        sn=nameSpace+'facialSet'
    if cmds.objExists(sn):
        cmds.select(sn,d=1)
        
#edo_setDisplayModel(cmds.optionMenu('nameSpaceOptionMenu',q=1,v=1),1)
def edo_setDisplayModel(nameSpace='',v=0):
    #nameSpace=cmds.optionMenu('nameSpaceOptionMenu',q=1,v=1)
    ms='Master'
    if not nameSpace=='':    
        if not nameSpace[-1]==':':
            nameSpace=nameSpace+':'
        ms=nameSpace+'Master'
    if cmds.objExists(ms+'.model_view'):
        cmds.setAttr(ms+'.model_view',v)
    cmds.select(cl=1)

def edo_setTentaclesCtrlSwitch(v=1):
    #v=1
    nsp=''
    sels=cmds.ls(sl=1)
    if sels:
        #sel='aa:bb:cc:dd'
        sel=sels[-1]
        ns=sel.split(':')
        if len(ns)>1:
            for i in range(0,len(ns)-1):
                nsp=nsp+ns[i]+':'
            #print nsp
        cmds.setAttr(nsp+'GRP_QKS_tentacles.switch',v)
        cmds.select(sel,d=1)

def edo_changeEasyCtrlPlaneWindowSize():
    index=cmds.tabLayout('edo_EasyCtrlPlaneTab',q=1,sti=1)
    if (index==1):
        cmds.window('edo_EasyCtrlPlane',e=1,w=1240,h=700)
        cmds.columnLayout('edo_facialCtrlColum1',e=1,columnWidth=1240)
    if (index==2):
        #cmds.window('edo_EasyCtrlPlane',e=1,w=480,h=730)
        #cmds.columnLayout('edo_facialCtrlColum1',e=1,columnWidth=480)
        cmds.window('edo_EasyCtrlPlane',e=1,w=850,h=900)
        cmds.columnLayout('edo_facialCtrlColum1',e=1,columnWidth=850)
     
def edo_EasyCtrlPlaneUI():
    edo_loadQSKplugin()
    global edo_facialCtrlModePanle
    global edo_facialViewModePanle
    global edo_bodyCtrlModePlane
    if cmds.window('edo_EasyCtrlPlane',ex=1):
        cmds.deleteUI('edo_EasyCtrlPlane')
    cmds.window('edo_EasyCtrlPlane',t='edo_EasyCtrlPlane',w=1050,h=600)
    cmds.columnLayout('edo_facialCtrlColum1',columnAttach=('both', 5), rowSpacing=5, columnWidth=1240)
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
    #cmds.rowLayout('edo_facialCtrlRow1',e=1,columnWidth2=(100,100))
    cmds.frameLayout('edo_facialViewFrameLayout',label='facialView---[right click to restore cam position]', borderStyle='in',w=600,h=700)
    #cmds.frameLayout('edo_facialViewFrameLayout',e=1,w=500,h=700)
    cmds.popupMenu('facialViewPopupMenu',button=3)
    cmds.menuItem('facialViewPopupMenuItem1',l='restore the camera pos!',c='edo_restoreTheViewCamera()')
    cmds.paneLayout('edo_facialViewPanel1')
    edo_facialViewModePanle=cmds.modelPanel(l='edo_facialViewModePanle')

    cmds.setParent('edo_facialCtrlRow1')
    cmds.frameLayout('edo_facialCtrlFrameLayout',label='facialCtrl---[right click to restore cam position]', borderStyle='in',w=600,h=700)
    cmds.popupMenu('facialCtrlPopupMenu',button=3)
    cmds.menuItem('facialCtrlPopupMenuItem1',l='restore the camera pos!',c='edo_restoreTheCtrlCamera()')
    cmds.paneLayout('edo_facialCtrlPanel1')
    edo_facialCtrlModePanle=cmds.modelPanel(l='edo_facialCtrlModePanle')

    cmds.setParent('edo_EasyCtrlPlaneTab')
    #cmds.columnLayout('edo_bodyCtrlColum1',columnAttach=('left', 5), rowSpacing=10, columnWidth=480)
    cmds.columnLayout('edo_bodyCtrlColum1',columnAttach=('left', 5), rowSpacing=10, columnWidth=850)
    #cmds.columnLayout('edo_bodyCtrlColum1',e=1, columnWidth=550)
    cmds.separator(style='single')
    #cmds.control('edo_bodyCtrlColum1',q=1,p=1)
    #cmds.button('referenceQKSbutton',l='initialize the bodyCtrlPanel',w=460,h=100,c='edo_iniBodyCtrlPanel()')
    cmds.button('referenceQKSbutton',l='initialize the bodyCtrlPanel',w=840,h=100,c='edo_iniBodyCtrlPanel()')
    qskOptionMenu=cmds.optionMenu('qskOptionMenu',label='select ctrlPanel\'s type as project:',w=460,vis=0,cc='edo_changeVersionCmd()')
    cmds.checkBox('reSelectSwithcCheckBox',label='reSelectionOn/Off',onc='reSelectionOn()',v=1,ofc='reSelectionOff()')
    #cmds.frameLayout('edo_bodyCtrlFrameLayout',label='bodyCtrl',borderStyle='in',w=500,h=460)
    cmds.frameLayout('edo_bodyCtrlFrameLayout',label='bodyCtrl',borderStyle='in',w=850,h=700)
    #cmds.frameLayout('edo_bodyCtrlFrameLayout',e=1,borderStyle='in',w=100,h=100)
    cmds.paneLayout('edo_bodyCtrlPanel1')
    edo_bodyCtrlModePlane=cmds.modelPanel(l='edo_bodyCtrlModePlane')
    if cmds.objExists('re_bodyCtrl_cam'):
        cmds.button('referenceQKSbutton',e=1,vis=0)
        cmds.optionMenu('qskOptionMenu',e=1,vis=1)
        cmds.frameLayout('edo_bodyCtrlFrameLayout',e=1,vis=1)
        cmds.modelPanel(edo_bodyCtrlModePlane,edit=True, camera='re_bodyCtrl_cam')
        cmds.modelEditor(edo_bodyCtrlModePlane,e=1,alo=1,gr=0,hud=0,lc=1,m=0,displayAppearance='smoothShaded')
    else:
        cmds.button('referenceQKSbutton',e=1,vis=1)
        cmds.optionMenu('qskOptionMenu',e=1,vis=0)
        cmds.frameLayout('edo_bodyCtrlFrameLayout',e=1,vis=0)
    
    cmds.tabLayout('edo_EasyCtrlPlaneTab',e=1,tabLabel=(('edo_facialCtrlRow1','facialCtrlPlane'),('edo_bodyCtrlColum1','bodyCtrlPlane')))
          
    edo_upDataCharacter()
    edo_findTheVersion()
    edo_saveAndLoadOptionVar()
    edo_changeVersionCmd()
    edo_ccCamButtonCmd()
 
    cmds.window('edo_EasyCtrlPlane',e=1,w=1050,h=600)
    cmds.showWindow('edo_EasyCtrlPlane')
edo_EasyCtrlPlaneUI()
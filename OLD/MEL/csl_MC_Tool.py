#-*- coding: utf-8 -*-
import sys
sys.path.append('//file-cluster/GDC/Resource/Support/Python/2.7-x64/Lib/site-packages/')
sys.path.append('//file-cluster/GDC/Resource/Support/Maya/Python/')
import os
import maya.cmds as mc
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
def csl_MC_Tool():
	TXTpath = 'Z:/Projects/ShunLiu/ShunLiu_Scratch/TD/Motion Capture/TXT/'
	TXTNames = os.listdir(TXTpath)
	TXTs=[]
	for TXTName in TXTNames:
	    TXT = TXTName.split('.')[0]
	    TXTs.append(TXT)
	    TXTs.sort()
	if mc.window('csl_MC_GetCtrlCamUI',ex = True):
	    mc.deleteUI('csl_MC_GetCtrlCamUI')
	mc.window('csl_MC_GetCtrlCamUI',w=100,h=100,title = u'顺溜项目Layout信息获取工具',rtf = True)
	mc.columnLayout()
	mc.text(l = u'镜头')
	mc.textScrollList( 'GetCamList',numberOfRows=12, allowMultiSelection=True,append=TXTs,selectCommand='csl_MC_sels_Cam()')
	mc.text(l = u'角色')
	mc.columnLayout()
	mc.textScrollList( 'GetCtrlList',numberOfRows=8, allowMultiSelection=True)
	mc.columnLayout( adjustableColumn=True )
	mc.button( label=u'导入摄像机',height=30,width=250,bgc= (0.6,0.1,0.3),c='csl_MC_import_Cam()')
	mc.button( label=u'移动角色到layout位置',height=30,width=250,bgc= (0.6,0.7,0.5),c='csl_MC_move_Character()')
	mc.button( label=u'动画通过,添加新的位移信息',height=30,width=250,bgc= (0.8,0.7,0.4),c='csl_MC_export_Variable()')
	mc.showWindow('csl_MC_GetCtrlCamUI')
	
def csl_MC_sels_Cam():
    shortInfo = mc.textScrollList('GetCamList', q=1, si=1)[0]
    TXTAllPath = 'Z:/Projects/ShunLiu/ShunLiu_Scratch/TD/Motion Capture/TXT/%s.txt' % (shortInfo)
    readInfos = sk_infoConfig.sk_infoConfig().checkFileRead(TXTAllPath)
    Vs = []
    for readInfo in readInfos:
        str_Info = r"variable=%s" % readInfo       
        exec(str_Info)
        Vs.append(variable[0])
    mc.textScrollList('GetCtrlList',e=1,removeAll=1)
    mc.textScrollList('GetCtrlList',e=1,append=Vs)
    
def csl_MC_move_Character():
    selectLocator = mc.ls(sl=1,l=1)
    if len(selectLocator) == 0:
        mc.error(u'===【请选择一个物体】===')   	
    shortInfo = mc.textScrollList('GetCamList', q=1, si=1)[0]
    Character = mc.textScrollList('GetCtrlList', q=1, si=1)[0]
    TXTAllPath = 'Z:/Projects/ShunLiu/ShunLiu_Scratch/TD/Motion Capture/TXT/%s.txt' % (shortInfo)
    readInfos = sk_infoConfig.sk_infoConfig().checkFileRead(TXTAllPath)
    for readInfo in readInfos:
        str_Info = r"variable=%s" % readInfo       
        exec(str_Info)
        if Character == variable[0]:
            mc.setAttr ((selectLocator[0]+'.translate'),variable[1][0],variable[1][1],variable[1][2])
            mc.setAttr ((selectLocator[0]+'.rotate'),variable[2][0],variable[2][1],variable[2][2])
            
def csl_MC_export_Variable():
    selectLocator = mc.ls(sl=1,l=1)
    if len(selectLocator) == 0:
        mc.error(u'===【请选择一个物体】===') 
    Warning = mc.confirmDialog(title = u'注意',message= u'导出位移信息覆盖', button=['OK','Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
    if Warning =='OK':
        valueT = mc.getAttr(selectLocator[0]+'.translate')[0]
        valueR = mc.getAttr(selectLocator[0]+'.rotate')[0]
        shortInfo = mc.textScrollList('GetCamList', q=1, si=1)[0]
        Character = mc.textScrollList('GetCtrlList', q=1, si=1)[0]
        TXTAllPath = 'Z:/Projects/ShunLiu/ShunLiu_Scratch/TD/Motion Capture/TXT/%s.txt' % (shortInfo)
        Values = []      
        V = (Character+'_NEW') , valueT,valueR
        if not V in Values:
            Values.append(V)
        writeInfos = sk_infoConfig.sk_infoConfig().checkFileWrite(TXTAllPath,Values,1)

def csl_MC_import_Cam():
    shortInfo = mc.textScrollList('GetCamList', q=1, si=1)[0]      
    CamPath = 'Z:/Projects/ShunLiu/Project/scenes/Animation/episode_140/episode_camera/%s_cam.ma'%(shortInfo)
    if mc.file(CamPath,query=1,exists=1):
        mc.file(CamPath, i = True)
    else:
        mc.error(u'没有这个相机')
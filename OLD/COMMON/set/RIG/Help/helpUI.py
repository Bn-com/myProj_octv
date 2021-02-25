#-*- coding: utf-8 -*-
import maya.mel as mel
import maya.cmds as rig
import headfile
bodyrigpath=headfile.__file__.replace('headfile.py','RIG/').replace('\\','/')

def SK_helptUI():
    buttonBackGroundColor=[0.3,0.2,0.05]
    IDMTRigGUI='HelpUIWindow'
    if rig.window(IDMTRigGUI,exists=True):
        rig.deleteUI(IDMTRigGUI)
    rig.window(IDMTRigGUI,title= u'选择你所需要的帮助',menuBar=True,wh=  (300,80),minimizeButton=True,maximizeButton=True)
    rig.columnLayout(rowSpacing=5)
    rig.button(l = u'表情设置:blendShape+次级控制方式',bgc=buttonBackGroundColor,w = 295,c ="SK_openHelpDoc(\"face\")")
    rig.button(l = u'表情设置:控制点+mesh影响体方式',bgc=buttonBackGroundColor,w = 295,c = "SK_openHelpDoc(\"influenceFace\")")
    rig.button(l = u'基础身体设置',w = 295,bgc=buttonBackGroundColor,c = "SK_openHelpDoc(\"body\")")

    rig.separator(w = 325,h=5,style='in')
    rig.separator(w = 325,h=5,style='in')
    ##rig.rowColumnLayout(nc = 2,columnWidth = [(1,147),(2,147)])
    #rig.button(l = u'WXTV',bgc=buttonBackGroundColor,w=295,c = "SK_openHelpDoc('winxTv版设置帮助文档')")
    ##rig.button(l = u'RR',c = "SK_openHelpDoc('RR')")
    rig.window(IDMTRigGUI,e=True,wh=(305,310))
    rig.showWindow(IDMTRigGUI)  

def SK_openHelpDoc(project):
    mainPath = bodyrigpath+'document/'
    if 'face' == project:
        mel.eval("system(\"load"+mainPath+project+"\")")
    
    if 'body' == project:
        mel.eval("system(\"load"+mainPath+project+"\")")
    
    if 'WXTV' == project:
        mel.eval("system(\"load"+mainPath+project+"\")")
    
    if 'RR' == project:
        mel.eval("system(\"load"+mainPath+project+"\")")

    if  'influenceFace' == project:
        mel.eval("system(\"load"+mainPath+project+"\")")

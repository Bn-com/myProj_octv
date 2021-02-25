#-*- coding: utf-8 -*-
###########################################
import os
import shutil
import maya.cmds as mc
import maya.mel as mm
def wwBatchFileModify(type):
    sourcePath = mc.textFieldButtonGrp('sfb',q=1,text=1)
    targetPath = mc.textFieldButtonGrp('ofb',q=1,text=1)
    faildPath =  mc.textFieldButtonGrp('lfb',q=1,text=1)
    scriptPath=  mc.textFieldButtonGrp('scb',q=1,text=1)
    pathList = os.listdir(sourcePath)
    print pathList
    if(os.path.isdir(targetPath)):
        shutil.rmtree(targetPath)
    os.mkdir(targetPath)
    if(os.path.isdir(faildPath)):
        shutil.rmtree(faildPath)
    os.mkdir(faildPath)
    failedFile=[]
    mc.file(f=1,new=1)
    for fin in pathList:
        #fin=pathList[0]
        refin = fin
        mc.file(sourcePath+'/'+fin,o=1,type=type)
        try:
            execfile(scriptPath)
            print '%s-----------------------succeed' % fin
        except:
            failedFile.append(targetPath+'\\'+refin)
            shutil.copy2(sourcePath+'/'+fin,faildPath+'/'+fin)
            print '%s-----------------------failded' % fin
        mc.file(rename = targetPath+'/'+refin)
        mc.file(save = True,type =type)
    for remove in failedFile:
        #remove='E:\\test\\script\\op\\d.mb'
        os.remove(remove)
    print 'failed file : %d' % len(failedFile)
    for remove in failedFile:
        print remove
def ww_okPath():
    okPath=mm.eval('idmtFolderDialog;')
    mc.textFieldButtonGrp('ofb',edit=1,text=okPath)
    print okPath
def ww_lostPath():
    lostPath=mm.eval('idmtFolderDialog;')
    mc.textFieldButtonGrp('lfb',edit=1,text=lostPath)
    print lostPath
def ww_sourcePath():
    sourcePath=mm.eval('idmtFolderDialog;')
    mc.textFieldButtonGrp('sfb',edit=1,text=sourcePath)
    print sourcePath
def ww_scriptPath():
    scriptPaths=mm.eval('idmtFileDialog;')
    scriptPath=scriptPaths[0]
    mc.textFieldButtonGrp('scb',edit=1,text=scriptPath)
    print scriptPath

def wwStartButtonCmd():
    mayaFileType=''
    if (mc.optionMenu('mayaTypeButton',q=1,sl=1)==1):
        mayaFileType='mayaBinary'
    if (mc.optionMenu('mayaTypeButton',q=1,sl=1)==2):
        mayaFileType='mayaAscii'
    print mayaFileType
    wwBatchFileModify(mayaFileType)

def wwBfmUI():
    if(mc.window('wwBfm',ex=1)):
        mc.deleteUI('wwBfm')
    window=mc.window('wwBfm',title="BFMUI",widthHeight=(520,200),sizeable=0)
    mc.columnLayout('wwbfmcl',adj=1)
    mc.separator(style='doubleDash',h=8)
    mc.separator(style='none',h=5)
    mc.textFieldButtonGrp('sfb',label='sourceFilePath', text='sourceFilePath', buttonLabel='selectPath',bc=ww_sourcePath)  
    mc.separator(style='none',h=10)
    mc.textFieldButtonGrp('ofb',label='okFilePath', text='okFilePath', buttonLabel='selectPath',bc=ww_okPath)
    mc.separator(style='none',h=10)
    mc.textFieldButtonGrp('lfb',label='lostFilePath', text='lostFilePath', buttonLabel='selectPath',bc=ww_lostPath)  
    mc.separator(style='none',h=10)
    mc.textFieldButtonGrp('scb',label='useScript', text='select a script', buttonLabel='select a script',bc=ww_scriptPath)  
    mc.separator(style='none',h=10)
    mc.optionMenu('mayaTypeButton',label='openSaveMayaType',w=100)
    mc.menuItem( label='mayaBinary')
    mc.menuItem( label='mayaAscii')
    mc.separator(style='none',h=10)
    mc.button('wwStartButton',label='start',bgc=(0.3,0.5,0.3),w=150,al="center",c='wwStartButtonCmd()')
    mc.separator(style='none',h=8)
    mc.separator(style='doubleDash')
    mc.window(window,e=1,wh=(520,200))
    mc.showWindow(window)
wwBfmUI()
#################################THE END#######################################
##reverse frameId
import os
import maya.mel as mm
import maya.cmds as mc
import shutil as sh
def mk_reverseFrameId():
    sourcePath=mc.textFieldButtonGrp('sfb',q=1,text=1);
    print sourcePath
    modifyPath=mc.textFieldButtonGrp('mfb',q=1,text=1);
    print modifyPath
    padding=mc.intFieldGrp('padding',q=1,v=1)
    padding=int(padding[0])
    print padding
    allFrame=os.listdir(sourcePath)
    fileNum=len(allFrame)
    endFrameAdd=fileNum-1
    splitTempa=allFrame[0].split('.')
    starFrame=splitTempa[1]
    starFrame=int(starFrame)
    endFrame=starFrame+endFrameAdd
    for one in allFrame:
        #one=allFrame[0]
        splitOne=one.split('.')
        name=splitOne[0]
        frameId=splitOne[1]
        frameId=int(frameId)
        imageEX=splitOne[2]
        reverseId=starFrame-(frameId-endFrame)
        reverseId=str(reverseId)
        realPadding=len(reverseId)
        zeroAddNum=padding-realPadding
        zeroAdd='0'*zeroAddNum
        reverseFullName=name+'.'+zeroAdd+reverseId+'.'+imageEX        
        sh.copy2(sourcePath+'\\'+one,modifyPath+'\\'+reverseFullName)
    print 'done'
    return 0

def mk_sourcePath():
    sourcePath=mm.eval('idmtFolderDialog;')
    mc.textFieldButtonGrp('sfb',edit=1,text=sourcePath)
    print sourcePath
def mk_modifyPath():
    modifyPath=mm.eval('idmtFolderDialog;')
    mc.textFieldButtonGrp('mfb',edit=1,text=modifyPath)
    print modifyPath

def reverseFrameIdUI():
    if(mc.window('mkRVF',ex=1)):
        mc.deleteUI('mkRVF')
    window=mc.window('mkRVF',title="mkRVF",widthHeight=(520,170),sizeable=0)
    mc.columnLayout('mkRVFcl',adj=1)
    mc.columnLayout('mkRVFcl',adj=1)
    mc.separator(style='doubleDash',h=8)
    mc.text(label="only use for \"imageName.####.exe.\"")
    mc.intFieldGrp('padding',numberOfFields=1,label='padding',value1=4)
    mc.textFieldButtonGrp('sfb',label='sourceFilePath', text='sourceFilePath', buttonLabel='selectPath',bc=mk_sourcePath)  
    mc.separator(style='none',h=10)
    mc.textFieldButtonGrp('mfb',label='modifyPath', text='modifyPath', buttonLabel='selectPath',bc=mk_modifyPath)
    mc.separator(style='none',h=10)
    mc.button('mkStartButton',label='start',bgc=(0.3,0.5,0.3),w=150,al="center",c='mk_reverseFrameId()')
    mc.separator(style='doubleDash',h=8)
    mc.window(window,e=1,wh=(520,170))
    mc.showWindow(window)
reverseFrameIdUI()



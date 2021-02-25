# -*- coding: gbk -*-
import maya.cmds as cmd
import maya.mel as mel
import os, time, shutil, re

def ysScaleAlphaGainUI():
    window = cmd.window(title='setDispalcement', widthHeight=(200, 55))
    cmd.columnLayout(adjustableColumn=True)
    cmd.text(label=u'输出局部置换强度')
    factor = cmd.floatField(value=0.5, precision=2, height=20)
    cmd.button(label=u'应用局部置换强度', height=50, width=200, command=('import idmt.maya.ROMA.ysSetDisplacementShdr as ysDS\nreload(ysDS)\nysDS.setAlphaGain()'))
    cmd.button(label=u'输出场景贴图参数', height=50, width=200, command=('import idmt.maya.ROMA.ysSetDisplacementShdr as ysDS\nreload(ysDS)\nysDS.ysWriteDownTexParams()'))
    cmd.button(label=u'获取场景贴图参数', height=50, width=200, command=('import idmt.maya.ROMA.ysSetDisplacementShdr as ysDS\nreload(ysDS)\nysDS.ysGetTexParms()'))
    cmd.separator()
    cmd.separator()
    cmd.text(label=u'设置整体置换强度')
    allFactor = cmd.floatField(value=0.00, precision=2, height=20)
    cmd.button(label=u'应用整体置换强度', height=50, width=200, command=('import idmt.maya.ROMA.ysSetDisplacementShdr as ysDS\nreload(ysDS)\nysDS.ysSetAllAlphaGain()'))
    cmd.button(label='Close', height=50, width=200,  command=('cmd.deleteUI(\"'+window+'\", window=True)'))
    cmd.setParent('..')
    cmd.showWindow(window)
    cmd.optionVar(sv=('dipalcementFactorField', factor))
    cmd.optionVar(sv=('allDisplacementFactor', allFactor))

def setAlphaGain():
    '''Reduce the alpha gain value of selected displacement map'''
    
    # Get scale factor
    field = cmd.optionVar(q='dipalcementFactorField')
    factor = cmd.floatField(field, q=True, value=1)
    
    disShdrs = [item for item in cmd.ls(sl=True) if cmd.nodeType(item)=='displacementShader']
    for item in disShdrs:
        tex = cmd.listConnections(item+'.displacement', plugs=True)
        if re.search('outAlpha', tex[0]):
            tex = tex[0].split('.')
            cmd.setAttr(tex[0]+'.alphaGain', factor)
        if re.search('outColorR', tex[0]):
            tex = tex[0].split('.')
            colorGain = cmd.getAttr(tex[0]+'.colorGain')[0]
            cmd.setAttr(tex[0]+'.colorGain', factor,factor,factor,\
                        type='double3')    
    print u'置换参数修改完成！'
    
    
def ysWriteDownTexParams():
    # Define the file name
    filename = cmd.file(query=True, shn=1, sn=1)
    filename = filename.split('_')
    filename = 'sq'+filename[1]+'_'+'sc'+filename[2]+'.txt'
    path = r'//File-cluster/GDC/Projects/WinxClubII/WinxClubII_Scratch/rendering/FlyingShip/'
    
    # Check directory an text file. If it exists make it backup
    if os.path.exists(path+'bak') == False:
        os.mkdir(path+'bak')
    
    if os.path.isfile(path+filename) == True:
        confirm = cmd.confirmDialog(title='confirmDialog', message=u'文件已存在，是否覆盖？', button=['Yes', 'No'],\
                                    defaultButton='No', cancelButton='No', dismissString='No')
        if confirm == 'No':
            return
        if confirm == 'Yes':
            currTime = ''
            getTime = time.localtime() 
            for i in range(0, 5):
                currTime = currTime.__add__(str(getTime[i]))+'.' 
            bakName = filename[:-3]+currTime+'.txt'
            os.rename(path+filename, path+bakName)  
            shutil.move(path+bakName, path+'bak/'+bakName)    
        
    # Write all textures and ramps' parameters in a text file
    outText = []
    alphaGains = []
    colorGains = []
    outrepeatUVs = []
    place2Ds = cmd.ls(type='place2dTexture')
    files = cmd.ls(type='file')
    ramp = cmd.ls(type='ramp')
    files.extend(ramp)
    
    # Record parameters of file and ramp
    for file in files:
        alphaGain = cmd.getAttr(file+'.alphaGain')
        alphaGains.append(alphaGain)
        colorGain = cmd.getAttr(file+'.colorGain')
        colorGains.append(colorGain[0])
                                  
    outTextFile = open(path+filename, 'w')     
    
    for i in range(len(files)):
        outTextFile.write(files[i]+'\n')
        outTextFile.write(str(alphaGains[i])+'\n')
        outTextFile.write(str(colorGains[i])+'\n')
   
    # List separator
    outTextFile.write('#'*40+'\n')
   
    # Record parameters of place2d
    for item in place2Ds:
        outrepeatUV = cmd.getAttr(item+'.repeatUV')
        outTextFile.write(item+'\n')
        outTextFile.write(str(outrepeatUV[0])+'\n')    
    
    outTextFile.close()   
    print u'贴图参数输出完成！'

def ysGetTexParms():
    filename = cmd.file(query=True, shn=1, sn=1)
    filename = filename.split('_')
    filename = 'sq'+filename[1]+'_'+'sc'+filename[2]+'.txt'
    path = r'//File-cluster/GDC/Projects/WinxClubII/WinxClubII_Scratch/rendering/FlyingShip/'
    
    if os.path.isfile(path+filename) == False:
        cmd.confirmDialog(title='confirmDialog', message=u'没有对应的文件', button='OK')
        return
    
    # Read the text file and separate it in two part
    inputText = open(path+filename, 'r').read()
    lines = inputText.split('#'*40)
    fileLines = lines[0].split('\n')[:-1]
    place2dLines = lines[1].split('\n')[1:-1]
    
    # Apply the values from text file
    for i in range(0, len(fileLines), 3):
        # Convert each line to right data type          
        textureName = fileLines[i]
        alphaGain = float(fileLines[i+1])
        colorGain = fileLines[i+2][1:-1] 
        colorGain = colorGain.split(',')
        colorGain = float(colorGain[0]), float(colorGain[1]), float(colorGain[2])
        cmd.select(textureName)
        cmd.setAttr(textureName+'.alphaGain', alphaGain)
        cmd.setAttr(textureName+'.colorGain', colorGain[0],colorGain[1],colorGain[2], type='double3')
      
    for i in range(0, len(place2dLines), 2):
        # Convert each line to right data type     
        place2dName = place2dLines[i]
        repeatUV = place2dLines[i+1][1:-1]
        repeatUV = repeatUV.split(',')
        repeatUV = float(repeatUV[0]), float(repeatUV[1])        
        cmd.select(place2dName)
        cmd.setAttr(place2dName+'.repeatU', repeatUV[0])
        cmd.setAttr(place2dName+'.repeatV', repeatUV[1])
        
    print u'贴图参数修改完成！'

def ysSetAllAlphaGain():
    # Get scale factor
    field4all = cmd.optionVar(q='allDisplacementFactor')
    allFactor = cmd.floatField(field4all, q=True, value=1)  
    
    disShdrs = cmd.ls(type='displacementShader')
    if len(disShdrs) == 0:
        print u'场景中没有使用置换'
        return
    for item in disShdrs:
        tex = cmd.listConnections(item+'.displacement', plugs=True)
        if re.search('outAlpha', tex[0]):
            tex = tex[0].split('.')
            cmd.setAttr(tex[0]+'.alphaGain', allFactor)
        if re.search('outColorR', tex[0]):
            tex = tex[0].split('.')
            colorGain = cmd.getAttr(tex[0]+'.colorGain')[0]
            cmd.setAttr(tex[0]+'.colorGain', allFactor,allFactor,allFactor,\
                        type='double3')    
    print u'置换参数修改完成！'
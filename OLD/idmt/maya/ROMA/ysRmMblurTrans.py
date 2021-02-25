# -*- coding: gbk -*-
import maya.cmds as cmd
import maya.mel as mel
import re, shutil, os, sys

def separateShdingEngine():
    # list all shaders in current scene except default shaders
    allshaders = [item for item in cmd.ls(mat=True)\
                  if item != 'lambert1' and\
                  item != 'particleCloud1' and\
                  item != 'shaderGlow1'\
                  if cmd.objExists(item+'.transparency')] 
       
    for item in allshaders:
        lostSG = cmd.listConnections(item+'.outColor', s=0, d=1, type='shadingEngine')
        if lostSG == None:
            print item
            allshaders.remove(item)
                            
    noTransSG = [] 
    transMap = []
    transSG = []
    for item in allshaders:
        map = cmd.listConnections(item+'.transparency', s=1, d=0)
        # list all Shading Engine which will be using normal MV shader
        if map == None:
            try:
                SG = cmd.listConnections(item+'.outColor', s=0, d=1, type='shadingEngine')
                noTransSG.extend(SG)
            except:
                pass
        
        # list all Shading Engine that will be connected by transMV shader
        if map != None:
            SG = cmd.listConnections(item+'.outColor', s=0, d=1, type='shadingEngine')
            transSG.extend(SG)
            transMap.extend(map)
        
    # Check total numbers of SG and material 
    sg = noTransSG + transSG  
    for ss in sg:
        if cmd.listConnections(ss+'.surfaceShader', s=1, d=0) == None:
            print ss
            sg.remove(ss)
    
    print len(allshaders)
    print len(sg)   
    
    if len(sg) != len(allshaders):
        cmd.confirmDialog(title='Confirm Shader and SG', message=u'请清理场景中多余的材质球！\n请渲染后检查错误',\
                          button='OK', defaultButton='OK')
        pass        
        
    if len(transMap) != len(transSG):
        cmd.confirmDialog(title='Confirm number of SG', message=u'有多余的SG节点！',\
                          button='OK', defaultButton='OK')
        return
    
    labeledList = {'noTransSG':noTransSG, 'transMap':transMap, 'transSG':transSG}
    return labeledList

def yscopyLocalTex2Network():
    '''copy local texture to network folder, if texture's path is not correct'''
    subDirectory = ''
    hostName = os.getenv('COMPUTERNAME')
    name = re.compile('\d$')
    nameMatch = re.search(name, hostName)
    if nameMatch.group() in ('13579'):
        subDirectory = 'Maya_Odd'
    if nameMatch.group() in ('02468'):
        subDirectory = 'Maya_Even'        
    netPath = r'//File-cluster/GDC/Netrender/%s/%s/sourceimages/' % (subDirectory, hostName)

    pattern = re.compile('^\${MC_winxII}', re.IGNORECASE)      
    files = cmd.ls(type='file')
    if files != None:
        for file in files:
            texPath = cmd.getAttr(file+'.fileTextureName')
            if pattern.search(texPath) == None:
                fileName = re.split('/', texPath)
                fileName = fileName.pop()
                newPath = netPath+fileName
                shutil.copy(texPath, newPath)
                cmd.setAttr(file+'.fileTextureName', newPath, type='string')      
    
def assignMVshaderOnNonTransObj():      
    
    confrim = cmd.confirmDialog(title='ConfirmBox', message=u'确定制作mblur文件吗？',\
                                button=('Yes', 'No'), defaultButton='No', dismissString='No',\
                                cancelButton='No')
    if confrim == 'No':
        return
    
    yscopyLocalTex2Network()
    sgdict = separateShdingEngine()
    transMap = sgdict['transMap']
    transSG = sgdict['transSG']
    noTransSG = sgdict['noTransSG']
    mel.eval('source "//file-cluster/GDC/Resource/Support/AnimalLogic/mayaman2.0.7/mel/AEMayaManCustomShaderTemplate.mel"')
    mel.eval('source "D:/Alias/MAYA8.5/2013/others/showEditor.mel"')
    
    mmMVshdrNoTrans = cmd.shadingNode('MayaManCustomShader', asShader=1, name='mvNoTrans')
    mel.eval('AEMayaManCustomShaderBrowseFile ("'+mmMVshdrNoTrans+'"+".ShaderFile")\
    "//file-cluster/GDC/Resource/Support/Pixar/Shader/RBW_MotionVector.slo" "RenderMan Shader"')
    mmMVshdrNoTrans = cmd.rename('RBW_MotionVector', 'mvNoTrans')
    
    for sg in noTransSG:
        cmd.connectAttr(mmMVshdrNoTrans+'.outColor', sg+'.surfaceShader', force=True)
    
    if len(transSG) !=0 and len(transMap) !=0:
        for i in range(len(transSG)):
            # Building Shading network
            mmMVshdrTrans = cmd.shadingNode('MayaManCustomShader', asShader=1, name='mvTrans')
            mel.eval('AEMayaManCustomShaderBrowseFile ("'+mmMVshdrTrans+'"+".ShaderFile")\
                     "//file-cluster/GDC/Resource/Support/Pixar/Shader/RBW_MotionVectorTrans.slo" "RenderMan Shader"')
            mmMVshdrTrans = cmd.rename('RBW_MotionVectorTrans', 'mvTrans')
            mel.eval('showEditor "'+mmMVshdrTrans+'"')
            mel.eval('callCSUpdateCustomShader "'+mmMVshdrTrans+'" ("'+mmMVshdrTrans+'"+".ShaderFile")')
            cmd.setAttr(mmMVshdrTrans+'.convertTransparencyMap', 1)
            
            # Assign transMV shader to SG node
            if cmd.nodeType(transMap[i]) == 'file':
                # Change texture's path into absolute path
                tex = cmd.getAttr(transMap[i]+'.fileTextureName')
                tex = tex.replace('${MC_winxII}', '//Serverone/CONTENT_4_GLOBAL/PRJ_winxII/MC_winxII')
                cmd.setAttr(mmMVshdrTrans+'.transparencyMap', tex, type='string')
                cmd.connectAttr(mmMVshdrTrans+'.outColor', transSG[i]+'.surfaceShader', force=True)
            
            # Assign noTransMV shader to normal objects    
            if cmd.nodeType(transMap[i]) != 'file':       
                cmd.connectAttr(mmMVshdrNoTrans+'.outColor', transSG[i]+'.surfaceShader', force=True)
        
            # Connect noTransMV shader on wingSG
            if re.search('wingSG', transSG[i]) != None:
                cmd.connectAttr(mmMVshdrNoTrans+'.outColor', transSG[i]+'.surfaceShader', force=True)          

    # Clean up unused MayaManCustomShader
    mmshdr = cmd.ls(type='MayaManCustomShader')
    for item in mmshdr:
        if cmd.listConnections(item+'.outColor', s=0, d=1) == None:
            cmd.delete(item)
    
    print u'mblur文件制作完成'
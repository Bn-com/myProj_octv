# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel

def nj_TexturePath_change(path):
    from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
    reload(sk_infoConfig)
    #path = 'E:/Scripts/Ninjago2015/Nuke/test.nk'
    readInfos = sk_infoConfig.sk_infoConfig().checkFileRead(path)
    import os
    if not os.path.exists(path):
        return 0
    
    needIndexs = []
    for i in range(len(readInfos)):  
        if 'Read {' in readInfos[i]:
            needIndexs.append(i) 
    
    if not needIndexs:
        return 0
    
    for j in needIndexs:
        for k in range(j,j+10):
            checkState = 0
            if 'file' in readInfos[k]:
                newLineInfo = readInfos[k].replace('Z:/Projects/Ninjago/Ninjago_scratch/lighting&compositing/masterlighting','Z:/Resource/Library/Reference/MasterLighting/Ninjago/season_2')
                readInfos[k] = newLineInfo
                checkState = 1
            if checkState:
                break
    
    sk_infoConfig.sk_infoConfig().checkFileWrite( path, readInfos, addtion = 0)

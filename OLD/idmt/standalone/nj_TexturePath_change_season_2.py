# -*- coding: utf-8 -*-
#import maya.cmds as mc
#import maya.mel as mel
import sys

def checkFileRead(path):
    import os 
    if not os.path.exists(path):
        print path
        print u'Error:    file do not exist'
        #mc.error(u'Error:    file do not exist')
    txt = open(path, 'r');
    try:
        fileContent = txt.readlines()
        print('Loading........')
    finally:
        #print path
        txt.close()
    result = []
    for info in fileContent:
        if '\r\n' in info:
            result.append(info.split('\r\n')[0])
        else:
            result.append(info)
    return result

#写文件================
def checkFileWrite(path , info , addtion=0):
    if addtion == 1:
        info = self.checkFileRead(path) + info
    txt = open(path, 'w')
    try:
        txt.writelines(str(a) + '\r\n' for a in info)
        print('Writing........')
    finally:
        txt.close()

def nj_TexturePath_change(path):
    #from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
    #reload(sk_infoConfig)
    #path = 'E:/Scripts/Ninjago2015/Nuke/test.nk'
    #readInfos = sk_infoConfig.sk_infoConfig().checkFileRead(path)
    readInfos = checkFileRead(path)
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
    
    #sk_infoConfig.sk_infoConfig().checkFileWrite( path, readInfos, addtion = 0)
    checkFileWrite( path, readInfos, addtion = 0)



path = sys.argv[1]
nj_TexturePath_change(path)
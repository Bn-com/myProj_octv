__author__ = 'xuweijian'
import os
import maya.cmds as mc
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig


def do5geocache():
    sceneName=mc.file(q=1,sn=1,shn=1)
    targetPath='D:/transFiles'
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    reload(sk_infoConfig)
    shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
    cacheNode=mc.ls(type='cacheFile')
    for one in cacheNode:
        cachePath='Z:/Projects/DiveollyDive5/project/data/GeoCache/%s/%s/'%(shotInfos[1],shotInfos[2])
        if os.path.exists(cachePath):
            mc.setAttr('%s.cachePath'%one,cachePath,type='string')
        else:
            mc.error('%s node cache:%s not exists'%(one,cachePath))
    mc.file(rn='%s/%s'%(targetPath,sceneName))
    mc.file(f=1,save=1)

    #mc.file('%s/%s'%(targetPath,sceneName),f=1,options='v=0',typ='mayaAscii',pr=1,es=1)

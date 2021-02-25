# -*- coding: utf-8 -*-

'''
Created on 2017

@author: hanhong
'''
import maya.cmds as mc
import maya.mel as mel
import re
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
import os
class GA_Tools(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    #【GA】工具集
    #@author: hanhong
    #Data：2017/6/9
    def GA_unknownPluginDel(self,open=1,fileType='mayaBinary'):
    #删除无用插件（黄仲维）
        import idmt.maya.unknownPlugin
        fileName=mc.file(q=1,sn=1)
        fileShort=mc.file(q=1,sn=1,shn=1)
        temppath='D:/TempInfo/unknownPlugin/'
        temppath01='D:/TempInfo/'
        mc.sysFile(temppath, makeDir=True)
        mc.sysFile(temppath01, makeDir=True)
        mc.file(rename=temppath01+fileShort)
        mc.file(save=1, force=1)
        if fileType=='mayaBinary':
            idmt.maya.unknownPlugin.RemoveUnknownPluginMb(temppath01+fileShort,temppath+fileShort)
        else:
            idmt.maya.unknownPlugin.RemoveUnknownPluginMa(temppath01+fileShort,temppath+fileShort)
        if open==1:
            mc.file((temppath+fileShort),options='v=0',type=fileType,f=1,o=1)
        result=temppath+fileShort
        return result


# -*- coding: utf-8 -*-
'''
Created on 2014-8-18

@author: liangyu
'''

import maya.cmds as mc


def cl_texureQuadratic():
    
    fileNodes = mc.ls(type='file')    
    for node in fileNodes:
        path = mc.getAttr(node + '.fileTextureName')
        formatNow = mc.getAttr(node + '.fileTextureName').split('.')[-1]
        if formatNow.lower() == 'map':
            mc.setAttr((node + '.filterType'), 3)
            
    from idmt.maya.py_common import sk_infoConfig
    reload(sk_infoConfig)
    shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
    pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
    fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]+ '_' + shotInfo[4]+ '_' + shotInfo[5]
    mc.file(rename=fileName)
    mc.file(save=1)
            
            

            
def cl_texureoff():
    
    fileNodes = mc.ls(type='file')    
    for node in fileNodes:
        path = mc.getAttr(node + '.fileTextureName')
        formatNow = mc.getAttr(node + '.fileTextureName').split('.')[-1]
        if formatNow.lower() == 'map':
            mc.setAttr((node + '.filterType'), 0)   
    
    from idmt.maya.py_common import sk_infoConfig
    reload(sk_infoConfig)
    shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
    pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
    fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]+ '_' + shotInfo[3] + '_' + shotInfo[4]+ '_' + shotInfo[5]
    mc.file(rename=fileName)
    mc.file(save=1)         
            
            
            
         

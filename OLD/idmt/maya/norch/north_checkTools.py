# -*- coding: utf-8 -*-

'''
Created on 2015

@author: liangyu
'''

import maya.cmds as mc
import maya.mel as mel

class ly_checkTools(object):
    def __init__(self):
        pass

    def ly_TXRIGCheckTools(self):        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_backCmd
        reload(sk_backCmd)
                
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()                        
        if shotInfo[0]=='ice':
            if (shotInfo[1][0] == 'C' or 'c') or (shotInfo[1][0] == 'P' or 'p'):
                sk_backCmd.sk_backCmd().checkAssetAnim2RenderCheckInConfig()
                
                
    def ly_AnCheckTools(self):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.ShunLiu import sk_ProjectTools_ShunLiu
        reload(sk_ProjectTools_ShunLiu)
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.norch import North_Ankey
        reload(North_Ankey)
                
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        if shotInfo[0]=='ice':
            if shotInfo[3]=='an':
                sk_ProjectTools_ShunLiu.sk_ProjectTools_ShunLiu().csl_rebuildClean()
                sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate()
                sk_sceneTools.sk_sceneTools().LY_CameraABC()
                North_Ankey.north_anKEY()
                North_Ankey.north_anRender()
                
        
    def ly_check(self):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)          
        from idmt.maya.norch import north_checkCommon
        reload(north_checkCommon)
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfo[0]=='ice':
            if (shotInfo[1][0] == 'C' or 'c') or (shotInfo[1][0] == 'P' or 'p'):               
                if shotInfo[3].split('.')[0] in ['rg', 'tx']:
                    north_checkCommon.sk_checkTools().ly_checkBASE()
                    self.ly_TXRIGCheckTools()
                
        if shotInfo[0]=='ice':
            if shotInfo[3]=='an':
                self.ly_AnCheckTools()
                               
             
        
        
        
        
        
        
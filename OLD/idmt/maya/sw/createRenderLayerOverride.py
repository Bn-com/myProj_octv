#
# Copyright (c) 2014 Bigbigsun Software Inc.
# ----------------------------------------------------
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided 'AS IS' and subject to the Bigbigsun programming
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Bigbigsun Source Code License. All rights
# not expressly granted therein are reserved by Bigbigsun Software Inc.
#
# Author:      Rongjie
# Email:       Rongjie@bigbigsun.com
# DateTime:    [16:20:57 2017-07-10]
# Description: Create RenderLayer Override
#

import maya.cmds as cmds

def overrideEnv_On():
    cmds.editRenderLayerAdjustment("redshiftOptions.environment")
    cmds.text('env',e=True,l="<font color=#e56b2e><strong><font size=4>{0}</font>".format('Environment:'))    

def overrideEnv_Off():
    cmds.editRenderLayerAdjustment("redshiftOptions.environment",remove=True)
    cmds.text('env',e=True,l="<font color=#F0F0F0><font size=4>{0}</font>".format('Environment:')) 

def overrideAtomsphere_On():
    cmds.editRenderLayerAdjustment("redshiftOptions.atmosphere")
    cmds.text('atm',e=True,l="<font color=#e56b2e><strong><font size=4>{0}</font>".format('Atmosphere:'))

def overrideAtomsphere_Off():
    cmds.editRenderLayerAdjustment("redshiftOptions.atmosphere",remove=True)
    cmds.text('atm',e=True,l="<font color=#F0F0F0><font size=4>{0}</font>".format('Environment:')) 

def overrideExposure_On():
    cmds.editRenderLayerAdjustment("redshiftOptions.exposure")
    cmds.text('exp',e=True,l="<font color=#e56b2e><strong><font size=4>{0}</font>".format('Photographic Exposure:'))

def overrideExposure_Off():
    cmds.editRenderLayerAdjustment("redshiftOptions.exposure",remove=True)
    cmds.text('exp',e=True,l="<font color=#F0F0F0><font size=4>{0}</font>".format('Environment:')) 

def judgeStatus_env():
    adAttrLists = cmds.editRenderLayerAdjustment(q=True)
    if adAttrLists:
        if 'redshiftOptions.environment' in adAttrLists:
            envStr = '<font color=#e56b2e><strong>'
        else:
            envStr = '<font color=#F0F0F0>'
    else:
        envStr = '<font color=#F0F0F0>'
    return envStr

def judgeStatus_atm():
    adAttrLists = cmds.editRenderLayerAdjustment(q=True)
    if adAttrLists:
        if 'redshiftOptions.atmosphere' in adAttrLists:
            atmStr = '<font color=#e56b2e><strong>'
        else:
            atmStr = '<font color=#F0F0F0>'
    else:
        atmStr = '<font color=#F0F0F0>'
    return atmStr

def judgeStatus_exp():
    adAttrLists = cmds.editRenderLayerAdjustment(q=True)
    if adAttrLists:
        if 'redshiftOptions.exposure' in adAttrLists:
            expStr = '<font color=#e56b2e><strong>'
        else:
            expStr = '<font color=#F0F0F0>'
    else:
        expStr = '<font color=#F0F0F0>'
    return expStr


def UI(envStr,atmStr,expStr):
    if cmds.window('CreateLayerOverride',exists=True):
        cmds.deleteUI('CreateLayerOverride')
        
    if cmds.windowPref('CreateLayerOverride',exists=True):
        cmds.windowPref('CreateLayerOverride',remove=True)
    
    window_width = 400
    window_height = 220
    window_UI = cmds.window('CreateLayerOverride',title = 'Create Layer Override',width = window_width,height = window_height,s=False)
    cmds.rowLayout(numberOfColumns=2)

    cmds.columnLayout()     
    cmds.scrollLayout(w=270,h=70)
    cmds.separator(h=10)
    cmds.text('env',l= envStr + "<font size=4>{0}</font>".format('Environment:'))
    cmds.separator(h=10)
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(w=20,style='none')
    cmds.button('env_on',label='ON',c = lambda *arge:overrideEnv_On(),width=80,height=25,bgc=[0.68,0.78,0.835],ebg=False)
    cmds.separator(w=10,style='none')
    cmds.button('env_off',label='OFF',c = lambda *arge:overrideEnv_Off(),width=80,height=25,bgc=[0.68,0.78,0.835],ebg=False)
    cmds.setParent('..')
    cmds.setParent('..')
    
    cmds.scrollLayout(w=270,h=70)
    cmds.separator(h=10)
    cmds.text('atm',l= atmStr + "<font size=4>{0}</font>".format('Atmosphere:'))
    cmds.separator(h=10)
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(w=20,style='none')
    cmds.button('env_on',label='ON',c = lambda *arge:overrideAtomsphere_On(),width=80,height=25,bgc=[0.68,0.78,0.835],ebg=False)
    cmds.separator(w=10,style='none')
    cmds.button('env_off',label='OFF',c = lambda *arge:overrideAtomsphere_Off(),width=80,height=25,bgc=[0.68,0.78,0.835],ebg=False)
    cmds.setParent('..')
    cmds.setParent('..')
    
    cmds.scrollLayout(w=270,h=70)
    cmds.separator(h=10)
    cmds.text('exp',l= expStr + "<font size=4>{0}</font>".format('Photographic Exposure:'))
    cmds.separator(h=10)
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(w=20,style='none')
    cmds.button('env_on',label='ON',c = lambda *arge:overrideExposure_On(),width=80,height=25,bgc=[0.68,0.78,0.835],ebg=False)
    cmds.separator(w=10,style='none')
    cmds.button('env_off',label='OFF',c = lambda *arge:overrideExposure_Off(),width=80,height=25,bgc=[0.68,0.78,0.835],ebg=False)
    cmds.setParent('..')
    cmds.setParent('..')    
    cmds.setParent('..')
    
    cmds.columnLayout()
    cmds.text('',h=36)
    cmds.button('Refresh',label='Refresh',width=80,height=25,c = lambda *arge:UI(judgeStatus_env(),judgeStatus_atm(),judgeStatus_exp()),bgc=[0.9,0.85,0.3])
    cmds.setParent('..')
       
    cmds.setParent('..')
    cmds.showWindow(window_UI)

def showWindow():
    UI(judgeStatus_env(),judgeStatus_atm(),judgeStatus_exp())


if __name__ == "__main__":
    showWindow()

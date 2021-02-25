#
# Redshift Channel Box Control by DGDM
#
# 1. Copy rsCBC.py to your scripts folder
# 2. in ScriptEditor type and execute
#
#       import rsCBC
#       rsCBC.rsChannelBoxControl()
#
# 3. Select Object(s) and press Hide / Show
#
# http://www.store.cgfront.com
#

import maya.cmds as cmds

def rsChannelBoxControl():
    if cmds.window('rsChannelBoxControlWin', q=1, ex=1):
        cmds.deleteUI('rsChannelBoxControlWin')
    cmds.window('rsChannelBoxControlWin', title="Redshift Channel Box Control", iconName='Short Name', w=150, h=70, s=1 )

    cmds.columnLayout('rsCBCLayout', adj=1, w=250, h=150, p='rsChannelBoxControlWin', bgc=[0.31, 0.31, 0.31])
    cmds.text(l='Redshift Channel Box Control', h=70, p='rsCBCLayout')
    cmds.button(l='Hide All', w=250, c=lambda *args: rsSwitch('0'), bgc=[0,0.75,0.99], p='rsCBCLayout')
    cmds.text(h=5, l='', p='rsCBCLayout')
    cmds.button(l='Show All', w=250, c=lambda *args: rsSwitch('1'), bgc=[0,0.75,0.99], p='rsCBCLayout')
    cmds.text(h=5, l='', p='rsCBCLayout')
    cmds.button(l='Close', command="cmds.deleteUI('rsChannelBoxControlWin')", bgc=[0.25, 0.25, 0.25], p='rsCBCLayout', w=250)
    cmds.showWindow('rsChannelBoxControlWin')

    list = [".rsObjectId",
            ".rsEnableVisibilityOverrides",
            ".rsPrimaryRayVisible",
            ".rsSecondaryRayVisible",
            ".rsShadowCaster",
            ".rsShadowReceiver",
            ".rsReflectionCaster",
            ".rsReflectionVisible",
            ".rsRefractionCaster",
            ".rsRefractionVisible",
            ".rsGiCaster",
            ".rsGiVisible",
            ".rsCausticCaster",
            ".rsCausticVisible",
            ".rsFgCaster",
            ".rsFgVisible",
            ".rsSelfShadows",
            ".rsAOCaster",
            ".rsForceBruteForceGI",
            ".rsMatteEnable",
            ".rsMatteApplyToSecondaryRays",
            ".rsMatteShowBackground",
            ".rsMatteAffectedByMatteLights",
            ".rsMatteAlpha",
            ".rsMatteReflectionScale",
            ".rsMatteRefractionScale",
            ".rsMatteDiffuseScale",
            ".rsMatteShadowEnable",
            ".rsMatteShadowAffectsAlpha",
            ".rsMatteShadowTransparency",
            ".rsMatteShadowColor",
            ".rsMatteShadowColorR",
            ".rsMatteShadowColorG",
            ".rsMatteShadowColorB",
            ".rsEnableSubdivision",
            ".rsScreenSpaceAdaptive",
            ".rsDoSmoothSubdivision",
            ".rsMinTessellationLength",
            ".rsMaxTessellationSubdivs",
            ".rsOutOfFrustumTessellationFactor",
            ".rsSubdivisionRule",
            ".rsEnableDisplacement",
            ".rsMaxDisplacement",
            ".rsDisplacementScale",
            ".rsAutoBumpMap",
            ".rsCausticReceiver",
            ".rsGiReceiver"]

    def rsSwitch(x):
        sel = cmds.listRelatives(cmds.ls(sl=1), s=1)
        if sel != None:
            for s in sel:
                for e in list:
                    cmds.setAttr(s + e, k=int(x))
                    cmds.setAttr(s + e, cb=int(x))
        else:
            print 'Please select Object(s) first!',

import maya.cmds as cmds
def gdc_IDMT_BODYRIG_2009_removeMainWindow():
    if cmds.menu('GDC_BODYRIG_2009',exists=1):
        cmds.deleteUI('GDC_BODYRIG_2009')
gdc_IDMT_BODYRIG_2009_removeMainWindow()
import maya.cmds as cmds
import maya.mel as mel
execfile('Z:/Resource/Groups/Production/Modeling/Rigging 2009 Development Plan/BodyRiggingTools/script/RIG/IKFK.py')

def gdc_IDMT_BODYRIG_2009_addMainWindow():
    if cmds.menu('GDC_BODYRIG_2009',exists=1):
        cmds.deleteUI('GDC_BODYRIG_2009')
    cmds.menu('GDC_BODYRIG_2009',label='GDC_BODYRIG_2009',tearOff=1,parent='MayaWindow',allowOptionBoxes=1)
    cmds.menuItem('GDC_BODYRIG_2009_help',parent='GDC_BODYRIG_2009',label="HOW TO USE",tearOff=1,command='mel.eval(\"system(\\\"load Z:/Resource/Groups/Production/Modeling/Rigging 2009 Development Plan/document/body/IDMT_BODY_RIG_2009_HOW_TO_USE.docx\\\")\")')
    cmds.menuItem('GDC_BODYRIG_2009_IKFKSWITCH',parent='GDC_BODYRIG_2009',label="IKFK_SWITCH",tearOff=1,command='SK_IKFKSwitchCommand()')
    cmds.menuItem('GDC_BODYRIG_2009_BODYCTRL_EASYSELECT',parent='GDC_BODYRIG_2009',label="BODY_CTRL_selectUI",tearOff=1,command='execfile(\'//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_EasyCtrlPlaneUI_v1.01.py\')')
gdc_IDMT_BODYRIG_2009_addMainWindow()
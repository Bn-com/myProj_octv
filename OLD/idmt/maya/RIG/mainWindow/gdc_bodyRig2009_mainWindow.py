import maya.cmds as cmds
def gdc_bodyRig2009_mainWindow():
    beforeScriptText='if (`getenv \"OFFICE_LOCATION\"`==\"shenzhen\")\n{\nprint \"GDC_shenzhen\";\npython(\"execfile(\'\\file-cluster\GDC\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\RIG\mainWindow\gdc_IDMT_BODYRIG_2009_addMainWindow.py\')\");\n};'
    afterScriptText='if (`getenv \"OFFICE_LOCATION\"`==\"shenzhen\")\n{\nprint \"GDC_shenzhen\";\npython(\"execfile(\'\\file-cluster\GDC\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\RIG\mainWindow\gdc_IDMT_BODYRIG_2009_removeMainWindow.py\')\");\n};'
    if cmds.objExists('GDC_BODYRIG2009_SCRIPTNODE'):
        cmds.delete('GDC_BODYRIG2009_SCRIPTNODE')
    cmds.scriptNode(beforeScript=beforeScriptText,afterScript=afterScriptText,n='GDC_BODYRIG2009_SCRIPTNODE')
    cmds.setAttr('GDC_BODYRIG2009_SCRIPTNODE.scriptType',1)
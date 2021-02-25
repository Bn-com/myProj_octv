import maya.cmds as cmds
import maya.mel as mel
mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/mel/edo/general/poseReaderUI.mel"')
mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/mel/edo/general/poseDeformerUI.mel"')
def PSD_posedeformerUI():
    #edo_addRiggingEnviourmentPath()
    w=200
    h=100
    if cmds.window('PSD_posedeformerUI',ex=1):
        cmds.deleteUI('PSD_posedeformerUI')
    cmds.window('PSD_posedeformerUI')
    cmds.columnLayout('PSD_posedeformerUI_CL01',w=w,h=h,rs=10)
    cmds.button('PSD_posedeformerUI_CL01_BT01',l='poseReaderUI',ann="poseReaderUI",w=w,h=50,c='mel.eval("poseReaderUI()")')
    cmds.button('PSD_posedeformerUI_CL01_BT02',l='poseDeformerUI',ann="poseDeformerUI",w=w,h=50,c='mel.eval("poseDeformerUI()")')
    cmds.showWindow('PSD_posedeformerUI')
    cmds.window('PSD_posedeformerUI',e=1,w=w,h=h)
PSD_posedeformerUI()
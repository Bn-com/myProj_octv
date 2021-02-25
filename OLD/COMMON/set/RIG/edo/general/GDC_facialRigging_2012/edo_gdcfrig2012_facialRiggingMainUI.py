#-*- coding: utf-8 -*-
import maya.cmds as cmds
execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/GDC_facialRigging_2012/edo_gdcfrig2012_createFacialJoint.py')
execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/GDC_facialRigging_2012/edo_gdcfrig2012_createFacialRig.py')

def edo_gdcfrig2012_facialRiggingMainUI():
    if cmds.window('facialRiggingMainUI',q=1,ex=1):
        cmds.deleteUI('facialRiggingMainUI')
    cmds.window('facialRiggingMainUI')
    cmds.formLayout('facialRiggingMainUI_FL01',w=300,h=500)
    cmds.tabLayout('facialRiggingMainUI_TB01',innerMarginWidth=5, innerMarginHeight=5)
    cmds.columnLayout('facialRiggingMainUI_CL01',cw=300,rs=5,p='facialRiggingMainUI_TB01')
    cmds.button('facialRiggingMainUI_CL01_BT01',l='导入模板',w=300,p='facialRiggingMainUI_CL01',c='edo_gdcfrig2012_createFacialJoint(3,3,3,3,7)')
    cmds.intSliderGrp('facialRiggingMainUI_CL01_IFG01',field=True,label='嘴皮骨骼数',minValue=0, maxValue=5, fieldMinValue=0, fieldMaxValue=10, value=3,cw3=[80,60,130])
    cmds.intSliderGrp('facialRiggingMainUI_CL01_IFG02',field=True,label='眼皮骨骼数',minValue=0, maxValue=5, fieldMinValue=0, fieldMaxValue=10, value=3,cw3=[80,60,130])
    cmds.intSliderGrp('facialRiggingMainUI_CL01_IFG03',field=True,label='鼻子骨骼数',minValue=0, maxValue=10, fieldMinValue=0, fieldMaxValue=10, value=3,cw3=[80,60,130])
    cmds.intSliderGrp('facialRiggingMainUI_CL01_IFG04',field=True,label='耳朵骨骼数',minValue=0, maxValue=10, fieldMinValue=0, fieldMaxValue=10, value=3,cw3=[80,60,130])
    cmds.intSliderGrp('facialRiggingMainUI_CL01_IFG05',field=True,label='舌头骨骼数',minValue=0, maxValue=12, fieldMinValue=0, fieldMaxValue=12, value=7,cw3=[80,60,130])
    cmds.rowLayout('facialRiggingMainUI_CL01_RL01',numberOfColumns=2, columnWidth2=(150,150))
    cmds.button('facialRiggingMainUI_CL01_RL01_BT01',l='刷新模板',w=150,c='edo_gdcfrig2012_refreshFacialJointCmd()')
    cmds.button('facialRiggingMainUI_CL01_RL01_BT02',l='镜像模板',w=150,c='edo_gdcfrig2012_mirrorFacialJoint()')
    cmds.setParent('facialRiggingMainUI_CL01')
    cmds.button('facialRiggingMainUI_CL01_BT02',l='生成设置',w=300,h=40,c='edo_gdcfrig2012_createFacialRig()')
    cmds.tabLayout('facialRiggingMainUI_TB01',e=True,tabLabel=('facialRiggingMainUI_CL01','facialRig2012'))
    cmds.showWindow('facialRiggingMainUI')
    cmds.window('facialRiggingMainUI',e=1,w=300,h=500)

def edo_gdcfrig2012_refreshFacialJointCmd():
    lip=cmds.intSliderGrp('facialRiggingMainUI_CL01_IFG01',q=True,v=1)
    lid=cmds.intSliderGrp('facialRiggingMainUI_CL01_IFG02',q=True,v=1)
    nose=cmds.intSliderGrp('facialRiggingMainUI_CL01_IFG03',q=True,v=1)
    ear=cmds.intSliderGrp('facialRiggingMainUI_CL01_IFG04',q=True,v=1)
    tongue=cmds.intSliderGrp('facialRiggingMainUI_CL01_IFG05',q=True,v=1)
    edo_gdcfrig2012_refreshFacialJoint(1,lip,lid,nose,ear,tongue)

edo_gdcfrig2012_facialRiggingMainUI()
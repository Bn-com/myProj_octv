#-*- coding: utf-8 -*-
import maya.cmds as mc


def CJW_connectAttrTool():
    selectCtrls = mc.ls(sl=1)
    if len(selectCtrls)!=0:
        selectCtrl = selectCtrls[-1]
        try:
            mc.addAttr(selectCtrl,ln='MeshSelection',at='enum',en='Normal:Template:Reference:',dv=2)
        except:
            pass
        try:
            mc.setAttr(selectCtrl+'.MeshSelection',e=1,keyable=1)
        except:
            pass
        allMeshs = mc.listRelatives('MODEL',allDescendents=1,type='mesh')
        for Mesh in allMeshs:
            if Mesh.split('_')[-1]=='Shape':  
                Transform = mc.listRelatives(Mesh,parent = 1)[0]
                try:
                    mc.setAttr(Transform+'.overrideEnabled',1)
                    mc.connectAttr(selectCtrl+'.MeshSelection',Transform+'.overrideDisplayType')
                except:
                    pass    


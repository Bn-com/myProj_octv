__author__ = 'xuweijian'
import maya.cmds as mc
import maya.mel as mel

def reloadBrush():
    objs=mc.ls(type='stroke')
    objs=mc.listRelatives(objs,p=1)
    for obj in objs:
        brushNodes=mc.listHistory(obj)
        for one in brushNodes:
            if mc.nodeType(one)=='brush':
                PreName=obj.split(':')[1]
                mel.eval('applyPresetToNode "%s" "" "" "%s" 1;'%(one,PreName))
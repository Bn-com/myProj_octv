# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Ninjago: Anim Cheanup Scene
'''
__author__	= 'zhaozhongjie@idmt.com.cn'
__date__	= '2013-07-18'

import maya.cmds as cmds
import maya.mel as mel
import re
import idmt.maya.Pluto.util as pu
reload(pu)
#   打开所有参考
references = cmds.file(q=1, r=1)
for r in references:  
    refRN = cmds.file(r,q=1, rfn=1)
    if cmds.file(r,q=1,dr=1,):
        cmds.file(loadReference =refRN )

#   删除客户的参考
    if "Reference/Handout" in r:
        cmds.file(r , importReference=1)
        
#   删除显示层
disL = cmds.ls(type = 'displayLayer')
for d in disL:
    low =d.lower()
    if 'defaultLayer' in d:
        continue
    elif not( 'no' in low and 'render' in low):
        try:
            pu.disconnectAttr(d)
            cmds.delete(d)
        except:
            pass

#   bake摄像机    
fileName = str(cmds.file(q=1 , sn =1 ,shn =1))
fileName_split = fileName.split("_")
camName = 'Cam_' + fileName_split[1] + '_' +fileName_split[2] + '_' +fileName_split[3]    
if cmds.objExists(camName):
    cams = cmds.ls(camName)
    cmds.select(cams[0])
    mel.eval('source "zwCameraImportExport.mel"; zwBakeCamera;')

#   删除多余的组        
for a in cmds.ls(assemblies =1):
#   如果是locator，则跳过    
    child = cmds.listRelatives(a,children=1,fullPath=1)
    if child:
        if cmds.objectType(child[0]) == 'locator' or cmds.objectType(child[0]) == 'nurbsCurve' :
            continue    
            
#   排除特殊的几个组      
    low = a.lower()
    if re.match('fx*',low) or re.match('cam*',low) or re.match('crowd*',low)  :
        continue
    try:
        cmds.delete(a)    
    except:
        continue
#   删除空组
#mel.eval('deleteEmptyGroups()')

#   后台模式自动保存文件    
if cmds.about(batch =1):
    cmds.file(f=1, save=1)
mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
print "Done!!"    
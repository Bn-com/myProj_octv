#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.face.baseClass import *
from RIG.simulation.simulationMain import SM_warning

class SK_MrrorEyebrowUI(object):
    def __init__(self):
        self.displayUI()
        
    def displayUI(self):
        IDMTRigGUI='MrrorEyebrowUI'
        if rig.window(IDMTRigGUI,exists=True):
            rig.deleteUI(IDMTRigGUI)
        rig.window(IDMTRigGUI,title= u'镜像眉毛工具',menuBar=True,wh=  (320,70),minimizeButton=True,maximizeButton=True)
        self.mainCLT = rig.columnLayout()
        
        rig.text(u'1-选择你要镜像的眉毛                     2-点击下面镜像按钮')
        rig.button(l = u'镜像',w = 310,c = lambda x:self.MirrorEyebrow())
        
        rig.window(IDMTRigGUI,e=True,wh=(325,70))
        rig.showWindow(IDMTRigGUI)   
        
    def MirrorEyebrow(self):
        objs =rig.ls(sl = True)
        if objs:
            unLock = unLockAttr(False,False,False)
            Lock = LockHideAttr(False,False,False,False)
            for obj in objs:
                if not (obj.split('_')[0] == 'Lf'):
                    SM_warning(u'命名有误\n物体名必须以Lf_开始')
                else:
                    newName = obj.replace('Lf_','Rt_')
                    if rig.objExists(newName):
                        SM_warning(newName+u'---物体已经存在')
                    else:
                        unLock.unLockObj(obj)
                        pos = rig.xform(obj,q = True,t = True,wd = True)
                        rig.xform(obj,t = (0,0,0),wd = True)                        
                        
                        newObj = rig.duplicate(obj,n = newName)[0]
                        unLock.unLockObj(newObj)
                        grp = rig.group(empty = True,w = True)
                        rig.parent(newObj,grp)
                        rig.setAttr(grp+'.sx',-1)
                        rig.makeIdentity(grp,apply = True,s = True,r = True,t = True)
                        rig.parent(newObj,w = True)
                        rig.delete(grp)
                        
                        rig.xform(obj,t = pos,wd = True)
                    
        else:
            SM_warning(u'请选择你需要镜像的物体')
        

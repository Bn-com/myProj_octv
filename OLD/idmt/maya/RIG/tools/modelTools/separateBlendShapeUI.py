#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.face.baseClass import *
from RIG.simulation.simulationMain import SM_warning

class separateBlendShapeUI(object):
    def __init__(self):
        self.displayUI()
        
    def displayUI(self):
        IDMTRigGUI='separateBlendShapeUI'
        if rig.window(IDMTRigGUI,exists=True):
            rig.deleteUI(IDMTRigGUI)
        rig.window(IDMTRigGUI,title= u'分离blendShape',menuBar=True,wh=  (330,300),minimizeButton=True,maximizeButton=True)
        self.mainCLT = rig.columnLayout()

        rig.text(u'1-载入原始物体:   2-选择需要分离的blendShape: 3-点击确定按钮:')
        rig.separator(w = 312,h=15,style='in') 
        rig.rowColumnLayout(numberOfColumns=3,columnWidth = [(1,100),(2,150),(3,73)],columnAttach = (3,'both',0))
        rig.text(u'载入原始物体:')
        self.ploygonTF = rig.textField(tx = u'')
        rig.button(l = u'>>',w = 30,c = lambda x:self.loadSeleteObj())
        rig.setParent(self.mainCLT)
        rig.separator(w = 312,h=15,style='in')  
              
        rig.button(l = u'确定',w = 310,c = lambda x:self.separate())
        
        rig.window(IDMTRigGUI,e=True,wh=(330,300))
        rig.showWindow(IDMTRigGUI)   
        
    def separate(self):
        objs =rig.ls(sl = True)
        if objs:
            origenObj = rig.textField(self.ploygonTF,q = True,tx = True)
            if origenObj:
                for obj in objs:
                    LfVtx = []#存放左边点的序号
                    LfPos = []#存放左边点的位置
                    RtVtx = []#存放右边点的序号
                    RtPos = []#存放右边点的位置
                    OVpos = []#存放原始模型的位置
                    
                    orVtxs = rig.ls(origenObj+'.vtx[*]',fl = True)
                    for vtx in orVtxs:
                        pos = rig.xform(vtx,q = True,t = True,wd = True)
                        OVpos.append(pos)
                        if pos[0] > 0.0001:
                            LfPos.append(pos)
                            LfVtx.append(vtx)
                            
                        if pos[0] < -0.0001:
                            RtPos.append(pos)
                            RtVtx.append(vtx)
                            
                    LfMesh = rig.duplicate(obj,n = 'Lf_'+obj)[0]#生成左边模型.
                    for i,vtx in enumerate(LfVtx):
                        newVtx = vtx.replace(origenObj,LfMesh)
                        rig.xform(newVtx,t = LfPos[i],wd = True)
                        
                    RtMesh = rig.duplicate(obj,n = 'Rt_'+obj)[0]#生成右边模型.
                    for i,vtx in enumerate(RtVtx):
                        newVtx = vtx.replace(origenObj,RtMesh)
                        rig.xform(newVtx,t = RtPos[i],wd = True)
                    
            else:
                SM_warning(u'请载入选择原始物体')
                    
        else:
            SM_warning(u'请选择你需要分离blendShpe的物体')
            
            
    def loadSeleteObj(self):
        objs =rig.ls(sl = True)
        if objs:
            rig.textField(self.ploygonTF,e = True,tx = objs[0])
                    
        else:
            SM_warning(u'请选择原始物体')
        

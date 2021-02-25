#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.tools.IOWeights.IOMainFun import *
from RIG.simulation.simulationMain import SM_warning
from RIG.commonly.base import SK_getSkinCluster

class SK_IOWeightsUI(object):
    def __init__(self):
        self.displayUI()
        
    def displayUI(self):
        IDMTRigGUI='IOWeightsUI'
        if rig.window(IDMTRigGUI,exists=True):
            rig.deleteUI(IDMTRigGUI)
        rig.window(IDMTRigGUI,title= u'导入导出权重工具1.0',menuBar=True,wh=  (325,500),minimizeButton=True,maximizeButton=True)
        self.mainCLT = rig.columnLayout()
        

        rig.button(l = u'导出选择的物体的权重',w = 320,c = lambda x:self.exportWeights())
        rig.button(l = u'导出场景中所有蒙皮的polygon物体权重',w = 320,c = lambda x:self.exportAllPloygon())
        rig.separator(w = 312,h=15,style='in')
        rig.button(l = u'导入权重',w = 320,c = lambda x:self.importWeigths())
                
        rig.showWindow(IDMTRigGUI)   
        rig.window(IDMTRigGUI,e=True,wh=(330,110))
    
    #--------------------------------------------------------------- 列出场景中所有蒙皮物体
    def allPolygon(self):
        allMesh = rig.ls(type = 'mesh')
        allMeshTransforms = [rig.listRelatives(mesh,p = True)[0] for mesh in allMesh]
        getMesh = []
        for mesh in allMeshTransforms:
            if 1 == len(rig.ls(mesh)):#检测重命名
                if not(mesh in getMesh) and SK_getSkinCluster(mesh):
                    getMesh.append(mesh)
            else:
                rig.warning(u'导出失败!   物体：'+mesh+u'有重命名')
        if getMesh:
            return getMesh
        else:
            return False
        
    #------------------------------------------------------------- 导出所有ploygon物体
    def exportAllPloygon(self):
        version = rig.about(v = True)
        if '2011' == version.split()[0] or '2012' == version.split()[0]:#maya版本
            objs = self.allPolygon()
            if objs:
                IO_exportWeights(objs)
            else:
                SM_warning(u'场景中没有找到蒙皮物体')
        else:
            SM_warning(u'此功能仅maya2011以上版本可用')
            
    def exportWeights(self):
        version = rig.about(v = True)
        if '2011' == version.split()[0] or '2012' == version.split()[0]:#maya版本
            IO_exportWeights(False)
        else:
            SM_warning(u'此功能仅maya2011以上版本可用')        
        
    def importWeigths(self):
        IO_importWeights()
    
        
        

    

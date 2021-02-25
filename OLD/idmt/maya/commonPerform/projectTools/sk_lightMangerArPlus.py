# -*- coding: utf-8 -*-
#------------------------------#
# Update Plus : shenkang
# 2017.5
# muti modify
#------------------------------#

import maya.cmds as cmds
import maya.utils as utils
import os.path
import glob
import re
import sys, os
import subprocess
import threading
import mtoa.callbacks as callbacks
import maya.OpenMaya as om
import mtoa.utils as mutils

class MtoALightManager(object):
    window = None
    def __new__(cls, *args, **kwargs):
        if not '_instance' in vars(cls):
            cls._instance = super(MtoALightManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if self.window is None:
            self.window = 'MtoALightManagerPlus'
            self.listElements = []
            self.column = ''
            callbacks.addNodeAddedCallback(callbacks.Callback(self.refreshUI), 'directionalLight', applyToExisting=False)
            callbacks.addNodeAddedCallback(callbacks.Callback(self.refreshUI), 'pointLight', applyToExisting=False)
            callbacks.addNodeAddedCallback(callbacks.Callback(self.refreshUI), 'spotLight', applyToExisting=False)
            callbacks.addNodeAddedCallback(callbacks.Callback(self.refreshUI), 'areaLight', applyToExisting=False)
            callbacks.addNodeAddedCallback(callbacks.Callback(self.refreshUI), 'aiAreaLight', applyToExisting=False)
            callbacks.addNodeAddedCallback(callbacks.Callback(self.refreshUI), 'aiSkyDomeLight', applyToExisting=False)
            callbacks.addNodeAddedCallback(callbacks.Callback(self.refreshUI), 'aiPhotometricLight', applyToExisting=False)
            callbacks.addAttributeChangedCallback(self.meshTranslatorChanged, 'mesh', 'aiTranslator', applyToExisting=True)
            
            callbacks.addNodeRemovedCallback(self.deleteLight, 'directionalLight', applyToExisting=False)
            callbacks.addNodeRemovedCallback(self.deleteLight, 'pointLight', applyToExisting=False)
            callbacks.addNodeRemovedCallback(self.deleteLight, 'spotLight', applyToExisting=False)
            callbacks.addNodeRemovedCallback(self.deleteLight, 'areaLight', applyToExisting=False)
            callbacks.addNodeRemovedCallback(self.deleteLight, 'aiAreaLight', applyToExisting=False)
            callbacks.addNodeRemovedCallback(self.deleteLight, 'aiSkyDomeLight', applyToExisting=False)
            callbacks.addNodeRemovedCallback(self.deleteLight, 'aiPhotometricLight', applyToExisting=False)
            callbacks.addNodeRemovedCallback(self.deleteMeshLight, 'mesh', applyToExisting=False)
            
            callbacks.addNameChangedCallback(callbacks.Callback(self.refreshUI), 'directionalLight', applyToExisting=True)
            callbacks.addNameChangedCallback(callbacks.Callback(self.refreshUI), 'pointLight', applyToExisting=True)
            callbacks.addNameChangedCallback(callbacks.Callback(self.refreshUI), 'spotLight', applyToExisting=True)
            callbacks.addNameChangedCallback(callbacks.Callback(self.refreshUI), 'areaLight', applyToExisting=True)
            callbacks.addNameChangedCallback(callbacks.Callback(self.refreshUI), 'aiAreaLight', applyToExisting=True)
            callbacks.addNameChangedCallback(callbacks.Callback(self.refreshUI), 'aiSkyDomeLight', applyToExisting=True)
            callbacks.addNameChangedCallback(callbacks.Callback(self.refreshUI), 'aiPhotometricLight', applyToExisting=True)
            callbacks.addNameChangedCallback(callbacks.Callback(self.refreshUI), 'mesh', applyToExisting=True)
            self.disValue = [(1, 30), (2, 50), (3, 150),(4, 150),(5, 150),(6, 150),(7, 150),(8, 160),(9, 160),(10, 60),(11, 60),(12, 60),(13, 60)]
            self.changCMDPre = 'sk_lightMangerArPlus.MtoALightManager()'

    def doCreateMeshLight(self):
        sls = cmds.ls(sl=True, et='transform')
        if len(sls) == 0:
            cmds.confirmDialog(title='Error', message='No transform is selected!', button='Ok')
            return
        shs = cmds.listRelatives(sls[0], type='mesh')
        if shs is None:
            cmds.confirmDialog(title='Error', message='The selected transform has no meshes', button='Ok')
            return
        elif len(shs) == 0:
            cmds.confirmDialog(title='Error', message='The selected transform has no meshes', button='Ok')
            return
        cmds.setAttr('%s.aiTranslator' % shs[0], 'mesh_light', type='string')
        
    def create(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window);
        
        self.window = cmds.window(self.window, widthHeight=(800, 600), title="Light Manager")
        self.refreshList()
        
        self.createUI()

        cmds.setParent(menu=True)

        cmds.showWindow(self.window)
        
        try:
            initPos = cmds.windowPref( self.window, query=True, topLeftCorner=True )
            if initPos[0] < 0:
                initPos[0] = 0
            if initPos[1] < 0:
                initPos[1] = 0
            cmds.windowPref( self.window, edit=True, topLeftCorner=initPos )
        except :
            pass
            
        self.refreshList()
            
    def refreshList(self):
        self.listElements = []
        list = cmds.ls(type='directionalLight')
        for light in list:
            self.listElements.append(['directionallight',light])
            
        list = cmds.ls(type='pointLight')
        for light in list:
            self.listElements.append(['pointlight',light])
            
        list = cmds.ls(type='spotLight')
        for light in list:
            self.listElements.append(['spotlight',light])
            
        list = cmds.ls(type='areaLight')
        for light in list:
            self.listElements.append(['arealight',light])
        
        list = cmds.ls(type='aiAreaLight')
        for light in list:
            self.listElements.append(['AreaLightShelf',light])
            
        list = cmds.ls(type='aiSkyDomeLight')
        for light in list:
            self.listElements.append(['SkydomeLightShelf',light])
            
        list = cmds.ls(type='aiPhotometricLight')
        for light in list:
            self.listElements.append(['PhotometricLightShelf',light])
            
        list = cmds.ls(type='mesh')
        for mesh in list:
            if cmds.getAttr(mesh+'.aiTranslator') == 'mesh_light':
                self.listElements.append(['MeshLightShelf',mesh])
                
    def removeLightFromList(self, node):
        self.listElements = [light for light in self.listElements if light[1] != node]
    
    def createUI(self):
        cmds.scrollLayout(childResizable=True, minChildWidth=800)
        
        cmds.columnLayout(adjustableColumn=True, columnAlign="right", rowSpacing=10)
        
        cmds.rowLayout(numberOfColumns=9, columnAttach=[(1, 'both', 10), (2, 'both', 5), (3, 'both', 5), (4, 'both', 5), (5, 'both', 5), (6, 'both', 5), (7, 'both', 5), (8, 'both', 5), (9, 'both', 5)] )
        cmds.text(label='Create Light:')
        selectCommand='import maya.cmds as cmds\ncmds.select(\''+'directionalLightShape1'+'\')'
        cmds.nodeIconButton( style='iconOnly', command=lambda *args: cmds.CreateDirectionalLight(), image1='directionallight.png' )
        cmds.nodeIconButton( style='iconOnly', command=lambda *args: cmds.CreatePointLight(), image1='pointlight.png' )
        cmds.nodeIconButton( style='iconOnly', command=lambda *args: cmds.CreateSpotLight(), image1='spotlight.png' )
        cmds.nodeIconButton( style='iconOnly', command=lambda *args: cmds.CreateAreaLight(), image1='arealight.png' )
        cmds.nodeIconButton( style='iconOnly', command=lambda *args: mutils.createLocator('aiAreaLight', asLight=True), image1='AreaLightShelf.png' )
        cmds.nodeIconButton( style='iconOnly', command=lambda *args: mutils.createLocator('aiSkyDomeLight', asLight=True), image1='SkydomeLightShelf.png' )
        cmds.nodeIconButton( style='iconOnly', command=lambda *args: mutils.createLocator('aiPhotometricLight', asLight=True), image1='PhotometricLightShelf.png' )
        cmds.nodeIconButton( style='iconOnly', command=lambda *args: self.doCreateMeshLight(), image1='MeshLightShelf.png' )
        cmds.setParent('..')
        cmds.separator()
        cmds.setParent('..')
        
        cmds.columnLayout(adjustableColumn=True, columnAlign="right", rowSpacing=10)

        cmds.rowColumnLayout('lightsMenu',numberOfColumns=13, columnWidth = self.disValue )
        cmds.checkBox('lightMenuCheckBoxAll',label='all',value = 0,cc='%s.mutiCheckBox()'%(self.changCMDPre))
        cmds.text(label='Select')
        cmds.text(label='Light Name')
        cmds.text(label='Color')
        cmds.text(label='Intensity')
        cmds.text(label='Exposure')
        cmds.text(label='Samples')
        cmds.text(label='Ai Radus')
        cmds.text(label='Ai Specular')
        cmds.text(label='Ai CastSDW')
        cmds.text(label='E Diffuse')
        cmds.text(label='E Specular')
        cmds.text(label='Enable')
        cmds.setParent('..')
        
        cmds.setParent('..')
        cmds.separator()
        cmds.setParent('..')

        self.column = cmds.columnLayout(adjustableColumn=True, columnAlign="right", rowSpacing=50)
        
        self.refreshControls()
        
        '''for element in self.listElements:
            elementName = element[1]
            cmds.rowLayout(numberOfColumns=6, adjustableColumn=2, columnWidth6=[50, 160, 160, 180, 180, 40], columnAttach=[(1, 'both', 5), (2, 'both', 5), (3, 'both', 5), (4, 'both', 5), (5, 'both', 5), (6, 'both', 10)] )
            
            selectCommand='import maya.cmds as cmds\ncmds.select(\''+elementName+'\')'
            cmds.nodeIconButton( style='iconOnly', command=selectCommand, image1=element[0]+'.png' )
            
            cmds.text(label=elementName, align='left')
            
            cmds.attrColorSliderGrp(label='C:', at=elementName+'.color', columnWidth4=[15,30,70,40], columnAlign=[1,"center"])
            
            if element[0] == 'MeshLightShelf':
                cmds.attrFieldSliderGrp(label='I:', at=elementName+'.intensity', columnWidth2=[15,45], columnAlign=[1,"center"])
                cmds.attrFieldSliderGrp(label='E:', at=elementName+'.aiExposure', columnWidth3=[15,45,70], columnAlign=[1,"center"])
            else:
                cmds.attrFieldSliderGrp(label='I:', at=elementName+'.intensity', columnWidth4=[15,45,70,40], columnAlign=[1,"center"])
                cmds.attrFieldSliderGrp(label='E:', at=elementName+'.aiExposure', columnWidth4=[15,45,70,40], columnAlign=[1,"center"])
            
            cmds.checkBoxGrp('lightMenuM_visibility_'+elementName, columnAlign=[1,"center"])
            cmds.connectControl('lightMenuM_visibility_'+elementName, elementName+'.visibility', index=1)
            
            cmds.setParent('..')'''
    
    def meshTranslatorChanged(self, transPlug, *args):
        self.refreshUI()
        #print "#### ",om.MFnMesh(transPlug.node()).name()
    
    def refreshUI(self):
        self.refreshList()
        self.refreshControls()
        
    def deleteLight(self, node):
        self.removeLightFromList(node)
        self.refreshControls()
        
    def deleteMeshLight(self, node):
        if cmds.getAttr(node+'.aiTranslator') == 'mesh_light':
            self.removeLightFromList(node)
            self.refreshControls()
        
    def refreshControls(self):
        if cmds.columnLayout(self.column, exists=True):
            cmds.setParent(self.column)

            #cmds.rowColumnLayout( numberOfColumns=13, columnWidth = self.disValue )

            for rowChild in cmds.columnLayout(self.column, query=True, childArray=True) or []:
                row = self.column+"|"+rowChild
                cmds.deleteUI(rowChild)

            for num in range(len(self.listElements)):
                try:
                    cmds.deleteUI('lightMenuRow_%s'%(str(num)))
                except:
                    pass

            changCMDPre = self.changCMDPre

            for num in range(len(self.listElements)):
                element = self.listElements[num]
                elementName = element[1]
                cmds.rowColumnLayout('lightMenuRow_%s'%(str(num)), numberOfColumns=13, columnWidth = self.disValue )
                # checkbox
                cmds.checkBox('lightCheckSel_%s'%elementName,value = 0,l = 'S')
                # select icon
                selectCommand='import maya.cmds as cmds\ncmds.select(\''+elementName+'\')'
                cmds.nodeIconButton( style='iconOnly', command=selectCommand, image1=element[0]+'.png' )
                # light name
                cmds.text(label=elementName, align='left')
                # color
                checkAttr = elementName+'.color'
                if cmds.ls(checkAttr):
                    #cmds.attrColorSliderGrp(label='C:', at=checkAttr, visibleChangeCommand = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth4=[15,30,70,40], columnAlign=[1,"left"])
                    colorValue = cmds.getAttr(checkAttr)
                    cmds.colorSliderGrp('lightMenuM_%s'%elementName,label = 'C:',rgb = (colorValue[0][0],colorValue[0][1],colorValue[0][2]),cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth3=[15,45,120], columnAlign=[1,"center"])
                else:
                    cmds.text("None")
                # Intensity
                checkAttr = elementName+'.intensity'
                if cmds.ls(checkAttr):
                    if element[0] == 'MeshLightShelf':
                        cmds.attrFieldSliderGrp(label='I:', at=checkAttr, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth2=[15,120], columnAlign=[1,"center"])
                    else:
                        cmds.attrFieldSliderGrp(label='I:', at=checkAttr, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth4=[15,45,70,40], columnAlign=[1,"center"])
                else:
                    cmds.text("None")
                # Exposure
                checkAttr = elementName+'.aiExposure'
                if cmds.ls(checkAttr):
                    if element[0] == 'MeshLightShelf':
                        cmds.attrFieldSliderGrp(label='E:', at=checkAttr, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth3=[15,45,110], columnAlign=[1,"center"])
                    else:
                        cmds.attrFieldSliderGrp(label='E:', at=checkAttr, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth4=[15,45,70,40], columnAlign=[1,"center"])
                else:
                    cmds.text("None")
                #cmds.rowLayout(numberOfColumns=2, columnWidth2=[60, 50], columnAttach=[(1, 'both', 0), (2, 'both', 5)] )
                # samples
                checkAttr = elementName+'.aiSamples'
                if cmds.ls(checkAttr):
                    if element[0] == 'MeshLightShelf':
                        cmds.attrFieldSliderGrp(label='S:', at=checkAttr, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth2=[25,120], columnAlign=[1,"center"])
                    else:
                        cmds.attrFieldSliderGrp(label='S:', at=checkAttr, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth4=[15,45,70,40], columnAlign=[1,"center"])
                else:
                    cmds.text("None")
                # ai Radus
                checkAttr = elementName+'.aiRadius'
                if cmds.ls(checkAttr):
                    if element[0] == 'MeshLightShelf':
                        cmds.attrFieldSliderGrp(label='ARU:', at=checkAttr, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth2=[25,45], columnAlign=[1,"center"])
                    else:
                        cmds.attrFieldSliderGrp(label='ARU:', at=checkAttr, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth4=[25,45,70,40], columnAlign=[1,"center"])
                else:
                    cmds.text("None")
                # ai Specular
                checkAttr = elementName+'.aiSpecular'
                if cmds.ls(checkAttr):
                    if element[0] == 'MeshLightShelf':
                        cmds.attrFieldSliderGrp(label='ASP:', at=checkAttr, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth3=[25,45,70], columnAlign=[1,"center"])
                    else:
                        cmds.attrFieldSliderGrp(label='ASP:', at=checkAttr, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),columnWidth4=[25,45,70,40], columnAlign=[1,"center"])
                else:
                    cmds.text("None")
                # ai cast shadow
                checkAttr = elementName+'.aiCastShadows'
                if cmds.ls(checkAttr):
                    cmds.checkBoxGrp('lightMenuM_aiCastShadow_'+elementName, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),label="ASD:", columnWidth2=[30,30])
                    try:
                        cmds.connectControl('lightMenuM_aiCastShadow_'+elementName, checkAttr, index=1)
                        cmds.connectControl('lightMenuM_aiCastShadow_'+elementName, checkAttr, index=2)
                    except:
                        pass
                else:
                    cmds.text("None")
                # E Diffuse
                checkAttr = elementName+'.emitDiffuse'
                if cmds.ls(elementName+'.aiCastShadows'):
                    cmds.checkBoxGrp('lightMenuM_emitDiffuse_'+elementName, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),label="ED:", columnWidth2=[30,30])
                    try:
                        cmds.connectControl('lightMenuM_emitDiffuse_'+elementName, checkAttr, index=1)
                        cmds.connectControl('lightMenuM_emitDiffuse_'+elementName, checkAttr, index=2)
                    except:
                        pass
                else:
                    cmds.text("None")
                # E Specular
                checkAttr = elementName+'.emitSpecular'
                if cmds.ls(checkAttr):
                    cmds.checkBoxGrp('lightMenuM_emitSpecular_'+elementName, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),label="ES:", columnWidth2=[30,30])
                    try:
                        cmds.connectControl('lightMenuM_emitSpecular_'+elementName, checkAttr, index=1)
                        cmds.connectControl('lightMenuM_emitSpecular_'+elementName, checkAttr, index=2)
                    except:
                        pass
                else:
                    cmds.text("None")
                # enable
                checkAttr = elementName+'.visibility'
                if cmds.ls(checkAttr):
                    cmds.checkBoxGrp('lightMenuM_visibility_'+elementName, cc = '%s.mutiModify("%s")'%(changCMDPre,checkAttr),label="E:", columnWidth2=[30,30])
                    try:
                        cmds.connectControl('lightMenuM_visibility_'+elementName, checkAttr, index=1)
                        cmds.connectControl('lightMenuM_visibility_'+elementName, checkAttr, index=2)
                    except:
                        pass
                else:
                    cmds.text("None")
                cmds.setParent('..')
                
                cmds.setParent('..')

    def mutiCheckBox(self):
        value = cmds.checkBox('lightMenuCheckBoxAll',q=1,v=1)
        for num in range(len(self.listElements)):
            element = self.listElements[num]
            elementName = element[1]
            cmds.checkBox('lightCheckSel_%s'%elementName,e=1,v=value)

    def mutiModify(self,checkAttr,printMode = 0):
        lightNow = checkAttr.split('.')[0]
        needAttr = '.' + checkAttr.split('.')[-1]
        # 处理color
        if needAttr in ['.color']:
            valueNow = cmds.colorSliderGrp('lightMenuM_%s'%lightNow,q=1,rgb=1)
            cmds.setAttr(checkAttr,valueNow[0],valueNow[1],valueNow[2],type = 'double3')
        # 本行是否选取
        nowSelCheckValue = cmds.checkBox('lightCheckSel_%s'%lightNow,q=1,v=1)
        if printMode:print '-----001'
        if printMode:print nowSelCheckValue
        if not nowSelCheckValue:
            return
        # 多个选取
        selCheckList = []
        for num in range(len(self.listElements)):
            element = self.listElements[num]
            elementName = element[1]
            if elementName == lightNow:
                continue
            checkValue = cmds.checkBox('lightCheckSel_%s'%elementName,q=1,v=1)
            if checkValue:
                selCheckList.append(elementName)
        if printMode:print '-----002'
        if printMode:print nowSelCheckValue
        if not selCheckList:
            return
        # 处理
        for checkObj in selCheckList:
            needValue = cmds.getAttr(checkAttr)
            if needAttr in ['.color']:
                cmds.setAttr(checkObj+needAttr,needValue[0][0],needValue[0][1],needValue[0][2],type = 'double3')
                cmds.colorSliderGrp('lightMenuM_%s'%checkObj,e=1,rgb = (needValue[0][0],needValue[0][1],needValue[0][2]))
            else:
                if cmds.ls(checkObj+needAttr):
                    cmds.setAttr(checkObj+needAttr,needValue)

#MtoALightManager().create()
    

# -*- coding: utf-8 -*-
import maya.cmds as mc
from pymel.core import *
import maya.mel as mel
import os
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class GA_modSwitch():
    def __init__(self):
        
        pass
    def GA_switchModeWin(self):
        if mc.window('GA_switchModeWin',exists = True):
            deleteUI('GA_switchModeWin')
        mc.window('GA_switchModeWin', title = u'Yak -- Switch Mode  Apply', width = 500, height = 180, sizeable = True,menuBar=1)
        mc.menu(l= "Help")
        mc.menuItem(l="Technical",command="mel.eval('system(\"loadZ:/Resource/Support/Maya/help/GA_proxyTechnical.mht\")')")
        mc.menuItem(l="Method",command="mel.eval('system(\"loadZ:/Resource/Support/Maya/help/mr_proxyMethod.mht\")')")   
        columnLayout(rowSpacing=2, columnAttach = ['both',5],columnWidth = 500, columnAlign = 'left')
        text(label = '')
        radioButtonGrp('GA_dt', label='Duplicate Type:', labelArray2=['Normal', 'Instance'], select = 1, numberOfRadioButtons = 2 )
        radioButtonGrp('GA_mode', label='Mode:', labelArray3=['Hight', 'Proxy','Low'], select = 1, numberOfRadioButtons = 3 )
        radioButtonGrp('GA_selType', label='Selected:', labelArray2=['By Selected', 'All By Selected Type'], select = 1, numberOfRadioButtons = 2 )
        mc.button( label=u'Apply', c = 'from idmt.maya.py_common import GA_modSwitch\nreload(GA_modSwitch)\nGA_modSwitch.GA_modSwitch().GA_switchMode()' )
        mc.showWindow( 'GA_switchModeWin' )
        
    
    
    
    def GA_getMiscCtrl(self, object ):
        if object.nodeName().find('_ctrl') > -1 and object.getShape():
            if objectType( object.getShape() ) == 'nurbsCurve':
                return object
        else:
            if not object.getParent():
                return 0
            else:
                
                return self.GA_getMiscCtrl( object.getParent() )
                
             
    def GA_copyKeyWith2Obj(self,obj1,obj2):
    
        copy = obj1
        past = obj2
        
        k = listAttr( copy, k = True, o = True)
        cb = listAttr (copy, cb = True, u = True)
        attrs = []
        if cb:
            attrs = set ( k ) & set( cb )
        else:
            attrs = k
        for attr in attrs:
            if getAttr (copy + '.' + attr, type = True,) != 'double3':
                val = getAttr(copy + '.' + attr)
                setAttr(past + '.' + attr, val)
        if copyKey( copy ):
            pasteKey (past, o = 'replaceCompletely')
    
    
    def GA_importMisc(self, name,mode ):
        import idmt
        EP=''
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        miscFile=''
        if  name[0] in ['p','P']:
            miscFile = serverPath+'scenes/props/' +name + '/rigging/' + shotInfos[0]+'_'+name + mode +'_rg.mb'
        if os.path.isfile(miscFile):
            newObject = importFile(miscFile,returnNewNodes = True)
            for n in newObject:
                if n.nodeType() == 'transform':
                    return n.root()
        else:
            return 0
               
    def GA_returnMiscName(self,ctrl):
        objectName = ''
        if ctrl.find('_l_ctrl') > -1:
            objectName = ctrl.split('_l_ctrl')[0]
        
        elif ctrl.find('_p_ctrl') > -1:
            objectName = ctrl.split('_p_ctrl')[0]
        else:
            objectName = ctrl.split('_h_ctrl')[0]
            
        return objectName     
    
    
    
    def GA_switchMode(self):
        mode = ''
        dt = radioButtonGrp('GA_dt', q = True, select = True )
        modeInt = radioButtonGrp('GA_mode', q = True, select = True )
        selType = radioButtonGrp('GA_selType', q = True, select = True )
        if modeInt == 2:
            mode = '_p'
        elif modeInt == 3:
            mode = '_lt'


        elif modeInt == 1:
            mode = '_h'
                      
        sels = ls( sl = True)
        
        if selType == 2:
            if len(sels) == 1:
                ctrl = self.GA_getMiscCtrl(sels[0])
                print ctrl
                if ctrl:
                    objectName = self.GA_returnMiscName(ctrl)
                    allMisc = ls(objectName + '*', type = 'transform')
                    del sels[:]
                    for m in allMisc:
                        if self.GA_getMiscCtrl(m):
                            sels.append(self.GA_getMiscCtrl(m))
            else:
                return 0
                
        sels = list(set(sels))
       
        for sel in sels:
            ctrl = self.GA_getMiscCtrl(sel)
            
            objectName = self.GA_returnMiscName(ctrl)
        
            if not objectName:
                return 0
                
            if objectName.find(':') > -1:
                objectName = objectName.split(':')[1]
            
            
            if not objExists(objectName + mode + '_ctrl_MiscType'):
               
                newCtrl = self.GA_importMisc( objectName,mode )
                if newCtrl:
                    rename(newCtrl, objectName + mode + '_ctrl_MiscType')
       
                
        for sel in sels:
            ctrl = self.GA_getMiscCtrl(sel)
            
            objectName = self.GA_returnMiscName(ctrl)
                
            if not objectName:
                return 0
                    
            if objectName.find(':') > -1:
                objectName = objectName.split(':')[1]
            
            newCtrl = ''
            miscObj = objectName + mode + '_ctrl_MiscType'
              
            if objExists(miscObj):
                #if dt == 1:
                    #newCtrl = duplicate(miscObj, n = objectName + mode + '_ctrl_#' )[0]
                #else:
                newCtrl = duplicate(miscObj, instanceLeaf  = True, n = objectName + mode + '_ctrl_#' )[0]
                
                if ctrl.getParent():
                    parent(newCtrl,ctrl.getParent())
                self.GA_copyKeyWith2Obj(ctrl,newCtrl)
                try:
                    mc.setAttr(ctrl + '.visibility', 0)
                    delete(ctrl)
                except:
                    mc.setAttr(ctrl + '.visibility', 0)
            
        allMiscType = ls('*_ctrl_MiscType')
        if allMiscType:
            try:
                for misc in allMiscType:
                    mc.setAttr(misc + '.visibility', 0)
                delete(allMiscType)
            except:
                for misc in allMiscType:
                    mc.setAttr(misc + '.visibility', 0)
                    


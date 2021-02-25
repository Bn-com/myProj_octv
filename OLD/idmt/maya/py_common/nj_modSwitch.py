# -*- coding: utf-8 -*-
import maya.cmds as mc
from pymel.core import *
import maya.mel as mel
import os
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class nj_modSwitch():
    def __init__(self):
        
        pass
    def nj_switchModeWin(self):
        if mc.window('nj_switchModeWin',exists = True):
            deleteUI('nj_switchModeWin')
        mc.window('nj_switchModeWin', title = u'NJ -- Switch Mode  Apply', width = 500, height = 180, sizeable = True,menuBar=1)
        mc.menu(l= "Help")
        mc.menuItem(l="Technical",command="mel.eval('system(\"loadZ:/Resource/Support/Maya/help/nj_proxyTechnical.mht\")')")   
        mc.menuItem(l="Method",command="mel.eval('system(\"loadZ:/Resource/Support/Maya/help/mr_proxyMethod.mht\")')")   
        columnLayout(rowSpacing=2, columnAttach = ['both',5],columnWidth = 500, columnAlign = 'left')
        text(label = '')
        radioButtonGrp('nj_dt', label='Duplicate Type:', labelArray2=['Normal', 'Instance'], select = 1, numberOfRadioButtons = 2 )
        radioButtonGrp('nj_mode', label='Mode:', labelArray3=['Hight', 'Proxy','Low'], select = 1, numberOfRadioButtons = 3 )
        radioButtonGrp('nj_selType', label='Selected:', labelArray2=['By Selected', 'All By Selected Type'], select = 1, numberOfRadioButtons = 2 )
        mc.button( label=u'Apply', c = 'from idmt.maya.py_common import nj_modSwitch\nreload(nj_modSwitch)\nnj_modSwitch.nj_modSwitch().nj_switchMode()' )
        mc.showWindow( 'nj_switchModeWin' )
        
    
    
    
    def nj_getMiscCtrl(self, object ):
        if object.nodeName().find('_ctrl') > -1 and object.getShape():
            if objectType( object.getShape() ) == 'nurbsCurve':
                return object
        else:
            if not object.getParent():
                return 0
            else:
                
                return self.nj_getMiscCtrl( object.getParent() )
                
             
    def nj_copyKeyWith2Obj(self,obj1,obj2):
    
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
    
    
    def nj_importMisc(self, name,mode ):
        import idmt
        EP=''
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        projectshortName=['nj','yd']
        miscFile=''
        if shotInfos[0] in projectshortName:
            asset = idmt.pipeline.db.GetAssetByFilename(shotInfos[0]+'_'+name)
            if asset:
                EP=asset.code
        if shotInfos[0] in projectshortName and name[0] in ['p'] and EP!='':
            miscFile = serverPath+'scenes/props/' + EP+'/'+name + '/master/' + shotInfos[0]+'_'+name + mode +'_ms_anim.mb'
        if shotInfos[0] in projectshortName and name[0] in ['s', 'S'] and EP!='':
            miscFile = serverPath+'scenes/sets/' + EP+'/'+name + '/master/' + shotInfos[0]+'_'+name + mode +'_ms_tex.mb' 
        if shotInfos[0] in projectshortName and name[0] in ['p'] and EP=='':
            miscFile = serverPath+'scenes/props/' +name + '/master/' + shotInfos[0]+'_'+name + mode +'_ms_anim.mb'
        if shotInfos[0] in projectshortName and name[0] in ['s', 'S'] and EP=='':
            miscFile = serverPath+'scenes/sets/' +name + '/master/' + shotInfos[0]+'_'+name + mode +'_ms_tex.mb'
        if shotInfos[0] not in projectshortName:
            mc.error(u'文件名有问题，请检查文件名')
        
        if os.path.isfile(miscFile):
            newObject = importFile(miscFile,returnNewNodes = True)
            for n in newObject:
                if n.nodeType() == 'transform':
                    return n.root()
        else:
            return 0
               
    def nj_returnMiscName(self,ctrl):
        objectName = ''
        if ctrl.find('_l_ctrl') > -1:
            objectName = ctrl.split('_l_ctrl')[0]
        
        elif ctrl.find('_p_ctrl') > -1:
            objectName = ctrl.split('_p_ctrl')[0]
        else:
            objectName = ctrl.split('_h_ctrl')[0]
            
        return objectName     
    
    
    
    def nj_switchMode(self):
        mode = ''
        dt = radioButtonGrp('nj_dt', q = True, select = True )
        modeInt = radioButtonGrp('nj_mode', q = True, select = True )
        selType = radioButtonGrp('nj_selType', q = True, select = True )
        if modeInt == 2:
            mode = '_p'
        elif modeInt == 3:
            mode = '_l'
    
        elif modeInt == 1:
            mode = '_h'
                      
        sels = ls( sl = True)
        
        if selType == 2:
            if len(sels) == 1:
                ctrl = self.nj_getMiscCtrl(sels[0])
                print ctrl
                if ctrl:
                    objectName = self.nj_returnMiscName(ctrl)
                    allMisc = ls(objectName + '*', type = 'transform')
                    del sels[:]
                    for m in allMisc:
                        if self.nj_getMiscCtrl(m):
                            sels.append(self.nj_getMiscCtrl(m))
            else:
                return 0
                
        sels = list(set(sels))
       
        for sel in sels:
            ctrl = self.nj_getMiscCtrl(sel)
            
            objectName = self.nj_returnMiscName(ctrl)
        
            if not objectName:
                return 0
                
            if objectName.find(':') > -1:
                objectName = objectName.split(':')[1]
            
            
            if not objExists(objectName + mode + '_ctrl_MiscType'):
               
                newCtrl = self.nj_importMisc( objectName,mode )
                if newCtrl:
                    rename(newCtrl, objectName + mode + '_ctrl_MiscType')
       
                
        for sel in sels:
            ctrl = self.nj_getMiscCtrl(sel)
            
            objectName = self.nj_returnMiscName(ctrl)
                
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
                self.nj_copyKeyWith2Obj(ctrl,newCtrl)
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
                    
# 优化 使用，非本class

    def nj_fixHidePro(self):
        mel.eval('source "channelBoxCommand.mel"')
        objs=mc.ls(type='transform',l=1)
        for obj in objs:
            # 排除非MODEL组的
            if 'MODEL|' not in obj:
                continue
            if "nj_c020003LordGarmadon4Arms*:*" in obj:
                continue
            # 排除组下的物体
            temObj = obj.split('|')[-1]
            if "prox" in temObj or "daili" in temObj or ":frame" in temObj or "GRP_DAILI" in temObj or ":GRP_DAILI" in temObj :
                try:
                    mel.eval(CBunlockAttr+" "+obj+".v")
                    mel.eval(CBdeleteConnection+" "+obj+".v")
                    mc.setAttr((obj+'.v'),0)                         
                except:
                    pass 
        return 0                 

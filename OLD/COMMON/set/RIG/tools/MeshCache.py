#-*- coding: utf-8 -*-

import maya.cmds as rig
class SK_AutoAddSetUI(object):
    def __init__(self):
        self.displayUI()
        
    def displayUI(self):
        IDMTRigGUI='SK_AutoAddSetUI'
        if rig.window(IDMTRigGUI,exists=True):
            rig.deleteUI(IDMTRigGUI)
        self.CurveSign = 'OFF'
        self.mainUI = rig.window(IDMTRigGUI,title= u'增加cacheSet工具',menuBar=True,minimizeButton=True,maximizeButton=True)
        self.mainFLY = rig.formLayout()
        self.mainSRL = rig.scrollLayout(cr = True)
        self.mainCLM = rig.columnLayout(adj = True)
        
        self.mainBT = rig.button(l = u'自动增加MODEL下的模型到MESHES',c = lambda x:self.AutoSets())
        
        rig.separator(st = 'out')
        self.mainBT = rig.button(l = u'增加选择模型到MESHES',c = lambda x:self.slelectSets())
        
        rig.separator(st = 'out')
        self.mainBT = rig.button(l = u'将选择的物体从MESHES中移除',c = lambda x:self.removeObjs())
        
        rig.setParent(self.mainFLY)
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'top', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'left', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'bottom', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'right', 2))
        rig.showWindow(IDMTRigGUI)  
        rig.window(self.mainUI,e=True,wh=(325,200))
        
    #===========================================================================
    # 检测'CACHE_OBJS'和'MESHES'是否存在，并提示是否增加'CACHE_OBJS'和'MESHES'
    #===========================================================================
    def FindSets(self):
        if rig.objExists('CACHE_OBJS'):#是否存在'CACHE_OBJS'
            pass
        else:
            reMS = rig.confirmDialog(t = u'警告',
                     m = u'场景中没有找到CACHE_OBJS!\n是否新建一个？',
                     ma = 'left',
                     button = ('Yes','Cancel'),
                     defaultButton = 'Yes',
                     cancelButton = 'Cancel',
                     dismissString = 'Cancel')
            
            if 'Yes' == reMS:
                rig.createNode('objectSet',n='CACHE_OBJS')#增加CACHE_OBJS
            else:
                return False
        #------------------------------------------------------------------------------ 
        if not rig.objExists('MESHES'):#是否存在'MESHES'
            reMS = rig.confirmDialog(t = u'警告',
                     m = u'场景中没有找到MESHES!\n是否新建一个？',
                     ma = 'left',
                     button = ('Yes','Cancel'),
                     defaultButton = 'Yes',
                     cancelButton = 'Cancel',
                     dismissString = 'Cancel')
            if 'Yes' == reMS:
                rig.createNode('objectSet',n='MESHES')#增加MESHES
                rig.sets('MESHES',e=1,addElement='CACHE_OBJS')

                return True
            else:
                return False    
            
        else:
           return True
    #===========================================================================
    # 自动增加MODEL下的物体到"MESHES"
    #===========================================================================
    def AutoSets(self):
        setSign = self.FindSets()
        if setSign:
            allMems = rig.sets('CACHE_OBJS',q = True)
            if not ('MESHES' in 'allMems'):
                rig.sets('MESHES',e=1,addElement='CACHE_OBJS')
            model = rig.ls('MODEL')
            if model:#场景中是否有MODEL组
                if 1 == len(model):#检测MODEL组是否有重命名
                    slAllobjs = rig.listRelatives(model[0],c = True,ad = True)
                    if slAllobjs:
                        Meshs = rig.ls(slAllobjs,type = 'mesh')
                        nurbs = rig.ls(slAllobjs,type = 'nurbsSurface')
                        Meshs.extend(nurbs)
                        
                        #------------------------------------------ 检测shape节点重命名
                        allObs = []
                        for obj in Meshs:
                            name = obj.split('|')[-1]
                            objs = rig.ls(name)
                            if 1 < len(objs):#是否有重命名
                                SM_warning(u'物体:'+obj+u'有重命名\n添加失败!!!')
                            else:
                                objParent = rig.listRelatives(objs[0],p = True)[0]
                                if not(objParent in allObs):#是否已经存在allObs中
                                    allObs.append(objParent)
                        
                        #-------------------------------------- 检测Transform节点重命名
                        trasformObjs = []
                        for obj in allObs:
                            name = obj.split('|')[-1]
                            objs = rig.ls(name)
                            if 1 < len(objs):#是否有重命名
                                SM_warning(u'物体:'+obj+u'有重命名\n添加失败!!!')
                            else:
                                if not(objs[0] in trasformObjs):#是否已经存在allObs中
                                    trasformObjs.append(objs[0])
                                            
                        rig.sets(trasformObjs,e = True,addElement='MESHES')
                    else:
                        SM_warning(u'MODEL组下没有找到物体:')
                else:
                    SM_warning(u'场景中MODEL组有重命名:')
            else:
                SM_warning(u'场景中没有MODEL组:')
        
        else:
            pass
        
    #===========================================================================
    # 增加选择的物体到'MESHS'
    #===========================================================================
    def slelectSets(self):
        setSign = self.FindSets()
        if setSign:
            allMems = rig.sets('CACHE_OBJS',q = True)
            if not ('MESHES' in 'allMems'):#
                rig.sets('MESHES',e=1,addElement='CACHE_OBJS')
            slObjs = rig.ls(sl = True)
            if slObjs:#场景中是否有物体被选择
                slAllobjs = rig.listRelatives(slObjs,c = True)
                if slAllobjs:
                    Meshs = rig.ls(slAllobjs,type = 'mesh')
                    nurbs = rig.ls(slAllobjs,type = 'nurbsSurface')
                    Meshs.extend(nurbs)
                    
                    #------------------------------------------ 检测shape节点重命名
                    allObs = []
                    for obj in Meshs:
                        name = obj.split('|')[-1]
                        objs = rig.ls(name)
                        if 1 < len(objs):#是否有重命名
                            SM_warning(u'物体:'+obj+u'有重命名\n添加失败!!!')
                        else:
                            objParent = rig.listRelatives(objs[0],p = True)[0]
                            if not(objParent in allObs):#是否已经存在allObs中
                                allObs.append(objParent)
                    
                    #-------------------------------------- 检测Transform节点重命名
                    trasformObjs = []
                    for obj in allObs:
                        name = obj.split('|')[-1]
                        objs = rig.ls(name)
                        if 1 < len(objs):#是否有重命名
                            SM_warning(u'物体:'+obj+u'有重命名\n添加失败!!!')
                        else:
                            if not(objs[0] in trasformObjs):#是否已经存在allObs中
                                trasformObjs.append(objs[0])
                    
                    if trasformObjs:                    
                        rig.sets(trasformObjs,e = True,addElement='MESHES')

            else:
                SM_warning(u'请选择需要增加的物体!')
        else:
            pass
        
    #===========================================================================
    # 将选择的模型从MESHES中移除
    #===========================================================================
    def removeObjs(self):
        slObjs = rig.ls(sl = True)
        if slObjs:#是否有物体被选择
            if rig.objExists('MESHES'):#MESHES是否存在
                meshSets = rig.sets('MESHES',q = True)#列出MESHES的所有成员.
                for obj in slObjs:
                    if obj in meshSets:#物体是否在MESHES中
                        rig.sets(obj,rm = 'MESHES')
                    else:
                        SM_warning(u'选择的物体:'+obj+u'不在MESHES中')
            else:
                SM_warning(u'在场景中没有找到MESHES')
        else:
            SM_warning(u'请选择需要从MESHES中移除的物体')
#===============================================================================
# 弹出警告窗口
#===============================================================================
def SM_warning(data):
        rig.confirmDialog(t = u'警告',\
                    m = data,\
                    ma = 'left',\
                    button = ('OK'),\
                    defaultButton = 'OK',\
                    cancelButton = 'OK',\
                    dismissString = 'OK')

        
def edo_autoCreateSetAndAddTheRenderMeshes():
    SK_AutoAddSetUI()
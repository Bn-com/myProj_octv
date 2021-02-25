#-*- coding: utf-8 -*-
import os
import pickle
import maya.cmds as rig
import maya.OpenMaya as om
import maya.OpenMayaAnim as omAnim
from RIG.simulation.simulationMain import SM_warning
from RIG.commonly.base import SK_getSkinCluster
#from RIG.tools.IOWeights.IOFile import *

class SK_IOgetOptionUI(object):
    def __init__(self,path):
        self.selectBT = 'OFF'
        self.importWeightBT = 'OFF'
        self.closeAdvancedBT = 'OFF'
        self.slJntBT = 'OFF'
#        self.progressWeightPB = 'OFF'
        self.path = path
        sign = self.loadWeightData()
        if sign:#如果能正确找到文件
            self.displayUI()
        
    def displayUI(self):
        self.IDMTRigGUI='IOgetOptionUI'
        if rig.window(self.IDMTRigGUI,exists=True):
            rig.deleteUI(self.IDMTRigGUI)
        rig.window(self.IDMTRigGUI,title= u'权重选项',menuBar=True,wh=  (325,500),minimizeButton=True,maximizeButton=True)

        self.mainCLT = rig.formLayout(numberOfDivisions=100)
        self.skinTV = rig.textScrollList(ams = True)
        self.jointTV = rig.textScrollList(ams = True)
        
        self.infsPB = rig.progressBar(vis = False)
        self.startBT = rig.button(l = u'开始导入',c = lambda x:self.startCompute())
        #-------------------------------------------------------------- 增加右边按钮选项
        self.column = rig.columnLayout(adj = True)
        rig.button(l = u'打开高级选项',c = lambda x = 0:self.AddtextScrollList())
        

        rig.setParent(self.mainCLT)
        self.deflautAddtextScrollList()
        rig.showWindow(self.IDMTRigGUI)#显示窗口 
        rig.window(self.IDMTRigGUI,e=True,wh=(500,500))#修改窗口大小
    #===========================================================================
    # 载入窗口默认布局    
    #===========================================================================
    def deflautAddtextScrollList(self):
        rig.formLayout( self.mainCLT, edit=True, 
                    #------------------------------------------------ attachFrom
                    attachForm=[
                                (self.skinTV, 'top', 5), (self.skinTV, 'left', 5), 
                                (self.infsPB,'left', 5),(self.infsPB,'right', 5),
                                (self.jointTV,'top', 5),
                                (self.startBT, 'left', 5), (self.startBT, 'bottom', 5), (self.startBT, 'right', 5), 
                                (self.column, 'top', 5), (self.column, 'right', 5) ], 
                    #--------------------------------------------- attachcontrol
                    attachControl=[
                                   (self.skinTV, 'bottom', 5, self.infsPB), 
                                   (self.jointTV,'right', 5 ,self.column),(self.jointTV,'left', 5 ,self.skinTV),(self.jointTV,'bottom', 5 ,self.infsPB),
                                   (self.infsPB, 'bottom', 5, self.startBT), 
                                   (self.column, 'bottom', 5, self.startBT)], 
                    #--------------------------------------------- attachPostion
                    attachPosition=[
                                    (self.skinTV, 'right', 5, 40), 
                                    (self.jointTV,'left',5,40),(self.jointTV,'right',5,80),
                                    (self.column, 'left', 0, 80)], 
                    #------------------------------------------------ attachNone
                    attachNone=(self.startBT, 'top') )
        self.listSkinObj()#载入权重文件列表
        rig.window(self.IDMTRigGUI,e=True,wh=(500,500))#修改窗口大小
    #===========================================================================
    # 载入高级选项面板
    #===========================================================================
    def AddtextScrollList(self):
        
        if self.selectBT == 'OFF':
            self.slBT = rig.button(p = self.column,l = u'载入选择的',c = lambda x = 0:self.loadSelectSkinObj())
            self.selectBT = 'ON'
        if self.importWeightBT == 'OFF':
            self.imBT = rig.button(p = self.column,l = u'自动匹配骨骼',c = lambda x = 0:self.findClosestJnt())
            self.importWeightBT = 'ON'
        if self.slJntBT == 'OFF':
            self.slJBT = rig.button(p = self.column,l = u'导入权重',c = lambda x = 0:self.mulObjWeights())
            self.slJntBT = 'ON'
        if self.closeAdvancedBT == 'OFF':
            self.clBT = rig.button(p = self.column,l = u'关闭高级选项',c = lambda x = 0:self.closeAdvanced())
            self.closeAdvancedBT = 'ON'
#        if self.progressWeightPB == 'OFF':
#            self.infsPB = rig.progressBar(p = self.column,vis = False)
#            self.progressWeightPB = 'ON'
            
        rig.button(self.startBT,e = True,en = False)#按钮失效
        rig.textScrollList(self.skinTV,e = True,ams = False)#禁止多选
        
        self.slSkinTV = rig.textScrollList(p = self.mainCLT)
        self.slJointTV = rig.treeView(p = self.mainCLT, numberOfButtons = 0, abr = False,arp = False)
        rig.formLayout( self.mainCLT, edit=True, 
                    #------------------------------------------------ attachFrom
                    attachForm=[
                                (self.skinTV, 'top', 5), (self.skinTV, 'left', 5), 
                                (self.infsPB,'left', 5),(self.infsPB,'right', 5),
                                (self.jointTV,'top', 5),
                                (self.slJointTV,'top', 5),
                                (self.slSkinTV,'top', 5),
                                (self.startBT, 'left', 5), (self.startBT, 'bottom', 5), (self.startBT, 'right', 5), 
                                (self.column, 'top', 5), (self.column, 'right', 5) ], 
                    #--------------------------------------------- attachcontrol
                    attachControl=[
                                   (self.skinTV, 'bottom', 5, self.infsPB), 
                                   (self.jointTV,'bottom', 5 ,self.infsPB),
                                   (self.slJointTV,'bottom', 5 ,self.infsPB),
                                   (self.slSkinTV,'bottom', 5 ,self.infsPB),
                                   
                                   (self.column, 'bottom', 5, self.infsPB)], 
                    #--------------------------------------------- attachPostion
                    attachPosition=[
                                    (self.skinTV, 'right', 5, 20), 
                                    (self.jointTV,'left',5,20),(self.jointTV,'right',5,40),
                                    (self.slJointTV,'left',5,40),(self.slJointTV,'right',5,60),
                                    (self.slSkinTV,'left',5,60),(self.slSkinTV,'right',5,80),
                                    (self.column, 'left', 0, 80)], 
                    #------------------------------------------------ attachNone
                    attachNone=(self.startBT, 'top') )
        rig.window(self.IDMTRigGUI,e=True,wh=(1000,700))
        
    def closeAdvanced(self):
        rig.button(self.startBT,e = True,en = True)#按钮有效
        rig.textScrollList(self.skinTV,e = True,ams = True)#开启多选
        
        self.selectBT = 'OFF'
        self.importWeightBT = 'OFF'
        self.closeAdvancedBT = 'OFF'
        self.slJntBT = 'OFF'
        rig.deleteUI(self.slBT,self.imBT,self.clBT,self.slJBT,control=True)
        rig.deleteUI(self.slSkinTV,self.slJointTV,control = True)

        
        self.deflautAddtextScrollList()
    #===========================================================================
    # 结束窗口设置
    #===========================================================================
    
    
    #------------------------------------------------------------------ 执行权重导入功能
    def startCompute(self):
        self.allToYes = False#所有没有蒙皮物体都将自动蒙皮
        self.allToNo = False#取消所有操作
        curFilePath = self.path
        childFiles = rig.textScrollList(self.skinTV,q = True,si = True)
        
        cf = rig.textScrollList(self.skinTV,q = True,sii = True)
        if childFiles:
            rig.progressBar(self.infsPB,e = True,maxValue= len(childFiles),vis = True)#显示进度条
            
            for i,fileName in enumerate(childFiles):
                rig.progressBar(self.infsPB, edit=True, step=1)#设置进度条
                filePath = curFilePath+'/'+fileName
                
                #    通过文件名获得物体名和skinCluster
                mesh = fileName.split('.')[0]
                if rig.objExists(mesh):
                    meshShape = IO_getSkinShape(mesh)#获得形节点
                    skin = SK_getSkinCluster(mesh)
                    
                    #    开始写入权重
                    if skin:#已经蒙皮
                        
                        #    获得权重
#                        readFile = open(filePath,'r')
#                        weights = pickle.load(readFile)
#                        readFile.close()

                        infs = rig.skinCluster(skin,q = True,inf = True)
                        if len(self.joints[cf[i] -1]) == len(infs):#权重文件的影响体个数是否与场景中的影响体个数相等
                            IO_setWeights(skin,meshShape,self.allData[cf[i] -1])
                        else:
                            rig.warning(u'导入权重失败!'+u'物体:'+mesh+u'的骨骼个数与权重文件里的骨骼个数不一样.解决方法：删掉蒙皮重新导入权重')
                    else:#没有蒙皮
                        if self.allToYes:
                            skin = IO_getSkin(meshShape,self.allData[cf[i] -1])
                            if skin:
                                IO_setWeights(skin,meshShape,self.allData[cf[i] -1])
                                
                        elif self.allToNo:
                            pass
                        
                        else:
                            reMS = rig.confirmDialog(t = u'警告',
                                                m = u'物体'+mesh+u'没有蒙皮.\n\nYes---将自动蒙皮.\nYesToAll---下次如果物体没有蒙皮将自动蒙皮不会弹出对话框.\nNo---放弃操作\
                                                    \nNoToAll---下次全部放弃操作不会弹出对话框\nCancel---关闭对话框',
                                                ma = 'left',
                                                button = ('Yes','YesToAll','No','NoToAll','Cancel'),
                                                defaultButton = 'YES',
                                                cancelButton = 'Cancel',
                                                dismissString = 'Cancel')
                           
                            if 'Yes' == reMS:
                                skin = IO_getSkin(meshShape,self.allData[cf[i] -1])
                                if skin:
                                    IO_setWeights(skin,meshShape,self.allData[cf[i] -1])
                            elif 'YesToAll' == reMS:
                                self.allToYes = True
                                skin = IO_getSkin(meshShape,self.allData[cf[i] -1])
                                if skin:
                                    IO_setWeights(skin,meshShape,self.allData[cf[i] -1])
                            elif 'No' == reMS:
                                pass
                            
                            elif 'NoToAll' == reMS:
                                self.allToNo = True
                                pass
                            
                            elif 'Cancel' == reMS:
                                pass
                else:
                    SM_warning(u'物体：'+mesh+u'没有找到')
            rig.progressBar(self.infsPB,e = True,vis = False)#隐藏进度条       
        else:
            SM_warning(u'请选择物体')
            
        self.allToYes = False#恢复初始值
        self.allToNo = False#恢复初始值
            
    
    #------------------------------------------------------------------ 载入所有权重文件
    def listSkinObj(self):
       curFilePath = self.path
       childFiles = os.listdir(curFilePath)#列出所有此目录下的文件
       if childFiles:
           rig.textScrollList(self.skinTV,e = True,ra = True)
           rig.textScrollList(self.skinTV,e = True,append = [fileName for fileName in childFiles if 'sc' == fileName.split('.')[-1]],sc = lambda x = 0:self.listInfluence())
    
    #------------------------------------------------------------------ 载入所有权重数据
    def loadWeightData(self):
        curFilePath = self.path
        childFiles = os.listdir(curFilePath)#列出所有此目录下的文件
        signSCFile = [fileName for fileName in childFiles if 'sc' == fileName.split('.')[-1]]
        if signSCFile:
            self.joints = []
            self.allData = []
            
            #    将磁盘上的数据写入内存
            amount = 0
            average = 100/len(childFiles)
            rig.progressWindow(title='正在获得权重......',
                                                    progress=amount,
                                                    status='Sleeping: 0%',
                                                    isInterruptable=True )
            for fp in childFiles:
                    if rig.progressWindow( query=True, isCancelled=True ) :
                            break
            
                    amount += average
            
                    rig.progressWindow( edit=True, progress=amount, status=(fp) )
            
                    readFile = open(curFilePath+'/'+fp,'r')
                    weights = pickle.load(readFile)
                    readFile.close()
                    self.joints.append(weights[0])
                    self.allData.append(weights)
            
            rig.progressWindow(endProgress=1)
            return True
        
        else:
            SM_warning(u'文件夹中没有.SC文件') 
            return False
    
    
    #---------------------------------------------------------------- 载入文件中蒙皮物体的影响体
    def listInfluence(self):
        skinMesh = rig.textScrollList(self.skinTV,q = True,si = True)
        index = rig.textScrollList(self.skinTV,q = True,sii = True)
        jnts = self.joints[index[0]-1]
        rig.textScrollList(self.jointTV,e = True,ra = True)
        rig.textScrollList(self.jointTV,e = True,append = [jnt[0] for jnt in jnts])
        
    #------------------------------------------------------------------- 载入文件中选择的物体
    def loadSelectSkinObj(self):
        allobjs = rig.ls(sl = True)
        
        if allobjs:
            rig.textScrollList(self.slSkinTV,e = True,ra = True)
            for obj in allobjs:
                skin = SK_getSkinCluster(obj)
                if skin:
                    rig.textScrollList(self.slSkinTV,e = True,append = obj,sc = lambda x = 0:self.slInfluence())
                else:
                    SM_warning(u'物体：'+obj+u'没有找到skinCluster,请确定已经蒙皮') 
        
        else:
            SM_warning(u'请先选择物体')
            
    #---------------------------------------------------------------- 载入场景中蒙皮物体的影响体
    def slInfluence(self):
        skinMesh = rig.textScrollList(self.slSkinTV,q = True,si = True)
        index = rig.textScrollList(self.slSkinTV,q = True,sii = True) 
        skin = SK_getSkinCluster(skinMesh)
        
        rig.treeView(self.slJointTV,e = True,ra = True)
        infs = rig.skinCluster(skin,q = True,inf = True)
        rig.treeView(self.slJointTV,e = True,addItem = [(inf,'') for inf in infs])
    
            
    #---------------------------------------------------- 将一个物体的一个影响体的权重拷到另一个物体上
    def mulObjWeights(self):
        sourceMeshs = rig.textScrollList(self.skinTV,q = True,si = True)
        sourceJointIndexs = rig.textScrollList(self.jointTV,q = True,sii = True)
        targetMeshs = rig.textScrollList(self.slSkinTV,q = True,si = True)
        targetJointNames = rig.treeView(self.slJointTV,q = True,si = True)
        
        if targetMeshs and sourceMeshs and targetJointNames and sourceJointIndexs:
            sourceMeshIndexs = rig.textScrollList(self.skinTV,q = True,sii = True)
            mainIndex = sourceMeshIndexs[0] - 1
            
            skin = SK_getSkinCluster(targetMeshs)#获得SkinCluster
            infs = rig.treeView(self.slJointTV,q = True,si = True)#获得目标物体的影响体
            
            sourData = self.allData[mainIndex][1]#获得权重数据
            
            if len(rig.ls(targetMeshs[0]+'.vtx[*]',fl = True)) == len(sourData):
                if len(sourceJointIndexs) == len(infs):

                    lockInfs = self.getLockInfs(infs)#解锁
                    
                    rig.progressBar(self.infsPB,e = True,maxValue= len(infs),vis = True)#显示进度条
                    
                    for num,jnt in enumerate(infs):#迭代选择影响体
                        if not('NONE_JOINT_X' in jnt):#骨骼是否被忽略
                            Index = sourceJointIndexs[num] -1
                            print 'complele:'+jnt
                            for i,data in enumerate(sourData):#迭代所有的点
                                
                                rig.skinPercent(skin,targetMeshs[0]+'.vtx['+str(i)+']', transformValue=[(jnt, data[Index])])
                            rig.setAttr(jnt+'.liw',1)#锁定已完成的影响体
                            rig.progressBar(self.infsPB, edit=True, step=1)#设置进度条
                        else:
                            print u'忽略.......'+jnt
                        
                        
                    self.setUnLockInfs(lockInfs)
                    rig.progressBar(self.infsPB,e = True,vis = False)#隐藏进度条
                else:
                    SM_warning(u'选择的影响体个数不一样') 
            else:
                SM_warning(u'物体拓扑不一样,请选择正确的物体') 
            
        else:
            SM_warning(u'请确定已经正确的选择')   
            
    #-------------------------------------------------------------------- 获得被锁定的影响体并解开权重锁定
    def getLockInfs(self,infs):
        lockInfs = []
        for inf in infs:
            if not('NONE_JOINT_X' in inf):
                if not rig.getAttr(inf+'.liw'):
                    lockInfs.append(inf)
                rig.setAttr(inf+'.liw',False)
        return lockInfs
    #--------------------------------------------------------------------- 锁定影响体
    def setUnLockInfs(self,infs):
        if infs:
            for inf in infs:
                rig.setAttr(inf+'.liw',False)         
    
    
    #------------------------------------------------------------------ 自动匹配最近骨骼
    def findClosestJnt(self):
        sourceMeshs = rig.textScrollList(self.skinTV,q = True,si = True)
        sourceJointIndexs = rig.textScrollList(self.jointTV,q = True,sii = True)
        targetMeshs = rig.textScrollList(self.slSkinTV,q = True,si = True)
        targetJointNames = rig.treeView(self.slJointTV,q = True,si = True) 
        
        if sourceMeshs and targetMeshs:
            sourceJointIndexs = rig.textScrollList(self.skinTV,q = True,sii = True)
            
            skin = SK_getSkinCluster(targetMeshs[0]) 
            targetInfs = rig.skinCluster(skin,q = True,inf = True)
            targetPos = [rig.xform(pos,q = True,t = True,ws = True) for pos in targetInfs]
            sourcePos = [pos[1] for pos in self.joints[sourceJointIndexs[0]-1]]
            
            
            minVal = 0.001
            orderInfs = []
            addNONEJnt = 0
            for spos in sourcePos:
                sign = False
                sv = om.MVector(spos[0],spos[1],spos[2])
                for i,tpos in enumerate(targetPos):
                    tv = om.MVector(tpos[0],tpos[1],tpos[2])
                    minus = sv - tv
                    if(minus.length() < minVal):
                        orderInfs.append(targetInfs[i])
                        sign = True
                        break
                if not sign:
                    orderInfs.append('NONE_JOINT_X'+str(addNONEJnt))
                    addNONEJnt += 1
            
            #-------------------------------------------------------- 设置treeView
            rig.treeView(self.slJointTV,e = True,ra = True)
            rig.treeView(self.slJointTV,e = True,addItem = [(inf,'') for inf in orderInfs])
            for jnt in orderInfs:
                if 'NONE_JOINT_X' in jnt:
                    rig.treeView(self.slJointTV,e = True,lbc = (jnt,0.314,0.185,0.241))           
            
        else:
            SM_warning(u'请确定已经正确的选择')         
    
def IO_setWeights(skinClus,Shape,weights):#获得蒙皮物体权重
    #    得到Ploygon物体
    obj = om.MDagPath()
    com = om.MObject()
    MSobj = om.MSelectionList()
    MSobj.add(Shape)
    MSobj.getDagPath(0,obj)
    
    #    创建MFnSkinCluster
    skin = om.MObject()   
    MSskin = om.MSelectionList()
    MSskin.add(skinClus) 
    MSskin.getDependNode(0,skin)   
    
    skinMFn = omAnim.MFnSkinCluster(skin)
 
    #    influence物体的问题名称和位置
    infPosAndName = []
    infsPaths = om.MDagPathArray()
    skinMFn.influenceObjects(infsPaths)
    for inf in range(infsPaths.length()):
        name = infsPaths[inf].partialPathName()
        pos = rig.xform(name,q = True,t = True,ws = True)
        infPosAndName.append([name,pos])
        
    #   将Python的列表转换为MIntArray
    infIntAarray = om.MIntArray()
    infWeights = om.MDoubleArray()
    infs = [i for i in range(infsPaths.length())]
    om.MScriptUtil.createIntArrayFromList(infs,infIntAarray)
    
    #    迭代Ploygon物体并设置每个点的权重
    setWeights = weights[1]
    iter = om.MItMeshVertex(obj)
    while not iter.isDone():
        #   将Python的列表转换为MDoubleArray
        infWeights = om.MDoubleArray()
        weightsList = setWeights[iter.index()]
        for val in range(len(weightsList)):
            convertDouble = om.MScriptUtil()
            convertDouble.createFromDouble(weightsList[val])
            infWeights.append(convertDouble.asDouble())
       
        com = iter.currentItem()
        # 开始设置权重
        skinMFn.setWeights(obj,com,infIntAarray,infWeights)
        
        iter.next()
#    iter.reset()

def IO_getSkin(meshShape,AllData):
    infs = [data[0] for data in AllData[0]]
    sign = True
    
    for inf in infs:#权重文件中的影响体在场景中是否存在
        if not rig.objExists(inf):
            sign = False
            rig.warning(u'物体:'+inf+u'没有找到，蒙皮失败')
            return False
        
    if sign:
        skin = rig.skinCluster(infs,meshShape,tsb = True)[0]
        return skin

        
        
def IO_getSkinShape(obj):
    skins = []
    shapes = rig.listRelatives(obj,s = True,f = True)
    for shape in shapes:
        
        if 1 < len(rig.ls(shape.split('|')[-1])):#检测是否有重命名
            rig.warning(u'物体：'+shape.split('|')[-1]+u'有重命名')
            
        skin = SK_getSkinCluster(shape)#检测是否存被蒙皮
        if skin:
            skins.append(shape)
            
    if skins:
        if 1 == len(skins):
            return skins[0]
        else:
            rig.warning(u'物体：'+obj+u'有多个形节点并且有多个skinCluster')
            return False
    else:
        rig.warning(u'物体：'+obj+u'没有找到skinCluster')
        return False  
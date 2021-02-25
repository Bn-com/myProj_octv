#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.simulation.importController import SM_controller

def SM_warning(data):
        rig.confirmDialog(t = u'警告',\
                    m = data,\
                    ma = 'left',\
                    button = ('OK'),\
                    defaultButton = 'OK',\
                    cancelButton = 'OK',\
                    dismissString = 'OK')
    
def SM_objExistsAttr(attr):
    if rig.attributeQuery():
        pass

def SM_importControllerTem(ployName,col,row,conPre,size,shape,color):
    if not ployName:
        rig.confirmDialog(t = u'警告',\
                            m = u'没有载入ploygon物体',\
                            ma = 'left',\
                            button = ('OK'),\
                            defaultButton = 'OK',\
                            cancelButton = 'OK',\
                            dismissString = 'OK')
    elif 'Pre_3_M' == conPre:
        rig.confirmDialog(t = u'警告',\
                            m = u'请输入新的控制器名称',\
                            ma = 'left',\
                            button = ('OK'),\
                            defaultButton = 'OK',\
                            cancelButton = 'OK',\
                            dismissString = 'OK')
    else:
        
        if rig.objExists(conPre+'_0_P'):
            allPreCons = rig.ls(conPre+'_*_P')
            nums = [int(i.split('_')[-2]) for i in allPreCons]
            nums.sort()
            start = nums[-1]+1
        else:
            start = 0
                    
        controller = SM_controller(ployName,col,row,conPre,size,shape,color,start)
        cons = controller.createController()
    
    
class SM_createSetup(object):
    def __init__(self,ployName,sign = True):
        self.ployName = ployName
        self.key = 'M'
        self.locatorModel = ployName
        
        if sign:
            self.runSetup()
        
    def runSetup(self):
        if not self.ployName:
            rig.confirmDialog(t = u'警告',\
                                m = u'没有载入ploygon物体',\
                                ma = 'left',\
                                button = ('OK'),\
                                defaultButton = 'OK',\
                                cancelButton = 'OK',\
                                dismissString = 'OK')
        
        else:
            #=======================================================================
            # 生成毛囊
            #=======================================================================
            Mesh =  self.ployName 
            MeshShape = rig.listRelatives(Mesh,s = True,ni = True)[0]
            FOLS = []
            
            
            if not rig.objExists(Mesh+'_CLM'): #增加closestPointOnMesh节点
                CLM = rig.createNode('closestPointOnMesh',n = Mesh+'_CLM',ss = True)
                rig.connectAttr(MeshShape+'.outMesh',CLM+'.inMesh')
            else:
                CLM = Mesh+'_CLM'
                
            if not rig.objExists(Mesh+'_ScaleSM_GRP'): #增加毛囊缩放组节点
                self.FolScale = rig.group(empty = True,n = Mesh+'_ScaleSM_GRP')
                rig.addAttr(self.FolScale,at = 'float',ln = 'vis',dv = 0)#增加控制器隐藏属性
            else:
                self.FolScale = Mesh+'_ScaleSM_GRP'    
                
            self.allCons = rig.listConnections(self.locatorModel+'.sign',s = False,d = True) #列出所有定位控制器
            if self.allCons:
                for con in self.allCons:
                    if rig.objExists(con+'_FOL'):
                        warning(u'毛囊:'+con+u'_FOL已经存在')
                        continue
                    
                    pos = rig.xform(con,q = True,t = True,ws = True)
                    rig.setAttr(CLM+'.inPositionX',pos[0])
                    rig.setAttr(CLM+'.inPositionY',pos[1])
                    rig.setAttr(CLM+'.inPositionZ',pos[2])
                    U = rig.getAttr(CLM+'.result.parameterU')
                    V = rig.getAttr(CLM+'.result.parameterV') 
                    
                    FOLShape = rig.createNode('follicle',n = con.replace('_P','_'+self.key)+'_FOLShape',ss = True)
                    rig.hide(FOLShape)
                    rig.connectAttr(MeshShape+'.worldMesh[0]',FOLShape+'.inputMesh')
                    FOL = rig.listRelatives(FOLShape,p = True)[0]
                    
                                   
                    rig.connectAttr(self.FolScale+'.scale',FOL+'.scale')
                    rig.connectAttr(MeshShape+'.worldMatrix[0]',FOL+'.inputWorldMatrix')
                    
                    newFol = rig.rename(FOL,con.replace('_P','_'+self.key)+'_FOL')
                    rig.connectAttr(FOLShape+'.outTranslate',newFol+'.translate')
                    rig.connectAttr(FOLShape+'.outRotate',newFol+'.rotate')
                    rig.setAttr(FOLShape+'.parameterU',U)
                    rig.setAttr(FOLShape+'.parameterV',V)
                    rig.setAttr(FOLShape+'.simulationMethod',0)
                    
                    FOLS.append(newFol)
                    
                self.origenCurve = rig.group(self.allCons,n = self.ployName+'_origen_ALL_Curves')
            else:
                warning(u'没有找定位控制器')
            #=======================================================================
            # 生成控制器和骨骼
            #=======================================================================
            if FOLS:
                jnts = []
                for fol in FOLS:
                    matFol = rig.getAttr(fol+'.worldMatrix')
                    rig.select(cl = True)
                    
                    JNT = rig.joint(n = fol.replace('_'+self.key+'_FOL','_JNT'+self.key))
                    rig.hide(JNT)
                    grpJnt = rig.group(JNT,n = JNT+'_GRP')
                    con = rig.duplicate(fol.replace('_'+self.key+'_FOL','_P'),n = fol.replace('_'+self.key+'_FOL','_'+self.key))[0]
                    rig.xform(con,t = (0,0,0),wd = True)
                    grpA = rig.group(con,n = con+'_GRP_A')
                    grpB = rig.group(grpA,n = con+'_GRP_B')
                    grpC = rig.group(grpB,n = con+'_GRP_C')
                    
                    rig.parent(grpJnt,con)
                    rig.xform(grpC,matrix = matFol)
                    rig.parent(grpC,fol)
                    
                    jnts.append(JNT)
                    
                    rig.connectAttr(self.FolScale+'.vis',grpA+'.visibility')
                    
                #复制出新的模型对其蒙皮  
                if not rig.objExists(self.ployName+'_SKIN'):
                    self.skinMesh = rig.duplicate(self.ployName,n = self.ployName+'_SKIN')[0]
                    skin = rig.skinCluster(jnts,self.skinMesh)[0]
                    
                    #连接矩阵
                    infs = rig.skinCluster(skin,q = True,inf = True)
                    for i,inf in enumerate(infs):
                        linkGrp = inf.replace('_JNT'+self.key,'_'+self.key+'_GRP_C')
                        rig.connectAttr(linkGrp+'.worldInverseMatrix[0]',skin+'.bindPreMatrix['+str(i)+']')
                        
                   
                else:
                    warning(u'蒙皮物体已经存在')
                    
                self.FOLGRP = rig.group(FOLS,n = self.ployName+'_ALL_FOL_GRP')
                rig.blendShape(self.ployName,self.skinMesh,n = self.ployName+'_BS',foc = True,w = (0,1))#创建blendShape
                
                    
                    
def SM_AutoNclothSetup(ployName,masterName):
    
    if not ployName:
        SM_warning(u'没有载入Ploygon物体')
        
    elif not rig.objExists(ployName):
        SM_warning(u'场景中没有名字为:'+ployName+u'物体')
        
    elif not masterName:
        SM_warning(u'没有载入增加属性的控制器')
        
    elif not rig.objExists(masterName):
        SM_warning(u'场景中没有找到增加属性的控制器名字为：'+masterName+u'物体')
                
    else:
        #生成布料解算前的设置
        preSetup = SM_createSetup(ployName)
        preScaleGrp = preSetup.FolScale
        preFolGRP = preSetup.FOLGRP
        preOrigenObj = preSetup.ployName
        preCopyObj = preSetup.skinMesh
        
        #生成ncloth
        import maya.mel as mel
        rig.select(preCopyObj)
        mel.eval("createNCloth 0")
        nclothShape = rig.ls(sl = True)[0]
        nucleus = rig.listConnections(nclothShape,s = False,d = True,type = 'nucleus')[0]
        ncloth = rig.listRelatives(nclothShape,p = True)[0]
#        rig.rename(ncloth,preCopyObj+'_ncloth')
        
    
        #生成布料解算后的设置        
        curSM = SM_createSetup(ployName+'_SKIN',False)
        curSM.key = 'B'
        curSM.locatorModel = ployName
        curSM.runSetup()
        
        ScaleGrp = curSM.FolScale
        FolGRP = curSM.FOLGRP
        OrigenObj = curSM.ployName
        CopyObj = curSM.skinMesh    
        
        #连接属性并整理层级
        if not rig.attributeQuery('DynamicCtrlCloak',node = masterName,ex = True):
            rig.addAttr(masterName,at = 'enum',ln = 'DynamicCtrlCloak',en = 'Off:On:',dv = 0,k = True)
            
        if not rig.attributeQuery('StartFrame',node = masterName,ex = True):
            rig.addAttr(masterName,at = 'long',ln = 'StartFrame',dv = 980,k = True)
            
        if not rig.attributeQuery('PrimaryDressCtrl',node = masterName,ex = True):
            rig.addAttr(masterName,at = 'enum',ln = 'PrimaryDressCtrl',en = 'Off:On:',dv = 0,k = True)
            
        if not rig.attributeQuery('SecondaryDressCtrl',node = masterName,ex = True):
            rig.addAttr(masterName,at = 'enum',ln = 'SecondaryDressCtrl',en = 'Off:On:',dv = 0,k = True)
            
        if not rig.attributeQuery('primaryHairCtrl',node = masterName,ex = True):
            rig.addAttr(masterName,at = 'enum',ln = 'primaryHairCtrl',en = 'Off:On:',dv = 0,k = True)
            
        if not rig.attributeQuery('SecondaryHairSwitch',node = masterName,ex = True):
            rig.addAttr(masterName,at = 'enum',ln = 'SecondaryHairSwitch',en = 'Off:On:',dv = 0,k = True)
            
        
        rig.connectAttr(masterName+'.StartFrame',nucleus+'.startFrame',f = True)
        rig.connectAttr(masterName+'.DynamicCtrlCloak',nclothShape+'.isDynamic',f = True)
        rig.connectAttr(masterName+'.DynamicCtrlCloak',nucleus+'.enable',f = True)
        rig.connectAttr(masterName+'.PrimaryDressCtrl',preScaleGrp+'.vis',f = True)
        rig.connectAttr(masterName+'.SecondaryDressCtrl',ScaleGrp+'.vis',f = True)

        
        FolsGRP = rig.group(preFolGRP,FolGRP,n = ployName+'_All_SM_Follicles')
        ScaleGRP = rig.group(preScaleGrp,ScaleGrp,n = ployName+'_All_SM_Scale')
        ModelGRP = rig.group(ployName,preCopyObj,CopyObj,n = ployName+'_Model_SM_GRP')
        deformerGRP = rig.group(FolsGRP,ScaleGRP,ModelGRP,n = ployName+'_Deformers_SM_GRP')
#------------------------------------------------------------------------------ 
        if not rig.objExists(ployName+'_SkinMesh'):
            skinMesh = rig.rename(ployName,ployName+'_SkinMesh')
        else:
            SM_warning(u'场景中已经存在:'+ployName+'_SkinMesh'+u'请删除该物体或将其改名')
#------------------------------------------------------------------------------ 
        if not rig.objExists(ployName+'_ClothMesh'):
            clothMesh = rig.rename(preCopyObj,ployName+'_ClothMesh')
        else:
            SM_warning(u'场景中已经存在:'+ployName+'_ClothMesh'+u'请删除该物体或将其改名')
#------------------------------------------------------------------------------ 
        if not rig.objExists(ployName+'_WrapMesh'):
            wrapMesh = rig.rename(CopyObj,ployName+'_WrapMesh')
        else:
            SM_warning(u'场景中已经存在:'+ployName+'_WrapMesh'+u'请删除该物体或将其改名')
#------------------------------------------------------------------------------ 
        if not rig.objExists(ployName+'_ncloth'):
            rig.rename(ncloth,ployName+'_ncloth')
        else:
            SM_warning(u'场景中已经存在:'+ployName+'_ncloth'+u'请删除该物体或将其改名')
#------------------------------------------------------------------------------ 
        if not rig.objExists(ployName+'_nucleus'):
            rig.rename(nucleus,ployName+'_nucleus')
        else:
            SM_warning(u'场景中已经存在:'+ployName+'_nucleus'+u'请删除该物体或将其改名')
#------------------------------------------------------------------------------ 
  
        rig.hide(skinMesh,clothMesh) 
        
        
        rig.delete(preSetup.origenCurve)#删除定位控制器

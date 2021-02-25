#-*- coding: utf-8 -*-
import os
import pickle
import maya.cmds as rig
import maya.OpenMaya as om
import maya.OpenMayaAnim as omAnim
from RIG.simulation.simulationMain import SM_warning
from RIG.commonly.base import SK_getSkinCluster
from RIG.tools.IOWeights.IOgetOptionUI import SK_IOgetOptionUI

def IO_newFile(allPolygon = False):
    filePath = rig.fileDialog(m=1)
    if filePath:
        if allPolygon:
            weightObjs = allPolygon
        else:
            weightObjs = rig.ls(sl = True)
        
        if weightObjs:
            os.mkdir(filePath)
            
            amount = 0
            average = 100/len(weightObjs)
            rig.progressWindow(title= u'正在导出权重..........',
                                                    progress=amount,
                                                    status='Sleeping: 0%',
                                                    isInterruptable=True )
            for skinMesh in weightObjs:
                    if rig.progressWindow( query=True, isCancelled=True ) :
                            break
            
                    amount += average
            
                    rig.progressWindow( edit=True, progress=amount, status=(skinMesh) )
            

                    skin = SK_getSkinCluster(skinMesh)
                    if(skin):
                        #    将权重信息写到磁盘
                        Shape = IO_getSkinShape(skinMesh)  
                        if Shape:  
                            weights = IO_getWeights(skin,Shape)
                            newFile = open(filePath+'/'+skinMesh+'.sc','w')
                            pickle.dump(weights,newFile)
                            newFile.close()
                        else:
                            rig.warning(u'物体：'+skinMesh+u'没有找的Shape节点')
                        
                    else:
                        SM_warning(u'物体：'+skinMesh+u'没有找到skinCluster,请确定已经蒙皮')   
            
            rig.progressWindow(endProgress=1)
            
        else:
            SM_warning(u'请选择需要导出权重的物体')  

def IO_getFile():#获得权重文件
    version = rig.about(v = True)
    signV = version.split()[0]
    if '2011' == signV:
        filePath = rig.fileDialog2( dialogStyle=3,fm = 3,okCaption = 'OK',cancelCaption = 'cannel')
    else:
        PathAndFile = rig.fileDialog(m=0,dm = '*.sc')
        filePath = os.path.split(PathAndFile)

    if filePath:
        curFilePath = filePath[0]
        
        childFiles = os.listdir(curFilePath)#列出所有此目录下的文件
        if childFiles:
            SK_IOgetOptionUI(curFilePath)
        else:
            SM_warning(u'此文件夹为空')





def IO_getWeights(skinClus,Shape):#获得蒙皮物体权重
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
    
    #    迭代Ploygon物体并获得每个点的权重
    allWeights = []
    iter = om.MItMeshVertex(obj)
    while not iter.isDone():
        com = iter.currentItem()
        skinMFn.getWeights(obj,com,infIntAarray,infWeights)
        allWeights.append([v for v in infWeights])
        
        iter.next()
        
    #    返回数据
    data = [infPosAndName,allWeights]
    return data
  
  

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

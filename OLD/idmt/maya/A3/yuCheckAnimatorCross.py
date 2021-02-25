# -*- coding: utf-8 -*-
'''
Created on 2017

@author: yufengsheng
'''
from maya.cmds import *
import maya.mel as mel
import sys

if not pluginInfo('SOuP',q=1,l=1):
    loadPlugin('SOuP', qt=True)

def yuCheckAnimatorWin():
	windowName='checkAnimatorWin'
	if(window(windowName,exists=1)):
		deleteUI(windowName)
	window(windowName,title=u'动画穿插检查工具',mxb=0,wh=(514,124))
	columnLayout(adj=1)
	formLayout('mainForm')
	intSliderGrp('smoothLevelTex',field=1,label=u'Smooth等级:',minValue=0,maxValue=10,fieldMinValue=0,fieldMaxValue=10,value=3)
	button('smoothCreateBut',label=u'创建smooth',h=30,c='createSmoothCmd()')
	button('clearSmoothClusterBut',label=u'清除Smooth和Cluster',h=30,c='removeSmooth_ClusterCmd()')
	floatSliderGrp('boundingObjectRadiusTex',field=1,label=u'BoudingObject半径:',step=0.001,minValue=0,maxValue=1,fieldMinValue=0,fieldMaxValue=1,value=0.025,cc='setBoundingObjRadiusCmd()')
	button('boundingObjectRadiusBut',label=u'修改半径',h=30,w=150,c='setBoundingObjRadiusCmd()')
	button('restoreSelectedCmdBut',label=u'清除所选的检查',w=255,h=30,c='restoreSelectedCmd()')
	button('restoreAllCmdBut',label=u'清除所有检查',w=255,h=30,c='restoreAllCmd()')
	formLayout('mainForm',e=1,af=[('smoothLevelTex','left',-70),('smoothLevelTex','top',3),('boundingObjectRadiusTex','left',-35)],
	           ac=[('smoothCreateBut','left',5,'smoothLevelTex'),('clearSmoothClusterBut','left',5,'smoothCreateBut'),
	           ('boundingObjectRadiusTex','top',10,'smoothLevelTex'),
	           ('boundingObjectRadiusBut','top',10,'smoothLevelTex'),
	           ('boundingObjectRadiusBut','left',5,'boundingObjectRadiusTex'),
	           ('restoreSelectedCmdBut','top',10,'boundingObjectRadiusTex'),
	           ('restoreAllCmdBut','top',10,'boundingObjectRadiusTex'),
	           ('restoreAllCmdBut','left',2,'restoreSelectedCmdBut')])
	setParent('..')
	button('checkCmdBut',label=u'创建检查',c='checkCmd()')
	setParent('..')
	showWindow(windowName)

def checkCmd():
    TransformName=''
    boudingObjName=''
    attributeTransferName=''
    objShapeNames=[]
    objs=ls(sl=1)
    checkNodeGrp='checkNode_grp'
    if not objExists(checkNodeGrp):
        createNode('transform',n=checkNodeGrp)
    for i in range(0,len(objs)):
        objShapeNames=listRelatives(objs[i],shapes=1,ni=1)
        if i==0:
            #判断物体有没有把worldMesh[0]输出给boudingObject
            if not listConnections(objShapeNames[0]+'.worldMesh[0]',s=0,d=1) or listConnections(objShapeNames[0]+'.worldMesh[0]',s=0,d=1)[0].find('boudingObject')<0:
                radiusVal=floatSliderGrp('boundingObjectRadiusTex',q=1,v=1)
                TransformName=createNode('transform',n=objs[i]+'boudingObject')
                boudingObjName=createNode('boundingObject',n=objs[i]+'boudingObjectShape',p=TransformName)
                setAttr(boudingObjName+'.type',3)
                setAttr(boudingObjName+'.pointRadius',radiusVal)
                setAttr(boudingObjName+'.pointColor',0,1,0,type='double3')
                boudingObjShapeName=listRelatives(objs[i],shapes=1,ni=1)
                connectAttr(boudingObjShapeName[0]+'.worldMesh[0]',boudingObjName+'.inMesh')
                parent(TransformName,checkNodeGrp)
            else:
                print '已经创建boundingObject'
                boudingObjName=listConnections(objShapeNames[0]+'.worldMesh[0]',s=1)[0]            
        else:
            #判断inMesh节点是否被连接
            if listConnections(objShapeNames[0]+'.inMesh',s=1):
                #判断inMesh节点是否被arrayToPointColor连接
                if listConnections(objShapeNames[0]+'.inMesh',s=1)[0].find('_arrayToPointColor')==-1:
                    attributeTransferName=createNode('attributeTransfer',n=objs[i]+'attributeTransfer')
                    setAttr(attributeTransferName+'.color',1)
                    setAttr(attributeTransferName+'.solidAlpha',1)
                    #判断attributeTransfer节点的boundingObjects[0]是否被连接
                    if not listConnections(attributeTransferName+'.boundingObjects[0]',s=1):
                        connectAttr(boudingObjName+'.outData',attributeTransferName+'.boundingObjects[0]')
                        connectAttr(boudingObjName+'.outParentMatrix',attributeTransferName+'.boundingObjects[0].boundParentMatrix')
                    else:
                        attributeTransferAttrs=getAttr(attributeTransferName+'.boundingObjects',mi=1)
                        for attributeTransferAttr in attributeTransferAttrs:
                            #判断attributeTransfer节点的boundingObjects是否被连接
                            if not listConnections(attributeTransferName+'.boundingObjects['+str(attributeTransferAttr)+']',s=1):
                                connectAttr(boudingObjName+'.outData',attributeTransferName+'.boundingObjects['+str(attributeTransferAttr)+']')
                                connectAttr(boudingObjName+'.outParentMatrix',attributeTransferName+'.boundingObjects['+str(attributeTransferAttr)+'].boundParentMatrix')
                    if getAttr(objShapeNames[0]+'.displayColors')==0:
                        setAttr(objShapeNames[0]+'.displayColors',1)
                    objOutputGeoAttr=listConnections(objShapeNames[0]+'.inMesh',s=1,p=1)
                    connectAttr(objOutputGeoAttr[0],attributeTransferName+'.inGeometry') 
                    #connectAttr(attributeTransferName+'.outGeometry',clusterGeo[0]+'.inMesh',force=1)
                    arrayDataContainerName=soup().create('arrayDataContainer')
                    arrayDataContainerName=rename(arrayDataContainerName,objs[i]+'arrayDataContainer')
                    arrayToPointColorName=createNode('arrayToPointColor',n=objs[i]+'arrayToPointColor')
                    connectAttr(attributeTransferName+'.outRgbaPP',arrayDataContainerName+'.inArray')
                    connectAttr(arrayDataContainerName+'.outArray',arrayToPointColorName+'.inRgbaPP')
                    connectAttr(attributeTransferName+'.outGeometry',arrayToPointColorName+'.inGeometry')
                    connectAttr(arrayToPointColorName+'.outGeometry',objShapeNames[0]+'.inMesh',force=1)
                else:
                    connectToMeshNode=listConnections(objShapeNames[0]+'.inMesh',s=1)[0]
                    attributeTransferName=listConnections(connectToMeshNode,s=1)[2]
                    #判断attributeTransfer节点的boundingObjects[0]是否被连接
                    if not listConnections(attributeTransferName+'.boundingObjects[0]',s=1):
                        connectAttr(boudingObjName+'.outData',attributeTransferName+'.boundingObjects[0]')
                        connectAttr(boudingObjName+'.outParentMatrix',attributeTransferName+'.boundingObjects[0].boundParentMatrix')
                    else:
                        attributeTransferAttrs=getAttr(attributeTransferName+'.boundingObjects',mi=1)
                        for i in range(0,len(attributeTransferAttrs)):
                            #判断attributeTransfer节点的哪个boundingObjects属性被连接
                            if not listConnections(attributeTransferName+'.boundingObjects['+str(attributeTransferAttrs[i])+']',s=1):
                                connectAttr(boudingObjName+'.outData',attributeTransferName+'.boundingObjects['+str(attributeTransferAttrs[i])+']')
                                connectAttr(boudingObjName+'.outParentMatrix',attributeTransferName+'.boundingObjects['+str(attributeTransferAttrs[i])+'].boundParentMatrix')
                            elif i>=len(attributeTransferAttrs)-1:
                                connectAttr(boudingObjName+'.outData',attributeTransferName+'.boundingObjects['+str(attributeTransferAttrs[i]+1)+']')
                                connectAttr(boudingObjName+'.outParentMatrix',attributeTransferName+'.boundingObjects['+str(attributeTransferAttrs[i]+1)+'].boundParentMatrix')
            else:
                if not ls(objs[i]+'cluster'):
                    clusterName=cluster(objs[i],relative=0,n=objs[i]+'cluster',)
                    attributeTransferName=createNode('attributeTransfer',n=objs[i]+'attributeTransfer')
                    setAttr(attributeTransferName+'.color',1)
                    setAttr(attributeTransferName+'.solidAlpha',1)
                    clusterGeo=cluster(clusterName[0],q=1,g=1)                                        
                    if not listConnections(attributeTransferName+'.boundingObjects[0]',s=1):
                        connectAttr(boudingObjName+'.outData',attributeTransferName+'.boundingObjects[0]')
                        connectAttr(boudingObjName+'.outParentMatrix',attributeTransferName+'.boundingObjects[0].boundParentMatrix')
                    else:
                        attributeTransferAttrs=getAttr(attributeTransferName+'.boundingObjects',mi=1)
                        for attributeTransferAttr in attributeTransferAttrs:
                            if not listConnections(attributeTransferName+'.boundingObjects['+str(attributeTransferAttr)+']',s=1):
                                connectAttr(boudingObjName+'.outData',attributeTransferName+'.boundingObjects['+str(attributeTransferAttr)+']')
                                connectAttr(boudingObjName+'.outParentMatrix',attributeTransferName+'.boundingObjects['+str(attributeTransferAttr)+'].boundParentMatrix')
                    if getAttr(clusterGeo[0]+'.displayColors')==0:
                        setAttr(clusterGeo[0]+'.displayColors',1)
                    connectAttr(clusterName[0]+'.outputGeometry[0]',attributeTransferName+'.inGeometry') 
                    #connectAttr(attributeTransferName+'.outGeometry',clusterGeo[0]+'.inMesh',force=1)
                    #parent(clusterName[1],checkNodeGrp)
                    arrayDataContainerName=soup().create('arrayDataContainer')
                    arrayDataContainerName=rename(arrayDataContainerName,objs[i]+'arrayDataContainer')
                    arrayToPointColorName=createNode('arrayToPointColor',n=objs[i]+'arrayToPointColor')
                    connectAttr(attributeTransferName+'.outRgbaPP',arrayDataContainerName+'.inArray')
                    connectAttr(arrayDataContainerName+'.outArray',arrayToPointColorName+'.inRgbaPP')
                    connectAttr(attributeTransferName+'.outGeometry',arrayToPointColorName+'.inGeometry')
                    connectAttr(arrayToPointColorName+'.outGeometry',clusterGeo[0]+'.inMesh',force=1)
                else:
                    connectToMeshNode=listConnections(objShapeNames[0]+'.inMesh',s=1)[0]
                    attributeTransferName=listConnections(connectToMeshNode,s=1)[2]
                    #判断attributeTransfer节点的boundingObjects[0]是否被连接
                    if not listConnections(attributeTransferName+'.boundingObjects[0]',s=1):
                        connectAttr(boudingObjName+'.outData',attributeTransferName+'.boundingObjects[0]')
                        connectAttr(boudingObjName+'.outParentMatrix',attributeTransferName+'.boundingObjects[0].boundParentMatrix')
                    else:
                        attributeTransferAttrs=getAttr(attributeTransferName+'.boundingObjects',mi=1)
                        for i in range(0,len(attributeTransferAttrs)):
                            #判断attributeTransfer节点的哪个boundingObjects属性被连接
                            if not listConnections(attributeTransferName+'.boundingObjects['+str(attributeTransferAttrs[i])+']',s=1):
                                connectAttr(boudingObjName+'.outData',attributeTransferName+'.boundingObjects['+str(attributeTransferAttrs[i])+']')
                                connectAttr(boudingObjName+'.outParentMatrix',attributeTransferName+'.boundingObjects['+str(attributeTransferAttrs[i])+'].boundParentMatrix')
                            elif i>=len(attributeTransferAttrs)-1:
                                connectAttr(boudingObjName+'.outData',attributeTransferName+'.boundingObjects['+str(attributeTransferAttrs[i]+1)+']')
                                connectAttr(boudingObjName+'.outParentMatrix',attributeTransferName+'.boundingObjects['+str(attributeTransferAttrs[i]+1)+'].boundParentMatrix')                
                            
def createSmoothCmd():
    smoothLevelValue=intSliderGrp('smoothLevelTex',q=1,value=1)
    objName=ls(sl=1,l=1)[0].split('|')[len(ls(sl=1,l=1)[0].split('|'))-1]
    temp_smoothName=polySmooth(c=0,dv=smoothLevelValue)
    smoothName=rename(temp_smoothName,objName+'Smooth')

def restoreAllCmd():
    grpName=ls('checkNode_grp',tr=1)[0]
    if grpName:
        delete(grpName)
    #boundingObjectNodes=ls('*:*boudingObject',tr=1)
    #if boundingObjectNodes:
    #    delete(boundingObjectNodes) 
    arrayToPointColorNodes=ls(type='arrayToPointColor')
    for arrayToPointColorNode in arrayToPointColorNodes:
        connectMesh=listConnections(arrayToPointColorNode,s=0,d=1,p=1)[0]
        attributeTransferNode=listConnections(arrayToPointColorNode,s=1,d=0,p=1)[1].split('.')[0]
        arrayDataContainerNode=listConnections(arrayToPointColorNode,s=1,d=0,p=1)[0].split('.')[0]
        timeToUnitNode=listConnections(arrayDataContainerNode,s=1,d=0,p=1)[0].split('.')[0]
        delete(timeToUnitNode)
        outGeoNode=listConnections(attributeTransferNode+'.inGeometry',s=1,d=0,p=1)[0]
        connectAttr(outGeoNode,connectMesh,force=1)
        setAttr(connectMesh.split('.')[0]+'.displayColors',0)
    if arrayToPointColorNodes:
        delete(arrayToPointColorNodes)
    
    arrayDataContainerNodes=ls(type='arrayDataContainer')
    if arrayDataContainerNodes:
        delete(arrayDataContainerNodes)
    
    attributeTransferNodes=ls(type='attributeTransfer')
    if attributeTransferNodes:
        delete(attributeTransferNodes)
    smoothNames=ls('*:*Smooth*',typ='polySmoothFace')
    if len(smoothNames)>0:
        for smoothName in smoothNames:
            setAttr(smoothName+'.divisions',0)
        #delete(smoothNames)


def restoreSelectedCmd():
    #boundingObjectNodes=ls('*:*boudingObject',tr=1)
    #if boundingObjectNodes:
    #    delete(boundingObjectNodes)
    selObjNames=ls(sl=1)
    okAttrs=[]
    boundingObjNodes=[]
    for selObj in selObjNames:
        arrayToPointColorNode=ls(selObj+'arrayToPointColor',type='arrayToPointColor')[0]
        connectMesh=listConnections(arrayToPointColorNode,s=0,d=1,p=1)[0]
        attributeTransferNode=listConnections(arrayToPointColorNode,s=1,d=0,p=1)[1].split('.')[0]
        attributeTransferInMeshSource=listConnections(attributeTransferNode,s=1,d=0,p=0)[2]
        arrayDataContainerNode=listConnections(arrayToPointColorNode,s=1,d=0,p=1)[0].split('.')[0]
        timeToUnitNode=listConnections(arrayDataContainerNode,s=1,d=0,p=1)[0].split('.')[0]
        delete(timeToUnitNode)
        outGeoNode=listConnections(attributeTransferNode+'.inGeometry',s=1,d=0,p=1)[0]
        connectAttr(outGeoNode,connectMesh,force=1)
        tmpBoundingObjNodes=listConnections(attributeTransferNode,s=1,d=0)
        for i in range(0,len(tmpBoundingObjNodes)):
            if i%2==0:
                if tmpBoundingObjNodes[i].find('boudingObject')>0:
                    boundingObjNodes.append(tmpBoundingObjNodes[i])
        delete(arrayToPointColorNode)
        #if nodeType(attributeTransferInMeshSource)=='cluster':
        #    delete(clusterOutMesh+'Orig')
        #delete(arrayDataContainerNode)
        #delete(attributeTransferNode)
        

        smoothNames=ls(selObj+'Smooth*',typ='polySmoothFace')
        smoothInMeshNodes=''
        if len(smoothNames)>0:
            for smoothName in smoothNames:
                setAttr(smoothName+'.divisions',0)
            #smoothInMeshNode=listConnections(smoothNames[0],s=1,d=0,p=1)[0].split('.')[0]   
            #delete(smoothNames)
            #delete(smoothInMeshNode)
        setAttr(connectMesh.split('.')[0]+'.displayColors',0)
    #去掉数组里重复的元素
    for i in range(len(boundingObjNodes)-1,-1,-1):
        if boundingObjNodes.count(boundingObjNodes[i])>1:
            boundingObjNodes.pop(i)

    if len(boundingObjNodes)>0:
        for boundingObjNode in boundingObjNodes:
            boundingObjShape=listRelatives(boundingObjNode,c=1)[0]
            if not listConnections(boundingObjShape,s=0,d=1):
                delete(boundingObjNode)
                    
    checkNodeGrp='checkNode_grp'
    if objExists(checkNodeGrp):
        if listRelatives(checkNodeGrp,c=1)==None:
            delete(checkNodeGrp)
        

def removeSmooth_ClusterCmd():
    selObjs=ls(sl=1,l=1)
    for selObj in selObjs:
        selObjName=selObj.split('|')[len(selObj.split('|'))-1]
        smoothNames=ls(selObjName+'Smooth*',typ='polySmoothFace')
        clusterNames=ls(selObjName+'cluster*',typ='cluster')    
    
        if len(smoothNames)>0:
            smoothInMeshNode=listConnections(smoothNames[0],s=1,d=0,p=1)[0].split('.')[0]           
            delete(smoothNames)
            if nodeType(smoothInMeshNode)=='mesh':
                delete(smoothInMeshNode)

        if len(clusterNames)>0:
            for clusterName in clusterNames:
                clusterOutMesh=listConnections(clusterName+'.outputGeometry[0]',s=1,p=1)[0].split('.')[0]
                delete(clusterOutMesh+'Orig')
            delete(clusterNames)
          
                
                
def setBoundingObjRadiusCmd():
    selBoundingObjs=ls(sl=1)
    radiusVal=floatSliderGrp('boundingObjectRadiusTex',q=1,v=1)
    for boundingObjNode in selBoundingObjs:
        boundingObjShape=listRelatives(boundingObjNode,c=1)[0]
        setAttr(boundingObjShape+'.pointRadius',radiusVal)
    

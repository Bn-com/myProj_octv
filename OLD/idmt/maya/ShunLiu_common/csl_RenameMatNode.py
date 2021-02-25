# # -*- coding: utf-8 -*-
# 【通用】【材质节点重命名工具】
#  Author : 韩虹
#  Data   : 2014_07
#  Mender:韩虹
#  Data  :2014_07
# import sys
# sys.path.append('D:\\')






import maya.cmds as mc
import maya.mel as mel
import os
import shutil 
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
class csl_RenameMatNode(object):
    def __init__(self):
        # namespace清理
        pass

    def csl_RenameMatNodeRecord(self,nodeName):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        Prefix=shotInfos[1]  
        SGs=mc.ls(type='shadingEngine')
        SGs.remove('initialParticleSE')
        SGs.remove('initialShadingGroup')
        oldName=[]
        NewName=[]
        Nodes=[]
        shadeNewName=''
        midName=''
        if SGs:
            for SG in SGs:
                cons=mc.listConnections((SG+'.surfaceShader'), s=1,plugs=0) or mc.listConnections((SG+'.miMaterialShader'), s=1,plugs=1)
                if cons:
                    Mesh=mc.sets(SG,q=1)
                    if Mesh:
                        shotNameMesh=Mesh[len(Mesh)-1].split('_')
                        midName=''
                        if len(shotNameMesh)>4:
                            midName= shotNameMesh[3]
                        else:
                            midName= shotNameMesh[len(shotNameMesh)-1]    
                        shadeNewName=Prefix+'_'+midName+'_'+mc.nodeType(cons[0])
                        if shadeNewName not in NewName: 
                            oldName.append(cons[0])
                            NewName.append(shadeNewName)
                            SGNewName=shadeNewName+'SG'
                            oldName.append(SG)
                            NewName.append(SGNewName)
                        else:
                            for i in range(1,100):
                                newshader='%s_%02d'%(shadeNewName,i)
                                oldName.append(cons[0])
                                NewName.append(newshader)
                                SGNewName=newshader+'SG'
                                oldName.append(SG)
                                NewName.append(SGNewName)
                                break                            
                    for i in range(5):
                        if i ==0:
                            nextNodes=mc.listConnections(cons[0],s=1,plugs=0)
                            if nextNodes==None:
                                pass
                            else:   
                                for nextNode in nextNodes:
                                    if mc.nodeType(nextNode)!='shadingEngine' and mc.nodeType(nextNode)!='defaultShaderList' and mc.nodeType(nextNode)!='materialInfo' :
                                       Nodes.append(nextNode)
                                       nodeNew=shadeNewName+'_'+mc.nodeType(nextNode)
                                       oldName.append(nextNode)
                                       NewName.append(nodeNew)
              
                        else:
                           if Nodes==None:
                               pass
                           else:
                               for node in Nodes:
                                   nextNodes=mc.listConnections(node,s=1,plugs=0)
                                   if nextNodes==None:
                                       pass
                                   else:
                                       for nextNode in nextNodes:
                                           if mc.nodeType(nextNode)!='shadingEngine' and mc.nodeType(nextNode)!='defaultShaderList' and mc.nodeType(node)!='materialInfo' :
                                               nodeNew=Prefix+'_'+midName+'_'+mc.nodeType(nextNode)
                                               oldName.append(nextNode)
                                               NewName.append(nodeNew)
                                                          
        
        nodeName=[oldName,NewName]
        return nodeName

    def csl_RenameMatNode(self,nodeName=[]):
        nodeName=self.csl_RenameMatNodeRecord(nodeName=[])[0]
        nodeNewName=self.csl_RenameMatNodeRecord(nodeName=[])[1]
        for i in range(len(nodeName)):
            if mc.objExists(nodeName[i])!= False  and 'default' not in mc.nodeType(nodeName[i]) and 'defaultColorMgtGlobals' not in nodeName[i]:
                try:
                    mc.rename(nodeName[i],nodeNewName[i])
                except:
                    pass
        print  u'===[Updating MatNode To Rename]===材质节点名修改[%s]完毕==='%nodeNewName
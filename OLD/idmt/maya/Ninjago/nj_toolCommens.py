# -*- coding: utf-8 -*-
# 【nj】【乐高常用工具】
#  Author : 韩虹
#  Data   : 2014_11
# import sys
# sys.path.append('D:\\food\pyp\common')

import maya.cmds as mc
import maya.mel as mel
import os
import re

from idmt.maya.Hh_common import hh_RenderArnoldLayer
reload(hh_RenderArnoldLayer)

class nj_toolCommens(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    def nj_colothImageApply(self): 
        print(u'======开始创建皮肤通道层======')
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer') 
        if mc.objExists('skin_Idp'):
            mc.delete('skin_Idp')        
        info=self.nj_colothInfoNew()
        allmeshs=info[0]
        clothobjs=info[1]
        clothimages=info[2]
               
        
        
    # matte 材质
        shader_Matte = 'SHD_Matte_Shader' 
        if mc.ls(shader_Matte):
            mc.delete(shader_Matte)
        MatteSG = shader_Matte+'SG'
        if mc.ls(MatteSG):
            mc.delete(MatteSG)
        shader_Matte = mc.shadingNode('lambert', asShader=True, name = shader_Matte)
        MatteSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = MatteSG)
        # 连接
        mc.setAttr((shader_Matte + '.color'), 0, 0, 0, type='double3')
        mc.setAttr((shader_Matte + '.ambientColor'), 1, 1, 1, type='double3')
        mc.setAttr((shader_Matte + '.diffuse'), 0)
        mc.setAttr((shader_Matte + '.matteOpacityMode'), 0)
        mc.connectAttr((shader_Matte + '.outColor'), (MatteSG + '.surfaceShader'))
        
        try:
            mc.sets(allmeshs,e = 1 , forceElement = MatteSG)
        except:
            print u'===有物体无法赋予材质==='
            print mesh
            mc.error(u'===有物体无法赋予材质===')
    # coloth 材质
        if  clothimages:
            conditionskin='condition_skin'
            multiplyDivide='multiply_skin'
            multiplyBlue='multiply_Blue'
            multiplyGreen='multiply_Green'
            multiplyRed='multiply_Red'
            Blue01='condition_Blue01' 
            Blue02='condition_Blue02' 
            Green01='condition_Green01' 
            Green02='condition_Green02'
            Red01='condition_Red01' 
            Red02='condition_Red02'  
                        
            multiplyDivide01='multiplyDivide_Blend'            
            for node in [conditionskin,multiplyDivide,multiplyBlue,multiplyGreen,multiplyRed,Blue01,Blue02,Green01,Green02,Red01,Red02,multiplyDivide01]:
                if mc.ls(node):
                    mc.delete(node) 
            for condit in [Blue01,Blue02,Green01,Green02,Red01,Red02,conditionskin]:
                mc.shadingNode('condition',asUtility=True,name=condit)
                mc.setAttr((condit+'.colorIfTrueR'),1)
                mc.setAttr((condit+'.colorIfTrueG'),1) 
                mc.setAttr((condit+'.colorIfTrueB'),1)
                mc.setAttr((condit+'.colorIfFalseR'),0)   
                mc.setAttr((condit+'.colorIfFalseG'),0)
                mc.setAttr((condit+'.colorIfFalseB'),0) 
                if condit== conditionskin:
                    mc.setAttr((condit+'.colorIfTrueG'),0) 
                    mc.setAttr((condit+'.colorIfTrueB'),0) 
                    mc.setAttr((condit+'.secondTerm'),1)                                                                                        
                if condit==Blue01:
                    mc.setAttr((condit+'.secondTerm'),0.038)
                    mc.setAttr((condit+'.operation'),2)                    
                if condit==Blue02:
                    mc.setAttr((condit+'.secondTerm'),0.040)
                    mc.setAttr((condit+'.operation'),4)                      
                if condit==Green01:
                    mc.setAttr((condit+'.secondTerm'),0.780)
                    mc.setAttr((condit+'.operation'),2)                    
                if condit==Green02:
                    mc.setAttr((condit+'.secondTerm'),0.790)
                    mc.setAttr((condit+'.operation'),4) 
                if condit==Red01:
                    mc.setAttr((condit+'.secondTerm'),0.978)
                    mc.setAttr((condit+'.operation'),2)
                if condit==Red02:
                    mc.setAttr((condit+'.secondTerm'),0.982) 
                    mc.setAttr((condit+'.operation'),4) 
            for multiply in [multiplyDivide,multiplyBlue,multiplyGreen,multiplyRed,multiplyDivide01]:
                mc.shadingNode('multiplyDivide',asUtility=True,name=multiply)                                                                                                                                                                                                                                   
            try:
 
                mc.connectAttr(('%s.%s') % (Blue01, 'outColor') , ('%s.%s') % (multiplyBlue, 'input1'), f=True)
                mc.connectAttr(('%s.%s') % (Blue02, 'outColor') , ('%s.%s') % (multiplyBlue, 'input2'), f=True)
                mc.connectAttr(('%s.%s') % (Green01, 'outColor') , ('%s.%s') % (multiplyGreen, 'input1'), f=True)
                mc.connectAttr(('%s.%s') % (Green02, 'outColor') , ('%s.%s') % (multiplyGreen, 'input2'), f=True)
                mc.connectAttr(('%s.%s') % (Red01, 'outColor') , ('%s.%s') % (multiplyRed, 'input1'), f=True)
                mc.connectAttr(('%s.%s') % (Red02, 'outColor') , ('%s.%s') % (multiplyRed, 'input1'), f=True)                                                                                
                mc.connectAttr(('%s.%s') % (multiplyGreen, 'output') , ('%s.%s') % (multiplyDivide01, 'input2'), f=True)
                mc.connectAttr(('%s.%s') % (multiplyRed, 'output') , ('%s.%s') % (multiplyDivide01, 'input1'), f=True)
               
                mc.connectAttr(('%s.%s') % (multiplyBlue, 'output') , ('%s.%s') % (multiplyDivide, 'input2'), f=True)                    
                mc.connectAttr(('%s.%s') % (multiplyDivide01, 'output') , ('%s.%s') % (multiplyDivide, 'input1'), f=True) 
                
                mc.connectAttr(('%s.%s') % (multiplyDivide, 'outputX') , ('%s.%s') % (conditionskin, 'firstTerm'), f=True)
                
            except:
                pass 
                                                   
            for i in range(len(clothimages)):
                shader_cloth='skin_idp_0'+str(i+1)
                clothSG=shader_cloth+'SG'
                skinLayer= 'skin_layer_0'+str(i+1)                
                for node in [shader_cloth,clothSG,skinLayer]:
                    if mc.ls(node):
                        mc.delete(node)
                shader_cloth = mc.shadingNode('surfaceShader', asShader=True, name = shader_cloth)
                clothSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = clothSG) 
                
                mc.setAttr((shader_cloth+'.outMatteOpacity'),0,0,0)
                skinLayer= mc.shadingNode('layeredTexture',asUtility=True,name=skinLayer) 

                try:
                    mc.connectAttr(('%s.%s') % (clothimages[i], 'outColor') , ('%s.%s') % (skinLayer, 'inputs[0].color'), f=True)
                    
                    mc.connectAttr(('%s.%s') % (skinLayer, 'outColor.outColorB') , ('%s.%s') % (Blue01, 'firstTerm'), f=True)
                    mc.connectAttr(('%s.%s') % (skinLayer, 'outColor.outColorB') , ('%s.%s') % (Blue02, 'firstTerm'), f=True)
                    mc.connectAttr(('%s.%s') % (skinLayer, 'outColor.outColorG') , ('%s.%s') % (Green01, 'firstTerm'), f=True)
                    mc.connectAttr(('%s.%s') % (skinLayer, 'outColor.outColorG') , ('%s.%s') % (Green02, 'firstTerm'), f=True)
                    mc.connectAttr(('%s.%s') % (skinLayer, 'outColor.outColorR') , ('%s.%s') % (Red01, 'firstTerm'), f=True)                                                            
                    mc.connectAttr(('%s.%s') % (skinLayer, 'outColor.outColorR') , ('%s.%s') % (Red02, 'firstTerm'), f=True)                      
                    
                    mc.connectAttr(('%s.%s') % (conditionskin, 'outColor') , ('%s.%s') % (shader_cloth, 'outColor'), f=True)
                    
                    mc.connectAttr(('%s.%s') % (shader_cloth, 'outColor') , ('%s.%s') % (clothSG, 'surfaceShader'), f=True)
                    
                except:
                    pass                                                                                         

                try:
                    mc.sets(clothobjs,e = 1 , forceElement = clothSG)
                except:
                    print u'===有物体无法赋予材质==='
                    print mesh
                    mc.error(u'===有物体无法赋予材质===')  
        #建层

        
        mc.createRenderLayer(allmeshs,name='skin_Idp', noRecurse=1, makeCurrent=1) 
        
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer') 
        mc.setAttr("defaultRenderLayer.renderable", 0)        
        return 0 
                          
    def nj_colothInfo(self):
        print(u'======开始读取======')
        meshs=mc.ls(type='mesh',l=1)
        allobjs=[]
        allSGs=[]
        clothSG=[]
        clothobjs=[]
        clothimges=[]
        Nodes=[]
        if meshs:
            for i in range(len(meshs)):
                if re.search('MODEL',meshs[i])!=None:
                    allobjs.append(meshs[i])
                msg=mc.listConnections(meshs[i],s=0,type = 'shadingEngine')
                if msg:
                    allSGs.append(msg[0])
        if allSGs:
            for sg in allSGs:                
                cons=mc.listConnections((sg+'.surfaceShader'),s=1,d=0) or mc.listConnections((sg+'.miMaterialShader'), s=1,d=0)                
                for k in range(4):               
                    if k==0:
                        if cons==None:
                            pass
                        else:
                            for j in range(len(cons)):
                                nextNode=mc.listConnections(cons[j],s=1,d=0,plugs=0)
                                if nextNode==None:
                                    pass
                                else:
                                    for Node in nextNode:
                                        Nodes.append(Node)
                                        if mc.nodeType(Node)=='file' and mc.objExists(Node+'.fileTextureName'):
                                            imag=mc.getAttr(Node+'.fileTextureName')
                                            shortimage=imag.split('/')[-1]
                                            if imag and re.search('cloth_color',shortimage)!=None and Node not in clothimges:
                                                clothSG.append(sg)
                                                clothimges.append(Node)
                    else:
                        if Nodes==None:
                            pass
                        else:
                           for node in Nodes:
                               nextNodes=mc.listConnections(node,s=1,plugs=0,d=0)
                               if nextNodes==None:
                                   pass
                               else:
                                   for Node in nextNodes:
                                        if mc.nodeType(Node)=='file' and mc.objExists(Node+'.fileTextureName'):
                                            imag=mc.getAttr(Node+'.fileTextureName')
                                            if imag and re.search('cloth_color',imag)!=None and Node not in clothimges:
                                                clothSG.append(sg)
                                                clothimges.append(Node)
    
            if clothSG:
                clothmesh=mc.sets(clothSG[0],q=1)
                if clothmesh:
                    for cmesh in clothmesh:
                        clothobjs.append(cmesh)  
    #        if clothSG:
    #            clothmesh=mc.sets(clothSG[0],q=1)
    #            for cmesh in clothmesh:
    #                cobjs=mc.listRelatives(cmesh, p=1, f=1) 
    #                if cobjs:
    #                    clothobjs.append(cobjs)                                                  
            return[allobjs,clothobjs,clothimges]                           
                                               
    def nj_colothInfoNew(self):
        meshs=mc.ls(type='mesh',l=1)
        allobjs=[]
        allSGs=[]
        clothobjs=[]
        clothimges=[]
        Nodes=[]
        if meshs:
            for i in range(len(meshs)):
                if re.search('MODEL',meshs[i])!=None:
                    allobjs.append(meshs[i])
                msg=mc.listConnections(meshs[i],s=0,type = 'shadingEngine')
                if msg:
                    allSGs.append(msg[0])
        
        objs=mc.ls('*Torso_*',type='transform')+mc.ls('*:*Torso_*',type='transform')
        if objs:
            for obj in objs:
                meshs=mc.listRelatives(obj,s=1,f=1)
                if meshs:
                    sg=mc.listConnections(meshs[0],s=0,type = 'shadingEngine')
                    if sg:               
                        shader=mc.listConnections((sg[0]+'.surfaceShader'),s=1,d=0) or mc.listConnections((sg[0]+'.miMaterialShader'), s=1,d=0)
                        if shader:
                            cons=mc.listConnections((shader[0]+'.color'),s=1,d=0)
                            if mc.ls(cons) and mc.nodeType(cons[0])=='file':
                                img=mc.getAttr(cons[0]+'.fileTextureName')
                                if img and '/' in img:
                                     clothobjs.append(obj)
                                     clothimges.append(cons[0])  
        if clothobjs==None:
            mc.error(u'===没有有效Torso物体===')                                                
        return[allobjs,clothobjs,clothimges]                    
                                                                
                                                
            
            
            
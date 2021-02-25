# -*- coding: utf-8 -*-

'''
Created on 2015

GDC 相机相关工具【通用】

@author: hanhong

Data   : 2015_12_17
'''

# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
#显示工具
#@author: hanhong
#Data：2015/12/18
#----------------------------------------------------------------------------------------------------------#
class GDC_DisTools(object):
    def __init__(self):
        pass
#显示
#@author: hanhong
#Data：2015/9/16
#sl==1,选择物体；sl==0，选择所有
#----------------------------------------------------------------------------------------------------------#
    def gdc_DisShader(self,sl=1):
        meshs=[]
        shades=[]
        if sl==0:
            meshs=mc.ls(type='mesh',l=1)
        if sl==1:
            objs=mc.ls(sl=1,l=1,tr=1)
            if objs:
                for obj in objs:
                    if mc.listRelatives(obj,s= 1,type='mesh',f=1):
                        shapes=mc.listRelatives(obj,s= 1,type='mesh',f=1)
                        for shape in shapes:
                            meshs.append(shape)
        if meshs:
            for mesh in meshs:
                SGS=mc.listConnections(mesh,s=1,type = 'shadingEngine')
                if SGS:
                    for SG in SGS:
                        Shade=mc.listConnections((SG+'.surfaceShader'), plugs=0,s=1,c=0)
                        if Shade and Shade[0] not in shades:
                            shades.append(Shade[0])
        if shades:
            for shade in shades:
                mc.select(shade)
                self.gdc_createDisplayMatNode()
        else:
            print '++++++++++++++++++++++++       pls select a obj   +++++++++++++++++++++++++'

        return 0
#----------------------------------------------------------------------------------------------------------#
#----------------------------- -----------------------------------------------------------------------------#
#GDC 【通用】 创建DIS节点
#由之前  '//file-cluster/gdc/Resource/Support/Maya/projects/VickytheViking/vv_createDisplayMatNode.py' 脚本修改而来
#Data：2015/12/18
#----------------------------------------------------------------------------------------------------------#
    def gdc_createDisplayMatNode(self):
        sel = mc.ls(sl = True)
        sg = []
        DisInfo=[]
        shadeInfo=[]
        if sel:
            sg = mc.listConnections(sel[0], d = True, s = False, type = 'shadingEngine')
        if sg:
            if not mel.eval('attributeExists "kitty" ' + sel[0]):
                mc.addAttr(sel[0],ln = "kitty", at = 'long')
            else:
                k = mc.listConnections(sel[0] + '.kitty', d = False, s = True)
                if k:
                    mc.delete(k[0])
            mat = mc.shadingNode('lambert', asShader = True, name = 'Disp_' + sel[0])
            mc.addAttr(mat,ln = "hello", at = 'long')
            sg = mc.listConnections(sel[0], d = True, s = False, type = 'shadingEngine')
            matInfo = mc.listConnections(sg[0], d = True, s = False, type = 'materialInfo')
            mc.connectAttr(mat + '.message', matInfo[0] + '.material',  f = True)
            mc.connectAttr( mat + '.hello', sel[0] + '.kitty',  f = True)
            DisInfo.append(mat)
            shadeInfo.append(sel[0])
            print '++++++++++++++++++++++++      Hello Kitty      +++++++++++++++++++++++++'
        else:
            print '++++++++++++++++++++++++       pls select a material node    +++++++++++++++++++++++++'

        info=[DisInfo,shadeInfo]
        return info


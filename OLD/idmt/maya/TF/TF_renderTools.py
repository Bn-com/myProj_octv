# -*- coding: utf-8 -*-
'''
Created on 2016
ToothFairies项目渲染面板工具
@author: 陈嘉伟
Data   : 2016_08_18
'''
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import json
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
reload(sk_renderLayerCore)
from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
reload(sk_smoothSet)
# ############【目录】################
# 【透明材质检测】【透贴信息字典】【清理选中物体为niShape】【转数组层级】
# 【透明材质检测】
# 【选中物体检测透贴信息并写入字典】
# ###################################
class TF_renderToolsClass(object):
    def __init__(self):
        pass
    #------------------------------#
    # 【透明材质检测】【检测输出本地透明材质信息】
    #  输入Shape,检测本地文件模型是否有透贴。输出SG节点影响模型点信息和贴图file节点名称
    #  由于lambert和surfaceShader材质球透明材质属性transparency和outTransparency的名称不同，加了try
    #------------------------------#

    def TF_TransparencyShaderInfo(self, selectObjShape):
        meshFaceInfos = []
        # 选中模型的所有SG节点上，连接的所有模型与面信息。meshFaceInfos = [['A','B','C.f[0:256]'],['A','B','C'],['A','B','C']]
        onlySelectObjMeshFaceinfos = []
        # 选中模型的所有SG节点上，连接的这个选中的模型与面信息。[['A'],['A'],['A']]
        ObjTransparencyFileAttrs = []
        # 选中模型上所有SG节点连接的材质球上连接的透贴文件file.outcolor。ObjTransparencyFileAttrs = ['key01','key02','key03']
        ObjShaderSGsCleans = []
        # 选中模型上所有SG节点。无重复。ObjShaderSGsCleans = ['SG01','SG02','SG03','SG04','SG05']
        ObjShaderSGsCleans02 = []
        # 02SG数组为 选中模型上所有的SG节点中有模型连接的SG节点。 ObjShaderSGsCleans02 = ['SG01','SG02','SG03','SG04']
        ObjShaderSGsCleans03 = []
        # 03SG数组为 选中模型上所有的SG节点中有模型连接的SG节点，并且有透贴连接的。 ObjShaderSGsCleans02 = ['SG01','SG02','SG03']
        # 这个SG节点由于分层的关系，有可能有多个SG连接，但由于不在一层，就并无连接任何模型信息。--猜测错误
        # 多出的无连接的SG节点是因为，先选整体模型上了材质球，然后又选面上了材质球，以后无论怎样操作，第一个选模型上的材质球一直会保留，但无模型连接信息了。
        mesh = mc.ls(selectObjShape, l=1, o=1)[0]
        ObjShaderSGs = mc.listConnections(mesh, s=0, d=1, c=0, type='shadingEngine')
        for ObjShaderSG in ObjShaderSGs:
            if ObjShaderSG not in ObjShaderSGsCleans:
                ObjShaderSGsCleans.append(ObjShaderSG)
        for ObjShaderSG in ObjShaderSGsCleans:
            if mc.sets(ObjShaderSG, q=1) and ObjShaderSG not in ObjShaderSGsCleans02:
                ObjShaderSGsCleans02.append(ObjShaderSG)
                try:
                    ObjShader = mc.listConnections(ObjShaderSG+'.surfaceShader', s=1, d=0, c=0)[0]
                    try:
                        ObjTransparencyFile = mc.listConnections(ObjShader+'.transparency', s=1, d=0, c=0, p=0)[0]
                        ObjTransparencyFileAttr = mc.listConnections(ObjShader+'.transparency', s=1, d=0, c=0, p=1)[0]
                        if mc.objExists(ObjTransparencyFile) and ObjShaderSG not in ObjShaderSGsCleans03:
                            ObjShaderSGsCleans03.append(ObjShaderSG)
                            if '.outColor' in ObjTransparencyFileAttr and mc.nodeType(ObjTransparencyFile) == 'file':
                                meshFaceInfo = mc.sets(ObjShaderSG, q=1)
                                meshFaceInfo = mc.ls(meshFaceInfo, l=1)  # 加长名
                                # meshFaceInfo = ['A','B','C']
                                # 由于要按数量排序，不能消除重复内容
                                # if meshFaceInfo not in meshFaceInfos:
                                meshFaceInfos.append(meshFaceInfo)
                                # 一个透贴可能被连接到几个SG节点上，不能排除重复
                                # if ObjTransparencyFileAttr not in ObjTransparencyFileAttrs:
                                ObjTransparencyFileAttrs.append(ObjTransparencyFileAttr)
                            else:
                                mc.warning(u'===========【非outColor属性连接出透明属性】%s==========='%ObjShader)
                                mc.error(u'===========文件中有非outColor属性连接出透明属性，或者连接出的节点为非file，请检查上面列出的材质球==========')
                    except:
                        pass
                    try:
                        ObjTransparencyFile = mc.listConnections(ObjShader+'.outTransparency',s=1,d=0,c=0,p=0)[0]
                        ObjTransparencyFileAttr = mc.listConnections(ObjShader+'.outTransparency',s=1,d=0,c=0,p=1)[0]
                        if mc.objExists(ObjTransparencyFile):
                            ObjShaderSGsCleans03.append(ObjShaderSG)
                            if '.outColor' in ObjTransparencyFileAttr and mc.nodeType(ObjTransparencyFile)=='file':
                                meshFaceInfo = mc.sets(ObjShaderSG,q=1)
                                meshFaceInfo = mc.ls(meshFaceInfo,l=1)#加长名
                                if meshFaceInfo not in meshFaceInfos:
                                    meshFaceInfos.append(meshFaceInfo)
                                if ObjTransparencyFileAttr not in ObjTransparencyFileAttrs:
                                    ObjTransparencyFileAttrs.append(ObjTransparencyFileAttr)
                            else:
                                mc.warning(u'===========【非outColor属性连接出透明属性】%s==========='%ObjShader)
                                mc.error(u'===========文件中有非outColor属性连接出透明属性，或者连接出的节点为非file，请检查上面列出的材质球==========')
                    except:
                        pass
                except:
                    pass
        result = [meshFaceInfos, ObjTransparencyFileAttrs, ObjShaderSGsCleans03, ObjShaderSGsCleans02]
        return result
        # 没有透贴的物体，有可能输出了[[],[],[A]]
    '''
    #[[[u'tf_c003001Twinkle:MSH_L_R_wings_.f[0:4]]', [u'tf_c003001Twinkle:MSH_L_L_wings_Shape']], [u'tf_c003001Twinkle:TXT_char_Twinkle_right_wing1.outColor', u'tf_c003001Twinkle:TXT_char_Twinkle_left_wing1.outColor']]
    #[[[u'tf_c003001Twinkle:MSH_L_R_wings_.f[0:4]', u'tf_c003001Twinkle:MSH_L_R_wings_.f[6:135]', u'tf_c003001Twinkle:MSH_L_R_wings_.f[137:139]', u'tf_c003001Twinkle:MSH_L_R_wings_.f[141:157]', u'tf_c003001Twinkle:MSH_L_R_wings_.f[159:457]'], [u'tf_c003001Twinkle:MSH_L_L_wings_Shape', u'tf_c003001Twinkle:MSH_L_R_wings_.f[5]', u'tf_c003001Twinkle:MSH_L_R_wings_.f[136]', u'tf_c003001Twinkle:MSH_L_R_wings_.f[140]', u'tf_c003001Twinkle:MSH_L_R_wings_.f[158]']], [u'tf_c003001Twinkle:TXT_char_Twinkle_right_wing1.outColor', u'tf_c003001Twinkle:TXT_char_Twinkle_left_wing1.outColor']]
    #一个模型上有可能选面连接了几个sg节点，每个连出的shader上又可能有透贴。
    # result[0][0]
    #第一个[0]为选中的那个模型上连接的sg节点(可能有几个sg节点，这一层是所有sg节点的)连接的所有模型的信息(可能会很多模型和面，但是共享唯一的sg节点)。
    #第二个[0]为对应下面第[i]个sg节点(单个)上连接的面或模型信息，类型仍为数组，可能连了很多模型。
    # result[1][0]
    #第一个[1]为选中的那个模型上连接的所有sg节点(复数sg节点)上，连接的透贴所有file文件(带'.outColor'属性)。
    #第二个[0]为第[i]个sg节点上(单个)上连接的透贴file文件。===****注意****=== result[1][0]内容上面没做判断，是有可能重复的，
    #===****注意****===
    #result[1][0]有可能出现选中的几个模型，有可能被同一个sg节点连接了，以上没做判断，所以有可能会出现透贴file节点重复(但相对内容-连接的模型信息会完全一样),请调用时用字典清理一次。
    '''
    #------------------------------#
    # 【透贴信息字典】【选中物体检测透贴信息并写入字典】
    #  key为file.outColor,内容为关联所有模型的信息
    #------------------------------#
    def TF_transparencyInfoDictInfo(self, selectObjs):
        transparencyInfoDict = dict({})
        # 没有透明贴图的物体导出为空{}
        selectShapes = self.TF_CleanNoIntermediateShapeNodes(selectObjs)
        for selectShape in selectShapes:
            TraToolInfo = self.TF_TransparencyShaderInfo(selectShape)
            meshFaceInfos = TraToolInfo[0]
            ObjTransparencyAttrs = TraToolInfo[1]
            for i in range(len(ObjTransparencyAttrs)):
                transparencyInfoDict[ObjTransparencyAttrs[i]] = meshFaceInfos[i]
        return transparencyInfoDict

    #------------------------------#
    # 【清理选中物体为niShape】【清理选择物体为MODEL组下，noIntermediate的mesh节点】
    #  制作人选中shape或transfrom节点，或MODEL大组，可有效清理出正确shape节点。
    #  注意导出的格式为 [['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]
    #------------------------------#
    def TF_CleanNoIntermediateShapeNodes(self, selectObjs):
        selecNoIntermediateShapes = []
        # [['|MODEL|group3|group2|group1|pSphere1|pSphereShape1'],['|MODEL|group3|group2|group1|pSphere2|pSphereShape2']]
        for selectObj in selectObjs:
            if 'MODEL' not in selectObj:
                mc.warning(u'===========【%s】===========所选物体包含非MODEL组下物体'%selectObj)
                mc.error(u'===========所选物体包含非MODEL组下物体==========')
            if mc.nodeType(selectObj) == 'mesh':
                mesh = [selectObj]
                if mesh not in selecNoIntermediateShapes:
                    selecNoIntermediateShapes.append(mesh)
            else:
                allShapes = mc.listRelatives(selectObj, ad=1, f=1, type='mesh')
                for shape in allShapes:
                    transform = mc.listRelatives(shape, p=1, f=1, type='transform')
                    mesh = mc.listRelatives(transform, s=1, f=1, ni=1, type='mesh')
                    if mesh not in selecNoIntermediateShapes:
                        selecNoIntermediateShapes.append(mesh)
        return selecNoIntermediateShapes
    #  注意导出的格式为 [['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]
    #------------------------------#
    # 【转数组层级】【转换数组】
    #  把[['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]转换为['pSphereShape1', 'pSphereShape2', 'pSphereShape3']
    #------------------------------#
    def TF_switchGroup(self,Objs):
        #修正为None的情况
        '''
        newGRP = []
        for obj in Objs:
            newGRP += obj
        return newGRP
        '''
        newGRP = []
        for obj in Objs:
            if obj!=None:
                newGRP += obj
        return newGRP
    #------------------------------#
    # 【材质球】【IDpass遮罩材质赋予】
    #  赋 R G B M A遮罩材质球,材质球连接本文件透贴
    #  //server为1时读取网上赋材质信息和透明信息
    #------------------------------#
    def TF_RBGMApass(self,type = 'R', transparency=1):
        selectObjs = mc.ls(sl=1, l=1)
        idpName = []
        matteShaderAttr = []
        if type == 'R':
            idpName = 'IdpR_colorR'
            matteShaderAttr = [(1,0,0),(0,0,0),0]
        elif type == 'G':
            idpName = 'IdpG_colorG'
            matteShaderAttr = [(0,1,0),(0,0,0),0]
        elif type == 'B':
            idpName = 'IdpB_colorB'
            matteShaderAttr = [(0,0,1),(0,0,0),0]
        elif type == 'M':
            idpName = 'IdpM_matte'
            matteShaderAttr = [(0,0,0),(0,0,0),0]
        elif type == 'A':
            idpName = 'IdpA_alpha'
            matteShaderAttr = [(0,0,0),(1,1,1),1]
        materialsNodes =mc.ls(mat=1)
        if idpName not in materialsNodes:
            matteShader = mc.shadingNode('lambert',asShader=1,name = idpName)
            matteShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(matteShader+'SG'))
            mc.connectAttr((matteShader +'.outColor'),(matteShaderSG +'.surfaceShader'),f=1)
            mc.setAttr(matteShader+'.color',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
            mc.setAttr(matteShader+'.ambientColor',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
            # mc.setAttr(matteShader+'.outMatteOpacity',float(matteShaderAttr[1][0]),float(matteShaderAttr[1][1]),float(matteShaderAttr[1][2]),type ='double3')
            mc.setAttr(matteShader+'.matteOpacityMode',2)
            mc.setAttr(matteShader+'.matteOpacity',float(matteShaderAttr[2]))
        else:
            matteShader = idpName
            matteShaderSG = matteShader+'SG'
        '''
        1、选择一个物体
            1、无透贴：直接赋材质球
            2、一个透贴：直接赋材质球，直接连透贴
            3、多个透贴：每个透贴生成材质球，选物体改为选面，根据透贴信息选面赋予物体
        2、选择一个面
            1、无透贴：根据选面信息赋一个材质球
            2、一个透贴：根据选面信息，赋一个材质球，直接连接透贴
            3、多个透贴：根据选面信息，赋一个材质球，检测每个透贴的选面信息，有选择重复的生成新材质球，用重复的面信息赋材质球，连接透贴。
        ############不管选物体还是选面，多透贴时一定要选面来赋材质#########
        如果所选模型只有一个sg节点的话就只有一个透贴,
        但还是要选判断制作人是否选面
        目前先判断一个物体上透贴的数量
        '''
        # 刷一遍SG节点
        # mel.eval('zwResetShadingEnginesN')
        # 字典收集本地透贴信息
        # transparencyInfoDict = self.TF_transparencyInfoDictInfo(selectObjs)
        # 清理选中的物体为noIntermediate的Shape节点,支持带面信息。
        NIselectShapes = self.TF_CleanNoIntermediateShapeNodes(selectObjs)
        #  把[['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]转为['pSphereShape1', 'pSphereShape2', 'pSphereShape3']
        NIselectShapes = self.TF_switchGroup(NIselectShapes)
        '''
        # ======当selectShape为选面时，点的分离会造成变为多个字符串，导致产生很多多余shade，需要整合
        tf_c003001Twinkle:MSH_L_R_wings_.f[247]
        tf_c003001Twinkle:MSH_L_R_wings_.f[251:252]
        tf_c003001Twinkle:MSH_L_R_wings_.f[291:297]
        tf_c003001Twinkle:MSH_L_R_wings_.f[324:330]
        tf_c003001Twinkle:MSH_L_R_wings_.f[364:373]
        tf_c003001Twinkle:MSH_L_R_wings_.f[418:425]
        tf_c003001Twinkle:MSH_L_R_wings_.f[453]
        '''
        if transparency == 1:
            # 整理出纯Shape节点的选择
            selectShapeOnlys = []
            for selectShapeFace in NIselectShapes:
                onlyShape = mc.ls(selectShapeFace, o=1, l=1)[0]
                if onlyShape not in selectShapeOnlys:
                    selectShapeOnlys.append(onlyShape)
            # print (u'把选中的所有物体或面信息转成onlyShape模式如下：%s'%selectShapeOnlys)
            # 把选面的信息整理成一个字典
            onlyShapeFace_dict = dict({})
            for selectShapeOnly in selectShapeOnlys:
                selectShapeFaces = []
                for selectShapeFace in NIselectShapes:
                    if '.f[' in selectShapeFace and (mc.ls(selectShapeFace, o=1, l=1)[0]) == selectShapeOnly and selectShapeFace not in selectShapeFaces:
                        selectShapeFaces.append(selectShapeFace)
                if len(selectShapeFaces) != 0:
                    onlyShapeFace_dict[selectShapeOnly] = selectShapeFaces
            # print (u'选中的所有物体里如果有面信息，输出成字典如下：%s'%onlyShapeFace_dict)
            RBG_Tra_objTraAttr_dict = dict({})
            # 每个物体的所有透贴file.outColor
            RBG_Tra_objSG_dict = dict({})
            # 每个物体下的所有SG
            RBG_Tra_SG_meshFace_dict = dict({})
            # 每个SG节点对应的模型点信息
            RBG_Tra_SG_transparency_dict = dict({})
            # 每个SG节点对应的唯一透贴文件file.outColor
            for selectShapeOnly in selectShapeOnlys:
                # 此物体的 所有SG节点,所有SG节点上连接的File.outColor节点,所有SG节点上连接的meshFace面信息。
                TraToolInfo = self.TF_TransparencyShaderInfo(selectShapeOnly)
                meshFaceInfos = TraToolInfo[0]
                # print (u'选中的此物体连接的所有SG节点，连接的模型信息：%s'%meshFaceInfos)
                ObjTransparencyAttrs = TraToolInfo[1]
                # print (u'选中的此物体连接的所有透贴.outColor信息：%s'%ObjTransparencyAttrs)
                ObjShaderSGsCleans = TraToolInfo[2]
                # print (u'选中的此物体连接的所有有模型面信息的SG节点的模型面信息：%s'%ObjShaderSGsCleans)
                if len(ObjTransparencyAttrs) != 0:
                    # 以选中的mesh为key
                    mesh = mc.ls(selectShapeOnly, o=1, l=1)[0]
                    RBG_Tra_objSG_dict[mesh] = ObjShaderSGsCleans
                    RBG_Tra_objTraAttr_dict[mesh] = ObjTransparencyAttrs
                    for i in range(len(ObjShaderSGsCleans)):
                        RBG_Tra_SG_meshFace_dict[ObjShaderSGsCleans[i]] = meshFaceInfos[i]
                    for i in range(len(ObjShaderSGsCleans)):
                        RBG_Tra_SG_transparency_dict[ObjShaderSGsCleans[i]] = ObjTransparencyAttrs[i]
        # 先给所选模型或面赋相应材质,以上为提前读取了信息保存在缓存里
        # mc.sets(selectObjs, e=1, forceElement = matteShaderSG)
        # 改为一个一个模型赋材质，成功率会高点
        for selectObj in selectObjs:
            mc.sets(selectObj, e=1, forceElement = matteShaderSG)
        # 上材质之前先转为选面模式
        # mc.select(clear=1)
        # mc.select(selectObjs,r=1)
        # mc.ConvertSelectionToFaces()
        # selectObjs02 = mc.ls(sl=1, l=1)
        # mc.sets(selectObjs02, e=1, forceElement = matteShaderSG)
        mc.select(clear=1)
        '''
        下面是肯定有透贴的了，接着要判断是有几个透贴，就一个透贴的话就生成材质球selectShape直接赋即可。
        '''
        # 如果字典里有内容，证明选中的物体里,至少有一个物体有透贴，再继续加材质球。
        if transparency == 1 and len(RBG_Tra_objTraAttr_dict) != 0:
            # keys = RBG_Tra_objSG_dict.keys()
            # 每个选中的物体开始检测所有SG节点
            for selectShapeOnly in selectShapeOnlys:
                haveTraMeshs = RBG_Tra_objTraAttr_dict.keys()
                # 下面为选择的物体或面，有透贴的物体才进入下面计算，添加新材质球，无透贴的忽略
                if selectShapeOnly in haveTraMeshs:
                    # 要先判断【一个】物体下，如果有两个透贴，但两个透贴的名称一样的话，为一个透贴
                    TransparencyFileAttrs = []
                    for TransparencyFileAttr in RBG_Tra_objTraAttr_dict[selectShapeOnly]:
                        if TransparencyFileAttr not in TransparencyFileAttrs:
                            TransparencyFileAttrs.append(TransparencyFileAttr)
                    '''
                    这层为判断是否多个透贴
                    '''
                    # 判断此物体有几个透贴，以下为多于两个透贴。
                    if len(TransparencyFileAttrs) > 1:
                        print (u'---成功进入单物体多透贴算法 ---')
                        # 字典为这个物体所有的SG节点对应的自己的点信息
                        preOBJfinalTraInfo_dict = dict({})
                        # 这个物体开始检测并收集透贴信息
                        AllSGs = RBG_Tra_objSG_dict[selectShapeOnly]
                        print (u'====【这个物体下的所有SG节点】%s===='%AllSGs)
                        for shaderSG in AllSGs:
                            # 这个SG节点下连接的所有模型信息,注意此信息有可能SG(key)有，但模型信息为[]
                            SGshapeSGs = []
                            for SGshapeSG in RBG_Tra_SG_meshFace_dict[shaderSG]:
                                # 不用考虑选面的情况，目前物体为onlyShape模式
                                if (mc.ls(SGshapeSG, o=1, l=1)[0]) == selectShapeOnly and SGshapeSG not in SGshapeSGs:
                                    # 这个SG节点下唯一与本模型相关的信息
                                    SGshapeSGs.append(SGshapeSG)
                            preOBJfinalTraInfo_dict[shaderSG] = SGshapeSGs
                        print (u'====【所有的SG节点下与这个模型相关的信息,字典】%s===='%preOBJfinalTraInfo_dict)
                        '''
                        以下为最复杂的选面、多透贴连接计算
                        开始计算透贴信息与所选信息的重复信息，生成新材质球连透贴。--------------透贴的选择信息有问题!!
                        '''
                        # 开始处理透贴信息
                        AllSGs02 = AllSGs
                        # 检测此物体上所有sg节点哪个带有透贴,如这个带透贴，就移去此sg节点，并加选其他SG点
                        for checkSG in AllSGs02:
                            if self.TF_CheckSGandTransparency(checkSG) == True:
                                # 下面为判断选择面还是物体
                                if selectShapeOnly in onlyShapeFace_dict.keys():
                                    print (u'---进入为多透贴选面模式---')
                                    selectShapeFaces = onlyShapeFace_dict[selectShapeOnly]
                                    print (u'====【制作人选择的面信息】%s ===='%selectShapeFaces)
                                    mc.select(clear=1)
                                    AllSGs02.remove(checkSG)
                                    for otherSG in AllSGs02:
                                        # 注意调用preOBJfinalTraInfo_dict字典时注意，SG里的模型内容有可能为空[]
                                        try:
                                            mc.select(preOBJfinalTraInfo_dict[otherSG], add=1)
                                        except:
                                            pass
                                    otherFaceInfo = mc.ls(sl=1,l=1)
                                    print (u'====【选中的非第一个透贴相关的所有模型信息】%s===='%otherFaceInfo)
                                    # 开始计算面,透贴的面信息
                                    if len(otherFaceInfo) != 0:
                                        mc.select(otherFaceInfo, r=1)
                                        # 反选赋新材质点
                                        mc.select(selectShapeFaces, tgl=1)
                                        # 减选other
                                        mc.select(otherFaceInfo, d=1)
                                        TraMeshFace01 = mc.ls(sl=1, l=1)
                                        mc.select(clear=1)
                                        print (u'---【正确的透贴选点信息】%s ---'%TraMeshFace01)
                                        if len(TraMeshFace01) != 0:
                                            matteShader = mc.shadingNode('lambert', asShader=1, name=idpName+'Tra')
                                            matteShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(matteShader+'SG'))
                                            mc.connectAttr((matteShader +'.outColor'),(matteShaderSG +'.surfaceShader'), f=1)
                                            mc.setAttr(matteShader+'.color',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                                            mc.setAttr(matteShader+'.ambientColor',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                                            mc.setAttr(matteShader+'.matteOpacityMode',2)
                                            mc.setAttr(matteShader+'.matteOpacity',float(matteShaderAttr[2]))
                                            mc.connectAttr(RBG_Tra_SG_transparency_dict[checkSG], (matteShader +'.transparency'), f=1)
                                            for TraMeshFace01a in TraMeshFace01:
                                                mc.sets(TraMeshFace01a, e=1, forceElement=matteShaderSG)
                                            mc.select(clear=1)
                                    else:
                                        print (u'---进入了特别模式---')
                                        # 如果进入，证明第一个透贴是全选了模型，直接按照单透贴处理方案,选择面上材质
                                        # 不用计算制作人选面跟透贴选面的交互了
                                        matteShader = mc.shadingNode('lambert', asShader=1, name=idpName+'Tra')
                                        matteShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(matteShader+'SG'))
                                        mc.connectAttr((matteShader +'.outColor'),(matteShaderSG +'.surfaceShader'), f=1)
                                        mc.setAttr(matteShader+'.color',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                                        mc.setAttr(matteShader+'.ambientColor',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                                        mc.setAttr(matteShader+'.matteOpacityMode',2)
                                        mc.setAttr(matteShader+'.matteOpacity',float(matteShaderAttr[2]))
                                        mc.connectAttr(RBG_Tra_SG_transparency_dict[checkSG], (matteShader +'.transparency'), f=1)
                                        mc.sets(onlyShapeFace_dict[selectShapeOnly], e=1, forceElement=matteShaderSG)
                                else:
                                    print (u'---进入为多透贴选模型模式---')
                                    # 选模型的话就按几个透贴几个材质球直接赋就行了,有的SG 关联的模型信息为[]
                                    # 因为SG节点有时是有链接，也有透贴，但没选中模型，下面多判断一下，就不多生成材质球了
                                    if len(preOBJfinalTraInfo_dict[checkSG]) != 0:
                                        matteShader = mc.shadingNode('lambert', asShader=1, name=idpName+'Tra')
                                        matteShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(matteShader+'SG'))
                                        mc.connectAttr((matteShader +'.outColor'),(matteShaderSG +'.surfaceShader'), f=1)
                                        mc.setAttr(matteShader+'.color',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                                        mc.setAttr(matteShader+'.ambientColor',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                                        mc.setAttr(matteShader+'.matteOpacityMode',2)
                                        mc.setAttr(matteShader+'.matteOpacity',float(matteShaderAttr[2]))
                                        mc.connectAttr(RBG_Tra_SG_transparency_dict[checkSG], (matteShader +'.transparency'), f=1)
                                        mc.sets(preOBJfinalTraInfo_dict[checkSG], e=1, forceElement=matteShaderSG)
                                        print (u'====【选整个模型赋予，带多透贴,打印SG节点,结束】== %s'%checkSG)
                                        mc.select(clear=1)
                    else:
                        # 以下物体透贴为一个
                        # 先生成材质球并连好透贴
                        print (u'---成功进入单物体单透贴算法 ---')
                        matteShader = mc.shadingNode('lambert',asShader=1,name = idpName+'Tra')
                        matteShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(matteShader+'SG'))
                        mc.connectAttr((matteShader +'.outColor'),(matteShaderSG +'.surfaceShader'),f=1)
                        mc.setAttr(matteShader+'.color',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                        mc.setAttr(matteShader+'.ambientColor',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                        mc.setAttr(matteShader+'.matteOpacityMode',2)
                        mc.setAttr(matteShader+'.matteOpacity',float(matteShaderAttr[2]))
                        mc.connectAttr(RBG_Tra_objTraAttr_dict[selectShapeOnly][0],(matteShader +'.transparency'),f=1)
                        print (u'===========【完成透明贴图属性连接】%s==========='%(RBG_Tra_objTraAttr_dict[selectShapeOnly][0]))
                        # 从字典读取选面的内容,判断是否有选面
                        print (u'===========【选面的话，打印选面的字典信息】%s==========='%onlyShapeFace_dict.keys())
                        if len(onlyShapeFace_dict.keys()) != 0 and selectShapeOnly in onlyShapeFace_dict.keys():
                            selectShapeFaces = onlyShapeFace_dict[selectShapeOnly]
                            mc.sets(selectShapeFaces,e=1, forceElement = matteShaderSG)
                            print (u'====【选面赋予，带单透贴】%s==========='%selectShapeFaces)
                        else:
                            mc.sets(selectShapeOnly,e=1, forceElement = matteShaderSG)
                            print (u'====【选整个模型赋予，带单透贴】== %s'%selectShapeOnly)
    #------------------------------#
    # 【通用】【检测SG节点上是否有透贴】
    #------------------------------#
    def TF_CheckSGandTransparency(self,ObjShaderSG):
        ObjShader = mc.listConnections(ObjShaderSG+'.surfaceShader',s=1,d=0,c=0)[0]
        ObjTransparencyFile = []
        try:
            ObjTransparencyFile = mc.listConnections(ObjShader+'.transparency',s=1,d=0,c=0,p=0)[0]
        except:
            pass
        try:
            ObjTransparencyFile = mc.listConnections(ObjShader+'.outTransparency',s=1,d=0,c=0,p=0)[0]
        except:
            pass
        if mc.objExists(ObjTransparencyFile):
            return True
        else:
            return False
    #------------------------------#
    # 【通用】【给出SG节点，得到所选模型的相关SG节点的点信息】
    #------------------------------#
    def TF_shaderSG_getMeshFaceInfo(self,ObjShaderSG):
        pass

    #------------------------------#
    # 【通用】【Z景深材质赋予】
    #  Z景深材质球，带本地透明通道
    #------------------------------#
    def TF_ZdepthTransparencyShader(self):
        selectObjs = mc.ls(sl=1,l=1)
        materialsNodes =mc.ls(mat=1)
        shaderNode = 'Zdepth_shader'
        setRangeNode = 'Zdepth_setRange'
        multiplyDivide1Node = 'Zdepth_MD'
        samplerInfoNode = 'Zdepth_samplerInfo'
        if shaderNode not in materialsNodes:
            ZdepthShader = mc.shadingNode('lambert',asShader=1,name = shaderNode)
            mc.addAttr(ZdepthShader,sn='black',longName='black',nn='black',attributeType='float')
            mc.addAttr(ZdepthShader,sn='white',longName='white',nn='white',attributeType='float')
            mc.setAttr(ZdepthShader+'.black',0)
            mc.setAttr(ZdepthShader+'.white',1)
            ZdepthShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(ZdepthShader+'SG'))
            mc.connectAttr((ZdepthShader +'.outColor'),(ZdepthShaderSG +'.surfaceShader'),f=1)
            mc.setAttr(ZdepthShader+'.ambientColor',1,1,1,type ='double3')
            mc.setAttr(ZdepthShader+'.diffuse',0)
            ZdepthSetRang = mc.shadingNode('setRange',asUtility=1,name = setRangeNode)
            mc.setAttr(ZdepthSetRang+'.oldMaxZ',3000)
            ZdepthMultiplyDivide = mc.shadingNode('multiplyDivide',asUtility=1,name = multiplyDivide1Node)
            mc.setAttr(ZdepthMultiplyDivide+'.input2Z',-1.0)
            ZdepthSamplerInfo = mc.shadingNode('samplerInfo',asUtility=1,name = samplerInfoNode)
            mc.addAttr(ZdepthSamplerInfo,sn='CNCP',longName='cameraNearClipPlane',nn='cameraNearClipPlane',attributeType='float')
            mc.addAttr(ZdepthSamplerInfo,sn='CFCP',longName='cameraFarClipPlane',nn='cameraFarClipPlane',attributeType='float')
            #属性连接
            mc.connectAttr((ZdepthSetRang +'.outValueZ'),(ZdepthShader +'.colorR'),f=1)
            mc.connectAttr((ZdepthSetRang +'.outValueZ'),(ZdepthShader +'.colorG'),f=1)
            mc.connectAttr((ZdepthSetRang +'.outValueZ'),(ZdepthShader +'.colorB'),f=1)
            mc.connectAttr((ZdepthShader +'.black'),(ZdepthSetRang +'.maxZ'),f=1)
            mc.connectAttr((ZdepthShader +'.white'),(ZdepthSetRang +'.minZ'),f=1)
            mc.connectAttr((ZdepthSamplerInfo +'.cameraNearClipPlane'),(ZdepthSetRang +'.oldMinZ'),f=1)
            mc.connectAttr((ZdepthSamplerInfo +'.pointCameraZ'),(ZdepthMultiplyDivide +'.input1Z'),f=1)
            mc.connectAttr((ZdepthMultiplyDivide +'.outputZ'),(ZdepthSetRang +'.valueZ'),f=1)
        else:
            ZdepthShader = shaderNode
            ZdepthShaderSG = ZdepthShader+'SG'
            ZdepthSetRang = setRangeNode
        #读取透明信息，写入字典
        transparencyInfoDict = self.TF_transparencyInfoDictInfo(selectObjs)
        #选择的物体先赋一遍Zdepth材质
        for selectObj in selectObjs:
            mc.sets(selectObj,e=1, forceElement = ZdepthShaderSG)
        # 如果为带透贴的，再继续加材质球。
        if transparencyInfoDict:
            keys = transparencyInfoDict.keys()
            for i in range(len(keys)):
                ZdepthShader = mc.shadingNode('lambert',asShader=1,name = shaderNode+'Tra')
                mc.addAttr(ZdepthShader,sn='black',longName='black',nn='black',attributeType='float')
                mc.addAttr(ZdepthShader,sn='white',longName='white',nn='white',attributeType='float')
                mc.setAttr(ZdepthShader+'.black',0)
                mc.setAttr(ZdepthShader+'.white',1)
                ZdepthShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(ZdepthShader+'SG'))
                mc.connectAttr((ZdepthShader +'.outColor'),(ZdepthShaderSG +'.surfaceShader'),f=1)
                #属性连接
                mc.connectAttr((ZdepthSetRang +'.outValueZ'),(ZdepthShader +'.colorR'),f=1)
                mc.connectAttr((ZdepthSetRang +'.outValueZ'),(ZdepthShader +'.colorG'),f=1)
                mc.connectAttr((ZdepthSetRang +'.outValueZ'),(ZdepthShader +'.colorB'),f=1)
                #关于远近摄像机用上面第一次的材质球控制
                #mc.connectAttr((ZdepthShader +'.black'),(ZdepthSetRang +'.maxZ'),f=1)
                #mc.connectAttr((ZdepthShader +'.white'),(ZdepthSetRang +'.minZ'),f=1)
                mc.connectAttr(keys[i],(ZdepthShader +'.transparency'),f=1)
                mc.sets(transparencyInfoDict[keys[i]],e=1, forceElement = ZdepthShaderSG)
    #------------------------------#
    # 【通用】【阴影】
    #------------------------------#
    def TF_shadowShader(self):
        selectObjs = mc.ls(sl=1,l=1)
        materialsNodes =mc.ls(mat=1)
        shaderNode = 'shadow_shader'
        if shaderNode not in materialsNodes:
            shadowShader = mc.shadingNode('useBackground',asShader=1,name = shaderNode)
            mc.setAttr(shadowShader+'.reflectivity',0)
            mc.setAttr(shadowShader+'.reflectionLimit',0)
            mc.setAttr(shadowShader+'.shadowMask',1)
            shadowShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(shadowShader+'SG'))
            mc.connectAttr((shadowShader +'.outColor'),(shadowShaderSG +'.surfaceShader'),f=1)
        else:
            shadowShader = shaderNode
            shadowShaderSG = shadowShader+'SG'
        for selectObj in selectObjs:
            mc.sets(selectObj,e=1, forceElement = shadowShaderSG)
    #------------------------------#
    # 【通用】【OCC带透明材质赋予】
    #  transparency=1为添加透明通道，0为不添加透明通道
    #------------------------------#
    def TF_OCCShader(self, transparency=1):
        selectObjs = mc.ls(sl=1,l=1)
        materialsNodes =mc.ls(mat=1)
        shaderName = 'OCC_shader'
        OCCTextureName = 'OCC_texture'
        if (mc.pluginInfo('Mayatomr.mll',query=1,loaded=1) == False):
            mc.loadPlugin('Mayatomr.mll')
        if shaderName not in materialsNodes:
            OCCTexture = mc.shadingNode('mib_amb_occlusion',asTexture=1,name = OCCTextureName)
            mc.setAttr(OCCTexture+'.samples',128)
            mc.setAttr(OCCTexture+'.spread',1)
            mc.setAttr(OCCTexture+'.max_distance',3)
            mc.setAttr(OCCTexture+'.output_mode',0)
            mc.setAttr(OCCTexture+'.falloff',1)
            mc.setAttr(OCCTexture+'.id_inclexcl',0)
            OCCShader = mc.shadingNode('surfaceShader',asShader=1,name = shaderName)
            mc.connectAttr((OCCTexture +'.outValue'),(OCCShader +'.outColor'),f=1)
            OCCShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(OCCShader+'SG'))
            mc.connectAttr((OCCShader +'.outColor'),(OCCShaderSG +'.surfaceShader'),f=1)
        else:
            OCCShader = shaderName
            OCCShaderSG = OCCShader+'SG'
            OCCTexture = OCCTextureName
        # 如果需要读取透明信息，写入字典
        if transparency == 1:
            transparencyInfoDict = self.TF_transparencyInfoDictInfo(selectObjs)
            # 选择的物体先赋一遍OCC材质
            for selectObj in selectObjs:
                mc.sets(selectObj,e=1, forceElement = OCCShaderSG)
            # 如果为带透贴的，再继续加材质球。
            if transparencyInfoDict:
                keys = transparencyInfoDict.keys()
                for i in range(len(keys)):
                    OCCShader = mc.shadingNode('surfaceShader',asShader=1,name = shaderName+'Tra')
                    mc.connectAttr((OCCTexture +'.outValue'),(OCCShader +'.outColor'),f=1)
                    OCCShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(OCCShader+'SG'))
                    mc.connectAttr((OCCShader +'.outColor'),(OCCShaderSG +'.surfaceShader'),f=1)
                    mc.connectAttr(keys[i],(OCCShader +'.outTransparency'),f=1)
                    mc.sets(transparencyInfoDict[keys[i]],e=1, forceElement = OCCShaderSG)
        else:
            for selectObj in selectObjs:
                mc.sets(selectObj,e=1, forceElement = OCCShaderSG)
    # ------------------------------#
    # 【通用】【normal带透明材质赋予】
    #  transparency=1为添加透明通道，0为不添加透明通道
    # ------------------------------#
    def TF_normalShader(self,transparency=1):
        selectObjs = mc.ls(sl=1,l=1)
        materialsNodes =mc.ls(mat=1)
        shaderName = 'normal_shader'
        normalTextureName = 'normal_Texture'
        if (mc.pluginInfo('Mayatomr.mll', query=1, loaded=1) == False):
            mc.loadPlugin('Mayatomr.mll')
        if shaderName not in materialsNodes:
            normalTexture = mc.shadingNode('mib_amb_occlusion', asTexture=1, name=normalTextureName)
            mc.setAttr(normalTexture+'.samples', 128)
            mc.setAttr(normalTexture+'.spread', 0.8)
            mc.setAttr(normalTexture+'.max_distance', 3)
            mc.setAttr(normalTexture+'.output_mode', 3)
            normalShader = mc.shadingNode('surfaceShader', asShader=1, name=shaderName)
            mc.connectAttr((normalTexture + '.outValue'), (normalShader + '.outColor'), f=1)
            normalShaderSG = mc.sets(renderable=1, noSurfaceShader =1,empty=1,name =(normalShader+'SG'))
            mc.connectAttr((normalShader + '.outColor'), (normalShaderSG + '.surfaceShader'), f=1)
        else:
            normalShader = shaderName
            normalShaderSG = normalShader+'SG'
            normalTexture = normalTextureName
        # 如果需要读取透明信息，写入字典
        if transparency == 1:
            transparencyInfoDict = self.TF_transparencyInfoDictInfo(selectObjs)
            # 选择的物体先赋一遍Normal材质
            for selectObj in selectObjs:
                mc.sets(selectObj, e=1, forceElement=normalShaderSG)
            # 如果为带透贴的，再继续加材质球。
            if transparencyInfoDict:
                keys = transparencyInfoDict.keys()
                for i in range(len(keys)):
                    normalShader = mc.shadingNode('surfaceShader', asShader=1, name=shaderName+'Tra')
                    mc.connectAttr((normalTexture + '.outValue'), (normalShader + '.outColor'), f=1)
                    normalShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(normalShader+'SG'))
                    mc.connectAttr((normalShader + '.outColor'), (normalShaderSG + '.surfaceShader'), f=1)
                    mc.connectAttr(keys[i], (normalShader + '.outTransparency'), f=1)
                    mc.sets(transparencyInfoDict[keys[i]], e=1, forceElement=normalShaderSG)
        else:
            for selectObj in selectObjs:
                mc.sets(selectObj, e=1, forceElement=normalShaderSG)
    # ------------------------------#
    # 【通用】【边缘光带透明材质赋予】
    #  transparency=1为添加透明通道，0为不添加透明通道
    # ------------------------------#
    def TF_FresnelShader(self,transparency=1):
        selectObjs = mc.ls(sl=1,l=1)
        materialsNodes =mc.ls(mat=1)
        shaderNode = 'fresnel_shader'
        freRampNode = 'fresnel_Ramp'
        freSamplerInfoNode = 'fresnel_samplerInfo'
        if shaderNode not in materialsNodes:
            freSamplerInfo = mc.shadingNode('samplerInfo',asUtility=1,name = freSamplerInfoNode)
            fresnelRamp = mc.shadingNode('ramp',asTexture=1,name = freRampNode)
            mc.setAttr(fresnelRamp+'.colorEntryList[0].color',1,1,1,type ='double3')
            mc.setAttr(fresnelRamp+'.colorEntryList[2].color',0,0,0,type ='double3')
            mc.setAttr(fresnelRamp+'.colorEntryList[2].position',1)
            mc.setAttr(fresnelRamp+'.colorEntryList[0].position',0)
            mc.connectAttr((freSamplerInfo +'.facingRatio'),(fresnelRamp +'.uvCoord.uCoord'),f=1)
            mc.connectAttr((freSamplerInfo +'.facingRatio'),(fresnelRamp +'.uvCoord.vCoord'),f=1)
            fresnelShader = mc.shadingNode('lambert',asShader=1,name = shaderNode)
            mc.setAttr(fresnelShader+'.ambientColor',1,1,1,type ='double3')
            mc.setAttr(fresnelShader+'.diffuse',0)
            mc.setAttr(fresnelShader+'.matteOpacityMode',2)
            mc.setAttr(fresnelShader+'.matteOpacity',0)
            mc.connectAttr((fresnelRamp +'.outColor'),(fresnelShader +'.color'),f=1)
            fresnelShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(fresnelShader+'SG'))
            mc.connectAttr((fresnelShader +'.outColor'),(fresnelShaderSG +'.surfaceShader'),f=1)
        else:
            fresnelShader = 'fresnel_shader'
            fresnelShaderSG = fresnelShader +'SG'
            fresnelRamp =  'fresnel_Ramp'
        # 如果需要读取透明信息，写入字典
        if transparency==1:
            transparencyInfoDict = self.TF_transparencyInfoDictInfo(selectObjs)
            # 选择的物体先赋一遍fresnel材质
            for selectObj in selectObjs:
                mc.sets(selectObj,e=1, forceElement = fresnelShaderSG)
            # 如果为带透贴的，再继续加材质球。
            if transparencyInfoDict:
                keys = transparencyInfoDict.keys()
                for i in range(len(keys)):
                    fresnelShader = mc.shadingNode('lambert',asShader=1,name = shaderNode+'Tra')
                    mc.setAttr(fresnelShader+'.ambientColor',1,1,1,type ='double3')
                    mc.setAttr(fresnelShader+'.diffuse',0)
                    mc.setAttr(fresnelShader+'.matteOpacityMode',2)
                    mc.setAttr(fresnelShader+'.matteOpacity',0)
                    mc.connectAttr((fresnelRamp +'.outColor'),(fresnelShader +'.color'),f=1)
                    fresnelShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(fresnelShader+'SG'))
                    mc.connectAttr((fresnelShader +'.outColor'),(fresnelShaderSG +'.surfaceShader'),f=1)
                    mc.connectAttr(keys[i],(fresnelShader +'.transparency'),f=1)
                    mc.sets(transparencyInfoDict[keys[i]],e=1, forceElement = fresnelShaderSG)
        else:
            for selectObj in selectObjs:
                mc.sets(selectObj,e=1, forceElement = fresnelShaderSG)
    # ------------------------------#
    # 【通用】【场景灯光层带透明材质赋予】
    #  transparency=1为添加透明通道，0为不添加透明通道
    # ------------------------------#
    def TF_setsLGTShader(self,transparency=1):
        selectObjs = mc.ls(sl=1,l=1)
        materialsNodes =mc.ls(mat=1)
        shaderNode = 'setsLGT_shader'
        if shaderNode not in materialsNodes:
            setsLGTShader = mc.shadingNode('lambert',asShader=1,name = shaderNode)
            setsLGTShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(setsLGTShader+'SG'))
            mc.connectAttr((setsLGTShader +'.outColor'),(setsLGTShaderSG +'.surfaceShader'),f=1)
            mc.setAttr(setsLGTShader+'.color',1,1,1,type ='double3')
        else:
            shaderNode = 'setsLGT_shader'
            setsLGTShaderSG = shaderNode +'SG'
        # 如果需要读取透明信息，写入字典
        if transparency == 1:
            transparencyInfoDict = self.TF_transparencyInfoDictInfo(selectObjs)
            # 选择的物体先赋一遍LGT材质
            for selectObj in selectObjs:
                mc.sets(selectObj,e=1, forceElement = setsLGTShaderSG)
            # 如果为带透贴的，再继续加材质球。
            if transparencyInfoDict:
                keys = transparencyInfoDict.keys()
                for i in range(len(keys)):
                    setsLGTShader = mc.shadingNode('lambert',asShader=1,name = shaderNode+'Tra')
                    setsLGTShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(setsLGTShader+'SG'))
                    mc.connectAttr((setsLGTShader +'.outColor'),(setsLGTShaderSG +'.surfaceShader'),f=1)
                    mc.setAttr(setsLGTShader+'.color',1,1,1,type ='double3')
                    mc.connectAttr(keys[i],(setsLGTShader +'.transparency'),f=1)
                    mc.sets(transparencyInfoDict[keys[i]],e=1, forceElement = setsLGTShaderSG)
        else:
            for selectObj in selectObjs:
                mc.sets(selectObj,e=1, forceElement = setsLGTShaderSG)

    # ------------------------------#
    # 【通用】【idpass遮罩材质赋模型信息输出】
    #  兼容选面，不上传透贴信息，透贴信息另外上传。
    # id为大编号，角色1~10，场景11~20;有几个id就分几层。
    #  Z:\Projects\ToothFairies\Project\data\RLayerInfo\RGB
    # ------------------------------#
    def TF_RGBMAInfoExport(self, idp):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        materialsNodes =mc.ls(mat=1)
        for shader in materialsNodes:
            SG = mc.listConnections((shader + '.outColor'),s=0,d=1)
            mesh = mc.sets(SG,q=1)
            # 要加shader节点或SG节点是否有连接mesh,空的话会报错
            # 读取SG时，只是会读到每层的信息，如果本层无连接mesh，是返回为 空
            if 'IdpR_colorR' in shader and mc.nodeType(shader) == 'lambert' and mesh:
                mc.select(shader,r=1)
                sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(idp,"R",1)
            elif 'IdpG_colorG' in shader and mc.nodeType(shader) == 'lambert'and mesh:
                mc.select(shader,r=1)
                sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(idp,"G",1)
            elif 'IdpB_colorB' in shader and mc.nodeType(shader) == 'lambert'and mesh:
                mc.select(shader,r=1)
                sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(idp,"B",1)
            elif 'IdpM_matte' in shader and mc.nodeType(shader) == 'lambert'and mesh:
                mc.select(shader,r=1)
                sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(idp,"M",1)
            elif 'IdpA_alpha' in shader and mc.nodeType(shader) == 'lambert'and mesh:
                mc.select(shader,r=1)
                sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(idp,"A",1)

    # ------------------------------#
    # 【通用】【记录idpass遮罩材质赋模型信息】
    #  用字典重新写入，以每个角色为单位，一个路径一个字典。
    #  key为材质球颜色，内容为 shape 节点信息
    #  taskFileNamePath = 'Z:/Projects/ToothFairies/Project/data/RLayerInfo/RGB/id01/c001001Airlie/'
    # ------------------------------#
    def TF_RGBMAInfoReadIn(self,taskFileNamePath):
        taskRGBMAInfoDict = dict({})
        taksRGBinfoTXTs = mc.getFileList(folder=taskFileNamePath)
        # [u'RGB_c001001Airlie_B_geo.txt', u'RGB_c001001Airlie_G_geo.txt', u'RGB_c001001Airlie_M_geo.txt', u'RGB_c001001Airlie_R_geo.txt']
        for taksRGBinfoTXT in taksRGBinfoTXTs:
            taskFileAllPath = taskFileNamePath+taksRGBinfoTXT
            taskInfos = sk_infoConfig.sk_infoConfig().checkFileRead(taskFileAllPath)
            shaderAttr = taskInfos[0]
            meshInfos = taskInfos[1:]
            taskRGBMAInfoDict[shaderAttr] = meshInfos
        return taskRGBMAInfoDict

    #------------------------------#
    #  专门为读取网上赋遮罩材质信息做的RGBMA赋材质
    #------------------------------#
    def TF_RBGMApassServerImport(self,taskFileNamePath,taskFile,nameSpace,prefixMODEL):
        # 赋RGB材质信息.角色名下所有txt文件名称
        taksRGBinfoTXTs = mc.getFileList(folder=taskFileNamePath)
        # 赋透明材质json文件路径
        TraFilePath = 'Z:/Projects/ToothFairies/Project/data/AssetInfo/transInfo/'+taskFile+'.json'
        TraInfoJson = dict({})
        Tra = 0
        if os.path.isfile(TraFilePath)==True:
            # 读取透明信息
            Tra = 1
            with open((TraFilePath), "r") as f:
                 data = json.loads(f.read())
            for texture,objs in data.items():
                TraTexturePath = texture
                TralongNameForMeshInfos = []
                # 断名，取出model组，用MODEL往后的名称
                for obj in objs:
                    if '|MODEL|' in obj:
                        newName = obj.split('MODEL')[1]
                        # 添加长命名
                        TralongNameForMesh = newName.replace('|', ('|' + nameSpace+ ':'))
                        # 添加前缀
                        NewName = prefixMODEL+'MODEL'+TralongNameForMesh
                        if NewName not in TralongNameForMeshInfos:
                            TralongNameForMeshInfos.append(NewName)
                TraInfoJson[TraTexturePath] = TralongNameForMeshInfos
        else:
            print (u'===========【物体无透明贴图】%s==========='%taskFile)
        print (u'====【打印透贴字典】%s===='%TraInfoJson)
        materialsNodes =mc.ls(mat=1)
        # 一堆txt文件按R、G、B 分别保存
        for taksRGBinfoTXT in taksRGBinfoTXTs:
            taskFileAllPath = taskFileNamePath+taksRGBinfoTXT
            print (u'====【打印此角色RGB信息路径】%s===='%taskFileAllPath)
            taskInfos = sk_infoConfig.sk_infoConfig().checkFileRead(taskFileAllPath)
            shaderColor = taskInfos[0]
            meshInfos = taskInfos[1:]
            # 断名，取出model组，用MODEL往后的名称
            longNameForMeshInfos = []
            # 上面材质球，赋的模型和面的信息，加长名和MODEL前缀。
            for meshInfo in meshInfos:
                if '|MODEL|' in meshInfo:
                    newName = meshInfo.split('MODEL')[1]
                    # 添加长命名
                    longNameForMesh = newName.replace('|', ('|' + nameSpace + ':'))
                    # 添加前缀
                    NewName = prefixMODEL+'MODEL'+longNameForMesh
                    if NewName not in longNameForMeshInfos:
                        longNameForMeshInfos.append(NewName)
            if '_R_geo' in taksRGBinfoTXT:
                idpName = 'IdpR_colorR'
                matteShaderAttr = [(1,0,0),(0,0,0),0]
            elif '_G_geo' in taksRGBinfoTXT:
                idpName = 'IdpG_colorG'
                matteShaderAttr = [(0,1,0),(0,0,0),0]
            elif '_B_geo' in taksRGBinfoTXT:
                idpName = 'IdpB_colorB'
                matteShaderAttr = [(0,0,1),(0,0,0),0]
            elif '_M_geo' in taksRGBinfoTXT:
                idpName = 'IdpM_matte'
                matteShaderAttr = [(0,0,0),(0,0,0),0]
            elif '_A_geo' in taksRGBinfoTXT:
                idpName = 'IdpA_alpha'
                matteShaderAttr = [(0,0,0),(1,1,1),1]
            print (u'====【上面角色的%s材质下连接的模型】%s'%(idpName, longNameForMeshInfos))
            if idpName not in materialsNodes:
                matteShader = mc.shadingNode('lambert',asShader=1,name = idpName)
                matteShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(matteShader+'SG'))
                mc.connectAttr((matteShader +'.outColor'),(matteShaderSG +'.surfaceShader'),f=1)
                mc.setAttr(matteShader+'.color',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                mc.setAttr(matteShader+'.ambientColor',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                mc.setAttr(matteShader+'.matteOpacityMode',2)
                mc.setAttr(matteShader+'.matteOpacity',float(matteShaderAttr[2]))
            else:
                matteShader = idpName
                matteShaderSG = matteShader+'SG'
            # 先赋予指定材质球给指定的模型
            for longNameForMeshInfo in longNameForMeshInfos:
                mc.sets(longNameForMeshInfo,e=1, forceElement = matteShaderSG)
            # 如果为带透贴的，再继续加材质球。
            # 以下为透明信息添加
            if Tra == 1:
                print (u'----进入导透贴----')
                TraInfoJsonKeys = TraInfoJson.keys()
                for i in range(len(TraInfoJsonKeys)):
                    TraTextureFilePath = TraInfoJsonKeys[i]
                    exname=''
                    if '/' in TraTextureFilePath:
                        exname = TraTextureFilePath.split('/')[-1].split('.')[0]
                    else:
                        exname = TraTextureFilePath.split('.')[0]
                    # 每个透贴路径，生成一个File文件连接组
                    fileNode = mc.shadingNode('file',asUtility=1, name='file_'+exname)
                    mc.setAttr((fileNode+'.fileTextureName'), TraTextureFilePath,type='string')
                    place2dTextureNode = mc.shadingNode('place2dTexture',asUtility=1,name = 'p2DTex_'+exname)
                    try:
                        mc.connectAttr((place2dTextureNode+'.outUvFilterSize'), (fileNode+'.uvFilterSize'), f=1)
                    except:
                        print TraInfoJsonKeys[i]
                    try:
                        mc.connectAttr((place2dTextureNode+'.outUV'), (fileNode+'.uvCoord'), f=1)
                    except:
                        print TraInfoJsonKeys[i]
                    # 每个透贴路径连接的模型点面信息。
                    TraShapes = TraInfoJson[TraTextureFilePath]
                    print (u'====【打印透贴字典】%s===='%TraTextureFilePath,TraShapes)
                    # 每个透贴路径连接的模型
                    for TraShape in TraShapes:
                        mesh = mc.ls(TraShape, l=1, o=1)[0]
                        print (u'====【如果为面或体时，都转为shape】%s===='%mesh)
                        # 选中的模型
                        for longNameForMeshInfo in longNameForMeshInfos:
                            # 选中的模型改为shape模式
                            selectMesh = mc.ls(longNameForMeshInfo, l=1, o=1)[0]
                            # 如果模型上有wing的属性才加透贴
                            # 每个透贴连接的模型和选中的模型对比，重合的加材质球
                            if selectMesh == TraShape and (self.CJW_readTansformAttr(selectMesh, 'wing') or self.CJW_readTansformAttr(selectMesh, 'Tra')):
                                matteShader = mc.shadingNode('lambert',asShader=1,name = idpName+'Tra')
                                matteShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(matteShader+'SG'))
                                mc.connectAttr((matteShader +'.outColor'),(matteShaderSG +'.surfaceShader'),f=1)
                                mc.setAttr(matteShader+'.color',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                                mc.setAttr(matteShader+'.ambientColor',float(matteShaderAttr[0][0]),float(matteShaderAttr[0][1]),float(matteShaderAttr[0][2]),type ='double3')
                                mc.setAttr(matteShader+'.matteOpacityMode',2)
                                mc.setAttr(matteShader+'.matteOpacity',float(matteShaderAttr[2]))
                                # 连接透贴File节点到材质球上
                                mc.connectAttr((fileNode+'.outColor '), (matteShader+'.transparency'), f=1)
                                mc.sets(longNameForMeshInfo,e=1, forceElement = matteShaderSG)
                                print (u'====【透贴连接成功】%s===='%matteShader)
                        '''
                        ObjShaderSGs = mc.listConnections(mesh, s=0, d=1, c=0, type='shadingEngine')
                        ObjShaderSGsCleans = []
                        for ObjShaderSG in ObjShaderSGs:
                            if ObjShaderSG not in ObjShaderSGsCleans:
                                ObjShaderSGsCleans.append(ObjShaderSG)
                        print (u'====【此透贴此模型连接的所有SG节点】%s===='%ObjShaderSGsCleans)
                        for ObjShaderSG in ObjShaderSGsCleans:
                            ObjShader = mc.listConnections(ObjShaderSG+'.surfaceShader', s=1, d=0, c=0)[0]
                            fileNode = mc.shadingNode('file',asUtility=1, name='file_'+exname)
                            mc.setAttr((fileNode+'.fileTextureName'), TraTextureFilePath,type='string')
                            mc.connectAttr((fileNode+'.outColor '), (ObjShader+'.transparency'), f=1)
                            place2dTextureNode = mc.shadingNode('place2dTexture',asUtility=1,name = 'p2DTex_'+exname)
                            mc.connectAttr((place2dTextureNode+'.outUvFilterSize '), (fileNode+'.uvFilterSize'), f=1)
                            mc.connectAttr((place2dTextureNode+'.outUV '), (fileNode+'.uvCoord'), f=1)
                    print (u'====【透贴连接成功】%s===='%exname)
                    '''
    #------------------------------#
    # 【通用】【根据网上RGBMA信息创建渲染层】
    # 每个ID一层。
    #  Z:\Projects\ToothFairies\Project\data\RLayerInfo\RGB
    #------------------------------#
    def TF_RGBMAInfoLayerCreat(self,type='chr',im=1):
        # 不加入RGB层里的角色
        noRenderCharacters = ['c009001Toothmouse','c013001PixelPixieFemale','c014001PixelPixieMale','c019001ReffieLion','c020001TambiKitten','c022001RosieSkunk','c023001RainbowBunny','c021001SnowettePoodle']
        #
        #allRef = pm.system.listReferences()
        # [FileReference(u'//file-cluster/GDC/Projects/ToothFairies/Project/scenes/characters/c003001Twinkle/master/tf_c003001Twinkle_h_ms_render.mb', refnode=u'tf_c003001TwinkleRN'),FileReference(u'//file-cluster/GDC/Projects/ToothFairies/Project/scenes/characters/c016001Kabria/master/tf_c016001Kabria_h_ms_render.mb', refnode=u'tf_c016001KabriaRN'), FileReference(u'//file-cluster/GDC/Projects/ToothFairies/Project/scenes/characters/c017001AirlieDad/master/tf_c017001AirlieDad_h_ms_render.mb', refnode=u'tf_c017001AirlieDadRN'),FileReference(u'//file-cluster/GDC/Projects/ToothFairies/Project/scenes/characters/c001014Airlie4yearsold/master/tf_c001014Airlie4yearsold_h_ms_render.mb', refnode=u'tf_c001014Airlie4yearsoldRN')]
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        # u'//file-cluster/GDC/Projects/ToothFairies/Project/'
        idFiles = mc.getFileList(folder = serverPath+'data/RLayerInfo/RGB/')
        # [u'id01', u'id02', u'id03', u'id04', u'id11']
        # 清除非参考nameSpace
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        refNamespace = mc.namespaceInfo(listOnlyNamespaces=1)
        #  [u'UI',u'shared',u'tf_c001014Airlie4yearsold',u'tf_c003001Twinkle',u'tf_c016001Kabria',u'tf_c017001AirlieDad']
        if im==1:
            self.nj_RefIm()
            mel.eval('source zwResetShadingEnginesN')
            mel.eval('zwResetShadingEnginesN()')
        for ns in refNamespace:
            if 'tf_' not in ns or 'c009001' in ns or 'c013001' in ns or 'c014001' in ns or 'c019001' in ns or 'c020001' in ns or 'c022001' in ns or 'c023001' in ns or 'c021001' in ns:
                continue
            #if ns.split('_')[1][0] in ['c'] and noRenderChr not in ns:
            if ns.split('_')[1][0] in ['c','p']:
                objname = ns.split('_')[1]
                # u'tf_c001014Airlie4yearsold'
                prefixMODEL = []
                #if mc.objExists(ns + ':CHR|'+ns+':MODEL|'+ns+':MSH_all'):
                if mc.objExists(ns+':MODEL|'+ns+':MSH_all'):
                    needMeshFull = mc.ls((ns+':MODEL|'+ns+':MSH_all'), l=1)
                    # u'|tf_c017001AirlieDadRNgroup|tf_c017001AirlieDad:CHR|tf_c017001AirlieDad:MODEL|tf_c017001AirlieDad:MSH_all'
                    taskAllShapes = self.TF_CleanNoIntermediateShapeNodes(needMeshFull)
                    # print (u'====【打印需要输出的模型1%s】===='%taskAllShapes)
                    taskAllShapes2 = self.TF_switchGroup(taskAllShapes)
                    # print (u'====【打印需要输出的模型2%s】===='%taskAllShapes2)
                    # 切一个Model组前的前缀，来匹配上材质时名称对应。
                    prefixMODEL = taskAllShapes2[0].split('MODEL')[0]
                else:
                    print '------------------'
                    print ns
                    mc.warning(u'========================【！！！文件内无法查到角色参考！！！】========================')
                    mc.error(u'========================【！！！文件内无法查到角色参考！！！】========================')
                for idFile in idFiles:
                    tempNum = int(idFile.split('id')[1])
                    if tempNum < 11:
                        taskFilesInIDXX = mc.getFileList(folder=serverPath+'data/RLayerInfo/RGB/'+idFile+'/')
                        # [u'c001001Airlie', u'c003001Twinkle', u'c021001SnowettePoodle', u'c022001RosieSkunk']
                        # 遍历所有id文件，建立渲染层
                        for taskFile in taskFilesInIDXX:
                            if re.match(objname, taskFile, re.IGNORECASE):
                                idLayer = 'chr'+idFile
                                if mc.objExists(idLayer):
                                    mc.editRenderLayerMembers(idLayer, taskAllShapes2, noRecurse=0)
                                    # 清理一次带标注的模型，（眼球反光膜不放入渲染层内）
                                    for taskAllShape in taskAllShapes2:
                                        if self.CJW_readTansformAttr(taskAllShape, '_norgb'):
                                            mc.editRenderLayerMembers(idLayer, taskAllShape, noRecurse=0, remove=1)
                                        # 把翅膀拿出非第一层
                                        if idLayer != 'chrid01':
                                            if self.CJW_readTansformAttr(taskAllShape, 'wing'):
                                                mc.editRenderLayerMembers(idLayer, taskAllShape, noRecurse=0, remove=1)
                                    mc.editRenderLayerGlobals(currentRenderLayer=idLayer)
                                    print (u'====【添加%s层】===='%idLayer)
                                else:
                                    mc.createRenderLayer(taskAllShapes2, noRecurse=1, makeCurrent=1, name=idLayer)
                                    sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
                                    # 渲染层属性设置
                                    self.CJW_setRenderSetting(renderUsing='mentalRay',type=0,imageFormatValue='iff')
                                    # 清理一次带标注的模型，（眼球反光膜不放入渲染层内）
                                    for taskAllShape in taskAllShapes2:
                                        if self.CJW_readTansformAttr(taskAllShape, '_norgb'):
                                            mc.editRenderLayerMembers(idLayer, taskAllShape, noRecurse=0, remove=1)
                                        # 把翅膀拿出非第一层
                                        if idLayer != 'chrid01':
                                            if self.CJW_readTansformAttr(taskAllShape, 'wing'):
                                                mc.editRenderLayerMembers(idLayer, taskAllShape, noRecurse=0, remove=1)
                                # 提供赋材质信息全路径,提供nameSpace,添加RGB信息,
                                taskFileNamePath = serverPath+'data/RLayerInfo/RGB/'+idFile+'/'+taskFile+'/'
                                self.TF_RBGMApassServerImport(taskFileNamePath, taskFile, ns, prefixMODEL)
                            else:
                                pass

    #------------------------------#
    # 【通用】【计算nameSpace】
    #------------------------------#
    def CJW_nameSpacTool(self,SelectObj):
        # SelectOBJs = mc.ls(sl=1)
        TheNameSpace = []
        if SelectObj == None or SelectObj == []:
            mc.error(u'=====请选择相关角色=====')
        else:
            # 转长名
            SelectObj = mc.ls(SelectObj, l=1)[0]
            buffer = SelectObj.split('|')[-1]
            prefix = buffer.split(':')
            TheNameSpace = ''
            if len(prefix) > 1:
                for i in range(len(prefix)-1):
                    TheNameSpace = TheNameSpace + prefix[i]+":"
            if len(prefix) == 1:
                TheNameSpace = ''
        return TheNameSpace
    #------------------------------#
    # 【通用】【建立渲染层】
    #------------------------------#
    def CJW_CreateRenderLayer(self,type='layer'):
        # 得到所有渲染层,关掉默认渲染层
        layerAttar = mc.listConnections('renderLayerManager.renderLayerId')
        for item in layerAttar:
            if item in "*:*defaultRenderLayer*" or item in "*defaultRenderLayer*":
                mc.setAttr(item+'.renderable', 0)
        renderLayer = mc.createRenderLayer(noRecurse=1, makeCurrent=1, name=type)
        mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
        return renderLayer

    #------------------------------#
    # 【通用】【渲染层渲染属性设置】 typt=0为角色，1为场景
    #------------------------------#
    def CJW_setRenderSetting(self, renderUsing = 'mentalRay', type=0, imageFormatValue='iff',fpsFrame=24):
        # MayaSoftware,mentalRay,Arnold
        # 先关掉默认渲染层
        AllLayerAttar = mc.listConnections('renderLayerManager.renderLayerId')
        for item in AllLayerAttar:
            if item in "*:*defaultRenderLayer*" or item in "*defaultRenderLayer*":
                mc.setAttr(item+'.renderable', 0)
        # mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
        # 基础属性调整
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<Layer>/<Scene>_<Layer>', type='string')
        mc.setAttr('defaultResolution.lockDeviceAspectRatio', 0)
        mc.setAttr('defaultResolution.width', 1920)
        mc.setAttr('defaultResolution.height', 1080)
        mc.setAttr('defaultResolution.pixelAspect', 0)
        mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        mc.setAttr('defaultResolution.dotsPerInch', 72)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        # 格式命名
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
        mc.setAttr('defaultRenderGlobals.periodInExt', 1)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
            mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        # FPS
        if fpsFrame == 25:
            mc.currentUnit(time='pal')
        if fpsFrame == 24:
            mc.currentUnit(time='film')
        if fpsFrame == 30:
            mc.currentUnit(time='ntsc')
        # 起始帧设置
        startFrame = int()
        endFrame = int()
        if startFrame and fpsFrame:
            # 起始帧
            mc.playbackOptions(min=startFrame)
            # 起始预留
            preStartFrame = startFrame - 10
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=endFrame)
            # 结束预留
            posEndFrame = endFrame + 10
            mc.playbackOptions(animationEndTime=posEndFrame)
            # 渲染范围设置
            mc.setAttr('defaultRenderGlobals.startFrame', startFrame)
            mc.setAttr('defaultRenderGlobals.endFrame', endFrame)
        # mr渲染器
        if renderUsing == 'mentalRay':
            if mc.pluginInfo('Mayatomr.mll', q=1, loaded=1) == 0:
                mc.loadPlugin('Mayatomr.mll')
                # mc.loadPlugin('Mayatomr', quiet=1)
                # mc.pluginInfo('Mayatomr', edit=1, aotoload=1)
            '''
            # 搜MR的节点然后清掉
            mentalRayNodes = mc.ls(type=['mentalrayItemsList','mentalrayGlobals','mentalrayOptions'])
            delMNs = []
            for mentalRayNode in mentalRayNodes:
                if mc.referenceQuery(mentalRayNode,inr=1) == 0 and mentalRayNode not in delMNs:
                     delMNs.append(mentalRayNode)
            try:
                mc.delete(delMNs)
            except:
                pass
            '''
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', typ='string')
            # 创建miDefaultOptions节点
            mel.eval('miCreateDefaultNodes()')
            # mel.eval('iCreateOtherOptionsNodesForURG()')
            # 读取之前创建的production_preset
            # mel.eval('nodePreset -load "miDefaultOptions" "production_mi"')
            # 删除天光，关闭FG
            mc.setAttr('miDefaultOptions.finalGather', 0)
            # try:
            #     mel.eval('miDeleteSunSky')
            # except:
            #     pass
            # 默认image format
            # mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            # mc.setAttr('defaultRenderGlobals.imageFormat',19)
            # 打开层属性覆盖，不过要先有其他层才能运行
            try:
                mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            except:
                pass
            if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
                if imageFormatValue == 'tga':
                    mc.optionMenuGrp('imageMenuMentalRay', e=1, value='Targa (tga)')
                if imageFormatValue == 'exr':
                    mc.optionMenuGrp('imageMenuMentalRay', e=1, value='OpenEXR (exr)')
                if imageFormatValue == 'iff':
                    mc.optionMenuGrp('imageMenuMentalRay', e=1, value='Maya IFF (iff)')
                # mc.setAttr('defaultRenderGlobals.imageFormat',19)
            mc.setAttr( "mentalrayGlobals.imageCompression", 0)
            #try:
            #    mel.eval('changeMentalRayImageFormat')
            #except:
            #    pass
            # mc.setAttr('defaultResolution.imageFormat', 16)
            mc.setAttr('miDefaultOptions.miRenderUsing', 2)
            # mc.control('miMinSampleCtrl',edit=1, enable=True)
            try:
                mc.editRenderLayerAdjustment('miDefaultOptions.maxSamples')
                mc.editRenderLayerAdjustment('miDefaultOptions.minSamples')
            except:
                pass
            mc.setAttr('miDefaultOptions.maxSamples', 2)
            mc.setAttr('miDefaultOptions.minSamples', 0)
            if type == 0:
                mc.setAttr('miDefaultOptions.contrastR', 0.01)
                mc.setAttr('miDefaultOptions.contrastG', 0.01)
                mc.setAttr('miDefaultOptions.contrastB', 0.01)
                mc.setAttr('miDefaultOptions.contrastA', 0.01)
            if type ==1:
                mc.setAttr('miDefaultOptions.contrastR', 0.1)
                mc.setAttr('miDefaultOptions.contrastG', 0.1)
                mc.setAttr('miDefaultOptions.contrastB', 0.1)
                mc.setAttr('miDefaultOptions.contrastA', 0.1)
            # mc.setAttr('miDefaultOptions.maxReflectionRays', 1)
            # mc.setAttr ('miDefaultOptions.maxRefractionRays', 1)
            # mc.setAttr ('miDefaultOptions.maxRayDepth', 2)
            # mc.setAttr ('miDefaultOptions.maxShadowRayDepth', 3)
            mc.setAttr('miDefaultOptions.filter', 2)
            mc.setAttr('miDefaultOptions.jitter', 1)

    #------------------------------#
    # 【通用】【建立角色颜色渲染层】
    #  选中角色某物体，把角色整体MODEL组下Shape放入层里
    #------------------------------#
    def TF_RenderColorLayer(self, layer='ChrColor'):
        selectObjs = mc.ls(sl=1, l=1)
        mc.select(cl=1)
        # 建立渲染层
        renderlayer = self.CJW_CreateRenderLayer(layer)
        sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
        # 设置渲染属性
        self.CJW_setRenderSetting(renderUsing='mentalRay',type=0,imageFormatValue='iff')
        # 角色color层，输出素材命名及路径设置
        if layer == 'ChrColor':
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFilePrefix')
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>', type='string')
        # 选中的角色清理，组内角色不重复
        ChrModelGroupClears = []
        for selectObj in selectObjs:
            TheNameSpace = self.CJW_nameSpacTool(selectObj)
            chrMODEL = TheNameSpace+'MODEL'
            ChrMODEL = mc.ls(chrMODEL, l=1)[0]
            if mc.objExists(ChrMODEL) and ChrMODEL not in ChrModelGroupClears:
                ChrModelGroupClears.append(ChrMODEL)
        # 把清理的物体选择正确的MODEL组下的Shape节点
        # 注意导出的格式为 [['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]
        chrModelMeshs = self.TF_CleanNoIntermediateShapeNodes(ChrModelGroupClears)
        #  把[['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]转为['pSphereShape1', 'pSphereShape2', 'pSphereShape3']
        ChrModelMeshs = self.TF_switchGroup(chrModelMeshs)
        # 物体放入渲染层
        if layer == 'ChrColor' or layer == 'ChrAmb':
            mc.editRenderLayerMembers(renderlayer, ChrModelMeshs, noRecurse=0)
            for ChrModelMesh in ChrModelMeshs:
                if self.CJW_readTansformAttr(ChrModelMesh, 'wing'):
                    mc.editRenderLayerMembers(renderlayer, ChrModelMesh, noRecurse=0, remove=1)
        if layer == 'ChrWingAmb'or layer == 'ChrWingColor':
            for ChrModelMesh in ChrModelMeshs:
                if self.CJW_readTansformAttr(ChrModelMesh, 'wing'):
                    mc.editRenderLayerMembers(renderlayer, ChrModelMesh, noRecurse=0)
        # 添加renderPass
        if layer == 'ChrColor':
            # 添加refraction折射层
            # RenderPass = mc.shadingNode('renderPass', asRendering=1)
            # mel.eval('applyAttrPreset "renderPass1" "D:/Alias/Maya2014x64/presets/attrPresets/renderPass/refraction.mel" 1;')
            # refractionNamemc = mc.rename(RenderPass, 'refraction')
            # mc.connectAttr(renderlayer+'.renderPass','refraction.owner')
            # print (u'====【成功添加renderPass-refraction层】====')
            # 添加Specular反射层
            allRenderPass =  mc.ls(type='renderPass')
            if 'specular' not in allRenderPass:
                RenderPass = mc.shadingNode('renderPass', asRendering=1)
                mel.eval('applyAttrPreset "renderPass1" "D:/Alias/Maya2014x64/presets/attrPresets/renderPass/specular.mel" 1;')
                refractionNamemc = mc.rename(RenderPass, 'specular')
                mc.connectAttr(renderlayer+'.renderPass','specular.owner')
            else:
                # [u'specular.owner', u'ChrColor.renderPass']
                specularAttr = mc.listConnections('specular.owner',s=1,d=0,connections=1,plugs=1)
                if specularAttr:
                    mc.disconnectAttr(specularAttr[1],specularAttr[0])
                    mc.connectAttr(renderlayer+'.renderPass','specular.owner')
                else:
                    mc.connectAttr(renderlayer+'.renderPass','specular.owner')
            print (u'====【成功添加renderPass-specular层】====')
        # 参考角色灯光组
        self.TF_lightGroupImport(type=0,mode=1)
        # 开始添加灯光
        if layer == 'ChrColor' or layer == 'ChrWingColor':
            ChrLights = mc.ls('MSH_CHR_light_color', '*:MSH_CHR_light_color', '*:*:MSH_CHR_light_color')
            for ChrLight in ChrLights:
                ChrLightsShapes = mc.listRelatives(ChrLight, ad=1, f=1, ni=1, type='light')
                mc.editRenderLayerMembers(renderlayer, ChrLightsShapes, noRecurse=0)
        elif layer == 'ChrAmb' or layer == 'ChrWingAmb':
            ChrLights = mc.ls('MSH_CHR_light_amb', '*:MSH_CHR_light_amb', '*:*:MSH_CHR_light_amb')
            for ChrLight in ChrLights:
                ChrLightsShapes = mc.listRelatives(ChrLight, ad=1, f=1, ni=1, type='light')
                mc.editRenderLayerMembers(renderlayer, ChrLightsShapes, noRecurse=0)
        print (u'---角色%s层添加完成---'%layer)
    #------------------------------#
    # 【通用】【建立角色OCC渲染层】
    #  选中角色某物体，把角色整体MODEL组下Shape放入层里
    #------------------------------#
    def TF_RenderOCCLayer(self, layer='ChrOCC', transparency=0):
        selectObjs = mc.ls(sl=1, l=1)
        mc.select(cl=1)
        # 建立渲染层
        renderlayer = self.CJW_CreateRenderLayer(layer)
        # 设置渲染属性
        self.CJW_setRenderSetting(renderUsing='mentalRay',type=0,imageFormatValue='iff')
        # 选中的角色清理，组内角色不重复
        ChrModelGroupClears = []
        for selectObj in selectObjs:
            TheNameSpace = self.CJW_nameSpacTool(selectObj)
            chrMODEL = TheNameSpace+'MODEL'
            ChrMODEL = mc.ls(chrMODEL, l=1)[0]
            if mc.objExists(ChrMODEL) and ChrMODEL not in ChrModelGroupClears:
                ChrModelGroupClears.append(ChrMODEL)
        # 把清理的物体选择正确的MODEL组下的Shape节点
        # 注意导出的格式为 [['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]
        chrModelMeshs = self.TF_CleanNoIntermediateShapeNodes(ChrModelGroupClears)
        #  把[['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]转为['pSphereShape1', 'pSphereShape2', 'pSphereShape3']
        ChrModelMeshs = self.TF_switchGroup(chrModelMeshs)
        if layer == 'ChrOCC':
            mc.editRenderLayerMembers(renderlayer, ChrModelMeshs, noRecurse=0)
            for ChrModelMesh in ChrModelMeshs:
                if self.CJW_readTansformAttr(ChrModelMesh, 'wing') or (('c005001' in ChrModelMesh and self.CJW_readTansformAttr(ChrModelMesh, 'Tra')) or ('c011002' in ChrModelMesh and self.CJW_readTansformAttr(ChrModelMesh, 'Tra'))):
                    mc.editRenderLayerMembers(renderlayer, ChrModelMesh, noRecurse=0, remove=1)
        if layer == 'ChrWingOCC':
            for ChrModelMesh in ChrModelMeshs:
                if self.CJW_readTansformAttr(ChrModelMesh, 'wing'):
                    mc.editRenderLayerMembers(renderlayer, ChrModelMesh, noRecurse=0)
        # 开始生成OCC材质球
        materialsNodes =mc.ls(mat=1)
        shaderName = 'ChrOCC_shader'
        OCCTextureName = 'ChrOCC_texture'
        if shaderName not in materialsNodes:
            ChrOCCTexture = mc.shadingNode('mib_amb_occlusion', asTexture=1, name=OCCTextureName)
            mc.setAttr(ChrOCCTexture+'.samples', 128)
            mc.setAttr(ChrOCCTexture+'.spread', 1)
            mc.setAttr(ChrOCCTexture+'.max_distance', 3)
            mc.setAttr(ChrOCCTexture+'.output_mode', 0)
            mc.setAttr(ChrOCCTexture+'.falloff', 1)
            mc.setAttr(ChrOCCTexture+'.id_inclexcl', 0)
            ChrOCCShader = mc.shadingNode('surfaceShader', asShader=1, name=shaderName)
            mc.connectAttr((ChrOCCTexture + '.outValue'), (ChrOCCShader + '.outColor'), f=1)
            ChrOCCShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(ChrOCCShader+'SG'))
            mc.connectAttr((ChrOCCShader + '.outColor'), (ChrOCCShaderSG + '.surfaceShader'), f=1)
        else:
            ChrOCCShader = shaderName
            ChrOCCShaderSG = ChrOCCShader+'SG'
            ChrOCCTexture = OCCTextureName
        # 如果需要读取透明信息，写入字典
        if transparency == 1:
            transparencyInfoDict = self.TF_transparencyInfoDictInfo(ChrModelMeshs)
            # 选择的物体先赋一遍OCC材质
            for ChrModelMesh in ChrModelMeshs:
                mc.sets(ChrModelMesh, e=1, forceElement=ChrOCCShaderSG)
            # 如果为带透贴的，再继续加材质球。
            keys = transparencyInfoDict.keys()
            for i in range(len(keys)):
                ChrOCCShader = mc.shadingNode('surfaceShader', asShader=1, name=shaderName+'Tra')
                mc.connectAttr((ChrOCCTexture + '.outValue'), (ChrOCCShader + '.outColor'), f=1)
                ChrOCCShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(ChrOCCShader+'SG'))
                mc.connectAttr((ChrOCCShader + '.outColor'), (ChrOCCShaderSG + '.surfaceShader'), f=1)
                mc.connectAttr(keys[i], (ChrOCCShader + '.outTransparency'), f=1)
                mc.sets(transparencyInfoDict[keys[i]], e=1, forceElement=ChrOCCShaderSG)
        else:
            trueModelMeshs = mc.editRenderLayerMembers(renderlayer, q=1,fn=1)
            for trueModelMesh in trueModelMeshs:
                mc.sets(trueModelMesh, e=1, forceElement=ChrOCCShaderSG)

    #------------------------------#
    # 【通用】【建立角色Normal渲染层】
    #  选中角色某物体，把角色整体MODEL组下Shape放入层里
    #------------------------------#
    def TF_RenderNormalLayer(self, transparency=0):
        selectObjs = mc.ls(sl=1, l=1)
        mc.select(cl=1)
        # 建立渲染层
        renderlayer = self.CJW_CreateRenderLayer('ChrNormal')
        # 设置渲染属性
        self.CJW_setRenderSetting(renderUsing='mentalRay',type=0,imageFormatValue='iff')
        # 选中的角色清理，组内角色不重复
        ChrModelGroupClears = []
        for selectObj in selectObjs:
            TheNameSpace = self.CJW_nameSpacTool(selectObj)
            chrMODEL = TheNameSpace+'MODEL'
            ChrMODEL = mc.ls(chrMODEL, l=1)[0]
            if mc.objExists(ChrMODEL) and ChrMODEL not in ChrModelGroupClears:
                ChrModelGroupClears.append(ChrMODEL)
        # 把清理的物体选择正确的MODEL组下的Shape节点
        # 注意导出的格式为 [['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]
        chrModelMeshs = self.TF_CleanNoIntermediateShapeNodes(ChrModelGroupClears)
        #  把[['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]转为['pSphereShape1', 'pSphereShape2', 'pSphereShape3']
        ChrModelMeshs = self.TF_switchGroup(chrModelMeshs)
        mc.editRenderLayerMembers(renderlayer, ChrModelMeshs, noRecurse=0)
        for ChrModelMesh in ChrModelMeshs:
            if self.CJW_readTansformAttr(ChrModelMesh, 'wing') or (('c005001' in ChrModelMesh and self.CJW_readTansformAttr(ChrModelMesh, 'Tra')) or ('c011002' in ChrModelMesh and self.CJW_readTansformAttr(ChrModelMesh, 'Tra'))):
                mc.editRenderLayerMembers(renderlayer, ChrModelMesh, noRecurse=0, remove=1)
        # 开始生成Normal材质球
        materialsNodes =mc.ls(mat=1)
        shaderName = 'ChrNormal_shader'
        NormalTextureName = 'ChrNormal_texture'
        if shaderName not in materialsNodes:
            ChrNormalTexture = mc.shadingNode('mib_amb_occlusion', asTexture=1, name=NormalTextureName)
            mc.setAttr(ChrNormalTexture+'.samples', 128)
            mc.setAttr(ChrNormalTexture+'.spread', 0.8)
            mc.setAttr(ChrNormalTexture+'.max_distance', 3)
            mc.setAttr(ChrNormalTexture+'.output_mode', 3)
            ChrNormalShader = mc.shadingNode('surfaceShader', asShader=1, name=shaderName)
            mc.connectAttr((ChrNormalTexture + '.outValue'), (ChrNormalShader + '.outColor'), f=1)
            ChrNormalShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(ChrNormalShader+'SG'))
            mc.connectAttr((ChrNormalShader + '.outColor'), (ChrNormalShaderSG + '.surfaceShader'), f=1)
        else:
            ChrNormalShader = shaderName
            ChrNormalShaderSG = ChrNormalShader+'SG'
            ChrNormalTexture = 'ChrNormal_texture'
        # 赋材质
        # 如果需要读取透明信息，写入字典
        if transparency == 1:
            transparencyInfoDict = self.TF_transparencyInfoDictInfo(ChrModelMeshs)
            # 选择的物体先赋一遍Normal材质
            for ChrModelMesh in ChrModelMeshs:
                mc.sets(ChrModelMesh, e=1, forceElement=ChrNormalShaderSG)
            # 如果为带透贴的，再继续加材质球。
            keys = transparencyInfoDict.keys()
            for i in range(len(keys)):
                ChrNormalShader = mc.shadingNode('surfaceShader', asShader=1, name=shaderName+'Tra')
                mc.connectAttr((ChrNormalTexture + '.outValue'), (ChrNormalShader + '.outColor'), f=1)
                ChrNormalShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(ChrNormalShader+'SG'))
                mc.connectAttr((ChrNormalShader + '.outColor'), (ChrNormalShaderSG + '.surfaceShader'), f=1)
                mc.connectAttr(keys[i], (ChrNormalShader + '.outTransparency'), f=1)
                mc.sets(transparencyInfoDict[keys[i]], e=1, forceElement=ChrNormalShaderSG)
        else:
            for ChrModelMesh in ChrModelMeshs:
                mc.sets(ChrModelMesh, e=1, forceElement=ChrNormalShaderSG)

    #------------------------------#
    # 【通用】【建立角色Fresnel边缘光渲染层】
    #  选中角色某物体，把角色整体MODEL组下Shape放入层里
    #------------------------------#
    def TF_RenderFresnelLayer(self, transparency=0):
        selectObjs = mc.ls(sl=1, l=1)
        mc.select(cl=1)
        # 建立渲染层
        renderlayer = self.CJW_CreateRenderLayer('ChrFresnel')
        # 设置渲染属性
        self.CJW_setRenderSetting(renderUsing='mentalRay',type=0,imageFormatValue='iff')
        # 选中的角色清理，组内角色不重复
        ChrModelGroupClears = []
        for selectObj in selectObjs:
            TheNameSpace = self.CJW_nameSpacTool(selectObj)
            chrMODEL = TheNameSpace+'MODEL'
            ChrMODEL = mc.ls(chrMODEL, l=1)[0]
            if mc.objExists(ChrMODEL) and ChrMODEL not in ChrModelGroupClears:
                ChrModelGroupClears.append(ChrMODEL)
        # 把清理的物体选择正确的MODEL组下的Shape节点
        # 注意导出的格式为 [['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]
        chrModelMeshs = self.TF_CleanNoIntermediateShapeNodes(ChrModelGroupClears)
        #  把[['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]转为['pSphereShape1', 'pSphereShape2', 'pSphereShape3']
        ChrModelMeshs = self.TF_switchGroup(chrModelMeshs)
        mc.editRenderLayerMembers(renderlayer, ChrModelMeshs, noRecurse=0)
        for ChrModelMesh in ChrModelMeshs:
            if self.CJW_readTansformAttr(ChrModelMesh, 'wing') or (('c005001' in ChrModelMesh and self.CJW_readTansformAttr(ChrModelMesh, 'Tra')) or ('c011002' in ChrModelMesh and self.CJW_readTansformAttr(ChrModelMesh, 'Tra'))):
                mc.editRenderLayerMembers(renderlayer, ChrModelMesh, noRecurse=0, remove=1)
        # 开始生成Fresnel材质球
        materialsNodes =mc.ls(mat=1)
        shaderNode = 'ChrFresnel_shader'
        freRampNode = 'ChrFresnel_Ramp'
        freSamplerInfoNode = 'ChrFresnel_samplerInfo'
        if shaderNode not in materialsNodes:
            freSamplerInfo = mc.shadingNode('samplerInfo', asUtility=1, name=freSamplerInfoNode)
            fresnelRamp = mc.shadingNode('ramp', asTexture=1, name=freRampNode)
            mc.setAttr(fresnelRamp+'.colorEntryList[0].color', 1, 1, 1, type='double3')
            mc.setAttr(fresnelRamp+'.colorEntryList[2].color', 0, 0, 0, type='double3')
            mc.setAttr(fresnelRamp+'.colorEntryList[2].position', 1)
            mc.setAttr(fresnelRamp+'.colorEntryList[0].position', 0)
            mc.connectAttr((freSamplerInfo + '.facingRatio'), (fresnelRamp + '.uvCoord.uCoord'), f=1)
            mc.connectAttr((freSamplerInfo + '.facingRatio'), (fresnelRamp + '.uvCoord.vCoord'), f=1)
            fresnelShader = mc.shadingNode('lambert', asShader=1, name=shaderNode)
            mc.setAttr(fresnelShader+'.ambientColor', 1, 1, 1, type='double3')
            mc.setAttr(fresnelShader+'.diffuse', 0)
            mc.setAttr(fresnelShader+'.matteOpacityMode', 2)
            mc.setAttr(fresnelShader+'.matteOpacity', 0)
            mc.connectAttr((fresnelRamp + '.outColor'), (fresnelShader + '.color'), f=1)
            fresnelShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(fresnelShader+'SG'))
            mc.connectAttr((fresnelShader + '.outColor'), (fresnelShaderSG + '.surfaceShader'), f=1)
        else:
            fresnelShader = 'ChrFresnel_shader'
            fresnelShaderSG = fresnelShader + 'SG'
            fresnelRamp =  'ChrFresnel_Ramp'
        # 如果需要读取透明信息，写入字典
        if transparency == 1:
            transparencyInfoDict = self.TF_transparencyInfoDictInfo(selectObjs)
            # 选择的物体先赋一遍Fresnel材质
            for ChrModelMesh in ChrModelMeshs:
                mc.sets(ChrModelMesh, e=1, forceElement=fresnelShaderSG)
            # 如果为带透贴的，再继续加材质球。
            keys = transparencyInfoDict.keys()
            for i in range(len(keys)):
                fresnelShader = mc.shadingNode('lambert', asShader=1, name=shaderNode+'Tra')
                mc.setAttr(fresnelShader+'.ambientColor', 1, 1, 1, type='double3')
                mc.setAttr(fresnelShader+'.diffuse', 0)
                mc.setAttr(fresnelShader+'.matteOpacityMode', 2)
                mc.setAttr(fresnelShader+'.matteOpacity', 0)
                mc.connectAttr((fresnelRamp + '.outColor'), (fresnelShader + '.color'), f=1)
                fresnelShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(fresnelShader+'SG'))
                mc.connectAttr((fresnelShader + '.outColor'), (fresnelShaderSG + '.surfaceShader'), f=1)
                mc.connectAttr(keys[i], (fresnelShader + '.transparency'), f=1)
                mc.sets(transparencyInfoDict[keys[i]], e=1, forceElement=fresnelShaderSG)
        else:
            for ChrModelMesh in ChrModelMeshs:
                mc.sets(ChrModelMesh, e=1, forceElement=fresnelShaderSG)

    #------------------------------#
    # 【通用】【建立角色LGT渲染层】
    #  选中角色某物体，把角色整体MODEL组下Shape放入层里
    #------------------------------#
    def TF_RenderLGTLayer(self, transparency=0):
        selectObjs = mc.ls(sl=1, l=1)
        mc.select(cl=1)
        # 建立渲染层
        renderlayer = self.CJW_CreateRenderLayer('ChrLGT')
        # 设置渲染属性
        self.CJW_setRenderSetting(renderUsing='mentalRay',type=0,imageFormatValue='iff')
        # 选中的角色清理，组内角色不重复
        ChrModelGroupClears = []
        for selectObj in selectObjs:
            TheNameSpace = self.CJW_nameSpacTool(selectObj)
            chrMODEL = TheNameSpace+'MODEL'
            ChrMODEL = mc.ls(chrMODEL, l=1)[0]
            if mc.objExists(ChrMODEL) and ChrMODEL not in ChrModelGroupClears:
                ChrModelGroupClears.append(ChrMODEL)
        # 把清理的物体选择正确的MODEL组下的Shape节点
        # 注意导出的格式为 [['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]
        chrModelMeshs = self.TF_CleanNoIntermediateShapeNodes(ChrModelGroupClears)
        #  把[['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]转为['pSphereShape1', 'pSphereShape2', 'pSphereShape3']
        ChrModelMeshs = self.TF_switchGroup(chrModelMeshs)
        mc.editRenderLayerMembers(renderlayer, ChrModelMeshs, noRecurse=0)
        for ChrModelMesh in ChrModelMeshs:
            if self.CJW_readTansformAttr(ChrModelMesh, 'wing'):
                    mc.editRenderLayerMembers(renderlayer, ChrModelMesh, noRecurse=0, remove=1)
        # mel.eval('zwResetShadingEnginesN')
        # 开始生成LGT材质球
        materialsNodes =mc.ls(mat=1)
        shaderName = 'ChrLGT_shader'
        if shaderName not in materialsNodes:
            ChrLGTShader = mc.shadingNode('lambert', asShader=1, name=shaderName)
            mc.setAttr(ChrLGTShader+'.color', 1, 1, 1, type='double3')
            ChrLGTShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(ChrLGTShader+'SG'))
            mc.connectAttr((ChrLGTShader + '.outColor'), (ChrLGTShaderSG + '.surfaceShader'), f=1)
        else:
            shaderName = shaderName
            ChrLGTShaderSG = shaderName+'SG'
        # 赋材质
        # 如果需要读取透明信息，写入字典
        if transparency == 1:
            transparencyInfoDict = self.TF_transparencyInfoDictInfo(ChrModelMeshs)
            # 选择的物体先赋一遍Normal材质
            for ChrModelMesh in ChrModelMeshs:
                mc.sets(ChrModelMesh, e=1, forceElement=ChrLGTShaderSG)
            # 如果为带透贴的，再继续加材质球。
            keys = transparencyInfoDict.keys()
            for i in range(len(keys)):
                ChrLGTShader = mc.shadingNode('lambert', asShader=1, name=shaderName+'Tra')
                mc.setAttr(ChrLGTShader+'.color', 1, 1, 1, type='double3')
                ChrLGTShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(ChrLGTShader+'SG'))
                mc.connectAttr((ChrLGTShader + '.outColor'), (ChrLGTShaderSG + '.surfaceShader'), f=1)
                mc.connectAttr(keys[i], (ChrLGTShader + '.transparency'), f=1)
                mc.sets(transparencyInfoDict[keys[i]], e=1, forceElement=ChrLGTShaderSG)
        else:
            for ChrModelMesh in ChrModelMeshs:
                mc.sets(ChrModelMesh, e=1, forceElement=ChrLGTShaderSG)
        # 导入角色灯光组
        self.TF_lightGroupImport(type=0,mode=1)
        # 开始添加LGT灯光
        ChrLightShapes = mc.ls(type='light', l=1)
        for ChrLightShape in ChrLightShapes:
            if self.CJW_readTansformAttr(ChrLightShape, 'keylight_01'):
                mc.editRenderLayerMembers(renderlayer, ChrLightShape, noRecurse=0)
                mc.editRenderLayerAdjustment(ChrLightShape + '.color')
                mc.setAttr(ChrLightShape + '.color', 1, 0, 0, type='double3')
            if self.CJW_readTansformAttr(ChrLightShape, 'fillight_01'):
                mc.editRenderLayerMembers(renderlayer, ChrLightShape, noRecurse=0)
                mc.editRenderLayerAdjustment(ChrLightShape + '.color')
                mc.setAttr(ChrLightShape + '.color', 0, 1, 0, type='double3')
            if self.CJW_readTansformAttr(ChrLightShape, 'rimlight_01'):
                mc.editRenderLayerMembers(renderlayer, ChrLightShape, noRecurse=0)
                mc.editRenderLayerAdjustment(ChrLightShape + '.color')
                mc.setAttr(ChrLightShape + '.color', 0, 0, 1, type='double3')

    #------------------------------#
    # 【通用】【建立角色接触阴影层】
    #  选中角色某物体，把角色整体MODEL组下Shape放入层里
    #------------------------------#
    def TF_RenderConShadowLayer(self):
        selectObjs = mc.ls(sl=1, l=1)
        mc.select(cl=1)
        # 建立渲染层
        renderlayer = self.CJW_CreateRenderLayer('conSHD')
        # 设置渲染属性
        self.CJW_setRenderSetting(renderUsing='mentalRay',type=0,imageFormatValue='iff')
        # 选中的角色清理，组内角色不重复
        ChrModelGroupClears = []
        for selectObj in selectObjs:
            TheNameSpace = self.CJW_nameSpacTool(selectObj)
            chrMODEL = TheNameSpace+'MODEL'
            ChrMODEL = mc.ls(chrMODEL, l=1)[0]
            if mc.objExists(ChrMODEL) and ChrMODEL not in ChrModelGroupClears:
                ChrModelGroupClears.append(ChrMODEL)
        # 把清理的物体选择正确的MODEL组下的Shape节点
        # 注意导出的格式为 [['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]
        chrModelMeshs = self.TF_CleanNoIntermediateShapeNodes(ChrModelGroupClears)
        #  把[['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]转为['pSphereShape1', 'pSphereShape2', 'pSphereShape3']
        ModelMeshs = self.TF_switchGroup(chrModelMeshs)
        mc.editRenderLayerMembers(renderlayer, ModelMeshs, noRecurse=0)
        # 开始生成阴影材质球
        materialsNodes =mc.ls(mat=1)
        shaderNode = 'conShadow_shader'
        if shaderNode not in materialsNodes:
            shadowShader = mc.shadingNode('useBackground', asShader=1, name = shaderNode)
            mc.setAttr(shadowShader+'.specularColor', 0, 0, 0, type='double3')
            mc.setAttr(shadowShader+'.reflectivity', 0)
            mc.setAttr(shadowShader+'.reflectionLimit', 0)
            shadowShaderSG = mc.sets(renderable =1, noSurfaceShader =1, empty=1, name =(shadowShader+'SG'))
            mc.connectAttr((shadowShader +'.outColor'),(shadowShaderSG +'.surfaceShader'),f=1)
        else:
            shadowShader = shaderNode
            shadowShaderSG = shadowShader+'SG'
        # 赋材质
        for ModelMesh in ModelMeshs:
            mc.sets(ModelMesh, e=1, forceElement=shadowShaderSG)
        # 关闭角色道具shape节点的pSphereShape1.primaryVisibility渲染属性
        for ModelMesh in ModelMeshs:
            if ModelMesh.split('tf_')[1][0] == 'c' or ModelMesh.split('tf_')[1][0] == 'p':
                mc.setAttr(ModelMesh+'.primaryVisibility', 0)
            # 场景物体关闭投射属性 setAttr "pSphereShape1.castsShadows" 0;
            if ModelMesh.split('tf_')[1][0] == 'l':
                mc.setAttr(ModelMesh+'.castsShadows', 0)
        # sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
        # 添加场景主灯
        AllLights = mc.ls(type = 'light')
        for light in AllLights:
            if '*:Key_Light_Day' or 'Key_Light_Day':
                if '*:Key_Light_Day' in light or 'Key_Light_Day' in light:
                    mc.editRenderLayerMembers(renderlayer,light, noRecurse=0)
                    print (u'====成功添加阴影主灯====')
            else:
                print (u'====注意！！！无发现阴影层主灯====')

    #------------------------------#
    # 【通用】【建立角色接触OCC层】
    #  选中角色某物体，把角色整体MODEL组下Shape放入层里
    #------------------------------#
    def TF_RenderConOCCLayer(self):
        selectObjs = mc.ls(sl=1, l=1)
        mc.select(cl=1)
        # 建立渲染层
        renderlayer = self.CJW_CreateRenderLayer('conOCC')
        # 设置渲染属性
        self.CJW_setRenderSetting(renderUsing='mentalRay',type=0,imageFormatValue='iff')
        # 选中的角色清理，组内角色不重复
        ChrModelGroupClears = []
        for selectObj in selectObjs:
            TheNameSpace = self.CJW_nameSpacTool(selectObj)
            chrMODEL = TheNameSpace+'MODEL'
            ChrMODEL = mc.ls(chrMODEL, l=1)[0]
            if mc.objExists(ChrMODEL) and ChrMODEL not in ChrModelGroupClears:
                ChrModelGroupClears.append(ChrMODEL)
        # 把清理的物体选择正确的MODEL组下的Shape节点
        # 注意导出的格式为 [['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]
        chrModelMeshs = self.TF_CleanNoIntermediateShapeNodes(ChrModelGroupClears)
        #  把[['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]转为['pSphereShape1', 'pSphereShape2', 'pSphereShape3']
        ModelMeshs = self.TF_switchGroup(chrModelMeshs)
        mc.editRenderLayerMembers(renderlayer, ModelMeshs, noRecurse=0)
        # 开始生成接触OCC材质球
        materialsNodes =mc.ls(mat=1)
        shaderName = 'conOCC_shader'
        OCCTextureName = 'conOCC_texture'
        if (mc.pluginInfo('Mayatomr.mll',query=1,loaded=1) == False):
            mc.loadPlugin('Mayatomr.mll')
        if shaderName not in materialsNodes:
            OCCTexture = mc.shadingNode('mib_amb_occlusion',asTexture=1,name = OCCTextureName)
            mc.setAttr(OCCTexture+'.samples',136)
            mc.setAttr(OCCTexture+'.spread',0.8)
            mc.setAttr(OCCTexture+'.max_distance',2)
            mc.setAttr(OCCTexture+'.output_mode',0)
            mc.setAttr(OCCTexture+'.falloff',1)
            mc.setAttr(OCCTexture+'.id_inclexcl',0)
            mc.setAttr(OCCTexture+'.id_nonself',1)
            OCCShader = mc.shadingNode('surfaceShader',asShader=1,name = shaderName)
            mc.connectAttr((OCCTexture +'.outValue'),(OCCShader +'.outColor'),f=1)
            OCCShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(OCCShader+'SG'))
            mc.connectAttr((OCCShader +'.outColor'),(OCCShaderSG +'.surfaceShader'),f=1)
        else:
            OCCShader = shaderName
            OCCShaderSG = OCCShader+'SG'
            OCCTexture = OCCTextureName
        # 所有物体赋材质
        for ModelMesh in ModelMeshs:
            mc.sets(ModelMesh, e=1, forceElement=OCCShaderSG)
        # 关闭角色道具shape节点的pSphereShape1.primaryVisibility渲染属性
        for ModelMesh in ModelMeshs:
            if ModelMesh.split('tf_')[1][0] == 'c' or ModelMesh.split('tf_')[1][0] == 'p':
                mc.setAttr(ModelMesh+'.primaryVisibility', 0)
            # # 场景物体添加miLabel属性
            if ModelMesh.split('tf_')[1][0] == 'l':
                transform = mc.listRelatives(ModelMesh, p=1, f=1, type='transform')[0]
                if not mc.objExists(transform+'.miLabel'):
                    mc.addAttr(transform, shortName='miLabel',longName='miLabel',defaultValue=1.0, minValue=0.0, maxValue=1.0, attributeType='double',k=1)
        # sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)

    #------------------------------#
    # 【通用】【建立角色WingAlpha渲染层】
    #  选中角色某物体，把角色整体MODEL组下Shape放入层里
    #------------------------------#
    def TF_RenderWingAlphaLayer(self, transparency=1):
        selectObjs = mc.ls(sl=1, l=1)
        mc.select(cl=1)
        # 建立渲染层
        renderlayer = self.CJW_CreateRenderLayer('ChrWingAlpha')
        # 设置渲染属性
        self.CJW_setRenderSetting(renderUsing='mentalRay',type=0,imageFormatValue='iff')
        # 选中的角色清理，组内角色不重复
        ChrModelGroupClears = []
        for selectObj in selectObjs:
            TheNameSpace = self.CJW_nameSpacTool(selectObj)
            chrMODEL = TheNameSpace+'MODEL'
            ChrMODEL = mc.ls(chrMODEL, l=1)[0]
            if mc.objExists(ChrMODEL) and ChrMODEL not in ChrModelGroupClears:
                ChrModelGroupClears.append(ChrMODEL)
        # 把清理的物体选择正确的MODEL组下的Shape节点
        # 注意导出的格式为 [['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]
        chrModelMeshs = self.TF_CleanNoIntermediateShapeNodes(ChrModelGroupClears)
        #  把[['pSphereShape1'],['pSphereShape2'],['pSphereShape3']]转为['pSphereShape1', 'pSphereShape2', 'pSphereShape3']
        ChrModelMeshs = self.TF_switchGroup(chrModelMeshs)
        mc.editRenderLayerMembers(renderlayer, ChrModelMeshs, noRecurse=0)
        # 添加WingAlpha材质球
        materialsNodes =mc.ls(mat=1)
        MshaderName = 'ChrWingAlphaMatte_shader'
        WAshaderName = 'ChrWingAlpha_shader'
        if MshaderName not in materialsNodes:
            ChrWingAlphaMatteShader = mc.shadingNode('lambert', asShader=1, name=MshaderName)
            mc.setAttr(ChrWingAlphaMatteShader+'.color', 0, 0, 0, type='double3')
            mc.setAttr(ChrWingAlphaMatteShader+'.matteOpacityMode', 0)
            ChrWingAlphaMatteShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(ChrWingAlphaMatteShader+'SG'))
            mc.connectAttr((ChrWingAlphaMatteShader + '.outColor'), (ChrWingAlphaMatteShaderSG + '.surfaceShader'), f=1)
            ChrWingAlphaShader = mc.shadingNode('lambert', asShader=1, name=WAshaderName)
            mc.setAttr(ChrWingAlphaShader+'.color', 1, 0, 0, type='double3')
            mc.setAttr(ChrWingAlphaShader+'.ambientColor', 1, 0, 0, type='double3')
            ChrWingAlphaShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(ChrWingAlphaShader+'SG'))
            mc.connectAttr((ChrWingAlphaShader + '.outColor'), (ChrWingAlphaShaderSG + '.surfaceShader'), f=1)
        else:
            ChrWingAlphaMatteShader = MshaderName
            ChrWingAlphaMatteShaderSG = ChrWingAlphaMatteShader+'SG'
            ChrWingAlphaShader = WAshaderName
            ChrWingAlphaShaderSG = ChrWingAlphaShader+'SG'
        # 赋翅膀透明材质
        # 如果需要读取透明信息，写入字典
        for ChrModelMesh in ChrModelMeshs:
            if self.CJW_readTansformAttr(ChrModelMesh, 'wing'):
                if transparency == 1:
                    # 写入透明信息
                    TraToolInfo = self.TF_TransparencyShaderInfo(ChrModelMesh)
                    meshFaceInfos = TraToolInfo[0]
                    ObjTransparencyAttrs = TraToolInfo[1]
                    ObjShaderSGsCleans = TraToolInfo[2]
                    if ObjTransparencyAttrs:
                        ChrWingAlphaShader = mc.shadingNode('lambert', asShader=1, name=WAshaderName+'Tra')
                        mc.setAttr(ChrWingAlphaShader+'.color', 1, 0, 0, type='double3')
                        mc.setAttr(ChrWingAlphaShader+'.ambientColor', 1, 0, 0, type='double3')
                        ChrWingAlphaShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(ChrWingAlphaShader+'SG'))
                        mc.connectAttr((ChrWingAlphaShader + '.outColor'), (ChrWingAlphaShaderSG + '.surfaceShader'), f=1)
                        mc.connectAttr(ObjTransparencyAttrs[0], (ChrWingAlphaShader + '.transparency'), f=1)
                        mc.sets(ChrModelMesh, e=1, forceElement=ChrWingAlphaShaderSG)
                else:
                    mc.sets(ChrModelMesh, e=1, forceElement=ChrWingAlphaShaderSG)
            else:
                mc.sets(ChrModelMesh, e=1, forceElement=ChrWingAlphaMatteShaderSG)
        # 开始添加灯光
        ChrLights = mc.ls('MSH_CHR_light_amb', '*:MSH_CHR_light_amb', '*:*:MSH_CHR_light_amb')
        for ChrLight in ChrLights:
            ChrLightsShapes = mc.listRelatives(ChrLight, ad=1, f=1, ni=1, type='light')
            mc.editRenderLayerMembers(renderlayer, ChrLightsShapes, noRecurse=0)

    # ------------------------------#
    # 【导入角色灯】
    #  当文件内没有角色灯光组时，导入一个。
    # type=1时每次运行都添加参考，为0时，检测文件内，无灯光时才添加参考。
    # mode=1时参考后导入，mode=0时为参考，不导入。
    # ------------------------------#
    def TF_lightGroupImport(self, type=0,mode=1):
        # 角色灯路径
        ChrLightPath = 'Z:/Projects/ToothFairies/Reference/Product manager/Render/chLight/toothfairies_chLight.mb'
        if type == 1:
            mc.file(ChrLightPath, reference=1, type='mayaBinary', namespace='toothfairies_chLight')
            print (u'===成功导入角色灯光组===')
        if type == 0:
            ChrLights = mc.ls('light_ctrl_GRP', '*:light_ctrl_GRP', '*:*:light_ctrl_GRP')
            if ChrLights:
                if mode == 1:
                    try:
                        mc.file(ChrLightPath,importReference = 1, f = 1)
                    except:
                        pass
                else:
                    pass
            else:
                mc.file(ChrLightPath, reference=1, type='mayaBinary', namespace='toothfairies_chLight')
                print (u'===成功导入角色灯光组===')
                if mode == 1:
                    try:
                        mc.file(ChrLightPath,importReference = 1, f = 1)
                    except:
                        pass
                else:
                    pass

    # ------------------------------#
    # 【通用】【读模型属性】
    #  扫属性是扫Shape节点上的Transform节点的属性
    #  注意，输入的Obj需要是shape节点
    # ------------------------------#
    def CJW_readTansformAttr(self, shape, Attr='wing'):
        transform = mc.listRelatives(shape, p=1, f=1, type='transform')[0]
        if mc.objExists(transform+'.'+Attr):
            return True
        else:
            return False
    '''
    #resetShadingEngines重置SG节点
    '''
#导入参考
    def nj_RefIm(self):
        while mc.file(q=1,r=1):
          refPath=mc.file(q=1,r=1)
          if len(refPath)!=0:
              for r in refPath:
                  refRN=mc.file(r,q=1,rfn=1)
                  if(mc.file(r,q=1,dr=1)):
                      mc.file(refRN,loadReference=1)
                  mc.file(r,ir=1)
        return 0
    #-------------





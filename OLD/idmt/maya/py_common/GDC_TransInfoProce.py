# -*- coding: utf-8 -*-

'''
Created on 2016

GDC 透明信息处理（包括信息导出，信息检测）

适用于需要处理透明信息的项目

@author: hanhong

Data   : 2016_08_03
'''

# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
import os
import sys
import json
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
#----------------------------------------------------------------------------------------------------------#     
#【通用】相机序列拍屏工具（用于blocking文件连续拍屏）
#@author: hanhong
#Data：2015/11/16

#----------------------------------------------------------------------------------------------------------#    
class GDC_TransInfoProce(object):
    def __init__(self,pro='nj'):
        if pro=='nj':
            self.project='Ninjago'
        if pro=='tf':
            self.project='ToothFairies'
#----------------------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【有透明贴图连接的材质球信息】
    #  Author  : 韩虹
    #  Data    : 2016_08_04
    #------------------------------#
    def gdc_TrShadeInfo(self,returnMode = 0):
        SGS=mc.ls(type='shadingEngine',l=1)
        if not SGS:
            pass
        shadeTrs=[]
        shadetrerror=[]
        for sg in SGS:
            cons=mc.listConnections( (sg+'.surfaceShader'), d=False, s=True,c=False )
            if cons:
                shade=cons[0]
                if mc.objExists(shade+'.transparency'):
                    trs=mc.listConnections((shade+'.transparency'),d=0,s=1,p=1 )
                elif mc.objExists(shade+'.outTransparency'):
                    trs=mc.listConnections((shade+'.outTransparency'),d=0,s=1,p=1 )
                else:
                    pass
                if mc.ls(trs) and '.outTransparency' in trs[0] and trs[0] not in shadetrerror:
                    shadetrerror.append(shade)
                if mc.ls(trs) and mc.nodeType(trs[0])!='file' and trs[0] not in shadetrerror:
                    shadetrerror.append(shade)
                if trs and '.outColor' in trs[0] and mc.nodeType(trs[0])=='file' and trs[0] not in shadeTrs:
                    shadeTrs.append(shade)
        result=[shadeTrs,shadetrerror]
        if not returnMode:
            return result
        else:
            return shadeTrs
#----------------------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【检测文件中透明节点连接】
    #  Author  : 韩虹
    #  Data    : 2016_08_04
    #  透明节点需要由 黑白贴图由out color连接为正确
    #  如果由贴图通道 由outTransparency 连接，渲染时会出现各种问题，所以为错
    #
    #------------------------------#
    def gdc_TrShadeCheck(self):
        TrShadeInfo=self.gdc_TrShadeInfo()
        shadetrerror=TrShadeInfo[1]
        if shadetrerror:
            mc.select(shadetrerror)
            mc.warning(u'===========文件中有outTransparency连接透明节点的材质球，或者连接的节点为非file，请检查以下列出的材质球==========')
            for shade in shadetrerror:
                mc.warning(u'===========【%s】==========='%shade)
            mc.error(u'===========文件中有outTransparency连接透明节点的材质球，或者连接的节点为非file，请检查以上列出的材质球==========')
        else:
            print u'====================透明贴图检测通过===================='
        return 0
#----------------------------------------------------------------------------------------------------------#
     #------------------------------#
    # 【通用】【导出透明信息】
    #  Author  : shenkang
    #  from sk_infoConfig
    #------------------------------#

    def checkShotInfo(self):
        temp = (mc.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
        else:
            #mc.warning(unicode('========================【！！！文件名不规范！！！】========================', 'utf8'))
            mc.warning(u'========================【！！！文件名不规范！！！】========================')
        return info
#----------------------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【通用】【检测模型信息要是在MODEL组下的】
    #  Author  : 陈嘉伟
    #  Data    : 2016_08_25
    # ------------------------------#
    def gdc_CheckMeshInModel(self, meshs):
        InModelMeshs = []
        # 转长名
        meshs = mc.ls(meshs, l=1)
        for mesh in meshs:
            if '|MODEL|' in mesh and mesh not in InModelMeshs:
                InModelMeshs.append(mesh)
        return InModelMeshs

     #------------------------------#
    # 【通用】【透明贴图信息】
    #  Author  : shenkang
    #  from sk_infoConfig
    #------------------------------#
    def gdc_TrInfo(self):
        self.gdc_TrShadeCheck()
        TrShadeInfo=self.gdc_TrShadeInfo()
        shadetrerror=TrShadeInfo[1]
        shadeTrs=TrShadeInfo[0]
        ImageInfo=[]
        meshInfo=[]
        if shadeTrs:
            for shade in shadeTrs:
                trs=[]
                meshs=[]
                sg=mc.listConnections( (shade+'.outColor'),type='shadingEngine', d=1, s=0,c=0)
                if sg :
                    mesh=mc.sets(sg[0],q=True,no=1)
                    mesh=mc.ls(mesh, l = 1)
                    InModelMeshs = self.gdc_CheckMeshInModel(mesh)
                    if InModelMeshs:
                        meshs = InModelMeshs
                if mc.objExists(shade+'.transparency'):
                    trs=mc.listConnections((shade+'.transparency'),d=0,s=1,p=0 )
                elif mc.objExists(shade+'.outTransparency'):
                    trs=mc.listConnections((shade+'.outTransparency'),d=0,s=1,p=0)
                if trs:
                    filTr=trs[0]
                img=''
                if mc.objExists(filTr+'.fileTextureName') and mc.getAttr(filTr+'.fileTextureName'):
                    img=mc.getAttr(filTr+'.fileTextureName')
                    if img and img not in ImageInfo and meshs:
                        ImageInfo.append(img)
                        meshInfo.append(meshs)
        result=[ImageInfo,meshInfo]
        return result
    #------------------------------#
    # 【通用】【导出透明信息】
    #  Author  : 韩虹
    #  Data    : 2016_08_09
    #------------------------------#
    def gdc_TrInfoExr(self,update=1):
        shotInfo=self.checkShotInfo()
        path='D:/TempInfo/AssetInfo/transInfo/'
        serverPath='Z:/Projects/'+self.project+'/Project/data/AssetInfo/transInfo/'
        mc.sysFile(path,makeDir=True)
        fileName=shotInfo[1]+'.json'
        TrInfos=self.gdc_TrInfo()
        ImgInfo=TrInfos[0]
        MeshInfo=TrInfos[1]
        json_data = {}
        if ImgInfo:
            for i in range(len(ImgInfo)):
                img=ImgInfo[i]
                meshs=MeshInfo[i]
                json_data[img] = meshs
            with open((path+fileName), "w") as f:
                json.dump(json_data, f, indent = 4)
            if update==1:
                serverFilePath = serverPath + shotInfo[1] + '\\' + fileName
                updateCMD = 'zwSysFile "copy" ' + '"' + ((path+fileName).replace('\\', '/')) + '"' + ' ' + '"' + ((serverPath+fileName).replace('\\', '/')) + '"' + ' true'
                mel.eval(updateCMD)
                # 注册数据库
                projName = self.project
                userName = mel.eval('getenv \"USERNAME\"')
                info = projName + '|' + shotInfo[1] + '|' + userName
                mc.idmtService('transInfo', info)
            print  u'====================【%s】透明贴图信息已上传===================='%shotInfo[1]
        else:
            print u'====================文件中没有透明贴图，不输出透明贴图信息===================='
        return 0
    #------------------------------#
    # 【通用】【读取透明信息】
    #  Author  : 韩虹
    #  Data    : 2016_08_09
    #------------------------------#
    def gdc_TrInfoRead(self):
        path='Z:/Projects/'+self.project+'/Project/data/AssetInfo/transInfo/'
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refnamspace=refInfos[2][0]
        refNams=[]
        #refNams= [u'tf_p001001StaceysWand']
        trfils=[]
        #trfils= [u'Z:/Projects/ToothFairies/Project/data/AssetInfo/transInfo/p001001StaceysWand.json']
        if not refnamspace:
            mc.error(u'需要在参考状态下读取，文件中没有参考')
        for ns in refnamspace:
            if '_' in ns and len(ns.split('_'))>1:
                id=ns.split('_')[1]
                trfil=path+id+'.json'
                if os.path.isfile(trfil)==True:
                    refNams.append(ns)
                    trfils.append(trfil)
        imgInfos=[]
        #imgInfos= [u'//file-cluster/GDC/Projects/ToothFairies/Project/sourceimages/props/p001001StaceysWand/tf_p001001StaceysWand_sphere01_transp_4k.iff']
        MeshesInfos=[]
        #MeshesInfos [[u'|tf_p001001StaceysWandRNgroup|tf_p001001StaceysWand:MODEL|tf_p001001StaceysWand:MSH_all|tf_p001001StaceysWand:MSH_Magicwand_18_|tf_p001001StaceysWand:MSH_Magicwand_18_Shape']]
        if refNams:
            for i in range(len(refNams)):
                trf=trfils[i]
                data = {}
                with open((trf), "r") as f:
                    data = json.loads(f.read())
                for texture, objs in data.items():
                    if texture not in imgInfos:
                        imgInfos.append(texture)
                        needMeshes=[]
                        for obj in objs:
                            if '|' not in obj:
                                if mc.objExists(ns + ':' + obj):
                                    needMeshFull = mc.ls(( ns + ':' + obj),l = 1)[0]
                                    needMeshes.append(needMeshFull)
                            else:
                                # 全面启动长名
                                needMesh = obj.replace('|',('|' + ns + ':'))
                                if needMesh[0]=='|':
                                    needMe=''
                                    needN=needMesh.split('|')
                                    for i in (2,(len(needN)-1)):
                                        needMe=needN[i-1]+'|'+needN[i]
                                    needMesh=needMe
                                if not mc.ls('*' + needMesh):
                                    continue
                                needMeshFull = mc.ls(('*' + needMesh),l = 1)[0]
                                needMeshes.append(needMeshFull)
                    MeshesInfos.append(needMeshes)
        return [imgInfos, MeshesInfos]

    #------------------------------#
    # 【通用】【透明材质赋】
    #  Author  : 韩虹
    #  Data    : 2016_08_12
    #------------------------------#
    def GDC_ShaderAssign(meshs,shaderType='G',transparency=1):
        if transparency==0:
            Shade='SHD_'+shaderType
            SG=Shade+'SG'
            if mc.objExists(Shade)==0 and shaderType in ['R','G','B','M','A']:
                mc.shadingNode('surfaceShader', asShader=True,n=Shade)
            if mc.objExists(SG)==0:
                mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
            try:
                mc.connectAttr(('%s.outColor' % Shade),('%s.surfaceShader' % SG))
            except:
                pass
            if meshs:
                mc.sets(meshs,e=1, forceElement = SG)
            else:
                pass
            if shaderType=='R':
                mc.setAttr(Shade+'.outColor',1,0,0,type='double3')
                mc.setAttr(Shade+'.outMatteOpacity',0,0,0,type='double3')
            if shaderType=='G':
                mc.setAttr(Shade+'.outColor',0,1,0,type='double3')
                mc.setAttr(Shade+'.outMatteOpacity',0,0,0,type='double3')
            if shaderType=='B':
                mc.setAttr(Shade+'.outColor',0,0,1,type='double3')
                mc.setAttr(Shade+'.outMatteOpacity',0,0,0,type='double3')
            if shaderType=='M':
                mc.setAttr(Shade+'.outColor',0,0,0,type='double3')
                mc.setAttr(Shade+'.outMatteOpacity',0,0,0,type='double3')
            if shaderType=='A':
                mc.setAttr(Shade+'.outColor',0,0,0,type='double3')
                mc.setAttr(Shade+'.outMatteOpacity',1,1,1,type='double3')
        else:
            trInfos=self.gdc_TrInfoRead()
            imageInfos=trInfos[0]
            meshInfos=trInfos[1]

            meshsTr=[]
            meshNTr=[]
            shaderTr=[]
            for i in range(len(imageInfos)):
                meshTr=meshInfos[2]
                for mesh in meshTr:
                    if mesh in meshs  and mesh not in meshsTr:
                        meshsTr.append(mesh)
            if meshsTr:
                for mesh in meshs:
                    if mesh  not in meshsTr:
                        meshNTr.append(mesh)
            else:
               meshNTr=meshs
            if meshNTr:
                Shade='SHD_'+shaderType
                SG=Shade+'SG'
                if mc.objExists(Shade)==0 and shaderType in ['R','G','B','M','A']:
                    mc.shadingNode('surfaceShader', asShader=True,n=Shade)
                if mc.objExists(SG)==0:
                    mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
                try:
                    mc.connectAttr(('%s.outColor' % Shade),('%s.surfaceShader' % SG))
                except:
                    pass
                if meshs:
                    mc.sets(meshNTr,e=1, forceElement = SG)
                else:
                    pass
                if shaderType=='R':
                    mc.setAttr(Shade+'.outColor',1,0,0,type='double3')
                    mc.setAttr(Shade+'.outMatteOpacity',0,0,0,type='double3')
                if shaderType=='G':
                    mc.setAttr(Shade+'.outColor',0,1,0,type='double3')
                    mc.setAttr(Shade+'.outMatteOpacity',0,0,0,type='double3')
                if shaderType=='B':
                    mc.setAttr(Shade+'.outColor',0,0,1,type='double3')
                    mc.setAttr(Shade+'.outMatteOpacity',0,0,0,type='double3')
                if shaderType=='M':
                    mc.setAttr(Shade+'.outColor',0,0,0,type='double3')
                    mc.setAttr(Shade+'.outMatteOpacity',0,0,0,type='double3')
                if shaderType=='A':
                    mc.setAttr(Shade+'.outColor',0,0,0,type='double3')
                    mc.setAttr(Shade+'.outMatteOpacity',1,1,1,type='double3')
            if  meshsTr:
                print meshsTr
                for j in range(len(imageInfos)):
                    img=imageInfos[j]
                    exname=''
                    if '/' in img:
                        exname=img.split('/')[-1].split('.')[0]
                    else:
                        exname=img.split('.')[0]

                    Shade='SHD_'+shaderType+'_'+exname
                    SG=Shade+'SG'
                    fil='file_'+exname
                    if mc.objExists(Shade)==0 and shaderType in ['R','G','B','M','A']:
                        Shade=mc.shadingNode('surfaceShader', asShader=True,n=Shade)
                        fil=mc.shadingNode('file',asTexture=1, n=fil)
                        mc.setAttr((fil+'.fileTextureName'),img,type='string')
                        mc.connectAttr((fil+'.outColor '),(Shade+'.outTransparency'),f=1)
                        mc.connectAttr((fil+'.outColor '),(Shade+'.outMatteOpacity'),f=1)
                    if mc.objExists(SG)==0:
                        mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
                    try:
                        mc.connectAttr(('%s.outColor' % Shade),('%s.surfaceShader' % SG))
                    except:
                        pass
                    if meshInfos[j]:
                        for mesh in meshInfos[j]:
                            if mesh in meshsTr:
                                mc.sets(mesh,e=1, forceElement = SG)
                    else:
                        pass
                    if shaderType=='R':
                        mc.setAttr(Shade+'.outColor',1,0,0,type='double3')
                    if shaderType=='G':
                        mc.setAttr(Shade+'.outColor',0,1,0,type='double3')
                    if shaderType=='B':
                        mc.setAttr(Shade+'.outColor',0,0,1,type='double3')
                    if shaderType=='M':
                        mc.setAttr(Shade+'.outColor',0,0,0,type='double3')
                    if shaderType=='A':
                        mc.setAttr(Shade+'.outColor',0,0,0,type='double3')
        return 0

    #------------------------------#
    # 【TF项目】【参考状态只赋予透明材质】
    #  Author  : 陈嘉伟
    #  Data    : 2016_08_15
    #------------------------------#
    def TF_ShaderAssign(self):
        jsonInfos = self.gdc_TrInfoRead()
        #贴图路径
        imageInfos = jsonInfos[0]
        #模型shape节点带namespace全名称
        meshInfos = jsonInfos[1]
        for meshInfo in meshInfos:
            OneChrShapes = meshInfo

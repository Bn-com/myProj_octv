# -*- coding: utf-8 -*-

'''
Created on 2013-6-18

@author: 韩虹
'''
import maya.cmds as mc
import maya.mel as mel
import os
import re
import sys
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.setdefaultencoding('utf8')
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.py_common import GDC_Tools
reload(GDC_Tools)
class GA_PreCheck(object):
    def __init__(self):
        pass

    #-------------#
    # 【后台】清理anim文件
    #anim =0,不弹出动画提醒
    # 韩虹
    #-------------#
    def GA_MeshCheck(self,mod=1):
        MeshErrors=[]
        objs=mel.eval('polyCleanupArgList 3 { "1","2","1","0","1","0","0","0","0","1e-005","0","1e-005","0","1e-005","0","1","1" }')
        if objs and mod>0:
            for obj in objs:
                objL=mc.ls(obj,l=1)
                if objL and 'MODEL|' in objL[0] and objL[0] not in MeshErrors:
                    MeshErrors.append(objL[0])
        if objs and mod==0:
            MeshErrors=objs
        if MeshErrors:
            for mesherror in MeshErrors:
                print mesherror;
            mc.error(u'文件中有非法模型，请检查以上模型')
        else:
            mc.select(cl=1)
            print u'已检测模型非法点'
        return 0
    #-------------#
    # 【通用】【DIS 节点信息】【为ms_anim】
    #  韩虹
    #-------------#
    def GA_DisInfo(self):
        ShaderDisLists=[]
        DisLists=[]
        DisObjs=[]
        SGS=mc.ls(type='shadingEngine')
        if not SGS:
            mc.error(u'文件中没有SG节点，请检查')
        for SG in SGS:
            cons=mc.listConnections(SG+'.surfaceShader')
            DisShder=[]
            if cons and mc.objExists(cons[0]+'.kitty') and mc.listConnections(cons[0]+'.kitty'):
                DisShder=mc.listConnections(cons[0]+'.kitty')
            if DisShder and DisShder[0] not in ShaderDisLists:
                ShaderDisLists.append(DisShder[0])
        if ShaderDisLists:
            for i in range(len(ShaderDisLists)):
                if mc.objExists(ShaderDisLists[i]+'.hello'):
                    shader=mc.listConnections(ShaderDisLists[i]+'.hello')
                    if shader and mc.objExists(shader[0]+'.outColor') and mc.listConnections((shader[0]+'.outColor'),type='shadingEngine'):
                        SG=mc.listConnections((shader[0]+'.outColor'),type='shadingEngine')
                        meshs = mc.sets(SG,q=1)
                        if meshs and ShaderDisLists[i] not in  DisLists:
                            DisLists.append(ShaderDisLists[i])
                            DisObjs.append(meshs)
        result=[DisLists,DisObjs]
        return result
    #-------------#
    # 【通用】【刷新材质】【为ms_anim】
    #  韩虹
    #-------------#
    def GA_MSShaderAssign(self):
        disInfos=self.GA_DisInfo()
        DisShaders=disInfos[0]
        DisMeshs=disInfos[1]
        if DisShaders:
            for i in range(len(DisShaders)):
                shderN=DisShaders[i]+'_sn'
                SG=shderN+'SG'
                shader=mc.shadingNode('lambert',asShader=True,n=shderN)
                mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
                try:
                    mc.connectAttr(('%s.outColor' % shader),('%s.surfaceShader' % SG))
                except:
                    pass

                if not mc.objExists(shader+'.kitty'):
                    mc.addAttr(shader,ln = "kitty", at = 'long')
                try:
                    mc.connectAttr(('%s.hello' % DisShaders[i]),('%s.kitty' % shader))
                except:
                    pass
                matInfo = mc.listConnections(SG, d = True, s = False, type = 'materialInfo')
                try:
                    mc.connectAttr(DisShaders[i] + '.message', matInfo[0] + '.material',  f = True)
                except:
                    pass
                if DisMeshs[i]:
                    try:
                        mc.select(DisMeshs[i])
                        mc.sets(e=1, forceElement = SG)
                    except:
                        for shape in DisMeshs[i]:
                            cons=mc.listConnections(shape,type='shadingEngine')
                            if cons:
                                mc.delete(cons)
                        mc.select(DisMeshs[i])
                        mc.sets(e=1, forceElement = SG)
        return 0

    #-------------#
    # 【通用】【刷新材质】【为ms_anim】
    #  韩虹
    #-------------#
    def GA_MSShaderAssignDis(self):
        disInfos=self.GA_DisInfo()
        DisShaders=disInfos[0]
        DisMeshs=disInfos[1]
        if DisShaders:
            for i in range(len(DisShaders)):
                shderN=DisShaders[i]+'_sn'
                SG=DisShaders[i]+'SG'
                mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
                try:
                    mc.connectAttr(('%s.outColor' % DisShaders[i]),('%s.surfaceShader' % SG))
                except:
                    pass
                if DisMeshs[i]:
                    try:
                        mc.select(DisMeshs[i])
                        mc.sets(e=1, forceElement = SG)
                    except:
                        for shape in DisMeshs[i]:
                            cons=mc.listConnections(shape,type='shadingEngine')
                            if cons:
                                mc.delete(cons)
                        mc.sets(DisMeshs[i],e=1, forceElement = SG)
        return 0


    #-------------#
    # 【DDZ项目】【生成ms_anim】
    #  韩虹
    #-------------#
    def GA_MSFileExr(self,mstype='anim',checkIn=1,fileopen=1):
        userName = os.environ['USERNAME']
        # 项目名
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileType=info[-1].split('.')[-1]
        if fileType=='mb':
            fileTypeAll='mayaBinary'
        if fileType=='ma':
            fileTypeAll='mayaAscii'
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(info[0])

        pathLocal = sk_infoConfig.sk_infoConfig().checkTX2AnimRenderLocalPath()
        fileLocal = pathLocal + mc.file(sceneName=1, q=1).split('/')[-1]
        GDC_Tools.GDC_Tools().GA_unknownPluginsRemove()
        mc.file(rename=fileLocal)
        mc.file(save=1, force=1)
        # 仅允许tx阶段使用
        # 先输出smoothSet信息
        self.checkAssetSmoothSetUpdate()
        if info[1][0] in ['c','p'] and 'rg.mb' in info[-1] and mstype=='anim':
            filename=info[0]+'_'+info[1]+'_h_ms_anim.mb'
            #self.ArnoldShaderAssign(shaderType='Lambert',transparency=0)
            self.GA_MSShaderAssignDis()
            GrupInfo=self.GA_GroupsInfo()
            mc.select(GrupInfo[0])
            mc.select(GrupInfo[1],add=1,ne=1)
            mc.file((pathLocal+filename),options='v=0',f=1,type=fileTypeAll,es=1)
            mc.file((pathLocal+filename),options='v=0',type=fileTypeAll,f=1,o=1)
        if info[1][0] in ['c','p'] and 'rg.mb' in info[-1] and mstype=='render':
            filename=info[0]+'_'+info[1]+'_h_ms_render.mb'

            GrupInfo=self.GA_GroupsInfo()
            mc.select(GrupInfo[0])
            mc.select(GrupInfo[1],add=1,ne=1)
            mc.file((pathLocal+filename),options='v=0',f=1,type=fileTypeAll,es=1)
            mc.file((pathLocal+filename),options='v=0',type=fileTypeAll,f=1,o=1)
        if checkIn == 1:
            print(unicode('=====================[Check in] Start=====================', "utf8"))
            # 全部显示层显示
            layerInfos = mc.ls(type='displayLayer')
            for layer in layerInfos:
                a = layer.lower()
                if 'defaultlayer' not in a and u'norender' not in a:
                    mc.setAttr((layer + '.visibility'), 1)
            # checkOut
            newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            # print checkOutCmd
            mel.eval(checkOutCmd)
            # checkIn
            mel.eval('idmtProject -checkin -description \"Creted By RG File\"')
        if fileopen==1:
            mc.file((fileLocal),options='v=0',type=fileTypeAll,f=1,o=1)
    #-------------#
    # 【通用】【GRP 及SET信息】【用于导出文件】
    #  韩虹
    #
    #-------------#
    def GA_GroupsInfo(self):
        objs=mc.ls(tr=1,l=1)
        groupList=[]
        setList=[]
        for obj in objs:
            if '|' in obj  and len(obj.split('|'))<3 and obj not in groupList and obj not in ['|top','|front','|persp','|side']:
                groupList.append(obj)
        set=mc.listSets(allSets=1)
        if set:
           for se in set:
               if 'SMOOTH_SET' in se or 'RigSets' in se:
                    setList.append(se)
        result=[groupList,setList]
        return result

    # 【通用】【赋材质】
    #
    # 韩虹
    #-------------#
    def ArnoldShaderAssign(self,shaderType='Shadow',transparency=0):
        meshs=mc.ls(sl=1,l=1)
        if transparency==0:
            Shade='SHD_'+shaderType+'_arnold'
            SG=Shade+'SG'
            #删除已有材质球和SG节点
            if mc.objExists(Shade):
                mc.delete(Shade)
            if mc.objExists(SG):
                mc.delete(SG)
            #创建新材质球和SG节点
            if shaderType=='AO':
                mc.shadingNode('aiAmbientOcclusion', asShader=True,n=Shade)
            if shaderType=='Shadow':
                mc.shadingNode('aiShadowCatcher', asShader=True,n=Shade)
            if shaderType=='reflection':
                mc.shadingNode('aiStandard', asShader=True,n=Shade)
            else:
                mc.shadingNode('aiUtility', asShader=True,n=Shade)
            mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
            mc.connectAttr(('%s.outColor' % Shade),('%s.surfaceShader' % SG))
            if meshs:
                mc.sets(meshs,e=1, forceElement = SG)
            else:
                pass
            if shaderType=='Zdp':
                #节点
                setRange='csl_setRange_arnold'
                express='csl_expression_arnold'
                multiply='csl_multiplyDivide_arnold'
                samplerInfo='csl_samplerInfo_arnold'
                #创建节点
                if mc.objExists(setRange):
                    mc.delete(setRange)
                if mc.objExists(multiply):
                    mc.delete(multiply)
                if mc.objExists(samplerInfo):
                    mc.delete(samplerInfo)
                if mc.objExists(express):
                    mc.delete(express)
                #创建节点
                #mc.shadingNode('aiUtility', asShader=True,n=Shade)
                mc.shadingNode('setRange',asUtility=True,n=setRange)
                mc.shadingNode('multiplyDivide',asUtility=True,n=multiply)
                mc.shadingNode('samplerInfo',asUtility=True,n=samplerInfo)
                #添加shade节点
                mc.setAttr((Shade+'.shadeMode'),2)
                mc.addAttr(Shade,sn='black',longName='black',nn='Black',attributeType='double')
                mc.addAttr(Shade,sn='write',longName='write',nn='Write',attributeType='double')
                mc.addAttr(Shade,sn='farClipPlane',longName='farClipPlane',nn='Far Clip Plane',attributeType='double')
                mc.addAttr(Shade,sn='nearClipPlane',longName='nearClipPlane',nn='Near Clip Plane',attributeType='double')
                #shade参数设置
                mc.setAttr((Shade+'.shade_mode'),2)
                mc.setAttr((Shade+'.black'),1)
                mc.setAttr((Shade+'.write'),-1)
                mc.setAttr((Shade+'.farClipPlane'),800)
                mc.setAttr((Shade+'.nearClipPlane'),1)
                #range设置
                mc.setAttr((setRange+".ai_max"), 1,0,0)
                #multiply设置
                mc.setAttr((multiply+".i2"), -1,1,1)
                mc.setAttr((multiply+'.input2X'),-1)
                #express创建
                expCommon=setRange+'.oldMinX='+Shade+'.nearClipPlane;\n'+setRange+'.oldMaxX='+Shade+'.farClipPlane;'
                mc.expression (n=express,s=expCommon)
                #连接节点
                #setRange 与Shade连接
                mc.connectAttr((setRange+'.outValueX'),(Shade+'.colorR'),f=1)
                mc.connectAttr((setRange+'.outValueX'),(Shade+'.colorG'),f=1)
                mc.connectAttr((setRange+'.outValueX'),(Shade+'.colorB'),f=1)
                mc.connectAttr((Shade+'.write'),(setRange+'.maxX'),f=1)
                mc.connectAttr((Shade+'.black'),(setRange+'.minX'),f=1)
                #multiplyDivide 与multiply连接
                mc.connectAttr((multiply+'.outputX'),(setRange+'.valueX'),f=1)
                #samplerInfo与multiplyDivide连接
                mc.connectAttr((samplerInfo+'.pointCameraZ'),(multiply+'.input1X'),f=1)
    #AO材质
            if shaderType=='AO':
                mc.setAttr ((Shade+'.falloff'),0.05)
                mc.setAttr ((Shade+'.samples'),4)
    #反射材质
            if shaderType=='reflection':
                mc.setAttr ((Shade+'.Kd'),0)
                mc.setAttr ((Shade+'.Ks'),1)
                mc.setAttr ((Shade+'.Ks'),1)
                mc.setAttr ((Shade+'.specularRoughness'),1)
                mc.setAttr ((Shade+'.specularFresnel'),1)
                mc.setAttr ((Shade+'.Kr'),1)
                mc.setAttr ((Shade+'.Fresnel'),1)
                mc.setAttr ((Shade+'.Krn'),1)

    #Normal 材质
            if shaderType=='Normal':
                mc.setAttr ((Shade+'.shadeMode'),2)
                mc.setAttr ((Shade+'.colorMode'),3)
            if shaderType=='Fre':
                FNRamp = 'SHD_Fresnel_ramp_arnold'
                FNSample = 'SHD_Fresnel_Sample_arnold'
                if mc.ls( FNRamp ):
                    mc.delete(FNRamp)
                if mc.ls( FNSample ):
                    mc.delete(FNSample)
                mc.shadingNode ('ramp', asShader=True, name= FNRamp)
                mc.shadingNode ('samplerInfo', asShader=True, name= FNSample)
                mc.removeMultiInstance((FNRamp + '.colorEntryList[1]') , b = 1)
                mc.setAttr((Shade + '.shadeMode'),2)
                mc.setAttr((FNRamp + '.interpolation'),3)
                mc.setAttr((FNRamp + '.colorEntryList[2].position'),1)
                mc.setAttr((FNRamp + '.colorEntryList[0].position'),0)
                mc.setAttr((FNRamp + '.colorEntryList[2].color'),0,0,0,type = 'double3')
                mc.setAttr((FNRamp + '.colorEntryList[0].color'),1,1,1,type = 'double3')
                mc.connectAttr(('%s.%s') % (FNSample , 'facingRatio') , ('%s.%s') % (FNRamp , 'uCoord'), f=True)
                mc.connectAttr(('%s.%s') % (FNSample , 'facingRatio') , ('%s.%s') % (FNRamp , 'vCoord'), f=True)
                mc.connectAttr(('%s.%s') % (FNRamp , 'outColor') , ('%s.%s') % (Shade , 'color'), f=True)
    #Shadow材质
            if shaderType=='Shadow':
                mc.setAttr((Shade + '.backgroundColor'),0,0,0,type = 'double3')
                mc.setAttr((Shade + '.shadowColor'),1,1,1,type = 'double3')
                mc.setAttr((Shade + '.hardwareColor'),0,1,0,type = 'double3')
            if shaderType=='Lambert':
                mc.setAttr((Shade + '.shadeMode'),1)
                mc.setAttr((Shade + '.color'),1,1,1,type = 'double3')
    # ------------------------------#
    # 记录tx文件中的smoothSet  角色道具不允许重名，场景。。随遇而安
    # 沈康
    def checkAssetSmoothSetUpdate(self):
        # 本地路径
        localInfoPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(server=0,infoMode=3)
        mc.sysFile(localInfoPath, makeDir=1)
        serverInfoPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(server=1,infoMode=3)
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverInfoPath + '\",\"\",1)'
        mel.eval(makeDirCMD)
        # 记录信息
        smoothSetNode = 'smooth_0'
        smoothObjs_lv0 = []
        if mc.ls(smoothSetNode):
            smoothObjs_lv0 = mc.sets(smoothSetNode, q=1)
            if not smoothObjs_lv0:
                smoothObjs_lv0 = []
        smoothSetNode = 'smooth_1'
        smoothObjs_lv1 = []
        if mc.ls(smoothSetNode):
            smoothObjs_lv1 = mc.sets(smoothSetNode, q=1)
            if not smoothObjs_lv1:
                smoothObjs_lv1 = []
        smoothSetNode = 'smooth_2'
        smoothObjs_lv2 = []
        if mc.ls(smoothSetNode):
            smoothObjs_lv2 = mc.sets(smoothSetNode, q=1)
            if not smoothObjs_lv2 :
                smoothObjs_lv2 = []
        # 输出信息
        sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + 'smooth_0.txt'), smoothObjs_lv0)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'smooth_0.txt') + '"' + ' ' + '"' + (serverInfoPath + 'smooth_0.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + 'smooth_1.txt'), smoothObjs_lv1)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'smooth_1.txt') + '"' + ' ' + '"' + (serverInfoPath + 'smooth_1.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + 'smooth_2.txt'), smoothObjs_lv2)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'smooth_2.txt') + '"' + ' ' + '"' + (serverInfoPath + 'smooth_2.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
    # ------------------------------#
    # Asset 场景，自动命名灯光(选择），为自动分层作准备
    # 韩虹
    #2017.10.08
    def GA_PreLightRename(self,ren='RS',lightType='key',setype='chr'):
        objs=mc.ls(sl=1,tr=1,l=1)
        RSlighttypeList=[]
        if ren=='RS':
            RSlighttypeList=['RedshiftPhysicalLight','RedshiftIESLight','RedshiftPortalLight','RedshiftDomeLight']
        lightLists=[]
        if not objs:
            mc.error(u'no select,please select')
        for obj in objs:
            shape=mc.listRelatives(obj,s=1,f=1)
            if shape and mc.nodeType(shape[0]) in RSlighttypeList and obj not in lightLists:
                lightLists.append(obj)
        if not lightLists:
            mc.error(u'所选物体，没有RS灯光，请重新选择')
        lightTyps=['key','fill','rim','rs']
        lightName=['keylight','fillight','rimlight','rsDomeLight']
        ligN=''
        for j in range(len(lightTyps)):
            if lightType==lightTyps[j]:
                ligN=lightName[j]
        if ligN=='':
            mc.error(u'灯光类型出错，请检查')
        gro=setype+'_light'
        lightNewList=[]
        for i in range(len(lightLists)):
            lightShort=lightLists[i]
            if '|' in lightLists[i]:
                lightShort=lightLists[i].split('|')[-1]
            lightPath= lightLists[i].split(lightShort)[0]
            lig=''
            if i <9:
                lig=ligN+'_0'+str(i+1)
            else:
                lig=ligN+'_'+str(i+1)
            ligS=mc.rename(lightLists[i],lig)
            ligA=lightPath+ligS
            if mc.objExists(ligA) and ligA not in lightNewList:
                lightNewList.append(ligA)
        if lightNewList and not mc.objExists(gro):
            mc.group(lightNewList, n=gro)
            mc.parent(gro,'SET')
        elif lightNewList and mc.objExists(gro):
            mc.parent(lightNewList,gro)
        return 0
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【mesh tr 互】
    #  Author  : 韩虹
    #  Data    : 2017_09_19
    #------------------------------#
    def GA_TRMeshInfo(self,objs):
        meshList=[]
        for obj in objs:
            if mc.nodeType(obj)=='mesh' and mc.listRelatives(obj,p=1,f=1) and mc.listRelatives(obj,p=1,f=1)[0] not in meshList :
                meshs=mc.listRelatives(obj,p=1,type='transform',f=1)
                meshList.append(meshs[0])
            if mc.nodeType(obj)=='transform' and mc.listRelatives(obj,s=1,type='mesh'):
                meshs=mc.listRelatives(obj,s=1,type='mesh',f=1)
                for mesh in meshs:
                    if mesh not in meshList:
                        meshList.append(mesh)
        return meshList










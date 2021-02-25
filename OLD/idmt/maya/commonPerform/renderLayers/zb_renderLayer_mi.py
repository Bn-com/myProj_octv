# -*- coding: utf-8 -*-
# 【通用】【mi项目工具】
#  Author : 沈康
#  Data   : 2016

#-----------------------------------------#
# idp 分 角色/道具/场景 和 asset自身的idp
#-------角色/道具/场景的需要额外处理
# 如 aovCPRGBCreate()
#-------asset自身的idp
# set组明名: namespace:aiMSK_idpName_TypeRGB
# 如:mi_c002002Teethless_h:aiMSK_TL_CHRR


import maya.cmds as mc
import maya.mel as mel
from pymel.core import *
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class zb_renderLayer_mi(object):
    def __init__(self):
        self.sylvainPath = 'Z:/Projects/MiniTiger/MiniTiger_Scratch/Td/renderLayerTools'

    def commonSettings(self):
        if not mc.pluginInfo('mtoa.mll',q=1,loaded = 1):
            mc.loadPlugin('mtoa.mll')
        import mtoa
        mtoa.core.createOptions()
        import mtoa.cmds.registerArnoldRenderer
        mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
        # 标准设置
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        mc.setAttr('defaultArnoldDriver.halfPrecision', 0)
        '''
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<Layer>/<Scene>_<Layer>', type='string')
        mc.setAttr('defaultResolution.deviceAspectRatio', 2.387)
        mc.setAttr('defaultResolution.pixelAspect', 1.00)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        mc.setAttr('defaultResolution.dotsPerInch', 72)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        '''
        # 开始处理
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()
        anim = idmt.pipeline.db.GetAnimByFilename(shotID)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        fpsFrame = anim.fps
        resW = anim.resolutionW
        resH = anim.resolutionH
        # res
        mc.setAttr('defaultResolution.width', resW)
        mc.setAttr('defaultResolution.height', resH)
        # FPS
        if fpsFrame == 25:
            mc.currentUnit(time='pal')
        if fpsFrame == 24:
            mc.currentUnit(time='film')
        if fpsFrame == 30:
            mc.currentUnit(time='ntsc')
        # frame
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

        # 格式命名
        # 原先调用菜单，现在直接改节点
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
        mc.setAttr('defaultRenderGlobals.periodInExt', 1)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
            mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

        # arnold配置
        mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 0)

        # aov error
        refNodes = mc.ls(type = 'reference')
        aiErrorState = 1
        for checkRef in refNodes:
            if 'MiniTiger' in checkRef and 'c001' in checkRef:
                aiErrorState = 0
        if not aiErrorState:
            mc.setAttr('defaultArnoldRenderOptions.abortOnError',0)

    #----------------------------------------------------#
    # aov_chrproprgb 角色道具aov
    def aovCPRGBCreate(self):
        refNodes = mc.ls(type ='reference')
        chrNsList = []
        prpNsList = []
        for checkRef in refNodes:
            if '_UNKNOWN_REF_NODE_' in checkRef:
                continue
            if 'CAM' in checkRef:
                continue
            try:
                checkNs = mc.referenceQuery(checkRef,namespace=1).split(':')[-1]
                if '_' not in checkNs:
                    continue
                assetType = self.getAssetType(checkNs)
                if assetType in ['c']:
                    chrNsList.append(checkNs)
                if assetType in ['p']:
                    prpNsList.append(checkNs)
            except:
                pass
        chrGrps = []
        prpGrps = []
        # chr
        for checkNs in chrNsList:
            meshes = mc.ls('%s:*'%checkNs,type = 'mesh',l=1)
            if not meshes:
                continue
            grps = mc.listRelatives(meshes,p=1,type = 'transform',f=1)
            if not grps:
                grps = []
            chrGrps = chrGrps + grps
        # prp
        for checkNs in prpNsList:
            meshes = mc.ls('%s:*'%checkNs,type = 'mesh',l=1)
            if not meshes:
                continue
            grps = mc.listRelatives(meshes,p=1,type = 'transform',f=1)
            if not grps:
                grps = []
            prpGrps = prpGrps + grps

        rgbList = self.aovCreateRGBNodes()

        self.aovRGBCreatCore([chrGrps,prpGrps,[]],rgbList,'chrprp',aiSetMode = 0)

    # chr asset aov
    def aovMiTlCreate(self):
        refNodes = mc.ls(type ='reference')
        # mini/t/xx
        MiTl_RList = []
        MiTl_GList = []
        MiTl_BList = []
        # Robot/Mushroom/StoryKing
        RMS_RList = []
        RMS_GList = []
        RMS_BList = []
        # Alpaca/AlpacaB/Geezer
        AAG_RList = []
        AAG_GList = []
        AAG_BList = []
        # Penguin/Artillery/Boxer
        PAB_RList = []
        PAB_GList = []
        PAB_BList = []
        for checkRef in refNodes:
            if '_UNKNOWN_REF_NODE_' in checkRef:
                continue
            if 'CAM' in checkRef:
                continue
            try:
                checkNs = mc.referenceQuery(checkRef,namespace=1).split(':')[-1]
                if '_' not in checkNs:
                    continue
                assetID = checkNs.split('_')[1].lower()
                idKey = assetID[:4]
                if idKey in ['c001']:
                    MiTl_RList.append(checkNs)
                if idKey in ['c002']:
                    MiTl_GList.append(checkNs)
                if idKey in ['c005','c006']:
                    MiTl_BList.append(checkNs)
                # RMS
                if idKey in ['c009']:
                    RMS_RList.append(checkNs)
                if idKey in ['c003','c004','c042']:
                    RMS_GList.append(checkNs)
                if idKey in ['c022']:
                    RMS_BList.append(checkNs)
                # AAG
                if 'c014001' in assetID:
                    AAG_RList.append(checkNs)
                if 'c014002' in assetID:
                    AAG_GList.append(checkNs)
                if idKey in ['c043']:
                    AAG_BList.append(checkNs)
                # PAB
                if idKey in ['c015','c050']:
                    PAB_RList.append(checkNs)
                if idKey in ['c031']:
                    PAB_GList.append(checkNs)
                if idKey in ['c010']:
                    PAB_BList.append(checkNs)
            except:
                pass

        rgbList = self.aovCreateRGBNodes()

        if MiTl_RList or MiTl_GList or MiTl_BList:
            RGrps = self.getObjsFromNs(MiTl_RList)
            GGrps = self.getObjsFromNs(MiTl_GList)
            BGrps = self.getObjsFromNs(MiTl_BList)
            self.aovRGBCreatCore([RGrps,GGrps,BGrps],rgbList,'chrMiTl',aiSetMode = 0)

        if RMS_RList or RMS_GList or RMS_BList:
            RGrps = self.getObjsFromNs(RMS_RList)
            GGrps = self.getObjsFromNs(RMS_GList)
            BGrps = self.getObjsFromNs(RMS_BList)
            self.aovRGBCreatCore([RGrps,GGrps,BGrps],rgbList,'chrRMS',aiSetMode = 0)

        if AAG_RList or AAG_GList or AAG_BList:
            RGrps = self.getObjsFromNs(AAG_RList)
            GGrps = self.getObjsFromNs(AAG_GList)
            BGrps = self.getObjsFromNs(AAG_BList)
            self.aovRGBCreatCore([RGrps,GGrps,BGrps],rgbList,'chrAAG',aiSetMode = 0)

        if PAB_RList or PAB_GList or PAB_BList:
            RGrps = self.getObjsFromNs(PAB_RList)
            GGrps = self.getObjsFromNs(PAB_GList)
            BGrps = self.getObjsFromNs(PAB_BList)
            self.aovRGBCreatCore([RGrps,GGrps,BGrps],rgbList,'chrPAB',aiSetMode = 0)

    # 从ns获取物体
    def getObjsFromNs(self,nsList):
        needGrps = []
        for checkNs in nsList:
            meshes = mc.ls('%s:*'%checkNs,type = 'mesh',l=1)
            if not meshes:
                continue
            grps = mc.listRelatives(meshes,p=1,type = 'transform',f=1)
            if not grps:
                grps = []
            needGrps += grps
        return needGrps

    def getAssetType(self,ns):
        assetType = ''
        assetID = ns.split('_')[1]
        if assetID[0] in ['c','C']:
            assetType = 'c'
        if assetID[0] in ['p','P']:
            assetType = 'p'
        if assetID[0] in ['s','S']:
            assetType = 's'
        if assetID[:7] in ['p024002']:
            assetType = 's'
        return assetType

    #----------------------------------------------------#
    # aov_rgb创建 'c' chr prp | 's' set
    #----------------------------------------------------#
    # set组明名: namespace:aiMSK_idpName_typeColor 如:mk_cBlueMonkey_h:aiMSK_Monkey_chrR
    def aovRGBCreate(self,setType):
        # 按RGB三个顺序去定位
        needSetList = self.aovRGBGetSetList(setType)

        rgbList = self.aovCreateRGBNodes()

        layerInfos = needSetList.keys()
        for layerInfo in layerInfos:
            self.aovRGBCreatCore(needSetList[layerInfo],rgbList,layerInfo,aiSetMode = 1  )

    def aovCreateRGBNodes(self):
        # rebuild rgb
        RColor = 'R_aiColor_mi'
        GColor = 'G_aiColor_mi'
        BColor = 'B_aiColor_mi'
        RColorTR = 'R_aiColor_TR_mi'
        GColorTR = 'G_aiColor_TR_mi'
        BColorTR = 'B_aiColor_TR_mi'

        if not mc.ls(RColor):
            mc.shadingNode('aiUserDataColor', asShader=1,name = RColor)
            #mc.shadingNode('aiStandard', asShader=1,name = RColor)
        if not mc.ls(GColor):
            mc.shadingNode('aiUserDataColor', asShader=1,name = GColor)
            #mc.shadingNode('aiStandard', asShader=1,name = GColor)
        if not mc.ls(BColor):
            mc.shadingNode('aiUserDataColor', asShader=1,name = BColor)
            #mc.shadingNode('aiStandard', asShader=1,name = BColor)
        if not mc.ls(RColorTR):
            mc.shadingNode('aiStandard', asShader=1,name = RColorTR)
        if not mc.ls(GColorTR):
            mc.shadingNode('aiStandard', asShader=1,name = GColorTR)
        if not mc.ls(BColorTR):
            mc.shadingNode('aiStandard', asShader=1,name = BColorTR)

        mc.setAttr(RColor+'.defaultValue',1,0,0,typ='double3')
        mc.setAttr(GColor+'.defaultValue',0,1,0,typ='double3')
        mc.setAttr(BColor+'.defaultValue',0,0,1,typ='double3')
        #mc.setAttr(RColor+'.color',1,0,0,typ='double3')
        #mc.setAttr(GColor+'.color',0,1,0,typ='double3')
        #mc.setAttr(BColor+'.color',0,0,1,typ='double3')
        mc.setAttr(RColorTR+'.color',1,0,0,typ='double3')
        mc.setAttr(RColorTR+'.emissionColor',1,0,0,typ='double3')
        mc.setAttr(RColorTR+'.Kd',1)
        mc.setAttr(RColorTR+'.Kt',1)
        mc.setAttr(RColorTR+'.emission',1)
        mc.setAttr(GColorTR+'.color',0,1,0,typ='double3')
        mc.setAttr(GColorTR+'.emissionColor',0,1,0,typ='double3')
        mc.setAttr(GColorTR+'.Kd',1)
        mc.setAttr(GColorTR+'.Kt',1)
        mc.setAttr(GColorTR+'.emission',1)
        mc.setAttr(BColorTR+'.color',0,0,1,typ='double3')
        mc.setAttr(BColorTR+'.emissionColor',0,0,1,typ='double3')
        mc.setAttr(BColorTR+'.Kd',1)
        mc.setAttr(BColorTR+'.Kt',1)
        mc.setAttr(BColorTR+'.emission',1)

        return [RColor,GColor,BColor,RColorTR,GColorTR,BColorTR]

    #----------------------------------------------------#
    # 获取rgbList setType 'c' chr prp | 's' set
    def aovRGBGetSetList(self,setType):
        allSetList = mc.ls('*:aiMSK_*',type = 'objectSet')
        aiSetList = {}
        assetDict = {}
        # 加载
        for checkSet in allSetList:
            setTypeKey = checkSet.split('_')[-1][:-1]
            needState = 0
            if setType in ['c','C'] and setTypeKey.lower() in ['chr']:
                needState = 1
            if setType in ['p','P'] and setTypeKey.lower() in ['prp']:
                needState = 1
            if setType in ['s','S'] and setTypeKey.lower() in ['set']:
                needState = 1
            if not needState:
                continue
            aovKey = checkSet.split(':')[-1].split('_')[1]
            ns = checkSet.split(':')[0]
            assetID = ns.split('_')[1]
            key = '%s_%s'%(aovKey,ns)
            assetID_key = '%s_%s'%(aovKey,assetID)
            assetKeys = assetDict.keys()
            if aovKey not in assetKeys:
                assetDict[aovKey] = [[assetID_key,key]]
            else:
                if [assetID_key,key] not in assetDict[aovKey]:
                    assetDict[aovKey].append([assetID_key,key])
            checkKeys = aiSetList.keys()
            if key not in checkKeys:
                aiSetList[key] = [checkSet]
            else:
                aiSetList[key].append(checkSet)
        # 修正重复
        fixedDict = {}
        for aovKey in assetDict.keys():
            if len(assetDict[aovKey]) == 1:
                fixedDict[aovKey] =  aiSetList[assetDict[aovKey][0][-1]]
            else:
                for num in range(len(assetDict[aovKey])):
                    if num == 0:
                        fixedDict[aovKey] =  aiSetList[assetDict[aovKey][0][-1]]
                    else:
                        fixedDict['%s%s'%(aovKey,str(num))] =  aiSetList[assetDict[aovKey][num][-1]]
        aiSetList = fixedDict
        # 排序
        checkSetKeys = aiSetList.keys()
        for checkKey in checkSetKeys:
            if not aiSetList[checkKey]:
                continue
            setName = aiSetList[checkKey][0]
            nsType = setName.split('_')[1][0].lower()
            setList = aiSetList[checkKey]
            tempList = ['','','',nsType]
            for checkSet in setList:
                if checkSet[-1] in ['R']:
                    tempList[0] = checkSet
                if checkSet[-1] in ['G']:
                    tempList[1] = checkSet
                if checkSet[-1] in ['B']:
                    tempList[2] = checkSet
            aiSetList[checkKey] = tempList

        return aiSetList

    '''
    # no transparency type
    #----------------------------------------------------#
    # aiSetList 最多3个元素一套
    # aiColors  [RColor,GColor,BColor]
    # aiSetMode 为1时，aiSetList为三个set的名字的list ; 为0时,aiSetList为三个objlist的list
    def aovRGBCreatCore(self,aiSetList,aiColors,layerInfo,aiSetMode = 1):
        aiMasksSets = aiSetList[:3]

        if not mc.objExists('defaultArnoldDriver'):
            import mtoa.core as core
            core.createOptions()

        # start
        for aiSetNum in xrange(0, len(aiMasksSets), 3):
            #customAOV = 'msk_Mask_%s'%(str(aovListSize+1))
            aovName = layerInfo
            print '-------'
            print aovName
            customAOV = 'msk_%s'%(aovName)
            if mc.ls(customAOV):
                mc.delete(customAOV)

            tSwitch = 'RGB_Switch_%s'%customAOV
            if mc.ls(tSwitch):
                mc.delete(tSwitch)
            tSwitch = mc.shadingNode('tripleShadingSwitch',au=1,name = tSwitch)
            mc.setAttr(tSwitch+'.default',0,0,0,typ='double3')

            aiUshader = 'RGB_aiUtility_%s'%customAOV
            if mc.ls(aiUshader):
                mc.delete(aiUshader)
            aiUshader = mc.shadingNode('aiUtility', asShader=1,name = aiUshader)
            mc.setAttr(aiUshader+'.shadeMode',2)

            mc.connectAttr(tSwitch+'.output', aiUshader+'.color',f=1)

            for num, setName in enumerate( aiMasksSets[aiSetNum:aiSetNum+3] ):
                if not mc.ls(setName):
                    continue
                aiColor = aiColors[num % len(aiColors)]
                if aiSetMode:
                    checkObjs = mc.sets(setName,q=1)
                else:
                    checkObjs = setName
                if not checkObjs:
                    continue
                for obj in checkObjs:
                    shape = mc.listRelatives(obj,s=1,type = 'mesh',ni=1)
                    if not shape:
                        continue
                    shape = shape[0]
                    inpt = mc.getAttr(tSwitch+'.input',s=1)
                    mc.connectAttr(shape+'.instObjGroups[0]',tSwitch+'.input['+str(inpt)+'].inShape',f=1)
                    mc.connectAttr(aiColor+'.outColor',tSwitch+'.input['+str(inpt)+'].inTriple',f=1)

            # AOV'S
            aovListSize = mc.getAttr('defaultArnoldRenderOptions.aovList',s=1)
            for checkNum in range(aovListSize):
                cons = mc.listConnections('defaultArnoldRenderOptions.aovList[%s]'%str(checkNum),s=1,d=0)
                if not cons:
                    aovListSize = checkNum
                    break

            customAOV = mc.createNode('aiAOV',n=customAOV, skipSelect=True)
            mc.setAttr(customAOV+'.name',customAOV,type='string')
            mc.connectAttr(customAOV+'.message','defaultArnoldRenderOptions.aovList['+ str(aovListSize)+']',f=1)

            mc.connectAttr('defaultArnoldDriver.message',customAOV+'.outputs[0].driver', f=1)
            mc.connectAttr('defaultArnoldFilter.message',customAOV+'.outputs[0].filter', f=1)

            # connect to default shader
            mc.connectAttr(aiUshader+'.outColor',customAOV+'.defaultValue',f=1)
    '''

    #----------------------------------------------------#
    # Transparency Type
    # aiSetList 最多3个元素一套
    # aiColors  [RColor,GColor,BColor]
    # aiSetMode 为1时，aiSetList为三个set的名字的list ; 为0时,aiSetList为三个objlist的list
    def aovRGBCreatCore(self,aiSetList,aiColors,layerInfo,aiSetMode = 1):
        cycleNum = 3

        aiMasksSets = aiSetList[:cycleNum]

        if not mc.objExists('defaultArnoldDriver'):
            import mtoa.core as core
            core.createOptions()

        # start
        for aiSetNum in xrange(0, len(aiMasksSets), cycleNum):
            #customAOV = 'msk_Mask_%s'%(str(aovListSize+1))
            aovName = layerInfo
            print '-------'
            print aovName
            customAOV = 'msk_%s'%(aovName)
            if mc.ls(customAOV):
                mc.delete(customAOV)

            tSwitch = 'RGB_Switch_%s'%customAOV
            if mc.ls(tSwitch):
                mc.delete(tSwitch)
            tSwitch = mc.shadingNode('tripleShadingSwitch',au=1,name = tSwitch)
            mc.setAttr(tSwitch+'.default',0,0,0,typ='double3')

            aiUshader = 'RGB_aiUtility_%s'%customAOV
            if mc.ls(aiUshader):
                mc.delete(aiUshader)
            aiUshader = mc.shadingNode('aiUtility', asShader=1,name = aiUshader)
            mc.setAttr(aiUshader+'.shadeMode',2)

            mc.connectAttr(tSwitch+'.output', aiUshader+'.color',f=1)

            for num, setName in enumerate( aiMasksSets[aiSetNum:aiSetNum+cycleNum] ):
                if not mc.ls(setName):
                    continue
                aiColor = aiColors[num % cycleNum]
                if aiSetMode:
                    checkObjs = mc.sets(setName,q=1)
                else:
                    checkObjs = setName
                if not checkObjs:
                    continue
                for obj in checkObjs:
                    checkType = mc.nodeType(obj)
                    if checkType in ['mesh']:
                        obj = mc.listRelatives(obj,p=1,type='transform',f=1)[0]
                    shape = mc.listRelatives(obj,s=1,type = 'mesh',ni=1,f=1)
                    if not shape:
                        continue
                    shape = shape[0]
                    inpt = mc.getAttr(tSwitch+'.input',s=1)
                    mc.connectAttr(shape+'.instObjGroups[0]',tSwitch+'.input['+str(inpt)+'].inShape',f=1)

                    noTrState = mc.getAttr(shape+'.aiOpaque')
                    #if noTrState:
                    mc.connectAttr(aiColor+'.outColor',tSwitch+'.input['+str(inpt)+'].inTriple',f=1)
                    #else:
                    #    mc.connectAttr(aiColors[num % cycleNum + cycleNum]+'.outColor',tSwitch+'.input['+str(inpt)+'].inTriple',f=1)
            # AOV'S
            aovListSize = mc.getAttr('defaultArnoldRenderOptions.aovList',s=1)
            for checkNum in range(aovListSize):
                cons = mc.listConnections('defaultArnoldRenderOptions.aovList[%s]'%str(checkNum),s=1,d=0)
                if not cons:
                    aovListSize = checkNum
                    break

            customAOV = mc.createNode('aiAOV',n=customAOV, skipSelect=True)
            mc.setAttr(customAOV+'.name',customAOV,type='string')
            mc.connectAttr(customAOV+'.message','defaultArnoldRenderOptions.aovList['+ str(aovListSize)+']',f=1)

            mc.connectAttr('defaultArnoldDriver.message',customAOV+'.outputs[0].driver', f=1)
            mc.connectAttr('defaultArnoldFilter.message',customAOV+'.outputs[0].filter', f=1)

            # connect to default shader
            mc.connectAttr(aiUshader+'.outColor',customAOV+'.defaultValue',f=1)

    #-----------------------------------------#
    # 标准aov创建
    # AO(rgba),N(vector),P(point),Z(float),ZAA(rgba),Fre,motionvector,sss,direct_specular ; indirect_specular ;
    def aovCommonBuild(self):
        mc.setAttr('defaultArnoldDriver.mergeAOVs',1)

        #-----------------#
        # AO shader
        AOShader = 'SHD_AO_arnold'
        if mc.ls( AOShader ):
            mc.delete(AOShader)
        AOSG = 'SHD_AO_arnold_SG'
        if mc.ls( AOSG ):
            mc.delete( AOSG )
        AOShader = mc.shadingNode ('aiAmbientOcclusion', asShader=True, name= AOShader)
        AOSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( AOSG ))
        mc.connectAttr(('%s.%s') % (AOShader , 'outColor') , ('%s.%s') % (AOSG , 'surfaceShader'), f=True)
        #-----------------#
        # AO driver
        occArnoldPass = 'aiAOV_Occ'
        if mc.ls(occArnoldPass) :
            mc.delete(occArnoldPass)
        mc.createNode('aiAOV',name = occArnoldPass )
        mc.setAttr((occArnoldPass + '.name'),'AO',type = 'string')
        mc.setAttr((occArnoldPass + '.type'),6)
        aiAOVFilter_AO =  'aiAOVFilter_AO'
        if mc.ls(aiAOVFilter_AO):
            mc.delete(aiAOVFilter_AO)
        mc.createNode('aiAOVFilter',name = aiAOVFilter_AO )
        #mc.setAttr('%s.aiTranslator'%aiAOVFilter_AO,'closest',type = 'string')
        #-----------------#
        # AO 连接
        sourceAttr = ('%s.%s') % ('defaultArnoldDriver' , 'message')
        targetAttr = ('%s.%s') % (occArnoldPass , 'outputs[0].driver')
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        sourceAttr = ('%s.%s') % ( aiAOVFilter_AO , 'message')
        targetAttr = ('%s.%s') % (occArnoldPass, 'outputs[0].filter')
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        sourceAttr = ('%s.%s') % ( AOShader , 'outColor')
        targetAttr = ('%s.%s') % (occArnoldPass, 'defaultValue')
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)
        mc.setAttr((AOShader + '.samples'),4)

        sourceAttr = ('%s.%s') % ( occArnoldPass , 'message')
        aovListSize = mc.getAttr('defaultArnoldRenderOptions.aovList',s=1)
        targetAttr = ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[%s]'%aovListSize)
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        #----------------------#
        # N Driver
        nmArnoldPass = 'aiAOV_N'
        if mc.ls(nmArnoldPass) :
            mc.delete(nmArnoldPass)
        mc.createNode('aiAOV',name = nmArnoldPass )
        mc.setAttr((nmArnoldPass + '.name'),'N',type = 'string')
        mc.setAttr((nmArnoldPass + '.type'),5)
        aiAOVFilter_N =  'aiAOVFilter_N'
        if mc.ls(aiAOVFilter_N):
            mc.delete(aiAOVFilter_N)
        mc.createNode('aiAOVFilter',name = aiAOVFilter_N )
        mc.setAttr('%s.aiTranslator'%aiAOVFilter_N,'closest',type = 'string')
        # N 连接
        sourceAttr = ('%s.%s') % ('defaultArnoldDriver' , 'message')
        targetAttr = ('%s.%s') % (nmArnoldPass , 'outputs[0].driver')
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        sourceAttr = ('%s.%s') % ( aiAOVFilter_N , 'message')
        targetAttr = ('%s.%s') % (nmArnoldPass , 'outputs[0].filter')
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        sourceAttr = ('%s.%s') % ( nmArnoldPass , 'message')
        aovListSize = mc.getAttr('defaultArnoldRenderOptions.aovList',s=1)
        targetAttr = ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[%s]'%aovListSize)
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        #----------------------#
        # P driver
        pArnoldPass = 'aiAOV_P'
        if mc.ls(pArnoldPass) :
            mc.delete(pArnoldPass)
        mc.createNode('aiAOV',name = pArnoldPass )
        mc.setAttr((pArnoldPass + '.name'),'P',type = 'string')
        mc.setAttr((pArnoldPass + '.type'),8)
        aiAOVFilter_P =  'aiAOVFilter_P'
        if mc.ls(aiAOVFilter_P):
            mc.delete(aiAOVFilter_P)
        mc.createNode('aiAOVFilter',name = aiAOVFilter_P )
        mc.setAttr('%s.aiTranslator'%aiAOVFilter_P,'closest',type = 'string')
        # N 连接
        sourceAttr = ('%s.%s') % ('defaultArnoldDriver' , 'message')
        targetAttr = ('%s.%s') % (pArnoldPass , 'outputs[0].driver')
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        sourceAttr = ('%s.%s') % ( aiAOVFilter_P , 'message')
        targetAttr = ('%s.%s') % (pArnoldPass , 'outputs[0].filter')
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        sourceAttr = ('%s.%s') % ( pArnoldPass , 'message')
        aovListSize = mc.getAttr('defaultArnoldRenderOptions.aovList',s=1)
        targetAttr = ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[%s]'%aovListSize)
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        #----------------------#
        # Z driver
        ZArnoldPass = 'aiAOV_Z'
        if mc.ls(ZArnoldPass) :
            mc.delete(ZArnoldPass)
        mc.createNode('aiAOV',name = ZArnoldPass )
        mc.setAttr((ZArnoldPass + '.name'),'Z',type = 'string')
        mc.setAttr((ZArnoldPass + '.type'),4)
        aiAOVFilter_Z =  'aiAOVFilter_Z'
        if mc.ls(aiAOVFilter_Z):
            mc.delete(aiAOVFilter_Z)
        mc.createNode('aiAOVFilter',name = aiAOVFilter_Z )
        mc.setAttr('%s.aiTranslator'%aiAOVFilter_Z,'closest',type = 'string')
        # Z连接
        sourceAttr = ('%s.%s') % ('defaultArnoldDriver' , 'message')
        targetAttr = ('%s.%s') % (ZArnoldPass , 'outputs[0].driver')
        #cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        sourceAttr = ('%s.%s') % ( aiAOVFilter_Z , 'message')
        targetAttr = ('%s.%s') % (ZArnoldPass, 'outputs[0].filter')
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        sourceAttr = ('%s.%s') % ( ZArnoldPass , 'message')
        aovListSize = mc.getAttr('defaultArnoldRenderOptions.aovList',s=1)
        targetAttr = ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[%s]'%aovListSize)
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        #----------------------#
        # Fre shader
        FNShader = 'SHD_Fresnel_arnold'
        if mc.ls( FNShader ):
            mc.delete(FNShader)
        FNRamp = 'SHD_Fresnel_ramp_arnold'
        if mc.ls( FNRamp ):
            mc.delete(FNRamp)
        FNSample = 'SHD_Fresnel_Sample_arnold'
        if mc.ls( FNSample ):
            mc.delete(FNSample)
        FNSG = 'SHD_Fresnel_arnold_SG'
        if mc.ls( FNSG ):
            mc.delete( FNSG )
        FNShader = mc.shadingNode ('aiUtility', asShader=True, name= FNShader)
        FNRamp = mc.shadingNode ('ramp', asShader=True, name= FNRamp)
        FNSample = mc.shadingNode ('samplerInfo', asShader=True, name= FNSample)
        FNSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( FNSG ))
        mc.removeMultiInstance((FNRamp + '.colorEntryList[1]') , b = 1)
        mc.setAttr((FNShader + '.shadeMode'),2)
        mc.setAttr((FNRamp + '.interpolation'),3)
        mc.setAttr((FNRamp + '.colorEntryList[2].position'),1)
        mc.setAttr((FNRamp + '.colorEntryList[0].position'),0)
        mc.setAttr((FNRamp + '.colorEntryList[2].color'),0,0,0,type = 'double3')
        mc.setAttr((FNRamp + '.colorEntryList[0].color'),1,1,1,type = 'double3')
        mc.connectAttr(('%s.%s') % (FNShader , 'outColor') , ('%s.%s') % (FNSG , 'surfaceShader'), f=True)
        mc.connectAttr(('%s.%s') % (FNSample , 'facingRatio') , ('%s.%s') % (FNRamp , 'uCoord'), f=True)
        mc.connectAttr(('%s.%s') % (FNSample , 'facingRatio') , ('%s.%s') % (FNRamp , 'vCoord'), f=True)
        mc.connectAttr(('%s.%s') % (FNRamp , 'outColor') , ('%s.%s') % (FNShader , 'color'), f=True)
        # Fre driver
        fresenlArnoldPass = 'aiAOV_Fresnel'
        if mc.ls(fresenlArnoldPass) :
            mc.delete(fresenlArnoldPass)
        mc.createNode('aiAOV',name = fresenlArnoldPass )
        mc.setAttr((fresenlArnoldPass + '.name'),'Fre',type = 'string')
        mc.setAttr((fresenlArnoldPass + '.type'),5)
        aiAOVFilter_Fre =  'aiAOVFilter_Fre'
        if mc.ls(aiAOVFilter_Fre):
            mc.delete(aiAOVFilter_Fre)
        mc.createNode('aiAOVFilter',name = aiAOVFilter_Fre )
        #mc.setAttr('%s.aiTranslator'%aiAOVFilter_Fre,'closest',type = 'string')
        # Fre 连接
        sourceAttr = ('%s.%s') % ('defaultArnoldDriver' , 'message')
        targetAttr = ('%s.%s') % (fresenlArnoldPass , 'outputs[0].driver')
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        sourceAttr = ('%s.%s') % ( aiAOVFilter_Fre , 'message')
        targetAttr = ('%s.%s') % (fresenlArnoldPass , 'outputs[0].filter')
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        sourceAttr = ('%s.%s') % ( FNShader , 'outColor')
        targetAttr = ('%s.%s') % (fresenlArnoldPass, 'defaultValue')
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

        sourceAttr = ('%s.%s') % ( fresenlArnoldPass , 'message')
        aovListSize = mc.getAttr('defaultArnoldRenderOptions.aovList',s=1)
        targetAttr = ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[%s]'%aovListSize)
        cons = mc.listConnections(targetAttr,s=1,d=0,plugs=1)
        if cons:
            mc.disconnectAttr(cons[0] , targetAttr)
        mc.connectAttr(sourceAttr,targetAttr, f=True)

    # aov 切换开关, 1 开启, 0 关闭
    def aovSwitchOnOff(self,mode = 0):
        aovNodes = mc.ls(type = 'aiAOV')
        for aovNode in aovNodes:
            mc.editRenderLayerAdjustment('%s.enabled'%aovNode)
            mc.setAttr('%s.v'%aovNode,mode)

    #---------------------------------#
    # Fur AOV 核心,使用SG方法处理
    #------------------#
    def aovSGRGBCreate(self,mskName,AOVSGList):
        # 创建AOV
        aovNode = 'aiAOV_%s'%mskName
        if not mc.ls(aovNode,type = 'aiAOV'):
            mc.createNode('aiAOV',name = aovNode )
            mc.setAttr((aovNode + '.name'),mskName,type = 'string')
            aovListSize = mc.getAttr('defaultArnoldRenderOptions.aovList',s=1)
            for checkNum in range(aovListSize):
                cons = mc.listConnections('defaultArnoldRenderOptions.aovList[%s]'%str(checkNum),s=1,d=0)
                if not cons:
                    aovListSize = checkNum
                    break
            mc.connectAttr(aovNode+'.message','defaultArnoldRenderOptions.aovList['+ str(aovListSize)+']',f=1)
            mc.connectAttr('defaultArnoldDriver.message',aovNode+'.outputs[0].driver', f=1)
            mc.connectAttr('defaultArnoldFilter.message',aovNode+'.outputs[0].filter', f=1)
        # 获取编号
        #consAttr = mc.listConnections(aovNode,s=0,d=1,plugs=1,type = 'aiOptions')
        #consIndex = int(consAttr[0].split('[')[-1].split(']')[0])
        # RGB
        aiUshaderR = 'R_aiUtility_%s'%mskName
        if mc.ls(aiUshaderR):
            mc.delete(aiUshaderR)
        aiUshaderR = mc.shadingNode('aiUtility', asShader=1,name = aiUshaderR)
        mc.setAttr(aiUshaderR+'.shadeMode',2)
        mc.setAttr(aiUshaderR+'.color',1,0,0,type = 'double3')

        aiUshaderG = 'G_aiUtility_%s'%mskName
        if mc.ls(aiUshaderG):
            mc.delete(aiUshaderG)
        aiUshaderG = mc.shadingNode('aiUtility', asShader=1,name = aiUshaderG)
        mc.setAttr(aiUshaderG+'.shadeMode',2)
        mc.setAttr(aiUshaderG+'.color',0,1,0,type = 'double3')

        aiUshaderB = 'B_aiUtility_%s'%mskName
        if mc.ls(aiUshaderB):
            mc.delete(aiUshaderB)
        aiUshaderB = mc.shadingNode('aiUtility', asShader=1,name = aiUshaderB)
        mc.setAttr(aiUshaderB+'.shadeMode',2)
        mc.setAttr(aiUshaderB+'.color',0,0,1,type = 'double3')
        # 连接
        for SGNode in AOVSGList[0]:
            consIndex = self.getAovIndexByName(SGNode,mskName)
            checkSGAttr = SGNode+'.aiCustomAOVs[%s].aovInput'%(str(consIndex))
            cons = mc.listConnections(checkSGAttr,s=1,d=0,plugs=1)
            if cons:
                mc.disconnectAttr(cons[0],checkSGAttr)
            mc.connectAttr((aiUshaderR+'.outColor'),checkSGAttr,f=1)
        for SGNode in AOVSGList[1]:
            consIndex = self.getAovIndexByName(SGNode,mskName)
            checkSGAttr = SGNode+'.aiCustomAOVs[%s].aovInput'%(str(consIndex))
            print '-------'
            print checkSGAttr
            cons = mc.listConnections(checkSGAttr,s=1,d=0,plugs=1)
            if cons:
                mc.disconnectAttr(cons[0],checkSGAttr)
            print aiUshaderG
            mc.connectAttr((aiUshaderG+'.outColor'),checkSGAttr,f=1)
        for SGNode in AOVSGList[2]:
            consIndex = self.getAovIndexByName(SGNode,mskName)
            checkSGAttr = SGNode+'.aiCustomAOVs[%s].aovInput'%(str(consIndex))
            cons = mc.listConnections(checkSGAttr,s=1,d=0,plugs=1)
            if cons:
                mc.disconnectAttr(cons[0],checkSGAttr)
            mc.connectAttr((aiUshaderB+'.outColor'),checkSGAttr,f=1)

    def getAovIndexByName(self,sgNode, aovName):
        import pymel.core as pm
        sg = pm.nt.ShadingEngine(sgNode)
        lastIndex = -1
        nextIndex = None
        for at in sg.aiCustomAOVs:
            currIndex = at.index()
            if at.aovName.get() == aovName:
                return currIndex
            if nextIndex is None and currIndex > (lastIndex +1):
                nextIndex = lastIndex +1
            lastIndex = currIndex
        if nextIndex is None:
            nextIndex = lastIndex +1
        at = sg.aiCustomAOVs[nextIndex]
        at.aovName.set(aovName)
        return nextIndex

    #---------------------------------#
    # FUR应用,MT,TL,XIAOXIAO->Geezer
    def mi_MTXFurCreate(self):
        yetiNodes = mc.ls(type = 'pgYetiMaya') + mc.ls(type = 'shaveHair')
        # XX/TL/MT
        MTX_RList = []
        MTX_GList = []
        MTX_BList = []
        for yetiNode in yetiNodes:
            SGNode = mc.listConnections(yetiNode,s=0,d=1,type = 'shadingEngine')
            if not SGNode:
                continue
            SGNode = SGNode[0]
            SGNS = SGNode
            if ':' in SGNS:
                SGNS = SGNode.split(':')[0]
            # MTX
            if 'mi_c002' in SGNS:
                MTX_RList.append(SGNode)
            if 'mi_c001' in SGNS:
                MTX_GList.append(SGNode)
            #if 'mi_c005' in SGNS or 'mi_c006' in SGNS:
            if 'mi_c043' in SGNS:
                MTX_BList.append(SGNode)

        if MTX_RList or MTX_GList or MTX_BList:
            FURRGBList = [MTX_RList,MTX_GList,MTX_BList]
            self.aovSGRGBCreate('FUR_MTX',FURRGBList)

    #---------------------------------#
    # 角色间 idp
    def mi_EveryIDPCreate(self):
        # 记录
        sgNodes = mc.ls(type = 'shadingEngine')
        SGInfoList = {}
        for sgNode in sgNodes:
            inr = mc.referenceQuery(sgNode,inr=1)
            if not inr:
                continue
            ns = sgNode.split(':')[0]
            if ns[0].lower() not in ['c']:
                continue
            if ns not in SGInfoList.keys():
                SGInfoList[ns] = [sgNode]
            else:
                SGInfoList[ns].append(sgNode)
        #分类创建,随机类型
        sgAssetList = SGInfoList.keys()
        cycleNum = len(sgAssetList) / 3
        checkE = len(sgAssetList) % 3
        if checkE != 0:
            cycleNum += 1
        for checkNum in range(cycleNum):
            RList = sgAssetList[checkNum*3]
            if (checkNum*3+1) <= (len(sgAssetList)-1):
                GList = sgAssetList[checkNum*3+1]
            else:
                GList = []
            if (checkNum*3+2) <= (len(sgAssetList)-1):
                BList = sgAssetList[checkNum*3+2]
            else:
                BList = []
            RGBList = [RList,GList,BList]
            self.aovSGRGBCreate('EAP_%s'%(str(checkNum)),RGBList)

    #---------------------------------#
    # 显示层创建篇
    #---------------------------------#
    def renderLayerCreateBG(self):
        pass


    def mi_set_Rnd_parameter01(self,encounter_asset_ID):####========if file asset encounter some special ID ,do something.......
        #PyNode(u'defaultArnoldDriver').halfPrecision.set(0)
        if encounter_asset_ID:
            p_mt = re.compile(encounter_asset_ID)
            for eachRef in listReferences():
                if p_mt.search(eachRef.path):
                    if encounter_asset_ID == u'c001002MiniTiger':
                        PyNode(u'defaultArnoldRenderOptions').abortOnError.set(0)

    # Sylvain Scripts
    def sylvainRenderLayersUI(self):
        import sys
        if self.sylvainPath not in sys.path:
            sys.path.append(self.sylvainPath)
        import sylvainRenderToolsUI
        reload(sylvainRenderToolsUI)
        sylvainRenderToolsUI.sylvainRenderToolsUI().sylvainRenderLayersUI()

    # uiSwicth
    def uiSwitch(self,menuName):
        needInfo = mc.optionMenuGrp(menuName,q=1,value = 1).replace(' ','')
        import sys
        if self.sylvainPath not in sys.path:
            sys.path.append(self.sylvainPath)
        import sylvainRenderToolsUI
        reload(sylvainRenderToolsUI)
        sylvainRenderToolsUI.sylvainRenderToolsUI().sylvainButtonUI(needInfo)

    # sylvain auto
    def sylvainAutoRenderLayers(self):
        import sys
        if self.sylvainPath not in sys.path:
            sys.path.append(self.sylvainPath)
        import sylvainRenderToolsUI
        reload(sylvainRenderToolsUI)
        sylvainRenderToolsUI.sylvainRenderToolsUI().sylvainAutoRenderLayers()

    def SylvainShaderCheck(self):
        import sys
        if self.sylvainPath not in sys.path:
            sys.path.append(self.sylvainPath)
        import sylvainRenderToolsUI
        reload(sylvainRenderToolsUI)
        sylvainRenderToolsUI.sylvainRenderToolsUI().SylvainShaderCheck()

    #--------------------------------------#
    # 通用分层
    #--------------------------------------#
    def checkCommonRenderLayersCreate(self):
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
        reload(sk_smoothSet)
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 导入AOV
        aovFile = 'Z:/Projects/MiniTiger/MiniTiger_Scratch/Render/ToS/010/BASE_SHADERS_AOV.mb'
        aovNodes = mc.ls(type = 'aiAOV')
        if not aovNodes:
            mc.file(aovFile,i=1)
        # 应用smoothSet
        sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify=0)
        # 另存
        localPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server=0,infoMode=9)
        fileName = mc.file(exn=1,q=1).split('/')[-1]
        localBaseFile = localPath + fileName
        mc.file(rename = localBaseFile)
        mc.file(s=1,f=1)
        # 分类
        chrObjs = self.getAssetObjs('chr')
        prpObjs = self.getAssetObjs('prp')
        setObjs = self.getAssetObjs('set')
        chrGrps = self.getAssetObjs('chr',grpMode=1)
        prpGrps = self.getAssetObjs('prp',grpMode=1)
        setGrps = self.getAssetObjs('set',grpMode=1)
        #-------------------#
        # 场景分层
        layerName = 'BG_CO'
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer((chrGrps + prpGrps + setGrps), name = layerName, noRecurse=1, makeCurrent=1)
        # 关闭pr
        self.checkSetTargetAttrs(chrObjs + prpObjs)
        setFile = '%s_bg_lr.mb'%(shotID)
        localSetFile = localPath + setFile
        mc.file(rename = localSetFile)
        mc.file(s=1,f=1)
        #-------------------#
        # CHR,FUR分层
        mc.file(localBaseFile,o=1,f=1)
        # CHR_CO
        layerName = 'CHR_CO'
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer((chrGrps + prpGrps + setGrps), name = layerName, noRecurse=1, makeCurrent=1)
        # 关闭pr
        self.checkSetTargetAttrs(setObjs)
        # FUR
        layerName = 'FUR_CO'
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer((chrGrps + prpGrps + setGrps), name = layerName, noRecurse=1, makeCurrent=1)
        # 关闭pr
        self.checkSetTargetAttrs(chrObjs + prpObjs+setObjs)
        chrFile = '%s_chr_lr.mb'%(shotID)
        localChrFile = localPath + chrFile
        mc.file(rename = localChrFile)
        mc.file(s=1,f=1)

        print '-----------outFiles'
        print localPath

    # 获取物体类型
    def getAssetObjs(self,assetType,grpMode = 0):
        if assetType in ['chr']:
            rootGrp = 'CHR_GRP'
        if assetType in ['prp']:
            rootGrp = 'PRP_GRP'
        if assetType in ['set']:
            rootGrp = 'SET_GRP'
        needObjs = []
        if grpMode:
            needObjs = mc.listRelatives(rootGrp,c=1,type = 'transform',f=1)
            if not needObjs:
                needObjs = []
        else:
            meshes = mc.listRelatives(rootGrp,ad=1,type = 'mesh',ni=1,f=1)
            if meshes:
                needObjs = mc.listRelatives(meshes,p=1,type = 'transform',f=1)
            if not needObjs:
                needObjs = []
            else:
                needObjs = list(set(needObjs))
        return needObjs

    # setObjAttrs
    def checkSetTargetAttrs(self,checkObjs):
        for checkObj in checkObjs:
            checkMesh = mc.listRelatives(checkObj,s=1,type = 'mesh',ni=1,f=1)
            checkMesh = checkMesh[0]
            meshAttr = checkMesh + '.primaryVisibility'
            mc.editRenderLayerAdjustment(meshAttr)
            mc.setAttr(meshAttr,0)

    #-------------------------------------#
    # 螺旋桨 系列

    # 镜头统一导出
    def bladeAnimationExport(self,sceneID = ''):
        xlsPath = 'Z:/Projects/MiniTiger/MiniTiger_Scratch/ModelingAndTexture/toRender/blade/xls'
        xlsPath = '%s/blade_xls.xls'%xlsPath
        import xlrd
        fileData = xlrd.open_workbook(xlsPath)
        needData = fileData.sheets()[0]
        shotIDList = needData.col_values(1)
        for checkID in shotIDList:
            if '_' not in checkID:
                continue
            if '\n' in checkID:
                checkID = checkID.replace('\n','')
            runState = 0
            if sceneID:
                if checkID.split('_')[0] == sceneID:
                    runState = 1
            else:
                runState = 1
            if runState:
                self.bladeGetAnimation(checkID)

    # 单镜头处理blade动画
    def bladeGetAnimation(self,infoID):
        shotInfos = infoID.split('_')
        sceneID = shotInfos[0]
        shotID = shotInfos[1]
        bladeServerPath = 'Z:/Projects/MiniTiger/MiniTiger_Scratch/ModelingAndTexture/toRender/blade'
        tempFolder = '%s/shotBlade'%bladeServerPath
        import os
        if not os.path.exists(tempFolder):
            os.makedirs(tempFolder)
        bladeShotFile = '%s/blade_%s_%s.mb'%(tempFolder,sceneID,shotID)
        if os.path.exists(bladeShotFile):
            print u'\n------------------'
            print bladeShotFile
            print u'--------[%s]:已存在\n'%infoID
            return
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        anFilePath = 'Z:/Projects/MiniTiger/Project/scenes/Animation/episode_%s/scene_%s/anim'%(sceneID,shotID)
        # 寻找最新版
        dataGet = os.popen('DIR %s /b'%(anFilePath.replace('/','\\')))
        getInfo = dataGet.read()
        allInfos = getInfo.split('\n')
        needFile = ''
        for checkInfo in allInfos:
            if '.mb' not in checkInfo:
                continue
            needFile = checkInfo
        anFile = '%s/%s'%(anFilePath,needFile)
        print '------'
        print anFile
        # 开始处理
        bladeFile = '%s/blade.mb'%bladeServerPath
        assetIDList = ['p077003LittleairplaneA','p077004LittleairplaneB']
        # 打开文件
        mc.file(anFile,open=1,f=1)
        io = (mc.playbackOptions(q=1, minTime=1)-10, mc.playbackOptions(q=1, maxTime=1)+10)
        # 查找飞机
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNsList = refInfos[2][0]
        filePlaneNsList = []
        for ns in refNsList:
            if '_' not in ns:
                continue
            assetID = ns.split('_')[1]
            if assetID in assetIDList:
                filePlaneNsList.append(ns)
        if not filePlaneNsList:
            print '--------[Error]:No Plane In File!!!'
            return 1
        # 处理blade
        bladeObjs = []
        bladeGrp = 'blade_Grp'
        if mc.ls(bladeGrp):
            mc.delete(bladeGrp)
        mc.group(em=1,name = bladeGrp)
        for checkNs in filePlaneNsList:
            mc.file(bladeFile,i=1)
            assetID = checkNs.split('_')[1]
            bladeObj = 'MSH_c_hi_blade_%s'%assetID
            mc.rename('MSH_c_hi_blade_','MSH_c_hi_blade_%s'%assetID)
            bladePosGrp = mc.group(em=1,name = 'MSH_c_hi_blade_Pos_%s'%assetID)
            mc.parent(bladeObj,bladePosGrp)
            mc.parent(bladePosGrp,bladeGrp)
            ctrlGrp = '%s:move_ctrl'%checkNs
            mc.parentConstraint(ctrlGrp , bladePosGrp , maintainOffset = 0)
            rotateGrp = '%s:luoXuanJiang_ctrl'%checkNs
            mc.orientConstraint(rotateGrp , bladeObj , maintainOffset = 0)
            bladeObjs.append(bladePosGrp)
            bladeObjs.append(bladeObj)
        mc.bakeResults(bladeObjs,  t=io,
                simulation = 0,
                sampleBy = 1,
                disableImplicitControl=1,
                preserveOutsideKeys=1,
                sparseAnimCurveBake=1,
                removeBakedAttributeFromLayer=0,
                bakeOnOverrideLayer=0,
                controlPoints=0,
                shape=1)
        childObjs = mc.listRelatives(bladeGrp,ad = 1)
        for childObj in childObjs:
            if 'Constraint' in childObj:
                mc.delete(childObj)
        mc.select(bladeGrp)
        mc.file(bladeShotFile, force=1, options="v=0", type='mayaBinary', preserveReferences=1, exportSelected=1)
        print '\n------BladeShotFIle'
        print bladeShotFile


    # 镜头文件导入
    def bladeRenderCreate(self):
        import os
        fileInfos = mc.file(exn=1,q=1).split('/')[-1].split('_')
        sceneID = fileInfos[1]
        shotID = fileInfos[2]
        bladeServerPath = 'Z:/Projects/MiniTiger/MiniTiger_Scratch/ModelingAndTexture/toRender/blade'
        bladeShotFile = '%s/shotBlade/blade_%s_%s.mb'%(bladeServerPath,sceneID,shotID)
        if not os.path.exists(bladeShotFile):
            print '\n--------------'
            print u'----[No Blade Shot File]:'
            print bladeShotFile
            mc.error()
        bladeGrp = 'blade_Grp'
        if mc.ls(bladeGrp):
            mc.delete(bladeGrp)
        mc.file(bladeShotFile,i=1)
        # rl create
        mc.editRenderLayerGlobals(currentRenderLayer = 'CHRCOLOR')
        camAAValue = mc.getAttr('defaultArnoldRenderOptions.AASamples')
        bladeRL  = 'BLADE'
        if mc.ls(bladeRL):
            mc.delete(bladeRL)
        mc.duplicate('CHRCOLOR',inputConnections = 1,name = bladeRL )
        # add
        mc.editRenderLayerMembers(bladeRL,bladeGrp)
        # 切渲染层
        mc.editRenderLayerGlobals(currentRenderLayer = bladeRL)
        mc.setAttr('defaultArnoldRenderOptions.AASamples',camAAValue)
        mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples',0)
        mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples',0)
        mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples',0)
        mc.setAttr('defaultArnoldRenderOptions.GISssSamples',0)
        mc.setAttr('defaultArnoldRenderOptions.GIVolumeSamples',0)
        # turn off
        rlObjs = mc.ls(type = 'renderLayer')
        for checkRL in rlObjs:
            refState = mc.referenceQuery(checkRL,inr=1)
            if refState:
                continue
            onState = 0
            if checkRL in ['BLADE']:
                onState = 1
            mc.setAttr('%s.renderable'%checkRL,onState)
        # hide
        hideObjs  = mc.ls('*Littleairplane*:*_propeller3_') + mc.ls('*Littleairplane*:*_propeller4_') + mc.ls('*Littleairplane*:*_propeller5_') + mc.ls('*Littleairplane*:*_propeller6_')
        for checkObj in hideObjs:
            mc.setAttr(checkObj+'.v',0)
        # aov off
        mc.setAttr('defaultArnoldRenderOptions.aovMode',0)
        mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',0)
        # CHR/PRP group in aiMatte 1
        chrMeshes = mc.listRelatives('CHR_GRP',ad=1,ni=1,type = 'mesh')
        if not chrMeshes:
            chrMeshes = []
        prpMeshes =  mc.listRelatives('PRP_GRP',ad=1,ni=1,type = 'mesh')
        if not prpMeshes:
            prpMeshes = []
        checkMeshes = chrMeshes + prpMeshes
        for checkMesh in checkMeshes:
            checkAttr = '%s.aiMatte'%checkMesh
            if not mc.ls(checkAttr):
                continue
            mc.setAttr(checkAttr,1)
        # save
        fileName = '%s/rlBlade/mi_%s_%s_BLADE_lr_c001.mb'%(bladeServerPath,sceneID,shotID)
        mc.file(rename = fileName)
        mc.file(s = 1,f=1)
        print '\n-------[Blade RL]Done!!!'
        print fileName
        print '\n'



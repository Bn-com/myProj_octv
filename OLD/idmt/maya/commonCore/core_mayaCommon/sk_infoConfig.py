# -*- coding: utf-8 -*-
#Created on 2013-8-1
#@author: shenkang

import re,os

class sk_infoConfig(object):
    def __init__(self):
        self.ppType = 'GDC'
        self.allProj = []
        self.simScale= [['sim4',0.0625],['sim4',0.0625],['sim16',0.0625],['sim4',0.0625]]
        self.simFolder=['sim2','sim4','sim8','sim16','sim32']
        # dictMode
        self.dictMode = 1
        # visionKey
        self.versionKey = '_c'
        self.renderGrp = 'MODEL'
        self.setInfos = ['SMOOTH_SET','CACHE_OBJS','TRANSANIM_OBJS']
        self.assetInfos     = ['c'         ,'p'    ,'s'   ,'e']
        self.assetFullInfos = ['characters','props','sets','envs']
        self.setKeys  = ['s','e','S','E']
        self.setFullKeys = ['sets','envs','Environment']
        self.hmlType  = ['l','m','h','t']
        self.masterAni = '_ms_anim.'
        self.masterASp = 'Master'
        self.masterRnd = '_ms_render.'
        self.masterRSp = 'Master'
        self.masterCtrl = 'World_Ctrl'
        self.bkImgAttr  = 'foodPath'
        self.bkCacheAttr= 'foodPath'
        self.dyMoGrps   = ['hairSys_Grp','vfxGrp']
        self.dyMoAttrs  = ['_hair_']
        self.fsNoHideGrps=['VFX_GRP','Cluster_GRP']
        self.simInfos  = ['mo'   ,'mp'   ,'rg'     ,'tx'     ,'pv'    ,'ly'    ,'bl'      ,'sl'      ,'an'       ,'sa'         ,'cw'   ,'sd'      ,'dy'      ,'fs'    ,'ef'    ,'lr'      ,'cp']
        self.fullInfos = ['model','morph','rigging','texture','previs','layout','blocking','3Dlayout','animation','3Danimation','crowd','setdress','dynamic','finish' ,'effect','lighting','composite']
        self.sceneGrps = ['CHR_GRP','PRP_GRP','SET_GRP','ENV_GRP','OTC_GRP','CAM_GRP']
        self.cVStep    = ['cw','cp','cr']
        self.aVStep    = ['ac','au','an','am','ani']
        self.donotCleanNsList = ['nd__']
        self.facialCamera = ['facial_camera']
        self.playblastSteps = ['ly','bl','an','dy','fx']
        # format
        self.formatInfo = {'ma':'mayaAscii','.ma':'mayaAscii','mb':'mayaAscii','.mb':'mayaAscii'}
        # folder
        self.sourceImgsFolder =  'Sourceimages'
        self.sourceImgsLower  =  'low'
        self.serverDataFolder =  'Data'
        self.serverDailyFolder=  'Daily'
        self.projFolder       =  'project'
        self.assetFolder      =  'assets'
        self.shotFolder       =  'shots'
        self.abcCacheFolder   =  'AbcCache'
        self.dyCacheFolder    =  'DyCache'
        self.vfxCacheFolder   =  'VfxCache'
        self.gpuCacheFolder   =  'GpuCache'
        self.assetCacheFolder =  'AssetCache'
        self.eyeInfosFolder   =  'EyeLight'
        self.childAssetsFolder=  'ChildAsset'
        self.shotCamFolder    =  'episode_camera'
        # 0-1???geoCache | 2???abc
        self.cacheType = 2
        self.cacheInfo = '_abcCache'
        # sysEnv
        self.localBase = 'D:/Info_Temp/temp'
        self.serverEnv = ['Z:/','//file-cluster/GDC/']
        self.serverPre = '//file-cluster/GDC/Projects'
        # stereo
        self.stereoProjs = ['']
        self.stereoAttrs = ['isep','interaxialSeparation','zeroParallax']
        self.stereoStep  = ['s1','s2']
        # rgModeProjs
        self.rgModeProjs = ['LION','Yak', 'do6']
        # shotType3
        self.shotType3Projs = ['nj','yd','tf','csl','Xyj']
        # assemblyProj
        self.assemblyProjs  = ['']
        # textureAttr
        self.textureAttrs = ['fileTextureName','filename']
        # ??????type
        self.SGMode = 0
        # baseDict
        self.baseDict = {'reel':'','sequence':'','shot':'','asset':'','area':'','taskName':'','taskType':'','hasTk':'','version':'','highMode':'','category':'','categoryShortname':'','fileExt':'','projBase':'','userShortname':''}
        self.taskType = {'mdl':'model','rig':'rigging','shd':'shading','art':'art','plate':'plate','cam':'camera','anim':'animation','comp':'composition','edit':'editorial','lgt':'lighting'}
        self.nodeDict = {'file':'.fileTextureName','aiImage':'.filename','aiStandIn':'.dso','AlembicNode':'.abc_File','cacheFile':'.cachePath'}
        # ?????????????????????
        self.camNMFProjList = ['mi','do6']

    #----------------------------------#
    # ??????????????????????????????
    # 0.??????????????????
    # 1.???????????????
    # Author: ???  ???
    # Data    :2013_05_16
    #----------------------------------#

    def checkShotInfo(self,noFormat = 0):
        import maya.cmds as mc
        temp = (mc.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
            if noFormat and '.' in info[-1]:
                info[-1] = info[-1].split('.')[0]
        else:
            #mc.warning(unicode('========================??????????????????????????????????????????========================', 'utf8'))
            mc.warning(u'========================??????????????????????????????????????????========================')
        return info                                    

    def checkShotID(self):
        shotInfos = self.checkShotInfo()
        shotType = self.checkShotType()
        shotID = '%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2])
        if shotType == 3:
            shotID = '%s_%s'%(shotID,shotInfos[3])
        if '.' in shotID:
            shotID = shotID.split('.')[0]
        return shotID

    def checkShotIDFolder(self):
        shotInfos = self.checkShotInfo()
        shotType = self.checkShotType()
        shotIDFolder = 'episode_%s/scene_%s'%(shotInfos[1],shotInfos[2])
        if shotType == 3:
            shotIDFolder = 'episode_%s/sequence_%s/scene_%s'%(shotInfos[1],shotInfos[2],shotInfos[3])
        return shotIDFolder

    def checkStereoProj(self,shotInfos = []):
        if not shotInfos:
            shotInfos = self.checkShotInfo()
        stereoMode = 0
        steProjList = ['do3','do4','do5','do6','mi','mi2','mk']
        if shotInfos[0] in steProjList:
            stereoMode = 1
        return stereoMode

    # ????????????????????????
    def checkPCFilePath(self):
        import maya.cmds as mc
        filePath = (mc.file(query=1, exn=1)).split('/')
        path = ''
        if filePath[0] != 'Z' and filePath[0] != '':
            for i in range(len(filePath) - 1):
                path = path + filePath[i] + '\\'
        return path

    #----------------------------------#
    # ????????????'/'???'\\'???
    # ??? ????????????
    # Author: ???  ???
    # Data    :2013_09_16
    #----------------------------------#
    def checkPath2ExplorerPath(self,path):
        pathInfo = []
        newPath = ''
        if '/' in path:
            pathInfo = path.split('/')
            for i in range(len(pathInfo)):
                if i == 0:
                    newPath = pathInfo[i] + '\\'
                else:
                    if pathInfo[i]:
                        newPath = newPath + pathInfo[i] + '\\'
        return newPath

    #----------------------------------#
    # ?????????????????????????????????
    # 0.??????
    # Author: ???  ???
    # Data    :2013_06_10
    #----------------------------------#
    # ??????infot??????
    def checkLocalInfoPath(self):
        import maya.cmds as mc
        localInfoPath = ('D:/Info_Temp/temp/')
        mc.sysFile(localInfoPath, makeDir=True)
        return localInfoPath
    
    # ????????????project??????
    # typeMode 0 ?????? '/' ?????? | typeMode 1 ?????? '\\' ??????
    # checkMode ??? shotAssetTextureCheck?????????,????????????file-cluster
    def checkProjectServerPath(self,typeMode = 0,stepMode = '',checkMode = 0,dirInfo = []):
        if not dirInfo:
            dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        projectServerPath = '//file-cluster/GDC/Projects/' + project + '/Project/'
        if project in ['YongTai']:
            projectServerPath = '//file-cluster/GDC/Projects/DomesticProject/' + project + '/Project/'
        if project in ['DiveollyDive5','LION'] and stepMode not in ['cache']:
            projectServerPath = 'L:/Projects/' + project + '/Project/'
        if stepMode in ['cp'] and project in ['ShunLiu','MiniTiger']:
            projectServerPath = 'L:/Projects/' + project + '/Project/'
        LProjList = ['DiveollyDive6']
        if project in LProjList and not checkMode:
            projectServerPath = 'L:/Projects/' + project + '/Project/'
        if typeMode:
            projectServerPath = projectServerPath.replace('/','\\')
        return projectServerPath

    #----------------------------------#
    # ????????????????????????????????????????????????
    # ?????? 2016.5
    #----------------------------------#
    #-----------------------------------------#
    # infoMode ??????
    # ShotInfo : 1 data/ShotShaderInfo  | 2 data/AbcCache | 3 dyCacheFolder | 4 vfxCacheFolder | 5 camInfoOutInfo |
    #            6 animCleanTemp        | 7 fxAbcCache    | 8 camAbc        | 9 lightInfo      | 10 ShotDisTemp
    #            11 camTemp
    def checkShotDataInfoPath(self,server = 0,infoMode = 1,shotInfos = []):
        infoKey = ''
        if server:
            pathBase = self.checkProjectServerPath()
        else:
            pathBase = self.checkLocalInfoPath()
        if not shotInfos:
            shotInfos = self.checkShotInfo()
        shotType = self.checkShotType(shotInfos[0])

        infoKey = ''

        if infoMode == 0:
            infoKey = 'GeoCache'
        if infoMode == 1:
            infoKey = 'ShotShaderInfo'
        if infoMode == 2:
            infoKey = 'AbcCache'
        if infoMode == 2.5:
            infoKey = 'alembic'
        if infoMode == 3:
            infoKey = 'DyCache'
        if infoMode == 4:
            infoKey = 'VfxCache'
        if infoMode == 5:
            infoKey = 'CamInOutInfo'
        if infoMode == 6:
            infoKey = 'AnimCleanTemp'
        if infoMode == 7:
            infoKey = 'FxAbcCache'
        if infoMode == 8:
            infoKey = 'CamAbc'
        if infoMode == 9:
            infoKey = 'LightInfos'
        if infoMode == 10:
            infoKey = 'ShotDisTemp'
        if infoMode == 11:
            infoKey = 'CamTemp'

        shotFolder = '%s/%s'%(shotInfos[1],shotInfos[2])
        if shotType == 3:
            shotFolder = '%s/%s/%s'%(shotInfos[1],shotInfos[2],shotInfos[3])

        if infoKey:
            needPathShot = '%sdata/%s/%s/'%(pathBase,infoKey,shotFolder)
        else:
            needPathShot = '%s%s/%s/'%(pathBase,shotInfos[0],shotFolder)

        if not server and not os.path.exists(needPathShot):
            os.makedirs(needPathShot)
        return needPathShot

    # AssetInfo : 1 eyeLightInfo | 2 gpuCache | 3 smoothSet       | 4 shaders                  |5 assetCacheFolder |
    # AssetInfo : 6 childAsset   | 7 CamAbc   | 8 transShaderInfo | 9  displacementShaderInfo  |10 refAssets       |
    def checkAssetInfoPath(self,server = 0,infoMode = 1,shotInfos = []):
        if server:
            pathBase = self.checkProjectServerPath()
        else:
            pathBase = self.checkLocalInfoPath()
        if not shotInfos:
            shotInfos = self.checkShotInfo()

        infoKey = ''

        if infoMode == 1:
            infoKey = 'EyeLight'
        if infoMode == 2:
            infoKey = 'GpuCache'
        if infoMode == 3:
            infoKey = 'AssetInfos/smoothSetInfo'
        if infoMode == 4:
            infoKey = 'AssetInfos/shaderInfos'
        if infoMode == 5:
            infoKey = 'AssetCache'
        if infoMode == 6:
            infoKey = 'ChildAsset'
        if infoMode == 7:
            infoKey = 'CamAbc'
        if infoMode == 8:
            infoKey = 'AssetInfos/transShaderInfo'
        if infoMode == 9:
            infoKey = 'AssetInfos/displacementShaderInfo'
        if infoMode == 10:
            infoKey = 'RefAssets'

        assetFolder = '%s/%s'%(shotInfos[1],shotInfos[2])
        if infoKey:
            needPathShot = '%sdata/%s/%s/'%(pathBase,infoKey,assetFolder)
        else:
            needPathShot = '%s%s/%s/'%(pathBase,shotInfos[0],assetFolder)

        if not server and not os.path.exists(needPathShot):
            os.makedirs(needPathShot)
        return needPathShot

    #---------------------------------------#
    # dict ????????????
    #---------------------------------------#
    #???getAssetDict
    def checkGetAssetDict(self,shotInfos = []):
        if not shotInfos:
            shotInfos = self.checkShotInfo(0)
        dictInfo = dict()
        dictInfo['project'] = self.checkProjectNameSimple2Full(shotInfos[0])
        dictInfo['showShortname'] = shotInfos[0]
        dictInfo['area'] = 'assets'
        dictInfo['asset'] = shotInfos[1]
        dictInfo['category'] = self.assetFullInfos[self.assetInfos.index(dictInfo['asset'][0])]
        dictInfo['highMode'] = ''
        dictInfo['hasTk'] = 0
        dictInfo['version'] = ''
        lastInfo = shotInfos[-1].split('.')[0]
        if lastInfo[0] in [self.versionKey] and lastInfo[0:2] not in self.cVStep:
            dictInfo['hasTk'] = 1
            dictInfo['version'] = lastInfo[0]
        if len(shotInfos) > 2:
            dictInfo['highMode'] = shotInfos[2]
        dictInfo['taskType'] = ''
        if len(shotInfos) > 3:
            dictInfo['taskType'] = shotInfos[3].split('.')[0]
        dictInfo['assetID'] = dictInfo['asset']
        dictInfo['assetType'] = dictInfo['category']
        dictInfo['projFull'] = dictInfo['project']
        dictInfo['projSimp'] = dictInfo['showShortname']
        dictInfo['stepFull'] = dictInfo['category']
        dictInfo['stepSimp'] = dictInfo['taskType']
        return dictInfo

    #???getShotDict
    def checkGetShotDict(self,shotInfos = []):
        if not shotInfos:
            shotInfos = self.checkShotInfo(0)
        shotType = self.checkShotType(shotInfos[0])
        dictInfo = dict()
        dictInfo['project'] = self.checkProjectNameSimple2Full(shotInfos[0])
        dictInfo['showShortname'] = shotInfos[0]
        dictInfo['area'] = 'shots'
        dictInfo['asset'] = ''
        dictInfo['taskName'] = ''
        dictInfo['shotType'] = shotType
        dictInfo['reel'] = ''
        dictInfo['hasTk'] = 0
        dictInfo['shotID'] = '%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2])
        dictInfo['version'] = ''
        lastInfo = shotInfos[-1].split('.')[0]
        if lastInfo[0] in [self.versionKey] and lastInfo[0:2] not in self.cVStep:
            dictInfo['hasTk'] = 1
            dictInfo['version'] = lastInfo[0]
        dictInfo['sequence'] = shotInfos[1]
        if len(shotInfos) < 3:
            dictInfo['shot'] = ''
        else:
            dictInfo['shot'] = shotInfos[2]
        dictInfo['taskType'] = ''
        if len(shotInfos) > 3:
            dictInfo['taskType'] = shotInfos[3]
        if shotType == 3:
            dictInfo['shotType'] = 3
            dictInfo['reel'] = shotInfos[1]
            dictInfo['sequence'] = shotInfos[2]
            dictInfo['shot'] = shotInfos[3]
            dictInfo['taskType'] = ''
            dictInfo['shotID'] = '%s_%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2],shotInfos[3])
            if len(shotInfos) > 4:
                dictInfo['taskType'] = shotInfos[3]
        dictInfo['step_type'] = ''
        dictInfo['category'] = ''
        dictInfo['fileExt'] = shotInfos[-1].split('.')[-1]
        if dictInfo['taskType'] and dictInfo['taskType'] in self.simInfos:
            dictInfo['step_type'] = self.fullInfos[self.simInfos.index(dictInfo['taskType'])]
        dictInfo['task_typeFolder'] = dictInfo['step_type']
        dictInfo['assetID'] = dictInfo['asset']
        dictInfo['assetType'] = dictInfo['category']
        dictInfo['projFull'] = dictInfo['project']
        dictInfo['projSimp'] = dictInfo['showShortname']
        dictInfo['stepFull'] = dictInfo['step_type']
        dictInfo['stepSimp'] = dictInfo['taskType']
        if '.' in dictInfo['shotID']:
            dictInfo['shotID'] = dictInfo['shotID'].split('.')[0]
        return dictInfo

    # ??????camTemp?????????
    #???final???0 ?????????layout?????? | 1 ??????????????????????????????cam | 2 ????????????
    def checkServerCamPath(self,final = 1 ,camReturn = 0,shotInfos = []):
        if not shotInfos:
            shotInfos = self.checkShotInfo(0)
        shotType = self.checkShotType()
        if final == 1:
            info01 = shotInfos[0]
            info02 = '_cam.ma'
        else:
            info01 = 'cam'
            info02 = '_baked.ma'
        serverPath = self.checkProjectServerPath()
        fileDictInfo = self.checkGetShotDict(shotInfos)
        shotID = '%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2])
        if shotType == 3:
            shotID = '%s_%s'%(shotID,shotInfos[3])
        camBK = '%s%s'%(shotID.replace(shotInfos[0],info01),info02)
        serverCamPath = '%sscenes/Animation/episode_%s/episode_camera'%(serverPath,shotInfos[1])
        fileDictInfo['task_typeFolder'] = 'shots'
        projFull = serverPath.split('/')[-3]
        if final:
            camPath = serverCamPath + '/'
        else:
            camPath = serverPath.replace('Project/','%s_Scratch'%projFull) + "/TD/SetCam/" + shotInfos[1] + "/"
        if not os.path.exists(camPath):
            self.checkServerFileSystem('mdr',camPath)
        if camReturn:
            return (camPath + camBK)
        else:
            return (camPath)

    # ???????????????????????????
    def checkEnvPath2FullPath(self,envPath):
        import maya.cmds as mc
        fullPath = mc.workspace(expandName = envPath)
        return fullPath

    # ????????????project??????
    def checkProjectTDPath(self):
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        projectPathBase = self.checkProjectServerPath()
        projectServerPath = projectPathBase.replace('/Project/',('/' + project+'_scratch/TD/'))
        return projectServerPath

    # sourceImage ??????
    def checkAssetSourceImagesPath(self,shotInfos = []):
        if not shotInfos:
            shotInfos = self.checkShotInfo()
        projectPathBase = self.checkProjectServerPath()
        assetTypeFull = self.assetFullInfos[self.assetInfos.index(shotInfos[1][0].lower())]
        assetSourceiamgeFolderPath = '%s%s/%s/%s/'%(projectPathBase,self.sourceImgsFolder,assetTypeFull,shotInfos[1])
        return assetSourceiamgeFolderPath

    # ??????tex????????????
    def checkTexLocalPath(self):
        import maya.cmds as mc
        # mel???
        dirInfo = self.checkShotInfo()
        localPathTex = ('D:/Info_Temp/temp/texTemp/' + str(dirInfo[1]) + '/')
        mc.sysFile(localPathTex, makeDir=True)
        return localPathTex
    
    # ????????????tex????????????
    def checkTexServerPath(self):
        # mel???
        dirInfo = self.checkShotInfo()
        projectServerBase = self.checkProjectServerPath()
        serverPathTex = projectServerBase + 'data/AssetShader/' + str(dirInfo[1]) + '/'
        return serverPathTex
   
    # ??????tx2AnimRender??????
    def checkTX2AnimRenderLocalPath(self):
        import maya.cmds as mc
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/temp/tx2AnimRenderTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    # ??????render????????????
    def checkRenderLayerLocalPath(self,shotType = 2):
        import maya.cmds as mc
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/renderLayerFile/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            localPathCache = ('D:/Info_Temp/renderLayerFile/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    # ??????cache??????
    def checkCacheLocalPath(self,shotType = 2):
        import maya.cmds as mc
        # mel???
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/temp/geoCacheTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            localPathCache = ('D:/Info_Temp/temp/geoCacheTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    # ????????????cache??????
    def checkCacheServerPath(self,shotType = 2):
        # mel???
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        projectPathBase = self.checkProjectServerPath()
        serverPathCache=''
        p_crwd = re.compile(u'crowd[a-zA-Z1-9]*')
        if shotType == 2:
            serverPathCache = projectPathBase + 'data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/'
            if project in ['DiveollyDive5','ShunLiu','LION'] and p_crwd.search(dirInfo[3]):
                serverPathCache = (projectPathBase + '/data/CROWDS_CACHE/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            serverPathCache = (projectPathBase + 'data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        return serverPathCache

    # ??????cache??????
    def alembicLocalPath(self,shotType = 2):
        import maya.cmds as mc
        # mel???
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/temp/alembic/'+ dirInfo[0] + '/'+str(dirInfo[1]) + '/')
        if shotType == 2:
            localPathCache = ('D:/Info_Temp/temp/alembic/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            localPathCache = ('D:/Info_Temp/temp/alembic/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache

    # ????????????cache??????
    def alembicServerPath(self,shotType = 2):
        # mel???
        dirInfo = self.checkShotInfo()
        shotType = self.checkShotType()
        serverPathCache=''
        projectServerBas = self.checkProjectServerPath(stepMode='cache')
        if shotType == 1:
            serverPathCache = (projectServerBas + 'data/alembic/' + str(dirInfo[1]) + '/')
        if shotType == 2:
            serverPathCache = (projectServerBas + 'data/alembic/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            serverPathCache = (projectServerBas + 'data/alembic/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        return serverPathCache    
        
    # ??????anim??????
    def checkAnimLocalPath(self,shotType = 2,rebuild = 0):
        import maya.cmds as mc
        # python???
        animInfo = 'animInfoTemp'
        if rebuild:
            animInfo = 'animRebuild'
        shotInfo = self.checkShotInfo()
        localPathAnim = ('D:\\Info_Temp\\temp\\' + animInfo + '\\' + shotInfo[0] + '\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
        if shotType == 3:
            localPathAnim = ('D:\\Info_Temp\\temp\\' + animInfo + '\\' + shotInfo[0] + '\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\' + str(shotInfo[3]) + '\\')
        mc.sysFile(localPathAnim, makeDir=True)
        return localPathAnim

    # ????????????anim??????
    def checkAnimServerPath(self,shotType = 2,rebuild = 0):
        # python???
        animInfo = 'AnimInfo'
        if rebuild:
            animInfo = 'AnimRebuild'
        shotInfo = self.checkShotInfo()
        projectPathBase = self.checkProjectServerPath(typeMode=1)
        serverPathAnim=''
        if shotType == 2:
            serverPathAnim = (projectPathBase + 'data\\' + animInfo + '\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
        if shotType == 3:
            serverPathAnim = (projectPathBase + 'data\\' + animInfo + '\\'  + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\' + str(shotInfo[3]) + '\\')
        return serverPathAnim

    # ??????RenderLayerInfo??????
    def checkLayerInfoLocalPath(self,LayerType = 'RGB',layerName = 'myRGB'):
        import maya.cmds as mc
        # python???
        shotInfo = self.checkShotInfo()
        localPathAnim = ( 'D:\\Info_Temp\\Project_Render_Info\\' + shotInfo[0] + '\\' + LayerType + '\\' + layerName + '\\')
        mc.sysFile(localPathAnim, makeDir=True)
        return localPathAnim

    # ????????????RenderLayerInfo??????
    def checkLayerInfoServerPath(self,LayerType = 'RGB',layerName = 'myRGB'):
        # python???
        projectPathBase = self.checkProjectServerPath(typeMode=1)
        serverPathAnim = (projectPathBase + 'data\\RLayerInfo\\' + LayerType + '\\' + layerName + '\\')
        return serverPathAnim

    # ??????finalLayout??????
    def checkFinalLayoutLocalPath(self,shotType = 2):
        import maya.cmds as mc
        # mel???
        dirInfo = self.checkShotInfo()
        localPathFinalLayout = ('D:/Info_Temp/temp/finalLayoutTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            localPathFinalLayout = ('D:/Info_Temp/temp/finalLayoutTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        mc.sysFile(localPathFinalLayout, makeDir=True)
        return localPathFinalLayout
    
    # ????????????cache??????
    def checkFinalLayoutServerPath(self,shotType = 2):
        # mel???
        dirInfo = self.checkShotInfo()
        projectPathBase = self.checkProjectServerPath()
        serverPathFinalLayout = (projectPathBase + 'scenes/Animation/episode_' + str(dirInfo[1]) + '/' + 'scene_' + str(dirInfo[2]) + '/' + 'finishing/')
        if shotType == 3:
            serverPathFinalLayout = (projectPathBase + 'scenes/Animation/episode_' + str(dirInfo[1]) + '/' + 'sequence_' + str(dirInfo[2]) + '/' + 'scene_' + str(dirInfo[3]) + '/' + 'finishing/')
        return serverPathFinalLayout
    
    # ????????????camera??????
    def checkCameraServerPath(self,dirInfo = []):
        # mel???
        if not dirInfo:
            dirInfo = self.checkShotInfo()
        projectPathBase = self.checkProjectServerPath()
        ServerPathCamera = projectPathBase + 'scenes/Animation/episode_' + str(dirInfo[1]) + '/episode_camera/'
        return ServerPathCamera
    
    # ??????????????????ID
    def checkStrangeIDInfo(self):
        dataPath = self.checkProjectServerPath() + 'data/localAsset.txt'
        print dataPath
        strangeID = self.checkFileRead(dataPath)
        return strangeID

    # ???????????????
    def checkNumStrList(self):
        numStr = []
        for i in range(10):
            numStr.append(str(i))
        return numStr

    # ??????asset ?????????
    def checkAssetRootGrp(self,shotInfos = []):
        if not shotInfos:
            shotInfos = self.checkShotInfo()
        rootGrpList = ['CHR','PRO','SET']
        assetList   = ['c','p','s']
        assetType = shotInfos[1][0].lower()
        if assetType not in assetList:
            errorInfo = u'\n----------File Name Error ,please check----------'
            print errorInfo
            import maya.cmds as mc
            mc.error()
        rootGrp = rootGrpList[assetList.index(assetType)]
        return rootGrp

    '''
            ??????????????????asset???
    Author: ???  ???
    Data    :2013_11_18
    '''
    # ??????????????????asset?????????????????????????????????????????????
    def checkProjectAssetNames(self):
        import maya.cmds as mc
        shotInfo = self.checkShotInfo()

        projectPathBase = self.checkProjectServerPath(typeMode=1)

        prePath = projectPathBase + '\\scenes\\'

        charPath = prePath + 'characters\\'

        charAssets = mc.getFileList(  folder = charPath )
        if charAssets:
            if 'bak' in charAssets:
                charAssets.remove('bak')
        else:
            charAssets = []

        propPath = prePath + 'props\\'

        propAssets = mc.getFileList(  folder = propPath )
        if propAssets:
            if 'bak' in propAssets:
                propAssets.remove('bak')
        else:
            propAssets = []

        setPath = prePath + 'sets\\'

        setsAssets = mc.getFileList(  folder = setPath )
        if setsAssets:
            if 'bak' in setsAssets:
                setsAssets.remove('bak')
        else:
            setsAssets = []

        miscPath = prePath + 'misc\\'

        miscAssets = mc.getFileList(  folder = miscPath )
        if miscAssets:
            if 'bak' in miscAssets:
                miscAssets.remove('bak')
        else:
            miscAssets = []
        
        resultAsset = []
        resultAsset.append(charAssets + propAssets + setsAssets + miscAssets)
        resultAsset.append(charAssets)
        resultAsset.append(propAssets)
        resultAsset.append(setsAssets)
        resultAsset.append(miscAssets)
        return resultAsset

    # ???????????????????????????
    # ?????????????????????namespace??????????????????asset???namespace
    # checkType 0 all | 1 char | 2 prop | 3 sets
    def checkAsset2FileObjsConfig(self,checkType = 1):
        import maya.cmds as mc
        # ???????????????????????????namespace
        # shotInfo
        shotInfo = self.checkShotInfo()
        namespaceList = mc.namespaceInfo(listOnlyNamespaces=1)
        namespaceList.remove('UI')
        namespaceList.remove('shared')
        if namespaceList:
            # ????????????asset
            assetInfo = self.checkProjectAssetNames()
            allAsset = assetInfo[0]
            charAsset = assetInfo[1]
            propAsset = assetInfo[2]
            setsAsset = assetInfo[3]
            # ???????????????asset
            # ?????????????????????namespace??????????????????asset???namespace
            needInfo = []
            checkList = []
            if checkType == 0:
                checkList = allAsset
            if checkType == 1:
                checkList = charAsset
            if checkType == 2:
                checkList = propAsset
            if checkType == 3:
                checkList = setsAsset
            if checkList:
                for assetID in checkList:
                    checkNs = 0
                    for ns in namespaceList:
                        if checkNs:
                            break
                        else:
                            if assetID in ns:
                                needInfo.append([ns,(shotInfo[0] + '_' + assetID)])
                                checkNs = checkNs + 1
                #needInfo = list(set(needInfo))
                return needInfo

    # ??????shotType
    # ???????????????,???sk_infoConfig??????,????????????????????????????????????
    def checkShotType(self,fileName = ''):
        if not fileName:
            import maya.cmds as mc
            fileName = mc.file(exn=1,q=1).split('/')[-1]
        shotInfos = fileName.split('/')[-1].split('_')
        shotType = 2
        if shotInfos[0] in self.shotType3Projs:
            shotType = 3
        return shotType

    # ????????????rgmode
    def checkRgMode(self,fileName = ''):
        if not fileName:
            import maya.cmds as mc
            fileName = mc.file(exn=1,q=1).split('/')[-1]
        shotInfos = fileName.split('_')
        rgMode = 0
        if shotInfos[0] in self.rgModeProjs:
            rgMode = 1
        return rgMode

    # ??????sgState
    def checkSGState(self,projSimp = ''):
        if not projSimp:
            import maya.cmds as mc
            fileName = mc.file(exn=1,q=1).split('/')[-1]
            shotInfos = fileName.split('_')
            projSimp = shotInfos[0]
        else:
            if '_' in projSimp:
                projSimp = projSimp.split('_')[0]
        sgState = 0
        return sgState

    #-----------------------------#
    # ???????????????????????????????????????
    # 0.??????
    # Author: ???  ???
    # Data    :2013_06_4
    #-----------------------------#
    def checkProjectNameSimple2Full(self, simple):
        full = ''
        if simple == 'zm':
            full = 'ZoomWhiteDolphin'
        if simple == 'zo':
            full = 'Zorro'
        if simple == 'cl':
            full = 'Calimero'
        if simple == 'hf':
            full = 'HeroFactory'
        if simple == 'do4':
            full = 'DiveollyDive4'
        if simple == 'do6':
            full = 'DiveollyDive6'
        if simple == 'ddz':
            full = 'DouDiZhu'
        if simple == 'csl':
            full = 'ShunLiu'
        if simple == 'sk':
            full = 'Strawberry'
        if simple == 'yd':
            full = 'YODA'
        if simple == 'nj':
            full = 'Ninjago'
        if simple == 'do5':
            full = 'DiveollyDive5'
        if simple == 'yt':
            full = 'YongTai'
        if simple == 'ice':
            full = 'North'
        if simple == 'nj':
            full = 'Ninjago'
        if simple == 'tf':
            full = 'ToothFairies'
        if simple == 'Yak':
            full = 'YAK'
        if simple == 'ddz':
            full = 'DouDiZhu'
        if not full:
            import maya.mel as mel
            full = mel.eval('zwGetProject(\"%s\")'%simple)
        return full


    def checkProjectNameFull2Simple(self, full):
        simple = ''
        if full == 'ZoomWhiteDolphin':
            simple = 'zm'
        if full == 'Zorro':
            simple = 'zo'
        if full == 'Calimero':
            simple = 'cl'
        if full == 'HeroFactory':
            simple = 'hf'
        if full == 'DiveollyDive4':
            simple = 'do4'
        if full == 'DiveollyDive6':
            simple = 'do6'
        if full == 'DouDiZhu':
            simple = 'ddz'
        if full == 'ShunLiu':
            simple = 'csl'
        if full == 'sk':
            simple = 'Strawberry'
        if full == 'YODA':
            simple = 'yd'
        if full == 'Ninjago':
            simple = 'nj'
        if full == 'DiveollyDive5':
            simple = 'do5'
        if full == 'YongTai':
            simple = 'yt'
        if full == 'North':
            simple = 'ice'
        if full == 'YAK':
            simple = 'Yak'
        if not simple:
            import maya.mel as mel
            simple = mel.eval('zwGetProjectShort(\"%s\")'%full)
        return simple
    
    def checkProjectAudioPath(self, full):
        audioPath = ''
        if full == 'ZoomWhiteDolphin' or full == 'zm':
            audioPath = 'zm'
        if full == 'Zorro' or full == 'zo':
            audioPath = 'zo'
        if full == 'Calimero' or full == 'cl':
            audioPath = 'CA'
        if full == 'HeroFactory' or full == 'hf':
            audioPath = 'hf'
        if full == 'DiveollyDive4' or full == 'do4':
            audioPath = 'do4'
        if full == 'DiveollyDive6' or full == 'do6':
            audioPath = 'do6'
        if full == 'DouDiZhu' or full == 'ddz':
            audioPath = 'ddz'

        if full == 'ShunLiu' or full == 'csl':
            audioPath = 'csl'
        if full == 'Strawberry' or full == 'sk':
            audioPath = 'sk'
        if full == 'YODA' or full == 'yd':
            audioPath = 'yd'
        if full == 'Ninjago' or full == 'nj':
            audioPath = 'nj'
        if full == 'DiveollyDive5' or full == 'do5':
            audioPath = 'do5'
        if full == 'North' or full == 'ice':
            audioPath = 'ice'
        if full == 'YAK':
            audioPath = 'Yak'
        if not audioPath:
            import maya.mel as mel
            audioPath = mel.eval('zwGetProjectShort(\"\")')
        return audioPath

    def checkProjectStartFrame(self, full):
        startFrame = 1001
        if full == 'Zorro' or full == 'zo':
            startFrame = 101
        if full == 'Calimero' or full == 'cl':
            startFrame = 1
        if full == 'HeroFactory' or full == 'hf':
            startFrame = 101
        if full == 'DiveollyDive4' or full == 'do4':
            startFrame = 101
        return startFrame
    
    def checkProjectFileFormat(self, pro,finalLayout = 0,shotInfo = []):
        if not shotInfo:
            shotInfo = self.checkShotInfo()
        # ????????????
        fileType = '.mb'
        maList = ['cl']
        if pro in maList:
            fileType = '.ma'
        # ????????????
        if shotInfo[3] in ['ly','an','sd','dy','ef','fs']:
            maList = ['cl','do4','mk','mtd']
            if pro in maList:
                fileType = '.ma'
            else:
                fileType = '.mb'
        if shotInfo[3] in ['lr']:
            fileType = '.mb'
        if finalLayout:
            fileType = '.ma'
        return fileType
    
    def checkProjectFileFormatFull(self, pro,finalLayout = 0):
        fileType = self.checkProjectFileFormat(pro)
        fileTypeFull = ''
        if fileType == '.ma':
            fileTypeFull = 'mayaAscii'
        if fileType == '.mb':
            fileTypeFull = 'mayaBinary'
        if finalLayout:
            fileTypeFull = 'mayaAscii'
        return fileTypeFull
    
    # ??????????????????
    def checkBaseAttrs(self,infoType = 0):
        attrs = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
        if infoType == 0:
            return attrs
        if infoType == 't':
            return  ['.tx','.ty','.tz']
        if infoType == 'r':
            return  ['.rx','.ry','.rz']
        if infoType in ['s', 'S']:
            return  ['.sx','.sy','.sz']

    # ????????????camera ????????????
    # shapeH  ,ShapeW ,overscan,Ratio,goldLineLineScale,goldlLineCircleScale
    # [0.825  ,0.346  ,1.1     ,1    ,1                ,1                  ]
    def checkProjCamSetting(self,projSimp,shotScene = '001'):
        resInfos = [1.417,0.945,1.3,1 ,1  ,1 ]
        return resInfos

    def path2L(self, path):
        pathPattern = re.compile('//file-cluster/GDC/|Z:/', re.IGNORECASE)
        return re.sub(pathPattern, 'L:/', path)

    #?????????================
    def checkFileRead(self, path):
        import os 
        if not os.path.exists(path):
            print path
            print u'Error:    file do not exist'
            import maya.cmds as mc
            mc.error(u'Error:    file do not exist')
        # path = self.path2L(path) 
        print '=' * 30 + ' Start Reading IDP info file ' + '=' * 30
        print path
        print '=' * 100

        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            #print path
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0]) # add  replace ????????????????????????????????? by zhangben 20160223
            else:
                result.append(info)
        return result
    
    #?????????================
    def checkFileWrite(self, path , info , addtion=0 , lineKey = '\r\n'):
        if addtion == 1:
            info = self.checkFileRead(path) + info
        #txt = open(path, 'w')
        try:
            txt = open(path,'w')
        except:
            print '----------'
            print path
            txt = open(path,'w')
        mayaState = 0
        mayaVersion = 0
        try:
            import maya.cmds as mc
            mayaState = 1
        except:
            pass
        if mayaState:
            mayaVersion = int(mc.about(v=1)[:4])
        try:
            # maya??????
            if mayaState:
                # maya 2016??????,???str(unicode)??????
                if mayaVersion >= 2016:
                    for a in info:
                        txt.write(u'%s%s'%(a,lineKey))
                else:
                    txt.writelines(str(a) + lineKey for a in info)
            # ???maya
            else:
                txt.writelines(str(a) + lineKey for a in info)
            print('Writing........')
        finally:
            txt.close()

    #-------------------------#
    # json???
    def writeDict(self,path,data):
        import json
        f = open(path, 'w')
        json_data = json.dumps(data)
        f.write(json_data)
        f.close()

    #-------------------------#
    # json???
    def readDict(self,path):
        import json
        f = open(path, 'r')
        data = json.loads(f.read())
        f.close()
        return data

    #???excel?????????????????????
    def checkExcelRead(self,path, SHEETS = 0  ):
        import xlrd
        data = xlrd.open_workbook(path)
        table = data.sheets()[SHEETS] 
        #nrows = table.nrows
        #ncols = table.ncols
        #rowInfo = table.row_values(num)
        return table

    #--------------------------------#
    # ????????????????????? 1 fetchone | 2 fetchall
    def checkReadServerData(self,checkInfo = '',shotInfo = [],cmd_name = '',returnAll = 0):
        if not shotInfo:
            shotInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(shotInfo[0])
        
        import pyodbc
        # ???????????????
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f'%(project))
        # ?????????????????????
        cursor = cnxn.cursor()
        # ???????????????
        #cmd_name = 'select isnull(TA.ic,\'0\') as ic from idmtPlex_DiveOllyDive5.dbo.TB_Asset TA where TA.asset_name=\'%s\''%(shotInfo[1])
        if not cmd_name:
            cmd_name = 'select isnull(TA.ic,\'0\') as ic from dbo.TB_Asset TA where TA.asset_name=\'%s\''%(shotInfo[1])
        needInfo=''
        # ?????????????????????
        try:
            if returnAll in [0,1]:
                data = cursor.execute(cmd_name).fetchone()
            if returnAll in [2]:
                data = cursor.execute(cmd_name).fetchall()
            if returnAll:
                return data
            # ????????????
            if data:
                needInfo = int(str(data).split('\'')[1].split('\'')[0])
        # ????????????
        finally:
            cursor.close()
            cnxn.close()

        return needInfo

    #------------------------------------#
    # ???????????????
    #-----------------------#
    def checkServerConnect(self,project):
        import pyodbc
        # ???????????????
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f'%(project))
        # ?????????????????????
        return cnxn

    #--------------------------------#
    # ????????????????????? ?????????????????????
    def checkReadShotCamData(self,shotInfo=[]):
        if not shotInfo:
            shotInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(shotInfo[0])

        import pyodbc
        # ???????????????
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f'%(project))
        # ?????????????????????
        cursor = cnxn.cursor()
        # ???????????????
        #cmd_name = 'select isnull(TA.ic,\'0\') as ic from idmtPlex_DiveOllyDive5.dbo.TB_Asset TA where TA.asset_name=\'%s\''%(shotInfo[1])
        cmd_name = 'SELECT ISNULL(pcpe_edit6, \'\') FROM tb_PageColumnProjectEdit INNER JOIN TB_Anim_Task ON tb_PageColumnProjectEdit.pcpe_tasktype = \'anim\' AND tb_PageColumnProjectEdit.pcpe_taskid = TB_Anim_Task.task_id INNER JOIN TB_Anim ON TB_Anim_Task.anim_id = TB_Anim.anim_id WHERE TB_Anim.anim_ep = \'%s\' AND TB_Anim.anim_sc = \'%s\'' % (shotInfo[1], shotInfo[2])
        needInfo=''
        # ?????????????????????
        try:
            data = cursor.execute(cmd_name).fetchone()
            # ????????????
            if data:
                needInfo = data[0]
        # ????????????
        finally:
            cursor.close()
            cnxn.close()

        return needInfo

    #--------------------------------#
    # ???????????????????????????
    def checkGetDataStereoMode(self,shotInfo = []):
        if not shotInfo:
            shotInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(shotInfo[0])

        import pyodbc
        # ???????????????
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f'%(project))
        # ?????????????????????
        cursor = cnxn.cursor()
        # ???????????????
        cmd_name = 'SELECT ISNULL(pcpe_edit6, \'\') FROM tb_PageColumnProjectEdit INNER JOIN TB_Anim_Task ON tb_PageColumnProjectEdit.pcpe_tasktype = \'anim\' AND tb_PageColumnProjectEdit.pcpe_taskid = TB_Anim_Task.task_id INNER JOIN TB_Anim ON TB_Anim_Task.anim_id = TB_Anim.anim_id WHERE TB_Anim.anim_ep = \'%s\' AND TB_Anim.anim_sc = \'%s\'' % (shotInfo[1], shotInfo[2])
        needInfo=''
        # ?????????????????????
        try:
            data = cursor.execute(cmd_name).fetchone()
            # ????????????
            if data:
                needInfo = data[0]
        finally:
            # ????????????
            cursor.close()
            cnxn.close()

        return needInfo

    #--------------------------------#
    # ??????????????????,????????????nj??????
    def checkGetShotListFromTimeData(self,timeData = '',shotInfo = []):
        if not shotInfo:
            shotInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(shotInfo[0])

        import pyodbc
        # ???????????????
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f'%(project))
        # ?????????????????????
        cursor = cnxn.cursor()
        # ???????????????
        cmd_name = 'select VSS.anim_ep,VSS.Tag,VSS.anim_sc,VSS.unfixed7,VSS.[mark] from idmtPlex_%s.dbo.View_SsomGetAnimStatus VSS where VSS.unfixed7=\'%s\' and VSS.mark=\'Y\''%(project,timeData)
        needInfo=[]
        # ?????????????????????
        try:
            data = cursor.execute(cmd_name).fetchall()
            # ????????????
            if data:
                for checkData in data:
                    shotID = '%s_%s_%s_%s'%(shotInfo[0],checkData.anim_ep,checkData.Tag,checkData.anim_sc)
                    needInfo.append(shotID)
        finally:
            # ????????????
            cursor.close()
            cnxn.close()

        return needInfo

    #--------------------------------#
    # ????????????????????????
    def checkErrorWindows(self,errorInfo ,errorPerform = 1):
        import maya.cmds as mc
        if mc.window ("ass_errorWindows", ex=1):
            mc.deleteUI("ass_errorWindows", window=True)
        mc.window('ass_errorWindows' , title = 'ass_errorWindows',width=150 , height = 50 )
        mc.columnLayout( adjustableColumn=True )
        mc.text( label=u'===!!!Error!!!===' )
        mc.text( label='')
        mc.text( label=errorInfo, align='center' )
        mc.text( label='')
        mc.button(label = 'I Know',c = 'import maya.cmds as mc\nmc.deleteUI(\"ass_errorWindows\", window=True)')
        mc.showWindow()

        if errorPerform:
            print '\n'
            print errorInfo

    # --------------------------------#
    # ??????????????????copy??????
    def checkServerFileSystem(self,cmdType = 'copy',sourcePath = '', targetPath = ''):
        import maya.mel as mel
        # ??????
        if cmdType in ['copy']:
            melCmd = 'zwSysFile "copy" ' + '"' + sourcePath + '"' + ' ' + '"' + targetPath + '"' + ' true'
            mel.eval(melCmd)
        # ?????????
        if cmdType in ['xcopy']:
            melCmd = 'zwSysFile "xcopy" ' + '"' + sourcePath + '"' + ' ' + '"' + targetPath + '"' + ' true'
            mel.eval(melCmd)
        # ????????????
        if cmdType in ['mdr','makeDir']:
            melCmd = 'zwSysFile "md" ' + '"' + sourcePath + '" ""' + ' true'
            mel.eval(melCmd)
        # ??????
        if cmdType in ['del','delete']:
            melCmd = 'zwSysFile "del" ' + '"' + sourcePath + '" ""' + ' true'
            mel.eval(melCmd)

    #---------------------------------#
    # ??????????????????
    def checkNum2Version(self,vNum,rangeNum):
        version = ''
        for idNum in range(rangeNum):
            version += str(int(vNum/pow(10,(rangeNum-idNum-1))))[-1]
        return version
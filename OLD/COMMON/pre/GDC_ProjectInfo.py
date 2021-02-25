# -*- coding: utf-8 -*-

'''
Created on 2015-7-13

@author: hanhong

usage:
import GDC_ProjectInfo as gdcPI
gdcPI.checkProjectName('nj')

'''
#sys.path.insert(0,'E:/GIT/GDC_Repository')
import maya.cmds as mc

import maya.mel as mel

import re,os

class GDC_ProjectInfo(object):
    def __init__(self):
        # namespace清理
        pass


    #-----------------------------#
    # 【通用：项目全称简写转换】
    #
    # Author: hanhong
    # Data    :2015_07_13
    #
    #-----------------------------#
    def checkProjectName(self, name):
        simple=['cl','do4','hf','zo','zm','do5','ice','nj','csl']
        fullname=['Calimero','DiveollyDive4','HeroFactory','Zorro','ZoomWhiteDolphin','DiveollyDive5','North','Ninjago','ShunLiu']
        namen=''
        if name in simple and name not in fullname:
            for i in range(len(simple)):
                if simple[i]==name:
                    namen=fullname[i]
        if name in fullname and name not in simple:
            for i in range(len(simple)):
                if fullname[i]==name:
                    namen=simple[i]
        if name in fullname and name in simple:
            namen=name
        if name not in fullname and name not in simple:
            mc.error(u'项目名错误，请检查')
        return namen

#初始帧
    def checkProjectStartFrame(self, full):
        startFrame = ''
        if full == 'ZoomWhiteDolphin' or full == 'zm':
            startFrame = 1001
        if full == 'Zorro' or full == 'zo':
            startFrame = 101
        if full == 'Calimero' or full == 'cl':
            startFrame = 1
        if full == 'HeroFactory' or full == 'hf':
            startFrame = 101
        if full == 'DiveollyDive4' or full == 'do4':
            startFrame = 101
        if full == 'North' or full == 'ice':
            startFrame = 1001            
        return startFrame

    def checkShotInfo(self):
        temp = (mc.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
        else:
            #mc.warning(unicode('========================【！！！文件名不规范！！！】========================', 'utf8'))
            mc.warning(u'========================【！！！文件名不规范！！！】========================')
        return info                                    
    
    # 获取本地文件路径
    def checkPCFilePath(self):
        filePath = (mc.file(query=1, exn=1)).split('/')
        path = ''
        if filePath[0] != 'Z' and filePath[0] != '':
            for i in range(len(filePath) - 1):
                path = path + filePath[i] + '\\'
        return path

    # 获取shotType
    # 有场的情况,由sk_infoConfig控制,其他工具走查询数据库系统
    def checkShotType(self,fileName = ''):
        if not fileName:
            import maya.cmds as mc
            fileName = mc.file(exn=1,q=1).split('/')[-1]
        shotInfos = fileName.split('_')
        shotType = 2
        if shotInfos[0] in self.shotType3Projs:
            shotType = 3
        return shotType

    '''
            【通用：'/'转'\\'】
            非 网络地址
    Author: 沈  康
    Data    :2013_09_16
    '''
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
    # 万能版路径查询，以后可改成此方案
    # 沈康 2016.5
    #----------------------------------#
        #-----------------------------------------#
    # infoMode 通用
    # ShotInfo : 1 data/ShotShaderInfo  | 2 data/AbcCache | 3 dyCacheFolder | 4 vfxCacheFolder | 5 camInfoOutInfo |
    #            6 animCleanTemp        | 7 fxAbcCache    | 8 camAbc        | 9 lightInfo
    def checkShotDataInfoPath(self,server = 0,infoMode = 1,shotInfos = []):
        infoKey = ''
        if server:
            pathBase = self.checkProjectServerPath()
        else:
            pathBase = self.checkLocalInfoPath()
        if not shotInfos:
            shotInfos = self.checkShotInfo()
        shotType = self.checkShotType(shotInfos[0])
        #print '------------pathBase'
        #print pathBase

        if infoMode == 0:
            infoKey = 'GeoCache'
        if infoMode == 1:
            infoKey = 'ShotShaderInfo'
        if infoMode == 2:
            infoKey = 'AbcCache'
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

        shotFolder = '%s/%s'%(shotInfos[1],shotInfos[2])
        if shotType == 3:
            shotFolder = '%s/%s/%s'%(shotInfos[1],shotInfos[2],shotInfos[3])
        needPathShot = '%sdata/%s/%s'%(pathBase,infoKey,shotFolder)

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
        shotType = self.checkShotType(shotInfos[0])

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
        if shotType == 3:
            assetFolder = '%s/%s/%s'%(shotInfos[1],shotInfos[2],shotInfos[3])

        needPathShot = '%sdata/%s/%s/'%(pathBase,infoKey,assetFolder)

        if not server and not os.path.exists(needPathShot):
            os.makedirs(needPathShot)
        return needPathShot

    '''
            【通用：路径更改地址】
    0.通用
    Author: 沈  康
    Data    :2013_06_10
    UPData    :韩虹 2015_08_25
    '''
    # 本地infot路径
    def checkLocalInfoPath(self):
        localInfoPath = ('D:/Info_Temp/temp/')
        mc.sysFile(localInfoPath, makeDir=True)
        return localInfoPath
    
    # 服务器端project路径
    def checkProjectServerPath(self):
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        projectServerPath=''
        if project=='YongTai':
            projectServerPath = '//file-cluster/GDC/Projects/DomesticProject/' + project + '/Project/'
        elif project == 'DiveollyDive5'  or project == 'ShunLiu':
            projectServerPath = 'L:/Projects/' + project + '/Project/'
        else:
            projectServerPath = '//file-cluster/GDC/Projects/' + project + '/Project/'                        
        return projectServerPath

    # 服务器端project路径
    def checkProjectTDPath(self):
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        projectServerPath=''
        if project=='YongTai':
            projectServerPath = '//file-cluster/GDC/Projects/DomesticProject/' + project + '/'+project+'_scratch/TD/'
        elif project == 'DiveollyDive5'  or project == 'ShunLiu':
            projectServerPath = 'L:/Projects/' + project + '/Project/'
        else:
            projectServerPath = '//file-cluster/GDC/Projects/' + project + '/'+project+'_scratch/TD/'                      
        return projectServerPath   
    # 本地tex方案路径
    def checkTexLocalPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        localPathTex = ('D:/Info_Temp/temp/texTemp/' + str(dirInfo[1]) + '/')
        mc.sysFile(localPathTex, makeDir=True)
        return localPathTex
    
    # 服务器端tex方案路径
    def checkTexServerPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathTex=''
        if project=='YongTai':
            serverPathTex = ('//file-cluster/GDC/Projects/DomesticProject/' + project + '/Project/data/AssetShader/' + str(dirInfo[1]) + '/') 
        elif project == 'DiveollyDive5'  or project == 'ShunLiu':
            serverPathTex = ('L:/Projects/' + project + '/Project/data/AssetShader/' + str(dirInfo[1]) + '/')        
        else:
            serverPathTex = ('//file-cluster/GDC/Projects/' + project + '/Project/data/AssetShader/' + str(dirInfo[1]) + '/')        
        return serverPathTex
   
    # 本地tx2AnimRender路径
    def checkTX2AnimRenderLocalPath(self):
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/temp/tx2AnimRenderTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    # 本地render文件路径
    def checkRenderLayerLocalPath(self,shotType = 2):
        dirInfo = self.checkShotInfo()
        if shotType == 2:
            localPathCache = ('D:/Info_Temp/renderLayerFile/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            localPathCache = ('D:/Info_Temp/renderLayerFile/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    # 本地cache路径
    def checkCacheLocalPath(self,shotType = 2):
        # mel用
        dirInfo = self.checkShotInfo()
        if shotType == 2:
            localPathCache = ('D:/Info_Temp/temp/geoCacheTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            localPathCache = ('D:/Info_Temp/temp/geoCacheTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    # 服务器端cache路径
    def checkCacheServerPath(self,shotType = 2):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathCache=''
        p_crwd = re.compile(u'crowd[a-zA-Z1-9]*')
        if shotType == 2:
            if project=='YongTai':
                serverPathCache = ('//file-cluster/GDC/Projects/DomesticProject/' + project + '/Project/data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
            elif project == 'DiveollyDive5'  or project == 'ShunLiu':
                if p_crwd.search(dirInfo[3]): serverPathCache = ('L:/Projects/' + project + '/Project/data/CROWDS_CACHE/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
                else: serverPathCache = ('L:/Projects/' + project + '/Project/data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
            else:
                serverPathCache = ('//file-cluster/GDC/Projects/' + project + '/Project/data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            serverPathCache = ('//file-cluster/GDC/Projects/' + project + '/Project/data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        return serverPathCache

    # 本地cache路径
    def alembicLocalPath(self,shotType = 2):
        # mel用
        dirInfo = self.checkShotInfo()
        if shotType == 1:
            localPathCache = ('D:/Info_Temp/temp/alembic/'+ dirInfo[0] + '/'+str(dirInfo[1]) + '/')        
        if shotType == 2:
            localPathCache = ('D:/Info_Temp/temp/alembic/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            localPathCache = ('D:/Info_Temp/temp/alembic/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    # 服务器端cache路径
    def alembicServerPath(self,shotType = 2):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathCache=''
        p_crwd = re.compile(u'crowd[a-zA-Z1-9]*')
        if shotType == 1:
            serverPathCache = ('//file-cluster/GDC/Projects/' + project + '/Project/data/alembic/' + str(dirInfo[1]) + '/')
        if shotType == 2:
            if project=='YongTai':
                serverPathCache = ('//file-cluster/GDC/Projects/DomesticProject/' + project + '/Project/data/alembic/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
            else:
                serverPathCache = ('//file-cluster/GDC/Projects/' + project + '/Project/data/alembic/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            serverPathCache = ('//file-cluster/GDC/Projects/' + project + '/Project/data/alembic/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        return serverPathCache    
        
    # 本地anim路径
    def checkAnimLocalPath(self,shotType = 2):
        # python用
        shotInfo = self.checkShotInfo()
        if shotType == 2:
            localPathAnim = ('D:\\Info_Temp\\temp\\animInfoTemp\\' + shotInfo[0] + '\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
        if shotType == 3:
            localPathAnim = ('D:\\Info_Temp\\temp\\animInfoTemp\\' + shotInfo[0] + '\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\' + str(shotInfo[3]) + '\\')
        mc.sysFile(localPathAnim, makeDir=True)
        return localPathAnim

    # 服务器端anim路径
    def checkAnimServerPath(self,shotType = 2):
        # python用
        shotInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(shotInfo[0])
        serverPathAnim=''
        if shotType == 2:
            if project=='YongTai':
                serverPathAnim = ('\\\\file-cluster\\GDC\\Projects\\DomesticProject\\' + project + '\\Project\\data\\AnimInfo\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')  
            elif project == 'DiveollyDive5'  or project == 'ShunLiu':
                serverPathAnim = ('L:\\Projects\\' + project + '\\Project\\data\\AnimInfo\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')       
            else:
                serverPathAnim = ('\\\\file-cluster\\GDC\\Projects\\' + project + '\\Project\\data\\AnimInfo\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')       
        if shotType == 3:
            serverPathAnim = ('\\\\file-cluster\\GDC\\Projects\\' + project + '\\Project\\data\\AnimInfo\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\' + str(shotInfo[3]) + '\\')
        return serverPathAnim

    # 本地RenderLayerInfo路径
    def checkLayerInfoLocalPath(self,LayerType = 'RGB',layerName = 'myRGB'):
        # python用
        shotInfo = self.checkShotInfo()
        localPathAnim = ( 'D:\\Info_Temp\\Project_Render_Info\\' + shotInfo[0] + '\\' + LayerType + '\\' + layerName + '\\')
        mc.sysFile(localPathAnim, makeDir=True)
        return localPathAnim

    # 服务器端RenderLayerInfo路径
    def checkLayerInfoServerPath(self,LayerType = 'RGB',layerName = 'myRGB'):
        # python用
        shotInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(shotInfo[0])
        serverPathAnim=''

        if project=='YongTai':
            serverPathAnim = ('\\\\file-cluster\\GDC\\Projects\\DomesticProject\\' + project + '\\Project\\data\\RLayerInfo\\' + LayerType + '\\' + layerName + '\\') 
        elif project == 'DiveollyDive5'  or project == 'ShunLiu':
            serverPathAnim = ('L:\\Projects\\' + project + '\\Project\\data\\RLayerInfo\\' + LayerType + '\\' + layerName + '\\')        
        else:
            serverPathAnim = ('\\\\file-cluster\\GDC\\Projects\\' + project + '\\Project\\data\\RLayerInfo\\' + LayerType + '\\' + layerName + '\\')        
        
        return serverPathAnim

    # 本地finalLayout路径
    def checkFinalLayoutLocalPath(self,shotType = 2):
        # mel用
        dirInfo = self.checkShotInfo()
        if shotType == 2:
            localPathFinalLayout = ('D:/Info_Temp/temp/finalLayoutTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            localPathFinalLayout = ('D:/Info_Temp/temp/finalLayoutTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        mc.sysFile(localPathFinalLayout, makeDir=True)
        return localPathFinalLayout
    
    # 服务器端cache路径
    def checkFinalLayoutServerPath(self,shotType = 2):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathFinalLayout=''
        if shotType == 2:
            if project=='YongTai':
                serverPathFinalLayout = ('//file-cluster/GDC/Projects/DomesticProject/' + project + '/Project/scenes/Animation/' + 'episode_' + str(dirInfo[1]) + '/' + 'scene_' + str(dirInfo[2]) + '/' + 'finishing/')
            elif project == 'DiveollyDive5'  or project == 'ShunLiu':
                serverPathFinalLayout = ('L:/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + str(dirInfo[1]) + '/' + 'scene_' + str(dirInfo[2]) + '/' + 'finishing/')
            else:                
                serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + str(dirInfo[1]) + '/' + 'scene_' + str(dirInfo[2]) + '/' + 'finishing/')
        if shotType == 3:
            serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + str(dirInfo[1]) + '/' + 'sequence_' + str(dirInfo[2]) + '/' + 'scene_' + str(dirInfo[3]) + '/' + 'finishing/')
        return serverPathFinalLayout
    
    # 服务器端cache路径
    def checkCameraServerPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        ServerPathCamera=''
        #serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + dirInfo[1] + '/' + 'scene_' + dirInfo[2] + '/' + 'finishing/')
        if project=='YongTai':
            ServerPathCamera = "//file-cluster/GDC/Projects/DomesticProject/"+ project + "/Project/scenes/Animation/episode_" + str(dirInfo[1]) + "/episode_camera/"
        elif project == 'DiveollyDive5'  or project == 'ShunLiu':
            ServerPathCamera = "L:/Projects/"+ project + "/Project/scenes/Animation/episode_" + str(dirInfo[1]) + "/episode_camera/" 
        else:
            ServerPathCamera = "//file-cluster/GDC/Projects/"+ project + "/Project/scenes/Animation/episode_" + str(dirInfo[1]) + "/episode_camera/" 
        return ServerPathCamera
    
    # 特殊内部任务ID
    def checkStrangeIDInfo(self):
        dataPath = self.checkProjectServerPath() + 'data/localAsset.txt'
        print dataPath
        strangeID = self.checkFileRead(dataPath)
        return strangeID

    # 数字字符串
    def checkNumStrList(self):
        numStr = []
        for i in range(10):
            numStr.append(str(i))
        return numStr

    '''
            获取项目所有asset名
    Author: 沈  康
    Data    :2013_11_18
    '''
    # 第一个是全部asset，后面依次是角色、道具、场景类
    def checkProjectAssetNames(self):
        shotInfo = self.checkShotInfo()
        projectName = self.checkProjectNameSimple2Full(shotInfo[0])

        charPath=''
        #serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + dirInfo[1] + '/' + 'scene_' + dirInfo[2] + '/' + 'finishing/')
        if projectName=='YongTai':
            charPath =  ('\\\\file-cluster\\GDC\\Projects\\DomesticProject\\' + projectName + '\\Project\\scenes\\characters\\')
        elif projectName == 'DiveollyDive5'  or projectName == 'ShunLiu':
            charPath =  ('L:\\Projects\\' + projectName + '\\Project\\scenes\\characters\\')
        else:
            charPath =  ('\\\\file-cluster\\GDC\\Projects\\' + projectName + '\\Project\\scenes\\characters\\')
 
        charAssets = mc.getFileList(  folder = charPath )
        if charAssets:
            if 'bak' in charAssets:
                charAssets.remove('bak')
        else:
            charAssets = []

        propPath=''
        #serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + dirInfo[1] + '/' + 'scene_' + dirInfo[2] + '/' + 'finishing/')
        if projectName=='YongTai':
            propPath =  ('\\\\file-cluster\\GDC\\Projects\\DomesticProject\\' + projectName + '\\Project\\scenes\\props\\')
        elif projectName == 'DiveollyDive5'  or projectName  == 'ShunLiu':
            propPath =  ('L:\\Projects\\DomesticProject\\' + projectName + '\\Project\\scenes\\props\\')
        else:
            propPath =  ('\\\\file-cluster\\GDC\\Projects\\' + projectName + '\\Project\\scenes\\props\\')
        
        propAssets = mc.getFileList(  folder = propPath )
        if propAssets:
            if 'bak' in propAssets:
                propAssets.remove('bak')
        else:
            propAssets = []

        setPath=''
        #serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + dirInfo[1] + '/' + 'scene_' + dirInfo[2] + '/' + 'finishing/')
        if projectName=='YongTai':
            setPath =  ('\\\\file-cluster\\GDC\\Projects\\DomesticProject\\' + projectName + '\\Project\\scenes\\sets\\')
        elif projectName == 'DiveollyDive5'  or projectName  == 'ShunLiu':
            setPath =  ('L:\\Projects\\DomesticProject\\' + projectName + '\\Project\\scenes\\sets\\')
        else:
            setPath =  ('\\\\file-cluster\\GDC\\Projects\\' + projectName + '\\Project\\scenes\\sets\\')

        setsAssets = mc.getFileList(  folder = setPath )
        if setsAssets:
            if 'bak' in setsAssets:
                setsAssets.remove('bak')
        else:
            setsAssets = []
            
        propPath=''
        #serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + dirInfo[1] + '/' + 'scene_' + dirInfo[2] + '/' + 'finishing/')
        if projectName=='YongTai':
            propPath =  ('\\\\file-cluster\\GDC\\Projects\\DomesticProject\\' + projectName + '\\Project\\scenes\\environments\\')
        elif projectName == 'DiveollyDive5'  or projectName  == 'ShunLiu':
            propPath =  ('L:\\Projects\\DomesticProject\\' + projectName + '\\Project\\scenes\\environments\\')
        else:
            propPath =  ('\\\\file-cluster\\GDC\\Projects\\' + projectName + '\\Project\\scenes\\environments\\')
        
        setsAssets = mc.getFileList(  folder = propPath )
        if setsAssets:
            if 'bak' in setsAssets:
                setsAssets.remove('bak')
        else:
            setsAssets = []
        
        propPath=''
        #serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + dirInfo[1] + '/' + 'scene_' + dirInfo[2] + '/' + 'finishing/')
        if projectName=='YongTai':
            propPath =  ('\\\\file-cluster\\GDC\\Projects\\DomesticProject\\' + projectName + '\\Project\\scenes\\misc\\')
        elif projectName == 'DiveollyDive5'  or projectName  == 'ShunLiu':
            propPath =  ('L:\\Projects\\DomesticProject\\' + projectName + '\\Project\\scenes\\misc\\')
        else:
            propPath =  ('\\\\file-cluster\\GDC\\Projects\\' + projectName + '\\Project\\scenes\\misc\\')
        
        miscAssets = mc.getFileList(  folder = propPath )
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

    # 文件内物体信息分析
    # 其一为文件内的namespace，其二为标准asset的namespace
    # checkType 0 all | 1 char | 2 prop | 3 sets
    def checkAsset2FileObjsConfig(self,checkType = 1):
        # 读取文件内所有非空namespace
        # shotInfo
        shotInfo = self.checkShotInfo()
        namespaceList = mc.namespaceInfo(listOnlyNamespaces=1)
        namespaceList.remove('UI')
        namespaceList.remove('shared')
        if namespaceList:
            # 获取所有asset
            assetInfo = self.checkProjectAssetNames()
            allAsset = assetInfo[0]
            charAsset = assetInfo[1]
            propAsset = assetInfo[2]
            setsAsset = assetInfo[3]
            # 处理匹配的asset
            # 其一为文件内的namespace，其二为标准asset的namespace
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


    
    
    def checkProjectFileFormat(self, pro):
        fileType = ''
        shotInfo = self.checkShotInfo()
        # 后期文件
        if shotInfo[3] in ['ly','an','sd','dy','ef','fs','lr']:
            maList = ['cl','do4']
            if pro in maList:
                fileType = '.ma'
            else:
                fileType = '.mb'
        # 前期文件
        else:
            maList = ['cl']
            if pro in maList:
                fileType = '.ma'
            else:
                fileType = '.mb'
        return fileType
    
    def checkProjectFileFormatFull(self, pro):
        fileType = self.checkProjectFileFormat(pro)
        fileTypeFull = ''
        if fileType == '.ma':
            fileTypeFull = 'mayaAscii'
        if fileType == '.mb':
            fileTypeFull = 'mayaBinary'
        return fileTypeFull
    
    # 基础属性信息
    def checkBaseAttrs(self,infoType = 0):
        attrs = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
        if infoType == 0:
            return attrs
        if infoType == 't':
            return  ['.tx','.ty','.tz']
        if infoType == 'r':
            return  ['.rx','.ry','.rz']
        if infoType == 's':
            return  ['.sx','.sy','.sz']

    #读文件================
    def checkFileRead(self, path):
        import os 
        if not os.path.exists(path):
            print path
            print u'Error:    file do not exist'
            mc.error(u'Error:    file do not exist')
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
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result
    
    #写文件================
    def checkFileWrite(self, path , info , addtion=0):
        if addtion == 1:
            info = self.checkFileRead(path) + info
        txt = open(path, 'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()
            
            
    #读excel表格，反馈数据
    def checkExcelRead(self,path, SHEETS = 0  ):
        import xlrd
        data = xlrd.open_workbook(path)
        table = data.sheets()[SHEETS] 
        #nrows = table.nrows
        #ncols = table.ncols
        #rowInfo = table.row_values(num)
        return table

    #--------------------------------#
    # 读取数据库信息
    def checkReadServerData(self,checkInfo = ''):
        shotInfo = self.checkShotInfo()  
        project = self.checkProjectNameSimple2Full(shotInfo[0])
        
        import pyodbc
        # 连接数据库
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f'%(project))
        # 数据库连接状态
        cursor = cnxn.cursor()
        # 数据库查询
        cmd_name = 'select isnull(TA.ic,\'0\') as ic from idmtPlex_DiveOllyDive5.dbo.TB_Asset TA where TA.asset_name=\'%s\''%(shotInfo[1])
        needInfo=''
        # 数据库返回数据
        
        data = cursor.execute(cmd_name).fetchone()
        # 处理数据
        if data:
            needInfo = int(str(data).split('\'')[1].split('\'')[0])
        # 关闭连接
        pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f'%(project)).close()

        return needInfo


GDC_ProjectInfo().checkProjectName('nj')


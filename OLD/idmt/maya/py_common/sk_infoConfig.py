# -*- coding: utf-8 -*-

'''
Created on 2013-8-1

@author: shenkang
'''

import maya.cmds as mc
import maya.mel as mel


class sk_infoConfig(object):
    def __init__(self):
        # namespace清理
        pass

    '''
            【通用：文件名检测】
    0.所有阶段通用
    1.检测文件名
    Author: 沈  康
    Data    :2013_05_16
    '''

    def checkShotInfo(self):
        temp = (mc.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
        else:
           mc.warning(u'========================【！！！文件名不规范！！！】========================')
        return info             #mc.warning(unicode('========================【！！！文件名不规范！！！】========================', 'utf8'))
                   
    
    # 获取本地文件路径
    def checkPCFilePath(self):
        filePath = (mc.file(query=1, exn=1)).split('/')
        path = ''
        if filePath[0] != 'Z' and filePath[0] != '':
            for i in range(len(filePath) - 1):
                path = path + filePath[i] + '\\'
        return path

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
                
    
    '''
            【通用：路径更改地址】
    0.通用
    Author: 沈  康
    Data    :2013_06_10
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
        if project=='LION':
            projectServerPath = 'L:/Projects/' + project + '/Project/'
        else:
            projectServerPath = '//file-cluster/GDC/Projects/' + project + '/Project/'
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
        serverPathTex = ('//file-cluster/GDC/Projects/' + project + '/Project/data/AssetShader/' + str(dirInfo[1]) + '/')
        return serverPathTex
   
    # 本地tx2AnimRender路径
    def checkTX2AnimRenderLocalPath(self):
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/temp/tx2AnimRenderTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    # 本地render文件路径
    def checkRenderLayerLocalPath(self):
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/renderLayerFile/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    # 本地cache路径
    def checkCacheLocalPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/temp/geoCacheTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    # 服务器端cache路径
    def checkCacheServerPath(self,shotType):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathCache=''
        if shotType==2:
            print '========================='
            if project=='LION':     
                serverPathCache = ('L:/Projects/' + project + '/Project/data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
            else:
                serverPathCache = ('//file-cluster/GDC/Projects/' + project + '/Project/data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType==3:
            serverPathCache = ('//file-cluster/GDC/Projects/' + project + '/Project/data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')        
        return serverPathCache
        
    # 本地anim路径
    def checkAnimLocalPath(self):
        # python用
        shotInfo = self.checkShotInfo()
        localPathAnim = ('D:\\Info_Temp\\temp\\animInfoTemp\\' + shotInfo[0] + '\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
        mc.sysFile(localPathAnim, makeDir=True)
        return localPathAnim

    # 服务器端anim路径
    def checkAnimServerPath(self):
        # python用
        shotInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(shotInfo[0])
        serverPathAnim = ('\\\\file-cluster\\GDC\\Projects\\' + project + '\\Project\\data\\AnimInfo\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
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
        serverPathAnim = ('\\\\file-cluster\\GDC\\Projects\\' + project + '\\Project\\data\\RLayerInfo\\' + LayerType + '\\' + layerName + '\\')
        return serverPathAnim

    # 本地finalLayout路径
    def checkFinalLayoutLocalPath(self,shotType=2):
        # mel用
        dirInfo = self.checkShotInfo()
        localPathFinalLayout=''
        if shotType==2:
            localPathFinalLayout = ('D:/Info_Temp/temp/finalLayoutTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType==3:
            localPathFinalLayout = ('D:/Info_Temp/temp/finalLayoutTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/'+str(dirInfo[3]) + '/')       
        mc.sysFile(localPathFinalLayout, makeDir=True)
        return localPathFinalLayout
    
    # 服务器端cache路径
    def checkFinalLayoutServerPath(self,shotType=2):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathFinalLayout=''
        if shotType==2:
            serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + str(dirInfo[1]) + '/' + 'scene_' + str(dirInfo[2]) + '/' + 'finishing/')
        if shotType==3:
            serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + str(dirInfo[1]) + '/' +'sequence_'+ str(dirInfo[2]) + '/'+'scene_' + str(dirInfo[2]) + '/' + 'finishing/')
        return serverPathFinalLayout
    
    # 服务器端cache路径
    def checkCameraServerPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        #serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + dirInfo[1] + '/' + 'scene_' + dirInfo[2] + '/' + 'finishing/')
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

        charPath =  ('\\\\file-cluster\\GDC\\Projects\\' + projectName + '\\Project\\scenes\\characters\\')
        charAssets = mc.getFileList(  folder = charPath )
        if charAssets:
            if 'bak' in charAssets:
                charAssets.remove('bak')
        else:
            charAssets = []

        propPath =  ('\\\\file-cluster\\GDC\\Projects\\' + projectName + '\\Project\\scenes\\props\\')
        propAssets = mc.getFileList(  folder = propPath )
        if propAssets:
            if 'bak' in propAssets:
                propAssets.remove('bak')
        else:
            propAssets = []

        propPath =  ('\\\\file-cluster\\GDC\\Projects\\' + projectName + '\\Project\\scenes\\sets\\')
        setsAssets = mc.getFileList(  folder = propPath )
        if setsAssets:
            if 'bak' in setsAssets:
                setsAssets.remove('bak')
        else:
            setsAssets = []
            
        propPath =  ('\\\\file-cluster\\GDC\\Projects\\' + projectName + '\\Project\\scenes\\environments\\')
        setsAssets = mc.getFileList(  folder = propPath )
        if setsAssets:
            if 'bak' in setsAssets:
                setsAssets.remove('bak')
        else:
            setsAssets = []
        
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
        import sk_checkCommon
        reload(sk_checkCommon)
        # shotInfo
        shotInfo = self.checkShotInfo()
        #sk_checkCommon.sk_checkTools().checkNamespaceCleanEmpty()
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

    '''
            【通用：项目简写转换全称】
    0.通用
    Author: 沈  康
    Data    :2013_06_4
    '''
    def checkProjectNameSimple2Full(self, simple):
        full = ''
        if simple in ['cl','do4','hf','zo','zm']:
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
            if simple == 'csl':
                full = 'ShunLiu'
            if simple == 'do5':
                full = 'DiveOllyDive5'
        else:
            full = mel.eval('zwGetProject(\"\")')
        #import maya.mel as mel
        #mel.eval('zwGetProject ""')    # 根据当前文件名
        #mel.eval('zwGetProject "cl_135_001"')
        #mel.eval('zwGetProject "cl"')
        return full
        
    def checkProjectNameFull2Simple(self, full):
        simple = ''
        if full in ['Calimero','DiveollyDive4','HeroFactory','Zorro','ZoomWhiteDolphin']:
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
            if full == 'ShunLiu':
                simple = 'csl'
        else:
            simple = mel.eval('zwGetProjectShort(\"\")')
        return simple
    
    def checkProjectAudioPath(self, full):
        audioPath = ''
        if full in ( ['cl','do4','hf','zo','zm'] + ['Calimero','DiveollyDive4','HeroFactory','Zorro','ZoomWhiteDolphin']):
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
            if full == 'ShunLiu' or full == 'csl':
                audioPath = 'csl'
        else:
            audioPath = mel.eval('zwGetProjectShort(\"\")')
        return audioPath
    
    
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
        return startFrame
    
    
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
        if infoType in ['s', 'S']:
            return  ['.sx','.sy','.sz']

    #读文件================
    def checkFileRead(self, path):
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
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
        #txt = open(path, 'w')
        try:
            txt = open(path,'w')
        except:
            print '----------'
            print path
            txt = open(path,'w')
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
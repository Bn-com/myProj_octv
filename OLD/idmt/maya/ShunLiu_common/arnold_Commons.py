# -*- coding: utf-8 -*-
# 【通用】【FinalLayout环节工具】
#  Author : 韩虹
#  Data   : 2014_06~2014_07
# import sys
# sys.path.append('D:\\food\pyp\common')


# Q:an标记是_an_还是_ca_
# A:_ct_an

# 关于proxy代理物体
# 原则就是，有高低模的，在材质没有做好的时候拼场景的，满足这两者任意一个条件的，必须做proxy.
# 其他的在场景里，你可以import，而不要用specialRef模式
# 缺少一个脚本，在设置上传之前自动将proxy层级关系设置正确

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
reload(sk_cacheFinalLayout)

class arnold_Commons(object):
    def __init__(self):
        # namespace清理
        pass
    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【arnold】【材质】【arnold 转换 lambert材质】（特效环节需求，只连color)


    def csl_shadeListRecord(self,shotType=2):
        SGNodes = mc.ls(type = 'shadingEngine')
        if SGNodes:
            if 'initialParticleSE' in SGNodes:
                SGNodes.remove('initialParticleSE')
            if 'initialShadingGroup' in SGNodes:
                SGNodes.remove('initialShadingGroup')
            if SGNodes:
                Shaders = []
                sgNote='SHD_headSG'
                for sgNode in SGNodes:
                    if mc.listConnections((sgNode + '.surfaceShader'),source = 1 , plugs = 0):
                        Shader = mc.listConnections((sgNode + '.surfaceShader'),source = 1,plugs = 0)[0]
                        if 'ai' in mc.nodeType(Shader):
                            Shaders.append(Shader)
                Shade=list(set(Shaders))
                print Shade
        ShadeLists = dict({})
        for shad in Shade:
            connecShade=mc.listConnections(shad,connections=1,destination=0,plugs=1)
            if connecShade:
                ShadeLists[shad] = connecShade
        self.csl_shadeListExport(ShadeLists,shotType)         
        return ShadeLists    
        
        
       

    def csl_shadeListExport(self,ShadeLists,shotType = 2):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        if shotType == 2:
            localShaderInfoPath = localPath + 'finalLayoutTemp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            localShaderInfoPath = localPath + 'finalLayoutTemp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        if shotType == 4:
            localShaderInfoPath = localPath + 'finalLayoutTemp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'+ str(shotInfo[4]) + '/'        
        ShadeKeys = ShadeLists.keys()
        allInfo = []
        for i in range(len(ShadeKeys)):
            if i == 0:
                allInfo = ShadeKeys + [u'********'] + ShadeLists[ShadeKeys[i]] + [u'--------']
            else:
                allInfo = allInfo  + ShadeLists[ShadeKeys[i]] + [u'--------']
        # 写
        fileInfo = 'TexShaderInfo.txt'
        mc.sysFile(localShaderInfoPath, makeDir=True)
        sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileWrite((localShaderInfoPath + fileInfo),allInfo)
        # 上传
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if shotType == 2:
            serverDataPath = serverPath + 'data/TexShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            serverDataPath = serverPath + 'data/TexShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localShaderInfoPath + fileInfo) + '"' + ' ' + '"' + (serverDataPath + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating ShotShaderInfo To Server]===传输[%s]完毕==='%fileInfo 
        
    def csl_RecordShadeImport(self,shotType=2):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if shotType == 1:
            serverDataPath = serverPath + 'data/TexShaderInfo/' + str(shotInfo[1]) + '/'       
        if shotType == 2:
            serverDataPath = serverPath + 'data/TexShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            serverDataPath = serverPath + 'data/TexShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        if shotType == 4:
            serverDataPath = serverPath + 'data/TexShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/' + str(shotInfo[4]) + '/'             
        fileInfo = 'TexShaderInfo.txt'
        allInfo = self.csl_checkFileRead(serverDataPath+fileInfo)
        # 分割点
        signKeyIndex = sk_cacheFinalLayout.sk_cacheFinalLayout().checkListSameAllIndex(allInfo,u'********')[0]
        signMeshSplitIndexList = sk_cacheFinalLayout.sk_cacheFinalLayout().checkListSameAllIndex(allInfo,u'--------')
        # 开始还原
        shadeLists = dict({})
        # 创建keys
        for i in range(signKeyIndex):
            shadeLists[allInfo[i]] = []
        # 每类创建
        for i in range(len(signMeshSplitIndexList)):
            if i == 0:
                meshNum = signMeshSplitIndexList[i] - signKeyIndex - 1
            else:
                meshNum = signMeshSplitIndexList[i] - signMeshSplitIndexList[i-1] - 1
            for j in range(meshNum):
                baseMeshIndex = signMeshSplitIndexList[i] - meshNum
                shadeLists[allInfo[i]].append(allInfo[baseMeshIndex + j])
        return shadeLists   
        
    def csl_checkFileRead(self,path):
        print u'>>>>>>[read]'
        #print path
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            txt.close()
        for i in range(len(fileContent)):
            if len(fileContent[i].split('\r\n')) > 1:
                temp = fileContent[i].split('\r\n')
                fileContent[i] = temp[0]
        return fileContent                                          
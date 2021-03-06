# -*- coding: utf-8 -*-

'''
Created on 2013-6-18

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_ProjectTools_ShunLiu(object):
    def __init__(self):
        pass

    #-------------#
    # 【后台】清理anim文件
    #-------------#
    def csl_rebuildClean(self , serverClean = 0 , norenderConfig = 0):
        # 开始处理
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        print u'====================多层namespace清理完毕===================='
        
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        
        # 检测ref
        #self.calimeroRefCheck('an',1)
        from idmt.maya.commonCore.core_mayaCommon import sk_animFileCheck
        reload(sk_animFileCheck)
        sk_animFileCheck.sk_animFileCheck().shotAssetRefCheck('an',1)
        
        print u'====================ref对比情况检测完毕===================='
        
        unload = 0
        result = u'[清理完毕]'
        if refNodes:
            for ref in refNodes:
                check = mc.referenceQuery(ref,isLoaded = 1)
                if check:
                    pass
                else:
                    unload = unload + 1
            if unload:
                result = result + u'|Ref Cleaned'
        
        print u'====================ref载入情况检测===================='
        '''
        shareNodes = mc.ls('sharedReferenceNode',type = 'reference')
        if shareNodes:
            print u'\n'
            print u'======本文件发现ShareNodes模式的参考，请修改为正常模式的参考======'
            print u'\n'
            mc.error(u'======本文件发现ShareNodes模式的参考，请修改为正常模式的参考======')
        '''
        print u'====================ShareNodes检测==================='
        
        sk_animFileCheck.sk_animFileCheck().shotAssetTextureCheck()
        
        print u'====================贴图信息情况检测===================='
        
        # 处理参考
        for i in range(len(refNodes)):
            refNode = refNodes[i]
            refPath = mc.referenceQuery(refNode, f=1)
            path = refPath.lower()
            # 最优先
            # 非标准参考转标准参考
            if '_c_h_ms_anim.mb' in path:
                newPath = path.replace('_c_h_ms_anim.mb','_h_ms_anim.mb')
                # 替换参考

                mc.file(newPath, loadReference = refNodes[i])
            # _ng_参考
            if '_ng_h_ms_anim.mb' in path:
                newPath = path.replace('_ng_h_ms_anim.mb','_h_ms_anim.mb')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
                
        print u'=====================参考修正完毕=====================' 
        
        sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig()
        
        print u'==================Ref Info 处理完毕=================='
        
        # FPS
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('FPS',3)
        # frame
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame',3)
        
        print u'=====================镜头标准化完毕=====================' 
        
        # 清理孙望参考
        # 处理参考
        for i in range(len(refNodes)):
            refNode = refNodes[i]
            print '-------------'
            print refNode
            refPath = mc.referenceQuery(refNode, f=1)
            path = refPath.lower()
            # 清理外部参考
            shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo() 
            if shotInfo[0]=='csl':
                if 'shunliu' not in path:
                    refExist = mc.referenceQuery(refPath,rfn=1)
                    mc.file(rfn=refExist , removeReference=1)
                # 转换参考
                if '/rigging/' in path:
                    newPath = path.replace('/rigging/','/master/')
                    newPath = newPath.replace('_rg.','_ms_anim.')
                    # 替换参考
                    mc.file(newPath, loadReference = refNodes[i])
                
        print u'====================参考整理完毕===================='

        print mc.ls(type='unknown')
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean(1)
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                if mc.ls(node):
                    mc.lockNode(node, l=0)
                    mc.delete(node)
        print mc.ls(type='unknown')
        
        print u'==================垃圾节点清理完毕=================='

        # 清理层和渲染层
        try:
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        except:
            print u'===请检查文件masterLayer，名字异常==='
            mc.error(u'===请检查文件masterLayer，名字异常===')

        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
        
        print u'=================显示层|渲染层处理完毕================='    
        
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        if shotInfo[0] in ['ice','mi']:    
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1,shotType = 2)
        else:
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1,shotType = 3)
                        
        print u'==================camera传输完毕=================='
        
        # mr插件检测
#        mrState = mc.pluginInfo('Mayatomr' , loaded = 1 , q = 1)
#        if mrState:
#            mrNodes = mc.ls(type='mentalrayGlobals')+ mc.ls(type='mentalrayItemsList') +mc.ls(type='mentalrayOptions')
#            if mrNodes:
#                print u'=====本文件 存在  MR 节点，请Export清理====='
#                mc.error(u'=====本文件 存在  MR 节点，请Export清理=====')
#            else:
#                try:
#                    mel.eval('unloadPlugin "Mayatomr"')
#                except:
#                    pass
#        print u'==================MR 加载检测完毕=================='
        
        # 处理组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)
        
        print u'=================outLiner重新分组================='  
  
    #------------------------------#
    # 前期用工具，修改非法字符系列
    #------------------------------#
    # 修改指定目录文件[梁宇]
    def checkFolderNameConfig(self, rootPath):
        noNeedSign = ['-',' ','(',')','{','}']
        fileName = ''
        folderList = mc.getFileList(folder= rootPath)
        if not folderList:
            return 0
        for folderPath in folderList:
            fileList =  mc.getFileList(folder= (rootPath + folderPath + '/'))
            if not fileList:
                continue
            for fileName in fileList:
                newName = fileName
                for sign in noNeedSign:
                    if sign in newName:
                        newName = newName.replace(sign,'_')
                mc.sysFile((rootPath + '/' + folderPath + '/' + fileName),rename = (rootPath + '/' + folderPath + '/' + newName))
            
            
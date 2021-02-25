# -*- coding: utf-8 -*-

'''
Created on 2013-6-18

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

class sk_clProjectTools(object):
    def __init__(self):
        #namespace清理
        pass
        
    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # 【UI篇】【前期】【CL临时工具集】
    #-----------------------------------------#
    # 项目专用工具集
    def sk_sceneUICLTempTools(self):
        # 窗口
        if mc.window ("sk_sceneUICLTempTools",ex=1):
            mc.deleteUI( "sk_sceneUICLTempTools", window=True )
        mc.window("sk_sceneUICLTempTools",title="Tools", widthHeight=(180, 260),menuBar=0)

        # 面板
        form = mc.formLayout()
        # 切换面板
        tabs = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
        
        # tab_前期临时工具集
        child1 = mc.rowColumnLayout()

        # 前期类
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===前期类===', 'utf8')))
        mc.setParent("..")   

        # 对比【anim】【render】差异
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('对比【anim】【render】差异', 'utf8')),c = 'from idmt.maya.Calimero import check_ctrl_name_between_anim_render\nreload(check_ctrl_name_between_anim_render)')
        mc.setParent("..")  

        # 清理【角色】【无用】材质
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('清理【角色】【无用】材质', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().calimeroTXClean()')
        mc.setParent("..")   

        # 模型RenderStats
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('模型【RenderStats】', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().sk_addRenderStats()')
        mc.setParent("..")   

        # 【王光伟】【贴图管理】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【王光伟】【贴图管理】', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().sk_sceneDisplayLayerObjects')
        mc.setParent("..")   
        
        
        # 【何浪】【tx->rg】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【何浪】【tx->rg】', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().sk_sceneTempCleanCalimeroTx2Rg')
        mc.setParent("..")   
        
        # 【参考路径转换】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【参考路径转换】', 'utf8')),c = 'from idmt.maya.Calimero import CalimeroReferencePathConfig')
        mc.setParent("..")     

        mc.setParent("..")
        
        # tab_动画临时工具集
        child2 = mc.rowColumnLayout()

        # 动画类
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===动画类===', 'utf8')))
        mc.setParent("..")   

        # 【选取】【头部】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【选取】【头部】', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().sk_getAnimHead()')
        mc.setParent("..")
        
        # 【隐藏眉毛】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('切换【隐藏】【眉毛】', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().sk_hideAnimEyeBrow()')
        mc.setParent("..")   

        # 【高清】【普通】【材质切换】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【高清】【普通】【材质切换】', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().calimeroTXModeTransform()')
        mc.setParent("..")

        # 【rg转anim】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【rg】转换【anim】', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().sk_calimeroRg2Anim()')
        mc.setParent("..")
        
        
        # 选取【Anim】转【Render】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0.2,0.7,0.7],label = (unicode('选取【Anim】转【Render】', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().calimeroAnimTest2RenderRef()')
        mc.setParent("..")
        
        # 【选取】保留【贴图】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0.2,0.7,0.7],label = (unicode('【选取】保留【贴图】', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().calimeroAnimTexturePlayblastConfig()')
        mc.setParent("..")
        
        # ！！！【角色归零】！！！
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0.5,0.7,0.2],label = (unicode('！【角色归零】！', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().calimeroCharBack20()')
        mc.setParent("..")

        # ！！！【增加鞋垫】！！！
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0.5,0.7,0.2],label = (unicode('！【增加鞋垫】！', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().calimeroFootNorenderConfig()')
        mc.setParent("..")
        
        
        # 【dkAnim】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0.2,0.2,0.2],label = (unicode('【DKAnim】数据导入', 'utf8')),c = 'cmd = r\'source "dkAnim-v0.7-.mel"\'\nmel.eval(cmd)\nmel.eval(\"dkAnim()\")')
        mc.setParent("..")
        
        
        mc.setParent("..")

        # tab_渲染临时工具集
        child3 = mc.rowColumnLayout()

        # 渲染类
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===渲染类===', 'utf8')))
        mc.setParent("..")   

        # 【anim】转【render】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【anim】转【render】', 'utf8')),c = 'from idmt.maya.py_common import sk_referenceConfig\nreload(sk_referenceConfig)\nsk_referenceConfig.sk_referenceConfig().calimeroLayout2Anim2Render(1)')
        mc.setParent("..")
        
        # 【整集】角色道具参考
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【整集】角色道具参考', 'utf8')),c = 'sk_calimeroProjectTools.sk_clProjectTools().calimeroRefEpisodeImport()')
        mc.setParent("..")
        
        # 【全自动】【renderLayer】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【全自动】【renderLayer】', 'utf8')),c = 'from idmt.maya.Calimero import sk_renderLayer_Calimero\nreload(sk_renderLayer_Calimero)\nsk_renderLayer_Calimero.clRLConfig().clRLAutoCreate()')
        mc.setParent("..")

        mc.setParent("..")
        
        mc.tabLayout( tabs, edit=True, tabLabel=((child1, unicode('前期集', 'utf8')), (child2, unicode('动画集', 'utf8')),(child3, unicode('灯光集', 'utf8'))) )
        
        mc.showWindow( "sk_sceneUICLTempTools" )
 

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # Calimero 前期用工具
    #-----------------------------------------#
    # 设置模型的渲染状态
    def sk_addRenderStats(self):
        objs = mc.ls(type = 'transform')
        for obj in objs:
            shape = mc.listRelatives(obj, pa=1 , ni=1 , s=1 , type='mesh' , f=1)
            mode = 0
            try:
                if shape:
                    mode = 1
            except:
                pass
            if mode == 1:
                mc.setAttr((shape[0] + '.castsShadows'),1)
                mc.setAttr((shape[0] + '.receiveShadows'),1)
                mc.setAttr((shape[0] + '.motionBlur'),1)
                mc.setAttr((shape[0] + '.primaryVisibility'),1)
                mc.setAttr((shape[0] + '.smoothShading'),1)
                mc.setAttr((shape[0] + '.visibleInReflections'),1)
                mc.setAttr((shape[0] + '.visibleInRefractions'),1)
                mc.setAttr((shape[0] + '.doubleSided'),1)
                

    #-----------------------------------------#
    # anim转render
    def sk_clAnim2Render(self):
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        #  清理
        sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
        # 处理参考
        for i in range(len(refPaths)):
            refPath = refPaths[i]
            path = refPath.lower()
            # 转换参考
            newPath = path.replace('_ms_anim.','_ms_render.')
            # 替换参考
            mc.file(newPath, loadReference = refNodes[i])


    #-----------------------------------------#
    # rg转anim
    def sk_calimeroRg2Anim(self):
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]

        # 处理参考
        for i in range(len(refPaths)):
            refPath = refPaths[i]
            path = refPath.lower()
            # 转换参考
            if '/rigging/' in path:
                newPath = path.replace('/rigging/','/master/')
                newPath = newPath.replace('_rg.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 转换参考
            if '/master/' in path and '_ms_render.' in path:
                newPath = newPath.replace('_ms_render.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # Calimero 清理工具
    #-----------------------------------------#
    # 手动清理
    def sk_rebuildClean(self , serverClean = 0):
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.py_common import sk_sceneConfig
        reload(sk_sceneConfig)
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        
        # 检测ref
        #self.calimeroRefCheck('an',1)
        
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
        
        sk_sceneConfig.sk_sceneConfig().sk_sceneNoRefNamespaceClean()
        
        print u'====================多层namespace清理完毕===================='
        
        # 强制显示眉毛
        
        self.sk_showAnimEyeBrow()
        
        print u'====================强制显示眉毛处理===================='
        '''
        # 清理鞋垫
        if mc.ls('*norender_foot_l'):
            mc.delete('*norender_foot_l')
        if mc.ls('*norender_foot_r'):
            mc.delete('*norender_foot_r')
        if mc.ls('*:*norender_foot_l'):
            mc.delete('*:*norender_foot_l')
        if mc.ls('*:*norender_foot_r'):
            mc.delete('*:*norender_foot_r')
        if mc.ls('TEMP_FEET_GRP'):
            mc.delete('TEMP_FEET_GRP')
    
        print u'====================鞋垫清理环节处理===================='
        '''
        # 清理孙望参考
        # 处理参考
        for i in range(len(refNodes)):
            refNode = refNodes[i]
            refPath = mc.referenceQuery(refNode, f=1)
            path = refPath.lower()
            # 清理外部参考
            if 'calimero' not in path:
            #if 'calimero' not in path or 'c:\\' in path or 'd:\\' in path or 'e:\\' in path:
                #if 'c:\\' in path or 'd:\\' in path or 'e:\\' in path:
                #    localRef = 1
                refExist = mc.referenceQuery(refPath,rfn=1)
                mc.file(rfn=refExist , removeReference=1)
            # 转换参考
            if '/rigging/' in path:
                newPath = path.replace('/rigging/','/master/')
                newPath = newPath.replace('_rg.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
                
        print u'====================参考整理完毕===================='
        
        
        # 开始处理
        from idmt.maya.py_common import sk_sceneConfig
        reload(sk_sceneConfig)
        #from idmt.maya.py_common import sk_infoConfig
        #reload(sk_infoConfig)
        #sk_sceneConfig.sk_sceneConfig().sk_sceneImportCameraAudioFrame()
        
        print u'=====================镜头标准化完毕=====================' 
        
        #mc.currentTime(mc.playbackOptions(min = 1,q = 1))
        # 清理插件
        try:
            mel.eval('unloadPlugin "finalRender"')
        except:
            pass      
        
        print u'=====================插件清理完毕=====================' 

        # 对norender层内物体进行处理
        layers = mc.ls(type = 'displayLayer')
        for layer in layers:
            layerLower = layer.lower()
            if layerLower == 'norender':
                objs = mc.editDisplayLayerMembers(layerLower, query=True )
                if objs:
                    for obj in objs:
                        try:
                            # 隐藏
                            mc.setAttr((obj+'.v'),0)
                        except:
                            # 判断属性连接
                            vcInfo = mc.connectionInfo((obj+'.v'),sourceFromDestination = 1)
                            if mc.ls(vcInfo):
                                mc.setAttr(vcInfo,0)
                            
                        
        print u'================norender层物体隐藏完毕================'                
        
        # 清理层和渲染层
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        # 尝试回到master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        sk_checkCommon.sk_checkTools().checkCleanDisplayLayers([],['norender'])
        sk_checkCommon.sk_checkTools().checkCleanRenderLayers()
        
        print u'=================显示层|渲染层清理完毕================='        

        # 处理组
        sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(2)
        
        print u'=================outLiner重新分组================='  
        
        #sk_checkCommon.sk_checkTools().sk_assetInfoUpdate([0,2],0)
        #print u'====================【assetInfo】【服务器端】【输出】完毕===================='
        
        # 判断VFX里
        if mc.ls('VFX_GRP'):
            mc.delete('Cluster_GRP')
        
        print u'=================VFX组信息保留完毕================='   
        
        # 处理K帧
        objs = mc.ls('*Facial_CTRL_FRAME',type = 'transform') + mc.ls('*:*Facial_CTRL_FRAME',type = 'transform') + mc.ls('*:*:*Facial_CTRL_FRAME',type = 'transform') 
        if objs:
            for obj in objs:
                # 判断是否nurbsCurve
                shape = mc.listRelatives(obj,c=1,type = 'nurbsCurve')
                if shape:
                    # 判断是否有twoDline_vis属性
                    if mc.objExists(obj+ '.twoDline_vis'):
                        # 判断该属性是否有K帧
                        if mc.ls((obj + '_twoDline_vis'),type = 'animCurve'):
                            try:
                                mc.delete(obj + '_twoDline_vis')
                                print (obj + '_twoDline_vis')
                            except:
                                print u'========%s清除不了========'%(obj + '_twoDline_vis')
        
        print u'==================twoDline_vis清理完毕=================='   
        
        #sk_sceneConfig.sk_sceneConfig().sk_sceneUnloadRefDel()
        
        #print u'==================未勾选参考清理完毕=================='
        
        #sk_sceneConfig.sk_sceneConfig().sk_sceneAssetNamespaceConfig()
        
        print u'==================Ref Info 处理完毕=================='
        
        sk_sceneConfig.sk_sceneConfig().sk_sceneCameraUpdate(1)
        print u'==================camera传输完毕=================='
        
        print mc.ls(type='unknown')
        sk_checkCommon.sk_checkTools().checkDonotNodeClean(1)
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                if mc.ls(node):
                    mc.lockNode(node, l=0)
                    mc.delete(node)
        print mc.ls(type='unknown')
        
        print u'==================垃圾节点清理完毕=================='
        
        return result

    #-----------------------------------------#
    # 批量处理
    def sk_rebuildFileSequence(self,mode = 0):
        # path
        dirPath = 'D:/export_temp/'
        files = mc.getFileList(folder = 'D:/export_temp/',filespec='*.ma')
        if files:
            mc.sysFile('D:/export_temp/OK/', makeDir=True)
            for myFile in files:
                # export mode
                if mode == 0:
                    mc.file((dirPath + myFile) ,force = 1, open = 1)
                    self.sk_rebuildFile(1,0)
                    
                # clean reference mode
                if mode == 1:
                    mc.file((dirPath + myFile) ,force = 1, open = 1,loadReferenceDepth='none')
                    # 清理孙望参考
                    from idmt.maya.py_common import sk_referenceConfig
                    reload(sk_referenceConfig)
                    refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
                    refPaths = refInfo[1][0]
                    
                    fix = 0
                    
                    for refPath in refPaths:
                        path = refPath.lower()
                        if 'calimero' not in path or 'c:\\' in path or 'd:\\' in path or 'e:\\' in path:
                            refExist = mc.referenceQuery(refPath,rfn=1)
                            mc.file(rfn=refExist , removeReference=1)
                            fix = 1
                    # 开始处理
                    from idmt.maya.py_common import sk_infoConfig
                    shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
                    shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
                    anim = idmt.pipeline.db.GetAnimByFilename(shot)
                    startFrame = anim.frmStart
                    endFrame = anim.frmEnd
                    fpsFrame = anim.fps
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
                        preStartFrame = startFrame - 0
                        mc.playbackOptions(animationStartTime=preStartFrame)
                        # 结束帧
                        mc.playbackOptions(max=endFrame)
                        # 结束预留
                        posEndFrame = endFrame + 0
                        mc.playbackOptions(animationEndTime=posEndFrame)
                           
                    mc.file(s=1)
                    
    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # Calimero 动画用工具
    #-----------------------------------------#
    # 点角色获取anim-head
    def sk_getAnimHead(self):
        # 对于没有顶级grp的
        rootGrp = mc.ls(sl=1,l=1)[0].split('|')[1]
        secondGrp = mc.ls(sl=1,l=1)[0].split('|')[2]
        if ':' in secondGrp:
            namespace = secondGrp.split(':')[0]
            # Cali类
            obj = '|' + rootGrp + '|' + secondGrp + '|' + namespace + ':DEFORMERS|'+  namespace + ':msh_head_2Dline_'
            # Cali类2d
            if mc.objExists(obj) == False:
                obj = '|' + rootGrp + '|' + secondGrp + '|' + namespace + ':DEFORMERS|'+  namespace + ':msh_head_2dline_'
            # head_DEFORMERS
            if mc.objExists(obj) == False:  
                obj =  '|' + rootGrp + '|' + secondGrp + '|' + namespace + ':DEFORMERS|'+ namespace + ':head_DEFORMERS|'+  namespace + ':msh_head_2Dline_'
            # head_DEFORMERS类2d
            if mc.objExists(obj) == False:  
                obj =  '|' + rootGrp + '|' + secondGrp + '|' + namespace + ':DEFORMERS|'+ namespace + ':head_DEFORMERS|'+  namespace + ':msh_head_2dline_'
            # FACIAL_DEFORMERS
            if mc.objExists(obj) == False:  
                obj = '|' +  rootGrp + '|' + secondGrp + '|' + namespace + ':DEFORMERS|'+ namespace + ':FACIAL_DEFORMERS|'+  namespace + ':msh_head_2Dline_'
            # FACIAL_DEFORMERS类2d
            if mc.objExists(obj) == False:  
                obj = '|' +  rootGrp + '|' + secondGrp + '|' + namespace + ':DEFORMERS|'+ namespace + ':FACIAL_DEFORMERS|'+  namespace + ':msh_head_2dline_'           
            # 处理smooth
            print obj
            mc.select(obj)   
            mc.setAttr((mc.listRelatives(obj,s=1)[0]+'.smoothLevel'),2)
        
    #-----------------------------------------#
    # 显示|隐藏眉毛
    def sk_hideAnimEyeBrow(self):
        #grps = mc.ls('msh_eyelash*',type = 'transform')
        grps = mc.ls('*:*brow_*',type = 'transform') + mc.ls('*:*eyelash_*',type = 'transform')
        needGrps = []
        # 剔除非render的模型
        if grps:
            for grp in grps:
                if '_geo|' in mc.ls(grp,l=1)[0].lower():
                    needGrps.append(grp)
                else:
                    mc.setAttr((grp+'.lodVisibility'),0)
        # 开始判断
        if needGrps:
            modeType = mc.getAttr(needGrps[0]+'.lodVisibility')
            for grp in needGrps:
                if modeType == 1:
                    try:
                        mc.setAttr((grp+'.lodVisibility'),0)
                    except:
                        pass
                else:
                    try:
                        mc.setAttr((grp+'.lodVisibility'),1)
                    except:
                        pass
         
    #-----------------------------------------#
    # 强制显示眉毛
    def sk_showAnimEyeBrow(self):
        #grps = mc.ls('msh_eyelash*',type = 'transform')
        grps = mc.ls('*:*brow_*',type = 'transform') + mc.ls('*:*eyelash_*',type = 'transform')
        needGrps = []
        # 剔除非render的模型
        if grps:
            for grp in grps:
                if '_geo|' in mc.ls(grp,l=1)[0].lower():
                    mc.setAttr((grp+'.lodVisibility'),1)
                    try:
                        mc.setAttr((grp+'.v'),1)
                    except:
                        pass
                else:
                    mc.setAttr((grp+'.lodVisibility'),0)
                    try:
                        mc.setAttr((grp+'.v'),0)
                    except:
                        pass
        
    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # Calimero 贴图转内部路径
    #-----------------------------------------#
    # 转贴图路径到GDC路径
    def sk_filePath2GDCPath(self):
        import os
        fileNodes = mc.ls(type = 'file')
        for node in fileNodes:
            path = mc.getAttr(node + '.fileTextureName')
            path = path.lower()
            if 'sourceimages' in path and 'cal_maya' in path or 'sourceimages' in path and 'cal_common_sync' in path:
                # 默认map
                fileType = '.map'
                cutInfo = path.split('sourceimages')[1].split('/')
                fileName = cutInfo[5].split('.')[0]
                needPath = cutInfo[0] + '/' + cutInfo[1] +  '/' + cutInfo[3] + '/' + fileName
                prePath = '//file-cluster/GDC/Projects/Calimero/Project/sourceimages'
                newPath = prePath + needPath + fileType
                fileE = os.path.exists(newPath)
                if not fileE:
                    # 再次tga
                    fileType = '.tga'
                    newPath = prePath + needPath + fileType
                    fileE = os.path.exists(newPath)
                    if not fileE:
                        # 最次png
                        fileType = '.png'
                        newPath = prePath + needPath + fileType
                mc.setAttr((node + '.fileTextureName'),newPath,type = 'string')
                
                #\Maya\ttCache\cal_server\projets\CALIMERO\CAL_COMMON_SYNC\sourceimages\SETS\SET_Theatre_Int\Theatre_Int\publish\cl_Theatre_Int_Ground_VHD_RGB

    '''
            临时给王光伟用的贴图管理
    '''   
    def sk_sceneDisplayLayerObjects(self):
        # 获取layers
        allDisplayLayaers = mc.ls(type = 'displayLayer')
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        # 开始本地路径
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        infoLocalPath = ('D:\\Info_Temp\\temp\\displayLayerInfoTemp\\' + shotInfo[0] + '\\' + shotInfo[1] + '\\')
        mc.sysFile(infoLocalPath, makeDir=True)
        sk_infoConfig.sk_infoConfig().checkFileWrite((infoLocalPath +  'displayLayerInfo.txt'),'')
        # 输出数据
        for layer in allDisplayLayaers:
            if 'defaultLayer' not in layer:
                temp = ['=====================================']
                sk_infoConfig.sk_infoConfig().checkFileWrite((infoLocalPath +  'displayLayerInfo.txt'),temp,1)
                layerinfo = []
                layerinfo.append(layer)
                sk_infoConfig.sk_infoConfig().checkFileWrite((infoLocalPath +  'displayLayerInfo.txt'),layerinfo,1)
                objects = mc.editDisplayLayerMembers(layer,q= 1)
                if objects:
                    sk_infoConfig.sk_infoConfig().checkFileWrite((infoLocalPath +  'displayLayerInfo.txt'),objects,1)
                temp = ['*************************************']
                sk_infoConfig.sk_infoConfig().checkFileWrite((infoLocalPath +  'displayLayerInfo.txt'),temp,1)
                
 
    '''
            临时给何浪用的清理工具,将小鸡的tx转成rg.......
    '''   
    def sk_sceneTempCleanCalimeroTx2Rg(self):
        # 清理层
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        sk_checkCommon.sk_checkTools().checkCleanDisplayLayers()
        sk_checkCommon.sk_checkTools().checkCleanRenderLayers()
        # 清理相机，灯光，其他等
        rootGrps = sk_checkCommon.sk_checkTools().checkOutlinerGroup()
        for grp in rootGrps:
            if 'CAM' in grp or 'LIGHT' in grp:
                mc.delete(grp)
        # 处理大环控制器
        grps = mc.ls('c_*',type = 'transform')
        for grp in grps:
            # 隐藏属性处理
            if mc.objExists((grp + '.tt_visibility')):
                pass
            else:
                # 客户需要的tt显示属性
                mc.addAttr(grp, ln='tt_visibility', at='enum', en='visible:hidden:primary_off')
                mc.setAttr(grp+'.tt_visibility', e=True, k=True)
                mc.setAttr(grp+'.visibility', k=False, cb=False)
                print '===============(%s)[tt_visibility]DONE!===============,%(str(grp))'
            # 对判断节点隐藏
            listNodes = mc.listConnections(grp,d=1)
            for node in listNodes:
                # 寻找判断节点
                if mc.nodeType(node) == 'condition':
                    # 寻找其连接节点
                    TempNodes = mc.listConnections(node,s=1)
                    for temp in TempNodes:
                        # 寻找default节点
                        if 'defaultRenderUtility' in temp:
                            # 获取目标连接属性
                            targetAttr = mc.connectionInfo((node+'.message'),destinationFromSource =1 )
                            if targetAttr:
                                # 断开
                                mc.disconnectAttr((node+'.message'),targetAttr)
                                break

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # Calimero 客户路径转GDC路径
    #-----------------------------------------#
    # 小鸡专用，客户路径转GDC路径
    # 原理：
    # M:/CAL_RSYNC/CAL_MAYA/scenes/PROPS/ep_106/PRP_Outdoor_ChairA_Child/publish/prp_outdoor_chaira_child_layout_000.ma
    # 取publish前方的数据作为GDC的KEY，再判断进角色还是道具还是Set类
    def calimeroPathToGDC(self,path = ''):
        #path = 'M:/CAL_RSYNC/CAL_MAYA/scenes/PROPS/ep_106/PRP_Outdoor_ChairA_Child/publish/prp_outdoor_chaira_child_layout_000.ma'
        # 获取大类型
        folderType = path.split('/')[-5]
        # 获取GDC关键字
        assetKey = path.split('/')[-3]
        # 获取环节名
        oldFileType = path.split('/')[-1].split('_')[-2]
        # 判断所属
        assetType = folderType
        if folderType == 'CHARACTERS' or folderType == 'characters':
            assetType = 'characters'
        # 判断道具
        if folderType == 'PROPS' or folderType == 'props':
            assetType = 'props'
        # 判断SET
        if folderType == 'SETS' or folderType == 'sets':
            assetType = 'sets'
        # layout阶段
        if oldFileType == 'layout':
            #fileType = 'mo'
            #circleType = 'model'
            fileType = 'ms_anim'
            circleType = 'master'
        if oldFileType == 'anim':
            fileType = 'ms_anim'
            circleType = 'master'
        if oldFileType == 'tx':
            fileType = 'tx'
            circleType = 'texture'
        if oldFileType == 'render':
            #fileType = 'ms_render'
            #circleType = 'master'
            fileType = 'ms_anim'
            circleType = 'master'
        # GDC路径
        pathGDC = '//file-cluster/GDC/Projects/Calimero/Project/scenes/' + assetType + '/' + assetKey + '/' + circleType +'/cl_' + assetKey + '_h_' + fileType + '.ma'
        print pathGDC
        return pathGDC

    #-----------------------------------------#
    # 小鸡专用，GDC路径转客户路径
    # 原理：
    # //file-cluster/GDC/Projects/Calimero/Project/scenes/characters/ADUA/master/cl_ADUA_h_ms_render.ma
    # 取publish前方的数据作为GDC的KEY，再判断进角色还是道具还是Set类
    # 同时注意2个要点
    # 1.要还原一个文件夹
    # 2.道具要归还集数
    # 无法还原：layout，缺px
    def calimeroPathToGA(self,path = ''):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        #path = '//file-cluster/GDC/Projects/Calimero/Project/scenes/characters/ADUA/master/cl_ADUA_h_ms_render.ma'
        # 获取大类型
        folderType = path.split('/')[-4]
        # 获取GDC关键字
        assetKey = path.split('/')[-3]
        # 获取环节名
        oldFileType = path.split('/')[-1]
        # 回来的大组
        addGrp = ''
        # 判断所属
        if folderType == 'CHARACTERS' or folderType == 'characters':
            assetType = 'characters'
            # 回来的大组
            addGrp = 'CHR_' + assetKey.split('_')[0]
            # 例外判断
            chrNeed = ['MOTHER_COT','mother_cot','MOTHER_POT','mother_pot']
            if '_' in assetKey:
                if assetKey in chrNeed:
                    addGrp = 'CHR_' + assetKey
        # 判断道具
        if folderType == 'PROPS' or folderType == 'props':
            assetType = 'props'
            # 该死的两层目录
            # 获取镜头信息
            shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            epNum = shotInfo[1]
            addGrp = 'ep_' + str(epNum) 

        # 判断SET
        if folderType == 'SETS' or folderType == 'sets':
            assetType = 'sets'
            # 回来的大组
            if '_Ext' in assetKey or '_Int' in assetKey or '_ext' in assetKey or '_int' in assetKey:
                # POS_类
                if 'POS_' in assetKey or 'pos_' in assetKey:
                    addGrp = assetKey
                # SET_类
                else:
                    addGrp = 'SET_' + assetKey
            # ENV_类
            if '_Ext' not in assetKey and '_Int' not in assetKey or '_ext' not in assetKey or '_int' not in assetKey:
                if 'Cyclo_' in assetKey or 'cyclo_' in assetKey:
                    addGrp = 'ENV_' + assetKey.split('_')[0] + '_' + assetKey.split('_')[1]
                    if assetKey == 'Cyclo_CityHall_Garden_Day':
                        addGrp = 'ENV_' + assetKey.split('_')[0] + '_' + assetKey.split('_')[1] + '_' + assetKey.split('_')[2]
                if 'Skydome_' in assetKey or 'skydome_' in assetKey:
                    addGrp = 'ENV_Skydome'
        
        # 文件名类型
        if '_ms_anim' in oldFileType:
            fileType = 'anim_000.ma'
        if '_ms_render' in oldFileType:
            fileType = 'render_000.ma'
        if '_mo' in oldFileType:
            fileType = 'mo_000.ma'
        if '_rg.ma' in oldFileType:
            fileType = 'rg_000.ma'
        if '_tx.ma' in oldFileType:
            fileType = 'tx_000.ma'
            
        # GA路径
        pathGA = 'Z:/Projects/Calimero/Common_Sync/CAL_MAYA/scenes/' + assetType + '/' + addGrp + '/' + assetKey + '/publish/' + assetKey + '_' + fileType 
        return pathGA
    
    #-----------------------------------------#
    # 小鸡专用，layout文件转anim文件，及anim文件转render文件
    def calimeroLayout2Anim2Render(self,transType = 1):
        # 进行优化，所有模型全部进layer然后隐藏
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        rootGrps = sk_checkCommon.sk_checkTools().checkOutlinerGroup()
        foodDisplayLayer = mc.createDisplayLayer(n = 'food_temp_DL')
        mc.editDisplayLayerMembers(foodDisplayLayer,rootGrps)
        mc.setAttr((foodDisplayLayer + '.visibility'),0)
        
        if transType == 0:
            old_file = '_mo.'
            new_file = '_ms_anim.'
            old_path = '/model/'
            new_path = '/master/'
        if transType == 1:
            old_file = '_ms_anim.'
            new_file = '_ms_render.'
            old_path = '/master/'
            new_path = '/master/'
        
        # 获取ref信息
        refInfo = self.checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        # 开始替换
        for i in range(len(refPaths)):
            newPath = refPaths[i].replace(old_file,new_file)
            newPath = newPath.replace(old_path,new_path)
            if newPath != refPaths[i]:
                self.checkReferenceChange(refNodes[i],newPath)
        
        # 删除displayLayer
        mc.delete(foodDisplayLayer)
    
    #-----------------------------------------#
    # 小鸡贴图高清转换    
    def calimeroTXModeTransform(self):
        fileNodes = mc.ls(type = 'file')
        if fileNodes:
            fileInfo = mc.getAttr(fileNodes[0] + '.fileTextureName').split('.')[-1]
            print fileInfo
            format = ''
            changeFormat = ' '
            if fileInfo.lower() == 'tga':
                format = '.tga'
                changeFormat = '.png'
            if fileInfo.lower() == 'png':
                format = '.png'
                changeFormat = '.tga'
            for fileNode in fileNodes:
                path = mc.getAttr(fileNode + '.fileTextureName').lower()
                if format in path:
                    path = path.replace(format,changeFormat)
                print path.split('.')[-1]
                mc.setAttr((fileNode + '.fileTextureName'),path,type = 'string')
                
        
    #-----------------------------------------#
    # 小鸡角色tx文件清理工具
    def calimeroTXClean(self):
        # 1:将没有赋予物体的材质球提取出来
        unused = []
        nodes = mc.ls(type = 'lambert')
        for node in nodes:
            if node != 'lambert1':
                cmd = 'hyperShade -objects ' + node
                mel.eval(cmd)
                objs = mc.ls(sl = 1)
                if objs == []:
                    unused.append(node)
        nodes = mc.ls(type = 'blinn')
        for node in nodes:
            cmd = 'hyperShade -objects ' + node
            mel.eval(cmd)
            objs = mc.ls(sl = 1)
            if objs == []:
                unused.append(node)
        unused = list(set(unused))
        mc.select(cl=1)
        #print(unicode('====【第一轮】无用节点====', "utf8"))
        print(u'====【第一轮】无用节点====')
        print unused
        # 2：角色名在材质球里的剔除
        doNot = []
        modelName = '_' + (mc.file(query=1, exn=1)).split('/')[-1].split('_')[1] + '_'
        for node in unused:
            if modelName not in node:
                doNot.append(node)
        #print(unicode('====【第二轮】无用节点====', "utf8"))
        print(u'====【第二轮】无用节点====')
        print doNot
        # 3.将最终得到的无用节点删除
        for node in doNot:
            mc.delete(node)
        #print(unicode('====【清理完毕，请仔细检查】====', "utf8"))
        print(u'====【清理完毕，请仔细检查】====')
    
    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # Calimero 选取物参考转render
    #-----------------------------------------#
    # 小鸡动画用：选取物参考转render，
    def calimeroAnimTest2RenderRef(self):
        # 获取参考列表
        objs = mc.ls(sl=1)
        if objs:
            refNodes = []
            for obj in objs:
                isRef = mc.referenceQuery(obj, isNodeReferenced=1)
                if isRef:
                    refNodes.append(mc.referenceQuery(obj, referenceNode=1))
            if refNodes:
                refNodes = list(set(refNodes))
                # 替换参考
                for ref in refNodes:
                    refPath = mc.referenceQuery(ref, filename=1)
                    newPath = refPath.replace('ms_anim.','ms_render.')
                    mc.file(newPath, loadReference = ref)
        
    #-----------------------------------------#
    # 小鸡动画用：选取物转render，并创建renderLayer
    def calimeroAnimTexturePlayblastConfig(self):
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        # 获取参考列表
        objs = mc.ls(sl=1)
        if objs:
            # 获取objs的mesh及SG信息
            animSpecialShaderInfo = []
            # 切换回去之前需要为4显示，这样最快
            # 或者CHR_GRP,PRP_GRP,SET_GRP等V为0,加快切换
            if mc.ls('CHR_GRP'):
                mc.setAttr('CHR_GRP.v',0)
            if mc.ls('PRP_GRP'):
                mc.setAttr('PRP_GRP.v',0)
            if mc.ls('SET_GRP'):
                mc.setAttr('SET_GRP.v',0)
            if mc.ls('OTC_GRP'):
                mc.setAttr('OTC_GRP.v',0)
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
            for obj in objs:
                if mc.nodeType(obj) == 'mesh':
                    objShape = [obj]
                else:
                    objShape = mc.listRelatives(obj,ni = 1,s = 1,type = 'mesh')
                if objShape:
                    objShape = objShape[0]
                    SGInfo = list(set(mc.listConnections( objShape ,destination = 1,type = 'shadingEngine')))
                    if SGInfo:
                        try:
                            SGInfo.remove('initialShadingGroup')
                        except:
                            pass
                        SGInfo = SGInfo[0]
                        animSpecialShaderInfo.append([objShape,SGInfo])
            # 但凡涉及render参考的都为meshes
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNodes = refInfos[0][0]
            refPathes = refInfos[1][0]
            meshes = []
            for i in range(len(refNodes)):
                refPath = refPathes[i]
                if '_ms_render.' in refPath:
                    print refNodes[i]
                    refRoot = mc.referenceQuery(refNodes[i],nodes = 1)[0]
                    meshes.append(mc.listRelatives(refRoot,ad = 1,type = 'mesh'))
            # 创建渲染层
            # 创建临时shader
            testAnimShader = 'animRLTestShader'
            if mc.ls(testAnimShader):
                mc.delete(testAnimShader)
            testAnimShader = mc.shadingNode ('lambert', asShader=True ,name = testAnimShader)
            testAnimSG = 'animRLTestSG'
            if mc.ls(testAnimSG):
                mc.delete(testAnimSG)
            testAnimSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True ,name = testAnimSG)
            mc.connectAttr(('%s.%s') % ( testAnimShader , 'outColor') , ('%s.%s') % ( testAnimSG , 'surfaceShader'), f=True)
            # 创建层
            if mc.ls('shotAnimRLTest'):
                mc.delete('shotAnimRLTest')
            try:
                meshAll = mc.ls(type = 'mesh')
                curvesShapeAll = mc.ls(type = 'nurbsCurve')
                curvesAll = []
                for shape in curvesShapeAll:
                    curvesAll.append(mc.listRelatives(shape,p=1,type = 'transform')[0])
                mc.createRenderLayer( (meshAll + curvesAll) , name='shotAnimRLTest' , noRecurse=1 , makeCurrent=1)
            except:
                allGrps = mc.ls(assemblies=True)
                mc.createRenderLayer( allGrps , name='shotAnimRLTest' , noRecurse=1 , makeCurrent=1)
            if mc.ls('CHR_GRP'):
                mc.setAttr('CHR_GRP.v',1)
            if mc.ls('PRP_GRP'):
                mc.setAttr('PRP_GRP.v',1)
            if mc.ls('SET_GRP'):
                mc.setAttr('SET_GRP.v',1)
            if mc.ls('OTC_GRP'):
                mc.setAttr('OTC_GRP.v',1)
            # 角色外给与材质
            for mesh in meshes:
                try:
                    mc.sets(mesh, e=1, forceElement= testAnimSG )
                except:
                    pass
            # 恢复选取物的材质
            for i in range(len(animSpecialShaderInfo)):
                mc.sets(animSpecialShaderInfo[i][0], e=1, forceElement= animSpecialShaderInfo[i][1] )
            mc.select(objs)

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # Calimero 摄像机对准工具
    #-----------------------------------------#
    def orient_billboard_to_camera(self,camera_name="CAMERA", set_key=False ):
        import math
        list_c_bil = mc.ls("*:c_BIL*",type="transform")
        for controller_bil in list_c_bil:
            animation_curve_list = mc.findKeyframe( controller_bil, curve=True)
            if animation_curve_list is None or set_key == True:
                mc.setAttr(controller_bil+".rotateY", 0 )
                list_mesh = mc.listRelatives(controller_bil, allDescendents=True, type="mesh")
                x = 0
                y = 0
                z = 0
                compt = 1.0
                bigger_mesh = ""
                if len(list_mesh) > 1:
                    temp_diagonal = 0.0
                    for mesh in list_mesh:
                        bbox = mc.exactWorldBoundingBox(mesh)
                        diagonal = math.sqrt((bbox[0] - bbox[3]) * (bbox[0] - bbox[3]) + (bbox[1] - bbox[4]) * (bbox[1] - bbox[4]) + (bbox[2] - bbox[5]) * (bbox[2] - bbox[5]))
                        if diagonal > temp_diagonal:
                            bigger_mesh = mesh
                            temp_diagonal = diagonal 
                else:
                    bigger_mesh = list_mesh[0]
                compt += 1
                face_normal = mc.polyInfo(bigger_mesh,faceNormals=True)        
                for face in face_normal:
                    normal = face.split(":")[1].replace("\n","").split(" ")
                    normal.pop(0)
                    cam_matrix = mc.getAttr(bigger_mesh + ".worldMatrix")
                    normal_world = [cam_matrix[0] * float(normal[0]) + cam_matrix[4] * float(normal[1]) + cam_matrix[8] * float(normal[2]),
                              cam_matrix[1] * float(normal[0]) + cam_matrix[5] * float(normal[1]) + cam_matrix[9] * float(normal[2]),
                              cam_matrix[2] * float(normal[0]) + cam_matrix[6] * float(normal[1]) + cam_matrix[10] * float(normal[2])]
                    x += float(normal_world[0])
                    y += float(normal_world[1])
                    z += float(normal_world[2])
                normal_x = x/compt
                normal_y = y/compt
                normal_z = z/compt 
                posistion_bil = mc.pointPosition(controller_bil + ".ep[1] ")
                if mc.ls('CAMERA'):
                    posistion_cam = mc.getAttr(camera_name + ".translate")
                if mc.ls("*:" + camera_name ):
                    posistion_cam = mc.getAttr("*:" + camera_name + ".translate")
                vector_bil_to_cam = [posistion_cam[0][0]-posistion_bil[0], posistion_cam[0][1]-posistion_bil[1], posistion_cam[0][2]-posistion_bil[2]]
                angle_between_normal_and_vector_bil_to_cam = mc.angleBetween(euler=True, v1=(normal_x, 0 , normal_z), v2=(vector_bil_to_cam[0], 0, vector_bil_to_cam[2]))
                mc.setAttr(controller_bil+".rotateY",angle_between_normal_and_vector_bil_to_cam[1] )
                if set_key == True:
                    mc.setKeyframe(controller_bil) 
                    mc.keyTangent( controller_bil, inTangentType='step',outTangentType="step")

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # Calimero 参考检测系统
    #-----------------------------------------#
    # Calimero 参考检测系统
    # backType 0 返回缺失的参考信息  | 1 报错缺失的参考信息
    def calimeroRefCheck(self,checkType = 'an', backType = 0 ):
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        
        fileType = ''
        if checkType == 'an':
            fileType = 'anim'
        if checkType == 'lr':
            fileType = 'render'
        
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refPaths = refInfo[1][0]
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projAssetBasePath = sk_infoConfig.sk_infoConfig().checkProjectServerPath() 
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        
        shotAssetInfoTemp = mc.idmtService('GetAssetNameInAnim', (shotInfo[0] + '_' + str(shotInfo[1]) + '_' + str(shotInfo[2])))
        shotAssetServerInfo = shotAssetInfoTemp.split('|')        
        
        refLowerPaths = []
        for refPath in refPaths:
            refLowerPaths.append(refPath.lower())
        
        assetLostID = []
        assetLostPath = []
        if shotAssetServerInfo:
            for i in range(len(shotAssetServerInfo)/2):
                assetNeed = projAssetBasePath + 'scenes/' + shotAssetServerInfo[2*i] + '/' + shotAssetServerInfo[2*i+1] + '/master/' + shotInfo[0] + '_' + shotAssetServerInfo[2*i+1] + '_h_ms_' + fileType + fileFormat
                if assetNeed.lower() not in refLowerPaths:
                    assetLostID.append(shotAssetServerInfo[2*i+1])
                    assetLostPath.append(assetNeed)

        if assetLostPath:
            # 返回消息模式
            if backType == 0:
                return [assetLostID,assetLostPath]
            # 报错模式
            if backType == 1:
                print u'\n'
                print u'------------------------本文件中以下参考丢失------------------------'
                for j in range(len(assetLostPath)):
                    print assetLostID[j]
                    print assetLostPath[j]
                print u'------------------------本文件中以上参考丢失------------------------'
                print u'\n'
                mc.error(u'=======！！！本文件丢失参考，请加载必要的参考！！！=======')
        
        return 0
            
    # Calimero 恢复被删掉的参考
    def calimeroRefAutoLoad(self,checkType = 'an'):
        assetLostInfo = self.calimeroRefCheck(checkType,0)
        if assetLostInfo:
            if assetLostInfo[0]:
                assetLostID = assetLostInfo[0]
                assetLostPath = assetLostInfo[1]
                for i in range(len(assetLostPath)):
                    mc.file(assetLostPath[i], r=1, namespace=assetLostID[i])
                    
    # Calimero 整场镜头道具角色参考处理
    def calimeroRefEpisodeImport(self):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projAssetBasePath = sk_infoConfig.sk_infoConfig().checkProjectServerPath() 
        projFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        
        shotNums = []
        shotDatas = mc.idmtService("GetEpisodeShots", (projFullName + '|' + str(shotInfo[1]))).split('|')
        for data in shotDatas:
            shotNums.append(data.split('_')[-1])

        assetLostType = []
        assetLostID = []
        for shotNum in shotNums:
            # refInfo
            shotAssetInfoTemp = mc.idmtService('GetAssetNameInAnim', (shotInfo[0] + '_' + str(shotInfo[1]) + '_' + shotNum))
            shotAssetServerInfo = shotAssetInfoTemp.split('|') 
            for i in range(len(shotAssetServerInfo)/2):
                if shotAssetServerInfo[2*i] == 'sets':
                    continue
                if not assetLostID:
                    assetLostType.append(shotAssetServerInfo[2*i])
                    assetLostID.append(shotAssetServerInfo[2*i+1])
                else:
                    if shotAssetServerInfo[2*i+1] not in assetLostID:
                        assetLostType.append(shotAssetServerInfo[2*i])
                        assetLostID.append(shotAssetServerInfo[2*i+1])
                        
        fileType = 'render'
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        
        # 导入参考
        if assetLostID:
            for j in range(len(assetLostID)):
                assetPath = projAssetBasePath + 'scenes/' + assetLostType[j] + '/' + assetLostID[j] + '/master/' + shotInfo[0] + '_' + assetLostID[j] + '_h_ms_' + fileType + fileFormat
                mc.file(assetPath, r=1, namespace = assetLostID[j])
                
        # 整理文件
        from idmt.maya.py_common import sk_sceneConfig
        reload(sk_sceneConfig)
        sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(2)
            

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # Calimero 鞋垫特殊处理系统
    #-----------------------------------------#
    # Calimero角色归0处理
    def calimeroCharBack20(self):
        # 获取当前CHR参考
        import os
        from idmt.maya.py_common import sk_common
        reload(sk_common)
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        if refInfo[0][0]:
            refNodes = refInfo[0][0]
            refPaths = refInfo[1][0]
            refNamespace = refInfo[2][0]
            chrID = []
            for i in range(len(refNodes)):
                path = refPaths[i].lower()
                if '/characters/' in path:
                    chrID.append(i)
            # 处理脚底板
            footFilePath = "//file-cluster/GDC/Projects/" + projectFullName + '/' + projectFullName + '_Scratch/FeetModels/characters/' + 'base.ma'
            if mc.ls('TEMP_FEET_GRP'):
                mc.delete('TEMP_FEET_GRP')
            mc.group(name = ('TEMP_FEET_GRP'),em=1)
            if chrID:
                # IK强制开启
                mc.ikSystem(e = 1,sol = 1)
                # 自动K帧状态
                autoKeyState = mc.autoKeyframe(q= 1, state=1 ) 
                mc.autoKeyframe( state= 0 ) 
                # 处理动画层
                animLayers = mc.ls(type = 'animLayer')
                if animLayers:
                    for animL in animLayers:
                        mc.setAttr((animL + '.weight'),0)
                # 处理约束
                sk_common.sk_constraintsOnOffConfig(0)
                # 处理charOffset
                charOffNodes = mc.ls(type = 'characterOffset')
                if charOffNodes:
                    for node in charOffNodes:
                        allCtrls = list(set(mc.listConnections(node,s=1)))
                        print allCtrls
                        if allCtrls:
                            for ctrl in allCtrls:
                                if mc.nodeType(ctrl) == 'transform':
                                    print ctrl
                                    mc.setAttr((ctrl + '.tx'),0)
                                    mc.setAttr((ctrl + '.ty'),0)
                                    mc.setAttr((ctrl + '.tz'),0)
                                    mc.setAttr((ctrl + '.rx'),0)
                                    mc.setAttr((ctrl + '.ry'),0)
                                    mc.setAttr((ctrl + '.rz'),0)
                                if mc.nodeType(ctrl) == 'animCurveTL':
                                    pass
                # 处理模型
                controls = ['WORLD', 'WALK' , 'c_LfLeg_Leg_IK' , 'c_RtLeg_Leg_IK']
                if mc.ls('*norender_foot_l'):
                    mc.delete('*norender_foot_l')
                if mc.ls('*norender_foot_r'):
                    mc.delete('*norender_foot_r')
                if mc.ls('*:*norender_foot_l'):
                    mc.delete('*:*norender_foot_l')
                if mc.ls('*:*norender_foot_r'):
                    mc.delete('*:*norender_foot_r')
                mc.file(footFilePath , i = 1)
                mc.parent(['norender_foot_l','norender_foot_r'],'TEMP_FEET_GRP')
                # 警告信息
                warningInfo = []
                # 导入base文件
                for ID in chrID:
                    # 获取assetName
                    if refNamespace[ID][0:3].lower() == 'cl_':
                        assetName = refNamespace[ID][3:]
                    if refNamespace[ID][0:5].lower() == 'char_':
                        assetName = refNamespace[ID][5:]
                    #footFilePathCHR = footFilePath + 
                    # 角色控制器到归0
                    controlCurveShapes = mc.ls(refNamespace[ID] + ':*',type = 'nurbsCurve')
                    controlCurves = []
                    for shape in controlCurveShapes:
                        if 'c_' in shape or ':WALK' in shape or ':WORLD' in shape:
                            controlCurves.append(mc.listRelatives(shape,p=1,type ='transform',f = 1)[0])
                    for curve in controlCurves:
                        attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                        for attr in attrs:
                            if mc.getAttr(( curve + attr ),settable = 1):
                                mc.setAttr(( curve + attr ),0)
                            else:
                                pass
                        if curve.split('|')[-1] == (refNamespace[ID] + ':c_RtLeg_Leg_IK') or curve.split('|')[-1] == (refNamespace[ID] + ':c_LfLeg_Leg_IK'):
                            attrs = ['.raiseBall', '.raiseToeTip' , '.side' , '.swivel' , '.roll','.original_raistToe','.original_swivelToe','.Open_Toe','.raiseToe','.RaiseToe','.swivelToe','.UpLegth','.LowLength']
                            for attr in attrs:
                                if mc.ls( curve + attr ):
                                    if mc.getAttr(( curve + attr ),settable = 1):
                                        mc.setAttr(( curve + attr ),0)
                                    else:
                                        pass
                    try:
                        sk_common.sk_deleteNamespace(assetName + '_feet')
                    except:
                        pass
                    print u'============【%s】角色归零完毕============'%(refNamespace[ID])
                # 再处理曲线
                #mc.evalDeferred('sk_calimeroProjectTools.sk_clProjectTools().calimeroMove20()')
                self.calimeroMove20()
                # 某些BUG设置处理
                curves = mc.ls('*ADUD*:*eyelids_duplicateCurve_*',type = 'transform') + mc.ls('*ADUD*:*eyelids_duplicateCurve_BaseWire*',type = 'transform')
                if curves:
                    for curve in curves:
                        mc.setAttr((curve + '.tx'),-66.864)
                mc.setAttr('norender_foot_l.v',0)
                mc.setAttr('norender_foot_r.v',0)
                # 自动K帧还原
                mc.ikSystem(e = 1,sol = 1)
                mc.autoKeyframe( state= autoKeyState ) 
                print u'====================！！！全部角色归零成功！！！========================'
     
    #-----------------------------------------#    
    # 该死的再处理曲线补丁
    def calimeroMove20(self,namespace = ''):
        attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
        if namespace:
            objs = mc.ls((namespace + ':WALK'),type = 'transform')
        else:
            objs = mc.ls(('*:WALK'),type = 'transform')
        if objs:
            # 先再次强制归0
            if namespace:
                # 角色控制器到归0
                controlCurveShapes = mc.ls(namespace + ':*',type = 'nurbsCurve')
                controlCurves = []
                for shape in controlCurveShapes:
                    if 'c_' in shape or ':WALK' in shape or ':WORLD' in shape:
                        controlCurves.append(mc.listRelatives(shape,p=1,type ='transform',f = 1)[0])
                for curve in controlCurves:
                    attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                    for attr in attrs:
                        if mc.getAttr(( curve + attr ),settable = 1):
                            mc.setAttr(( curve + attr ),0)
                        else:
                            pass
                    if curve.split('|')[-1] == (namespace + ':c_RtLeg_Leg_IK') or curve.split('|')[-1] == (namespace + ':c_LfLeg_Leg_IK'):
                        attrs = ['.raiseBall', '.raiseToeTip' , '.side' , '.swivel' , '.roll','.original_raistToe','.original_swivelToe','.Open_Toe','.raiseToe','.RaiseToe','.swivelToe','.UpLegth','.LowLength']
                        for attr in attrs:
                            if mc.ls( curve + attr ):
                                if mc.getAttr(( curve + attr ),settable = 1):
                                    mc.setAttr(( curve + attr ),0)
                                else:
                                    pass
            # 再强制处理WALK
            for obj in objs:
                if 'c_' in obj or ':WALK' in obj or ':WORLD' in obj:
                    for attr in attrs:
                        mc.setAttr(( obj + attr ),0)
    

    #-----------------------------------------#
    # Calimero鞋垫特殊处理
    def calimeroFootNorenderConfig(self):
        # 获取当前CHR参考
        import os
        from idmt.maya.py_common import sk_common
        reload(sk_common)
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        testInfo = []
        if refInfo[0][0]:
            refNodes = refInfo[0][0]
            refPaths = refInfo[1][0]
            refNamespace = refInfo[2][0]
            chrID = []
            for i in range(len(refNodes)):
                path = refPaths[i].lower()
                if '/characters/' in path:
                    chrID.append(i)
            # 处理脚底板
            footFilePath = "//file-cluster/GDC/Projects/" + projectFullName + '/' + projectFullName + '_Scratch/FeetModels/characters/' + 'base.ma'
            if mc.ls('TEMP_FEET_GRP'):
                mc.delete('TEMP_FEET_GRP')
            mc.group(name = ('TEMP_FEET_GRP'),em=1)
            if chrID:
                # 自动K帧状态
                autoKeyState = mc.autoKeyframe(q= 1, state=1 ) 
                mc.autoKeyframe( state= 0 ) 
                # IK强制开启
                mc.ikSystem(e = 1,sol = 1)
                # 处理动画层
                animLayers = mc.ls(type = 'animLayer')
                if animLayers:
                    for animL in animLayers:
                        mc.setAttr((animL + '.weight'),0)
                # 处理约束
                sk_common.sk_constraintsOnOffConfig(0)
                # 处理charOffset
                charOffNodes = mc.ls(type = 'characterOffset')
                if charOffNodes:
                    for node in charOffNodes:
                        allCtrls = list(set(mc.listConnections(node,s=1)))
                        print allCtrls
                        if allCtrls:
                            for ctrl in allCtrls:
                                if mc.nodeType(ctrl) == 'transform':
                                    print ctrl
                                    mc.setAttr((ctrl + '.tx'),0)
                                    mc.setAttr((ctrl + '.ty'),0)
                                    mc.setAttr((ctrl + '.tz'),0)
                                    mc.setAttr((ctrl + '.rx'),0)
                                    mc.setAttr((ctrl + '.ry'),0)
                                    mc.setAttr((ctrl + '.rz'),0)
                                if mc.nodeType(ctrl) == 'animCurveTL':
                                    pass

                # 处理模型
                controls = ['WORLD', 'WALK' , 'c_LfLeg_Leg_IK' , 'c_RtLeg_Leg_IK']
                if mc.ls('*norender_foot_l'):
                    mc.delete('*norender_foot_l')
                if mc.ls('*norender_foot_r'):
                    mc.delete('*norender_foot_r')
                if mc.ls('*:*norender_foot_l'):
                    mc.delete('*:*norender_foot_l')
                if mc.ls('*:*norender_foot_r'):
                    mc.delete('*:*norender_foot_r')
                mc.file(footFilePath , i = 1)
                mc.parent(['norender_foot_l','norender_foot_r'],'TEMP_FEET_GRP')
                # 警告信息
                warningInfo = []
                # 导入base文件
                for ID in chrID:
                    refPath = refPaths[ID]
                    assetFile = refPath.split('/')[-1]
                    assetName = assetFile.split('_h_ms_')[0][3:]
                    # 角色控制器到归0
                    controlCurveShapes = mc.ls(refNamespace[ID] + ':*',type = 'nurbsCurve')
                    controlCurves = []
                    for shape in controlCurveShapes:
                        if 'c_' in shape or ':WALK' in shape or ':WORLD' in shape:
                            controlCurves.append(mc.listRelatives(shape,p=1,type ='transform',f = 1)[0])

                    for curve in controlCurves:
                        attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                        for attr in attrs:
                            if mc.getAttr(( curve + attr ),settable = 1):
                                mc.setAttr(( curve + attr ),0)
                            else:
                                pass
                        if curve.split('|')[-1] == (refNamespace[ID] + ':c_RtLeg_Leg_IK') or curve.split('|')[-1] == (refNamespace[ID] + ':c_LfLeg_Leg_IK'):
                            attrs = ['.raiseBall', '.raiseToeTip' , '.side' , '.swivel' , '.roll','.original_raistToe','.original_swivelToe','.Open_Toe','.raiseToe','.RaiseToe','.swivelToe','.UpLegth','.LowLength']
                            for attr in attrs:
                                if mc.ls( curve + attr ):
                                    if mc.getAttr(( curve + attr ),settable = 1):
                                        mc.setAttr(( curve + attr ),0)
                                    else:
                                        pass
                    
                    # 单独导入独特模型
                    footFilePathCHR = "//file-cluster/GDC/Projects/" + projectFullName + '/' + projectFullName + '_Scratch/FeetModels/characters/' + assetName + '/feet.ma' 
                    print '----'
                    print footFilePathCHR
                    if os.path.exists(footFilePathCHR):
                        try:
                            sk_common.sk_deleteNamespace(assetName + '_feet')
                        except:
                            pass
                        mc.file(footFilePathCHR,i=1,namespace = (assetName + '_feet') )
                        footObjL = ((assetName + '_feet') + ':' + 'norender_foot_l')
                        footObjR = ((assetName + '_feet') + ':' + 'norender_foot_r')
                        mc.parent([footObjL,footObjR],'TEMP_FEET_GRP')
                    # 若无，使用通用模型
                    else:
                        warningInfo.append(u'============【%s】脚垫【不存在】============'%assetName)
                        footObjL = mc.duplicate('norender_foot_l')
                        footObjL = mc.rename(footObjL[0],(assetName + '_' + footObjL[0]))
                        footObjR = mc.duplicate('norender_foot_r')
                        footObjR = mc.rename(footObjR[0],(assetName + '_' + footObjR[0]))
    
                    # 蒙皮
                    jointsID = mc.ls((refNamespace[ID] + ':*'),type = 'joint')
                    if jointsID:
                        # 寻找目标体
                        #mc.select(jointsL)
                        footL = ''
                        # 第一优先级foot
                        grp = mc.ls((refNamespace[ID] + ':msh_foot_L_org*'),type = 'transform')
                        if grp:
                            footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        else:
                            grp = mc.ls((refNamespace[ID] + ':msh_foot_L*'),type = 'transform')
                            if grp:
                                footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        if footL == '':
                            grp = mc.ls((refNamespace[ID] + ':msh_shose_L_org*'),type = 'transform')
                            if grp:
                                footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                            else:
                                grp = mc.ls((refNamespace[ID] + ':msh_shose_L*'),type = 'transform')
                                if grp:
                                    footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        # 第二优先级leg
                        if footL == '':
                            grp = mc.ls((refNamespace[ID] + ':msh_leg_L_org*'),type = 'transform')
                            if grp:
                                footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                            else:
                                grp = mc.ls((refNamespace[ID] + ':msh_leg_L*'),type = 'transform')
                                if grp:
                                    footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        # 第三优先级legs
                        if footL == '':
                            grp = mc.ls((refNamespace[ID] + ':msh_leg_org*'),type = 'transform')
                            if grp:
                                footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                            else:
                                grp = mc.ls((refNamespace[ID] + ':msh_leg*'),type = 'transform')
                                if grp:
                                    footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        # 第四优先级body
                        if footL == '':
                            grp = mc.ls((refNamespace[ID] + ':msh_body_org*'),type = 'transform')
                            if grp:
                                footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                            else:
                                grp = mc.ls((refNamespace[ID] + ':msh_body_tmp*'),type = 'transform')
                                if grp:
                                    footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                                if not grp:
                                    grp = mc.ls((refNamespace[ID] + ':msh_body_*'),type = 'transform')
                                    if grp:
                                        footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                                if not grp:
                                    grp = mc.ls((refNamespace[ID] + ':msh_body*'),type = 'transform')
                                    if grp:
                                        footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        # CHIC 特殊处理
                        if 'CHIC' in refNamespace[ID]:
                            grp = mc.ls((refNamespace[ID] + ':msh_body2*'),type = 'transform')
                            if grp:
                                footL = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                                    
                        print refNamespace[ID]
                        print footL
                        if mc.ls(footL):
                            testInfo.append(footL)
                            # 寻找mesh
                            meshL = mc.listRelatives(footL,s = 1 , ni = 1 ,type = 'mesh')
                            if not meshL:
                                warningInfo.append((refNamespace[ID] + u'___L脚有隐患************'))
                                continue
                            # 寻找fdd节点
                            fddNode = mc.listConnections(meshL[0],s = 1 ,d = 0,type = 'ffd')
                            skins = []
                            if fddNode:
                            # 寻找skin节点
                                skins = mc.listConnections(fddNode[0],s = 1 ,d = 0,type = 'skinCluster')
                            else:
                                skins = mc.listConnections(meshL[0],s = 1 ,d = 0,type = 'skinCluster')
                            # 寻找joint节点
                            if skins:
                                jointsL = mc.skinCluster(skins[0],inf = 1, q= 1)
                            else:
                                jointsL = mc.skinCluster(footL,inf = 1, q= 1)
                            # 寻找目标体的影响骨骼
                            needJoint = []
                            if jointsL :
                                for jointL in jointsL:
                                    if ':Lf' in jointL:
                                        needJoint.append(jointL)
                            jointsL = list(set(needJoint))
                            if jointsL:
                                # 蒙皮之前强制对某些角色归0
                                self.calimeroMove20(refNamespace[ID])
                                mc.select(jointsL)
                                print len(jointsL)
                                mc.select(footObjL,add = 1)
                                #mc.skinCluster(jointsL,footObjL,toSelectedBones =1, ignoreHierarchy = 1 , normalizeWeights = 1 , mi = 5 ,omi = 1 ,dr = 4 ,rui = 1 )
                                mel.eval('newSkinCluster \"-toSelectedBones -ignoreHierarchy -normalizeWeights 1 -mi 5 -omi true -dr 4 -rui true,multipleBindPose,1\";')
                                print len(mc.skinCluster(footObjL,inf = 1, q= 1))
                                mc.select(cl=1)
                                mc.select(footL)
                                mc.select(footObjL,add = 1)
                                mel.eval('CopySkinWeights')
                                mc.select(cl=1)
                            else:
                                warningInfo.append((refNamespace[ID] + u'___L脚有隐患************'))
                        else:
                            warningInfo.append((refNamespace[ID] + u'___L脚有隐患************'))

                        #右脚
                        footR = ''
                        # 第一优先级foot 
                        grp = mc.ls((refNamespace[ID] + ':msh_foot_R_org*'),type = 'transform')
                        if grp:
                            footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        else:
                            grp = mc.ls((refNamespace[ID] + ':msh_foot_R*'),type = 'transform')
                            if grp:
                                footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        if footR == '':
                            grp = mc.ls((refNamespace[ID] + ':msh_shose_R_org*'),type = 'transform')
                            if grp:
                                footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                            else:
                                grp = mc.ls((refNamespace[ID] + ':msh_shose_R*'),type = 'transform')
                                if grp:
                                    footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        # 第二优先级leg
                        if footR == '':
                            grp = mc.ls((refNamespace[ID] + ':msh_leg_R_org*'),type = 'transform')
                            if grp:
                                footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                            else:
                                grp = mc.ls((refNamespace[ID] + ':msh_leg_R*'),type = 'transform')
                                if grp:
                                    footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        # 第三优先级legs
                        if footR == '':
                            grp = mc.ls((refNamespace[ID] + ':msh_leg_org*'),type = 'transform')
                            if grp:
                                footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                            else:
                                grp = mc.ls((refNamespace[ID] + ':msh_leg*'),type = 'transform')
                                if grp:
                                    footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        # 第四优先级body
                        if footR == '':
                            grp = mc.ls((refNamespace[ID] + ':msh_body_org*'),type = 'transform')
                            if grp:
                                footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                            else:
                                grp = mc.ls((refNamespace[ID] + ':msh_body_tmp*'),type = 'transform')
                                if grp:
                                    footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                                if not grp:
                                    grp = mc.ls((refNamespace[ID] + ':msh_body_*'),type = 'transform')
                                    if grp:
                                        footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                                if not grp:
                                    grp = mc.ls((refNamespace[ID] + ':msh_body*'),type = 'transform')
                                    if grp:
                                        footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        # CHIC 特殊处理
                        if 'CHIC' in refNamespace[ID]:
                            grp = mc.ls((refNamespace[ID] + ':msh_body2*'),type = 'transform')
                            if grp:
                                footR = refNamespace[ID] + grp[0][len(refNamespace[ID]):]
                        print refNamespace[ID]
                        print footR
                        if mc.ls(footR):
                            testInfo.append(footR)
                            # 寻找mesh
                            meshR = mc.listRelatives(footR,s = 1 , ni = 1 ,type = 'mesh')
                            if not meshR:
                                warningInfo.append((refNamespace[ID] + u'___R脚有隐患************'))
                                continue
                            # 寻找fdd节点
                            fddNode = mc.listConnections(meshR[0],s = 1 ,d = 0,type = 'ffd')
                            skins = []
                            if fddNode:
                            # 寻找skin节点
                                skins = mc.listConnections(fddNode[0],s = 1 ,d = 0,type = 'skinCluster')
                            else:
                                skins = mc.listConnections(meshR[0],s = 1 ,d = 0,type = 'skinCluster')
                            # 寻找joint节点
                            if skins:
                                jointsR = mc.skinCluster(skins[0],inf = 1, q= 1)
                            else:
                                jointsR = mc.skinCluster(footR,inf = 1, q= 1)
                            # 寻找目标体的影响骨骼
                            needJoint = []
                            if jointsR :
                                for jointR in jointsR:
                                    if ':Rt' in jointR:
                                        needJoint.append(jointR)
                            jointsR = list(set(needJoint))
                            if jointsR :
                                # 蒙皮之前强制对某些角色归0
                                self.calimeroMove20(refNamespace[ID])
                                mc.select(jointsR)
                                print len(jointsR)
                                mc.select(footObjR,add = 1)
                                #mc.skinCluster(jointsR,footObjR,toSelectedBones =1, ignoreHierarchy = 1 , normalizeWeights = 1 , mi = 5 ,omi = 1 ,dr = 4 ,rui = 1 )
                                mel.eval('newSkinCluster \"-toSelectedBones -ignoreHierarchy -normalizeWeights 1 -mi 5 -omi true -dr 4 -rui true,multipleBindPose,1\";')
                                print len(mc.skinCluster(footObjR,inf = 1, q= 1))
                                mc.select(cl=1)
                                mc.select(footR)
                                mc.select(footObjR,add = 1)
                                mel.eval('CopySkinWeights')
                                mc.select(cl=1)
                            else:
                                warningInfo.append((refNamespace[ID] + u'___R脚有隐患************'))
                        else:
                            warningInfo.append((refNamespace[ID] + u'___R脚有隐患************'))
                    else:
                        #mc.error(u'=========请确定【%s】的参考是否载入========='%refNamespace[ID])
                        warningInfo.append(u'=========请确定【%s】的参考是否载入========='%refNamespace[ID]) 
                # 再处理曲线
                #mc.evalDeferred('sk_calimeroProjectTools.sk_clProjectTools().calimeroMove20()')
                self.calimeroMove20()
                # 某些BUG设置处理
                curves = mc.ls('*ADUD*:*eyelids_duplicateCurve_*',type = 'transform') + mc.ls('*ADUD*:*eyelids_duplicateCurve_BaseWire*',type = 'transform')
                if curves:
                    for curve in curves:
                        mc.setAttr((curve + '.tx'),-66.864)
                mc.setAttr('norender_foot_l.v',0)
                mc.setAttr('norender_foot_r.v',0)
                # animLayer恢复
                animLayers = mc.ls(type = 'animLayer')
                if animLayers:
                    for animL in animLayers:
                        mc.setAttr((animL + '.weight'),1)
                # 自动K帧还原
                mc.ikSystem(e = 1,sol = 1)
                mc.autoKeyframe( state= autoKeyState ) 
                if testInfo:
                    for i in testInfo:
                        print i
                sk_common.sk_constraintsOnOffConfig(1)
                if warningInfo:
                    for info in warningInfo:
                        mc.warning(info)
                print u'====================！！！全部角色处理成功！！！========================'
             
    #-----------------------------------------------------------------------------------------------------#
    #---------------------------#
    # 客串dod用
                
    # camera导出更新 do4版本
    def sk_sceneCameraUpdate(self,batchUpadate = 0):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        from idmt.maya.py_common import sk_hbExceptCam
        reload(sk_hbExceptCam)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        shotID = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        anim = idmt.pipeline.db.GetAnimByFilename(shotID)
        proStartFrame = int(anim.frmStart)
        
        # 清理unknown节点
        if batchUpadate:
            sk_checkCommon.sk_checkTools().checkDonotNodeCleanBase(0)
        
        # 本地临时目录
        camTempPath = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + shotInfo[1] + "/" + 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_baked.ma'
        # serve目录
        camServerPath = "//file-cluster/GDC/Projects/" + projectInfo + "/Project/scenes/Animation/episode_" + shotInfo[1] + "/episode_camera/" 
        # 需要创建目录
        # 更新server文件路径
        camServerPath = camServerPath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_cam.ma'
        print camServerPath
        # 先删除cam参考
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refPaths:
            if camServerPath in refPaths:
                id = refPaths.index(camServerPath)
                refNode = refNodes[id]
                if batchUpadate:
                    mc.file(rfn=refNode , removeReference=1)
        # 检查bake相机
        needCam = ''
        bkCam = ''
        camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
        testNeedCam = []
        camBakeName = camSourceName + '_baked'
        cameras = mc.ls(type = 'camera', l = 1)
        if cameras:
            for cam in cameras:
                isRef = mc.referenceQuery(cam,isNodeReferenced = 1)
                if not isRef:
                    camGrp = mc.listRelatives(cam,p=1,f= 1)[0]
                    if ('_' + str(shotInfo[1]) + '_').lower() in camGrp.split('|')[-1].lower() and ('_' + str(shotInfo[2])).lower() in camGrp.split('|')[-1].lower():
                        if '_baked' in camGrp:
                            bkCam = camGrp
                        else:
                            needCam = camGrp
        if not needCam and bkCam:
            needCam = mc.rename(bkCam,camSourceName)
        if camSourceName not in needCam:
            needCam = mc.rename(needCam,camSourceName)
        if needCam:
            mc.select(needCam)
        else:
            mc.error(u'=============找不到对应镜头的CAM=============')
        camBakeName = needCam.split('|')[-1] + '_baked'
        mel.eval('source \"//file-cluster/GDC/Resource/Support/Maya/2013/zwCameraImportExport.mel\"')
        mel.eval('zwBakeCamera')
        mc.select(camBakeName)
        # 相机Export
        sk_hbExceptCam.sk_hbExceptCam().HbExceptSelectReCam(projectInfo , 0 , str(proStartFrame),batchUpadate)
        # 输出相机
        newCmd = r"zwSysFile  \"copy\" \"" + camTempPath + r"\" \"" + camServerPath + r"\" 1"
        mel.eval('zwSysFile \"copy\" \"' + camTempPath + '\" \"' + camServerPath + '\" 1')
        print u'====================成功更新camera到服务器端===================='
        # 删除bake后的相机
        mc.delete(camBakeName)
        mc.select(cl=1)
        
        # 成功代码
        return 0


    # 地面材质导入覆盖
    def sk_do4GroundShaderTrans(self,replaceType = 'ground'):
        fileReplace = mc.ls(sl = 1, l = 1)
        if not fileReplace:
            mc.error(u'=======请选择%s物体！！！========'%replaceType)
        if len(fileReplace) != 1:
            if replaceType in ['ground','ground2','mountain']:
                mc.error(u'=======请选择一个物体！！！========')

        if replaceType == 'ground':
            replaceFilePath = 'Z:/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/SD_ground/ground_001.ma'
            ns = 'foodTest'
            replaceObj = 'ground'
            replaceSG = 'SHD_sandfloorSG'
            replaceShader = 'SHD_sandfloor'
            replaceDisplacement = ''
            
        if replaceType == 'ground2':
            replaceFilePath = 'Z:/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/SD_ground/ground_002.ma'
            ns = 'foodTest'
            replaceObj = 'ground'
            replaceSG = 'SHD_sandfloorLayerSG'
            replaceShader = 'SHD_sandfloorLayer'
            replaceDisplacement = ''
            
        if replaceType == 'mountain':
            replaceFilePath = 'Z:/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/SD_ground/mountain_001.ma'
            ns = 'foodTest'
            replaceObj = 'mountain'
            replaceShader = 'SHD_mountain'
            replaceSG = 'SHD_mountainSG'
            replaceDisplacement = 'SHD_mountain_dis'
            
        if replaceType == 'polo':
            replaceFilePath = 'Z:/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/SD_ground/polo_001.ma'
            ns = 'foodTest'
            replaceObj = 'polo_base'
            replaceShader = 'SHD_polo_low'
            replaceSG = 'SHD_polo_lowSG'
            replaceDisplacement = ''

        if replaceType == 'polo2':
            replaceFilePath = 'Z:/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/SD_ground/polo_002.ma'
            ns = 'foodTest'
            replaceObj = 'polo_base2'
            replaceShader = 'SHD_polo_low2'
            replaceSG = 'SHD_polo_low2SG'
            replaceDisplacement = ''
            
            
        if replaceType == 'dorado':
            replaceFilePath = 'Z:/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/SD_ground/dorado_001.ma'
            ns = 'foodTest'
            replaceObj = 'dorado_base'
            replaceSG = 'SHD_doradoSG'
            replaceShader = 'SHD_dorado'
            replaceDisplacement = ''
            
        if replaceType == 'LingFar':
            replaceFilePath = 'Z:/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/SD_ground/lingFar_001.ma'
            ns = 'foodTest'
            replaceObj = 'LingFar'
            replaceSG = 'SHD_LingFarSG'
            replaceShader = 'SHD_LingFar'
            replaceDisplacement = ''
            
        if replaceType == 'CaiFar':
            replaceFilePath = 'Z:/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/SD_ground/caiFar_001.ma'
            ns = 'foodTest'
            replaceObj = 'CaiFar'
            replaceSG = 'SHD_CaiFarSG'
            replaceShader = 'SHD_CaiFar'
            replaceDisplacement = ''
            
        if replaceType == 'CaiStarFar':
            replaceFilePath = 'Z:/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/SD_ground/caiStarFar_001.ma'
            ns = 'foodTest'
            replaceObj = 'CaiStarFar'
            replaceSG = 'SHD_CaiStarFarSG'
            replaceShader = 'SHD_CaiStarFar'
            replaceDisplacement = ''
            
        if replaceType == 'PeachFar':
            replaceFilePath = 'Z:/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/SD_ground/peachFar_001.ma'
            ns = 'foodTest'
            replaceObj = 'PeachFar'
            replaceSG = 'SHD_PeachFarSG'
            replaceShader = 'SHD_PeachFar'
            replaceDisplacement = ''
            
        if replaceType == 'BabyFar':
            replaceFilePath = 'Z:/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/SD_ground/babyFar_001.ma'
            ns = 'foodTest'
            replaceObj = 'BabyFar'
            replaceSG = 'SHD_BabyFarSG'
            replaceShader = 'SHD_BabyFar'
            replaceDisplacement = ''
        
        namespaces = mc.namespaceInfo(listOnlyNamespaces = 1)
        if ns in namespaces:
            # 使得namespace成为空的namespace
            mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
            # 清理空namespace
            mc.namespace(removeNamespace= (':' + ns))

        mc.file(replaceFilePath,i = 1 , namespace = ns)
        
        if replaceType in ['ground','ground2','mountain','LingFar','PeachFar','BabyFar','CaiFar','CaiStarFar']:
            fileReplace = fileReplace[0]
            print (ns + ':' + replaceObj)
            mc.delete(ns + ':' + replaceObj)
            mc.delete(ns + ':' + replaceSG )
        
            meshReplace = mc.listRelatives(fileReplace,ni = 1 ,s = 1,f = 1 ,type = 'mesh')[0]
            SGNodes = mc.listConnections(meshReplace , d = 1 ,type = 'shadingEngine')
            
            SGNodes = list(set(SGNodes))
            for SGnode in SGNodes:
                attrToSG = mc.listConnections((SGnode + '.surfaceShader'),s = 1,plugs = 1)
                if attrToSG:
                    if attrToSG[0] != (ns + ':' + replaceShader + '.outColor'):
                        mc.connectAttr((ns + ':' + replaceShader + '.outColor'),(SGnode + '.surfaceShader'),f = 1)
                else:
                    mc.connectAttr((ns + ':' + replaceShader + '.outColor'),(SGnode + '.surfaceShader'),f = 1)
                #mc.connectAttr((ns + ':' + replaceShader + '.outColor'),(SGnode + '.surfaceShader'),f = 1)
                
                displacementShader = mc.listConnections((SGnode + '.displacementShader'),s = 1,plugs = 1)
                
                if displacementShader:
                    mc.connectAttr((ns + ':' + replaceDisplacement + '.displacement'),(SGnode + '.displacementShader'),f = 1)
                else:
                    if displacementShader:
                        mc.disconnectAttr(displacementShader[0],(SGnode + '.displacementShader'))
                
                # 处理3s通道 和lightmap
                configAttr = ['.miMaterialShader','.miLightMapShader','.miShadowShader','.miPhotonShader']
                for attr in configAttr:
                    if mc.ls(SGnode + attr):
                        nodeConect = mc.listConnections((SGnode + attr),s = 1,plugs = 1)
                        if nodeConect:
                            mc.disconnectAttr(nodeConect[0],(SGnode + attr))
                            
        if replaceType in ['polo','polo2','dorado']:
            mc.delete(ns + ':' + replaceObj)
            mc.delete(ns + ':' + replaceSG )
            
            for obj in fileReplace:
                meshReplace = mc.listRelatives(obj,ni = 1 ,s = 1,f = 1 ,type = 'mesh')[0]
                SGNodes = mc.listConnections(meshReplace , d = 1 ,type = 'shadingEngine')
                
                SGNodes = list(set(SGNodes))
                
                for SGnode in SGNodes:
                    attrToSG = mc.listConnections((SGnode + '.surfaceShader'),s = 1,plugs = 1)
                    if attrToSG:
                        if attrToSG[0] != (ns + ':' + replaceShader + '.outColor'):
                            mc.connectAttr((ns + ':' + replaceShader + '.outColor'),(SGnode + '.surfaceShader'),f = 1)
                    else:
                        mc.connectAttr((ns + ':' + replaceShader + '.outColor'),(SGnode + '.surfaceShader'),f = 1)
                    
                    displacementShader = mc.listConnections((SGnode + '.displacementShader'),s = 1,plugs = 1)
                    
                    if displacementShader:
                        mc.connectAttr((ns + ':' + replaceDisplacement + '.displacement'),(SGnode + '.displacementShader'),f = 1)
                    else:
                        if displacementShader:
                            mc.disconnectAttr(displacementShader[0],(SGnode + '.displacementShader'))
                        
                    # 处理3s通道 和lightmap
                    configAttr = ['.miMaterialShader','.miLightMapShader','.miShadowShader','.miPhotonShader']
                    for attr in configAttr:
                        if mc.ls(SGnode + attr):
                            nodeConect = mc.listConnections((SGnode + attr),s = 1,plugs = 1)
                            if nodeConect:
                                mc.disconnectAttr(nodeConect[0],(SGnode + attr))

        # 使得namespace成为空的namespace
        mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
        # 清理空namespace
        mc.namespace(removeNamespace= (':' + ns))
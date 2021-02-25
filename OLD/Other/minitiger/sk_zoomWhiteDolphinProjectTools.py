# -*- coding: utf-8 -*-

'''
Created on 2013-8-1

@author: shenkang
'''

import maya.cmds as mc
import maya.mel as mel

class sk_zmProjectTools(object):
    def __init__(self):
        #namespace清理
        pass
    
    '''
            【UI篇】【前期】【zm临时工具集】
    '''
    # 前期check工具集
    def sk_sceneUIZMTempTools(self):
        # 窗口
        if mc.window ("sk_sceneUIZMTempTools",ex=1):
            mc.deleteUI( "sk_sceneUIZMTempTools", window=True )
        mc.window("sk_sceneUIZMTempTools",title="Tools", widthHeight=(160, 150),menuBar=0)
       
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

        # 前台检测Anim和Render版本
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【检测】Anim和Render版本', 'utf8')),c = 'from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkAssetAnim2RenderCheckInConfig()')
        mc.setParent("..")   

        # sign替换工具
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('选取【ca_】【清理】', 'utf8')),c = 'from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkSignReplace(\"ca_\")')
        mc.setParent("..")

        # 清理Clamp节点
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【整理Clamp连接】', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_clamp2RampConfig()')
        mc.setParent("..")
        
        # 双MAP命名修正
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【双MAP命名修正】', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_mapTexConfig()')     
        mc.setParent("..")
        
        # proxy替换路径
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【proxy】anim转tx', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_proxyAnim2Tx()')
        mc.setParent("..")     
        
        # proxyID修正
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【proxyID】【修正】', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_proxyIDCompleteConfig()')
        mc.setParent("..")    
        
        # 选取所有隐藏物体
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【选取】所有【隐藏】', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_zmGetAllHideObjs()')
        mc.setParent("..")  
        
        
        # 【临时】自动整理tx文件
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.7,0.2],label = (unicode('【临时】自动整理tx文件', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_zmTempFileReorganize()')
        mc.setParent("..")    
        
        # 【临时】自动高模替换锁选asset类
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.7,0.2],label = (unicode('【临时】所选[类][高][替]', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_zmProxyTransHModel()')
        mc.setParent("..")         

        # 检测角色道具WDCO
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0.2,0.7,0.7],label = (unicode('【参考】检测WCO_DCO', 'utf8')),c = 'import maya.cmds as mc\nmc.file(rename = \"D:/zm_101_001_an_c001.mb\")\nfrom idmt.maya.py_common import sk_sceneConfig\nreload(sk_sceneConfig)\nsk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(0)\nfrom idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_COLOR\")\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_SHADOW\")')
        mc.setParent("..")
        
        # 【选取】检测【无法赋予材质】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【选取】检测【无法赋予材质】', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_zmShaderErrorObjs()')
        mc.setParent("..")
        
        # 【自动】赋予【sea材质】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【自动】赋予【sea材质】', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_seaShaderAutoCreate()')
        mc.setParent("..")
        
        # 【自动】分叉黑白透明贴图
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【自动】分叉黑白透明贴图', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_zmTransparencyNodesCreate()')
        mc.setParent("..")
        

        mc.setParent("..")

        # tab_动画临时工具集
        child2 = mc.rowColumnLayout()

        # 动画类
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===动画类===', 'utf8')))
        mc.setParent("..")   

        # 【转移】【恢复】船动画
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.7,0.2],label = (unicode('【转移】【恢复】船动画', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_TaaoraBoatKeyConfig()')
        mc.setParent("..")

        # 【非Anim】转换【Anim】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.7,0.2],label = (unicode('【非Anim】转换【Anim】', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_zmNotAnim2Anim()')
        mc.setParent("..")

        # 清理Clamp节点
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【整理Clamp连接】', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_clamp2RampConfig()')
        mc.setParent("..")

        # 整理anim文件
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0.2,0.1,0.45],label = (unicode('【整理maya动画文件】', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_rebuildClean()')
        mc.setParent("..")


        mc.setParent("..")
        
        
        # tab_渲染临时工具集
        child3 = mc.rowColumnLayout()

        # 渲染类
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===渲染类===', 'utf8')))
        mc.setParent("..")   

        # 清理选取物节点
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【清理】【选取物】SG节点', 'utf8')),c = 'from idmt.maya.py_common import sk_sceneConfig\nreload(sk_sceneConfig)\nsk_sceneConfig.sk_sceneConfig().sk_sceneCleanMeshSG()')
        mc.setParent("..")

        # 转参考
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.7,0.2],label = (unicode('【Anim】转换【Render】', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_zmNotAnim2Render(1)')
        mc.setParent("..")
        
        # 转参考
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.7,0.2],label = (unicode('【Anim】转换【Tx】', 'utf8')),c = 'sk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_zmNotAnim2Render(2)')
        mc.setParent("..")

        # 【特效用】【shot文件SmoothSet】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【特效用】【shot文件SmoothSet】', 'utf8')),c = 'from idmt.maya.py_common import sk_sk_smoothSet\nreload(sk_smoothSet)\nsk_smoothSet.sk_smoothSetTools().smoothSetDoSmooth(0)')
        mc.setParent("..")

        mc.setParent("..")
        
        # tab_全局扫描工具集
        child4 = mc.rowColumnLayout()

        # 全局扫描类
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===全局扫描类===', 'utf8')))
        mc.setParent("..")   

        # 【全局扫描】【多余master文件】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【扫描】【多余master文件】', 'utf8')),c = 'from idmt.maya.py_common import sk_sceneConfig\nreload(sk_sceneConfig)\nsk_sceneConfig.sk_sceneConfig().sk_sceneGlobalAllAssetMasterCheck()')
        mc.setParent("..")

        # 【全局扫描】【面赋予材质文件】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【扫描】【面赋予材质文件】', 'utf8')),c = 'from idmt.maya.py_common import sk_sceneConfig\nreload(sk_sceneConfig)\nsk_sceneConfig.sk_sceneConfig().sk_sceneGlobalAllAssetFaceShaderCheck()')
        mc.setParent("..")

        # 【全局扫描】【SmoothSet信息】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【扫描】【SmoothSet信息】', 'utf8')),c = 'from idmt.maya.py_common import sk_sceneConfig\nreload(sk_sceneConfig)\nsk_sceneConfig.sk_sceneConfig().sk_sceneGlobalAllAssetSmoothSetCheck()')
        mc.setParent("..")

        # 【全局扫描】【RenderState信息】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【扫描】【RenderState信息】', 'utf8')),c = 'from idmt.maya.py_common import sk_sceneConfig\nreload(sk_sceneConfig)\nsk_sceneConfig.sk_sceneConfig().sk_sceneGlobalModelRenderStateCheck()')
        mc.setParent("..")

        # 【全局扫描】【AnimRender差异信息】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【扫描】【AnimRender差异信息】', 'utf8')),c = 'from idmt.maya.py_common import sk_sceneConfig\nreload(sk_sceneConfig)\nsk_sceneConfig.sk_sceneConfig().sk_sceneGlobalAnimRenderDifChcek()')
        mc.setParent("..")

        # 【全局扫描】【Cache List信息】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【扫描】【Cache List信息】', 'utf8')),c = 'from idmt.maya.py_common import sk_sceneConfig\nreload(sk_sceneConfig)\nsk_sceneConfig.sk_sceneConfig().sk_sceneGlobalCacheAnimListChcek()')
        mc.setParent("..")

        # 【全局扫描】【W|D color 检测】
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.1,0.45],label = (unicode('【扫描】【W|D color 检测】', 'utf8')),c = 'from idmt.maya.py_common import sk_sceneConfig\nreload(sk_sceneConfig)\nsk_zoomWhiteDolphinProjectTools.sk_zmProjectTools().sk_sceneGlobalAssetWDRampErrorInfoExport()')
        mc.setParent("..")

        mc.setParent("..")
        
        mc.tabLayout( tabs, edit=True, tabLabel=((child1, unicode('前期集', 'utf8')), (child2, unicode('动画集', 'utf8')),(child3, unicode('灯光集', 'utf8')),(child4, unicode('全局扫描类', 'utf8')) ))
        
        mc.setParent("..")
        mc.showWindow( "sk_sceneUIZMTempTools" )
    

    '''
            【UI篇】【灯光】【FinalLayout界面】
    '''
    # finalLayout界面
    def sk_sceneFinalLayoutUI(self):
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        from idmt.maya.py_common import sk_camMatrixScene
        reload(sk_camMatrixScene)
        
        # 窗口
        if mc.window ("sk_sceneFinalLayoutTools",ex=1):
            mc.deleteUI( "sk_sceneFinalLayoutTools", window=True )
        mc.window("sk_sceneFinalLayoutTools",title="FinalLayout Tools", widthHeight=(260, 375),menuBar=0)
       
        # 面板
        mc.scrollLayout( 'scrollLayout' )
        
        # finalLayout自动
        mc.frameLayout( label=u'FinalLayout Auto| 自动化FinalLayout', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout(numberOfColumns = 2,columnWidth2=(120, 120))
        mc.button(l=u'FinalLayout快速版',bgc = [0.1,0.8,0.2],width = 120,height = 30,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutPerform()')
        mc.button(l=u'FinalLayout完整版',bgc = [0.1,0.8,0.8],width = 120,height = 30,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutPerform(1,1)')
        mc.setParent( '..' )
        mc.setParent( '..' )
        
        # finalLayout分解导出
        mc.frameLayout( label=u'FinalLayout Export| 【An】导出信息', borderStyle='etchedOut' ,width = 250 )
        # grpExport = 0 , cacheExport = 0 , animExport = 0 , assetInfoExport = 0 , hideInfoExport = 0 ,server = 1
        mc.rowLayout(numberOfColumns = 3,columnWidth3=(80 , 80 ,80))
        mc.button(l=u'导出OTC文件',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutExport(1,0,0,0,0)')
        mc.button(l=u'导出AssetInfo',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutExport(0,0,0,1,0)')
        mc.button(l=u'输出Camera',bgc = [0.0,0.0,0.0],width = 80,height = 22,c='from idmt.maya.py_common import sk_sceneConfig\nreload(sk_sceneConfig)\nsk_sceneConfig.sk_sceneConfig().sk_sceneCameraUpdate()')
        mc.setParent( '..' )
        
        
        mc.rowLayout(numberOfColumns = 3,columnWidth3=(80, 80, 80 ))
        mc.button(l=u'导出Cache',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutExport(0,1,0,0,0)')
        mc.button(l=u'导出AnimInfo',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutExport(0,0,1,0,0)')
        mc.button(l=u'导出HideInfo',bgc = [0.0,0.0,0.0],width = 80,height = 22,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutExport(0,0,0,0,1)')
        mc.setParent( '..' )
        
        mc.setParent( '..' )

        # finalLayout分解导入
        mc.frameLayout( label=u'FinalLayout Import| 【Fs】导入信息', borderStyle='etchedOut' ,width = 250 )
        # grpImport = 0 , cacheImport = 0 , animImport = 0 , assetInfoImport = 0 ,  hideInfoImport= 0 
        mc.rowLayout(numberOfColumns = 3,columnWidth3=(80 , 80 ,80))
        mc.button(l=u'导入OTC文件',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutImport(1,0,0,0,0)')
        mc.button(l=u'创建Asset',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutImport(0,0,0,1,0)')
        mc.button(l=u'参考Camera',bgc = [0.0,0.0,0.0],width = 80,height = 22,c='mel.eval(\'source zwCameraImportExport.mel; zwGetCameraUI;\')')
        mc.setParent( '..' )
        
        mc.rowLayout(numberOfColumns = 3,columnWidth3=(80, 80 ,80))
        mc.button(l=u'导入Cache',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutImport(0,1,0,0,0)')
        mc.button(l=u'导入AnimInfo',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutImport(0,0,1,0,0)')
        mc.button(l=u'导入HideInfo',bgc = [0.0,0.0,0.0],width = 80,height = 22,c ='from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkFinalLayoutImport(0,0,0,0,1)')
        mc.setParent( '..' )
        
        mc.setParent( '..' )
        
        # 参考材质历史清理
        mc.frameLayout( label=u'参考材质历史清理 | 所有参考unload状态', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout()
        mc.button(l=u'=====【Fs文件】清理参考材质历史=====',bgc = [0.0,0.0,0.0],width = 240,height = 28,c ='from idmt.maya.py_common import sk_referenceConfig\nreload(sk_referenceConfig)\nsk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)')
        mc.setParent( '..' )
        mc.setParent( '..' )
        
        # 导入CamInOut信息
        mc.frameLayout( label=u'Camera视野信息导入 | 从服务器端读取已经解算好的数据', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout()
        mc.button(l=u'=====【Fs|Lr文件】Camera信息导入=====',bgc = [0.0,0.0,0.0],width = 240,height = 28,c ='from idmt.maya.py_common import sk_camMatrixScene\nreload(sk_camMatrixScene)\nsk_camMatrixScene.sk_camMatrixScene().sk_sceneCamServerInfoImport()')
        mc.setParent( '..' )
        mc.setParent( '..' )
        
        
        # 视野检测
        mc.frameLayout( label=u'Camera视野检测 | 视野内显示，视野外隐藏', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout()
        mc.button(l=u'======【Fs文件】Camera视野检测======',bgc = [0.15,0.55,0.95],width = 240,height = 38,c ='from idmt.maya.py_common import sk_camMatrixScene\nreload(sk_camMatrixScene)\nsk_camMatrixScene.sk_camMatrixScene().sk_sceneMeshCamConfigBatch(0)')
        mc.setParent( '..' )
        mc.setParent( '..' )
        
        # 视野检测
        mc.frameLayout(label = u'测试阶段，若有报错信息，请及时联系TD',borderStyle='etchedOut' ,width = 250 )
        mc.setParent( '..' )
        
        mc.setParent("..")
        mc.showWindow( "sk_sceneFinalLayoutTools" )
    


    # 手动清理
    def sk_rebuildClean(self , serverClean = 0):
        # 开始处理
        from idmt.maya.py_common import sk_sceneConfig
        reload(sk_sceneConfig)
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        
        sk_sceneConfig.sk_sceneConfig().sk_sceneNoRefNamespaceClean()
        print u'====================多层namespace清理完毕===================='
        
        # 检测ref
        from idmt.maya.commonCore.core_mayaCommon import sk_animFileCheck
        reload(sk_animFileCheck)
        sk_animFileCheck.sk_animFileCheck().shotAssetRefCheck('an',1)
        
        print u'====================ref对比情况检测完毕===================='
        
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]

        # 处理参考
        for i in range(len(refNodes)):
            refNode = refNodes[i]
            refPath = mc.referenceQuery(refNode, f=1)
            path = refPath.lower()
            # 最优先
            # 清理外部参考 # 孙望插件
            if '/zoomwhitedolphin/' not in path:
            #if 'calimero' not in path or 'c:\\' in path or 'd:\\' in path or 'e:\\' in path:
                #if 'c:\\' in path or 'd:\\' in path or 'e:\\' in path:
                #    localRef = 1
                refExist = mc.referenceQuery(refPath,rfn=1)
                mc.file(rfn=refExist , removeReference=1)
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
        
        # FPS
        sk_sceneConfig.sk_sceneConfig().sk_sceneImportFrame('FPS')
        # frame
        sk_sceneConfig.sk_sceneConfig().sk_sceneImportFrame('frame')
        
        print u'=====================镜头标准化完毕=====================' 
        
        # 处理组
        #sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(0)
        
        #print u'=================OutLiner重新分组================='  
        
        
        #sk_sceneConfig.sk_sceneConfig().sk_sceneCleanDislayLayers()
        
        #print u'==================显示层清理完毕=================='
        # 清理层和渲染层
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        # 尝试回到master层
        '''
        if mc.ls('defaultRenderLayer'):
            if mc.referenceQuery('defaultRenderLayer',isNodeReferenced = 1):
                print u'===请检查文件masterLayer，名字异常==='
                mc.error(u'===请检查文件masterLayer，名字异常===')
        else:
            print u'===请检查文件masterLayer，名字异常==='
            mc.error(u'===请检查文件masterLayer，名字异常===')
        '''
        try:
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        except:
            print u'===请检查文件masterLayer，名字异常==='
            mc.error(u'===请检查文件masterLayer，名字异常===')
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
          
        print u'=================显示层|渲染层处理完毕================='    
        #sk_sceneConfig.sk_sceneConfig().sk_sceneUnloadRefDel()
        
        #print u'==================未勾选参考清理完毕=================='
        
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
        
        sk_sceneConfig.sk_sceneConfig().sk_sceneAssetNamespaceConfig()
        
        print u'==================Ref Info 处理完毕=================='

        sk_sceneConfig.sk_sceneConfig().sk_sceneCameraUpdate(1)
        print u'==================camera传输完毕=================='
        
        # 处理组
        sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(2)
        
        print u'=================outLiner重新分组================='  

        # 保存文件
        #if serverClean == 0:
        #    import maya.cmds as mc
        #    mc.file(save = 1)
        
    # 修正map后缀中存在多种.格式的情况
    # 统一更改贴图，考虑到不是所有人有权限改服务器端，则临时放入D盘指定temp
    # 上传后手动清理D盘temp文件
    def sk_mapTexConfig(self):    
        #创建目录
        tempPath = 'D:/Info_Temp/temp/texTemp'
        mc.sysFile(tempPath ,makeDir = 1)
        #获取贴图节点
        texNames = mc.ls(type = 'file')
        for i in range(len(texNames)):
            #获取贴图路径
            sysPath = mc.getAttr((texNames[i] + '.fileTextureName'))
            #获取最终文件名
            tempSplit = sysPath.split('/')[-1]
            tempNames = tempSplit.split('.')
            finalName = tempNames[0]+'.'+tempNames[-1]
            #复制，改名
            mc.sysFile(sysPath ,copy = (tempPath + '/' + tempSplit))
            mc.sysFile((tempPath + '/' + tempSplit) , rename = (tempPath + '/' +finalName) )
            #重新更改路径
            mc.setAttr((texNames[i] + '.fileTextureName'),(tempPath + '/' +finalName),type = 'string')
            print ('\t\t\t\t\t！！！Done!!!\t\t\t\t\t') 
    
    # 前期整理clamp和ramp连接
    def sk_clamp2RampConfig(self):
        clampNodes = mc.ls(type = 'clamp')
        for clamp in clampNodes:
            toNode = mc.connectionInfo((clamp + '.outputR'),destinationFromSource=1)
            if toNode:
                mc.disconnectAttr((clamp + '.outputR'), (toNode[0]))
                mc.connectAttr((clampNodes[0] +'.outputR' ), (toNode[0]))
                print (clamp + '\t\t\t\t\tDone!!!') 
                
    # 特效用，动画师加载参考
    def sk_zmSplashReference(self,type = 'in'):
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        if type == 'in':
            keyFolder = 'I'
            keyFile = 'In'
        if type == 'out':
            keyFolder = 'O'
            keyFile = 'Out'
        fullPath = '//file-cluster/GDC/Projects/ZoomWhiteDolphin/Project/data/ClusterCache/Splash_Base/' + 'Splash_Above_' + keyFolder + '/' + 'zm_ef_Splash' + keyFile + '_Above_l_c001.mb'
        # 检测FX_GRP
        # OTC_GRP
        if mc.ls('OTC_GRP'):
            otcGrp = 'OTC_GRP'
        else:
            otcGrp = mc.group(em=1, name='OTC_GRP')
        # VFX_GRP
        if mc.ls('VFX_GRP'):
            vfxGrp = 'VFX_GRP'
        else:
            vfxGrp = mc.group(em=1, name='VFX_GRP')
        # 打组
        if otcGrp not in mc.ls(vfxGrp, l=1)[0]:
            mc.parent(vfxGrp, otcGrp)

        # 判断版本号
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refPaths = refInfo[1][0]
        refNum = 0
        if refPaths:
            for refPath in  refPaths:
                if refPath == fullPath:
                    refNum =  refNum + 1
        
        # 直接先参考进来
        print fullPath
        mc.file(fullPath,r = 1,namespace = ('zm_ef_splash_' + str(refNum) ))
        
        # 参考
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        # 打组
        for i in range(len(refPaths)):
            if refPaths[i] == fullPath:
                refNode = refNodes[i]
                refObjs = mc.referenceQuery(refNode , nodes=1)
                objFullPath = mc.ls(refObjs[0],l = 1)[0]
                if 'VFX_GRP' not in objFullPath:
                    mc.parent(objFullPath,vfxGrp)
        # 删除VFX组下的空组
        grps = mc.listRelatives('VFX_GRP',c = 1 ,type = 'transform',f = 1)
        for grp in grps:
            child = mc.listRelatives(grp,c = 1,f=1)
            if not child :
                try:
                    mc.delete(grp)
                except:
                    pass
            
    # 非anim转anim
    def sk_zmNotAnim2Anim(self):
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]

        # 处理参考
        for i in range(len(refPaths)):
            refPath = refPaths[i]
            path = refPath.lower()
            # 最优先
            # 非标准参考转标准参考
            if '_c_h_ms_anim.mb' in path:
                newPath = path.replace('_c_h_ms_anim.mb','_h_ms_anim.mb')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 非标准参考转标准参考
            if '_ng_h_ms_anim.mb' in path:
                newPath = path.replace('_ng_h_ms_anim.mb','_h_ms_anim.mb')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 转换参考，model文件
            if '_mo.' in path:
                newPath = path.replace('/model/','/master/')
                newPath = newPath.replace('_mo.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 转换参考，rigging文件
            if '_rg.' in path:
                newPath = path.replace('/rigging/','/master/')
                newPath = newPath.replace('_rg.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 转换参考，tx文件
            if '_tx.' in path:
                newPath = path.replace('/texture/','/master/')
                newPath = newPath.replace('_tx.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 转换参考，notex和tex
            if '_ms_notex.' in path:
                newPath = path.replace('_ms_notex.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 转换参考，notex和tex
            if '_ms_tex.' in path:
                newPath = path.replace('_ms_tex.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
                
    # anim转render  1 anim->render | 2 anim->tx
    def sk_zmNotAnim2Render(self,transType = 1):
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
            if transType== 1:
                oldKey = '_ms_anim.'
                newKey = '_ms_render.'
                if oldKey in path:
                    newPath = path.replace(oldKey,newKey)
                    # 替换参考
                    mc.file(newPath, loadReference = refNodes[i])
            if transType== 2:
                oldKey = '_ms_anim.'
                newKey = '_tx.'
                if oldKey in path:
                    newPath = path.replace(oldKey,newKey)
                tempPath = newPath
                oldKey = 'master'
                newKey = 'texture'
                if oldKey in tempPath:
                    newPath = tempPath.replace(oldKey,newKey)
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])

    # 提取无法赋予材质的物体
    def sk_zmShaderErrorObjs(self):
        objs = mc.ls(sl = 1,l = 1)
        if objs:
            needObjs = []
            for obj in objs:
                if mc.listRelatives(obj , ni = 1 ,c = 1 , type = 'mesh'):
                    needObjs.append(obj)
            if needObjs:
                shaderNode = 'Food_Test_Shader'
                shaderSG = 'Food_Test_SG'
                errorList = []
                if mc.ls(shaderNode):
                    mc.delete(shaderNode)
                if mc.ls(shaderSG):
                    mc.delete(shaderSG)
                shaderNode = mc.shadingNode ('lambert', asShader=True, name= shaderNode )  
                shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name= shaderSG )
                mc.connectAttr((shaderNode + '.outColor'), (shaderSG + '.surfaceShader'))
                for obj in needObjs:
                    try:
                        mc.sets(obj ,e=1, forceElement= shaderSG)
                    except:
                        errorList.append(obj)
                if errorList:
                    print u'-----请处理以下无法赋予材质的物体-----'
                    for info in errorList:
                        print info
                    print u'-----请处理以上无法赋予材质的物体-----'    

    # 给船校正动画
    def sk_TaaoraBoatKeyConfig(self):
        # 寻找boat
        boatConfig = 0
        boatID = 0
        boatRelace = 0
        from idmt.maya.py_common import sk_referenceConfig
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        print refInfo
        refPaths = refInfo[1][0]
        refNamespaces = refInfo[2][0]
        if refPaths:
            for i in range(len(refPaths)):
                if 'zm_s009001TaaoraBoat_h_ms_notex.mb' in refPaths[i] :
                    boatConfig = 1      
                    boatID = i
                    boatRelace = 1
                    break
                if 'zm_s009001TaaoraBoat_h_ms_tex.mb' in refPaths[i]:
                    boatConfig = 1      
                    boatID = i
                    boatRelace = 2
                    break
        # 是否开启船修正
        if boatConfig:
            # old Boat Namespace 加temp后缀
            boatNamespace = refNamespaces[boatID]
            boatPath_Temp = refPaths[boatID]
            boatNamespace_Temp = boatNamespace + '_temp'
            mc.file(boatPath_Temp,e=1,ns = boatNamespace_Temp)

            # reference new Boat
            if boatRelace == 1:
                boatPath = boatPath_Temp.replace('_notex.','_anim.')
            if boatRelace == 2:
                boatPath = boatPath_Temp.replace('_tex.','_anim.')
            cmd = 'importReference \"' + boatPath + '\" \"mayaBinary\"'
            mel.eval(cmd)
            try:
                mc.file(boatPath,e=1,ns = boatNamespace)
            except:
                pass
            
            # 传递动画_Master
            oldMasterName = boatNamespace_Temp + ':Master'
            newMasterName = boatNamespace + ':MSH_Master_ct_an'
            
            # 第一帧
            mc.currentTime(1)
            mc.setAttr((newMasterName+'.tx'),mc.getAttr(oldMasterName+'.tx'))
            mc.setAttr((newMasterName+'.ty'),mc.getAttr(oldMasterName+'.ty'))
            mc.setAttr((newMasterName+'.tz'),mc.getAttr(oldMasterName+'.tz'))
            mc.setAttr((newMasterName+'.rx'),mc.getAttr(oldMasterName+'.rx'))
            mc.setAttr((newMasterName+'.ry'),mc.getAttr(oldMasterName+'.ry'))
            mc.setAttr((newMasterName+'.rz'),mc.getAttr(oldMasterName+'.rz'))
            mc.setAttr((newMasterName+'.sx'),mc.getAttr(oldMasterName+'.sx'))
            mc.setAttr((newMasterName+'.sy'),mc.getAttr(oldMasterName+'.sy'))
            mc.setAttr((newMasterName+'.sz'),mc.getAttr(oldMasterName+'.sz'))

            # tx
            if mc.ls(oldMasterName + '_translateX'):
                mc.copyKey(oldMasterName + '_translateX')
                mc.select(newMasterName)
                mc.pasteKey(newMasterName)
            
            # ty
            if mc.ls(oldMasterName + '_translateY'):
                mc.copyKey(oldMasterName + '_translateY')
                mc.select(newMasterName)
                mc.pasteKey(newMasterName)

            # tz
            if mc.ls(oldMasterName + '_translateZ'):
                mc.copyKey(oldMasterName + '_translateZ')
                mc.select(newMasterName)
                mc.pasteKey(newMasterName)
                
            # rx
            if mc.ls(oldMasterName + '_rotateX'):
                mc.copyKey(oldMasterName + '_rotateX')
                mc.select(newMasterName)
                mc.pasteKey(newMasterName)
                
            # ry
            if mc.ls(oldMasterName + '_rotateY'):
                mc.copyKey(oldMasterName + '_rotateY')
                mc.select(newMasterName)
                mc.pasteKey(newMasterName)
                
            # rz
            if mc.ls(oldMasterName + '_rotateZ'):
                mc.copyKey(oldMasterName + '_rotateZ')
                mc.select(newMasterName)
                mc.pasteKey(newMasterName)
                
            # sx
            if mc.ls(oldMasterName + '_scaleX'):
                mc.copyKey(oldMasterName + '_scaleX')
                mc.select(newMasterName)
                mc.pasteKey(newMasterName)
                
            # sy
            if mc.ls(oldMasterName + '_scaleY'):
                mc.copyKey(oldMasterName + '_scaleY')
                mc.select(newMasterName)
                mc.pasteKey(newMasterName)

            # sz
            if mc.ls(oldMasterName + '_scaleZ'):
                mc.copyKey(oldMasterName + '_scaleZ')
                mc.select(newMasterName)
                mc.pasteKey(newMasterName)

            # 传递动画_World
            oldWorldName = boatNamespace_Temp + ':World'
            newWorldName = boatNamespace + ':MSH_World_ct_an'
            
            # 第一帧
            mc.currentTime(1)
            mc.setAttr((newWorldName+'.tx'),mc.getAttr(oldWorldName+'.tx'))
            mc.setAttr((newWorldName+'.ty'),mc.getAttr(oldWorldName+'.ty'))
            mc.setAttr((newWorldName+'.tz'),mc.getAttr(oldWorldName+'.tz'))
            mc.setAttr((newWorldName+'.rx'),mc.getAttr(oldWorldName+'.rx'))
            mc.setAttr((newWorldName+'.ry'),mc.getAttr(oldWorldName+'.ry'))
            mc.setAttr((newWorldName+'.rz'),mc.getAttr(oldWorldName+'.rz'))
            mc.setAttr((newWorldName+'.sx'),mc.getAttr(oldWorldName+'.sx'))
            mc.setAttr((newWorldName+'.sy'),mc.getAttr(oldWorldName+'.sy'))
            mc.setAttr((newWorldName+'.sz'),mc.getAttr(oldWorldName+'.sz'))

            # tx
            if mc.ls(oldWorldName + '_translateX'):
                mc.copyKey(oldWorldName + '_translateX')
                mc.select(newWorldName)
                mc.pasteKey(newWorldName)
            
            # ty
            if mc.ls(oldWorldName + '_translateY'):
                mc.copyKey(oldWorldName + '_translateY')
                mc.select(newWorldName)
                mc.pasteKey(newWorldName)

            # tz
            if mc.ls(oldWorldName + '_translateZ'):
                mc.copyKey(oldWorldName + '_translateZ')
                mc.select(newWorldName)
                mc.pasteKey(newWorldName)
                
            # rx
            if mc.ls(oldWorldName + '_rotateX'):
                mc.copyKey(oldWorldName + '_rotateX')
                mc.select(newWorldName)
                mc.pasteKey(newWorldName)
                
            # ry
            if mc.ls(oldWorldName + '_rotateY'):
                mc.copyKey(oldWorldName + '_rotateY')
                mc.select(newWorldName)
                mc.pasteKey(newWorldName)
                
            # rz
            if mc.ls(oldWorldName + '_rotateZ'):
                mc.copyKey(oldWorldName + '_rotateZ')
                mc.select(newWorldName)
                mc.pasteKey(newWorldName)
                
            # sx
            if mc.ls(oldWorldName + '_scaleX'):
                mc.copyKey(oldWorldName + '_scaleX')
                mc.select(newWorldName)
                mc.pasteKey(newWorldName)
                
            # sy
            if mc.ls(oldWorldName + '_scaleY'):
                mc.copyKey(oldWorldName + '_scaleY')
                mc.select(newWorldName)
                mc.pasteKey(newWorldName)

            # sz
            if mc.ls(oldWorldName + '_scaleZ'):
                mc.copyKey(oldWorldName + '_scaleZ')
                mc.select(newWorldName)
                mc.pasteKey(newWorldName)
            
            # 处理约束
            # Master
            nodeMasterConstraints = mc.listConnections(oldMasterName,type = 'parentConstraint')
            nodeMasterConstraintsNeed = []
            if nodeMasterConstraints:
                for node in nodeMasterConstraints:
                    if boatNamespace_Temp not in node:
                        nodeMasterConstraintsNeed.append(node)
            print nodeMasterConstraintsNeed
            
            if nodeMasterConstraintsNeed:
                nodeMasterConstraintsNeed = list(set(nodeMasterConstraintsNeed))
                for constraint in nodeMasterConstraintsNeed:
                    print constraint
                    # translate
                    try:
                        mc.disconnectAttr((oldMasterName + '.translate'), (constraint + '.target[0].targetTranslate'))
                    except:
                        pass
                    mc.connectAttr((newMasterName + '.translate'), (constraint + '.target[0].targetTranslate'))
                    # rotatePivot
                    try:
                        mc.disconnectAttr((oldMasterName + '.rotatePivot'), (constraint + '.target[0].targetRotatePivot'))
                    except:
                        pass
                    mc.connectAttr((newMasterName + '.rotatePivot'), (constraint + '.target[0].targetRotatePivot'))
                    # parentMatrix
                    try:
                        mc.disconnectAttr((oldMasterName + '.parentMatrix[0]'), (constraint + '.target[0].targetParentMatrix'))
                    except:
                        pass
                    mc.connectAttr((newMasterName + '.parentMatrix[0]'), (constraint + '.target[0].targetParentMatrix'))
                    # scale
                    try:
                        mc.disconnectAttr((oldMasterName + '.scale'), (constraint + '.target[0].targetScale'))
                    except:
                        pass
                    mc.connectAttr((newMasterName + '.scale'), (constraint + '.target[0].targetScale'))
                    # rotateOrder
                    try:
                        mc.disconnectAttr((oldMasterName + '.rotateOrder'), (constraint + '.target[0].targetRotateOrder'))
                    except:
                        pass
                    mc.connectAttr((newMasterName + '.rotateOrder'), (constraint + '.target[0].targetRotateOrder'))
                    # rotate
                    try:
                        mc.disconnectAttr((oldMasterName + '.rotate'), (constraint + '.target[0].targetRotate'))
                    except:
                        pass
                    mc.connectAttr((newMasterName + '.rotate'), (constraint + '.target[0].targetRotate'))
                    # rotatePivotTranslate
                    try:
                        mc.disconnectAttr((oldMasterName + '.rotatePivotTranslate'), (constraint + '.target[0].targetRotateTranslate'))
                    except:
                        pass
                    mc.connectAttr((newMasterName + '.rotatePivotTranslate'), (constraint + '.target[0].targetRotateTranslate'))
                
            # World
            nodeWorldConstraints = mc.listConnections(oldWorldName,type = 'parentConstraint')
            nodeWorldConstraintsNeed = []
            if nodeWorldConstraints:
                for node in nodeWorldConstraints:
                    if boatNamespace_Temp not in node:
                        nodeWorldConstraintsNeed.append(node)
            print nodeWorldConstraintsNeed
            
            if nodeWorldConstraintsNeed:
                nodeWorldConstraintsNeed = list(set(nodeWorldConstraintsNeed))
                for constraint in nodeWorldConstraintsNeed:
                    # translate
                    try:
                        mc.disconnectAttr((oldWorldName + '.translate'), (constraint + '.target[0].targetTranslate'))
                    except:
                        pass
                    mc.connectAttr((newWorldName + '.translate'), (constraint + '.target[0].targetTranslate'))
                    # rotatePivot
                    try:
                        mc.disconnectAttr((oldWorldName + '.rotatePivot'), (constraint + '.target[0].targetRotatePivot'))
                    except:
                        pass
                    mc.connectAttr((newWorldName + '.rotatePivot'), (constraint + '.target[0].targetRotatePivot'))
                    # parentMatrix
                    try:
                        mc.disconnectAttr((oldWorldName + '.parentMatrix[0]'), (constraint + '.target[0].targetParentMatrix'))
                    except:
                        pass
                    mc.connectAttr((newWorldName + '.parentMatrix[0]'), (constraint + '.target[0].targetParentMatrix'))
                    # scale
                    try:
                        mc.disconnectAttr((oldWorldName + '.scale'), (constraint + '.target[0].targetScale'))
                    except:
                        pass
                    mc.connectAttr((newWorldName + '.scale'), (constraint + '.target[0].targetScale'))
                    # rotateOrder
                    try:
                        mc.disconnectAttr((oldWorldName + '.rotateOrder'), (constraint + '.target[0].targetRotateOrder'))
                    except:
                        pass
                    mc.connectAttr((newWorldName + '.rotateOrder'), (constraint + '.target[0].targetRotateOrder'))
                    # rotate
                    try:
                        mc.disconnectAttr((oldWorldName + '.rotate'), (constraint + '.target[0].targetRotate'))
                    except:
                        pass
                    mc.connectAttr((newWorldName + '.rotate'), (constraint + '.target[0].targetRotate'))
                    # rotatePivotTranslate
                    try:
                        mc.disconnectAttr((oldWorldName + '.rotatePivotTranslate'), (constraint + '.target[0].targetRotateTranslate'))
                    except:
                        pass
                    mc.connectAttr((newWorldName + '.rotatePivotTranslate'), (constraint + '.target[0].targetRotateTranslate'))
                
            
            # 删除oldRefrence
            rfBoat_Temp = mc.referenceQuery(boatPath_Temp,referenceNode=1)
            mc.file(rfn=rfBoat_Temp , removeReference=1)

    # proxy从anim文件转为tx文件路径
    def sk_proxyAnim2Tx(self):
        if mc.ls('Proxy_Set',type = 'objectSet'):
            objs = mc.sets(mc.ls('Proxy_Set',type = 'objectSet'), q=1)
            if objs:
                for obj in objs:
                    if mc.objExists(obj + '.proxyPath'):
                        path = mc.getAttr(obj + '.proxyPath')
                        # anim版本
                        if '/master/' in path:
                            path = path.replace('/master/','/texture/')
                        if '_ms_anim.' in path:
                            path = path.replace('_ms_anim.','_tx.')
                        # rig版本
                        if '/rigging/' in path:
                            path = path.replace('/rigging/','/texture/')
                        if '_rg.' in path:
                            path = path.replace('_rg.','_tx.')
                        # modle版本
                        if '/model/' in path:
                            path = path.replace('/model/','/texture/')
                        if '_mo.' in path:
                            path = path.replace('_mo.','_tx.')
                        mc.setAttr((obj + '.proxyPath'),path, type = 'string')
                    else:
                        print (u'【 错 误 】\t\t%s' % obj)
            
    # proxy插件补充
    # 把ID补全
    def sk_proxyIDCompleteConfig(self):
        from idmt.maya.py_common import sk_sceneConfig
        # proxySet
        if mc.objExists('Proxy_Set'):
            pass
        else:
            sk_sceneConfig.sk_sceneConfig().sk_sceneProxySetAdd()
        proxyObjs = sk_sceneConfig.sk_sceneConfig().sk_sceneProxySetObjects()
        # proxyID修复
        for proxy in proxyObjs:
            if mc.objExists(proxy.split('|')[-1] + '.proxyID'):
                path = mc.getAttr(proxy.split('|')[-1] + '.proxyPath')
                IDInfo = path.split('/')[-1].split('_')
                proxyID = IDInfo[0] + '_' + IDInfo[1]
                mc.setAttr((proxy + '.proxyID'),proxyID,type = 'string')
                
    # 前期用生成海面材质
    def sk_seaShaderAutoCreate(self):
        objs = mc.ls(sl = 1)
        if objs:
            # 创建材质
            oceanShader = 'sea_SHD'
            if mc.ls( oceanShader ,type = 'lambert'):
                mc.delete( oceanShader )
            # 导入文件
            tempNs = 'foodSeaTemp'
            seaFile = '//file-cluster/GDC/Projects/ZoomWhiteDolphin/Project/data/AssetShader/sea_tex/sea_tex.mb'
            mc.file(seaFile, i=1 , namespace = tempNs , type= 'mayaBinary', preserveReferences=1 , options="v=0")
            mc.namespace(force=1 , moveNamespace=[(':' + tempNs) , ':'])
            mc.namespace(removeNamespace=(':' + tempNs))
            # 赋予物体材质
            shNode = mc.listConnections(oceanShader , d = 1 , type  = 'shadingEngine')[0]
            mc.sets(objs, e=1, forceElement= shNode )
 
    # temp功能
    # tx文件结构统一处理
    def sk_zmTempFileReorganize(self):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        # 获取大环
        masterGrp = mc.ls(sl = 1)
        if masterGrp:
            # 重命名 + 归0
            masterGrp = mc.rename(masterGrp[0],'Master')
            attrs = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
            for attr in attrs:
                if attr not in ['.sx','.sy','.sz']:
                    mc.setAttr((masterGrp + attr) , 0)
                else:
                    mc.setAttr((masterGrp + attr) , 1)
            # 加载大组和MODEL组
            rootGrp = mc.group(name =shotInfo[1],em = 1 )
            modelGrp = mc.group(name ='MODEL',em = 1 )
            # 归组
            mc.parent(masterGrp,modelGrp)
            mc.parent(modelGrp,rootGrp)
            # 自动创建proxy物体
            proxyGrp = mc.polyCube(name= 'MSH_c_hi_proxy_')[0]
            mc.setAttr((proxyGrp + '.ty'),0.5)
            mc.select(proxyGrp)
            mel.eval('DeleteHistory')
            mc.makeIdentity(proxyGrp , apply = 1)
            mc.select(proxyGrp)
            mel.eval('ResetTransformations')
            # 获取Master物体的bbox
            bboxMatrix = mc.exactWorldBoundingBox(masterGrp)
            mc.setAttr((proxyGrp + '.sx'),abs(bboxMatrix[3] - bboxMatrix[0]))
            mc.setAttr((proxyGrp + '.sy'),abs(bboxMatrix[4] - bboxMatrix[1]))
            mc.setAttr((proxyGrp + '.sz'),abs(bboxMatrix[5] - bboxMatrix[2]))
            mc.select(proxyGrp)
            mc.makeIdentity(proxyGrp , apply = 1)
            # proxyShader
            proxyShader = mc.shadingNode ('lambert', asShader=True, name= 'proxyShader')
            mc.setAttr((proxyShader + '.color'),0,1,1,type = 'double3')
            proxySG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name= 'proxySG' )
            mc.connectAttr(('%s.%s') % (proxyShader , 'outColor') , ('%s.%s') % (proxySG , 'surfaceShader'), f=True)
            mc.sets(proxyGrp, e=1, forceElement= proxySG )
            # 放到MODEL组
            mc.parent(proxyGrp,modelGrp)
            # save
            mc.file(save = 1 ,force = 1)

    # 临时工具：选取所有隐藏物体
    def sk_zmGetAllHideObjs(self):
        objs = mc.ls(type = 'transform',l= 1)
        if objs:
            needObjs = []
            for obj in objs:
                if '|MODEL|' in obj and obj[-1] == '_':
                    if mc.getAttr(obj + '.v') == 0:
                        needObjs.append(obj)
            if needObjs:
                mc.select(needObjs)
                
    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # Calimero 参考检测系统
    #-----------------------------------------#
    # Calimero 参考检测系统
    # backType 0 返回缺失的参考信息  | 1 报错缺失的参考信息
    '''
    def sk_zmRefCheck(self,checkType = 'an', backType = 0 ):
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
                print(u'=======！！！本文件丢失参考，请加载必要且正确的参考！！！=======')
                print(u'=======！！！本文件丢失参考，请检查版本有没有用错！！！=======')
                mc.error(u'=======！！！本文件丢失参考，请加载必要的参考！！！=======')
        
        return 0
    '''             
    # 临时工具
    # 选取proxy此类的盒子都变成高模
    # 必须选大环或者proxy
    def sk_zmProxyTransHModel(self):
        from idmt.maya.py_common import sk_sceneConfig
        reload(sk_sceneConfig)

        # 获得选取物的proxy
        objs = mc.ls(sl = 1)
        
        if objs:
            # 获得assetInfo信息
            needAssetInfo = []
            for obj in objs:
                mc.select(obj)
                proxy = sk_sceneConfig.sk_sceneConfig().sk_sceneMasterProxyDetails(1, 0)[0][0]
                proxyID = mc.getAttr(proxy + '.proxyID')
                # 记录 zm_p001002
                needAssetInfo.append(proxyID[:10])
            
            # 获取场景中所有类别的植物信息
            sceneVegetationTypeInfo = sk_sceneConfig.sk_sceneConfig().sk_sceneVegetationTypeInfo()
        
            if sceneVegetationTypeInfo:
                for assetID in needAssetInfo:
                    for assetGrp in sceneVegetationTypeInfo:
                        if assetID in assetGrp[0]:
                            # 处理proxy
                            proxyOldPath = mc.getAttr(assetGrp[2] + '.proxyPath')
                            HTMType = proxyOldPath.split('/')[-1].split('_')[2]
                            if HTMType != 'h':
                                # 更新模型
                                mc.select(assetGrp[2])
                                sk_sceneConfig.sk_sceneConfig().sk_sceneProxyImport(2)
                    
    # 临时工具
    # tx文件全部输出smoothSet
    def sk_zmTxSmoothSetUpadate(self):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        import os
        # 获取项目所有asset ID
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        localInfoPath = localPath + 'smoothSetInfo/'
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        serverInfoPath = serverPath + 'data/AssetInfos/smoothSetInfo/'
        charAsset = allAssetInfo[1]
        propAsset = allAssetInfo[2]
        # 存储错误ID
        errorAssetFile = []
        for i in range(2):
            if i == 0:
                assetInfo = charAsset
                assetType = 'characters'
            if i == 1:
                assetInfo = propAsset
                assetType = 'props'
            if assetInfo:
                for asset in assetInfo:
                    # 获取master路径
                    assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + '/texture/'
                    if os.path.exists(assetServerPath):
                        # 获取文件名
                        assetFiles = mc.getFileList(folder = assetServerPath)
                        if assetFiles:
                            for fileName in assetFiles:
                                # 不允许'_ng_'在文件名里
                                if ('_tx.m') in fileName and shotInfo[0] in fileName and '_ng_' not in fileName:
                                    # 检测smoothSet
                                    mc.file((assetServerPath + fileName),force = 1,open = 1)
                                    result = sk_checkCommon.sk_checkTools().checkModelSmoothSet(shotInfo[0])
                                    if result:
                                        errorAssetFile.append(asset)
                                        errorAssetFile.append(fileName)
                                        errorAssetFile.append(u'--------------------------------------------')
                                    else:
                                        sk_checkCommon.sk_checkTools().checkAssetSmoothSetUpdate()
        # 输出信息
        sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + 'AllAssetSmoothSetCheck.txt'), errorAssetFile)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'AllAssetSmoothSetCheck.txt' ) + '"' + ' ' + '"' + (serverInfoPath + 'AllAssetSmoothSetCheck.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)

    # ZM专用工具
    # 角色道具测试co和dark color
    def sk_zmWDCoCheck(self):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin
        reload(sk_renderLayer_ZoomWhiteDolphin)
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if (shotInfo[1][0] == 'c' or shotInfo[1][0] == 'p') and 'tx.' in shotInfo[3]:
            fileName = mc.file(q = 1 , exn = 1)
            
            meshes = mc.ls(type = 'mesh',l = 1 )
            needObjs = []
            if meshes :
                for mesh in meshes:
                    if '|MODEL' in mesh and '_ca_' in mesh:
                        sgNode = mc.listConnections(mesh ,d = 1 ,type = 'shadingEngine')
                        if sgNode:
                            if sgNode[0] != 'initialParticleSE' and sgNode[0] != 'initialShadingGroup':
                                obj = mc.listRelatives(mesh ,p = 1 ,type = 'transform')[0]
                                needObjs.append(obj)
            if needObjs:
                for i in range(2):
                    if i == 0:
                        mc.createRenderLayer((needObjs) , name='zm_temp' , noRecurse=1 , makeCurrent=1)
                        sk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLWDColorcheck(needObjs ,0 )
                    else:
                        mc.file(fileName ,open = 1 , force = 1)
                        mc.createRenderLayer((needObjs) , name='zm_temp' , noRecurse=1 , makeCurrent=1)
                        sk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLWDColorcheck(needObjs ,1 )
                        
            mc.file(fileName ,open = 1 , force = 1)
            print '\n'
            print u'=================恭喜！本文件能通过WhiteCO和DarkCO渲染层================='
        
    # 临时工具
    # 将render文件smoothSet还原
    def sk_zmSmoothSetRenderImport(self):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        from idmt.maya.py_common import sk_smoothSet
        reload(sk_smoothSet)
        import os
        # 获取项目所有asset ID
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        charAsset = allAssetInfo[1]
        propAsset = allAssetInfo[2]
        # 存储错误ID
        for i in range(2):
            if i == 0:
                assetInfo = charAsset
                assetType = 'characters'
            if i == 1:
                assetInfo = propAsset
                assetType = 'props'
            # 寻找到render文件
            if assetType:
                for j in range(len(assetInfo)):
                    asset = assetInfo[j]
                    assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + '/master/'
                    if os.path.exists(assetServerPath):
                        # 获取文件名
                        assetFiles = mc.getFileList(folder = assetServerPath)
                        if assetFiles:
                            for fileName in assetFiles:
                                # 不允许'_ng_'在文件名里
                                if '_ms_render.m' in fileName and shotInfo[0] in fileName and '_ng_' in fileName:
                                    # 判断该render文件有没有smoothSet文件
                                    fileInfos = fileName.split('_')
                                    serverSmoothSetInfoPath = serverPath + 'data/AssetInfos/smoothSetInfo/' + fileInfos[0] + '/' + fileInfos[1] + '/' + fileInfos[2] + '/'
                                    smoothSetFiles = mc.getFileList(folder = serverSmoothSetInfoPath)
                                    if smoothSetFiles:
                                        if 'smooth_0.txt' in smoothSetFiles and 'smooth_1.txt' in smoothSetFiles and 'smooth_2.txt' in smoothSetFiles:
                                            mc.file((assetServerPath + fileName),force = 1 ,open = 1)
                                            objsSmoothSet_lv0 = sk_infoConfig.sk_infoConfig().checkFileRead(serverSmoothSetInfoPath + 'smooth_0.txt')
                                            if objsSmoothSet_lv0:
                                                needObjs = []
                                                for obj in objsSmoothSet_lv0:
                                                    if mc.ls(obj):
                                                        objName = mc.ls(obj,l = 1)[0]
                                                        if '|MODEL|' in objName and '_si_' not in obj and  '_nr_' not in obj and '_proxy_' not in obj:
                                                            needObjs.append(obj)
                                                objsSmoothSet_lv0 = needObjs
                                                mc.select(objsSmoothSet_lv0)
                                                sk_smoothSet.sk_smoothSetTools().smoothSetAdd(1,0)
                                            objsSmoothSet_lv1 = sk_infoConfig.sk_infoConfig().checkFileRead(serverSmoothSetInfoPath + 'smooth_1.txt')
                                            if objsSmoothSet_lv1:
                                                needObjs = []
                                                for obj in objsSmoothSet_lv1:
                                                    if mc.ls(obj):
                                                        objName = mc.ls(obj,l = 1)[0]
                                                        if '|MODEL|' in objName and '_si_' not in obj and  '_nr_' not in obj and '_proxy_' not in obj:
                                                            needObjs.append(obj)
                                                objsSmoothSet_lv1 = needObjs
                                                mc.select(objsSmoothSet_lv1)
                                                sk_smoothSet.sk_smoothSetTools().smoothSetAdd(1,1)
                                            objsSmoothSet_lv2 = sk_infoConfig.sk_infoConfig().checkFileRead(serverSmoothSetInfoPath + 'smooth_2.txt')
                                            if objsSmoothSet_lv2:
                                                needObjs = []
                                                for obj in objsSmoothSet_lv2:
                                                    if mc.ls(obj):
                                                        objName = mc.ls(obj,l = 1)[0]
                                                        if '|MODEL|' in objName and '_si_' not in obj and  '_nr_' not in obj and '_proxy_' not in obj:
                                                            needObjs.append(obj)
                                                objsSmoothSet_lv2 = needObjs
                                                mc.select(objsSmoothSet_lv2)
                                                sk_smoothSet.sk_smoothSetTools().smoothSetAdd(1,2)
                                            mc.file(save = 1 ,force = 1)
    
    # 临时工具
    # locator box 位移，旋转 连接
    def sk_zmLoc2Box(self):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        locs = mc.ls(sl = 1)
        attrsT = sk_infoConfig.sk_infoConfig().checkBaseAttrs('t')
        attrsR = sk_infoConfig.sk_infoConfig().checkBaseAttrs('r')
        attrs = attrsT + attrsR
        if locs:
            for loc in locs:
                box = mc.polyCube()[0]
                box = mc.rename(box,(loc + '_box'))
                for attr in attrs:
                    mc.connectAttr((loc + attr), (box + attr))


    # WCO和DCO分辨
    # wdType 0    dark | 1    white
    def zmRLWDColorErrorCheck(self ):
        # Shader记录
        whiteColorShader = ''
        darkColorShader = ''
        errorList = []
        # 获取mesh的SG节点
        objs = []
        meshes = mc.ls(type = 'mesh')
        if meshes:
            for mesh in meshes:
                objs.append(mc.listRelatives(mesh,p=1,type = 'transform')[0])
                
        SGNodes = []
        
        if objs:
            for obj in objs:
                mesh = mc.listRelatives(obj , s = 1 , ni = 1,f= 1)
                if mesh:
                    mesh = mesh[0]
                    shaderSG = mc.listConnections(mesh,d = 1, type = 'shadingEngine')
                    if shaderSG:
                        SGNodes = SGNodes + shaderSG
        
        if SGNodes:
            SGNodes = list(set(SGNodes))
            # 获取WCO和DCO
            for node in SGNodes:
                # 获取colorShader
                colorShader = mc.listConnections( (node + '.surfaceShader') , s = 1)
                if colorShader:
                    colorShader = colorShader[0]
                    # 获取colorRamp
                    rampShader = mc.listConnections( (colorShader + '.color') ,s = 1)
                    if rampShader:
                        rampShader = rampShader[0]
                        # ramp节点引入点
                        #rampInputs = mc.listAttr((rampShader + '.colorEntryList') , m = 1)
                        if mc.nodeType(rampShader) == 'ramp':
                            rampInputs = mc.getAttr((rampShader + '.colorEntryList'),mi = 1)
                            if rampInputs:
                                needRampInputs = rampInputs[:]
                                if len(needRampInputs) < 2:

                                    errorList.append(rampShader)
                                    #mc.error(u'==============[%s]do not have 2 or more inputs'%rampShader)
                        else:
                            errorList.append(rampShader)
        return errorList
    
    # 临时工具
    # 将角色道具的render,tx,rg文件，进行处理，设置上牙齿的显示
    def sk_zmUpteethModify(self):   
        # 获取asset信息
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        from idmt.maya.py_common import sk_smoothSet
        reload(sk_smoothSet)
        import os
        # 获取项目所有asset ID
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        charAsset = allAssetInfo[1]
        propAsset = allAssetInfo[2]
        for i in range(2):
            if i == 0:
                assetInfo = charAsset
                assetType = 'characters'
            if i == 1:
                assetInfo = propAsset
                assetType = 'props'
            for asset in assetInfo:
                for j in range(3):
                    assetServerPath = ''
                    # render
                    if j == 0:
                        needFolder = '/master/'
                        fileKeyInfo = '_render.m'
                    # tx
                    if j == 1:
                        needFolder = '/texture/'
                        fileKeyInfo = '_tx.m'
                    # rg
                    if j == 2:
                        needFolder = '/rigging/'
                        fileKeyInfo = '_rg.m'
                    assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + needFolder
                    if os.path.exists(assetServerPath):
                        # 获取文件名
                        assetFiles = mc.getFileList(folder = assetServerPath)
                        if assetFiles:
                            for fileName in assetFiles:
                                if fileKeyInfo in fileName  and shotInfo[0] in fileName and '_ng_' not in fileName:
                                    checkFile = assetServerPath + fileName
                                    print u'-------'
                                    print fileName
                                    mc.file(checkFile ,open = 1, force = 1 , loadReferenceDepth = 'none' )
                                    # 处理好牙齿信息
                                    if mc.ls('MODEL'):
                                        meshes = mc.listRelatives('MODEL', ad = 1 ,type = 'mesh',f = 1)
                                        if meshes:
                                            for mesh in meshes:
                                                objGrp = mc.listRelatives(mesh ,p=1 ,type = 'transform',f = 1)[0]
                                                if '_si_' not in objGrp and  '_nr_' not in objGrp and '_proxy_' not in objGrp and '_ca_' in objGrp:
                                                    meshReal = mc.listRelatives(objGrp ,ni = 1, c = 1 ,type = 'mesh')[0]
                                                    mc.setAttr((meshReal + '.castsShadows'),1)
                                                    mc.setAttr((meshReal + '.receiveShadows'),1)
                                                    mc.setAttr((meshReal + '.motionBlur'),1)
                                                    mc.setAttr((meshReal + '.primaryVisibility'),1)
                                                    mc.setAttr((meshReal + '.smoothShading'),1)
                                                    mc.setAttr((meshReal + '.visibleInReflections'),1)
                                                    mc.setAttr((meshReal + '.visibleInRefractions'),1)
                                            mc.file(save = 1,force = 1)
                
        
    # 临时工具
    # 表达式作弊工具？
    def sk_zmTempTempRigConfig(self):  
        # 关闭表达式
        exNodes = mc.ls(type = 'expression')
        if exNodes:
            for exNode in exNodes :
                try:
                    mc.setAttr((exNode + '.nodeState') , 2)
                except:
                    pass
        # 创建scriptNode
        if mc.ls('IDMT_RG_CTRL'):
            mc.delete('IDMT_RG_CTRL')
        scriptNode = mc.scriptNode(n = 'IDMT_RG_CTRL',bs = 'import idmtRgCtrlPerform\nidmtRgCtrlPerform.idmtEnvOpenConfig()',afterScript = 'import idmtRgCtrlPerform\nidmtRgCtrlPerform.idmtFixEnv()',stp = 'python')
    
    ''' 
    def sk_zmTempTempRigConfigBatch(self):
        serverPath = 'Z:/Scratch/sk/rg_temp_files/'
        mayaFiles = mc.getFileList(folder = serverPath)
        for tempFile in mayaFiles:
            assetType = tempFile.split('_')[1][0]
            if assetType not in ['s', 'S']:
                # 打开清理
                mc.file((serverPath + tempFile) ,open = 1, force = 1 , loadReferenceDepth = 'none' )
                self.sk_zmTempTempRigConfig()
                # 保存
                assetAnimName = tempFile.split('_temp')[0] + tempFile.split('_temp')[1]
                # rg处理
                assetRgName = assetAnimName.replace('_ms_anim.','_rg.')
                # 保存
                localPath = 'E:/temp_files/'
                fileName = ''
                
                if assetType == 'c':
                    localPath = localPath + tempFile.split('_')[1] + '/master/'
                    fileName = assetAnimName
                if assetType == 'p':
                    localPath = localPath + tempFile.split('_')[1] + '/rg/'
                    fileName = assetRgName
                mc.sysFile(localPath, makeDir=True)
                mc.file(rename =(localPath + fileName) )
                mc.file(force = 1 , save = 1)
    '''   
    # 临时工具
    # 将所有asset的tx文件输出透明贴图信息
    def sk_zmAssetTextureInfoExportBatch(self):   
        # 获取asset信息
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        from idmt.maya.py_common import sk_smoothSet
        reload(sk_smoothSet)
        import os
        # 获取项目所有asset ID
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        charAsset = allAssetInfo[1]
        propAsset = allAssetInfo[2]
        setAsset = allAssetInfo[3]
        for i in range(3):
            if i == 0:
                assetInfo = charAsset
                assetType = 'characters'
            if i == 1:
                assetInfo = propAsset
                assetType = 'props'
            if i == 2:
                assetInfo = setAsset
                assetType = 'sets'
            for asset in assetInfo:
                assetServerPath = ''
                # tx
                needFolder = '/texture/'
                fileKeyInfo = '_tx.m'
                assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + needFolder
                if os.path.exists(assetServerPath):
                    # 获取文件名
                    assetFiles = mc.getFileList(folder = assetServerPath)
                    if assetFiles:
                        for fileName in assetFiles:
                            # 不允许'_ng_'在文件名里
                            if fileKeyInfo in fileName  and shotInfo[0] in fileName and '_ng_' not in fileName:
                                checkFile = assetServerPath + fileName
                                print u'-------'
                                print fileName
                                mc.file(checkFile ,open = 1, force = 1 , loadReferenceDepth = 'all' )
                                # 输出透明信息
                                sk_checkCommon.sk_checkTools().checkTransparencyObjsInfoExport()

    # 临时
    # 全局扫描 fs文件处理
    def sk_zmFsRefEditListConfig(self):
        # 获取asset信息
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)

        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        import os
        # 处理范围
        configList = [101,102,103,104]
        #shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        for checkNum in configList:
            episodeServerPath = serverPath + 'scenes/Animation/episode_' + str(checkNum) + '/'
            if os.path.exists(episodeServerPath):
                shotFolders = mc.getFileList(folder = episodeServerPath)
                if shotFolders:
                    for shotNum in shotFolders:
                        if 'scene_' in shotNum:
                            fsServerFile = episodeServerPath + shotNum + '/finishing/'
                            if os.path.exists(fsServerFile):
                                fsFiles = mc.getFileList(folder = fsServerFile)
                                if fsFiles:
                                    for fsFile in fsFiles:
                                        if '_fs_' in fsFile and '.m' in fsFile:
                                            mc.file((fsServerFile + fsFile) ,open = 1 ,force = 1 , loadReferenceDepth = 'none')
                                            # 处理参考列表
                                            sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
                                            # 保存
                                            mc.file(save = 1, force = 1)
                                            
    # 全局扫描
    # 将所有asset的tx文件white|dark信息
    def sk_sceneGlobalAssetWDRampInfoExport(self):   
        # 获取asset信息
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        import sk_renderLayer_ZoomWhiteDolphin
        reload(sk_renderLayer_ZoomWhiteDolphin)
        import os
        # 获取项目所有asset ID
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        charAsset = allAssetInfo[1]
        propAsset = allAssetInfo[2]
        setAsset = allAssetInfo[3]
        for i in range(2):
            if i == 0:
                assetInfo = charAsset
                assetType = 'characters'
            if i == 1:
                assetInfo = propAsset
                assetType = 'props'
            for asset in assetInfo:
                assetServerPath = ''
                # tx
                needFolder = '/texture/'
                fileKeyInfo = '_tx.m'
                assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + needFolder
                if os.path.exists(assetServerPath):
                    # 获取文件名
                    assetFiles = mc.getFileList(folder = assetServerPath)
                    if assetFiles:
                        for fileName in assetFiles:
                            # 不允许'_ng_'在文件名里
                            if fileKeyInfo in fileName  and shotInfo[0] in fileName and '_ng_' not in fileName:
                                checkFile = assetServerPath + fileName
                                print u'-------'
                                print fileName
                                mc.file(checkFile ,open = 1, force = 1 , loadReferenceDepth = 'all' )
                                # 输出Ramp信息
                                sk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLWDInfoExport()
        # 输出路径
        print u'/n=====请到下面路径查询[全asset]wdRamp信息====='
        print (serverPath + 'data/AssetInfos/wdRampInfo/')
        
    # 全局扫描
    # 将所有asset的tx文件white|dark信息
    def sk_sceneGlobalAssetWDRampErrorInfoExport(self):   
        # 获取asset信息
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        import sk_renderLayer_ZoomWhiteDolphin
        reload(sk_renderLayer_ZoomWhiteDolphin)
        import os
        # serverInfoPath
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        localInfoPath = localPath + 'wdRampErrorInfo/'
        mc.sysFile(localInfoPath, makeDir=True)
        serverInfoPath = serverPath + 'data/AssetInfos/wdRampErrorInfo/'
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverInfoPath + '\",\"\",1)'
        mel.eval(makeDirCMD)
        # 清理掉历史文件
        localOldFiles = mc.getFileList(folder = localInfoPath)
        if localOldFiles:
            for oldFile in localOldFiles:
                mc.sysFile((localInfoPath + oldFile) , delete = 1)
        print u'======本地历史文件清理完毕======'
        serverOldFiles = mc.getFileList(folder = serverInfoPath)
        if serverOldFiles:
            for oldFile in serverOldFiles:
                cmd = 'zwSysFile(\"del\",\"' + (serverInfoPath + oldFile) + '\",\"\",1)'
                mel.eval(cmd)
        print u'======服务器端历史文件清理完毕======'
        # 获取项目所有asset ID
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        charAsset = allAssetInfo[1]
        propAsset = allAssetInfo[2]
        setAsset = allAssetInfo[3]
        for i in range(2):
            if i == 0:
                assetInfo = charAsset
                assetType = 'characters'
            if i == 1:
                assetInfo = propAsset
                assetType = 'props'
            for asset in assetInfo:
                assetServerPath = ''
                # tx
                needFolder = '/master/'
                fileKeyInfo = '_ms_render.m'
                assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + needFolder
                if os.path.exists(assetServerPath):
                    # 获取文件名
                    assetFiles = mc.getFileList(folder = assetServerPath)
                    if assetFiles:
                        for fileName in assetFiles:
                            # 不允许'_ng_'在文件名里
                            if fileKeyInfo in fileName  and shotInfo[0] in fileName and '_ng_' not in fileName:
                                checkFile = assetServerPath + fileName
                                print u'-------'
                                print fileName
                                mc.file(checkFile ,open = 1, force = 1 , loadReferenceDepth = 'all' )
                                # 检测信息
                                errorList = self.zmRLWDColorErrorCheck()
                                if errorList:
                                    mc.sysFile((localInfoPath + asset), makeDir=True)
                                    sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + asset + '_wdEorro.txt'), errorList)
                                    updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + asset + '_wdEorro.txt' ) + '"' + ' ' + '"' + (serverInfoPath + asset + '_wdEorro.txt') + '"' + ' true'
                                    mel.eval(updateAnimCMD)
        # 输出路径
        print u'/n=====请到下面路径查询[全asset]wdRamp信息====='
        print (serverPath + 'data/AssetInfos/wdRampErrorInfo/')
        
    
    # 单贴图自动分叉。自动创建一个file节点承载黑白alpha贴图
    def sk_zmTransparencyNodesCreate(self):
        meshes=mc.ls(type='mesh',l=1)
        NeedSGNodes = []
        if meshes:
            for mesh in meshes:
                shadeSGs=mc.listConnections(mesh,type='shadingEngine',d=1)
                if shadeSGs:
                    NeedSGNodes = NeedSGNodes + shadeSGs
        
        NeedSGNodes = list(set(NeedSGNodes))
        
        if NeedSGNodes:
            for shadeSG in NeedSGNodes:
                shader=mc.listConnections((shadeSG+".surfaceShader"),s=1,d=0)
                if shader:
                    shader = shader[0]
                    if mc.nodeType(shader)=='lambert':
                        transAttr = '.transparency'
                        colorShader = mc.listConnections((shader+'.color'),s =1 ,plugs = 1)
                    if mc.nodeType(shader)=='surfaceShader':
                        transAttr = '.outTransparency'
                        colorShader = mc.listConnections((shader+'.outColor'),s =1 ,plugs = 1)
                    transparencyShader = mc.listConnections((shader+transAttr),s =1 ,plugs = 1)
                    if colorShader and transparencyShader:
                        if mc.nodeType(colorShader[0].split('.')[0]) == 'file':
                            mc.setAttr((colorShader[0].split('.')[0] + '.filterType'),0)
                        if colorShader[0].split('.')[0] == transparencyShader[0].split('.')[0]:
                            mc.disconnectAttr((colorShader[0].split('.')[0]+'.outTransparency'),(shader+transAttr))
                            texturePath = mc.getAttr(colorShader[0].split('.')[0] + '.fileTextureName')
                            # new file
                            newFileNode = mc.shadingNode('file',asTexture=True)
                            mc.setAttr((newFileNode+'.fileTextureName'),(texturePath.split('.')[0]+'_alpha_.'+texturePath.split('.')[-1]),type="string")
                            mc.setAttr((newFileNode+'.filterType'),0)
                            mc.setAttr((newFileNode+'.invert'),1)
                            mc.connectAttr( (newFileNode+'.outColor'), (shader + transAttr) )
                            # new plasce2D
                            newPlaceNode =mc.shadingNode('place2dTexture',asUtility=True)
                            attrs = ['.coverage','.uvFilterSize','.uvCoord','.vertexCameraOne','.vertexUvThree','.vertexUvOne','.vertexUvTwo','.noiseUV','.rotateUV','.offset','.repeatUV','.wrapV','.wrapU','.stagger','.mirrorV','.mirrorU','.rotateFrame','.translateFrame']
                            for attr in attrs:
                                mc.connectAttr((newPlaceNode + attr),(newFileNode+attr),f = 1)
                            print (shader + '    :    Done')
                                            

    # 临时工具
    # 将所有asset的render文件MODEL组解锁
    def sk_zmAssetRenderModelConfig(self):   
        # 获取asset信息
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        import os
        # 获取项目所有asset ID
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        charAsset = allAssetInfo[1]
        propAsset = allAssetInfo[2]
        for i in range(2):
            if i == 0:
                assetInfo = charAsset
                assetType = 'characters'
            if i == 1:
                assetInfo = propAsset
                assetType = 'props'
            for asset in assetInfo:
                assetServerPath = ''
                # tx
                needFolder = '/master/'
                fileKeyInfo = '_ms_render.m'
                assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + needFolder
                if os.path.exists(assetServerPath):
                    # 获取文件名
                    assetFiles = mc.getFileList(folder = assetServerPath)
                    if assetFiles:
                        for fileName in assetFiles:
                            # 不允许'_ng_'在文件名里
                            if fileKeyInfo in fileName  and shotInfo[0] in fileName and '_ng_' not in fileName:
                                checkFile = assetServerPath + fileName
                                mc.file(checkFile ,open = 1, force = 1 , loadReferenceDepth = 'all' )
                                sk_sceneTools.sk_sceneTools().checkLockObjs(['MODEL'],1)
                                mc.file(save = 1,force = 1)


    # 全局扫描
    # 所有asset的anim及render文件MR插件检测
    def sk_sceneGlobalAssetMRCheck(self):   
        # 获取asset信息
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        import sk_renderLayer_ZoomWhiteDolphin
        reload(sk_renderLayer_ZoomWhiteDolphin)
        import os
        # serverInfoPath
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        localInfoPath = localPath + 'mrCheck/'
        mc.sysFile(localInfoPath, makeDir=True)
        serverInfoPath = serverPath + 'data/AssetInfos/mrCheck/'
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverInfoPath + '\",\"\",1)'
        mel.eval(makeDirCMD)
        # 清理掉历史文件
        localOldFiles = mc.getFileList(folder = localInfoPath)
        if localOldFiles:
            for oldFile in localOldFiles:
                mc.sysFile((localInfoPath + oldFile) , delete = 1)
        print u'======本地历史文件清理完毕======'
        serverOldFiles = mc.getFileList(folder = serverInfoPath)
        if serverOldFiles:
            for oldFile in serverOldFiles:
                cmd = 'zwSysFile(\"del\",\"' + (serverInfoPath + oldFile) + '\",\"\",1)'
                mel.eval(cmd)
        print u'======服务器端历史文件清理完毕======'
        
        checkErrorInfos = []
        
        sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath +  'mrCheck.txt'), [])
        
        # 获取项目所有asset ID
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        charAsset = allAssetInfo[1]
        propAsset = allAssetInfo[2]
        setAsset = allAssetInfo[3]
        envAsset = allAssetInfo[4]
        for i in range(4):
            if i == 0:
                assetInfo = charAsset
                assetType = 'characters'
            if i == 1:
                assetInfo = propAsset
                assetType = 'props'
            if i == 2:
                assetInfo = setAsset
                assetType = 'sets'
            if i == 3:
                assetInfo = envAsset
                assetType = 'environments'
            for asset in assetInfo:
                assetServerPath = ''
                # anim及render
                needFolder = '/master/'
                allFileKeyInfos = ['_ms_anim.m','_ms_render.m']
                for fileKeyInfo in allFileKeyInfos:
                    assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + needFolder
                    if os.path.exists(assetServerPath):
                        # 获取文件名
                        assetFiles = mc.getFileList(folder = assetServerPath)
                        if assetFiles:
                            for fileName in assetFiles:
                                # 不允许'_ng_'在文件名里
                                if fileKeyInfo in fileName  and shotInfo[0] in fileName and '_ng_' not in fileName:
                                    # 清理默认的mr
                                    mc.file(f=1, new=1)
                                    try:
                                        mel.eval('unloadPlugin "Mayatomr"')
                                    except:
                                        pass
                                    # 打开文件检测
                                    checkFile = assetServerPath + fileName
                                    print u'-------'
                                    print fileName
                                    try:
                                        mc.file(checkFile ,open = 1, force = 1 , loadReferenceDepth = 'all' )
                                    except:
                                        pass
                                    # 检测信息
                                    mrState = mc.pluginInfo('Mayatomr' , loaded = 1 , q = 1)
                                    #mrNodes = mc.ls(type='mentalrayGlobals')+ mc.ls(type='mentalrayItemsList') +mc.ls(type='mentalrayOptions')
                                    if mrState:
                                        checkErrorInfos = [fileName]
                                    # 统一记录
                                    if checkErrorInfos:
                                        print '\n'
                                        print '===============start'
                                        print '\n'
                                        mc.sysFile((localInfoPath), makeDir=True)
                                        print (localInfoPath +  'mrCheck.txt')
                                        sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath +  'mrCheck.txt'), checkErrorInfos, addtion = 1)
                                        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath +  'mrCheck.txt' ) + '"' + ' ' + '"' + (serverInfoPath +  'mrCheck.txt') + '"' + ' true'
                                        mel.eval(updateAnimCMD)
        # 输出路径
        print u'/n=====请到下面路径查询[全asset]MRRamp信息====='
        print (serverPath + 'data/AssetInfos/mrCheck/')
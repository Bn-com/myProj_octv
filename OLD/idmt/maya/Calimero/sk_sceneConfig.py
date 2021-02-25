# -*- coding: utf-8 -*-

'''
Created on 2013-6-19

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

class sk_sceneConfig(object):
    def __init__(self):
        sk_proxyTypeAllInfo = []
        
    '''
           【系统】 【UI篇】【动画】【camer工具集】
    '''
    # camera工具集
    def sk_sceneUICameraTools(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        
        # 窗口
        if mc.window ("sk_sceneUICameraTools", ex=1):
            mc.deleteUI("sk_sceneUICameraTools", window=True)
        mc.window("sk_sceneUICameraTools", title="Camera Tools", widthHeight=(150, 120), menuBar=0)
        # 主界面
        mc.columnLayout()

        # 行按钮
        mc.rowLayout()
        # 文件asset
        mc.button(w=150 , h=30 , bgc=[0, 1, 0.2], label=(unicode('【动画】打开文件系统', 'utf8')) , c='mel.eval(\"zwAssetFile\")')
        mc.setParent("..")

        # 行按钮
        mc.rowLayout()
        # 我的规则是，import了scene类，于是这里可以直接用起来
        mc.button(w=150 , h=30 , bgc=[0, 1, 0.2], label=(unicode('【动画】导入音频及相机', 'utf8')) , c='sk_sceneConfig.sk_sceneConfig().sk_sceneImportCameraAudioFrame()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150 , h=30 , bgc=[0.6, 0.2, 0.2], label=(unicode('【动画】导出最终相机', 'utf8')), c='sk_sceneConfig.sk_sceneConfig().sk_sceneCameraUpdate()')
        mc.setParent("..")
        # newCmd = r"zwSysFile  \"copy\" \"" + camTempPath + r"\" \"" + camServerPath + r"\" 1"

        mc.rowLayout()
        mc.button(w=150 , h=30 , bgc=[0, 0.5, 1], label=(unicode('【通用】参考最终相机', 'utf8'))  , c='mel.eval(\'source zwCameraImportExport.mel; zwGetCameraUI;\')')
        mc.setParent("..")
        
        mc.setParent("..")
        mc.showWindow("sk_sceneUICameraTools")

    '''
           【系统】 【核心】【Camera Bake及Update】
    '''
    # camera导出更新
    def sk_sceneCameraUpdate(self,batchUpadate = 0):
        import sk_infoConfig
        reload(sk_infoConfig)
        import sk_referenceConfig
        reload(sk_referenceConfig)
        import sk_checkCommon
        reload(sk_checkCommon)
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
        camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
        # 获取真正cam 居然有|cam_102_001|cam_102_001的情况
        camList = mc.ls(camSourceName,l=1)
        needCam = ''
        if camList:
            for cam in camList:
                if mc.listRelatives(cam,s=1,ni=1,type = 'camera'):
                    needCam = cam
                if mc.nodeType(cam) == 'camera':
                    mc.rename(mc.ls(cam,l=1)[0],(cam+'Shape'))
        else:
            mc.error(u'=============找不到对应镜头的CAM=============')
        camBakeName = camSourceName + '_baked'
        print camBakeName
        # bakeCame
        if mc.ls(camBakeName):
            mc.delete(camBakeName)
        if needCam:
            mc.select(needCam)
        else:
            mc.error(u'=============找不到对应镜头的CAM=============')
        mel.eval('source \"//file-cluster/GDC/Resource/Support/Maya/2013/zwCameraImportExport.mel\"')
        mel.eval('zwBakeCamera')
        mc.select(camBakeName)
        # 相机Export
        import sk_hbExceptCam
        reload(sk_hbExceptCam)
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
    

    '''
            【系统】 【UI篇】【前期】【prxy系统UI】
    '''
    # 场景工具集
    def sk_sceneProxyConfigUI(self):        
        import sk_referenceConfig
        reload(sk_referenceConfig)
        
        # 窗口
        if mc.window ("sk_sceneProxyConfigUI", ex=1):
            mc.deleteUI("sk_sceneProxyConfigUI", window=True)

        mc.window("sk_sceneProxyConfigUI", title=unicode('===AssetScene处理===', "utf8"), widthHeight=(170, 260), menuBar=0)
        
        # 面板
        form = mc.formLayout()
        # 切换面板
        tabs = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout(form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
       
        # ===Proxy参考处理===
        child1 = mc.rowColumnLayout()

        # ===Proxy参考处理===
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0, 0, 0.0], label=(unicode('===Proxy参考处理===', 'utf8')))
        mc.setParent("..")   

        # 【选取】proxy【对位】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【选取】proxy【对位】', 'utf8')), c='sk_sceneConfig.sk_sceneConfig().sk_sceneProxyMoveConfig()')
        mc.setParent("..")

        # 【只保留】【proxy】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【只保留】【proxy】', 'utf8')), c='sk_sceneConfig.sk_sceneConfig().sk_sceneMasterDelete()')
        mc.setParent("..")   

        # 【清理】【合并】Set
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【清理】【合并】Set', 'utf8')), c='sk_sceneConfig.sk_sceneConfig().sk_sceneSetCombineConfig(\"ZM\")')
        mc.setParent("..")  
        
        # 【Asset替换系统】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【Asset替换系统】', 'utf8')), c='sk_sceneConfig.sk_sceneConfig().sk_UIProxyReplaceSys()')
        mc.setParent("..")  

        # 【同类替换系统】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【同类替换系统】', 'utf8')), c='food = sk_sceneConfig.sk_sceneConfig().sk_sceneProxyReplaceUI()')
        mc.setParent("..")
      
        # 【更新】【选取】【同类】第一物
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【更新】【选取】【同类】第一物', 'utf8')), c='food = sk_sceneConfig.sk_sceneConfig().sk_sceneProxyAssetNO1Update()')
        mc.setParent("..")
        
        # 【Proxy】批量【Instance】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.7, 0.45, 0.1], label=(unicode('【Proxy】批量【Instance】', 'utf8')), c='food = sk_sceneConfig.sk_sceneConfig().sk_sceneProxyInstanceUI()')
        mc.setParent("..")

        '''
        # 【流氓法】自动恢复模型
        mc.rowLayout()
        mc.button(w = 160 , h = 30 ,bgc = [0.1,0.45,0.1],label = (unicode('【流氓法】自动恢复模型', 'utf8')),c = 'sk_sceneConfig.sk_sceneConfig().sk_sceneBugsCombine()')
        mc.setParent("..")  
        '''

        mc.setParent("..")
        
        # ===Proxy修正处理===
        child2 = mc.rowColumnLayout()

        # ===Proxy参考处理===
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0, 0, 0.0], label=(unicode('===Proxy修正处理===', 'utf8')))
        mc.setParent("..")   

        # 【创建】proxySet
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【创建】proxySet', 'utf8')), c='sk_sceneConfig.sk_sceneConfig().sk_sceneProxySetAdd()')
        mc.setParent("..")

        # 【清理】所有【空组】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【清理】所有【空组】', 'utf8')), c='mel.eval(\"deleteEmptyGroups()\")')
        mc.setParent("..")

        # 提取【空】proxy
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('提取【空】proxy', 'utf8')), c='sk_sceneConfig.sk_sceneConfig().sk_sceneProxyDebugCheck()')
        mc.setParent("..")

        # proxy【重命名】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('proxy【重命名】', 'utf8')), c='sk_sceneConfig.sk_sceneConfig().sk_sceneProxyGrpLevelRename(0)')
        mc.setParent("..")

        # 【显示|隐藏】所有proxy
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【显示|隐藏】所有proxy', 'utf8')), c='sk_sceneConfig.sk_sceneConfig().sk_sceneProxySetObjectsHide()')
        mc.setParent("..")

        # proxy【位移】【修正】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('proxy【位移】【修正】', 'utf8')), c='food = sk_sceneConfig.sk_sceneConfig().sk_sceneProxyUpGroupMoveConfig()')
        mc.setParent("..")

        # 【选取】所有proxy
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【选取】所有proxy', 'utf8')), c='food = sk_sceneConfig.sk_sceneConfig().sk_sceneProxySetObjects()\nmc.select(food)')
        mc.setParent("..")


        mc.setParent("..")
        
        # ===Asset参考处理===
        child3 = mc.rowColumnLayout()

        # ===Asset参考处理===
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0, 0, 0.0], label=(unicode('===Asset参考处理===', 'utf8')))
        mc.setParent("..")   

        # 高低模
        mc.rowLayout(numberOfColumns=2  , adjustableColumn=2)
        
        mc.columnLayout()
        mc.optionMenuGrp('sk_AssetReferenceSourceType', label=(unicode('原始', 'utf8')), bgc=[0.1, 0.1, 0.4], w=80, adjustableColumn=1)
        mc.menuItem(label='_h_')
        mc.menuItem(label='_m_')
        mc.menuItem(label='_l_')
        mc.setParent("..")   
        
        mc.columnLayout()
        mc.optionMenuGrp('sk_AssetReferenceReplaceType', label=(unicode('替换', 'utf8')), bgc=[0.4, 0.1, 0.1], w=80, adjustableColumn=1)
        mc.menuItem(l='_h_')
        mc.menuItem(l='_m_')
        mc.menuItem(l='_l_')
        mc.setParent("..")   
        
        mc.setParent("..")   
        
        # 【选取物】参考【替换】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【选取物】参考【替换】', 'utf8')), c='sk_sceneConfig.sk_sceneConfig().sk_sceneReferenceReplace(1)')
        mc.setParent("..")   

        # 【所有】参考物【替换】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【所有】参考物【替换】', 'utf8')), c='sk_sceneConfig.sk_sceneConfig().sk_sceneReferenceReplace(2)')
        mc.setParent("..")   
        
        
        # 【移除】【选取物参考】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【移除】【选取物参考】', 'utf8')), c='refNodes = sk_referenceConfig.sk_referenceConfig().checkReferenceGetInfo()\nif refNodes:\n\tfor ref in refNodes:\n\t\tsk_referenceConfig.sk_referenceConfig().checkReferenceDelete(ref)')
        mc.setParent("..")   
        
        # 【Unload】【选取参考】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【Unload】【选取参考】', 'utf8')), c='refNodes = sk_referenceConfig.sk_referenceConfig().checkReferenceGetInfo()\nif refNodes:\n\tfor ref in refNodes:\n\t\tsk_referenceConfig.sk_referenceConfig().checkReferenceUnload(ref)')
        mc.setParent("..")        

        # 【ShareNodes】【处理】
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【ShareNodes】【处理】', 'utf8')), c='sk_referenceConfig.sk_referenceConfig().checkReferenceShareNodes()')
        mc.setParent("..")   

        mc.setParent("..")
        
        mc.tabLayout(tabs, edit=True, tabLabel=((child1, unicode('Proxy类', 'utf8')), (child2, unicode('修正Proxy', 'utf8')), (child3, unicode('Ref类', 'utf8'))))
        
        mc.showWindow("sk_sceneProxyConfigUI")

    # Proxy替换系统
    def sk_UIProxyReplaceSys(self):
        # 窗口
        if mc.window ("sk_UIProxyReplaceSys", ex=1):
            mc.deleteUI("sk_UIProxyReplaceSys", window=True)
        mc.window("sk_UIProxyReplaceSys", title="sk_UIProxyReplaceSys", widthHeight=(420, 80), menuBar=0)
        # 主界面
        mc.columnLayout()
        
        mc.frameLayout( label=u'模型|材质 全更新', borderStyle='etchedOut' ,width = 420 )
        
        # 模型替换
        mc.rowLayout(numberOfColumns = 4,columnWidth4=(100, 100,100,100))
        mc.button(l=u'【模型】高模',bgc = [0.8,0.1,0.1],width = 100,height = 25,c ='sk_sceneConfig.sk_sceneConfig().sk_sceneProxyImport(2)')
        mc.button(l=u'【模型】中模',bgc = [0.1,0.8,0.1],width = 100,height = 25,c ='sk_sceneConfig.sk_sceneConfig().sk_sceneProxyImport(1)')
        mc.button(l=u'【模型】低模',bgc = [0.1,0.6,0.8],width = 100,height = 25,c ='sk_sceneConfig.sk_sceneConfig().sk_sceneProxyImport(0)')
        mc.button(l=u'【模型】面片',bgc = [0.1,0.1,0.1],width = 100,height = 25,c ='sk_sceneConfig.sk_sceneConfig().sk_sceneProxyImport(3)')
        mc.setParent("..")
        
        mc.setParent("..")
        
        # 路径替换
        mc.frameLayout( label=u'仅更新proxy路径信息', borderStyle='etchedOut' ,width = 420 )
        
        mc.rowLayout(numberOfColumns = 4,columnWidth4=(100, 100,100,100))
        mc.button(l=u'【路径】高模',bgc = [0.8,0.3,0.3],width = 100,height = 25,c ='sk_sceneConfig.sk_sceneConfig().sk_sceneProxyPathHMLTypeChange(2)')
        mc.button(l=u'【路径】中模',bgc = [0.3,0.8,0.3],width = 100,height = 25,c ='sk_sceneConfig.sk_sceneConfig().sk_sceneProxyPathHMLTypeChange(1)')
        mc.button(l=u'【路径】低模',bgc = [0.3,0.3,0.8],width = 100,height = 25,c ='sk_sceneConfig.sk_sceneConfig().sk_sceneProxyPathHMLTypeChange(0)')
        mc.button(l=u'【路径】面片',bgc = [0.3,0.3,0.3],width = 100,height = 25,c ='sk_sceneConfig.sk_sceneConfig().sk_sceneProxyPathHMLTypeChange(3)')
        mc.setParent("..")
        
        mc.setParent("..")

        mc.setParent("..")
        mc.showWindow("sk_UIProxyReplaceSys")
        
    # 场景工具集
    def sk_sceneProxyReplaceUI(self):        
        import sk_referenceConfig
        reload(sk_referenceConfig)
        
        # 窗口
        if mc.window ("sk_sceneProxyReplaceUI", ex=1):
            mc.deleteUI("sk_sceneProxyReplaceUI", window=True)
        mc.window("sk_sceneProxyReplaceUI", title=unicode('===Proxy替换处理===', "utf8"), widthHeight=(170, 260), menuBar=0)
        
        # 面板
        form = mc.formLayout()
        # 切换面板
        tabs = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout(form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
       
        # ===Proxy参考处理===
        child1 = mc.rowColumnLayout()

        # ===Proxy参考处理===
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0, 0, 0.0], label=(unicode('===Proxy同类处理===', 'utf8')))
        mc.setParent("..")   
        
        # 替换菜单
        mc.rowLayout(numberOfColumns=4, columnWidth4=(30, 45, 30, 45))
        mc.button(l=u'源', width=30, height=20 , bgc=[0.1, 0.1, 0.4])
        mc.textField('sk_proxyReplaceSourceInfo', text='', width=45, height=20)
        mc.button(l=u'替', width=30, height=20 , bgc=[0.4, 0.1, 0.1])
        mc.textField('sk_proxyReplaceReplaceInfo', text='A' , width=45, height=20)
        mc.setParent('..')

        # 同类Proxy替换
        mc.rowLayout()
        mc.button(w=160 , h=30 , bgc=[0.1, 0.45, 0.1], label=(unicode('【同类Proxy替换】', 'utf8')), c='import maya.cmds as mc\nsourceKey = mc.textField(\"sk_proxyReplaceSourceInfo\",text = 1 , q = 1)\nreplaceKey = mc.textField(\"sk_proxyReplaceReplaceInfo\",text = 1 , q = 1)\nsk_sceneConfig.sk_sceneConfig().sk_sceneProxyTypeAddConfig(sourceKey,replaceKey)')
        mc.setParent("..")   
        
        mc.setParent("..")
        
        mc.tabLayout(tabs, edit=True, tabLabel=((child1, unicode('同类换', 'utf8'))))
        mc.showWindow("sk_sceneProxyReplaceUI")
    

    # 配套参考处理
    def sk_sceneReferenceReplace(self, modeType=1):
        sourceType = mc.optionMenuGrp('sk_AssetReferenceSourceType', q=1, value=1)
        replaceType = mc.optionMenuGrp('sk_AssetReferenceReplaceType', q=1, value=1)
        import sk_referenceConfig
        reload(sk_referenceConfig)
        if sourceType != replaceType:
            rfNodeInfos = []
            # 指定文件替换
            if modeType == 1:
                rfNodeInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceGetInfo()
            # 整个文件替换
            if modeType == 2:
                rfNodes = sk_referenceConfig.sk_referenceConfig().checkReferenceGetInfo()
                rfNodeInfos = rfNodes[0][0]
            # 执行替换
            if rfNodeInfos:
                for refNode in rfNodeInfos:
                    newPath = sk_referenceConfig.sk_referenceConfig().checkReferenceHMLModelChange(refNode , sourceType , replaceType)
                    if newPath:
                        sk_referenceConfig.sk_referenceConfig().checkReferenceChange(refNode , newPath)

        
    '''
            【系统】 【前期】【proxy系统】
             替代参考，拥有参考的更新功能，比参考快
             参与此系统的，只有Master大环，没有world大环
    '''
    # 批量导入复制
    def sk_sceneImportCopy(self, refSource, targets):
        # refSource = 'zm_p000005benthophyteRNgroup'
        # targets = ['MSH_GreenAlgae100','MSH_GreenAlgae103','MSH_GreenAlgae105','MSH_GreenAlgae107']
        # 保留原物体
        prefix = refSource.split(':')[0]
        for i in range(len(targets)):
            # 获取复制|原物体名
            # copyObjs = mc.instance(refSource)
            copyObjs = mc.duplicate(refSource)

            # 获取大环
            masterGrp = ''
            modelGrp = mc.listRelatives(copyObjs , c=1 , f=1)
            if 'Master' in modelGrp[0]:
                masterGrp = modelGrp
            else:
                masterGrp = mc.listRelatives(modelGrp , c=1, f=1)

            # 中心化目标体
            mc.select(targets[i])
            mel.eval('CenterPivot')
            mc.select(cl=1)
            # 获取目标体位置
            pivots = mc.xform(targets[i], q=1 , pivots=1 , ws=1)
            tx = mc.getAttr(targets[i] + '.tx')
            ty = mc.getAttr(targets[i] + '.ty')
            tz = mc.getAttr(targets[i] + '.tz')
            rx = mc.getAttr(targets[i] + '.rx')
            ry = mc.getAttr(targets[i] + '.ry')
            rz = mc.getAttr(targets[i] + '.rz')
            sx = mc.getAttr(targets[i] + '.sx')
            sy = mc.getAttr(targets[i] + '.sy')
            sz = mc.getAttr(targets[i] + '.sz')
            # copy版本
            # 还原
            mc.setAttr((masterGrp[0] + '.tx'), 0)
            mc.setAttr((masterGrp[0] + '.ty'), 0)
            mc.setAttr((masterGrp[0] + '.tz'), 0)
            mc.setAttr((masterGrp[0] + '.rx'), 0)
            mc.setAttr((masterGrp[0] + '.ry'), 0)
            mc.setAttr((masterGrp[0] + '.rz'), 0)           
            mc.setAttr((masterGrp[0] + '.sx'), 1)
            mc.setAttr((masterGrp[0] + '.sy'), 1)
            mc.setAttr((masterGrp[0] + '.sz'), 1)   
            # 移动,由于是instance，那么。。不能给与大环位移               
            pivots_source = mc.xform(copyObjs[0], q=1 , pivots=1 , ws=1)
            # copy版本改0
            pivots_source = [0, 0, 0, 0, 0, 0]
            mc.setAttr((masterGrp[0] + '.tx'), (tx + pivots[0] - pivots_source[0]))
            mc.setAttr((masterGrp[0] + '.ty'), (ty + pivots[1] - pivots_source[1]))
            mc.setAttr((masterGrp[0] + '.tz'), (tz + pivots[2] - pivots_source[2]))
            mc.setAttr((masterGrp[0] + '.rx'), rx)
            mc.setAttr((masterGrp[0] + '.ry'), ry)
            mc.setAttr((masterGrp[0] + '.rz'), rz)             
            # 获取目标物的bbox
            bbox = mc.xform(targets[i], q=1 , bb=1)
            x_line = bbox[3] - bbox[0]
            # 获取物体的bbx
            bbox_copy = mc.xform(copyObjs[0], q=1 , bb=1)
            x_line_copy = bbox_copy[3] - bbox_copy[0]
            # 修正缩放
            mc.setAttr((masterGrp[0] + '.sx'), (sx * x_line / x_line_copy))
            mc.setAttr((masterGrp[0] + '.sy'), (sy * x_line / x_line_copy))
            mc.setAttr((masterGrp[0] + '.sz'), (sz * x_line / x_line_copy))  
            
            # 所有子物体            
            listChildren = mc.listRelatives(copyObjs[0], ad=1, type='transform')
            # 赋予namespace
            for child in listChildren:
                mc.rename(child, (prefix + ':' + child))
            mc.rename(copyObjs[0], (prefix + ':' + copyObjs[0]))

    # 返回GEO下第二层物体的名字,对于GRP_Ground单独处理，其代表着类型
    def sk_sceneGeoDownObjs(self):
        root = 'GEO'
        rootLv1 = mc.listRelatives(root, c=1)
        rootLv2 = []
        rootGroundLv2 = []
        rootVegetationLv2 = []
        for grp in rootLv1:
            # 处理非植物非地面类
            if grp != 'GRP_Ground' and grp != 'GRP_Vegetation':
                grpDown = mc.listRelatives(grp, c=1, type='transform')
                rootLv2 = rootLv2 + grpDown
            # 处理地面类
            if grp == 'GRP_Ground':
                tempDown = mc.listRelatives(grp, ad=1, type='transform')
                grpDow = []
                for obj in tempDown:
                    # 避免shape重名。。。
                    shape = mc.listRelatives(obj, pa=1 , ni=1 , s=1 , type='mesh' , f=1)
                    if shape:
                        rootGroundLv2.append(obj)
            # 处理植物类
            if grp == 'GRP_Vegetation':
                tempDown = mc.listRelatives(grp, ad=1, type='transform')
                grpDow = []
        result = []
        result.append(rootLv2)
        result.append(rootGroundLv2)
        result.append(rootVegetationLv2)
        return result

    # 小鸡用，可去掉
    # 新增复制同一类物体匹配到目标体
    # 一律选最上层组
    def sk_sceneSameTypeReplace(self):
        # 先处理smooth
        self.sk_sceneSmoothSetConfig(0, 'Calimero')
        self.sk_sceneSmoothSetConfig(1, 'Calimero')
        self.sk_sceneSmoothSetConfig(2, 'Calimero')
        # 删除所有非参考namespace
        import sk_checkCommon
        reload(sk_checkCommon)
        sk_checkCommon.sk_checkTools().checkNamespaceCleanEmpty(2)
        # 先改名
        source = mc.ls(sl=1, l=1)
        if source:
            sourceChildren = mc.listRelatives(source[0] , ad=1, f=1, type='transform')
            if sourceChildren:
                for child in sourceChildren:
                    mc.rename(child, (child.split('|')[-1] + '_temp'))
            source = mc.rename(source[0], (source[0] + '_temp'))
            # 前提准备工作
            # 获取清单
            grps = self.sk_sceneGeoDownObjs()
            # 非地面
            rootLv2 = grps[0]
            detaiGrplsLv2 = sk_checkCommon.sk_checkTools().checkSameIDConfig(rootLv2, 1)
            keyGrp = detaiGrplsLv2.keys()
            # 地面
            rootGroundLv2 = grps[1]
            detailsGroundLv2 = sk_checkCommon.sk_checkTools().checkSameIDConfig(rootGroundLv2, 2)
            keyGround = detailsGroundLv2.keys()
            # 该死，植物类！
            # start copy and replace
                   
            signs = source.split('_')
            errorInfo = []
            targets = []
            # 编号
            index = 0
            
            # Calimero:ground类                                                        Done
            if signs[0] == 'msh':
                shape = mc.listRelatives(source, s=1)[0]
                # 选取物必须为mesh
                if mc.nodeType(shape) == 'mesh':
                    signKey = ''
                    # 因为加了temp后缀，因此最低4级
                    if len(signs) >= 4:
                        signKey = signs[1] + '_' + signs[2]
                    else:
                        signKey = signs[1]
                    # 获取同类物体
                    if signKey in keyGround:
                        targets = detailsGroundLv2[signKey]
                        if targets:
                            for target in targets:
                                # 复制
                                mc.select(source)
                                sourceCopy = mc.duplicate(rr=1, un=1)[0]
                                mc.select(cl=1)
                                # 改名
                                sourceChildren = mc.listRelatives(sourceCopy , ad=1, f=1, type='transform')
                                if sourceChildren:
                                    for child in sourceChildren:
                                        mc.rename(child, (child.split('|')[-1] + signKey + str(index)))
                                sourceCopy = mc.rename(sourceCopy, (sourceCopy + signKey + str(index)))
                                # 每复制一次，重命名
                                self.sk_sceneCalimeroGroundMove(sourceCopy, target)
                                # 删除target
                                mc.delete(target)
                                # 递增index
                                index += 1
                else:
                    errorInfo.append('=====================!!!【选取的不是polygon】!!!=====================')
            # Calimero：植物类
            if signs[0:2] == 'c_':
                print ''
            
            # Calimero:非ground类，非植物类                                Done
            # 需要加复制
            if signs[0] != 'msh' and signs[0] != 'c':
                # 获取同类物体
                signKey = signs[1]
                if signKey in keyGrp:
                    targets = detaiGrplsLv2[signKey]
                if targets:
                    for target in targets:
                        # 复制
                        mc.select(source)
                        sourceCopy = mc.duplicate(rr=1, un=1)[0]
                        mc.select(cl=1)
                        # 重改名
                        sourceChildren = mc.listRelatives(sourceCopy , ad=1, f=1, type='transform')
                        if sourceChildren:
                            for child in sourceChildren:
                                mc.rename(child, (child.split('|')[-1] + signKey + str(index)))
                        sourceCopy = mc.rename(sourceCopy, (sourceCopy + signKey + str(index)))
                        # 大环进入,改名后大环唯一了
                        sourceMaster = mc.listRelatives(sourceCopy, c=1, type='transform')[0]
                        # 移动
                        self.sk_sceneCalimeroCommonMove(sourceMaster, target)
                        # 获取子物体
                        sourceChildren = []
                        sourceChildren.append(sourceMaster)
                        sourceChildren = sourceChildren + mc.listRelatives(sourceMaster , ad=1, type='transform')
                        targetChildren = []
                        targetChildren.append(target)
                        targetChildren = targetChildren + mc.listRelatives(target , ad=1, type='transform')
                        # 删除，重命名
                        childTarget = mc.listRelatives(target, c=1)[0]
                        mc.delete(childTarget)
                        # 仅仅重命名 sourceMaster
                        mc.rename(sourceMaster, targetChildren[0])
                        # 增加index
                        index += 1
                        # for i in range(len(sourceChildren)):
                        #    mc.rename(sourceChildren[i],targetChildren[i])
            # 删除原物体
            mc.delete(source)

   
    # Calimero临时用
    def sk_sceneCalimeroReplaceTemp(self, source, target, centerPivotSource=0, centerPivotTarget=1, reGroup=1, Copy=1, reName=0):
        # 处理smoothSet
        self.sk_sceneSmoothSetConfig(0, 'Calimero')
        self.sk_sceneSmoothSetConfig(1, 'Calimero')
        self.sk_sceneSmoothSetConfig(2, 'Calimero')
        # 先进入组
        parentGrp = mc.listRelatives(target, p=1)
        newObj = mc.parent(source, parentGrp)[0]
        source = newObj
        # 获取os
        pivotOsTarget = mc.xform(target, q=1 , pivots=1 , os=1)
        # 归0
        mc.setAttr((source + '.tx'), pivotOsTarget[0])
        mc.setAttr((source + '.ty'), pivotOsTarget[1])
        mc.setAttr((source + '.tz'), pivotOsTarget[2])
        mc.setAttr((source + '.rx'), 0)
        mc.setAttr((source + '.ry'), 0)
        mc.setAttr((source + '.rz'), 0)
        mc.setAttr((source + '.sx'), 1)
        mc.setAttr((source + '.sy'), 1)
        mc.setAttr((source + '.sz'), 1)  


    # Calimero:Ground类移动
    # 白海豚通用的是copy = 2
    def sk_sceneCalimeroGroundMove(self, source, target, reGroup=1, Copy=1):
        # 中心化目标体,对客户内blocking文件有效
        mc.select(target)
        mel.eval('CenterPivot')
        mc.select(cl=1)
        # 获取目标体位置
        pivots = mc.xform(target, q=1 , pivots=1 , os=1)
        # translation = mc.xform(target ,q = 1 , t = 1 ,ws = 1 )
        # rotation = mc.xform(target ,q = 1 , ro = 1 ,ws = 1 )
        tx = mc.getAttr(target + '.tx')
        ty = mc.getAttr(target + '.ty')
        tz = mc.getAttr(target + '.tz')
        rx = mc.getAttr(target + '.rx')
        ry = mc.getAttr(target + '.ry')
        rz = mc.getAttr(target + '.rz')
        sx = mc.getAttr(target + '.sx')
        sy = mc.getAttr(target + '.sy')
        sz = mc.getAttr(target + '.sz')
        # copy版本改0
        if Copy == 1:
            pivots_source = [0, 0, 0, 0, 0, 0]
        # 非copy版本。import或者instance或者reference
        if Copy == 2:
            parent = mc.listRelatives(source, p=1, f=1)[0]
            parent = mc.listRelatives(parent, p=1, f=1)[0]
            pivots_source = mc.xform(parent, q=1 , pivots=1 , ws=1)
        mc.setAttr((source + '.tx'), (tx + pivots[0] - pivots_source[0]))
        mc.setAttr((source + '.ty'), (ty + pivots[1] - pivots_source[1]))
        mc.setAttr((source + '.tz'), (tz + pivots[2] - pivots_source[2]))
        mc.setAttr((source + '.rx'), rx)
        mc.setAttr((source + '.ry'), ry)
        mc.setAttr((source + '.rz'), rz)
        mc.setAttr((source + '.sx'), 1)
        mc.setAttr((source + '.sy'), 1)
        mc.setAttr((source + '.sz'), 1)      
        # 获取目标物的bbox
        bbox = mc.xform(target, q=1 , bb=1)
        x_line = bbox[3] - bbox[0]
        # 获取物体的bbx
        bbox_copy = mc.xform(source, q=1 , bb=1)
        x_line_copy = bbox_copy[3] - bbox_copy[0]
        # 修正缩放
        mc.setAttr((source + '.sx'), (sx * x_line / x_line_copy))
        mc.setAttr((source + '.sy'), (sy * x_line / x_line_copy))
        mc.setAttr((source + '.sz'), (sz * x_line / x_line_copy))
        # 进target的上级组
        if reGroup == 1:
            parentGrp = mc.listRelatives(target, p=1)
            newObj = mc.parent(source, parentGrp)[0]
            # 设置属性归0
            mc.setAttr((newObj + '.tx'), 0)
            mc.setAttr((newObj + '.ty'), 0)
            mc.setAttr((newObj + '.tz'), 0)
            mc.setAttr((newObj + '.rx'), 0)
            mc.setAttr((newObj + '.ry'), 0)
            mc.setAttr((newObj + '.rz'), 0)
            mc.setAttr((newObj + '.sx'), 1)
            mc.setAttr((newObj + '.sy'), 1)
            mc.setAttr((newObj + '.sz'), 1) 
        else:
            newObj = source
        return newObj
    
    # Calimero:非Ground类移动
    def sk_sceneCalimeroCommonMove(self, source, target):
        # 放target其内部组，并清零
        newObj = mc.parent(source, target)[0]
        # 处理位移
        mc.setAttr((newObj + '.tx'), 0)
        mc.setAttr((newObj + '.ty'), 0)
        mc.setAttr((newObj + '.tz'), 0)
        mc.setAttr((newObj + '.rx'), 0)
        mc.setAttr((newObj + '.ry'), 0)
        mc.setAttr((newObj + '.rz'), 0)
        mc.setAttr((newObj + '.sx'), 1)
        mc.setAttr((newObj + '.sy'), 1)
        mc.setAttr((newObj + '.sz'), 1)
        mc.select(cl=1)
        return newObj

    # GDC：Master大环对位处理
    def sk_sceneGDCCommonMove(self, source , target , animFile=0):
        # 获取tagrtRoot
        targetRoot = target.split('|MSH_c_hi_proxy_')[0]
        
        # 获取Rig母结构，并打组
        rootGrp = source.split('|')[1]
        # 遵循CHR|MODEL|Master层级
        childrenGrp = mc.listRelatives(rootGrp, c=1, type='transform', f=1)
        childrenGrp = mc.listRelatives(childrenGrp[0], c=1, type='transform', f=1)
        for grp in childrenGrp:   
            if 'MSH_c_hi_proxy_' not in grp:
                # anim阶段处理
                if animFile:
                    if mc.ls('TEMP_GRP', type='transform'):
                        tempGrp = 'TEMP_GRP'
                    else:
                        tempGrp = mc.group(name='TEMP_GRP' , em=1)
                    mc.parent(grp, tempGrp)
                else:
                    mc.parent(grp, targetRoot)

        # 查询新Master
        # anim阶段处理
        if animFile:
            childrenGrp = mc.listRelatives('TEMP_GRP', ad=1, type='transform', f=1)
        else:
            childrenGrp = mc.listRelatives(targetRoot, ad=1, type='transform', f=1)
        newMaster = ''
        for child in childrenGrp:
            if 'Master' in child and child[-1] != '_':
                # anim阶段处理
                if animFile:
                    # 判断proxyInfo
                    # 此处是Master
                    if mc.objExists((child + '.proxyInfo')):
                        if mc.getAttr((child + '.proxyInfo')) == target:
                            shape = mc.listRelatives(child, s=1, f=1)
                            if shape:
                                if mc.nodeType(shape[0]) == 'nurbsCurve':
                                    newMaster = child
                                    break
                else:
                    shape = mc.listRelatives(child, c=1, f=1)
                    if shape:
                        if mc.nodeType(shape[0]) == 'nurbsCurve':
                            newMaster = child
                            break
        # newObj = mc.parent(source,target)[0]
        # 处理位移
        # target位移
        if mc.getAttr((newMaster + '.tx') , l=1):
            mc.getAttr((newMaster + '.tx') , l=0)
        if mc.getAttr((newMaster + '.ty') , l=1):
            mc.getAttr((newMaster + '.ty') , l=0)
        if mc.getAttr((newMaster + '.tz') , l=1):
            mc.getAttr((newMaster + '.tz') , l=0)
        if mc.getAttr((newMaster + '.rx') , l=1):
            mc.getAttr((newMaster + '.rx') , l=0)
        if mc.getAttr((newMaster + '.ry') , l=1):
            mc.getAttr((newMaster + '.ry') , l=0)
        if mc.getAttr((newMaster + '.rz') , l=1):
            mc.getAttr((newMaster + '.rz') , l=0)
        if mc.getAttr((newMaster + '.sx') , l=1):
            mc.getAttr((newMaster + '.sx') , l=0)
        if mc.getAttr((newMaster + '.sy') , l=1):
            mc.getAttr((newMaster + '.sy') , l=0)
        if mc.getAttr((newMaster + '.sz') , l=1):
            mc.getAttr((newMaster + '.sz') , l=0)
        mc.setAttr((newMaster + '.tx'), (mc.getAttr(target + '.tx')))
        mc.setAttr((newMaster + '.ty'), (mc.getAttr(target + '.ty')))
        mc.setAttr((newMaster + '.tz'), (mc.getAttr(target + '.tz')))
        mc.setAttr((newMaster + '.rx'), (mc.getAttr(target + '.rx')))
        mc.setAttr((newMaster + '.ry'), (mc.getAttr(target + '.ry')))
        mc.setAttr((newMaster + '.rz'), (mc.getAttr(target + '.rz')))
        mc.setAttr((newMaster + '.sx'), (mc.getAttr(target + '.sx')))
        mc.setAttr((newMaster + '.sy'), (mc.getAttr(target + '.sy')))
        mc.setAttr((newMaster + '.sz'), (mc.getAttr(target + '.sz')))
        
        mc.select(cl=1)
        return newMaster

    # 文件内素材同一类别整理
    def sk_sceneProxyAssetInfoConfig(self):
        proxyObjs = self.sk_sceneProxySetAdd()
        # 分类
        assetProxyInfo = dict([])
        if proxyObjs:
            for proxy in proxyObjs:
                if mc.ls(proxy + '.proxyID'):
                    assetID = mc.getAttr(proxy + '.proxyID').split('_')[-1]
                    HMLType = mc.getAttr(proxy + '.proxyPath').split('/')[-1].split('_')[2]
                    # 字典存储
                    keys = assetProxyInfo.keys()
                    if (assetID + '_' + HMLType) in keys:
                        assetProxyInfo[(assetID + '_' + HMLType)].append(proxy)
                    else:
                        assetProxyInfo[(assetID + '_' + HMLType)] = [proxy]
        return assetProxyInfo
            
    '''
            【smoothSet合并处理】
            小鸡用，其他项目或可通用
            获取所有smooth级别的objectSet，甄别出非正版的"smoothx"，将盗版物体绑架到正版Set去
    '''
    def sk_sceneSmoothSetConfig(self, smoothLV, proType):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        keyWords = ''
        proType_A = ['Calimero']
        # 设置正版smoothSet名字
        if proType in proType_A:
            keyWords = 'smooth' + str(smoothLV)
        if proType not in proType_A:
            keyWords = 'smooth_' + str(smoothLV)
        for temp in tempSet:
            # 获取盗版Set
            if keyWords in temp and temp != keyWords:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                # 获取盗版mesh
                meshes = mc.sets(objSet, q=1)
                if meshes:
                    mc.sets(meshes , e=1 , addElement=keyWords)
                mc.delete(objSet)
    
    # Proxy Need
    '''
            【cacheSet合并处理】
           白海豚用，其他项目或可通用
            获取所有MESHES或CTRLS级别的objectSet，甄别出非正版的"CacheSetx"或"AnimSetx"，将盗版物体绑架到正版Set去
            加入proxy_Set处理
    '''
    def sk_sceneCacheAnimSetConfig(self, setType, proType):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        keyWords = ''
        # proType_A= ['Calimero']
        # 设置正版smoothSet名字
        if setType == 'Cache':
            keyWords = 'MESHES'
        if setType == 'Anim':
            keyWords = 'CTRLS'
        if setType == 'Proxy':
            keyWords = 'Proxy_Set'
        for temp in tempSet:
            # 获取盗版Set
            if keyWords in temp and temp != keyWords:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                # 获取盗版mesh
                meshes = mc.sets(objSet, q=1)
                if meshes:
                    mc.sets(meshes , e=1 , addElement=keyWords)
                try:
                    # 对于参考，pass
                    mc.delete(objSet)
                except:
                    pass
                
    # 直接全部处理好所有的set合并
    def sk_sceneSetCombineConfig(self,proType):
        import sk_smoothSet
        reload(sk_smoothSet)
        self.sk_sceneCacheAnimSetConfig('Anim',proType)
        self.sk_sceneCacheAnimSetConfig('Cache',proType)
        self.sk_sceneCacheAnimSetConfig('Proxy',proType)
        sk_smoothSet.sk_smoothSetTools().smoothSetCombine('Smooth',proType)
        
    # 孙望freeze恢复调用
    def sk_sceneFreezeRecoverMove(self, sourceObjs , targetObjs , copyMode = 0):
        # 在记录好参考好的物体后再处理对位物的位移
        attrs = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz']
        # 记录位移
        if copyMode == 0:
            if sourceObjs and targetObjs and len(sourceObjs) == len(targetObjs):
                for i in range(len(sourceObjs)):
                    #transInfoOG = []
                    sourceObj = sourceObjs[i]
                    targetObj = targetObjs[i]
                    # 用孙望的方法来执行强制替换
                    if mc.ls('*MSH_c_temp_food_source_'):
                        mc.delete('MSH_c_temp_food_source_')
                    if mc.ls('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_'):
                        mc.delete('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_')
                    if mc.ls('AssetFoodFreezeTempGrp'):
                        mc.delete('AssetFoodFreezeTempGrp')
                    if mc.ls('GRP_EDO_TRIANGEL_MATCH'):
                        mc.delete('GRP_EDO_TRIANGEL_MATCH')
                    # 准备工作
                    mc.group(name = 'AssetFoodFreezeTempGrp',em = 1)
                    # 备份目标体，并freeze处理
                    needObj = mc.duplicate(targetObj)[0]
                    if '|' in mc.ls(needObj,l=1)[0]:
                        #needObj = mc.parent(needObj,world = 1)[0]
                        needObj = mc.parent(needObj,'AssetFoodFreezeTempGrp')[0]
                        needObj = '|AssetFoodFreezeTempGrp|' + needObj
                    # unlock ,freeze
                    for attr in attrs:
                        mc.setAttr((needObj + attr),lock = 0)
                    mc.makeIdentity(needObj,apply = 1, t = 1,r = 1,s = 1,n = 0)
                    import sys
                    sys.path.append('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/edward/python')
                    import edo_ThreePointMatherUI.edo_ThreePointMatherCmd as etpmc
                    # 还原freeze信息
                    print sourceObj
                    mc.duplicate(sourceObj,name = 'MSH_c_temp_food_source_')
                    etpmc.edo_ThreePointMatherCmd('MSH_c_temp_food_source_',needObj,[0,1,2],[0,1,2],1)
                    targetObj = 'EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_'
                        
                    obj = targetObj
                    for attr in attrs:
                        #transInfoOG.append(mc.getAttr(obj + attr))
                        mc.setAttr((sourceObj + attr), mc.getAttr(obj + attr))
                    # 清理
                    if mc.ls('*MSH_c_temp_food_source_'):
                        mc.delete('MSH_c_temp_food_source_')
                    if mc.ls('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_'):
                        mc.delete('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_')
                    if mc.ls('AssetFoodFreezeTempGrp'):
                        mc.delete('AssetFoodFreezeTempGrp')
                    if mc.ls('GRP_EDO_TRIANGEL_MATCH'):
                        mc.delete('GRP_EDO_TRIANGEL_MATCH')
                    
                    print u'-------------------[%s]对位成功-------------------'%targetObj
                        
        if copyMode == 1:
            if sourceObjs and targetObjs and len(sourceObjs) == 1:
                souceObjBase = sourceObjs[0]
                for i in range(len(targetObjs)):
                    print u'------------------'
                    print souceObjBase
                    sourceObj = mc.duplicate(souceObjBase)[0]
                    sourceObj = mc.rename(sourceObj ,(sourceObj + '_'))
                    targetObj = targetObjs[i]
                    # 用孙望的方法来执行强制替换
                    if mc.ls('*MSH_c_temp_food_source_'):
                        mc.delete('MSH_c_temp_food_source_')
                    if mc.ls('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_'):
                        mc.delete('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_')
                    if mc.ls('AssetFoodFreezeTempGrp'):
                        mc.delete('AssetFoodFreezeTempGrp')
                    if mc.ls('GRP_EDO_TRIANGEL_MATCH'):
                        mc.delete('GRP_EDO_TRIANGEL_MATCH')
                    # 准备工作
                    mc.group(name = 'AssetFoodFreezeTempGrp',em = 1)
                    # 备份目标体，并freeze处理
                    needObj = mc.duplicate(targetObj)[0]
                    if '|' in mc.ls(needObj,l=1)[0]:
                        #needObj = mc.parent(needObj,world = 1)[0]
                        needObj = mc.parent(needObj,'AssetFoodFreezeTempGrp')[0]
                        needObj = '|AssetFoodFreezeTempGrp|' + needObj
                    # unlock ,freeze
                    for attr in attrs:
                        mc.setAttr((needObj + attr),lock = 0)
                    mc.makeIdentity(needObj,apply = 1, t = 1,r = 1,s = 1,n = 0)
                    import sys
                    sys.path.append('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/edward/python')
                    import edo_ThreePointMatherUI.edo_ThreePointMatherCmd as etpmc
                    # 还原freeze信息
                    print sourceObj
                    mc.duplicate(sourceObj,name = 'MSH_c_temp_food_source_')
                    etpmc.edo_ThreePointMatherCmd('MSH_c_temp_food_source_',needObj,[0,1,2],[0,1,2],1)
                    targetObj = 'EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_'
                        
                    obj = targetObj
                    for attr in attrs:
                        #transInfoOG.append(mc.getAttr(obj + attr))
                        mc.setAttr((sourceObj + attr), mc.getAttr(obj + attr))
                    
                    # 传UV
                    mc.transferAttributes( targetObjs[i], sourceObj, transferUVs=2, transferColors=2 )  
                    mc.select(sourceObj)
                    mel.eval('DeleteAllHistory')  
                    # 传材质，不支持选面
                    shaderSG = mc.listConnections(mc.listRelatives(targetObjs[i],ni=1,c=1,type = 'mesh')[0])[0]
                    mc.sets(sourceObj, e=1, forceElement= shaderSG )
                    
                    # 清理
                    if mc.ls('*MSH_c_temp_food_source_'):
                        mc.delete('MSH_c_temp_food_source_')
                    if mc.ls('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_'):
                        mc.delete('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_')
                    if mc.ls('AssetFoodFreezeTempGrp'):
                        mc.delete('AssetFoodFreezeTempGrp')
                    if mc.ls('GRP_EDO_TRIANGEL_MATCH'):
                        mc.delete('GRP_EDO_TRIANGEL_MATCH')
                        
                    print u'-------------------[%s]对位成功-------------------'%targetObj
                        
                        
                        
    # Proxy Need
    '''
           【系统】【前期】【proxy核心】
            白海豚用，其他项目可通用，前期拼场景，带代理物体记录信息
    1.reference special import 
    reference，proxy add attr,import.undisplay proxy
    2.place
    move proxy to the right place,delete objs,display proxy
    3.change type
    read select objs's proxy attr , import ,move ,undisplay proxy
    '''
    # 处理参考进来的物体
    def sk_sceneSpecialRefereceConfig(self, targetObj='' , freezeReset = 0):
        # 记录当前选取的物体位移信息
        transInfoOG = []
        # 获取proxy
        root = mc.ls(sl=1)[0]
        children = mc.listRelatives(root, ad=1, type='transform')
        proxy = ''
        for child in children:
            if 'MSH_c_hi_proxy_' in child:
                proxy = child
                break
            
        # 在记录好参考好的物体后再处理对位物的位移
        attrs = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz']
        # 记录位移
        if targetObj:
        # 用孙望的方法来执行强制替换
            if freezeReset:
                if mc.ls('*MSH_c_temp_food_source_'):
                    mc.delete('MSH_c_temp_food_source_')
                if mc.ls('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_'):
                    mc.delete('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_')
                if mc.ls('AssetFoodFreezeTempGrp'):
                    mc.delete('AssetFoodFreezeTempGrp')
                # 准备工作
                mc.group(name = 'AssetFoodFreezeTempGrp',em = 1)
                # 备份目标体，并freeze处理
                needObj = mc.duplicate(targetObj)[0]
                if '|' in mc.ls(needObj,l=1)[0]:
                    #needObj = mc.parent(needObj,world = 1)[0]
                    needObj = mc.parent(needObj,'AssetFoodFreezeTempGrp')[0]
                    needObj = '|AssetFoodFreezeTempGrp|' + needObj
                # unlock ,freeze
                for attr in attrs:
                    mc.setAttr((needObj + attr),lock = 0)
                mc.makeIdentity(needObj,apply = 1, t = 1,r = 1,s = 1,n = 0)
                import sys
                sys.path.append('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/edward/python')
                import edo_ThreePointMatherUI.edo_ThreePointMatherCmd as etpmc
                # 还原freeze信息
                mc.polyCube(name = 'MSH_c_temp_food_source_')
                etpmc.edo_ThreePointMatherCmd('MSH_c_temp_food_source_',needObj,[0,1,2],[0,1,2],0)
                targetObj = 'EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_'
                
            obj = targetObj
            for attr in attrs:
                transInfoOG.append(mc.getAttr(obj + attr))
            
        # 获取ref信息
        refPath = mc.referenceQuery(proxy, filename=True)
        # 素材是不允许有namespace的，所以这里的namespace只有一层
        namespace = proxy.split(':')[0]
        if refPath[-1] != 'a' and refPath[-1] != 'b':
            refPath = refPath[0:-1]
        proxyNameSimple = proxy.split(':')[0].split('_')
        refID = proxyNameSimple[0] + '_' + proxyNameSimple[1]
        # 创建属性
        if mc.objExists((proxy + '.proxyPath')) == False :
            mc.addAttr(proxy, ln='proxyPath' , dt='string')
        mc.setAttr((proxy + '.proxyPath'), refPath, type='string')
        if mc.objExists((proxy + '.proxyID')) == False :
            mc.addAttr(proxy, ln='proxyID' , dt='string')
        mc.setAttr((proxy + '.proxyID'), refID, type='string')
        if mc.objExists((proxy + '.proxyArea')) == False :
            mc.addAttr(proxy, ln='proxyArea' , dt='string')
        if mc.objExists((proxy + '.specialRef')) == False :
            mc.addAttr(proxy, ln='specialRef' , attributeType='float')
        mc.setAttr((proxy + '.specialRef'), 1)
        mc.setAttr((proxy + '.specialRef'), k=1)
        # import
        mc.file(refPath, importReference=1)
        # 记录时间
        import time
        timeNow = time.ctime().split(" ")[3].replace(":", "_")
        # 记录毫秒
        import datetime
        msTime = datetime.datetime.now().microsecond
        timeNow = timeNow + str(msTime / 100000)
        #timeMsec = datetime.datetime.now().microsecond
        #timeNow = timeNow + '_' + str(timeMsec)
        # 获取机器名
        import platform
        hostname = platform.uname()[1]
        specialMeshAdd = 'food' + hostname + '_' + timeNow + '_'
        specialGrpAdd = '_food' + hostname + '_' + timeNow
        # 改名
        masterObj = ''
        proxyObj = ''
        for grp in children:
            if grp[-1] == '_':
                newName = mc.rename(grp, (grp + specialMeshAdd))
            else:
                newName = mc.rename(grp, (grp + specialGrpAdd))
            if 'Master' in newName:
                masterObj = newName
            if 'proxy_' in newName:
                proxyObj = newName
        # unlock
        import sk_checkCommon
        reload(sk_checkCommon)
        objs = []
        objs.append((proxy + specialMeshAdd))
        sk_checkCommon.sk_checkTools().checkLockObjs(objs, 0)
        # 移动位置
        if transInfoOG:
            for i in range(2):
                if i == 0 :
                    obj = masterObj
                if i == 1 :
                    obj = proxyObj
                for j in range(len(attrs)):
                    mc.setAttr((obj + attrs[j]), transInfoOG[j])
        # 材质处理系统开始
        # 在namespace前，判断是否文件内同类素材的第一个物体，并处理材质
        # 必须每次创建更新，因为可能有新的asset类别产生
        assetSceneInfo = self.sk_sceneProxyAssetInfoConfig()
        assetName = refID.split('_food_')[0].split('_')[-1] + '_' + refPath.split('/')[-1].split('_')[2]
        assetCheckProxys = assetSceneInfo[assetName]
        print '--------NO1--------'
        print assetCheckProxys[0]
        # 本asset的proxy是第一个则pass
        if assetCheckProxys[0] != proxyObj:
            # 判断第一个物体有没有材质
            mc.select(assetCheckProxys[0])
            masterNO1 = self.sk_sceneMasterProxyDetails(0, 1)[1]
            if masterNO1:
                masterNO1 = masterNO1[0]
                # 开始记录材质
                rootGrp = mc.listRelatives(masterNO1, p = 1 , type = 'transform',f=1)[0]
                meshes = mc.listRelatives(rootGrp , ad = 1 ,type = 'mesh',f = 1)
                if meshes:
                    shaderNO1Info = dict([])
                    NO1Objs = []
                    for mesh in meshes:
                        # 强制更新keys
                        shaderSGNO1info = shaderNO1Info.keys()
                        shaderSG = mc.listConnections( mesh , d = 1 , type = 'shadingEngine' )
                        obj = mc.listRelatives(mesh,p = 1 ,type = 'transform',f = 1)[0]
                        shaderSG = list(set(shaderSG))
                        # 对该死的选面处理，记录mesh全名
                        if len(shaderSG) > 1:
                            for sgNode in shaderSG:
                                meshes = mc.sets(sgNode, q=1)
                                if meshes:
                                    for faceMesh in meshes:
                                        if (mc.listRelatives(mesh,p=1)[0] + '.f[') in faceMesh:
                                            if shaderSG in shaderSGNO1info:
                                                shaderNO1Info[sgNode].append(faceMesh)
                                            else:
                                                shaderNO1Info[sgNode] = [faceMesh]
                        # 非选面模式，记录简名
                        if len(shaderSG) == 1:
                            shaderSG = shaderSG[0]
                            if shaderSG in shaderSGNO1info:
                                shaderNO1Info[shaderSG].append(obj.split('|')[-1].split('_food')[0] + '_')
                            else:
                                shaderNO1Info[shaderSG] = [obj.split('|')[-1].split('_food')[0] + '_']
                        NO1Objs.append(mc.listRelatives(mesh,p = 1 ,type = 'transform')[0])
                    # 记录好shaderNOInfo后开始强制赋予材质
                    rootGrp = rootGrp = mc.listRelatives(masterObj, p = 1 , type = 'transform',f=1)[0]
                    meshes = mc.listRelatives(rootGrp , ad = 1 ,type = 'mesh',f = 1)
                    for mesh in meshes:
                        obj = mc.listRelatives(mesh,p = 1 ,type = 'transform',f = 1)[0]
                        # 这时候还有namespace
                        if ':' in obj.split('|')[-1]:
                            objSimple = obj.split('|')[-1].split(':')[-1].split('_food')[0] + '_'
                        else:
                            objSimple = obj.split('|')[-1].split('_food')[0] + '_'
                        # 寻找匹配物体
                        shaderSGNO1info = shaderNO1Info.keys()
                        for key in shaderSGNO1info:
                            if objSimple != 'MSH_c_hi_proxy_':
                                for meshGrp in shaderNO1Info[key]:
                                    # 选面处理，先判断mesh全名，再判断简名
                                    if '.f[' in meshGrp:
                                        if objSimple == (meshGrp.split('_food')[0] + '_'):
                                            faceMeshNew = obj + '.' + meshGrp.split('.')[-1]
                                            mc.sets(faceMeshNew , e = 1 , forceElement= key)
                                    else:
                                        # 整体处理，判断简名
                                        if objSimple in shaderNO1Info[key]:
                                            mc.sets(obj, e=1, forceElement= key )
                                    # 传UV
                                    for No1Obj in NO1Objs:
                                        if No1Obj.split('_food')[0] == obj.split('|')[-1].split('_food')[0]:
                                            #print u'>>>>>>>>'
                                            #print No1Obj
                                            #print obj.split('|')[-1]
                                            mc.transferAttributes( No1Obj, obj, transferUVs=2, transferColors=2 ,sampleSpace = 4  )  
                                            mc.select(obj)
                                            mel.eval('DeleteAllHistory')  
        # 清理临时物体
        if mc.ls('MSH_c_temp_food_source_'):
            mc.delete('MSH_c_temp_food_source_')
        if mc.ls('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_'):
            mc.delete('EDO_TRIANGEL_MATCH_MSH_c_temp_food_source_')
        if mc.ls('AssetFoodFreezeTempGrp'):
            mc.delete('AssetFoodFreezeTempGrp')
        # 清除namespace
        # sk_checkCommon.sk_checkTools().checkNamespaceCleanEmpty(2)
        mc.namespace(set=':')
        mc.namespace(force=1, moveNamespace=[namespace, ':'])
        mc.namespace(removeNamespace=namespace)
        mc.select(cl = 1)

    # 强制更新选取物体同一类的高中低模的第一个物体
    # # -1 原状 |0 低模 | 1 中模 | 2 高模    | 3 面片
    def sk_sceneProxyAssetNO1Update(self,modelType = -1):
        # 修正ID
        self.sk_proxyIDCompleteConfig()
        # 获得选取物体的proxy
        intList = ['0','1','2','3','4','5','6','7','8','9']
        shaderCombine = 0
        objs = mc.ls(sl = 1, l = 1)
        if objs == []:
            objs = self.sk_sceneProxySetAdd()
        if modelType == -1:
            shaderCombine = 1
        # asset分类
        # 里面有选取，所以objs要提前获取
        assetSceneInfo = self.sk_sceneProxyAssetInfoConfig()
        # asset更新后标记创建
        assetUpdatSign = dict()
        assetTypeInfo = assetSceneInfo.keys()
        assetTypeInfoNum = len(assetTypeInfo)
        assetReplaceNum = 1
        for asset in assetTypeInfo:
            assetUpdatSign[asset] = 0
        # 筛选替换
        if objs:
            allNumI = len(objs)
            for i in range(len(objs)):
                obj = objs[i]
                mc.select(obj)
                proxyGrp =  self.sk_sceneMasterProxyDetails(1,0)[0]
                if proxyGrp:
                    proxyGrp = proxyGrp[0]
                    assetPath = mc.getAttr( proxyGrp + '.proxyPath' )
                    assetID = mc.getAttr( proxyGrp + '.proxyID' )
                    HMLType = assetPath.split('/')[-1].split('_')[2]
                    assetType = assetID.split('_')[-1] + '_' + HMLType
                    allAssetType = assetSceneInfo.keys()
                    allNumJ = len(allAssetType)
                    for j in range(len(allAssetType)):
                        asset = allAssetType[j]
                        #if asset.split('_')[0] == assetType.split('_')[0] :
                        # 现在只一一对应
                        if asset == assetType:
                            # 没替换过时，则强制替换第一个物体
                            if assetUpdatSign[assetType] == 0:
                                print '[ NO 1_B][  %s  |   %s]'%(str(i),str(allNumI))
                                print '[ NO 1_I][  %s  |   %s]'%(str(assetReplaceNum),str(assetTypeInfoNum))
                                print asset
                                proxyObj = assetSceneInfo[assetType][0]
                                mc.select(proxyObj)
                                self.sk_sceneProxyImport(modelType)

                                # 同类材质合并
                                if shaderCombine == 1:
                                    # 记录第一个物体
                                    mc.select(proxyObj)
                                    masterNO1 = self.sk_sceneMasterProxyDetails(0, 1)[1]
                                    if masterNO1:
                                        masterNO1 = masterNO1[0]
                                        # 开始记录材质
                                        rootGrp = mc.listRelatives(masterNO1, p = 1 , type = 'transform',f=1)[0]
                                        meshes = mc.listRelatives(rootGrp , ad = 1 ,type = 'mesh',f = 1)
                                        if meshes:
                                            shaderNO1Info = dict()
                                            NO1Objs = []
                                            for mesh in meshes:
                                                if 'MSH_c_hi_proxy_' not in mesh:
                                                    # 强制更新keys
                                                    objBase = ''
                                                    shaderSGNO1info = shaderNO1Info.keys()
                                                    shaderSG = mc.listConnections( mesh , d = 1 , type = 'shadingEngine' )
                                                    shaderSG = list(set(shaderSG))
                                                    objNo1ID = ''
                                                    # 对该死的选面处理，记录mesh全名
                                                    if len(shaderSG) > 1:
                                                        for sgNode in shaderSG:
                                                            meshes = mc.sets(sgNode, q=1)
                                                            if meshes:
                                                                for faceMesh in meshes:
                                                                    if (mc.listRelatives(mesh,p=1)[0] + '.f[') in faceMesh:
                                                                        if shaderSG in shaderSGNO1info:
                                                                            shaderNO1Info[sgNode].append(faceMesh)
                                                                        else:
                                                                            shaderNO1Info[sgNode] = [faceMesh]
                                                    # 非选面模式，记录简名
                                                    if len(shaderSG) == 1:
                                                        obj = mc.listRelatives(mesh,p = 1 ,type = 'transform',f = 1)[0]
                                                        shaderSG = shaderSG[0]
                                                        objBase = obj.split('|')[-1].split('_food')[0]
                                                        print '------------->'
                                                        print objBase
                                                        objNo1ID = 'food' + obj.split('|')[-1].split('_food')[-1]
                                                        objBase = self.sk_sceneModelNameBase(objBase)
                                                        if shaderSG in shaderSGNO1info:
                                                            shaderNO1Info[shaderSG].append(objBase)
                                                        else:
                                                            shaderNO1Info[shaderSG] = [objBase]
                                                    NO1Objs.append(mc.listRelatives(mesh,p = 1 ,type = 'transform')[0])
                                            print u'--------[%s]    Shader Combine--------'%(asset)
                                            print shaderNO1Info
                                            # 循环处理后面的物体,强制赋予材质
                                            for i in range(1,len(assetSceneInfo[asset])):
                                                mc.select(assetSceneInfo[asset][i])
                                                masterOther = self.sk_sceneMasterProxyDetails(0, 1)[1]
                                                if masterOther:
                                                    masterOther = masterOther[0]
                                                    rootGrpOther = mc.listRelatives(masterOther, p = 1 , type = 'transform',f=1)[0]
                                                    meshesOther = mc.listRelatives(rootGrpOther , ad = 1 ,type = 'mesh',f = 1)
                                                    if meshesOther:
                                                        for mesh in meshesOther:
                                                            obj = mc.listRelatives(mesh,p = 1 ,type = 'transform',f = 1)[0]
                                                            objBase = ''
                                                            # 这时候没有namespace,还是加上好些
                                                            if ':' in obj.split('|')[-1]:
                                                                objBase = obj.split('|')[-1].split(':')[-1].split('_food')[0]
                                                                objBase = self.sk_sceneModelNameBase(objBase)
                                                            else:
                                                                objBase = obj.split('|')[-1].split('_food')[0]
                                                                objBase = self.sk_sceneModelNameBase(objBase)
                                                            objSimple = objBase
                                                            # 寻找匹配物体
                                                            shaderSGNO1info = shaderNO1Info.keys()
                                                            for key in shaderSGNO1info:
                                                                if objSimple == 'MSH_c_hi_proxy_':
                                                                    continue
                                                                for meshGrp in shaderNO1Info[key]:
                                                                    # [赋予材质]选面处理，判断mesh全名，再处理简名
                                                                    if '.f[' in meshGrp:
                                                                        print (meshGrp.split('_food')[0] + '_')
                                                                        if objSimple == (meshGrp.split('_food')[0] + '_'):
                                                                            faceMeshNew = obj + '.' + meshGrp.split('.')[-1]
                                                                            print faceMeshNew
                                                                            # 材质
                                                                            mc.sets(faceMeshNew , e = 1 , forceElement= key)
                                                                    else:
                                                                        # 整体处理，判断简名
                                                                        if objSimple in shaderNO1Info[key]:
                                                                            # 材质
                                                                            mc.sets(obj, e=1, forceElement= key )
                                                                    # 传UV
                                                                    for No1Obj in NO1Objs:
                                                                        if No1Obj.split('_food')[0] == obj.split('|')[-1].split('_food')[0]:
                                                                            #print u'>>>>>>>>'
                                                                            #print No1Obj
                                                                            #print obj.split('|')[-1]
                                                                            mc.transferAttributes( No1Obj, obj, transferUVs=2, transferColors=2 ,sampleSpace = 4  )  
                                                                            mc.select(obj)
                                                                            mel.eval('DeleteAllHistory')  

                                            print u'--------[%s]    Shader Combine    Done!--------'%(asset)
                                                    
                                # 更新标记
                                assetUpdatSign[asset] = 1
                                assetReplaceNum = assetReplaceNum + 1
                                mc.select(cl=1)
                                    
            # 处理proxy材质
            proxySG = mc.ls('SHD_proxy_*',type = 'shadingEngine')
            if proxySG:
                mc.sets(objs, e=1, forceElement= proxySG[0] )
                self.sk_sceneCacheAnimSetConfig('Cache','ZM')
                self.sk_sceneCacheAnimSetConfig('Anim','ZM')
            
            mc.select(cl = 1)
            return assetSceneInfo
        
    # 模型最原始名字
    def sk_sceneModelNameBase(self,obj):
        intList = ['0','1','2','3','4','5','6','7','8','9']
        if '_' in obj:
            objInfo = obj.split('_')
            numCheck = 0
            for i in range(len(objInfo)):
                if objInfo[i][0] in intList and objInfo[i][-1] in intList:
                    if i:
                        nameBase = ''
                        for j in range(i):
                            if j == 0:
                                nameBase = objInfo[j] + '_'
                            else:
                                nameBase = nameBase + objInfo[j] + '_'
                        numCheck = 1
                        break
            if numCheck == 1:
                return nameBase
            else:
                return (obj + '_')


    # [全局]强制所有类别，所有同类物体向第一个物体合并材质
    def sk_sceneProxyAssetShaderCombine(self):
        # 修正ID
        self.sk_proxyIDCompleteConfig()
        objs = mc.ls(sl = 1, l = 1)
        if objs == []:
            objs = self.sk_sceneProxySetAdd()
            if objs:
                # asset分类信息
                assetSceneInfo = self.sk_sceneProxyAssetInfoConfig()
                assetTypeInfo = assetSceneInfo.keys()
                for asset in assetTypeInfo:
                    print u'---------------'
                    print asset
                    # 记录第一个物体
                    mc.select(assetSceneInfo[asset][0])
                    masterNO1 = self.sk_sceneMasterProxyDetails(0, 1)[1]
                    if masterNO1:
                        masterNO1 = masterNO1[0]
                        # 开始记录材质
                        rootGrp = mc.listRelatives(masterNO1, p = 1 , type = 'transform',f=1)[0]
                        meshes = mc.listRelatives(rootGrp , ad = 1 ,type = 'mesh',f = 1)
                        if meshes:
                            shaderNO1Info = dict([])
                            for mesh in meshes:
                                # 强制更新keys
                                shaderSGNO1info = shaderNO1Info.keys()
                                shaderSG = mc.listConnections( mesh , d = 1 , type = 'shadingEngine' )
                                obj = mc.listRelatives(mesh,p = 1 ,type = 'transform',f = 1)[0]
                                if shaderSG:
                                    shaderSG = shaderSG[0]
                                    if shaderSG in shaderSGNO1info:
                                        shaderNO1Info[shaderSG].append(obj.split('|')[-1].split('_food')[0] + '_')
                                    else:
                                        shaderNO1Info[shaderSG] = [obj.split('|')[-1].split('_food')[0] + '_']
                            # 循环处理后面的物体,强制赋予材质
                            for i in range(1,len(assetSceneInfo[asset])):
                                mc.select(assetSceneInfo[asset][i])
                                masterOther = self.sk_sceneMasterProxyDetails(0, 1)[1]
                                masterOther = masterOther[0]
                                if masterOther:
                                    rootGrpOther = mc.listRelatives(masterOther, p = 1 , type = 'transform',f=1)[0]
                                    meshesOther = mc.listRelatives(rootGrpOther , ad = 1 ,type = 'mesh',f = 1)
                                    if meshesOther:
                                        for mesh in meshesOther:
                                            obj = mc.listRelatives(mesh,p = 1 ,type = 'transform',f = 1)[0]
                                            # 这时候没有namespace,还是加上好些
                                            if ':' in obj.split('|')[-1]:
                                                objSimple = obj.split('|')[-1].split(':')[-1].split('_food')[0] + '_'
                                            else:
                                                objSimple = obj.split('|')[-1].split('_food')[0] + '_'
                                            # 寻找匹配物体
                                            shaderSGNO1info = shaderNO1Info.keys()
                                            for key in shaderSGNO1info:
                                                if objSimple in shaderNO1Info[key]:
                                                    if objSimple != 'MSH_c_hi_proxy_':
                                                        mc.sets(obj, e=1, forceElement= key )
                # 处理proxy材质
                proxySG = mc.ls('SHD_proxy_*',type = 'shadingEngine')
                if proxySG:
                    mc.sets(objs, e=1, forceElement= proxySG[0] )
                    self.sk_sceneCacheAnimSetConfig('Cache','ZM')
                    self.sk_sceneCacheAnimSetConfig('Anim','ZM')
                                            
                                            

    # 对位处理
    # 白海豚通用的是copy = 2，regroup为0
    def sk_sceneCommonMovePlace(self, source, target, reGroup=0, Copy=1, freeze=0):
        # 非freeze情况处理
        if freeze == 0:
            # 中心化目标体,对客户内blocking文件有效
            mc.select(target)
            mel.eval('CenterPivot')
            mc.select(cl=1)
            # 获取目标体位置
            pivots = mc.xform(target, q=1 , pivots=1 , os=1)
            tx = mc.getAttr(target + '.tx')
            ty = mc.getAttr(target + '.ty')
            tz = mc.getAttr(target + '.tz')
            rx = mc.getAttr(target + '.rx')
            ry = mc.getAttr(target + '.ry')
            rz = mc.getAttr(target + '.rz')
            sx = mc.getAttr(target + '.sx')
            sy = mc.getAttr(target + '.sy')
            sz = mc.getAttr(target + '.sz')
            # copy版本改0
            if Copy == 1:
                pivots_source = [0, 0, 0, 0, 0, 0]
            # 非copy版本。import或者instance或者reference
            if Copy == 2:
                parent = mc.listRelatives(source, p=1, f=1)[0]
                parent = mc.listRelatives(parent, p=1, f=1)[0]
                pivots_source = mc.xform(parent, q=1 , pivots=1 , ws=1)
            mc.setAttr((source + '.tx'), (tx + pivots[0] - pivots_source[0]))
            mc.setAttr((source + '.ty'), (ty + pivots[1] - pivots_source[1]))
            mc.setAttr((source + '.tz'), (tz + pivots[2] - pivots_source[2]))
            mc.setAttr((source + '.rx'), rx)
            mc.setAttr((source + '.ry'), ry)
            mc.setAttr((source + '.rz'), rz)
            mc.setAttr((source + '.sx'), 1)
            mc.setAttr((source + '.sy'), 1)
            mc.setAttr((source + '.sz'), 1)      
        # freez情况处理
        if freeze == 1:
            # 位移
            bboxMatrix = mc.exactWorldBoundingBox(target)
            worldPlace = [(bboxMatrix[0] + bboxMatrix[3]) / 2, (bboxMatrix[1] + bboxMatrix[4]) / 2, (bboxMatrix[2] + bboxMatrix[5]) / 2]
            mc.setAttr((source + '.tx'), worldPlace[0])
            mc.setAttr((source + '.ty'), worldPlace[1])
            mc.setAttr((source + '.tz'), worldPlace[2])
            # 其他信息
            # 获取
            rx = mc.getAttr(target + '.rx')
            ry = mc.getAttr(target + '.ry')
            rz = mc.getAttr(target + '.rz')
            sx = mc.getAttr(target + '.sx')
            sy = mc.getAttr(target + '.sy')
            sz = mc.getAttr(target + '.sz')
            # 还原
            mc.setAttr((source + '.rx'), rx)
            mc.setAttr((source + '.ry'), ry)
            mc.setAttr((source + '.rz'), rz)
            mc.setAttr((source + '.sx'), 1)
            mc.setAttr((source + '.sy'), 1)
            mc.setAttr((source + '.sz'), 1)    
            
        # 获取目标物的bbox
        bbox = mc.xform(target, q=1 , bb=1)
        x_line = bbox[3] - bbox[0]
        # 获取物体的bbx
        bbox_copy = mc.xform(source, q=1 , bb=1)
        x_line_copy = bbox_copy[3] - bbox_copy[0]
        # 修正缩放
        mc.setAttr((source + '.sx'), (sx * x_line / x_line_copy))
        mc.setAttr((source + '.sy'), (sy * x_line / x_line_copy))
        mc.setAttr((source + '.sz'), (sz * x_line / x_line_copy))
        # 进target的上级组
        if reGroup == 1:
            parentGrp = mc.listRelatives(target, p=1)
            newObj = mc.parent(source, parentGrp)[0]
            # 设置属性归0
            mc.setAttr((newObj + '.tx'), 0)
            mc.setAttr((newObj + '.ty'), 0)
            mc.setAttr((newObj + '.tz'), 0)
            mc.setAttr((newObj + '.rx'), 0)
            mc.setAttr((newObj + '.ry'), 0)
            mc.setAttr((newObj + '.rz'), 0)
            mc.setAttr((newObj + '.sx'), 1)
            mc.setAttr((newObj + '.sy'), 1)
            mc.setAttr((newObj + '.sz'), 1) 
        else:
            newObj = source
        return newObj     
    
    # Proxy Need
    # 将指定物体的proxy的proxyPath替换高低模版本
    # 0 低模 | 1 中模 | 2 高模    | 3 面片
    def sk_sceneProxyPathHMLTypeChange(self,modelType):
        proxyGrps = self.sk_sceneMasterProxyDetails(1,0)[0]
        if proxyGrps:
            for proxy in proxyGrps:
                path = mc.getAttr(proxy + '.proxyPath')
                newPath = path
                if modelType == 0:
                    if '_l_' not in path:
                        newPath = newPath.replace('_m_', '_l_')
                        newPath = newPath.replace('_h_', '_l_')
                        newPath = newPath.replace('_p_', '_l_')
                if modelType == 1:
                    if '_m_' not in path:
                        newPath = newPath.replace('_l_', '_m_')
                        newPath = newPath.replace('_h_', '_m_')
                        newPath = newPath.replace('_p_', '_m_')
                    # newPath = path.replace('_h_','_l_')
                if modelType == 2:
                    if '_h_' not in path:
                        newPath = newPath.replace('_l_', '_h_')
                        newPath = newPath.replace('_m_', '_h_')
                        newPath = newPath.replace('_p_', '_h_')
                if modelType == 3:
                    if '_p_' not in path:
                        newPath = newPath.replace('_l_', '_p_')
                        newPath = newPath.replace('_m_', '_p_')
                        newPath = newPath.replace('_h_', '_p_')
                mc.setAttr((proxy + '.proxyPath'),newPath,type = 'string')
            print u'==============[%s]路径信息处理完毕=============='%(proxy.split('|')[-1])
            

    # Proxy Need
    # 获取proxy及Master
    # 选取的是Master或者Proxy均可
    # 该版本只支持只有Master大环没有World大环的物体
    def sk_sceneMasterProxyDetails(self, proxy=1, master=1):
        # 获取root大组
        # 由于前期植物归类到大组，改变方法为选取获取proxy
        proxySel = mc.ls(sl=1)
        proxyGrps = []
        masterGrps = []

        for i in range(len(proxySel)):
            parent = mc.listRelatives(proxySel[i], p=1, type='transform', f=1)
            children = mc.listRelatives(parent, ad=1, type='transform', f=1)
            for child in children:
                checkChild = child.split('|')[-1]
                # 获取proxy
                if proxy == 1:
                    if 'MSH_c_hi_proxy_' in checkChild:
                        proxyGrps.append(child)
                # 获取Master
                if master == 1:
                    if 'Master' in checkChild and checkChild[-1] != '_':
                        shape = mc.listRelatives(child, s=1, f=1)
                        if shape:
                            if mc.nodeType(shape[0]) == 'nurbsCurve':
                                masterGrps.append(child)
                if proxy == 1 and master != 1:
                    if len(proxyGrps) == (i + 1):
                        break
                if proxy != 1 and master == 1:
                    if len(masterGrps) == (i + 1):
                        break  
                if proxy == 1 and master == 1:
                    if len(proxyGrps) == len(masterGrps) and len(proxyGrps) == (i + 1):
                        break
        result = []
        result.append(proxyGrps)
        result.append(masterGrps)
        if master == 1 and masterGrps == []:
            mc.warning(u'==============有空proxy的植物，请排查==============')
        return result

    # Proxy Need
    # 将所有proxy对位
    def sk_sceneProxyMoveConfig(self):
        result = self.sk_sceneProxyDebugCheck()
        errorGrps = result[0]
        proxyGrps = result[1]
        if errorGrps == []:
            mc.select(proxyGrps)
            result = self.sk_sceneMasterProxyDetails(1, 1)
            proxyGrps = result[0]
            masterGrps = result[1]
            if len(proxyGrps) == len(masterGrps) and proxyGrps:
                for i in range(len(proxyGrps)):
                    tx = mc.getAttr(masterGrps[i] + '.tx')
                    ty = mc.getAttr(masterGrps[i] + '.ty')
                    tz = mc.getAttr(masterGrps[i] + '.tz')
                    rx = mc.getAttr(masterGrps[i] + '.rx')
                    ry = mc.getAttr(masterGrps[i] + '.ry')
                    rz = mc.getAttr(masterGrps[i] + '.rz')
                    sx = mc.getAttr(masterGrps[i] + '.sx')
                    sy = mc.getAttr(masterGrps[i] + '.sy')
                    sz = mc.getAttr(masterGrps[i] + '.sz')
                    mc.setAttr((proxyGrps[i] + '.tx'), tx)
                    mc.setAttr((proxyGrps[i] + '.ty'), ty)
                    mc.setAttr((proxyGrps[i] + '.tz'), tz)
                    mc.setAttr((proxyGrps[i] + '.rx'), rx)
                    mc.setAttr((proxyGrps[i] + '.ry'), ry)
                    mc.setAttr((proxyGrps[i] + '.rz'), rz)
                    mc.setAttr((proxyGrps[i] + '.sx'), sx)
                    mc.setAttr((proxyGrps[i] + '.sy'), sy)
                    mc.setAttr((proxyGrps[i] + '.sz'), sz)
        else:
            # mc.warning(unicode('=====================【proxy】有错误=====================', "utf8"))
            mc.warning(u'=====================【proxy】有错误=====================')
    
    # Proxy Need
    # 选取proxy只改名字
    def sk_sceneProxyOnlyRename(self,proxySel):
        # 获取阶段文件
        #proxySel = self.sk_sceneProxySetAdd()
        # 计数开始
        myNum = 1000
        if proxySel:
            # 开始循环
            for proxy in proxySel:
                # 记录时间
                import time
                timeNow = time.ctime().split(" ")[3].replace(":", "_")
                # 记录毫秒
                import datetime
                msTime = datetime.datetime.now().microsecond
                timeNow = timeNow + str(msTime / 100000)
                #timeMsec = datetime.datetime.now().microsecond
                #timeNow = timeNow + '_' + str(timeMsec)
                specialMeshAdd = 'food' + str(myNum) + '_' + timeNow + '_'
                # 开始更改名字
                oldName = proxy
                newName = 'MSH_c_hi_proxy_' + specialMeshAdd
                print oldName
                print newName
                mc.rename(oldName, newName)
                # 更新计数
                myNum += 1

    # Proxy Need
    # 选取proxySet中的proxy，全自动更改层级名字
    # 层次为MODEL|MSH_all|MSH_geo|MSH_c_hi_plant|植物类|植物同类root
    def sk_sceneProxyGrpLevelRename(self,modeType = 1):
        # 获取阶段文件
        import sk_checkCommon
        reload(sk_checkCommon)
        import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if modeType:
            proxySel = self.sk_sceneProxySetAdd()
        else:
            proxySel = mc.ls(sl=1 , l = 1)
        
        print proxySel

        if proxySel:
            # 项目设置
            projectGrp = ['zm']
            # 计数开始
            myNum = 1000
            # 开始循环
            outProxy = []
            for proxy in proxySel:
                # root = mc.ls(proxy,l=1)[0].split('|')[-2]
                # 获取proxy所在的根目录
                if '|MSH_c_hi_proxy_' in proxy:
                    grpModel = mc.ls(proxy, l=1)[0].split('|MSH_c_hi_proxy_')
                    if grpModel:
                        grpModel = grpModel[0]
                    else:
                        print proxy
                        mc.error(u'=====================检查该proxy物体的层级关系======================')
                    # 2到3层到RNgroup的处理
                    rootGrp = mc.listRelatives(grpModel, p=1, f=1)[0]
                    if 'RNgroup' not in rootGrp.split('|')[-1]:
                        rootGrp = mc.listRelatives(rootGrp, p=1, f=1)[0]
                    else:
                        pass
                    root = mc.ls(rootGrp, l=1)[0]
                    # 获取root的所有子物体
                    children = mc.listRelatives(root, ad=1, type='transform', f=1)
                    children.append(root)
                    # 获取层级
                    childLevel = []
                    for child in children:
                        childLevel.append(len(child.split('|')) - 1)
                    # 记录时间
                    import time
                    timeNow = time.ctime().split(" ")[3].replace(":", "_")
                    # 记录毫秒
                    import datetime
                    msTime = datetime.datetime.now().microsecond
                    timeNow = timeNow + str(msTime / 100000)
                    #timeMsec = datetime.datetime.now().microsecond
                    #timeNow = timeNow + '_' + str(timeMsec)
                    specialMeshAdd = 'food' + str(myNum) + '_' + timeNow + '_'
                    specialGrpAdd = '_food' + str(myNum) + '_' + timeNow
                    # 开始更改名字
                    # 根目录不用管，铁定相同
                    levelMax = max(childLevel)
                    while levelMax > 1:
                        deepIndexs = sk_checkCommon.sk_checkTools().checkListSameAllIndex(childLevel, levelMax)
                        for ID in deepIndexs:
                            oldName = children[ID]
                            if oldName[-1] == '_':
                                if 'food' not in oldName:
                                    oldNameLast = oldName.split('|')[-1]
                                if 'food' in oldName:
                                    oldNameLast = oldName.split('|')[-1].split('food')[0]
                                newName = oldNameLast + specialMeshAdd
                            else:
                                if 'food' not in oldName:
                                    oldNameLast = oldName.split('|')[-1]
                                if 'food' in oldName:
                                    oldNameLast = oldName.split('|')[-1].split('_food')[0]
                                newName = oldNameLast + specialGrpAdd
                            mc.rename(oldName, newName)
                            if 'MSH_c_hi_proxy_' in newName:
                                outProxy.append(newName)
                            # 将转化后的转为0。最小的
                            childLevel[ID] = 0
                        # 更新最大值
                        levelMax = max(childLevel)
                    # 更新计数
                    myNum += 1
            print outProxy
            # 还原proxy名字
            self.sk_sceneProxyOnlyRename(outProxy)
        else:
            # mc.warning(unicode('==========【!!!请创建proxySet!!!】==========', "utf8"))
            mc.warning(u'==========【!!!请创建proxySet!!!】==========')

    # Proxy Need
    # 选取proxy
    # 处理错误的proxy
    def sk_sceneProxyDebugCheck(self):
        proxySel = mc.ls(sl=1, l=1)
        proxyGrp = []
        errorProxy = []
        for i in range(len(proxySel)):
            parent = mc.listRelatives(proxySel[i], p=1, type='transform', f=1)
            children = mc.listRelatives(parent, ad=1, type='transform', f=1)
            checkMaster = 0
            for child in children:
                # 获取Master
                if 'Master' in child and child[-1] != '_':
                    shape = mc.listRelatives(child, s=1, f=1)
                    if shape:
                        if mc.nodeType(shape[0]) == 'nurbsCurve':
                            checkMaster = 1
            if checkMaster == 0:
                errorProxy.append(proxySel[i])
            if checkMaster == 1:
                proxyGrp.append(proxySel[i])
        result = []
        result.append(errorProxy)
        result.append(proxyGrp)
        mc.select(cl=1)
        if errorProxy:
            mc.select(errorProxy)
            # print(unicode('=====================【空置】的proxy选取成功=====================', "utf8"))
            print(u'=====================【空置】的proxy选取成功=====================')
        else:
            # print(unicode('=====================【proxy】都正常=====================', "utf8"))
            print(u'=====================【proxy】都正常=====================')
        return result
    
    # Proxy Need
    # 创建proxySet
    # 选取proxy
    def sk_sceneProxySetAdd(self):
        # 必须放前面，否则创建set时取消选择状态了
        # proxyGrps = mc.ls(sl = 1, l = 1)
        proxyGrps = mc.ls('*MSH_c_hi_proxy_*', type='transform') + mc.ls('*:*MSH_c_hi_proxy_*', type='transform')
        if proxyGrps:
            # 创建
            if mc.objExists('Proxy_Set'):
                mc.sets(cl='Proxy_Set')
            else:
                mc.createNode('objectSet', n='Proxy_Set')
            # 判断，更新
            mc.select(proxyGrps)
            # 开始创建
            for grp in proxyGrps:
                mc.sets(grp , e=1 , addElement='Proxy_Set')
            self.sk_sceneCacheAnimSetConfig('Proxy','')
            return proxyGrps
    
    # Proxy Need
    # 获取场景中所有proxySet的物体
    # 为方便修改更新，所有proxySet物体全部获取
    def sk_sceneProxySetObjects(self):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        objsProxy = [] 
        if tempSet:
            for temp in tempSet:
                if 'Proxy_Set' in temp:
                    objsSet.append(temp)
            if temp == []:
                # mc.warning(unicode('=====================【!!!请创建好proxySet!!!】=====================', "utf8"))
                mc.warning(u'=====================【!!!请创建好proxySet!!!】=====================')
            if objsSet:
                for objSet in objsSet:
                    meshes = mc.sets(objSet, q=1)
                    if meshes:
                        for mesh in meshes:
                            # 不要长命，为shareNodes做准备
                            objsProxy.append(mc.ls((mesh), l=1)[0])
        return objsProxy
    
    # Proxy Need
    # 选取proxySet内的物体
    def sk_sceneProxySetObjectsSelect(self):
        objs = self.sk_sceneProxySetObjects()
        if objs:
            mc.select(objs)
        
    # Proxy Need
    # 隐藏/显示proxySet内的物体
    def sk_sceneProxySetObjectsHide(self, hide=0):
        objs = self.sk_sceneProxySetObjects()
        if objs:
            hide = mc.getAttr(objs[0] + '.v')
            for obj in objs:
                if hide:
                    mc.setAttr((obj + '.v'), 0)
                else:
                    mc.setAttr((obj + '.v'), 1)
    
    # Proxy Need
    # 清理多余的Set
    def sk_sceneCacheAnimSetDoClean(self):
        # 加入Set清理
        self.sk_sceneCacheAnimSetConfig('Cache', 'ZM')
        self.sk_sceneCacheAnimSetConfig('Anim', 'ZM')
    
    # Proxy Need
    # 所有Master删掉 ==> 改成选取的物体的Master删掉
    # 只保留proxy
    def sk_sceneMasterDelete(self):
        result = self.sk_sceneMasterProxyDetails(1, 0)
        # 获取proxy的上级路径，获取其子组，删除非proxy
        if result[0]:
            for obj in result[0]:
                parentGrp = mc.listRelatives(obj, p=1, f=1)
                childrenGrps = mc.listRelatives(parentGrp[0], type='transform', c=1 , f=1)
                for grp in childrenGrps:
                    if 'MSH_c_hi_proxy_' not in grp:
                        mc.delete(grp)
                # print(unicode('=====================【proxy】独留完毕=====================', "utf8"))
                print(u'=====================【proxy】独留完毕=====================')

    # Proxy Need
    '''
            【系统】 【前期】【proxy系统】
    proxy替换新asset功能
    '''
    # 【严格注意】【材质未通过期间】在有空盒子的情况下，先清理空盒子
    # import新物体 , 支持动画系统
    # 最好场景内没有参考
    # 在anim阶段，给导入的master加入属性，来和植物一一对应
    # import之前查询TEMP_GRP是否有对应的Master并传递动画
    # 新增处理：
    # 材质强制调用获取场景内同一类素材的第一个物体；若本身为同类第一个物体，则直接创建新材质，而不是share nodes
    # 【用法】
    # 前期：animFile模式是0
    # check in时，只保留proxy盒子
    # 动画：想要K哪个的帧，选中盒子，执行导入，此时是animFile 1模式
    # 动画：有K帧的物体，再次切换时，会自动把动画信息赋予proxy物体
    # -1 原状 |0 低模 | 1 中模 | 2 高模    | 3 面片
    def sk_sceneProxyImport(self, modelType=1, animFile=0 ):
        import sk_checkCommon
        reload(sk_checkCommon)
        import os
        if animFile:
            objs = mc.ls(sl=1, l=1)
            if objs:
                result = []
                proxyGrp = []
                masterGrp = []
                for obj in objs:
                    # 选取的是proxy
                    if 'MSH_c_hi_proxy_' in obj:
                        if mc.ls('TEMP_GRP'):
                            grps = mc.listRelatives('TEMP_GRP', c=1, f=1)
                            if grps:
                                for grp in grps:
                                    # 此处是Master
                                    if mc.getAttr(grp + '.proxyInfo') == obj:
                                        masterGrp.append(grp)
                        proxyGrp.append(obj)     
                    # 选取的是Master
                    if 'Master' in obj:
                        # 对anim文件来说，只有TEMP_GRP里的有效
                        # 此处是Master
                        proxyGrp.append(mc.getAttr(obj + '.proxyInfo'))
                        masterGrp.append(obj)
                result.append(proxyGrp)
                result.append(masterGrp) 
        else:
            result = self.sk_sceneMasterProxyDetails(1, 0)
        if result[0]:
            proxyGrps = result[0]
            errorInfo = []
            # 不想用i in range啊。。用个临时变量好了
            # 清理namespace
            try:
                sk_checkCommon.sk_checkTools().checkNamespaceCleanEmpty(2)
            except:
                pass
            # 标准namespace
            renameID = 1000
            import time
            timeNow = time.ctime().split(" ")[3].replace(":", "_")
            # 记录毫秒
            import datetime
            msTime = datetime.datetime.now().microsecond
            timeNow = timeNow + str(msTime / 100000)
            #timeMsec = datetime.datetime.now().microsecond
            #timeNow = timeNow + '_' + str(timeMsec)
            # 开始循环
            for proxyGrp in proxyGrps:
                # 获取proxy上层组
                rootGrp = mc.listRelatives(proxyGrp, p=1)[0]
                renameID += 1
                posMeshName = proxyGrp.split('MSH_c_hi_proxy_')[-1]
                posGrpName = '_' + posMeshName[0:-1]
                # 此处是proxy物体
                if mc.objExists((proxyGrp + '.proxyPath')) == True and mc.objExists((proxyGrp + '.proxyID')):
                    path = mc.getAttr(proxyGrp + '.proxyPath')
                    nsID = mc.getAttr(proxyGrp + '.proxyID') + '_food_' + str(renameID) + '_' + timeNow
                    # 处理路径
                    newPath = path
                    if modelType == -1:
                        newPath = path
                    if modelType == 0:
                        if '_l_' not in path:
                            newPath = newPath.replace('_m_', '_l_')
                            newPath = newPath.replace('_h_', '_l_')
                            newPath = newPath.replace('_p_', '_l_')
                    if modelType == 1:
                        if '_m_' not in path:
                            newPath = newPath.replace('_l_', '_m_')
                            newPath = newPath.replace('_h_', '_m_')
                            newPath = newPath.replace('_p_', '_m_')
                        # newPath = path.replace('_h_','_l_')
                    if modelType == 2:
                        if '_h_' not in path:
                            newPath = newPath.replace('_l_', '_h_')
                            newPath = newPath.replace('_m_', '_h_')
                            newPath = newPath.replace('_p_', '_h_')
                    if modelType == 3:
                        if '_p_' not in path:
                            newPath = newPath.replace('_l_', '_p_')
                            newPath = newPath.replace('_m_', '_p_')
                            newPath = newPath.replace('_h_', '_p_')
                        # newPath = path.replace('_h_','_l_')
                    # 判断是否存在参考文件
                    print os.path.exists(newPath)
                    if os.path.exists(newPath):
                        # 选取指定proxy
                        mc.select(proxyGrp)
                        # 清理原来的
                        try:
                            self.sk_sceneMasterDelete()
                        except:
                            pass
                        # 更改proxyPath属性
                        mc.setAttr((proxyGrp + '.proxyPath'),newPath,type = 'string')
                        # 判断在否，在则先传递动画再删除master
                        if animFile:
                            if mc.ls('TEMP_GRP'):
                                grps = mc.listRelatives('TEMP_GRP', c=1 , f=1)
                                if grps:
                                    for grp in grps:
                                        # 此处是Master
                                        proxyInfo = mc.getAttr(grp + '.proxyInfo')
                                        if proxyGrp == proxyInfo:
                                            # 现传递动画
                                            needMaster = []
                                            needMaster.append(grp)
                                            self.sk_sceneProxyAnimInfoConfig(needMaster)
                                            # 再删除
                                            mc.delete(grp)
                        # 首先reference，然后shareNodes|新增版本改动，不要shareNodes
                        #mc.file(newPath, r=1, sharedNodes="shadingNetworks", namespace=nsID)
                        mc.file(newPath, r=1, namespace=nsID)
                        # 删除reference，import
                        mc.file(newPath, importReference=1)
                        # 获取Master大环 
                        mc.namespace(setNamespace=(':' + nsID))
                        objs = mc.namespaceInfo(dagPath=1, ls=1)
                        mc.namespace(setNamespace=':')
                        masterGrp = ''
                        rootTempGrp = ''
                        # proxy 处理
                        proxyInfo = []
                        for obj in objs:
                            # 查询Master
                            if 'Master' in obj and obj[-1] != '_':
                                shape = mc.listRelatives(obj, s=1, f=1)
                                if shape:
                                    if mc.nodeType(shape[0]) == 'nurbsCurve':
                                        masterGrp = obj
                            # 删除组内的proxy
                            if 'MSH_c_hi_proxy_' in obj:
                                proxyInfo.append(obj)
                            # 查询rootGrp
                            if len(obj.split('|')) == 2:
                                rootTempGrp = obj
                            # 都找到后break
                            if rootTempGrp and masterGrp:
                                break
                        # proxy清理
                        if proxyInfo:
                            for proxy in proxyInfo:
                                if proxy in objs:
                                    objs.remove(proxy)
                            mc.delete(proxyInfo)
                        # 处理masterGrp属性
                        # 创建属性
                        # 此处是Master
                        if mc.objExists((masterGrp + '.proxyInfo')) == False :
                            mc.addAttr(masterGrp, ln='proxyInfo' , dt='string')
                        mc.setAttr((masterGrp + '.proxyInfo'), proxyGrp, type='string')
                        # 对位
                        newMaster = self.sk_sceneGDCCommonMove(masterGrp , proxyGrp , animFile)
                        # 重命名
                        grps = mc.listRelatives(newMaster, ad=1, type='transform', f=1)
                        grps.append(newMaster)
                        for grp in grps:
                            if grp[-1] == '_':
                                newName = grp.split('|')[-1] + posMeshName
                            else:
                                newName = grp.split('|')[-1] + posGrpName
                            mc.rename(grp, newName)
                        # 更新newMaster
                        newMaster = newMaster.split('|')[-1] + posGrpName
                        # 动画信息传递
                        if animFile:
                            needPorxyAnim = []
                            needPorxyAnim.append(proxyGrp)
                            # 替换信息
                            proxyPre = proxyGrp.split('MSH_c_hi_proxy_food')[0] + 'MSH_c_hi_proxy_food'
                            masterPre = newMaster.split('Master_food')[0] + 'Master_food'
                            # 导出动画
                            sk_checkCommon.sk_checkTools().checkAnimCurveInfoExport(needPorxyAnim , 0 , 'proxy')
                            sk_checkCommon.sk_checkTools().checkAnimCurveInfoImport(0 , 'proxy' , [proxyPre, masterPre])
                            # 隐藏proxy
                            mc.setAttr((proxyGrp + '.v'), 0)
                        # 删除其他物体
                        mc.delete(rootTempGrp)
                        # 材质处理系统开始
                        # 在namespace前，判断是否文件内同类素材的第一个物体，并处理材质
                        # 必须每次创建更新，因为可能有新的asset类别产生
                        assetSceneInfo = self.sk_sceneProxyAssetInfoConfig()
                        proxyPath = mc.getAttr(proxyGrp + '.proxyPath')
                        assetName = nsID.split('_food_')[0].split('_')[-1] + '_' + proxyPath.split('/')[-1].split('_')[2]
                        assetCheckProxys = assetSceneInfo[assetName]
                        # 本asset的proxy是第一个则pass
                        if assetCheckProxys[0] != proxyGrp:
                            # 判断第一个物体有没有材质
                            mc.select(assetCheckProxys[0])
                            masterNO1 = self.sk_sceneMasterProxyDetails(0, 1)[1]
                            if masterNO1:
                                print u'====================================='
                                print u'This is type NO.1'
                                print masterNO1
                                masterNO1 = masterNO1[0]
                                # 开始记录材质
                                rootGrp = mc.listRelatives(masterNO1, p = 1 , type = 'transform',f=1)[0]
                                meshes = mc.listRelatives(rootGrp , ad = 1 ,type = 'mesh',f = 1)
                                if meshes:
                                    shaderNO1Info = dict()
                                    NO1Objs = []
                                    for mesh in meshes:
                                        # 强制更新keys
                                        shaderSGNO1info = shaderNO1Info.keys()
                                        shaderSG = mc.listConnections( mesh , d = 1 , type = 'shadingEngine' )
                                        obj = mc.listRelatives(mesh,p = 1 ,type = 'transform',f = 1)[0]
                                        shaderSG = list(set(shaderSG))
                                        # 对该死的选面处理，记录mesh全名
                                        if len(shaderSG) > 1:
                                            for sgNode in shaderSG:
                                                meshes = mc.sets(sgNode, q=1)
                                                if meshes:
                                                    for faceMesh in meshes:
                                                        if (mc.listRelatives(mesh,p=1)[0] + '.f[') in faceMesh:
                                                            if shaderSG in shaderSGNO1info:
                                                                shaderNO1Info[sgNode].append(faceMesh)
                                                            else:
                                                                shaderNO1Info[sgNode] = [faceMesh]
                                        # 非选面模式，记录简名
                                        if len(shaderSG) == 1:
                                            shaderSG = shaderSG[0]
                                            if shaderSG in shaderSGNO1info:
                                                shaderNO1Info[shaderSG].append(obj.split('|')[-1].split('_food')[0] + '_')
                                            else:
                                                shaderNO1Info[shaderSG] = [obj.split('|')[-1].split('_food')[0] + '_']
                                        NO1Objs.append(mc.listRelatives(mesh,p = 1 ,type = 'transform')[0])       
                                    # 记录好shaderNOInfo后开始强制赋予材质
                                    rootGrp = rootGrp = mc.listRelatives(newMaster, p = 1 , type = 'transform',f=1)[0]
                                    meshes = mc.listRelatives(rootGrp , ad = 1 ,type = 'mesh',f = 1)
                                    for mesh in meshes:
                                        obj = mc.listRelatives(mesh,p = 1 ,type = 'transform',f = 1)[0]
                                        # 这时候还有namespace
                                        if ':' in obj.split('|')[-1]:
                                            objSimple = obj.split('|')[-1].split(':')[-1].split('_food')[0] + '_'
                                        else:
                                            objSimple = obj.split('|')[-1].split('_food')[0] + '_'
                                        # 寻找匹配物体
                                        shaderSGNO1info = shaderNO1Info.keys()
                                        for key in shaderSGNO1info:
                                            if objSimple != 'MSH_c_hi_proxy_':
                                                for meshGrp in shaderNO1Info[key]:
                                                    # 选面处理，判断mesh全名，后判断简名
                                                    if '.f[' in meshGrp:
                                                        if objSimple == (meshGrp.split('_food')[0] + '_'):
                                                            faceMeshNew = obj + '.' + meshGrp.split('.')[-1]
                                                            mc.sets(faceMeshNew , e = 1 , forceElement= key)
                                                    else:
                                                        # 整体处理，判断简名
                                                        if objSimple in shaderNO1Info[key]:
                                                            mc.sets(obj, e=1, forceElement= key )
                                                    # 传UV
                                                    for No1Obj in NO1Objs:
                                                        if No1Obj.split('_food')[0] == obj.split('|')[-1].split('_food')[0]:
                                                            #print u'>>>>>>>>'
                                                            #print No1Obj
                                                            #print obj.split('|')[-1]
                                                            mc.transferAttributes( No1Obj, obj, transferUVs=2, transferColors=2 ,sampleSpace = 4  )  
                                                            mc.select(obj)
                                                            mel.eval('DeleteAllHistory')  
                                                
                        # 删除namespace
                        mc.namespace(force=1, moveNamespace=[nsID, ':'])
                        mc.namespace(removeNamespace=nsID)
                        # 清空选取
                        mc.select(cl = 1)
                    else:
                        errorInfo.append(u'===============请检查【%s】，确保转换的类型有文件在服务器===============' % proxyGrp)
                else:
                    # errorInfo.append(('===============请检查【%s】，确保proxy有path及ID属性===============') % (str(proxyGrp)))
                    errorInfo.append(u'===============请检查【%s】，确保proxy有path及ID属性===============' % proxyGrp)
            
            for info in errorInfo:
                # print(unicode('%s' % (str(info)), 'utf8'))
                print(u'%s' % info)
            if len(errorInfo):
                # mc.warning(unicode('===========================【目前】共计【%s】处纰漏===========================' % (str(len(errorInfo))), 'utf8'))
                mc.warning(u'===========================【目前】共计【%s】处纰漏===========================' % len(errorInfo))
            else:
                # print(unicode('===========================【恭喜】成功导入并匹配！！！===========================' , 'utf8'))
                print(u'===========================【恭喜】成功导入并匹配！！！===========================')
            return len(errorInfo)

    # 后台批量处理替换
    # -1 保留原状 | 0 低模 | 1 中模 | 2 高模    | 3 面片 
    def sk_sceneAutoReplace(self,modelType=1, animFile=0 ,save = 0):
        # 修正ID
        self.sk_proxyIDCompleteConfig()
        configNum = 100
        # 重新set
        proxySel = self.sk_sceneProxySetAdd()
        if proxySel:
            mc.select(proxySel)
            emptyProxy = self.sk_sceneProxyDebugCheck()
            if emptyProxy[0] == []:
                # 强制更新NO1
                mc.select(proxySel)
                self.sk_sceneProxyAssetNO1Update(modelType)
                # 处理替换
                mc.select(proxySel)
                if modelType != -1:
                    i = 1
                    for proxy in proxySel:
                        print u'[    [当前]    %s    |    [总数]    %s    ]'%(i,len(proxySel))
                        if i % configNum == 0:
                            mel.eval('MLdeleteUnused')
                        mc.select(proxy)
                        self.sk_sceneProxyImport(modelType, animFile)
                        i = i  +1 
                else:
                    i = 1
                    for proxy in proxySel:
                        print u'[    [当前]    %s    |    [总数]    %s    ]'%(i,len(proxySel))
                        if i % configNum == 0:
                            mel.eval('MLdeleteUnused')
                        path = mc.getAttr(proxy + '.proxyPath')
                        needModelType = path.split('/')[-1].split('_')[2]
                        mc.select(proxy)
                        self.sk_sceneProxyImport(needModelType, animFile)
                        i = i  +1 
                mc.select(cl = 1)
                print(u'==================！！！【恭喜】全部替换成功！！！==================')
                # 处理proxy材质
                proxySG = mc.ls('SHD_proxy_*',type = 'shadingEngine')
                if proxySG:
                    mc.sets(proxySel, e=1, forceElement= proxySG[0] )
                    self.sk_sceneCacheAnimSetConfig('Cache','ZM')
                    self.sk_sceneCacheAnimSetConfig('Anim','ZM')
                    print(u'==================！！！【proxy】材质处理完毕！！！==================')
                else:
                    mc.warning(u'********************！！！【proxy】有异常！！！********************')
                if save == 1:
                    # 删除unuse节点
                    mel.eval('MLdeleteUnused')
                    print(u'==================！！！【unuse】清理完毕！！！==================')
                    # 保存
                    fileName =  (mc.file(query=1, exn=1)).split('/')[-1]
                    mc.file(rename = 'D:/' +fileName )
                    mc.file(save = 1, f = 1)
                    print(u'==================！！！【恭喜】保存完毕！！！==================')
                
                # 成功代码
                return 0
            
            else:
                mc.error(u'==================有【空】的proxy，请清理后再替换==================')
        else:
            mc.error(u'==================未发现proxy，请检查==================')
    
    # Proxy Need
    '''
            【UI】 【前期】【proxy替换Instance】
    '''
    def sk_sceneProxyInstanceUI(self):
        
        
        # 窗口
        if mc.window ("sk_sceneProxyInstanceUI", ex=1):
            mc.deleteUI("sk_sceneProxyInstanceUI", window=True)

        mc.window("sk_sceneProxyInstanceUI", title=unicode('===ProxyInstance处理===', "utf8"), widthHeight=(170, 260), menuBar=0)

        # 主界面
        mc.columnLayout()

        mc.rowLayout()
        mc.button(w=235 , h=30 , bgc=[0, 0, 0.0], label=(unicode('===ProxyInstance处理===', 'utf8')))
        mc.setParent("..")   

        mc.scriptTable('sk_sceneProxyTypeInfoTable', w=235 , h=300)


        '''
        mc.rowLayout(numberOfColumns = 2 , columnWidth2 = (180,40))
        mc.textScrollList('sk_sceneProxyTypeScrollList' , w = 180 , h = 260 , allowMultiSelection = 1)
        mc.textScrollList('sk_sceneProxyTypeNumScrollList' , w = 40 , h = 260 , enable = 0)
        mc.setParent("..")   
        '''
        
        mc.rowLayout()
        mc.button(w=235 , h=50 , bgc=[0, 0.6, 0.1], label=(u'选取类别进行Instance处理'), c=self.sk_sceneProxyInstanceUISelectDoCMD)
        mc.setParent("..")   
        
        # 信息储存。这个是局部产生的赋值。。
        # 居然不是全局变量
        self.sk_proxyTypeAllInfo = self.sk_sceneAssetTypeInfoConfig()
        # 更新表格
        self.sk_sceneProxyInstanceUIScrollListInfoUpdate()

        mc.showWindow("sk_sceneProxyInstanceUI")

    # Proxy Need
    # UI相关，更新list信息
    def sk_sceneProxyInstanceUIScrollListInfoUpdate(self):
        allInfo = self.sk_proxyTypeAllInfo
        if allInfo[0]:
            # 获取数据
            proxyTypeInfo = allInfo[0]
            proxyTypeIndexInfo = allInfo[1]
            proxyTypeNumInfo = []
            for index in proxyTypeIndexInfo:
                proxyTypeNumInfo.append(len(index))
            # 更新列表
            '''
            mc.textScrollList('sk_sceneProxyTypeScrollList', e = 1 , removeAll = 1)
            mc.textScrollList('sk_sceneProxyTypeScrollList', e = 1 , append = proxyTypeInfo)
            mc.textScrollList('sk_sceneProxyTypeNumScrollList', e = 1 , removeAll = 1)
            mc.textScrollList('sk_sceneProxyTypeNumScrollList', e = 1 , append = proxyTypeNumInfo)
            '''
            mc.scriptTable('sk_sceneProxyTypeInfoTable', e=1 , clearTable=1)
            mc.scriptTable('sk_sceneProxyTypeInfoTable', e=1 , rows=len(proxyTypeInfo) , columns=2 , label=[(1, u'种类名称'), (2, u'同种数量')])
            mc.scriptTable('sk_sceneProxyTypeInfoTable', e=1 , columnWidth=[2, 50])
            mc.scriptTable('sk_sceneProxyTypeInfoTable', e=1 , columnWidth=[1, 150])
            # 此处是表格的算法，不加括号直接运行
            mc.scriptTable('sk_sceneProxyTypeInfoTable', e=1 , getCellCmd=self.sk_sceneProxyInstanceUIScriptTableUpdate)
            
    # Proxy Need
    # UI相关，更新list信息
    def sk_sceneProxyInstanceUIScriptTableUpdate(self, i , j):
        allInfo = self.sk_proxyTypeAllInfo
        result = ''
        if allInfo[0]:
            # 获取数据
            proxyTypeInfo = allInfo[0]
            proxyTypeIndexInfo = allInfo[1]
            proxyTypeNumInfo = []
            for index in proxyTypeIndexInfo:
                proxyTypeNumInfo.append(len(index))  
            if j == 1:
                result = proxyTypeInfo[i - 1]
            if j == 2:
                result = proxyTypeNumInfo[i - 1]
        return result

    # Proxy Need
    # UI相关，同时选取对应物体
    def sk_sceneProxyInstanceUISelectDoCMD(self, noNeed=''):
        # 获取选取的table
        rowNum = mc.scriptTable('sk_sceneProxyTypeInfoTable', q=1, selectedRow=1)
        allInfo = self.sk_proxyTypeAllInfo
        if rowNum:
            assetType = allInfo[0][rowNum - 1]
            self.sk_sceneProxyInstanceConfig([assetType])

    
    # Proxy Need
    '''
            【系统】 【前期】【proxy系统】
             同一ID分类替换
    '''
    # 添加新分类，ZM的补丁
    # 该死的客户在早期只提供了植物种类，但后期又突然说每种植物要有不同颜色
    # 于是针对这种情况修正proxy的数据
    # 每类植物后添加A-Z的标记来分辨分类
    # asset名末尾有A-Z中的则执行替换，没有则添加
    # 使用条件：选取植物的大环Master控制器
    def sk_sceneProxyTypeAddConfig(self , sourceKeyInfo='' , replaceKeyInfo=''):
        # 获取选取物的proxy
        proxyInfos = self.sk_sceneMasterProxyDetails(1, 1)[0]
        if proxyInfos:
            errorproxy = []
            for proxy in proxyInfos:
                if mc.objExists(proxy + '.proxyPath') and mc.objExists(proxy + '.proxyID'):
                    pathInfo = mc.getAttr(proxy + '.proxyPath')
                    # 分解路径信息
                    fileTypeSpiltInfos = pathInfo.split('.')
                    filePathSplitInfos = fileTypeSpiltInfos[0].split('/')
                    fileNameInfos = filePathSplitInfos[-1].split('_')
                    # 替换系统
                    if sourceKeyInfo == '':
                        sourceKeyInfo = fileNameInfos[1][-1]
                    else:
                        sourceKeyInfo = sourceKeyInfo
                    if sourceKeyInfo in map(chr, range(65, 91)):
                        assetReplaceInfo = fileNameInfos[1].replace(sourceKeyInfo, replaceKeyInfo)
                    else:
                        assetReplaceInfo = fileNameInfos[1] + replaceKeyInfo
                    # 获取系统路径
                    for i in range(len(filePathSplitInfos) - 1):
                        if i == 0:
                            filePath = filePathSplitInfos[i] + '/'
                        else:
                            if i == len(filePathSplitInfos) - 3:
                                filePath = filePath + assetReplaceInfo + '/'
                            else:
                                filePath = filePath + filePathSplitInfos[i] + '/'
                    # 整理文件名
                    for i in range(len(fileNameInfos)):
                        if i == 0:
                            fileName = fileNameInfos[i]
                        else:
                            if i == 1:
                                fileName = fileName + '_' + assetReplaceInfo
                            else:
                                fileName = fileName + '_' + fileNameInfos[i]      
                    fileName = fileName + '.' + fileTypeSpiltInfos[-1]
                    newPath = filePath + fileName
                    mc.setAttr((proxy + '.proxyPath'), newPath, type='string')
                    # 处理proxyID信息
                    newID = fileNameInfos[0] + '_' + assetReplaceInfo
                    mc.setAttr((proxy + '.proxyID'), newID, type='string')
                else:
                    errorproxy.append(proxy)
            if errorproxy:
                print u'==============以下proxy无效=============='
                for error in errorproxy:
                    print error
                print u'===============请修正proxy==============='
                
    # Proxy Need
    '''
            【系统】 【前期】【proxy信息处理】
    '''
    # 【核心函数】获取场景内物体类别信息
    # 存储的数据，以list为单位，每个list单位第一位是ID，第二位是grps的list
    def sk_sceneVegetationTypeInfo(self):
        # 存储的数据，以list为单位，每个list单位第一位是ID，第二位是grps的list
        # 嵌套list['p001001_h',['head','body'],proxyList]
        cacheObjsVegetation = []
        # 重新创建proxySet
        self.sk_sceneProxySetAdd()
        # 获取所有proxy物体
        proxyObjs = self.sk_sceneProxySetAdd()
        for proxy in proxyObjs:
            proxyInfo = []
            # 获取proxy的proxyID
            # 此处是proxy
            proxyID = mc.getAttr(proxy + '.proxyID')
            # 处理高中低模状态
            proxyPath = mc.getAttr(proxy + '.proxyPath')
            HTMType = proxyPath.split('/')[-1].split('_')[2]
            # 记录
            proxyInfo.append(proxyID[:10] + '_' + HTMType)
            # 获取objs
            # 获取proxy的父级
            grp = mc.ls(proxy, l=1)[0].split('|')[-2]
            meshes = mc.listRelatives(grp, ad=1, type='mesh', f=1)
            objsVegetation = []
            for mesh in meshes:
                if 'proxy' not in mesh:
                    objsVegetation.append(mc.listRelatives(mesh, p=1)[0])
            # 存储cacheObjs
            proxyInfo.append(objsVegetation)
            # 存储proxy物体
            proxyInfo.append(proxy)
            # 存储所有信息
            cacheObjsVegetation.append(proxyInfo)
        return cacheObjsVegetation      
                
    # Proxy Need
    # 处理asset类别对应数量信息
    def sk_sceneAssetTypeInfoConfig(self):
        # 获取proxy类别
        assetTypeInfos = self.sk_sceneVegetationTypeInfo()
        typeInfos = []
        for assetType in assetTypeInfos:
            typeInfos.append(assetType[0])
        needTypeInfos = list(set(typeInfos))
        # 获取编号
        typeIndexs = []
        import sk_checkCommon
        if typeInfos:
            for typeInfo in needTypeInfos:
                # 第二种方法，很快，但不详细
                # print typeInfo
                # typeCount = typeInfos.count(typeInfo)
                # print typeCount
                # typeNums.append(typeCount)
                # 第一种方法，完整编号信息
                IDInfo = sk_checkCommon.sk_checkTools().checkListSameAllIndex(typeInfos, typeInfo)
                typeIndexs.append(IDInfo)
        # 第一个为无重复的素材类型名
        # 第二个为对应的素材的数量
        # 第三个为完整的信息，sk_sceneVegetationTypeInfo的返回值
        resultInfo = [needTypeInfos, typeIndexs, assetTypeInfos]
        return resultInfo

    # Proxy Need
    '''
            【系统】 【前期】【proxy替换Instance】
             同一类物体（相同ID下不同分支各一类），选取source源，并统一处理为instance
             要处理好层级关系再重命名
    '''
    # 需要更新：已经创建好instance的，额外进行更新
    # 类别参数类型处理为list
    def sk_sceneProxyInstanceConfig(self , selectAssetTypes=[]):
        import sk_checkCommon
        reload(sk_checkCommon)
        # 创建sourceSet
        # 创建
        if mc.objExists('ProxySource_Set'):
            pass
        else:
            mc.createNode('objectSet', n='ProxySource_Set')
        souceSet = 'ProxySource_Set'
        
        # 获取proxy类别
        assetTypeInfos = self.sk_sceneAssetTypeInfoConfig()
        if assetTypeInfos[0]:
            # 数据整合
            typeInfos = assetTypeInfos[0]
            typeIndexs = assetTypeInfos[1]
            allAssetTypeInfos = []
            allAssetProxyInfos = []
            for assetType in assetTypeInfos[2]:
                allAssetTypeInfos.append(assetType[0])
                allAssetProxyInfos.append(assetType[2])
            # 开始处理所选类别
            if selectAssetTypes:
                for selectType in selectAssetTypes:
                    typeInTypeIndex = typeInfos.index(selectType)
                    typeInAllInfoIndex = typeIndexs[typeInTypeIndex]
                    # 获取第一个proxy物体作为源
                    sourceProxy = allAssetProxyInfos[typeInAllInfoIndex[0]]
                    mc.select(sourceProxy)
                    sourceMaster = self.sk_sceneMasterProxyDetails(1, 1)[1][0]
                    mc.select(cl=1)
                    # 获取根root
                    rootGrp = mc.listRelatives(mc.listRelatives(mc.listRelatives(sourceProxy, p=1)[0], p=1)[0], p=1)[0]
                    # 对多异常层级进行判断
                    if 'RNgroup' in rootGrp:
                        rootGrp = rootGrp
                    else:
                        rootGrp = mc.listRelatives(mc.listRelatives(sourceProxy, p=1)[0], p=1)[0]
                    if '_source' not in rootGrp:
                        # 处理source，整理出instanceBase
                        allAssetProxyInfos[typeInAllInfoIndex[0]] = sourceProxy
                        # 备份位移信息
                        proxyTx = mc.getAttr(sourceProxy + '.tx')
                        proxyTy = mc.getAttr(sourceProxy + '.ty')
                        proxyTz = mc.getAttr(sourceProxy + '.tz')
                        proxyRx = mc.getAttr(sourceProxy + '.rx')
                        proxyRy = mc.getAttr(sourceProxy + '.ry')
                        proxyRz = mc.getAttr(sourceProxy + '.rz')
                        proxySx = mc.getAttr(sourceProxy + '.sx')
                        proxySy = mc.getAttr(sourceProxy + '.sy')
                        proxySz = mc.getAttr(sourceProxy + '.sz')
                        mc.setAttr((sourceProxy + '.tx'), 0)
                        mc.setAttr((sourceMaster + '.tx'), 0)
                        mc.setAttr((sourceProxy + '.ty'), 0)
                        mc.setAttr((sourceMaster + '.ty'), 0)
                        mc.setAttr((sourceProxy + '.tz'), 0)
                        mc.setAttr((sourceMaster + '.tz'), 0)
                        mc.setAttr((sourceProxy + '.rx'), 0)
                        mc.setAttr((sourceMaster + '.rx'), 0)
                        mc.setAttr((sourceProxy + '.ry'), 0)
                        mc.setAttr((sourceMaster + '.ry'), 0)
                        mc.setAttr((sourceProxy + '.rz'), 0)
                        mc.setAttr((sourceMaster + '.rz'), 0)
                        mc.setAttr((sourceProxy + '.sx'), 1)
                        mc.setAttr((sourceMaster + '.sx'), 1)
                        mc.setAttr((sourceProxy + '.sy'), 1)
                        mc.setAttr((sourceMaster + '.sy'), 1)
                        mc.setAttr((sourceProxy + '.sz'), 1)
                        mc.setAttr((sourceMaster + '.sz'), 1)
                        # 处理属性
                        if mc.getAttr((rootGrp + '.tx') , l=1):
                            mc.setAttr((rootGrp + '.tx') , l=0)
                        mc.setAttr((rootGrp + '.tx'), proxyTx)
                        if mc.getAttr((rootGrp + '.ty') , l=1):
                            mc.setAttr((rootGrp + '.ty') , l=0)
                        mc.setAttr((rootGrp + '.ty'), proxyTy)
                        if mc.getAttr((rootGrp + '.tz') , l=1):
                            mc.setAttr((rootGrp + '.tz') , l=0)
                        mc.setAttr((rootGrp + '.tz'), proxyTz)
                        if mc.getAttr((rootGrp + '.rx') , l=1):
                            mc.setAttr((rootGrp + '.rx') , l=0)
                        mc.setAttr((rootGrp + '.rx'), proxyRx)
                        if mc.getAttr((rootGrp + '.ry') , l=1):
                            mc.setAttr((rootGrp + '.ry') , l=0)
                        mc.setAttr((rootGrp + '.ry'), proxyRy)
                        if mc.getAttr((rootGrp + '.rz') , l=1):
                            mc.setAttr((rootGrp + '.rz') , l=0)
                        mc.setAttr((rootGrp + '.rz'), proxyRz)
                        if mc.getAttr((rootGrp + '.sx') , l=1):
                            mc.setAttr((rootGrp + '.sx') , l=0)
                        mc.setAttr((rootGrp + '.sx'), proxySx)
                        if mc.getAttr((rootGrp + '.sy') , l=1):
                            mc.setAttr((rootGrp + '.sy') , l=0)
                        mc.setAttr((rootGrp + '.sy'), proxySy)
                        if mc.getAttr((rootGrp + '.sz') , l=1):
                            mc.setAttr((rootGrp + '.sz') , l=0)
                        mc.setAttr((rootGrp + '.sz'), proxySz)
                        
                        # 重命名rootGrp
                        mc.rename(rootGrp, (rootGrp.split('|')[-1] + '_source'))
                        rootGrp = rootGrp + '_source'
                        
                        # 对于只有一个物体的不处理instance
                        if len(typeInAllInfoIndex) > 1:
                            mc.select(rootGrp)
                            
                            # 开始处理后面的
                            for j in range(1, len(typeInAllInfoIndex)):
                                # 备份旧name信息
                                # 子物体顺序可能不一样，但去除_food后是一致的
                                targetRootGrp = mc.instance(rootGrp)[0]
                                
                                oldProxy = allAssetProxyInfos[typeInAllInfoIndex[j]]
                                oldRootGrp = mc.listRelatives(mc.listRelatives(mc.listRelatives(oldProxy, p=1)[0], p=1)[0], p=1)[0]
                                if 'RNgroup' in oldRootGrp: 
                                    oldRootGrp = oldRootGrp
                                else:
                                    oldRootGrp = mc.listRelatives(mc.listRelatives(oldProxy, p=1)[0], p=1)[0]
                                oldObjs = mc.listRelatives(oldRootGrp , ad=1 , type='transform')
                                oldObjs.append(oldRootGrp)
                                oldObjsReorder = sk_checkCommon.sk_checkTools().sk_checkObjOutlinerReorder(oldObjs)
                                
                                oldShareParent = mc.listRelatives(oldRootGrp, p=1)[0]
                                
                                # 开始移动位置
                                if mc.getAttr((targetRootGrp + '.tx') , l=1):
                                    mc.setAttr((targetRootGrp + '.tx') , l=0)
                                mc.setAttr((targetRootGrp + '.tx'), mc.getAttr(oldProxy + '.tx')) 
                                if mc.getAttr((targetRootGrp + '.ty') , l=1):
                                    mc.setAttr((targetRootGrp + '.ty') , l=0)
                                mc.setAttr((targetRootGrp + '.ty'), mc.getAttr(oldProxy + '.ty'))
                                if mc.getAttr((targetRootGrp + '.tz') , l=1):
                                    mc.setAttr((targetRootGrp + '.tz') , l=0)
                                mc.setAttr((targetRootGrp + '.tz'), mc.getAttr(oldProxy + '.tz'))
                                if mc.getAttr((targetRootGrp + '.rx') , l=1):
                                    mc.setAttr((targetRootGrp + '.rx') , l=0)
                                mc.setAttr((targetRootGrp + '.rx'), mc.getAttr(oldProxy + '.rx'))
                                if mc.getAttr((targetRootGrp + '.ry') , l=1):
                                    mc.setAttr((targetRootGrp + '.ry') , l=0)
                                mc.setAttr((targetRootGrp + '.ry'), mc.getAttr(oldProxy + '.ry'))
                                if mc.getAttr((targetRootGrp + '.rz') , l=1):
                                    mc.setAttr((targetRootGrp + '.rz') , l=0)
                                mc.setAttr((targetRootGrp + '.rz'), mc.getAttr(oldProxy + '.rz'))
                                if mc.getAttr((targetRootGrp + '.sx') , l=1):
                                    mc.setAttr((targetRootGrp + '.sx') , l=0)
                                mc.setAttr((targetRootGrp + '.sx'), mc.getAttr(oldProxy + '.sx'))
                                if mc.getAttr((targetRootGrp + '.sy') , l=1):
                                    mc.setAttr((targetRootGrp + '.sy') , l=0)
                                mc.setAttr((targetRootGrp + '.sy'), mc.getAttr(oldProxy + '.sy'))
                                if mc.getAttr((targetRootGrp + '.sz') , l=1):
                                    mc.setAttr((targetRootGrp + '.sz') , l=0)
                                mc.setAttr((targetRootGrp + '.sz'), mc.getAttr(oldProxy + '.sz'))
                                # 清理旧asset，还原name及层级信息
                                mc.delete(oldRootGrp)
                                # 还原组，只还原到proxy上2层，保留MODEL组开始
                                if oldShareParent not in mc.ls(targetRootGrp, l=1)[0]:
                                    targetRootGrp = mc.parent(targetRootGrp , oldShareParent)[0]
                                else:
                                    targetRootGrp = targetRootGrp
                                # 删除_source标记
                                mc.rename(targetRootGrp, (targetRootGrp.split('_source')[0] + targetRootGrp.split('_source')[1]))
                                # 无法重命名
                                # 因为是instance
                                '''
                                instanceObjs = mc.listRelatives(targetRootGrp , ad = 1 ,f=1 ,type = 'transform')
                                instanceObjs.append(targetRootGrp)
                                instanceObjsReorder = sk_checkCommon.sk_checkTools().sk_checkObjOutlinerReorder(instanceObjs)
                                # 重命名
                                # 基于同类植物排序后可以优化算法。不用判断的这么麻烦
                                # 最好还是判断
                                # 因为。。很可能出现同种植物出现的是不同的版本，如anim和tx
                                for m in range(len(instanceObjsReorder)):
                                    for mi in range(len(instanceObjsReorder[m])):
                                        if m != (len(instanceObjsReorder) -1):
                                            preInfo = instanceObjsReorder[m][mi].split('|')[-1].split('_food')[0]
                                        else:
                                            preInfo = instanceObjsReorder[m][0].split('|')[-1]
                                        oldName = ''
                                        for n in range(len(oldObjsReorder)):
                                            for ni in range(len(oldObjsReorder[n])):
                                                if n != (len(oldObjsReorder) - 1):
                                                    oldPreInfo = oldObjsReorder[n][ni].split('|')[-1].split('_food')[0]
                                                else:
                                                    oldPreInfo = oldObjsReorder[n][0].split('|')[-1]
                                                if preInfo == oldPreInfo:
                                                    oldName = oldObjsReorder[n][ni]
                                                    break
                                        if oldName:
                                            print '========================='
                                            print instanceObjsReorder[m][mi].split('|')[-1]
                                            print oldName.split('|')[-1]
                                            print instanceObjsReorder[m][mi]
                                            print '========================='
                                            mc.rename(instanceObjsReorder[m][mi],oldName.split('|')[-1])
                                '''
                            # 添加到sourceSet组
                            mc.sets(rootGrp  , e=1 , addElement=souceSet)
                            print u'=====================【%s】instance成功！！！=====================' % (selectType)
                        else:
                            print u'=====================【%s】只有一个，无需instance=====================' % (selectType)
                    else:
                        print u'=====================【%s】已经instance过=====================' % (selectType)
    
    # Proxy Need     
    '''
            【系统】 【前期】【proxy检测】
            位移属性只允许在Master下
    '''
    def sk_sceneProxyInfoCheck(self, show=1):
        # 重新创建proxySet
        self.sk_sceneProxySetAdd()
        # 获取所有proxy物体
        proxyObjs = self.sk_sceneProxySetAdd()
        errorProxy = []
        if proxyObjs:
            for proxy in proxyObjs:
                checkAttr = 0
                # ModelGrp
                grpModel = mc.listRelatives(proxy , p=1 , f = 1)[0]
                # allGrp
                grpAll = mc.listRelatives(grpModel , p=1 , f = 1)[0]
                # rootGrp
                if 'RNgroup' in grpAll:
                    grpRoot = grpAll
                    checkNum = 3
                else:
                    grpRoot = mc.listRelatives(grpAll , p=1 , f = 1)
                    if grpRoot:
                        grpRoot = grpRoot[0]
                        checkNum = 3
                    else:
                        grpRoot = ''
                        checkNum = 2
                for i in range(checkNum):
                    if i == 0:
                        checkGrp = grpModel
                    if i == 1:
                        checkGrp = grpAll
                    if checkNum == 3:
                        if i == 2:
                            checkGrp = grpRoot
                    if mc.getAttr(checkGrp + '.tx') != 0:
                        checkAttr = checkAttr + 1
                    if mc.getAttr(checkGrp + '.ty') != 0:
                        checkAttr = checkAttr + 1
                    if mc.getAttr(checkGrp + '.tz') != 0:
                        checkAttr = checkAttr + 1
                    if mc.getAttr(checkGrp + '.rx') != 0:
                        checkAttr = checkAttr + 1
                    if mc.getAttr(checkGrp + '.ry') != 0:
                        checkAttr = checkAttr + 1
                    if mc.getAttr(checkGrp + '.rz') != 0:
                        checkAttr = checkAttr + 1
                    if mc.getAttr(checkGrp + '.sx') != 1:
                        checkAttr = checkAttr + 1
                    if mc.getAttr(checkGrp + '.sy') != 1:
                        checkAttr = checkAttr + 1
                    if mc.getAttr(checkGrp + '.sz') != 1:
                        checkAttr = checkAttr + 1
                if checkAttr:
                    #print proxy.split('|')[-1]
                    errorProxy.append(proxy)
                    
        mc.select(cl=1)
        
        if show:
            if errorProxy:
                mc.warning(u'================================================')
                for error in errorProxy:
                    print error
                mc.warning(u'============以上proxy上三层大组有属性，请处理！============')
        return list(set(errorProxy))
    
    # proxy Need
    # 自动处理proxy位移错误
    # 只处理tx,ty,tz
    def sk_sceneProxyUpGroupMoveConfig(self):
        errorProxy = self.sk_sceneProxyInfoCheck(0)
        if errorProxy:
            for proxy in errorProxy:
                # 获取proxy及master
                mc.select(proxy)
                master = self.sk_sceneMasterProxyDetails(0, 1)[1][0]
                mc.select(cl=1)
                # ModelGrp
                grpModel = mc.listRelatives(proxy , p=1 ,f = 1)[0]
                # allGrp
                grpAll = mc.listRelatives(grpModel , p=1 , f = 1)[0]
                # rootGrp
                if 'RNgroup' in grpAll:
                    grpRoot = grpAll
                else:
                    grpRoot = mc.listRelatives(grpAll , p=1 , f = 1)[0]
                # 处理位移
                for i in range(3):
                    if i == 0:
                        checkGrp = grpModel
                    if i == 1:
                        checkGrp = grpAll
                    if i == 2:
                        checkGrp = grpRoot
                    if mc.getAttr((proxy + '.tx'), l=1):
                        mc.setAttr((proxy + '.tx'), l=0)
                    if mc.getAttr((master + '.tx'), l=1):
                        mc.setAttr((master + '.tx'), l=0)
                    if mc.getAttr((proxy + '.ty'), l=1):
                        mc.setAttr((proxy + '.ty'), l=0)
                    if mc.getAttr((master + '.ty'), l=1):
                        mc.setAttr((master + '.ty'), l=0)
                    if mc.getAttr((proxy + '.tz'), l=1):
                        mc.setAttr((proxy + '.tz'), l=0)
                    if mc.getAttr((master + '.tz'), l=1):
                        mc.setAttr((master + '.tz'), l=0)
                    if mc.getAttr(checkGrp + '.tx') != 0:
                        txResult = mc.getAttr(proxy + '.tx') + mc.getAttr(checkGrp + '.tx')
                        mc.setAttr((proxy + '.tx'), txResult)
                        mc.setAttr((master + '.tx'), txResult)
                        mc.setAttr((checkGrp + '.tx'), 0)
                    if mc.getAttr(checkGrp + '.ty') != 0:
                        tyResult = mc.getAttr(proxy + '.ty') + mc.getAttr(checkGrp + '.ty')
                        mc.setAttr((proxy + '.ty'), tyResult)
                        mc.setAttr((master + '.ty'), tyResult)
                        mc.setAttr((checkGrp + '.ty'), 0)
                    if mc.getAttr(checkGrp + '.tz') != 0:
                        tzResult = mc.getAttr(proxy + '.tz') + mc.getAttr(checkGrp + '.tz')
                        mc.setAttr((proxy + '.tz'), tzResult)
                        mc.setAttr((master + '.tz'), tzResult)
                        mc.setAttr((checkGrp + '.tz'), 0)
                        
            
    # Proxy Need           
    '''
            【系统】 【前期】【proxy补充】
    rg文件proxy处理在MODEL下
    '''
    # 设置文件提交处理。将MSH_c_hi_proxy_处理成MODEL下
    def sk_sceneProxyRigSet(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 只对植物进行代理处理
        # 加入部分set
        if info[1][0:4] == 'p000' or info[1][0] in ['s', 'S']:
            proxy = mc.ls('MSH_c_*_proxy_')
            if proxy:
                # 判断只有一个
                if len(proxy) == 1:
                    path = mc.ls(proxy[0], l=1)[0]
                    if ('|MODEL|' + proxy[0]) not in path:
                        mc.parent(proxy[0], 'MODEL')
                else:
                    # mc.warning(unicode('===========================【错误】有多个【%s】===========================' % (str('MSH_c_*_proxy_'), 'utf8')))
                    mc.warning(u'===========================【错误】有多个【%s】===========================' % u'MSH_c_*_proxy_')
            else:
                if info[1][0:4] == 'p000':
                    # mc.warning(unicode('===========================【错误】没有【proxy】===========================' , 'utf8'))
                    mc.warning(u'===========================【错误】没有【proxy】===========================')

    # Proxy Need
    '''
            【系统】【动画&灯光】【proxy系统】
    '''            
    # 传递动画数据到proxy
    def sk_sceneProxyAnimInfoConfig(self, masterGrp=''):
        import sk_checkCommon
        reload(sk_checkCommon)
        # MASTER不在TEMP_GRP里就是老版本处理，若在TEMP_GRP里是新版本处理
        # 获取代理物体
        proxyGrp = self.sk_sceneProxySetAdd()
        # 默认全局获取
        if masterGrp == '':
            # 获取老版本master大环
            masterGrp = []
            for proxy in proxyGrp:
                root = mc.listRelatives(proxy, p=1 , f=1)[0]
                for grp in mc.listRelatives(root, c=1, f=1):
                    if 'Master_food' in grp and grp[-1] != '_':
                        masterGrp.append(grp)
            # 处理老版本大环
            if masterGrp:
                # 查询动画信息
                haveAnimMaster = []
                needAnimProxy = []
                for master in masterGrp:
                    if 'TEMP_GRP' not in master:
                        animInfo = mc.ls((master.split('|')[-1] + '_*'), type='animCurve')
                        if animInfo:
                            # 记录proxy
                            grps = mc.listRelatives(mc.listRelatives(masterGrp, p=1, f=1)[0], c=1, f=1)
                            for grp in grps:
                                if 'MSH_c_hi_proxy_' in grp:
                                    needAnimProxy.append(grp)
                            # 记录Master
                            haveAnimMaster.append(master)
                # 导出动画
                sk_checkCommon.sk_checkTools().checkAnimCurveInfoExport(haveAnimMaster , 0 , 'proxy')
                sk_checkCommon.sk_checkTools().checkAnimCurveInfoImport(0 , 'proxy' , ['Master_food', 'MSH_c_hi_proxy_food'])
            # 处理新版本
            if mc.ls('TEMP_GRP'):
                masterNewGrp = []
                masterNewGrp = mc.listRelatives('TEMP_GRP', c=1, f=1)
                if masterNewGrp:
                    for master in masterNewGrp:
                        # 再排除次
                        if 'Master_food' in master and master[-1] != '_' and 'TEMP_GRP' in master:
                            animInfo = mc.ls((master.split('|')[-1] + '_*'), type='animCurve')
                            if animInfo:
                                # 查询动画信息
                                haveAnimMaster = []
                                needAnimProxy = []
                                # 记录proxy
                                # 此处是Master
                                proxy = mc.getAttr(master + '.proxyInfo')
                                # 记录master
                                haveAnimMaster.append(master)
                                # 替换信息
                                proxyPre = proxy.split('MSH_c_hi_proxy_food')[0] + 'MSH_c_hi_proxy_food'
                                masterPre = master.split('Master_food')[0] + 'Master_food'
                                # 导出动画
                                sk_checkCommon.sk_checkTools().checkAnimCurveInfoExport(haveAnimMaster , 0 , 'proxy')
                                sk_checkCommon.sk_checkTools().checkAnimCurveInfoImport(0 , 'proxy' , [masterPre, proxyPre])
        # 指定master进行处理
        else:
            for master in masterGrp:
                if 'TEMP_GRP' in master:
                    animInfo = mc.ls((master.split('|')[-1] + '_*'), type='animCurve')
                    if animInfo:
                        # 查询动画信息
                        haveAnimMaster = []
                        needAnimProxy = []
                        # 记录proxy
                        # 此处是Master
                        proxy = mc.getAttr(master + '.proxyInfo')
                        # 记录master
                        haveAnimMaster.append(master)
                        # 替换信息
                        proxyPre = proxy.split('MSH_c_hi_proxy_food')[0] + 'MSH_c_hi_proxy_food'
                        masterPre = master.split('Master_food')[0] + 'Master_food'
                        # 导出动画
                        sk_checkCommon.sk_checkTools().checkAnimCurveInfoExport(haveAnimMaster , 0 , 'proxy')
                        sk_checkCommon.sk_checkTools().checkAnimCurveInfoImport(0 , 'proxy' , [masterPre, proxyPre])

        # proxy信息备份
        self.sk_sceneProxyAnimInfoUpdate()

    # proxy Need
    # proxy动画传服务器
    def sk_sceneProxyAnimInfoUpdate(self):
        import sk_checkCommon
        reload(sk_checkCommon)
        # 获取代理物体
        proxyGrp = self.sk_sceneProxySetAdd()
        # 获取动画proxy
        needAnimProxy = []
        for proxy in proxyGrp:
            animInfo = mc.ls((proxy.split('|')[-1] + '_*'), type='animCurve')
            if animInfo:
                needAnimProxy.append(proxy)
        # 导出动画
        if needAnimProxy:
            sk_checkCommon.sk_checkTools().checkAnimCurveInfoExport(needAnimProxy , 1 , 'proxy')

    # proxy Need
    # 自动将所选master大环的proxy物体显示
    def sk_sceneMaster2ProxyDisplay(self):
        objs = mc.ls(sl=1 , l=1)
        if objs:
            for obj in objs:
                if 'Master' in obj and 'TEMP_GRP' in obj:
                    # 此处是Master
                    if mc.objExists(obj + '.proxyInfo'):
                        proxy = mc.getAttr(obj + '.proxyInfo')
                        mc.setAttr((proxy + '.v'), 1)
    '''
           【系统】【盒子系统配套】 【镜头内植物缓存】
    '''
    # proxy Need                    
    # UI-植物cache系统
    def sk_sceneVegetationCacheSystemUI(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        
        # 窗口
        if mc.window ("sk_sceneCacheSystemUI", ex=1):
            mc.deleteUI("sk_sceneCacheSystemUI", window=True)
        mc.window("sk_sceneCacheSystemUI", title="Cache System", widthHeight=(180, 70), menuBar=0)
        # 主界面
        mc.columnLayout()

        # cache导出
        mc.rowLayout()
        mc.button(label=u'Asset Cache导出', backgroundColor=[0.2, 0.5, 0.8], width=160, height=30, c='sk_sceneConfig.sk_sceneConfig().sk_sceneVegetationCacheTypeExport()')
        mc.setParent("..")
        
        # cache导人
        mc.rowLayout()
        mc.button(label=u'所有cache类别导入', backgroundColor=[0.1, 0.6, 0.1], width=160, height=30, c='sk_sceneConfig.sk_sceneConfig().sk_sceneVegetationCacheImportUI()')
        mc.setParent("..")
        
        mc.setParent("..")
        mc.showWindow("sk_sceneCacheSystemUI")

    # proxy Need
    # UI-import
    # 缓存文件统一导入
    def sk_sceneVegetationCacheImportUI(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        
        # 窗口
        if mc.window ("sk_sceneCacheImportUI", ex=1):
            mc.deleteUI("sk_sceneCacheImportUI", window=True)
        mc.window("sk_sceneCacheImportUI", title="Cache Import", widthHeight=(180, 360), menuBar=0)
        # 主界面
        mc.columnLayout()

        # 项目列表
        mc.rowLayout()
        mc.optionMenuGrp('sk_sceneCacheProjectList', adjustableColumn=1, width=180, height=30 , cc='sk_sceneConfig.sk_sceneConfig().sk_sceneVegetationInfoListGet()')
        mc.menuItem('ZoomWhiteDolphin')
        mc.menuItem('Calimero')
        mc.menuItem('HeroFactory')
        mc.setParent("..")

        # cache列表
        mc.rowLayout()
        mc.textScrollList('sk_sceneCacheInfoList', width=180, height=190, doubleClickCommand='sk_sceneConfig.sk_sceneConfig().sk_sceneVegetationCacheDoImport()')
        mc.setParent("..")
        
        # 选取导入
        mc.rowLayout()
        mc.button(label=u'选取cache类别导入', backgroundColor=[0.1, 0.8, 0.2], width=180, height=35, c='sk_sceneConfig.sk_sceneConfig().sk_sceneVegetationCacheDoImport()')
        mc.setParent("..")
        
        # 全部导入
        mc.rowLayout()
        mc.button(label=u'所有cache类别导入', backgroundColor=[0.7, 0.1, 0.1], width=180, height=35, c='sk_sceneConfig.sk_sceneConfig().sk_sceneVegetationCacheDoImport(1)')
        mc.setParent("..")
        
        mc.setParent("..")
        mc.showWindow("sk_sceneCacheImportUI")
        
        self.sk_sceneVegetationInfoListGet()
        
    # Proxy Need
    # UI系列函数
    # 获取指定项目服务器端目录
    def sk_sceneVegetationInfoListGet(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        # 获取项目名
        projectInfo = mc.optionMenuGrp('sk_sceneCacheProjectList', value=1, q=1)
        projectSimple = sk_infoConfig.sk_infoConfig().checkProjectNameFull2Simple(projectInfo)
        # 获取cluster服务器端路径
        serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
        serverPathCache = serverPathCache.split('/GeoCache/')[0] + '/ClusterCache/'
        # 获取下属文件夹信息
        fileDirInfo = mc.getFileList(folder=serverPathCache)
        # 剔除非文件夹信息
        for info in fileDirInfo:
            if '.' in info:
                fileDirInfo.remove(info)
        # 更新list
        mc.textScrollList('sk_sceneCacheInfoList', edit=1, removeAll=1)
        for info in fileDirInfo:
            mc.textScrollList('sk_sceneCacheInfoList', edit=1, append=info)
            
    # Proxy Need
    # UI系列函数
    # 获取选取物并转信息
    def sk_sceneVegetationCacheDoImport(self, returnType=0):
        import sk_infoConfig
        reload(sk_infoConfig)
        # 获取项目名
        projectInfo = mc.optionMenuGrp('sk_sceneCacheProjectList', value=1, q=1)
        projectSimple = sk_infoConfig.sk_infoConfig().checkProjectNameFull2Simple(projectInfo)
        # 获取item名
        if returnType == 0:
            items = mc.textScrollList('sk_sceneCacheInfoList', q=1, selectItem=1)
        else:
            items = mc.textScrollList('sk_sceneCacheInfoList', q=1, allItems=1)
        cacheInfo = []
        if items:
            for item in items:
                cacheInfo.append((projectSimple + '_' + item))
        # 执行函数
        if cacheInfo:
            # 如zm_p001002_h
            self.sk_sceneVegetationCacheTypeImport(cacheInfo)
            
    # Proxy Need
    # 【核心函数】proxy植物缓存文件输出
    # 带动画的文件，需要将文件名改成类似
    def sk_sceneVegetationCacheTypeExport(self, server = 1):
        import sk_infoConfig
        reload(sk_infoConfig)
        import sk_checkCommon
        reload(sk_checkCommon)
        
        # 检测文件名，必须是道具类
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfo[1][0] != 'p':
            mc.warning(u'================请用道具类文件输出缓存================')
            mc.warning(u'======文件名如[zm_p000003benthophyte_h_tx]======')
        else:
            # 获取时间轴
            frameStart = mc.playbackOptions(q=1, min=1) 
            frameEnd = mc.playbackOptions(q=1, max=1) 
            
            # 镜头信息
            dirInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            
            # HMLType信息
            HMLType = shotInfo[2]
            fileName = dirInfo[0] + '_' + dirInfo[1][0:7] +  '_'  + HMLType + '_cluster_geoCache'

            # 本地及服务器端路径
            localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()
            localPathCache = localPathCache.split('/geoCacheTemp/')[0] + '/geoCacheTemp/' + dirInfo[0] + '/' + dirInfo[1][0:7] + '_' + HMLType + '/'
            
            serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
            serverPathCache = serverPathCache.split('/GeoCache/')[0] + '/ClusterCache/' + dirInfo[1][0:7] + '_'  + HMLType + '/'

            # 清理历史文件
            oldFiles = mc.getFileList(folder=localPathCache)
            if oldFiles:
                for oldfile in oldFiles:
                    mc.sysFile((localPathCache + oldfile), delete=1)
                
            # 获取cache物体
            meshes = mc.ls(type='mesh', l=1)
            cacheObjs = []
            if meshes:
                for mesh in meshes:
                    obj = mc.listRelatives(mesh, p=1, type='transform')[0]
                    if obj != 'MSH_c_hi_proxy_':
                        cacheObjs.append(mc.ls(obj, l=1)[0])
            # 可能有org的shape节点
            cacheObjs = list(set(cacheObjs))
            # 经典版本cache处理
            mc.select(cacheObjs)
            # 删除已有的cache
            try:
                mel.eval('deleteCacheFile 3 { "keep", "", "geometry" } ;')
            except:
                pass
            mc.select(cl=1)
    
            # 经典版本cache处理
            # 执行缓存创建
            if server == 0:
                sk_checkCommon.sk_checkTools().checkCacheDoCreate((fileName + '_0'), cacheObjs, localPathCache)
                # 输出分段物体信息
                objPath = localPathCache + 'cache_objs_0.txt'
                sk_infoConfig.sk_infoConfig().checkFileWrite(objPath, cacheObjs)
                # 输出分段信息
                cacheIndexPath = localPathCache + 'cache_objsIndex.txt'
                sk_infoConfig.sk_infoConfig().checkFileWrite(cacheIndexPath, '0')

                # 传服务器
                updateCacheCMD = 'zwXcopyEx(\"' + localPathCache + '\", \"' + serverPathCache + '\",1,1)'
                mel.eval(updateCacheCMD)
                print u'===缓存全部创建完毕==='
            
            if server == 1:
                sk_checkCommon.sk_checkTools().checkCacheDoCreate((fileName + '_0'), cacheObjs, serverPathCache)
                # 输出分段物体信息
                objPath = serverPathCache + 'cache_objs_0.txt'
                sk_infoConfig.sk_infoConfig().checkFileWrite(objPath, cacheObjs)
                # 输出分段信息
                cacheIndexPath = serverPathCache + 'cache_objsIndex.txt'
                sk_infoConfig.sk_infoConfig().checkFileWrite(cacheIndexPath, '0')
                
            '''
            #cacheInfos = mc.getFileList(folder=localPathCache)
            
            #for info in cacheInfos:
            #    if '_cluster_geoCache' in info :
            #        fileInfo = info
            #        updateCacheCMD = 'zwSysFile "copy" ' + '"' + (localPathCache + fileInfo) + '"' + ' ' + '"' + (serverPathCache + fileInfo) + '"' + ' true'
            #        mel.eval(updateCacheCMD)
            #        print u'===传输[%s]完毕==='%fileInfo
            print u'===缓存全部创建完毕==='
            '''
            
    # Proxy Need
    # 【核心函数】按类型导入cache
    def sk_sceneVegetationCacheTypeImport(self, listType=[]):
        import sk_infoConfig
        reload(sk_infoConfig)
        import sk_checkCommon
        reload(sk_checkCommon)
        import os
        
        '''
        # 清理ShapeOrig
        shapes = mc.ls(type='mesh')
        for mesh in shapes:
            if mc.getAttr(mesh + '.intermediateObject'):
                try:
                    mc.delete(mesh)
                except:
                    pass
        '''
        # 服务器端综合信息
        serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
        serverPathCache = serverPathCache.split('/GeoCache/')[0] + '/GeoCache/'
        serverPathCache = serverPathCache.replace('/GeoCache/', '/ClusterCache/')

        # 先检测cache是否在服务器端
        # 有则加载，无则警告
        if listType:
            # 错误信息
            errorinfo = []
            usefulList = []
            # typeInfo : zm_p001002_h
            for typeInfo in listType:
                cachePath = serverPathCache + typeInfo.split('_')[1] + '_' + typeInfo.split('_')[2] + '/'
                cachePathFile = cachePath + typeInfo + '_cluster_geoCache_0.xml'
                # 判断文件是否在
                if os.path.exists(cachePathFile):
                    usefulList.append(typeInfo)
                else:
                    errorinfo.append(cachePathFile)
                    errorinfo.append(u'==========服务器端cache文件【%s】不存在==========' % (typeInfo))

            # 无措继续
            sceneVegetationTypeInfo = self.sk_sceneVegetationTypeInfo()
            if sceneVegetationTypeInfo:
                # 清理ShapeOrig
                shapes = mc.ls(type='mesh')
                for mesh in shapes:
                    if mc.getAttr(mesh + '.intermediateObject'):
                        mc.delete(mesh)
                        
                # 备份材质
                MatLists = sk_checkCommon.sk_checkTools().checkCacheRecordMaterial()
                
                # 删除已有的cache
                try:
                    mel.eval('deleteCacheFile 3 { "keep", "", "geometry" } ;')
                except:
                    pass
                
                # 载入参考
                for objGrp in sceneVegetationTypeInfo:
                    #print u'-------------'
                    #print objGrp[0]
                    #print usefulList
                    # 第一个元素是type信息
                    if objGrp[0] in usefulList:
                        # 准备导入
                        cachePath = serverPathCache + objGrp[0].split('_')[1] + '_' + objGrp[0].split('_')[2] + '/'
                        cachePathFile = cachePath + objGrp[0] + '_cluster_geoCache_0.xml'
                        cacheObjsTxt = cachePath + 'cache_objs_0.txt'
                        # 调整objGrp[1]顺序，否则参考会错
                        if len(objGrp[1]) > 1:
                            tempObjs = []
                            cacheServerObjs = sk_infoConfig.sk_infoConfig().checkFileRead(cacheObjsTxt)
                            for cacheObj in cacheServerObjs:
                                objName = cacheObj.split('|')[-1]
                                for k in range(len(objGrp[1])):
                                    print '*****'
                                    print objName
                                    print objGrp[1][k]
                                    if objName in objGrp[1][k]:
                                        tempObjs.append(objGrp[1][k])
                            objGrp[1] = tempObjs
                        #print u'-------------'
                        #print objGrp[1]
                        # 导入cache
                        #print usefulList
                        mc.select(objGrp[1]) 
                        melCacheCMD = 'doImportCacheFile ' + '"' + cachePathFile + '"' + ' "xml" {} {};' 
                        print melCacheCMD
                        mel.eval(melCacheCMD)
                        mc.select(cl=1)
                        print '\n'
                        print u'======================【%s】cache加载一株完毕======================' % (objGrp[0])
                        print '\n'
                        
                # cache合并
                mel.eval('zwOptimizeGeoCache();')
                        
                # 还原材质
                sk_checkCommon.sk_checkTools().checkCacheReturnMaterial(MatLists)
                
                # 烘焙表情贴图
                sk_checkCommon.sk_checkTools().checkCacheBakeTexAniFiles()
                
                # 有错报错，无错继续
                if errorinfo:
                    print u'--------------------以下ID的cache不存在--------------------'
                    print u'\n'
                    for info in errorinfo:
                        print info
                    print u'\n'
                    print u'-------------------------------------------------------'
                print '\n'
                print u'======================！！！cache全部加装【完毕】！！！======================'
                print '\n'
                
    # 动画用proxy参考载入
    # 只给参考的物体，cache植物进入SET_GRP
    def sk_proxyAnimVegetationCacheImport(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        import os
        objs = mc.ls(sl = 1,l =1)
        if objs:
            errorinfo = []
            # 获取asset信息
            assetInfos = []
            for obj in objs:
                refNode = mc.referenceQuery(obj,referenceNode = 1)
                assetInfos.append(refNode)
            refNodes = list(set(assetInfos))
            # 获取cache物体
            allCacheObjs = []
            for refNode in refNodes:
                assetInfo = refNode[:10]
                cacheObjs = []
                # 获取root
                assetObjs = mc.referenceQuery(refNode , nodes= 1)
                for grp in assetObjs:
                    if mc.nodeType(grp) == 'mesh' and 'proxy' not in grp:
                        cacheObjs.append(mc.listRelatives(grp,p =1 ,f = 1)[0])
                cacheObjs = list(set(cacheObjs))
                allCacheObjs.append([assetInfo,cacheObjs])
            # 处理cache
            serverPathCache = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            serverPathCache = serverPathCache + 'data/ClusterCache/'
            for objGrp in allCacheObjs:
                cachePath = serverPathCache + objGrp[0][:10].split('_')[1] + '/'
                cachePathFile = cachePath + objGrp[0][:10] + '_cluster_geoCache_0.xml'
                # 开始载入参考
                if os.path.exists(cachePathFile):
                    mc.select(objGrp[1])
                    melCacheCMD = 'doImportCacheFile ' + '"' + cachePathFile + '"' + ' "xml" {} {};' 
                    mel.eval(melCacheCMD)
                else:
                    errorinfo.append(objGrp[0][:10])
            
            # cache合并
            mel.eval('zwOptimizeGeoCache();')
            
            if errorinfo:
                print u'--------------------以下ID的cache不存在--------------------'
                print u'\n'
                for info in errorinfo:
                    print info
                print u'\n'
                print u'-------------------------------------------------------'
            print '\n'
            print u'======================！！！cache全部加装【完毕】！！！======================'
            print '\n'
    
    # proxyCache开关
    def sk_proxyCacheRunOnOff(self):
        cacheFiles = mc.ls(type = 'cacheFile')
        if cacheFiles:
            proxyCacheFiles = []
            for cacheFile in cacheFiles:
                if '_cluster_geoCache_' in cacheFile:
                    proxyCacheFiles.append(cacheFile)
            if proxyCacheFiles:
                state = mc.getAttr(proxyCacheFiles[0] + '.enable')
                if state == 0:
                    setState = 1
                else:
                    setState = 0
                for cacheFile in proxyCacheFiles:
                    mc.setAttr(( cacheFile + '.enable' ),setState)
                    
    # proxy插件补充
    # 把ID补全
    def sk_proxyIDCompleteConfig(self):
        # proxySet
        if mc.objExists('Proxy_Set'):
            pass
        else:
            self.sk_sceneProxySetAdd()
        proxyObjs = self.sk_sceneProxySetObjects()
        # proxyID修复
        for proxy in proxyObjs:
            if mc.objExists(proxy.split('|')[-1] + '.proxyID'):
                path = mc.getAttr(proxy.split('|')[-1] + '.proxyPath')
                IDInfo = path.split('/')[-1].split('_')
                proxyID = IDInfo[0] + '_' + IDInfo[1]
                mc.setAttr((proxy + '.proxyID'),proxyID,type = 'string')
    
    '''
            清理SG节点
    '''
    # 删除指定物体的SG节点
    def sk_sceneCleanMeshSG(self):
        objs = mc.ls(sl=1, l=1)
        for obj in objs:
            # 获取shape名
            mc.select(obj)
            mesh_c = mc.listRelatives(c=1 , s=1, f=0)[0]
            # 获取连接的SG节点
            SGInfo = list(set(mc.listConnections(mesh_c, destination=1, type='shadingEngine')))
            try:
                SGInfo.remove('initialShadingGroup')
            except:
                pass
            # 清理SG
            if SGInfo:
                mc.delete(SGInfo)
        mc.select(cl=1)

    '''
           【系统】【CAM,AUDIO】       
            动画用导cam及音频
    '''
    # 导入项目的音频及cam及帧信息
    def sk_sceneImportCameraAudioFrame(self):    
        # camera
        self.sk_sceneImportCamera()
        # FPS
        self.sk_sceneImportFrame('FPS')
        # frame
        self.sk_sceneImportFrame('frame')
        # audio
        self.sk_sceneImportAudio()
        # 开始镜头信息
        import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        grpCList = ['zm']
        # 处理组
        if shotInfo[0] in grpCList:
            self.sk_sceneReorganize()
        
        
    # 导入项目的cam
    def sk_sceneImportCamera(self):
        import os
        import sk_infoConfig
        reload(sk_infoConfig)
        # 开始镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 处理清单
        camIList = ['zm']
        audioIList = ['zm', 'cl']
        camProjectInfos = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        audioProjectInfos = sk_infoConfig.sk_infoConfig().checkProjectAudioPath(shotInfo[0])
        # 开始cam部分
        camName = 'cam_' + shotInfo[1] + '_' + shotInfo[2]
        # 判断摄像机在不在
        if mc.ls(camName):
            # print (unicode('==============================!!!已存在相机【%s】!!!==============================' % (str(camName)), 'utf8'))
            print (u'==============================!!!已存在相机【%s】!!!==============================' % camName)
        else:
            if shotInfo[0] in camIList:
                camPath = "//file-cluster/GDC/Projects/" + camProjectInfos + "/" + camProjectInfos + "_Scratch/TD/SetCam/" + shotInfo[1] + "/" 
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '.ma'
                # 判断是否存在
                file = os.path.exists(camPath)
                if file:
                    # 导入相机，清除namespace
                    mc.file(camPath , i=1)
                    # print (unicode('==============================成功【导入】【%s】==============================' % (str(camName)), 'utf8'))
                    print (u'==============================成功【导入】【%s】==============================' % camName)
                else:
                    # 创建相机
                    camTemp = mc.camera()
                    mc.rename(camTemp[1], (camName + 'Shape'))
                    mc.rename(camTemp[0], camName)
                    # print (unicode('==============================成功【创建】【%s】==============================' % (str(camName)), 'utf8'))
                    print (u'==============================成功【创建】【%s】==============================' % camName)
                # 处理安全框
                camShape = mc.listRelatives(camName, s=1)[0]
                mc.setAttr((camShape + '.displayResolution'), 1)
                mc.setAttr((camShape + '.displayGateMask'), 1)
                mc.setAttr((camShape + '.displaySafeAction'), 1)
                mc.setAttr((camShape + '.displaySafeTitle'), 0)
                # 处理其他信息
                mc.setAttr((camShape + '.nearClipPlane'), 0.1)
                mc.setAttr((camShape + '.farClipPlane'), 1000000)
                
    
    # 导入Audio
    def sk_sceneImportAudio(self):
        import os
        import sk_infoConfig
        reload(sk_infoConfig)
        # 开始镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 处理清单
        camIList = ['zm']
        audioIList = ['zm', 'cl']
        camProjectInfos = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        audioProjectInfos = sk_infoConfig.sk_infoConfig().checkProjectAudioPath(shotInfo[0])
        # 开始audio部分
        if shotInfo[0] in audioIList:
            audios = mc.ls(type='audio')
            if audios:
                mc.delete(audios)
            audioPath = "//file-cluster/GDC/Projects/" + camProjectInfos + "/Reference/Animation_production/" + audioProjectInfos + str(shotInfo[1]) + '/Audio files/wav/'
            audioPath += shotInfo[2] + '.wav'
            # 判断是否存在
            file = os.path.exists(audioPath)
            if file:
                # 导入audio
                cmd = "doSoundImportArgList (\"1\",{\"" + audioPath + "\",\"0\"});"
                mel.eval(cmd)
                # 处理Offset
                audios = mc.ls(type='audio')
                offsetFrame = mc.playbackOptions(min=1, q=1)
                mc.setAttr((audios[0] + '.offset'), offsetFrame)
                # print (unicode('==============================【成功】本镜头【音频】【导入】==============================', 'utf8'))
                print (u'==============================【成功】本镜头【音频】【导入】==============================')
            else:
                # mc.warning(unicode('==============================【！！！错误！！！】本镜头【音频】不存在==============================', 'utf8'))
                mc.warning(u'==============================【！！！错误！！！】本镜头【音频】不存在==============================')

    # 导入起始|结束帧
    def sk_sceneImportFrame(self, configType='FPS'):
        import sk_infoConfig
        reload(sk_infoConfig)
        # 开始镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 命令
        shot = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        # 开始处理
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        fpsFrame = anim.fps
        resW = anim.resolutionW
        resH = anim.resolutionH
        # 分辨率
        mc.setAttr(('defaultResolution.width'), resW)
        mc.setAttr(('defaultResolution.height'), resH)
        ratio = resW / (resH + float('.0'))
        mc.setAttr(('defaultResolution.deviceAspectRatio'), ratio)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        # FPS
        if configType == 'FPS':
            if fpsFrame:
                if fpsFrame == 25:
                    mc.currentUnit(time='pal')
                if fpsFrame == 24:
                    mc.currentUnit(time='film')
                if fpsFrame == 30:
                    mc.currentUnit(time='ntsc')
            else:
                # mc.warning(unicode('==============================!!!【错误】本镜头【帧速率】【不存在】!!!==============================', 'utf8'))
                mc.warning(u'==============================!!!【错误】本镜头【帧速率】【不存在】!!!==============================')
        # frame
        if configType == 'frame':
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
            else:
                # mc.warning(unicode('==============================!!!【错误】本镜头【帧信息】【不存在】!!!==============================', 'utf8'))
                mc.warning(u'==============================!!!【错误】本镜头【帧信息】【不存在】!!!==============================')
        # 设置帧播放模式
            mc.playbackOptions(playbackSpeed=1)
        # 允许undo
            mc.undoInfo(state=True, infinity=True)

    '''
           【系统】 【场景文件整理】
    '''
    # 根据参考整理文件 0 不删除多余物体，保留在OTC | 1 删除多余物体
    # finalLayout环节先清理约束再处理分组
    def sk_sceneReorganize(self, finalLayout=0):
        import sk_referenceConfig
        reload(sk_referenceConfig)
        import sk_checkCommon
        reload(sk_checkCommon)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRoot = []
        refNodes = []
        for refLeval in refInfos[0]:
            refNodes = refNodes + refLeval
        for refNode in refNodes:
            refObjs = mc.referenceQuery(refNode , nodes=1)
            # Q,need to test
            if refObjs:
                refRoot.append(refObjs[0])
        # CAM_GRP
        if mc.ls('CAM_GRP'):
            camGrp = 'CAM_GRP'
        else:
            camGrp = mc.group(em=1, name='CAM_GRP')
        # CHR_GRP
        if mc.ls('CHR_GRP'):
            chrGrp = 'CHR_GRP'
        else:
            chrGrp = mc.group(em=1, name='CHR_GRP')
        # PRP_GRP
        if mc.ls('PRP_GRP'):
            prpGrp = 'PRP_GRP'
        else:
            prpGrp = mc.group(em=1, name='PRP_GRP')
        # SET_GRP
        if mc.ls('SET_GRP'):
            setGrp = 'SET_GRP'
        else:
            setGrp = mc.group(em=1, name='SET_GRP')
        # VFX_GRP
        if mc.ls('VFX_GRP'):
            vfxGrp = 'VFX_GRP'
        else:
            vfxGrp = mc.group(em=1, name='VFX_GRP')
        # 鱼群集群
        if mc.ls('Cluster_GRP'):
            clusterFlowGrp = 'Cluster_GRP'
        else:
            clusterFlowGrp = mc.group(em=1, name='Cluster_GRP')
        # OTC_GRP
        if mc.ls('OTC_GRP'):
            otcGrp = 'OTC_GRP'
        else:
            otcGrp = mc.group(em=1, name='OTC_GRP')
        # 打组
        if otcGrp not in mc.ls(vfxGrp, l=1)[0]:
            mc.parent(vfxGrp, otcGrp)
        if otcGrp not in mc.ls(clusterFlowGrp, l=1)[0]:
            mc.parent(clusterFlowGrp, otcGrp)
        # needRoot
        needRoot = ['persp', 'top', 'front', 'side', 'CAM_GRP', 'CHR_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP']
        keepRoot = ['CHR_GRP', 'CAM_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP', 'persp', 'top', 'front', 'side']
        # 开始处理
        # 优先记录：带有namespace的基本GRP
        ogGrp = ['CHR_GRP', 'CAM_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP']
        ogNsGrp = []
        for grp in ogGrp:
            checkGrps = mc.ls('*:*' + grp + '*') + mc.ls('*:*:*' + grp + '*')
            if checkGrps:
                for obj in checkGrps:
                    lastName = obj.split(':')[-1]
                    ogNsGrp.append(obj[0:-1*(len(lastName)+1)])
        ogNsGrp = list(set(ogNsGrp))
        print refRoot
        # 1为参考方式处理
        # 这个方式对VFX会有影响,所以要修正
        for root in refRoot:
            # 首先判断是否在VFX_GRP和Cluster_GRP
            if '|VFX_GRP|' not in mc.ls(root, l=1)[0] and 'Cluster_GRP' not in mc.ls(root, l=1)[0]:
                print root
                refPath = mc.referenceQuery(root, filename=1)
                path = refPath.lower()
                # CAM
                if '/camera/' in path or '/episode_camera/' in path:
                    # 判断是否在CAM_GRP组里
                    if ('|' + camGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, camGrp)
                # CHR
                if '/characters/' in path:
                    # 判断是否在CHR_GRP组里
                    if ('|' + chrGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, chrGrp)
                    else:
                        # 处理上级物体有RNgroup的组的情况
                        upGrp = mc.listRelatives(root,p=1)
                        if upGrp:
                            upGrp = upGrp[0]
                            if 'rngroup' in upGrp.lower():
                                mc.parent(root, chrGrp)
                                mc.delete(upGrp)
                # PRP
                if '/props/' in path:
                    # 判断是否在PRP_GRP组里
                    if ('|' + prpGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, prpGrp)
                    else:
                        # 处理上级物体有RNgroup的组的情况
                        upGrp = mc.listRelatives(root,p=1)
                        if upGrp:
                            upGrp = upGrp[0]
                            if 'rngroup' in upGrp.lower():
                                mc.parent(root, prpGrp)
                                mc.delete(upGrp)
                # SET
                if '/sets/' in path:
                    # 判断是否在SET_GRP组里
                    if ('|' + setGrp + '|') not in mc.ls(root , l=1)[0]:
                        mc.parent(root , setGrp)
                    else:
                        # 处理上级物体有RNgroup的组的情况
                        upGrp = mc.listRelatives(root,p=1)
                        if upGrp:
                            upGrp = upGrp[0]
                            if 'rngroup' in upGrp.lower():
                                # 对于参考的子参考使用try
                                try:
                                    mc.parent(root, setGrp)
                                    mc.delete(upGrp)
                                except:
                                    pass

        # 整理外部约束之类的，用outLine方式修正
        allGrps = mc.ls(assemblies=True)
        for root in allGrps:
            if finalLayout == 1 and root not in needRoot:
                try:
                    mc.delete(root)
                except:
                    pass
            if finalLayout == 2:
                if root:
                    if root not in keepRoot:
                        mc.parent(root , 'OTC_GRP')
        
        # 清理不必要的namespace
        if ogNsGrp:
            import sk_common
            reload(sk_common)
            for ns in ogNsGrp:
                sk_common.sk_deleteNamespace(ns)


    # OTC结构处理：删除
    def sk_sceneGRPDelete(self, fileGRP='OTC'):
        import sk_infoConfig
        reload(sk_infoConfig)
      
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePathServer + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + fileGrpType + fileFomat
        import os
        if os.path.exists(otcFileServer):
            cmd = 'zwSysFile(\"del\",\"' + otcFileServer + '\",\"\",1)'
            mel.eval(cmd)

    # OTC结构处理：导出
    def sk_sceneGRPExport(self, fileGRP='OTC' , server=1):
        import sk_infoConfig
        reload(sk_infoConfig)
        renderFilePath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfo[0])
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFile = renderFilePath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + fileGrpType + fileFomat
        
        root = mc.ls(assemblies=True)
        if root:
            if (fileGRP + '_GRP') in root:
                # OTC和SET处理，导出
                mc.select(fileGRP + '_GRP')
                mc.file(otcFile, force=1, options="v=0" , type=fileTypeFull, preserveReferences=1, exportSelected=1)
        mc.select(cl=1)
        
        # 传至服务器
        if server:
            renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
            otcFileServer = renderFilePathServer + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + fileGrpType + fileFomat
            cmd = 'zwSysFile(\"copy\",\"' + otcFile + '\",\"' + otcFileServer + '\",1)'
            mel.eval(cmd)
            
    # 处理OTC的SET文件
    def sk_sceneSETRefShaderReset(self , info , serverModify = 1):
        import sk_infoConfig
        reload(sk_infoConfig)
        import sk_referenceConfig
        reload(sk_referenceConfig)
        # 处理OTC的SET文件，但不载入参考
        #mc.file(rename = (info[0] + '_' + str(info[1]) + '_' + str(info[2] + '.mb')) )
        
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
        fileGrpType = '_set_render'
        
        if serverModify == 0:
            needFilePath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()

        if serverModify == 1:
            needFilePath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()

        needSetFile = needFilePath + info[0] + '_' + info[1] + '_' + info[2] + fileGrpType + fileFomat
        
        import os
        if os.path.exists(needSetFile):
            # 不加载参考导入
            mc.file(needSetFile , open = 1, loadReferenceDepth = 'none' , force = 1)
            print u'====================开始处理SET_GRP文件===================='
            # 处理好文件
            # 在importOTC之前处理好anim中材质更改的情况
            sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            mc.file(save = 1, force = 1)

        
        if serverModify == 0:
            # 传至服务器
            renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
            otcFileServer = renderFilePathServer + info[0] + '_' + info[1] + '_' + info[2] + fileGrpType + fileFomat
            print otcFileServer
            cmd = 'zwSysFile(\"copy\",\"' + needSetFile + '\",\"' + otcFileServer + '\",1)'
            mel.eval(cmd)
        print u'====================SET_GRP更新完毕===================='

    # OTC结构处理：导入
    def sk_sceneGRPImport(self, fileGRP='OTC'):
        import sk_infoConfig
        reload(sk_infoConfig)
        import sk_referenceConfig
        reload(sk_referenceConfig)
        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfo[0])
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePathServer + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + fileGrpType + fileFomat
        
        # 判断otcFile存在与否
        import os
        if os.path.exists(otcFileServer):
            # 在则删除OTC_GRP，并import去掉namespace
            # finalLayout阶段是OTC_GRP是空的
            if mc.ls(fileGRP + '_GRP'):
                mc.delete(fileGRP + '_GRP')
            # import 
            # 记录时间
            import time
            timeNow = time.ctime().split(" ")[3].replace(":", "_")
            # 记录毫秒
            import datetime
            msTime = datetime.datetime.now().microsecond
            timeNow = timeNow + str(msTime / 100000)
            #timeMsec = datetime.datetime.now().microsecond
            #timeNow = timeNow + '_' + str(timeMsec)
            ns = 'food' + timeNow
            if fileGRP == 'SET':
                print u'------------------'
                print 'setInfo'
                print fileTypeFull
                print ns
                # SET文件需要把参考从anim替换成render
                mc.file(otcFileServer, i=1 , loadReferenceDepth="none", namespace = ns , type=fileTypeFull , preserveReferences=1 , options="v=0")
                # 清理set贴图方面的信息
                sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
                # 获取references信息
                refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
                rfnNodeLv1 = refInfos[0][0]
                rfnPathLv1 = refInfos[1][0]                
                # 导入参考，注意将_ms_anim替换成_ms_render
                # OTC内的参考不参与处理
                # shareNode只能对第一级reference处理。。。
                if rfnNodeLv1:
                    for i in range(len(rfnNodeLv1)):
                        pathLower = rfnPathLv1[i].lower()
                        if 'set' in pathLower:
                            newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                            mc.file(newPath, loadReference=rfnNodeLv1[i])
            if fileGRP == 'OTC':
                # VFX文件采用tx文件做参考，可以直接用于渲染，无需切换参考
                mc.file(otcFileServer, i=1 , namespace=ns , type=fileTypeFull , preserveReferences=1 , options="v=0")
            # 删除namespace
            mc.namespace(force=1 , moveNamespace=[(':' + ns) , ':'])
            mc.namespace(removeNamespace=(':' + ns))
           
    '''
            重建displayLayer
            好像没什么用，不如导出去有效解决层没法点的问题
    '''
    def sk_sceneDisplayLayerRebuild(self):
        displayLayers = mc.listConnections('layerManager.displayLayerId')
        for layer in displayLayers:
            if layer != 'defaultLayer':
                # 读取
                objs = mc.editDisplayLayerMembers(layer, q=1)
                displayType = mc.getAttr(layer + '.displayType')
                displayLeval = mc.getAttr(layer + '.levelOfDetail')
                displayShading = mc.getAttr(layer + '.shading')
                displayTexturing = mc.getAttr(layer + '.texturing')
                displayPlayback = mc.getAttr(layer + '.playback')
                displayVisibility = mc.getAttr(layer + '.visibility')
                displayColor = mc.getAttr(layer + '.color')
                # 删除层
                try:
                    mc.delete(layer)
                except:
                    pass
                if mc.ls(layer) == []:
                    # 创建
                    mc.createDisplayLayer(n=layer)
                    # 编辑
                    mc.editDisplayLayerMembers(layer, objs)
                    mc.setAttr((layer + '.displayType'), displayType)
                    mc.setAttr((layer + '.levelOfDetail'), displayLeval)
                    mc.setAttr((layer + '.shading'), displayShading)
                    mc.setAttr((layer + '.texturing'), displayTexturing)
                    mc.setAttr((layer + '.playback'), displayPlayback)
                    mc.setAttr((layer + '.visibility'), displayVisibility)
                    mc.setAttr((layer + '.color'), displayColor)
            
    # 检测错误的参考
    def sk_sceneReferenceInfoCheck(self):
        # 只对anim文件进行检测
        import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()  
        
        import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        
        localRef = 0
        notAnimRef = 0
        # 处理参考
        for i in range(len(refPaths)):
            refPath = refPaths[i]
            path = refPath.lower()
            # 检测外部参考
            if 'c:\\' in path or 'c:/' in path or 'd:\\' in path or 'd:/' in path or 'e:\\' in path or 'e:/' in path:
                localRef = localRef + 1
            # 检测非anim参考,排除孙望参考及相机参考
            fileRef = path.split('/')[-1].split('.')[0].split('_')
            if fileRef[-1] in ['anim', 'cam', 'notex'] or path.split('/')[-1].split('.')[0] == 'qsk_model' or '_c_h_' in path:
                pass
            else:
                # 小鸡rg暂时不处理
                if shotInfo[0] == 'cl' and fileRef[-1] == 'rg':
                    pass
                else:
                    notAnimRef = notAnimRef + 1
            # 检测非法的anim参考
            if '_c_h_ms_anim.mb' in path:
                notAnimRef = notAnimRef + 1

        if shotInfo[3] == 'an' and localRef:
            # 动画文件里本地参考警告
            mc.error(u'===============【错误】有【%s】个本地参考===============' % (localRef))
            
        if shotInfo[3] == 'an' and notAnimRef:
            # 白海豚报错
            if shotInfo[0] == 'zm':
                mc.error(u'===============【错误】有【%s】个非anim参考===============' % (notAnimRef))
            # Calimero报错
            if shotInfo[0] == 'cl':
                mc.warning(u'===============【错误】有【%s】个非anim参考===============' % (notAnimRef))

    # 删除未勾选的参考
    def sk_sceneUnloadRefDel(self):
        import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        for i in range(len(refInfos[0][0])):
            loadInfo = mc.referenceQuery(refInfos[0][0][i], isLoaded=1)
            if loadInfo:
                pass
            else:
                mc.file(rfn=refInfos[0][0][i] , removeReference=1)
                mc.warning(u'===============【清理警告】未勾选的【%s】参考被清理完毕！===============' % (refInfos[0][0][i]))
    
    # 删除不需要的层(除了norender)
    def sk_sceneCleanDislayLayers(self):
        import sk_checkCommon
        reload(sk_checkCommon)
        displayLayers = mc.listConnections('layerManager.displayLayerId')
        if displayLayers:
            for layer in displayLayers:
                if layer.lower() == 'norender':
                    displayLayers.remove(layer)
            sk_checkCommon.sk_checkTools().checkCleanDisplayLayers(displayLayers)

    '''
            【场景贴图检测】
           根据当前素材名，导入所有相关的CAM，并批量渲染
    '''
    # 根据asset导入相机
    def sk_sceneAssetCamImport(self , edNum=0):
        import os
        import sk_infoConfig
        reload(sk_infoConfig)
        fileName = mc.file(query=1, exn=1).split('/')[-1]
        camResult = mc.idmtService('GetAnimsInAsset', fileName)
        if camResult:
            shotInfo = camResult.split('|')
            # 获取常用数据
            projectInfo = fileName.split('_')[0]
            projectFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(projectInfo)
            serverPathPre = "//file-cluster/GDC/Projects/" + projectFullName + '/Project/scenes/Animation/episode_'
            # 创建级别CAM组
            if mc.ls('CAM_TEST_GRP'):
                mc.delete('CAM_TEST_GRP')
            mc.group(em=1, name='CAM_TEST_GRP')
            for shot in shotInfo:
                if edNum == 0 or shot.split('_')[0] == edNum:
                    # 创建分集group
                    if mc.ls('CAM_' + str(shot.split('_')[0])):
                        pass
                    else:
                        mc.group(em=1, name=('CAM_' + str(shot.split('_')[0])))
                    if '|CAM_TEST_GRP|' not in mc.ls(('CAM_' + str(shot.split('_')[0])), l=1)[0]:
                        mc.parent(('CAM_' + str(shot.split('_')[0])), ('CAM_TEST_GRP'))
                    camFilePath = serverPathPre + str(shot.split('_')[0]) + '/episode_camera/' + projectInfo + '_' + shot + '_cam.ma'
                    if os.path.exists(camFilePath):
                        # 非baked
                        if mc.ls('cam_' + shot):
                            mc.delete('cam_' + shot)
                            mc.file(camFilePath , i=1)
                            mc.parent(('cam_' + shot), ('CAM_' + str(shot.split('_')[0])))
                        else:
                            if mc.ls('cam_' + shot + '_baked') == []:
                                mc.file(camFilePath , i=1)
                                try:
                                    mc.parent(('cam_' + shot), ('CAM_' + str(shot.split('_')[0])))
                                except:
                                    mc.parent(('cam_' + shot + '_baked'), ('CAM_' + str(shot.split('_')[0])))
                        # baked
                        if mc.ls('cam_' + shot + '_baked'):
                            mc.delete('cam_' + shot + '_baked')
                            mc.file(camFilePath , i=1)
                            mc.parent(('cam_' + shot + '_baked'), ('CAM_' + str(shot.split('_')[0])))
                        else:
                            if mc.ls('cam_' + shot) == []:
                                mc.file(camFilePath , i=1)
                                try:
                                    mc.parent(('cam_' + shot + '_baked'), ('CAM_' + str(shot.split('_')[0])))
                                except:
                                    mc.parent(('cam_' + shot), ('CAM_' + str(shot.split('_')[0])))
                    else:
                        print (u'==============================!!!相机【%s】不存在!!!==============================' % shot)
            print (u'==============================！！！所有相机成功导入！！！==============================')           
                        
    # 批量渲染
    # 必须存到本地
    # 并且工程目录在本地
    def sk_sceneCamAssetRender(self , frameType=0 , renderType=1):
        if mc.ls('CAM_TEST_GRP'):
            import sk_infoConfig
            reload(sk_infoConfig)
            import sk_checkCommon
            reload(sk_checkCommon)
            cams = mc.listRelatives('CAM_TEST_GRP' , ad=1 , type='camera')
            # 获取素材名信息
            sceneName = mc.file(sceneName=1 , q=1)
            projectInfoSimple = sceneName.split('/')[-1].split('_')[0]
            projectFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(projectInfoSimple)
            assetID = sceneName.split('/')[-1].split('_')[1]
            cmdBatFile = 'E:/' + assetID + '_renderCheck.bat'
            # 创建文本
            if cams:
                for cam in cams:
                    # 启动渲染CAM
                    mc.setAttr((cam + '.renderable'), 1)
                    # 获取镜头号信息
                    camGrp = mc.listRelatives(cam, p=1, type='transform')[0]
                    episodeNum = camGrp.split('_')[1]
                    shotNum = camGrp.split('_')[2][0:3]
                    fileName = projectInfoSimple + '_' + str(episodeNum) + '_' + str(shotNum) + '.png'
                    path = '//file-cluster/GDC/Projects/' + projectFullName + '/' + projectFullName + '_Scratch/Mastlighting/Compositiong/Detect/' + assetID + '/' + episodeNum + '/' + shotNum + '/'
                    mc.sysFile(path, makeDir=True)
                    # 获取帧信息
                    if frameType == 1:
                        shotInfo = projectInfoSimple + '_' + str(episodeNum) + '_' + str(shotNum)
                        anim = idmt.pipeline.db.GetAnimByFilename(shotInfo)
                        startFrame = anim.frmStart
                        endFrame = anim.frmEnd
                        mc.currentTime((endFrame - startFrame + 1) / 2)
                        renderFrame = (endFrame - startFrame + 1) / 2
                    if frameType == 0:
                        renderFrame = mc.currentTime(q=1)
                    # renderType
                    # 模式1，直接渲染，但XP容易出现多进程一起运行
                    if renderType == 0:
                        melCMD = 'system(\"start render.exe -s ' + str(renderFrame) + ' -e ' + str(renderFrame) + ' -rd \\\"' + path + '\\\" -cam ' + cam + ' -im ' + fileName + ' ' + sceneName + '\")'
                        print melCMD
                        mel.eval(melCMD)
                    # 模式2，输出BAT运行
                    if renderType == 1:
                        melCMD = '\"D:/Alias/Maya2012x64/bin/render.exe\" -r mr -art -s ' + str(renderFrame) + ' -e ' + str(renderFrame) + ' -rd ' + path + ' -cam ' + cam + ' -im ' + fileName + ' ' + sceneName
                        if cam == cams[0]:
                            sk_infoConfig.sk_infoConfig().checkFileWrite(cmdBatFile, [melCMD])
                        else:
                            sk_infoConfig.sk_infoConfig().checkFileWrite(cmdBatFile, [melCMD], addtion=1)

    '''
            获取选取物的骨骼并蒙皮复制权重给另一个物体
    '''   
    # 整体缩放
    def sk_skinObjScale(self,sourceObj = '',scale = 1, selectMode = 0 ):
        if selectMode:
            objs = mc.ls(sl = 1)
            sourceObj = objs[0]
        joints = mc.skinCluster(sourceObj,inf = 1, q= 1)
        if joints:
            for joint in joints:
                mc.setAttr((joint + '.sx'),scale)
                mc.setAttr((joint + '.sz'),scale)
        
    # 传递蒙皮
    def sk_skinAndCopyA2B(self,sourceObj = '',targetObj= '', selectMode = 0 ):
        if selectMode:
            objs = mc.ls(sl = 1)
            sourceObj = objs[0]
            targetObj = objs[1]
        joints = mc.skinCluster(sourceObj,inf = 1, q= 1)
        if joints:
            if mc.nodeType(joints[0])== 'joint':
                # 蒙皮
                mc.select(joints)
                mc.select(targetObj,add = 1)
                #mc.skinCluster(sourceObj,targetObj,toSelectedBones =1, ignoreHierarchy = 1 , normalizeWeights = 1 , mi = 5 ,omi = 1 ,dr = 4 ,rui = 1 )
                mel.eval('newSkinCluster \"-toSelectedBones -ignoreHierarchy -normalizeWeights 1 -mi 5 -omi true -dr 4 -rui true,multipleBindPose,1\";')
                # 复制权重
                mc.select(sourceObj)
                mc.select(targetObj,add = 1)
                mel.eval('CopySkinWeights')
                mc.select(cl=1)
            else:
                mc.error(u'=============选取源【%s】没有蒙皮骨骼============='%sourceObj)
        else:
            mc.error(u'=============选取源【%s】没有蒙皮骨骼============='%sourceObj)

    '''
            面片旋转Cam
    '''   
    # UI_treeplane_aim_CAM
    def sk_sceneUITreeplaneAimCam(self):
        # 窗口
        if mc.window ("sk_sceneUITreeplaneAimCam", ex=1):
            mc.deleteUI("sk_sceneUITreeplaneAimCam", window=True)
        mc.window("sk_sceneUITreeplaneAimCam", title="Treeplane_Aim_Cam", widthHeight=(150, 100), menuBar=0)
        # 主界面
        mc.columnLayout()

        # 行按钮
        mc.rowLayout()
        # 创建aim系统
        mc.button(w=150 , h=30 , bgc=[0, .5, 0.8], label=(unicode('【创建】  Aim系统', 'utf8')) , c='sk_sceneConfig.sk_sceneConfig().sk_sceneTreeplaneAimCam(1)')
        mc.setParent("..")

        # 行按钮
        mc.rowLayout()
        # 修正aim方向
        mc.button(w=150 , h=30 , bgc=[0, .5, 0.8], label=(unicode('【修正】  Aim方向', 'utf8')) , c='sk_sceneConfig.sk_sceneConfig().sk_sceneTreeplaneAimCamConfig()')
        mc.setParent("..")

        # 行按钮
        mc.rowLayout()
        # 面片朝向CAM
        mc.button(w=150 , h=30 , bgc=[0, .5, 0.8], label=(unicode('【删除】  Aim系统', 'utf8')) , c='sk_sceneConfig.sk_sceneConfig().sk_sceneTreeplaneAimCam(0)')
        mc.setParent("..")
        
        mc.setParent("..")
        mc.showWindow("sk_sceneUITreeplaneAimCam")
        
    # setType 0  清理  |  1  创建  |
    def sk_sceneTreeplaneAimCam(self,setType = 1):
        # plance信息
        planeGrps = mc.ls('*_treeplane_*',type = 'transform',l=1) + mc.ls('*:*_treeplane_*',type = 'transform',l=1) + mc.ls('*:*:*_treeplane_*',type = 'transform',l=1)
        # CAM信息
        import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        nameCAM = 'CAM:cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_baked' 
        # 清理animC
        aimCGrp = mc.ls('*_aimC',type = 'aimConstraint') +mc.ls('*:*_aimC',type = 'aimConstraint')
        if aimCGrp:
            mc.delete(aimCGrp)
        # 清理orientC
        orientCGrp = mc.ls('*_orientC',type = 'orientConstraint') + mc.ls('*:*_orientC',type = 'orientConstraint')
        if orientCGrp:
            mc.delete(orientCGrp)
        # 设置临时组
        if mc.ls('CAM_TEMP_GRP'):
            mc.delete('CAM_TEMP_GRP')
        # 创建模式
        if setType == 1:
            camTempGrp = mc.group(name = ('CAM_TEMP_GRP') , em = 1)
            if mc.ls(nameCAM):
                if planeGrps:
                    for plane in planeGrps:
                        if plane[-1] == '_':
                            # 首先给与一个空组，坐标中心处理
                            mc.select(cl = 1)
                            tempGrp = mc.group(name = (plane.split('|')[-1] + 'food_grp'),em = 1)
                            tempGrp = mc.parent(tempGrp,camTempGrp)[0]
                            if (mc.getAttr(plane + '.tx')) == 0 and (mc.getAttr(plane + '.ty')) == 0 and (mc.getAttr(plane + '.tz')) == 0:
                                pivot = mc.xform(plane,pivots = 1,q=1,ws = 1)
                                mc.setAttr((tempGrp + '.tx'),pivot[0])
                                mc.setAttr((tempGrp + '.ty'),pivot[1])
                                mc.setAttr((tempGrp + '.tz'),pivot[2])
                            else: 
                                mc.setAttr((tempGrp + '.tx'),(mc.getAttr(plane + '.tx')))
                                mc.setAttr((tempGrp + '.ty'),(mc.getAttr(plane + '.ty')))
                                mc.setAttr((tempGrp + '.tz'),(mc.getAttr(plane + '.tz')))
                            #mc.xform(tempGrp,rotatePivot = [tx,ty,tz])
                            #mc.xform(tempGrp,scalePivot = [tx,ty,tz])
                            # 约束：grp->plane
                            orientC = mc.orientConstraint(tempGrp,plane)
                            orientC = mc.rename(orientC , (plane.split('|')[-1]+ 'orientC'))
                            # 约束:cam->grp
                            animC = mc.aimConstraint(nameCAM,tempGrp)
                            mc.setAttr((animC[0] + '.offsetY'),90)
                            animC = mc.rename(animC[0] , (plane.split('|')[-1]+ 'aimC'))
                            print u'=============[%s]与treeplane互动设置完毕============='%nameCAM
                            
                else:
                    mc.warning(u'=====================【！！！本镜头treeplane不存在！！！】=====================')
            else:
                mc.error(u'=====================【！！！本镜头相机不存在！！！】=====================')
        else:
            print u'=============[%s]与treeplane互动删除完毕============='%nameCAM
    
    # 修正系统
    def sk_sceneTreeplaneAimCamConfig(self):
        aimCGrp = mc.ls('*_aimC',type = 'aimConstraint') +mc.ls('*:*_aimC',type = 'aimConstraint')
        if aimCGrp:
            setValue = 0
            if mc.getAttr(aimCGrp[0] + '.offsetY') == 90:
                setValue = 0
            if mc.getAttr(aimCGrp[0] + '.offsetY') == 0:
                setValue = 90
            for aimC in aimCGrp:
                mc.setAttr((aimC + '.offsetY'),setValue)
            
    '''
           猥琐招数，处理模型bug
    '''
    def sk_sceneBugsCombine(self):
        objs = mc.ls(sl=1)
        for obj in objs:
            # 记录
            objName = obj
            # 这里不检测是否有父物体，但肯定有
            parent = mc.listRelatives(obj, parent=1)[0]
            path = mc.listRelatives(parent, parent=1, f=1)[0]
            box = mc.polyCube()
            # 创建临时层
            mc.group(obj)
            # 开始combine
            combineObj = mc.polyUnite(objName, box, ch=1, mergeUVSets=1)[0]
            # 删除历史
            mc.select(combineObj)
            mel.eval("DeleteHistory")
            # 开始seperate
            seperateObj = mc.polySeparate(combineObj, ch=1)
            # 对于特殊情况进行combine
            if len(seperateObj) > 3:
                lastObj = mc.polyUnite(seperateObj[0:-2], ch=1, mergeUVSets=1)[0]
            else:
                lastObj = seperateObj[0]
            # 开始清历史
            mc.select(lastObj)
            mel.eval("DeleteHistory")
            # 改名
            newObj = mc.rename(lastObj, objName)
            # 层级关系恢复
            if mc.ls(parent, type='transform'):
                mc.parent(newObj, parent)
            else:
                grp = mc.group(newObj)
                mc.rename(grp, parent)
                mc.parent(parent, path)
            # 删除余下
            boxParent = mc.listRelatives(seperateObj[-2], parent=1)[0]
            mc.delete(boxParent)
        mc.select(cl=1)
        
    '''
            【孙望】后台处理maya中难缠垃圾节点
    '''  
    def sk_sceneEdoAnimCleanBatch(self):
        import os
        import sys
        sys.path.append('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/edward/python')
        import edo_clearUpScenesUI.edo_clearUpScene as ecus
        # 读取文件路径，并备份
        fileName = mc.file(query=1, exn=1)
        fileNameSimple = fileName.split('/')[-1]
        serverPath = fileName[:(-1*len(fileNameSimple))]
        historyPath = serverPath + 'history/'
        mc.sysFile(historyPath, makeDir=True)
        # 另存备份
        newName = historyPath + fileNameSimple.split('.')[0] + '_temp.' +  fileNameSimple.split('.')[-1]
        if os.path.exists(newName):
            newName = historyPath + fileNameSimple.split('.')[0] + '_temp02.' +  fileNameSimple.split('.')[-1]
        mc.file(rename = newName)
        mc.file(save = 1 ,force = 1)
        # 开始清理
        ecus.edo_clearUpScenes()
        # 覆盖服务器端文件
        mc.file(rename = fileName)
        mc.file(save = 1 ,force = 1)
        
        #  成功代码
        return 0

        
    '''
            临时给王光伟用的贴图管理
    '''   
    def sk_sceneDisplayLayerObjects(self):
        # 获取layers
        allDisplayLayaers = mc.ls(type='displayLayer')
        import sk_checkCommon
        reload(sk_checkCommon)
        import sk_infoConfig
        reload(sk_infoConfig)
        # 开始本地路径
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        infoLocalPath = ('D:\\Info_Temp\\temp\\displayLayerInfoTemp\\' + shotInfo[0] + '\\' + shotInfo[1] + '\\')
        mc.sysFile(infoLocalPath, makeDir=True)
        sk_infoConfig.sk_infoConfig().checkFileWrite((infoLocalPath + 'displayLayerInfo.txt'), '')
        # 输出数据
        for layer in allDisplayLayaers:
            if 'defaultLayer' not in layer:
                temp = ['=====================================']
                sk_infoConfig.sk_infoConfig().checkFileWrite((infoLocalPath + 'displayLayerInfo.txt'), temp, 1)
                layerinfo = []
                layerinfo.append(layer)
                sk_infoConfig.sk_infoConfig().checkFileWrite((infoLocalPath + 'displayLayerInfo.txt'), layerinfo, 1)
                objects = mc.editDisplayLayerMembers(layer, q=1)
                if objects:
                    sk_infoConfig.sk_infoConfig().checkFileWrite((infoLocalPath + 'displayLayerInfo.txt'), objects, 1)
                temp = ['*************************************']
                sk_infoConfig.sk_infoConfig().checkFileWrite((infoLocalPath + 'displayLayerInfo.txt'), temp, 1)

    '''
            批量mb转ma工具，或批量ma转mb工具
    '''   
    # 批量转ma或者mb
    def sk_scenemayaMb2Ma(self, basePath, maType=1):
        if basePath[-1] == '/':
            fileList = mc.getFileList(folder=basePath, filespec='*.mb')
            if fileList:
                for path in fileList:
                    filePath = basePath + path
                    mc.file(filePath, open=1 , f=1)
                    if maType == 1:
                        mbFilePath = filePath.replace('.mb', '.ma')
                        mc.file(rename=mbFilePath)
                        mc.file(save=1, type='mayaAscii')
                    else:
                        mbFilePath = filePath.replace('.ma', '.mb')
                        mc.file(rename=mbFilePath)
                        mc.file(save=1)

        else:
            print 'path error,last code must be /'    
            
    '''
            临时给何浪用的清理工具,将小鸡的tx转成rg.......
    '''   
    def sk_sceneTempCleanCalimeroTx2Rg(self):
        # 清理层
        import sk_checkCommon
        reload(sk_checkCommon)
        sk_checkCommon.sk_checkTools().checkCleanDisplayLayers()
        sk_checkCommon.sk_checkTools().checkCleanRenderLayers()
        # 清理相机，灯光，其他等
        rootGrps = sk_checkCommon.sk_checkTools().checkOutlinerGroup()
        for grp in rootGrps:
            if 'CAM' in grp or 'LIGHT' in grp:
                mc.delete(grp)
        # 处理大环控制器
        grps = mc.ls('c_*', type='transform')
        for grp in grps:
            # 隐藏属性处理
            if mc.objExists((grp + '.tt_visibility')):
                pass
            else:
                # 客户需要的tt显示属性
                mc.addAttr(grp, ln='tt_visibility', at='enum', en='visible:hidden:primary_off')
                mc.setAttr(grp + '.tt_visibility', e=True, k=True)
                mc.setAttr(grp + '.visibility', k=False, cb=False)
                print '===============(%s)[tt_visibility]DONE!===============,%(str(grp))'
            # 对判断节点隐藏
            listNodes = mc.listConnections(grp, d=1)
            for node in listNodes:
                # 寻找判断节点
                if mc.nodeType(node) == 'condition':
                    # 寻找其连接节点
                    TempNodes = mc.listConnections(node, s=1)
                    for temp in TempNodes:
                        # 寻找default节点
                        if 'defaultRenderUtility' in temp:
                            # 获取目标连接属性
                            targetAttr = mc.connectionInfo((node + '.message'), destinationFromSource=1)
                            if targetAttr:
                                # 断开
                                mc.disconnectAttr((node + '.message'), targetAttr)
                                break
                
    '''
            【全局扫描】
    '''  
    # # 后台扫描：全asset master文件夹和项目相关的maya文件，超过3个的记录
    def sk_sceneAllAssetMasterCheck(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        import os
        # 获取项目所有asset ID
        #mc.file(rename = ('E：/test/' + project + '_101_001_an_c001.mb'))
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        charAsset = allAssetInfo[1]
        propAsset = allAssetInfo[2]
        setAsset = allAssetInfo[3]
        # 存储错误ID
        errorAsset = []
        errorAssetPath = []
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
            if assetInfo:
                for asset in assetInfo:
                    # 获取master路径
                    assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + '/master/'
                    if os.path.exists(assetServerPath):
                        # 获取文件名
                        assetFiles = mc.getFileList(folder = assetServerPath)
                        if assetFiles:
                            for j in range(3):
                                if j == 0:
                                    HMLType = '_h'
                                if j == 1:
                                    HMLType = '_m'
                                if j == 2:
                                    HMLType = '_l'
                                if j == 3:
                                    HMLType = '_p'
                                animNum = 0
                                renderNum = 0
                                # 高中低片模判断
                                for fileName in assetFiles:
                                    if (HMLType + '_ms_anim.m') in fileName:
                                        animNum = animNum + 1
                                    if (HMLType + '_ms_render.m') in fileName:
                                        renderNum = renderNum + 1
                                if animNum > 1 or renderNum > 1:
                                    errorAsset.append(asset)
                                    errorAssetPath.append(assetServerPath)
        # 输出
        if errorAsset:
            errorAsset = list(set(errorAsset))
            errorAssetPath = list(set(errorAssetPath))
            for i in range(len(errorAsset)):
                print u'---------------'
                print errorAsset[i]
                print errorAssetPath[i]
        return errorAsset
    
    # 全局扫描面材质|角色道具
    def sk_sceneAllAssetFaceShaderCheck(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        import os
        # 获取项目所有asset ID
        #mc.file(rename = ('E：/test/' + project + '_101_001_an_c001.mb'))
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        charAsset = allAssetInfo[1]
        propAsset = allAssetInfo[2]
        # serverInfoPath
        localInfoPath = localPath + 'faceShaderInfoTemp/'
        mc.sysFile(localInfoPath, makeDir=True)
        serverInfoPath = serverPath + 'data/AssetInfos/faceShaderInfo/'
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
        # 开始检测
        for i in range(2):
            if i == 0:
                assetInfo = charAsset
                assetType = 'characters'
            else:
                assetInfo = propAsset
                assetType = 'props'
            if assetInfo:
                for asset in assetInfo:
                    # 存储错误ID 
                    errorAssetSGInfo = []      
                    errorAssetMeshes = []    
                    assetWriteInfo = []
                    # 获取master路径
                    assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + '/master/'
                    if os.path.exists(assetServerPath):
                        # 获取文件名
                        assetFiles = mc.getFileList(folder = assetServerPath)
                        if assetFiles:
                            for fileName in assetFiles:
                                if '_ms_render.m' in fileName :
                                    mc.file((assetServerPath + fileName) , open = 1 , force = 1)
                                    # 检测SG节点
                                    SGNodes = mc.ls(type='shadingEngine')
                                    if SGNodes:
                                        for node in SGNodes:
                                            meshes = mc.sets(node, q=1)
                                            if meshes:
                                                for mesh in meshes:
                                                    meshFull = mc.ls(mesh,l = 1)[0]
                                                    if '|MODEL|' in meshFull and '.f[' in mesh:
                                                        errorAssetMeshes.append(meshFull)
                                        if errorAssetMeshes:
                                            errorAssetSGInfo = errorAssetSGInfo + [u'=============',node,u'------------'] + errorAssetMeshes + [u'------------']
                                # 每个文件进行处理
                                if  errorAssetMeshes:
                                    assetWriteInfo = assetWriteInfo + [asset , (assetServerPath + fileName)] + errorAssetSGInfo + [u'=============']
                                    sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + fileName.split('.')[0] + '.txt'), assetWriteInfo)
        print u'======本地信息更新完毕======'
        # 上传新历史文件
        localNewFiles = mc.getFileList(folder = localInfoPath)
        if localNewFiles:
            for newFile in localNewFiles:
                updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + newFile ) + '"' + ' ' + '"' + (serverInfoPath + newFile) + '"' + ' true'
                mel.eval(updateAnimCMD)
        print u'======服务器端信息更新完毕======'
        # 输出路径
        print u'/n=====请到下面路径查询[角色|道具]异常信息====='
        print serverInfoPath
                             
    # 全局扫描SmoothSet            
    def sk_sceneAllAssetSmoothSetCheck(self):  
        import sk_infoConfig
        reload(sk_infoConfig)
        import sk_checkCommon
        reload(sk_checkCommon)
        import os
        # 获取项目所有asset ID
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        allAsset = allAssetInfo[0]
        # serverInfoPath
        localInfoPath = localPath + 'smoothSetInfo/'
        mc.sysFile(localInfoPath, makeDir=True)
        serverInfoPath = serverPath + 'data/AssetInfos/smoothSetInfo/'
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverInfoPath + '\",\"\",1)'
        mel.eval(makeDirCMD)
        # 处理信息，全面检测render文件
        errorAssetFile = []
        for asset in allAsset:
            assetType = ''
            if asset[0] == 'c':
                assetType = 'characters'
            if asset[0] == 'p':
                assetType = 'props'
            if asset[0] in ['s', 'S']:
                assetType = 'sets'
            if assetType:
                assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + '/master/'
                if os.path.exists(assetServerPath):
                    # 获取文件名
                    assetFiles = mc.getFileList(folder = assetServerPath)
                    if assetFiles:
                        for fileName in assetFiles:
                            if '_ms_render.m' in fileName:
                                mc.file((assetServerPath + fileName) , open = 1 , force = 1)
                                # 检测smoothSet
                                result = sk_checkCommon.sk_checkTools().checkModelSmoothSet(shotInfo[0])
                                if result:
                                    errorAssetFile.append(asset)
                                    errorAssetFile.append(fileName)
                                    errorAssetFile.append(u'--------------------------------------------')
        # 输出信息
        sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + 'AllAssetSmoothSetCheck.txt'), errorAssetFile)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'AllAssetSmoothSetCheck.txt' ) + '"' + ' ' + '"' + (serverInfoPath + 'AllAssetSmoothSetCheck.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        # 输出路径
        print u'/n=====请到下面路径查询[全asset]异常信息====='
        print serverInfoPath
        
    # 全局扫描renderState
    def sk_sceneModelRenderStateCheck(self):  
        import sk_infoConfig
        reload(sk_infoConfig)
        import sk_checkCommon
        reload(sk_checkCommon)
        import os
        # 获取项目所有asset ID
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        allAsset = allAssetInfo[0]
        # serverInfoPath
        localInfoPath = localPath + 'renderStateInfo/'
        mc.sysFile(localInfoPath, makeDir=True)
        serverInfoPath = serverPath + 'data/AssetInfos/renderStateInfo/'
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
        # 处理信息，全面检测render文件
        for asset in allAsset:
            # 清零
            errorAssetFile = []
            # 处理类型
            assetType = ''
            if asset[0] == 'c':
                assetType = 'characters'
            if asset[0] == 'p':
                assetType = 'props'
            if asset[0] in ['s', 'S']:
                assetType = 'sets'
            if assetType:
                for j in range(2):
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
                                if fileKeyInfo in fileName:
                                    mc.file((assetServerPath + fileName) , open = 1 , force = 1)
                                    # 检测smoothSet
                                    result = sk_checkCommon.sk_checkTools().checkMeshRenderStates()
                                    if result:
                                        errorAssetFile.append(asset)
                                        errorAssetFile.append(fileName)
                                        errorAssetFile.append(result)
                                        errorAssetFile.append(u'--------------------------------------------')
            # 输出信息
            if errorAssetFile:
                mc.sysFile((localInfoPath + asset), makeDir=True)
                sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + asset + '_renderState.txt'), errorAssetFile)
                updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + asset + '_renderState.txt' ) + '"' + ' ' + '"' + (serverInfoPath + asset + '_renderState.txt') + '"' + ' true'
                mel.eval(updateAnimCMD)
        # 输出路径
        print u'/n=====请到下面路径查询[全asset]异常信息====='
        print serverInfoPath
        
    # 全局扫描anim和render版本差异
    def sk_sceneAnimRenderDifChcek(self):  
        import sk_infoConfig
        reload(sk_infoConfig)
        import sk_checkCommon
        reload(sk_checkCommon)
        import os
        # 获取项目所有asset ID
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        allAssetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        allAsset = allAssetInfo[0]
        modelHML = ['_l_','_m_','_h_','_p_']
        # serverInfoPath
        localInfoPath = localPath + 'animRenderDifInfo/'
        mc.sysFile(localInfoPath, makeDir=True)
        serverInfoPath = serverPath + 'data/AssetInfos/animRenderDifInfo/'
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
        # 处理信息，全面检测render文件
        for asset in allAsset:
            # 清零
            errorAssetFile = []
            # 处理类型
            assetType = ''
            if asset[0] == 'c':
                assetType = 'characters'
            if asset[0] == 'p':
                assetType = 'props'
            if assetType:
                assetServerPath = ''
            # 全局路径
            needFolder = '/master/'
            fileKeyAnimInfo = '_ms_anim.m'
            fileKeyRenderInfo = '_ms_render.m'
            assetServerPath = serverPath + 'scenes/' + assetType + '/' + asset + needFolder
            # 处理不同类型的高中低模
            for assetType in modelHML:
                if os.path.exists(assetServerPath):
                    # 获取文件名
                    assetFiles = mc.getFileList(folder = assetServerPath)
                    if assetFiles:
                        animFile = ''
                        renderFile = ''
                        for fileName in assetFiles:
                            if fileKeyAnimInfo in fileName and assetType in fileName:
                                animFile = fileName
                            if fileKeyRenderInfo in fileName and assetType in fileName:
                                renderFile = fileName
                        if animFile and renderFile:
                            # 检测版本性
                            # 先打开同类型anim文件
                            animSetNum = []
                            cacheSetNum =[]
                            difInfo = ''
                            # 先检测本文件
                            mc.file((assetServerPath + animFile ),open = 1 ,force = 1)
                            sk_checkCommon.sk_checkTools().checkTransAnimSetAdd()
                            sk_checkCommon.sk_checkTools().checkCacheSetAdd()
                            localCacheObjs = []
                            anotherCacheObjs = []
                            if mc.sets('CTRLS', q=1):
                                localAnimObjs = mc.sets('CTRLS', q=1)
                                animSetNum.append(len(mc.sets('CTRLS', q=1)))
                            else:
                                animSetNum.append(0)
                            if mc.sets('MESHES', q=1):
                                localCacheObjs = mc.sets('MESHES', q=1)
                                cacheSetNum.append(len(mc.sets('MESHES', q=1)))
                            else:
                                cacheSetNum.append(0)
                            # 打开同类型render文件
                            # 打开另一半文件并检测
                            mc.file((assetServerPath + renderFile ) , open = 1, f = 1)
                            localAnimObjs = []
                            anotherAnimObjs = []
                            sk_checkCommon.sk_checkTools().checkTransAnimSetAdd()
                            sk_checkCommon.sk_checkTools().checkCacheSetAdd()
                            if mc.sets('CTRLS', q=1):
                                anotherAnimObjs = mc.sets('CTRLS', q=1)
                                animSetNum.append(len(mc.sets('CTRLS', q=1)))
                            else:
                                animSetNum.append(0)
                            if mc.sets('MESHES', q=1):
                                anotherCacheObjs = mc.sets('MESHES', q=1)
                                cacheSetNum.append(len(mc.sets('MESHES', q=1)))
                            else:
                                cacheSetNum.append(0)
                            # 开始对比！！！！！
                            # 数量对比处理
                            if animSetNum[0] != animSetNum[1]:
                                difInfo = difInfo + (u'AnimSetNum_Dif') + '\n'
                            if cacheSetNum[0] != cacheSetNum[1]:
                                difInfo = difInfo + (u'CacheSetNum_Dif') + '\n'
                            if difInfo:
                                result = u'======[Anim|Render]:CacheList Check======'
                                errorAssetFile.append(asset)
                                errorAssetFile.append(result)
                            else:
                                # cache处理异常名字
                                difLocalCacheNameInfo = []
                                difAnotherCacheNameInfo = []
                                for cacheObj in localCacheObjs:
                                    if cacheObj not in anotherCacheObjs:
                                        difLocalCacheNameInfo.append(cacheObj)
                                for cacheObj in anotherCacheObjs:
                                    if cacheObj not in localCacheObjs:
                                        difAnotherCacheNameInfo.append(cacheObj)
                                # anim处理异常名字
                                difLocalAnimNameInfo = []
                                difAnotherAnimNameInfo = []
                                for animObj in localAnimObjs:
                                    if animObj not in anotherAnimObjs:
                                        difLocalAnimNameInfo.append(animObj)
                                for animObj in anotherAnimObjs:
                                    if animObj not in localAnimObjs:
                                        difAnotherAnimNameInfo.append(animObj)
                                if difLocalCacheNameInfo or difLocalAnimNameInfo:
                                    errorAssetFile.append(asset)
                                    print asset
                                    if difLocalCacheNameInfo:
                                        errorAssetFile.append(u'------------------[cache][Anim File][Different List]------------------')
                                        for info in difLocalCacheNameInfo:
                                            errorAssetFile.append(info)
                                        errorAssetFile.append(u'------------------[cache][Render File][Different List]------------------')
                                        for info in difAnotherCacheNameInfo:
                                            errorAssetFile.append(info)
                                    if difLocalAnimNameInfo:
                                        errorAssetFile.append(u'------------------[anim][Anim File][Different List]------------------')
                                        for info in difLocalAnimNameInfo:
                                            errorAssetFile.append(info)
                                        errorAssetFile.append(u'------------------[anim][Render File][Different List]------------------')
                                        for info in difAnotherAnimNameInfo:
                                            errorAssetFile.append(info)
            # 输出信息
            if errorAssetFile:
                sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + asset + '_animRenderDif.txt'), errorAssetFile)
                updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + asset + '_animRenderDif.txt' ) + '"' + ' ' + '"' + (serverInfoPath + asset + '_animRenderDif.txt') + '"' + ' true'
                mel.eval(updateAnimCMD)
        # 输出路径
        print u'/n=====请到下面路径查询[全asset]异常信息====='
        print serverInfoPath
        
        
    # 全局扫描 anim及render版本中AnimSet和CacheSet异常情况
    # checkType 0:项目全局 | 1：所有角色 | 2：所有道具 | 3：所有场景 | 4：当前asset
    # modelType 0 = 所有   | 1:低模          | 2：中模         | 3:高模 
    def sk_sceneAnim2RenderSetInfo(self,checkType = 0 , modelType = 2):
        # 获取项目信息
        import sk_infoConfig
        reload(sk_infoConfig)
        import os
        # 准备工作
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        mayaType = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        modelHML = ['_l_','_m_','_h_']
        # 数据存储处理
        difInfo = []
        nofileInfo = []
        meshInfo = []
        # 开始检测
        if len(shotInfo) >= 4: 
            assetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
            if assetInfo[0]:
                # 当前asset模式
                if checkType == 4:
                    assetName = shotInfo[1]
                    if assetName in assetInfo[0]:
                        if assetName in assetInfo[1]:
                            assetType = 'characters'
                        if assetName in assetInfo[2]:
                            assetType = 'props'
                        if assetName in assetInfo[3]:
                            assetType = 'sets'
                        checkResult = self.checkAssetAnim2RenderCore(assetName,assetType,checkType,modelType)
                        if checkResult[0]:
                            difInfo.append(checkResult[0])
                        if checkResult[1]:
                            nofileInfo.append(checkResult[1])
                    else:
                        mc.error(u'==============================[%s]不在本项目asset中=============================='%assetName)
                # 类别检测
                if checkType in [0,1,2,3]:
                    allCheckAsset = assetInfo[checkType]
                    # zm不检测set
                    if shotInfo[0] == 'zm' and checkType == 0:
                        allCheckAsset = assetInfo[1] + assetInfo[2]
                    if allCheckAsset:
                        for asset in allCheckAsset:
                            if asset in assetInfo[1]:
                                assetType = 'characters'
                            if asset in assetInfo[2]:
                                assetType = 'props'
                            if asset in assetInfo[3]:
                                assetType = 'sets'
                            checkResult = self.checkAssetAnim2RenderCore(asset,assetType,checkType,modelType)
                            if checkResult[0]:
                                difInfo.append(checkResult[0])
                            if checkResult[1]:
                                nofileInfo.append(checkResult[1])
                            if checkResult[2]:
                                meshInfo.append(checkResult[2])
                    else:
                        mc.error(u'==============================本项目对应类别asset为空==============================')
                # 处理信息
                allInfo = [u'===========Different Asset List==========='] + list(set(difInfo)) + ['===========No File Asset List==========='] + list(set(nofileInfo)) + ['===========Mesh Error List==========='] + meshInfo
                for info in allInfo:
                    if info == '':
                        allInfo.remove(info)
                serverProjectPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
                needPathInfo = serverProjectPath[:-1*len(serverProjectPath.split('/')[-1])]
                infoFilePath = needPathInfo + projectName + '_Scratch/Modeling/cache_test/'
                self.checkFileWrite((infoFilePath + 'cache_test.txt'),allInfo)
                # 输出help信息
                helpInfo = [u'后台处理anim及render版本中AnimSet和CacheSet异常情况',u'checkType 0:项目全局 | 1：所有角色 | 2：所有道具 | 3：所有场景 | 4：当前asset',u'modelType 0 = 所有   | 1:低模          | 2：中模         | 3:高模 ']
                #self.checkFileWrite((infoFilePath + 'readme.txt'),helpInfo)
                for info in helpInfo:
                    print info
                    
                # 成功代码
                return 0
        else:
            mc.error(u'==============================请检查文件名==============================')

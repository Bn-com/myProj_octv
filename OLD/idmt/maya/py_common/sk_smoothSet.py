# -*- coding: utf-8 -*-

'''
Created on 2013-6-14

@author: shenkang
'''

import maya.cmds as mc
import maya.mel as mel


class sk_smoothSetTools(object):
    
    def __init__(self):
        pass
    
    
    def UI_setSmooth(self):
        if mc.window('setSmooth_UI', q=True, exists=True):
            mc.deleteUI('setSmooth_UI')
            
        smoothSetUI = mc.window('setSmooth_UI', t=(unicode('smoothSet工具','utf8')), wh=[300, 100], mb=True)

        UI_win_formL = mc.formLayout()
        UI_slider_frameL = mc.frameLayout(lv=False, bv=True, bs='etchedOut', p=UI_win_formL)
        UI_slider_formL = mc.formLayout()
        UI_smoothLvl_intSG = mc.intSliderGrp('intSliderGrp_intsmoothSetLevel',l='Smooth Level: ', field=1, min=0, max=3)
        mc.setParent('..')
        UI_buttons_formL = mc.formLayout(nd=3, p=UI_win_formL)
        UI_add_b = mc.button(l=(unicode('添加所选','utf8')), c = 'sk_smoothSet.sk_smoothSetTools().smoothSetAdd()' )
        UI_rm_b = mc.button(l=(unicode('移除所选','utf8')), c = 'sk_smoothSet.sk_smoothSetTools().smoothSetRemove(0)')
        UI_rmAll_b = mc.button(l=(unicode('移除该级下所有','utf8')), c = 'sk_smoothSet.sk_smoothSetTools().smoothSetRemove()')
        mc.setParent('..')
        
        # --- UI: arrange layout
        
        mc.formLayout(UI_win_formL, e=True, \
        af = ((UI_slider_frameL, 'top', 5), \
            (UI_slider_frameL, 'left', 5), \
            (UI_slider_frameL, 'right', 5), \
            (UI_buttons_formL, 'left', 5), \
            (UI_buttons_formL, 'right', 5), \
            (UI_buttons_formL, 'bottom', 5)))
        
        mc.formLayout(UI_slider_formL, e=True, \
        af = ((UI_smoothLvl_intSG, 'top', 10), \
            (UI_smoothLvl_intSG, 'left', 0), \
            (UI_smoothLvl_intSG, 'right', 0), \
            (UI_smoothLvl_intSG, 'bottom', 10)))
        
        mc.formLayout(UI_buttons_formL, e=True, \
        af = ((UI_add_b, 'top', 0), \
            (UI_add_b, 'left', 0), \
            (UI_rm_b, 'top', 0), \
            (UI_rmAll_b, 'top', 0), \
            (UI_rmAll_b, 'right', 0)), \
        ac = ((UI_rm_b, 'left', 1, UI_add_b), \
            (UI_rm_b, 'right', 1, UI_rmAll_b)), \
        ap = ((UI_add_b, 'right', 0, 1), \
            (UI_rmAll_b, 'left', 0, 2)))
        
        mc.showWindow(smoothSetUI)
    
    # 剔除不需要的并只添加参与渲染的mesh
    def objectMeshConfig(self,objs):
        outObjs = []
        for obj in objs:
            # 判断命名
            if obj[-1] == '_' or obj[-2]=='_':
                # 判断是否参与渲染
                if '_si_' not in obj and  '_nr_' not in obj and '_proxy_' not in obj:
                    # 判断mesh
                    shape = mc.listRelatives(obj, ni = 1 , s=1, f=1)
                    if shape:
                        # print mc.nodeType(shape)
                        if mc.nodeType(shape[0]) == 'mesh':
                            outObjs.append(obj)
        return outObjs

    # 创建标准smoothSet
    def smoothSetBuild(self , projType = 1):
        # smoothLeval
        if projType == 1:
            smoothLeval_0 = 'smooth_0'
            smoothLeval_1 = 'smooth_1'
            smoothLeval_2 = 'smooth_2'
        else:
            smoothLeval_0 = 'smooth_0_lv'
            smoothLeval_1 = 'smooth_1_lv'
            smoothLeval_2 = 'smooth_2_lv'
        
        # 创建默认Set
        if mc.objExists('SMOOTH_SET'):
            pass
        else:
            mc.createNode('objectSet', n='SMOOTH_SET')
        # smooth_0
        smoothObjs_lv0 = []
        if mc.objExists(smoothLeval_0):
            smoothObjs_lv0 = mc.sets(smoothLeval_0 , q = 1)
            mc.delete(smoothLeval_0)
        mc.createNode('objectSet', n= smoothLeval_0 )
        mc.sets(smoothLeval_0, e=1, addElement='SMOOTH_SET')   
        if smoothObjs_lv0:
            mc.sets(smoothObjs_lv0 , e=1 , addElement= smoothLeval_0) 
        # smooth_1
        smoothObjs_lv1 = []       
        if mc.objExists(smoothLeval_1):
            smoothObjs_lv1 = mc.sets(smoothLeval_1 , q = 1)
            mc.delete(smoothLeval_1)
        mc.createNode('objectSet', n= smoothLeval_1 )
        mc.sets(smoothLeval_1, e=1, addElement='SMOOTH_SET')    
        if smoothObjs_lv1:
            mc.sets(smoothObjs_lv1 , e=1 , addElement= smoothLeval_1) 
        # smooth_2
        smoothObjs_lv2 = []       
        if mc.objExists(smoothLeval_2):
            smoothObjs_lv2 = mc.sets(smoothLeval_2 , q = 1)
            mc.delete(smoothLeval_2)
        mc.createNode('objectSet', n= smoothLeval_2 )
        mc.sets(smoothLeval_2, e=1, addElement='SMOOTH_SET')
        if smoothObjs_lv2:
            mc.sets(smoothObjs_lv2 , e=1 , addElement= smoothLeval_2) 
        mc.select(cl = 1)

    # 开始创建smoothSet
    def smoothSetAdd(self,projType = 1, smoothLevel = -1):
        objs = self.objectMeshConfig(mc.ls(sl=1,l=1))
        # smoothLeval
        self.smoothSetBuild()
        # 更新列表
        if objs:
            needObjs = []
            for obj in objs:
                #print obj
                objName = mc.ls(obj,l = 1)[0]
                if '|MODEL|' in objName and '_si_' not in obj and  '_nr_' not in obj and '_proxy_' not in obj:
                    needObjs.append(obj)
            objs = needObjs
            if needObjs:
                # 获取smooth级别
                if smoothLevel == -1:
                    smoothLevel = mc.intSliderGrp('intSliderGrp_intsmoothSetLevel',q=1,value =1)
                # 从其他Set删除
                idList = [0,1,2]
                idList.remove(int(smoothLevel))
                for intId in idList:
                    self.smoothSetRemoveDetails(objs,intId,0)
                # 添加到所选项
                mc.sets(objs , e=1 , addElement=('smooth_' + str(smoothLevel)) )
                # 设置属性
                for obj in objs:
                    shape = mc.listRelatives(obj, s=1, f=0)
                    mc.setAttr((shape[0] + '.smoothLevel'),smoothLevel)
                    mc.setAttr((shape[0] + '.renderSmoothLevel'),smoothLevel)
        # 说明
        print '\n'
        print u'-------------SmoothSet说明-------------'
        print u'[有效物体]：|MODEL|组下；无_si_；无_nr_；无_proxy_；最后一个为_'
        print u'-------------------------------------'
#P5项目组专用
        

    # 移除
    def smoothSetRemove(self,doType =1):
        objs = self.objectMeshConfig(mc.ls(sl=1,l=1))
        # 获取smooth级别
        smoothLevel = mc.intSliderGrp('intSliderGrp_intsmoothSetLevel',q=1,value =1)
        self.smoothSetRemoveDetails(objs,smoothLevel,doType)

    # 从指定smoothSet移除指定物体 doType是执行与否
    def smoothSetRemoveDetails(self,objs,smoothLevel,doType = 1):
        if doType == 0:
            if mc.objExists('smooth_' + str(smoothLevel)):
                objsInSet = mc.sets(('smooth_' + str(smoothLevel)), q=1)
                if objsInSet:
                    for obj in objs:
                        objSimple = obj.split('|')[-1]
                        if objSimple in objsInSet:
                            # 移除
                            mc.sets(obj, rm = ('smooth_' + str(smoothLevel)))
                            # 还原属性
                            shape = mc.listRelatives(obj, s=1, f=0)
                            mc.setAttr((shape[0] + '.smoothLevel'),0)
                            mc.setAttr((shape[0] + '.renderSmoothLevel'),2)
            else:
                #print(unicode('========================未发现Set：【smooth_%s】========================' % (str(smoothLevel)), 'utf8'))
                print(u'========================未发现Set：【smooth_%s】========================' % smoothLevel)
        if doType ==1:
            if mc.objExists('smooth_' + str(smoothLevel)):
                objsSet = mc.sets(('smooth_' + str(smoothLevel)), q=1)
                if objsSet:
                    # 移除
                    mc.sets(objsSet, rm = ('smooth_' + str(smoothLevel)))
                    # 还原属性
                    objSimple = obj.split('|')[-1]
                    for objSimple in objs:                           
                        shape = mc.listRelatives(obj, s=1, f=0)
                        mc.setAttr((shape[0] + '.smoothLevel'),0)
                        mc.setAttr((shape[0] + '.renderSmoothLevel'),2)

    # 合并SmoothSet
    # 删除盗版
    def smoothSetCombine(self, setType, proType = ''):
        keyRoot = ''
        # proType_A= ['Calimero']
        # 设置正版smoothSet名字
        if setType == 'Smooth':
            if proType.lower() not in ['cl']: 
                keyRoot = 'SMOOTH_SET'
                #keyWords = ['smooth_0','smooth_1','smooth_2']
        # 三个级别一次判断
        tempSet = mc.ls(type='objectSet')
        checkReal = 0
        checkRealObj = []
        objsSets = []
        for temp in tempSet:
            # 判断正版在不在
            if temp == keyRoot:
                checkRealObjs = mc.sets(keyRoot, q=1)
                if checkRealObjs:
                    if 'smooth_0' in checkRealObjs and 'smooth_1' in checkRealObjs and 'smooth_2' in checkRealObjs:
                        checkReal = 1
            # 获取盗版Set
            if keyRoot in temp and temp != keyRoot:
                objsSets.append(temp)
        if checkReal:
            if objsSets:
                checkSetNum = 0
                # 开始循环
                for objSet in objsSets:
                    # 获取当前objSet的子物体
                    childSets = mc.sets(objSet, q=1)
                    if childSets and len(childSets) == 3:
                        # 去除smooth_后进行大小对比
                        cSetNum = [str(childSets[0].split('smooth_')[-1]),str(childSets[1].split('smooth_')[-1]),str(childSets[2].split('smooth_')[-1])]
                        # 处理smooth0
                        childSmooth0 = 'smooth_' + str(min(cSetNum))
                        meshes = mc.sets(childSmooth0,q=1)
                        if meshes:
                            mc.sets(meshes , e=1 , addElement = 'smooth_0')
                        # 处理smooth2
                        childSmooth2 = 'smooth_' + str(max(cSetNum))
                        meshes = mc.sets(childSmooth2,q=1)
                        if meshes:
                            mc.sets(meshes , e=1 , addElement = 'smooth_2')
                        # 处理smooth1
                        cSetNum.remove(min(cSetNum))
                        cSetNum.remove(max(cSetNum))
                        childSmooth2 = 'smooth_' + str(cSetNum[0])
                        meshes = mc.sets(childSmooth2,q=1)
                        if meshes:
                            mc.sets(meshes , e=1 , addElement = 'smooth_1')

                    else:
                        checkSetNum = 1
                        print u'=========[%s]子set组数量不对========='%(objSet)
                      
                    # 删除多余的objSet  
                    try:
                        # 对于参考，pass
                        mc.delete(childSets)
                    except:
                        pass
                    
                    # 删除多余的objSet  
                    try:
                        # 对于参考，pass
                        mc.delete(objSet)
                    except:
                        pass
                
                # 删不掉的是参考，拦截也没意义
                # 0是正常
                return 0
            else:
                return 0
        else:
            print u'=========未发现正版的[%s]Set组========='%(setType)
            return 1
            
    # 渲染前处理
    def smoothConfigForRender(self):
        # 处理smooth_1
        obj_lv1 = self.smoothSetGetObjects(1)
        for obj in obj_lv1:
            # 检测历史，有没有smooth历史
            # mc.listHistory
            print ''
        
    # 获取smoothSet的物体
    def smoothSetGetObjects(self,level,shortType = 1):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        objsSmooth = [] 
        for temp in tempSet:
            if ('smooth_' + str(level)) in temp or ('smooth' + str(level)) in temp:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                meshes = mc.sets(objSet, q=1)
                if meshes:
                    for mesh in meshes:
                        # 不要长名，为shareNodes做准备
                        if shortType == 1:
                            objsSmooth.append(mc.ls((mesh), l=0)[0])
                        else:
                            objsSmooth.append(mc.ls((mesh), l=1)[0])
        return objsSmooth
    
    # smoothSet移除非MODEL组的
    def smoothSetModelGrpCheck(self):
        fileName = (mc.file(query=1, exn=1)).split('/')[-1]
        if fileName in ['zm']:
            # 依次处理
            for i in range(3):
                objs = self.smoothSetGetObjects(i)
                for obj in objs:
                    if '|MODEL|' not in mc.ls(obj ,l =1)[0]:
                        # 移除
                        self.smoothSetRemoveDetails(obj,i)
    
    # 处理所有smoothSet的smooth级别
    # useSmoothSet: 1    从文件内set读取    |    0    从参考获取网络信息
    def smoothSetDoSmooth(self , useSmoothSet = 1 ):
        fileName = (mc.file(query=1, exn=1)).split('/')[-1]
        if '_' in fileName:
            projName = fileName.split('_')[0]
            import sk_referenceConfig
            reload(sk_referenceConfig)
            # 处理网络模式的文件namespace信息
            refNodes = []
            serverInfoPath = ''
            warnningInfo = []
            if useSmoothSet == 0:
                import sk_referenceConfig
                reload(sk_referenceConfig)
                import sk_infoConfig
                reload(sk_infoConfig)
                import os
                serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
                serverInfoPath = serverPath + 'data/AssetInfos/smoothSetInfo/' + projName + '/'
                refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
                refNamespaceLevel =  refInfos[0]
                if refNamespaceLevel:
                    for i in range(len(refNamespaceLevel)):
                        refNodes = refNodes + refNamespaceLevel[i]
            if refNodes:
                for refNode in refNodes:
                    if refNode == 'CAMRN':
                        refNodes.remove(refNode)
            # 处理smooth 0
            objs =[]
            if useSmoothSet:
                if projName == 'cl':
                    objs = self.smoothSetGetObjects(0,0)
                else:
                    objs = self.smoothSetGetObjects(0)
            else:
                for refNode in refNodes:
                    fileSmoothPath = serverInfoPath
                    namespace = sk_referenceConfig.sk_referenceConfig().checkReferenceGetNamespaceInfoByPath(mc.referenceQuery(refNode, f=1))
                    ns = namespace
                    if ns[-1] in ['0','1','2','3','4','5','6','7','8','9'] and(ns[-2] == '_' or ns[-3] == '_'):
                        asset = ns[:-1*(len(ns.split('_')[-1])+1)]
                    else:
                        asset = ns
                    if ':' in asset:
                        asset = asset.split(':')[-1]
                
                    if '_' in asset:
                        asset = asset.split('_')[-1]
                    filePath = mc.referenceQuery(refNode,filename = 1)
                    HMLType = filePath.split('/')[-1].split('_')[2]
                    fileSmoothPath = fileSmoothPath + asset + '/' + HMLType + '/smooth_0.txt'
                    if os.path.exists(fileSmoothPath):
                        #print fileSmoothPath
                        smoothObjs = sk_infoConfig.sk_infoConfig().checkFileRead( fileSmoothPath )
                        if smoothObjs:
                            for obj in smoothObjs:
                                objs.append( ns + ':' + obj )
                    else:
                        warnningInfo.append(namespace)
            if objs:
                for obj in objs:
                    if mc.listRelatives(obj,ni = 1, s=1):
                        #print u'------0------'
                        #print obj
                        # 先关闭显示
                        shape = mc.listRelatives(obj,ni = 1,s=1,f = 1)[0]
                        try:
                            mc.setAttr((shape+'.useSmoothPreviewForRender'),0)
                        except:
                            pass
                        # 担心被锁
                        try:
                            mc.setAttr((shape+'.displaySmoothMesh'),2)
                        except:
                            pass
                        try:
                            mc.setAttr((shape+'.smoothLevel'),0)
                        except:
                            pass
                        #print shape
                        try:
                            mc.setAttr((shape+'.renderSmoothLevel'),0)
                        except:
                            print u'---'
                            print shape
                            print u'===请检查这个物体是否非法的nurbs，nurbs不能加进smoothSet==='
                            mc.error(u'===请检查这个物体是否非法的nurbs，nurbs不能加进smoothSet===')
            # 处理smooth 1
            objs =[]
            if useSmoothSet:
                if projName == 'cl':
                    objs = self.smoothSetGetObjects(1,0)
                else:
                    objs = self.smoothSetGetObjects(1)
            else:
                for refNode in refNodes:
                    fileSmoothPath = serverInfoPath
                    namespace = sk_referenceConfig.sk_referenceConfig().checkReferenceGetNamespaceInfoByPath(mc.referenceQuery(refNode, f=1))
                    ns = namespace
                    if ns[-1] in ['0','1','2','3','4','5','6','7','8','9'] and(ns[-2] == '_' or ns[-3] == '_'):
                        asset = ns[:-1*(len(ns.split('_')[-1])+1)]
                    else:
                        asset = ns
                    if ':' in asset:
                        asset = asset.split(':')[-1]
                
                    if '_' in asset:
                        asset = asset.split('_')[-1]
                    filePath = mc.referenceQuery(refNode,filename = 1)
                    HMLType = filePath.split('/')[-1].split('_')[2]
                    fileSmoothPath = fileSmoothPath + asset + '/' + HMLType + '/smooth_1.txt'
                    if os.path.exists(fileSmoothPath):
                        #print fileSmoothPath
                        smoothObjs = sk_infoConfig.sk_infoConfig().checkFileRead( fileSmoothPath )
                        if smoothObjs:
                            for obj in smoothObjs:
                                objs.append( ns + ':' + obj )
                    else:
                        warnningInfo.append(namespace)
            if objs:
                for obj in objs:
                    if mc.listRelatives(obj,ni = 1,s=1):
                        #print u'------1------'
                        #print obj
                        # 先关闭显示
                        shape = mc.listRelatives(obj,ni = 1,s=1,f = 1)[0]
                        try:
                            mc.setAttr((shape+'.useSmoothPreviewForRender'),0)
                        except:
                            pass
                        # 担心被锁
                        try:
                            mc.setAttr((shape+'.displaySmoothMesh'),2)
                        except:
                            pass
                        try:
                            mc.setAttr((shape+'.smoothLevel'),0)
                        except:
                            pass
                        try:
                            mc.setAttr((shape+'.renderSmoothLevel'),1)
                        except:
                            print u'---'
                            print shape
                            print u'===请检查这个物体是否非法的nurbs，nurbs不能加进smoothSet==='
                            mc.error(u'===请检查这个物体是否非法的nurbs，nurbs不能加进smoothSet===')
            # 处理smooth 2
            objs =[]
            if useSmoothSet:
                if projName == 'cl':
                    objs = self.smoothSetGetObjects(2,0)
                else:
                    objs = self.smoothSetGetObjects(2)
            else:
                for refNode in refNodes:
                    fileSmoothPath = serverInfoPath
                    namespace = sk_referenceConfig.sk_referenceConfig().checkReferenceGetNamespaceInfoByPath(mc.referenceQuery(refNode, f=1))
                    ns = namespace
                    if ns[-1] in ['0','1','2','3','4','5','6','7','8','9'] and(ns[-2] == '_' or ns[-3] == '_'):
                        asset = ns[:-1*(len(ns.split('_')[-1])+1)]
                    else:
                        asset = ns
                    if ':' in asset:
                        asset = asset.split(':')[-1]
                
                    if '_' in asset:
                        asset = asset.split('_')[-1]
                    filePath = mc.referenceQuery(refNode,filename = 1)
                    HMLType = filePath.split('/')[-1].split('_')[2]
                    fileSmoothPath = fileSmoothPath + asset + '/' + HMLType + '/smooth_2.txt'
                    if os.path.exists(fileSmoothPath):
                        #print fileSmoothPath
                        smoothObjs = sk_infoConfig.sk_infoConfig().checkFileRead( fileSmoothPath )
                        if smoothObjs:
                            for obj in smoothObjs:
                                objs.append( ns + ':' + obj )
                    else:
                        warnningInfo.append(namespace)
            if objs:
                for obj in objs:
                    if mc.listRelatives(obj,ni = 1,s=1):
                        #print u'------2------'
                        #print obj
                        # 先关闭显示
                        shape = mc.listRelatives(obj,ni = 1,s=1,f = 1)[0]
                        try:
                            mc.setAttr(( shape + '.useSmoothPreviewForRender'),0)
                        except:
                            pass
                        # 担心被锁
                        try:
                            mc.setAttr(( shape + '.displaySmoothMesh'),2)
                        except:
                            pass
                        try:
                            mc.setAttr(( shape +'.smoothLevel'),0)
                        except:
                            pass
                        try:
                            mc.setAttr((shape+'.renderSmoothLevel'),2)
                        except:
                            print u'---'
                            print shape
                            print u'===请检查这个物体是否非法的nurbs，nurbs不能加进smoothSet==='
                            mc.error(u'===请检查这个物体是否非法的nurbs，nurbs不能加进smoothSet===')
            # 根目录smooth显示
            topNodes = mc.ls(assemblies=True)
            mc.displaySmoothness(topNodes, polygonObject=3)
            # 输出错误信息
            if warnningInfo:
                mc.warning(u'---------------[注意]以下asset没有有效smooth数据---------------')
                for info in warnningInfo:
                    print info.split(':')[-1]
                mc.warning(u'---------------[注意]以上asset没有有效smooth数据---------------')
        else:
            mc.error(u'===========请处理好File-Name===========')
    
    # 收集镜头内smoothSet
    def smoothSetObjsShotInfo(self):
        smothSets = mc.ls('*:SMOOTH_SET' , type = 'objectSet') + mc.ls('*:*:SMOOTH_SET' , type = 'objectSet')
        smoothObjs = []
        #for i in range(3):
        #    objs = []
        #    for objSet in smothSets:
        #        setChildren = 
        print ''
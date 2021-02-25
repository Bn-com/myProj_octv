# -*- coding: utf-8 -*-

'''
Created on 2013-6-14

@author: shenkang
'''

import maya.cmds as mc
import maya.mel as mel


class sk_smoothSet(object):
    
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
        UI_buttons_formL = mc.formLayout(nd=4, p=UI_win_formL)
        UI_add_b = mc.button(l=(unicode('添加所选','utf8')),bgc=[0.2,0.2,0.2], c = 'reload(sk_smoothSet);sk_smoothSet.sk_smoothSet().smoothSetAdd()' )
        UI_rm_b = mc.button(l=(unicode('移除所选','utf8')),bgc=[0.2,0.2,0.2],c = 'reload(sk_smoothSet);sk_smoothSet.sk_smoothSet().smoothSetRemove(0)')
        UI_rmAll_b = mc.button(l=(unicode('移除该级物','utf8')),bgc=[0.2,0.2,0.2],c = 'reload(sk_smoothSet);sk_smoothSet.sk_smoothSet().smoothSetRemove()')
        UI_mg_b = mc.button(l=(unicode('[合并]','utf8')),bgc=[0.1,0.6,0.1],c = 'reload(sk_smoothSet);sk_smoothSet.sk_smoothSet().smoothSetCombine("Smooth",remove = 0)')
        UI_ck_b = mc.button(l=(unicode('[检测]','utf8')),bgc=[0.3,0.8,0.3],c = 'from idmt.maya.commonCore.core_mayaCommon import sk_checkTools;reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelSmoothSet("",1)')
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
            (UI_mg_b, 'top', 0), \
            (UI_ck_b, 'top', 0), \
            (UI_ck_b, 'right', 0)), \
        ac = ((UI_rm_b, 'left', 1, UI_add_b), \
            (UI_mg_b, 'right', 1, UI_ck_b)), \
        ap = ((UI_add_b, 'right', 0, 1), \
            (UI_rmAll_b, 'left', 0, 2)))

        mc.showWindow(smoothSetUI)
    
    # 剔除不需要的并只添加参与渲染的mesh
    def objectMeshConfig(self,objs,donotKeys = ['_si_','_nr_','_proxy_'],MODELCheck = 1):
        outObjs = []
        for obj in objs:
            state = 0
            # 判断是否参与渲染
            for key in donotKeys:
                if key in obj:
                    state = 1
                if state:
                    continue
            if state:
                continue
            # 判断mesh
            shape = mc.listRelatives(obj, ni = 1 , s=1, f=1 ,type = 'mesh')
            if not shape:
                continue
            #print obj
            # MODEL判断
            if '|MODEL|' not in obj:
                continue
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
    def smoothSetAdd(self, projType = 1,smoothLevel = -1 ,donotKeys = ['_si_','_nr_','_proxy_'],MODELCheck = 1,previewFix = 1):
        objs = self.objectMeshConfig((mc.ls(sl=1,l=1)),donotKeys = donotKeys,MODELCheck = MODELCheck)
        # smoothLeval
        self.smoothSetBuild()
        # 更新列表
        objs = mc.ls(objs , l = 1)
        if objs:
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
                shape = mc.listRelatives(obj, s=1, f=1)
                if previewFix:
                    mc.setAttr((shape[0] + '.smoothLevel'),smoothLevel)
                mc.setAttr((shape[0] + '.renderSmoothLevel'),smoothLevel)
        # 说明
        print '\n'
        print u'-------------SmoothSet说明-------------'
        print u'[有效物体]：|MODEL|组下；无_si_；无_nr_；无_proxy_；物体为polygon'
        print u'-------------------------------------'

    # 移除
    def smoothSetRemove(self,doType =1,donotKeys = ['_si_','_nr_','_proxy_'],MODELCheck = 1):
        objs = self.objectMeshConfig((mc.ls(sl=1,l=1)),donotKeys = donotKeys,MODELCheck = MODELCheck)
        # 获取smooth级别
        smoothLevel = mc.intSliderGrp(('intSliderGrp_intsmoothSetLevel'),q=1,value =1)
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
                            shape = mc.listRelatives(obj, s=1, f=1)
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
                    #objSimple = obj.split('|')[-1]
                    for obj in objs:                           
                        shape = mc.listRelatives(obj, s=1, f=1)
                        mc.setAttr((shape[0] + '.smoothLevel'),0)
                        mc.setAttr((shape[0] + '.renderSmoothLevel'),2)

    # 合并SmoothSet
    # 删除盗版
    def smoothSetCombine(self, setType, proType = '',remove = 1):
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
                # 开始循环
                for objSet in objsSets:
                    # 获取当前objSet的子物体
                    childSets = mc.sets(objSet, q=1)
                    if childSets and len(childSets) == 3:
                        # 去除smooth_后进行大小对比
                        cSetNum = [str(childSets[0].split('smooth_')[-1]),str(childSets[1].split('smooth_')[-1]),str(childSets[2].split('smooth_')[-1])]
                        minNum = min(cSetNum)
                        maxNum = max(cSetNum)
                        for checkNum in cSetNum:
                            if checkNum in [minNum,maxNum]:
                                continue
                            midNum = checkNum
                        # 处理smooth0
                        childSmooth0 = childSets[cSetNum.index(minNum)]
                        meshes = mc.sets(childSmooth0,q=1)
                        if meshes:
                            mc.sets(meshes , e=1 , addElement = 'smooth_0')
                        # 处理smooth2
                        childSmooth2 = childSets[cSetNum.index(maxNum)]
                        meshes = mc.sets(childSmooth2,q=1)
                        if meshes:
                            mc.sets(meshes , e=1 , addElement = 'smooth_2')
                        # 处理smooth1
                        cSetNum.remove(min(cSetNum))
                        cSetNum.remove(max(cSetNum))
                        childSmooth1 = childSets[cSetNum.index(midNum)]
                        meshes = mc.sets(childSmooth1,q=1)
                        if meshes:
                            mc.sets(meshes , e=1 , addElement = 'smooth_1')
                    else:
                        print u'=========[%s]子set组数量不对========='%(objSet)
                    if remove:
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
        obj_lv1 = self.smoothSetGetObjects(1,1)
        for obj in obj_lv1:
            # 检测历史，有没有smooth历史
            # mc.listHistory
            print ''
        
    # 获取smoothSet的物体
    def smoothSetGetObjects(self,level,longType = 1,selObjs = []):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        objsSmooth = [] 
        for temp in tempSet:
            if ('smooth_' + str(level)) in temp or ('smooth' + str(level)) in temp:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                meshes = mc.sets(objSet, q=1)
                if not meshes:
                    continue
                needState = 0
                if selObjs:
                    for checkObj in meshes:
                        longName = mc.ls(checkObj,l=1)[0]
                        if longName in selObjs:
                            objsSmooth = objsSmooth + [longName]
                else:
                    needState = 1
                if needState:
                    objsSmooth = objsSmooth + (mc.ls((meshes), l=longType))
        return objsSmooth
    
    # smoothSet移除非MODEL组的
    def smoothSetModelGrpCheck(self):
        fileName = (mc.file(query=1, exn=1)).split('/')[-1]
        if fileName in ['zm']:
            # 依次处理
            for i in range(3):
                objs = self.smoothSetGetObjects(i,1)
                for obj in objs:
                    if '|MODEL|' not in mc.ls(obj ,l =1)[0]:
                        # 移除
                        self.smoothSetRemoveDetails(obj,i)
    
    # 处理所有smoothSet的smooth级别
    # useSmoothSet: 1    从文件内set读取    |    0    从参考获取网络信息
    def smoothSetDoSmooth(self , useSmoothSet = 1 ,disModify = 1,selMode = 0):
        import os
        import sk_infoConfig
        reload(sk_infoConfig)
        import sk_referenceConfig
        reload(sk_referenceConfig)
        numStrList = ['0','1','2','3','4','5','6','7','8','9']
        # selMode
        selObjs = []
        if selMode:
            selObjs = mc.ls(sl = 1,l=1)
        fileName = (mc.file(query=1, exn=1)).split('/')[-1]
        if '_' not in fileName:
            mc.error(u'===========请处理好File-Name===========')
        projSimp = fileName.split('_')[0]
        # 处理网络模式的文件namespace信息
        refNodes = []
        serverInfoPath = ''
        warnningInfo = []
        if useSmoothSet == 0:
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            serverInfoPath = serverPath + 'data/AssetInfos/smoothSetInfo/' + projSimp + '/'
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
        errorObjs = []
        for num in range(3):
            objs =[]
            if useSmoothSet:
                if projSimp == 'cl':
                    objs = self.smoothSetGetObjects(num,1,selObjs)
                else:
                    objs = self.smoothSetGetObjects(num,1,selObjs)
            else:
                for refNode in refNodes:
                    fileSmoothPath = serverInfoPath
                    namespace = sk_referenceConfig.sk_referenceConfig().checkReferenceGetNamespaceInfoByPath(mc.referenceQuery(refNode, f=1))
                    ns = namespace
                    if ns[-1] in numStrList and(ns[-2] == '_' or ns[-3] == '_'):
                        asset = ns[:-1*(len(ns.split('_')[-1])+1)]
                    else:
                        asset = ns
                    if ':' in asset:
                        asset = asset.split(':')[-1]

                    if '_' in asset:
                        asset = asset.split('_')[-1]
                    filePath = mc.referenceQuery(refNode,filename = 1)
                    HMLType = filePath.split('/')[-1].split('_')[2]
                    fileSmoothPath = fileSmoothPath + asset + '/' + HMLType + '/smooth_%s.txt'%(str(num))
                    if os.path.exists(fileSmoothPath):
                        #print fileSmoothPath
                        smoothObjs = sk_infoConfig.sk_infoConfig().checkFileRead( fileSmoothPath )
                        if smoothObjs:
                            for obj in smoothObjs:
                                objs.append( ns + ':' + obj )
                    else:
                        warnningInfo.append(namespace)
            if not objs:
                continue
            for obj in objs:
                shape = mc.listRelatives(obj,ni = 1,s=1,f = 1)
                if not shape:
                    continue
                shape = shape[0]
                if mc.nodeType(shape) not in  ['mesh']:
                    continue
                checkAttr = (shape+'.useSmoothPreviewForRender')
                value = mc.getAttr(checkAttr)
                if value not in [0]:
                    try:
                        mc.setAttr(checkAttr,0)
                    except:
                        pass
                # 担心被锁
                checkAttr = (shape+'.displaySmoothMesh')
                value = mc.getAttr(checkAttr)
                if value not in [2]:
                    try:
                        mc.setAttr(checkAttr,2)
                    except:
                        pass
                checkAttr = (shape+'.smoothLevel')
                value = mc.getAttr(checkAttr)
                if disModify:
                    disValue = 1
                else:
                    disValue = 0
                if value not in [disValue]:
                    try:
                        mc.setAttr(checkAttr,disValue)
                    except:
                        pass
                #print shape
                checkAttr = (shape+'.renderSmoothLevel')
                value = mc.getAttr(checkAttr)
                if value not in [num]:
                    try:
                        mc.setAttr(checkAttr,num)
                    except:
                        errorObjs.append(shape)
        if errorObjs:
            print '---------SetSmooth Failed Objs:'
            for errorObj in errorObjs:
                print errorObj
            errorInfo = u'===请检查这些物体是否非法的nurbs，nurbs不能加进smoothSet==='
            print errorInfo
            mc.error(errorInfo)

        # 根目录smooth显示
        #topNodes = mc.ls(assemblies=True)
        #mc.displaySmoothness(topNodes, polygonObject=3)
        # 输出错误信息
        if warnningInfo:
            mc.warning(u'---------------[注意]以下asset没有有效smooth数据---------------')
            for info in warnningInfo:
                print info.split(':')[-1]
            mc.warning(u'---------------[注意]以上asset没有有效smooth数据---------------')

    
    # 收集镜头内smoothSet
    def smoothSetObjsShotInfo(self):
        smothSets = mc.ls('*:SMOOTH_SET' , type = 'objectSet') + mc.ls('*:*:SMOOTH_SET' , type = 'objectSet')
        smoothObjs = []
        print ''


    # shot smooth set apply
    def smoothSetShotSelApply(self,disModify = 1):
        rootGrps = mc.ls(sl=1,l=1)
        if not rootGrps:
            print u'\n----------Please Select Some Groups----------\n'
            mc.error()
            return
        # 获取物体
        shapes = mc.listRelatives(rootGrps,ad=1,type = 'mesh',f=1)
        if not shapes:
            return
        for mesh in shapes:
            grp = mc.listRelatives(mesh,p=1,type = 'transform',f=1)
            if not grp:
                continue
            grp = grp[0]
            checkSets = mc.listConnections(grp,s=0,d=1,type = 'objectSet')
            if not checkSets:
                continue
            smsSet = ''
            for checkSet in checkSets:
                if 'smooth_' not in checkSet:
                    continue
                smsSet = checkSet
            if not smsSet:
                continue
            smsLev = int(smsSet.split('_')[-1])
            if disModify:
                disModify = smsLev
            try:
                mc.setAttr(( mesh + '.useSmoothPreviewForRender'),0)
            except:
                pass
            # 担心被锁
            try:
                mc.setAttr(( mesh + '.displaySmoothMesh'),2)
            except:
                pass
            try:
                mc.setAttr(( mesh +'.smoothLevel'),disModify)
            except:
                pass
            try:
                mc.setAttr((mesh+'.renderSmoothLevel'),smsLev)
            except:
                pass


    # doSmooth2SelObjs
    def doSmoothSelObjs(self,smsLev = 0 ,disModify = 0):
        rootGrps = mc.ls(sl=1,l=1)
        if not rootGrps:
            print u'\n----------Please Select Some Groups----------\n'
            mc.error()
            return
        # 获取物体
        shapes = mc.listRelatives(rootGrps,ad=1,type = 'mesh',f=1)
        if not shapes:
            return
        # 应用
        for checkMesh in shapes:
            try:
                mc.setAttr(( checkMesh + '.useSmoothPreviewForRender'),0)
            except:
                pass
            # 担心被锁
            try:
                mc.setAttr(( checkMesh + '.displaySmoothMesh'),2)
            except:
                pass
            try:
                mc.setAttr(( checkMesh +'.smoothLevel'),disModify)
            except:
                pass
            try:
                mc.setAttr((checkMesh+'.renderSmoothLevel'),smsLev)
            except:
                pass
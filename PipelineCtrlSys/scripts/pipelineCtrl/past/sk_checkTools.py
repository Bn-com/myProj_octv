# -*- coding: utf-8 -*-

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
import os

class sk_checkTools(object):
    def __init__(self):
        self.bothInfo = 10
        self.winSize01= [470,300]
        self.winSize02= [530,220]
        self.winSize03= [38,249,110]
        self.winSize05= [150,215]
        self.winSize06= [360,180]
        self.spaceH01 = 20
        self.spaceH02 = 10
        self.spaceH03 = 7
        self.renderGrp = sk_infoConfig.sk_infoConfig().renderGrp
        self.tempRGrp  = 'TEMPMDL'

    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【UI篇】【CheckTools界面】
    #------------------------------#
    # 前期check工具集
    def sk_sceneUICheckTools(self):
        # 窗口
        if mc.window ("sk_sceneUICheckTools", ex=1):
            mc.deleteUI("sk_sceneUICheckTools", window=True)
        mc.window("sk_sceneUICheckTools", title="Check Tools", widthHeight=(360, 450), menuBar=0)
        # 主界面
        mc.columnLayout()
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig

        # 选取栏
        mc.rowLayout(numberOfColumns=2, columnWidth2=(230, 100))
        mc.textField('sk_sceneUICheckName', w=230 , h=30 , en=1 , text=(u'输入整行然后按【提取选择】按钮'))
        mc.button(w=100 , h=30 , bgc=[0.3, 0.2, 0.6], label=(u'【提取选择】') , c='sk_checkTools.sk_checkTools().sk_sceneDetailsSelectObject()')
        mc.setParent("..")
        # 行按钮
        mc.rowLayout(numberOfColumns=2, columnWidth2=(80, 250))
        # 全自动
        mc.button(w=80 , h=350 , bgc=[0.1, 0.1, 0.1], label=(u'【全自动】\n【Check】'), c='sk_checkTools.sk_checkTools().checkModelDetailsWarning()')
        mc.columnLayout()
        # 分割按钮
        # 第1排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0.2, 0.4, 0.5], label=(u'【Check】【参考】          '), c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"refCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.4, 0.5, 0.3], label=(u'<<自动更新标记Set>>'),c = 'import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().checkCacheSetAdd()\nsk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()\nsk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig(\"Cache\",\"ZM\")\nsk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig(\"Anim\",\"ZM\")')
        mc.setParent("..")
        # 第2排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0.2, 0.4, 0.5], label=(u'【Check】【namespace】'),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"nsCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.4, 0.5, 0.3], label=(u'<<namespace工具>>'),c = 'mel.eval(\"common_namespaceTools\")')
        mc.setParent("..")
        # 第3排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0.2, 0.4, 0.5], label=(u'【Check】【命名】          '),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"MSHCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.4, 0.5, 0.3], label=(u'<<选取添加_后缀>>'),c ='sk_checkTools.sk_checkTools().checkRenameMSHPosfix()')
        mc.setParent("..")
        # 第4排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0.2, 0.4, 0.5], label=(u'【Check】【面数】          '),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"faceCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.4, 0.5, 0.3], label=(u'<<自动处理重命名>>'),c ='sk_checkTools.sk_checkTools().checkSameRename()\nsk_checkTools.sk_checkTools().checkSameRename(\"mesh\")\nsk_checkTools.sk_checkTools().checkSameRename(\"nurbsCurve\")\nsk_checkTools.sk_checkTools().checkMSHKeepOneRename(\"MSH\")')
        mc.setParent("..")
        # 第5排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0.2, 0.4, 0.5], label=(u'【Check】【instance】    '),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"insCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.4, 0.5, 0.3], label=(u'<<displaceLayer清理>>'),c = 'from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().checkCleanDisplayLayers()')
        mc.setParent("..")
        # 第6排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0.2, 0.4, 0.5], label=(u'【Check】【smooth】     '),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"smoothCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.4, 0.5, 0.3], label=(u'<<renderLayer清理>>'), c = 'from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().checkCleanRenderLayers()')
        mc.setParent("..")        
        # 第7排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0.2, 0.4, 0.5], label=(u'【Check】【标记】         '),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"signCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.4, 0.5, 0.3], label=(u'<<自动清理空组>>'),c = 'mel.eval(\"deleteEmptyGroups()\")')
        mc.setParent("..")
        # 第8排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0.2, 0.4, 0.5], label=(u'【Check】【物体重名】  '),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"sameTransformCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.4, 0.5, 0.3], label=(u'<<显示|隐藏骨骼>>'),c = 'sk_checkTools.sk_checkTools().checkJointViewHide()')
        mc.setParent("..")
        # 第9排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0.2, 0.4, 0.5], label=(u'【Check】【shape重名】'),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"sameShapeCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.4, 0.5, 0.3], label=(u'<<赋予ct_an标记>>'),c='sk_checkTools.sk_checkTools().checkCTANSignAdd()')
        mc.setParent("..")     
        
        # 第10排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0.2, 0.4, 0.5], label=(u'【Check】【Mesh同名】'),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"sameShapeNodeCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.4, 0.5, 0.3], label=(u'【Check】【proxy位移】'),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"proxyInfo\")')
        mc.setParent("..")    
        
        # 第11排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0.2, 0.4, 0.5], label=(u'【Check】【smoothSet】'),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"smoothSet\")')
        mc.button(w=125 , h=30 , bgc=[0.4, 0.5, 0.3], label=(u'【Check】【renderState】'),c='sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"renderState\")')
        mc.setParent("..")     
        
        mc.setParent("..")

        mc.setParent("..")
        mc.showWindow("sk_sceneUICheckTools")
        
    #------------------------------#
    # 提取选择物体
    def sk_sceneDetailsSelectObject(self):
        pathInfo = mc.textField('sk_sceneUICheckName', q=1, text=1)
        objPath = pathInfo.split('\t')[-1]
        mc.select(objPath)
        
    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【总篇】【CheckTools】
    #------------------------------#
    # 错误警告显示
    def checkModelDetailsWarning(self,checkType = ''):
        import sk_sceneTools
        reload(sk_sceneTools)
        infoWrong = []
        errorPrint = 0
        mo = 0
 
        # 创建ErrorSet
        self.checkErrorSetCreate()
 
        # 文件名检测，判断环节
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if len(info) > 3:
            
            # 错误检测，根据阶段不同而不同
            fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
            if info[3] == ('mo' + fileFormat):
                mo = 1
            
            # 参考检测
            if checkType == '' or checkType == 'refCheck':
                # 对set类不检测
                if info[1][0] not in ['s', 'S']:
                    # 获取参考数
                    rfnNods = mc.file(q=1, reference=1)
                    # 有参考时
                    if rfnNods:
                        infoWrong.append(u'【 警告 】\t\t有参考存在，请注意核查！！')
                # 无参考时
                else:
                    # 检测是否有非法MODEL组
                    if info[0] == 'zm':
                        for i in range(0, 9):
                            grp = mc.ls('MODEL' + str(i))
                            if mc.ls('MODEL' + str(i)):
                                infoWrong.append(u'【错误存在】\t\t%s' % (str(grp[0])))
                                errorPrint += 1
            print '\n'
            
            # 检测namespace
            if checkType == '' or checkType == 'nsCheck':
                # 对set类不检测
                if info[1][0] not in ['s', 'S']:
                    namespace = mc.namespaceInfo(listOnlyNamespaces = 1)
                    if len(namespace) > 2:
                        infoWrong.append(u'【 错 误 】\t\t存在namespace，请清理掉！')
                        errorPrint += 1
                        
            print '\n'
                        
            # 检测MODEL组重命名
            model = mc.ls('MODEL')
            # ZM的设置居然出现MODEL1这样的组。。。我很无语了。。。就这样吧
            if info[0] != 'zm':
                for num in range(9):
                    model = model + mc.ls('MODEL' + str(num) + '*')
            if model:
                if len(model) > 1:
                    infoWrong.append(u'【 错 误 】\t\tMODEL组不止一个！')
                    errorPrint += 1
                else:
                    print '\n'
                    
                    # 检测大组数目
                    rootGrps = self.checkOutlinerGroup()
                    if rootGrps:
                        # 根目录大组数目。特殊项目特殊情况
                        if info[0] == 'zm':
                            numRootGrp = len(rootGrps)
                            if numRootGrp > 1:
                                infoWrong.append(u'【 错 误 】\t\t大组不止一个！')
                                errorPrint += 1
                    else:
                        infoWrong.append(u'【 错 误 】\t\t文件是空的！！')
                        errorPrint += 1

                print '\n'

                # 需要判断[mo]的MODEL的函数才能执行
                if checkType == '' or checkType == 'MSHCheck':
                    # 检测错误命名
                    errorNames = self.checkMSHName(mo)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【命名错误】\t\t%s' % (str(name)))
                            errorPrint += 1  
                        mc.sets(errorNames , e=1 , addElement='Error_MSHName')  
                    else:
                        mc.delete('Error_MSHName')

                print '\n'

                # 渲染属性检测
                if checkType == '' or checkType == 'renderState':
                    # 对zm的set不检测
                    if not (info[0] == 'zm' and info[1][0] in ['s', 'S']):
                        errorNames = self.checkMeshRenderStates()
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【渲染属性】\t\t%s' % (str(name)))
                                errorPrint += 1
                            mc.sets(errorNames , e=1 , addElement='Error_RenderState')  
                        else:
                            mc.delete('Error_RenderState')     

                print '\n'


                # 多边面错误
                if checkType == '' or checkType == 'faceCheck':
                    # 英雄工厂不检测五边面
                    if info[0] != 'hf' and info[1][0] not in ['s', 'S']:
                        errorNames = self.checkFaceVertexs(mo)
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【非四边形】\t\t%s' % (str(name)))
                                errorPrint += 1
                            mc.sets(errorNames , e=1 , addElement='Error_N4Edges')  
                        else:
                            mc.delete('Error_N4Edges')     
                    else:
                        mc.delete('Error_N4Edges')      
                    
                print '\n'
                
                # instance检测
                # 对场景不检测
                if checkType == '' or checkType == 'insCheck':
                    if info[1][0] not in ['s', 'S']:
                        errorNames = self.checkInstance(mo)
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【instance】\t\t%s' % (str(name)))
                                errorPrint += 1
                            mc.sets(errorNames , e=1 , addElement='Error_Instance')  
                        else:
                            mc.delete('Error_Instance')    
                    else:
                        mc.delete('Error_Instance')  
                        
                print '\n'

                # 检测MaxSmooth属性
                if checkType == '' or checkType == 'smoothCheck':
                    # 英雄工厂需要
                    if info[0] == 'hf':
                        errorNames = self.checkModelSmooth(mo)
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【无Max平滑】\t\t%s' % (str(name)))
                                errorPrint += 1
                            mc.sets(errorNames , e=1 , addElement='Error_MaxSmooth')  
                        else:
                            mc.delete('Error_MaxSmooth')         
                    else:
                        mc.delete('Error_MaxSmooth')                 

                print '\n'

                # 检测标记错误
                if checkType == '' or checkType == 'signCheck':
                    if info[0] == 'zm':
                        errorNames = self.checkSignName()
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【标记错误】\t\t%s' % (str(name)))
                                errorPrint += 1
                            mc.sets(errorNames , e=1 , addElement='Error_SignInfo')  
                        else:
                            mc.delete('Error_SignInfo')  
                    else:
                        mc.delete('Error_SignInfo')  
                
            else:
                print '\n'
                infoWrong.append(u'【 错 误 】\t\tMODEL组不存在！！')
                errorPrint += 1

            print '\n'

            # 对set类不检测
            if info[1][0] not in ['s', 'S']:
                # 检测重名错误
                if checkType == ''  or checkType == 'sameTransformCheck':
                    errorNames = []
                    errorNamesTemp = self.checkSameName()
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            if '|MODEL|' in name:
                                errorNames.append(name)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【节点重名】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement='Error_SameNameNode')  
                    else:
                        mc.delete('Error_SameNameNode')  
                            
                print '\n'   
                
                # 检测重名错误|shape节点检测
                if checkType == '' or checkType == 'sameShapeCheck':
                    errorNames = []
                    errorNamesTemp = self.checkSameName('mesh')
                    errorNamesTemp = errorNamesTemp + self.checkSameName('nurbsCurve')
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            if '|MODEL|' in name:
                                errorNames.append(name)
                    passList = []
                    if errorNames and (info[0] + '_' + info[1]) not in passList:
                        for name in errorNames:
                            infoWrong.append(u'【shape重名】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement='Error_SameNameShape')  
                    else:
                        mc.delete('Error_SameNameShape')                      
    
                print '\n'
                
                # 检测mesh同名节点 
                if checkType == '' or checkType == 'sameShapeNodeCheck':
                    errorNames = []
                    errorNamesTemp = self.checkMeshSameNameNodes()
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            if '|MODEL|' in name:
                                errorNames.append(name)
                    if errorNames:
                        if errorNames == [u'有同名mesh!!!']:
                            infoWrong.append(u'【shape重名】\t\t%s' % (str('有同名mesh!!!')))
                        else:
                            for name in errorNames:
                                infoWrong.append(u'【shape同名】\t\t%s' % (str(name)))
                                errorPrint += 1
                            mc.sets(errorNames , e=1 , addElement='Error_SameShapeNode')  
                    else:
                        mc.delete('Error_SameShapeNode')                      
    
                print '\n'

            # 检测proxy属性信息
            if checkType == '' or checkType == 'proxyInfo':
                from idmt.maya.py_common import sk_sceneConfig
                reload(sk_sceneConfig)
                errorNames = sk_sceneConfig.sk_sceneConfig().sk_sceneProxyInfoCheck(0)
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【proxy位移】\t\t%s' % (str(name)))
                        errorPrint += 1
                    mc.sets(errorNames , e=1 , addElement='Error_ProxyInfo')  
                else:
                    mc.delete('Error_ProxyInfo')
                    
            print '\n'

            # 检测Mesh错误
            if checkType == '' or checkType == 'meshError':
                errorNames = self.checkMeshError()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【Mesh错误】\t\t%s' % (str(name)))
                        errorPrint += 1

            # 检测SmoothSet
            # 只对model，tx，render进行检测
            if checkType == '' or checkType == 'smoothSet':
                import sk_smoothSet
                reload(sk_smoothSet)
                if info[3].split('.')[0] in ['mo','tx']:
                    errorNames = self.checkModelSmoothSet(info[0])
                    if errorNames:
                        if errorNames == [u'未发现正版SMOOTH_SET']:
                            infoWrong.append(u'【SmoothSet】\t\tDidn\'t find SMOOTH_SET')
                            errorPrint += 1
                        if errorNames == [u'未发现有效SMOOTH物体']:
                            infoWrong.append(u'【SmoothSet】\t\tDidn\'t find Smooth Objects')
                            errorPrint += 1
                        if errorNames and errorNames != [u'未发现正版SMOOTH_SET'] and errorNames != [u'未发现有效SMOOTH物体']:
                            for name in errorNames:
                                infoWrong.append(u'【Smmoth漏掉】\t\t%s' % (str(name)))
                                errorPrint += 1
                            mc.sets(errorNames , e=1 , addElement='Error_SmoothLost')  
                    else:
                        mc.delete('Error_SmoothLost')
                # CacheSet
                sk_sceneTools.sk_sceneTools().checkCacheSetAdd()
                # AnimSet
                sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()
                sk_sceneTools.sk_sceneTools().sk_sceneSetCombineConfig(info[0])

        else:
            print '\n'
            infoWrong.append(u'【 错 误 】\t\t文件名错误！ ')
            errorPrint += 1
        # 删除ErrorSet
        if errorPrint == 0:
            try:
                mc.delete('ErrorTemp_Set')
            except:
                pass

        # 输出错误消息
        print(u'=============================【文件中错误如下】=============================')
        for info in infoWrong:
            print info
        print(u'===========================【目前】共计【%s】处错误===========================' % (errorPrint))
        mc.warning(u'===========================【目前】共计【%s】处错误===========================' % errorPrint)
        
        # 解锁
        sk_sceneTools.sk_sceneTools().checkUnlockMSHV()
        sk_sceneTools.sk_sceneTools().checkUnlockMSHGeo()
        
        return errorPrint
    
    #------------------------------#
    # 选取报错物体
    def checkDetailsObject(self, info):
        info = info.split('\t')[-1]

    #------------------------------#
    # ErrorSet
    def checkErrorSetCreate(self):
        # 文件名检测，判断环节
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if mc.objExists('ErrorTemp_Set'):
            pass
        else:
            mc.createNode('objectSet', n='ErrorTemp_Set')
        # 命名错误
        if mc.objExists('Error_MSHName'):
            mc.sets(cl='Error_MSHName')
        else:
            mc.createNode('objectSet', n='Error_MSHName')
            mc.sets('Error_MSHName', e=1, addElement='ErrorTemp_Set')
        # 非四边形
        if mc.objExists('Error_N4Edges'):
            mc.sets(cl='Error_N4Edges')
        else:
            mc.createNode('objectSet', n='Error_N4Edges')
            mc.sets('Error_N4Edges', e=1, addElement='ErrorTemp_Set')   
        # instance
        if mc.objExists('Error_Instance'):
            mc.sets(cl='Error_Instance')
        else:
            mc.createNode('objectSet', n='Error_Instance')
            mc.sets('Error_Instance', e=1, addElement='ErrorTemp_Set')   
        if len(info) > 3:
            # MaxSmoothSet
            if mc.objExists('Error_MaxSmooth'):
                mc.sets(cl='Error_MaxSmooth')
            else:
                mc.createNode('objectSet', n='Error_MaxSmooth')
                mc.sets('Error_MaxSmooth', e=1, addElement='ErrorTemp_Set')
            # MaxSmoothSet
            if mc.objExists('Error_SignInfo'):
                mc.sets(cl='Error_SignInfo')
            else:
                mc.createNode('objectSet', n='Error_SignInfo')
                mc.sets('Error_SignInfo', e=1, addElement='ErrorTemp_Set')
        # SameName Transform
        if mc.objExists('Error_SameNameNode'):
            mc.sets(cl='Error_SameNameNode')
        else:
            mc.createNode('objectSet', n='Error_SameNameNode')
            mc.sets('Error_SameNameNode', e=1, addElement='ErrorTemp_Set')  
        # SameName Shape
        if mc.objExists('Error_SameNameShape'):
            mc.sets(cl='Error_SameNameShape')
        else:
            mc.createNode('objectSet', n='Error_SameNameShape')
            mc.sets('Error_SameNameShape', e=1, addElement='ErrorTemp_Set')  
        # Error_SameShapeNode
        if mc.objExists('Error_SameShapeNode'):
            mc.sets(cl='Error_SameShapeNode')
        else:
            mc.createNode('objectSet', n='Error_SameShapeNode')
            mc.sets('Error_SameShapeNode', e=1, addElement='ErrorTemp_Set') 
        # ProxyInfo
        if mc.objExists('Error_ProxyInfo'):
            mc.sets(cl='Error_ProxyInfo')
        else:
            mc.createNode('objectSet', n='Error_ProxyInfo')
            mc.sets('Error_ProxyInfo', e=1, addElement='ErrorTemp_Set')  
        # SmoothLost
        if mc.objExists('Error_SmoothLost'):
            mc.sets(cl='Error_SmoothLost')
        else:
            mc.createNode('objectSet', n='Error_SmoothLost')
            mc.sets('Error_SmoothLost', e=1, addElement='ErrorTemp_Set')  
        # RenderState
        if mc.objExists('Error_RenderState'):
            mc.sets(cl='Error_RenderState')
        else:
            mc.createNode('objectSet', n='Error_RenderState')
            mc.sets('Error_RenderState', e=1, addElement='ErrorTemp_Set')  

    #------------------------------#
    # cache path 环境变量处理
    def checkCacheEnvPath(self):
        cacheFiles = mc.ls(type='cacheFile')
        if cacheFiles:
            for node in cacheFiles:
                cachePath = mc.getAttr(node + '.cachePath')
                cachePathNew = cachePath.replace('//file-cluster/GDC/Projects','${IDMT_PROJECTS}')
                mc.setAttr((node + '.cachePath'),cachePathNew,type = 'string')
    
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】model命名检测工具系统
    # 0.仅在model,rig,texture通用
    # 1.检测只有一个大组
    # 2.所有最后一位是'_'的物体是否有mesh节点
    # Author : 沈  康
    # Data   : 2013_05_16
    #------------------------------#
    # 检测大纲内大组数
    def checkOutlinerGroup(self):
        grps = mc.ls(type='transform', l=1)
        grps.remove('|persp')
        grps.remove('|top')
        grps.remove('|front')
        grps.remove('|side')
        rootGrp = []
        for grp in grps:
            setpGrp = grp.split('|')
            if len(setpGrp) == 2:
                rootGrp.append(grp)
        return rootGrp
    
    #------------------------------#
    # 仅检测MODEL及其下的节点    
    # 检测MSH前缀,'_'后缀的检测：有'_'必须有shape，无'_'必须无shape    
    # 检测最后后缀多重'_'的检测，如'MSH_c_hi_mouth__'进行报错处理
    # 对于MSH命名，必须是MSH_c_hi_XX这样的命名，除了MSH_all及MSH_geo
    # 允许nurbs控制器在MODEL组
    def checkMSHName(self, model):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if model == 1:
            grps = mc.ls(type='transform', l=1)
            grps.remove('|persp')
            grps.remove('|top')
            grps.remove('|front')
            grps.remove('|side')
        else:
            model = mc.ls('MODEL')
            try:
                grps = mc.listRelatives(model[0], c=1, type='transform', ad=1, f=1)
            except:
                grps = []
        errorInfo = []
        if grps:
            for grp in grps:
                # 检测命名后缀    
                # MSH前缀判断，MODEL除外
                setpGrp = grp.split('|')
                grpConfig = setpGrp[-1]
                # 对set类不处理MSH前缀
                if shotInfo[1][0] not in ['s', 'S']:
                    # 对RIG组不检测MSH
                    if '|RIG|' not in grp and grpConfig != 'RIG':
                        if grpConfig[0:4] != 'MSH_':
                            exGrp = ['MODEL', 'Master']
                            if grpConfig not in exGrp:
                                errorInfo.append(grp)
                # 长度问题.只对mesh检测
                exName = ['MSH_all', 'MSH_geo', 'Master', 'WORLD']
                if grpConfig[-1] == '_':
                    split = grpConfig.split('_')
                    if len(split) < 4:
                        errorInfo.append(grp)
                # mesh'_'后缀判断
                if grpConfig[-1] == '_':
                    split = grpConfig.split('_')
                    # '__'的处理
                    if split[-2] == '':
                        errorInfo.append(grp)
                    # 模型的子物体必须有shape,且为mesh
                    shape = mc.listRelatives(grp , pa=1 , ni=1 , s=1 , type='mesh' , f=1)
                    if shape :
                        continue
                    else:
                        errorInfo.append(grp)
                # 无'_'后缀的判断，除了nurbsCurve，必须没有Shape
                else:
                    shape = mc.listRelatives(grp, s=1, ni = 1,f=1)
                    if shape:
                        needNodes = ['nurbsCurve','directionalLight','ambientLight','pointLight','spotLight','areaLight','volumeLight']
                        if mc.nodeType(shape[0]) not in needNodes:
                            errorInfo.append(grp)
        return list(set(errorInfo))
    
    #------------------------------#
    # 仅检测MODEL及其下的节点    
    # 检测每个有mesh节点的物体是否有.MaxSmooth属性
    def checkModelSmooth(self, model):
        if model == 1:
            grps = mc.ls(type='transform', l=1)
            grps.remove('|persp')
            grps.remove('|top')
            grps.remove('|front')
            grps.remove('|side')
        else:
            model = mc.ls('MODEL')
            try:
                grps = mc.listRelatives(model[0], c=1, type='transform', ad=1, f=1)
            except:
                grps = []
        errorInfo = []
        if grps:
            for grp in grps:
                # 只支持mesh
                shape = mc.listRelatives(grp , pa=1 , ni=1 , s=1 , type='mesh' , f=1)
                if shape:
                    if mc.nodeType(shape[0]) == 'mesh':
                        # 判断是否有MaxSmooth属性
                        attr = mc.ls(grp + '.MaxSmooth')
                        if not attr:
                            errorInfo.append(grp)
        return errorInfo

    #------------------------------#
    # 检测物体里属性值NaN的情况 mode:0_asset,1_shot
    def checkAttrNaNValue(self,mode = 0,returnMode = 0):
        errorObjs = []
        attrList = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
        modelKey = 'MODEL'
        if mode in [1]:
            modelKey = '*:MODEL'
        modelGrp = mc.ls(modelKey,type = 'transform',l=1)
        checkGrps = mc.listRelatives(modelGrp,ad=1,type='transform',f=1)
        if not checkGrps:
            return errorObjs
        for checkGrp in checkGrps:
            errorState = 0
            for attr in attrList:
                value = mc.getAttr(checkGrp+attr)
                # nan NaN
                if value != value:
                    errorState = 1
                if errorState:
                    if checkGrp not in errorObjs:
                        if returnMode:
                            errorObjs.append(u'[NaNValue|检查物体位移属性] %s'%checkGrp)
                        else:
                            errorObjs.append(checkGrp)
                    continue
        return errorObjs

    #-----------------------------------------#
    
    #------------------------------#
    # 【核心】重命名检测及修正工具
    # 0.所有环节通用
    # 1.对多边形,nurbs曲面和细分曲面后缀加'_'
    # Author: 沈  康
    # Data    :2013_05_29-2013_05_30
    # 2.修正顺序：
    # checkSameRename('MSH')
    # checkSameRename('mesh')
    # checkSameRename('nurbsCurve')
    # checkTransformShapeSameNameConfig()
    # checkMeshSameNameNodesConfig()
    #------------------------------#
    # 新版重名，只有一个循环、while还可以优化
    # 获取重名
    def checkSameName(self, nodeType='transform',skipGrp = '',needShape = 0):
        # translate处理
        errorInfo = []
        if nodeType in ['transform']:
            grps = mc.ls(type=nodeType, l=1)
            simpleGrps = []
            simpleSetGrps = []
            check = 0
            skipNum = 0
            for grp in grps:
                if skipGrp :
                    if not (':%s|'%skipGrp in grp or '|%s|'%skipGrp in grp):
                        skipNum += 1
                        continue
                if needShape:
                    shape = mc.listRelatives(grp,s=1)
                    if not shape:
                        skipNum += 1
                        continue
                simple = grp.split('|')[-1]
                simpleGrps.append(simple)
                simpleSetGrps.append(simple)
                if (len(list(set(simpleSetGrps))) + check) != len(simpleGrps):
                    check += 1
                    tempGrps = simpleGrps[:]
                    tempAdd = 0
                    while tempGrps.count(simple) > 0:
                        errorInfo.append(grps[int(tempGrps.index(simple) + tempAdd + skipNum)])
                        tempAdd += 1
                        tempGrps.remove(simple)
        # mesh|shape处理
        if nodeType in ['mesh','nurbsCurve']:
            grps = mc.ls(type=nodeType, l=1)
            simpleGrps = []
            simpleSetGrps = []
            check = 0
            skipNum = 0
            for grp in grps:
                if skipGrp and '%s|'%(skipGrp) not in grp:
                    skipNum += 1
                    continue
                simple = grp.split('|')[-1]
                simpleGrps.append(simple)
                simpleSetGrps.append(simple)
                if (len(list(set(simpleSetGrps))) + check) != len(simpleGrps):
                    check += 1
                    tempGrps = simpleGrps[:]
                    tempAdd = 0
                    while tempGrps.count(simple) > 0:
                        errorInfo.append(grps[int(tempGrps.index(simple) + tempAdd + skipNum)])
                        tempAdd += 1
                        tempGrps.remove(simple)
        return list(set(errorInfo))

    #------------------------------#
    # 【辅助】数据处理，涉及到重名父子先后关系
    # 重名字典存储,存储数据深度
    def checkSameNameDetails(self , nodeType='transform' , objs = []):
        needNodeType = ['transform','mesh','nurbsCurve']
        # 相同名字
        if objs == []:
            if nodeType in needNodeType:
                grps = self.checkSameName(nodeType)
            # 全部大写MSH
            if nodeType == 'MSH':
                grps = mc.ls('msh_*', type='transform', l=1)
            # 全部小写msh
            if nodeType == 'msh':
                grps = mc.ls('MSH_*', type='transform', l=1)
        else:
            grps = objs
        # 信息
        simpleGrps = []
        # 全名信息
        sameDetails = dict({})
        MSHNameDetails = []
        # 组深度信息
        deepDetails = dict({})
        MSHDeepDetails = []
        if grps:
            for grp in grps:
                simple = grp.split('|')[-1]
                simpleGrps.append(simple)
                if nodeType == 'MSH' or nodeType == 'msh':
                    MSHNameDetails.append(grp)
                    MSHDeepDetails.append(len(grp.split('|')))
            # 键集
            simpleSetGrps = list(set(simpleGrps))
            # 键集合,创建默认键list(set(simpleGrps))
            for key in simpleSetGrps:
                # 创建键
                sameDetails[key] = []
                deepDetails[key] = []
                if nodeType in needNodeType:
                    allIndex = self.checkListSameAllIndex(simpleGrps, key)
                    for index in allIndex:
                        sameDetails[key].append(grps[index])
                        deepDetails[key].append(len(grps[index].split('|'))) 
        else:
            sameDetails = []
            deepDetails = []
        # 返回数据
        result = []
        if nodeType in needNodeType:
            result.append(sameDetails)
            result.append(deepDetails)
        if nodeType == 'MSH' or nodeType == 'msh':
            result.append(MSHNameDetails)
            result.append(MSHDeepDetails)
        return result

    #------------------------------#
    # 【核心】 重命名执行函数
    # 重命名相同名字 
    def checkSameRename(self, nodeType='transform',renderCheck = 'MODEL'):
        # 对本身要处理，MSH类
        # 组深度信息
        info = self.checkSameNameDetails(nodeType)
        sameDetails = info[0]
        deepDetails = info[1]
        # 重名编号
        checkID = 1
        if info != [[], []]:
            # 获取key数组
            keyDetail = sameDetails.keys()   
            # Key值下最深信息
            maxDetails = []
            for key in sameDetails:
                if deepDetails[key]:
                    maxDetails.append(max(deepDetails[key]))
            # 处理组类型
            while max(maxDetails) != 0:
                deepIndex = self.checkListSameAllIndex(maxDetails, max(maxDetails))
                # 最深的编号
                for index in deepIndex:
                    # 获取key组内最大值
                    keyMaxIndex = self.checkListSameAllIndex(deepDetails[keyDetail[index]], max(maxDetails))
                    # 重名编号
                    for jIndex in keyMaxIndex:
                        # 判断是否需要重命名
                        renamePerform = 0
                        if renderCheck:
                            if ('|' + renderCheck + '|') in sameDetails[keyDetail[index]][jIndex]:
                                renamePerform = 1
                        else:
                            renamePerform = 1
                        # 重命名
                        if renamePerform:
                            # 先处理shape
                            shape = mc.listRelatives(sameDetails[keyDetail[index]][jIndex], s=1, f=1)
                            if shape:
                                # 重命名
                                # mesh类,nurbs及细分类
                                if mc.nodeType(shape[0]) == 'mesh' or mc.nodeType(shape[0]) == 'nurbsSurface' or mc.nodeType(shape[0]) == 'subdiv':
                                    newName = sameDetails[keyDetail[index]][jIndex].split('|')[-1] + str(checkID) + '_'
                                    checkID += 1
                                    mc.rename(sameDetails[keyDetail[index]][jIndex] , newName)
                                # nurbs曲线及骨骼等
                                else:
                                    newName = sameDetails[keyDetail[index]][jIndex].split('|')[-1] + '_' + str(checkID)
                                    checkID += 1
                                    mc.rename(sameDetails[keyDetail[index]][jIndex] , newName)
                            # 大组类
                            else:
                                newName = sameDetails[keyDetail[index]][jIndex].split('|')[-1] + '_' + str(checkID)
                                checkID += 1
                                mc.rename(sameDetails[keyDetail[index]][jIndex] , newName)
                        # 清除key信息
                        sameDetails[keyDetail[index]][jIndex] = ''
                        deepDetails[keyDetail[index]][jIndex] = 0
                # 下一轮更新
                maxDetails = []
                for key in sameDetails:
                    # objs = sameDetails[key]
                    if deepDetails[key]:
                        maxDetails.append(max(deepDetails[key]))
                    else:
                        maxDetails.append(0)           
        # 输出重命名数量
        #print(u'====================共处理【%s】处【%s】重命名====================' % (str(checkID - 1), str(nodeType)))
        print(u'====================共处理【%s】处【%s】重命名====================' % ((checkID - 1), (nodeType)))

    #------------------------------#
    # 处理物体和形节点同名
    def checkTransformShapeSameNameConfig(self):
        grps = mc.ls(type = 'transform',l=1)
        renameNum = 0
        if grps:
            for grp in grps:
                shape = mc.listRelatives(grp,ni=1 ,s = 1,f = 1)
                if shape:
                    grpName = grp.split('|')[-1]
                    shapeName = shape[0].split('|')[-1]
                    if grpName == shapeName:
                        mc.rename(shape[0],shapeName + 'Shape')
                        renameNum += 1
        print(u'====================共处理【%s】处【%s】重命名====================' % ((renameNum), (u'物形')))
    
    #------------------------------#
    # 处理mesh同名物体
    def checkMeshSameNameNodesConfig(self):
        meshInfos = self.checkMeshSameNameNodes()
        renameNum = 0
        if meshInfos and meshInfos != [u'有同名mesh!!!']:
            # 被transform和mesh检测干掉后应该不存在同类型的同名
            # 保险点不处理组
            num = 0
            for infoNode in meshInfos:
                shape = mc.listRelatives(infoNode,ni=1 ,s = 1,f = 1)
                if shape:
                    nodeName = infoNode.split('|')[-1]
                    # 后缀记数
                    num += 1
                    if mc.nodeType(shape[0]) == 'mesh':
                        newName = nodeName + str(num) + '_'
                    else:
                        newName = nodeName + str(num)
                    mc.rename(infoNode , newName)
                    renameNum += 1
        print(u'====================共处理【%s】处【%s】重命名====================' % ((renameNum), (u'mesh同名')))
                        
    #------------------------------#
    # 检测mesh同名物体（包括）
    def checkMeshSameNameNodes(self):
        # 获取mesh
        meshes = mc.ls(type = 'mesh')
        allMeshes = list(set(meshes))
        errorInfo = []
        if len(meshes) == len(allMeshes):
            for mesh in meshes:
                shapeName = mesh
                if '|' in mesh:
                    shapeName = mesh.split('|')[-1]
                meshSame = mc.ls(shapeName,l=1)
                if len(meshSame) > 1:
                    for obj in meshSame:
                        if mc.nodeType(obj) != 'mesh':
                            errorInfo.append(obj)
        else:
            errorInfo = [u'有同名mesh!!!']
        return errorInfo

    #------------------------------#
    # 处理msh及MSH统一问题
    def checkMSHKeepOneRename(self, mshType='MSH'):
        # 处理msh大小写问题，统一大写
        grpInfos = self.checkSameNameDetails(mshType)
        nameDetails = grpInfos[0]
        deepDetails = grpInfos[1]
        # ID
        checkID = 0
        if nameDetails:
            # 传递数据
            nameConfig = nameDetails[:]
            deepConfig = deepDetails[:]
            # 处理最深的
            maxDeep = max(deepConfig)
            # 开始循环
            while deepConfig:
                maxInfo = self.checkListSameAllIndex(deepConfig, maxDeep)
                # 开始处理
                for i in range(len(maxInfo)):
                    oldName = nameConfig[maxInfo[i] - i]
                    if mshType == 'MSH':
                        tempName = oldName.split('|')[-1]
                        samePart = tempName.split('msh_')[-1]
                    if mshType == 'msh':
                        tempName = oldName.split('|')[-1]
                        samePart = tempName.split('MSH_')[-1]
                    newName = mshType + '_' + samePart
                    mc.rename(oldName , newName)
                    checkID += 1
                    # 剔除记录
                    nameConfig.remove(nameConfig[maxInfo[i] - i])
                    deepConfig.remove(deepConfig[maxInfo[i] - i])
                if deepConfig:
                    maxDeep = max(deepConfig)
        # 输出重命名数量
        #print(u'====================共处理【%s】处【%s】重命名====================' % (str(checkID), str(mshType)))
        print(u'====================共处理【%s】处【%s】重命名====================' % ((checkID), (mshType)))
        
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】【CheckTools小功能】
    #------------------------------#
    # MODEL或者其他阶段的instance检测
    def checkInstance(self, model = 0):
        if model == 1:
            grps = mc.ls(type='transform', l=1)
            grps.remove('|persp')
            grps.remove('|top')
            grps.remove('|front')
            grps.remove('|side')
        else:
            model = mc.ls('MODEL')
            try:
                grps = mc.listRelatives(model[0], c=1, type='transform', ad=1, f=1)
            except:
                grps = []
        errorInfo = []
        newGrps = []
        if grps:
            for grp in grps:
                shape = mc.listRelatives(grp , pa=1 , ni=1 , s=1 , type='mesh' , f=1)
                if shape:
                    newGrps.append(shape[0].split('|')[-1])
                    lenOld = len(newGrps)
                    newGrps = list(set(newGrps))
                    lenNew = len(newGrps)
                    if lenOld != lenNew:
                        errorInfo.append(grp)

    #------------------------------#
    # 非polygon检测
    def checkNotPoly(self,MODELSkipState = 0):
        nodeTypes = ['nurbsSurface','nurbsCurve','subdiv']
        noCheckGrps = sk_infoConfig.sk_infoConfig().dyMoGrps
        errorNames = []
        model = self.renderGrp
        if MODELSkipState:
            model = mc.ls(self.tempRGrp)
        for nodeType in nodeTypes:
            if not mc.ls(model):
                continue
            objs = mc.listRelatives(model,ad = 1,type = nodeType,f=1)
            if not objs:
                continue
            errorNames = errorNames + objs
        errorObjs = []
        for checkObj in errorNames:
            checkState = 1
            for noCheckGrp in noCheckGrps:
                if '|%s|'%noCheckGrp in checkObj:
                    checkState = 0
            if not checkState:
                continue
            errorObjs.append(checkObj)
        return errorObjs

    #------------------------------#
    # rootGrp检测
    def checkRootGrpName(self):
        rootGrp = mc.ls(assemblies=True,l=1)
        try:
            rootGrp.remove('|persp')
            rootGrp.remove('|top')
            rootGrp.remove('|front')
            rootGrp.remove('|side')
        except:
            pass
        rightRootGrp = sk_infoConfig.sk_infoConfig().checkAssetRootGrp()
        if '|%s'%rightRootGrp not in rootGrp:
            return 1
        return 0

    #------------------------------#
    # namespace检测
    def checkNamespace(self,setMode = 0):
        infoWrong = []
        namespace = mc.namespaceInfo(listOnlyNamespaces = 1)
        namespace.remove('UI')
        namespace.remove('shared')
        if len(namespace) != 0:
            if not setMode:
                for ns in namespace:
                    infoWrong.append(u'存在namespace [%s],请清理掉'%ns)
            else:
                for ns in namespace:
                    objs = mc.ls(ns + ':*',l=1)
                    if not objs:
                        # 空的
                        infoWrong.append(u'存在非参考namespace [%s],请清理掉'%ns)
                    else:
                        # 检查是否参考
                        isRef = mc.referenceQuery(objs[0], isNodeReferenced = 1)
                        if not isRef:
                            infoWrong.append(u'存在非参考namespace [%s],请清理掉'%ns)
        return infoWrong

    #------------------------------#
    # rg文件MODEL组内非参考检测
    def checkRGModel(self,MODELSkipState = 0):
        modelKey = self.renderGrp
        if MODELSkipState:
            modelKey = self.tempRGrp
        if not mc.ls('*:%s'%(modelKey)):
            return []
        ModelGrp = mc.ls('*:%s'%(modelKey))
        checkGrp = mc.listRelatives(ModelGrp,p=1,f= 1)
        meshes = []
        temp = mc.listRelatives(checkGrp,ad = 1, type = 'mesh',f=1)
        if not temp:
            temp = []
        meshes = meshes + temp
        temp = mc.listRelatives(checkGrp,ad = 1,type = 'baseLattice',f = 1)
        if not temp:
            temp = []
        meshes = meshes + temp
        errorList = []
        for mesh in meshes:
            ifRef = mc.referenceQuery(mesh,isNodeReferenced = 1)
            if ifRef:
                continue
            grp = mc.listRelatives(mesh,p=1,f=1,type = 'transform')
            if not grp:
                continue
            ifRef = mc.referenceQuery(grp,isNodeReferenced = 1)
            if ifRef:
                continue
            errorList.append(mesh)
        return errorList
    
    #------------------------------#
    # model用intermediate物体检测
    def checkIntermediateObjectError(self,MODELSkipState = 0):
        errorInfo = []
        extraInfo = ['eye']
        model = mc.ls(self.renderGrp,l = 1)
        if MODELSkipState:
            model = mc.ls(self.tempRGrp,l = 1)
        if not model:
            return []
        meshes = mc.listRelatives(model,ad = 1,type = 'mesh',f = 1)
        if not meshes:
            return []
        extraAttrs = sk_infoConfig.sk_infoConfig().dyMoAttrs
        for mesh in meshes:
            value = mc.getAttr(mesh + '.intermediateObject')
            if not value:
                continue
            grp = mc.listRelatives(mesh,ap = 1,type = 'transform',f = 1)
            if not grp:
                continue
            grp = grp[0]
            if mc.ls(grp + '._nr_'):
                continue
            # 屏蔽特殊属性物体
            checkMode = 1
            for attr in extraAttrs:
                if mc.ls(grp + '.' + attr):
                    checkMode = 0
            if not checkMode:
                continue
            # 开始检测
            checkState = 1
            for info in extraInfo:
                if info in grp.split('|')[-1].lower():
                    checkState = 0
            if checkState:
                errorInfo.append(mesh)
        return errorInfo

    #------------------------------#
    # 设置文件线框丢材质检测
    #------------------------------#
    def checkRgLostShader(self,MODELSkipState = 0,refMode = 0):
        modelKey = self.renderGrp
        if MODELSkipState:
            modelKey = self.tempRGrp
        if refMode:
            ModelGrp = mc.ls('*:%s'%modelKey,l=1)
        else:
            ModelGrp = mc.ls(modelKey,l=1)
        sgState = sk_infoConfig.sk_infoConfig().checkSGState()
        if sgState:
            ModelGrp = mc.ls(modelKey,l=1)
        objs = mc.listRelatives(ModelGrp , ad = 1, type = 'transform' , f  = 1)
        meshes = mc.listRelatives(objs , s = 1 ,ni =  1, type = 'mesh' , f  = 1)
        errorMesh = []
        for mesh in meshes:
            sgNode = mc.listConnections(mesh,s=0,d=1,type = 'shadingEngine')
            if not sgNode:
                errorMesh.append(mesh)
        return errorMesh

    # ------------------------------#
    # 设置，约束必须放到灯光或者物体层级
    def checkconstraintObjs(self,returnMode = 1):
        constraintNodes = mc.ls(type = 'constraint')
        skipTypes = ['mesh','joint','light','baselattice','lattice','constraint']
        renderGrp = sk_infoConfig.sk_infoConfig().renderGrp
        errorGrps = []
        for checkNode in constraintNodes:
            targetGrps = mc.listConnections(checkNode,s=0,d=1,type = 'transform')
            if not targetGrps:
                continue
            targetGrps = list(set(targetGrps))
            for checkGrp in targetGrps:
                if 'constraint' in checkGrp.lower():
                    continue
                fullNode = mc.ls(checkGrp,l=1)[0]
                if '%s|'%renderGrp not in fullNode:
                    continue
                if not ('|%s|'%renderGrp in fullNode or ':%s|'%renderGrp in fullNode):
                    continue
                childNode = mc.listRelatives(fullNode,s=1,ni=1)
                if not childNode:
                    errorGrps.append(fullNode)
                else:
                    childType = mc.nodeType(childNode)
                    skipState = 0
                    for skipType in skipTypes:
                        if skipType in childType.lower():
                            skipState = 1
                    if not skipState:
                        errorGrps.append(fullNode)
        # 进一步判断,下面的mesh有没有蒙皮
        tempGrps = []
        for checkGrp in errorGrps:
            meshes = mc.listRelatives(checkGrp,ad = 1, type = 'mesh',f = 1)
            if not meshes:
                continue
            grps = mc.listRelatives(meshes,p=1,type = 'transform',f=1)
            grps = list(set(grps))
            for grp in grps:
                childMeshes = mc.listRelatives(grp,ad=1,type = 'mesh',f=1)
                if len(childMeshes) == 1:
                    tempGrps.append(checkGrp)
        errorGrps = tempGrps
        # 返回
        if returnMode:
            return errorGrps
        else:
            if errorGrps:
                print u'--------------[角色道具]请把约束放到物体级别，别放组上--------------'
                for errorGrp in errorGrps:
                    print errorGrp
                print u'--------------[角色道具]请把约束放到物体级别，别放组上--------------'


    #------------------------------#
    # 所有节点中_an_与_ca_无法共存; 同一节点中，_si_,_nr_,_an_,_ca_只能存在一个
    # ca标记的物体必须是mesh的transform节点
    # ca标记的必须是nurbsCurve
    def checkSignName(self):
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        grps = mc.ls(type='transform', l=1)
        errorInfo = []
        caCheck = 0
        anCheck = 0
        for grp in grps:
            grpName = grp.split('|')[-1]
            signCheck = 0
            # 仅仅mesh
            # 对白海豚来说，_ca_在收集创建list时有MODEL和mesh两个条件，不必再检测
            if '_ct_an' in grpName:
                signCheck += 1
            if '_si_' in grpName:
                signCheck += 1
            if '_nr_' in grpName:
                signCheck += 1
            if signCheck > 1:
                errorInfo.append(grp)
        #if caCheck == 1 and anCheck == 1:
        #    errorInfo.append('cache命名和an命名同时存在！')
        return errorInfo

    #------------------------------#
    # 多边面检测
    def checkFaceVertexs(self ,outInfo = 0,smoothSkip = 0 , triangleNum = 1,doNotCheckGrp = ['hairSys_Grp'],MODELSkipState = 0):
        errorInfo = []
        irInfo = '_ir_'
        nrAttr = '_nr_'
        modelKey = self.renderGrp
        if MODELSkipState:
            modelKey = self.tempRGrp
        model = mc.ls(modelKey)
        if not model:
            model = mc.ls('*:%s'%(modelKey))
            if not model:
                return [[],[]]
        doNotCheckGrp = doNotCheckGrp + sk_infoConfig.sk_infoConfig().dyMoGrps
        # smoothSkip处理
        smoothCheckObjs = []
        if smoothSkip:
            checkObjs = []
            if mc.ls('smooth_0'):
                smoothCheckObjs = mc.sets('smooth_0', q=1)
                smoothCheckObjs = mc.ls(smoothCheckObjs,l=1)
                checkObjs = checkObjs + smoothCheckObjs
            if mc.ls('*:smooth_0'):
                smsSetNode = mc.ls('*:smooth_0')
                smoothCheckObjs = mc.sets(smsSetNode, q=1)
                smoothCheckObjs = mc.ls(smoothCheckObjs,l=1)
                checkObjs = checkObjs + smoothCheckObjs
            smoothCheckObjs = checkObjs
        grps = mc.listRelatives(model[0], type='transform', ad=1, f=1)
        if not grps:
            return [[],[]]
        triangleErrorObjs = []
        for grp in grps:
            shape = mc.listRelatives(grp, ni=1 , s=1 , type='mesh' , f=1)
            triangleCheckNum = 0
            doNotCheckState = 0
            for checkGrp in doNotCheckGrp:
                if '%s|'%checkGrp in grp:
                    doNotCheckState = 1
                break
            if doNotCheckState:
                continue
            if not shape:
                continue
            if smoothSkip and grp in smoothCheckObjs:
                continue
            try:
                faceNum = mc.polyEvaluate(grp, f=1)
                # 这里有时候会出错,尤其是命名中加了"_ca_"和"_"后缀的时候
                if faceNum:
                    for i in range(faceNum):
                        # 获取面的点
                        pointInfo = list(set(mc.polyInfo((grp + '.f[' + str(i) + ']'), faceToVertex=1)[0].split(':')[1].split(' ')))
                        if outInfo:
                            # 检测模式，查询所有非四边形
                            if len(pointInfo) not in [6]:
                                addState = 1
                                if irInfo in grp.split('|')[-1].lower():
                                    addState = 0
                                if mc.ls(grp + '.' + nrAttr):
                                    addState = 0
                                if addState:
                                    errorInfo.append(grp + '.f[' + str(i) + ']')
                            else:
                                if len(pointInfo) in [5]:
                                    triangleCheckNum += 1
                        else:
                            # checkin模式，拦截非三角形、四边形、五边形
                            if len(pointInfo) not in [5,6,7]:
                                addState = 1
                                if irInfo in grp.split('|')[-1].lower():
                                    addState = 0
                                if mc.ls(grp + '.' + nrAttr):
                                    addState = 0
                                if addState:
                                    errorInfo.append(grp + '.f[' + str(i) + ']')
                            else:
                                if len(pointInfo) in [5]:
                                    triangleCheckNum += 1
                else:
                    addState = 1
                    if irInfo in grp.split('|')[-1].lower():
                        addState = 0
                    if mc.ls(grp + '.' + nrAttr):
                        addState = 0
                    if addState:
                        errorInfo.append(grp)
                if triangleCheckNum / faceNum > triangleNum:
                    triangleErrorObjs.append(grp)
            # 对残留的shape节点进行处理，某些组有shape节点，但不是polygon
            except:
                addState = 1
                if irInfo in grp.split('|')[-1].lower():
                    addState = 0
                if mc.ls(grp + '.' + nrAttr):
                    addState = 0
                if addState:
                    errorInfo.append(grp)
        return [list(set(errorInfo)),triangleErrorObjs]

    #------------------------------#
    # MODEL组下，非眼球的模型属性位移、旋转归零;控制器位移、旋转归零；新增大组缩放非1
    # meshes
    def checkZeroMeshAttrs(self,minCheck = -3,MODELSkipState = 0):
        errorObjs = []
        checkAttrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
        scaleAttrs = ['.sx','.sy','.sz']
        extraInfo = ['_eye','_nozero']
        extraAttrs = ['_noZero','_nozero_','_noZero_']
        modelKey = self.renderGrp
        if MODELSkipState:
            modelKey = self.tempRGrp
        modelGrp = mc.ls(modelKey)
        if not modelGrp:
            modelGrp = mc.ls('*:%s'%(modelKey))
        if modelGrp:
            rootGrp = mc.ls(assemblies=True,l=1)
            removelist = ['|persp','|top','|front','|side']
            for removGrp in removelist:
                if removGrp in rootGrp:
                    rootGrp.remove(removGrp)
            # mesh
            objs = mc.listRelatives(modelGrp,ad = 1 ,type = 'transform',f= 1)
            if not objs:
                return errorObjs
            objs = objs + rootGrp
            for checkObj in objs:
                errorState = 0
                extraState = 0
                # 判断是否例外
                for info in extraInfo:
                    if info in checkObj.split('|')[-1].lower():
                        extraState = 1
                for exAttr in extraAttrs:
                    if mc.ls('%s.%s'%(checkObj,exAttr)):
                        extraState = 1
                if extraState:
                    continue
                # tx,rotate
                for attr in checkAttrs:
                    if not mc.getAttr((checkObj + attr),keyable = 1):
                        continue
                    if abs(mc.getAttr(checkObj + attr)) > 5*pow(10,minCheck):

                        if extraState == 0:
                            errorState = 1
                            break
                # scale
                for checkAttr in scaleAttrs:
                    if mc.getAttr(checkObj + checkAttr) == 1:
                        continue
                    if checkObj in errorObjs:
                        continue
                    errorObjs.append(checkObj)
                if errorState:
                    errorObjs.append(checkObj)
        return errorObjs

    # ctrls
    def checkZeroCtrlAttrs(self,checkType = 0,minCheck = -5,ctrlSetList = ['All_BodySet']):
        errorObjs = []
        checkAttrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
        scaleAttrs = ['.sx','.sy','.sz']
        skipKey = ['_noZero_','_nozero_']
        # 控制器
        ctrlShapes = []
        if checkType == 0:
            ctrlShapes = mc.ls(type = 'nurbsCurve',l = 1)
        if checkType == 1:
            for ctrlSet in ctrlSetList:
                if not mc.ls(ctrlSet):
                    continue
                ctrlTemp = mc.sets(ctrlSet, q=1)
                ctrlTemp = mc.listRelatives(ctrlTemp,s = 1,type = 'nurbsCurve',f = 1)
                ctrlShapes += ctrlTemp
        if not ctrlShapes:
            return errorObjs
        for ctrlShape in ctrlShapes:
            ctrl = mc.listRelatives(ctrlShape,p = 1,f=1)
            if not mc.ls(ctrl):
                continue
            ctrl = ctrl[0]
            skipState = 0
            for checkInfo in skipKey:
                if mc.ls('%s.%s'%(ctrl,checkInfo)):
                    skipState = 1
            if skipState:
                continue
            errorState = 0
            for attr in checkAttrs:
                if not mc.getAttr((ctrl + attr),keyable = 1):
                    continue
                if abs(mc.getAttr(ctrl + attr)) > pow(10,minCheck):
                    errorState = 1
                    break
            for attr in scaleAttrs:
                if not mc.getAttr((ctrl + attr),keyable = 1):
                    continue
                if abs(mc.getAttr(ctrl + attr)-1) > pow(10,minCheck):
                    errorState = 1
                    break
            if errorState:
                errorObjs.append(ctrl)
        return errorObjs

    #------------------------------#
    # 检测polygon是polygon的父体
    def checkPolyParents(self):
        meshes = mc.listRelatives('MODEL',ad = 1, type = 'mesh',f=1)
        errorObjs = []
        extraInfo = ['eye']
        extraAttrs = sk_infoConfig.sk_infoConfig().dyMoAttrs
        if not meshes:
            return errorObjs
        for mesh in meshes:
            objGrp = mc.listRelatives(mesh,p=1,type = 'transform',f=1)
            if not objGrp:
                continue
            objGrp = objGrp[0]
            if mc.ls(objGrp + '._nr_'):
                continue
            checkMode = 1
            # 屏蔽特殊类型物体
            for attr in extraAttrs:
                if mc.ls(objGrp + '.' + attr):
                    checkMode = 0
                    break
            if not checkMode:
                continue
            # 检测
            childMeshes = mc.listRelatives(objGrp,ad = 1,type = 'mesh',f=1)
            lenCheck = 2
            for info in extraInfo:
                if info in mesh.split('|')[-1].lower():
                    lenCheck = 3
                    break
            if len(childMeshes) >= lenCheck:
                errorObjs.append(objGrp)
        if errorObjs:
            return list(set(errorObjs))
        else:
            return errorObjs

    #-------------------------------#
    # tx文件参考rnd文件
    def checkTXRefRnd(self):
        fileName = mc.file(exn = 1, q= 1).split('/')[-1]
        if '_' not in fileName:
            return []
        errorInfos = []
        import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        rfnPathLv1 = refInfos[1][0]
        for refPath in rfnPathLv1:
            needInfo = refPath.split('/')[-1]
            if len(needInfo.split('_')) < 4:
                errorInfos.append(refPath.split('/')[-1])
            else:
                if sk_infoConfig.sk_infoConfig().masterRnd not in needInfo.split('_')[3]:
                    errorInfos.append(refPath.split('/')[-1])
        return errorInfos

    #------------------------------#
    # tx check in shader
    # tx文件测试，所有模型重新赋予材质，失败则报错
    def checkTextureModelShader(self,returnMode = 0,MODELSkipState = 0):
        meshes = mc.ls(type='mesh', l=1)
        if not meshes:
            return
        return
        # 创建新渲染层
        testLayer = 'food_shaderLayer_test'
        if mc.ls(testLayer):
            mc.delete(testLayer)
        modelKey = self.renderGrp
        if MODELSkipState:
            modelKey = self.tempRGrp
        # 获取MODEL下的
        needObjs = []
        noCheckGrps = sk_infoConfig.sk_infoConfig().dyMoGrps
        for mesh in meshes:
            checkState = 1
            for checkGrp in noCheckGrps:
                if '|%s|'%modelKey in mesh:
                    checkState = 0
            if not checkState:
                continue
            if '|%s|'%(modelKey) in mesh:
                needObjs.append(mc.listRelatives(mesh, p=1, f=1)[0])
        needObjs = list(set(needObjs))
        # 创建层
        if not needObjs:
            return
        # 首先备份材质球信息
        from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
        reload(sk_cacheFinalLayout)
        MatLists = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheRecordMaterial(checkObjs = needObjs , finalLayout = 0 ,faceMode = 1,shotType = sk_infoConfig.sk_infoConfig().checkShotType(), server = 0)
        errorObjs = []
        mc.createRenderLayer(needObjs , name='food_shaderLayer_test' , noRecurse=1 , makeCurrent=1)
        # 创建材质
        shaderMain = mc.shadingNode ('lambert', asShader=True, name='food_shader_test')
        shaderMianSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='food_shader_test_SG')
        mc.connectAttr((shaderMain + '.outColor'), (shaderMianSG + '.surfaceShader'))
        for obj in needObjs:
            mesh = mc.listRelatives(obj, ni=1, s=1)
            if not mesh:
                continue
            mesh = mesh[0]
            try:
                mc.sets(obj, e=1, forceElement=shaderMianSG)
            except:
                errorObjs.append(mesh)
        # 删除层，清理垃圾节点
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.delete(testLayer)
        mc.delete(shaderMain)
        mc.delete(shaderMianSG)
        SGInfos = MatLists.keys()
        print '----------------'
        print MatLists

        for checkSGNode in SGInfos:
            shapes = MatLists[checkSGNode]
            for mesh in shapes:
                checkMesh = mesh
                if '.f[' in mesh:
                    checkMesh = mc.listRelatives(mesh.split('.f[')[0],s=1,ni=1,type = 'mesh',f=1)[0]
                SGNode = mc.listConnections(checkMesh,d=1,type = 'shadingEngine')
                if not SGNode:
                    errorObjs.append(mesh)
                else:
                    if checkSGNode not in SGNode:
                        errorObjs.append(mesh)

        if returnMode:
            if errorObjs:
                errorObjs = list(set(errorObjs))
            return errorObjs
        if errorObjs:
            errorObjs = list(set(errorObjs))
            for errorObj in errorObjs:
                print u'-------------'
                print errorObj
                print errorObj.split('|')[-1]
            #errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(39)
            errorInfo= u'-------------[着色]某些物体无法赋予材质，请处理好它们-------------'
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()

        # mel.eval('MLdeleteUnused')

    #------------------------------#
    # 非法mesh检测
    # 这个处理大纲里显示为空组，但实际上有mesh节点的情况
    def checkMeshError(self):
        shaderSGList = self.checkCacheRecordMaterial()
        errorInfo = []
        if shaderSGList:
            keys = shaderSGList.keys()
            for key in keys:
                objs = shaderSGList[key]
                if objs:
                    for obj in objs:
                        if mc.ls(obj):
                            pass
                        else:
                            errorInfo.append(obj) 
        return errorInfo
    
    #------------------------------#
    # smoothSet检测
    #　MODEL下所有物体在3个smoothSet下
    def checkModelSmoothSet(self,projType,errorMode = 0):
        import sk_smoothSet
        reload(sk_smoothSet)
        errorInfo = []
        if not projType:
            projType = 'zm'
        # 合并smoothSet组
        smoothSetCheck = sk_smoothSet.sk_smoothSet().smoothSetCombine('Smooth',projType)
        if smoothSetCheck == 0:
            # 检测是否有货
            smoothObjs = sk_smoothSet.sk_smoothSet().smoothSetGetObjects(0) + sk_smoothSet.sk_smoothSet().smoothSetGetObjects(1) + sk_smoothSet.sk_smoothSet().smoothSetGetObjects(2)
            if smoothObjs:
                needSmoothObjs = []
                for obj in smoothObjs:
                    needState = 1
                    if '_si_' in obj or  '_nr_' in obj or '_proxy_' in obj:
                        needState = 0
                    if mc.ls(obj+'._si_') or mc.ls(obj+'._nr_') or mc.ls(obj+'._proxy_'):
                        needState = 0
                    if needState:
                        needSmoothObjs.append(mc.ls(obj,l=1)[0])
                # 获取MODEL下所有物体
                meshes = mc.listRelatives('MODEL',ad = 1 ,type = 'mesh',f= 1)
                objs = []
                if meshes:
                    for mesh in meshes:
                        objs.append(mc.listRelatives(mesh,p=1,type = 'transform',f=1)[0])
                    objs = list(set(objs))
                    for obj in objs:
                        # 排除参考
                        needState = 1
                        if '_si_' in obj or  '_nr_' in obj or '_proxy_' in obj:
                            needState = 0
                        if mc.ls(obj+'._si_') or mc.ls(obj+'._nr_') or mc.ls(obj+'._proxy_'):
                            needState = 0
                        if needState and (':' not in obj) and (obj not in needSmoothObjs):
                            errorInfo.append(obj)
            else:
                if mc.ls(type = 'mesh'):
                    errorInfo = [u'未发现有效SMOOTH物体']
        else:
            errorInfo = [u'未发现正版SMOOTH_SET']
        smsESet = 'smooth_errorSet'
        if errorMode and errorInfo:
            print '\n-------------Smooth Error'
            needErrorObjs = []
            for info in errorInfo:
                print info
                if mc.ls(info):
                    needErrorObjs.append(info)
            print u'-----共[%s]项'%(str(len(errorInfo)))
            print u'-----若以上是物体信息，请检查是否在smoothSet组-----'
            print u'-----不用于渲染的物体请给transform节点加_nr_属性-----\n'
            if needErrorObjs:
                if not mc.objExists(smsESet):
                    mc.createNode('objectSet', n=smsESet)
                mc.sets(cl=smsESet)
                mc.sets(needErrorObjs, e=1, addElement=smsESet)
            else:
                if mc.objExists(smsESet):
                    mc.delete(smsESet)
            mc.error()
        else:
            if mc.objExists(smsESet):
                mc.delete(smsESet)
        return errorInfo

    #------------------------------#
    # MODEL组下，模型基本渲染属性开启检测
    def checkMeshRenderStates(self,errorMode = 0):
        errorObjs = []
        nrKeyList = ['_si_','_nr_','_proxy_']
        modelGrps = mc.ls('MODEL',l=1) + mc.ls('*:MODEL',l=1)
        attrs = ['.castsShadows','.receiveShadows','.motionBlur','.primaryVisibility','.smoothShading']
        attrs += ['.aiVisibleInDiffuse','.aiVisibleInGlossy']
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        Eyes=[]
        if modelGrps:
            objs = mc.listRelatives(modelGrps,ad = 1 ,type = 'transform',f= 1)
            if objs:
                for mod in objs:
                    if mc.objExists(mod+'.eye') and mod not in Eyes:
                        Eyes.append(mod)
        print Eyes
        attrsN=['.motionBlur','.primaryVisibility','.smoothShading','.aiVisibleInDiffuse','.aiVisibleInGlossy']
        if shotInfo[0] in ['ddz']:
            attrsN=['.motionBlur']
        if modelGrps:
            objs = mc.listRelatives(modelGrps,ad = 1 ,type = 'transform',f= 1)
            if not objs:
                return []
            for obj in objs:
                if obj not in Eyes:
                    attrs=attrs
                else:
                    attrs=attrsN
                mesh = mc.listRelatives(obj,s=1,ni=1,type = 'mesh',f=1)
                if mesh:
                    mesh = mesh[0]
                    checkState = 0
                    for attr in attrs:
                        if not mc.ls(mesh + attr):
                            continue
                        state = mc.getAttr(mesh + attr)
                        if state == 0:
                            checkState = 1
                            break
                    if '_si_' in obj or '_nr_' in obj or '_proxy_' in obj  or '_p_' in obj or '_ctrl' in obj:
                        checkState = 0
                    for nrKey in nrKeyList:
                        if mc.ls('%s.%s'%(obj,nrKey)):
                            checkState = 0
                    if checkState:
                        errorObjs.append(obj)
        else:
            errorObjs = ['No Model']
        if errorMode and errorObjs:
            print '----------------------'
            for errorInfo in errorObjs:
                print errorInfo
            print u'-----渲染shape属性没开启-----'
            mc.error()
        return errorObjs

    #------------------------------#
    # 前期mo,tx非法模型检测
    def checkErrorObjects(self,checkType = ''):
        checkMeshes = mc.listRelatives('MODEL',ad=1,ni=1,type = 'mesh',f=1)
        if not checkMeshes:
            return []
        checkObjs = mc.listRelatives(checkMeshes,p=1,f=1)
        errorObjs = []
        if checkType in ['nonManifoldEdges']:
            errorObjs= mc.polyInfo(checkObjs,nonManifoldEdges=True)

        if checkType in ['nonManifoldVertices']:
            errorObjs= mc.polyInfo(checkObjs,nonManifoldVertices=True)

        if checkType in ['laminaFaces']:
            errorObjs= mc.polyInfo(checkObjs,laminaFaces=True)

        needObjs = []
        if not errorObjs:
            errorObjs = []
        for checkObj in errorObjs:
            checkNode = checkObj
            if '.' in checkNode:
                checkNode = checkNode.split('.')[0]
            if mc.ls(checkNode + '._plfIg_'):
                continue
            needObjs.append(checkObj)

        return needObjs

    #------------------------------#
    # 前期角色道具tx文件检测选面
    def checkFaceShaderDetails(self,MODELSkipState = 0):
        # 检测SG节点
        errorAssetMeshes = []
        SGNodes = mc.ls(type='shadingEngine')
        modelKey = self.renderGrp
        if MODELSkipState:
            modelKey = self.tempRGrp
        if SGNodes:
            for node in SGNodes:
                meshes = mc.sets(node, q=1)
                if not meshes:
                    continue
                for mesh in meshes:
                    if '.' in mesh:
                        checkType = mc.nodeType(mesh.split('.')[0])
                    else:
                        checkType = mc.nodeType(mesh)
                    if checkType in ['mesh']:
                        meshFull = mc.ls(mesh,l = 1)[0]
                        if '|%s|'%(modelKey) in meshFull and '.f[' in mesh:
                            errorAssetMeshes.append(meshFull)
                    else:
                        mesh = mesh.split('.')[0]
                        if mesh not in errorAssetMeshes:
                            errorAssetMeshes.append(mesh)
        return errorAssetMeshes

    #------------------------------#
    # 无用表达式筛选
    def checkNoNeedExpression(self):
        # 检测SG节点
        expNodes = mc.ls(type = 'expression')
        noNeedList = []
        for checkNode in expNodes:
            cons = mc.listConnections(checkNode,s=0,d=1)
            if not cons:
                noNeedList.append(checkNode)
        return noNeedList

    #------------------------------#
    # 特殊内部任务ID
    def checkStrangeIDInfo(self):
        dataPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath() + 'data/localAsset.txt'
        strangeID = sk_infoConfig.sk_infoConfig().checkFileRead(dataPath)
        if strangeID:
            strangeID.remove(strangeID[0])
        return strangeID

    #------------------------------#
    # tx文件，sourceimages 检测
    def checkFileTexture(self):
        errorObjs = []
        # 获取贴图信息
        txDict = {'file':'.fileTextureName','aiImage':'.filename','aiStandIn':'.dso','gpuCache':'.cacheFileName'}
        for fileType in txDict.keys():
            checkNodes = mc.ls(type = fileType)
            keyAttr = txDict[fileType]
            for fileNode in checkNodes:
                inr = mc.referenceQuery(fileNode,inr=1)
                if inr:
                    continue
                imagePath = mc.getAttr(fileNode + keyAttr,x=1)
                if not os.path.exists(imagePath):
                    checkKey = '.<udim>.'
                    if checkKey not in imagePath:
                        errorObjs.append(fileNode)
        return errorObjs

    #------------------------------#
    # 【通用：切换显示|隐藏骨骼】
    #------------------------------#
    # 显示|隐藏骨骼
    def checkJointViewHide(self,showType = 0):
        # 隐藏骨骼
        joints = mc.ls(type='joint')
        if not joints:
            return
        if mc.getAttr(joints[0] + '.drawStyle') == 2:
            showType = 0
        if mc.getAttr(joints[0] + '.drawStyle') == 0:
            showType = 2
        for joint in joints:
            if mc.getAttr(joint +'.drawStyle',l=1):
                pass
            else:
                mc.setAttr((joint + '.drawStyle'), showType)
                
    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【核心】【问题处理函数】
    #------------------------------#
    
    #------------------------------#
    # 为所选物体添加ct_an标记|属性
    def checkCTANSignAdd(self):
        nodes = mc.ls(sl = 1,l= 1)
        if not nodes:
            print (u'=====请选择有效curve====')
            mc.error(u'=====请选择有效curve====')
        nodeNurbsCurveShapes = mc.listRelatives(nodes,ni = 1 ,c = 1 ,type = 'nurbsCurve',f = 1)
        if not nodeNurbsCurveShapes:
            print (u'=====请选择有效curve====')
            mc.error(u'=====请选择有效curve====')
        
        sign = 'ct_an'
        nodeNurbsCurves = mc.listRelatives(nodeNurbsCurveShapes,p = 1 ,type = 'transform',f = 1)
        for node in nodeNurbsCurves:
            attrList = mc.listAttr(node)
            if sign not in attrList:
                mc.select(node)
                mc.addAttr(longName = sign , keyable = 1,attributeType = 'float' , defaultValue = 1.0)
        mc.select(cl = 1)

    #------------------------------#
    # 后缀'_'更改
    # 此函数只处理_ca_及_ct_an
    def checkRenameAddPosfix(self, need, noNeed):
        nodes = mc.ls(sl=1)
        allNodes = mc.ls(type='transform')
        for node in allNodes:
            if noNeed in node:
                #print(u'====================发现【%s】，删除【%s】====================' % (str(noNeed), str(noNeed)))
                print(u'====================发现【%s】，删除【%s】====================' % (noNeed, noNeed))
                temp = node.split(noNeed)
                newNode = temp[0] + temp[1]
                if newNode[-1] != '_':
                    newNode += '_'
                mc.rename(node, newNode)
        for node in nodes:
            if mc.nodeType(node) == 'transform' and need not  in node and '_nr_' not in node  and '_si_' not in node:
                if node[-1] != '_':
                    nodeNew = node + '_' + need[1:]
                else:
                    nodeNew = node + need[1:]
                mc.rename(node, nodeNew)
    
    #------------------------------#
    # 添加'_'后缀
    def checkRenameMSHPosfix(self):
        nodes = mc.ls(sl=1,l=1)
        ID = 0
        for node in nodes:
            temp = node.split('|')[-1]
            if temp[-1] != '_':
                newName = temp + '_'
                mc.rename(node,newName)
                ID += 1
        #print(u'====================共处理【%s】处【无_后缀】命名====================' % (str(ID)))
        print(u'====================共处理【%s】处【无_后缀】命名====================' % (ID))

    #------------------------------#
    # 选取所有的mesh的transfrom节点
    # 选取非MODEL组的
    def sk_sceneSelectAllPolygon(self):
        grps = mc.ls(type = 'transform',l=1)
        objs = []
        for grp in grps:
            if '|MODEL' not in grp:
                shape = mc.listRelatives(grp,s=1,type = 'mesh')
                if shape:
                    objs.append(grp)
        if objs:
            mc.select(objs)

    #------------------------------#
    # 去掉_ca_
    def checkSignReplace(self,sign):
        objs = mc.ls(sl=1)
        for obj in objs:
            if sign in obj:
                splitInfo = obj.split(sign)
                newName = ''
                for i in range(len(splitInfo)):
                    if i == 0:
                        newName = splitInfo[i]
                    if i <(len(splitInfo)-1) and i != 0:
                        newName = newName + splitInfo[i]
                    if i == (len(splitInfo)-1):
                        newName = newName + splitInfo[i]
                print newName
                mc.rename(obj,newName)
        mc.select(cl=1)
                
    #------------------------------#
    # 检测传递动画类型或者cacheSet类型
    def checkSetsType(self):
        cache = 0
        anim = 0
        # 合并Set
        import sk_sceneTools
        reload(sk_sceneTools)
        sk_sceneTools.sk_sceneTools().checkCacheAnimSetCombine('Cache')
        sk_sceneTools.sk_sceneTools().checkCacheAnimSetCombine('Anim')
        # 检测cache
        sk_sceneTools.sk_sceneTools().checkCacheSetAdd()
        objs = mc.sets('MESHES', q=1)
        if objs:
            cache = 1
        # 检测anim
        sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()
        objs = mc.sets('CTRLS', q=1)
        if objs:
            anim = 1
            
        checkSets = [cache,anim]
        return checkSets
    
    #------------------------------#
    # 备份材质，不处理Set材质
    # 字典真爽/\ /\
    def checkCacheRecordMaterial(self, checkObjs = [] , finalLayout = 0 ,cacheMode = 1 ):
        SG = mc.ls(type='shadingEngine')
        # 选取模式
        if checkObjs:
            needSG = []
            errorObjs = []
            for obj in checkObjs:
                if mc.ls(obj) == []:
                    errorObjs.append(obj)
            if errorObjs:
                print u'------------------------以下物体不存在------------------------'
                for info in errorObjs:
                    print info
                print u'------------------------以上物体不存在------------------------'
                mc.error(u'------------------------请检测物体清单------------------------')
            else:
                for obj in checkObjs:
                    mesh = mc.listRelatives(obj,ni=1,type = 'mesh',c =1 ,f = 1)[0]
                    if mc.listConnections(mesh,destination = 1,type = 'shadingEngine'):
                        nodeSG = mc.listConnections(mesh,destination = 1,type = 'shadingEngine')
                        for node in nodeSG:
                            needSG.append(node)
                SG = list(set(needSG))
        # 备份信息
        MatLists = dict({})
        for node in SG:
            connectObjsSG = mc.sets(node, q=1)
            if connectObjsSG:
                MatLists[node] = connectObjsSG
        # finalLayout上传信息
        if finalLayout:
            self.checkCacheRecordMaterialExport(MatLists)
        return MatLists
        
    #------------------------------#
    # 还原材质
    def checkCacheReturnMaterial(self, MatLists = [] ,finalLayout = 0):
        if finalLayout:
            MatLists = self.checkCacheRecordMaterialImport()
        keysSG = MatLists.keys()
        for key in keysSG:
            objs = MatLists[key]
            # 必须加objs，不然会断掉
            if objs:
                mc.sets(objs, forceElement = key)

    #------------------------------#
    # 【辅助】【材质信息备份到服务器端】【拆分用】
    #------------------------------#
    # 输出材质信息
    def checkCacheRecordMaterialExport(self,MatLists,shotType = 2):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localShaderInfoPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server=0,infoMode=1)
        SGKeys = MatLists.keys()
        allInfo = []
        for i in range(len(SGKeys)):
            if i == 0:
                allInfo = SGKeys + [u'********'] + MatLists[SGKeys[i]] + [u'--------']
            else:
                allInfo = allInfo  + MatLists[SGKeys[i]] + [u'--------']
        # 写
        fileInfo = 'ShotShaderInfo.txt'
        mc.sysFile(localShaderInfoPath, makeDir=True)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localShaderInfoPath + fileInfo),allInfo)
        # 上传
        serverDataPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server=1,infoMode=1)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localShaderInfoPath + fileInfo) + '"' + ' ' + '"' + (serverDataPath + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating ShotShaderInfo To Server]===传输[%s]完毕==='%fileInfo

    #------------------------------#
    # 【辅助】【材质信息导入】【拆分用】
    #------------------------------#
    # 输出材质信息
    def checkCacheRecordMaterialImport(self,shotType):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverDataPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server=1,infoMode=1)
        fileInfo = 'ShotShaderInfo.txt'
        allInfo = sk_infoConfig.sk_infoConfig().checkFileRead(serverDataPath + fileInfo)
        # 分割点
        signKeyIndex = self.checkListSameAllIndex(allInfo,u'********')[0]
        signMeshSplitIndexList = self.checkListSameAllIndex(allInfo,u'--------')
        # 开始还原
        MatLists = dict({})
        # 创建keys
        for i in range(signKeyIndex):
            MatLists[allInfo[i]] = []
        # 每类创建
        for i in range(len(signMeshSplitIndexList)):
            if i == 0:
                meshNum = signMeshSplitIndexList[i] - signKeyIndex - 1
            else:
                meshNum = signMeshSplitIndexList[i] - signMeshSplitIndexList[i-1] - 1
            for j in range(meshNum):
                baseMeshIndex = signMeshSplitIndexList[i] - meshNum
                MatLists[allInfo[i]].append(allInfo[baseMeshIndex + j])
        return MatLists

    # 检测贴图尺寸
    def checkTextureFileSize(self,returnMode = 1,sizeMax = 2):
        checkTxFiles = []
        checkNodes = []
        # 收集
        fileNodes = mc.ls(type = 'file') + mc.ls(type = 'aiImage')
        for checkNode in fileNodes:
            checkType = mc.nodeType(checkNode)
            checkAttr = '.fileTextureName'
            if checkType in ['aiImage']:
                checkAttr = '.filename'
            txFile = mc.getAttr(checkNode + checkAttr)
            checkTxFiles.append(txFile)
            checkNodes.append(checkNode)
        yetiNodes = mc.ls(type = 'pgYetiMaya')
        for yetiNode in yetiNodes:
            txNodes = mc.pgYetiGraph(yetiNode,listNodes= 1, type = 'texture')
            if not txNodes:
                continue
            for checkTxNode in txNodes:
                txFile = mc.pgYetiGraph(yetiNode,node = checkTxNode,param= 'file_name', getParamValue = 1)
                checkTxFiles.append(txFile)
                checkNodes.append(checkTxNode)
        # 检测
        maxSize = 1024*sizeMax
        import maya.OpenMaya
        img = maya.OpenMaya.MImage()
        errorFiles = []
        for num in range(len(checkTxFiles)):
            txFile = checkTxFiles[num]
            if not txFile:
                continue
            #img.readFromFile(txFile)
            #width = maya.OpenMaya.uIntPtr()
            #height = maya.OpenMaya.uIntPtr()
            #img.getSize(width, height)
            #if width.value() > maxSize:
            # 这一段有两问题，一来txFile带环境变量时会报错，二来很慢，暂时用这个旧的mel函数代替，黄仲维，20161115
            wh = mel.eval('zwImageSize "%s"' % (txFile.replace("\\", "/")))
            if not wh:
                print u'------------TxFile Path Error'
                print txFile
                mc.error()
            if wh[0] > maxSize:
                indexNum = checkTxFiles.index(txFile)
                errorFiles.append(checkNodes[indexNum])
        if returnMode:
            return errorFiles

    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【辅助】【数据处理】
    #------------------------------#

    #------------------------------#
    # 【辅助】【获取checkList内所有相同元素的编号】
    #  0.通用
    #  Author  : 沈  康
    #  Data    : 2013_05_20
    #------------------------------#
    # 获取list内所有相同元素的编号 ，index number
    def checkListSameAllIndex(self, checkList, checkObj):
        tempList = checkList[:]
        checkAdd = 0
        allIndex = []
        while tempList.count(checkObj) > 0:
            indexNow = tempList.index(checkObj)
            allIndex.append(checkAdd + indexNow)
            tempList.remove(checkObj)
            checkAdd = checkAdd + 1
        return allIndex

    #------------------------------#
    # 【辅助】【层级归类，最深到最高层级】
    #  0.通用
    #  Author  : 沈  康
    #  Data    : 2013_10_30
    #------------------------------#
    # 重新排序
    def sk_checkObjOutlinerReorder(self,objList):
        # 记录长度
        lenInfoList = []
        for obj in objList:
            lenInfoList.append(len(mc.ls(obj,l=1)[0].split('|'))-1)
        # 重新排序
        # 最大值最小为1，最小值最小为1
        reorderList = []
        lenInfo = lenInfoList[:]
        maxDeep = max(lenInfo)
        minDeep = min(lenInfo)
        while maxDeep >= minDeep:
            allIndex = self.checkListSameAllIndex(lenInfo, maxDeep)
            maxObj = []
            for index in allIndex:
                maxObj.append(mc.ls(objList[index],l=1)[0])
                # 更新lenInfo
                lenInfo[index] = 0
            # 存储信息
            reorderList.append(maxObj)
            # 更新max
            maxDeep = max(lenInfo)
        return reorderList
    
    
    #------------------------------#
    #  全流程用
    #------------------------------#
    # 前期禁止arnold,mr test
    def checkAssetforbidenNodes(self,arnoldCheck = 1,mentalray = 1):
        if arnoldCheck:
            arnoldNodes = mc.ls(type='aiAOVDriver')+ mc.ls(type='aiAOVFilter') +mc.ls(type='aiOptions')
            if arnoldNodes:
                print (u'=====Asset 存在 Arnold 节点，请Export清理=====')
                mc.error(u'=====Asset 存在 Arnold 节点，请Export清理=====')
        if mentalray:
            mentalrayNodes = mc.ls(type='mentalrayFramebuffer')+ mc.ls(type='mentalrayOptions') +mc.ls(type='mentalrayGlobals') + mc.ls(type='mentalrayItemsList')
            if mentalrayNodes:
                print (u'=====Asset 存在MR 节点，请用专用工具清理=====')
                mc.error(u'=====Asset 存在MR 节点，请用专用工具清理=====')
            try:
                mel.eval('unloadPlugin "Mayatomr"')
            except:
                pass


    #------------------------------# 
    # 【通用：检测动画文件参考是否anim参考】
    # Author  : 沈  康
    # Data    :2014_08_20
    #------------------------------# 
    # 检测错误的参考
    def checkReferenceInfoCheck(self,inCheckin = 1):
        # 只对anim文件进行检测
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()  
        import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refPaths = refInfo[1][0]
        
        localRef = 0
        localRefInfo = []
        notAnimRef = 0
        notAnimInfo = []
        # 处理参考
        for i in range(len(refPaths)):
            refPath = refPaths[i]
            path = refPath.lower()
             # 检测外部参考
            if 'c:\\' in path or 'c:/' in path or 'd:\\' in path or 'd:/' in path or 'e:\\' in path or 'e:/' in path:
                localRefInfo.append(path.split('/')[0])
                localRef +=1
            # 检测非anim参考,排除孙望参考及相机参考
            fileName = path.split('/')[-1]
            fileRef = path.split('/')[-1].split('.')[0].split('_')
            checkState = 1
            # 小鸡rg暂时不处理
            if shotInfo[0] in ['cl'] and fileRef[-1] == 'rg':
                checkState = 0
            # dod 对动画环节不处理 非anim文件被参考，为函数添加了判定参数，是否是在playblast时的检测===============================
            if shotInfo[0] in [u'do'] and inCheckin != 1:
                checkState = 0
            if fileRef[-1] in ['anim', 'cam', 'notex', 'gpu'] or path.split('/')[-1].split('.')[0] == 'qsk_model' or '_c_h_' in path:
                checkState = 0
            if shotInfo[0] in ['mk'] and 'dy_camerarig_new' in fileName.lower():
                checkState = 0
            if checkState:
                notAnimInfo.append(fileName)
                notAnimRef += 1
            # 检测非法的anim参考
            if '_c_h_ms_anim.mb' in path:
                notAnimInfo.append(fileName)
                notAnimRef += 1
        
        if len(shotInfo) < 4:
            return 0

        if shotInfo[3] in ['an'] and (localRef or notAnimRef):
            localEState = 1
            # 动画文件里本地参考警告
            if shotInfo[0]  in ['nj','yd']:
                localEState = 0
            if localEState:
                print (u'\n===============【错误】有【%s】个本地参考===============' % (localRef))
                for info in notAnimInfo:
                    print info
                print (u'===============【错误】有【%s】个本地参考===============\n' % (localRef))

            # 选择性报错
            notAnimEState = 1
            if shotInfo[0]  in ['nj','yd','ld']:
                notAnimEState = 1
            if shotInfo[0] in ['zm']:
                checkState = 0
                for info in localRefInfo:
                    if 'zm_ef' in info or 'Splash' in info:
                        checkState += 1
                if checkState == len(notAnimInfo):
                    return 0
            if notAnimEState:
                print (u'\n===============【错误】有【%s】个非anim参考===============' % (notAnimRef))
                for info in notAnimInfo:
                    print info
                print (u'===============【错误】有【%s】个非anim参考===============\n' % (notAnimRef))

            if localEState or notAnimEState:
                if shotInfo[0] not in ['dr']:   #temp for deer run project
                    mc.error(u'===============【错误】本文件参考有问题,请处理===============')

    # mel调用重名检测
    def checkSameNameErrorShow(self):
        infoWrong = []
        errorNames = []
        errorNamesTemp = self.checkSameName()
        if errorNamesTemp:
            for name in errorNamesTemp:
                if '|MODEL|' in name:
                    errorNames.append(name)
        if errorNames:
            for name in errorNames:
                infoWrong.append(u'【节点重名】\t\t%s' % (str(name)))
        if infoWrong:
            for info in infoWrong:
                print info
            print u'==============请处理好重名问题！！！=============='
            mc.error()

    #------------------------------#
    # 窗口提醒
    #------------------------------#
    def checkDetailsUI(self,infoWrong):

        errorNum = len(infoWrong)
        result = ''
        for i in range(errorNum):
            if i == 0:
                result = result + infoWrong[i]
            else:
                result = result + '\n' + infoWrong[i]
        UIName = 'sk_checkDetails'
        if mc.window (UIName, ex=1):
            mc.deleteUI(UIName, window=True,)
        mc.window("sk_checkDetails", title=u"检测信息明细 | checkDetails", widthHeight=(self.winSize01[0], self.winSize01[1]), menuBar=0,sizeable = 0)
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',self.bothInfo])
        mc.text(label = '' , height = self.spaceH02)
        mc.text(label = u'请配合outliner的  [ ErrorTemp_Set ] 使用',align = 'center')
        mc.text(label = '' , height = self.spaceH03)
        mc.text(label = u'=============================【文件中错误如下】=============================',align = 'center')
        mc.text(label = '' , height = self.spaceH02)
        mc.scrollField( editable=False, wordWrap=False, text=result )
        mc.text(label = '' , height = self.spaceH02)
        mc.text(label = u'===========================【目前】共计【%s】处错误==========================='%(str(errorNum)),align = 'center')
        mc.text(label = '' , height = self.spaceH01)
        mc.setParent()

        mc.showWindow(UIName)

    #------------------------------#
    # 处理帮助
    #------------------------------#
    def checkConfigHelpUI(self):
        needInfos   = self.checkConfigHelpDict()
        infoKey     = needInfos[0]
        UIName = 'sk_checkConfigHelp'
        if mc.window (UIName, ex=1):
            mc.deleteUI(UIName, window=True)
        mc.window(UIName, title=u"处理方法 | FixHelp", widthHeight=(self.winSize02[0], self.winSize02[1]), menuBar=0,sizeable = 0)
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',self.bothInfo])
        mc.text(label = '' , height = self.spaceH02)
        base = mc.rowColumnLayout(numberOfColumns=2)

        mc.columnLayout(adjustableColumn = True)
        mc.textScrollList('sk_checkKeyScroll',width = self.winSize05[0],height = self.winSize05[1],selectCommand ='from idmt.maya.commonCore.core_mayaCommon import sk_checkTools\nreload(sk_checkTools)\nsk_checkTools.sk_checkTools().checkKeyDetailsGoTo(0)')
        mc.setParent(base)

        mc.columnLayout(adjustableColumn = True)

        mc.textFieldButtonGrp('sk_checkKeyField',label = 'Search',tx = u'【贴图路径】',buttonLabel = u'Search | 搜索',columnWidth3 = self.winSize03,buttonCommand ='from idmt.maya.commonCore.core_mayaCommon import sk_checkTools\nreload(sk_checkTools)\nsk_checkTools.sk_checkTools().checkKeyDetailsGoTo(1)')
        mc.text(label = '' , height = self.spaceH02)
        mc.scrollField('sk_checkDetailsField',width = self.winSize06[0],height = self.winSize06[1],editable = 0 )
        mc.setParent(base)

        mc.setParent()
        mc.text(label = '' , height = self.spaceH02)
        mc.setParent()

        # 处理
        mc.textScrollList('sk_checkKeyScroll',e = 1,append = infoKey)

        mc.showWindow(UIName)

    # 信息转换  0 点击 | 1 搜索
    def checkKeyDetailsGoTo(self,checkType = 0):
        needInfos   = self.checkConfigHelpDict()
        infoKey     = needInfos[0]
        infoDetails = needInfos[1]
        noneInfo    = u'无匹配信息!!!'
        tempKey = []
        for checkInfo in infoKey:
            if u'【' in checkInfo:
                checkInfo = checkInfo.split(u'【')[-1]
            if u'】' in checkInfo:
                checkInfo = checkInfo.split(u'】')[0]
            tempKey.append(checkInfo)
        infoKey = tempKey
        if checkType == 0:
            keyInfo = mc.textScrollList('sk_checkKeyScroll',selectItem = 1, q= 1)[0]
        if checkType == 1:
            keyInfo = mc.textFieldButtonGrp('sk_checkKeyField',tx = 1, q= 1)
            if keyInfo[-1] == '\t':
                keyInfo = keyInfo.split('\t')[0]
            if keyInfo[-1] == ' ':
                keyInfo = keyInfo.split(' ')[0]
        if u'【' in keyInfo:
            keyInfo = keyInfo.split(u'【')[-1]
        if u'】' in keyInfo:
            keyInfo = keyInfo.split(u'】')[0]
        getResult = 0
        for checkInfo in infoKey:
            if keyInfo in checkInfo:
                indexNum = infoKey.index(keyInfo)
                getResult = infoDetails[indexNum]
        if not getResult:
            infoNeed = noneInfo
        else:
            infoNeed = getResult
        mc.scrollField('sk_checkDetailsField',e = 1, tx = infoNeed)

    # 数据录入
    def checkConfigHelpDict(self):
        infoKey     = []
        infoDetails = []
        # 错误
        infoKey.append(u'【 错 误 】')
        infoDetails.append(u'[文件名相关]\t文件名请遵循各环节规范,\n如  项目简写_assetID_高低模类型_环节类型\n[MODEL相关]\tMODEL组是所有用于渲染的物体存放的组，\n这个组每个asset必须有且只有一个，且命名必须是MODEL。\n[大组相关]\tasset的outliner里,大组（也叫总组）只能有一个。\n[参考存在]\tasset阶段，除了rg和某些set，是不允许有参考存在的。\n')
        # 【约束到物】      checkconstraintObjs
        infoKey.append(u'【约束到物】')
        infoDetails.append(u'[说明]角色道具做abc cache,尽量使用蒙皮;一定要用约束的话，请约束到物体自身级别')
        # 【空白Mesh】
        infoKey.append(u'【空白Mesh】')
        infoDetails.append(u'[说明]这个处理大纲里显示为空组，但实际上有mesh节点的情况。\n[解决]如果shape节点不需要，把和空transform节点连接的shape节点处理掉。\n若需要，视情况重做模型。')
        # 【namespace】
        infoKey.append(u'【namespace】')
        infoDetails.append(u'[说明]asset文件，除了设置、场景文件及特殊情况外，不得拥有namespace\n[解决]使用前期工具架的 namespace 工具处理掉不需要的namespace。')
        # 【非poly】       2
        infoKey.append(u'【非poly】')
        infoDetails.append(u'[说明]asset文件不得有细分及nurbs模型\n[解决]处理掉列出的非polygon的物体')
        # 【NaN数值】
        infoKey.append(u'【NaN数值】')
        infoDetails.append(u'[说明]对应物体的位移属性值有NaN\n[解决]一般是设置计算异常导致的,重新检查计算过程')
        # 【临时Shape】    checkIntermediateObjectError
        infoKey.append(u'【临时Shape】')
        infoDetails.append(u'[说明]模型阶段，不能有IntermediateObject。\n这个一般是蒙皮之后没删历史造成的。\n[解决]清除列出物体的不需要的shape。')
        # 【贴图路径】      checkFileTexture
        infoKey.append(u'【贴图路径】')
        infoDetails.append(u'[说明]若贴图文件指向的路径访问不了，则会列出来\n[解决]将贴图路径处理正确')
        # 【.tx错误】      checkArnoldTX
        infoKey.append(u'【.tx错误】')
        infoDetails.append(u'[说明]anorld渲染器项目,需要输出.tx文件\n若目录没有.tx或者.tx时间不匹配则报错')
        # 【渲染属性】      checkMeshRenderStates
        infoKey.append(u'【渲染属性】')
        infoDetails.append(u'[说明]MODEL组里的物体默认是用于被渲染的，\n若属于应该被渲染却没打开的，会列出来。\n一般是设置包裹变形默认设置会关闭renderstate\n[解决]若该物体确实要被渲染，请开启renderstate；\n若该物体不需要参与渲染，请在其自定义属性里加入_nr_或_si_即可进入豁免清单。')
        # 【三角面过多】
        infoKey.append(u'【三角面过多】')
        infoDetails.append(u'[说明]MODEL组里的物体，物体的三角面数量超过自身总面数的一定比例，则拦截下来。。\n一般为20%。\n[解决]改布线，成为合规范的布线。')
        # 【非四边形】
        infoKey.append(u'【非四边形】')
        infoDetails.append(u'[说明]MODEL组里的物体，布线要求允许三角形、四边形、五边形存在。\n尽量四边形。异常会列出。\n如果显示的是物体级别而不是face级别，\n请检查它是否有错误shape导致它的点线面无法正常获取.\n[解决]改布线，成为合规范的布线。')
        # 【蒙皮错误】      checkFaceVertexs
        infoKey.append(u'【蒙皮错误】')
        infoDetails.append(u'[说明]这些物体通常是蒙皮后源物体发生变化导致蒙皮信息错误,\n请检查它是否有错误shape导致它的点线面无法正常获取.\n[解决]重新蒙皮')
        # 【instance】
        infoKey.append(u'【instance】')
        infoDetails.append(u'[说明]asset文件，若无特殊需求，禁止使用instance\n[解决]用duplicate的方式复制物体，而不是instance')
        # 【SmoothSet】
        infoKey.append(u'【SmoothSet】')
        infoDetails.append(u'[说明]未发现正版SMOOTH_SET：\n正版smoothSet，是一个SmoothSet组下辖3个级别的smooth小组\n未发现有效SMOOTH物体：\n有smoothSet组，但都是空的\n[解决]重新用smoothSet工具打组')
        # 【Smooth漏掉】    checkModelSmoothSet
        infoKey.append(u'【Smooth漏掉】')
        infoDetails.append(u'[说明]有smoothSet组，但MODEL组用于渲染的物体，\n有漏掉没设置smooth级别的\n[解决]重新用smoothSet工具将其加入到正确的级别')
        # 【MODEL层级】
        infoKey.append(u'【MODEL层级】')
        infoDetails.append(u'[说明]设置专用检测,MODEL组下不得有非参考的物体或组\n[解决]请将多余的物体和组放到MODEL组外的组里')
        # 【节点重名】
        infoKey.append(u'【节点重名】')
        infoDetails.append(u'[说明]transform节点有相同名字的节点\n[解决]使用前期工具架的A_Re工具自动重命名重名物体')
        # 【shape重名】
        infoKey.append(u'【shape重名】')
        infoDetails.append(u'[说明]mesh节点里，有相同名字的节点\n[解决]使用前期工具架的A_Re工具自动重命名重名物体')
        # 【shape同名】
        infoKey.append(u'【shape同名】')
        infoDetails.append(u'[说明]transform和shape节点有相同名字的情况,\n即a|a,第一个a是物体名，第二个是shape节点\n[解决]改成a|aShape')
        # 【没有归零】      checkZeroMeshAttrs
        infoKey.append(u'【没有归零】')
        infoDetails.append(u'[说明]asset阶段，所有物体(除眼睛外)需要位移、旋转、缩放归零\n[解决]列出的物体一个个处理好\n若要保留数值,请在transform上添加_noZero_属性')
        # 【透明贴图连接】   透明贴图检测
        infoKey.append(u'【透明贴图连接】')
        infoDetails.append(u'[说明]透明贴图连接方式没通过检测\n[解决]所有透明贴图使用黑白贴图，使用outColor连接到对方通道')
        # 【父子Polyon】    checkPolyParents
        infoKey.append(u'【父子Polyon】')
        infoDetails.append(u'[说明]asset阶段，不允许有polygon下还有polygon\n[解决]在保留效果的情况下父子关系打断')
        # 【参考错误】
        infoKey.append(u'【参考错误】')
        infoDetails.append(u'[说明]tx的文件，参考对象应该是rnd文件\n[解决]请把参考指向msrnd的rnd文件')
        # 【无用表达式】    checkNoNeedExpression
        infoKey.append(u'【无用表达式】')
        infoDetails.append(u'[说明]存在没生效的表达式\n[解决]恢复作用或清理掉,看需求')
        # 【分层测试】      checkTextureModelShader
        infoKey.append(u'【分层测试】')
        infoDetails.append(u'[说明]这个测试是创建一个渲染层,\n然后加所有mesh进入并给个新的材质球,\n测试能否正常在渲染层内重新赋予材质\n[解决]出问题的有3种情况:\n其一是无法赋予材质,断开SG节点重新连接即可;\n其二是能赋予材质但分层赋予材质后材质丢失,\n这个需要选取所有物体,加选set组然后export再打开;\n其三是tx文件默认是lambert1的报错')
        # 【rg丢材质】
        infoKey.append(u'【rg丢材质】')
        infoDetails.append(u'[说明]检测rg文件参考mo文件后有多少丢失材质的物体,\n\n[解决]1.先用下面代码处理:\nfrom commonCore.core_mayaCommon import sk_backCmd\nreload(sk_backCmd)\nsk_backCmd.sk_backCmd().deformerAfterObjectSetMod()\n\n2.如果运行后还有物体,检查mo和rg对应物体的区别，修正shape\n或者给与线框物体正确材质')
        # 【pasted】
        infoKey.append(u'【pasted__】')
        infoDetails.append(u'[说明]检测文件名命名中有pasted__字段,复制出来的物体\nDouf项目新增\n\n[解决][目前]直接手动改名吧，少年!\n')
        # 【group】
        infoKey.append(u'【group】')
        infoDetails.append(u'[说明]检测文件名命名中有group字段,默认打组的产物\nDouf项目新增\n\n[解决][目前]直接手动改名吧，少年!\n')
        # 【显示层】
        infoKey.append(u'【显示层】')
        infoDetails.append(u'[说明]文件中存在的显示层,场景文件不检测\n\n[解决]1.直接手动删除吧，少年!\n2.from commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().checkCleanDisplayLayers()\n')
        # 【渲染层】
        infoKey.append(u'【渲染层】')
        infoDetails.append(u'[说明]文件中存在的渲染层\n\n[解决]1.直接手动删除吧，少年!\n2.from commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().checkCleanRenderLayers()\n')
        # 【动画层】
        infoKey.append(u'【动画层】')
        infoDetails.append(u'[说明]文件中存在的动画层\n\n[解决]1.直接手动删除吧，少年!\n2.from commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().().checkCleanAnimLayers()\n')
        # 【尺寸超标】      checkTextureFileSize
        infoKey.append(u'【尺寸超标】')
        infoDetails.append(u'[说明]这些列出的贴图都比项目指定的最大尺寸大\n\n[解决]问清楚项目贴图尺寸要求，改好吧\n')
        # 【选面物体】      checkFaceShaderDetails
        infoKey.append(u'【选面物体】')
        infoDetails.append(u'[说明]这些列出的物体用了face shader\n\n[解决]合并材质球，一个物体一个shader\n')
        # 【未缝合点】      checkErrorObjects('nonManifoldVertices')
        infoKey.append(u'【未缝合点】')
        infoDetails.append(u'[说明]坏点,坏边，坏面，未缝合点，请找到物体查看\n\n豁免请在物体级别加_plfIg_属性')
        # 【未缝合边】      checkErrorObjects('nonManifoldEdges')
        infoKey.append(u'【未缝合边】')
        infoDetails.append(u'[说明]坏点,坏边，坏面，未缝合点，请找到物体查看\n\n豁免请在物体级别加_plfIg_属性')
        # 【未缝合面】      checkErrorObjects('laminaFaces')
        infoKey.append(u'【未缝合面】')
        infoDetails.append(u'[说明]坏点,坏边，坏面，未缝合点，请找到物体查看\n\n豁免请在物体级别加_plfIg_属性')

        return [infoKey,infoDetails]

    #--------------------------------------------#
    # 检测豁免查询系列
    #--------------------------------------------#

    #-------------------------------#
    # 忽略坏点坏边坏面检测
    def checkErrorIgnoreState(self,projSimp,checkAssetID,ignoreState = 'errorEdgeIgnore'):
        serverPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(server=1,infoMode = 1,shotInfos = [projSimp,checkAssetID,'h']).split('EyeLight')[0]
        errorEdgeIgnoreFile = serverPath + ignoreState + '.txt'
        import os
        if not os.path.exists(errorEdgeIgnoreFile):
            return 0
        readInfos = sk_infoConfig.sk_infoConfig().checkFileRead(errorEdgeIgnoreFile)
        ignoreState = 0
        for num in range(len(readInfos)):
            if num == 0:
                continue
            if checkAssetID == readInfos[num]:
                ignoreState = 1
        return ignoreState


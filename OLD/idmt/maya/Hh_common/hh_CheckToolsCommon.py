# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
reload(sk_renderLayerCore)
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class csl_CheckCommon(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    # 窗口
    def csl_CheckUI(self):        
    # 窗口
        if mc.window('csl_CheckTollsWin', exists=True):
            mc.deleteUI('csl_CheckTollsWin')
        mc.window('csl_CheckTollsWin', title=u'顺溜文件检测工具',
                  width=320, height=350, sizeable=True)
         # 面板
        form = mc.formLayout()
         # 切换面板
        tabs = mc.tabLayout('csl_CheckTools',innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout(
            form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
         # 前期文件检测工具
        child1 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label='PreCheck',bgc=[0,0,0.0],borderStyle='in',cll=1)
        
        mc.rowColumnLayout(numberOfColumns=2)
        collection01 = mc.radioCollection()
        set01 = mc.checkBox('Precheck01',label='check01',visible=1,v=1,bgc=[0.13,0.15,0.25],height=30,width=130)
        mc.button(label=u'检测',bgc=[0,0,0.0],width=110,height=30,command='')
        mc.setParent('..')  
        
        mc.rowColumnLayout(numberOfColumns=2)
        collection02 = mc.radioCollection()
        set02 = mc.checkBox('Precheck02',label='check02',visible=1,v=1,bgc=[0.13,0.15,0.25],height=30,width=130)
        mc.button(label=u'检测',bgc=[0,0,0.0],width=110,height=30,command='')
        mc.setParent('..')  
        
        mc.rowColumnLayout(numberOfColumns=2)
        collection03 = mc.radioCollection()
        set03 = mc.checkBox('Precheck03',label='check03',visible=1,v=1,bgc=[0.13,0.15,0.25],height=30,width=130)
        mc.button(label=u'检测',bgc=[0,0,0.0],width=110,height=30,command='')
        mc.setParent('..')  
        
        mc.rowColumnLayout(numberOfColumns=2)
        collection04 = mc.radioCollection()
        set04 = mc.checkBox('Precheck04',label='check04',visible=1,v=1,bgc=[0.13,0.15,0.25],height=30,width=130)
        mc.button(label=u'检测',bgc=[0,0,0.0],width=110,height=30,command='')
        mc.setParent('..')  
        
        mc.rowColumnLayout(numberOfColumns=2)
        collection05 = mc.radioCollection()
        set05 = mc.checkBox('Precheck05',label='check05',visible=1,v=1,bgc=[0.13,0.15,0.25],height=30,width=130)
        mc.button(label=u'检测',bgc=[0,0,0.0],width=110,height=30,command='')
        mc.setParent('..')    
                    
        mc.setParent('..')
        
                
        mc.frameLayout(label=u'一键式检测工具',bgc=[0,0,0.0],borderStyle='in')
        #mc.rowColumnLayout(numberofColumns=2)
        mc.button(label=u'前期检测',width=170,height=30,bgc=[0,0,0.0],command='')
         
        mc.setParent('..')                
        mc.setParent('..')
         
        
         # 动画文件检测工具
        child2 = mc.columnLayout('anCheckC',adjustableColumn=True)
        mc.frameLayout('anCheckF',label='AnCheck',bgc=[0,0,0.0],borderStyle='in',cll=1)
        mc.rowColumnLayout(numberOfColumns=2)
        
        ancollection01=mc.radioCollection()
        anset01=mc.checkBox('ancheck01',label='check01',visible=1,v=1,bgc=[0.13,0.15,0.25],height=30,width=130)
        mc.button('anbu01',label=u'检测',bgc=[0,0,0.0],width=110,height=30,command='')
        
        ancollection02=mc.radioCollection()
        anset02=mc.checkBox('ancheck02',label='check02',visible=1,v=1,bgc=[0.13,0.15,0.25],height=30,width=130)
        mc.button('anCheckB',label=u'检测',bgc=[0,0,0.0],width=110,height=30,command='')
        mc.setParent('..')                
        mc.setParent('..')
        
                
        mc.frameLayout(label=u'一键式检测工具',bgc=[0,0,0.0],borderStyle='in')
        #mc.rowColumnLayout(numberofColumns=2)
        mc.button(label=u'动画检测',width=170,height=30,bgc=[0,0,0.0],command='')
         
        mc.setParent('..')                
        mc.setParent('..')
        #渲染文件检测工具
        child3 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label='RenderCheck',bgc=[0,0,0.0],borderStyle='in',cll=1)
        mc.rowColumnLayout(numberOfColumns=2)
        
        Rendercollection01=mc.radioCollection()
        Renderset01=mc.checkBox('Rendercheck01',label='check01',visible=1,v=1,bgc=[0.13,0.15,0.25],height=30,width=130)
        mc.button(label=u'检测',bgc=[0,0,0.0],width=110,height=30,command='')
        
        Rendercollection02=mc.radioCollection()
        Renderset02=mc.checkBox('Rendercheck02',label='check02',visible=1,v=1,bgc=[0.13,0.15,0.25],height=30,width=130)
        mc.button(label=u'检测',bgc=[0,0,0.0],width=110,height=30,command='') 
        mc.setParent('..')
        mc.setParent('..') 
        
        mc.frameLayout(label=u'一键式检测工具',bgc=[0,0,0.0],borderStyle='in')
        #mc.rowColumnLayout(numberOfColumns=2)
        mc.button(label=u'渲染检测',width=170,height=30,bgc=[0,0,0.0],command='')
         
        mc.setParent('..')                
        mc.setParent('..')
        
        
        mc.tabLayout(tabs, edit=True, tabLabel=((child1, u'前期检测工具'),(child2, u'动画检测工具'),(child3, u'渲染检测工具')))
        mc.showWindow('csl_CheckTollsWin')
 
    def csl_checkModelDetailsWarning(self,checkType = ''):
        infoWrong = []
        errorPrint = 0
        mo = 0
 
        # 创建ErrorSet
        self.checkErrorSetCreate()
 
        # 文件名检测，判断环节
        import sk_infoConfig
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
                                errorPrint = errorPrint + 1
            print '\n'
            
            # 对set类不检测
            if info[1][0] not in ['s', 'S']:
                # 检测namespace
                if checkType == '' or checkType == 'nsCheck':
                    namespace = mc.namespaceInfo(listOnlyNamespaces = 1)
                    if len(namespace) > 2:
                        infoWrong.append(u'【 错 误 】\t\t存在namespace，请清理掉！')
                        errorPrint = errorPrint + 1
                        
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
                    errorPrint = errorPrint + 1
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
                                errorPrint = errorPrint + 1
                    else:
                        infoWrong.append(u'【 错 误 】\t\t文件是空的！！')
                        errorPrint = errorPrint + 1

                print '\n'

                # 需要判断[mo]的MODEL的函数才能执行
                if checkType == '' or checkType == 'MSHCheck':
                    # 检测错误命名
                    errorNames = self.checkMSHName(mo)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【命名错误】\t\t%s' % (str(name)))
                            errorPrint = errorPrint + 1  
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
                                errorPrint = errorPrint + 1
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
                                errorPrint = errorPrint + 1
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
                                errorPrint = errorPrint + 1
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
                                errorPrint = errorPrint + 1
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
                                errorPrint = errorPrint + 1
                            mc.sets(errorNames , e=1 , addElement='Error_SignInfo')  
                        else:
                            mc.delete('Error_SignInfo')  
                    else:
                        mc.delete('Error_SignInfo')  
                
            else:
                print '\n'
                infoWrong.append(u'【 错 误 】\t\tMODEL组不存在！！')
                errorPrint = errorPrint + 1

            print '\n'

            # 对set类不检测
            if info[1][0] not in ['s', 'S']:
                # 检测重名错误
                if checkType == ''  or checkType == 'sameTransformCheck' :
                    errorNames = []
                    errorNamesTemp = self.checkSameName()
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            if '|MODEL|' in name:
                                errorNames.append(name)
                    passList = ['zm_p075001Rope101B']
                    if errorNames and (info[0] + '_' + info[1]) not in passList:
                        for name in errorNames:
                            infoWrong.append(u'【节点重名】\t\t%s' % (str(name)))
                            errorPrint = errorPrint + 1
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
                    passList = ['zm_p075001Rope101B']
                    if errorNames and (info[0] + '_' + info[1]) not in passList:
                        for name in errorNames:
                            infoWrong.append(u'【shape重名】\t\t%s' % (str(name)))
                            errorPrint = errorPrint + 1
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
                                errorPrint = errorPrint + 1
                            mc.sets(errorNames , e=1 , addElement='Error_SameShapeNode')  
                    else:
                        mc.delete('Error_SameShapeNode')                      
    
                print '\n'

            # 检测proxy属性信息
            if checkType == '' or checkType == 'proxyInfo':
                import sk_sceneConfig
                reload(sk_sceneConfig)
                errorNames = sk_sceneConfig.sk_sceneConfig().sk_sceneProxyInfoCheck(0)
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【proxy位移】\t\t%s' % (str(name)))
                        errorPrint = errorPrint + 1
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
                        errorPrint = errorPrint + 1

            # 检测SmoothSet
            # 只对model，tx，render进行检测
            if checkType == '' or checkType == 'smoothSet':
                import sk_smoothSet
                reload(sk_smoothSet)
                if info[3].split('.')[0] in ['mo','tx']:
                    if info[0] in ['zm']:
                        errorNames = self.checkModelSmoothSet(info[0])
                        if errorNames:
                            if errorNames == [u'未发现正版SMOOTH_SET']:
                                infoWrong.append(u'【SmoothSet】\t\tDidn\'t find SMOOTH_SET')
                                errorPrint = errorPrint + 1
                            if errorNames == [u'未发现有效SMOOTH物体']:
                                infoWrong.append(u'【SmoothSet】\t\tDidn\'t find Smooth Objects')
                                errorPrint = errorPrint + 1
                            if errorNames and errorNames != [u'未发现正版SMOOTH_SET'] and errorNames != [u'未发现有效SMOOTH物体']:
                                for name in errorNames:
                                    infoWrong.append(u'【Smmoth漏掉】\t\t%s' % (str(name)))
                                    errorPrint = errorPrint + 1
                                mc.sets(errorNames , e=1 , addElement='Error_SmoothLost')  
                        else:
                            mc.delete('Error_SmoothLost')

                if info[0] == 'zm':
                    # CacheSet
                    self.checkCacheSetAdd()
                    # AnimSet
                    self.checkTransAnimSetAdd()
                    import sk_sceneConfig
                    reload(sk_sceneConfig)
                    sk_sceneConfig.sk_sceneConfig().sk_sceneSetCombineConfig("ZM")
            
            # 检测参考有没有加载
            if checkType == '' or checkType == 'refCheck':
                import sk_referenceConfig
                reload(sk_referenceConfig)
                refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
                checkRef = 0
                if refInfos[0][0]:
                    for refNode in refInfos[0][0]:
                        isLoad = mc.referenceQuery(refNode,isLoaded = 1)
                        if not isLoad:
                            checkRef = 1
                if checkRef:
                    infoWrong.append(u'【Unload Reference】\t\t请加载所有参考！！！')
                    errorPrint = errorPrint + 1
        else:
            print '\n'
            infoWrong.append(u'【 错 误 】\t\t文件名错误！ ')
            errorPrint = errorPrint + 1
        # 删除ErrorSet
        if errorPrint == 0:
            try:
                mc.delete('ErrorTemp_Set')
            except:
                pass
        

        # 输出错误消息
        #print(unicode('=============================【文件中错误如下】=============================', 'utf8'))
        print(u'=============================【文件中错误如下】=============================')
        for info in infoWrong:
            #print(unicode('%s' % (str(info)), 'utf8'))
            print info
        #print(unicode('===========================【目前】共计【%s】处错误===========================' % (str(errorPrint)), 'utf8'))
        print(u'===========================【目前】共计【%s】处错误===========================' % (errorPrint))
        #mc.warning(unicode('===========================【目前】共计【%s】处错误===========================' % (str(errorPrint)), 'utf8'))
        mc.warning(u'===========================【目前】共计【%s】处错误===========================' % errorPrint)
        
        # 解锁
        self.checkUnlockMSHV()
        self.checkUnlockMSHGeo()
        
        return errorPrint 
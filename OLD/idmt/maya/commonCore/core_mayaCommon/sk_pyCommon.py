# -*- coding: utf-8 -*-

import sys,os
import maya.cmds as mc

class sk_pyCommon(object):
    def __init__(self):
        pass
    
    #------------------------------#
    # 【通用：锁lock/解锁unlock工具】
    # 对选取物体的下属子节点及其本身进行lock处理
    # Author : 沈  康
    # Data   : 2013_03_29
    # Data   : 2013_05_10 处理重名物体带来的问题。解锁和锁合并函数
    #------------------------------#
    def sk_lockObjs(self,typeNum):
        objs = mc.ls(sl = 1,l = 1)
        if not objs:
            mc.error(u'======请选取物体======')
            
        doNotLock = ['drawOverride','visibility','lodVisibility']
        lockAttrList = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz',]
        allObjs = mc.listRelatives(objs,ad =1,type ='transform',f = 1) + objs
        nurbsCurvs = mc.listRelatives(objs,ad =1,ni = 1,type ='nurbsCurve',f = 1)
        nurbsObjs  = mc.listRelatives(nurbsCurvs,p =1,type ='transform',f = 1)
        if not nurbsObjs:
            nurbsObjs = []
        
        for obj in allObjs:
            if obj in nurbsObjs:
                continue
            inr = mc.referenceQuery(obj,inr = 1)
            if inr:
                continue
            for attr in lockAttrList:
                checkAttr = obj + attr
                if typeNum == 1:
                    mc.setAttr(checkAttr,l=1)
                if typeNum == 0:
                    tempAttr = mc.connectionInfo(checkAttr,gla=1)
                    if tempAttr:
                        mc.setAttr(tempAttr,l=0)

    #------------------------------#
    # 【通用：bake约束工具】
    # 本函数只对非参考的约束有效
    # Author   : 沈  康
    # Data     : 2013_03_29
    #------------------------------#
    def sk_bakeConstraints(self):
        constraints = mc.ls(type='constraint')
        #�޳�ο���Լ��
        if  constraints:
            constraints = [x for x in constraints if not mc.referenceQuery(x,inr=1)]
            tobake= []
            if constraints:
                for constraint in constraints:
                    objs = mc.listHistory(constraint)
                    plugs = []
                    for obj in objs:
                        if mc.nodeType(obj) == "transform" or mc.nodeType(obj) == "joint":
                            plugs.append(obj)
                    plugs = list(set(plugs))
                    if not plugs:
                        continue
                        #mc.error(u'请检查文件是否存在没用的约束，如果有请删掉')
                    tobake+= [x for x in plugs if x != constraint]
                io = (mc.playbackOptions(q=1, minTime=1)-1, mc.playbackOptions(q=1, maxTime=1)+1)
                if not tobake:
                    return
                mc.bakeResults(tobake,	t=io,
                            simulation=1,
                            sampleBy=1,
                            disableImplicitControl=1,
                            preserveOutsideKeys=1,
                            sparseAnimCurveBake=1,
                            removeBakedAttributeFromLayer=0,
                            bakeOnOverrideLayer=0,
                            controlPoints=0,
                            shape=1)
                mc.delete(constraints)
                #print(unicode('===成功烘焙约束===',"gbk"))
                print(u'===成功烘焙约束===')
        else:
            #print(unicode('===没有约束存在===',"gbk"))
            print(u'===没有约束存在===')
    
    #------------------------------#
    # 【通用：路径动画bake工具】
    # 本函数只对非参考的路径动画有效
    # Author  : 沈  康
    # Data    : 2013_04_01
    #------------------------------#
    def sk_bakeMotionPaths(self):
        motionPaths = mc.ls(type='motionPath')
        if motionPaths:
            #剔除参考类动画曲线
            motionPaths = [x for x in motionPaths if not mc.referenceQuery(x,inr=1)]
            tobake= []
            for motionPath in motionPaths:
                objs = mc.listConnections(motionPath,destination = 1,type = 'transform')
                objs = list(set(objs))
                tobake+= [x for x in objs if x != motionPaths]    
            io = (mc.playbackOptions(q=1, minTime=1)-1, mc.playbackOptions(q=1, maxTime=1)+1)
        
            mc.bakeResults(tobake,	t=io,
        				simulation=1,
        				sampleBy=1,
        				disableImplicitControl=1,
        				preserveOutsideKeys=1,
        				sparseAnimCurveBake=1,
        				removeBakedAttributeFromLayer=0,
        				bakeOnOverrideLayer=0,
        				controlPoints=0,
        				shape=1)
            mc.delete(motionPaths)
            #print(unicode('===成功烘焙路径动画===',"gbk"))
            print(u'===成功烘焙路径动画===')
        else:
            #print(unicode('===没有路径动画===',"gbk"))
            print(u'===没有路径动画===')
    
    #------------------------------#
    # 【通用：maya路径转化工具】
    # 将maya专用'\'转化为'/'
    # 注意：                 path是数组
    # Author  : 沈  康
    # Data    : 2013_04_03
    #------------------------------#
    def sk_mayaPathConfig(self,path):
        for i in path:
            i = i.replace('\\','/')
            if i[0:2] == '//':
                a = i[0:2].replace('//','\\\\')
                i = a + i[2:]
                print i
    
    #------------------------------#
    # 【通用：空namespace清理工具】
    # 本函数只对非参考的namespace有效
    # Author  : 沈  康
    # Data    : 2013_04_07
    #------------------------------#
    def checkNamespaceCleanEmpty(self,configType = 1):
        # 设置之前必须清除当前默认前缀，最后还原回去
        preName = mc.namespaceInfo(currentNamespace=1)
        mc.namespace(set=':')
        namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        namespaces.remove('UI')
        namespaces.remove('shared')
        if namespaces :
            for name in namespaces:
                # 必须设置namespace才能返回当前默认set的信息
                mc.namespace(setNamespace=str(':' + name))
                # 1为处理空的namespace
                if configType == 1:
                    info = mc.namespaceInfo(listOnlyDependencyNodes=1, dagPath=1)
                    if info == None:
                        mc.namespace(set=':')
                        mc.namespace(removeNamespace=name)
                # 2为处理所有非参考namespace
                if configType == 2:
                    mc.namespace(set=':')
                    mc.namespace(force=1, moveNamespace =[name,':'])
                    mc.namespace(removeNamespace = name)
        mc.namespace(set=str(':' + preName))
    
    #------------------------------#
    # 【通用：删除指定非参考namespace的工具】
    # Author  : 沈  康
    # Data    : 2013_09_23
    #------------------------------#
    def sk_deleteNamespace(self,namespace):
        ns = namespace
        try:
            # 使得namespace成为空的namespace
            mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
            # 清理空namespace
            mc.namespace(removeNamespace= (':' + ns))
        except:
            pass
    
    #------------------------------#
    # 【通用：获取指定namespace的工具】
    # Author  : 沈  康
    # Data    : 2013_06_23
    #------------------------------#
    def sk_getNamespaceObjs(self,namespace):
        mc.namespace(setNamespace = (':' + namespace ))
        objs = mc.namespaceInfo(dagPath =1,ls = 1)
        mc.namespace(setNamespace = ':' )
        return objs
        
    
    #------------------------------#
    # 【通用：辨识模型部位重命名shader】
    # 通过读取set里的模型更改名字
    # Author  : 沈  康
    # Data    : 2013_04_27
    # Data    : 2013_07_01
    # 新增保留后缀，及保留ID
    #------------------------------#
    def sk_partShaderRename(self,proj = ''):
        # 获取所有set的有效
        # mc.select('MESHES')
        # meshNames = mc.ls(sl = 1)
        
        # SHD_ + bodyPart + assetName + shaderType
        
        # 特殊处理项目
        special_01 = ['ZoomWhiteDolphin','Calimero']
        
        # 特殊字符
        special_add = ''
        
        # 获取ID
        import sk_infoConfig
        reload(sk_infoConfig)
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        # 获取MODEL下的mesh
        model = mc.ls('MODEL')
        if model:
            objs = mc.listRelatives('MODEL',ad=1,f=1,type = 'transform')
            errorNames = []
            doNotNeedCheck = ['Master','World']
            for obj in objs:
                if '_' in obj:
                    # 排除非mesh
                    if mc.listRelatives(obj,s=1,ni=1,type = 'mesh'):
                        if len(obj.split('_')) < 4:
                            errorNames.append(obj)
                else:
                    if obj.split('|')[-1] not in doNotNeedCheck:
                        errorNames.append(obj)
            if errorNames == []:
                meshNames = []
                for obj in objs:
                    shape = mc.listRelatives(obj,s=1,ni=1,type = 'mesh',f = 1)
                    if shape:
                        meshNames.append(obj)
                if meshNames:
                    for meshName in meshNames:
                        #获取shape名
                        #mc.select(meshName)
                        mesh_c = mc.listRelatives(meshName , c = 1 ,s = 1 ,ni=1,type = 'mesh',f= 1)[0]
                        #获取连接的SG节点
                        SGInfo = list(set(mc.listConnections(mesh_c,destination = 1,type = 'shadingEngine')))
                        try:
                            SGInfo.remove('initialShadingGroup')
                        except:
                            pass
                        for i in range(len(SGInfo)):    
                            #获取shader节点并改名shader及SG
                            tex_cInfo = mc.connectionInfo((SGInfo[i] + '.surfaceShader'),sourceFromDestination = 1)
                            texInfo = tex_cInfo.split('.')[0]
                            if proj in special_01:
                                special_add = info[1] + '_' + texInfo.split('_')[-1]
                            texName = 'SHD_' +  mesh_c.split('_')[3] + '_' + special_add
                            SGName = 'SHD_' +  mesh_c.split('_')[3] + '_' + special_add + '_' + 'SG'
                            print texInfo
                            mc.rename(texInfo,texName)
                            mc.rename(SGInfo[i],SGName)
                    # 处理file节点名字
                    self.sk_fileNodeBodyRename()
                    mc.select(cl = 1)
                    print u'============材质们成功重命名============'
                else:
                    #print(unicode('======未发现mesh存在======',"utf8"))
                    print(u'======未发现mesh存在======')
            else:
                mc.warning(u'============以下命名不规范============')
                for error in errorNames:
                    mc.warning(error)
                mc.warning(u'===========最少要有3个下斜杠===========')            
        else:
            #print(unicode('======未发现MODEL======',"utf8"))
            print(u'======未发现MODEL======')
            
    #------------------------------#
    def sk_fileNodeBodyRename(self):
        fileNodes = mc.ls(type ='file')
        for fileNode in fileNodes:
            path = mc.getAttr((fileNode + '.fileTextureName'))
            newInfo = path.split('/')[-1]
            newName = 'SHD_file_' + newInfo[0] + '_' + newInfo[1]
            mc.rename(fileNode,newName)
    
    #------------------------------#
    # 【通用：显示/隐藏表情面板控制器】
    # Author  : 沈  康
    # Data    : 2013_07_08
    #------------------------------#
    def sk_animFrameVChange(self,pro = 'Calimero'):
        projectTypeA = ['Calimero','ZoomWhiteDolphin']
        projectTypeB = ['']
        if pro in projectTypeA:
            ctrls = mc.ls('*_CTRL_FRAME_GRP',type = 'transform')
            # 处理带namespace的
            if ctrls == []:
                ctrls = mc.ls('*:*_CTRL_FRAME_GRP',type = 'transform')
            if ctrls:
                type = mc.getAttr(ctrls[0]+'.v')
                for ctrl in ctrls:
                    if type == 1:
                        mc.setAttr((ctrl+'.v'),0)
                    else:
                        mc.setAttr((ctrl+'.v'),1)
                        
    #------------------------------#
    # 【通用：统一处理所有约束】
    # Author  : 沈  康
    # Data    : 2013_11_21
    #------------------------------#   
    # 0 全部 |1 点约束 | 2 朝向约束 | 3 父子约束 | 4 旋转约束 | 5 缩放约束
    # 临时改变模式
    def sk_constraintsOnOffConfig(self,on = 0,fixType = 0 ):
        # 获取约束
        allConstraints = []
        if fixType == 0:
            allConstraints = mc.ls(type = 'pointConstraint') + mc.ls(type = 'aimConstraint') + mc.ls(type = 'orientConstraint') + mc.ls(type = 'parentConstraint') + mc.ls(type = 'scaleConstraint')
        if fixType == 1:
            allConstraints = mc.ls(type = 'pointConstraint')
        if fixType == 2:
            allConstraints = mc.ls(type = 'aimConstraint')
        if fixType == 3:
            allConstraints = mc.ls(type = 'parentConstraint')
        if fixType == 4:
            allConstraints = mc.ls(type = 'orientConstraint')
        if fixType == 4:
            allConstraints = mc.ls(type = 'scaleConstraint')
        if allConstraints:
            for constraint in allConstraints:
                # 对于参考的不处理
                refCheck = mc.referenceQuery(constraint,isNodeReferenced = 1)
                if refCheck:
                    pass
                else:
                    # 获取约束的开关属性
                    # 末尾2个字符是"W0"
                    attrs = mc.listAttr(constraint , settable = 1)
                    if attrs:
                        for attr in attrs:
                            if attr[-2:] == 'W0':
                                # 开始处理开关属性
                                if mc.getAttr((constraint + '.' + attr),l=1):
                                    pass
                                else:
                                    # 对于有属性连接的，pass
                                    try:
                                        mc.setAttr((constraint + '.' + attr),on)
                                    except:
                                        pass

    #------------------------------#
    # 【通用，对list实现乱序功能，lenList必须大于1】
    #------------------------------#      
    def checkRandomList(self,sourceList):
        if len(sourceList) > 1:
            import random
            tempList = sourceList[:]
            indexNum = len(tempList)
            needList = []
            for i in range(indexNum):
                tempIndex = int(random.uniform(1,indexNum))-1
                needList.append(tempList[tempIndex])
                tempList.remove(tempList[tempIndex])
                indexNum = indexNum - 1
            return needList
        
        
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
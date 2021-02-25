# -*- coding: utf-8 -*-
# 【通用】【FinalLayout 共同调用的功能】
#  Author : 沈康
#  Data   : 2014_08

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_baseCommon import sk_infoCore
reload(sk_infoCore)

class sk_animCurveCore(object):
    
    def __init__(self):
        self.ppType = 'GDC'

    #----------------------------------------------------------------------------------------------#

    #------------------------------#
    # 【核心】【动画数据导入导出PYTHON版】
    # 0.动画
    # Author : 沈  康
    # 参考          : 万寿龙
    # Data   : 2013_05_24 - 2013_05_28
    #------------------------------#   
    # 导出信息
    # 增加上传服务器功能
    def checkAnimCurveInfoExport(self, objs, serverFile = 1, infoFile='anim' , targetPath = '' , shotType = sk_infoConfig.sk_infoConfig().checkShotType(),frameRange = []):
        # 前提基本信息
        AnimsInfo = []
        AnimsInfo.append('ImportExportAnimationForSets v 1.5   (Author: shenkang)')
        # 版本号 + # 帧范围
        frameMin = int(mc.playbackOptions(min=1,q=1))
        frameMax = int(mc.playbackOptions(max=1,q=1))
        AnimsInfo.append('mayaVersion  ' + mc.about(v=1) + ';' + 'frameRange  %s-%s;'%(str(frameMin),str(frameMax)))
        # 单位类型
        AnimsInfo.append('linearUnit  ' + mc.currentUnit(q=1, f=1, l=1) + ';')
        # 角度单位，弧度还是角度
        AnimsInfo.append('angularUnit  ' + mc.currentUnit(q=1, f=1, a=1) + ';')
        # 制式，PAL等
        AnimsInfo.append('timeUnit  ' + mc.currentUnit(q=1, f=1, t=1) + ';')
        # frameRangeCheck
        frameRangeCheck = 0
        if len(frameRange) == 2:
            frameRangeCheck = 1
        # 获取objs
        if objs:
            for obj in objs:
                # 通道盒子里能被K帧的属性
                keys = mc.listAttr(obj, k=1)
                # 通道盒子中无法被K帧的属性
                noKeys = mc.listAttr(obj, cb=1)
                if not keys:
                    continue
                if noKeys:
                    allAttr = keys + noKeys
                else:
                    allAttr = keys
                if allAttr:
                    for attr in allAttr:
                        animCurve = []
                        if mc.objExists(obj + '.' + attr):
                            # 获取属性的动画曲线
                            animCurve = mc.listConnections((obj + '.' + attr), s=1, d=0)
                        # 剔除无法K帧的情况
                        if animCurve:
                            # 判断是否存在及是否animCurve
                            if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                AnimsInfo.append('anim ' + obj + '.' + attr + '\n{')
                                # 更新信息
                                infoAll = self.checkAnimCurveInfoGet(animCurve[0],frameRangeCheck,frameRange)  
                                for info in infoAll:
                                    AnimsInfo.append(info)
                                AnimsInfo.append('}')
                        else:
                            # 无动画的信息
                            if mc.objExists(obj + '.' + attr):
                                if 'double3' not in mc.getAttr((obj + '.' + attr), type=1) :
                                    value = mc.getAttr(obj + '.' + attr)
                                    AnimsInfo.append('non-anim ' + obj + '.' + attr + ' ' + str(value) + ';')
                # 对曲线K点的处理
                expShapes = mc.listHistory(obj)
                # 显示控制点的判断
                if expShapes and mc.objectType(expShapes[0], isType='nurbsCurve') and mc.getAttr(expShapes[0] + '.dispCV'):
                    pointNum = mc.getAttr(expShapes[0] + '.spans')
                    # 此处和原脚本不一样
                    for j in range(pointNum * 2):
                        if mc.objExists(expShapes[0] + '.cv[' + str(j) + ']'):
                            allAttr = mc.listAttr((expShapes[0] + '.cv[' + str(j) + ']'), k=1)
                            if not allAttr:
                                continue
                            for attr in allAttr:
                                animCurve = mc.listConnections((expShapes[0] + '.' + attr), type='animCurve', s=1, d=0)
                                if animCurve:
                                    if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                        AnimsInfo.append('anim ' + expShapes[0] + '.' + attr + '\n{') 
                                        # 更新信息
                                        infoAll = self.checkAnimCurveInfoGet(animCurve[0],frameRangeCheck,frameRange)
                                        for info in infoAll:
                                            AnimsInfo.append(info)
                                        AnimsInfo.append('}')
                                else:
                                    # 无动画的信息，不过对于点来说基本用不到
                                    if 'double3' not in mc.getAttr((expShapes[0] + '.' + attr), type=1) :             
                                        value = mc.getAttr(expShapes[0] + '.' + attr)
                                        AnimsInfo.append('non-anim ' + expShapes[0] + '.' + attr + ' ' + str(value) + ';')
        # fsMode，指定输出地址
        if targetPath == '':
            # 本地输出
            print '-----001'
            # shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType)
            mc.sysFile(localPathAnim, makeDir=True)
            print '-----0011'
            sk_infoConfig.sk_infoConfig().checkFileWrite((localPathAnim + infoFile + '.sla'), AnimsInfo)
            # 本地输出object信息
            personalObjsFile = localPathAnim + infoFile + '_objs.txt'
            if serverFile == 1:
                # 上传服务器
                self.checkAnimInfoUpdate(infoFile,shotType)
        else:
            print '-----002'
            # 自定义输出地址
            sk_infoConfig.sk_infoConfig().checkFileWrite( (targetPath + infoFile + '.sla') , AnimsInfo)
            # 本地输出object信息
            print '-----0022'
            personalObjsFile = targetPath + infoFile + '_objs.txt'
            sk_infoConfig.sk_infoConfig().checkFileWrite(personalObjsFile, objs)

    #------------------------------#   
    # 动画信息更新到服务器
    def checkAnimInfoUpdate(self, infoFile , shotType = sk_infoConfig.sk_infoConfig().checkShotType()):
        import os
        # 本地路径转mel用
        localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType).replace('\\', '/')
        # 服务器端路径转mel用
        serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType).replace('\\', '/')
        # 开始上传
        fileInfo = infoFile + '.sla'
        # -----需要服务器端账号
        if self.ppType == 'GDC':
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
            mel.eval(updateAnimCMD)
        fileInfo = infoFile + '_objs.txt'
        # -----需要服务器端账号
        if self.ppType == 'GDC':
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
            mel.eval(updateAnimCMD)
        fileInfo = infoFile + '_Lobjs.txt'
        if os.path.exists(localPathAnim + fileInfo):
            # -----需要服务器端账号
            if self.ppType == 'GDC':
                updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
                mel.eval(updateAnimCMD)
        print '-------'
        print serverPathAnim
        
    #------------------------------#           
    # 模块：记录功能
    def checkAnimCurveInfoGet(self, animCurve,frameRangeCheck = 0,frameRange = []):
        #print '-----------------'
        #print animCurve
        # 帧的时间值
        time = mc.keyframe(animCurve, q=1, tc=1)
        #print time
        # 帧的属性值
        value = mc.keyframe(animCurve, q=1, vc=1)
        # 切线 类型
        inputType = mc.keyTangent(animCurve, q=1, itt=1)
        outputType = mc.keyTangent(animCurve, q=1, ott=1)
        # 切线角度
        inputAngle = mc.keyTangent(animCurve, q=1, ia=1)
        outputAngle = mc.keyTangent(animCurve, q=1, oa=1)
        # 权重
        inputWeight = mc.keyTangent(animCurve, q=1, iw=1)
        outputWeight = mc.keyTangent(animCurve, q=1, ow=1)
        # 锁与否
        # lockType = mc.keyTangent(animCurve, q= 1, l=1)
        weightLock = mc.keyTangent(animCurve, q=1, wl=1)
        
        infoW = ''
        infoAll = []
        if time:
            for i in range(len(time)):
                if frameRangeCheck:
                    frameCheck = time[i]
                    frameMin = frameRange[0]
                    frameMax = frameRange[1]
                    if frameCheck > frameMax or frameCheck < frameMin:
                        continue
                # time  value  inputType   outputType weightLock
                infoW = (' ' + str(time[i]) + ' ' + str(value[i]) + ' ' + str(inputType[i]) + ' ' + str(outputType[i]) + ' ' + str(weightLock[i])) 
                specialFix = ['fixed']
                # 特殊情况补充行
                if (inputType[i] in specialFix or outputType[i] in specialFix) and weightLock[i]:
                    infoW = infoW + (' ' + str(inputAngle[i]) + ' ' + str(outputAngle[i]))
                else:
                    if (inputType[i] in specialFix  or outputType[i] in specialFix)  and weightLock[i] != 'True':
                        infoW = infoW + (' ' + str(inputAngle[i]) + ' ' + str(inputWeight[i]) + ' ' + str(outputAngle[i]) + ' ' + str(outputWeight[i]))
                infoAll.append(infoW + ';')
        return infoAll

    #------------------------------#   
    # 导入信息
    # 加入从服务器端读取功能
    def checkAnimCurveInfoImport(self, serverFile=1, infoFile='anim' , replace = [] ,targetPath = '' ,offset = 0 ,breakMode = 1, shotType = sk_infoConfig.sk_infoConfig().checkShotType(), replaceObjs = [],missStop = 1,rootParentGrp = '',simpleGrpMode = 0,doNotAttrs = []):
        # 考虑下清理动画
        # 错误信息
        errorInfo = []
        # fsMode，指定路径读取
        if targetPath == '':
            # 本地获取
            if serverFile == 1:
                serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType)
                personalAmimFile = serverPathAnim + infoFile + '.sla'
                personalObjFile = serverPathAnim + infoFile + '_objs.txt'
            else:
                localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType)
                personalAmimFile = localPathAnim + infoFile + '.sla'
                personalObjFile = localPathAnim + infoFile + '_objs.txt'
        else:
            # 自定义读取路径
            personalAmimFile = targetPath + infoFile + '.sla'
            personalObjFile = targetPath + infoFile + '_objs.txt'
        # 动画信息
        AnimsInfo = sk_infoConfig.sk_infoConfig().checkFileRead(personalAmimFile)
        # 获取objct信息，检测obj
        someMode = 0
        if replaceObjs:
            nsObjs = replaceObjs
            someMode = 1
        else:
            nsObjs = sk_infoConfig.sk_infoConfig().checkFileRead(personalObjFile)
        print '--------'
        print personalObjFile
        print len(nsObjs)
        print replace
        # 对物体有效性进行处理
        if nsObjs:
            checkNoneName = []
            for obj in nsObjs:
                # 替换物处理
                if replace:
                    obj = obj.replace(replace[0],replace[1])
                    if infoFile == 'proxy':
                        # master传proxy
                        if 'MSH_c_hi_proxy' not in replace[0]:
                            obj = obj + '_'
                        # proxy传master
                        if 'MSH_c_hi_proxy' in replace[0]:
                            obj = obj[0:-1]
                obj = rootParentGrp + obj
                exist = mc.objExists(obj)
                if exist != True:
                    if simpleGrpMode:
                        obj = obj.split('|')[-1]
                    else:
                        checkNoneName.append(obj)
            # 无错误
            if not missStop or checkNoneName == []:
                print '------'
                print missStop
                linesInfo = len(AnimsInfo)
                if linesInfo > 5:
                    # 预设置
                    aniID = []
                    nonAnimID = []
                    # 帧范围
                    frameInfos = AnimsInfo[1].split(';')[1].split(' ')[-1].split('-')
                    frameRange = [int(frameInfos[0]),int(frameInfos[1])]
                    # 单位
                    # linear = mc.currentUnit(q=1, f=1, l=1) 
                    linearSla = AnimsInfo[2].split(' ')[2][0:-1]
                    mc.currentUnit(linear=linearSla) 
                    # 角度
                    # anglular = mc.currentUnit(q=1, f=1, a=1)
                    anglularSla = AnimsInfo[3].split(' ')[2][0:-1]
                    mc.currentUnit(angle=anglularSla) 
                    # 制式
                    # timeType = mc.currentUnit(q=1, f=1, t=1)
                    timeTypeSla = AnimsInfo[4].split(' ')[2][0:-1]
                    mc.currentUnit(time=timeTypeSla) 
                    # 处理不对信息
                    for i in range(5, linesInfo):
                        # 去掉回车符
                        lineInfo = AnimsInfo[i][0:-1]
                        # 取anim行数信息
                        # maya的python中没有startsWith，换个方法
                        if 'anim ' in lineInfo and 'non-anim' not in lineInfo:
                            aniID.append(i)
                        if 'non-anim'  in lineInfo:
                            nonAnimID.append(i)
                    # 处理anim信息
                    for aid in aniID:
                        lineInfo = AnimsInfo[aid][0:-1]
                        # 获取属性
                        attr = lineInfo.split('.')[-1]
                        # 物体名处理
                        objCtrl = lineInfo.split('.')[0].split(' ')[-1]
                        # 在选取模式排除无用
                        if someMode and objCtrl not in nsObjs:
                            continue
                        # 排除不要的属性
                        if attr in doNotAttrs:
                            continue
                        # 替换
                        if replace:
                            objCtrl = objCtrl.replace(replace[0],replace[1])
                            if infoFile == 'proxy':
                                # master传proxy
                                if 'MSH_c_hi_proxy' not in replace[0]:
                                    objCtrl = objCtrl + '_'
                                # proxy传master
                                if 'MSH_c_hi_proxy' in replace[0]:
                                    objCtrl = objCtrl[0:-1]
                        objCtrl = rootParentGrp + objCtrl
                        key = ''
                        if 'Shape' not in objCtrl:
                            key = objCtrl + '.' + attr
                        else:
                            ctrolPoint = lineInfo.split('.')[-2]
                            key = objCtrl + '.' + ctrolPoint + '.' + attr
                        # 处理不同角色之间
                        if simpleGrpMode:
                            if not mc.ls(key):
                                key = key.split('|')[-1]
                            if not mc.ls(key):
                                continue
                        # key要存在，且只有一个，且可K帧，且没被锁
                        if len(mc.ls(key)) == 1 and mc.getAttr(key, keyable=True) and mc.getAttr(key, l=1) != 1:
                            # 处理存在的动画曲线
                            existAnim = mc.listConnections(key, s=1, d=0)
                            if existAnim and breakMode:
                                mc.delete(existAnim)
                            # 获取{}内数据
                            for j in range(1, linesInfo):
                                nextLine = AnimsInfo[aid + j ]
                                if (nextLine != '}') :
                                    if (nextLine != '{'):
                                        # 开始获取属性数据
                                        infoDetails = nextLine.split(' ')
                                        # time
                                        keyFrame = float(infoDetails[1]) + offset
                                        # value
                                        keyValue = float(infoDetails[2])
                                        # in & out
                                        keyInput = infoDetails[3]
                                        keyOutput = infoDetails[4]
                                        # weight
                                        infoWeightLock = infoDetails[5]
                                        if infoWeightLock == 'True' and (infoDetails[3] == 'fixed' or infoDetails[4] == 'fixed'):
                                            # in & out angle
                                            keyInputAngle = float(infoDetails[6])
                                            if ';' in infoDetails[7]:
                                                infoDetails[7] = infoDetails[7][0:-1]
                                            keyOutputAngle = float(infoDetails[7])
                                            # 还原帧
                                            mc.setKeyframe(key, t=keyFrame , v=keyValue)
                                            mc.selectKey(key, k=keyFrame, r=1)
                                            mc.keyTangent(e=1, ia=keyInputAngle, iw=1, oa=keyOutputAngle, ow=1)
                                        else:
                                            if infoWeightLock != 'True' and (infoDetails[3] == 'fixed' or infoDetails[4] == 'fixed'):
                                                # in & out angle and weight
                                                keyInputAngle = float(infoDetails[6])
                                                keyInputWeight = float(infoDetails[7])
                                                keyOutputAngle = float(infoDetails[8])
                                                if ';' in infoDetails[9]:
                                                    infoDetails[9] = infoDetails[9][0:-1]
                                                keyOutputWeight = float(infoDetails[9])
                                                # 还原帧
                                                mc.setKeyframe(key, t=keyFrame , v=keyValue)
                                                mc.selectKey(key, k=keyFrame, r=1)
                                                mc.keyTangent(e=1, ia=keyInputAngle, iw=keyInputWeight, oa=keyOutputAngle, ow=keyOutputWeight)
                                            else:
                                                mc.setKeyframe(key, t=keyFrame , v=keyValue, itt=keyInput, ott=keyOutput)
                                else:       
                                    break
                        else:
                            # 如果可以设置值,设置为第一帧状态
                            if mc.getAttr(key, settable=1):
                                for j in range(1, linesInfo):
                                    nextLine = AnimsInfo[aid + j ]
                                    if (nextLine == '}') :
                                        break
                                    if (nextLine == '{') :
                                        continue
                                    # 开始获取属性数据
                                    infoDetails = nextLine.split(' ')
                                    # value
                                    keyValue = float(infoDetails[2])
                                    mc.setAttr(key,keyValue)
                                    break
                            else:
                                errorInfo.append(sk_infoCore.sk_infoCore().sk_infoCore(74))
                                errorInfo.append('-------------%s'%key)
                    # 处理non-anim信息
                    for nid in nonAnimID:
                        # 获取属性
                        key = AnimsInfo[nid].split(' ')[1]
                        # 替换
                        if replace:
                            key = key.replace(replace[0],replace[1])
                            if infoFile == 'proxy':
                                # master传proxy
                                if 'MSH_c_hi_proxy' not in replace[0]:
                                    key = key + '_'
                                # proxy传master
                                if 'MSH_c_hi_proxy' in replace[0]:
                                    key = key[0:-1]
                        # key要存在，且只有一个，且可K帧，且没被锁
                        # 锁住后无法处理
                        # valueType 1,浮点数 | 0 字符串
                        valueType = 1
                        if len(mc.ls(key)) == 1 and mc.getAttr(key, k=1) and mc.getAttr(key, settable=1) and mc.getAttr(key, l=1) != 1:
                            # 处理存在的动画曲线
                            existAnim = mc.listConnections(key, s=1, d=0)
                            if existAnim and breakMode:
                                mc.delete(existAnim)
                            # 获取属性数据
                            value = AnimsInfo[nid].split(' ')[2][0:-1]
                            if value == 'True':
                                value = float(1.0)
                            if value == 'False':
                                value = float(0.0)
                            if value != 'True' and value != 'False':
                                try:
                                    value = float(value)
                                except:
                                    valueType = 0
                                    value = str(value)
                            if valueType:
                                mc.setAttr(key, value)
                            else:
                                mc.setAttr(key, value,type = 'string')
                else:  
                    errorInfo.append(sk_infoCore.sk_infoCore().sk_infoCore(73))
            # 丢失物体
            else:
                for error in checkNoneName:
                    errorInfo.append(u'-------------No object:[%s]-------------' % (error))
                    errorInfo.append(sk_infoCore.sk_infoCore().sk_infoCore(73))
            for i in errorInfo:
                print(i)
            return checkNoneName

    # 清理时间轴外的动画曲线
    def checkAnimCleanNoneTimeRange(self,animCurves):
        frameMin = mc.playbackOptions(min = 1,q=1)
        frameMax = mc.playbackOptions(max = 1,q=1)
        # 卡帧
        frameNow = mc.currentTime(q=1)
        mc.currentTime(frameMin-1)
        mc.setKeyframe(animCurves)
        mc.currentTime(frameMax)
        mc.setKeyframe(animCurves)
        mc.currentTime(frameNow)
        #checkObjs = mc.listConnections(animCurves,s=0,d=1)
        for animCurve in animCurves:
            timeInfos = mc.keyframe(animCurve, q=1, tc=1)
            objsInfos = mc.listConnections(animCurve,s=0,d=1,plugs=1)
            if not objsInfos:
                continue
            obj = objsInfos[0].split('.')[0]
            attr = objsInfos[0].split('.')[-1]
            for frame in timeInfos:
                if frame >= frameMin-1 and frame <= frameMax+1:
                    continue
                mc.cutKey(obj,attribute = attr,option="keys",time = (frame,frame))
                
    # 清理选中曲线的多余曲线            
    def checkCleanSelAnimCurvs(self):
        objs = mc.ls(sl=1,l=1)
        if not objs:
            return 
        # 卡帧
        frameMin = mc.playbackOptions(min = 1,q=1)
        frameMax = mc.playbackOptions(max = 1,q=1)
        mc.currentTime(frameMin)
        mc.setKeyframe(objs)
        mc.currentTime(frameMax)
        mc.setKeyframe(objs)
        # 处理
        animCurvs = mc.listConnections(objs,s=1,d=0,type = 'animCurve')
        if not animCurvs:
            return
        needAnims = []
        for anim in animCurvs:
            refState = mc.referenceQuery(anim,inr = 1)
            if refState:
                continue
            needAnims.append(anim)
        if not needAnims:
            return
        self.checkAnimCleanNoneTimeRange(needAnims)

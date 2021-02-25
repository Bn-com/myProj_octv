# -*- coding: utf-8 -*-
# 【通用】【FinalLayout 共同调用的功能】
#  Author : 沈康
#  Data   : 2014_08

import maya.cmds as mc
import maya.mel as mel
import os

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
    def checkAnimCurveInfoExport(self, objs, serverFile = 1, infoFile='anim' , targetPath = '' ,frameRange = []):
        AnimsInfo = []
        AnimsInfo.append('ImportExportAnimationForSets v 1.5   (Author: shenkang)')
        frameMin = int(mc.playbackOptions(min=1,q=1))
        frameMax = int(mc.playbackOptions(max=1,q=1))
        AnimsInfo.append('mayaVersion  ' + mc.about(v=1) + ';' + 'frameRange  %s-%s;'%(str(frameMin),str(frameMax)))
        AnimsInfo.append('linearUnit  ' + mc.currentUnit(q=1, f=1, l=1) + ';')
        AnimsInfo.append('angularUnit  ' + mc.currentUnit(q=1, f=1, a=1) + ';')
        AnimsInfo.append('timeUnit  ' + mc.currentUnit(q=1, f=1, t=1) + ';')
        frameRangeCheck = 0
        if len(frameRange) == 2:
            frameRangeCheck = 1
        if objs:
            for obj in objs:
                keys = mc.listAttr(obj, k=1)
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
                            animCurve = mc.listConnections((obj + '.' + attr), s=1, d=0)
                        if animCurve:
                            if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                AnimsInfo.append('anim ' + obj + '.' + attr + '\n{')
                                infoAll = self.checkAnimCurveInfoGet(animCurve[0],frameRangeCheck,frameRange)
                                for info in infoAll:
                                    AnimsInfo.append(info)
                                AnimsInfo.append('}')
                        else:
                            if mc.objExists(obj + '.' + attr):
                                if 'double3' not in mc.getAttr((obj + '.' + attr), type=1) :
                                    value = mc.getAttr(obj + '.' + attr)
                                    AnimsInfo.append('non-anim ' + obj + '.' + attr + ' ' + str(value) + ';')
                if 'motionTrain' in obj:
                    continue
                '''
                expShapes = mc.listHistory(obj)
                if expShapes and mc.objectType(expShapes[0], isType='nurbsCurve') and mc.getAttr(expShapes[0] + '.dispCV'):
                    pointNum = mc.getAttr(expShapes[0] + '.spans')
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
                                        infoAll = self.checkAnimCurveInfoGet(animCurve[0],frameRangeCheck,frameRange)
                                        for info in infoAll:
                                            AnimsInfo.append(info)
                                        AnimsInfo.append('}')
                                else:
                                    if 'double3' not in mc.getAttr((expShapes[0] + '.' + attr), type=1) :
                                        value = mc.getAttr(expShapes[0] + '.' + attr)
                                        AnimsInfo.append('non-anim ' + expShapes[0] + '.' + attr + ' ' + str(value) + ';')
                '''
        if targetPath == '':
            localPathAnim = self.checkAnimLocalPath()
            mc.sysFile(localPathAnim, makeDir=True)
            self.checkFileWrite((localPathAnim + infoFile + '.sla'), AnimsInfo)
            personalObjsFile = localPathAnim + infoFile + '_objs.txt'
        else:
            self.checkFileWrite( (targetPath + infoFile + '.sla') , AnimsInfo)
            personalObjsFile = targetPath + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)

    def checkAnimCurveInfoGet(self, animCurve,frameRangeCheck = 0,frameRange = []):
        time = mc.keyframe(animCurve, q=1, tc=1)
        value = mc.keyframe(animCurve, q=1, vc=1)
        inputType = mc.keyTangent(animCurve, q=1, itt=1)
        outputType = mc.keyTangent(animCurve, q=1, ott=1)
        inputAngle = mc.keyTangent(animCurve, q=1, ia=1)
        outputAngle = mc.keyTangent(animCurve, q=1, oa=1)
        inputWeight = mc.keyTangent(animCurve, q=1, iw=1)
        outputWeight = mc.keyTangent(animCurve, q=1, ow=1)
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
                infoW = (' ' + str(time[i]) + ' ' + str(value[i]) + ' ' + str(inputType[i]) + ' ' + str(outputType[i]) + ' ' + str(weightLock[i]))
                specialFix = ['fixed']
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
    def checkAnimCurveInfoImport(self, infoFile='anim' , replace = [] ,targetPath = '' ,offset = 0 ,breakMode = 1, replaceObjs = [],missStop = 1,rootParentGrp = '',simpleGrpMode = 0,doNotAttrs = []):
        errorInfo = []
        if targetPath == '':
            localPathAnim = self.checkAnimLocalPath()
            personalAmimFile = localPathAnim + infoFile + '.sla'
            personalObjFile = localPathAnim + infoFile + '_objs.txt'
        else:
            personalAmimFile = targetPath + infoFile + '.sla'
            personalObjFile = targetPath + infoFile + '_objs.txt'
        AnimsInfo = self.checkFileRead(personalAmimFile)
        someMode = 0
        if replaceObjs:
            nsObjs = replaceObjs
            someMode = 1
        else:
            nsObjs = self.checkFileRead(personalObjFile)
        if nsObjs:
            checkNoneName = []
            for obj in nsObjs:
                if replace:
                    obj = obj.replace(replace[0],replace[1])
                    if infoFile == 'proxy':
                        if 'MSH_c_hi_proxy' not in replace[0]:
                            obj = obj + '_'
                        if 'MSH_c_hi_proxy' in replace[0]:
                            obj = obj[0:-1]
                obj = rootParentGrp + obj
                exist = mc.objExists(obj)
                if exist != True:
                    if simpleGrpMode:
                        obj = obj.split('|')[-1]
                    else:
                        checkNoneName.append(obj)
            if not missStop or checkNoneName == []:
                linesInfo = len(AnimsInfo)
                if linesInfo > 5:
                    aniID = []
                    nonAnimID = []
                    frameInfos = AnimsInfo[1].split(';')[1].split(' ')[-1].split('-')
                    frameRange = [int(frameInfos[0]),int(frameInfos[1])]
                    linearSla = AnimsInfo[2].split(' ')[2][0:-1]
                    mc.currentUnit(linear=linearSla)
                    anglularSla = AnimsInfo[3].split(' ')[2][0:-1]
                    mc.currentUnit(angle=anglularSla)
                    timeTypeSla = AnimsInfo[4].split(' ')[2][0:-1]
                    mc.currentUnit(time=timeTypeSla)
                    for i in range(5, linesInfo):
                        lineInfo = AnimsInfo[i][0:-1]
                        if 'anim ' in lineInfo and 'non-anim' not in lineInfo:
                            aniID.append(i)
                        if 'non-anim'  in lineInfo:
                            nonAnimID.append(i)
                    for aid in aniID:
                        lineInfo = AnimsInfo[aid][0:-1]
                        attr = lineInfo.split('.')[-1]
                        objCtrl = lineInfo.split('.')[0].split(' ')[-1]
                        if someMode and objCtrl not in nsObjs:
                            continue
                        if attr in doNotAttrs:
                            continue
                        if replace:
                            objCtrl = objCtrl.replace(replace[0],replace[1])
                            if infoFile == 'proxy':
                                if 'MSH_c_hi_proxy' not in replace[0]:
                                    objCtrl = objCtrl + '_'
                                if 'MSH_c_hi_proxy' in replace[0]:
                                    objCtrl = objCtrl[0:-1]
                        objCtrl = rootParentGrp + objCtrl
                        key = ''
                        if 'Shape' not in objCtrl:
                            key = objCtrl + '.' + attr
                        else:
                            ctrolPoint = lineInfo.split('.')[-2]
                            key = objCtrl + '.' + ctrolPoint + '.' + attr
                        if simpleGrpMode:
                            if not mc.ls(key):
                                key = key.split('|')[-1]
                            if not mc.ls(key):
                                continue
                        if len(mc.ls(key)) == 1 and mc.getAttr(key, keyable=True) and mc.getAttr(key, l=1) != 1:
                            existAnim = mc.listConnections(key, s=1, d=0)
                            if existAnim and breakMode:
                                mc.delete(existAnim)
                            for j in range(1, linesInfo):
                                nextLine = AnimsInfo[aid + j ]
                                if (nextLine != '}') :
                                    if (nextLine != '{'):
                                        infoDetails = nextLine.split(' ')
                                        keyFrame = float(infoDetails[1]) + offset
                                        keyValue = float(infoDetails[2])
                                        keyInput = infoDetails[3]
                                        keyOutput = infoDetails[4]
                                        infoWeightLock = infoDetails[5]
                                        if infoWeightLock == 'True' and (infoDetails[3] == 'fixed' or infoDetails[4] == 'fixed'):
                                            keyInputAngle = float(infoDetails[6])
                                            if ';' in infoDetails[7]:
                                                infoDetails[7] = infoDetails[7][0:-1]
                                            keyOutputAngle = float(infoDetails[7])
                                            mc.setKeyframe(key, t=keyFrame , v=keyValue)
                                            mc.selectKey(key, k=keyFrame, r=1)
                                            mc.keyTangent(e=1, ia=keyInputAngle, iw=1, oa=keyOutputAngle, ow=1)
                                        else:
                                            if infoWeightLock != 'True' and (infoDetails[3] == 'fixed' or infoDetails[4] == 'fixed'):
                                                keyInputAngle = float(infoDetails[6])
                                                keyInputWeight = float(infoDetails[7])
                                                keyOutputAngle = float(infoDetails[8])
                                                if ';' in infoDetails[9]:
                                                    infoDetails[9] = infoDetails[9][0:-1]
                                                keyOutputWeight = float(infoDetails[9])
                                                mc.setKeyframe(key, t=keyFrame , v=keyValue)
                                                mc.selectKey(key, k=keyFrame, r=1)
                                                mc.keyTangent(e=1, ia=keyInputAngle, iw=keyInputWeight, oa=keyOutputAngle, ow=keyOutputWeight)
                                            else:
                                                mc.setKeyframe(key, t=keyFrame , v=keyValue, itt=keyInput, ott=keyOutput)
                                else:
                                    break
                        else:
                            if mc.ls(key) and mc.getAttr(key, settable=1):
                                for j in range(1, linesInfo):
                                    nextLine = AnimsInfo[aid + j ]
                                    if (nextLine == '}') :
                                        break
                                    if (nextLine == '{') :
                                        continue
                                    infoDetails = nextLine.split(' ')
                                    keyValue = float(infoDetails[2])
                                    mc.setAttr(key,keyValue)
                                    break
                            else:
                                errorInfo.append('---No object:[%s]'%key)
                    for nid in nonAnimID:
                        key = AnimsInfo[nid].split(' ')[1]
                        if replace:
                            key = key.replace(replace[0],replace[1])
                            if infoFile == 'proxy':
                                if 'MSH_c_hi_proxy' not in replace[0]:
                                    key = key + '_'
                                if 'MSH_c_hi_proxy' in replace[0]:
                                    key = key[0:-1]
                        # valueType 1,浮点数 | 0 字符串
                        valueType = 1
                        if len(mc.ls(key)) == 1 and mc.getAttr(key, k=1) and mc.getAttr(key, settable=1) and mc.getAttr(key, l=1) != 1:
                            existAnim = mc.listConnections(key, s=1, d=0)
                            if existAnim and breakMode:
                                mc.delete(existAnim)
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
                   errorInfo.append(u'-------------[Anim] Anim Info Error -------------')
            else:
                for error in checkNoneName:
                    errorInfo.append(u'-------------[Anim] Anim Info Error -------------')
                    errorInfo.append(u'----No object:[%s]-------------' % (error))
            for i in errorInfo:
                print(i)
            return checkNoneName

    # 清理时间轴外的动画曲线
    def checkAnimCleanNoneTimeRange(self,animCurves):
        frameMin = mc.playbackOptions(min = 1,q=1)
        frameMax = mc.playbackOptions(max = 1,q=1)
        frameNow = mc.currentTime(q=1)
        mc.currentTime(frameMin-1)
        mc.setKeyframe(animCurves)
        mc.currentTime(frameMax)
        mc.setKeyframe(animCurves)
        mc.currentTime(frameNow)
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
        frameMin = mc.playbackOptions(min = 1,q=1)
        frameMax = mc.playbackOptions(max = 1,q=1)
        mc.currentTime(frameMin)
        mc.setKeyframe(objs)
        mc.currentTime(frameMax)
        mc.setKeyframe(objs)
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

    #------------------------------#
    # 该死的摘出来
    #------------------------------#
    def checkAnimLocalPath(self):
        localInfoPath = ('D:/Info_Temp/temp/')
        shotInfo  = self.checkShotInfo()
        localPath = localInfoPath + 'animRebuild/' + shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/' +shotInfo[3] + '/'
        if not os.path.exists(localPath):
            mc.sysFile(localPath,makeDir = 1)
        mc.sysFile(localInfoPath, makeDir=True)
        return localInfoPath

    def checkShotInfo(self):
        temp = (mc.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
        else:
            mc.warning(u'========================【！！！文件名不规范！！！】========================')
        return info

    #读文件================
    def checkFileRead(self, path):
        import os
        if not os.path.exists(path):
            print path
            print u'Error:    file do not exist'
            mc.error(u'Error:    file do not exist')
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            #print path
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0]) # add  replace 方法，删除误写入的空格 by zhangben 20160223
            else:
                result.append(info)
        return result

    #写文件================
    def checkFileWrite(self, path , info , addtion=0):
        if addtion == 1:
            info = self.checkFileRead(path) + info
        txt = open(path, 'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()

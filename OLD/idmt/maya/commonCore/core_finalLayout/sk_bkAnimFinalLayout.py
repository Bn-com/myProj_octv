# -*- coding: utf-8 -*-
# 【通用】【FinalLayout环节工具】【BK Anim版】
#  Author : 沈康
#  Data   : 2014_08

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)
from idmt.maya.commonCore.core_baseCommon import sk_infoCore
reload(sk_infoCore)
from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
reload(sk_hbExportCam)
import os

# BK动画信息版
class sk_bkAnimFinalLayout(object):
    def __init__(self):
        self.ppType = 'GDC'

    #--------------------------------------------#
    # anim执行输出
    #--------------------------------------------#
    # curveOnly 0 时transform都能输出  | 1 时只输出动画曲线
    def sk_checkBakeAnimExportPerform(self , exportPath = '' , infoFile = 'cleanAnim' , bkPerform = 1 ,curveOnly = 1 ,step = 1,server = 0):

        if exportPath == '':
            shotInfo  = sk_infoConfig.sk_infoConfig().checkShotInfo()
            localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath() + 'animCurveTemp/' + shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/'
            shotType = sk_infoConfig.sk_infoConfig().checkShotType()
            if shotType == 2:
                idNum = 3
            if shotType == 3:
                idNum = 4
            if shotInfo[idNum] != 'an':
                localPath = localPath + shotInfo[3] + '/'
            if not os.path.exists(localPath):
                mc.sysFile(localPath,makeDir = 1)
            exportPath = localPath

        mc.cycleCheck(evaluation = 0)
        # 约束BK阶段
        if bkPerform:
            import sk_bkCore
            reload(sk_bkCore)
            sk_bkCore.sk_bkCore().sk_bkPerform(preFrame = 10 , posFrame = 10 , simulation = 1 , animType = 2 ,step = step)

        # 参考顶级化
        refInfos = self.sk_refTopConfig()

        # 优化数据
        self.sk_checkAnimCleanSingleKey()

        # 找到动画曲线
        needObjs = []
        if curveOnly:
            curveShapes = mc.ls(type = 'nurbsCurve',l=1)
            for curve in curveShapes:
                # 参考的才是合法的
                isRef = mc.referenceQuery(curve,isNodeReferenced = 1)
                if not isRef:
                    continue
                # 参考上级组不允许K帧
                curveObj = mc.listRelatives(curve,ap = 1,type = 'transform',f = 1)
                if not curveObj:
                    continue
                curveObj = curveObj[0]
                if curveObj not in needObjs:
                    needObjs = needObjs + mc.ls(curveObj,l=1)
        else:
            allGrps = mc.ls(type = 'transform',l=1)
            for grp in allGrps:
                # 参考的才是合法的
                isRef = mc.referenceQuery(grp,isNodeReferenced = 1)
                if not isRef:
                    continue
                if grp not in needObjs:
                    needObjs.append(grp)

        # frames
        fpsMode = mc.currentUnit(time=1,q=1)
        startFrame = mc.playbackOptions(min=1,q=1)
        endFrame = mc.playbackOptions(max=1,q=1)
        frameInfos = [fpsMode,str(startFrame),str(endFrame)]
        frameFile = exportPath + infoFile + '_frm.txt'
        sk_infoConfig.sk_infoConfig().checkFileWrite(frameFile,frameInfos)

        # 导出
        if needObjs:
            import sk_animCurveCore
            reload(sk_animCurveCore)
            sk_animCurveCore.sk_animCurveCore().checkAnimCurveInfoExport(needObjs, targetPath = exportPath , infoFile = infoFile)
            # 输出参考信息
            refFile = exportPath + infoFile + '_ref.txt'
            sk_infoConfig.sk_infoConfig().checkFileWrite(refFile,refInfos)

            print u'\n=====================[Anim Export] Done!!!====================='

            # camBK
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1,shotType)
            '''
            sk_bkCore.sk_bkCore().sk_sceneCameraBK()
            # cam处理
            shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            camName = 'cam_' +  shotInfo[1] + '_' + shotInfo[2] + '_baked'
            shotType = sk_infoConfig.sk_infoConfig().checkShotType()
            if shotType == 3:
                camName = 'cam_' +  shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '_baked'
            mc.select(camName)
            # 导出
            camFileName = camName.replace('cam_',(shotInfo[0]+'_')).replace('_baked','_cam.ma')
            mc.file((exportPath + camFileName), force=1, options="v=0" , type='mayaAscii', preserveReferences=1, exportSelected=1)
            '''
            print u'\n=====================[Cam Export] Done!!!====================='

        if server:
            serverBase = sk_infoConfig.sk_infoConfig().checkAnimServerPath(rebuild=1)
            serverBase = serverBase.replace('\\','/')
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (exportPath + infoFile + '.sla') + '"' + ' ' + '"' + (serverBase + infoFile + '.sla') + '"' + ' true'
            mel.eval(updateAnimCMD)
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (exportPath + infoFile + '_objs.txt') + '"' + ' ' + '"' + (serverBase + infoFile + '_objs.txt') + '"' + ' true'
            mel.eval(updateAnimCMD)
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (exportPath + infoFile + '_ref.txt') + '"' + ' ' + '"' + (serverBase + infoFile + '_ref.txt') + '"' + ' true'
            mel.eval(updateAnimCMD)
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (exportPath + infoFile + '_frm.txt') + '"' + ' ' + '"' + (serverBase + infoFile + '_frm.txt') + '"' + ' true'
            mel.eval(updateAnimCMD)
            print serverBase
            print u'\n=====================[Server Update] Done!!!====================='

    # 重构指定镜头文件文件
    def sk_checkAnimRebuildPerform(self , shotInfo = 'lb_101_102' , infoFile = 'cleanAnim' ,mayaType = 'ma', checkIn = 0):
        mc.file(new = 1,f = 1)

        # 允许undo
        mc.undoInfo(state=True, infinity=True)
        # -----需要服务器端查版本号
        tk = 'c001'
        newFileName  = (shotInfo) + '_an_' + tk + '.' + mayaType
        print '-----------001'
        shotId = shotInfo.split('_')
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath() + 'animRebuild/' + shotId[0]  + '/' + shotId[1]  + '/' + shotId[2]  + '/'
        if len(shotId) > 3:
            localPath = localPath + shotId[3]  + '/'
        import os
        if not os.path.exists(localPath):
            mc.sysFile(localPath,makeDir = 1)
        print '-----------002'
        mc.file(rename = (localPath + newFileName) )

        # 备份
        localRebuildPath = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(rebuild = 1)
        mc.file(rename = (localRebuildPath + newFileName))
        # 查询数据库路径
        serverRebuildPath = sk_infoConfig.sk_infoConfig().checkAnimServerPath(rebuild = 1)
        import os
        frmInfoFile = serverRebuildPath + infoFile + '_frm.txt'
        if not os.path.exists(frmInfoFile):
            errorInfo = u'===本镜头缺失Frame信息==='
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        frameInfos = sk_infoConfig.sk_infoConfig().checkFileRead(frmInfoFile)
        fpsInfo = frameInfos[0]
        startFrame = float(frameInfos[1])
        endFrame = float(frameInfos[2])
        mc.currentUnit(time=fpsInfo)
        mc.playbackOptions(min=startFrame)
        mc.playbackOptions(animationStartTime=(startFrame - 10))
        mc.playbackOptions(max=endFrame)
        mc.playbackOptions(animationEndTime=(endFrame + 10))

        # ref处理
        refInfoFile = serverRebuildPath + infoFile + '_ref.txt'
        if not os.path.exists(refInfoFile):
            errorInfo = u'===本镜头缺失RebuildRef信息==='
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        refInfos = sk_infoConfig.sk_infoConfig().checkFileRead(refInfoFile)

        print u'\n=====================Start  Rebuilding Reference=====================\n'
        for i in range(len(refInfos)/2):
            refNamespace = refInfos[2*i].split(':')[-1]
            refPath = refInfos[2*i + 1]
            mc.file(refPath,reference = 1,namespace = refNamespace)
        print u'\n=====================Sucess Rebuilding Reference=====================\n'

        # 导入信息
        slaInfoFile = serverRebuildPath + infoFile + '.sla'
        if not os.path.exists(slaInfoFile):
            errorInfo = u'===本镜头缺失RebuildSla信息==='
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        objInfoFile = serverRebuildPath + infoFile + '_objs.txt'
        if not os.path.exists(objInfoFile):
            errorInfo = u'===本镜头缺失RebuildObj信息==='
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        import sk_animCurveCore
        reload(sk_animCurveCore)

        print u'\n=====================Start  Recovering Animation=====================\n'
        sk_animCurveCore.sk_animCurveCore().checkAnimCurveInfoImport(targetPath = serverRebuildPath , infoFile = infoFile)
        print u'\n=====================Sucess Recovering Animation=====================\n'

        # cam导入
        '''
        camFile = shotId[0] + '_' + shotId[1] + '_' + shotId[2]
        camName = 'cam_' + shotId[1] + '_' + shotId[2]
        if len(shotId) > 3:
            camFile = camFile + '_' + shotId[3]
            camName = camName + '_' + shotId[3]
        mc.file(((serverRebuildPath + camFile + '_cam.ma').replace('\\','/')),i = 1 ,f = 1,type = 'mayaAscii' ,mergeNamespacesOnClash = 0,rpr = True,options = "v=0;p=17;f=0")
        mc.rename((camName + '_baked'),camName)
        '''
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        sk_hbExportCam.sk_hbExportCam().camServerReference(shotType)

        mc.file(save = 1, force = 1)

        if checkIn:
            from commonCore.core_aasCheckin import aas_checkIn
            reload(aas_checkIn)
            aas_checkIn.aas_checkIn().aas_checkInPerform('Creted By OutSide',checkMode = 0)

        # 时间轴处理

        print u'\n---outPath\t%s'%(localPath)
        print u'\n=================[Anim Import] Done!!!================='

    # 参考组顶级化
    def sk_refTopConfig(self):
        referencesLV_0 = mc.file(q = 1,reference =1)
        result = []
        if not referencesLV_0:
            mc.warning(u'-------------No Reference in File-------------')
            return result
        for refPath in referencesLV_0:
            refObjs = mc.referenceQuery(refPath,nodes=1)
            if not refObjs:
                continue
            refTopObjs = mc.ls(refObjs[0],l = 1)[0]
            if len(refTopObjs.split('|')) != 2:
                mc.parent(refTopObjs,world = 1)
            namespace = mc.referenceQuery(refPath,namespace=1)
            result = result + [namespace,refPath]
        return result


    #------------------------------#
    # 【辅助】【动画信息处理函数】
    # 0.动画通用
    # 1.动画曲线点问题修正
    # 2.动画曲线0清除
    # Author : 沈  康
    # Data   : 2013_03_01
    #------------------------------#
    # 清理无用动画曲线，修正动画曲线问题
    def sk_checkAnimCleanSingleKey(self):
        animCurvs = mc.ls(type='animCurve')
        if not animCurvs:
            return 0
        for animC in animCurvs:
            # 必须是非参考的
            isRef = mc.referenceQuery(animC, isNodeReferenced = 1)
            if isRef:
                continue
            # 删除单帧动画曲线
            valuePoints = mc.keyframe(animC, q=1, vc=1)
            if not valuePoints:
                continue
            # 单帧信息
            if len(list(set(valuePoints))) == 1:
                # 清理关键帧
                mc.delete(animC)



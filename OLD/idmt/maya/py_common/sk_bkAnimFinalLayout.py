# -*- coding: utf-8 -*-
# 【通用】【FinalLayout环节工具】【BK Anim版】
#  Author : 沈康
#  Data   : 2014_08
'''
#--01 以下功能不支持传递
# 约束物体
# 自建属性
# camera
#--02 使用方法
先把2个脚本放到纯英文简单路径，如d:\myScript或服务器端
在maya python路径里输入

# 以下是导出版
localPath = 'd:/myScript'
import sys
if localPath not in sys.path:
	sys.path.append(localPath)
import sk_bkAnimFinalLayout
reload(sk_bkAnimFinalLayout)
sk_bkAnimFinalLayout.sk_bkAnimFinalLayout().sk_checkBakeAnimExportPerform()


# 以下是导入版
localPath = 'd:/myScript'
shotID = 'nj_E0011_Q0315_S0070'
import sys
if localPath not in sys.path:
	sys.path.append(localPath)
import sk_bkAnimFinalLayout
reload(sk_bkAnimFinalLayout)
sk_bkAnimFinalLayout.sk_bkAnimFinalLayout().sk_checkAnimRebuildPerform(shotID)

'''
import maya.cmds as mc
import maya.mel as mel
import sk_animCurveCore
reload(sk_animCurveCore)
import os

# BK动画信息版
class sk_bkAnimFinalLayout(object):
    def __init__(self):
        self.ppType = 'GDC'

    #--------------------------------------------#
    # anim执行输出
    #--------------------------------------------#
    # curveOnly 0 时transform都能输出  | 1 时只输出动画曲线
    def sk_checkBakeAnimExportPerform(self , exportPath = '' , infoFile = 'cleanAnim' , curveOnly = 1 ,step = 1,server = 0):

        if exportPath == '':
            shotInfo  = self.checkShotInfo()
            localPath = self.checkLocalInfoPath() + 'animRebuild/' + shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/' +shotInfo[3] + '/'
            if not os.path.exists(localPath):
                mc.sysFile(localPath,makeDir = 1)
            exportPath = localPath

        mc.cycleCheck(evaluation = 0)

        # 参考顶级化
        refInfos = self.sk_refTopConfig()

        # 优化数据
        #self.sk_checkAnimCleanSingleKey()

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
        self.checkFileWrite(frameFile,frameInfos)

        # 导出
        if needObjs:
            sk_animCurveCore.sk_animCurveCore().checkAnimCurveInfoExport(needObjs, targetPath = exportPath , infoFile = infoFile)
            # 输出参考信息
            refFile = exportPath + infoFile + '_ref.txt'
            self.checkFileWrite(refFile,refInfos)
            print '\n'
            print localPath
            print u'=====================[Anim Export] Done!!!====================='

#重构面板
    def sk_checkAnimRebuildUI(self):
        if mc.window('nj_animImportTools', exists=True):
          mc.deleteUI('nj_animImportTools')
        mc.window('nj_animImportTools', width=150, height=60, sizeable=True)
        mc.columnLayout(adjustableColumn=True )
        mc.textFieldGrp('shotInfo',label='ShotName', text='nj_E0001_Q0001_S0001' )
        mc.button( label=u'创建', bgc = [0,0,0.0],command='import sys;sys.path.append(r"//file-cluster/GDC/Resource/Support/Maya/OEM/python/py_common");import sk_bkAnimFinalLayout\nreload(sk_bkAnimFinalLayout)\nsk_bkAnimFinalLayout.sk_bkAnimFinalLayout().sk_checkAnimRebuildApply()' )
        mc.showWindow('nj_animImportTools')
#重构命令
    def sk_checkAnimRebuildApply(self):  
        shotID=mc.textFieldGrp('shotInfo',q=1,text=1)
        self.sk_checkAnimRebuildPerform(shotID)     
    # 重构指定镜头文件文件
    def sk_checkAnimRebuildPerform(self , shotInfo = 'lb_101_102' , infoFile = 'cleanAnim' ,mayaType = 'mb'):
        
        mc.file(new = 1,f = 1)

        # 允许undo
        mc.undoInfo(state=True, infinity=True)
        # -----需要服务器端查版本号
        tk = 'c001'
        newFileName  = (shotInfo) + '_an_' + tk + '.' + mayaType
        print '-----------001'
        shotId = shotInfo.split('_')
        localPath = self.checkLocalInfoPath() + 'animRebuild/' + shotId[0]  + '/' + shotId[1]  + '/' + shotId[2]  + '/' + shotId[3]  + '/'
        import os
        if not os.path.exists(localPath):
            mc.sysFile(localPath,makeDir = 1)
        print '-----------002'
        mc.file(rename = (localPath + newFileName) )

        # 查询数据库路径
        serverRebuildPath = localPath
        import os
        frmInfoFile = serverRebuildPath + infoFile + '_frm.txt'
        if not os.path.exists(frmInfoFile):
            errorInfo = u'===本镜头缺失Frame信息==='
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        frameInfos = self.checkFileRead(frmInfoFile)
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
        refInfos = self.checkFileRead(refInfoFile)

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

        print u'\n=====================Start  Recovering Animation=====================\n'
        sk_animCurveCore.sk_animCurveCore().checkAnimCurveInfoImport(targetPath = serverRebuildPath , infoFile = infoFile)
        print u'\n=====================Sucess Recovering Animation=====================\n'

        mc.file(save = 1, force = 1)
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
	
	#------------------------------#
	# 该死的摘出来
	#------------------------------#
    def checkShotInfo(self):
        temp = (mc.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
        else:
            mc.warning(u'========================【！！！文件名不规范！！！】========================')
        return info      
	
    def checkLocalInfoPath(self):
        localInfoPath = ('D:/Info_Temp/temp/')
        mc.sysFile(localInfoPath, makeDir=True)
        return localInfoPath

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
            
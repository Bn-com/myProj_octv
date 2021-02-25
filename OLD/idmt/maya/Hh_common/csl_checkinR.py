# -*- coding: utf-8 -*-

# import sys
# sys.path.append('D:\\food\pyp\common')
# tx文件上传为anim 及render文件（特proxy物体，无cache)

import maya.cmds as mc
import maya.mel as mel
import os
from idmt.maya.commonCore.core_mayaCommon import sk_backCmd
reload(sk_backCmd)
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class csl_checkinR(object):
    def __init__(self):
        # namespace清理
        pass
    def csl_checkpoxy(self):
        userName = os.environ['USERNAME']
        # 项目名
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(info[0])
        # 改成复制到本地
        # 是否本地文件判断
        # path = self.checkPCFilePath()
        # 另存到temp文件夹
    
        pathLocal = sk_infoConfig.sk_infoConfig().checkTX2AnimRenderLocalPath()
        fileName = mc.file(sceneName=1, q=1).split('/')[-1]
        fileLocal = pathLocal + fileName
        mc.file(rename=fileLocal)
        mc.file(save=1 , force = 1)
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(info[0])
        fileNameNow = mc.file(query=1, exn=1)
        # 上传asstoc文件
        self.csl_asstocchecinCopy() 
        # 另存anim
        mc.file(fileNameNow, force=1, options="v=0", type=fileTypeFull  , open=1)
        print '------'
        print fileNameNow
        tempName = fileNameNow
        animname = tempName.replace('_tx.', '_ms_anim.') 
        print animname
        mc.file(rename= animname)
        mc.file(force=1, options="v=0" , type=fileTypeFull , save=1)
        newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3]+ '_' + newInfo[4] + '|' + userName
        mc.idmtService('Checkout', fileInfo)
        mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
        #另存render
        mc.file(fileNameNow, force=1, options="v=0", type=fileTypeFull  , open=1)
        print '------'
        print fileNameNow
        tempName = fileNameNow
        rendername = tempName.replace('_tx.', '_ms_render.') 
        mc.file(rename=rendername)
        mc.file(force=1, options="v=0" , type=fileTypeFull , save=1)
        newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] +"_"+ newInfo[4]  + '|' + userName
        mc.idmtService('Checkout', fileInfo)
        mel.eval('idmtProject -checkin -description \"Creted By TX File\"')

#copy 渲染代理asstoc文件
    def csl_asstocchecin(self):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        assserverPath=serverPath+'data/ArnoldStandIn/'+shotInfos[1]+'/'
        aiS=mc.ls(type='aiStandIn')
        if aiS:
            for ai in aiS:
                files=mc.getAttr(ai+".dso")
                name=files.split('/')
                path=''
                if name:
                    for i in range(len(name)-1):
                        if i==0:
                            path=name[0]+'/'
                        else:    
                            path=path+name[i]+'/'
                shortname=name[-1]
                asstocname=shortname.split('.')[0]+'.asstoc' 
                if path and asstocname in mc.getFileList(folder=path):
                   updateAnimCMD = 'zwSysFile "copy" ' + '"' + (path+asstocname) + '"' + ' ' + '"' + (assserverPath + asstocname) + '"' + ' true'
                   mel.eval(updateAnimCMD)
                   print(u'=====================【asstoc文件已经上传】【%s】=====================' % (asstocname))  

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【检测并上传asstoc文件】
    #  Author  : 韩虹
    #  Data    : 2015_01_26
    #------------------------------#  
    def csl_asstocchecinCopy(self):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        assserverPath=serverPath+'data/ArnoldStandIn/'+shotInfos[1]+'/'
        aiS=mc.ls(type='aiStandIn',l=1)
        aiInfo = []
        errorInfo=[]
        '''
        if aiS:
            for ai in aiS:
                filePath = mc.getAttr(ai+".dso")
                if '/' in filePath and '.ass' in filePath:
                    aiInfo[ai] = [filePath]
                    tocFile = filePath + 'toc'
                    if os.path.exists(tocFile):
                        aiInfo[ai] = [filePath,tocFile]

                    shortName = filePath.split('/')[-1]
                    folderPath = filePath.split(shortName)[0]
                    asstocname = shortName + 'toc'
                    pathz=folderPath
                    if '${IDMT_PROJECTS}' in folderPath:
                        pathz=folderPath.replace('${IDMT_PROJECTS}','Z:/Projects')

                    if (folderPath+asstocname) not in aiInfo:
                        aiInfo.append(folderPath+asstocname)
        if aiInfo:
            for info in aiInfo:
                shotname=info.split('/')[-1]
                path=os.path.expandvars(info.split(shotname)[0])
                print '--------------'
                print path
                if os.path.exists(path):# and shotname  in mc.getFileList(folder=path):
                    updateAnimCMD = 'zwSysFile "copy" ' + '"' + info + '"' + ' ' + '"' + (assserverPath + shotname) + '"' + ' true'
                    mel.eval(updateAnimCMD)
                else:
                    errorInfo.append(info)
        '''
        for aiNode in aiS:
            filePath = mc.getAttr(aiNode+'.dso')
            if filePath.split('/')[-1] not in ['ass']:
                continue
            if filePath not in aiInfo:
                aiInfo.append(filePath)
            tocFile = filePath + 'toc'
            if os.path.exists(tocFile):
                if tocFile not in aiInfo:
                    aiInfo.append(tocFile)
            else:
                errorInfo.append(aiNode)
            mc.setAttr((aiNode+'.dso'),filePath,type = 'string')

        if errorInfo:
            for err in errorInfo:
                mc.error(u'============缺少【%s】asstoc文件=======' %err)

        needSets = [u'defaultLightSet', u'defaultObjectSet', u'initialParticleSE', u'initialShadingGroup']
        setGrps = mc.ls(type = 'objectSet')
        for setGrp in setGrps:
            if setGrp in needSets:
                continue
            if mc.ls(setGrp):
                mc.delete(setGrp)

        for checkFile in aiInfo:
            fileName = checkFile.split('/')[-1]
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + checkFile + '"' + ' ' + '"' + (assserverPath + fileName) + '"' + ' true'
            mel.eval(updateAnimCMD)

        print (u'=====================【asstoc文件已经上传】=====================' )                          
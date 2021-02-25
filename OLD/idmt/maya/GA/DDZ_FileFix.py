# -*- coding: utf-8 -*-
# 【DDZ项目】【渲染文件优化】【包含smooth,转参考】
#  Author : 韩虹
#  Data   : 2017_09
# import sys

import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db
import pymel.core as pm
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
reload(sk_cacheFinalLayout)
from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
reload(sk_hbExportCam)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)

from idmt.maya.GA import GA_RedShiftRender
reload(GA_RedShiftRender)


import os
import re

class DDZ_FileFix(object):
    def __init__(self):
        # namespace清理
        pass
        
    #----------------------------------------------------------------------------------------------#
    

    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【总篇】【灯光】【FinalLayout环节工具】【后台】
    #  Author  : 沈康
    #  Data    : 2013_06_03
    #------------------------------#
    
    # cache最好先本地使用，最后upload并更新cache路径
    # anim可直接upload至服务器
    # 需要增加每个角色创建cache的功能
    # 新增功能：但凡cache物体和anim物体，只要其属于OTC_GRP,一概不参与cache和anim记录
    # template模式下，强制换anim参考，不处理帧信息，不导入相机，只输出cache到服务器端，不check in到服务器
    def ddz_renderFileFIX(self,server = 1,shotType = 2,smooth=1):
        #---------------------------#
        # Setup 000  外部操作，
        #---------------------------#
        mel.eval('cycleCheck -e off')
        #---------------------------#
        # Setup 001  多级非参考的namespace清理。
        # 某些外包，喜欢做动作模板，然后import进来，这样形成了两级namespace，而在参考是不会记录import的那级参考。
        # 这种情况，要处理掉，不然后面记录参考信息时会出问题
        #---------------------------#
        # 处理非参考的namespace
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        print u'====================多层namespace清理完毕===================='
        #---------------------------#
        # Setup 002  判断是否动画shot里的参考是否都有render 版本。如果没有，报错退出
        #---------------------------#
        # 检测参考是否正确，是否有render参考
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_FLCheckRenderFile(refInfos)
        
        #---------------------------#
        # Setup 003  记录基本信息，修正时间轴        #---------------------------#
        
        # 记录项目，场次，镜头号,文件类型
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFormat = '.mb'
        print u'\n'
        print(u'=====================【%s_%s】【文件优化】开始处理！！！====================='%(shotInfos[1],shotInfos[2]))
        print(u'=========================================================================')
        # 修正时间轴
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame',shotType )
        #---------------------------#
        # Setup 004  本地另存，备份
        #---------------------------#
        # 获取finalLayout临时路径
        localPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath(shotType )
        # 获取finalLayout服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutServerPath(shotType )
        
        # 本地另存
        shotName=''
        if shotType==2:
           shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]  
        if shotType==3:
            shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]   
        localFile = localPath + shotName+'_an_c001' + fileFormat
        mc.file(rename = localFile)
        mc.file(save=1,force = 1)
        #---------------------------#
        # Setup 005  清理外包残留的playblast表达式
        #---------------------------#
        if mc.ls('zwHeadsUpDisplay',type = 'expression'):
            mc.delete('zwHeadsUpDisplay')
            print u'\n'
            print u'====================【zwHeadsUpDisplay】清理完毕===================='
            print u'\n'
        #---------------------------#
        # Setup 006  清理未勾选的参考，清理垃圾节点，更新camera，IKR再启动
        #---------------------------#
        sk_sceneTools.sk_sceneTools().sk_sceneUnloadRefDel(1,0)
        print u'\n'
        print u'========================未勾选参考清理完毕========================'
        print u'\n'
        # 初步清理垃圾节点
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean(unuse=1 , turtle=1)
        # 强制启动IK解算
        mc.ikSystem(e = 1,sol = 1)
        print u'\n'
        print u'=========================IK解算器强制更新========================'
        print u'\n'
        # 更新摄像机           
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfos[0])
        camServerPath=''
        if projectInfo in ['YongTai']:
            camServerPath = '//file-cluster/GDC/Projects/DomesticProject/' + projectInfo + '/Project/scenes/Animation/episode_' + shotInfos[1] + '/episode_camera/'
        else:            
            camServerPath = '//file-cluster/GDC/Projects/' + projectInfo + '/Project/scenes/Animation/episode_' + shotInfos[1] + '/episode_camera/'
        camServerPathN = camServerPath + shotName+ '_cam.ma'
        if os.path.exists(camServerPath):
            pass
        else:
            if server:
                sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1,3)
                print u'\n'
                print u'==========================camera传输完毕=========================='
                print u'\n'

        #---------------------------#
        # Setup 009 文件内部大组归类
        #---------------------------#
        # 处理SET_GRP和OTC_GRP内的参考
        # 处理大组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
        print u'\n'
        print u'==========================文件整理完毕=========================='
        print u'\n'
                
        #---------------------------#
        # Setup 011 获取anim shot的参考信息
        #---------------------------#
        # 获取references信息
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()

        #---------------------------#
        # Setup 012 默认OTC和SET组内的参考不参与cache及重新参考，这里记录不需要的参考信息
        #---------------------------#
        # 处理大组
        noNeedRefNodeInfo = sk_cacheFinalLayout.sk_cacheFinalLayout().skFLNoNeedRefNodeInfo()
        
        print u'\n'
        print(u'=====================【Group】【服务器端】【输出】完毕=====================')
        print u'\n'
        
        print u'\n-------------------------'
        print '[Ref Info]'
        print refInfos[0][0]
        print u'-------------------------'
        # 准备先另存，因为update需要用到文件名
        fileName = shotName +'_base_lr_c001' + fileFormat
        # 本地文件
        localFile = localPath + fileName
        # 服务器端文件
        # serverFile = serverPath + fileName
        # 重命名
        mc.file( rename= localFile )
        mc.file(save = 1 ,force = 1)
        #---------------------------#
        # 转参考
        self.ddz_RefRefSwitch()
        #---------------------------#
        # Setup 021 参考最终相机
        #---------------------------#
        # 导入cam
        # 导入相机
        if shotType ==2:
            sk_hbExportCam.sk_hbExportCam().camServerReference(info=2)
        if shotType ==3:
            sk_hbExportCam.sk_hbExportCam().camServerReference(info=3)                    
    
        #---------------------------#
        # Setup 022 新建后的文件大组重新处理
        #---------------------------#
        # 处理大组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(1)
        # Setup 023 smooth
        #---------------------------#
        if smooth==1:
            GA_RedShiftRender.GA_RedShiftRender().GA_RSmoothSet()
        #---------------------------#
        # Setup 024 镜头信息，时间轴信息处理
        #---------------------------#
        #---------------------------#
        # 本地保存
        fileTypeFull = 'mayaBinary'
        mc.file(force=1, options="v=0", type=fileTypeFull , save=1)
        # 设置时间轴等消息
        # 命令
        if shotType == 2:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType == 3:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]
        #删除多余参考
        self.GA_unknownPluginsRemove()

        # 开始处理
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart

        endFrame = anim.frmEnd
        fpsFrame = anim.fps
        resW = anim.resolutionW
        resH = anim.resolutionH
        # 分辨率
        mc.setAttr(('defaultResolution.width'), resW)
        mc.setAttr(('defaultResolution.height'), resH)
        # FPS
        if fpsFrame == 25:
            mc.currentUnit(time='pal')
        if fpsFrame == 24:
            mc.currentUnit(time='film')
        if fpsFrame == 30:
            mc.currentUnit(time='ntsc')
        # frame
        if startFrame and fpsFrame:
            # 起始帧
            mc.playbackOptions(min=startFrame)
            # 起始预留
            preStartFrame = startFrame - 10
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=endFrame)
            # 结束预留
            posEndFrame = endFrame + 10
            mc.playbackOptions(animationEndTime=posEndFrame)
        # 设置帧播放模式每帧
        mc.playbackOptions(playbackSpeed=0)
        mc.file(save=1, force = 1)
        if server == 1:
            # 用户名
            userName = os.environ['USERNAME']
            newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(newInfo[0])
            fileInfo=''
            if shotType==3:
                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
            if shotType==2:
                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3]  + '|' + userName                    
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            #print checkOutCmd
            mel.eval(checkOutCmd)
            # checkIn
            description = u'base file(no rendering)'
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')
        print '\n'
        print(u'=========================================================================')
        print(u'=====================【%s_%s】【文件优化】处理完毕====================='%(shotInfos[1],shotInfos[2]))
        return localFile
        
    #----------------------------------------------------------------------------------------------

    def ddz_RefRefSwitch(self):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        referroList=[]
        if not refNodes:
            mc.error(u'文件中没有参考文件，请检查')
        for i in range(len(refNodes)):
            if 'ms_anim' in refPaths[i]:
                refPathN=refPaths[i].replace('ms_anim','ms_render')
                try:
                    mc.file(refPathN, lr=refNodes[i])
                except:
                    referroList.append(refNodes[i])
            else:
                referroList.append(refNodes[i])
        return referroList
    #【通用】
    #删除多余参考，用于maya2016以上版本
    #@author: hanhong
    #Data：2017/6/9
    def GA_unknownPluginsRemove(self):
        unknownPlugins = mc.unknownPlugin(list = 1, q=1)
        PluginList=[]
        unPluginList=[]
        if unknownPlugins:
            for plug in unknownPlugins:
                try:
                    mc.unknownPlugin(plug, r=1)
                    PluginList.append(plug)
                except:
                    mc.warning(u'【%s】多余参考未删除，请检查' %plug)
                    unPluginList.append(plug)
                    pass
        return unPluginList
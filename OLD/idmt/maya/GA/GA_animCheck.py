# -*- coding: utf-8 -*-

'''
Created on 2013-6-18

@author:
'''
import maya.cmds as mc
import maya.mel as mel
import os
import re
import sys
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.setdefaultencoding('utf8')
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde


from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
reload(sk_cacheFinalLayout)
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
class GA_animCheck(object):
    def __init__(self):
        pass

    #-------------#
    # 【后台】清理anim文件
    #anim =0,不弹出动画提醒
    #-------------#
    def GA_animCheck(self , serverClean = 0 , norenderConfig = 0,Constraints=1,anim=0,camcheckin=1):
        # 开始处理
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.py_common import GDC_checkin
        reload(GDC_checkin)
        from idmt.maya.commonCore.core_mayaCommon import sk_animFileCheck
        reload(sk_animFileCheck)
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        print u'====================多层nsamespace清理完毕===================='
        mel.eval('source zwRemoveAllProxy') 
        mel.eval('zwRemoveAllProxy()')
        #显示属性
        if anim==1:
            a=mc.layoutDialog(ui=self.njcheckboxPrompt)
            if a=='Abort':
                return mc.error()
        # 原始组显示属性传递到下一层级
        self.DisAnmSet()
        print u'====================refProxy清理完毕===================='
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]

         #导入参考相机
        refNodes = refInfo[0][0]

        refPaths = refInfo[1][0]
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        #
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()

        print '==========================================='
        print u'====================ref对比情况检测完毕===================='
        unload = 0
        result = u'[清理完毕]'
        if refNodes:
            for ref in refNodes:
                check = mc.referenceQuery(ref,isLoaded = 1)
                if check:
                    pass
                else:
                    unload = unload + 1
            if unload:
                result = result + u'|Ref Cleaned'
        
        print u'====================ref载入情况检测===================='
        
        refUnloadInfo=[]
        
        if refNodes:
            for ref in refNodes:
                check = mc.referenceQuery(ref,isLoaded = 1)
                if check==False:
                    refUnloadInfo.append(ref)
        
        if refUnloadInfo: 
            print u'\n'
            mc.warning(u'======本文件发现Unload模式的参考，请检查文件======') 
            for ref in refUnloadInfo:        
                print(u'======【%s】未载入参考，请检查文件======'%ref) 
            print u'\n'
            mc.error(u'======本文件发现Unload模式的参考，请检查以上文件参考======')

        print u'====================ref 开始检测简模参考 ===================='
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        refNJE=[]
        refPJE=[]
        for i in range(len(refNodes)):
            if '/Projects/YODA/Reference/' in refPaths[i]:
                refNJE.append(refNodes[i])
                refPJE.append(refPaths[i])
        if refNJE:
            mc.warning(u'====================文件中有简模参考，请检查文件，并修改====================')
            for j in range(len(refNJE)):
                mc.warning(u'====================【%s】为简模参考路径【%s】,请检查文件====================' %(refNJE[j], refPJE[j]))
            mc.error(u'文件中有简模参考，请检查文件，并修改')
        
        print u'====================ref 已检测简模参考 ===================='
        '''
        shareNodes = mc.ls('sharedReferenceNode',type = 'reference')
        if shareNodes:
            print u'\n'
            print u'======本文件发现ShareNodes模式的参考，请修改为正常模式的参考======'
            print u'\n'
            mc.error(u'======本文件发现ShareNodes模式的参考，请修改为正常模式的参考======')
        '''
        print u'====================ShareNodes检测==================='

        #sk_animFileCheck.sk_animFileCheck().shotAssetTextureCheck()
        print u'====================LaserShots检测==================='        
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo() 
 
        if shotInfo[0] in ['yd']:
            GDC_checkin.GDC_checkin().GDC_LaserShotCheck(1,1)  
        
        print u'====================LaserShots检测完毕==================='
        print u'====================贴图信息情况检测===================='

        print u'====================文件格式检测========================'
        if shotInfo[0] in ['yd']:
            self.FileNameCheck('ma')
        else:
            self.FileNameCheck('mb')
        print u'====================文件格式检测完毕==================='
        print u'====================vectorRenderGlobals节点检测清理开始==================='
        vct=mc.ls(type='vectorRenderGlobals',l=1)
        if vct:
            for vc in vct:
                try:
                    mc.delete(vc)
                except:
                    mc.warning(u'【%s】节点无法删除，请检查文件'%vc)
            print u'===============已清理【vectorRenderGlobals】节点====================='
        else:
            print u'=============vectorRenderGlobals节点已检测========================'
        print u'====================vectorRenderGlobals节点检测清理完毕==================='
        # 处理参考
        for i in range(len(refNodes)):
            refNode = refNodes[i]
            refPath = mc.referenceQuery(refNode, f=1)
            path = refPath.lower()
            # 最优先
            # 非标准参考转标准参考
            if '_c_h_ms_anim.mb' in path:
                newPath = path.replace('_c_h_ms_anim.mb','_h_ms_anim.mb')
                # 替换参考

                mc.file(newPath, loadReference = refNodes[i])
            # _ng_参考
            if '_ng_h_ms_anim.mb' in path:
                newPath = path.replace('_ng_h_ms_anim.mb','_h_ms_anim.mb')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])

        print u'=====================检测高低模参考开始====================='
        '''
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRN=refInfo[0][0]
        refPath = refInfo[1][0]
        refErr=[]
        if refPath:
            for i in range(len(refPath)):
                refshot=refPath[i].split('/')[-1].split('_')[1]
                if re.search(r"\d{6,}(.*)$", refshot) and refRN[i].split('_')[-1][0]!='c':
                    id=re.search(r"\d{6,}(.*)$", refshot).group(1)
                else:
                    mc.error(u'====文件中有参考的相机，请检查文件==========')
                if id:
                    idNum=refshot.split(id)[0][-1]
                    if idNum=='6':
                        refErr.append(refRN[i])
        if refErr:
            mc.warning(u'======================文件中有高低模参考，请检查以下参考，请联系前期，将需要的树置于场景中==============')
            for err in refErr:
                print(u'======================【%s】======================='%err)
            mc.error(u'======================文件中有高低模参考，请联系前期，将需要的树置于场景中==============')
        print u'=====================检测高低模参考已完毕====================='
        '''
        print u'=====================参考修正完毕====================='
        print u'=====================检测高模参考开始====================='
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        refError=[]
        if refPaths:
            for i in range(len(refPaths)):
                shortname=refPaths[i].split('/')[-1]
                if '_h_ms_' not in shortname:
                    refError.append(refPaths[i])
        if refError:
            mc.warning(u'=====================下列参考有问题，请检查(非 _h_ms参考路径）=====================')
            print refError
            mc.error(u'=====================参考有问题，请检查以上参考路径，并修改(非 _h_ms参考路径）=====================')

        sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig()
        
        print u'==================Ref Info 处理完毕=================='
        
        # FPS
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('FPS',3)
        # frame
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame',3)
        # 7068 集修改 ce7065043001JaySwamp 角色属性
        self.nj_ModFInfo(0)
        print u'=====================镜头标准化完毕====================='
        # 7068 集修改 ce7065043001JaySwamp 角色属性
        # 转换草坪属性（新 旧）
        self.nj_LawnSwitch()
        # 清理孙望参考
        # 处理参考
        for i in range(len(refNodes)):
            refNode = refNodes[i]
            print '-------------'
            print refNode
            refPath = mc.referenceQuery(refNode, f=1)
            path = refPath.lower()
            # 清理外部参考
            shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo() 
            if shotInfo[0]=='csl':
                if 'shunliu' not in path:
                    refExist = mc.referenceQuery(refPath,rfn=1)
                    mc.file(rfn=refExist , removeReference=1)
                # 转换参考
                if '/rigging/' in path:
                    newPath = path.replace('/rigging/','/master/')
                    newPath = newPath.replace('_rg.','_ms_anim.')
                    # 替换参考
                    mc.file(newPath, loadReference = refNodes[i])
                
        print u'====================参考整理完毕===================='
#删除文件中bake相机
        cam= 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])  + '_' + str(shotInfo[3])+'_baked'
        if mc.ls(cam,l=1) and camcheckin==1:
            mc.delete(cam)

        print u'====================更新相机========================'
        if camcheckin==1:
            if shotInfo[0]=='ice':
                sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1,shotType = 2)
            else:
                sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1,shotType = 3)

            print u'==================camera传输完毕=================='

        # 处理组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)

        #删除文件中非bake相机
        if camcheckin==1:
            cam= 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])  + '_' + str(shotInfo[3])
            try :
                mc.delete(cam)
            except:
                pass

        #YODA项目需要导入相机
        #导入相机
        print u'导入相机'
        if camcheckin==1:
            sk_sceneTools.sk_sceneTools().sk_sceneImportCameraF(3)


        print u'====================相机更新完毕========================'
        print u'====================开始约束清理===================='
        if Constraints==1:
            sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()

        print u'====================约束清理完毕===================='

        print u'====================删除天空球开始===================='
        skys='MSH_starfield1_1'        
        objs=mc.ls(skys,l=1)+mc.ls(('*:'+skys),l=1)       
        if objs:
            for obj in objs:
                if '|' in obj:
                    Gro=obj.split('|')[1]
                    try:
                        mc.delete(Gro)
                    except:
                        pass
        print u'====================删除天空球完毕===================='
                   

        print mc.ls(type='unknown')
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean(1)
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                if mc.ls(node):
                    mc.lockNode(node, l=0)
                    mc.delete(node)
        print mc.ls(type='unknown')
        
        print u'==================垃圾节点清理完毕=================='
        #bake 蛇头
        self.nj_hotBake()
        # 清理层和渲染层
        try:
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        except:
            print u'===请检查文件masterLayer，名字异常==='
            mc.error(u'===请检查文件masterLayer，名字异常===')


        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
        self.gdc_LayerCheck()
        
        print u'=================显示层|渲染层处理完毕================='
        
        print u'=================处理显示层================='
        self.gdc_LayerDelete()
        print u'=================显示层处理完毕================='

        #Tpose检测
        
        #GDC_checkin.GDC_checkin().GDC_TPOSECheck(3)

        #print u'=================Apose检测完毕================='
        

        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()

        #导入相机动画
        #self.CamanimImp(3)
        #相机打组
        if camcheckin==1:
            camGRP='|CAM_GRP'
            mc.parent(cam,camGRP)

        print u'=================outLiner重新分组================='
  
    #------------------------------#
    # 前期用工具，修改非法字符系列
    #------------------------------#
    # 修改指定目录文件[梁宇]
    def checkFolderNameConfig(self, rootPath):
        noNeedSign = ['-',' ','(',')','{','}']
        fileName = ''
        folderList = mc.getFileList(folder= rootPath)
        if not folderList:
            return 0
        for folderPath in folderList:
            fileList =  mc.getFileList(folder= (rootPath + folderPath + '/'))
            if not fileList:
                continue
            for fileName in fileList:
                newName = fileName
                for sign in noNeedSign:
                    if sign in newName:
                        newName = newName.replace(sign,'_')
                mc.sysFile((rootPath + '/' + folderPath + '/' + fileName),rename = (rootPath + '/' + folderPath + '/' + newName))
            
#导出相机动画
    def CamanimExr(self,shotType = 3):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotname=''
        if shotType == 3:
            shotname=shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        if shotType == 2:
            shotname=shotInfo[1] + '_' + shotInfo[2]
        temppath='D:/Info_Temp/YD/exr/' + shotname+ '/'
        mc.sysFile(temppath, makeDir=True)
        cam='cam_'+shotname
        starttime=mc.playbackOptions(q=1, minTime=1)-12
        endtime=mc.playbackOptions(q=1, maxTime=1)+12
        io = (starttime, endtime)
        fiename=shotname+'_cam.anim'
        if mc.ls(cam):
            mc.currentTime(starttime)
            mc.setKeyframe(cam)
            locn=cam+'_locator'
            if mc.objExists(locn):
                mc.delete(locn)
            loct=mc.CreateLocator()
            mc.rename(loct,locn)
            point=mc.pointConstraint(cam,locn,name=shotname+'_pointConstraint')
            poinp=mc.parentConstraint(cam,locn,name=shotname+'_parentConstraint')
            mc.select(locn)
            mc.bakeResults(locn,t=io,simulation=1,sampleBy=1,disableImplicitControl=1,preserveOutsideKeys=1,sparseAnimCurveBake=0,removeBakedAttributeFromLayer=0,bakeOnOverrideLayer=0,controlPoints=0,shape=0)
            mc.select(locn)
            mc.file((temppath+fiename),options="precision=17;intValue=17;nodeNames=1;verboseUnits=0;whichRange=1;range=0:10;options=keys;hierarchy=below;controlPoints=0;shapes=1;helpPictures=0;useChannelBox=0;copyKeyCmd=-animation objects -option keys -hierarchy below -controlPoints 0 -shape 1 ",f=1,type="animExport",preserveReferences=1,es=1)
            if mc.objExists(locn):
                mc.delete(locn)
        return 0

#导入相机动画

    def CamanimImp(self,shotType = 3):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotname=''
        if shotType == 3:
            shotname=shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        if shotType == 2:
            shotname=shotInfo[1] + '_' + shotInfo[2]
        temppath='D:/Info_Temp/YD/exr/' + shotname+ '/'
        mc.sysFile(temppath, makeDir=True)
        cam='cam_'+shotname
        fiename=shotname+'_cam.anim'
        if mc.ls(cam) and os.path.exists(temppath+fiename):
            mc.select(cam)
            mc.file((temppath+fiename),i=1,pr=1)
        return temppath

#删除多余层
    def gdc_LayerDelete(self):
        info=mc.ls(type='displayLayer',l=1)
        if mc.objExists('defaultLayer'):
            info.remove('defaultLayer')
        if mc.objExists('norender'):
            info.remove('norender')
        try:
            mc.delete(info)
        except:
            pass
        return 0
#检测非norender且未显示的层

    def gdc_LayerCheck(self):
        info=mc.ls(type='displayLayer',l=1)
        if mc.objExists('defaultLayer'):
            info.remove('defaultLayer')
        if mc.ls('norender',type='displayLayer'):
            info.remove('norender')
        nodis=[]
        if info:
            for dis in info:
                if mc.objExists(dis+'.v') and mc.getAttr(dis+'.v')==False:
                    nodis.append(dis)
        if nodis:
            for di in nodis:
                mc.warning(u'【%s】这个层为非norender命名，且未显示，请检查文件并修改'%di)
            mc.error(u'文件中有上述非norender且未显示的层，请检查并修改')
        return 0
#检测文件格式
    def FileNameCheck(self,filetyp='mb'):
        filename=mc.file(q=1,shn=1,sn=1)
        if filename and '.' in filename:
            fileType=filename.split('.')[-1]
            if fileType.lower()!=filetyp:
                mc.warning(u'================文件格式不正确，请修改================')
                mc.error(u'文件格式不正确，请修改,应该是【%s】格式)'%filetyp)
        else:
            mc.error(u'文件名不正确，请检查并修改')
        return 0
#删除声音节点
    def AudiosDelete(self):
        Audios=mc.ls(type='audio',l=1)
        if Audios:
            for audio in Audios:
                try:
                    mc.delete(audio)
                except:
                    mc.warning(u'=============未能删除Audio【%s】，请检查文件===================' %audio)
                    mc.error(u'=============声音文件无法删除，请检查文件=======================')
        print u'===================已删除声音文件===================='
        return 0
#7068集修改角色属性
    def nj_ModFInfo(self,server=0):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refSpace=refInfo[-1][0]
        modInfo=[]
        for i in range(len(refSpace)):
            if shotInfo[1] in ['E7068'] and 'ce7065043001JaySwamp' in refSpace[i] and mc.objExists(refSpace[i]+':Lf_ature1_ctrl') and mc.objExists(refSpace[i]+':Lf_ature1_ctrl'+'.shoulderpad_L_switch'):
                modInfo.append(refSpace[i]+':Lf_ature1_ctrl')
        if modInfo:
            for info in modInfo:
                mc.setAttr((info + '.shoulderpad_L_switch'),1)
        if modInfo and server==1:
            fileName=mc.file(q=1,shn=1,sn=1)
            tempPath='D:/TempInfo/anim/'
            mc.file(rename=tempPath+fileName)
            mc.file(save=1,type ='mayaBinary',f = 1)
        return modInfo
# 修改草坪
# 'E7065','E7066','E7071' 及'E7070_Q0010_S0010','E7070_Q0280_S0113' 新草坪
#'E7068' 旧草坪
# 集除以上两个镜头，均用旧草坪
    def nj_LawnSwitch(self):
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        refNameSpace = refInfo[2][0]
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        grassRefs=[]
        for i in range(len(refNameSpace)):
            master=refNameSpace[i]+':Master'
            if 'se7065007001TempleOfAirjitzuNinjaHQEXT' in refNameSpace[i] and mc.objExists(master) and mc.objExists(master+'.lawn_switch'):
               grassRefs.append(master)
        if not grassRefs:
            pass
        for ms in grassRefs:
            if shotInfo[1] in ['E7065','E7066','E7071'] or (shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]) in ['E7070_Q0010_S0010','E7070_Q0280_S0113']:
                mc.setAttr((ms+'.lawn_switch'),1)

            if shotInfo[1] in ['E7068','E7070'] and (shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]) not in ['E7070_Q0010_S0010','E7070_Q0280_S0113']:
                mc.setAttr((ms+'.lawn_switch'),0)
        if grassRefs:
            result=grassRefs
        else:
            result=0
        return result
# 原始组显示属性传递到下一层级
    def DisAnmSet(self):
        GRPS=[]
        GRPNS=[]
        objs=mc.ls(tr=1,l=1)
        if objs:
            for obj in objs:
                if '|' in obj and len(obj.split('|'))==2 and not mc.listRelatives(obj,s=1) and mc.objExists(obj+'.visibility') and mc.listRelatives(obj,c=1,type='transform') and 'cam_' not in mc.listRelatives(obj,c=1,type='transform',f=1)[0]:
                    GRPS.append(obj)
        if not GRPS:
            pass
        for ob in GRPS:
            gr=mc.listRelatives(ob,c=1,type='transform',f=1)
            GRPNS.append(gr[0])
        for i in range(len(GRPS)):
            VisG=GRPS[i]+'.visibility'
            VisC=GRPNS[i]+'.visibility'
            if mc.keyframe(VisG,q=1) and mc.keyframe(VisC,q=1):
                mc.error(u'=============【%s】【%s】均有Vis K帧，请修改后再上传=============')

            if mc.keyframe(VisG,q=1) and not mc.keyframe(VisC,q=1):
                mc.copyKey(VisG)
                try:
                    mc.pasteKey(VisC)
                    mc.cutKey(VisG)
                    mc.setAttr(VisG,1)
                except:
                    mc.error(u'【%s】被锁，无法粘贴显示信息'%VisC)
            if not mc.keyframe(VisG,q=1) and not mc.keyframe(VisC,q=1):
                VisNum=mc.getAttr(VisG)
                if VisNum==0:
                    try:
                        mc.setAttr(VisC,VisNum)
                    except:
                        pass
                    try:
                        mc.setAttr(VisG,1)
                    except:
                        pass
        return 0
# 后台bake
#  Author : hanhong
    def nj_hotBake(self):
        import idmt.pipeline.db
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shot=shotInfos[0]+'_'+shotInfos[1]+'_'+shotInfos[2]+'_'+shotInfos[3]
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        endFrame = anim.frmEnd
        startFrame = anim.frmStart
        io = ((startFrame-12), (endFrame+12))
        DYs=[]
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        refNamespace=refInfo[2][0]
        for ns in refNamespace:
            if 'ce' in ns and mc.ls(ns+':Hat') and mc.objExists(ns+':Hat'+'.S_DY') and mc.getAttr(ns+':Hat'+'.S_DY')==1:
                DYs.append(ns)
        if not DYs:
            pass
        bakeJoints=[]
        joints=mc.ls(type='joint',l=1)
        if not joints:
            mc.warning(u'============文件中没有joint物体===============')
            pass
        joinB=[]
        for i in range(len(joints)):
            for j in range(len(DYs)):
                if DYs[j] in joints[i] and joints[i] not in joinB:
                    joinB.append(joints[i])
        if not joinB:
            pass
        for joi in joinB:
            if mc.objExists(joi+'.clothbake'):
                bakeJoints.append(joi)
        if not bakeJoints:
            pass
        else:
            print 'u===========开始bake蛇头============'
            mc.select(bakeJoints)
            mc.bakeResults(bakeJoints,t=io,simulation=1,sampleBy=1,disableImplicitControl=1,preserveOutsideKeys=1,sparseAnimCurveBake=0,removeBakedAttributeFromLayer=0,bakeOnOverrideLayer=0,controlPoints=0,shape=0)
            print 'u===========蛇头bake 结束============'
            #mc.select(DYs)
        if bakeJoints:
            result=bakeJoints
        else:
            result=0
        return result
#

    def njcheckboxPrompt(self):
            # Get the dialog's formLayout.
            #
            form = mc.setParent(q=True)
            # layoutDialog's are not resizable, so hard code a size here,
            # to make sure all UI elements are visible.
            #
            mc.formLayout(form, e=True, width=300)
            t = mc.text(l=u'请确保在镜头开始前或结束后有对移动中的物体和相机进行补帧（前后各多10帧')
            b1 = mc.button(l='Abort', c='mc.layoutDialog( dismiss="Abort" )' )
            b2 = mc.button(l='Skip', c='mc.layoutDialog( dismiss="Skip" )' )
            b3 = mc.button(l='Continue', c='mc.layoutDialog( dismiss="Continue" )' )
            cb1 = mc.checkBox(label='Remember my choice')
            spacer = 5
            top = 5
            edge = 5
            mc.formLayout(form, edit=True,
                                            attachForm=[(t, 'top', top), (t, 'left', edge), (t, 'right', edge), (b1, 'left', edge), (b3, 'right', edge), (cb1, 'left', edge), (cb1, 'bottom', spacer)],
                                            attachNone=[(t, 'bottom'), (b1, 'bottom'), (b2, 'bottom'), (b3, 'bottom'), (cb1, 'right')],
                                            attachControl=[(b1, 'top', spacer, t), (b2, 'top', spacer, t), (b3, 'top', spacer, t), (cb1, 'top', spacer, b1)],
                                            attachPosition=[(b1, 'right', spacer, 33), (b2, 'left', spacer, 33), (b2, 'right', spacer, 66), (b3, 'left', spacer, 66)])

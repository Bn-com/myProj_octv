#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2016/4/5'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import re, os, sys,time
import maya.cmds as mc
import maya.mel as mel
from pymel.core import *
import pyodbc
import idmt.pipeline
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig;reload(sk_infoConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig;reload(sk_referenceConfig)
from idmt.maya.py_common import sk_checkCommon;reload(sk_checkCommon)
class mi_pipelineProcs(object):
    def __init__(self):
        pass
    def mi_queryMsSQL_mutipleCameInfo(self,project, ep,sc):#===数据库读取多景别相机的标记值==============
        try:
            cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EReader;PWD=123123'%(project))
        except:
            return None
        cursor = cnxn.cursor()
        cmd_sql = '''select PCPE.pcpe_edit6 from idmtPlex_MiniTiger.dbo.tb_PageColumnProjectEdit PCPE
        inner join idmtPlex_MiniTiger.dbo.TB_Anim_Task TAT on PCPE.pcpe_taskid=TAT.task_id
        inner join idmtPlex_MiniTiger.dbo.TB_Anim TA on TAT.anim_id=TA.anim_id
        where PCPE.pcpe_tasktype='anim' and TA.anim_ep=\'%s\' and TA.anim_sc=\'%s\''''%(ep,sc)
        sf_ef = cursor.execute(cmd_sql).fetchone()
        if sf_ef and sf_ef[0] == str('是'):return True
        else: return None
    def mi_multicam_upload2server(self,batchUpadate=1,info=2,abcToggle=True):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        shotID = u'_'.join(shotInfo[:info+1])
        anim = idmt.pipeline.db.GetAnimByFilename(shotID)
        proStartFrame = int(anim.frmStart)
        proEndFrame = int(anim.frmEnd)
        #清理unkown 节点
        sk_checkCommon.sk_checkTools().checkDonotNodeCleanBase(0)
        #shot_dir = "_".join(shotInfo[:info+1])
        # serve目录
        camServerBasePath = "//file-cluster/GDC/Projects/%s/Project/scenes/Animation/episode_%s/episode_camera/" % (projectInfo,shotInfo[1])
        # 更新server文件路径
        camFile_onServer = u'%smi_%s_%s_cam[_(near)(far)(mid)]*.ma' % (camServerBasePath,shotInfo[1],shotInfo[2])
        # 先删除cam参考
        p_cam_path = re.compile(camFile_onServer)
        shot_refs = listReferences()
        for each_ref in shot_refs:
            if p_cam_path.search(each_ref.path):each_ref.remove()
        # 检查bake相机
        camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
        # 获取真正cam 居然有|cam_102_001|cam_102_001的情况
        print camSourceName
        camList = ls('%s*'%camSourceName,type='transform')
        p_shotCam_name = re.compile(u'cam_%s_%s[_(far)(mid)(near)]*'%(shotInfo[1],shotInfo[2]))
        multiCams = []
        needCam = ''
        if not camList:
            error(u'=======================文件里没有对应镜头的camera===========================')
            return
        for eachOne in camList:
            if eachOne.nodeType() == u'stereoRigTransform' and eachOne.name().find(u'_baked') ==-1: multiCams.append(eachOne)
            elif eachOne.nodeType() == u'transform' and eachOne.childAtIndex(0).nodeType() == u'camera': multiCams.append(eachOne)
        if len(multiCams) > 3: error(u' ==========more than 3 cameras in scene file ======================')
        # baked camera
        for each_cam in multiCams:
            #from pymel.core import *
            #each_cam = multiCams[0]
            camBakeName = each_cam.name() + '_baked'
            camSelect = 0
            shotInfos = []
            if ls(camBakeName): delete(camBakeName)
            exp = each_cam.listConnections(d=1,type='expression')
            if exp: delete(exp)#删除残留表达式
            #=======specify camera file path on server ================================
            p_cam_category = re.compile( u'(near)|(far)|(mid)$')#p_cam_category = re.compile( u'[^_]+$')
            cam_category = u''
            if p_cam_category.search(each_cam.name()): cam_category = '_%s'%(p_cam_category.search(each_cam.name()).group())
            camServerPath = '%s%s_cam%s.ma'% (camServerBasePath,shotID,cam_category)
            cam_abc_serverPath = u'%s%s_cam%s.abc'%(camServerBasePath,shotID,cam_category)
            select(each_cam.longName(),r=True)
            mel.eval('source \"//file-cluster/GDC/Resource/Support/Maya/2013/zwCameraImportExport.mel\"')
            mel.eval('zwBakeCamera')
            select(camBakeName)
            # 相机Export
            from idmt.maya.py_common import sk_hbExceptCam
            reload(sk_hbExceptCam)
            sk_hbExceptCam.sk_hbExceptCam().HbExceptSelectReCam(projectInfo ,0,str(proStartFrame),batchUpadate,camSelect,shotInfos)
            # 临时目录
            camTempPath = "//file-cluster/GDC/Projects/%s/%s_Scratch/TD/SetCam/%s/cam_%s_%s%s_baked.ma" %(projectInfo,projectInfo,shotInfo[1],shotInfo[1],shotInfo[2],cam_category)
            mel.eval('zwSysFile \"copy\" \"' + camTempPath + '\" \"' + camServerPath + '\" 1')
            print u'====================成功更新camera到服务器端===================='
             #===export camera abc file to server======================
            if abcToggle:
                select(camBakeName,r=True)
                #proStartFrame = int(anim.frmStart)
                #proEndFrame = int(anim.frmEnd)
                if not pluginInfo('AbcExport',l=True,q=True):loadPlugin('AbcExport')
                # AbcExport(j="-frameRange %d %d -stripNamespaces -worldSpace -sl -file  %s"
                #           %(proStartFrame,proEndFrame,cam_abc_serverPath))
                mc.AbcExport(j="-frameRange %d %d -stripNamespaces -worldSpace -eulerFilter -root %s -file  %s"
                  %(proStartFrame-5,proEndFrame+5,PyNode(camBakeName).longName(),cam_abc_serverPath))
                print u'========================camera abc file  upload to server ================================'
            # 删除bake后的相机
            delete(camBakeName)
            select(cl=1)
            # 成功代码
    def mi_get_camsOnServer(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        # serve目录
        camServerPath = sk_infoConfig.sk_infoConfig().checkCameraServerPath()
        #camServerPath = "//file-cluster/GDC/Projects/"+ projectInfo + "/Project/scenes/Animation/episode_" + shotInfo[1] + "/episode_camera/"
        shot_cam_file = u''
        info = 2
        shotID = u'_'.join(shotInfo[:info+1])
        p_shotId = re.compile(u'%s[_(far),(mid),(near)]*'%(shotID))
        shot_camFiles = []
        for each_camFile in os.listdir(camServerPath):
            if p_shotId.search(each_camFile) and os.path.splitext(each_camFile)[-1] == u'.ma': shot_camFiles.append(u'%s%s'%(camServerPath,each_camFile))
        return shot_camFiles
    def mi_multiCam_toggle(self,cam_category,allow_multiCam = None):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        use_cam = ''
        for each in self.mi_get_camsOnServer():
            if each.find(u'_%s' % cam_category) != -1: use_cam = each
        camServerPath = u'%s/' % os.path.split(use_cam)[0]
        p_cam_path = re.compile(u'%smi_%s_%s_cam[_(near)(far)(mid)]*.ma' % (camServerPath,shotInfo[1],shotInfo[2]))
        cam_refs = [each_ref for each_ref in listReferences() if p_cam_path.search(each_ref.path)]
        if len(cam_refs) >1: # 当场景理有多个相机参考时，需要选择要替换的相机
            if allow_multiCam:
                mc.file(use_cam,reference = 1,ignoreVersion=1,namespace='CAM_%s'%(cam_category))
                return
            if not selected(): error(u'===========there more than one Cam Ref files in ,please select one to replace===================')
            elif not selected()[0].isReferenced() or not selected()[0].referenceFile() in cam_refs:error(u'==== please select cam ref to replace========')
            selected()[0].referenceFile().replaceWith(use_cam)
        elif len(cam_refs)==1: # 当场景里只有一个参考的相机的时候，要看是否允许多相机，如果允许，那么就再参考一个进来，如果不允许，那么就是替换这个相机
            if not allow_multiCam:
                cam_refs[0].replaceWith(use_cam)
                print(u'==============camera change to %s =================') % cam_category
                #return
            else:
                mc.file(use_cam,reference = 1,ignoreVersion=1,namespace='CAM_%s'%(cam_category))
        # 无则导入参考相机
        elif not cam_refs: mc.file(use_cam,reference = 1,ignoreVersion=1,namespace='CAM')
    def mi_export_camAbc2Server(self,sourceCame,cam_abc_serverPath,shotType=2):#===========导出摄像机的abc到指定路径
        import idmt.pipeline
        shotID = u'_'.join(sceneName().basename().split(u'_')[:shotType+1])
        anim = idmt.pipeline.db.GetAnimByFilename(shotID)
        proStartFrame = int(anim.frmStart)-50
        proEndFrame = int(anim.frmEnd)+10
        #===export camera abc file to server======================
        select(PyNode(sourceCame),r=True)
        #proStartFrame = int(anim.frmStart)
        #proEndFrame = int(anim.frmEnd)
        if not pluginInfo('AbcExport',l=True,q=True):loadPlugin('AbcExport')
        mc.AbcExport(j="-frameRange %d %d -stripNamespaces -worldSpace -eulerFilter -root %s -file  %s"
                  %(proStartFrame-5,proEndFrame+5,PyNode(sourceCame).longName(),cam_abc_serverPath))
        print u'========================camera abc file  upload to server ================================'
    def mi_export_abc_proc(self,localPath,frame_min,frame_max,shotType=2,server=0,userAttr=u'alembic'):#=============按照namespace 导出每个namespace里缓存物体的abc==========================
        #localPath = sk_infoConfig.sk_infoConfig().alembicLocalPath(2)
        #frame_min = playbackOptions(min=True,q=True)-50
        #frame_max = playbackOptions(max=True,q=True) +3
        get_ns_inRef =  self.mi_refNS_list()
        self.mi_export_abc_baseOn_ns(localPath,frame_min,frame_max,shotType,server,userAttr,*get_ns_inRef)
    def mi_cacheOBjsInfo_from_ns(self,excludeGrp,userAttr=u'alembic',*spec_ns):#============get cache objects informations by namespace ======================
        cacheObjs_in_ns = {}#spec_ns = get_ns_inRef
        p_excludeGrp = re.compile(u'|'.join([u'(%s)'% each_nm for each_nm in excludeGrp]),re.I)###正则表达式，列表解析，格式化字符串 ,pymel四种技能的合体语句====课=========
        for each_ns in spec_ns: ###
            temp_list  = [eachObj for eachObj in namespaceInfo(each_ns,lod=True) if eachObj.nodeType()==u'transform' and eachObj.hasAttr(userAttr) and not p_excludeGrp.search(eachObj.longName())]
            if temp_list: cacheObjs_in_ns[each_ns] = temp_list
            else: print '===============There isno cache objects  in the scene====================='
        return cacheObjs_in_ns
    def mi_refNS_list(self):#================get namespace of each ref=================================================
        ref_ls = listReferences()
        return [each_ns.namespace for each_ns in ref_ls]
    def mi_export_abc_baseOn_ns(self,abcPath,frame_min,frame_max,shotTp=2,server=0,userAttr=u'alembic',*ns_list):#================export abc cache file by namespace list ===========================
        exclude_grp = [u'DEFORMERS',u'DYN_FUR']#====在这添加了需要筛选掉的组，这些组内的物体，不需要出缓存
        abcMeshes_in_ns = self.mi_cacheOBjsInfo_from_ns(exclude_grp,userAttr,*ns_list)
        shotID = u''
        if sceneName():
            scene_bn = os.path.splitext(sceneName().basename())[0]
            if len(scene_bn.split(u'_'))> shotTp: shotID = u'_'.join(scene_bn.split(u'_')[:shotTp+1])
            else:shotID = scene_bn
        else:shotID = u'testExport'
        for each_ns in abcMeshes_in_ns:
            print (u'\n===============%s:::::::::::::: ready for generate abc cache ===================\n' % (time.strftime("%Y-%m-%d %H:%M:%S")))
            abc_file_name = u'%s_%s_%s.abc' % (shotID,each_ns,userAttr)
            root_join_meshesLs = u' -root %s' %( u' -root '.join([eachMesh.longName() for eachMesh in abcMeshes_in_ns[each_ns]]))
            #select(abcMeshes_in_ns[each_ns])
            #abcPath = localPath
            if not pluginInfo('AbcExport',l=True,q=True):loadPlugin('AbcExport')
            mc.AbcExport(j="-frameRange %s %s -uvWrite -worldSpace -writeVisibility  -eulerFilter %s -file %s"
            %(frame_min,frame_max,root_join_meshesLs,abcPath + abc_file_name))
            print (u'============================= ABC Cache %s Exported ================================' % (abc_file_name))
            print (u'\n===============%s:::::::::::::: end generated  abc cache===================\n' % (time.strftime("%Y-%m-%d %H:%M:%S")))
            if server == 1:
                import idmt.maya.commonCore.core_mayaCommon.sk_infoConfig as skinc;reload(skinc)
                serverPath = skinc.sk_infoConfig().alembicServerPath()
                up2serv_cmd = u'zwSysFile "copy" "%s%s" "%s%s" true' % (abcPath,abc_file_name,serverPath,abc_file_name)
                mel.eval(up2serv_cmd)
                print (u'============================ABC: %s up2server ================================' % (abc_file_name))
                print (u'===========================abc exported  whole time range::::::: 【%d】 frames=========================' % (int(frame_max)-int(frame_min)))
    def mi_cacheObjsInfo_from_ref(self):#===== get cache objects informations ,in each reference grp ======return cache file spechars and obj list ======
        ref_ls = listReferences()
        ref_cachObj_info = {}
        for each_ref in ref_ls:
            #refNode_ns = each_ref.namespace
            list_ref_contents = each_ref.nodes()
            list_cach_obj_temp =  [eachObj for eachObj in list_ref_contents if eachObj.nodeType()==u'transform' and eachObj.hasAttr(u'alembic')]
            if list_cach_obj_temp: ref_cachObj_info[each_ref.namespace] = list_cach_obj_temp
        return ref_cachObj_info

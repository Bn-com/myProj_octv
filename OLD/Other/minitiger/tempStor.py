import maya.cmds as mc
from pymel.core import *
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
import idmt.pipeline
def list_shotCam(shotMarkNum=2): # list the cameras of the shot necessary
    #shotMarkNum = 2
    sn_base_spl = sceneName().basename().split(u'_')
    shot_ID = u'_'.join(sn_base_spl[:shotMarkNum+1])
    shot_mark_code = u'_'.join(sn_base_spl[1:shotMarkNum+1])
    sht_cam_nm = u'cam_{}'.format(shot_mark_code)
    # 获取真正cam 居然有|cam_102_001|cam_102_001的情况
    print sht_cam_nm
    camList = ls('%s*'%sht_cam_nm,type='transform')
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
    return multiCams
def expShtCam(shotMarkNum=2):# export select camera to project scratch direction
    # baked camera
    shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
    projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
    ls_cams = list_shotCam()
    cam_stor_dir = ur'//file-cluster/GDC/Projects/{0}/{0}_Scratch/Layout/cam_export/episode_{1}'.format(projectInfo,shotInfo[1])
    if not os.path.isdir(cam_stor_dir):os.mkdir(cam_stor_dir)
    shotID = u'_'.join(shotInfo[:shotMarkNum+1])
    for each_cam in ls_cams:
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
        #camServerPath = '%s%s_cam%s.ma'% (camServerBasePath,shotID,cam_category)
        cam_exp_dir = '{0}/{1}_cam{2}.mb'.format(cam_stor_dir,shotID,cam_category)
        select(each_cam.longName(),r=True)
        mel.eval('source \"//file-cluster/GDC/Resource/Support/Maya/2013/zwCameraImportExport.mel\"')
        mel.eval('zwBakeCamera')
        select(camBakeName)
        exportSelected(cam_exp_dir,force=True,type=u'mayaBinary')
def mi_msfile_im_relativesCams(projs_wksp = ur'\\file-cluster\gdc\Projects',shotMarkNum =2):
    shot_section = u'ly'
    shotInfomation = sk_infoConfig.sk_infoConfig().checkShotInfo()
    proj_name = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfomation[0])
    asset_name = sceneName().basename()#asset_name = 'mi_s023001CastleLaboratory_h_rg.mb'
    shots_lsInfo = cmds.idmtService('GetAnimsInAsset', asset_name)
    shot_list = [u'{3}_{0}_{1}_{2}'.format(each_shotID.split(u'_')[0],each_shotID.split(u'_')[2],shot_section,shotInfomation[0]) for each_shotID in shots_lsInfo.split(u'|')]
    for eachShot in shot_list[:2]:
        shtNm_spl = eachShot.split(u'_')
        p_shtnm = re.compile(u'{0}_[a-z0-9]+.m[ab]'.format(eachShot))
        ly_file_searchDir = ur'{0}\{1}\Project\scenes\Animation\episode_{2}\scene_{3}\layout'.format(projs_wksp,proj_name,shtNm_spl[1],shtNm_spl[2])
        shotID = u'_'.join(shtNm_spl[:shotMarkNum+1])
        if not os.path.isdir(ly_file_searchDir):
            warning(u'===================={} file is not exist===================='.format(eachShot))
            continue
        exact_lyf = u''
        for dir_path,sub_path,files in os.walk(ly_file_searchDir):
            for each_file in files:
                lyf_path = os.path.join(dir_path,each_file)
                if p_shtnm.search(each_file) and lyf_path.find(u'history') == -1: #exact_lyf = lyf_path
                    print lyf_path
                    exact_lyf = lyf_path
                    pythonCmdStr = u"\"python(\\\"import Other.minitiger.mi_kit_pre as mkp;mkp.expShtCam()\\\");\""
                    batchRun_cmd(exact_lyf,pythonCmdStr)
                    exp_cam_path = ur'{0}\{1}\{1}_scratch\Layout\cam_export\episode_{2}\{3}_cam.mb'.format(projs_wksp,proj_name,shtNm_spl[1],shotID)
                    if os.path.isfile(exp_cam_path):
                        im_cam_nodes = importFile(exp_cam_path,ns=u'CHK_RNDCam_{0}_{1}'.format(shtNm_spl[1],shtNm_spl[2]),returnNewNodes=True)
                        for each_im_nd in im_cam_nodes:
                            if each_im_nd.nodeType() == u'camera': each_im_nd.renderable.set(0)
                            if each_im_nd.nodeType() == u'stereoRigCamera':each_im_nd.renderable.set(1)
                        print u'{1:|>30}CAMERA IMPORTED:{0}{1:|>30}'.format(shotID,u'|')
                    else: print u'{1:|>30}THERE IS NO CAMERA IMPORT:{0}{1:|>30}'.format(shotID,u'|')
    rndf_svd_dir = mi_config_msf2Rnd()
    print u'{0:+>25}FILE SAVED{0:+>25}:\n{0:+>25}{1}{0:+>25}'.format(u'+',rndf_svd_dir)
    rnd_msf_cmdStr(rndf_svd_dir)
def mi_config_msf2Rnd(driveID = u'D:'):
    if not mc.pluginInfo('mtoa.mll',q=1,loaded = 1):
        mc.loadPlugin('mtoa.mll')
    import mtoa
    mtoa.core.createOptions()
    import mtoa.cmds.registerArnoldRenderer
    mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
    # 标准设置
    mc.setAttr('defaultRenderGlobals.imageFormat', 3)
    mc.setAttr('defaultArnoldDriver.halfPrecision', 0)
    # 开始处理
    shotID = sk_infoConfig.sk_infoConfig().checkShotID()
    anim = idmt.pipeline.db.GetAnimByFilename(u'mi_s002bak_h_mo')
    fpsFrame = anim.fps
    startFrame,endFrame = 1001,1001
    resW = anim.resolutionW
    resH = anim.resolutionH
    # res
    mc.setAttr('defaultResolution.width', resW)
    mc.setAttr('defaultResolution.height', resH)
    # FPS
    if fpsFrame == 25:
        mc.currentUnit(time='pal')
    if fpsFrame == 24:
        mc.currentUnit(time='film')
    if fpsFrame == 30:
        mc.currentUnit(time='ntsc')
        # 渲染范围设置
    mc.setAttr('defaultRenderGlobals.startFrame', startFrame)
    mc.setAttr('defaultRenderGlobals.endFrame', endFrame)
    # 格式命名
    # 原先调用菜单，现在直接改节点
    mc.setAttr('defaultRenderGlobals.animation', 1)
    mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
    mc.setAttr('defaultRenderGlobals.periodInExt', 1)
    mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
    mc.setAttr('defaultArnoldRenderOptions.AASamples',3)
    mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples',5)
    mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples',0)
    if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
    # arnold配置
    mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
    msf_tempStor_dir = ur'{0}/MS_RND_ALLCAMS/{1}'.format(driveID,shotID)
    if not os.path.isdir(msf_tempStor_dir):os.makedirs(msf_tempStor_dir)
    msf_tempStor_fullPath = u'{0}/{1}_RNDALLCAM.mb'.format(msf_tempStor_dir,shotID)
    renameFile(msf_tempStor_fullPath,force=True,type = u'mayaBinary')
    saveFile()
    return msf_tempStor_fullPath
def back_rnd_opt(rndCam,opt_dir):  
    import pymel.core as pm
    pm.PyNode('defaultRenderGlobals').ren.set('arnold')
    mc.RenderViewWindow()
    mc.showWindow(u'renderViewWindow')
    mc.tearOffPanel("Render View","renderWindowPanel")
    maya.mel.eval ('tearOffPanel "Render View" "renderWindowPanel" true;')
    #mel.eval('RenderIntoNewWindow;')
    mel.eval('renderWindowRenderCamera render renderView {}'.format(rndCam))
    #mel.eval('renderWindowRenderCamera render renderView  CHK_RNDCam_200_0100:cam_200_0100_bakedCenterCamShape')
    #opt_dir = ur"e:/temp/testSave.img"
    saveImag_melcmd = u"renderWindowSaveImageCallback \"renderView\" \"{}\" \"Maya IFF\" ;".format(opt_dir)
    mel.eval(saveImag_melcmd)
    #sysFile -makeDir ($imgDir + $currentLayer);
    #renderWindowRender redoPreviousRender renderView;    
    #sysFile -delete ($path + ".iff"); 
    #renderWindowSaveImageCallback "renderView" $path "Maya IFF";
def batchRun_cmd(eachFile,melCmdStr):
    #melCmdStr=u'\"polyCube;file -save;\"'
    sysTemp = os.environ['TEMP']
    logfile = u'%s/BatchProcLog%s.txt'%(sysTemp,os.path.split(eachFile)[-1].split(u'.')[0])
    maya_loc = os.getenv("MAYA_LOCATION")
    m_b_dir = ur"%s/bin\mayabatch.exe"%maya_loc
    cmdStr = ur"%s -file %s -command %s -log %s" % (m_b_dir,eachFile,melCmdStr,logfile)   
    #resulContant = os.popen(cmdStr)    
    os.system(cmdStr)

def rnd_msf_cmdStr(rnd_filepath):
    #rnd_filepath = lyf_svd_dir
    maya_loc = os.getenv("MAYA_LOCATION")
    m_rnder_dir = ur"%s/bin\render.exe"%maya_loc
    rndOpt_path = os.path.split(rnd_filepath)[0]
    rndLog_path = rnd_filepath.replace(u'.mb',u'.log')
    cmdStr = ur'{0} -r file -rd {1} -log {3} {2} '.format(m_rnder_dir,rndOpt_path,rnd_filepath,rndLog_path)
    os.system(cmdStr)
#batFile = u'%s\PrevBatchRender.bat'%(sysTemp)
#os.system(batFile)

back_rnd_opt(


shot_file_list = []
file_folder =ur'E:\projectFolder\miniTiger\sc_000\scenes\tt_fold'
for dir_path,subpaths,files in os.walk(file_folder,False):
        for each_file in files:
            shot_file_list.append(os.path.join(dir_path,each_file))

for eachFile in shot_file_list:
    batchRun_cmd(os.path.abspath(eachFile),u'\"polyCube;file -save;\"')
    print u'++++++++++++++++++++done+++++++++++++++++++++++++'



pythonCmdStr = u"\"python(\\\"import idmt.maya.DOD.DODIV.Maya.do4_batchPreviewRender as dbpr;dbpr.do4_batchProc_wholeLayoutFile()\\\");\""%(storeFolde)

for dir_path,sub_path,files in os.walk(ly_file_searchDir):
for each_file in files:
    lyf_path = os.path.join(dir_path,each_file)
    if p_shtnm.search(each_file) and lyf_path.find(u'history') == -1: #exact_lyf = lyf_path
        print lyf_path


opt_dir = ur"e:/temp/back_rndOpt_test.iff"
pythonCmdStr = u"\"python(\\\"import Other.minitiger.mi_kit_pre as mkp;mkp.back_rnd_opt({0},{1})\\\");\"".format(u'cam_testCenterCamShape',opt_dir)

lyf_path = ur'E:\projectFolder\miniTiger\sc_000\scenes\tt_fold\rndOpt_test.mb'

batchRun_cmd(lyf_path,pythonCmdStr)
       

















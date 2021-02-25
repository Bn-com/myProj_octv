# -*- coding: utf-8 -*-
# ��ͨ�á���FinalLayout���ڹ��ߡ�
#  Author : ��
#  Data   : 2013_04~2013_06
#  Mender:����
#  Data  :2014_05
# import sys
# sys.path.append('D:\\food\pyp\common')


# Q:an�����_an_����_ca_
# A:_ct_an

# ����proxy��������
# ԭ����ǣ��иߵ�ģ�ģ��ڲ���û�����õ�ʱ��ƴ�����ģ���������������һ�������ģ�������proxy.
# �������ڳ���������import������Ҫ��specialRefģʽ
# ȱ��һ���ű����������ϴ�֮ǰ�Զ���proxy�㼶��ϵ������ȷ

import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
reload(sk_cacheFinalLayout)

class csl_cacheFinalLayout(object):
    def __init__(self):
        # namespace����
        pass
        
    #----------------------------------------------------------------------------------------------#
    

    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # ����ƪ�����ƹ⡿��FinalLayout���ڹ��ߡ�����̨��
    #  Author  : ��
    #  Data    : 2013_06_03
    #------------------------------#
    
    # cache����ȱ���ʹ�ã����upload������cache·��
    # anim��ֱ��upload��������
    # ��Ҫ����ÿ����ɫ����cache�Ĺ���
    # �������ܣ�����cache�����anim���壬ֻҪ������OTC_GRP,һ�Ų�����cache��anim��¼
    # templateģʽ�£�ǿ�ƻ�anim�ο���������֡��Ϣ�������������ֻ���cache���������ˣ���check in��������
    def csl_checkFinalLayoutPerform(self , server = 1 , viewCheck = 0 , cachePre = -50 ):
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        import os
        #---------------------------#
        # Setup 000  �ⲿ������
        #---------------------------#
        
        
        
        #---------------------------#
        # Setup 001  �༶�ǲο���namespace����
        # ĳЩ�����ϲ��������ģ�壬Ȼ��import�����������γ�������namespace�����ڲο��ǲ����¼import���Ǽ��ο���
        # ���������Ҫ���������Ȼ�����¼�ο���Ϣʱ�������
        #---------------------------#
        # ����ǲο���namespace
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        print u'====================���namespace�������===================='
        
        
        #---------------------------#
        # Setup 002  �ж��Ƿ񶯻�shot��Ĳο��Ƿ���render �汾�����û�У������˳�
        #---------------------------#
        # ���ο��Ƿ���ȷ���Ƿ���render�ο�
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_FLCheckRenderFile(refInfos)
        
        #---------------------------#
        # Setup 003  ��¼������Ϣ������ʱ����
        #---------------------------#
        
        # ��¼��Ŀ�����Σ���ͷ��,�ļ�����
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfos[0])
        print u'\n'
        print(u'=====================��%s_%s����FinalLayout����ʼ��������====================='%(shotInfos[1],shotInfos[2]))
        print(u'=========================================================================')
        
        # ����ʱ����
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame',shotType = 3)
        
        
        #---------------------------#
        # Setup 004  ������棬����
        #---------------------------#
        # ��ȡfinalLayout��ʱ·��
        localPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath(shotType = 3)
        # ��ȡfinalLayout��������·��
        serverPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutServerPath(shotType = 3)
        
        # �������
        localFile = localPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3] + '_c001' + fileFormat
        mc.file(rename = localFile)
        mc.file(save=1,force = 1)
        
        
        
        #---------------------------#
        # Setup 005  �������������playblast���ʽ
        #---------------------------#
        if mc.ls('zwHeadsUpDisplay',type = 'expression'):
            mc.delete('zwHeadsUpDisplay')
            print u'\n'
            print u'====================��zwHeadsUpDisplay���������===================='
            print u'\n'
        
        #---------------------------#
        # Setup 006  ����δ��ѡ�Ĳο������������ڵ㣬����camera��IKR������
        #---------------------------#
        sk_sceneTools.sk_sceneTools().sk_sceneUnloadRefDel(1,0)
        print u'\n'
        print u'========================δ��ѡ�ο��������========================'
        print u'\n'
        
        # �������������ڵ�
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean(0)
        
        # ǿ������IK����
        mc.ikSystem(e = 1,sol = 1)
        print u'\n'
        print u'=========================IK������ǿ�Ƹ���========================'
        print u'\n'
        
        # ���������           
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfos[0])
        camServerPath = '//file-cluster/GDC/Projects/' + projectInfo + '/Project/scenes/Animation/episode_' + shotInfos[1] + '/episode_camera/'
        camServerPathN = camServerPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] +'_' + shotInfos[3]+ '_cam.ma'
        if os.path.exists(camServerPath):
            pass
        else:
            if server:
                sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1)
                print u'\n'
                print u'==========================camera�������=========================='
                print u'\n'
        
        #---------------------------#
        # Setup 007  Լ���決
        #---------------------------#
        # Ԥ����Լ������
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()
        #print(u'========================��Լ�������決�����ɹ���========================')
        
        
        #---------------------------#
        # Setup 008 ���������dataĿ¼������SET��OTC�ļ�
        # ��ע�⡿ �����SD���ڣ���������OTC��SET��Ҫ�ӷ������˲ο�
        #---------------------------#
        # ����������˾ɵ�SET��OTC�ļ�
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPDelete('SET')
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPDelete('OTC')
        
        
        #---------------------------#
        # Setup 009 �ļ��ڲ��������
        #---------------------------#
        # ����SET_GRP��OTC_GRP�ڵĲο�
        # �������
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
        print u'\n'
        print u'==========================�ļ��������=========================='
        print u'\n'
        
        
        #---------------------------#
        # Setup 010 �����ļ��ڣ����ص����壬��¼������cache֮��ָ�����
        #---------------------------#
        unDisplayLayerObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().sk_FL_RefHideObjsRecord(server=1,shotType=3)
        
                
        #---------------------------#
        # Setup 011 ��ȡanim shot�Ĳο���Ϣ
        #---------------------------#
        # ��ȡreferences��Ϣ
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        
        
        #---------------------------#
        # Setup 012 Ĭ��OTC��SET���ڵĲο�������cache�����²ο��������¼����Ҫ�Ĳο���Ϣ
        #---------------------------#
        # �������
        noNeedRefNodeInfo = sk_cacheFinalLayout.sk_cacheFinalLayout().skFLNoNeedRefNodeInfo()
        
        #---------------------------#
        # Setup 013 ���ļ�asset�ο���Ϣ���������ֽⲽ����
        # ����ֻ��¼��ɫ�͵���
        #---------------------------#
        # �����Ҫ�Ľ�ɫ�͵��߲ο���Ϣ
        if server:
            assetNeedOutputInfo = sk_cacheFinalLayout.sk_cacheFinalLayout().skFLAssetNeedInfo(refInfos,noNeedRefNodeInfo,shotType=3)
        
        #---------------------------#
        # Setup 014 OTC��SET�鵼��
        # ���ʹ��ma��ʽ��֮������ı���ȡ��ʽ�滻�ο�������򿪺��ּ��زο������Ч��
        #---------------------------#
        # ����SET_GRP��OTC_GRP�ļ�
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('SET',shotType = 3)
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('OTC',shotType = 3)
        print u'\n'
        print(u'=====================��Group�����������ˡ�����������=====================')
        print u'\n'
        
        print u'\n-------------------------'
        print '[Ref Info]'
        print refInfos[0][0]
        print u'-------------------------'
        
        # �ж��Ƿ�ms_anim�ļ�
        if shotInfos[4] == 'an':
            #---------------------------#
            # Setup 015 ɾ��set�ο����ӿ��ٶ�
            #---------------------------#
            # ����ɾ��set�ο����ӿ��ٶ�
            rfnLv1 = refInfos[0][0]
            rfnPathLv1 = refInfos[1][0]
            if refNodes:
                for ref in refNodes:
                    if '_' not in ref:
                        continue
                    if ref.split('_')[1][0] in ['s', 'S']:
                        # ɾ���ο�
                        mc.file(rfn=ref, removeReference=1)
            print u'\n'
            print(u'=====================��SET��ο������������=====================')
            print u'\n'
            
            
            #---------------------------#
            # Setup 016 ���cache���Լ����ݶ����Ŀ���������
            # cache�����У������˶�����|��K֡����ļ�⣬��¼��ʾ���ض����Ա㻹ԭ
            #---------------------------#
            # ���cache �� anim
            # �����anim
            animObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimSetObjects()
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoExport(animObjs, 1,shotType = 3)
            #print(unicode('=====================��Anim�����������ˡ�����������=====================', "utf8"))
            print u'\n'
            print(u'=====================��Anim�����������ˡ�����������=====================')
            print u'\n'
            # ���cache
            # ��Ҫ����250�ָ��
            # checkCacheSetObjects
            cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()
            if cacheObjs:
                # �����ʾ���ض�����Ϣ
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheVStateExport(cacheObjs,shotType = 3)
                print u'\n'
                print(u'=====================��Cache����V��Ϣ�����������ˡ�����������=====================')
                print u'\n'
                # ���cache
                # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheExport(cacheObjs, serverFile = server , cachePre = 0, refMode = 1 , createType = 0 , shotType = 3)
                if server:
                    print u'\n'
                    print(u'=====================��Cache�����������ˡ�����������=====================')
                    print u'\n'
                else:
                    print u'\n'
                    print(u'=====================��Cache�������ء�����������=====================')
                    print u'\n'
            else:
                print u'\n'
                print(u'=====================��Cache�������壡����������=====================')
                print u'\n'
            
            #---------------------------#
            # Setup 017 �Զ����ļ��Ĵ����һ���䣬���ﴦ��SET��OTC����Ĳο��滻��ͬʱ����ο����ʸ���
            #---------------------------#
            # �½��ļ�֮ǰ�����SET_GRP�ļ� | ���洦���� |��ʱ������ⱸ��ʱ�ı���
            sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneSETRefShaderReset(shotInfos,serverModify = 1 , shotType = 3)
        
        
            #---------------------------#
            # Setup 018 ��ʼ���ļ��ļܹ�
            #---------------------------#
            # �½��ļ�,��ʱ�ļ������
            mc.file(f=1, new=1)
            
            print '\n'
            print '[Ref Info]'
            print refInfos[0][0]
            print '\n'
            print(u'=========================���������ļ���=========================')
            print '\n'
            
            # ׼������棬��Ϊupdate��Ҫ�õ��ļ���
            fileName = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] +'_'+ shotInfos[3] +'_base_fs_c001' + fileFormat
            # �����ļ�
            localFile = localPath + fileName
            # ���������ļ�
            # serverFile = serverPath + fileName
            # ������
            mc.file( rename= localFile )
            mc.file(save = 1 ,force = 1)
            
        
            #---------------------------#
            # Setup 019 �ȵ���OTC��SET���󴴽��ο�������OTC��SETĬ�ϲ����أ�����ٶ�
            #---------------------------#
            # ���볡��
            # �����ȵ���OTC��������ο����������׳���(PORORO����)
            # ����SET_GRP��OTC_GRP
            sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPImport('SET')
            sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPImport('OTC')
            print u'\n'
            print(u'=====================��Group�����������ˡ������롿���=====================')
            print u'\n'
            
            #---------------------------#
            # Setup 020 ������Ҫ�Ľ�ɫ�͵������render�ο�
            #---------------------------#
            # ����reference��share nodes���µ��볡��������ο���
            sk_cacheFinalLayout.sk_cacheFinalLayout().sk_FLRefRebuild(refInfos,noNeedRefNodeInfo)
            
            #---------------------------#
            # Setup 021 �ο��������
            #---------------------------#
            # ����cam
            # �������
            sk_hbExportCam.sk_hbExportCam().camServerReference(info=3)  
        
            #---------------------------#
            # Setup 022 �½�����ļ��������´���
            #---------------------------#
            # �������
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(1)
            
        
            #---------------------------#
            # Setup 023 �����ļ���fl�ļ���cache list�Աȣ���һ���򱨴� 
            # ���ﲻһ��һ������������﷢��
            # 1,anim�ļ���render�ļ�cache list��һ��;
            # 2.Լ��bakeʧ�ܣ�ĳЩCHR��PROP��SET��Լ������������ȥ��ʱ��CHR,PROP����SET�ļ�����SET�ļ���Ĭ�ϲ����صģ���ʧ����cacheList
            #---------------------------#
            # ���cache�����б�
            errorObjs = []
            for obj in cacheObjs:
                if mc.ls(obj) == []:
                    errorObjs.append(obj)
            if errorObjs:
                print u'-------------------�������岻����-------------------'
                for info in errorObjs:
                    print info
                print u'-------------------�������岻����-------------------'
                mc.error(u'=====================��֪ͨǰ�ڼ��anim��render�汾cache list=====================')
        
            #---------------------------#
            # Setup 024 import cache
            # 1.���ݲ��ʣ�zwcache�ϲ�cache�ڵ�Ӧ�û�����߿�ģʽ������ỹԭ���ʡ���ԭ��ܹؼ������������߿�ģʽ��
            # 2.����cache��ͬʱ��K�鵼�µ���ʾ������Ϣ��ԭ
            # 3.��ʾ�����廹ԭ
            #---------------------------#
            # ǿ�б��ݲ���
            if cacheObjs:
                MatLists = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheRecordMaterial(cacheObjs,1,shotType = 3)
        
            # ��������
            # ����anim
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoImport(1)
            
            print u'\n'
            print(u'=====================��Anim�����������ˡ������롿���=====================')
            print u'\n'
            # ����buging
        
            # ����cache���Դ���anim
            cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()
            if cacheObjs:
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheImport(cacheObjs, server,shotType = 3,resetPosition = 1)
                # ���вο�reload
                for i in range(len(rfnLv1)):
                    ns = refInfos[2][0][i]
                    refNode = refInfos[0][0][i]
                    if noNeedRefNodeInfo:
                        if refNode not in noNeedRefNodeInfo:
                            print u'================='
                            print refNode
                            print noNeedRefNodeInfo
                            print u'================='
                            newPath = mc.referenceQuery(refNode, filename=True)
                # ������ʾ������Ϣ
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheVStateImport(shotType = 3)
                if server:
                    print u'\n'
                    print(u'=====================��Cache�����������ˡ������롿���=====================')
                    print u'\n'
                else:
                    print u'\n'
                    print(u'=====================��Cache�������ء������롿���=====================')
                    print u'\n'
            else:
                print u'\n'
                print(u'=====================��Cache�������壡������������=====================')
                print u'\n'
        
            # ������ʾ���������
            if unDisplayLayerObjs:
                hideObjs = []
                for obj in unDisplayLayerObjs:
                    if mc.ls(obj):
                        hideObjs.append(obj)
                # �ŵ�norender��
                if hideObjs:
                    if mc.ls('norender',type = 'displayLayer'):
                        pass
                    else:
                        mc.createDisplayLayer(empty = 1, name = 'norender')
                    mc.setAttr('norender.visibility',0)
                    mc.editDisplayLayerMembers('norender',hideObjs , nr = 1)
            print u'\n'
            print(u'=====================��Displayer�����ػָ�=====================')
            print u'\n'
            
            #---------------------------#
            # Setup 025 ����FL�ļ�
            #---------------------------#
            # ���ر���
            fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfos[0])
            mc.file(force=1, options="v=0", type=fileTypeFull , save=1)
            # ����ʱ�������Ϣ
            # ����
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]+ '_' + shotInfos[3]
            
            #---------------------------#
            # Setup 026 ��ͷ��Ϣ��ʱ������Ϣ����
            #---------------------------#
            # ��ʼ����
            anim = idmt.pipeline.db.GetAnimByFilename(shot)
            startFrame = anim.frmStart
            endFrame = anim.frmEnd
            fpsFrame = anim.fps
            resW = anim.resolutionW
            resH = anim.resolutionH
            # �ֱ���
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
                # ��ʼ֡
                mc.playbackOptions(min=startFrame)
                # ��ʼԤ��
                preStartFrame = startFrame - 10
                mc.playbackOptions(animationStartTime=preStartFrame)
                # ����֡
                mc.playbackOptions(max=endFrame)
                # ����Ԥ��
                posEndFrame = endFrame + 10
                mc.playbackOptions(animationEndTime=posEndFrame)
            # ����֡����ģʽÿ֡
            mc.playbackOptions(playbackSpeed=0)
                
            # ����undo
            mc.undoInfo(state=True, infinity=True)
            
            description = 'FinalLayout Base File'
        
            #---------------------------#
            # Setup 027 ��ԭ����
            #---------------------------#
            # ǿ�л�ԭ����
            if cacheObjs:
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheReturnMaterial(MatLists,finalLayout = 0,shotType = 3)
            
            # �決������ͼ
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheBakeTexAniFiles()
        
            #---------------------------#
            # Setup 028 camera��Ұ���
            #---------------------------#
            # ����camera��Ұ
            if viewCheck:
                # �������вο�
                sk_sceneTools.sk_sceneTools().sk_sceneUnloadRefDel(0,1)
                from idmt.maya.commonCore.core_mayaCommon import sk_camMatrixScene
                reload(sk_camMatrixScene)
                print '\n'
                print(u'=====================��Camera����ȫ�Զ������Ұ������ʼ��=====================')
                print '\n'
                # ��¼��ʾ�㣬Ĭ��ȫ����
                
                
                camName = 'CAM:cam_' + shotInfos[1] + '_' + shotInfos[2] + '_baked'
                if mc.ls(camName):
                    sk_camMatrixScene.sk_camMatrixScene().sk_sceneMeshCamConfig( startFrame, endFrame ,camName,[],8)
                else:
                    pass
                # ���⴦���������ܶ������壬��_sea_
                seaObj = mc.ls('*:*_sea_*',type = 'transform') + mc.ls('*_sea_*',type = 'transform')
                if seaObj:
                    for obj in seaObj:
                        mc.setAttr((obj+'.v'),1)
                        
                # ��ԭ��ʾ��        
                
                print '\n'
                print(u'=====================��Camera����ȫ�Զ������Ұ�����ɹ���=====================')
                print '\n'
                description = 'FinalLayout Base File | View Sight Configed'
                
            #---------------------------#
            # Setup 029 ����֮ǰ��ԭ�˲��ʣ�asset��reference edit�б�����м�¼����Ҫ��û���زο������������
            #---------------------------#
            mc.file(save=1, force = 1)
            # �ش�FL�ļ�
            #mc.file(localFile , open = 1, loadReferenceDepth = 'none' , force = 1)
            #sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            # ����cache��������
            #sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheEnvPath()
            
           #mc.file(save=1, force = 1)
            
            #---------------------------#
            # Setup 030 ���ر���֮��check in
            #---------------------------#
            # �ϴ�����������
            if server == 1:
                #sk_cacheFinalLayout.sk_cacheFinalLayout().checkFinalLayoutUpdate()
                # ��ʼ�ύ�ļ���������
                mc.file(save=1,force = 1)
                # �û���
                userName = os.environ['USERNAME']
                newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(newInfo[0])
                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                #print checkOutCmd
                mel.eval(checkOutCmd)
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
        
            # ȱ��check in baseFile
            print '\n'
            print(u'=========================================================================')
            print(u'=====================��%s_%s����FinalLayout���������====================='%(shotInfos[1],shotInfos[2]))
            
            # �ɹ�����
            return 0
        
    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # ����������FL�ļ� ReferenceEdit��ԭ��
    #------------------------------#

    # ����FINALLAYOUT�ļ�
    def sk_sceneFLRefShaderReset(self , info ):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        # ����OTC��SET�ļ�����������ο�
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
        fileGrpType = '_base_fs_c001'

        needFilePath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath() 
        needFsFile = needFilePath + info[0] + '_' + info[1] + '_' + info[2] + fileGrpType + fileFomat
        
        print needFsFile
        
        # �����زο�����
        mc.file(needFsFile , open = 1, loadReferenceDepth = 'none' , force = 1)
        # ��������вο�
        sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
        mc.file(save = 1, force = 1)

    #------------------------------#
    # ����������FL�ļ�Cache�ϴ���
    #------------------------------#

    # finalLayout�ϴ�������
    def checkFinalLayoutUpdate(self):
        # ��ȡcacheSet����
        cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()
        if cacheObjs:
            # �ϴ�������
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheLocalUpdate()
            #print(unicode('=====================��Cache�����������ˡ�����������=====================', "utf8"))
            print(u'=====================��Cache�����������ˡ�����������=====================')
        # ��󱣴�
        mc.file(save=1)

    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # ����֡�������������ݡ�����̨��
    #------------------------------#

    # �����������
    def checkFinalLayoutExport(self, grpExport = 0 , cacheExport = 0 , animExport = 0 , assetInfoExport = 0 , hideInfoExport = 0 ,server = 1 , cachePre = -50):
        if grpExport or cacheExport or animExport or assetInfoExport or hideInfoExport:
            from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
            reload(sk_sceneTools)
            from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
            reload(sk_referenceConfig)
            
            # info��¼
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            
            # ǿ�Ƹ���IK������
            mc.ikSystem(e = 1,sol = 1)
            
            # Ԥ����Լ������
            if not hideInfoExport or not assetInfoExport:
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()

            # ��ȡreferences��Ϣ
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            
            # �������
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(server)
            
            # �����SET��OTC֮ǰ�����anim�в��ʸ��ĵ����
            # ���������������²ο����ʹҵ�
            #sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            
            #����SET��OTC
            if grpExport:
                # ����ɵ�SET��OTC�ļ�
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPDelete('SET')
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPDelete('OTC')
                # ����SET_GRP��OTC_GRP�ļ�
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('SET')
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('OTC')
                print(u'=====================��Group�����������ˡ�����������=====================')
                
                # �½��ļ�֮ǰ�����SET_GRP�ļ�
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneSETRefShaderReset(shotInfos,serverModify=1,shotType=3)
                print(u'=====================��Group�����������ˡ�����������=====================')

            # ���assetInfo
            if assetInfoExport:
                # �������
                noNeedRefNodeInfo = []
                if mc.ls('OTC_GRP') and mc.ls('SET_GRP'):
                    allGrps = []
                    if mc.listRelatives('OTC_GRP',ad = 1,f=1):
                        allGrps = allGrps +  mc.listRelatives('OTC_GRP',ad = 1,f=1)
                    if mc.listRelatives('SET_GRP',ad = 1,f=1):
                        allGrps = allGrps + mc.listRelatives('SET_GRP',ad = 1,f=1)
                    if allGrps:
                        for grp in allGrps:
                            if mc.referenceQuery(grp,isNodeReferenced = 1):
                                refNode = mc.referenceQuery(grp,referenceNode = 1)
                                noNeedRefNodeInfo.append(refNode)
                        if noNeedRefNodeInfo:
                            noNeedRefNodeInfo = list(set(noNeedRefNodeInfo))
                # ����asset
                assetNeedOutputInfo = []
                rfnLv1 = refInfos[0][0]
                rfnPathLv1 = refInfos[1][0]
                for i in range(len(rfnLv1)):
                    ns = refInfos[2][0][i]
                    refNode = refInfos[0][0][i]
                    if noNeedRefNodeInfo:
                        if refNode not in noNeedRefNodeInfo:
                            newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                            assetNeedOutputInfo.append(newPath)
                            assetNeedOutputInfo.append(ns)
                    else:
                        if refNode.split('_')[1][0] not in ['s', 'S']:
                            newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                            assetNeedOutputInfo.append(newPath)
                            assetNeedOutputInfo.append(ns)
                assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType = 3)
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileWrite((assetNeedServerPath +  'assetReference.txt'), assetNeedOutputInfo)
                print(u'=====================��assetInfo�����������ˡ�����������=====================')

            # ���cache �� anim
            if animExport:
                # ���anim
                animObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimSetObjects()
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoExport(animObjs, server , cachePre)
                #print(unicode('=====================��Anim�����������ˡ�����������=====================', "utf8"))
                print(u'=====================��Anim�����������ˡ�����������=====================')

            # ���cache
            if cacheExport:
                # ��Ҫ����250�ָ��
                # checkCacheSetObjects
                cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()
                if cacheObjs:
                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheVStateExport(cacheObjs,shotType = 3)
                    # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheExport(cacheObjs, server=1 ,cachePre=cachePre , refMode = 1 , createType = 0,resetPosition = resetPosition)
                    #print(unicode('=====================��Cache�����������ˡ�����������=====================', "utf8"))
                    print(u'=====================��Cache�����������ˡ�����������=====================')
                else:
                    print(u'=====================��Cache�������壡������������=====================')
                    
            # ���hideInfo
            if hideInfoExport:
                # ��¼��shot�ļ��ǲο������ص���ʾ�������
                unDisplayLayerObjs = []
                displayLayers = mc.ls(type = 'displayLayer')
                if displayLayers:
                    for layer in displayLayers:
                        isRef = mc.referenceQuery(layer, isNodeReferenced = 1)
                        if isRef == 0 and layer != 'defaultLayer':
                            viewState  = mc.getAttr(layer + '.visibility')
                            if viewState == False:
                                objs = mc.editDisplayLayerMembers( layer, query=True )
                                if objs:
                                    unDisplayLayerObjs = unDisplayLayerObjs + objs
                hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType = 3)
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileWrite((hideObjsServerPath +  'shotHideObjs.txt'), unDisplayLayerObjs)
                print(u'=====================��hideObjs�����������ˡ�����������=====================')

            # �ɹ�����
            return 0

    #------------------------------#
    # ����֡������µ������ݡ�����̨��
    #------------------------------#

    # ������������
    def checkFinalLayoutImport(self, grpImport = 0 , cacheImport = 0 , animImport = 0 , assetInfoImport = 0 ,  hideInfoImport= 0 ,server = 1):
        if grpImport or cacheImport or animImport or assetInfoImport or hideInfoImport:
            from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
            reload(sk_sceneTools)
            from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
            reload(sk_referenceConfig)
            import os
            
            # info��¼
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            
            # �������
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(server)
            
            # ��ȡreferences��Ϣ
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            
            # ���ȴ����ʱ����
            # FPS
            sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('FPS')
            # frame
            sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame')
            
            #����SET��OTC
            if grpImport:
                # ���SET_GRP��OTC�Ĳο�
                # Ŀǰͨ��namespace��ȡ�����ж��Ƿ�����������
                refNode = refInfos[0][0]
                #refPathInfo = refInfos[1][0]
                refNsInfo = refInfos[2][0]
                for i in range(len(refNsInfo)):
                    mc.namespace(setNamespace = (  ':' + refNsInfo[i]))
                    objs = mc.namespaceInfo(ls= 1,dagPath =1 )
                    mc.namespace(setNamespace = ':')
                    if objs:
                        needObj = ''
                        for obj in objs:
                            if obj[-1] == '_' and mc.listRelatives(obj, c= 1,type = 'mesh'):
                                needObj = obj
                                break
                        if needObj:
                            objLong = mc.ls(needObj,l=1)[0]
                            # �ж��Ƿ���������
                            if 'SET_GRP' in objLong or 'OTC_GRP' in objLong:
                                print objLong
                                print refNode[i]
                                # ִ��ɾ���ο�
                                mc.file(rfn = refNode[i] , removeReference = 1)
                    print(u'=====================��Group����ԭ�ο������������=====================')
                # ɾ��SET_GRP��OTC_GRP
                if mc.ls('SET_GRP'):
                    mc.delete('SET_GRP')
                if mc.ls('OTC_GRP'):
                    mc.delete('OTC_GRP')
                # ����SET_GRP��OTC_GRP
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPImport('SET')
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPImport('OTC')
                print(u'=====================��Group�����������ˡ������롿���=====================')
            
            # ����asset
            if assetInfoImport:
                assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType = 3)
                if os.path.exists(assetNeedServerPath +  'assetReference.txt'):
                    assetNeedOutputInfo = sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileRead((assetNeedServerPath +  'assetReference.txt'))
                    if assetNeedOutputInfo:
                        for i in range(len(assetNeedOutputInfo)/2):
                            newPath = assetNeedOutputInfo[i*2]
                            ns = assetNeedOutputInfo[i*2 + 1]
                            mc.file(newPath, r=1, namespace= ns , referenceNode = (ns + 'RN') )
                            print u'\n'
                            print(u'=====================�������ο�����%s��=====================' % (ns))
                            print u'\n'
                else:
                    print u'\n'
                    print(u'=====================��serverȱ�١���%s�������¡������=====================' % ('assetInfo'))
                    print u'\n'
                
            # ����anim
            if animImport:
                #animObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimSetObjects()
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoImport(server)
                #print(unicode('=====================��Anim�����������ˡ������롿���=====================', "utf8"))
                print(u'=====================��Anim�����������ˡ������롿���=====================')

            # ����cache
            if cacheImport:
                cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()
                if cacheObjs:
                    #sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheImport(cacheObjs, server)
                    sk_cacheFinalLayout.sk_cacheFinalLayout().sk_flCacheImportRefreshShaders(server)
                    # ������ʾ������Ϣ
                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheVStateImport()
                    # ����cache��������
                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheEnvPath()
                    #print(unicode('=====================��Cache�����������ˡ������롿���=====================', "utf8"))
                    print(u'=====================��Cache�����������ˡ������롿���=====================')
                else:
                    print(u'=====================��Cache�������壡������������=====================')
                    
            # ����hideInfo
            if hideInfoImport :
                hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType = 3)
                unDisplayLayerObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileRead((hideObjsServerPath +  'shotHideObjs.txt'))
                if unDisplayLayerObjs:
                    hideObjs = []
                    for obj in unDisplayLayerObjs:
                        if mc.ls(obj):
                            hideObjs.append(obj)
                    # �ŵ�norender��
                    if hideObjs:
                        if mc.ls('norender',type = 'displayLayer'):
                            pass
                        else:
                            mc.createDisplayLayer(empty = 1, name = 'norender')
                        mc.setAttr('norender.visibility',0)
                        mc.editDisplayLayerMembers('norender',hideObjs , nr = 1)
                        print u'\n'
                        print(u'=====================��Displayer�����ػָ�=====================')
                        print u'\n'
    def csl_checkReferenceShaderReset(self,configType = 0 , assetType = 0):
        # ��ȡ�ļ��ڲο���Ϣ
        refInfos = self.checkReferenceListInfo()
        refNodes = refInfos[0][0]
        if refNodes:
            checkTypes = ['setAttr','connectAttr','disconnectAttr','addAttr','parent']
            for checkType in checkTypes:
                # ���Ĺ���������Ϣ
                modifyInfos = []
                for refNode in refNodes:
                    if 'CAM' not in refNode :
                        #print refNode
                        if configType == 1:
                            modifyInfos = modifyInfos + mc.referenceQuery( refNode ,failedEdits = 0 , successfulEdits = 1 ,editCommand = checkType , editStrings = 1)
                        if configType == 0:
                            if refNode.split('_')[1][0] in ['s', 'S']:
                                modifyInfos = modifyInfos + mc.referenceQuery( refNode ,failedEdits = 0 , successfulEdits = 1 ,editCommand = checkType , editStrings = 1)
                if modifyInfos:
                    # ��Ҫ��ӭ��SG�����Ϣ
                    resetShaderInfo = []
                    resetUVInfo = []
                    for info in modifyInfos:
                        if 'SG' in info :
                            #print info
                            needInfo = info.split('\"')[1]
                            #print needInfo
                            resetShaderInfo.append(needInfo)
                        if '.uv' in info :
                            #print '-----------'
                            #print info
                            needInfo = info.split(' ')[1]
                            #print needInfo
                            resetUVInfo.append(needInfo)
                        if 'initialShadingGroup.dagSetMembers' in info:
                            #print info
                            needInfo = info.split('\"')[1]
                            #print needInfo
                            resetShaderInfo.append(needInfo)
                    # ��ʼ��ӭ
                    for info in resetShaderInfo:
                        mc.referenceEdit(info,failedEdits = 1 , successfulEdits = 1 ,editCommand = checkType , removeEdits = 1)
                          
                       
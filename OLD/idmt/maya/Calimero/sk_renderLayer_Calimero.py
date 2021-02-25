# -*- coding: utf-8 -*-

'''
Created on 2013-6-18

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

import os
import shutil
import sys
import time
from subprocess import call

'''




# wrongRef
# wrongRef is set to True identify assets based on their top node versus the folder they are stored in... shouldnt be used, just in case of debug scene out of pipeline

# correctTexturesAndSave
# correctTexturesAndSave if set to True, check and subsitute all wrong references and save the corrected scene before splitting layers

# correctTexturesAndSave
# projectBase points to the proper location of textures

# oldProjectBase
# oldProjectBase is the string to be substituted with projectBase

'''


# shader import 
# file nodes ,for tga ,filter off ,for map ,filter config minmap

# 【new】
# fix path
def get_resolved_path(sourcePath):
    list_file = mc.file(q=True, l=True)
    
    for fileInfo in list_file:
        fileInfo.encode('utf-8')
        if fileInfo.find(sourcePath.replace("/","\\")) != -1 or fileInfo.find(sourcePath.replace("\\","/")) != -1:
            return fileInfo
    return sourcePath

# class
class clRLConfig(object):
    sceneName = None
    episode = None
    shot = None
    wrongRef = None
    pathLocalBase = None
    bklfile = None
    
    
    def __init__(self):
        pass
    '''
    # 【new】
    def __init__(self, wrongRef=False, bklfile=r'Z:\CALI_Ref\CA_Ep106\BKLCA106_2013_06_18_mood.xlsx', correctTexturesAndSave=False, projectBase='//tex/Calimero/CAL_RSYNC/CAL_MAYA', oldProjectBase='//tex.alphanim.lan/Calimero/CAL_RSYNC/CAL_MAYA'):
        self.bklfile = None
        if not os.path.isfile(bklfile):
            print 'bkl file',bklfile,'doensn\'t exist'
        else:
            self.bklfile = bklfile
        self.wrongRef = wrongRef
        self.sceneName = mc.file(q=True, sn=True)
        self.episode = os.path.basename(self.sceneName).split('_')[1].replace('ep','')
        self.shot = os.path.basename(self.sceneName).split('_')[2].replace('sh','')
        shotInfo = self.checkShotInfo()
        self.pathLocalBase = '//TEX/Calimero/01_SAISON_1/11_TEAMSHARE/Sylvain/PRERENDER/'+shotInfo[1]+'/scenes/sh'+shotInfo[2].replace('sh','')+'/publish/'
        
        # change the name of the camera dag node to akcam for compositing issue
        
        shotN = None
        mainCamera = 'perspShape'
        for el in os.path.basename(mc.file(q=True, sn=True)).split('_'):
            if el.startswith('sh'):
                shotN = el.replace('sh','')
                break
        for cam in mc.ls(type='camera'):
            if shotN in cam or "CAMERA" in cam:
                mainCamera = cam
                break
        # which means i found a valid camera matching the shot!!
        if mainCamera != 'perspShape':           
            for cam in mc.ls(type='camera'):
                val = False
                if cam==mainCamera: val = True
                mc.setAttr(cam+'.renderable', val)
            cameranode = mc.listRelatives(mainCamera, f=True, p=True)[0]
            ## this will not change the shape name... no need to change setCurrentCamera procedure
            if mainCamera.find('CAMERA') == -1:
                newcam = mc.rename(cameranode, 'CAMERA',ignoreShape=True)                            
                camshape = mc.listRelatives('*CAMERA*', f=True, c=True, type='camera')[0]
            else:
                camshape = mc.listRelatives(cameranode, f=True, c=True, type='camera')[0]
            mc.setAttr(camshape+'.nearClipPlane', 1)
            mc.setAttr(camshape+'.farClipPlane',70000)
            if mainCamera.find('CAMERA') == -1:
                mc.rename(camshape, 'cam_'+str('106')+'_'+str(shotN))
        self.cal_hide_skidome_lighting_if_set_int()    

        if correctTexturesAndSave:
            #mc.setAttr('defaultRenderGlobals.preMel', "eval (\"source \\\"AK_PRERENDER/akPreRender.mel\\\"\");", type="string")
            #mc.setAttr('defaultRenderGlobals.preMel', "eval (\"source \\\"//VELA/vela/prod/CALIMERO/AK_SCRIPTS/AK_PRERENDER/akPreRender.mel\\\"\");", type="string")  
            self.checkTextures(projectBase)
            self.recover_map_from_zip()
            self.saveScene()
    '''
    # 【new】
    # save
    def saveScene(self):
        fileName = self.pathLocalBase + os.path.basename(self.sceneName)
        mc.file(rename=fileName)
        mc.file(save=True)
        return
    
    # 【new】
    # check Texture
    def checkTextures(self, projectBase):
        files = mc.ls(type='file')
        for fil in files:        
            texture = mc.getAttr(fil+'.fileTextureName')
            #print projectBase,'sourceimages',texture.split('sourceimages')[-1]
            if not projectBase.endswith('/'): projectBase += '/'
            typ = 'sourceimages'
            if 'SOURCEIMAGES' in texture: typ = 'SOURCEIMAGES'
            newTexture = projectBase+'sourceimages'+texture.split(typ)[-1]
            print 'renaming',texture,'---->',newTexture
            mc.setAttr(fil+'.fileTextureName',newTexture,type='string')
        return
    
    # 【new】
    # read asset by path
    def get_asset_name_by_path(self, path):
        path_split_slash = path.replace("\\","/").split("/")
        for i,part_of_path in enumerate(path_split_slash):
            if (part_of_path == "SETS" or  part_of_path == "PROPS" or part_of_path == "CHARACTERS" or part_of_path == "FX") and i != len(path_split_slash)-1:
                if part_of_path == "PROPS" and i != len(path_split_slash)-2:
                    return path_split_slash[i+2]
                else:
                    return path_split_slash[i+1]
        return ""
    
    # 【new】
    # unzip map
    def recover_map_from_zip(self):
        print '====================!!!zip to map!!!===================='
        list_file = mc.ls(l=True, type="file")
        for file in list_file:
            fileTextureName = mc.getAttr(file + ".fileTextureName")
            destination_folder = "//tex/Calimero/01_SAISON_1/11_TEAMSHARE/Sylvain/CAL_SOURCESIMAGES/" + self.get_asset_name_by_path(fileTextureName) + "/"
            # destination_folder = "D:/" + self.get_asset_name_by_path(fileTextureName) + "/"
            result2 = self.convert_zip_to_map_ga(fileTextureName, destination_folder)
            if result2 != "":
                print file.replace(".png",".zip") + " map unzipped" 
                mc.setAttr(file + ".fileTextureName", result2, type="string")
                print file.replace(".png","") + " switch to map"   

    # 【new】
    # lampost lights shadow off
    def cal_lampost_cast_shadow_off(self):
        lighting_mood_list = mc.ls("*:*LIGHTING.Mood")
        if mc.getAttr(lighting_mood_list[0]) == 3:
            wanted_selection_list = ["*:*Bar*", "*:*bar*", "*:*BillBoard*", "*:*Billboard*", "*:*billboard*", "*:*Light*", "*:*light*", "*:*Bulb*", "*:*bulb*"]
            mesh_for_cast_shadow_of_list = []
            for wanted_selection in wanted_selection_list:
                mesh_list = mc.ls(wanted_selection, l=True, type="mesh")
                for mesh in mesh_list:
                    if mesh.find("LAMPOST_") != -1 or mesh.find("WALLLAMP_")!= -1 or mesh.find("street_lamp_") != -1 or mesh.find("WallLamps_") != -1 or mesh.find("WALLLAMPB") != -1:
                        mc.setAttr(mesh + ".castsShadows", 0)
    # 【new】  
    # hide skidome light          
    def cal_hide_skidome_lighting_if_set_int(self):
        #set_int_list = mc.objExists("*SET_*_INT*:*")
        #dzn_int_list = mc.objExists("*DZN_*_INT*:*")
        set_int_list = mc.ls("*_Int*:*") + mc.ls("*_int*:*") + mc.ls("*_INT*:*")
        #if set_int_list or dzn_int_list:
        if set_int_list:
            if mc.ls('*_SKYDOME:LIGHTING'):
                obj = mc.ls('*_SKYDOME:LIGHTING',l=1)[0]
                mc.setAttr((obj + ".visibility"),False)
            if mc.ls('*_Skydome*:LIGHTING'):
                obj = mc.ls('*_Skydome*:LIGHTING',l=1)[0]
                mc.setAttr((obj + ".visibility"),False)
            if mc.ls('*_skydome*:LIGHTING'):
                obj = mc.ls('*_skydome*:LIGHTING',l=1)[0]
                mc.setAttr((obj + ".visibility"),False)
            if mc.ls('*SKYDOME*:LIGHTING'):
                obj = mc.ls('*SKYDOME*:LIGHTING',l=1)[0]    
                mc.setAttr((obj + ".visibility"),False)                
                  

    # 【new】    
    # complete check texture
    def _checkTextures(self, useMapVsPng = True, useTextureLocal=True, projectBase='M:/CAL_RSYNC/CAL_MAYA', oldProjectBase='//tex.alphanim.lan/Calimero/CAL_RSYNC/CAL_MAYA'):
        '''
        # if useTextureLocal is false then textures are read wherever they are
        # if useTextureLocal is true then textures are copied, unzipped and used locally
        #
        # useMapVsPng = False uses png
        # useMapVsPng = True uses map
        '''
        files = mc.ls(type='file')
        for fil in files:
            texture = mc.getAttr(fil+'.fileTextureName')
            newTexture = texture.replace(oldProjectBase,projectBase)
                # change from .png to .map
            '''        '''
            if useMapVsPng:
                if texture.endswith('.png') or texture.endswith('.PNG'):
                    if not useTextureLocal:        # use .map wherever they are
                        texture = texture.replace('.png','.map').replace('.PNG','.map')
                    else:    # copy .zip to local dir, unzip them, set newTexture..
                        localFolder = 'C:/tempProject'+os.path.dirname(texture).split(':')[-1]
                        if not os.path.isdir(localFolder):
                            os.makedirs(localFolder)
                        srcZipFile = texture[:-4]+'.zip'
                        if not os.path.isfile(srcZipFile):
                            print srcZipFile,'doesn\'t exist.. fuck off'
                            continue
                        dstZipFile = localFolder+'/'+os.path.basename(texture)[:-4]+'.zip'
                        shutil.copy(srcZipFile, dstZipFile)
                        if not os.path.isfile(dstZipFile):
                            if not self.convert_zip_to_map(dstZipFile, destination_folder=os.path.dirname(dstZipFile)):
                                print dstZipFile, 'something went wrong while unzipping.. fuck off'
                                continue
                        newTexture = dstZipFile.replace('.zip','.map')
                    print 'changing', texture, 'to ' ,newTexture.replace('//','/')
                    mc.setAttr(fil+'.fileTextureName',newTexture.replace('//','/'),type='string')
            '''        '''

            if 'tex.alphanim.lan' in texture:
                print 'changing', texture, 'to ' ,newTexture.replace('//','/')
                mc.setAttr(fil+'.fileTextureName',newTexture.replace('//','/'),type='string')
        return 
        
    # 【new】
    # [GA]unZip，winrar
    def convert_zip_to_map_ga(self, fileTextureName, destination_folder="D:\\"):
        
        if fileTextureName.find(".png") != -1: 
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            file_texture_path = get_resolved_path(fileTextureName)
            result_file_name = destination_folder + os.path.split(file_texture_path.replace(".png", ".map"))[1]
            png_is_newer_file = False
            if os.path.exists(result_file_name):
                modification_time_png = os.path.getctime(file_texture_path)
                modification_time_map = os.path.getctime(result_file_name)
                if modification_time_map < modification_time_png:
                    png_is_newer_file = True 
            if os.path.exists(file_texture_path) and (not os.path.exists(result_file_name) or png_is_newer_file) :
                os.system("\"C:\\Program Files\\WinRAR\\WinRar.exe\" e " + file_texture_path.replace(".png", ".zip").replace("/","\\") + " " + destination_folder.replace("/","\\") + " -y")
                print destination_folder + os.path.split(file_texture_path.replace(".png", ".map"))[1]
                return destination_folder + os.path.split(file_texture_path.replace(".png", ".map"))[1]
            elif os.path.exists(result_file_name):
                return destination_folder + os.path.split(file_texture_path.replace(".png", ".map"))[1]
        return ""          
    
    # 【new】
    # 7z unzip
    def convert_zip_to_map(self, file, destination_folder):
        if os.path.exists(destination_folder):
            call("\"C:\\Program Files\\7-Zip\\7z.exe\" x \""+file+"\" -o\""+destination_folder+"\"")
            print ("\"C:\\Program Files\\7-Zip\\7z.exe\" x \""+file+"\" -o\""+destination_folder+"\"")
            return True
        return False


    '''
            【UI篇】【渲染】【渲染分层界面】
    '''
    # 渲染工具界面
    def sk_UICalimeroRenderLayersLayers(self):
        # 窗口
        if mc.window ("sk_sceneUICalimeroRenderLayers", ex=1):
            mc.deleteUI("sk_sceneUICalimeroRenderLayers", window=True)
        mc.window("sk_sceneUICalimeroRenderLayers", title="Calimero RenderLayers Tools", widthHeight=(330, 300), menuBar=0)
        # 主界面
        mc.columnLayout()
        
        # 模块
        # from idmt.maya.py_common import sk_checkCommon
        # import sk_checkCommon
        # reload(sk_checkCommon)
        
        # 行按钮
        mc.rowLayout(numberOfColumns=2, columnWidth2=(100, 230))
        # 全自动
        mc.button(w=100 , h=300 , bgc=[0.25, 0.25, 0.25], label=(unicode('【全自动】【分层】', 'utf8')), c='sk_renderLayer_Calimero.clRLConfig().clRLAutoCreate()')
        mc.columnLayout()
        # 分割按钮
        # 第1排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(120, 110))
        mc.button(w=120 , h=30 , bgc=[0.2, 0.2, 0.2], label=(unicode('【分层】【RGB】          ', 'utf8')), c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"RGB\")')
        mc.button(w=110 , h=30 , bgc=[0.3, 0.3, 0.3], label=(unicode('<<打开本地路径>>', 'utf8')),c = 'sk_renderLayer_Calimero.clRLConfig().clRLLocalFilePath()')
        mc.setParent("..")
        # 第2排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(120,110))
        mc.button(w=120 , h=30 , bgc=[0.2, 0.2, 0.2], label=(unicode('【分层】【BW】          ', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"BW\")')
        mc.button(w=110 , h=30 , bgc=[0.3, 0.3, 0.3], label=(unicode('<<通用镜头设置>>', 'utf8')),c = 'sk_renderLayer_Calimero.clRLConfig().clRLCommonConfig()')
        mc.setParent("..")
        # 第3排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(120, 110))
        mc.button(w=120 , h=30 , bgc=[0.2, 0.2, 0.2], label=(unicode('【分层】【SPEC】        ', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"SPEC\")')
        mc.button(w=110 , h=30 , bgc=[0.3, 0.3, 0.3], label=(unicode('<<MR产品设置>>', 'utf8')),c ='sk_renderLayer_Calimero.clRLConfig().mentalRayProductionLevel()')
        mc.setParent("..")
        # 第4排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(110, 110))
        mc.button(w=120 , h=30 , bgc=[0.2, 0.2, 0.2], label=(unicode('【分层】【RIM】          ', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"RIMLIGHT\")')
        mc.button(w=110 , h=30 , bgc=[0.3, 0.3, 0.3], label=(unicode('<<Map材质处理>>', 'utf8')),c ='sk_renderLayer_Calimero.clRLConfig().clRLFileNodeConfig()')
        mc.setParent("..")
        # 第5排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(120, 110))
        mc.button(w=120 , h=30 , bgc=[0.2, 0.2, 0.2], label=(unicode('【分层】【LIGHT】       ', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"LIGHT\")')
        mc.button(w=110 , h=30 , bgc=[0.3, 0.3, 0.3], label=(unicode('<<VisTT处理>>', 'utf8')),c = 'sk_renderLayer_Calimero.clRLConfig().clRLVisConfig()')
        mc.setParent("..")
        # 第6排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(120, 110))
        mc.button(w=120 , h=30 , bgc=[0.2, 0.2, 0.2], label=(unicode('【分层】【ZDEPTH】    ', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"ZDEPTH\")')
        mc.button(w=110 , h=30 , bgc=[0.3, 0.3, 0.3], label=(unicode('<<SmoothSet处理>>', 'utf8')), c = 'sk_renderLayer_Calimero.clRLConfig().clRLDoSmooth()')
        mc.setParent("..")        
        # 第7排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(120, 110))
        mc.button(w=120 , h=30 , bgc=[0.2, 0.2, 0.2], label=(unicode('【分层】【BG_RGB】    ', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"BG_RGB\")')
        mc.button(w=110 , h=30 , bgc=[0.3, 0.3, 0.3], label=(unicode('<<清理全部分层>>', 'utf8')),c = 'from idmt.maya.py_common import sk_checkCommon\nreload(sk_checkCommon)\nsk_checkCommon.sk_checkTools().checkCleanRenderLayers()')
        mc.setParent("..")
        # 第8排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(120, 110))
        mc.button(w=120 , h=30 , bgc=[0.2, 0.2, 0.2], label=(unicode('【分层】【2D】            ', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"RENDER_2D\")')
        mc.button(w=110 , h=30 , bgc=[0.0, 0.3, 0.0], label=(unicode('【分层】【LCHR】', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"LIGHTCHR\")')
        mc.setParent("..")
        # 第9排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(120, 110))
        mc.button(w=120 , h=30 , bgc=[0.2, 0.2, 0.2], label=(unicode('【分层】【PFX】           ', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"PFX\")')
        mc.button(w=110 , h=30 , bgc=[0.0, 0.3, 0.0], label=(unicode('【分层】【LSET】', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"LIGHTSET\")')
        mc.setParent("..")     
        
        # 第10排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(120, 110))
        mc.button(w=120 , h=30 , bgc=[0.2, 0.2, 0.2], label=(unicode('【分层】【LIGHTCHR】    ', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"LIGHTCHR\")')
        mc.button(w=120 , h=30 , bgc=[0.2, 0.2, 0.2], label=(unicode('【分层】【LIGHTSET】    ', 'utf8')),c='sk_renderLayer_Calimero.clRLConfig().clRLSpeficCreate(\"LIGHTSET\")')
        mc.setParent("..")
           
        mc.setParent("..")
        
        # 行按钮
        # mc.rowLayout()
        # 单独导入音轨
        # mc.button(w = 150 , h = 30 ,bgc = [0,0.7,0.2],label = (unicode('【动画】只导入音频', 'utf8')) , c = 'sk_sceneConfig.sk_sceneConfig().sk_sceneImportAudio()' )
        # mc.setParent("..")
        
        
        mc.setParent("..")
        mc.showWindow("sk_sceneUICalimeroRenderLayers")

    # Auto Create
    def clRLAutoCreate(self, render2D = 1 , PFX = 1 ,batchRun = 0):
        print ('=================================================================')
        print '====================!!!Start AutoRenderLayer!!!===================='
        fileNameNow = mc.file(q = 1 ,exn= 1)
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.py_common import sk_sceneConfig
        reload(sk_sceneConfig)
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        
        # 处理非参考的namespace
        sk_sceneConfig.sk_sceneConfig().sk_sceneNoRefNamespaceClean()
        print u'\n====================多层namespace清理完毕====================\n'

        # Clean Unknwon Nodes
        sk_checkCommon.sk_checkTools().checkDonotNodeCleanBase(0)
        
        # 额外的，处理skydome与灯光的关系
        self.cal_hide_skidome_lighting_if_set_int()

        # 灯光组强制打开,给马书春外包打补丁
        ltGrps = mc.ls('*:LIGHTING',type = 'transform')
        if ltGrps:
            for grp in ltGrps:
                mc.setAttr((grp + '.v'),1)
           
        #导入相机
        self.setCurrentCamera()

        #修正显示层模式问题
        self.clRepairDisplayLayers

        #处理norender及pv显示层
        self.clNorenderObjs()

        if batchRun == 1 or batchRun == 2:
            # 时间轴修正
            # 开始处理
            from idmt.maya.py_common import sk_infoConfig
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
            anim = idmt.pipeline.db.GetAnimByFilename(shot)
            startFrame = anim.frmStart
            endFrame = anim.frmEnd
            fpsFrame = anim.fps
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
                # 渲染范围设置
                mc.setAttr('defaultRenderGlobals.startFrame', startFrame)  
                mc.setAttr('defaultRenderGlobals.endFrame', endFrame)  
            # bake 约束 
            from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
            reload(sk_cacheFinalLayout)
            sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()
            localPath = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
            localBaseFile = localPath + fileNameNow.split('/')[-1]
            mc.sysFile(localPath, makeDir=True)
        
        if batchRun == 1:
            # 另存
            mc.file(rename = localBaseFile)
            mc.file(save = 1 ,force = 1)
        
        if batchRun == 2:
            # 导出
            mc.select(['CHR_GRP','PRP_GRP','SET_GRP','OTC_GRP','CAM_GRP'])
            print '-------'
            print localBaseFile
            mc.file( localBaseFile, force=1, options="v=0" , type = 'mayaAscii', preserveReferences=1, exportSelected=1)
            # 重打开
            mc.file( localBaseFile ,open = 1 ,f = 1)
            
        if batchRun == 1 or batchRun == 2:
            fileNameNow = mc.file(q = 1 ,exn= 1)
            
        # 参考import
        #sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        
        # 记录norender物体
        #norenderObjs = self.clNorenderObjs()
        #if norenderObjs:
        #    meshes = mc.listRelatives(norenderObjs ,ad = 1, type = 'mesh' , f = 1)
        #    if meshes:
        #        for mesh in meshes:
        #            mc.setAttr(mesh + '.primaryVisibility',0)
        '''
        if norenderObjs:
            for obj in norenderObjs:
                #　ttV
                if mc.ls(obj + '.tt_visibility'):
                    attr = '.tt_visibility'
                    attrV = 1
                    try:
                        mc.setAttr((obj+ attr),attrV)
                    except:
                        print u'===以下物体属性被锁，请联系前期==='
                        print (obj+ attr)
                        mc.error(u'===以下物体属性被锁，请联系前期===')
                # v和lodV
                attr = '.v'
                attrV = 0
                try:
                    mc.setAttr((obj+ attr),attrV)
                except:
                    attr = '.lodVisibility'
                    try:
                        mc.setAttr((obj+ attr),attrV)
                    except:
                        print u'===以下物体属性被锁，请联系前期==='
                        print (obj+ attr)
                        mc.error(u'===以下物体属性被锁，请联系前期===')
        '''
        # 干掉鞋垫
        objs = mc.ls('TEMP_FEET_GRP', l = 1)
        if objs:
            mc.delete(objs)
            
        # 判断int处理
        objInfo = self.clRLObjectsTList()
        intState = objInfo[7]
        
        # Back To MasterLayer
#        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        # clean renderlayer
        sk_checkCommon.sk_checkTools().checkCleanRenderLayers()
        # File Node Config
        self.clRLFileNodeConfig()
        # VisTT
        self.clRLVisConfig()
        # skydome Setting
        self.clSkydomeExcelLoad()
        # renderpass Create
        self.clRLRenderPass()
        #导入相机  调整到保存中间文件前
        #self.setCurrentCamera()
        # common Setting
        self.clRLCommonConfig()
        # mr Setting
        self.mentalRayProductionLevel()
        
        # Step 1：RGB,BW,SPEC,RIM
        
        # RGB
        self.clRLRGBCreate()
        # BW
        self.clRLBWCreate()
        # SPEC
        self.clRLSPECCreate()        
        # RIM
        self.clRLRIMLIGHTCreate()
        # smoothSet
        self.clRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable",0)
        # mc.setAttr
        # common Setting
        self.clRLCommonConfig()
        # save
        localPath = self.clRLSave('auto_01')
        
        # Step 2：Light,ZDepth,BG_RGB
        if not batchRun or batchRun == 1:
            if mc.ls('RGB'):
                mc.delete('RGB')
            if mc.ls('BW'):
                mc.delete('BW')
            if mc.ls('SPEC'):
                mc.delete('SPEC')
            if mc.ls('RIMLIGHT'):
                mc.delete('RIMLIGHT')
        if batchRun == 2:
            mc.file(fileNameNow,open = 1 ,force = 1)
            self.clRLBaseSettings()
        
        # Light
        if intState:
            self.clRLLIGHTCHRCreate()
            self.clRLLIGHTSETCreate()
        else:
            self.clRLLIGHTCreate()
        # ZDepth
        self.clRLZDEPTHCreate()
        # BG_RGB
        self.clRLBGRGBCreate()
        
        # smoothSet
        self.clRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable",0)
        # common Setting
        self.clRLCommonConfig()
        # save
        self.clRLSave('auto_02')
        
        # render2D PFX
        if not batchRun or batchRun == 1:
            if mc.ls('LIGHT'):
                mc.delete('LIGHT')
            if mc.ls('LIGHTSET'):
                mc.delete('LIGHTSET')
            if mc.ls('ZDEPTH'):
                mc.delete('ZDEPTH')
            if mc.ls('BG_RGB'):
                mc.delete('BG_RGB')
        if batchRun == 2:
            mc.file(fileNameNow,open = 1 ,force = 1)
            self.clRLBaseSettings()
        
        # RENDER_2D
        self.clRLSpeficCreate('RENDER_2D', '2D')
        # PFX
        self.clRLSpeficCreate('PFX', 'PFX')
        
        print '=======================!!!All Done!!!======================='
        print ('===========================================================')
        
        #if batchRun:
        print '\n'
        print u'Please Go To This Path To Find The Last RenderLayer Files'
        print u'------------------------------------------------------------------------'
        print localPath
        print u'------------------------------------------------------------------------'
        print '\n'
        return 0
    
    # Create Single Render Layer
    def clRLSpeficCreate(self, renderLayer , mode=''):
        print (u'===============!!!Start 【%s】!!!===============' % renderLayer)
        print 'Working...'
        
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)

        # 额外的，处理skydome与灯光的关系
        self.cal_hide_skidome_lighting_if_set_int()

        # 干掉鞋垫
        objs = mc.ls('TEMP_FEET_GRP', l = 1)
        if objs:
            mc.delete(objs)

        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Clean Unknwon Nodes
        sk_checkCommon.sk_checkTools().checkDonotNodeCleanBase(0)
        # File Node Config
        self.clRLFileNodeConfig()
        # VisTT
        self.clRLVisConfig()
        # skydome Setting
        self.clSkydomeExcelLoad()
        # renderpass Create
        self.clRLRenderPass()
        # common Setting
        self.clRLCommonConfig()
        # mr Setting
        self.mentalRayProductionLevel()
        # 指定层
        render2dOk = ''
        pfxOk = ''
        
        # RGB
        if renderLayer == 'RGB':
            try:
                mc.delete('RGB')
            except:
                pass
            self.clRLRGBCreate()
        # BW
        if renderLayer == 'BW':
            try:
                mc.delete('BW')
            except:
                pass
            self.clRLBWCreate()
        # SPE
        if renderLayer == 'SPEC':
            try:
                mc.delete('SPEC')
            except:
                pass
            self.clRLSPECCreate()
        # RIM
        if renderLayer == 'RIMLIGHT':
            try:
                mc.delete('RIMLIGHT')
            except:
                pass
            self.clRLRIMLIGHTCreate()
        # Light
        if renderLayer == 'LIGHT':
            try:
                mc.delete('LIGHT')
            except:
                pass
            self.clRLLIGHTCreate()
            
        if renderLayer == 'LIGHTCHR':
            try:
                mc.delete('LIGHT')
            except:
                pass
            self.clRLLIGHTCHRCreate()
            
        if renderLayer == 'LIGHTSET':
            try:
                mc.delete('LIGHTSET')
            except:
                pass
            self.clRLLIGHTSETCreate()
        # ZDepth
        if renderLayer == 'ZDEPTH':
            try:
                mc.delete('ZDEPTH')
            except:
                pass
            self.clRLZDEPTHCreate()

        # BG_RGB
        if renderLayer == 'BG_RGB':
            try:
                mc.delete('BG_RGB')
            except:
                pass
            self.clRLBGRGBCreate()
        # RENDER_2D
        if renderLayer == 'RENDER_2D':
            try:
                mc.delete('RENDER_2D')
            except:
                pass
            sk_checkCommon.sk_checkTools().checkCleanRenderLayers()
            render2dOk = self.clRLBGRENDER2DCreate()
            
        # PFX
        if renderLayer == 'PFX':
            try:
                mc.delete('PFX')
            except:
                pass
            sk_checkCommon.sk_checkTools().checkCleanRenderLayers()
            # 【new】,software , must polysmooth
            from idmt.maya.py_common import sk_smoothSet
            #import  sk_smoothSet
            reload(sk_smoothSet)
            objs = sk_smoothSet.sk_smoothSetTools().smoothSetGetObjects(2)    
            for obj in objs:
                if 'CALI' in obj or 'cali' in obj:
                    mc.polySmooth(obj,  mth=0, dv=2, bnr=1, c=1, kb=1, ksb=1, khe=0, kt=1, kmb=1, suv=1, peh=0, sl=1, dpe=1, ps=0.1, ro=1, ch=1)
            
            pfxOk = self.clRLBGPFXCreate()
            
        # smoothSet
        self.clRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # UnRender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable",0)
        # common Setting
        self.clRLCommonConfig()
        
        if mode:
            if render2dOk:
                print 'renderLayer,  pfxOk', renderLayer,  render2dOk
            if pfxOk:
                print 'renderLayer,  pfxOk', renderLayer,  pfxOk
            if (renderLayer == 'PFX' and pfxOk==True) or (renderLayer == 'RENDER_2D' and render2dOk==True):
                self.clRLSave(mode)
                #self.clRLSave(mode)
        
        print (u'===============!!!Done  【%s】!!!===============' % 'renderLayer')
        print '\n'
    
    # 【new】 特殊处理
    def clSpecialConfig(self):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        if shotInfo[1] in ['147']:
            camNearRange = ['51','52','53','54','55','56','57','58','66','67','68','69']
            for i in range(95,168):
                if i not in [98,103,105,110,114,142,147,148,149,150,151]:
                    camNearRange.append(str(i))
            if shotInfo[2] in camNearRange:
                mc.setAttr('CAM:CAMERA.nearClipPlane',1)
    
    # 记录norender信息   改为处理显示层信息，norender层物体隐藏，pv层显示，但取消可渲染   wanshoulong 2015/7/6
    def clNorenderObjs(self):
        displayLayers = mc.ls(type = 'displayLayer')
        norenderObjs = []
        for layer in displayLayers:
            if layer.lower() == 'pv':
                objs = mc.editDisplayLayerMembers(layer,q = 1,fn=1)
                if objs:
                    norenderObjs = mc.ls(objs,l=1)
                    if norenderObjs:
                        meshes = mc.listRelatives(norenderObjs ,ad = 1, type = 'mesh' , f = 1)
                        if meshes:
                            for mesh in meshes:
                                try :
                                    mc.setAttr(mesh + '.primaryVisibility',0)
                                except :
                                    pass
                mc.setAttr(layer+'.visibility',1)
            elif layer.lower() == 'norender':
                objs = mc.editDisplayLayerMembers(layer,q = 1,fn=1)
                if objs:
                    for obj in objs :
                        try :
                            mc.setAttr(obj+'.visibility',0)
                        except :
                            pass
                mc.setAttr(layer+'.visibility',0)
        #return norenderObjs
    

    #处理显示层模式错误
    def clRepairDisplayLayers(self):
        displayLayers=mc.ls(type='displayLayer')
        for layer in displayLayers :
            try :
                mc.setAttr(layer+'.displayType',0)
            except :
                pass

    # 【new】
    # set camera
    def setCurrentCamera(self):
                               
        from idmt.maya.py_common import sk_hbExceptCam
        reload(sk_hbExceptCam)
        sk_hbExceptCam.sk_hbExceptCam().camServerReference()  
        
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)

        refInfos = sk_referenceConfig.sk_referenceConfig ().checkReferenceListInfo()    
        refPaths = refInfos[1][0]

        mc.setAttr('*CAM:CAMERA.renderable',1)
        mc.setAttr('*CAM:CAMERA.farClipPlane',100000)

        referrens=[]
        for ref in refPaths:
            if ref.split('_')[-1]=='cam.ma':
                referrens.append(ref)

        # 移除客户参考相机 及无效相机
        for ref in refPaths:
            if ref.split('_')[-1]=='00.ma' : 
                mc.file(ref,rr=1)
        unusecam = mc.ls('cam_*',type='camera')
        for cam in unusecam :
            trans = mc.listRelatives(cam,f=1,p=1)
            try :
                mc.delete(trans)
            except:
                pass


        if len(referrens)==1:
            mc.file(referrens[0],ir=1)
        
        newname="CAMERA_CAMERA"    
        cameras=mc.ls('*:*CAMERA')

        if cameras:
            camShape=mc.listRelatives(cameras[0])
            mc.rename(camShape[0],(cameras[0]+'Shape'))
            mc.rename(cameras[0],newname)

        cam=mc.ls("*CAMERA_CAMERA")    
        if cam:
            camGRP=mc.listRelatives(cam[0],parent=1)
            if camGRP and 'CAM_GRP':
                mc.ungroup(camGRP[0])                              
                mc.parent(cam[0],'CAM_GRP')
                       
    # Save File
    def clRLSave(self, mode):
        print (u'===============!!!Start 【%s】!!!===============' % 'Save')
        print 'Working...'
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)

        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
        fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if mode == 'auto_01':
            fileType = '_l4AllLayer_lr_c001.mb'
        if mode == 'auto_02':
            fileType = '_l3AllLayer_lr_c001.mb'
        if mode == '2D':
            fileType = '_l1Render2D_lr_c001.mb'
        if mode == 'PFX':
            fileType = '_l1PFX_lr_c001.mb'
        '''    
        # Camera
        from idmt.maya.py_common import sk_hbExceptCam
        reload(sk_hbExceptCam)
        sk_hbExceptCam.sk_hbExceptCam().camServerReference()   
        
        
        refInfos = sk_referenceConfig.sk_referenceConfig ().checkReferenceListInfo()    
        refPaths = refInfos[1][0]
        mc.setAttr('CAM*:CAMERA.renderable',1)
        mc.setAttr('CAM*:CAMERA.farClipPlane',100000)
        
        referrens=[]
        for ref in refPaths:
            if ref.split('_')[-1]=='cam.ma':
                referrens.append(ref)

                
        if len(referrens)==1:
            mc.file(referrens[0],ir=1)
        
        newname="CAMERA_CAMERA"    
        cameras=mc.ls('*:*CAMERA')

        if len(cameras)==1:
            print 'strat.......'
            print cameras[0]
            mc.rename(cameras[0],newname)

        cam=mc.ls("CAMERA_CAMERA")
        camGRP=mc.listRelatives(cam[0],parent=1)
        if cam:
            if camGRP:
                mc.ungroup(camGRP[0])                              
                mc.parent(cam[0],'CAM_GRP')
        '''
        # 特殊处理
        self.clSpecialConfig()
        
        # skydome Setting
        self.clSkydomeExcelLoad()
               
        fileName = fileName + fileType
        mc.file(rename=fileName)
        mc.file(save=1,type = 'mayaBinary',f = 1)
        #mc.file(save=1,f = 1)
        return pathLocal
        print (u'===============!!!Done  【%s】!!!===============' %'Save')
        print '\n'
    
    # Base Setting
    def clRLBaseSettings(self):
        # File Node Config
        self.clRLFileNodeConfig()
        # VisTT
        self.clRLVisConfig()
        # skydome Setting
        self.clSkydomeExcelLoad()
        # renderpass Create
        self.clRLRenderPass()
        # common Setting
        self.clRLCommonConfig()
        # mr Setting
        self.mentalRayProductionLevel()
    
    # open local path
    def clRLLocalFilePath(self):
        from idmt.maya.py_common import sk_infoConfig
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
        import os
        os.system('explorer ' + pathLocal)
        
    # Import Camera
    def clCamImport(self):
        camGrp = mc.ls('CAM_GRP')
        if camGrp:
            mc.delete(camGrp)
        
    # Create renderPass
    def clRLRenderPass(self):
        print (u'===============!!!Start 【%s】!!!===============' % 'RenderPass')
        print 'Working...'
        
        # 看起来没区别。。不用函数是方便修改调整
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        
        # 创建idPass1
        ex_idPass1 = mc.ls(('idPass1'), type='renderPass')
        if ex_idPass1:
            renderPass = 'idPass1'
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.clRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, 'idPass1')
        
        # 创建idPass2
        ex_idPass2 = mc.ls('idPass2', type='renderPass')
        if ex_idPass2:
            renderPass = 'idPass2'
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.clRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, 'idPass2')
        
        # 创建idPass3
        ex_idPass3 = mc.ls('idPass3', type='renderPass')
        if ex_idPass3:
            renderPass = 'idPass3'
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.clRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass,'idPass3')
        
        # 创建idPass4
        ex_idPass4 = mc.ls('idPass4', type='renderPass')
        if ex_idPass4:
            renderPass = ('idPass4')
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.clRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, 'idPass4')
        
        # 创建idPassChr
        ex_idPassChr = mc.ls('idPassChr', type='renderPass')
        if ex_idPassChr:
            renderPass = ('idPassChr')
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.clRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, 'idPassChr')
        
        # 创建idPassChrMain
        ex_idPassChrMain = mc.ls('idPassChrMain', type='renderPass')
        if ex_idPassChrMain:
            renderPass = 'idPassChrMain'
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 4, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.clRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass,'idPassChrMain')
        
        # 连接节点到renderpass
        self.renderpassConnect()
        
        print (u'===============!!!Done  【%s】!!!===============' %'RenderPass')
        print '\n'
        
    # 设置renderpass属性
    def clRLRenderPassConfig(self, renderPass, configType):
        # renderable
        mc.setAttr((renderPass + '.renderable'), int(configType[0]))
        # nodeType
        mc.setRenderPassType(renderPass, type=str(configType[1]))
        # channels
        mc.setAttr((renderPass + '.numChannels'), int(configType[2]))
        # frameType
        mc.setAttr((renderPass + '.frameBufferType'), int(configType[3]))
        # colorProfile
        mc.setAttr((renderPass + '.colorProfile'), int(configType[4]))
        # filtering
        mc.setAttr((renderPass + '.filtering'), int(configType[5]))
        # passGroupName
        mc.setAttr((renderPass + '.passGroupName'), str(configType[6]), type='string')
        # holdout
        mc.setAttr((renderPass + '.holdout'), int(configType[7]))
        # transparency
        mc.setAttr((renderPass + '.useTransparency'), int(configType[8]))
        # reflectHidden
        mc.setAttr((renderPass + '.reflectHidden'), int(configType[9]))
        # refractHidden
        mc.setAttr((renderPass + '.refractHidden'), int(configType[10]))
        # hiddenReflect
        mc.setAttr((renderPass + '.hiddenReflect'), int(configType[11]))
        # hiddenRefract
        mc.setAttr((renderPass + '.hiddenRefract'), int(configType[12]))
        # transparentAttenuation
        mc.setAttr((renderPass + '.transparentAttenuation'), int(configType[13]))
        # minReflectionLevel
        mc.setAttr((renderPass + '.minReflectionLevel'), int(configType[14]))
        # maxReflectionLevel
        mc.setAttr((renderPass + '.maxReflectionLevel'), int(configType[15]))
        # minRefractionLevel
        mc.setAttr((renderPass + '.minRefractionLevel'), int(configType[16]))
        # maxRefractionLevel
        mc.setAttr((renderPass + '.maxRefractionLevel'), int(configType[17]))
    
    # 连接所有材质节点到对应的idpass
    def renderpassConnect(self):
        colorBufferNods = mc.ls(type='writeToColorBuffer')
        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        for node in colorBufferNods:
            # 无法将通用的断开命令提前。。断开和连接操作必须连续才有效
            # 处理colorID
            if '_ColorID' in node and '_ColorID2' not in node and '_ColorID3' not in node:
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr(("idPass1.message"), (node + '.renderPass'))
            # 处理colorID2
            if '_ColorID2' in node :
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr("idPass2.message", (node + '.renderPass'))
            # 处理colorID3
            if '_ColorID3' in node :
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr("idPass3.message", (node + '.renderPass'))
            # 处理colorID_CHR
            if '_ColorID_CHR' in node:
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr("idPassChr.message", (node + '.renderPass'))
            if '_ColorID_ChrMain' in node:
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr("idPassChrMain.message", (node + '.renderPass'))
    
    # 处理texture file节点属性
    # tga filter off;map minimap and 3 modify
    def clRLFileNodeConfig(self):
        print (u'===============!!!Start 【%s】!!!===============' % 'fileNodeConfig')
        print 'Working...'
        import os
        # 处理map
        fileNodes = mc.ls(type='file')

        for node in fileNodes:
            path = mc.getAttr(node + '.fileTextureName')
            format = path.split('.')[-1]
            # 小写化
            if format.lower() != 'map':
                newpath = path.replace(format,'map')
                realPath = mc.workspace(expandName = newpath)
                if os.path.exists(realPath.lower()):
                    mc.setAttr((node + '.fileTextureName'),newpath,type = 'string')
                else:
                    newpath = path.replace(format,'tga')
                    mc.setAttr((node + '.fileTextureName'),newpath,type = 'string')
                    mc.setAttr((node + '.filterType'), 0)
            formatNow = mc.getAttr(node + '.fileTextureName').split('.')[-1]
            if formatNow.lower() == 'map':
                mc.setAttr((node + '.filterType'), 1)
                mc.setAttr((node + '.miOverrideConvertToOptim'), 1)
                mc.setAttr((node + '.miUseEllipticalFilter'), 1)
                cmd = "setAttr \\\"" + node +".miConvertToOptim\\\"" + "  0";
                fullCmd = "evalDeferred -lowestPriority \"" + cmd + "\""
                mel.eval(fullCmd)
                mc.setAttr((node + '.miEllipticalMaxMinor'), 8)

        print (u'===============!!!Done  【%s】!!!===============' % 'fileNodeConfig')
        print '\n'


    # 物体分类清单
    def clRLObjectsTList(self, objType=1, objs=[]):
        # 获取root
        rootGrps = []
        if mc.ls('CHR_GRP'):
            if mc.listRelatives('CHR_GRP',c=1,f=1):
                rootGrps  = rootGrps + mc.listRelatives('CHR_GRP',c=1,f=1)
        if mc.ls('PRP_GRP'):
            if mc.listRelatives('PRP_GRP',c=1,f=1):
                rootGrps  = rootGrps + mc.listRelatives('PRP_GRP',c=1,f=1)
        if mc.ls('SET_GRP'):
            if mc.listRelatives('SET_GRP',c=1,f=1):
                rootGrps  = rootGrps + mc.listRelatives('SET_GRP',c=1,f=1)
        if mc.ls('VFX_GRP'):
            if mc.listRelatives('VFX_GRP',c=1,f=1):
                rootGrps  = rootGrps + mc.listRelatives('VFX_GRP',c=1,f=1)
        
        refCHR = []
        refPROP = []
        refSET = []
        refENV = []
        refSKY = []
        refCalimero = []
        refVisTT = []
        refIntState = 0
        for grp in rootGrps:
            # 剔除非ref
            isRef = mc.referenceQuery(grp, isNodeReferenced=True)
            if isRef:
                # 获取refPath
                refPath = mc.referenceQuery(grp, filename=True)
                refPath = refPath.lower()
                # 角色
                if '/characters/' in refPath:
                    refCHR.append(grp)
                    newCheckPath = ( '/' + refPath.split('/characters/')[-1] )
                    # Calimero
                    if '/cali' in newCheckPath:
                        refCalimero.append(grp)
                    # 特殊处理
                    if '/cali' in newCheckPath or '/pris' in newCheckPath or '/vale' in newCheckPath or '/pier' in newCheckPath:
                        refVisTT.append(grp)
                # 道具
                if '/props/' in refPath:
                    # Set
                    pathInfo = refPath.split('/props/')[-1].split('/')[0]
                    print pathInfo
                    setKeys = [ 'col_']
                    configNum = 0
                    for key in setKeys:
                        if key in pathInfo:
                            refENV.append(grp)
                        else:
                            refPROP.append(grp)
                # 其他类，下面细化
                if  '/sets/' in refPath:
                    # Set
                    #pathInfo = refPath.split('/sets/')[-1].split('/')[0]
                    #print pathInfo
                    setKeys = [ '_int',  '_ext']
                    configNum = 0
                    for key in setKeys:
                        if key in refPath:
                            if key == '_int':
                                refIntState = 1
                            refSET.append(grp)
                        else:
                            configNum += 1
                    # Env,非int非ext
                    if configNum == 2:
                        refENV.append(grp)
        result = []
        result.append(refCHR)
        result.append(refPROP)
        result.append(refSET)
        result.append(refENV)
        result.append(refSKY)
        result.append(refCalimero)
        result.append(refVisTT)
        result.append(refIntState)
        return result
    
    # 渲染标准设置
    def clRLCommonConfig(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'标准设置')
        print 'Working...'


        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        # 处理非参考的namespace
        from idmt.maya.py_common import sk_sceneConfig
        reload(sk_sceneConfig)
        sk_sceneConfig.sk_sceneConfig().sk_sceneNoRefNamespaceClean()

        # IKR开启
        mc.setAttr('defaultRenderGlobals.preMel',"ikSystem -e -sol 1",type = 'string')

        # camera renderer
        cameras = mc.ls(type = 'camera')
        renderCam = mc.ls('*CAMERA_CAMERA')
        if mc.ls(renderCam):
            for cam in cameras:
                if 'CAMERAShape' not in cam:
                    mc.setAttr((cam + '.renderable'),0)
                else:
                    mc.setAttr((cam + '.renderable'),1)
        else:
            print(u'请确认文件有渲染相机')
        # 摄像机距离
        #mc.setAttr((renderCam + '.farClipPlane'),1000000)

        # 开启窗口，创建各种UI
        #mel.eval('unifiedRenderGlobalsWindow')
        
        # 标准设置
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)    
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 3)
        #mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<Layer>/<Scene>_<Layer>', type='string')
        imageFilePrefix = '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_'+'<RenderPass>'
        #imageFilePrefix = '<RenderLayer>/<Scene>_<RenderLayer>'
        mc.setAttr('defaultRenderGlobals.imageFilePrefix', imageFilePrefix, type='string')
        mc.setAttr('defaultResolution.width', 1920)
        mc.setAttr('defaultResolution.height', 1080)
        mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
        mc.setAttr('defaultResolution.pixelAspect', 1.00)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)',lowestPriority=1)
        mc.setAttr('defaultResolution.dotsPerInch', 72)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)  
        
        # FPS制式设置
        #mc.currentUnit(time='pal')
        # 渲染范围设置
        #mc.setAttr('defaultRenderGlobals.startFrame', 1)  
        #mc.setAttr('defaultRenderGlobals.endFrame', 20)  
        
        # 开始处理
        from idmt.maya.py_common import sk_infoConfig
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        fpsFrame = anim.fps
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
            # 渲染范围设置
            mc.setAttr('defaultRenderGlobals.startFrame', startFrame)  
            mc.setAttr('defaultRenderGlobals.endFrame', endFrame)  

        # 输出格式设置
        mc.setAttr('defaultRenderGlobals.imageFormat', 7) 
        # 格式命名
        '''
        mc.optionMenuGrp('extMenu', e=1, select=1)
        mel.eval('changeMayaSoftwareFileNameFormat;')
        mc.optionMenuGrp('extMenu', e=1, select=3)
        mel.eval('changeMayaSoftwareFileNameFormat;')
        '''
        # 原先调用菜单，现在直接改节点
        mc.setAttr('defaultRenderGlobals.animation',1)
        mc.setAttr('defaultRenderGlobals.putFrameBeforeExt',1)
        mc.setAttr('defaultRenderGlobals.periodInExt',1)
        #mc.setAttr('defaultRenderGlobals.extensionPadding',3)
        mc.setAttr('defaultRenderGlobals.extensionPadding',3)
        if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
            mc.setAttr('defaultRenderGlobals.outFormatControl',0)
        
        # 清理未知节点
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        sk_checkCommon.sk_checkTools().checkDonotNodeCleanBase(0)

        # 关闭默认灯光
        mc.setAttr('defaultRenderGlobals.enableDefaultLight',0)

        print (u'===============!!!Done  【%s】!!!===============' % u'标准设置')
        print '\n'
        
    # mr 产品级设置    
    def mentalRayProductionLevel(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'MR设置')
        print 'Working...'
        
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)   
        try:
            mel.eval('loadPlugin "Mayatomr"')
        except:
            pass
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
        # 创建UI
        mel.eval('mentalrayUI ""')
        # 读取之前创建的production_preset
        mel.eval('nodePreset -load "miDefaultOptions" "production_mi"')
        
        mc.setAttr("miDefaultOptions.minSamples",0)
        mc.setAttr("miDefaultOptions.maxSamples",2)
        mc.setAttr("miDefaultOptions.contrastR",0.1)
        mc.setAttr("miDefaultOptions.contrastG",0.1)
        mc.setAttr("miDefaultOptions.contrastB",0.1)
        mc.setAttr("miDefaultOptions.contrastA",0.1)
        mc.setAttr("miDefaultOptions.filter",2)
        mc.setAttr("miDefaultOptions.filterWidth",1)
        mc.setAttr("miDefaultOptions.filterHeight",1)
        mc.setAttr("miDefaultOptions.jitter",1)
        mc.setAttr("miDefaultOptions.rayTracing",1)
        mc.setAttr("miDefaultOptions.maxReflectionRays",0)
        mc.setAttr("miDefaultOptions.maxRefractionRays",0)
        mc.setAttr("miDefaultOptions.maxRayDepth",0)
        mc.setAttr("miDefaultOptions.maxShadowRayDepth",2)
        mc.setAttr("miDefaultOptions.maxReflectionBlur",1)
        mc.setAttr("miDefaultOptions.maxRefractionBlur",1)
               
        # 默认image format
        if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
            mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
            mel.eval('changeMentalRayImageFormat')
        
        print (u'===============!!!Done  【%s】!!!===============' % u'MR设置')
        print '\n'

    # 【new】
    # 处理表格信息
    def clExcelInfoConfig(self,info):
        info = str(info)
        while info[-1] in [';',' ']:
            info = info[:-1]
        while '.' in info:
            info = info.split('.')[0]
        return info

    # 【new】
    # 处理excel灯光信息
    def clSkydomeExcelLoad(self):
        # 处理excel信息？
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projFullName = 'Calimero'
        
        #serverPath = '//file-cluster/GDC/Projects/' + projFullName + '/' + projFullName +  '_scratch/TD/ExcelInfo/' + str(shotInfo[1]) + '/' 
        serverPath = '//file-cluster/GDC/Projects/' + projFullName + '/Reference/Product manager/Render/ExcelInfo/' + str(shotInfo[1]) + '/' 
        serverExcelPath = serverPath + shotInfo[0].upper() + str(shotInfo[1]) + '_TimeOfDay.xls'
        
        print '-----'
        print serverExcelPath
        
        import os
        if not os.path.exists(serverExcelPath):
            serverExcelPath='//file-cluster/GDC/Projects/Calimero/Reference/Sylvain/ExcelInfo/'+str(shotInfo[1]) + '/' +shotInfo[0].upper() + str(shotInfo[1]) + '_TimeOfDay.xls'
            if not os.path.exists(serverExcelPath):
                print(u'=======本集Excel文件不存在，请联系TD及PA处理=======')
                mc.error(u'=======本集Excel文件不存在，请联系TD及PA处理=======')
            
        import xlrd
        reload(xlrd)
        shotAllData = xlrd.open_workbook(serverExcelPath).sheets()[0]
        
        rowMax = shotAllData.nrows
        rowID = 0
        for i in range(rowMax):
            shotID = self.clExcelInfoConfig(shotAllData.row_values(i)[0])
            checkID = shotInfo[2]
            while checkID[0] == '0':
                checkID = checkID[1:]
            while shotID[0] == '0':
                shotID = shotID[1:]
            if shotID == checkID:
                rowID = i
                break

        shotData = shotAllData.row_values(rowID)
        print shotData

        # skydomeId
        skyInfo = ['day','sunrise','sunset','night_on','night_off','day_autumn']
        skyMood = ''
        if shotData[1][-1] == ' ':
            skyMood = shotData[1][:-2]
        else:
            skyMood = shotData[1][:-1]
        
        skyMoodId = skyInfo.index(skyMood.lower())
            
        # assetAllInfo
        import os
        assetAllInfo = []
        txtName = 'assetAllReference.txt'
        assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
        print (assetNeedServerPath +  txtName )
        if os.path.exists(assetNeedServerPath +  txtName ):
            assetNeedOutputInfo = sk_infoConfig.sk_infoConfig().checkFileRead((assetNeedServerPath +  txtName ))
            if assetNeedOutputInfo:
                for i in range(len(assetNeedOutputInfo)/2):
                    assetAllInfo.append(assetNeedOutputInfo[i*2+1])
            else:
                print(u'======本镜头AssetReference信息没有输出|请重新将an文件放入daily check in======')
                mc.error(u'======本镜头AssetReference信息没有输出|请重新将an文件放入daily check in======')
        else:
            print(u'======本镜头AssetReference信息没有输出|请重新将an文件放入daily check in======')
            mc.error(u'======本镜头AssetReference信息没有输出|请重新将an文件放入daily check in======')
        checkHatchPlace  = 0
        setKey = ['int','ext']
        
        for asset in assetAllInfo:
            if 'HatchPlaceL' in asset and asset[-3:].lower() in setKey:
                checkHatchPlace = 1
            if 'HatchPlaceM' in asset and asset[-3:].lower() in setKey:
                checkHatchPlace = 2
            if 'HatchPlaceH' in asset and asset[-3:].lower() in setKey:
                checkHatchPlace = 3
        # 处理skydome
        skydomeWorld = mc.ls('*Skydome*:WORLD',type = 'transform')
        if skydomeWorld:
            mc.setAttr((skydomeWorld[0] + '.Mood'),skyMoodId)
            mc.setAttr((skydomeWorld[0] + '.location'),checkHatchPlace)
            
        skydomeLightGrp = mc.ls('*Skydome*:LIGHTING',type = 'transform')
        if skydomeLightGrp:
            mc.setAttr((skydomeLightGrp[0] + '.Mood'),skyMoodId)
            
        LIGHTgrp = mc.ls('*:LIGHTING',type = 'transform')
        if LIGHTgrp:
            for obj in LIGHTgrp:
                mc.setAttr((obj + '.Mood'),skyMoodId)
            
        # 额外的，处理skydome与灯光的关系
        self.cal_hide_skidome_lighting_if_set_int()

        # 额外的，隐藏非参考的灯光
        lights = mc.ls(type ='light')
        if lights:
            for light in lights:
                ifRef = mc.referenceQuery(light,isNodeReferenced = 1)
                if not ifRef:
                    mc.setAttr((mc.listRelatives(light,p=1,type= 'transform',f = 1)[0]+'.v'),0)
        
        #补充，若是室内INT场景，则隐藏灯光                                
        if shotData[2].split('_')[-1]=="Int;" or shotData[2].split('_')[-1]=='int;':
            if mc.ls('*:*SKYDOME_ALL'):
               obj = mc.ls('*:*SKYDOME_ALL',l=1)[0]
               mc.setAttr((obj + ".visibility"),False)

    # exr压缩格式设置
    # [dataatype]=4 16bit, =2 8 bit, =5 32 bit
    def setExtensionFramebuffer(self, datatype=4):    
            
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
        mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")

        # exr

        mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')        
        mc.setAttr('defaultRenderGlobals.imageFormat',51)
        mc.setAttr('defaultRenderGlobals.imfkey','exr',type = 'string')
        mc.setAttr('mentalrayGlobals.imageCompression',4)
        mc.setAttr('mentalrayGlobals.compressionQuality',0)

        # 8 zip
        mc.setAttr('mentalrayGlobals.imageCompression', 4)
        mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
        mc.setAttr('miDefaultFramebuffer.datatype', datatype)

        mc.editRenderLayerAdjustment('defaultRenderGlobals.imfPluginKey')
        mc.setAttr('defaultRenderGlobals.imfPluginKey','exr', type="string")    
        
        
        mc.editRenderLayerAdjustment('miDefaultOptions.finalGather')
        mc.setAttr('miDefaultOptions.finalGather', 0)    
        
        return


    # 获取所有SG节点
    def clRLSGNodesGet(self):
        SGNodes = mc.ls(type='shadingEngine')
        SGNodes.remove('initialParticleSE')
        SGNodes.remove('initialShadingGroup')
        # SG分类
        refSGCHR = []
        refSGPROP = []
        refSGSET = []
        refSGENV = []
        refSGSKY = []
        refSGCalimero = []
        # 判断分类
        # 根据连接的物体的参考进行判断
        for SGNode in SGNodes:
            if '_cam_' not in SGNode and '_CAM_' not in SGNode:
                listMeshTransform = mc.listConnections(SGNode, type='mesh')
                if listMeshTransform:
                    isRef = mc.referenceQuery(SGNode, isNodeReferenced=True)
                    # 参考类
                    if isRef:
                        # 只选一个进行处理即可
                        # 取参考路径
                        # 获取refPath
                        refPath = mc.referenceQuery(listMeshTransform[0], filename=True)
                        refPathInfo = refPath.lower()
                        # 角色
                        if '/characters/' in refPathInfo:
                            refSGCHR.append(SGNode)
                            # Calimero
                            if 'cali' in refPathInfo :
                                refSGCalimero.append(SGNode)
                        # 道具
                        if '/props/' in refPathInfo:
                            refSGPROP.append(SGNode)
                        # 其他类，下面细化
                        if '/sets/' in refPathInfo:
                            # Set
                            setKeys = ['_int','_ext']
                            configNum = 0
                            for key in setKeys:
                                if key in refPathInfo:
                                    refSGSET.append(SGNode)
                                else:
                                    configNum += 1
                            # Env
                            if configNum == 2:
                                refSGENV.append(SGNode)
                    else:
                        # 非参考类，由VFX提供
                        nameInfo = SGNode.lower()
                        # 道具
                        if '_prp_' in nameInfo:
                            refSGPROP.append(SGNode)


        result = []
        result.append(refSGCHR)
        result.append(refSGPROP)
        result.append(refSGSET)
        result.append(refSGENV)
        result.append(refSGSKY)
        result.append(refSGCalimero)
        return result
    
    # smoothSet
    def clRLDoSmooth(self, layerType=1):
        from idmt.maya.py_common import sk_smoothSet
        #import  sk_smoothSet
        reload(sk_smoothSet)
        # 非PFX层用
        if layerType == 1:
            sk_smoothSet.sk_smoothSetTools().smoothSetDoSmooth()
            
    # 【new】
    # asset可能会import，面临解锁
    
    # 【new】修改
    # vis属性
    def clRLVisConfig(self):
        objs = self.clRLObjectsTList()
        refVisTT = objs[6]
        if refVisTT:
            for asset in refVisTT:
                controlShapes = mc.listRelatives(asset , ad=1 , type = 'nurbsCurve', f= 1)
                if controlShapes:
                    for ctrlShape in controlShapes:
                        ctrl = mc.listRelatives(ctrlShape,p=1,type = 'transform',f=1)[0]
                        if mc.ls(ctrl + '.twoDline_vis'):
                            #mc.setAttr((ctrl + '.twoDline_vis'),1)
                            connections = mc.listConnections(ctrl, s=True, d=False, c=True, p=True)
                            if connections:
                                for i in range(0, len(connections),2):
                                    if 'twoDline_vis' in connections[i] or 'twoDline_vis' in connections[i+1]:
                                        print connections[i], connections[i+1]
                                        try:
                                            mc.disconnectAttr(connections[i+1], connections[i])
                                        except:
                                            pass
                            mc.setAttr((ctrl + '.twoDline_vis'),1)

                            #CHAR_PRIS:c_Facial_CTRL_FRAME
                            print 'setting to 1',ctrl    
        print 'clRLVisConfig------------ done --------------->'
        
    # 【new】
    # PFX属性修改
    def settingPFXvisibility(self, value):
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]
        rlObjs = refCalimero 
        for cal in rlObjs:
                print 'cal.......',cal
                rels = mc.listRelatives(cal, c=True)
                if rels:
                    print 'rels.......',cal
                    for rel in rels:
                        print 'rel.......',rel
                        if rel.endswith(':PFX'):
                            print 'SETTING PFX visibility',rel
                            mc.editRenderLayerAdjustment(rel + '.visibility')
                            mc.setAttr(rel+'.visibility', value)
        for aa in mc.ls('*GRP_twoDline_stroke', r=True):
            if '_CALI' in aa:
                try:
                    mc.editRenderLayerAdjustment(aa + '.visibility')
                    mc.setAttr(aa+'.visibility', value)    
                except:
                    print 'for some reason is not possible to change visibility of',aa
                    pass
        return
        
    
    # RGB层
    # No Lights
    def clRLRGBCreate(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'RGB层')
        print 'Working...'
        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        # 物体
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refCHR + refPROP + refSET + refSKY
        
        
        # 创建RenderLayer
        if (refCHR + refPROP + refSET):
            layerName = 'RGB'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(0)
            
            print '>>>>>---switching msh_iris_ visibility--->>>>>'
            for aa in mc.ls('*msh_iris_*_', r=True):
                if '_PRIS' in aa:
                    try:
                        print 'setting ',aa+'.visibility'
                        mc.editRenderLayerAdjustment(aa + '.visibility')
                        mc.setAttr(aa+'.visibility', 0)
                    except:
                        print 'ERROR:can\'t set visibility at 0',aa

            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1,f = 1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)
                
            # 连接renderPass
            # 赋予idpass1
            mc.connectAttr('RGB.renderPass', 'idPass1.owner')
            
            # 材质不理会
            # 设置
            # self.clRLCommonConfig()
            
            # 格式压缩
            self.setExtensionFramebuffer(datatype=16)
            
            mc.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")    
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_'+ '<RenderPass>', type='string')             
            mc.editRenderLayerAdjustment("defaultRenderGlobals.extensionPadding")
            mc.setAttr('defaultRenderGlobals.extensionPadding', 3)

            print (u'===============!!!Done  【%s】!!!===============' % u'RGB层' )
            print '\n'
        else:
            print (u'===============!!!None  【%s】!!!===============' % u'RGB层' )        
            print '\n'
            
    # BW层
    # No Lights
    def clRLBWCreate(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'BW层' )
        print 'Working...'
        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()        
        
        # 物体
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refPROP + refSET + refENV + refSKY + lights
        
        # 创建RenderLayer
        if (refPROP + refSET + refENV + refSKY):
            layerName = 'BW'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(0)
            
            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1,f = 1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)
            
            # 连接renderPass
            # 无
            
            # 材质
            SGnodes = self.clRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGPROP + refSGSET + refSGENV + refSGSKY
            
            # 创建备用材质组
            shaderName = 'SHD_' + 'BW'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            shaderNeed = mc.shadingNode ('lambert', asShader=True, name=shaderName)   
            mc.setAttr(('%s.color') % (shaderNeed), 1, 1, 1, type="double3")
            mc.setAttr(('%s.ambientColor') % (shaderNeed), 1, 1, 1, type="double3")
    
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # 寻找BW节点
                    needTxNode = RGBNode.replace('_RGB', '_BW')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
    
            # 设置
            # self.clRLCommonConfig()

            # 格式压缩
            self.setExtensionFramebuffer(datatype=2)
 
            mc.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")    
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_'+ '<RenderPass>', type='string')             
            mc.editRenderLayerAdjustment("defaultRenderGlobals.extensionPadding")
            mc.setAttr('defaultRenderGlobals.extensionPadding', 3)


            print (u'===============!!!Done  【%s】!!!===============' % u'BW层' )        
            print '\n'
        else:
            print (u'===============!!!None  【%s】!!!===============' % u'BW层' )        
            print '\n'

    
    # SPEC层
    # 客户灯光规则错误
    def clRLSPECCreate(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'SPEC层' )
        print 'Working...'
        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        
        # 物体
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refCHR + refPROP + lights
        
        # 创建RenderLayer
        if refCHR:
            layerName = 'SPEC'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(0)
                   
            # 主光开启，其他光隐藏
            for light in lights:
                if 'KEY' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 1, 1, 1, type='double3')
                else:
                    lightGrp = mc.listRelatives(light, p=1,f = 1)[0]
                    mc.editRenderLayerAdjustment(lightGrp + '.v')
                    mc.setAttr((light + '.v'), 0)
                    mc.editRenderLayerAdjustment(light + '.intensity')
      
                    mc.setAttr((light + '.intensity'), 0)
                    
                # 所有灯光黑色阴影
                mc.editRenderLayerAdjustment(light + '.shadowColor')
                mc.setAttr((light + '.shadowColor'), 0, 0, 0, type='double3')
                
            # 连接renderPass
            mc.connectAttr('SPEC.renderPass', 'idPassChr.owner')
            mc.connectAttr('SPEC.renderPass', 'idPassChrMain.owner')
            
            # 材质
            SGnodes = self.clRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGENV
            
            # 设置reflect属性
            # 仅仅关闭beauty开启specular
            mel.eval("renderLayerBuiltinPreset specular SPEC")
            
            # 设置
            # self.clRLCommonConfig()

            # 压缩格式
            self.setExtensionFramebuffer(datatype=2)

            mc.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")    
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_'+ '<RenderPass>', type='string')             
            mc.editRenderLayerAdjustment("defaultRenderGlobals.extensionPadding")
            mc.setAttr('defaultRenderGlobals.extensionPadding', 3)
                      
            print (u'===============!!!Done  【%s】!!!===============' % u'SPEC层' )        
            print '\n'
        else:
            print (u'===============!!!None  【%s】!!!===============' % u'SPEC层' )        
            print '\n'
       
    # RIMLIGHT层
    def clRLRIMLIGHTCreate(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'RIMLIGHT层' )
        print 'Working...'
        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()        
        
        # 物体
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refCHR + lights
        
        # 创建RenderLayer
        if refCHR:
            layerName = 'RIMLIGHT'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(0)
            
            # 主光开启强度1颜色1 1 1，其他光隐藏
            for light in lights:
                # 判断是否ENV的灯光
                if '_KEY' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 1, 1, 1, type='double3')
                else:
                    mc.editRenderLayerAdjustment(light + '.intensity')
                    mc.setAttr((light + '.intensity'), 0)
                    mc.editRenderLayerAdjustment(light + '.v')
                    mc.setAttr((light + '.v'), 0)
                # 所有灯光黑色阴影
                mc.editRenderLayerAdjustment(light + '.shadowColor')
                mc.setAttr((light + '.shadowColor'), 0, 0, 0, type='double3')
            
            # 连接renderPass
            
            # 材质
            SGnodes = self.clRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR
            
            # 创建备用材质组
            shaderName = 'SHD_' + 'BLACK'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            shaderNeed = mc.shadingNode ('lambert', asShader=True, name=shaderName)   
            mc.setAttr(('%s.color') % (shaderNeed), 0, 0, 0, type="double3")
    
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # 寻找RIMLIGHT节点
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_RIM')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_RIM')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
                                  
            # 设置
            # self.clRLCommonConfig()

            # 压缩格式
            self.setExtensionFramebuffer(datatype=2)
 
            mc.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")    
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_'+ '<RenderPass>', type='string')             
            mc.editRenderLayerAdjustment("defaultRenderGlobals.extensionPadding")
            mc.setAttr('defaultRenderGlobals.extensionPadding', 3)
             
            print (u'===============!!!Done  【%s】!!!===============' % u'RIMLIGHT层' )        
            print '\n'
        else:
            print (u'===============!!!None  【%s】!!!===============' % u'RIMLIGHT层' )        
            print '\n'

    # LIGHT层
    # 客户灯光规则错误
    # 另外可能从SHD_LIGHT提供
    def clRLLIGHTCreate(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'LIGHT层' )
        print 'Working...'
        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
     
        # 物体
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refCHR + refPROP + refSET + refSKY + lights
        
        # 创建RenderLayer
        if (refCHR + refPROP + refSET + refSKY):
            layerName = 'LIGHT'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # 连接renderPass
            mc.connectAttr('LIGHT.renderPass', 'idPass3.owner')
            
            
            # KEY光红色，BRANCH蓝色，EXTRA绿色
            for light in lights:
                # 判断是否ENV的灯光
                if '_KEY' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 1, 0, 0, type='double3')
                if '_BOUNCE' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 0, 0, 1, type='double3')
                if '_EXTRA' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 0, 1, 0, type='double3')
                if '_ONLY' in light:
                    if '_KEY' not in light and '_BOUNCE' not in light and '_EXTRA' not in light:
                        mc.editRenderLayerAdjustment(light + '.intensity')
                        mc.setAttr((light + '.intensity'), 0)
                        mc.editRenderLayerAdjustment(light + '.v')
                        mc.setAttr((light + '.v'), 0)
                # 所有灯光黑色阴影
                mc.editRenderLayerAdjustment(light + '.shadowColor')
                mc.setAttr((light + '.shadowColor'), 0, 0, 0, type='double3')
    
            # 材质
            SGnodes = self.clRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR + refSGPROP + refSGSET + refSGSKY
            
            # 创建备用材质组
            shaderName = 'SHD_' + 'LIGHT'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            shaderNeed = mc.shadingNode ('lambert', asShader=True, name=shaderName)   
            mc.setAttr(('%s.color') % (shaderNeed), 1, 1, 1, type="double3")
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # 寻找LIGHT节点
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_LIGHT')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_LIGHT')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode) and 'LIGHT' in needTxNode:
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'), f=1)
            # 设置
            # self.clRLCommonConfig()

            # 压缩格式
            self.setExtensionFramebuffer(datatype=16)

            mc.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")    
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_'+ '<RenderPass>', type='string')             
            mc.editRenderLayerAdjustment("defaultRenderGlobals.extensionPadding")
            mc.setAttr('defaultRenderGlobals.extensionPadding', 3)
          
    
            print (u'===============!!!Done  【%s】!!!===============' % u'LIGHT层' )        
            print '\n'
        else:
            print (u'===============!!!None  【%s】!!!===============' % u'LIGHT层' )        
            print '\n'


    # LIGHTCHR层
    # 客户灯光规则错误
    # 另外可能从SHD_LIGHT提供
    def clRLLIGHTCHRCreate(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'LIGHTCHR层' )
        print 'Working...'
        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

      
        # 物体
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refCHR + refPROP + refSET +refSKY + lights
        
        # 创建RenderLayer
        if (refCHR + refPROP + refSET + refSKY):
            layerName = 'LIGHT'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # 连接renderPass
            #mc.connectAttr('LIGHT.renderPass', (prefixName+'_idPass3.owner'))
            
            # 处理SET的pr属性
            if refSET:
                meshes = mc.listRelatives(refSET,ad = 1,ni =1 ,type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'), 0)
            
            # KEY光红色，BRANCH蓝色，EXTRA绿色
            for light in lights:
                # 判断是否ENV的灯光
                if '_KEY' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 1, 0, 0, type='double3')
                if '_BOUNCE' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 0, 0, 1, type='double3')
                if '_EXTRA' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 0, 1, 0, type='double3')
                if '_ONLY' in light:
                    if '_KEY' not in light and '_BOUNCE' not in light and '_EXTRA' not in light:
                        mc.editRenderLayerAdjustment(light + '.intensity')
                        mc.setAttr((light + '.intensity'), 0)
                        mc.editRenderLayerAdjustment(light + '.v')
                        mc.setAttr((light + '.v'), 0)
                # 所有灯光黑色阴影
                mc.editRenderLayerAdjustment(light + '.shadowColor')
                mc.setAttr((light + '.shadowColor'), 0, 0, 0, type='double3')
    
            # 材质
            SGnodes = self.clRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR + refSGPROP + refSGSET + refSGSKY
            
            # 创建备用材质组
            shaderName = 'SHD_' + 'LIGHT'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            shaderNeed = mc.shadingNode ('lambert', asShader=True, name=shaderName)   
            mc.setAttr(('%s.color') % (shaderNeed), 1, 1, 1, type="double3")
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # 寻找LIGHT节点
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_LIGHT')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_LIGHT')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode) and 'LIGHT' in needTxNode:
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'), f=1)
            # 设置
            # self.clRLCommonConfig()
            
            self.cal_hide_skidome_lighting_if_set_int()

            # 压缩格式
            self.setExtensionFramebuffer(datatype=16)
   
            mc.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")    
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_'+ '<RenderPass>', type='string')             
            mc.editRenderLayerAdjustment("defaultRenderGlobals.extensionPadding")
            mc.setAttr('defaultRenderGlobals.extensionPadding', 3)
          
    
            print (u'===============!!!Done  【%s】!!!===============' % u'LIGHTCHR层' )        
            print '\n'
        else:
            print (u'===============!!!None  【%s】!!!===============' % u'LIGHTCHR层' )        
            print '\n'

    # LIGHTSET层
    # 客户灯光规则错误
    # 另外可能从SHD_LIGHT提供
    def clRLLIGHTSETCreate(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'LIGHTSET层' )
        print 'Working...'
        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

      
        # 物体
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_SetKeyLight' in lights:
            lights.remove('IDMT_2D_SetKeyLight')
        if 'IDMT_2D_SetSideLight' in lights:
            lights.remove('IDMT_2D_SetSideLight')
        
        # 物体
        rlObjs = refCHR + refPROP + refSET + refSKY + lights
        
        # 创建RenderLayer
        if (refCHR + refPROP + refSET + refSKY):
            layerName = 'LIGHTSET'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # 连接renderPass
            mc.connectAttr('LIGHTSET.renderPass', 'idPass3.owner')
            
            # 处理CHR,PROP的pr属性
            if (refCHR + refPROP):
                meshes = mc.listRelatives((refCHR + refPROP),ad = 1,ni =1 ,type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'), 0)
            
            # KEY光红色，BRANCH蓝色，EXTRA绿色
            for light in lights:
                # 判断是否ENV的灯光
                if '_KEY' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 1, 0, 0, type='double3')
                if '_BOUNCE' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 0, 0, 1, type='double3')
                if '_EXTRA' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 0, 1, 0, type='double3')
                if '_ONLY' in light:
                    if '_KEY' not in light and '_BOUNCE' not in light and '_EXTRA' not in light:
                        mc.editRenderLayerAdjustment(light + '.intensity')
                        mc.setAttr((light + '.intensity'), 0)
                        mc.editRenderLayerAdjustment(light + '.v')
                        mc.setAttr((light + '.v'), 0)
                # 所有灯光黑色阴影
                mc.editRenderLayerAdjustment(light + '.shadowColor')
                mc.setAttr((light + '.shadowColor'), 0, 0, 0, type='double3')
    
            # 材质
            SGnodes = self.clRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR + refSGPROP + refSGSET + refSGSKY
            
            # 创建备用材质组
            shaderName = 'SHD_' + 'LIGHTSET'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            shaderNeed = mc.shadingNode ('lambert', asShader=True, name=shaderName)   
            mc.setAttr(('%s.color') % (shaderNeed), 1, 1, 1, type="double3")
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # 寻找LIGHT节点
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_LIGHT')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_LIGHT')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode) and 'LIGHT' in needTxNode:
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'), f=1)
            # 设置
            # self.clRLCommonConfig()
            self.cal_hide_skidome_lighting_if_set_int()

            # 压缩格式
            self.setExtensionFramebuffer(datatype=16)

            mc.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")    
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_'+ '<RenderPass>', type='string')             
            mc.editRenderLayerAdjustment("defaultRenderGlobals.extensionPadding")
            mc.setAttr('defaultRenderGlobals.extensionPadding', 3)
             
            print (u'===============!!!Done  【%s】!!!===============' % u'LIGHTSET层' )        
            print '\n'
        else:
            print (u'===============!!!None  【%s】!!!===============' % u'LIGHTSET层' )        
            print '\n'

    # ZDEPTH层
    # No Lights
    def clRLZDEPTHCreate(self, distance=14000):
        print (u'===============!!!Start 【%s】!!!===============' % u'ZDEPTH层' )
        print 'Working...'
        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        
        # 物体
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refCHR + refPROP + refSET + refENV + refSKY
        
        # 创建RenderLayer
        if (refCHR + refPROP + refSET + refENV + refSKY):
            layerName = 'ZDEPTH'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(0)
            
            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1,f = 1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)            
                mc.setAttr((light + '.intensity'), 0)
    
            # 连接renderPass
            
            # 材质
            SGnodes = self.clRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR + refSGPROP + refSGSET + refSGENV + refSGSKY
    
            # 创建备用材质组
            shaderName = 'SHD_' + 'ZDEPTH'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            if mc.ls('%s_sampleInfo' % (shaderName)):
                mc.delete('%s_sampleInfo' % (shaderName))
            if mc.ls('SHD_ZDEPTH_setRangeZ'):
                mc.delete('SHD_ZDEPTH_setRangeZ')
            if mc.ls('SHD_ZDEPTH_multDivZ'):
                mc.delete('SHD_ZDEPTH_multDivZ')
            if mc.ls('SHD_ZDEPTH_sampInfoZ'):
                mc.delete('SHD_ZDEPTH_sampInfoZ')  
            if mc.ls('SHD_Depth_SG'):
                mc.delete('SHD_Depth_SG')  
            depthShader = mc.shadingNode ('lambert', asShader=True, name=shaderName)
            mc.setAttr((depthShader + '.ambientColor'),1,1,1,type = 'double3')
            setRangeNode = mc.shadingNode ('setRange', asUtility=True, name='SHD_ZDEPTH_setRangeZ')
            mc.setAttr((setRangeNode+'.minX'),1)
            multiplyDivideNode = mc.shadingNode ('multiplyDivide', asUtility=True, name='SHD_ZDEPTH_multDivZ')
            mc.setAttr((multiplyDivideNode+'.input2X'),-1)
            samplerInfoNode = mc.shadingNode ('samplerInfo', asUtility=True, name='SHD_ZDEPTH_sampInfoZ')
            mc.addAttr(samplerInfoNode, longName='NearClipCalimero',nn='Near Clip Calimero', attributeType='float', defaultValue=0.1)
            mc.addAttr(samplerInfoNode, longName='FarClipCalimero',nn='Far Clip Calimero', attributeType='float', defaultValue= distance )
            depthSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='SHD_Depth_SG')
            mc.connectAttr(('%s.%s') % (depthShader , 'outColor') , ('%s.%s') % (depthSG , 'surfaceShader'), f=True)
            shaderNeed = depthShader
            # 连接
            mc.connectAttr(('%s.%s') % (setRangeNode , 'outValueX') , ('%s.%s') % (depthShader , 'colorR'), f=True)
            mc.connectAttr(('%s.%s') % (setRangeNode , 'outValueX') , ('%s.%s') % (depthShader , 'colorG'), f=True)
            mc.connectAttr(('%s.%s') % (setRangeNode , 'outValueX') , ('%s.%s') % (depthShader , 'colorB'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfoNode , 'NearClipCalimero') , ('%s.%s') % (setRangeNode , 'oldMinX'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfoNode , 'FarClipCalimero') , ('%s.%s') % (setRangeNode , 'oldMaxX'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfoNode , 'pointCameraZ') , ('%s.%s') % (multiplyDivideNode , 'input1X'), f=True)
            mc.connectAttr(('%s.%s') % (multiplyDivideNode , 'outputX') , ('%s.%s') % (setRangeNode , 'valueX'), f=True)
    
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # 寻找ZDEPTH节点
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_ZDEPTH')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_ZDEPTH')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
    
            # 设置
            # self.clRLCommonConfig()
            
            # sampInfoZ
            sampleInfoZ = mc.ls('*_sampInfoZ',type = 'samplerInfo' ) + mc.ls('*:*_sampInfoZ',type = 'samplerInfo' )
            if sampleInfoZ:
                for sampleNode in sampleInfoZ:
                    mc.setAttr((sampleNode + '.NearClipCalimero'),0.1)
                    mc.setAttr((sampleNode + '.FarClipCalimero'),distance)

            # 压缩格式
            self.setExtensionFramebuffer(datatype=5)

            mc.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")    
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_'+ '<RenderPass>', type='string')             
            mc.editRenderLayerAdjustment("defaultRenderGlobals.extensionPadding")
            mc.setAttr('defaultRenderGlobals.extensionPadding', 3)
           
            print (u'===============!!!Done  【%s】!!!===============' % u'ZDEPTH层' )        
            print '\n'
        else:
            print (u'===============!!!None  【%s】!!!===============' % u'ZDEPTH层' )        
            print '\n'

    # BG_RGB层
    def clRLBGRGBCreate(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'BG_RGB' )
        print 'Working...'
        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        
        # 物体
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refENV + lights
        
        if refENV:
            
            # 创建RenderLayer
            layerName = 'BG_RGB'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1,f = 1)[0]
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
            
            # 连接renderPass
            mc.connectAttr('BG_RGB.renderPass', 'idPass2.owner')
            
            # 设置
            # self.clRLCommonConfig()
            
            #压缩格式
            self.setExtensionFramebuffer(datatype=16)

            imageFilePrefix = '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_<RenderPass>'
            mc.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")    
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', imageFilePrefix, type='string')              
            mc.editRenderLayerAdjustment("defaultRenderGlobals.extensionPadding")
            mc.setAttr('defaultRenderGlobals.extensionPadding', 3)
           
            print (u'===============!!!Done  【%s】!!!===============' % u'BG_RGB层' )        
            print '\n'
        else:
            print (u'===============!!!None  【%s】!!!===============' % u'BG_RGB层' )        
            print '\n'        
        
        
    # RENDER2D层
    def clRLBGRENDER2DCreate(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'RENDER_2D层' )
        print 'Working...'
        
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        
        # 物体
        # 仅仅ENV，不接受阴影
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        #lights = mc.ls(type='light')
        lights = []

        # CreateLight
        # 主光
        if mc.ls('IDMT_2D_KeyLight'):
            mc.delete('IDMT_2D_KeyLight')
        if mc.ls('IDMT_2D_SideLight'):
            mc.delete('IDMT_2D_SideLight')
        keyLight = mc.directionalLight(name='IDMT_2D_KeyLight', rotation=(-24, 36, 11), intensity=1)
        mc.setAttr((keyLight + '.color'), 1, 1, 1, type='double3')
        mc.setAttr((keyLight + '.intensity'), 0.5)
        mc.setAttr((keyLight + '.useDepthMapShadows'), 0)
        mc.setAttr((keyLight + '.useRayTraceShadows'), 1)
        mc.setAttr((keyLight + '.lightAngle'), 0)
        mc.setAttr((keyLight + '.shadowRays'), 1)
        mc.setAttr((keyLight + '.rayDepthLimit'), 1)
        lights.append(mc.listRelatives(keyLight,p=1,type = 'transform',f= 1)[0])
        # 辅光
        sideLight = mc.directionalLight(name='IDMT_2D_SideLight', rotation=(90, 0, 0), intensity=0.5)
        mc.setAttr((sideLight + '.color'), 1, 1, 1, type='double3')
        mc.setAttr((sideLight + '.intensity'), 0.3)
        mc.setAttr((sideLight + '.useDepthMapShadows'), 0)
        mc.setAttr((sideLight + '.useRayTraceShadows'), 0)
        lights.append(mc.listRelatives(sideLight,p=1,type = 'transform',f= 1)[0])

        # 物体
        rlObjs = refENV + refCHR + refPROP + lights
        
        if refENV:
            # 创建RenderLayer
            layerName = 'RENDER_2D'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            refCOL = []
            meshCol = mc.ls('*_COL:*',type = 'mesh', l = 1) + mc.ls('*_COL_*:*',type = 'mesh', l = 1)
            if meshCol:
                refCOL = list(set(mc.listRelatives(meshCol , p = 1 , type = 'transform', f = 1)))
            
            # 处理ENV的mesh不接受阴影
            for grp in (refENV + refCOL):
                allChildren = mc.listRelatives(grp, ad=1, type='transform',f = 1)
                # 只处理mesh
                if allChildren:
                    for child in allChildren:
                        shape = mc.listRelatives(child, s=1,f= 1)
                        if shape:
                            if mc.nodeType(shape[0]) == 'mesh':
                                # 处理不接收阴影
                                mc.editRenderLayerAdjustment(shape[0] + '.receiveShadows')
                                mc.setAttr((shape[0] + '.receiveShadows'), 0)
    
            # 隐藏灯光
            for light in lights:
                lightGrp = light
                if 'IDMT_2D_' not in light:
                    mc.editRenderLayerAdjustment(light + '.intensity')
                    mc.setAttr((light + '.intensity'), 0)
                    mc.editRenderLayerAdjustment(lightGrp + '.v')
                    mc.setAttr((light + '.v'), 0)
                else:
                    mc.editRenderLayerAdjustment(lightGrp + '.v')
                    mc.setAttr((light + '.v'), 1)
                
            # 材质
            SGnodes = self.clRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR + refSGPROP + refSGSET + refSGENV  + refSGSKY
            
            # 创建备用材质组
            #mc.setAttr(('%s.outColor') % (shaderNeed), 0, 0, 0, type="double3")
            
            # 处理物体
            sets = mc.ls('*:smooth*',type = 'objectSet')
            needSets = []
            if sets:
                for setInfo in sets:
                    if '_col_' in setInfo.split(':')[0].lower():
                        needSets.append(setInfo)
            if needSets:   
                for setInfo in needSets:
                    objs = mc.sets(setInfo,q = 1)
                    objs = mc.ls(objs ,l = 1)
                    for obj in objs:
                        mesh = mc.listRelatives(obj,s=1,ni=1,type='mesh',f=1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                        mc.setAttr((mesh + '.castsShadows'),0)
                        mc.setAttr((mesh + '.receiveShadows'),0)
            # 连接材质
            for SGNode in rlSGNodes:
                id = rlSGNodes.index(SGNode)
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    colState = 0
                    if '_col_' in RGBNode.split(':')[0].lower():
                        colState = 1
                    needTxNode = ''
                    shaderNode = ''
                    # 寻找2D节点
                    if '_RGBA' not in needTxNode:
                        needTxNode = RGBNode.replace('_RGB', '_2D')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_2D')
                    
                    # 存在2D材质节点    
                    if mc.objExists(needTxNode):
                        shaderNode = needTxNode    

                    # 不存在
                    else:
                        shader_2D = 'SHD_CALI_' +str(id) + '_2D'
                        if mc.ls(shader_2D):
                            mc.delete(shader_2D)
                        shader_2D = mc.shadingNode ('lambert', asShader=True, name = shader_2D)   
                            
                        shaderAOConn = mc.listConnections((RGBNode + '.ambientColor'),plugs = 1)
                        shaderCOConn = mc.listConnections((RGBNode + '.color'),plugs = 1)
                        shaderTsConn = mc.listConnections((RGBNode + '.transparency'),plugs = 1)
                        
                        if not shaderCOConn:
                            if mc.nodeType(RGBNode) == 'surfaceShader':
                                mc.copyAttr((RGBNode + '.outColor'),(shader_2D + '.color'),v = 1)
                            else:
                                mc.copyAttr((RGBNode + '.color'),(shader_2D + '.color'),v = 1)
                        else:
                            mc.connectAttr((shaderCOConn[0]),(shader_2D + '.color'))
                            
                        if not shaderTsConn:
                            mc.copyAttr((RGBNode + '.transparency'),(shader_2D + '.transparency'),v = 1)
                        else:
                            mc.connectAttr((shaderTsConn[0]),(shader_2D + '.transparency'))
                            
                        if not shaderAOConn:
                            mc.copyAttr((RGBNode + '.ambientColor'),(shader_2D + '.ambientColor'),v = 1)
                            if colState:
                                mc.setAttr((shader_2D + '.ambientColor'),1,1,1,type = 'double3')
                        else:
                            mc.setAttr((shader_2D + '.ambientColor'),1,1,1,type = 'double3')

                        mc.setAttr((shader_2D + '.diffuse'),0.4)								#add by wanshoulong 2015/4/13 http://moss-server/Project/Calimero/Lists/Calimero/Flat.aspx?RootFolder=%2fProject%2fCalimero%2fLists%2fCalimero%2f1%20Sylvain%e7%ad%94%e5%a4%8d%e6%b5%8b%e8%af%95%e7%9a%84%e6%96%b0%e9%95%9c%e5%a4%b4&FolderCTID=0x012002002323950FE61CDB458C48255DCB3CF176&TopicsView=http%3A%2F%2Fmoss%2Dserver%2FProject%2FCalimero%2FLists%2FCalimero%2FAllItems%2Easpx

                        # 连接自定义2D材质球
                        shaderNode = shader_2D
                        '''
                        shaderAO = mc.listConnections((RGBNode + '.ambientColor'),plugs = 1)
                        if shaderAO:
                            mc.editRenderLayerAdjustment((RGBNode + '.ambientColor'))
                            mc.disconnectAttr(shaderAO[0], (RGBNode + '.ambientColor'))
                        mc.setAttr((RGBNode + '.ambientColor'),1,1,1,type = 'double3')
                        '''
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((shaderNode + '.outColor'), (SGNode + '.surfaceShader'))
            
            # 赋予idpass1
            mc.connectAttr('RENDER_2D.renderPass', 'idPass1.owner')

            # 设置
            # self.clRLCommonConfig()

            # 压缩格式
            self.setExtensionFramebuffer(datatype=16)

            mc.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")    
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_'+ '<RenderPass>', type='string')             
            mc.editRenderLayerAdjustment("defaultRenderGlobals.extensionPadding")
            mc.setAttr('defaultRenderGlobals.extensionPadding', 3)
                                
            print (u'===============!!!Done  【%s】!!!===============' % u'RENDER_2D层' )        
            print '\n'
            return True
        else:
            print (u'===============!!!None  【%s】!!!===============' % u'RENDER_2D层' )        
            print '\n'
            return False


    # PFX层,仅仅CALI
    def clRLBGPFXCreate(self):
        print (u'===============!!!Start 【%s】!!!===============' % u'PFX层' )
        print 'Working...'

        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        # 物体
        objs = self.clRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]
        
        # 判断'CHR_GRP'自定义属性，且判断值
        
        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')

        # 物体
        rlObjs = refCalimero 
        if refCalimero:
            # 创建RenderLayer
            layerName = 'PFX'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(1)
            
            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1,f = 1)[0]
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                   
            # 连接renderPass
    
            # 材质
            SGnodes = self.clRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCalimero
            
            # 创建备用材质组
            shaderName = 'SHD_' + 'BLACK'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            shaderNeed = mc.shadingNode ('lambert', asShader=True, name=shaderName)   
            mc.setAttr(('%s.color') % (shaderNeed), 0, 0, 0, type="double3")
    
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    '''
                    # 寻找内部节点
                    listTxNodes = mc.listConnections(RGBNode)
                    for nd in listTxNodes:
                        if "_BLACK" in nd:
                            needTxNode = nd
                            break
                    '''
                    # 寻找BLACK节点
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_BLACK')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_BLACK')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
            
            # 设置
            # self.clRLCommonConfig()

            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')        
            mc.setAttr('defaultRenderGlobals.imageFormat', 32)
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imfPluginKey')
            mc.setAttr('defaultRenderGlobals.imfPluginKey','png', type="string")

            # 渲染器
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')
            
            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 3840)
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 2160)
            try :
                mc.setAttr('defaultResolution.enableStrokeRender', 1)
            except :
                pass
    
            # exr格式
            '''
            if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                mel.eval('changeMentalRayImageFormat')
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                mel.eval('changeMentalRayImageFormat')
            '''
            
            # 8位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 2)
 

            mc.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")    
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<RenderPass>/CAL_' +  shotInfo[1] + '_' + shotInfo[2] +  '_LAYERS_'+ '<RenderPass>', type='string')             
            mc.editRenderLayerAdjustment("defaultRenderGlobals.extensionPadding")
            mc.setAttr('defaultRenderGlobals.extensionPadding', 3)
           
              
            print (u'===============!!!Done  【%s】!!!===============' % u'PFX层' )        
            print '\n'
            return True
        else:
            print (u'===============!!!None  【%s】!!!===============' % u'PFX层' )        
            print '\n' 
            return False
        


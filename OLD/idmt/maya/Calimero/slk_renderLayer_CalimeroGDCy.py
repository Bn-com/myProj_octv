# -*- coding: utf-8 -*-

'''
Created on 2013-6-18

@author: shenkang
'''
import maya.cmds as cmds
import maya.mel as mel
import os
import shutil
from subprocess import call
import sys
import time
#sys.path.append('Z:/AK_PIPELINE/maya/python/')
#import readExcel as rdexc
#reload(rdexc)


# shader import 
# file nodes ,for tga ,filter off ,for map ,filter config minmap
'''
import sys
sys.path.append('Z:/AK_SCRIPTS/AK_PRERENDER/GDC_Prerender/')
import slk_renderLayer_Calimero as slk
reload(slk)
clr = slk.cllRLConfig()
clr.cllRLAutoCreate()



import sys
sys.path.append('Z:/AK_SCRIPTS/AK_PRERENDER/GDC_Prerender/')
import slk_renderLayer_Calimero as slk
reload(slk)
clr = slk.cllRLConfig(correctTexturesAndSave=True)
clr.cllRLAutoCreate()


#wrongRef is set to True identify assets based on their top node versus the folder they are stored in... shouldnt be used, just in case of debug scene out of pipeline
#correctTexturesAndSave if set to True, check and subsitute all wrong references and save the corrected scene before splitting layers
#projectBase points to the proper location of textures
#oldProjectBase is the string to be substituted with projectBase


'''
def get_resolved_path(path):
    list_file = cmds.file(q=True, l=True)
    
    for file in list_file:
        file.encode('utf-8')
        if file.find(path.replace("/","\\")) != -1 or file.find(path.replace("\\","/")) != -1:
            return file
    return path    
    
class cllRLConfig(object):
    sceneName = None
    episode = None
    shot = None
    wrongRef = None
    pathLocalBase = None
    bklfile = None
    
    
    def __init__(self):
        pass
    '''
    def __init__(self, wrongRef=False, bklfile=r'Z:\CALI_Ref\CA_Ep106\BKLCA106_2013_06_18_mood.xlsx', correctTexturesAndSave=False, projectBase='//tex/Calimero/CAL_RSYNC/CAL_MAYA', oldProjectBase='//tex.alphanim.lan/Calimero/CAL_RSYNC/CAL_MAYA'):
        self.bklfile = None
        if not os.path.isfile(bklfile):
            print 'bkl file',bklfile,'doensn\'t exist'
        else:
            self.bklfile = bklfile
        self.wrongRef = wrongRef
        self.sceneName = cmds.file(q=True, sn=True)
        self.episode = os.path.basename(self.sceneName).split('_')[1].replace('ep','')
        self.shot = os.path.basename(self.sceneName).split('_')[2].replace('sh','')
        shotInfo = self.checkShotInfo()
        self.pathLocalBase = '//TEX/Calimero/01_SAISON_1/11_TEAMSHARE/Sylvain/PRERENDER/'+shotInfo[1]+'/scenes/sh'+shotInfo[2].replace('sh','')+'/publish/'
        
        #####
        #change the name of the camera dag node to akcam for compositing issue
        
        shotN = None
        mainCamera = 'perspShape'
        for el in os.path.basename(cmds.file(q=True, sn=True)).split('_'):
            if el.startswith('sh'):
                shotN = el.replace('sh','')
                break
        for cam in cmds.ls(type='camera'):
            if shotN in cam or "CAMERA" in cam:
                mainCamera = cam
                break
        if mainCamera != 'perspShape':            #which means i found a valid camera matching the shot!!
            for cam in cmds.ls(type='camera'):
                val = False
                if cam==mainCamera: val = True
                cmds.setAttr(cam+'.renderable', val)
            cameranode = cmds.listRelatives(mainCamera, f=True, p=True)[0]
            if mainCamera.find('CAMERA') == -1:
                newcam = cmds.rename(cameranode, 'CAMERA',ignoreShape=True)                            ##this will not change the shape name... no need to change setCurrentCamera procedure
                camshape = cmds.listRelatives('*CAMERA*', f=True, c=True, type='camera')[0]
            else:
                camshape = cmds.listRelatives(cameranode, f=True, c=True, type='camera')[0]
            cmds.setAttr(camshape+'.nearClipPlane', 1)
            cmds.setAttr(camshape+'.farClipPlane',70000)
            if mainCamera.find('CAMERA') == -1:
                cmds.rename(camshape, 'cam_'+str('106')+'_'+str(shotN))
        self.cal_hide_skidome_lighting_if_set_int()    
    '''
        #####
        '''
        if self.bklfile:
            excekfile = rdexc.readExcel(self.bklfile)
            elems = excekfile.getEpisodeElem(shot=self.shot)
            if elems['mood'].lower()=='night_on':
                cmds.setAttr("*:*LIGHTING.Mood", 3)
                self.cal_lampost_cast_shadow_off()
        '''
        
        '''
        # GDC do not
        if correctTexturesAndSave:
            #cmds.setAttr('defaultRenderGlobals.preMel', "eval (\"source \\\"AK_PRERENDER/akPreRender.mel\\\"\");", type="string")
            #cmds.setAttr('defaultRenderGlobals.preMel', "eval (\"source \\\"//VELA/vela/prod/CALIMERO/AK_SCRIPTS/AK_PRERENDER/akPreRender.mel\\\"\");", type="string")  
            self.checkTextures(projectBase)
            self.recover_map_from_zip()
            self.saveScene()
        '''
            
            
    def saveScene(self):
        fileName = self.pathLocalBase + os.path.basename(self.sceneName)
        cmds.file(rename=fileName)
        cmds.file(save=True)
        return
    
    def checkTextures(self, projectBase):
        files = cmds.ls(type='file')
        for fil in files:        
            texture = cmds.getAttr(fil+'.fileTextureName')
            #print projectBase,'sourceimages',texture.split('sourceimages')[-1]
            if not projectBase.endswith('/'): projectBase += '/'
            typ = 'sourceimages'
            if 'SOURCEIMAGES' in texture: typ = 'SOURCEIMAGES'
            newTexture = projectBase+'sourceimages'+texture.split(typ)[-1]
            print 'renaming',texture,'---->',newTexture
            cmds.setAttr(fil+'.fileTextureName',newTexture,type='string')
        return
        
    def get_asset_name_by_path(self, path):
        path_split_slash = path.replace("\\","/").split("/")
        for i,part_of_path in enumerate(path_split_slash):
            if (part_of_path == "SETS" or  part_of_path == "PROPS" or part_of_path == "CHARACTERS" or part_of_path == "FX") and i != len(path_split_slash)-1:
                if part_of_path == "PROPS" and i != len(path_split_slash)-2:
                    return path_split_slash[i+2]
                else:
                    return path_split_slash[i+1]
        return ""
        
    def recover_map_from_zip(self):
        print '====================!!!zip to map!!!===================='
        list_file = cmds.ls(l=True, type="file")
        for file in list_file:
            fileTextureName = cmds.getAttr(file + ".fileTextureName")
            destination_folder = "//tex/Calimero/01_SAISON_1/11_TEAMSHARE/Sylvain/CAL_SOURCESIMAGES/" + self.get_asset_name_by_path(fileTextureName) + "/"
            # destination_folder = "D:/" + self.get_asset_name_by_path(fileTextureName) + "/"
            result2 = self.convert_zip_to_map_ga(fileTextureName, destination_folder)
            if result2 != "":
                print file.replace(".png",".zip") + " map unzipped" 
                cmds.setAttr(file + ".fileTextureName", result2, type="string")
                print file.replace(".png","") + " switch to map"   

    def cal_lampost_cast_shadow_off():
        lighting_mood_list = cmds.ls("*:*LIGHTING.Mood")
        if cmds.getAttr(lighting_mood_list[0]) == 3:
            wanted_selection_list = ["*:*Bar*", "*:*bar*", "*:*BillBoard*", "*:*Billboard*", "*:*billboard*", "*:*Light*", "*:*light*", "*:*Bulb*", "*:*bulb*"]
            mesh_for_cast_shadow_of_list = []
            for wanted_selection in wanted_selection_list:
                mesh_list = cmds.ls(wanted_selection, l=True, type="mesh")
                for mesh in mesh_list:
                    if mesh.find("LAMPOST_") != -1 or mesh.find("WALLLAMP_")!= -1 or mesh.find("street_lamp_") != -1 or mesh.find("WallLamps_") != -1 or mesh.find("WALLLAMPB") != -1:
                        cmds.setAttr(mesh + ".castsShadows", 0)
                        
    def cal_hide_skidome_lighting_if_set_int(self):
        set_int_list = cmds.objExists("*SET_*_INT:*")
        dzn_int_list = cmds.objExists("*DZN_*_INT:*")
        if set_int_list or dzn_int_list:
            cmds.setAttr("*_SKYDOME:LIGHTING.visibility",False)
                        
    def _checkTextures(self, useMapVsPng = True, useTextureLocal=True, projectBase='M:/CAL_RSYNC/CAL_MAYA', oldProjectBase='//tex.alphanim.lan/Calimero/CAL_RSYNC/CAL_MAYA'):
        '''
        # if useTextureLocal is false then textures are read wherever they are
        # if useTextureLocal is true then textures are copied, unzipped and used locally
        #
        # useMapVsPng = False uses png
        # useMapVsPng = True uses map
        '''
        files = cmds.ls(type='file')
        for fil in files:
            texture = cmds.getAttr(fil+'.fileTextureName')
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
                    cmds.setAttr(fil+'.fileTextureName',newTexture.replace('//','/'),type='string')
            '''        '''

            if 'tex.alphanim.lan' in texture:
                print 'changing', texture, 'to ' ,newTexture.replace('//','/')
                cmds.setAttr(fil+'.fileTextureName',newTexture.replace('//','/'),type='string')
        return 
        
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
    
    def convert_zip_to_map(self, file, destination_folder):
        if os.path.exists(destination_folder):
            call("\"C:\\Program Files\\7-Zip\\7z.exe\" x \""+file+"\" -o\""+destination_folder+"\"")
            print ("\"C:\\Program Files\\7-Zip\\7z.exe\" x \""+file+"\" -o\""+destination_folder+"\"")
            return True
        return False

    # Auto Create
    def cllRLAutoCreate(self, render2D = 1 , PFX = 1 ):
    
        print ('=================================================================')
        print '====================!!!Start AutoRenderLayer!!!===================='
    
        
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # clean unknown nodes
        print '====================!!!clean unknown nodes!!!===================='
        self.checkDonotNodesClean()
        # File Node Config
        print '====================!!!cllRLFileNodeConfig!!!===================='
        self.cllRLFileNodeConfig()
        # VisTT
        print '====================!!!cllRLVisConfig!!!===================='
        self.cllRLVisConfig()
        # renderpass Create
        print '====================!!!cllRLRenderPass!!!===================='
        self.cllRLRenderPass()
        # common Setting
        print '====================!!!cllRLCommonConfig!!!===================='
        self.cllRLCommonConfig()
        # mr Setting
        print '====================!!!mentalRayProductionLevel!!!===================='
        self.mentalRayProductionLevel()
        
        
        # Step 1：RGB,BW,SPEC,RIM
        
        # RGB
        print '====================!!!cllRLRGBCreate!!!===================='
        self.cllRLRGBCreate()
        # BW
        print '====================!!!cllRLBWCreate!!!===================='
        self.cllRLBWCreate()
        # SPEC
        print '====================!!!cllRLSPECCreate!!!===================='
        self.cllRLSPECCreate()        
        # RIM
        print '====================!!!cllRLRIMLIGHTCreate!!!===================='
        self.cllRLRIMLIGHTCreate()

        # smoothSet
        print '====================!!!cllRLDoSmooth!!!===================='
        self.cllRLDoSmooth()
        # Back To MasterLayer
        print '====================!!!mel.eval!!!===================='
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        print '====================!!!mel.eval!!!===================='
        #STANDALONE#mel.eval(r'renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0";')
        cmds.setAttr("defaultRenderLayer.renderable", 0)

        # cmds.setAttr
        # common Setting
        
                
        print '====================!!!cllRLCommonConfig!!!===================='
        self.cllRLCommonConfig()
        # save
        print '====================!!!cllRLSave!!!===================='
        self.cllRLSave('auto_01')
        
        
        
        
        # Step 2：Light,ZDepth,BG_RGB
        if cmds.ls('RGB'):    cmds.delete('RGB')
        if cmds.ls('BW'):    cmds.delete('BW')
        if cmds.ls('SPEC'):    cmds.delete('SPEC')
        if cmds.ls('RIMLIGHT'):    cmds.delete('RIMLIGHT')
        
        
        
        # Light
        self.cllRLLIGHTCreate('CHR')
        self.cllRLLIGHTCreate('SET')
        # ZDepth
        self.cllRLZDEPTHCreate()
        # BG_RGB
        self.cllRLBGRGBCreate()
        
        
        # smoothSet
        self.cllRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        #STANDALONE#mel.eval(r'renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0";')
        cmds.setAttr("defaultRenderLayer.renderable", 0)
        
        # common Setting
        self.cllRLCommonConfig()
        # save
        self.cllRLSave('auto_02')
        
        
        
        if cmds.ls('LIGHT_CHR'):    cmds.delete('LIGHT_CHR')
        if cmds.ls('LIGHT_SET'):    cmds.delete('LIGHT_SET')
        if cmds.ls('ZDEPTH'):    cmds.delete('ZDEPTH')
        if cmds.ls('BG_RGB'):    cmds.delete('BG_RGB')        
        # RENDER_2D
        self.cllRLSpeficCreate('RENDER_2D', '2D')
        # PFX
        self.cllRLSpeficCreate('PFX', 'PFX')
        
        print '=======================!!!All Done!!!======================='
        print ('===========================================================')
        return 1
    
    
    def setCurrentCamera(self):
        shotN = None
        mainCamera = 'perspShape'
        for el in os.path.basename(cmds.file(q=True, sn=True)).split('_'):
            if el.startswith('sh'):
                shotN = el.replace('sh','')
                break
        for cam in cmds.ls(type='camera'):
            if shotN in cam:
                mainCamera = cam
                break
        if mainCamera != 'perspShape':            #which means i found a valid camera matching the shot!!
            for cam in cmds.ls(type='camera'):
                val = False
                if cam==mainCamera: val = True
                cmds.setAttr(cam+'.renderable', val)
        os.environ['AKCAMERA']=str(cmds.listRelatives(mainCamera,p=True)[0])
        return mainCamera

        # Create Single Render Layer
    def cllRLSpeficCreate(self, renderLayer , mode=''):
        print '====================!!!Start cllRLSpeficCreate!!!===================='
        print 'Working...'

        pfxOk = None
        render2dOk = None
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Clean Unknwon Nodes
        self.checkDonotNodesClean()
        # File Node Config
        self.cllRLFileNodeConfig()
        # renderpass Create
        self.cllRLRenderPass()
        # common Setting
        self.cllRLCommonConfig()
        # mr Setting
        self.mentalRayProductionLevel()
        # 
        # RGB
        if renderLayer == 'RGB':
            try:
                cmds.delete('RGB')
            except:
                pass
            self.cllRLRGBCreate()
        # BW
        if renderLayer == 'BW':
            try:
                cmds.delete('BW')
            except:
                pass
            self.cllRLBWCreate()
        # SPE
        if renderLayer == 'SPEC':
            try:
                cmds.delete('SPEC')
            except:
                pass
            self.cllRLSPECCreate()
        # RIM
        if renderLayer == 'RIMLIGHT':
            try:
                cmds.delete('RIMLIGHT')
            except:
                pass
            self.cllRLRIMLIGHTCreate()
        # Light
        if renderLayer == 'LIGHT':
            try:
                cmds.delete('LIGHT_CHR')
            except:
                pass
            self.cllRLLIGHTCreate('CHR')
            try:
                cmds.delete('LIGHT_SET')
            except:
                pass
            self.cllRLLIGHTCreate('SET')
        # ZDepth
        if renderLayer == 'ZDEPTH':
            try:
                cmds.delete('ZDEPTH')
            except:
                pass
            self.cllRLZDEPTHCreate()

        # BG_RGB
        if renderLayer == 'BG_RGB':
            try:
                cmds.delete('BG_RGB')
            except:
                pass
            self.cllRLBGRGBCreate()
        # RENDER_2D
        if renderLayer == 'RENDER_2D':
            try:
                cmds.delete('RENDER_2D')
            except:
                pass
            #sk_checkCommon.sk_checkTools().checkCleanRenderLayers()
            render2dOk = self.cllRLBGRENDER2DCreate()
        # PFX
        if renderLayer == 'PFX':
            try:
                cmds.delete('PFX')
            except:
                pass
            #sk_checkCommon.sk_checkTools().checkCleanRenderLayers()
            try:
                cmds.delete('RENDER_2D')
            except:
                pass
                
            objs = self.smoothSetGetObjects(2)    
            for obj in objs:
                if 'CALI' in obj or 'cali' in obj:
                    cmds.polySmooth(obj,  mth=0, dv=2, bnr=1, c=1, kb=1, ksb=1, khe=0, kt=1, kmb=1, suv=1, peh=0, sl=1, dpe=1, ps=0.1, ro=1, ch=1)

            pfxOk = self.cllRLBGPFXCreate()
        # smoothSet
        self.cllRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # UnRender MasterLayer
        #STANDALONE#mel.eval(r'renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0";')
        cmds.setAttr("defaultRenderLayer.renderable", 0)

        # common Setting
        self.cllRLCommonConfig()
        
        if mode:
            print 'renderLayer,  pfxOk', renderLayer,  pfxOk
            if (renderLayer == 'PFX' and pfxOk==True) or (renderLayer == 'RENDER_2D' and render2dOk==True):
                self.cllRLSave(mode)
        
        print '====================!!!Done cllRLSpeficCreate!!!===================='
        print '\n'
       
    # getShotInfo
    def checkShotInfo(self):
        temp = (cmds.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
        else:
            cmds.warning('========================[File Name Wrong]========================')
        return info    
    
    # delete unknown nodes
    def checkDonotNodesClean(self):
        # 
        unknownNodes = cmds.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                cmds.lockNode(node, l=0)
                cmds.delete(node)
        # 
        turtleNodes = cmds.ls(type='ilrBakeLayer')
        for node in turtleNodes:
            cmds.lockNode(node, l=0)
            cmds.delete(node)
       
    # Save File
    def cllRLSave(self, mode):
        print '====================!!!Start cllRLSave!!!===================='
        print 'Working...'
        shotInfo = self.checkShotInfo()
        #pathLocal = ('C:/Users/svilla/Documents/maya/projects/default/scenes/renderLayerFile/' + shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/')
        #pathLocal = ('C:/temp/renderLayerFile/'+os.path.basename(self.sceneName)+'/'+ shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/')
        #pathLocal = 'Z:/CALI_Lighting_MayaPrj/CALI_LO_'+shotInfo[1]+'/scenes/AK_LIGHTING/sh'+shotInfo[2].replace('sh','')+'/publish/renderLayers/'
        
        pathLocal = self.pathLocalBase+'renderLayers/'
        
        cmds.sysFile(pathLocal, makeDir=True)
        #fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        fileName = pathLocal + os.path.basename(self.sceneName).replace('.ma','')
        if mode == 'auto_01':
            fileType = '_l4AllLayer_c001.ma'
        if mode == 'auto_02':
            fileType = '_l3AllLayer_c001.ma'
        if mode == '2D':
            fileType = '_l1Render2D_c001.ma'
        if mode == 'PFX':
            fileType = '_l1PFX_c001.ma'
        fileName = fileName + fileType
        cmds.file(rename=fileName)
        cmds.file(save=1)
        print '====================!!!Done cllRLSave!!!===================='
        print '\n'
        
    # Import Camera
    def cllRLCamImport(self):
        camGrp = cmds.ls('CAM_GRP')
        if camGrp:
            cmds.delete(camGrp)
        
        
    # Create renderPass
    def cllRLRenderPass(self):
        print '====================!!!Start cllRLRenderPass!!!===================='
        print 'Working...'
        
        shotInfo = self.checkShotInfo()
        prefixName = ''    #shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        # idPass1
        ex_idPass1 = cmds.ls((prefixName + 'idPass1'), type='renderPass')
        if ex_idPass1:
            renderPass = (prefixName + 'idPass1')
        else:
            renderPass = cmds.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cllRLRenderPassConfig(renderPass, configType)
        cmds.rename(renderPass, (prefixName + 'idPass1'))
        
        # idPass2
        ex_idPass2 = cmds.ls((prefixName + 'idPass2'), type='renderPass')
        if ex_idPass2:
            renderPass = (prefixName + 'idPass2')
        else:
            renderPass = cmds.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cllRLRenderPassConfig(renderPass, configType)
        cmds.rename(renderPass, (prefixName + 'idPass2'))
        
        # idPass3
        ex_idPass3 = cmds.ls((prefixName + 'idPass3'), type='renderPass')
        if ex_idPass3:
            renderPass = (prefixName + 'idPass3')
        else:
            renderPass = cmds.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cllRLRenderPassConfig(renderPass, configType)
        cmds.rename(renderPass, (prefixName + 'idPass3'))
        
        # idPassChr
        ex_idPassChr = cmds.ls((prefixName + 'idPassChr'), type='renderPass')
        if ex_idPassChr:
            renderPass = (prefixName + 'idPassChr')
        else:
            renderPass = cmds.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cllRLRenderPassConfig(renderPass, configType)
        cmds.rename(renderPass, (prefixName + 'idPassChr'))
        
        # idPassChrMain
        ex_idPassChrMain = cmds.ls((prefixName + 'idPassChrMain'), type='renderPass')
        if ex_idPassChrMain:
            renderPass = (prefixName + 'idPassChrMain')
        else:
            renderPass = cmds.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 4, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cllRLRenderPassConfig(renderPass, configType)
        cmds.rename(renderPass, (prefixName + 'idPassChrMain'))
        
        # renderpass
        self.renderpassConnect()
        
        print '====================!!!Done cllRLRenderPass!!!===================='
        print '\n'
        
    # renderpass
    def cllRLRenderPassConfig(self, renderPass, configType):
        # renderable
        cmds.setAttr((renderPass + '.renderable'), int(configType[0]))
        # nodeType
        cmds.setRenderPassType(renderPass, type=str(configType[1]))
        # channels
        cmds.setAttr((renderPass + '.numChannels'), int(configType[2]))
        # frameType
        cmds.setAttr((renderPass + '.frameBufferType'), int(configType[3]))
        # colorProfile
        cmds.setAttr((renderPass + '.colorProfile'), int(configType[4]))
        # filtering
        cmds.setAttr((renderPass + '.filtering'), int(configType[5]))
        # passGroupName
        cmds.setAttr((renderPass + '.passGroupName'), str(configType[6]), type='string')
        # holdout
        cmds.setAttr((renderPass + '.holdout'), int(configType[7]))
        # transparency
        cmds.setAttr((renderPass + '.useTransparency'), int(configType[8]))
        # reflectHidden
        cmds.setAttr((renderPass + '.reflectHidden'), int(configType[9]))
        # refractHidden
        cmds.setAttr((renderPass + '.refractHidden'), int(configType[10]))
        # hiddenReflect
        cmds.setAttr((renderPass + '.hiddenReflect'), int(configType[11]))
        # hiddenRefract
        cmds.setAttr((renderPass + '.hiddenRefract'), int(configType[12]))
        # transparentAttenuation
        cmds.setAttr((renderPass + '.transparentAttenuation'), int(configType[13]))
        # minReflectionLevel
        cmds.setAttr((renderPass + '.minReflectionLevel'), int(configType[14]))
        # maxReflectionLevel
        cmds.setAttr((renderPass + '.maxReflectionLevel'), int(configType[15]))
        # minRefractionLevel
        cmds.setAttr((renderPass + '.minRefractionLevel'), int(configType[16]))
        # maxRefractionLevel
        cmds.setAttr((renderPass + '.maxRefractionLevel'), int(configType[17]))
    
    # idpass
    def renderpassConnect(self):
        colorBufferNods = cmds.ls(type='writeToColorBuffer')
        
        shotInfo = self.checkShotInfo()
        prefixName = ''    #shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        for node in colorBufferNods:
            # 
            # colorID
            if '_ColorID' in node and '_ColorID2' not in node and '_ColorID3' not in node:
                # 
                lastNode = cmds.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    cmds.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                cmds.connectAttr((prefixName + "idPass1.message"), (node + '.renderPass'))
            # colorID2
            if '_ColorID2' in node :
                # 
                lastNode = cmds.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    cmds.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                cmds.connectAttr((prefixName + "idPass2.message"), (node + '.renderPass'))
            # colorID3
            if '_ColorID3' in node :
                # 
                lastNode = cmds.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    cmds.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                cmds.connectAttr((prefixName + "idPass3.message"), (node + '.renderPass'))
            # colorID_CHR
            if '_ColorID_CHR' in node:
                # 
                lastNode = cmds.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    cmds.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                cmds.connectAttr((prefixName + "idPassChr.message"), (node + '.renderPass'))
            if '_ColorID_ChrMain' in node:
                # 
                lastNode = cmds.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    cmds.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                cmds.connectAttr((prefixName + "idPassChrMain.message"), (node + '.renderPass'))
    
    # texture file
    # tga filter off;map minimap and 3 modify
    def cllRLFileNodeConfig(self):
        print '====================!!!Start cllRLFileNodeConfig!!!===================='
        print 'Working...'
        fileNodes = cmds.ls(type='file')
        num = 1
        for node in fileNodes:
            path = cmds.getAttr(node + '.fileTextureName')
            format = path.split('.')[-1]
            # 
            format = format.lower()
            if format == 'tga':
                cmds.setAttr((node + '.filterType'), 0)
            #
            #    Switch to .map is done at render time!!!
            #
            #if format == 'png':
            #    path = path.replace('png','map')
            #    cmds.setAttr((node + '.fileTextureName'),path,type = 'string')
            if format == 'map':
                cmds.setAttr((node + '.filterType'), 1)
                cmds.setAttr((node + '.miOverrideConvertToOptim'), 1)
                cmds.setAttr((node + '.miUseEllipticalFilter'), 1)
                #mel.eval('enableAutoConvertForElliptical ' + node)
                #cmds.setAttr((node + '.miOverrideConvertToOptim'), 0)
                cmd = "setAttr \\\"" + node +".miConvertToOptim\\\"" + "  0";
                fullCmd = "evalDeferred -lowestPriority \"" + cmd + "\""
                mel.eval(fullCmd)
                #cmds.evalDeferred('cmds.setAttr((node + \".miConvertToOptim\"), 0)',lowestPriority=1)
                #cmds.setAttr((node + '.miConvertToOptim'), 0)
                cmds.setAttr((node + '.miEllipticalMaxMinor'), 8)
                num += 1
        checkType = 'File Noeds'
        if num == len(fileNodes):  
            print '====================!!!Done cllRLFileNodeConfig!!!===================='
            print '\n'
        else:
            print '====================!!!Done cllRLFileNodeConfig!!!===================='
            print '\n'

    # 
    def cllRLObjectsTList(self, objType=1, objs=[]):
        if self.wrongRef:
            return self.cllRLObjectsTListWrongRef(objType, objs)
        # root
        CHR_GRP_Grps = None
        if cmds.objExists('CHR_GRP'):
            CHR_GRP_Grps = cmds.listRelatives('CHR_GRP',c=1)
            
        PRP_GRP_Grps = None            
        if cmds.objExists('PRP_GRP'):
            PRP_GRP_Grps = cmds.listRelatives('PRP_GRP',c=1)
            
        SET_GRP_Grps = None            
        if cmds.objExists('SET_GRP'):
            SET_GRP_Grps = cmds.listRelatives('SET_GRP',c=1)
            
        rootGrps =  []
        if CHR_GRP_Grps:
            rootGrps += CHR_GRP_Grps 
        if PRP_GRP_Grps:
            rootGrps += PRP_GRP_Grps 
        if SET_GRP_Grps:
            rootGrps += SET_GRP_Grps 
            
            
            
            
                
        refCHR = []
        refPROP = []
        refSET = []
        refENV = []
        refSKY = []
        refCalimero = []
        refVisTT = []
        for grp in rootGrps:
            # ref
            isRef = cmds.referenceQuery(grp, isNodeReferenced=True)
            if isRef:
                # refPath
                refPath = cmds.referenceQuery(grp, filename=True)
                print 'refPath',refPath
                # 
                if '/CHARACTERS/' in refPath or '/characters/' in refPath:
                    refCHR.append(grp)
                    # Calimero
                    if 'cali' in refPath or 'CALI' in refPath:
                        refCalimero.append(grp)
                    if 'cali' in refPath or 'pris' in refPath or 'vale' in refPath or 'pier' in refPath or 'CALI' in refPath or 'PRIS' in refPath or 'VALE' in refPath or 'PIER' in refPath:
                        refVisTT.append(grp)
                # 
                if '/PROPS/' in refPath or '/props/' in refPath:
                    refPROP.append(grp)
                # 
                if '/SETS/' in refPath or '/sets/' in refPath:                ##### or 'hatchplacel' in refPath or 'hatchstreetc' in refPath:    #STE
                    # Set
                    setKeys = ['_Int', '_int', '_Ext', '_ext']
                    configNum = 0
                    for key in setKeys:
                        if key in refPath:
                            refSET.append(grp)
                        else:
                            configNum += 1
                    # Env
                    if configNum == 4:
                        refENV.append(grp)
        result = []
        result.append(refCHR)
        result.append(refPROP)
        result.append(refSET)
        result.append(refENV)
        result.append(refSKY)
        result.append(refCalimero)
        result.append(refVisTT)
        return result
        
    def cllRLObjectsTListWrongRef(self, objType=1, objs=[]):
        # root
        
        CHR_GRP_Grps = None
        if cmds.objExists('CHR_GRP'):
            CHR_GRP_Grps = cmds.listRelatives('CHR_GRP',c=1)
            
        PRP_GRP_Grps = None            
        if cmds.objExists('PRP_GRP'):
            PRP_GRP_Grps = cmds.listRelatives('PRP_GRP',c=1)
            
        SET_GRP_Grps = None            
        if cmds.objExists('SET_GRP'):
            SET_GRP_Grps = cmds.listRelatives('SET_GRP',c=1)        
        
        
        
        
        
        rootGrps =  []
        if CHR_GRP_Grps:
            rootGrps += CHR_GRP_Grps 
        if PRP_GRP_Grps:
            rootGrps += PRP_GRP_Grps 
        if SET_GRP_Grps:
            rootGrps += SET_GRP_Grps 
            
            
            
            
                
        refCHR = []
        refPROP = []
        refSET = []
        refENV = []
        refSKY = []
        refCalimero = []
        for grp in rootGrps:
            # ref
            isRef = cmds.referenceQuery(grp, isNodeReferenced=True)
            if isRef:
                # refPath
                refPath = cmds.referenceQuery(grp, filename=True)
                # 
                #if '/CHARACTERS/' in refPath or '/characters/' in refPath:
                if self.getRecursParent(grp)=='CHR_GRP':
                    refCHR.append(grp)
                    # Calimero
                    if 'cali' in refPath or 'CALI' in refPath:
                        refCalimero.append(grp)
                    if 'cali' in refPath or 'pris' in refPath or 'vale' in refPath or 'pier' in refPath or 'CALI' in refPath or 'PRIS' in refPath or 'VALE' in refPath or 'PIER' in refPath:
                        refVisTT.append(grp)
                # 
                #if '/PROPS/' in refPath or '/props/' in refPath:
                if self.getRecursParent(grp)=='PRP_GRP':
                    refPROP.append(grp)
                # 
                #if '/SETS/' in refPath or '/sets/' in refPath:                ##### or 'hatchplacel' in refPath or 'hatchstreetc' in refPath:    #STE
                if self.getRecursParent(grp)=='SET_GRP':
                    # Set
                    setKeys = ['_Int', '_int', '_Ext', '_ext']
                    configNum = 0
                    for key in setKeys:
                        if key in refPath:
                            refSET.append(grp)
                        else:
                            configNum += 1
                    # Env
                    if configNum == 4:
                        refENV.append(grp)
        result = []
        result.append(refCHR)
        result.append(refPROP)
        result.append(refSET)
        result.append(refENV)
        result.append(refSKY)
        result.append(refCalimero)
        return result        


    def getRecursParent(self, obj):
        par = cmds.listRelatives(obj, p=True)
        if par:
            return self.getRecursParent(par[0])
        return obj        
    # 
    def cllRLCommonConfig(self):
        print '====================!!!Start cllRLCommonConfig!!!===================='
        print 'Working...'
        
        # Camera
        #from idmt.maya.py_common import sk_hbExceptCam
        #reload(sk_hbExceptCam)
        #sk_hbExceptCam.sk_hbExceptCam().camServerReference()   
        
        
        # camera renderer
        # taking care of setting proper renderable camera already, in setCurrentCamera!!
        '''
        cameras = cmds.ls(type = 'camera')
        renderCam = 'CAM:' + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_bkShape'
        if cmds.ls(renderCam):
            for cam in cameras:
                if cam != renderCam:
                    cmds.setAttr((cam + '.renderable'),0)
                else:
                    cmds.setAttr((cam + '.renderable'),1)
        else:
            for cam in cameras:
                if 'shShape' not in cam:
                    cmds.setAttr((cam + '.renderable'),0)
                else:
                    cmds.setAttr((cam + '.renderable'),1)        
        '''
        
        # 
        #STANDALONE#mel.eval('unifiedRenderGlobalsWindow')
        
        # 
        
        #cmds.setAttr('defaultRenderGlobals.imageFilePrefix', ('M:/CAL_RSYNC/CAL_RENDER/CAL_RENDER_EP'+self.episode+'/sh'+self.shot+'/<RenderLayer>/<RenderPass>/CAL_'+self.episode+'_sh'+self.shot+'_<RenderPass>'), type='string')                            ##'<Layer>/<Scene>_<Layer>', type='string')
        ##cmds.setAttr('defaultRenderGlobals.imageFilePrefix', (r'//VELA/vela/CAL_DB/CAL_RSYNC/CAL_RENDER'+'/CAL_RENDER_EP'+self.episode+'/sh'+self.shot+'/<RenderLayer>/<RenderPass>/CAL_'+self.episode+'_sh'+self.shot+'_<RenderPass>'), type='string')                            ##'<Layer>/<Scene>_<Layer>', type='string')
        
        #####
        #
        #    output directory not found (\vela\vela\....    
        #
        #cmds.setAttr('defaultRenderGlobals.imageFilePrefix', ("\\\\vela\\vela\\CAL_DB\\CAL_RSYNC\\CAL_RENDER\\CAL_RENDER_EP"+self.episode+'/sh'+self.shot+'/<RenderLayer>/<RenderPass>/CAL_'+self.episode+'_sh'+self.shot+'_<RenderPass>'), type='string')                            ##'<Layer>/<Scene>_<Layer>', type='string')

        #####
        #
        #    output directory not found (\vela\vela\....    
        #    .. -proj "\\vela\vela\prod\CALIMERO\CALI_Lighting_MayaPrj\CALI_LO_ep106" -r mr -rt 2  -rd "M:/CAL_DB/CAL_RSYNC/CAL_RENDER/CAL_RENDER_EP106/images/sh072" -im "<Layer>/<RenderPass>/CAL_106_sh072_<RenderPass>" ....
        #cmds.setAttr('defaultRenderGlobals.imageFilePrefix', ("\\\\\\\\vela\\vela\\CAL_DB\\CAL_RSYNC\\CAL_RENDER\\CAL_RENDER_EP"+self.episode+'/sh'+self.shot+'/<RenderLayer>/<RenderPass>/CAL_'+self.episode+'_sh'+self.shot+'_<RenderPass>'), type='string')                            ##'<Layer>/<Scene>_<Layer>', type='string')
        
        #####
        #
        #    it works but you have to set proj in '//VELA/vela/CAL_DB/CAL_RSYNC/CAL_RENDER/CAL_RENDER_EPXXX'
        #        
        cmds.setAttr('defaultRenderGlobals.imageFilePrefix', ('998-'+self.shot+'/<RenderLayer>/<RenderPass>/CAL_'+self.episode+'_'+self.shot+'_LAYERS_<RenderPass>'), type='string')                            ##'<Layer>/<Scene>_<Layer>', type='string')
        cmds.setAttr('defaultResolution.width', 1920)
        cmds.setAttr('defaultResolution.height', 1080)
        cmds.setAttr('defaultResolution.deviceAspectRatio', 1.777)
        cmds.setAttr('defaultResolution.pixelAspect', 1.00)
        cmds.evalDeferred('cmds.setAttr((\'defaultResolution.pixelAspect\'),1)',lowestPriority=1)
        cmds.setAttr('defaultResolution.dotsPerInch', 72)
        cmds.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)  
        
        # FPS
        cmds.currentUnit(time='pal')
        '''
        cmds.playbackOptions(q=True, ast=True)
        cmds.playbackOptions(q=True, aet=True)

        cmds.playbackOptions(q=True, min=True)
        cmds.playbackOptions(q=True, max=True)
        '''
        
        startFrame = cmds.playbackOptions(q=True, ast=True)
        endFrame = cmds.playbackOptions(q=True, aet=True)
        
        #startFrame = 0
        #endFrame = 100
        frameIns = cmds.ls('*.Frame_In')
        if frameIns:
            startFrame = cmds.getAttr(frameIns[0])
        if len(frameIns)>1:
            print 'WARNING::::there are many Frame_In attributes..maybe more then one camera????',frameIns
        frameOuts = cmds.ls('*.Frame_Out')
        if frameOuts:
            endFrame = cmds.getAttr(frameOuts[0])
        if len(frameOuts)>1:
            print 'WARNING::::there are many Frame_Out attributes..maybe more then one camera????',frameOuts
                
        
        

        
        cmds.setAttr('defaultRenderGlobals.startFrame', startFrame)  
        cmds.setAttr('defaultRenderGlobals.endFrame', endFrame)  
        self.setCurrentCamera()




        os.environ['AKSTARTFRAME']=str(startFrame)
        os.environ['AKENDFRAME']=str(endFrame)
        if os.environ.has_key('AK_TEMPFILE'):
            print 'writing os.environ[AK_TEMPFILE]',os.environ['AK_TEMPFILE']
            f = open(os.environ['AK_TEMPFILE'],'w')
            f.write(os.environ['AKCAMERA']+','+os.environ['AKSTARTFRAME']+','+os.environ['AKENDFRAME'])
            f.close()
            print 'writing os.environ[AK_TEMPFILE] DONE',os.environ['AK_TEMPFILE']

        
        
        cmds.setAttr('defaultRenderGlobals.imageFormat', 7) 
        cmds.setAttr('defaultRenderGlobals.outFormatControl', 0)
        cmds.setAttr('defaultRenderGlobals.animation', 1)
        cmds.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
        cmds.setAttr('defaultRenderGlobals.extensionPadding', 3)
        cmds.setAttr('defaultRenderGlobals.periodInExt ', 1)

        
        #STANDALONE#cmds.optionMenuGrp('extMenu', e=1, select=1)
        #STANDALONE#mel.eval('changeMayaSoftwareFileNameFormat;')
        #STANDALONE#cmds.optionMenuGrp('extMenu', e=1, select=3)
        #STANDALONE#mel.eval('changeMayaSoftwareFileNameFormat;')
        #STANDALONE#cmds.setAttr('defaultRenderGlobals.enableDefaultLight',0)

        # mel.eval("prefWndUnitsChanged \"time\";")

        print '====================!!!Done cllRLCommonConfig!!!===================='
        print '\n'
        
    # mr     
    def mentalRayProductionLevel(self):
        print '====================!!!Start mentalRayProductionLevel!!!===================='
        print 'Working...'
        
        cmds.setAttr('defaultRenderGlobals.imageFormat', 7)   
        try:
            mel.eval('loadPlugin "Mayatomr"')
        except:
            pass
        cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
        # UI
        mel.eval('mentalrayUI ""')
        # production_preset
        #mel.eval('nodePreset -load "miDefaultOptions" "production_mi"')
        
        
        cmds.setAttr( "defaultResolution.width", 1920)
        cmds.setAttr( "defaultResolution.height", 1080)
        
        cmds.setAttr("miDefaultOptions.minSamples",0)
        cmds.setAttr("miDefaultOptions.maxSamples",2)
        cmds.setAttr("miDefaultOptions.contrastR",0.1)
        cmds.setAttr("miDefaultOptions.contrastG",0.1)
        cmds.setAttr("miDefaultOptions.contrastB",0.1)
        cmds.setAttr("miDefaultOptions.contrastA",0.1)
        cmds.setAttr("miDefaultOptions.filter",2)
        cmds.setAttr("miDefaultOptions.filterWidth",1)
        cmds.setAttr("miDefaultOptions.filterHeight",1)
        cmds.setAttr("miDefaultOptions.jitter",1)
        cmds.setAttr("miDefaultOptions.rayTracing",1)
        cmds.setAttr("miDefaultOptions.maxReflectionRays",0)
        cmds.setAttr("miDefaultOptions.maxRefractionRays",0)
        cmds.setAttr("miDefaultOptions.maxRayDepth",0)
        cmds.setAttr("miDefaultOptions.maxShadowRayDepth",2)
        cmds.setAttr("miDefaultOptions.maxReflectionBlur",1)
        cmds.setAttr("miDefaultOptions.maxRefractionBlur",1)
        
        # image format
        if cmds.optionMenuGrp('imageMenuMentalRay', exists=1):
            cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
            mel.eval('changeMentalRayImageFormat')
        
        print '====================!!!Done mentalRayProductionLevel!!!===================='
        print '\n'

    # SG
    def cllRLSGNodesGet(self):
        SGNodes = cmds.ls(type='shadingEngine')
        SGNodes.remove('initialParticleSE')
        SGNodes.remove('initialShadingGroup')
        # SG
        refSGCHR = []
        refSGPROP = []
        refSGSET = []
        refSGENV = []
        refSGSKY = []
        refSGCalimero = []
        # 
        # 
        for SGNode in SGNodes:
            if '_cam_' not in SGNode and '_CAM_' not in SGNode and 'camera' not in SGNode:
                listMeshTransform = cmds.listConnections(SGNode, type='mesh')
                if listMeshTransform:
                    # 
                    # 
                    # refPath
                    if cmds.referenceQuery(listMeshTransform[0], inr=True): 
                    
                        refPath = cmds.referenceQuery(listMeshTransform[0], filename=True)
                        # 
                        if '/CHARACTERS/' in refPath or '/characters/' in refPath:
                            refSGCHR.append(SGNode)
                            # Calimero
                            # if '/CHR_CALI/' in refPath or '/chr_cali/' in refPath:
                            if 'CALI' in refPath or 'cali' in refPath :
                                refSGCalimero.append(SGNode)
                        # 
                        if '/PROPS/' in refPath or '/props/' in refPath:
                            refSGPROP.append(SGNode)
                        # 
                        if '/SETS/' in refPath or '/sets/' in refPath:
                            # Set
                            setKeys = ['_Int', '_int', '_Ext', '_ext']
                            configNum = 0
                            for key in setKeys:
                                if key in refPath:
                                    refSGSET.append(SGNode)
                                else:
                                    configNum += 1
                            # Env
                            if configNum == 4:
                                refSGENV.append(SGNode)

        result = []
        result.append(refSGCHR)
        result.append(refSGPROP)
        result.append(refSGSET)
        result.append(refSGENV)
        result.append(refSGSKY)
        result.append(refSGCalimero)
        return result
    
    # smoothSet
    def cllRLDoSmooth(self, layerType=1):
        self.smoothSetDoSmooth()
    
    def smoothSetGetObjects(self,level):
        tempSet = cmds.ls(type='objectSet')
        objsSet = []
        objsSmooth = [] 
        for temp in tempSet:
            if ('smooth_' + str(level)) in temp or ('smooth' + str(level)) in temp:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                meshes = cmds.sets(objSet, q=1)
                if meshes:
                    for mesh in meshes:
                        objsSmooth.append(cmds.ls((mesh), l=1)[0])
        return objsSmooth
        
    # smoothSet smooth
    def smoothSetDoSmooth(self):
        topNodes = cmds.ls(assemblies=True)
        cmds.displaySmoothness(topNodes, polygonObject=3)
    


                # smooth 0
        objs = self.smoothSetGetObjects(0)
        #print 'self.smoothSetGetObjects(0)',objs
        if objs:
            for obj in objs:
                #print '\tobj',obj
                #print '\tcmds.listRelatives(obj,s=1)',cmds.listRelatives(obj,s=1,f=True)
                try:
                    self.unlockAttribute(cmds.listRelatives(obj,s=1,f=True)[0])
                except:
                    print obj
                try:
                    cmds.setAttr((cmds.listRelatives(obj,s=1,f=True)[0]+'.displaySmoothMesh'),2)
                except:
                    pass
                try:
                    cmds.setAttr((cmds.listRelatives(obj,s=1,f=True)[0]+'.useSmoothPreviewForRender'),0)
                except:
                    pass
                try:
                    cmds.setAttr((cmds.listRelatives(obj,s=1,f=True)[0]+'.renderSmoothLevel'),0)
                except:
                    pass

                # smooth 1
        objs = self.smoothSetGetObjects(1)
        #print 'self.smoothSetGetObjects(1)',objs
        if objs:
            for obj in objs:
                self.unlockAttribute(cmds.listRelatives(obj,s=1,f=True)[0])
                try:
                    cmds.setAttr((cmds.listRelatives(obj,s=1,f=True)[0]+'.displaySmoothMesh'),2)
                except:
                    pass
                try:
                    cmds.setAttr((cmds.listRelatives(obj,s=1,f=True)[0]+'.useSmoothPreviewForRender'),0)
                except:
                    pass
                try:
                    cmds.setAttr((cmds.listRelatives(obj,s=1,f=True)[0]+'.renderSmoothLevel'),1)
                except:
                    pass

                # smooth 2
        objs = self.smoothSetGetObjects(2)
        #print 'self.smoothSetGetObjects(2)',objs
        if objs:
            #scriptEditorInfo -e -suppressWarnings true;
            for obj in objs:
                if not obj: continue
                if not cmds.listRelatives(obj,s=1,f=True): continue
                self.unlockAttribute(cmds.listRelatives(obj,s=1,f=True)[0])
                try:
                    cmds.setAttr((cmds.listRelatives(obj,s=1,f=True)[0]+'.displaySmoothMesh'),2)
                except:
                    pass
                try:
                    cmds.setAttr((cmds.listRelatives(obj,s=1,f=True)[0]+'.useSmoothPreviewForRender'),0)
                except:
                    pass
                try:
                    cmds.setAttr((cmds.listRelatives(obj,s=1,f=True)[0]+'.renderSmoothLevel'),2)    
                except:
                    pass
                    
    def unlockAttribute(self, obj):
        #getAttr -l "msh_tree_bircha_Trunck__000_Shape.displaySmoothMesh"
        try:
            cmds.setAttr(obj+'.displaySmoothMesh', l=False)
        except:
            pass
        try:
            cmds.setAttr(obj+'.useSmoothPreviewForRender', l=False)
        except:
            pass
        try:
            cmds.setAttr(obj+'.renderSmoothLevel', l=False)
        except:
            pass
        return
    # vis
    def cllRLVisConfig(self):
        print 'clRLVisConfig-------------------------------->'
        objs = self.cllRLObjectsTList()
        print 'objs',objs
        refVisTT = objs[6]
        if refVisTT:
            for asset in refVisTT:
                controlShapes = cmds.listRelatives(asset , ad=1 , type = 'nurbsCurve', f= 1)
                if controlShapes:
                    for ctrlShape in controlShapes:
                        ctrl = cmds.listRelatives(ctrlShape,p=1,type = 'transform',f=1)[0]
                        if cmds.ls(ctrl + '.twoDline_vis'):
                            
                            connections = cmds.listConnections(ctrl, s=True, d=False, c=True, p=True)
                            if connections:
                                for i in range(0, len(connections),2):
                                    if 'twoDline_vis' in connections[i] or 'twoDline_vis' in connections[i+1]:
                                        print connections[i], connections[i+1]
                                        try:
                                            cmds.disconnectAttr(connections[i+1], connections[i])
                                        except:
                                            pass
                            
                            cmds.setAttr((ctrl + '.twoDline_vis'),1)
                            
                            
                            
                            print 'setting to 1',ctrl    #CHAR_PRIS:c_Facial_CTRL_FRAME
        print 'clRLVisConfig------------ OUT --------------->'
        
        
        
        
    def setExtensionFramebuffer(self, datatype=4):    #dataatype=4 16bit, =2 8 bit, =5 32 bit
        
        cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
        mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")

        # exr
        cmds.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')        
        cmds.setAttr('defaultRenderGlobals.imageFormat', 51)
        if cmds.optionMenuGrp('imageMenuMentalRay', exists=1):
            # cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
            # mel.eval('changeMentalRayImageFormat')
            cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
            try:
                mel.eval('changeMentalRayImageFormat')
            except:
                pass

        # 8 zip
        cmds.setAttr('mentalrayGlobals.imageCompression', 4)
        cmds.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
        cmds.setAttr('miDefaultFramebuffer.datatype', datatype)

        cmds.editRenderLayerAdjustment('defaultRenderGlobals.imfPluginKey')
        cmds.setAttr('defaultRenderGlobals.imfPluginKey','exr', type="string")    
        
        
        cmds.editRenderLayerAdjustment('miDefaultOptions.finalGather')
        cmds.setAttr('miDefaultOptions.finalGather', 0)    
        
        return
        
    # RGB
    # No Lights
    def cllRLRGBCreate(self):
        print '====================!!!Start cllRLRGBCreate!!!===================='
        print 'Working...'
        shotInfo = self.checkShotInfo()
        prefixName = ''    #shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        # idPass1
                    
        # 
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 
        lights = cmds.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 
        rlObjs = refCHR + refPROP + refSET + refSKY
        
        
        # RenderLayer
        if (refCHR + refPROP + refSET):
            layerName = 'RGB'
            cmds.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(0)
            
            print 'switching msh_iris_ visibility'
            for aa in cmds.ls('*msh_iris_*_', r=True):
                if '_PRIS' in aa:
                    try:
                        print 'setting ',aa+'.visibility'
                        cmds.editRenderLayerAdjustment(aa + '.visibility')
                        cmds.setAttr(aa+'.visibility', 0)
                    except:
                        print 'ERROR:can\'t set visibility at 0',aa

            # 
            for light in lights:
                lightGrp = cmds.listRelatives(light, p=1)[0]
                cmds.editRenderLayerAdjustment(lightGrp + '.v')
                cmds.setAttr((light + '.v'), 0)
                cmds.editRenderLayerAdjustment(light + '.intensity')
                cmds.setAttr((light + '.intensity'), 0)
                
            # light_grp,hide
            lightGrps = mc.ls('*:LIGHTING')
            if lightGrps:
                for grp in lightGrps:
                    cmds.editRenderLayerAdjustment(grp + '.v')
                    cmds.setAttr((grp + '.v'), 0)
            
            # renderPass
            # idpass1
            try:
                cmds.connectAttr('RGB.renderPass', (prefixName+'idPass1.owner'))
            except:
                pass
            # 
            # 
            # self.cllRLCommonConfig()
            
            
            '''
            cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")

            # exr
            # cmds.setAttr('defaultRenderGlobals.imfPluginKey', 'exr', type='string')
            # mel.eval('updateMultiCameraBufferNamingMenu;')
            cmds.editRenderLayerAdjustment('defaultRenderGlobals.imfPluginKey')
            cmds.setAttr('defaultRenderGlobals.imfPluginKey','exr', type="string")

            #mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            cmds.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')        
            cmds.setAttr('defaultRenderGlobals.imageFormat', 51)
            
            
            if cmds.optionMenuGrp('imageMenuMentalRay', exists=1):
                # cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass

            # 16 bit compress
            cmds.setAttr('mentalrayGlobals.imageCompression', 4)
            cmds.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            cmds.setAttr('miDefaultFramebuffer.datatype', 16)

            cmds.editRenderLayerAdjustment('miDefaultOptions.finalGather')
            cmds.setAttr('miDefaultOptions.finalGather', 0)    
            cmds.optionMenuGrp('extMenu', e=1, select=3)
            '''
            self.setExtensionFramebuffer(datatype=16)
            
            print '====================!!!Done cllRLRGBCreate!!!===================='
            print '\n'
        else:
            print '====================!!!None cllRLRGBCreate!!!===================='
            print '\n'
    
    # BW
    # No Lights
    def cllRLBWCreate(self):
        print '====================!!!Start cllRLBWCreate!!!===================='
        print 'Working...'
        shotInfo = self.checkShotInfo()
        prefixName = ''    #shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        # 
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 
        lights = cmds.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 
        rlObjs = refPROP + refSET + refENV + refSKY + lights
        
        # RenderLayer
        if (refPROP + refSET + refENV + refSKY):
            layerName = 'BW'
            cmds.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(0)
            
            # 
            for light in lights:
                lightGrp = cmds.listRelatives(light, p=1)[0]
                cmds.editRenderLayerAdjustment(lightGrp + '.v')
                cmds.setAttr((light + '.v'), 0)
                cmds.editRenderLayerAdjustment(light + '.intensity')
                cmds.setAttr((light + '.intensity'), 0)
            
            # light_grp,hide
            lightGrps = mc.ls('*:LIGHTING')
            if lightGrps:
                for grp in lightGrps:
                    cmds.editRenderLayerAdjustment(grp + '.v')
                    cmds.setAttr((grp + '.v'), 0)
            
            # renderPass
            # 
            
            # 
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGPROP + refSGSET + refSGENV + refSGSKY
            
            # 
            shaderName = 'SHD_' + 'BW'
            if cmds.ls(shaderName):
                cmds.delete(shaderName)
            shaderNeed = cmds.shadingNode ('lambert', asShader=True, name=shaderName)   
            cmds.setAttr(('%s.color') % (shaderNeed), 1, 1, 1, type="double3")
            cmds.setAttr(('%s.ambientColor') % (shaderNeed), 1, 1, 1, type="double3")

            # 
            for SGNode in rlSGNodes:
                # RGB RGBA
                RGBNodeGrp = cmds.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # BW
                    needTxNode = RGBNode.replace('_RGB', '_BW')
                    # RGB/RGBA node
                    if cmds.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    cmds.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    cmds.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    cmds.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))

            # 
            # self.cllRLCommonConfig()

            ''' 
            cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")

            # exr
            cmds.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')        
            cmds.setAttr('defaultRenderGlobals.imageFormat', 51)
            if cmds.optionMenuGrp('imageMenuMentalRay', exists=1):
                # cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass

            # cmds.setAttr('defaultRenderGlobals.imfPluginKey','exr',type = 'string')
            # mel.eval('updateMultiCameraBufferNamingMenu;')
            # mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            
            # 8 zip
            cmds.setAttr('mentalrayGlobals.imageCompression', 4)
            cmds.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            cmds.setAttr('miDefaultFramebuffer.datatype', 2)

            
            
            cmds.editRenderLayerAdjustment('defaultRenderGlobals.imfPluginKey')
            cmds.setAttr('defaultRenderGlobals.imfPluginKey','exr', type="string")
            '''
            self.setExtensionFramebuffer(datatype=2)

            
            print '====================!!!Done cllRLBWCreate!!!===================='
            print '\n'
        else:
            print '====================!!!None cllRLBWCreate!!!===================='
            print '\n'


        
        
    # SPEC
    # 
    def cllRLSPECCreate(self):
        print '====================!!!Start cllRLSPECCreate!!!===================='
        print 'Working...'
        
        shotInfo = self.checkShotInfo()
        prefixName = ''    #shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        # 
        objs = self.cllRLObjectsTList()
        print 'cllRLSPECCreate',objs
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 
        lights = cmds.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 
        rlObjs = refCHR + refPROP + lights
        
        # RenderLayer
        if refCHR:
            layerName = 'SPEC'
            cmds.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(0)
            
            # 
            for light in lights:
                if 'KEY' in light:
                    cmds.editRenderLayerAdjustment(light + '.color')
                    cmds.setAttr((light + '.color'), 1, 1, 1, type='double3')
                else:
                    lightGrp = cmds.listRelatives(light, p=1)[0]
                    lightGrpP = cmds.listRelatives(lightGrp, p=1)[0]
                    cmds.editRenderLayerAdjustment(lightGrpP + '.v')
                    cmds.setAttr((lightGrpP + '.v'), 0)
                    #cmds.editRenderLayerAdjustment(lightGrpP + '.intensity')
                    #cmds.setAttr((lightGrpP + '.intensity'), 0)
                # 
                cmds.editRenderLayerAdjustment(light + '.shadowColor')
                cmds.setAttr((light + '.shadowColor'), 0, 0, 0, type='double3')
                
            # renderPass
            cmds.connectAttr('SPEC.renderPass', (prefixName+'idPassChr.owner'))
            cmds.connectAttr('SPEC.renderPass', (prefixName+'idPassChrMain.owner'))
            
            # 
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGENV
            

            # reflect
            # beauty specular
            mel.eval("renderLayerBuiltinPreset specular SPEC")
            
            
            # 
            # self.cllRLCommonConfig()

            ''' 
            cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")

            # exr
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            cmds.setAttr('defaultRenderGlobals.imageFormat', 51)
            if cmds.optionMenuGrp('imageMenuMentalRay', exists=1):
                # cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
            
            # 8 zip
            cmds.setAttr('mentalrayGlobals.imageCompression', 4)
            cmds.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            cmds.setAttr('miDefaultFramebuffer.datatype', 2)


            cmds.editRenderLayerAdjustment('defaultRenderGlobals.imfPluginKey')
            cmds.setAttr('defaultRenderGlobals.imfPluginKey','exr', type="string")
            '''
            self.setExtensionFramebuffer(datatype=2)

            
            print '====================!!!Done cllRLSPECCreate!!!===================='      
            print '\n'
        else:
            print '====================!!!None cllRLSPECCreate!!!===================='        
            print '\n'
        
    # RIMLIGHT
    def cllRLRIMLIGHTCreate(self):
        print '====================!!!Start cllRLRIMLIGHTCreate!!!===================='
        print 'Working...'

        shotInfo = self.checkShotInfo()
        prefixName = ''    #shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        # 
        objs = self.cllRLObjectsTList()
        print 'cllRLRIMLIGHTCreate',objs
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 
        lights = cmds.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 
        rlObjs = refCHR + lights
        
        # RenderLayer
        if refCHR:
            layerName = 'RIMLIGHT'
            cmds.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(0)
            # 
            for light in lights:
                # 
                #rootGrp = '|' + cmds.ls(light, l=1)[0].split('|')[1]
                if '_KEY' in light:
                    cmds.editRenderLayerAdjustment(light + '.color')
                    cmds.setAttr((light + '.color'), 1, 1, 1, type='double3')
                else:
                    lightGrp = mc.listRelatives(light ,p =1 ,type = 'transform')[0]
                    lightGrpP = mc.listRelatives(lightGrp ,p =1 ,type = 'transform')[0]
                    #cmds.editRenderLayerAdjustment(light + '.intensity')
                    #cmds.setAttr((light + '.intensity'), 0)
                    cmds.editRenderLayerAdjustment(lightGrpP + '.v')
                    cmds.setAttr((lightGrpP + '.v'), 0)
                # 
                cmds.editRenderLayerAdjustment(light + '.shadowColor')
                cmds.setAttr((light + '.shadowColor'), 0, 0, 0, type='double3')
            
            # renderPass
            
            # 
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR
            
            # 
            shaderName = 'SHD_' + 'BLACK'
            if cmds.ls(shaderName):
                cmds.delete(shaderName)
            shaderNeed = cmds.shadingNode ('lambert', asShader=True, name=shaderName)   
            cmds.setAttr(('%s.color') % (shaderNeed), 0, 0, 0, type="double3")

            # 
            for SGNode in rlSGNodes:
                # RGBA
                RGBNodeGrp = cmds.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    '''
                    #
                    listTxNodes = cmds.listConnections(RGBNode)
                    for nd in listTxNodes:
                        if "_RIM" in nd:
                            needTxNode = nd
                            break
                    '''
                    # RIMLIGHT
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_RIM')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_RIM')
                    # RGB/RGBA node
                    if cmds.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    cmds.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    cmds.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    cmds.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
                                  
            # 
            # self.cllRLCommonConfig()
            
            ''' 
            cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
                    
            # exr
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            cmds.setAttr('defaultRenderGlobals.imageFormat', 51)
            if cmds.optionMenuGrp('imageMenuMentalRay', exists=1):
                # cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
               
            # 8 zip
            cmds.setAttr('mentalrayGlobals.imageCompression', 4)
            cmds.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            cmds.setAttr('miDefaultFramebuffer.datatype', 2)

            
            cmds.editRenderLayerAdjustment('defaultRenderGlobals.imfPluginKey')
            cmds.setAttr('defaultRenderGlobals.imfPluginKey','exr', type="string")
            '''
            self.setExtensionFramebuffer(datatype=2)
            
    

            print '====================!!!Done cllRLRIMLIGHTCreate!!!===================='
            print '\n'
        else:
            print '====================!!!None cllRLRIMLIGHTCreate!!!===================='
            print '\n'
        

    # LIGHT
    # 
    # SHD_LIGHT
    def cllRLLIGHTCreate(self,type = 'CHR'):
        print '====================!!!Start cllRLLIGHTCreate!!!===================='
        print 'Working...'
        
        shotInfo = self.checkShotInfo()
        prefixName = ''    #shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]

        # 
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 
        lights = cmds.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 
        rlObjs = refCHR + refPROP + refSET + refSKY + lights
        
        # RenderLayer
        if (refCHR + refPROP + refSET + refSKY):
            if type == 'CHR':
                layerName = 'LIGHT_CHR'
                checkGrps = refSET
            if type == 'SET':
                layerName = 'LIGHT_SET'
                checkGrps = refCHR + refPROP
            cmds.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # primary
            if checkGrps:
                for grp in checkGrps:
                    meshes = mc.listRelatives(grp ,ad = 1 ,type = 'mesh')
                    if meshes:
                        for mesh in meshes ��
                            cmds.editRenderLayerAdjustment(mesh + '.primary ')
                            cmds.setAttr((mesh + '.primary '),0)
            
            # renderPass
            cmds.connectAttr('LIGHT.renderPass', (prefixName+'idPass3.owner'))
            
            self.settingPFXvisibility(0)
            
            # KEY，BRANCH，EXTRA
            for light in lights:
                # 
                #rootGrp = '|' + cmds.ls(light, l=1)[0].split('|')[1]
                #if rootGrp in refENV:
                if '_KEY' in light:
                    cmds.editRenderLayerAdjustment(light + '.color')
                    cmds.setAttr((light + '.color'), 1, 0, 0, type='double3')
                if '_BOUNCE' in light:
                    cmds.editRenderLayerAdjustment(light + '.color')
                    cmds.setAttr((light + '.color'), 0, 0, 1, type='double3')
                if '_EXTRA' in light:
                    cmds.editRenderLayerAdjustment(light + '.color')
                    cmds.setAttr((light + '.color'), 0, 1, 0, type='double3')
                if '_ONLY' in light:
                    if '_KEY' not in light and '_BOUNCE' not in light and '_EXTRA' not in light:
                        lightGrp = mc.listRelatives(light ,p =1 , type = 'transform')[0]
                        lightGrpP = mc.listRelatives(lightGrp ,p =1 , type = 'transform')[0]
                        #cmds.editRenderLayerAdjustment(light + '.intensity')
                        #cmds.setAttr((light + '.intensity'), 0)
                        cmds.editRenderLayerAdjustment(lightGrpP + '.v')
                        cmds.setAttr((lightGrpP + '.v'), 0)
                # 
                cmds.editRenderLayerAdjustment(light + '.shadowColor')
                cmds.setAttr((light + '.shadowColor'), 0, 0, 0, type='double3')

            # 
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR + refSGPROP + refSGSET + refSGSKY
            
            # 
            shaderName = 'SHD_' + 'LIGHT'
            if cmds.ls(shaderName):
                cmds.delete(shaderName)
            shaderNeed = cmds.shadingNode ('lambert', asShader=True, name=shaderName)   
            cmds.setAttr(('%s.color') % (shaderNeed), 1, 1, 1, type="double3")
            # 
            for SGNode in rlSGNodes:
                # RGB RGBA
                RGBNodeGrp = cmds.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # LIGHT
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_LIGHT')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_LIGHT')
                    # RGB/RGBA node
                    if cmds.objExists(needTxNode) and 'LIGHT' in needTxNode:
                        node = needTxNode
                    else:
                        node = shaderNeed
                    cmds.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    cmds.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    cmds.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'), f=1)
            # 
            # self.cllRLCommonConfig()
            # 
            
            '''
            cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
            
            # exr
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if cmds.optionMenuGrp('imageMenuMentalRay', exists=1):
                # cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
                
            # 16 zip
            # 
            cmds.setAttr('mentalrayGlobals.imageCompression', 4)
            cmds.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            cmds.setAttr('miDefaultFramebuffer.datatype', 16)
            '''
            self.setExtensionFramebuffer(datatype=16)
            
            
            
            print '====================!!!Done cllRLLIGHTCreate!!!===================='
            print '\n'
        else:
            print '====================!!!None cllRLLIGHTCreate!!!===================='  
            print '\n'

        
    # ZDEPTH
    # No Lights
    def cllRLZDEPTHCreate(self, distance=14000):
        print '====================!!!Start cllRLZDEPTHCreate!!!===================='
        print 'Working...'
        
        # 
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 
        lights = cmds.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 
        rlObjs = refCHR + refPROP + refSET + refENV + refSKY
        
        # RenderLayer
        if (refCHR + refPROP + refSET + refENV):
            layerName = 'ZDEPTH'
            cmds.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(0)
            
            # 
            for light in lights:
                lightGrp = cmds.listRelatives(light, p=1)[0]
                lightGrpP = cmds.listRelatives(lightGrp, p=1)[0]
                cmds.editRenderLayerAdjustment(lightGrpP + '.v')
                cmds.setAttr((lightGrpP + '.v'), 0)
                #cmds.editRenderLayerAdjustment(light + '.intensity')
                #cmds.setAttr((light + '.intensity'), 0)
                
            # light_grp,hide
            lightGrps = mc.ls('*:LIGHTING')
            if lightGrps:
                for grp in lightGrps:
                    cmds.editRenderLayerAdjustment(grp + '.v')
                    cmds.setAttr((grp + '.v'), 0)

            # renderPass
            
            # 
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR + refSGPROP + refSGSET + refSGENV + refSGSKY

            # 
            shaderName = 'SHD_' + 'ZDEPTH'
            if cmds.ls(shaderName):
                cmds.delete(shaderName)
            if cmds.ls('%s_sampleInfo' % (shaderName)):
                cmds.delete('%s_sampleInfo' % (shaderName))
            if cmds.ls('SHD_ZDEPTH_setRangeZ'):
                cmds.delete('SHD_ZDEPTH_setRangeZ')
            if cmds.ls('SHD_ZDEPTH_multDivZ'):
                cmds.delete('SHD_ZDEPTH_multDivZ')
            if cmds.ls('SHD_ZDEPTH_sampInfoZ'):
                cmds.delete('SHD_ZDEPTH_sampInfoZ')  
            if cmds.ls('SHD_Depth_SG'):
                cmds.delete('SHD_Depth_SG')  
            depthShader = cmds.shadingNode ('lambert', asShader=True, name=shaderName)
            cmds.setAttr((depthShader + '.ambientColor'),1,1,1,type = 'double3')
            setRangeNode = cmds.shadingNode ('setRange', asUtility=True, name='SHD_ZDEPTH_setRangeZ')
            cmds.setAttr((setRangeNode+'.minX'),1)
            multiplyDivideNode = cmds.shadingNode ('multiplyDivide', asUtility=True, name='SHD_ZDEPTH_multDivZ')
            cmds.setAttr((multiplyDivideNode+'.input2X'),-1)
            samplerInfoNode = cmds.shadingNode ('samplerInfo', asUtility=True, name='SHD_ZDEPTH_sampInfoZ')
            cmds.addAttr(samplerInfoNode, longName='NearClipCalimero',nn='Near Clip Calimero', attributeType='float', defaultValue=0.1)
            cmds.addAttr(samplerInfoNode, longName='FarClipCalimero',nn='Far Clip Calimero', attributeType='float', defaultValue= distance )
            depthSG = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='SHD_Depth_SG')
            cmds.connectAttr(('%s.%s') % (depthShader , 'outColor') , ('%s.%s') % (depthSG , 'surfaceShader'), f=True)
            shaderNeed = depthShader
            # 
            cmds.connectAttr(('%s.%s') % (setRangeNode , 'outValueX') , ('%s.%s') % (depthShader , 'colorR'), f=True)
            cmds.connectAttr(('%s.%s') % (setRangeNode , 'outValueX') , ('%s.%s') % (depthShader , 'colorG'), f=True)
            cmds.connectAttr(('%s.%s') % (setRangeNode , 'outValueX') , ('%s.%s') % (depthShader , 'colorB'), f=True)
            cmds.connectAttr(('%s.%s') % (samplerInfoNode , 'NearClipCalimero') , ('%s.%s') % (setRangeNode , 'oldMinX'), f=True)
            cmds.connectAttr(('%s.%s') % (samplerInfoNode , 'FarClipCalimero') , ('%s.%s') % (setRangeNode , 'oldMaxX'), f=True)
            cmds.connectAttr(('%s.%s') % (samplerInfoNode , 'pointCameraZ') , ('%s.%s') % (multiplyDivideNode , 'input1X'), f=True)
            cmds.connectAttr(('%s.%s') % (multiplyDivideNode , 'outputX') , ('%s.%s') % (setRangeNode , 'valueX'), f=True)

            # 
            for SGNode in rlSGNodes:
                # RGB RGBA
                RGBNodeGrp = cmds.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    #  ZDEPTH 
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_ZDEPTH')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_ZDEPTH')
                    # RGB/RGBA node
                    if cmds.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    cmds.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    cmds.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    cmds.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))

            # 
            # self.cllRLCommonConfig()
            
            
            # sampInfoZ
            sampleInfoZ = cmds.ls('*_sampInfoZ',type = 'samplerInfo' ) + cmds.ls('*:*_sampInfoZ',type = 'samplerInfo' )
            if sampleInfoZ:
                for sampleNode in sampleInfoZ:
                    cmds.setAttr((sampleNode + '.NearClipCalimero'),0.1)
                    cmds.setAttr((sampleNode + '.FarClipCalimero'),distance)

            ''' 
            cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
            
            # exr
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if cmds.optionMenuGrp('imageMenuMentalRay', exists=1):
                # cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
                
            # 32 zip
            # 
            cmds.setAttr('mentalrayGlobals.imageCompression', 4)
            cmds.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            cmds.setAttr('miDefaultFramebuffer.datatype', 5)
            '''
            self.setExtensionFramebuffer(datatype=5)
            
            
            print '====================!!!Done cllRLZDEPTHCreate!!!====================' 
            print '\n'
        else:
            print '====================!!!None cllRLZDEPTHCreate!!!===================='
            print '\n'
        

    # BG_RGB
    def cllRLBGRGBCreate(self):
        print '====================!!!Start cllRLBGRGBCreate!!!===================='
        print 'Working...'
        
        shotInfo = self.checkShotInfo()
        prefixName = ''    #shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        
        # 
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 
        lights = cmds.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 
        rlObjs = refENV + lights
        
        if refENV:
            
            # RenderLayer
            layerName = 'BG_RGB'
            cmds.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # 
            for light in lights:
                lightGrp = cmds.listRelatives(light, p=1)[0]
                lightGrpP = cmds.listRelatives(lightGrp, p=1)[0]
                #cmds.editRenderLayerAdjustment(light + '.intensity')
                #cmds.setAttr((light + '.intensity'), 0)
                cmds.editRenderLayerAdjustment(lightGrpP + '.v')
                cmds.setAttr((lightGrpP + '.v'), 0)
                
            # light_grp,hide
            lightGrps = mc.ls('*:LIGHTING')
            if lightGrps:
                for grp in lightGrps:
                    cmds.editRenderLayerAdjustment(grp + '.v')
                    cmds.setAttr((grp + '.v'), 0)
            
            # renderPass
            cmds.connectAttr('BG_RGB.renderPass', (prefixName+'idPass2.owner'))
            # 
            # self.cllRLCommonConfig()
            
            # 
            cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")        
    
            # exr
            '''
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if cmds.optionMenuGrp('imageMenuMentalRay', exists=1):
                # cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
    
            # 16 zip
            cmds.setAttr('mentalrayGlobals.imageCompression', 4)
            cmds.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            cmds.setAttr('miDefaultFramebuffer.datatype', 16)
            '''
            self.setExtensionFramebuffer(datatype=16)
            
            
            print '====================!!!Done cllRLBGRGBCreate!!!===================='  
            print '\n'
            return True
        print '====================!!!None cllRLBGRGBCreate!!!===================='
        print '\n'
        return False
        
        
    # RENDER2D
    def cllRLBGRENDER2DCreate(self):
        print '====================!!!Start cllRLBGRENDER2DCreate!!!===================='
        print 'Working...'
        
        # 
        # NV
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = cmds.ls(type='light')

        # CreateLight
        # 
        if cmds.ls('IDMT_2D_KeyLight'):
            cmds.delete('IDMT_2D_KeyLight')
        if cmds.ls('IDMT_2D_SideLight'):
            cmds.delete('IDMT_2D_SideLight')
        keyLight = cmds.directionalLight(name='IDMT_2D_KeyLight', rotation=(24, 36, 11), intensity=1)
        cmds.setAttr((keyLight + '.color'), 1, 1, 1, type='double3')
        cmds.setAttr((keyLight + '.useDepthMapShadows'), 0)
        cmds.setAttr((keyLight + '.useRayTraceShadows'), 1)
        cmds.setAttr((keyLight + '.lightAngle'), 0)
        cmds.setAttr((keyLight + '.shadowRays'), 1)
        cmds.setAttr((keyLight + '.rayDepthLimit'), 1)
        # 
        sideLight = cmds.directionalLight(name='IDMT_2D_SideLight', rotation=(90, 0, 0), intensity=0.5)
        cmds.setAttr((sideLight + '.color'), 1, 1, 1, type='double3')
        cmds.setAttr((sideLight + '.useDepthMapShadows'), 0)
        cmds.setAttr((sideLight + '.useRayTraceShadows'), 0)
        # 
        # lights = []
        lights.append(keyLight)
        lights.append(sideLight)

        #
        rlObjs = refENV + lights
        
        print 'refENV',refENV
        
        if refENV:
            # RenderLayer
            layerName = 'RENDER_2D'
            cmds.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            print 'createRenderLayer'
            #  ENV mesh
            for grp in refENV:
                allChildren = cmds.listRelatives(grp, ad=1, type='transform')
                # mesh
                if allChildren:
                    for child in allChildren:
                        shape = cmds.listRelatives(child, s=1)
                        if shape:
                            if cmds.nodeType(shape[0]) == 'mesh':
                                # 
                                cmds.editRenderLayerAdjustment(shape[0] + '.receiveShadows')
                                cmds.setAttr((shape[0] + '.receiveShadows'), 0)
            # renderPass
    
    
            # 
            for light in lights:
                lightGrp = cmds.listRelatives(light, p=1)[0]
                lightGrpP = cmds.listRelatives(lightGrp, p=1)[0]
                if 'IDMT_2D_' not in light:
                    cmds.editRenderLayerAdjustment(light + '.intensity')
                    cmds.setAttr((light + '.intensity'), 0)
                cmds.editRenderLayerAdjustment(lightGrpP + '.v')
                cmds.setAttr((lightGrpP + '.v'), 0)
                
            # 
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGENV
            
            # 
            shaderName = 'SHD_CALI_' + '2D'
            if cmds.ls(shaderName):
                cmds.delete(shaderName)
            shaderNeed = cmds.shadingNode ('surfaceShader', asShader=True, name=shaderName)   
            cmds.setAttr(('%s.outColor') % (shaderNeed), 0, 0, 0, type="double3")
    
            # 
            for SGNode in rlSGNodes:
                #  RGB RGBA 
                RGBNodeGrp = cmds.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # 2D
                    if '_RGBA' not in needTxNode:
                        needTxNode = RGBNode.replace('_RGB', '_2D')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_2D')
                    # RGB/RGBA node
                    if cmds.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    cmds.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    cmds.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    cmds.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
            
    
            # 
            # self.cllRLCommonConfig()
    
            ''' 
            cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
            
            # exr
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if cmds.optionMenuGrp('imageMenuMentalRay', exists=1):
                # cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
                
            # 16 zip 
            cmds.setAttr('mentalrayGlobals.imageCompression', 4)
            cmds.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            cmds.setAttr('miDefaultFramebuffer.datatype', 16)
            '''
            self.setExtensionFramebuffer(datatype=16)
            
            
            print '====================!!!Done cllRLBGRENDER2DCreate!!!===================='    
            print '\n'
            return True
        print '====================!!!None cllRLBGRENDER2DCreate!!!===================='     
        print '\n'
        return False
    

    def settingPFXvisibility(self, value):
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]
        rlObjs = refCalimero 
        for cal in rlObjs:
                print 'cal.......',cal
                rels = cmds.listRelatives(cal, c=True)
                if rels:
                    print 'rels.......',cal
                    for rel in rels:
                        print 'rel.......',rel
                        if rel.endswith(':PFX'):
                            print 'SETTING PFX visibility',rel
                            cmds.editRenderLayerAdjustment(rel + '.visibility')
                            cmds.setAttr(rel+'.visibility', value)
        for aa in cmds.ls('*GRP_twoDline_stroke', r=True):
            if '_CALI' in aa:
                try:
                    cmds.editRenderLayerAdjustment(aa + '.visibility')
                    cmds.setAttr(aa+'.visibility', value)    
                except:
                    print 'for some reason is not possible to change visibility of',aa
                    pass
        return
    
    # PFX, CALI
    def cllRLBGPFXCreate(self):
        print '====================!!!Start cllRLBGPFXCreate!!!===================='
        print 'Working...cllRLBGPFXCreate'
        
        # 
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 
        lights = cmds.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')

        # 
        rlObjs = refCalimero 
        if rlObjs:
            # RenderLayer
            layerName = 'PFX'
            cmds.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            self.settingPFXvisibility(1)
            
            
            #
            for light in lights:
                lightGrp = cmds.listRelatives(light, p=1)[0]
                lightGrpP = cmds.listRelatives(lightGrp, p=1)[0
                #cmds.editRenderLayerAdjustment(light + '.intensity')
                #cmds.setAttr((light + '.intensity'), 0)
                cmds.editRenderLayerAdjustment(lightGrpP + '.v')
                cmds.setAttr((lightGrpP + '.v'), 0)
                
            # light_grp,hide
            lightGrps = mc.ls('*:LIGHTING')
            if lightGrps:
                for grp in lightGrps:
                    cmds.editRenderLayerAdjustment(grp + '.v')
                    cmds.setAttr((grp + '.v'), 0)
                   
            # renderPass
    
            # 
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCalimero
            
            # 
            shaderName = 'SHD_' + 'BLACK'
            if cmds.ls(shaderName):
                cmds.delete(shaderName)
            shaderNeed = cmds.shadingNode ('lambert', asShader=True, name=shaderName)   
            cmds.setAttr(('%s.color') % (shaderNeed), 0, 0, 0, type="double3")
    
            # 
            for SGNode in rlSGNodes:
                # RGB RGBA
                RGBNodeGrp = cmds.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    '''
                    # 寻找内部节点
                    listTxNodes = cmds.listConnections(RGBNode)
                    for nd in listTxNodes:
                        if "_BLACK" in nd:
                            needTxNode = nd
                            break
                    '''
                    #  BLACK
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_BLACK')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_BLACK')
                    # RGB/RGBA node
                    if cmds.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    cmds.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    cmds.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    cmds.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
            
            # 
            # self.cllRLCommonConfig()
    

            #mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            cmds.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')        
            cmds.setAttr('defaultRenderGlobals.imageFormat', 32)
            cmds.editRenderLayerAdjustment('defaultRenderGlobals.imfPluginKey')
            cmds.setAttr('defaultRenderGlobals.imfPluginKey','png', type="string")

            # 
            cmds.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')
            
            cmds.editRenderLayerAdjustment('defaultResolution.width')
            cmds.setAttr('defaultResolution.width', 3840)
            cmds.editRenderLayerAdjustment('defaultResolution.height')
            cmds.setAttr('defaultResolution.height', 2160)
    
            # exr
            '''
            if cmds.optionMenuGrp('imageMenuMentalRay', exists=1):
                cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                mel.eval('changeMentalRayImageFormat')
                cmds.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                mel.eval('changeMentalRayImageFormat')
            '''
            
            # 8 zip
            cmds.setAttr('mentalrayGlobals.imageCompression', 4)
            cmds.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            cmds.setAttr('miDefaultFramebuffer.datatype', 2)
    
            
            print '====================!!!Done cllRLBGPFXCreate!!!===================='   
            print '\n'
            return True
        print '====================!!!None cllRLBGPFXCreate!!!===================='   
        print '\n'
        return False
        

# -*- coding: utf-8 -*-

'''
Created on 2013-8-5

@author: liangyu
'''

import maya.cmds as mc
import maya.mel as mel


def zm_batchFX():
    
    #导入相机
    from idmt.maya.py_common import sk_infoConfig
    reload(sk_infoConfig)
    
    shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()          
    camFile = '//file-cluster/GDC/Projects/ZoomWhiteDolphin/Project/scenes/Animation/episode_'+shotInfo[1]+'/episode_camera/zm_'+shotInfo[1]+'_'+shotInfo[2]+'_cam.ma'
    cam='cam_'+shotInfo[1]+'_'+shotInfo[2]+'_baked'    
    if mc.ls(cam):
        mc.delete(cam)

    try:
        mc.file(camFile, i=1)
    except:
        print u'请确保有_bake相机'
        mc.error(u'请确保有_bake相机')

        
    #导入渲染文件
    from idmt.maya.ZoomWhiteDolphin import zm_AutoRenderLayer_ZoomWhiteDolphin
    reload(zm_AutoRenderLayer_ZoomWhiteDolphin)
    shot_info=zm_AutoRenderLayer_ZoomWhiteDolphin.zmRLConfig().ReadEXcle()
    shot_sence=shot_info[4]
    
    filepath='Z:/Projects/ZoomWhiteDolphin/ZoomWhiteDolphin_Scratch/VFX/waveBeachAutoRender/WavesBeach/'
    sign=''
    fileslist=mc.getFileList(folder= filepath)
    if fileslist:
        for list in fileslist:
            if list.split(".")[0]==shot_sence:
                sign=list.split(".")[0]
                
    if mc.ls('waveBeach'):
        mc.delete('waveBeach')                
    if sign:
        objFile='Z:/Projects/ZoomWhiteDolphin/ZoomWhiteDolphin_Scratch/VFX/waveBeachAutoRender/WavesBeach/'+shot_sence+'.mb'
        mc.file(objFile, i=1)
    else:
        print u'请确认文件夹下有相应镜头的场景文件'

        
    #分层
    layerName = 'fx_waveBeach'
    rlObjs=mc.ls('waveBeach')
    print rlObjs
    if mc.ls(layerName):
        mc.delete(layerName)
        
    if rlObjs:
        mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)
    else:
        print u'没有渲染物体'
    
               
    
    #渲染设置    
    zm_AutoRenderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLCommonConfig()
    zm_AutoRenderLayer_ZoomWhiteDolphin.zmRLConfig().mentalRayProductionLevel()        
   
    camShape = mc.listRelatives(mc.ls(cam, type='transform')[0], ni=1, s=1)[0]
    if mc.ls(cam, type='transform'):             
        mc.setAttr((camShape + '.renderable'), 1)
        try:
            mc.setAttr(('perspShape.renderable'), 0)
        except:
            pass
        
    #回到MASTER层
    mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
    mc.setAttr("defaultRenderLayer.renderable", 0)
    
    
def zmbatchFXwautoCreate():
    print ('=================================================================')
    print '====================!!!Start AutoRenderLayer!!!===================='

    from idmt.maya.ZoomWhiteDolphin import zm_batchrender
    reload(zm_batchrender)
    zm_batchrender.zm_batchFX()
    # save
    from idmt.maya.py_common import sk_infoConfig
    reload(sk_infoConfig)
    shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
    pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
    fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
    fileType = '_render_ef_c001.mb'
    fileName = fileName + fileType
    mc.file(rename=fileName)
    mc.file(save=1)
    
    mel.eval('zwMusterCheckin2 "" "" 0 0 0;')

    print '=======================!!!All Done!!!======================='
    print ('===========================================================')
    
    
    
    
    
        
        
    
        
        
    
    



            

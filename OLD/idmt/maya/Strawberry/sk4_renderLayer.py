# -*- coding: utf-8 -*-


import maya.cmds as mc
import maya.mel as mel

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_renderLayer_SK4(object):
    def __init__(self):
        pass


    # UIZMRenderLayer
    def sk_UISK4RenderLayersLayers(self):
        # 窗口
        if mc.window("sk_UISK4RenderLayersLayers", ex=1):
            mc.deleteUI("sk_UISK4RenderLayersLayers", window=True)
        mc.window("sk_UISK4RenderLayersLayers", title="SK4 RenderLayers Tools", widthHeight=(420, 500), resizeToFitChildren = True, menuBar=0)
        mc.window("sk_UISK4RenderLayersLayers", edit = True, widthHeight=(420, 500))
        # 主界面
        mc.columnLayout(adjustableColumn = True)

        mc.image(image = "Z:/Projects/Strawberry/Strawberry_Scratch/TD/image/p4.jpg",vis=1,width=445,height=267)
        mc.setParent("..")
        mc.setParent("..")
        # 分解创建
        mc.frameLayout(label=u'[MR]RenderLayers Ganeral | 通用设置', borderStyle='etchedOut', width=500)

        
        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'版本切换', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().sk_sceneNotAnim2Render(1)')
        mc.button(l=u'参考修正', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()\nsk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig()\nfrom idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam\nreload(sk_hbExportCam)\nsk_hbExportCam.sk_hbExportCam().camServerReference()')
        mc.button(l=u'自动分组', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)')
        mc.button(l=u'存lighting文件', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Strawberry4/sk4_SceneSave.mel"\')\nmel.eval(\"skSceneSave\")')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'工程目录设置', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Strawberry4/sk4_SetProject.mel"\')\nmel.eval(\"skSetProject\")')
        mc.button(l=u'Zdepth设置', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLayerZdepthDistanceConfigUI()')
        mc.button(l=u'贴图尺寸设置', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='mel.eval(\'source zwToggleMaps.mel;\')\nmel.eval(\"zwToggleMaps\\"\\"\")')
        mc.button(l=u'拆分文件', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='from idmt.maya.Strawberry import sk4_seperateTools\nreload(sk4_seperateTools)\nsk4_seperateTools.sk4_seperateUITools()')  
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'关闭头发系统', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='from idmt.maya.Strawberry import sk4_autorenderLayer\nreload(sk4_autorenderLayer)\nsk4_autorenderLayer.sk4_autorenderLayer().closeHairSysterm()')
        mc.button(l=u'p女孩手臂', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='from idmt.maya.Strawberry import p_arm\nreload(p_arm)\np_arm.p_arm()')
        mc.button(l=u'贴图转L盘', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/VickytheViking/slCGReplaceTexturePath.mel"\')\nmel.eval(\"slCGReplaceTexturePath\")')
        mc.button(l=u'wait', bgc=[0.3, 0.3, 0.3], width=100, height=25)
        mc.setParent("..")  
         
        mc.setParent("..")

        # 分解创建
        mc.frameLayout(label=u'[MR]RenderLayers Manual | 手动创建RenderLayers', borderStyle='etchedOut', width=500)

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[CHR]CO', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"CHR_CO\",0)')
        mc.button(l=u'[CHR]OCC', bgc=[0.3, 0.2, 0.1], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"CHR_AO\",1)')
        mc.button(l=u'[CHR]OSD', bgc=[0.3, 0.2, 0.1], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"CHRD_AO\",1)')
        mc.button(l=u'[CHR]NM', bgc=[0.3, 0.2, 0.1], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"CHR_NM\",1)')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[CHR]SHDW', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"CHR_SHDW\",0)')
        mc.button(l=u'[ALL]FBR', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"ALL_FBR\",0)')
        mc.button(l=u'[ALL]BSR', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"ALL_BSR\",0)')
        mc.button(l=u'[CHR]HAIR', bgc=[0.3, 0.2, 0.1], width=100, height=25,c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"CHR_HAIR\",1)')
        #mc.button(l=u'[Auto RL]', bgc=[0.2, 0.9, 0.2], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLAutoCreate()')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[BG]CO', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"BG_CO\",0)')
        mc.button(l=u'[BG]OCC', bgc=[0.3, 0.2, 0.1], width=100, height=25,c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"BG_AO\",1)')
        mc.button(l=u'[BG]NM', bgc=[0.3, 0.2, 0.1], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"BG_NM\",1)')
        mc.button(l=u'[BG]ZDP', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"BG_ZDP\",0)')
        mc.setParent("..")
        
        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'Smooth', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSwDoSmooth()')
        mc.button(l=u'控制器显隐', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbHideAllCharCon.mel"\')\nmel.eval(\"HbHideAllCharCon\")')
        mc.button(l=u'隐藏绿底', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Sk3/HhRenderTools.mel"\')\nmel.eval(\"HhFootDis\")')
        mc.button(l=u'镜像相机', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Sk3/HHCamMirror.mel"\')\nmel.eval(\"HHCamMirror\")')
        mc.setParent("..")  
        mc.setParent("..") 
        
        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'删除所有材质', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbLittleTools.mel"\')\nmel.eval(\"HbDeleteMaterials\")')
        mc.button(l=u'导入灯光', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Strawberry4/sk4_SceneSave.mel"\')\nmel.eval(\"sk4_importlight\")')
        mc.button(l=u'berry', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Strawberry/sk3RenderSwitchBerrykin.mel"\')\nmel.eval(\"sk3RenderSwitchBerrykin\")')
        mc.button(l=u'berrykin', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Strawberry/slRenderBerrykinColor.mel"\')\nmel.eval(\"slRenderBerrykinColor\")')
        mc.setParent("..")  
        mc.setParent("..")    
        
        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[ALL]FBR无透明', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"ALL_FBR01\",0)')
        mc.button(l=u'[ALL]BSR无透明', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.commonPerform.renderLayers import sk_renderLayer_SK4\nreload(sk_renderLayer_SK4)\nsk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLSpeficCreate(\"ALL_BSR01\",0)')
        mc.button(l=u'修改眼线', bgc=[0.1, 0.1, 0.1], width=100, height=25 ,c='from idmt.maya.Strawberry import changeeye\nreload(changeeye)\nchangeeye.sk4_changeeye()')
        mc.button(l=u'指定cache路径', bgc=[0.1, 0.1, 0.1], width=100, height=25 ,c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Strawberry4/sk4_serachcacheFile.mel"\')')
        mc.setParent("..")  
        mc.setParent("..")  
        
                                        
        
        mc.frameLayout(label=u'[Tools]RGBA ', borderStyle='etchedOut', width=500)
        mc.rowLayout(numberOfColumns=5, columnWidth4=(80, 80, 80, 80))
        mc.button(l=u'[Shader]R', bgc=[0.8, 0.1, 0.1], width=80, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/JT/HbJtRenderTools.mel"\')\nmel.eval(\"HbMaterialR()\")')
        mc.button(l=u'[Shader]G', bgc=[0.1, 0.8, 0.1], width=80, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/JT/HbJtRenderTools.mel"\')\nmel.eval(\"HbMaterialG()\")')
        mc.button(l=u'[Shader]B', bgc=[0.1, 0.6, 0.8], width=80, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/JT/HbJtRenderTools.mel"\')\nmel.eval(\"HbMaterialB()\")')
        mc.button(l=u'[Shader]M', bgc=[0.0, 0.0, 0.0], width=80, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/JT/HbJtRenderTools.mel"\')\nmel.eval(\"HbMaterialM()\")')
        mc.button(l=u'[Shader]A', bgc=[1.0, 1.0, 1.0], width=80, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/JT/HbJtRenderTools.mel"\')\nmel.eval(\"HbMaterialA()\")')
        mc.setParent("..")
        mc.setParent("..")
         
        mc.setParent("..")
        mc.showWindow("sk_UISK4RenderLayersLayers")
    

 
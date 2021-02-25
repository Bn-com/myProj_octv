# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_renameEnvLights.mel"')
mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/2013/zzjIdPassInfo.mel"')
def lUI():
    try:
        cmds.deleteUI("wxIISetRenderLayerUI")
    except:
        pass
    cmds.window('wxIISetRenderLayerUI',title="wxII__LightingTools",mxb=False)
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

##zzj  ▲Common
##zzj      ▲Create layers
    child1 = cmds.columnLayout(adjustableColumn=1)
    cmds.frameLayout( label='Create layers', labelAlign='top', collapsable=1)
    cmds.columnLayout(adjustableColumn=1)
##zzj          ▲GDC_layer
##zzj          ▲RBW_layer
    cmds.button(l='GDC_layer',h=40,c='import idmt.maya.ROMA.lightingUICMD as lightUICMD\nreload(lightUICMD)\nlightUICMD.createLayer()')
    cmds.button(l='RBW_layer',h=40,c='mel.eval(\"py_autoSetForRendering();rnd_wxII_setSpotLightFocus;\")')
    cmds.setParent( '..' )

    cmds.setParent( '..' )
##zzj      ▲Common tools
    cmds.frameLayout( label='Common tools', labelAlign='top')
##zzj          ▲存文件
##zzj          ▲导入渲染用摄像机
##zzj          ▲Shave补
##zzj          ▲Fur补
##zzj          ▲网渲补
    cmds.columnLayout(adjustableColumn=1)
    cmds.button(l=u'存文件',             c='mel.eval("py_saveLighting()")'   )
    cmds.button(l=u'导入渲染用摄像机',   c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_ImportRenderCam();")'    )
    cmds.button(l=u'Shave补',            c='mel.eval("eff_wxII_MShavePsets")'    )
    cmds.button(l=u'Fur补',              c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_FixBeforeRender.mel\\\";wxII_FixFurExtraAttributes();")'   )
    cmds.button(l=u'网渲补',             c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_FixBeforeRender.mel\\\";wxII_FixBeforeNetRender();")'   )
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.setParent( '..' )

##zzj  ▲Setting
##zzj      ▲setting
    child2 = cmds.columnLayout(adjustableColumn=1)
    cmds.frameLayout( label='Setting ', labelAlign='top')






##zzj          ▲设置Alpha、预乘以及渲染器参数
##zzj          ▲alph
##zzj          ▲quality
##zzj          ▲删除材质
    cmds.columnLayout(adjustableColumn=1)
    cmds.button(l=u'设置Alpha、预乘以及渲染器参数',c='execfile("//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_lightingTools4UI.py")\nwxII_LightingTools_setAlphaAndRenderSetting()')
    cmds.button(l='alpha',en=0)
    cmds.button(l='quality',c='',en=0)
    cmds.button(l=u'删除材质',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";lighting_DeleteUnusedNode();")')
    cmds.setParent( '..' )
    cmds.setParent( '..' )

##zzj      ▲打开
    cmds.frameLayout( label=u'打开', labelAlign='top')
    cmds.columnLayout(adjustableColumn=1)
##zzj          ▲打开Finishing文件目录
##zzj          ▲打开分层规范表
##zzj          ▲打开头发阴影颜色表
    cmds.button(l=u'打开Finishing文件目录',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_OpenFinishingPath();")')
    cmds.button(l=u'打开分层规范表',c='import os\nos.startfile(r"\\\\file-cluster\GDC\Resource\Support\Maya\Import\iRender\RenderInfo\ROMA\lighting_parameter.xls")')
    cmds.button(l=u'打开头发阴影颜色表',c='import os\nos.startfile(r"\\\\file-cluster\GDC\Resource\Support\Maya\Import\iRender\RenderInfo\ROMA\GDC_lights_ShadowColor.xls")')

    cmds.setParent( '..' )
    cmds.setParent( '..' )




    cmds.setParent( '..' )

##zzj  ▲Light tools
    child3 = cmds.columnLayout(adjustableColumn=1)
##zzj      ▲重命名灯光`
    cmds.frameLayout( label=u'重命名灯光', labelAlign='top')
    form = cmds.formLayout(numberOfDivisions=100)
##zzj          ▲columnLayout`
    column1 = cmds.columnLayout(adj=1)
##zzj              ▲chr_keyLight`
##zzj              ▲chr_fillLight`
##zzj              ▲chr_bounceLight`
##zzj              ▲chr_ambientLight`
    cmds.button(l='chr_keyLight',         c='mel.eval("renameEnvLights(\\\"chrkeyLight\\\")")')
    cmds.button(l='chr_fillLight',          c='mel.eval("renameEnvLights(\\\"chrfillLight\\\")")')
    cmds.button(l='chr_bounceLight',    c='mel.eval("renameEnvLights(\\\"chrbounceLight\\\")")')
    cmds.button(l='chr_ambientLight',   c='mel.eval("renameEnvLights(\\\"chrambientLight\\\")")')
    cmds.setParent( '..' )
##zzj          ▲columnLayout
    column2 = cmds.columnLayout(adj=1)
##zzj              ▲env_keyLight
##zzj              ▲env_fillLight
##zzj              ▲env_bounceLight
##zzj              ▲env_ambientLight
    cmds.button(l='env_keyLight',         c='mel.eval("renameEnvLights(\\\"envkeyLight\\\")")')
    cmds.button(l='env_fillLight',          c='mel.eval("renameEnvLights(\\\"envfillLight\\\")")')
    cmds.button(l='env_bounceLight',    c='mel.eval("renameEnvLights(\\\"envbounceLight\\\")")')
    cmds.button(l='env_ambientLight',   c='mel.eval("renameEnvLights(\\\"envambientLight\\\")")')
    cmds.setParent( '..' )
    column3 = cmds.columnLayout(adj=1)
##zzj          ▲columnLayout
##zzj              ▲手动重命名
    cmds.button(l=u'手动重命名',   c='mel.eval("renameEnvLights(\\\"manualUI\\\")")')
    cmds.setParent( '..' )

    cmds.formLayout( form,
            edit=True,
            attachForm=     [
                                (column1, 'left', 5), (column1, 'top', 5),
                                (column2, 'right', 5),(column2, 'top', 5),
                                (column3, 'left', 5),(column3, 'right', 5),(column3, 'bottom', 5)
                            ]
                        ,
            attachPosition= [
                                (column1, 'right', 5, 50),
                                (column2, 'left', 5, 50)
                            ]
                        ,
			attachControl=	[
    							(column3, 'top', 5, column2)
						    ]

                )
    cmds.setParent( '..' )
    cmds.setParent( '..' )
##zzj      ▲Other tools
    cmds.frameLayout( label='Other tools ', labelAlign='top')
    cmds.columnLayout(adjustableColumn=1)
    form = cmds.formLayout(numberOfDivisions=100)
##zzj          ▲columnLayout`
    column1 = cmds.columnLayout(adj=1)
##zzj          ▲关闭灯光漫反射
    cmds.button(l=u'关闭灯光漫反射',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_TurnOffEmitDiffuse();")')

    cmds.setParent( '..' )
##zzj          ▲columnLayout
    column2 = cmds.columnLayout(adj=1)
##zzj          ▲关闭灯光高光
    cmds.button(l=u'关闭灯光高光',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_TurnOffEmitSpecular();")')

    cmds.setParent( '..' )

    cmds.formLayout( form,
            edit=True,
            attachForm=     [
                                (column1, 'left', 5), (column1, 'top', 5),
                                (column2, 'right', 5),(column2, 'top', 5)
                            ]
                        ,
            attachPosition= [
                                (column1, 'right', 5, 50),
                                (column2, 'left', 5, 50)
                            ]
                )
    cmds.setParent( '..' )

##zzj          ▲眼球
##zzj          ▲灯光变白，阴影变黑
##zzj          ▲导入kiko 专用灯
##zzj          ▲根据数据库，改头发灯阴影颜色
    cmds.button(l=u'眼球',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_eyeTools();")')
    cmds.button(l=u'灯光变白，阴影变黑',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_TurnBackLightColor();")')
    cmds.button(l=u'导入kiko 专用灯',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";importKikoLight();")')
    cmds.button(l=u'根据数据库，改头发灯阴影颜色',c='import idmt.maya.ROMA.GDC_lights_ShadowColor as GDC_Sc\nreload(GDC_Sc)\nGDC_Sc.ChangeColor()')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.setParent( '..' )


##zzj  ▲Utility Tools
    child4 = cmds.columnLayout(adjustableColumn=1)
##zzj      ▲tool1
    cmds.frameLayout( label='Tool1 ', labelAlign='top')
    cmds.columnLayout(adjustableColumn=1)
##zzj          ▲贴图缩放
##zzj          ▲设置smooth级别
##zzj          ▲设置摄像机的剪切面
    cmds.button(l=u'贴图缩放',c='mel.eval("zwToggleMaps\\\"WinxClubII\\\"")')
    cmds.button(l=u'设置smooth级别',c='mel.eval("zjTDSmooth")')
    cmds.button(l=u'设置摄像机的剪切面',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_SetFarClipOfCamera();")')
    cmds.setParent( '..' )
    cmds.setParent( '..' )

##zzj      ▲材质工具
    cmds.frameLayout( label=u'材质工具', labelAlign='top')
    cmds.columnLayout()
##zzj          ▲rCLayout
    cmds.rowColumnLayout(numberOfRows=1,rh=(1,40))
##zzj              ▲ColorR
##zzj              ▲ColorG
##zzj              ▲ColorB
##zzj              ▲Color
##zzj              ▲Matte
    cmds.symbolButton(ann="ColorR",     image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorR.xpm",     c='mel.eval("zzjIDPass_Material_Assign(\\\"colorR\\\")")')
    cmds.symbolButton(ann="ColorG",     image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorG.xpm",     c='mel.eval("zzjIDPass_Material_Assign(\\\"colorG\\\")")')
    cmds.symbolButton(ann="ColorB",     image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorB.xpm",     c='mel.eval("zzjIDPass_Material_Assign(\\\"colorB\\\")")')
    cmds.symbolButton(ann="ColorA",     image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorA.xpm",     c='mel.eval("zzjIDPass_Material_Assign(\\\"colorA\\\")")')
    cmds.symbolButton(ann="Matte",      image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\matte.xpm",      c='mel.eval("zzjIDPass_Material_Assign(\\\"matte\\\")")')
    cmds.setParent( '..' )
##zzj          ▲rCLayout
    cmds.columnLayout()
    cmds.separator(style='out',height=10,w=1000)
    cmds.setParent( '..' )
    cmds.rowColumnLayout(numberOfRows=1,rh=(1,40))
##zzj              ▲Depth
##zzj              ▲Shadow
##zzj              ▲AO
##zzj              ▲Lambert
    cmds.symbolButton(ann="Depth",      image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\depth.bmp",      c='mel.eval("zzjIDPass_Material_Assign(\\\"depth\\\")")')
    cmds.symbolButton(ann="Shadow", image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\shadow.bmp", c='mel.eval("zzjIDPass_Material_Assign(\\\"shadow\\\")")')
    cmds.symbolButton(ann="AO",     image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\AO.bmp",     c='mel.eval("zzjIDPass_Material_Assign(\\\"AO\\\")")')
    cmds.symbolButton(ann="Lambert",    image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\lambert.xpm",    c='mel.eval("zzjIDPass_Material_Assign(\\\"lambert\\\")")')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.setParent( '..' )

##zzj  ▲RBW Tools
    child5 = cmds.columnLayout(adjustableColumn=1)
##zzj      ▲Setting
    cmds.frameLayout( label='Setting ', labelAlign='top')
##zzj          ▲Create Light Rig
##zzj          ▲Create Hairs Light Rig
##zzj          ▲Neutralize Color
##zzj          ▲Create Occlusion
##zzj          ▲Create SSS Shader
    cmds.columnLayout(adjustableColumn=1)
    cmds.button(l='Create Light Rig',       c='mel.eval("py_createLightRig")')
    cmds.button(l='Create Hairs Light Rig', c='mel.eval("py_createHairsLightRig")')
    cmds.button(l='Neutralize Color',       c='mel.eval("py_neutralizeColor")')
    cmds.button(l='Create Occlusion',       c='mel.eval("py_createOcclusion")')
    cmds.button(l='Create SSS Shader',  c='mel.eval("py_createSSSShader")')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
##zzj      ▲MM Shader Path
    cmds.frameLayout( label='MM Shader Path ', labelAlign='top')
    cmds.columnLayout(adjustableColumn=1)
    cmds.textField(text=r'\\file-cluster\GDC\Resource\Support\Pixar\Shader',editable=0)
##zzj          ▲打开MM文件夹
    cmds.button(l=u'打开MM文件夹',c='os.startfile(r"\\\\file-cluster\\GDC\\Resource\\Support\\Pixar\\Shader")')
    cmds.setParent( '..' )
    cmds.setParent( '..' )


    cmds.setParent( '..' )

    cmds.tabLayout( tabs, edit=True, tabLabel=(
                                        (child1, 'Common'),
                                        (child2, 'Setting'),
                                        (child3, 'Light Tools'),
                                        (child4, 'Utility Tools'),
                                        (child5, 'RBW Tools')
                                    ))
    cmds.window('wxIISetRenderLayerUI',e=1,width=305,height=340)

    cmds.showWindow("wxIISetRenderLayerUI")

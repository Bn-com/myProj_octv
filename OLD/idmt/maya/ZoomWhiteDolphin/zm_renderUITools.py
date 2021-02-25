import maya.cmds as mc
import maya.mel as mel
import sys


def zm_renderUITools():
    ui = '//file-cluster/GDC/Resource/Support/Maya/projects/ZoomWhiteDolphin/ZMrenderTools.myuis'
    sys.path.append('//file-cluster/GDC/Resource/Support/Maya/projects/DODIII/')
    if mc.window('ZMrenderTools', ex=1):
        mc.deleteUI('ZMrenderTools')
    mui = mc.loadUI(f=ui)

    mc.window("ZMrenderTools", e=1, tlc=(10, 10))
    mc.showWindow(mui)
    mc.button("setProject_button", e=1, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/VickytheViking/vvSetProject.mel"\')\nmel.eval(\"vvSetProject\")')
    mc.button("setsmooth_button", e=1, c='from idmt.maya.py_common import sk_smoothSet\nreload(sk_smoothSet)\nsk_smoothSet.sk_smoothSetTools().smoothSetDoSmooth()')
    mc.button("split_button", e=1, c='')
    mc.button("layering_button", e=1, c='')
    mc.button("net_button", e=1, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/2013/MusterCheckin.mel"\');\nmel.eval(\" MusterCheckin()\")')

    mc.button("r1_button", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"R\")')
    mc.button("g1_button", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"G\")')
    mc.button("b1_button", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"B\")')
    mc.button("m1_button", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"M\")')

    mc.button("LGTSYS_CHR", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_LGTSYS\")')
    mc.button("LINE_CHR", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_LINE\")')
    mc.button("CO_FG", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"FG_CO\")')
    mc.button("CO_BG", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"BG_CO\")')

    mc.button("LGT_FG", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"FG_LGT\")')
    mc.button("Zdepht_ALL", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"ALL_ZDEPTH\")')
    mc.button("Mask01_ALL", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"ALL_MASK01\")')

    mc.button("Caustics_CHR", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_CAUSTICS\")')
    mc.button("Cautics_FG", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"BG_CAUSTICS\")')
    mc.button("SHDW_SEA", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"SEA_SHDW\")')
    mc.button("MSK_SEA", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"SEA_MSK\")')

    mc.button("Mask_FG", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"BG_MASK02\")')
    mc.button("CP_SEA", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"SEA_CP\")')

    mc.button("Normal_ALL", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"ALL_NM\")')
    mc.button("Zdepht_FG", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"BG_ZDEPTH\")')

    #mc.button("deleteMaterial_button",e=1,c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbLittleTools.mel"\');\nmel.eval(\'HbDeleteMaterials()\')')
    mc.button("Zdepth", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLayerZdepthDistanceConfigUI()')
    mc.button("DeleteLayer", e=1, c='import do3_renderToolsUICMDS\ndo3_renderToolsUICMDS.do3_deleteAllRenderlayer()')

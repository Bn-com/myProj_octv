# -*- coding: utf-8 -*-
'''
Created on 2014-7-25

@author: liangyu
'''

import maya.cmds as mc
import sys


def zm_renderUITools():
    ui = '//file-cluster/GDC/Resource/Support/Maya/projects/Strawberry4/sk4_seperatefile.myuis'
    if mc.window('sk4_seperateTools', ex=1):
        mc.deleteUI('sk4_seperateTools')
    mui = mc.loadUI(f=ui)

    mc.window("sk4_seperateTools", e=1, tlc=(10, 10))
    mc.showWindow(mui)
    
 

    mc.button("MRBG_Ridio", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"R\")')
    mc.button("MRCHR_Ridio", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"G\")')
    mc.button("MRhair_Ridio", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"B\")')
    mc.button("SWBG_Ridio", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"M\")')
    mc.button("SWCHR_Ridio", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_LGTSYS\")')   
    mc.button("SWRGB_Ridio", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_LINE\")')
   
    mc.button("sk4_button", e=1, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"FG_CO\")')
  

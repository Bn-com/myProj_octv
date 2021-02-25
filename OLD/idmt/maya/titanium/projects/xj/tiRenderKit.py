# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import mtoa
import mtoa.cmds.registerArnoldRenderer
import json
import tempfile


def RenderToolKit():
    
    if mc.window('tiRenderToolKitUI', exists=True):
        mc.deleteUI('tiRenderToolKitUI')
    mc.window('tiRenderToolKitUI', title=u'tiRenderToolKitUI -- 星际车神',
              width=320, height=350, sizeable=True)

    form = mc.formLayout()
    tabs = mc.tabLayout('tabTiRenderToolKit',innerMarginWidth=5, innerMarginHeight=5)
    mc.formLayout(
        form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
    child1 = mc.columnLayout(adjustableColumn=True)
    # mc.frameLayout(label=u'角色', bgc=[0, 0, 0.0], cll=0,cl=1)
    # mc.rowColumnLayout(numberOfColumns=4)
    # mc.button(label=u'Char Color',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck = True).setupChrColorLayer()')
    # mc.button(label=u'Char AOV',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck = True).setupChrAovLayer()')
    # mc.button(label=u'Char IDP',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck = True).setupChrIdpLayer()')

    # mc.setParent('..')
    # mc.setParent('..')

    # mc.frameLayout(label=u'场景', bgc=[0, 0, 0.0], cll=0,cl=1)
    # mc.rowColumnLayout(numberOfColumns=4)
    # mc.button(label=u'Set Color',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck = True).setupSetColorLayer()')
    # mc.button(label=u'Set AOV',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck = True).setupSetAovLayer()')
    # mc.button(label=u'Set IDP',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck = True).setupSetIdpLayer()')
    # mc.setParent('..')
    # mc.setParent('..')

    # mc.frameLayout(label=u'角色&场景', bgc=[0, 0, 0.0], cll=0,cl=1)
    # mc.rowColumnLayout(numberOfColumns=4)
    # mc.button(label=u'SetCon',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck = True).setupSetConLayer()')

    # mc.setParent('..')
    # mc.setParent('..')


    mc.frameLayout(label=u'角色&场景&合并', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'Color',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck =  True).setupColorLayer()')
    mc.button(label=u'AOV',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck =  True).setupAovLayer()')
    mc.button(label=u'IDP',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck =  True).setupIdpLayer()')
    mc.button(label=u'AO',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck =  True).setupAOLayer()')
    mc.button(label=u'Shadow',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer(preCheck =  True).setupShadowLayer()')

    mc.setParent('..')
    mc.setParent('..')




    mc.setParent('..')
    
    child2 = mc.columnLayout(adjustableColumn=True)
    mc.frameLayout(label=u'IDP输出工具', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'ID11',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.rgbInfoExport("ID11")')
    mc.button(label=u'ID12',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.rgbInfoExport("ID12")')
    mc.button(label=u'ID13',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.rgbInfoExport("ID13")')
    mc.button(label=u'ID14',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.rgbInfoExport("ID14")')
    mc.button(label=u'ID检测',width=90,height=30,bgc=[0, 0.5, 0], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.readRGBInfoTest()')
    mc.setParent('..')
    mc.setParent('..')

    mc.frameLayout(label=u'IDP材质工具', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'R',width=90,height=30,bgc=[1, 0, 0], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.ArnoldIDCreat("ArnoldIdpR")')
    mc.button(label=u'G',width=90,height=30,bgc=[0,1, 0], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.ArnoldIDCreat("ArnoldIdpG")')
    mc.button(label=u'B',width=90,height=30,bgc=[0, 0, 1], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.ArnoldIDCreat("ArnoldIdpB")')
    mc.button(label=u'M',width=90,height=30,bgc=[0, 0, 0], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.ArnoldIDCreat("ArnoldIdpM")')
    mc.button(label=u'A',width=90,height=30,bgc=[1, 1, 1], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.ArnoldIDCreat("ArnoldIdpA")')
    mc.setParent('..')
    mc.setParent('..')

    # mc.button(label=u'Char IDP11',width=90,height=30,bgc=[0.13, 0.15, 0.25])
    # mc.button(label=u'Char IDP12',width=90,height=30,bgc=[0.0, 0.0, 0.0])
    # mc.button(label=u'Char IDP21',width=90,height=30,bgc=[0.0, 0.0, 0.0])
    # mc.button(label=u'Char IDP22',width=90,height=30,bgc=[0.0, 0.5, 0.0])

    mc.setParent('..')


    child3 = mc.columnLayout(adjustableColumn=True)
    mc.frameLayout(label=u'角色', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'Char Color',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("chrColor")')
    mc.button(label=u'Glass Color',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("glassColor")')
    mc.button(label=u'Char AOV',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("chrAov")')
    mc.button(label=u'Char AO',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("chrAo")')
    mc.button(label=u'Char Shadow',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("chrShadow")')
    mc.button(label=u'Char IDP',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("chrIdp")')

    mc.setParent('..')
    mc.setParent('..')

    mc.frameLayout(label=u'场景', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'Set Color',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("setColor")')
    mc.button(label=u'Set AOV',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("setAov")')
    mc.button(label=u'Set AO',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("setAo")')
    mc.button(label=u'Set IDP',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("setIdp")')
    mc.button(label=u'Set Shadow',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("setShadow")')

    mc.setParent('..')
    mc.setParent('..')

    # mc.frameLayout(label=u'角色&场景', bgc=[0, 0, 0.0], cll=0,cl=1)
    # mc.rowColumnLayout(numberOfColumns=4)
    # mc.button(label=u'SetCon',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'from idmt.maya.titanium.projects.xj import tiAutoRenderLayer;reload(tiAutoRenderLayer);tiAutoRenderLayer.tiAutoRenderLayer().testSetupLayer("setCon")')
    # mc.setParent('..')
    # mc.setParent('..')

    mc.setParent('..')


    child4 = mc.columnLayout(adjustableColumn=True)
    mc.button(label = 'c')
    mc.setParent('..')
    mc.tabLayout(tabs, edit=True, tabLabel=(
        (child1, u'分层'), (child2, u'工具'), (child3, u'分层测试'),(child4, u'TMP')))
    mc.showWindow('tiRenderToolKitUI')    




def tiFindIDPUI():
    
    if mc.window('tiFindIDP', exists=True):
        mc.deleteUI('tiFindIDP')
    mc.window('tiFindIDP', title=u'tiFindIDP -- 星际车神',
              width=320, height=350, sizeable=True)

    form = mc.formLayout()
    tabs = mc.tabLayout('tabTiFindIDP',innerMarginWidth=5, innerMarginHeight=5)
    mc.formLayout(
        form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
    child1 = mc.columnLayout(adjustableColumn=True)

    items = getIdpFiles().keys()

    mc.textScrollList( 
        numberOfRows=8, 
        allowMultiSelection=True,
        append=items,
        showIndexedItem=4,
        font = 'plainLabelFont',
        height = 50

    )
    mc.setParent('..')


    
    child2 = mc.columnLayout(adjustableColumn=True)
    

    mc.setParent('..')


    child3 = mc.columnLayout(adjustableColumn=True)
    

    mc.setParent('..')


    
    mc.tabLayout(tabs, edit=True, tabLabel=(
        (child1, u'角色'), (child2, u'道具'), (child3, u'场景')))
    mc.showWindow('tiFindIDP')   


def getIdpFiles():

    basePath = r'\\file-cluster\gdc\Projects\XJCS\Project\data\AssetInfos'

    chrPath = os.path.join(basePath, 'characters')
    propPath = os.path.join(basePath, 'props')
    setPath = os.path.join(basePath, 'sets')

    idpInfos = {}

    
    for key, val in {'characters':chrPath, 'props': propPath, 'sets': setPath}.items():
        objs = {}

        for root, dirs, files in os.walk(val):

            for f in files:
                seps = f.split('_RGB_ID')
                if len(seps) > 1:
                    obj = seps[0]
                    if obj not in objs:
                        objs[obj] = os.path.join(root, f)
        idpInfos[key] = objs



    path = os.path.join(tempfile.gettempdir(), 'IDP-INFO.json')

    with open(path, 'w') as fh:
        fh.write(json.dumps(idpInfos, indent = 4))
        print 'aaaaaaaaaa'


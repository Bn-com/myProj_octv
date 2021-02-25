# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import time
import json
import shutil

import tempfile
import math
from functools import partial

import tiCheckTools as tiCheckTools
reload(tiCheckTools)

import idmt.maya.unknownPlugin as rup

import tiBase as  tiBase
reload(tiBase)

import tiFile as tiFile
reload(tiFile)

import tiBatchCmd as tiBatchCmd
reload(tiBatchCmd)


def myRemoveUnknownPlugin(dest):
    filename = os.path.basename(dest)
    temp = os.path.join(tempfile.gettempdir(), filename)
    if os.path.isfile(temp):
        os.remove(temp)
    plugins = rup.RemoveUnknownPluginMb(dest, temp)

    if len(plugins) > 0:
        print temp
        mc.file(temp, open = True, force = True)
        msg = u'未知插件已清理,\n当前文件临时保存在: %s \n请另存' % temp
        mc.confirmDialog( title=u'请另存当前文件', message=msg, messageAlign = 'center', button=[u'确定'] )
    else:
        print dest
        mc.file(dest, open = True, force = True)

    tiBase.deleteNodesByType('makeTextCurves')
    tiBase.deleteNodesByType('unknownDag')
    tiBase.deleteNodesByType('unknown')

    if not mc.objExists( '__OA__'):
        mc.createNode('closestPointOnMesh', name = '__OA__')

    os.remove(temp)

# if not mc.attributeQuery( '__OA__', node='layerManager', ex = True):
#     mc.addAttr('layerManager', ln = '__OA__',  at = 'bool')

# mc.deleteAttr('layerManager.__OAa__')

def openAndCleanUnknownPluginFile():
    multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb)"
    filePath = pm.fileDialog2(fileFilter=multipleFilters, dialogStyle=2, fileMode = 1)
    if filePath:
        myRemoveUnknownPlugin(filePath[0])



    

    
def deleteOANode():
    try:
        if mc.objExists( '__OA__'):
            mc.delete('__OA__')
    except:
        pass


def deleteUnknownAttrs():
    obj = mc.ls(sl = True, type = 'transform')
    for o in obj:
        for i in mc.listAttr(o, keyable  = True):
            if i not in ['visibility', 'translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ', 'scaleX', 'scaleY', 'scaleZ']:
                try:
                    pm.PyNode(o + '.' + i).delete()
                except:
                    mc.warning('Attribute can not delete: %s' % i)
    
def setupFileGroups(type):
    groups = ['MODEL', 'MSH_all', 'MSH_geo']
    groups.insert(0,type)
    if type:
        if not mc.objExists(groups[0]):
            cGrp = None
            for grp in groups:
                if grp == groups[0]:
                    cGrp = mc.group(em = True, name = grp)
                else:
                    cGrp = mc.group(em = True, name = grp, parent = cGrp)

            # for i in range(len(groups) - 1):
            #     mc.parent(groups[i+1], groups[i])
        else:
            mc.error('%s is already exists!!!' % groups[0])
    

def shaderNameRuelsUI():
    
    names = tiBase.readShaderNameRules()
        
    cols = math.ceil(len(names) / 5)

    if mc.window('tiShaderRulesWin',exists = True):

        mc.deleteUI('tiShaderRulesWin')
    mc.window('tiShaderRulesWin', title = u'Titanium 材质球命名工具', width = 680, height = 300, sizeable = False)
    mc.windowPref( 'tiShaderRulesWin', remove = True )
    mc.scrollLayout(horizontalScrollBarThickness=16,verticalScrollBarThickness=16)
    mc.columnLayout(columnAttach=('both', 5), rowSpacing=10, columnWidth=660)

    for name in sorted(names):
        mc.columnLayout( rowSpacing=10, columnWidth=660 )
        mc.text( label=names[name]['chn'], font = 'fixedWidthFont', bgc = [0,1,1], width = 50 )
        mc.gridLayout( numberOfColumns=5, cellWidthHeight=(130, 50) )
        for item in names[name]['items']:
            mc.button(label = item['chn'], command = partial(renameSelShader,item['eng']))
        mc.setParent('..')
        mc.setParent('..')
        
    mc.showWindow( 'tiShaderRulesWin' )


def openAndSelPath(*args):
    # multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb)"
    filePath = pm.fileDialog2(dialogStyle=2, fileMode = 3)
    if filePath:
        mc.textFieldButtonGrp('unknownFilePath', e = True, text = filePath[0])
        fileItems = []
        for path, subdirs, files in os.walk(filePath[0]):
            for file in files:
                item = os.path.normpath(os.path.join(path, file))
                if os.path.splitext(item)[1] in ['.mb', '.ma']:
                    fileItems.append(item)
        mc.textScrollList( "fileList", e = True, append = fileItems)


def doRemoveUnknownPlugin(*args):
    
    import datetime
    now = datetime.datetime.now()  

    files = mc.textScrollList("fileList", q = True, allItems = True)
    if files:
        for dest in files:

            filename = os.path.basename(dest)
            
            temp = os.path.join(tempfile.gettempdir(), filename)
            
            if os.path.isfile(temp):
                os.remove(temp)
            plugins = []
            if os.path.splitext(dest)[1] == '.mb':
                plugins = rup.RemoveUnknownPluginMb(dest, temp)

            elif os.path.splitext(dest)[1] == '.ma':
                plugins = rup.RemoveUnknownPluginMa(dest, temp)

            if len(plugins) > 0:
                if filename[:2] == 'xj':
                    bakePath = os.path.normpath(u'Z:/Projects/XJCS/xjcs_交换空间/TD/备份/%s' % (now.strftime('%Y-%m-%d')))
                    if not os.path.exists(bakePath):
                        os.makedirs(bakePath)
                    newFile = os.path.join(bakePath, filename)
                    shutil.copyfile(dest, os.path.join(bakePath, filename))
                    print u'文件已备份到: %s' % newFile
                shutil.copyfile(temp,dest)


def cleanUnknownPluginsUI():
    
    if mc.window('tiCleanUnknownPluginsWin', q = True, exists = True):
        
        mc.deleteUI('tiCleanUnknownPluginsWin')
    mc.window('tiCleanUnknownPluginsWin', title = u'Titanium 清除未知插件工具', width = 680, height = 300, sizeable = False)
    mc.windowPref( 'tiCleanUnknownPluginsWin', remove = True )

    mc.scrollLayout(horizontalScrollBarThickness=16,verticalScrollBarThickness=16)
    mc.columnLayout(columnAttach=('both', 5), rowSpacing=10, columnWidth=660)
    mc.textFieldButtonGrp('unknownFilePath', label=u'路径', text='', buttonLabel=u'浏览', bc = openAndSelPath )
    mc.textScrollList( "fileList", allowMultiSelection=True)

    mc.button( label=u'开始清除', command = doRemoveUnknownPlugin)

    mc.showWindow( 'tiCleanUnknownPluginsWin' )


def renameSelShader(name, *args):
    aiMats = mc.ls(sl = True, type = 'aiStandardSurface') + mc.ls(sl = True, type = 'aiTwoSided')
    if aiMats:
        propName = tiBase.propName()
        for mat in aiMats:
            objs = tiBase.getObjsByMaterial(mat)
            SE =  mc.listConnections(mat, type = 'shadingEngine')

            if objs:
                objName = objs[0].split('|')[-1] if '|' in objs[0] else objs[0]
                objName = objName[0:-1] if objName[-1] == '_' else  objName

                newMatName = 'SHD_%s_%s_%s' % (propName, objName, name)
                if objName[-1] == '_':
                    newMatName = 'SHD_%s_%s%s' % (propName, objName, name)

                if mat != newMatName:
                    step = 666
                    while True:
                        if mc.objExists(newMatName):
                            objNameAdd = (objName + str(step))
                            newMatName = 'SHD_%s_%s_%s' % (propName, objNameAdd, name)
                            step = step + 1
                        else:
                            break
                    mc.rename(mat, newMatName)

                    mc.rename(SE[0], newMatName.replace('SHD_', 'SG_'))
            else:
                mc.warning(u'该材质球没有赋给任何物体')

    else:
        mc.warning(u'该材质球不是 aiStandardSurface 类型的')


def checkFile(proj):
    tiCheckTools.checkDetailsWarning(errorMode = 1)


def checkFileUI(proj):
    tiCheckTools.sk_sceneUICheckTools()


def rgCompareTx():
    print u'======start rg2tx compare======'
    compareAssetInfoTo('TX')
    print u'======end rg2tx compare======'


def txCompareRg():
    print u'======start tx2rg compare======'
    compareAssetInfoTo('RG')
    print u'======end tx2rg compare======'


def compareFile():
    tf = tiFile.tiAssetFile()
    if tf.type in ['tx', 'ms_render']:
        txCompareRg()
    elif tf.type in ['rg', 'ms_anim']:
        rgCompareTx()

# def rgCompareTx():
#     isDiffer = False
#     tf = tiFile.tiAssetFile()
#     if not tf.rgtxIgnore:
#         jsonFile = tf.txAssetInfoFile
#         if os.path.exists(jsonFile):
#             isDiffer = tiBase.compareFile(jsonFile, 'TX')
#         else:
#             txFile = tf.msRenderFile if os.path.exists(tf.msRenderFile) else (tf.txFile if os.path.exists(tf.txFile) else None)
            
#             if txFile:
#                 tiBatchCmd.runMayaBatch(txFile, 'python(\\"import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.writeAssetInfo(\'TX\')\\")')
#                 isDiffer = tiBase.compareFile(jsonFile, 'TX')
#             else:
#                 print u'暂无TX或MS_RENDER文件,不做对比，略过'

#         if isDiffer:
#             mc.error(u'======本素材rg和tx版本有出入，请前期和设置协商共同处理。详细信息请打开Script Editor查看======')
#     else:
#         mc.warning(u'%s 在 rgtxIgnore 文件中存在,不做对比检测。严禁非法豁免操作!' % tf.id)

def compareVtxInfo():
    mc.currentUnit(linear = 'cm')
    mc.select(cl = True)
    tf = tiFile.tiAssetFile()
    if not tf.rgtxIgnore:
        if tf.type in ['rg', 'ms_anim', 'tx', 'ms_render']:
            
            # jsonFile = tf.rgVertexInfoFile if tf.type in ['tx', 'ms_render'] else tf.txVertexInfoFile
        
            # if not os.path.exists(jsonFile):
            #     compareFile = None
            #     if tf.type in ['tx', 'ms_render']:
            #         compareFile = tf.msAnimFile if os.path.exists(tf.msAnimFile) else (tf.rgFile if os.path.exists(tf.rgFile) else None)
                
            #     else:
            #         compareFile = tf.msRenderFile if os.path.exists(tf.msRenderFile) else (tf.txFile if os.path.exists(tf.txFile) else None)

            #     if compareFile:
            #         tiBatchCmd.runMayaBatch(compareFile, 'python(\\"import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.writeVertexInfo()\\")')
            #     else:

            #         newCompareFile = 'AN' if tf.type in ['tx', 'ms_render'] else 'TX'
            #         print u'\n=== 无%s文件，现尝试与MO文件作对比 ===\n' % newCompareFile


            #         jsonFile = tf.moVertexInfoFile
                    
            #         if not os.path.exists(jsonFile):
            #             compareFile = tf.moFile if os.path.exists(tf.moFile) else None
                    
            #             if not compareFile:

            #                 print u'没有此文件: %s' % tf.moFile
            #                 mc.error(u'====== 无对比文件, 请联系PA ======')
            #             else:
            #                 tiBatchCmd.runMayaBatch(compareFile, 'python(\\"import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.writeVertexInfo()\\")')

            jsonFile = tf.moVertexInfoFile
            
            if not os.path.exists(jsonFile):
                
                compareFile = tf.moFile if os.path.exists(tf.moFile) else None
            
                if compareFile:
                    tiBatchCmd.runMayaBatch(compareFile, 'python(\\"import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.writeVertexInfo()\\")')
                else:
                    print u'没有此文件: %s' % tf.moFile
                    mc.error(u'====== see more information ======')

            isDiffer = False
            vtxData = tiBase.jsonRead(jsonFile)
            objs = tiBase.getObjsUnderModel()
            for obj in objs:
                
                if vtxData.has_key(obj.longName()):
                    vtxNum = pm.polyEvaluate(obj, vertex = True)
                    vtxDataNum = len(vtxData[obj.longName()])
                    if vtxNum == vtxDataNum:
                        for i, pos in enumerate(vtxData[obj.longName()]):
                            mypos = pm.xform('%s.vtx[%d]' % (obj, i), q = True, a = True, ws = True, translation = True )

                            if tiBase.distance(pos, mypos) > 0.001:
                                isDiffer = True
                                print u'点 %s.vtx[%d] 位置信息和MO文件不一致 %s | %s \n' % (obj, i, str(mypos), str(pos))
                    else:
                        isDiffer = True
                        print u'%s 点数量不一致 %d | %d\n' % (obj, vtxNum, vtxDataNum)
                else:
                    isDiffer = True
                    print u'对比文件中不存在此物体: %s\n' % obj.longName()
            print jsonFile        
            if isDiffer:
                print u'点检测不一致,打开Scipt Editor查看详细信息'
                mc.error(u'=== see more information ===')   
            else: 
                print u'============= 点检测通过 ============='
            
        else:
            if tf.type in ['mo']:
                print u'=== 这是一个MO文件，不需要做点对比检测 ==='
            else:
                print u'这不是一个前期文件'
                mc.error(u'=== see more information ===') 
    else:
        mc.warning(u'%s 在 rgtxIgnore 文件中存在,不做对比检测。严禁非法豁免操作!' % tf.id)  

def compareAssetInfoTo(compareTo):
    isDiffer = False
    tf = tiFile.tiAssetFile()
    if not tf.rgtxIgnore:

        # jsonFile = tf.txAssetInfoFile if compareTo == 'TX' else tf.rgAssetInfoFile
        # if os.path.exists(jsonFile):
        #     isDiffer = tiBase.compareFile(jsonFile, compareTo)
        # else:
        #     compareFile = None
        #     if compareTo == 'TX':
        #         compareFile = tf.msRenderFile if os.path.exists(tf.msRenderFile) else (tf.txFile if os.path.exists(tf.txFile) else None)
                
        #     else:
        #         compareFile = tf.msAnimFile if os.path.exists(tf.msAnimFile) else (tf.rgFile if os.path.exists(tf.rgFile) else None)


        #     if compareFile:
        #         tiBatchCmd.runMayaBatch(compareFile, 'python(\\"import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.writeAssetInfo(\'%s\')\\")' % compareTo)
        #         isDiffer = tiBase.compareFile(jsonFile, compareTo)
        #     else:
        #         newCompareFile = 'TX' if compareTo == 'TX' else 'AN'
        #         print u'\n=== 无%s文件，现尝试与MO文件作对比 ===\n' % newCompareFile

        #         compareTo = 'MO'
        #         jsonFile = tf.moAssetInfoFile

        #         if os.path.exists(jsonFile):
        #             isDiffer = tiBase.compareFile(jsonFile, compareTo)
        #         else:
        #             compareFile = tf.moFile if os.path.exists(tf.moFile) else None

        #             if not compareFile:
        #                 print u'没有此文件: %s' % tf.moFile
        #                 mc.error(u'====== 无对比文件, 请联系PA ======')
        #             else:
        #                 tiBatchCmd.runMayaBatch(compareFile, 'python(\\"import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.writeAssetInfo(\'%s\')\\")' % compareTo)
        #                 isDiffer = tiBase.compareFile(jsonFile, compareTo)

        jsonFile = tf.moAssetInfoFile
        

        if not os.path.exists(jsonFile):
            
            compareFile = tf.moFile if os.path.exists(tf.moFile) else None

            if not compareFile:
                print u'没有此文件: %s' % tf.moFile
                mc.error(u'=== see more information ===')
            else:
                compareTo = 'MO'
                tiBatchCmd.runMayaBatch(compareFile, 'python(\\"import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.writeAssetInfo(\'%s\')\\")' % compareTo)
        else:

            compareFile = tf.moFile
            mTime = int('%d' % os.path.getmtime(jsonFile))
            compareTime = 1532747604
            if mTime < compareTime:
                print u'=== 文件需更新 %s ===' % jsonFile
                compareTo = 'MO'
                tiBatchCmd.runMayaBatch(compareFile, 'python(\\"import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.writeAssetInfo(\'%s\')\\")' % compareTo)

        isDiffer = tiBase.compareFile(jsonFile, compareTo)
        if isDiffer:
            print u'======本文件和%s文件有出入，请前期和设置协商共同处理。详细信息请打开Script Editor查看======' % 'MO'

            mc.error()
        else:
            print u'====== 对比检测一致 ======'
    else:
        mc.warning(u'%s 在 rgtxIgnore 文件中存在,不做对比检测。严禁非法豁免操作!' % tf.id)


def rgSetupUvs():
    tf = tiFile.tiAssetFile()
    jsonFile = tf.txAssetInfoFile

    if os.path.exists(jsonFile):
        tiBase.assignAssetUvs(jsonFile)
    else:
        txFile = tf.msRenderFile if os.path.exists(tf.msRenderFile) else (tf.txFile if os.path.exists(tf.txFile) else None)
        if txFile:
            tiBatchCmd.runMayaBatch(txFile, 'python(\\"import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.writeAssetInfo(\'TX\')\\")')
            tiBase.assignAssetUvs(jsonFile)
        else: 
            mc.warning(u'=== no tx file , not setup uv ===')


def updateMsAnimUV():
    tf = tiFile.tiAssetFile()
    if tf.type in ['tx']:
        # 如果已上传的ms_anim UV 和TX文件不一致，后台更新UV
        if os.path.exists(tf.rgAssetInfoFile) and os.path.exists(tf.txAssetInfoFile):
            if not tiBase.compareUv(tf.rgAssetInfoFile, tf.txAssetInfoFile):
                msAnim = tf.msAnimFile if os.path.exists(tf.msAnimFile) else None
                if msAnim:
                    tiBatchCmd.runMayaBatch(msAnim, 'python(\\"import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.updateMsAnimFileUvAndCheckin()\\")')


def writeVertexInfo():
    tf = tiFile.tiAssetFile()
    jsonFile = tf.vertexInfoFile
    print tf.type
    if tf.type in ['mo']:
        tiBase.writeVertexInfo(tf.moVertexInfoFile)
        print u'======output mo vertexInfo ======'
    elif tf.type in ['rg', 'ms_anim']:
        tiBase.writeVertexInfo(tf.rgVertexInfoFile)
        print u'======output rg vertexInfo ======'
    elif tf.type in ['tx', 'ms_render']:
        tiBase.writeVertexInfo(tf.txVertexInfoFile)
        print u'======output tx vertexInfo ======'



def writeAssetInfo(assetType):
    print u'======start output AssetInfo ======'
    tf = tiFile.tiAssetFile()
    jsonFile = None

    if assetType == 'MO':
        if tf.type.lower() not in ['mo']:
            mc.error(u'this is not a mo file')
        jsonFile = tf.moAssetInfoFile

    if assetType == 'TX':
        if tf.type.lower() not in ['tx', 'ms_render']:
            mc.error(u'this is not a tx or ms_render file')
        jsonFile = tf.txAssetInfoFile

    if assetType == 'RG':
        if tf.type.lower() not in ['rg', 'ms_anim']:
            mc.error(u'this is note a rg or ms_anim file')
        jsonFile = tf.rgAssetInfoFile

    #if not os.path.exists(os.path.dirname(jsonFile)):
    #    os.makedirs(os.path.dirname(jsonFile))

    #tiBase.writeAssetInfo(jsonFile)
    if jsonFile:
        # tempJson = os.path.join(tempfile.gettempdir(), os.path.basename(jsonFile))
        tiBase.writeAssetInfo(jsonFile)
        # mel.eval("zwSysFile \"move\" \"%s\" \"%s\" 1" % (tempJson.replace("\\", "/"), jsonFile.replace("\\", "/")))
        if assetType == 'TX':
            tiBase.exportMaterials(tf.assetInfoMaterialFile)
        print u'======AssetInfo output finished======'
    else:
        mc.error(u'========= assetType: %s illegal ========='  % assetType)


def updateMsAnimFileUvAndCheckin():
    rgSetupUvs()

    tiBatchCmd.checkoutAsset(u'后台更新UV')
    
    # fielName = mc.file(q = True, sn = True, shn = True)
    # temp = os.path.join(tempfile.gettempdir(), fielName)
    # mc.file(rename = temp)
    # mc.file(save=1, force=1)

    # userName = os.environ['USERNAME']
    
    # fileInfo = '1|%s|%s|%s'%('XingJiCheShen1', fielName, userName)
    # checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
    # mel.eval(checkOutCmd)
    # result = mc.idmtProject(checkin = True, description = u'后台更新UV')
    # if result:
    #     print '%s Update Uv and Chekcin Finished' % fielName


def renameSelectObj(name):
    sels = mc.ls(sl = True)

    if len(sels) != 1:
        mc.error(u'请选择一个物体')

    if name == sels[0]:
        mc.error(u'需要修改的名字和当前选择的物体名字相同')
    else:
        if mc.objExists(name):
            mc.error(u'=== 场景中已经存在 %s 物体  ===' % name)

        mc.rename(sels[0], name)

def changeImageFileToDollarPath():
    tiBase.changeImageFileToDollarPath()
def maketx():

    arnoldPath = ''
    if "mtoa" in mc.moduleInfo(listModules = True):
        arnoldPath = "%s/bin" % mc.moduleInfo(path = True, moduleName = "mtoa")
    if not arnoldPath:
        mc.error('-----No Arnold-----')
        
    maketxPath = os.path.normpath(os.path.join(arnoldPath, 'maketx.exe'))

    files = mc.ls(type = 'file') + mc.ls(type = 'aiImage')
    procFiles = []
    for f in files:
        nodeType = mc.nodeType(f)
        attrName = '.fileTextureName' if nodeType == 'file' else '.filename'
        filePath = mc.getAttr(f + attrName)
        fpath = os.path.expandvars(filePath)
        
        if os.path.exists(fpath):
            if nodeType == 'file' and mc.getAttr(f+'.useFrameExtension'):
                procFiles +=tiBase.getSeqFiles(fpath)

            else:
                procFiles.append(fpath)

    for pf in procFiles:
        root, ext = os.path.splitext(pf)

        tmptxFile = root + '.tx'

        if 'mapping_final' not in tmptxFile:
            print tmptxFile
            tempFile = os.path.join(tempfile.gettempdir(), os.path.basename(tmptxFile))
            ######### tempFile = os.path.join(r'd:\xj', os.path.basename(tmptxFile))
            cmd = '%s -o %s -u --oiio --colorconvert sRGB linear %s' % (maketxPath, tempFile, pf)
            ###### print cmd
            os.popen(cmd)

            mel.eval("zwSysFile \"move\" \"%s\" \"%s\" 1" % (tempFile.replace("\\", "/"), tmptxFile.replace("\\", "/")))
        else:
            print u'跳过，不转: %s' % tmptxFile
    print '=== MAKE TX DONE ==='


def maketxUnderPath():
    import os
    arnoldPath = ''
    if "mtoa" in mc.moduleInfo(listModules = True):
        arnoldPath = "%s/bin" % mc.moduleInfo(path = True, moduleName = "mtoa")
    if not arnoldPath:
        mc.error('-----No Arnold-----')
        
    maketxPath = os.path.normpath(os.path.join(arnoldPath, 'maketx.exe'))

    for dd, dirs, files in os.walk(r'L:\Projects\XJCS\Project\sourceimages'):
        
        for f in files:
            if not f.endswith('.tx'):
        
                pf = os.path.normpath(os.path.join(dd, f))

                root, ext = os.path.splitext(pf)

                tmptxFile = root + '.tx'
                print tmptxFile
                
                tempFile = os.path.join(tempfile.gettempdir(), os.path.basename(tmptxFile))
                print tempFile
                cmd = '%s -o %s -u --oiio --colorconvert sRGB linear %s' % (maketxPath, tempFile, pf)
                os.popen(cmd)
                mel.eval("zwSysFile \"move\" \"%s\" \"%s\" 1" % (tempFile.replace("\\", "/"), tmptxFile.replace("\\", "/")))

def layerRGBInfoExport(shader):

    rgbDic = {}


    # shader = mc.ls(sl=1)

    
    if mc.nodeType(shader) not in ['lambert','surfaceShader','aiUtility',u'aiStandard']:
        mc.error(u'===请选中有效材质球===')
    if mc.nodeType(shader) in ['lambert','aiUtility',u'aiStandard']:
        colorInfo = mc.getAttr(shader + '.color')
    if mc.nodeType(shader) == 'surfaceShader':
        colorInfo = mc.getAttr(shader + '.outColor')

    rgbDic['color'] = (colorInfo[0][0], colorInfo[0][1], colorInfo[0][2])
    
    SGNodes = mc.listConnections(shader,d=1,type = 'shadingEngine')

    if not SGNodes:
        mc.error(u'===请选中有效材质球===')

    meshes = mc.sets(SGNodes,q=1)

    meshes = mc.ls(meshes, l = 1)

    objs = []
    for mesh in meshes:
        objs.append(mesh)
    
    rgbDic['objs'] = objs

    return rgbDic

    # openPath = os.path.normpath(serverPath + shotInfo[1])
    # os.startfile(openPath)


def creatRenderLayer(layerName):
    if pm.objExists(layerName):
        if pm.editRenderLayerGlobals(currentRenderLayer = True, q = True) == layerName:
            pm.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        pm.delete(layerName)

    renderLayer = pm.createRenderLayer(pm.ls(sl = True), name = layerName, number = 1, noRecurse = True)
    
    pm.setAttr(renderLayer + '.renderable', True)
    pm.setAttr('defaultRenderLayer.renderable', False)
    pm.editRenderLayerGlobals(currentRenderLayer = renderLayer)
    # pm.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
    return renderLayer




def readRGBInfoTest():

    tf = tiFile.tiAssetFile()
    infoFiles = []
    for i in range(1,5):
        name = 'ID1%d' % i
        fh = tf.rgbInfoFile(name)
        if os.path.exists(fh):
            infoFiles.append({'name': name,'file':fh})

    if infoFiles:
        for f in infoFiles:
            data = tiBase.jsonRead(f['file'])
            objs = []
            mc.select(cl = True)
            for key, val in data.items():

                for obj  in val['objs']:
                    o = obj.split('.f[')[0]
       
                    if o not in objs:
                        mc.select(o, add = True)

                    
                # objs += val['objs']
            # print objs
            # mc.select(objs, r = True)
            creatRenderLayer(f['name'])

            mc.select(cl = True)
            for key, val in data.items():
                shdName = 'Arnold%s' % key
                ArnoldIDCreat(shdName, False)
                sg = mc.listConnections(shdName, s = False, d = True, type = 'shadingEngine')
                if sg:
                    for obj  in val['objs']:
                        mc.sets(obj, e=1, forceElement = sg[0])
    else:
        print u'=== 没有找到 %s 的IDP信息,请先输出 ===' % tf._filename

def rgbInfoExport(id):
    tf = tiFile.tiAssetFile()
    colors = {}
    shader = mc.ls(mat=1)

    infoValid = False
    for shade in shader:
        if shade!='particleCloud1' and shade!='lambert1' and shade!='shaderGlow1':
            if('IdpR' in shade):
                colors['IdpR'] = layerRGBInfoExport(shade)
                infoValid = True if colors['IdpR']['objs'] else infoValid
            elif('IdpG' in shade):
                colors['IdpG'] = layerRGBInfoExport(shade)
                infoValid = True if colors['IdpG']['objs'] else infoValid
            elif('IdpB' in shade):
                colors['IdpB'] = layerRGBInfoExport(shade)  
                infoValid = True if colors['IdpB']['objs'] else infoValid                             
            elif('IdpM' in shade):
                colors['IdpM'] = layerRGBInfoExport(shade)  
                infoValid = True if colors['IdpM']['objs'] else infoValid           
            elif('IdpY' in shade):
                colors['IdpY'] = layerRGBInfoExport(shade) 
                infoValid = True if colors['IdpY']['objs'] else infoValid              
            elif('IdpC' in shade):
                colors['IdpC'] = layerRGBInfoExport(shade) 
                infoValid = True if colors['IdpC']['objs'] else infoValid             
            elif('IdpK' in shade):
                colors['IdpK'] = layerRGBInfoExport(shade)
                infoValid = True if colors['IdpK']['objs'] else infoValid
            elif('IdpA' in shade):
                colors['IdpA'] = layerRGBInfoExport(shade)
                infoValid = True if colors['IdpA']['objs'] else infoValid

    if colors and infoValid:
        content = json.dumps(colors)
        # print content

        path = tf.rgbInfoFile(id.upper())
        tiBase.writeFile(content, path)
        print path
        print(u'========[%s]_[输出]完毕！！！========' % id)
    else:
        print u'=== 文件中没有任何IDP信息，没有输出 ==='



def ArnoldIDCreat(idpShader, assignObjs = True):
        
        sels=mc.ls(sl=True)

        if mc.objExists(idpShader)==0:
            mc.shadingNode('aiStandard', asShader=True,n=idpShader)
        idpSG=idpShader+'SG'
        if mc.objExists(idpSG)==0:
            mc.sets(renderable=1,noSurfaceShader=1,em=1,n=idpSG)
            mc.select(cl = True)
        cons=mc.listConnections('%s.outColor' % idpShader)
        if cons!=None:
            #print 'sss'
            if(cons[0]!=idpSG):
                mc.disconnectAttr(('%s.outColor' % idpShader), ('%s.surfaceShader' % cons[0]))
                mc.connectAttr(('%s.outColor' % idpShader),('%s.surfaceShader' % idpSG))
        else:
            mc.connectAttr(('%s.outColor' % idpShader),('%s.surfaceShader' % idpSG))
        #mc.setAttr((idpShader+".shadeMode"),2 )
        #mc.setAttr((idpShader+".colorMode"),0 )

        mc.setAttr((idpShader+".FresnelAffectDiff"),0 )
        mc.setAttr((idpShader+".Kd"),1 )
        if(idpShader=='ArnoldIdpR'):
            mc.setAttr((idpShader+'.color'),1,0,0)
            mc.setAttr((idpShader+".aiEnableMatte"),1 )
            mc.setAttr((idpShader+".aiMatteColor"),1,0,0 )
            mc.setAttr((idpShader+".aiMatteColorA"),0 )
            #mc.setAttr((idpShader+'.hardwareColor'),1,0,0)
        elif(idpShader=='ArnoldIdpG'):
            mc.setAttr((idpShader+'.color'),0,1,0)
            mc.setAttr((idpShader+".aiEnableMatte"),1 )
            mc.setAttr((idpShader+".aiMatteColor"),0,1,0 )
            mc.setAttr((idpShader+".aiMatteColorA"),0 )
            #mc.setAttr((idpShader+'.hardwareColor'),0,1,0)
        elif(idpShader=='ArnoldIdpB'):
            mc.setAttr((idpShader+'.color'),0,0,1)
            mc.setAttr((idpShader+".aiEnableMatte"),1 )
            mc.setAttr((idpShader+".aiMatteColor"),0,0,1 )
            mc.setAttr((idpShader+".aiMatteColorA"),0 )
            #mc.setAttr((idpShader+'.hardwareColor'),0,0,1)
        elif(idpShader=='ArnoldIdpM'):
            mc.setAttr((idpShader+'.color'),0,0,0)
            mc.setAttr((idpShader+".aiEnableMatte"),1 )
            mc.setAttr((idpShader+".aiMatteColor"),0,0,0 )
            mc.setAttr((idpShader+".aiMatteColorA"),0 )
            #mc.setAttr((idpShader+'.hardwareColor'),0,0,0)
        elif(idpShader=='ArnoldIdpA'):
            mc.setAttr((idpShader+'.color'),1,1,1)
            mc.setAttr((idpShader+'.opacity'),1,1,1)
            mc.setAttr((idpShader+".aiEnableMatte"),1 )
            mc.setAttr((idpShader+".aiMatteColor"),0,0,0 )
            mc.setAttr((idpShader+".aiMatteColorA"),1 )
            #mc.setAttr((idpShader+'.hardwareColor'),0,0,0)
        elif(idpShader=='ArnoldIdpY'):
            mc.setAttr((idpShader+'.color'),1,1,0)
            #mc.setAttr((idpShader+'.hardwareColor'),1,1,0)
        elif(idpShader=='ArnoldIdpC'):
            mc.setAttr((idpShader+'.color'),0,1,1)
            #mc.setAttr((idpShader+'.hardwareColor'),0,1,1)
        elif(idpShader=='ArnoldIdpK'):
            mc.setAttr((idpShader+'.color'),1,0,1)
            #mc.setAttr((idpShader+'.hardwareColor'),1,0,1)
        else:
            print u'请正确输入IDP类型'
        
        if assignObjs:
            if sels:
                mc.select(sels, r = True)
                try:
                    mc.sets(e = 1 , forceElement = idpSG)
                    # mc.sets(e = 1 , forceElement = idpSG)
                    # mc.sets(e = 1 , forceElement = idpSG)
                    # mc.hyperShade(assign=idpSG)
                    # mc.hyperShade(assign=idpSG)
                    # mc.hyperShade(assign=idpSG)
                except:
                    print sels
                    mc.warning(u'===有物体无法赋予材质===')
            else:
                print u'=== 请先选择物体 ==='



def fixedSkinClusterPrecision():
    objs = tiBase.getObjsUnderModel()
    joints = []
    for obj in objs:
        skinClusters = pm.listConnections(obj.getShape(), s = True, d = False, type = 'skinCluster')
        for skinCluster in skinClusters:
            jnts = pm.listConnections(skinCluster, s = True, d = False, type = 'joint')
            joints += jnts

    joints = list(set(joints))
    topNode = pm.PyNode('MASTER')
    modelNode = pm.PyNode('MODEL')

    for jnt in joints:
        nodeNme = jnt.name() + '_multMatrix'
        if not pm.objExists(nodeNme):
            pm.createNode('multMatrix', name = nodeNme)
        multMatrixNode = pm.PyNode(nodeNme)
        jnt.worldMatrix >> multMatrixNode.matrixIn[0]

        topNode.worldInverseMatrix >> multMatrixNode.matrixIn[1]

        skinClusters = pm.listConnections(jnt + '.worldMatrix', s = False, d = True, p = True, type = 'skinCluster')
        for skinMatrix in skinClusters:
            multMatrixNode.matrixSum >> skinMatrix
            print u'=== %s -> %s finished setup ===' % (multMatrixNode.name(), skinMatrix.name())
    

    topNode.translate >> modelNode.translate
    topNode.rotate >> modelNode.rotate
    topNode.scale >> modelNode.scale
    
    x = topNode.tx.get()
    topNode.tx.set(99999)
    topNode.tx.set(x)
    print u'=== ok ==='
        
def zmUpdateScript():
    import compileall
    import os
    import shutil
    path = r'E:\LocalDevelope\GDC_Repository\idmt\maya\titanium'
    dst = r'L:\Projects\XJCS\Project\data\OEM\python\idmt\maya\titanium'
    syncDst = r'\\idmt-fileq\XJCS_OEM\python\idmt\maya\titanium'
    compileall.compile_dir(path)
    # compileall.compile_dir(r'E:\LocalDevelope\OEM\python\idmt\maya')
    for root, dirs, files in os.walk(path, topdown=False):
        for f in files:
            
            ff = os.path.normpath(os.path.join(root, f))
            name,ext =  os.path.splitext(ff)
            if ext == '.pyc':
                syncFile = os.path.join(syncDst, f)
               
                shutil.copyfile(ff, syncFile)
                print 'copy %s -> %s' % (ff, syncFile)

                dd = os.path.normpath(os.path.join(dst, f))
                shutil.move(ff, dd)
                print 'cut %s -> %s' % (ff, dd)
      
'''
import idmt
anim = idmt.pipeline.db.GetAnimByFilename("xj_101_002_007")
assets = anim.GetAssetNameInAnim()
if assets:
    for asset in assets:
        print asset.asset_name


import maya.cmds as cmds
import idmt
s = cmds.idmtService("GetAssetNameInEpisode",  "XingJiCheShen1|xj101")
if s:
    buf = s.split('|')
    for i in range(0, len(buf), 5):
        asset = idmt.pipeline.project.asset()
        asset.asset_id = int(buf[i])
        asset.asset_type = buf[i+1]
        asset.asset_name = buf[i+2]
        asset.asset_sep = buf[i+3]
        asset.code = buf[i+4]
        print asset.asset_name
'''

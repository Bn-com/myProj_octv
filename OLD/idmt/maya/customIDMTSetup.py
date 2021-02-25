# -*- coding: utf-8 -*-

# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Maya启动的时候会运行My Documents里面的userSetup.py、userSetup.mel，我们可以在这时候来设置IDMT的工作环境。
由于userSetup是存放在本机的，不便于频繁修改，所以我们的userSetup唯一做的就是调用网上的customIDMTSetup函数，任何修改，都在网上的customIDMTSetup函数进行。
userSetup.py -> idmt.maya.customIDMTSetup
userSetup.mel -> customIDMTSetup.mel
相关参考：
http://doc.idmt.com.cn/mayadoc/Maya2011/en_US/files/Python_Python_in_Maya.htm
http://doc.idmt.com.cn/mayadoc/Maya2011/en_US/files/PC_Run_MEL_commands_whenever_Maya_starts_up.htm
'''
__author__    = 'huangzhongwei@idmt.com.cn'
__date__    = '2010-12-02'



import ctypes
import datetime
import idmt.maya.path
import maya.cmds
import maya.mel
import maya.OpenMaya
import maya.utils
import os
import re
import shutil
import sys

def setRenderTex(computername = None):
    MAYAMAN_TEX_CACHE = 'renderTex'

    if computername == None:
        computername = os.getenv('COMPUTERNAME')
    if re.compile(r'^renderg', re.IGNORECASE).search(computername) != None:
        MAYAMAN_TEX_CACHE = 'texMirrow1'
    elif re.compile(r'^renderi', re.IGNORECASE).search(computername) != None:
        MAYAMAN_TEX_CACHE = 'texMirrow2'
    elif re.compile(r'^renderf', re.IGNORECASE).search(computername) != None:
        MAYAMAN_TEX_CACHE = 'texMirrow3'
    elif re.compile(r'^a(\d{3})-\d{2}$', re.IGNORECASE).search(computername) != None:
        m = re.compile(r'^a(\d{3})-\d{2}$', re.IGNORECASE).search(computername)
        machine = int(m.group(1))
        if machine < 20:
            MAYAMAN_TEX_CACHE = 'texMirrow5'
        elif machine < 40:
            MAYAMAN_TEX_CACHE = 'texMirrow6'
        elif machine < 60:
            MAYAMAN_TEX_CACHE = 'texMirrow7'
        elif machine < 65:
            MAYAMAN_TEX_CACHE = 'texMirrow6'
        elif machine < 70:
            MAYAMAN_TEX_CACHE = 'texMirrow7'
        else:
            MAYAMAN_TEX_CACHE = 'texMirrow7'
    else:
        MAYAMAN_TEX_CACHE = 'texMirrow9'

    MAYAMAN_TEX_CACHE = os.path.join(r'\\file-cluster\GDC\Netrender\Scenes', MAYAMAN_TEX_CACHE)
    
    return MAYAMAN_TEX_CACHE

def InitPyQt():
    version = maya.cmds.about(version = True)
    m = re.search(r'2008|2009|2010', version)
    if m != None:
        path = 'D:/Alias/MAYA' + m.group(0)
        if maya.cmds.about(is64 = True):
            path = path + 'x64'
        path = path + '/devkit/other/PyQtScripts/qt'
        if not path in sys.path:
            sys.path.append(path)
        if m.group(0) == '2010':
            path = os.getenv('PATH')
            if re.search('32 bit', sys.version) == None:
                path = '//file-cluster/GDC/Resource/Support/Python/%s-x64/Lib/site-packages/PyQt4/bin;%s' % (sys.winver, path)
            else:
                path = '//file-cluster/GDC/Resource/Support/Maya/projects/MayaTheBee/_RD/studio100/tools/utils/pylib/PySide/bin;%s' % (path)
            os.environ['PATH'] = path
    #import sip
    #sip.setapi('QString', 2)
    #sip.setapi('QVariant', 2)
    path = r'\\file-cluster\GDC\Resource\Support\Python\%s%s\Lib\site-packages\PyQt4\plugins' % (sys.winver, '-x64' if re.search('32 bit', sys.version) == None else '')
    import PyQt4.QtGui
    PyQt4.QtGui.QApplication.addLibraryPath(path)

def InitPywin32():
    if sys.winver == '2.7':
        return
    path = os.getenv('PATH')
    if re.search('32 bit', sys.version) == None:
        path = '//file-cluster/GDC/Resource/Support/Python/%s-x64/Lib/site-packages/pywin32_system32;%s' % (sys.winver, path)
    else:
        path = '//file-cluster/GDC/Resource/Support/Python/%s/Lib/site-packages/pywin32_system32;%s' % (sys.winver, path)
    os.environ['PATH'] = path

def BeforeSaveCheck(retCode, clientData):
    ctypes.cast(long(retCode), ctypes.POINTER(ctypes.c_ubyte)).contents.value = True

    try:
        if not maya.cmds.about(batch = True) and re.search(r'^vv_.*_(animation|an)[_\.]', sceneName, re.IGNORECASE) != None:
            if not maya.cmds.pluginInfo("stereoCamera", query = True, loaded = True):
                maya.cmds.loadPlugin("stereoCamera", quiet = True)

            from maya.app.stereo import stereoCameraRig

            cam = []
            cameras = maya.cmds.listCameras(perspective = True)
            for i in range(len(cameras)):
                if maya.cmds.reference(cameras[i], isNodeReferenced = True):
                    continue
                if maya.cmds.camera(cameras[i], query = True, startupCamera = True):
                    continue
                if stereoCameraRig.rigRoot(cameras[i]) == "":
                    cam.append(cameras[i])
            cam.extend(stereoCameraRig.listRigs())
            msg = "";
            if len(cam) > 1:
                msg = u"只允许有一个摄像机：\n\n%s\n\n点“Cancel”取消存盘，返回检查；点“Ignore”忽略警告，继续存盘" % u"\n".join(cam)
            elif len(cam) == 1:
                attrs = ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ", "scaleX", "scaleY", "scaleZ", "horizontalFilmAperture", "verticalFilmAperture", "focalLength", "lensSqueezeRatio", "fStop", "focusDistance", "shutterAngle", "centerOfInterest"]#, "stereo", "interaxialSeparation", "zeroParallax", "toeInAdjust", "filmOffsetRightCam", "filmOffsetLeftCam"]
                for i in range(len(attrs)):
                    if maya.cmds.objExists("%s.%s" % (cam[0], attrs[i])):
                        if not maya.cmds.getAttr("%s.%s" % (cam[0], attrs[i]), lock = True):
                            msg = u"请锁定摄像机位置及属性：\n\n%s\n\n点“Cancel”取消存盘，返回检查；点“Ignore”忽略警告，继续存盘" % u"\n".join(cam)
                            break
            if msg != "":
                rs = maya.cmds.confirmDialog(icon = "critical", message = msg, button = ["Cancel", "Ignore"], defaultButton = "Cancel", cancelButton = "Cancel", dismissString = "Cancel")
                if rs == "Cancel":
                    ctypes.cast(long(retCode), ctypes.POINTER(ctypes.c_ubyte)).contents.value = False
                    maya.cmds.select(cam)
    except:
        pass


def MiniTiger():
    attrs = [("defaultArnoldRenderOptions.use_sample_clamp", 0),
             ("defaultArnoldRenderOptions.use_existing_tiled_textures", 1),
             ("defaultArnoldRenderOptions.procedural_searchpath", "\\\\file-cluster\\GDC\\Resource\\Development\\Maya\\GDC\\3partPlugin\\2014\\Yeti1.3.5Maya2014\\bin"),
             ("defaultArnoldDriver.ai_translator", "exr"),
             ("defaultRenderGlobals.imageFormat", 51),
             ("defaultRenderGlobals.imfkey", "exr"),
             ("defaultArnoldDriver.exrCompression", 2),
             ("defaultArnoldDriver.halfPrecision", 1),
             ("defaultArnoldDriver.autocrop", 1),
             ("defaultArnoldDriver.append", 0)]
    for (attr, value) in attrs:
        idmt.maya.cmds.setAttr(attr, value)
    sceneName = maya.cmds.file(query=True, sceneName = True, shortName = True)
    if re.search(r'^mi_.*_(sd|fs|ef|lr)[_\.]', sceneName, re.IGNORECASE) != None:
        import idmt.maya.commonPerform.renderLayers.zb_renderLayer_mi as mirl
        reload(mirl)
        ins_proc = mirl.zb_renderLayer_mi()
        ins_proc.mi_set_Rnd_parameter01(u'c001002MiniTiger')

def AfterOpen(clientData):
    try:
        sceneName = maya.cmds.file(query=True, sceneName = True, shortName = True)
        # if re.search(r'^mi_', sceneName, re.IGNORECASE) != None:
        #     MiniTiger()
    except:
        pass

def BeforeSave(clientData):
    try:
        nodes = maya.cmds.ls(type = "script")
        if nodes:
            for node in nodes:
                if "GDC_BODYRIG2009_SCRIPTNODE" in node:
                    if not maya.cmds.reference(node, isNodeReferenced = True):
                        maya.cmds.setAttr('%s.scriptType' % node, 0)
                        maya.cmds.delete(node)
                    else:
                        if maya.cmds.getAttr('%s.scriptType' % node):
                            maya.cmds.setAttr('%s.scriptType' % node, 0)
    except:
        pass

    try:
        sceneName = maya.cmds.file(query=True, sceneName = True, shortName = True)
        # if re.search(r'^mi_', sceneName, re.IGNORECASE) != None:
        #      MiniTiger()
    except:
        pass

def BeforeOpenCheck(retCode, file, clientData):
    ctypes.cast(long(retCode), ctypes.POINTER(ctypes.c_ubyte)).contents.value = True

    try:
        if not maya.cmds.about(batch = True):
            sceneName = file.rawFullName()
            anim_file = re.compile('.*/Projects/VickytheViking/Project/scenes/02_episodes/', re.IGNORECASE).sub('', sceneName)
            if anim_file != sceneName:
                anim_file = anim_file.replace("/", "\\")
                progress = maya.cmds.idmtService('GetProgress', anim_file)
                if progress != "" and progress != "100":
                    msg = u"请注意：本文件的进度只有 %s%% ，客户还没有通过！\n\n点“Cancel”取消打开操作；点“Ignore”忽略警告，继续打开" % progress
                    rs = maya.cmds.confirmDialog(icon = "warning", message = msg, button = ["Cancel", "Ignore"], defaultButton = "Cancel", cancelButton = "Cancel", dismissString = "Cancel")
                    if rs == "Cancel":
                        ctypes.cast(long(retCode), ctypes.POINTER(ctypes.c_ubyte)).contents.value = False
    except:
        pass

def BeforeCreateReference(retCode, file, clientData):
    ctypes.cast(long(retCode), ctypes.POINTER(ctypes.c_ubyte)).contents.value = True
    try:
        pathOld = file.expandedFullName()    # 得到原来的路径
        if re.compile(r'[/\\](DiveollyDive4|VickyTheViking)[/\\].*\.ma$', re.IGNORECASE).search(pathOld) != None:
            pathNew = re.compile(r'\.ma$', re.IGNORECASE).sub(r'.mb', pathOld)
            if os.path.isfile(pathNew):
                pathNew = idmt.maya.path.GetDollarPath(pathNew)
                print "%s -> %s" % (pathOld, pathNew)
                file.setRawFullName(pathNew)
        elif re.compile(r'^//file-cluster/GDC/Projects/Lion/', re.IGNORECASE).search(pathOld) != None:
            pathNew = re.compile(r'^//file-cluster/GDC/', re.IGNORECASE).sub('L:/', pathOld)
            if os.path.isfile(pathNew):
                print "%s -> %s" % (pathOld, pathNew)
                file.setRawFullName(pathNew)
        elif not os.path.isfile(pathOld):
            pathNew = pathOld
            if re.compile(r'[/\\]HeroFactory[/\\]', re.IGNORECASE).search(pathOld) != None:
                pathNew = re.compile(r'([/\\])characters([/\\])', re.IGNORECASE).sub(r'\g<1>Character\g<2>', pathNew)
                if re.compile(r'[/\\](BubbleCar|bubbleTaxi|bulkDrillMech|citizencar|drill|dropshipLarge|evoDropship|evoSpiderMech|evoTurretWalker|evoXMech|furnoFireMech|metroTrain|REB|REBbox|rockaCrawlerMech|rockaStealthMech|stormerFreezerMech|surgeCombinerMech|truck)[/\\]', re.IGNORECASE).search(pathNew) != None:
                    pathNew = re.compile(r'([/\\])props([/\\])', re.IGNORECASE).sub(r'\g<1>Vehicle\g<2>', pathNew)
                else:
                    pathNew = re.compile(r'([/\\])props([/\\])', re.IGNORECASE).sub(r'\g<1>Prop\g<2>', pathNew)
                pathNew = re.compile(r'([/\\])sets([/\\])', re.IGNORECASE).sub(r'\g<1>Environment\g<2>', pathNew)
            elif re.compile(r'[/\\](CAL_RSYNC|cal_maya)[/\\]', re.IGNORECASE).search(pathOld) != None:
                from idmt.maya.Calimero import sk_calimeroProjectTools
                reload(sk_calimeroProjectTools);
                pathNew = sk_calimeroProjectTools.sk_clProjectTools().calimeroPathToGDC(pathOld)
            elif re.compile(r'[/\\](Calimero|ZoomWhiteDolphin|Strawberry|ShunLiu)[/\\]', re.IGNORECASE).search(pathOld) != None:
                pathNew = re.compile(r'.*([/\\](Calimero|ZoomWhiteDolphin|Strawberry|ShunLiu)[/\\].*)', re.IGNORECASE).sub(r'//file-cluster/GDC/Projects\g<1>', pathNew)
                pathNew = re.compile(r'_(c|ng)_h_ms_anim\.', re.IGNORECASE).sub('_h_ms_anim.', pathNew)
            elif re.compile(r'^L:', re.IGNORECASE).search(pathOld) != None:
                pathNew = re.compile(r'^L:', re.IGNORECASE).sub('//file-cluster/GDC', pathOld)
            elif re.compile(r'^tf_', re.IGNORECASE).search(file.rawName()) != None:
                pathNew = re.compile(r'.*/scenes/', re.IGNORECASE).sub('//file-cluster/GDC/Projects/ToothFairies/Project/scenes/', pathOld)
            if os.path.isfile(pathNew):
                print "%s -> %s" % (pathOld, pathNew)
                pathNew = idmt.maya.path.GetDollarPath(pathNew)
                file.setRawFullName(pathNew)
            elif maya.OpenMaya.MGlobal.mayaState() == maya.OpenMaya.MGlobal.kBatch:
                os.environ['REFERENCE_FILE_NOT_FOUND'] = "REFERENCE_FILE_NOT_FOUND"
                #if maya.OpenMaya.MGlobal.apiVersion() < 201400:
                #    maya.OpenMaya.MGlobal.displayError(u'Reference file not found. %s' % (pathOld))
                #    import time
                #    time.sleep(5.0)
                #    os._exit(-1)
        else:
            pathOld = file.rawFullName()
            pathNew = idmt.maya.path.GetDollarPath(pathOld)
            if pathNew != pathOld:
                print "%s -> %s" % (pathOld, pathNew)
                file.setRawFullName(pathNew)
    except:
        pass

def AfterSave(clientData):
    maya.cmds.idmtService("StartTask", "%s|%s" % (maya.OpenMaya.MFileIO.currentFile(), os.getenv('USERNAME')))
    pass

def BeforeImport(retCode, file, clientData):
    ctypes.cast(long(retCode), ctypes.POINTER(ctypes.c_ubyte)).contents.value = True
    path = file.expandedFullName()
    if re.search(r'[/\\]Projects([/\\]DomesticProject)?[/\\][^/\\]+[/\\]Project[/\\]scenes[/\\]', path, re.IGNORECASE) == None:
        s = "%s\t%s\t%s\t%s\t%s\r\n" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), os.getenv('COMPUTERNAME'), os.getenv('USERNAME'), maya.OpenMaya.MFileIO.currentFile(), path)
        maya.cmds.idmtService("StartTask", "%s|%s" % (maya.OpenMaya.MFileIO.currentFile(), os.getenv('USERNAME')));
        try:
            f = open(r"Z:\Netrender\Maya_Odd\N335\import.txt", "a")
            f.write(s)
            f.close()
        except:
            pass

def customIDMTSetup():
    '''Maya启动的时候设置IDMT的工作环境'''

    # 登录时关闭网渲服务
    username = os.getenv('USERNAME')
    #if username.lower() != "musterservice":
    #    #os.system("\"\"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\lsrunase.exe\" /user:musterservice /domain:product /password:41pknfMA+qrL /command:\"net stop Muster_Renderclient\" /runpath:\"c:\\\"\"")
    #    maya.mel.eval("system(\"shell \\\"\\\"C:\\\\ProgramData\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\Startup\\\\lsrunase.exe\\\" /user:musterservice /domain:product /password:41pknfMA+qrL /command:\\\"net stop Muster_Renderclient\\\" /runpath:\\\"c:\\\\\\\"\\\"\")")

    if sys.version_info[0] + sys.version_info[1] / 10.0 >= 2.6:
        sys.dont_write_bytecode = True

    if os.path.isdir('L:/Projects'):
        os.environ['L_PROJECTS'] = 'L:/Projects'
    else:
        os.environ['L_PROJECTS'] = '//file-cluster/GDC/Projects'

    # 自动重新配置
    src = r'\\file-cluster\GDC\Resource\Support\Maya\userSetup.py'
    dst = maya.cmds.internalVar(userScriptDir=True) + 'userSetup.py'
    #shutil.copyfile(src, dst)

    path = re.sub(r'[/\\]$', '', maya.cmds.internalVar(userScriptDir = True))
    if not path in sys.path:
        maya.utils.executeDeferred('import sys; sys.path.append(\'' + path + '\')')

    maya.utils.executeDeferred('import sys; sys.path.append(r\'\\\\file-cluster\\GDC\\Projects\\Calimero\\Common_Sync\\CAL_MAYA\\2013\\python\\teamto\'); sys.path.append(r\'\\\\file-cluster\\GDC\\Projects\\Calimero\\Common_Sync\\CAL_MAYA\\2013\\python\\alphanim\')')

    path = '//file-cluster/GDC/Resource/Support/Maya/Python'
    if not path in sys.path:
        sys.path.append(path)

        riggingToolPythonPath='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/edward/python'
        if not riggingToolPythonPath in sys.path:
                sys.path.append(riggingToolPythonPath)

    # hotOcean for 2012-x64
    version = maya.mel.eval('zwAboutVersion')
    x64 = ''
    if maya.cmds.about(is64 = True):
        x64 = '-x64'
    os.environ['PATH'] = '//file-cluster/GDC/Resource/Support/Maya/%s%s/bin;%s' % (version, x64, os.getenv('PATH'))

    # MtoA for 2012-x64
    if version == '2012' and maya.cmds.about(is64 = True):
        #os.environ['ARNOLD_PLUGIN_PATH'] = '//file-cluster/GDC/Resource/Support/Maya/2012-x64/modules/MtoA-0.14.1-win64-2012/shaders'
        #os.environ['MAYA_RENDER_DESC_PATH'] = '//file-cluster/GDC/Resource/Support/Maya/2012-x64/modules/MtoA-0.14.1-win64-2012'
        #os.environ['PATH'] = '%s;//file-cluster/GDC/Resource/Support/Maya/2012-x64/modules/MtoA-0.14.1-win64-2012/bin' % os.getenv('PATH')
        os.environ['ARNOLD_PLUGIN_PATH'] = '//file-cluster/gdc/Resource/Support/Maya/2012-x64/modules/solidangle1.0/mtoadeploy/2012/shaders'
        os.environ['MAYA_RENDER_DESC_PATH'] = '//file-cluster/gdc/Resource/Support/Maya/2012-x64/modules/solidangle1.0/mtoadeploy/2012'
        os.environ['PATH'] = '//file-cluster/gdc/Resource/Support/Maya/2012-x64/modules/solidangle1.0/mtoadeploy/2012/bin;%s' % os.getenv('PATH')
        os.environ['MTOA_EXTENSIONS_PATH'] = '//file-cluster/gdc/Resource/Support/Maya/2012-x64/modules/solidangle1.0/mtoadeploy/2012/extensions'

    try:
        InitPyQt()
    except:
        pass

    InitPywin32()

    if maya.cmds.about(apiVersion = True) >= 201400:
        if 'GDC_PlugIns' in maya.cmds.moduleInfo(listModules = True):
            maya.mel.eval('evalDeferred -lowestPriority "if (!`pluginInfo -q -loaded -name \\\"GDC_Plugin_Init\\\"`) loadPlugin \\\"GDC_Plugin_Init\\\""')

    # Z:
    #if not os.path.isdir('Z:'):
    #    try:
    #        import win32net
    #        win32net.NetUseAdd(None, 1, {'remote' : r'\\file-cluster\GDC', 'local' : 'Z:'})
    #        print(r'SUCCESS: net use Z: \\file-cluster\GDC')
    #    except:
    #        print(r'FAIL: net use Z: \\file-cluster\GDC')
    #        pass
    #else:
    #    print('Z: exists!')

    ## RenderMan根mayaman有冲突，去掉
    #os.environ['MAYA_PLUG_IN_PATH'] = re.sub(r';//file-cluster/GDC/Resource/Support/Maya/2008/modules/RenderMan-Studio-1.0.1-Maya2008/bin', r'', os.getenv('MAYA_PLUG_IN_PATH'))

    ## 2011-x64 mayaman
    #if version == '2011' and maya.cmds.about(is64 = True):
    #    os.environ['MAYA_SCRIPT_PATH'] = os.getenv("MAYA_SCRIPT_PATH") + r';\\file-cluster\GDC\Resource\Support\AnimalLogic\mayaman3.0.07_64\mel'
    #    os.environ['MAYA_PLUG_IN_PATH'] = os.getenv("MAYA_PLUG_IN_PATH") + r';\\file-cluster\GDC\Resource\Support\AnimalLogic\mayaman3.0.07_64\plugins\2011'
    #    os.environ['XBMLANGPATH'] = os.getenv("XBMLANGPATH") + r';\\file-cluster\GDC\Resource\Support\AnimalLogic\mayaman3.0.07_64\mel'
    #    os.environ['PATH'] = '//file-cluster/GDC/Resource/Support/AnimalLogic/mayaman3.0.07_64/bin;' + os.getenv('PATH')
    #if version == '2010' and not maya.cmds.about(is64 = True):
    #    os.environ['MAYA_SCRIPT_PATH'] = os.getenv("MAYA_SCRIPT_PATH") + r';\\file-cluster\GDC\Resource\Support\AnimalLogic\mayaman3.0.07\mel'
    #    os.environ['MAYA_PLUG_IN_PATH'] = os.getenv("MAYA_PLUG_IN_PATH") + r';\\file-cluster\GDC\Resource\Support\AnimalLogic\mayaman3.0.07\plugins\2010'
    #    os.environ['XBMLANGPATH'] = os.getenv("XBMLANGPATH") + r';\\file-cluster\GDC\Resource\Support\AnimalLogic\mayaman3.0.07\mel'
    #    os.environ['PATH'] = '//file-cluster/GDC/Resource/Support/AnimalLogic/mayaman3.0.07/bin;' + os.getenv('PATH')
        
    ## Woodlies 项目插件载入
    #if version == '2011' and not maya.cmds.about(is64 = True):
    #    if not maya.cmds.pluginInfo( 'idmtWoodliesFace',q = True, loaded = True):# Woodlies
    #        maya.cmds.loadPlugin( 'idmtWoodliesFace')    
    #        
    #if version == '2009':
    #    if not maya.cmds.pluginInfo( 'idmtWoodliesFace',q = True, loaded = True):# Woodliesￏￄ﾿
    #        maya.cmds.loadPlugin( 'idmtWoodliesFace')

    if version == '2014' or version == '2016':
        if not maya.cmds.about(batch = True):
            os.environ['idmtOpenFileDebug'] = 'x'
        if (not maya.cmds.about(batch = True)) or (os.getenv('idmtOpenFileDebug') == None):
            import idmt.maya.OpenFileLog
            idmt.maya.OpenFileLog.addCallback()
    if maya.cmds.about(apiVersion = True) >= 201200:
        #maya.OpenMaya.MSceneMessage.addCheckFileCallback(maya.OpenMaya.MSceneMessage.kBeforeOpenCheck, BeforeOpenCheck)
        #maya.OpenMaya.MSceneMessage.addCheckCallback(maya.OpenMaya.MSceneMessage.kBeforeSaveCheck, BeforeSaveCheck)
        maya.OpenMaya.MSceneMessage.addCheckFileCallback(maya.OpenMaya.MSceneMessage.kBeforeCreateReferenceCheck, BeforeCreateReference)
        maya.OpenMaya.MSceneMessage.addCheckFileCallback(maya.OpenMaya.MSceneMessage.kBeforeLoadReferenceCheck, BeforeCreateReference)
        maya.OpenMaya.MSceneMessage.addCallback(maya.OpenMaya.MSceneMessage.kAfterOpen, AfterOpen)
        maya.OpenMaya.MSceneMessage.addCallback(maya.OpenMaya.MSceneMessage.kBeforeSave, BeforeSave)
        maya.OpenMaya.MSceneMessage.addCallback(maya.OpenMaya.MSceneMessage.kAfterSave, AfterSave)
        maya.OpenMaya.MSceneMessage.addCheckFileCallback(maya.OpenMaya.MSceneMessage.kBeforeImportCheck, BeforeImport)

    # Relight
    #path = r'D:\The Bakery\Relight\plugins\maya_mud_export_' + re.search(r'^\d{4}', maya.cmds.about(version = True)).group(0)
    path = r'D:\The Bakery\Relight\plugins\maya_mud_export_%d' % (maya.cmds.about(apiVersion = True) / 100)
    if os.path.isdir(path):
        os.environ['MAYA_SCRIPT_PATH'] = os.getenv("MAYA_SCRIPT_PATH") + r';' + path
        os.environ['MAYA_PLUG_IN_PATH'] = os.getenv("MAYA_PLUG_IN_PATH") + r';' + path

    ## ROMA, 2008
    #pipelineVer = os.getenv("PIPELINE_VERSION", '20111201')
    #os.environ['MC_roma'] = r'\\file-cluster\GDC\Projects\ROMA\PRJ_roma\MC_roma'
    #if version == '2008':    # and os.environ['OFFICE_LOCATION'] == 'shenzhen'
    #    # mayaman
    #    if not maya.cmds.about(is64 = True):
    #        IDMT_MAYAMAN_VERSION = os.getenv('IDMT_MAYAMAN_VERSION')
    #        if IDMT_MAYAMAN_VERSION == None:
    #            IDMT_MAYAMAN_VERSION = '2.0.15'
    #        os.environ['MAYA_SCRIPT_PATH'] = os.getenv("MAYA_SCRIPT_PATH") + r';\\file-cluster\GDC\Resource\Support\AnimalLogic\mayaman%s\mel' % (IDMT_MAYAMAN_VERSION)
    #        os.environ['MAYA_PLUG_IN_PATH'] = os.getenv("MAYA_PLUG_IN_PATH") + r';\\file-cluster\GDC\Resource\Support\AnimalLogic\mayaman%s\plugins\2008' % (IDMT_MAYAMAN_VERSION)
    #        os.environ['XBMLANGPATH'] = os.getenv("XBMLANGPATH") + r';\\file-cluster\GDC\Resource\Support\AnimalLogic\mayaman%s\mel' % (IDMT_MAYAMAN_VERSION)

    #    os.environ['MAYAMAN_TEX_CACHE'] = setRenderTex()

    #    os.environ['PIPELINE_SCRIPTS'] = r'\\file-cluster\GDC\Resource\Support\Maya\modules\rbw_pipeline_%s' % (pipelineVer)
    #    sys.path.append(r'\\file-cluster\GDC\Resource\Support\Maya\modules\rbw_pipeline_%s\RBW\utility' % (pipelineVer))
    #    os.environ['CONTENT_PATH'] = r'\\file-cluster\GDC\Projects\ROMA'
    #    os.environ['PROJECT_PATH'] = r'\\file-cluster\GDC\Projects'
    #    os.environ['ISILON_PATH'] = r'\\Isilon.nas'

    #    import RBW_pipeline as p

    #    str= "\tinit ENVs...."
    #    mainEnvPth= os.getenv("PIPELINE_SCRIPTS")
    #    prjpath=os.getenv("CONTENT_PATH")
    #    if mainEnvPth != None and prjpath != None:
    #        str+="OK, pipeline starts...."
    #        print str
    #        p.setPipeline(mainEnvPth,prjpath)
    #        maya.utils.executeDeferred('import RBW_menus as RBWm\nRBWm.Create("'+mainEnvPth+'")')
    #    else:
    #        print "WARNING!\nyou have to set up the PIPELINE_SCRIPTS and CONTENT_PATH \nenvironents variables\n"

    #    os.environ['MAYA_SCRIPT_PATH'] = r'\\file-cluster\GDC\Resource\Support\Maya\projects\ROMA;' + os.getenv("MAYA_SCRIPT_PATH")

    ## extra
    #for root, dirs, files in os.walk(r'\\file-cluster\GDC\Resource\Support\Maya\extra'):
    #    for folder in dirs:
    #        if folder == "icons":
    #            os.environ['XBMLANGPATH'] = r'%s;%s\%s' % (os.getenv("XBMLANGPATH"), root, folder)
    #        elif folder == "2013":
    #            os.environ['MAYA_SCRIPT_PATH'] = r'%s;%s\%s' % (os.getenv("MAYA_SCRIPT_PATH"), root, folder)
    #        else:
    #            os.environ['MAYA_SCRIPT_PATH'] = r'%s;%s\%s' % (os.getenv("MAYA_SCRIPT_PATH"), root, folder)
    #            os.environ['XBMLANGPATH'] = r'%s;%s\%s' % (os.getenv("XBMLANGPATH"), root, folder)

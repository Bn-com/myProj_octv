# -*- coding: utf-8 -*-
# huangzhongwei@idmt.com.cn

import datetime
import glob
import nuke
import os
import re
import socket
import sys
pyodbcPath = '//file-cluster/GDC/Resource/Development/Maya/GDC/Plug/Python/2.7/Lib/site-packages'
if pyodbcPath not in sys.path:
    sys.path.append(pyodbcPath)
import pyodbc

try:
    import pyUtil3 as pyUtil
except:
    import pyUtil2 as pyUtil
import idmt.pipeline.db
import idmt.pipeline.project


def plexMini():
    path = nuke.root().knob("name").getValue()
    url = 'http://app-server/wa/Plex/Maya/Redirector.aspx?filename=%s&t=%s' % (os.path.basename(path), datetime.datetime.now().strftime('%Y%m%d%H%M'))
    import webbrowser
    webbrowser.open(url)

# ------------------------------------------------------------------------------#
# 新版规划:沈康
# ---------------------------------------------------#
#【核心】【通用】【执行函数】
# ---------------------------------------------------#

# 项目设置
def commonProjectSetting():
    shotInfo = commonGetShotInfo()
    shot = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]

    project = ''
    # shotInfoCheck
    if shotInfo[0] == 'mi':
        project = 'MI'
    if shotInfo[0] == 'sk':
        project = 'SK'
    if shotInfo[0] == 'do4':
        project = 'DODIV'
    if shotInfo[0] == 'do5':
        project = 'DODV'
    if shotInfo[0] == 'zm':
        project = 'ZM'
    if shotInfo[0] == 'cl':
        project = 'CL'
    if shotInfo[0] == 'ddz':
        project = 'DouDiZhu'
    if shotInfo[0] == 'csl':
        project = 'CSL'
        shot = shotInfo[0] + '_' + shotInfo[1].lower() + '_' + shotInfo[2] + '_' + shotInfo[3]
    if shotInfo[0] == 'nj':
        project = 'Ninjago'
        shot = shotInfo[0] + '_' + shotInfo[1].lower() + '_' + shotInfo[2] + '_' + shotInfo[3]
    if shotInfo[0] == 'ice':
        project = 'North'
    if shotInfo[0] == 'LION':
        project = 'LION'
    if shotInfo[0] == 'tf':
        project = 'TF'
        shot = shotInfo[0] + '_' + shotInfo[1].lower() + '_' + shotInfo[2] + '_' + shotInfo[3]

    if not project:
        project = commonGetProjFullName(shotInfo[0])

    # frame
    anim = idmt.pipeline.db.GetAnimByFilename(shot)
    startFrame = anim.frmStart
    endFrame = anim.frmEnd
    fpsFrame = anim.fps

    # settings
    if project == 'MI':
        GT = '2048 858 GT'
        nuke.addFormat(GT)
        nuke.knobDefault('Root.format', GT)
        nuke.root().knob('format').setValue('GT')

    if project == 'GT':
        GT = '1332 720 GT'
        nuke.addFormat(GT)
        nuke.knobDefault('Root.format', GT)
        nuke.root().knob('format').setValue('GT')
        nuke.root().knob('views_colours').setValue(True)

    if project == 'GT2':
        GT = '1332 720 GT'
        nuke.addFormat(GT)
        nuke.knobDefault('Root.format', GT)
        nuke.root().knob('format').setValue('GT')
        nuke.root().knob('views_colours').setValue(True)

    if project == 'OT':
        OT = '1332 720 OT'
        nuke.addFormat(OT)
        nuke.knobDefault('Root.format', OT)
        nuke.root().knob('format').setValue('OT')
        nuke.root().knob('views_colours').setValue(True)

    if project == 'OT2':
        setUpMultiView()
        OT = '1332 720 OT'
        nuke.addFormat(OT)
        nuke.knobDefault('Root.format', OT)
        nuke.root().knob('format').setValue('OT')
        nuke.root().knob('views_colours').setValue(True)

    if project == 'EQ':
        EQ = '2880 800 EQ'
        nuke.addFormat(EQ)
        nuke.knobDefault('Root.format', EQ)
        nuke.root().knob('format').setValue('EQ')
        nuke.root().knob('views_colours').setValue(True)

    if project == 'SK':
        SK = '1280 720 SK'
        nuke.addFormat(SK)
        nuke.knobDefault('Root.format', SK)
        nuke.root().knob('format').setValue('SK')
        nuke.root().knob('views_colours').setValue(True)
        nuke.root().knob('fps').setValue(fpsFrame)
        nuke.root().knob('first_frame').setValue(startFrame)
        nuke.root().knob('last_frame').setValue(endFrame)

    if project == 'CH':
        CH = '3072 1200 CH'
        nuke.addFormat(CH)
        nuke.knobDefault('Root.format', CH)
        nuke.root().knob('format').setValue('CH')
        nuke.root().knob('views_colours').setValue(True)

    if project == 'LION':
        CL = '1280 720 CL'
        nuke.addFormat(CL)
        nuke.knobDefault('Root.format', CL)
        nuke.root().knob('format').setValue('CL')
        nuke.root().knob('views_colours').setValue(True)
        nuke.root().knob('fps').setValue(fpsFrame)
        nuke.root().knob('first_frame').setValue(startFrame)
        nuke.root().knob('last_frame').setValue(endFrame)

    if project == 'DODV':
        nuke.showSettings()
        setUpMultiView()
        #DOD3='1920 1080 DOD3'
        # nuke.addFormat(DOD3)
        #nuke.knobDefault('Root.format',DOD3 )
        DODIV = '2048 1106 DODV'
        nuke.addFormat(DODIV)
        nuke.knobDefault('Root.format', DODIV)
        nuke.root().knob('format').setValue('DODIV')
        nuke.root().knob('views_colours').setValue(True)
        nuke.root().knob('fps').setValue(fpsFrame)
        nuke.root().knob('first_frame').setValue(startFrame)
        nuke.root().knob('last_frame').setValue(endFrame)

    if project == 'ZM':
        ZM = '1920 1080 ZM'
        nuke.addFormat(ZM)
        nuke.knobDefault('Root.format', ZM)
        nuke.root().knob('format').setValue('ZM')
        nuke.root().knob('views_colours').setValue(True)
        nuke.root().knob('fps').setValue(fpsFrame)
        nuke.root().knob('first_frame').setValue(startFrame)
        nuke.root().knob('last_frame').setValue(endFrame)

    if project == 'DouDiZhu':
        DDZ = '1920 1080 DDZ'
        nuke.addFormat(DDZ)
        nuke.knobDefault('Root.format', DDZ)
        nuke.root().knob('format').setValue('DDZ')
        nuke.root().knob('views_colours').setValue(True)
        nuke.root().knob('fps').setValue(fpsFrame)
        nuke.root().knob('first_frame').setValue(startFrame)
        nuke.root().knob('last_frame').setValue(endFrame)

    if project == 'CL':
        CL = '1920 1080 CL'
        nuke.addFormat(CL)
        nuke.knobDefault('Root.format', CL)
        nuke.root().knob('format').setValue('CL')
        nuke.root().knob('views_colours').setValue(True)
        nuke.root().knob('fps').setValue(fpsFrame)
        nuke.root().knob('first_frame').setValue(startFrame)
        nuke.root().knob('last_frame').setValue(endFrame)

    if project == 'CSL':
        CSL = '1280 720 CSL'
        nuke.addFormat(CSL)
        nuke.knobDefault('Root.format', CSL)
        nuke.root().knob('format').setValue('CSL')
        nuke.root().knob('views_colours').setValue(True)
        nuke.root().knob('fps').setValue(fpsFrame)
        nuke.root().knob('first_frame').setValue(startFrame)
        nuke.root().knob('last_frame').setValue(endFrame)
    if project == 'TF':
        TF = '1920 1080 TF'
        nuke.addFormat(TF)
        nuke.knobDefault('Root.format', TF)
        nuke.root().knob('format').setValue('TF')
        nuke.root().knob('views_colours').setValue(True)
        nuke.root().knob('fps').setValue(fpsFrame)
        nuke.root().knob('first_frame').setValue(startFrame)
        nuke.root().knob('last_frame').setValue(endFrame)

    if project == 'Ninjago':
        Ninjago = '1280 720 Ninjago'
        nuke.addFormat(Ninjago)
        nuke.knobDefault('Root.format', Ninjago)
        nuke.root().knob('format').setValue('Ninjago')
        nuke.root().knob('views_colours').setValue(True)
        nuke.root().knob('fps').setValue(fpsFrame)
        nuke.root().knob('first_frame').setValue(startFrame)
        nuke.root().knob('last_frame').setValue(endFrame)

        nuke.root().knob('monitorLut').setValue('sRGB')
        nuke.root().knob('int8Lut').setValue('sRGB')
        nuke.root().knob('int16Lut').setValue('sRGB')
        nuke.root().knob('logLut').setValue('Cineon')
        nuke.root().knob('floatLut').setValue('linear')


    if project == 'North':
        North = '1998 1080 North'
        nuke.addFormat(North)
        nuke.knobDefault('Root.format', North)
        nuke.root().knob('format').setValue('North')
        nuke.root().knob('views_colours').setValue(True)
        nuke.root().knob('fps').setValue(fpsFrame)
        nuke.root().knob('first_frame').setValue(startFrame)
        nuke.root().knob('last_frame').setValue(endFrame)
        
        nuke.root().knob('monitorLut').setValue('linear')
        nuke.root().knob('int8Lut').setValue('linear')
        nuke.root().knob('int16Lut').setValue('linear')
        nuke.root().knob('logLut').setValue('linear')
        nuke.root().knob('floatLut').setValue('linear')        

        v = nuke.toNode('Viewer1')
        v['viewerProcess'].setValue(0)

# 项目全称
def commonGetProjFullName(projSimp):
    import pyUtil3 as pyUtil
    s = pyUtil.idmtService('GetProjectByFile', projSimp)
    buf = [0,0]
    if s != '':
        buf = s.split('|')
    if not buf[1]:
        nuke.message(u'Please check file name,no project info on server')
        raise
    return buf[1]

# 创建目录
def commonCreateFolder(folder):
    path = folder
    if path[-1] not in ['/','\\']:
        path += '/'
    path = path.replace('/','\\')
    import idmt.nuke.utils
    idmt.nuke.utils.myMd(path)
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
        except:
            pass

# 输出节点处理
def commonOutputSetting():
    import os
    shotInfo = commonGetShotInfo()

    compression = 1
    # shotInfoCheck
    sRGB = 'sRGB'
    fileFormat = 'targe'
    fileFormatSimp = 'tga'
    drive = 'L:'
    proj = commonGetProjFullName(shotInfo[0])
    proj_abb = shotInfo[0]
    ep = shotInfo[1]
    tg = ''
    sc = shotInfo[2]
    if shotInfo[0] in ['mi']:
        compression = 'none'
        fileFormat = 'tiff'
        fileFormatSimp = 'tif'
    if shotInfo[0] in ['tf']:
        compression = 'none'
        fileFormat = 'tiff'
        fileFormatSimp = 'tif'
        tg = shotInfo[2]
        sc = shotInfo[3]
    if shotInfo[0] in ['Yak']:
        compression = 'none'
        fileFormat = 'tiff'
        fileFormatSimp = 'tif'
    if shotInfo[0] in ['sk']:
        compression = 0
    if shotInfo[0] in ['csl']:
        drive = 'L:'
        compression = 'none'
        fileFormat = 'tiff'
        fileFormatSimp = 'tif'
        tg = shotInfo[2]
        sc = shotInfo[3]
    if shotInfo[0] in ['nj']:
        compression = 'LZW'
        fileFormat = 'tiff'
        fileFormatSimp = 'tif'
        tg = shotInfo[2]
        sc = shotInfo[3]
    if shotInfo[0] in ['ice']:
        sRGB = 'linear'
        fileFormat = 'dex'
        fileFormatSimp = 'dex'
    if shotInfo[0] in ['LION']:
        drive = 'L:'
        compression = 'none'
    if shotInfo[0] in ['do6']:
        drive = 'L:'
        compression = 'none'
        fileFormat = 'tiff'
        fileFormatSimp = 'tif'

    parity = getParity(ep)

    retakeInfo = TK_Version_queryMsSQL(proj, ep, tg , sc)
    if not retakeInfo:
        tk_final = '001'
    else:
        tk = int(retakeInfo[0]) + 1
        tk_final = '00' + str(tk)
    if shotInfo[0] in ['mi','nj']:
        tk_final = shotInfo[4]
        if len(tk_final) > 3:
            tk_final = tk_final[-3:]
    if shotInfo[0] in ['nj']:
        tk_final = shotInfo[5]
    # setting
    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message(u'Please select one node and only a node!!')
        return
    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)

    gdcEnvPath = '//file-cluster/GDC/Resource/Development/Maya/GDC/Plug/Python/GDC'
    oneframeCmd = 'import sys;sys.path.append("%s");from idmt.nuke import utils;reload(utils);utils.copySingleFrame()'%gdcEnvPath

    folder = u'%s/Projects/%s/Production/Render/Compositing/%s/%s/%s/c%s' % (drive, proj, parity, ep, sc, tk_final)
    filename = '%s_%s_%s_cp_c%s.%%04d.%s' % (proj_abb, ep, sc, tk_final,fileFormatSimp)
    if shotInfo[0] in ['csl','tf']:
        folder = u'%s/Projects/%s/Production/Render/Compositing/%s/%s/%s/%s/c%s' % (drive, proj, parity, ep,tg, sc, tk_final)        
        filename = '%s_%s_%s_%s_cp_c%s.%%04d.tif' % (proj_abb, ep,tg, sc, tk_final) 
    if shotInfo[0] in ['nj']:
        folder = u'%s/Projects/%s/Production/Render/Compositing/%s/%s/%s/%s/%s' % (drive, proj, parity, ep,tg, sc, tk_final)
        filename = '%s_%s_%s_%s_cp_%s.%%04d.tif' % (proj_abb, ep,tg, sc, tk_final)
    if shotInfo[0] == 'Yak':
        folder = u'%s/Projects/%s/Production/Render/Compositing/%s/%s/%s/c%s' % (drive, 'YAK', parity, ep, sc, tk_final)

    if shotInfo[0] == 'ice':
        #modify with liangyu     
        s = nuke.getInput(r'tk num', '1')
        if s == None:
            return
        if re.search('\d{1,3}', s) == None:
            return
        tk = int(s)  
        folder = '//file-cluster/GDC/Projects/North/Production/Render/Compositing/%s/ep_%s/sq_%s/tk%d' % (parity, ep, sc, tk)         
        filename = '%s_%s_%s_cp_c%s.%%04d.dpx' % (proj_abb, shotInfo[1], sc, tk_final)
    if shotInfo[0] in ['mi']:
        folder = u'%s/Projects/%s/Production/Render/Compositing/%s/%s/%s/tk%s/%%V' % (drive, proj, parity, ep, sc, str(int(tk_final)))
        filename = '%s_%s_%s_%%V_cp_c%s.%%04d.%s' % (proj_abb, ep, sc, tk_final,fileFormatSimp)

    path = '%s/%s' % (folder, filename)

    # writeNode
    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("colorspace").setValue(sRGB)
    node.knob("file_type").setValue(fileFormat)
    if shotInfo[0]!='ice':
        node.knob("compression").setValue(compression)
    node.knob("beforeRender").setValue('')
    if shotInfo[0] != 'csl':
        node.knob("afterRender").setValue(oneframeCmd)
    if shotInfo[0] == 'nj':
        node.knob("datatype").setValue("16")
    if shotInfo[0] in ['tf','Yak']:
        node.knob("datatype").setValue("16")

    if shotInfo[0]=='ice':        
        node.knob("datatype").setValue("16")        
        nuke.toNode(node.name()).knob(21).setValue(2)
    if shotInfo[0] in ['mi']:
        node.knob("datatype").setValue(1)

    if shotInfo[0] in ['do6']:
        node.knob("datatype").setValue("16")

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)

    # 创建目录
    from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
    reload(sk_infoConfig)
    stereoMode = sk_infoConfig.sk_infoConfig().checkStereoProj(shotInfo)
    if stereoMode:
        for info in ['Left','Right']:
            checkFolder = folder.replace('%V',info)
            #nuke.message(checkFolder)
            if not os.path.exists(checkFolder):
                commonCreateFolder(checkFolder)
    else:
        if not os.path.exists(folder):
            commonCreateFolder(folder)

    # 保存
    nuke.scriptSave()

# ---------------------------------------------------#
# 复制单帧到服务器端
def copySingleFrame():

    shotInfo = commonGetShotInfo()
    proj = shotInfo[0]

    # 项目信息
    project_name = commonGetProjFullName(shotInfo[0])
    # 设置
    import nuke
    nuke.message("输出序列成功!!!")
    import shutil
    start_f = int(nuke.root().knob('first_frame').value())
    end_f = int(nuke.root().knob('last_frame').value())
    center_f = str(int((start_f + end_f + 1) / 2))

    if len(center_f) < 4:
        center_f = '0' + center_f
    if len(center_f) < 4:
        center_f = '0' + center_f
    if len(center_f) < 4:
        center_f = '0' + center_f
    if len(center_f) < 4:
        center_f = '0' + center_f

    path = ''

    allNodes = nuke.allNodes()
    for node in allNodes:
        if node.Class() == 'Write':
            afterRenderInfo = node.knob("afterRender").value()
            if '.copySingleFrame()' in afterRenderInfo:
            #if afterRenderInfo.find('from idmt.nuke import utils\nreload(utils)\nutils.copySingleFrame()') == 0:
                path = node.knob("file").value()

    path_split = path.split('%04d')
    filePath = center_f.join(path_split)

    filePath = filePath.split('####')
    filePath = center_f.join(filePath)

    filePath = re.sub('%V', 'left', filePath)
    filePath = re.sub('%V', 'left', filePath)

    fileName = filePath.split('/')[-1]
    epi = fileName.split('_')[1]
    epi = epi.split('_')[0]

    targetFolder = '//file-cluster/gdc/Projects/%s/%s_scratch/colorcorrect/%s' % (project_name, project_name, epi)

    newfileName = fileName.split('_cp')[0]
    newfileName = re.sub('_left$', '', newfileName)
    filetype = fileName.split('_cp_')[-1]

    targetPath = targetFolder + '/' + newfileName + '_cp_' + filetype

    import os
    if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)

    try:
        print filePath
        print targetPath
        shutil.copyfile(filePath, targetPath)
        nuke.message("copy单帧到colorcorrect目录成功!!!")

    except:
        nuke.message("copy单帧到colorcorrect目录失败!!!\n请检查渲染的帧数是否和数据库一致")
        pass

# ---------------------------------------------------#
# 自动构建镜头所需的nuke模板
def autoShotNukeConfig():
    shotInfo = commonGetShotInfo()
    filePath = nuke.root().knob("name").getValue()
    specialPro = 0
    linkType = 'L'

    if shotInfo[0] in ['cl']:
        clAutoShotNukeConfig()
        specialPro = 1

    if shotInfo[0] in ['csl']:
        import sys
        sys.path.append("//file-cluster/GDC/Resource/Support/Nuke_plugins/user")
        import  csl_autoNuke
        reload(csl_autoNuke)
        csl_autoNuke.csl_autoNukeLine(3)
        specialPro = 1

    if shotInfo[0] in ['nj']:
        import sys
        sys.path.append("//file-cluster/GDC/Resource/Support/Nuke_plugins/user")
        import  nj_autoNuke
        reload(nj_autoNuke)
        nj_autoNuke.nj_autoNukeLine(3)
        specialPro = 1

    if shotInfo[0] in ['zm']:
        import sys
        sys.path.append("//file-cluster/GDC/Resource/Support/Nuke_plugins/user")
        import  zm_autoNuke
        reload(zm_autoNuke)
        zm_autoNuke.zmAutoShotNukeConfig()
        specialPro = 1

    if shotInfo[0] in ['mi']:
        linkType = 'L'
        GT = '2048 858 GT'
        nuke.addFormat(GT)
        nuke.knobDefault('Root.format', GT)
        nuke.root().knob('format').setValue('GT')

    if shotInfo[0][:2] in ['do']:
        linkType = 'L'
        GT = '2048 858 GT'
        nuke.addFormat(GT)
        nuke.knobDefault('Root.format', GT)
        nuke.root().knob('format').setValue('GT')

    # 若无特殊项目需求，只处理镜头路径替换
    if not specialPro:
        autoRelpaceSeqImages(linkType)

# ------------------------------------------------------------------------------#

# ---------------------------------------------------#
#【辅助】【通用】【辅助函数】
# ---------------------------------------------------#

# 获取镜头号名字
def commonGetShotInfo():
    filePath = nuke.root().knob("name").getValue()
    if filePath:
        fileInfo = filePath.split('/')[-1].split('.')[0].split('_')
        return fileInfo
    else:
        nuke.message("请检查Nuke文件名字！！！")

# ---------------------------------------------------#
# 赵仲捷 提供
# SQL查询获取版本信息
def TK_Version_queryMsSQL(project, ep, tg, sc):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f'%(project))
    cursor = cnxn.cursor()
    
    ep = "'%s'"%(ep)
    if tg == '':        tg = 'TA.Tag'
    else:        tg = "'%s'"%(tg)
    sc = "'%s'"%(sc)
    
    cmd_tk = '''
    select ISNULL(TSTS.stss_CountComments,0) stss_CountComments, 
    ISNULL(TSTS.stss_ConutSendFile,0) stss_ConutSendFile, 
    TAT.task_mode,TA.anim_ep,TA.Tag,TA.anim_sc 
    from dbo.tb_SsomTaskStatus TSTS 
    inner join dbo.TB_Anim_Task TAT on TSTS.stss_taskid=TAT.task_id 
    inner join dbo.TB_Anim TA on TAT.anim_id=TA.anim_id 
    where TA.anim_ep=%s and TA.Tag=%s and TA.anim_sc=%s and TAT.task_mode = 'composite' and TSTS.stss_tasktype='anim'

    '''%(ep,tg,sc)
    
    
    cmd_sf_ef = '''    
    select frmStart,frmEnd,anim_ep,Tag,anim_sc from TB_Anim TA where anim_ep=%s and Tag=%s and anim_sc=%s
    '''%(ep,tg,sc)
    
    
    tk = cursor.execute(cmd_tk).fetchone()
    
    sf_ef = cursor.execute(cmd_sf_ef).fetchone()
    
    tk_sf_ef = []
    if tk and sf_ef:
        tk_sf_ef.append(list(tk)[0])
        tk_sf_ef.append(list(sf_ef)[0])
        tk_sf_ef.append(list(sf_ef)[1])
    return tk_sf_ef

# ---------------------------------------------------#

# 奇偶信息
def getParity(episode):
    parity = idmt.pipeline.project.GetParity(episode)
    return parity

# ---------------------------------------------------#

# 读文件===============
def checkFileRead(path):
    print u'>>>>>>[read]'
    print path
    txt = open(path, 'r')
    try:
        fileContent = txt.readlines()
        print('Loading........')
    finally:
        txt.close()
    for i in range(len(fileContent)):
        if len(fileContent[i].split('\r\n')) > 1:
            temp = fileContent[i].split('\r\n')
            fileContent[i] = temp[0]
    return fileContent

# ---------------------------------------------------#

# 写文件================
def checkFileWrite(path, info, addtion=0):
    print u'>>>>>>[write]'
    if addtion == 1:
        info = checkFileRead(path) + info
    txt = open(path, 'w')
    try:
        txt.writelines(str(a) + '\r\n' for a in info)
        print('Writing........')
    finally:
        txt.close()

# ---------------------------------------------------#

# 读excel表格，反馈数据
def checkExcelRead(path, SHEETS=0):
    import xlrd
    data = xlrd.open_workbook(path)
    table = data.sheets()[SHEETS]
    #nrows = table.nrows
    #ncols = table.ncols
    #rowInfo = table.row_values(num)
    return table

# ------------------------------------------------------------------------------#

# ---------------------------------------------------#
#【核心】【项目专用】【函数】
# ---------------------------------------------------#

# idPass输出模板
def autoOutputIdPass():
    shotInfo = commonGetShotInfo()
    filePath = nuke.root().knob("name").getValue()

    if shotInfo[0] == 'cl':
        clAutoOutputIdPass()
    else:
        nuke.message("[本功能][目前]为Calimoro专用工具")

# 处理表格信息
def clExcelInfoConfig(info):
    info = str(info)
    while info[-1] in [';',' ']:
        info = info[:-1]
    while '.' in info:
        info = info.split('.')[0]
    return info


# ------------------------------------------------------------------------------#

#--------------------------------#
#【核心】 只替换序列帧路径
#--------------------------------#
def autoRelpaceSeqImages(linkType = 'Z'):
    printMode = 1
    # -----------------#
    # Step 0 : 获取 项目名 ，项目全名，(自动读取) 场景号，镜头号，版本号 ,时间轴
    shotInfo = commonGetShotInfo()
    shot = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
    print '------------s'
    print shot

    import os
    anim = idmt.pipeline.db.GetAnimByFilename(shot)

    ep = str(shotInfo[1])
    sc = str(shotInfo[2])
    tk = str(shotInfo[-1])
    parity = getParity(ep)
    startFrame = anim.frmStart
    endFrame = anim.frmEnd
    fpsFrame = anim.fps

    # 获取readNodes
    allNodes = nuke.allNodes()
    readNodes = {}
    import os
    for nd in allNodes:
        if nd.Class() != 'Read':
            continue
        # 记录
        readPath = nd.knob('file').getValue()
        readNodes[nd] = readPath
        # 替换
        pathInfos = readPath.split('/')
        oldEp = ''
        oldSc = ''
        oldTake = ''
        newTake = ''
        stereoMode = 0
        steRelaceKey = '_%V'
        stereoKeys = ['_Left','_Right','_left','_right']
        for checkKey in stereoKeys:
            if checkKey not in readPath:
                continue
            steRelaceKey = checkKey
        #if 'COLORAMB_beauty' not in readPath:
        #    continue
        if printMode:
            print '=========='
            print readPath
            print stereoMode
            print steRelaceKey
        for num in range(len(pathInfos)):
            # 场
            if 'ep_' in [pathInfos[num][0:3]]:
                oldEp = pathInfos[num]
                pathInfos[num] = 'ep_' + ep
                if printMode:
                    print '-------'
                    print oldEp
                    print pathInfos[num]
            # 镜
            if 'sc_' in [pathInfos[num][0:3]]:
                oldSc = pathInfos[num]
                pathInfos[num] = 'sc_' + sc
            # 版本
            if 'c' in [pathInfos[num][0]]:
                oldTake = pathInfos[num]
                layerPath = readPath.split('/c')[0]
                layerPath = layerPath.replace('/%s/'%oldEp,'/ep_%s/'%ep)
                layerPath = layerPath.replace('/%s/'%oldSc,'/sc_%s/'%sc)
                searchPath = layerPath.replace('/','\\')
                # 加/S意味着文件夹下所有信息
                dataGet = os.popen('DIR /d %s /b'%searchPath)
                getInfo = dataGet.read()
                allInfos = getInfo.split('\n')
                needTks = []
                for checkInfo in allInfos:
                    if not checkInfo:
                        continue
                    if 'c' in [checkInfo[0]]:
                        needTks.append(int(checkInfo[1:]))
                if needTks:
                    maxTk = max(needTks)
                    tkInfo = str(maxTk / 100)[-1] + str(maxTk / 10)[-1] + str(maxTk)[-1]
                    pathInfos[num] = 'c%s'%(str(tkInfo))
                if printMode:
                    print '-------'
                    print oldTake
                    print layerPath
                    print allInfos
                    print needTks
                    print pathInfos[num]
                newTake = pathInfos[num]
            # 文件
            if num == (len(pathInfos)-1):
                seqFolder = readPath[:-1*(1+len(readPath.split('/')[-1]))]
                seqFolder = seqFolder.replace('/%s/'%oldEp,'/ep_%s/'%ep)
                seqFolder = seqFolder.replace('/%s/'%oldSc,'/sc_%s/'%sc)
                seqFolder = seqFolder.replace('/%s'%oldTake,'/%s'%newTake)
                searchPath = seqFolder.replace('/','\\')
                # 加/S意味着文件夹下所有信息
                dataGet = os.popen('DIR /d %s /b'%searchPath)
                getInfo = dataGet.read()
                allInfos = getInfo.split('\n')
                needFileInfo = ''
                for checkInfo in allInfos:
                    if not checkInfo:
                        continue
                    if shot in checkInfo and '.' in checkInfo:
                        needFileInfo = checkInfo
                    if needFileInfo:
                        break
                if needFileInfo:
                    tempInfos = needFileInfo.split('.')
                    imgNum = len(tempInfos[1])
                    lastFile = tempInfos[0] + '.' + '%0' + str(imgNum) + 'd.' + tempInfos[-1]
                    for checkKey in stereoKeys:
                        if checkKey not in lastFile:
                            continue
                        lastFile = lastFile.replace(checkKey,steRelaceKey)
                    pathInfos[num] = lastFile
                if printMode:
                    print '------------e'
                    print ep
                    print sc
                    print oldTake
                    print newTake
                    print seqFolder
                    print needFileInfo
                    print pathInfos[num]
        newPath = ''
        for num in range(len(pathInfos)):
            if num == 0:
                newPath = pathInfos[num]
            else:
                newPath = newPath + '/' + pathInfos[num]
        if linkType in ['L']:
            if 'z:' in newPath:
                newPath = newPath.replace('z:','L:')
            if 'Z:' in newPath:
                newPath = newPath.replace('Z:','L:')
        if printMode:
            print '------lle'
            print newPath
        nd.knob('file').setValue(newPath)
        nd.knob('first').setValue(startFrame)
        nd.knob('origfirst').setValue(startFrame)
        nd.knob('last').setValue(endFrame)
        nd.knob('origlast').setValue(endFrame)

    nuke.root().knob("first_frame").setValue(startFrame)
    nuke.root().knob("last_frame").setValue(endFrame)

# -------------------------------#
#【核心】【Calimero】
# -------------------------------#
# 自动加载idPass模板
def clAutoOutputIdPass():
    # -----------------#
    # Step 0 : 获取 项目名 ，项目全名，(自动读取) 场景号，镜头号，版本号 ,时间轴
    shotInfo = commonGetShotInfo()
    
    if shotInfo[0] != 'cl':
        nuke.message("本功能目前为Calimoro专用工具")
        return 1
    
    shot = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
    import os
    anim = idmt.pipeline.db.GetAnimByFilename(shot)

    ep = str(shotInfo[1])
    sc = str(shotInfo[2])
    tk = str(shotInfo[-1])
    parity = getParity(ep)
    startFrame = anim.frmStart
    endFrame = anim.frmEnd
    fpsFrame = anim.fps
    
    projSimple = 'cl'
    projFullName = 'Calimero'
    
    # -----------------#
    # Step 1 : 强行清空脚本
    nuke.scriptClear()
    
    # -----------------#
    # Step 2 : 导入文件
    serverPath = ('//file-cluster/GDC/Projects/' + projFullName + '/' + projFullName + '_scratch/TD/nuke/')
    idPassBaseFile = serverPath + 'cl_idPass_Base.nk'
    
    spec = "*.nk; *.gizmo"
    s = nuke.getFilename("Import Script", spec, idPassBaseFile, "script")
    nuke.nodePaste(s)

    # -----------------#
    # Step 3 :read文件路径更新
    layerKeys = ['/SPEC/', '/RGB/', '/BG_RGB/' ,'/LIGHT/']
    imagesPathBase = ('//file-cluster/GDC/Projects/' + projFullName + '/Production/Render/Images/' + parity + '/ep_' + ep + '/sc_' + sc + '/lr/')
    
    allNodes = nuke.allNodes()
    readNodes = []
    for nd in allNodes:
        if nd.Class() == 'Read':
            readNodes.append(nd)

    for nd in readNodes:
        oldPath = nd.knob('file').getValue()
        imagePath = ''
        needLayerKey = ''
        layerFolder = ''
        # 检测layerKey
        for layerKey in layerKeys:
            if layerKey in oldPath:
                needLayerKey = layerKey[1:-1]
                try:
                    filesInPath = os.listdir(imagesPathBase + needLayerKey + '/' + tk + '/')
                    layerFolder = needLayerKey
                    imagePath = imagesPathBase + needLayerKey + '/' + tk + '/' + filesInPath[0].split('.')[0] + '.%04d.' + filesInPath[0].split('.')[-1]
                except:
                    pass
        if imagePath:
            nd.knob('file').setValue(imagePath)
        nd.knob('first').setValue(startFrame)
        nd.knob('origfirst').setValue(startFrame)
        nd.knob('last').setValue(endFrame)
        nd.knob('origlast').setValue(endFrame)

    # -----------------#
    # Step 4 : 另存文件
    localNukePath = 'D:/Info_Temp/temp/NukeComp/' + str(shotInfo[0]) + '/' 
    localNukeFile = localNukePath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_idPass_Base.nk'
    
    import os
    if not os.path.exists(localNukePath):
        os.makedirs(localNukePath)

    nuke.root().knob("name").setValue(localNukeFile)

    nuke.scriptSave("")
    
    
# 自动素材加载对比路径
def clAutoShotNukeConfig():
    # -----------------#
    # Step 0 : 获取 项目名 ，项目全名，(自动读取) 场景号，镜头号，版本号 ,时间轴
    shotInfo = commonGetShotInfo()
    filePath = nuke.root().knob("name").getValue()

    if shotInfo[0] != 'cl':
        nuke.message("本功能目前为Calimoro专用工具")
        return 1

    shot = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
    import os
    anim = idmt.pipeline.db.GetAnimByFilename(shot)

    projSimple = 'cl'
    projFullName = 'Calimero'

    ep = str(shotInfo[1])
    sc = str(shotInfo[2])
    tk = str(shotInfo[-1])
    parity = getParity(ep)
    startFrame = anim.frmStart
    endFrame = anim.frmEnd
    fpsFrame = anim.fps

    # -----------------#
    # Step 1 : 判断是否空文件，空文件则读取nuke，非空文件则直接进入素材更新
    checkNodes = nuke.allNodes()
    viewNodes=nuke.allNodes('Viewer')
    if not checkNodes or checkNodes == viewNodes:
        # -----------------#
        # Step A1 : 读取nuke

        # 获取assetInfo
        #serverPath = ('//file-cluster/GDC/Projects/' + projFullName + '/' + projFullName + '_scratch/TD/ExcelInfo/')
        serverPath = '//file-cluster/GDC/Projects/' + projFullName + '/Reference/Product manager/Render/ExcelInfo/' 
        serverExcelPath = serverPath  + '/' + ep + '/' + shotInfo[0].upper() + ep + '_TimeOfDay.xls'

        import sys
        sys.path.append('//file-cluster/GDC/Resource/Support/Maya/Python/')
        import xlrd
        shotAllData = xlrd.open_workbook(serverExcelPath).sheets()[0]

        rowMax = shotAllData.nrows
        rowID = 0
        for i in range(rowMax):
            shotID = clExcelInfoConfig(shotAllData.row_values(i)[0])
            checkID = shotInfo[2]
            while checkID[0] == '0':
                checkID = checkID[1:]
            while shotID[0] == '0':
                shotID = shotID[1:]
            if shotID == checkID:
                rowID = i
                break

        #shotData = shotAllData.row_values(int(sc) + 1)
        shotData = shotAllData.row_values(rowID)
        print shotData

        # skyMood
        skyMoodKey = ''
        if shotData[1][-1] == ' ':
            skyMoodKey = shotData[1][:-2]
        else:
            skyMoodKey = shotData[1][:-1]

        # assetInfo
        setAsset = ''
        if len(shotData) < 3:
            print u'===请检查本镜头的excel表格信息==='
            nuke.error(u'===请检查本镜头的excel表格信息===')
        if shotData[2][-1] == ' ':
            setAsset = shotData[2][:-2].split(';')[0]
        else:
            setAsset = shotData[2][:-1].split(';')[0]
            
        addInfo = ''
        if len(shotData)> 3:
            if shotData[3]:
                if shotData[3][-1] == ' ':
                    addInfo = shotData[3][:-2]
                else:
                    addInfo = shotData[3][:-1]

        # -----------------#
        # Step A2 : GA asset data <<==>> GDC asset data
        otherAssetFile = ''
        assetGATemp = checkFileRead(serverPath + 'OutsideAsset.txt')
        assetGA = []
        if assetGATemp:
            for info in assetGATemp:
                needInfo = info
                if '\n' in needInfo.split('|')[-1]:
                    needInfo = needInfo.split('|')[-1].replace('\n','')
                assetGA.append(needInfo)
        
        assetGDCTemp = checkFileRead(serverPath + 'GDCAsset.txt')
        assetGDC = []
        if assetGDCTemp:
            for info in assetGDCTemp:
                needInfo = info
                if '\n' in needInfo.split('|')[-1]:
                    needInfo = needInfo.split('|')[-1].replace('\n','')
                assetGDC.append(needInfo)
                
        # nuke.message("%s"%setAsset)
        assetFile = setAsset
        if setAsset in assetGDC:
            id = assetGDC.index(setAsset)
            # nuke.message("%s"%id)
            setAsset = assetGA[id]
        
        # nuke.message("%s"%setAsset)

        # -----------------#
        # Step A3 : data|geoCache 获取 asset Info，与模板路径对比确定使用的场景
        #templatePath = '//file-cluster/GDC/Projects/Calimero/Common_Sync/CAL_COMPO/TEMPLATES/SETS/'
        templatePath = '//file-cluster/gdc/Projects/Calimero/Reference/Product manager/Render/SETS/'
        templateFolders = os.listdir(templatePath)
        if not templateFolders:
            nuke.message("Nuke路径有问题，请和TD联系")
            return 1
        # 获取模板路径
        needNukePath = ''
        for folder in templateFolders:
            if folder.lower() == setAsset.lower():
                needNukePath = templatePath + folder + '/'
        
        # nuke.message("%s"%needNukePath)

        # -----------------#
        # Step A4 : 读取skydome表格，确定场景的氛围nuke模板
        # 目前无表格读取
        nukeFileBase = 'CAL_' + setAsset + '_'
        # test
        nukeFileKey = skyMoodKey + '.nk'
        if setAsset.lower() == 'render_2d':
            nukeFileBase = 'CAL_' + setAsset
            nukeFileKey = '.nk'
        nukeFile = needNukePath + nukeFileBase + nukeFileKey

        if not os.path.exists(nukeFile):
            nukeFile = needNukePath + nukeFileBase +  addInfo + '_' + nukeFileKey

        print setAsset
        print nukeFile
        nuke.message("[%s_%s]如有问题，请联系TD:\n[%s]\n\n[注意]点的太快nuke容易崩溃，请温柔操作o(╯□╰)o" % (str(shotInfo[1]), str(shotInfo[2]), str(nukeFileBase + nukeFileKey)))

        # -----------------#
        # Step A5 : 打开nuke模板，另存到本地，改名
        # Q .如何打开nuke文件，如何保存nuke文件

        #spec = "*.nk; *.gizmo"
        #s = nuke.getFilename("Import Script", spec, nukeFile, "script")
        #nuke.nodePaste(s)
        
        # 前面有信息提示，能让nuke将本次打开命令进行缓行化，如同maya的延迟代码
        try:
            #nuke.scriptOpen( nukeFile )
            nuke.nodePaste(nukeFile)
        except:
            pass
        
        nuke.message("文件已加载，即将进入素材替换阶段...")

        localNukePath = 'D:/Info_Temp/temp/NukeComp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        localNukeFile = localNukePath + filePath.split('/')[-1]
        
        if not os.path.exists(localNukePath):
            os.makedirs(localNukePath)

        nuke.root().knob("name").setValue(localNukeFile)

        nuke.scriptSave("")

    # -----------------#
    # Step 2 : 判断文件类型，处理信息
    allNodes = nuke.allNodes()
    readNodes = []
    writeNodes = []
    writeNodeNames = []
    writeNodeKeys = ['RGB_idPass1','BG_RGB_idPass2','LIGHT_idPass3','SPEC_idPassChr','SPEC_idPassChrMain']
    for nd in allNodes:
        if nd.Class() == 'Read':
            readNodes.append(nd)
        if nd.Class() == 'Write':
            nodeName = nd.knob('name').value()
            if nodeName in writeNodeKeys:
                writeNodes.append(nd)
                writeNodeNames.append(nodeName)
    
    # -----------------#
    # Step 2A 判断为idPass输出文件时
    if writeNodes and readNodes:
        #屏蔽没有此流程
        '''import os
        # 本地路径处理
        oldPath = readNodes[0].knob('file').getValue()
        fileOldInfo = oldPath.split('/')[-1].split('_')
        localIdPassPath = '//file-cluster/GDC/Projects/'+projFullName+'/Production/Render/Images' + parity + '/ep_'  + str(fileOldInfo[1]) + '/sc_' + str(fileOldInfo[2])  
        
        # write节点处理
        for node in writeNodes:
            node.knob("disable").setValue(True)
        
        # read节点路径处理
        for node in readNodes:
            # 需要获取文件名
            fileName = ''
            oldPath = node.knob('file').getValue()
            # 判断文件存在与否
            if os.path.exists(oldPath.split('/')[0]):
                continue
            # RGB_idPass1
            if '/RGB/' in oldPath:
                fileOldName = oldPath.split('/')[-1]
                fileNewName = fileOldName.split('.')[0] + '_idPass1' + oldPath[len(oldPath.split('.')[0]):]
                fileNewPath = localIdPassPath +'/RGB_idPass1/c001/'+ fileNewName
                
                if not os.path.exists(localIdPassPath +'/RGB_idPass1/c001/'):
                    os.makedirs(localIdPassPath +'/RGB_idPass1/c001/')

                # 设置write节点
                idPassIndex = writeNodeNames.index('RGB_idPass1')
                writeNodes[idPassIndex].knob('file').setValue(fileNewPath)
                writeNodes[idPassIndex].knob("disable").setValue(False)
            # BG_RGB_idPass1
            if '/BG_RGB/' in oldPath:
                fileOldName = oldPath.split('/')[-1]
                fileNewName = fileOldName.split('.')[0] + '_idPass2' + oldPath[len(oldPath.split('.')[0]):]
                fileNewPath = localIdPassPath + '/BG_RGB_idPass2/c001/' + fileNewName
                
                if not os.path.exists(localIdPassPath + '/BG_RGB_idPass2/c001/'):
                    os.makedirs(localIdPassPath + '/BG_RGB_idPass2/c001/')

                # 设置write节点
                idPassIndex = writeNodeNames.index('BG_RGB_idPass2')
                writeNodes[idPassIndex].knob('file').setValue(fileNewPath)
                writeNodes[idPassIndex].knob("disable").setValue(False)
            # LIGHT_idPass3
            if '/LIGHT/' in oldPath:
                fileOldName = oldPath.split('/')[-1]
                fileNewName = fileOldName.split('.')[0] + '_idPass3' + oldPath[len(oldPath.split('.')[0]):]
                fileNewPath = localIdPassPath + '/LIGHT_idPass3/c001/' + fileNewName
                
                if not os.path.exists(localIdPassPath +'/LIGHT_idPass3/c001/'):
                    os.makedirs(localIdPassPath + '/LIGHT_idPass3/c001/')

                # 设置write节点
                idPassIndex = writeNodeNames.index('LIGHT_idPass3')
                writeNodes[idPassIndex].knob('file').setValue(fileNewPath)
                writeNodes[idPassIndex].knob("disable").setValue(False)
            # SPEC_idPassChr
            if '/SPEC/' in oldPath:
                # SPEC_idPassChr
                fileOldName = oldPath.split('/')[-1]
                fileNewName = fileOldName.split('.')[0] + '_idPassChr' + oldPath[len(oldPath.split('.')[0]):]
                fileNewPath = localIdPassPath + '/SPEC_idPassChr/c001/' + fileNewName
                
                if not os.path.exists(localIdPassPath +'/SPEC_idPassChr/c001/'):
                    os.makedirs(localIdPassPath + '/SPEC_idPassChr/c001/')

                # 设置write节点
                idPassIndex = writeNodeNames.index('SPEC_idPassChr')
                writeNodes[idPassIndex].knob('file').setValue(fileNewPath)
                # SPEC_idPassChrMain
                fileNewName = fileOldName.split('.')[0] + '_idPassChrMain' + oldPath[len(oldPath.split('.')[0]):]
                fileNewPath = localIdPassPath  + '/SPEC_idPassChrMain/c001/' + fileNewName
                
                if not os.path.exists(localIdPassPath +'/SPEC_idPassChrMain/c001/'):
                    os.makedirs(localIdPassPath  + '/SPEC_idPassChrMain/c001/')

                writeNodes[idPassIndex].knob("disable").setValue(False)
                # 设置write节点
                idPassIndex = writeNodeNames.index('SPEC_idPassChrMain')
                writeNodes[idPassIndex].knob('file').setValue(fileNewPath)
                writeNodes[idPassIndex].knob("disable").setValue(False)
        
        # 另存
        localNukeFile = localIdPassPath + '/' + str(fileOldInfo[0]) + '_' + str(fileOldInfo[1]) + '_' + str(fileOldInfo[2]) + '_idPass_cp_c001.nk'
        
        if not os.path.exists(localIdPassPath):
            os.makedirs(localIdPassPath)

        nuke.root().knob("name").setValue(localNukeFile)
    
        nuke.scriptSave("")'''
    
    else:
    # -----------------#
    # Step 2B : 根据镜头信息和版本号信息，更改素材路径
    # Q ，素材节点名字是否完全一致，获取节点class
    # 判断节点性质
    # 设计: RGB_idpass1 ; RGB_idpass2，分离出这样的素材
        #layerKeys = ['/RGB/', '/BW/', '/LIGHT/', '/SPEC/', '/RIMLIGHT/', '/ZDEPTH/', '/BG_RGB/', '/PFX/', '/RENDER2D/',
        #             '/RGB_idPass1/', '/BG_RGB_idpass2/', '/LIGHT_idPass3/', '/SPEC_idPassChrMain/', 'SPEC_idPassChr', 'SPEC_idPassChr']
        layerKeys = ['/RGB/', '/BW/', '/LIGHT/', '/SPEC/', '/RIMLIGHT/', '/ZDEPTH/', '/BG_RGB/', '/PFX/', '/RENDER2D/','/LIGHTSET/','/dust/']
        idpassKeys = ['/idPass1/', '/idPass2/', '/idPass3/', '/idPassChrMain/', '/idPassChr/','/MasterBeauty/']
        imagesPathBase = ('//file-cluster/GDC/Projects/' + projFullName + '/Production/Render/Images/' + parity + '/ep_' + ep + '/sc_' + sc + '/')
        #imagesPathBase = ('//file-cluster/GDC/Netrender/Scenes/' + projFullName + '/' + parity + '/ep_' + ep + '/sc_' + sc + '/' )
    
        for nd in readNodes:
            oldPath = nd.knob('file').getValue()
            extName = oldPath.split('.')[-1]
            imagePath = ''
            LayerName=''
            IdpassName=''

            # 检测layerKey
            needLayerKey = ''
            for layerKey in layerKeys:
                if layerKey in oldPath:
                    needLayerKey = layerKey[1:-1]
                    if needLayerKey == 'dust': #特殊素材，统一路径
                        LayerName = needLayerKey
                    else :
                        try:
                            filesInPath = os.listdir(imagesPathBase + needLayerKey + '/')
                            LayerName = needLayerKey
                        except:
                            pass
            # 检测idpass
            needIdpass = ''
            for idp in idpassKeys:
                if idp in oldPath:
                    needIdpass = idp[1:-1]
                    try:
                        filesInPath = os.listdir(imagesPathBase + LayerName + '/' + needIdpass+'/')
                        IdpassName =  needIdpass
                        #imagePath = imagesPathBase + (needLayerKey + '_' + needIdpass) + '/' + tk + '/' + filesInPath[0].split('.')[0] + '.%04d.' + filesInPath[0].split('.')[-1]
                    except:
                        pass
                    #    if ('/' + needLayerKey + '/' + needIdpass + '/') in oldPath:
                            # ['RGB_idPass1','BG_RGB_idPass2','LIGHT_idPass3','SPEC_idPassChrMain','SPEC_idPassChr']
                    #        layerFolder = (needLayerKey + '_' + needIdpass)
                            #nuke.message("层[%s]不存在"%(needLayerKey + '_' + needIdpass))
                    #        imagePath = imagesPathBase + (needLayerKey + '_' + needIdpass) + '/' + tk + '/'
            if LayerName :
                imagePath=imagesPathBase+LayerName+'/'+IdpassName+'/'
                fileNewName = 'CAL_'+ep+'_'+sc+'_LAYERS_'+IdpassName+'.%03d.'+extName
                if LayerName == 'PFX' : #PFX特殊路径及命名规则
                    imagePath=imagesPathBase+LayerName+'/'
                    fileNewName = 'CAL_'+ep+'_'+sc+'_LAYERS_'+'.%03d.'+extName
                if LayerName == 'dust' : #特殊素材，统一路径
                    imagePath = '//file-cluster/GDC/Projects/Calimero/Production/Render/Images/ODD/FX/BANK/dust/PNG/'
                    fileNewName = 'Dust.%04d.png'
                NewImage = imagePath+fileNewName
                # if '%04d' not in imagePath :
                #    nuke.message("层[%s]不存在"%layerFolder)
                if NewImage:
                     nd.knob('file').setValue(NewImage)
                nd.knob('first').setValue(startFrame)
                nd.knob('origfirst').setValue(startFrame)
                nd.knob('last').setValue(endFrame)
                nd.knob('origlast').setValue(endFrame)
            else  :
                nd.knob("disable").setValue(True)

    # -----------------#
    # Step 3 : 项目设置
    commonProjectSetting()

    nuke.scriptSave("")
    
    return 0


# ------------------------------------------------------------------------------#
# old system
# 替换镜头
def changeShot():
    sqLabel = 'SQ:'
    scLabel = 'SC:'
    sqNew = ''
    scNew = ''
    p = nuke.Panel("Change Shot")
    p.addSingleLineInput(sqLabel, sqNew)
    p.addSingleLineInput(scLabel, scNew)
    p.addButton("Cancel")
    p.addButton("OK")
    result = p.show()
    if(result == 1):
        sqNew = p.value(sqLabel)
        scNew = p.value(scLabel)
        nodes = nuke.allNodes()
        for node in nodes:
            if(node.Class() == "Read" or node.Class() == "Write"):
                pathOld = node.knob("file").value()
                pathNew = pathOld
                p = re.compile('/(sq|ep)_([^/]+)/(sc)_([^/]+)/', re.IGNORECASE)
                m = p.search(pathNew)
                if(m != None):
                    sqOld = m.group(2)
                    scOld = m.group(4)
                    if(sqNew == ''):
                        sqNew = sqOld
                    if(scNew == ''):
                        scNew = scOld
                    pathNew = p.sub('/\g<1>_' + sqNew + '/\g<3>_' + scNew + '/', pathNew)
                    p = re.compile('_' + sqOld + '(_(sc_)?)' + scOld + '(_|\.)', re.IGNORECASE)
                    m = p.search(pathNew)
                    if(m != None):
                        pathNew = p.sub('_' + sqNew + '\g<1>' + scNew + '\g<3>', pathNew)
                    parityOld = getParity(sqOld)
                    parityNew = getParity(sqNew)
                    if(parityOld != parityNew):
                        pathNew = re.compile('/' + parityOld + '/', re.IGNORECASE).sub('/' + parityNew + '/', pathNew)
                if(pathNew != pathOld):
                    if(node.Class() == "Write"):
                        dir = re.sub('/[^/]+$', '', pathNew)
                        if(not os.path.isdir(dir)):
                            myMd(dir)
                    node.knob("file").setValue(pathNew)
                    if(node.Class() == "Read"):
                        seq = IsSequence(pathNew)
                        if(seq != None):
                            pathNew = re.sub(r'\.[^.]+\.([^.]+)$', r'.%04d.\1', pathNew)
                            first = re.search(r'\.([^.]+)\.[^.]+$', seq[0]).group(1)
                            last = re.search(r'\.([^.]+)\.[^.]+$', seq[len(seq) - 1]).group(1)
                            node.knob("first").setValue(int(first))
                            node.knob("last").setValue(int(last))

# 替换工具


def panelReplace():
    slLabel = 'For Selected:'
    sqLabel = 'Sequence:'
    scLabel = 'Scene:'
    characterLabel = 'Character:'
    frameLabel = 'Frame:'

    sl = False
    sq = 'sq_'
    sc = 'sc_'
    character = ''
    frame = ''

    p = nuke.Panel("Replace")
    p.addBooleanCheckBox(slLabel, sl)
    p.addSingleLineInput(sqLabel, sq)
    p.addSingleLineInput(scLabel, sc)
    p.addSingleLineInput(characterLabel, character)
    p.addSingleLineInput(frameLabel, frame)
    p.addButton("Cancel")
    p.addButton("OK")
    result = p.show()
    if(result == 1):
        sl = p.value(slLabel)
        sq = p.value(sqLabel)
        sc = p.value(scLabel)
        character = p.value(characterLabel)
        frame = p.value(frameLabel)
        nodes = None
        if(sl):
            nodes = nuke.selectedNodes()
        else:
            nodes = nuke.allNodes()
        for node in nodes:
            if(node.Class() == "Read"):
                pathOld = node.knob("file").value()
                pathNew = pathOld
                pathNew = re.sub(r'^Z:', r'//file-cluster/GDC', pathNew)
                p = re.compile(r'(.*)/(EVEN|ODD)/((sq_)*[^_/]+)/((sc_)*[^_/]+)/(([^/]+/)*)(sq_[^_/.]+)_(sc_[^_/.]+)(_[^/]+)$', re.IGNORECASE)
                m = p.match(pathNew)
                if(m != None):
                    mySq1 = m.group(3)
                    mySq2 = m.group(9)
                    if(sq != r'sq_' and sq != ''):
                        mySq1 = sq
                        mySq2 = sq
                    mySc1 = m.group(5)
                    mySc2 = m.group(10)
                    if(sc != r'sc_' and sc != ''):
                        mySc1 = sc
                        mySc2 = sc
                    pathNew = p.sub(r'\1/\2/' + mySq1 + r'/' + mySc1 + r'/\7' + mySq2 + r'_' + mySc2 + '\g<11>', pathNew)
                p = re.compile(r'(.*/(EVEN|ODD)/([^/]+/){2}(footage/)*)[^/]+(/[^/]+/sq_[^_/.]+_sc_[^_/.]+_)[^_/.]+(_[^/]+)$', re.IGNORECASE)
                m = p.match(pathNew)
                if(m != None):
                    if(character != ''):
                        pathNew = p.sub(r'\1' + character + r'\5' + character + r'\6', pathNew)
                        print(pathNew)
                if(frame != ''):
                    p = re.compile(r'(/[^/.]+\.)[^/.]+(\.[^/.]+)$', re.IGNORECASE)
                    pathNew = p.sub(r'\g<1>' + frame + r'\g<2>', pathNew)
                if(pathNew != pathOld):
                    node.knob("file").setValue(pathNew)

# Tests -> Lighting_Passes


def Tests2Lighting_Passes():
    for node in nuke.allNodes():
        if(node.Class() == "Read"):
            pathOld = node.knob("file").value()
            pathNew = pathOld
            m = re.match(r'.*/(env|vfx)/.*', pathNew)
            if(m == None):
                pathNew = re.sub(r'.*/(EVEN|ODD)/', r'//file-cluster/GDC/Projects/WinxClubII/Production/Render/Lighting_Passes/\1/', pathNew)
            else:
                pathNew = re.sub(r'.*(/(EVEN|ODD)/([^/]+/){2})(footage/)*', r'[getenv NK_winxII]\g<1>footage/', pathNew)
            if(pathNew != pathOld):
                seq = IsSequence(pathNew)
                if(seq != None):
                    pathNew = re.sub(r'\.[^.]+\.([^.]+)$', r'.%04d.\1', pathNew)
                    first = re.search(r'\.([^.]+)\.[^.]+$', seq[0]).group(1)
                    last = re.search(r'\.([^.]+)\.[^.]+$', seq[len(seq) - 1]).group(1)
                    node.knob("first").setValue(int(first))
                    node.knob("last").setValue(int(last))
                node.knob("file").setValue(pathNew)


def IsSequence(path):
    result = None
    path = re.sub(r'\[getenv NK_winxII\]', os.environ["NK_winxII"], path)
    path = re.sub(r'\[getenv NK_roma\]', os.environ["NK_roma"], path)
    p = re.search(r'([^/]+)$', path).group(1)
    p = re.sub(r'\.[^.]+\.', r'*', p)
    path = re.sub(r'/[^/]+$', '', path)
    for root, dirs, files in os.walk(path):
        result = glob.glob(os.path.join(root, p))
    if(result != None and len(result) > 4):
        return result
    return None

# Z: -> //file-clister/GDC


def unc():
    nuke.root().setProxy(False)
    for node in nuke.allNodes():
        file = node.knob("file")
        if(file != None):
            pathOld = node.knob("file").value()
            pathNew = re.sub(r'^Z:', r'//file-cluster/GDC', pathOld)
            pathNew = re.compile(r'^//file-cluster/GDC/Projects/WinxClubII/Production/Render/EXR/', re.IGNORECASE).sub(r'[getenv NK_winxII]/', pathNew)
            pathNew = re.compile(r'^//file-cluster/GDC/Projects/ROMA/Production/Render/EXR/', re.IGNORECASE).sub(r'[getenv NK_roma]/', pathNew)
            if(pathNew != pathOld):
                node.knob("file").setValue(pathNew)
    roma().UploadCamera()

# 根据选择的节点建立Write EXR
# def createExr():
#    createExrProc(True)
#
# def createExrProc(publish):
#    sel = nuke.selectedNodes()
#    if(len(sel) != 1):
#        nuke.message("请选择一个节点")
#        return
#    path = getReadFile(sel[0])
#    if(path == ""):
#        nuke.message("出错啦:不能获取输出路径！")
#        return
#    if(re.compile(r'/hairs/', re.IGNORECASE).search(path) != None):
#        reads = []
#        num = getPasses(sel[0], reads)
#        if(num < 6):
#            nuke.message("出错啦:头发应该有6个通道以上！")
#            return
#        findMblur = False
#        for read in reads:
#            if(re.compile(r'/hairs/mblur/', re.IGNORECASE).search(read.knob("file").value()) != None):
#                findMblur = True
#                break
#        if(not findMblur):
#            nuke.message("出错啦:没有mblur通道！")
#            return
#    p = re.compile('_[^_./]+_RX\.[^/]+$', re.IGNORECASE)
#    if(p.search(path) != None):
#        path = p.sub(r'_RX.%04d.exr', path)
#    else:
#        path = re.sub('_[^_]+$', '.%04d.exr', path)
#    p = re.compile('.*/(EVEN|ODD)/(sq_)?([^_/]+)/(sc_)?([^_/]+)(_R)?/(footage/)?([^/]+/(hairs/)?)[^/]+/([^/]+)$', re.IGNORECASE)
#    if(p.match(path) == None):
#        nuke.message("不能获取输出路径")
#        return
#    if(publish):
#        if(p.match(path).group(6) != None):
#            path = p.sub(r'[getenv NK_winxII]/\1/sq_\3/sc_\5/footage\6/\8\10', path)
#        else:
#            path = p.sub(r'[getenv NK_winxII]/\1/sq_\3/sc_\5/footage/\8\10', path)
#        dir = re.sub(r'\[getenv NK_winxII\]', os.environ["NK_winxII"], path)
#        dir = re.sub('/[^/]+$', '', dir)
#        if(not os.path.isdir(dir)):
#            myMd(dir)
#    else:
#        if(p.match(path).group(6) != None):
#            path = p.sub(r'E:/EXR/\1/sq_\3/sc_\5/footage\6/\8\10', path)
#        else:
#            path = p.sub(r'E:/EXR/\1/sq_\3/sc_\5/footage/\8\10', path)
#        dir = re.sub('/[^/]+$', '', path)
#        if(not os.path.isdir(dir)):
#            os.makedirs(dir)
#    sel[0].knob("selected").setValue(False)
#    render_order = getRenderOrder()
#    exr = nuke.createNode("Write")
#    exr.knob("xpos").setValue(sel[0].knob("xpos").value() + 50)
#    exr.knob("ypos").setValue(sel[0].knob("ypos").value() + 50)
#    exr.knob("file_type").setValue("exr")
#    exr.knob("file").setValue(path)
#    exr.knob("channels").setValue("all")
# exr.knob("compression").setValue(0)
#    exr.knob("render_order").setValue(render_order)
#    exr.setInput(0, sel[0])


def createExrProcEx(publish, isRx):
    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message("请选择一个节点")
        return
    path = getReadFile(sel[0])
    if(path == ""):
        nuke.message("出错啦:不能获取输出路径！")
        return
    if(re.compile(r'/hairs/', re.IGNORECASE).search(path) != None):
        reads = []
        num = getPasses(sel[0], reads)
        if(num < 6):
            nuke.message("出错啦:头发应该有6个通道以上！")
            return
        findMblur = False
        for read in reads:
            if(re.compile(r'/hairs/mblur/', re.IGNORECASE).search(read.knob("file").value()) != None):
                findMblur = True
                break
        if(not findMblur):
            nuke.message("出错啦:没有mblur通道！")
            return
    filename = re.search(r'[^/\\]+$', path).group(0)
    p = re.compile(r'_?RX([_.])', re.IGNORECASE)
    if(p.search(filename) != None):
        filename = p.sub(r'\1', filename)
    if(isRx):
        filename = re.sub('_[^_]+$', '_RX.%04d.exr', filename)
    else:
        filename = re.sub('_[^_]+$', '.%04d.exr', filename)
    path = re.sub(r'[^/\\]+$', filename, path)
    p = re.compile('.*/(EVEN|ODD)/(sq_)?([^_/]+)/(sc_)?([^_/]+)(_R)?/(footage/)?([^/]+/(hairs/)?)[^/]+/([^/]+)$', re.IGNORECASE)
    if(p.match(path) == None):
        nuke.message("不能获取输出路径")
        return
    if(publish):
        if(isRx):
            path = p.sub(r'[getenv NK_roma]/\1/sq_\3/sc_\5/footage_R/\8\10', path)
        else:
            path = p.sub(r'[getenv NK_roma]/\1/sq_\3/sc_\5/footage_L/\8\10', path)
        dir = re.sub(r'\[getenv NK_winxII\]', os.environ["NK_winxII"], path)
        dir = re.sub('/[^/]+$', '', dir)
        if(not os.path.isdir(dir)):
            myMd(dir)
    else:
        if(isRx):
            path = p.sub(r'E:/EXR/\1/sq_\3/sc_\5/footage_R/\8\10', path)
        else:
            path = p.sub(r'E:/EXR/\1/sq_\3/sc_\5/footage_L/\8\10', path)
        dir = re.sub('/[^/]+$', '', path)
        if(not os.path.isdir(dir)):
            os.makedirs(dir)
    sel[0].knob("selected").setValue(False)
    render_order = getRenderOrder()
    exr = nuke.createNode("Write")
    if(isRx):
        exr.knob("xpos").setValue(sel[0].knob("xpos").value() + 50)
    else:
        exr.knob("xpos").setValue(sel[0].knob("xpos").value() - 50)
    exr.knob("ypos").setValue(sel[0].knob("ypos").value() + 50)
    exr.knob("file_type").setValue("exr")
    exr.knob("file").setValue(path)
    exr.knob("channels").setValue("all")
    # exr.knob("compression").setValue(0)
    exr.knob("render_order").setValue(render_order)
    exr.setInput(0, sel[0])
    if(nuke.views() == ['left', 'right']):
        if(isRx):
            exr.knob("views").setValue('{right}')
            exr.knob("heroview").setValue('right')
        else:
            exr.knob("views").setValue('{left}')
            exr.knob("heroview").setValue('left')
    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)


def romaCreateExrProcEx(publish, LR):
    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message("请选择一个节点")
        return
    source = getReadFile(sel[0])
    if(source == ""):
        nuke.message("出错啦:不能获取输出路径！")
        return

    filename = os.path.basename(source)
    filename = re.compile(r'^(sq_[0-9a-z]+_sc_[0-9a-z]+_[0-9a-z]+(_hairs)?)(_[0-9a-z]+)*_(left|right)\..*$', re.IGNORECASE).sub(r'\g<1>_%s.0001.exr' % (LR), filename)
    filename = re.compile(r'_hairs_(left|right)\.', re.IGNORECASE).sub(r'_fur_\g<1>.', filename)
    if filename == os.path.basename(source):
        nuke.message("出错啦:不能获取输出路径！")
        return

    s = pyUtil.idmtService("ImagePublish", filename)
    buf = re.compile(r'\|').split(s)
    if len(buf) < 4:
        nuke.message("出错啦:不能获取输出路径！")
        return
    folder = re.sub(r'\\', r'/', buf[1])
    if folder == "":
        nuke.message("出错啦:不能获取输出路径！")
        return
    filename = filename.replace('.0001.exr', '.%04d.exr')

    if(publish):
        if(not os.path.isdir(folder)):
            myMd(folder)
        folder = re.compile(r'^//file-cluster/GDC/Projects/ROMA/Production/Render/EXR/', re.IGNORECASE).sub(r'[getenv NK_roma]/', folder)
    else:
        folder = re.compile(r'^//file-cluster/GDC/Projects/ROMA/Production/Render/', re.IGNORECASE).sub(r'E:/', folder)
        if(not os.path.isdir(folder)):
            os.makedirs(folder)
    sel[0].knob("selected").setValue(False)
    render_order = getRenderOrder()
    exr = nuke.createNode("Write")
    if LR == 'right':
        exr.knob("xpos").setValue(sel[0].knob("xpos").value() + 50)
    else:
        exr.knob("xpos").setValue(sel[0].knob("xpos").value() - 50)
    exr.knob("ypos").setValue(sel[0].knob("ypos").value() + 50)
    exr.knob("file_type").setValue("exr")
    exr.knob("file").setValue(folder + '/' + filename)
    exr.knob("channels").setValue("all")
    exr.knob("render_order").setValue(render_order)
    exr.setInput(0, sel[0])
    if(nuke.views() == ['left', 'right']):
        if LR == 'right':
            exr.knob("views").setValue('{right}')
            exr.knob("heroview").setValue('right')
        else:
            exr.knob("views").setValue('{left}')
            exr.knob("heroview").setValue('left')
    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)


def getReadFile(node):
    path = ""
    if(node != None):
        if(node.Class() == "Read"):
            return (node.knob("file").value())
        for i in range(node.inputs()):
            path = getReadFile(node.input(i))
            if(path != ""):
                return path
    return path

# 得到EXR的通道数


def getPasses(node, passes):
    num = 0
    if(node != None):
        if(node.Class() == "Read"):
            try:
                i = passes.index(node)
            except:
                passes.append(node)
                num = num + 1
        for i in range(node.inputs()):
            num = num + getPasses(node.input(i), passes)
    return num


def mySysFile(action, source, dest):
    print '%s \"%s\" \"%s\"' % (action, source, dest)

    #source = GetUNC(source)
    source = re.compile(r'^Z:', re.IGNORECASE).sub(r'//file-cluster/GDC', source)
    source = re.compile(r'^([A-KM-Z]):', re.IGNORECASE).sub(r'//%s/\g<1>$' % os.getenv('COMPUTERNAME'), source)

    ss = '%s%%%%%s%%%%%s%%%%%s' % (os.getenv('USERNAME'), action, source, dest)

    import suds
    client = suds.client.Client('http://cq-file02/CheckinService.asmx?wsdl')
    reply = client.service.cmd(ss)

    if reply == 'True':
        return True
    else:
        print reply
        return False

def myMd(dir):
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.connect(('192.168.168.152', 2345))
    #sock.send(os.getenv('USERNAME') + r'%%md%%' + dir + '%%')
    #sock.close()
    mySysFile("md", dir, "")


def myCopy(source, dest):
    source = re.compile(r'^Z:', re.IGNORECASE).sub(r'//file-cluster/GDC', source)
    source = re.compile(r'^([a-z]):', re.IGNORECASE).sub(r'//%s/\g<1>$' % os.getenv('COMPUTERNAME'), source)

    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.connect(('192.168.168.152', 2345))
    #command = '%s%%%%%s%%%%%s%%%%%s' % (os.getenv('USERNAME'), 'copy', source, dest)
    #sock.send(command)
    #sock.recv(1024)
    #sock.close()
    mySysFile("copy", source, dest)


def getRenderOrder():
    render_order = 0
    for node in nuke.allNodes():
        if(node.Class() == "Write"):
            current = node.knob("render_order").value()
            if(current > render_order):
                render_order = current
    render_order = render_order + 1
    return render_order

# DeRelative Path
# def deRelative():
#    for node in nuke.allNodes():
#        if(node.Class() == "Read" or node.Class() == "Write"):
#            pathOld = node.knob("file").value()
#            pathNew = pathOld
#            pathNew = re.sub(r'^Z:', r'//file-cluster/GDC', pathNew)
#            pathNew = re.sub(r'\[getenv NK_winxII\]', r'//file-cluster/GDC/Projects/WinxClubII/Production/Render/Lighting_Passes', pathNew)
#            if(pathNew != pathOld):
#                node.knob("file").setValue(pathNew)

# Disable Write Exr


def disableWriteExr():
    for node in nuke.allNodes():
        if(node.Class() == "Write"):
            if(node.knob("file_type").value() == "exr"):
                node.knob("disable").setValue(True)

# Disable Write


def disableWrite():
    for node in nuke.allNodes():
        if(node.Class() == "Write"):
            node.knob("disable").setValue(True)

# Check EXR Path


def checkRead(envName):
    find = False
    for node in nuke.allNodes():
        node.knob("selected").setValue(False)
    p = re.compile(r'^\[getenv \"?' + envName + r'\"?\]', re.IGNORECASE)
    for node in nuke.allNodes():
        if node.Class() != "Write":
            file = node.knob("file")
            if(file != None):
                path = file.value()
                if(p.match(path) == None and path != ""):
                    find = True
                    node.knob("selected").setValue(True)
    if(find):
        nuke.message("发现路径不规范的Read节点！\n\n不规范的Read节点已经被选上")
    else:
        nuke.message("没有发现路径不规范的Read节点！")


# 根据选择的Write EXR节点建立Read EXR
def exrReadByWrite():
    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message("请选择一个节点")
        return
    write = sel[0]
    if(write.Class() != "Write"):
        return
    write.knob("selected").setValue(False)
    path = write.knob("file").value()
    myPath = re.sub(r'\[getenv NK_winxII\]', os.environ["NK_winxII"], path)
    myPath = re.sub(r'\[getenv NK_roma\]', os.environ["NK_roma"], path)
    cmd = "file {" + myPath
    seq = IsSequence(path)
    if(seq != None):
        first = re.search(r'\.([^.]+)\.[^.]+$', seq[0]).group(1)
        last = re.search(r'\.([^.]+)\.[^.]+$', seq[len(seq) - 1]).group(1)
        cmd += " " + first + "-" + last
    cmd += "}"
    read = nuke.createNode("Read", cmd, inpanel=True)
    read.knob("file").setValue(path)
    read.knob("ypos").setValue(write.knob("ypos").value() + 80)
    for node in nuke.allNodes():
        for i in range(node.inputs()):
            if(node.input(i) == write):
                node.setInput(i, read)

# Check EXR Path


def checkMuster():
    find = False
    for node in nuke.allNodes():
        node.knob("selected").setValue(False)
    p = re.compile(':')
    for node in nuke.allNodes():
        file = node.knob("file")
        if(file != None):
            path = file.value()
            if(p.search(path) != None):
                find = True
                node.knob("selected").setValue(True)
    if(find):
        nuke.message("发现路径指向本机的节点！\n\n路径指向本机的Read节点已经被选上")
    else:
        nuke.message("没有发现路径指向本机的节点！")


def ATW_material():
    for node in nuke.allNodes():
        file = node.knob("file")
        if(file != None):
            pathOld = node.knob("file").value()
            pathNew = re.compile(r'^Z:', re.IGNORECASE).sub(r'//file-cluster/GDC', pathOld)
            pathNew = re.compile(r'^//file-cluster/GDC/Projects/ATW/Production/Render/', re.IGNORECASE).sub(r'[getenv ATW_material]/', pathNew)
            if(pathNew != pathOld):
                node.knob("file").setValue(pathNew)


def getUnc(path):
    unc = re.compile(r'^Z:', re.IGNORECASE).sub(r'//file-cluster/GDC', path)
    unc = re.compile(r'^//file-cluster/GDC/Projects/WinxClubII/Production/Render/EXR/', re.IGNORECASE).sub(r'[getenv NK_winxII]/', unc)
    unc = re.compile(r'^//file-cluster/GDC/Projects/ROMA/Production/Render/EXR/', re.IGNORECASE).sub(r'[getenv NK_roma]/', unc)
    return unc


def getRight(left):
    right = left
    if(re.compile(r'/footage(_R)?/', re.IGNORECASE).search(left) != None):
        right = re.compile(r'/footage/', re.IGNORECASE).sub(r'/footage_R/', left)
    else:
        right = re.compile(r'/sc_([^_/]+)/', re.IGNORECASE).sub(r'/sc_\1_R/', left)
    right = re.compile(r'_RX(\.[^/]+)$', re.IGNORECASE).sub(r'\1', right)
    right = re.compile(r'([^/.]+)(\.[^/]+)$', re.IGNORECASE).sub(r'\1_RX\2', right)
    return right


def getLeft(right):
    left = right
    left = re.compile(r'_R/', re.IGNORECASE).sub('/', left)
    left = re.compile(r'_RX(\.[^/]+)$', re.IGNORECASE).sub(r'\1', left)
    return left


def matchStereo(left, right):
    p = re.compile(r'(/[^./]+\.)[^./]+(\.[^./]+)$')
    str1 = left
    if(p.search(left) != None):
        str1 = p.sub(r'\1#\2', left)
    str2 = right
    if(p.search(right) != None):
        str2 = p.sub(r'\1#\2', right)
    return (str1.lower() == str2.lower())


def RX():
    for node in nuke.allNodes():
        for knob in node.knobs():
            if(node.knob(knob).Class() == "File_Knob"):
                pathOld = node.knob(knob).value()
                if(pathOld != ""):
                    pathNew = pathOld
                    if(re.compile(r'/footage(_R)?/', re.IGNORECASE).search(pathOld) != None):
                        pathNew = re.compile(r'/footage/', re.IGNORECASE).sub(r'/footage_R/', pathNew)
                    else:
                        pathNew = re.compile(r'/sc_([^_/]+)/', re.IGNORECASE).sub(r'/sc_\1_R/', pathNew)
                    pathNew = re.compile(r'_RX(\.[^/]+)$', re.IGNORECASE).sub(r'\1', pathNew)
                    pathNew = re.compile(r'([^/.]+)(\.[^/]+)$', re.IGNORECASE).sub(r'\1_RX\2', pathNew)
                    if(pathNew != pathOld):
                        if(node.Class() == "Write"):
                            dir = re.sub(r'\[getenv NK_winxII\]', os.environ["NK_winxII"], pathNew)
                            dir = re.sub('/[^/]+$', '', dir)
                            if(not os.path.isdir(dir)):
                                myMd(dir)
                        node.knob(knob).setValue(pathNew)


def checkStereo():
    rs = False
    for node in nuke.allNodes():
        node.knob("selected").setValue(False)
    for node in nuke.allNodes():
        if(node.Class() == "Viewer"):
            continue
        for i in range(node.inputs()):
            if(node.input(i) == None):
                continue
            if(node.input(i).Class() == "Read"):
                file = getUnc(node.input(i).knob("file").value())
                if(re.compile(r'/background/', re.IGNORECASE).search(file) != None):
                    continue
                right = getRight(file)
                left = getLeft(file)
                find = False
                if(right != file):
                    for j in range(node.inputs()):
                        if(node.input(j) == None):
                            continue
                        if(node.input(j).Class() == "Read"):
                            if(matchStereo(getUnc(node.input(j).knob("file").value()), right)):
                                find = True
                                break
                elif(left != file):
                    for j in range(node.inputs()):
                        if(node.input(j) == None):
                            continue
                        if(node.input(j).Class() == "Read"):
                            if(matchStereo(getUnc(node.input(j).knob("file").value()), left)):
                                find = True
                                break
                else:
                    find = True
                if(not find):
                    rs = True
                    node.knob("selected").setValue(True)
    if(rs):
        nuke.message("发现独眼素材！\n\n节点已经被选上")
    else:
        nuke.message("没有发现独眼素材！")


# def createMerge(nodeType):
#    for leftNode in nuke.allNodes():
#        if(leftNode.Class() == "Read"):
#            for node in nuke.selectedNodes():
#                node.knob("selected").setValue(False)
#            leftNode.knob("selected").setValue(True)
#            nuke.nodeCopy("%clipboard%")
#            for node in nuke.selectedNodes():
#                node.knob("selected").setValue(False)
#            rightNode = nuke.nodePaste("%clipboard%")
#            leftPath = leftNode.knob("file").value()
#            rightPath = getRight(leftPath)
#            rightNode.knob("file").setValue(rightPath)
#            rightNode.knob("xpos").setValue(leftNode.knob("xpos").value() + 100)
#            rightNode.knob("ypos").setValue(leftNode.knob("ypos").value())
#            for outputNode in nuke.allNodes():
#                for i in range(outputNode.inputs()):
#                    if(outputNode.input(i) == leftNode):
#                        for node in nuke.selectedNodes():
#                            node.knob("selected").setValue(False)
#                        mergeNode = nuke.createNode(nodeType)
#                        mergeNode.setInput(0, leftNode)
#                        mergeNode.setInput(1, rightNode)
#                        outputNode.setInput(i, mergeNode)
#                        mergeNode.knob("xpos").setValue(outputNode.knob("xpos").value())
#                        mergeNode.knob("ypos").setValue(outputNode.knob("ypos").value() - 50)

def createMerge(nodeType):
#    for view in nuke.views():
#        nuke.deleteView(view)
#    nuke.addView("left")
#    nuke.addView("right")
#    nuke.root().knob("views_colours").setValue(True)
    if nuke.views() != ['left', 'right']:
        nuke.message("请先\"Set up views for stereo\"")
        return
    for leftNode in nuke.allNodes():
        if(leftNode.Class() == "Read"):
            for node in nuke.selectedNodes():
                node.knob("selected").setValue(False)
            leftNode.knob("selected").setValue(True)
            mergeNode = nuke.createNode(nodeType)
            for node in nuke.selectedNodes():
                node.knob("selected").setValue(False)
            leftNode.knob("selected").setValue(True)
            nuke.nodeCopy("%clipboard%")
            rightNode = nuke.nodePaste("%clipboard%")
            leftPath = leftNode.knob("file").value()
            rightPath = getRight(leftPath)
            rightNode.knob("file").setValue(rightPath)
            mergeNode.setInput(0, leftNode)
            mergeNode.setInput(1, rightNode)
            rightNode.knob("xpos").setValue(leftNode.knob("xpos").value() + 100)
            rightNode.knob("ypos").setValue(leftNode.knob("ypos").value())
            mergeNode.knob("xpos").setValue(leftNode.knob("xpos").value() + 50)
            mergeNode.knob("ypos").setValue(leftNode.knob("ypos").value() + 100)


def romaGetRight(left):
    right = left
    right = re.compile(r'/footage_L/', re.IGNORECASE).sub(r'/footage_R/', right)
    right = re.compile(r'_left\.', re.IGNORECASE).sub(r'_right.', right)
    return right


def romaCreateMerge(nodeType):
#    for view in nuke.views():
#        nuke.deleteView(view)
#    nuke.addView("left")
#    nuke.addView("right")
#    nuke.root().knob("views_colours").setValue(True)
    for leftNode in nuke.allNodes():
        if(leftNode.Class() == "Read"):
            for node in nuke.selectedNodes():
                node.knob("selected").setValue(False)
            leftNode.knob("selected").setValue(True)
            mergeNode = nuke.createNode(nodeType)
            for node in nuke.selectedNodes():
                node.knob("selected").setValue(False)
            leftNode.knob("selected").setValue(True)
            nuke.nodeCopy("%clipboard%")
            rightNode = nuke.nodePaste("%clipboard%")
            leftPath = leftNode.knob("file").value()
            rightPath = romaGetRight(leftPath)
            rightNode.knob("file").setValue(rightPath)
            mergeNode.setInput(0, leftNode)
            mergeNode.setInput(1, rightNode)
            rightNode.knob("xpos").setValue(leftNode.knob("xpos").value() + 100)
            rightNode.knob("ypos").setValue(leftNode.knob("ypos").value())
            mergeNode.knob("xpos").setValue(leftNode.knob("xpos").value() + 50)
            mergeNode.knob("ypos").setValue(leftNode.knob("ypos").value() + 100)


def selectByType():
    nodeType = None
    for node in nuke.selectedNodes():
        nodeType = node.Class()
        break
    p = nuke.Panel("Select by Type")
    nodeTypeLabel = "节点类型:"
    p.addSingleLineInput(nodeTypeLabel, nodeType)
    p.addButton("Cancel")
    p.addButton("OK")
    result = p.show()
    if(result == 1):
        nodeType = p.value(nodeTypeLabel)
        for node in nuke.allNodes():
            node.knob("selected").setValue(node.Class() == nodeType)


def GetAnimByFilename():
    path = nuke.root().knob("name").getValue()
    if path == "":
        for node in nuke.allNodes():
            if(node.Class() == "Read" or node.Class() == "Write"):
                path = node.knob("file").value()
                if path != "":
                    break
    anim = pyUtil.GetAnimByFilename(path)
    if 'fps' in anim:
        nuke.root().knob("fps").setValue(anim['fps'])
    if 'frmStart' in anim:
        nuke.root().knob("first_frame").setValue(anim['frmStart'])
    if 'frmEnd' in anim:
        nuke.root().knob("last_frame").setValue(anim['frmEnd'])
    if 'resolutionW' in anim and 'resolutionH' in anim:
        format = None
        for f in nuke.formats():
            if f.width() == anim['resolutionW'] and f.height() == anim['resolutionH']:
                format = f
                break
        if format == None:
            format = nuke.addFormat(str(anim['resolutionW']) + ' ' + str(anim['resolutionH']) + ' 1 ' + anim['name'])
        nuke.root().knob("format").setValue(format)
    nuke.showSettings()

# Local -> Production


def Local2Production():
    for node in nuke.allNodes():
        if(node.Class() == "Read"):
            pathOld = node.knob("file").value()
            if pathOld == "":
                continue
            filename = re.search(r'[^/\\]+$', pathOld).group(0)
            myFilename = re.sub(r'(([/\\]|^)[^/\\.]+\.)[^/\\]+$', r'\g<1>1001.iff', pathOld)
            str = pyUtil.idmtService("ImagePublish", myFilename)
            buf = re.compile(r'\|').split(str)
            if len(buf) < 4:
                continue
            folder = re.sub(r'\\', r'/', buf[1])
            if folder == "":
                continue
            # if not os.path.isdir(folder):
            #    continue
            pathNew = folder + r'/' + filename
            if(pathNew != pathOld):
                node.knob("file").setValue(pathNew)


def createLeftRight(views):
    if nuke.views() != ['left', 'right']:
        nuke.message("请先\"Set up views for stereo\"")
        return
    for read in nuke.allNodes():
        if(read.Class() == "Read"):
            path = read.knob("file").value()
            if(path == ""):
                continue
            filetitle = re.search(r'[^.]+', re.search(r'[^/\\]+$', path).group(0)).group(0)
            filetitle = re.compile('_RX$', re.IGNORECASE).sub("", filetitle)
            filetitle = re.compile('rx', re.IGNORECASE).sub("", filetitle)
            sq = ""
            sc = ""
            if re.compile(r'^sq_[0-9a-z]+_sc_[0-9a-z]+', re.IGNORECASE).match(filetitle) != None:
                buf = re.compile(r'_').split(filetitle)
                sq = buf[1]
                sc = buf[3]
            else:
                continue
            parity = getParity(sq)
            dir = "//file-cluster/GDC/Netrender/Scenes/WinxClubII/" + parity + "/sq_" + sq + "/sc_" + sc
            if views.count("left") == 1:
                leftDir = dir + "/" + filetitle
                if(not os.path.isdir(leftDir)):
                    os.makedirs(leftDir)
                leftPath = leftDir + "/" + filetitle + ".%04d.tif"
                for node in nuke.selectedNodes():
                    node.knob("selected").setValue(False)
                left = nuke.createNode("Write")
                left.setInput(0, read)
                left.knob("xpos").setValue(read.knob("xpos").value() - 100)
                left.knob("ypos").setValue(read.knob("ypos").value() + 100)
                left.knob("file").setValue(leftPath)
                left.knob("views").setValue('{left}')
                left.knob("file_type").setValue("tiff")
                left.knob("datatype").setValue("16 bit")
                left.knob("compression").setValue(0)
            if views.count("right") == 1:
                filetitle = filetitle + "_RX"
                rightDir = dir + "/" + filetitle
                if(not os.path.isdir(rightDir)):
                    os.makedirs(rightDir)
                rightPath = rightDir + "/" + filetitle + ".%04d.tif"
                for node in nuke.selectedNodes():
                    node.knob("selected").setValue(False)
                right = nuke.createNode("Write")
                right.setInput(0, read)
                right.knob("xpos").setValue(read.knob("xpos").value() + 100)
                right.knob("ypos").setValue(read.knob("ypos").value() + 100)
                right.knob("file").setValue(rightPath)
                right.knob("views").setValue('{right}')
                right.knob("file_type").setValue("tiff")
                right.knob("datatype").setValue("16 bit")
                right.knob("compression").setValue(0)


def romaCreateLeftRight(views):
    if nuke.views() != ['left', 'right']:
        nuke.message("请先\"Set up views for stereo\"")
        return
    for read in nuke.allNodes():
        if(read.Class() == "Read"):
            path = read.knob("file").value()
            if(path == ""):
                continue
            filetitle = re.search(r'[^.]+', re.search(r'[^/\\]+$', path).group(0)).group(0)
            filetitle = re.compile('_(left|right)$', re.IGNORECASE).sub("", filetitle)
            sq = ""
            sc = ""
            if re.compile(r'^sq_[0-9a-z]+_sc_[0-9a-z]+', re.IGNORECASE).match(filetitle) != None:
                buf = re.compile(r'_').split(filetitle)
                sq = buf[1]
                sc = buf[3]
            else:
                continue
            parity = getParity(sq)
            dir = "//file-cluster/GDC/Netrender/Scenes/ROMA/" + parity + "/sq_" + sq + "/sc_" + sc
            if views.count("left") == 1:
                leftDir = dir + "/" + filetitle + "_left"
                if(not os.path.isdir(leftDir)):
                    os.makedirs(leftDir)
                leftPath = leftDir + "/" + filetitle + "_left.%04d.tif"
                for node in nuke.selectedNodes():
                    node.knob("selected").setValue(False)
                left = nuke.createNode("Write")
                left.setInput(0, read)
                left.knob("xpos").setValue(read.knob("xpos").value() - 100)
                left.knob("ypos").setValue(read.knob("ypos").value() + 100)
                left.knob("file").setValue(leftPath)
                left.knob("views").setValue('{left}')
                left.knob("file_type").setValue("tiff")
                left.knob("datatype").setValue("16 bit")
                left.knob("compression").setValue(0)
            if views.count("right") == 1:
                filetitle = filetitle + "_right"
                rightDir = dir + "/" + filetitle
                if(not os.path.isdir(rightDir)):
                    os.makedirs(rightDir)
                rightPath = rightDir + "/" + filetitle + "_right.%04d.tif"
                for node in nuke.selectedNodes():
                    node.knob("selected").setValue(False)
                right = nuke.createNode("Write")
                right.setInput(0, read)
                right.knob("xpos").setValue(read.knob("xpos").value() + 100)
                right.knob("ypos").setValue(read.knob("ypos").value() + 100)
                right.knob("file").setValue(rightPath)
                right.knob("views").setValue('{right}')
                right.knob("file_type").setValue("tiff")
                right.knob("datatype").setValue("16 bit")
                right.knob("compression").setValue(0)


def outputComposition():
    '''
    TTMS: Output Composition
    Z:\Projects\TTMS\Production\Compositing\Pre_Compositing\EVEN\010_seq\000c\left
    '''
    if nuke.views() != ['left', 'right']:
        nuke.message("请先\"Set up views for stereo\"")
        return
    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message("请选择一个节点")
        return
    sq = ""
    sc = ""
    for read in nuke.allNodes():
        if(read.Class() == "Read"):
            path = read.knob("file").value()
            if(path == ""):
                continue
            (dir, filename) = os.path.split(path)
            if re.compile(r'^ts_[0-9a-z]+_[0-9a-z]+_', re.IGNORECASE).match(filename) != None:
                buf = re.compile(r'_').split(filename)
                sq = buf[1]
                sc = buf[2]
                break
    if sq == "" or sc == "":
        nuke.message("不能从素材中获得镜头号")
        return
    parity = getParity(sq)
    folder = "//file-cluster/GDC/Projects/TTMS/Production/Compositing/Pre_Compositing/" + parity + "/" + sq + "_seq/" + sc
    filename = "ts_" + sq + "_" + sc + "_cp_c001.%04d.tif"

    leftFolder = folder + "/left"
    for root, dirs, files in os.walk(leftFolder):
        for file in files:
            if re.compile('^ts_' + sq + '_' + sc + r'_cp_c001\.[0-9]{4}\.tif', re.IGNORECASE).match(file) != None:
                if nuke.ask("左眼序列已经存在，是否覆盖？") == False:
                    return
                break
    if(not os.path.isdir(leftFolder)):
        os.makedirs(leftFolder)
    #leftPath = leftFolder + "/" + filename
    leftPath = leftFolder + "/" + "ts_" + sq + "_" + sc + "_cp_c001.%04d.tif"
    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    left = nuke.createNode("Write")
    left.setInput(0, sel[0])
    left.knob("xpos").setValue(sel[0].knob("xpos").value() - 100)
    left.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    left.knob("file").setValue(leftPath)
    left.knob("views").setValue('{left}')
    left.knob("file_type").setValue("tiff")
    left.knob("datatype").setValue("16 bit")
    left.knob("compression").setValue("LZW")
    left.knob("render_order").setValue(1)

    rightFolder = folder + "/right"
    for root, dirs, files in os.walk(rightFolder):
        for file in files:
            if re.compile('^ts_' + sq + '_' + sc + r'_cp_c001_RX\.[0-9]{4}\.tif', re.IGNORECASE).match(file) != None:
                if nuke.ask("右眼序列已经存在，是否覆盖？") == False:
                    return
                break
    if(not os.path.isdir(rightFolder)):
        os.makedirs(rightFolder)
    #rightPath = rightFolder + "/" + filename
    rightPath = rightFolder + "/" + "ts_" + sq + "_" + sc + "_cp_c001_RX.%04d.tif"
    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    right = nuke.createNode("Write")
    right.setInput(0, sel[0])
    right.knob("xpos").setValue(sel[0].knob("xpos").value() + 100)
    right.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    right.knob("file").setValue(rightPath)
    right.knob("views").setValue('{right}')
    right.knob("file_type").setValue("tiff")
    right.knob("datatype").setValue("16 bit")
    right.knob("compression").setValue("LZW")
    right.knob("render_order").setValue(2)


def outputComposition1(projectShort='ss', projectLong='ShenShou'):
    '''
    TTMS: Output Composition
    Z:\Projects\TTMS\Production\Compositing\Pre_Compositing\EVEN\010_seq\000c\left
    '''
    if nuke.views() != ['left', 'right']:
        nuke.message("请先\"Set up views for stereo\"")
        return
    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message("请选择一个节点")
        return
    sq = ""
    sc = ""
    for read in nuke.allNodes():
        if(read.Class() == "Read"):
            path = read.knob("file").value()
            if(path == ""):
                continue
            (dir, filename) = os.path.split(path)
            if re.compile(r'^%s_[0-9a-z]+_[0-9a-z]+_' % (projectShort), re.IGNORECASE).match(filename) != None:
                buf = re.compile(r'_').split(filename)
                sq = buf[1]
                sc = buf[2]
                break
    if sq == "" or sc == "":
        nuke.message("不能从素材中获得镜头号")
        return
    parity = getParity(sq)
    folder = r'//file-cluster/GDC/Projects/%s/Production/Render/Compositing/%s/sq_%s/sc_%s' % (projectLong, parity, sq, sc)
    #filename = "ts_" + sq + "_" + sc + "_cp_c001.%04d.tif"

    leftFolder = folder + "/left"
    for root, dirs, files in os.walk(leftFolder):
        for file in files:
            if re.compile(r'^%s_%s_%s_cp_left\.[0-9]{4}\.tif' % (projectShort, sq, sc), re.IGNORECASE).match(file) != None:
                if nuke.ask("左眼序列已经存在，是否覆盖？") == False:
                    return
                break
    if(not os.path.isdir(leftFolder)):
        os.makedirs(leftFolder)
    #leftPath = leftFolder + "/" + filename
    leftPath = leftFolder + "/" + r'%s_%s_%s_cp_left.%%04d.tif' % (projectShort, sq, sc)
    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    left = nuke.createNode("Write")
    left.setInput(0, sel[0])
    left.knob("xpos").setValue(sel[0].knob("xpos").value() - 100)
    left.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    left.knob("file").setValue(leftPath)
    left.knob("views").setValue('{left}')
    left.knob("file_type").setValue("tiff")
    left.knob("datatype").setValue("16 bit")
    left.knob("compression").setValue("LZW")
    left.knob("render_order").setValue(1)

    rightFolder = folder + "/right"
    for root, dirs, files in os.walk(rightFolder):
        for file in files:
            if re.compile(r'^%s_%s_%s_cp_right\.[0-9]{4}\.tif' % (projectShort, sq, sc), re.IGNORECASE).match(file) != None:
                if nuke.ask("右眼序列已经存在，是否覆盖？") == False:
                    return
                break
    if(not os.path.isdir(rightFolder)):
        os.makedirs(rightFolder)
    #rightPath = rightFolder + "/" + filename
    rightPath = rightFolder + "/" + r'%s_%s_%s_cp_right.%%04d.tif' % (projectShort, sq, sc)
    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    right = nuke.createNode("Write")
    right.setInput(0, sel[0])
    right.knob("xpos").setValue(sel[0].knob("xpos").value() + 100)
    right.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    right.knob("file").setValue(rightPath)
    right.knob("views").setValue('{right}')
    right.knob("file_type").setValue("tiff")
    right.knob("datatype").setValue("16 bit")
    right.knob("compression").setValue("LZW")
    right.knob("render_order").setValue(2)

# 替换素材路径


def replaceRead():
    searchLabel = 'Search:'
    replaceLabel = 'Replace:'
    searchStr = ''
    replaceStr = ''
    p = nuke.Panel("替换素材路径")
    p.addSingleLineInput(searchLabel, searchStr)
    p.addSingleLineInput(replaceLabel, replaceStr)
    p.addButton("Cancel")
    p.addButton("OK")
    result = p.show()
    if(result == 1):
        searchStr = p.value(searchLabel)
        replaceStr = p.value(replaceLabel)
        nodes = nuke.allNodes()
        for node in nodes:
            if node.Class() == "Read":
                pathOld = node.knob("file").value()
                #pathNew = re.sub(re.escape(searchStr), re.escape(replaceStr), pathOld)
                pathNew = re.compile(re.escape(searchStr), re.IGNORECASE).sub(replaceStr.replace('\\', '/'), pathOld)
                if(pathNew != pathOld):
                    node.knob("file").setValue(pathNew)


def PathRelateToRoot():
    errStr = ''
    dirty = False
    path = nuke.root().knob("name").getValue()
    if path == "":
        nuke.message("请先存盘到 images 目录，使用完本工具以后需要再次存盘")
        return
    if re.compile('/images(/|$)', re.IGNORECASE).search(os.path.dirname(path)) == None:
        nuke.message("请先存盘到 images 目录，使用完本工具以后需要再次存盘")
        return
    for node in nuke.allNodes():
        if node.Class() == "Read":
            pathOld = node.knob("file").value()
            if re.search(r'^\[', pathOld) != None or pathOld == '':
                continue
            pathNew = re.compile('.*/images/', re.IGNORECASE).sub(r'[file dirname [knob root.name]]/', pathOld)
            if pathNew != pathOld:
                node.knob("file").setValue(pathNew)
                dirty = True
            else:
                errStr = '%s\n%s' % (errStr, node.knob("name").value())
    if errStr != '':
        nuke.message('以下素材并不是存放在 images 目录，无法替换成相对路径\n' + errStr)
    elif dirty:
        nuke.message('素材路径已经替换成相对，请检查，无误后需要再次存盘')


def single2sequence():
    patterns = {r'\.(\d{4})\.': '.%04d.', r'_(\d{4})\.': '_%04d.'}

    for node in nuke.allNodes():
        if node.Class() == "Read":
            path = node.knob("file").value()
            (folder, filename) = os.path.split(path)

            pattern = None
            s = None
            for p in patterns:
                s = re.sub(p, patterns[p], filename)
                if s != filename:
                    pattern = p
                    break
            if pattern == None:
                continue

            first = None
            last = None
            folder = re.sub(r'\[getenv NK_roma\]', os.environ["NK_roma"], folder)
            frames = os.listdir(folder)
            for frame in frames:
                if s != re.sub(pattern, patterns[pattern], frame):
                    continue

                m = re.search(pattern, frame)
                i = int(m.group(1))
                if first == None or last == None:
                    first = i
                    last = i
                elif i < first:
                    first = i
                elif i > last:
                    last = i
            if first == last:
                continue

            path = path.replace(filename, s)
            node.knob('file').setValue(path)
            node.knob('first').setValue(first)
            node.knob('last').setValue(last)
        elif node.Class() == "Write":
            path = node.knob("file").value()
            path = re.sub(r'\.(\d{4})\.', '.%04d.', path)
            node.knob('file').setValue(path)


class importShot(object):

    def __init__(self):
        importFolder()
        return

        sqLabel = 'SQ:'
        scLabel = 'SC:'
        sq = ''
        sc = ''
        p = nuke.Panel("Import EXR's footage_L")
        p.addSingleLineInput(sqLabel, sq)
        p.addSingleLineInput(scLabel, sc)
        p.addButton("Cancel")
        p.addButton("OK")
        result = p.show()
        if(result == 1):
            xpos = 0
            sq = p.value(sqLabel)
            sc = p.value(scLabel)
            parity = getParity(sq)
            footage_L = r'\\file-cluster\GDC\Projects\ROMA\Production\Render\EXR\%s\sq_%s\sc_%s\footage_L' % (parity, sq, sc)

            for root, dirs, files in os.walk(footage_L):
                done = {}
                for i in range(len(files)):
                    s = re.sub(r'\.(\d{4})\.', '.%04d.', files[i])
                    s1 = s.lower()

                    if s != files[i]:
                        m = re.search(r'\.(\d{4})\.', files[i])
                        k = int(m.group(1))

                        if s1 in done:
                            if k < done[s1][2]:
                                done[s1][2] = k
                            elif k > done[s1][3]:
                                done[s1][3] = k
                        else:
                            done[s1] = [s, files[i], k, k]

                for s1 in done:
                    command = ''
                    if(done[s1][2] != done[s1][3]):
                        path = os.path.join(root, done[s1][0]).replace('\\', '/')
                        command = 'file {%s %d-%d}' % (path, done[s1][2], done[s1][3])
                    else:
                        path = os.path.join(root, done[s1][1]).replace('\\', '/')
                        command = 'file {%s}' % path

                    node = nuke.createNode("Read", command, inpanel=True)
                    node.knob("file").setValue(re.compile(r'^//file-cluster/GDC/Projects/ROMA/Production/Render/EXR/', re.IGNORECASE).sub(r'[getenv NK_roma]/', path))
                    node.knob("xpos").setValue(xpos)
                    node.knob("ypos").setValue(100)
                    xpos += 100

                done.clear()


def importFolder():
    p = nuke.Panel("Import Footage Within Folder")
    p.setWidth(480)
    folderLabel = 'Folder'
    folder = ''
    p.addFilenameSearch(folderLabel, folder)
    p.addButton("Cancel")
    p.addButton("OK")
    result = p.show()
    if result == 1:
        folder = p.value(folderLabel)
    if not os.path.isdir(folder):
        return
    xpos = 0
    for root, dirs, files in os.walk(folder):
        done = {}
        for i in range(len(files)):
            s = re.sub(r'\.(\d{4})\.', '.%04d.', files[i])
            s1 = s.lower()

            if s != files[i]:
                m = re.search(r'\.(\d{4})\.', files[i])
                k = int(m.group(1))

                if s1 in done:
                    if k < done[s1][2]:
                        done[s1][2] = k
                    elif k > done[s1][3]:
                        done[s1][3] = k
                else:
                    done[s1] = [s, files[i], k, k]

        for s1 in done:
            command = ''
            if(done[s1][2] != done[s1][3]):
                path = os.path.join(root, done[s1][0]).replace('\\', '/')
                command = 'file {%s %d-%d}' % (path, done[s1][2], done[s1][3])
            else:
                path = os.path.join(root, done[s1][1]).replace('\\', '/')
                command = 'file {%s}' % path

            node = nuke.createNode("Read", command, inpanel=False)
            path = re.compile(r'^Z:', re.IGNORECASE).sub(r'//file-cluster/GDC', path)
            path = re.compile(r'^//file-cluster/GDC/Projects/ROMA/Production/Render/EXR/', re.IGNORECASE).sub(r'[getenv NK_roma]/', path)
            node.knob("file").setValue(path)
            node.knob("xpos").setValue(xpos)
            node.knob("ypos").setValue(100)
            xpos += 100

        done.clear()


class roma(object):

    def UploadCamera(self):
        sceneName = nuke.root().knob('name').value()
        sceneName = os.path.basename(sceneName)
        m = re.compile(r'^rm1_[0-9a-z]+_([0-9a-z]+)_([0-9a-z]+)(_|\.)', re.IGNORECASE).match(sceneName)
        if m == None:
            return
        sq = m.group(1)
        sc = m.group(2)
        filename = 'cam_sq_%s_sc_%s.fbx' % (sq, sc)
        s = pyUtil.idmtService("ImagePublish", filename)
        buf = re.compile(r'\|').split(s)
        if len(buf) < 2:
            return
        folder = re.sub(r'\\', r'/', buf[1])
        if not os.path.isdir(folder):
            return
        dest = folder + '/' + filename

        for node in nuke.allNodes():
            if node.Class() != "Camera2":
                continue
            source = node.knob("file").value()
            if source == '':
                continue
            if re.compile(r'^\[getenv \"?NK_roma\"?\]', re.IGNORECASE).match(source) != None:
                continue
            if not os.path.isfile(source):
                continue
            if not os.path.isfile(dest):
                myCopy(source, dest)
            if not os.path.isfile(dest):
                continue

            dest = re.compile(r'^//file-cluster/GDC/Projects/ROMA/Production/Render/EXR/', re.IGNORECASE).sub(r'[getenv NK_roma]/', dest)
            node.knob('file').setValue(dest)

# 改自Woodlies.py


def writeNode_gt():
    if nuke.views() != ['left', 'right']:
        nuke.message(u"请先\"Set up views for stereo\"")
        return

    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message('请选择一个节点')
        return

    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)
    m = re.compile(r'^gt_([^_\.]+)_(Q\d+)_(S\d+)[_\.]', re.IGNORECASE).search(filename)
    if m == None:
        nuke.message('不能从文件名获得镜头号')
        return
    ep = m.group(1)
    sq = m.group(2)
    sc = m.group(3)
    parity = getParity(ep)

    s = nuke.getInput(r'tk num', '1')
    if s == None:
        return
    if re.search('\d{1,3}', s) == None:
        return
    tk = int(s)

    folder = '//file-cluster/GDC/Projects/GummiTarzan/Production/Render/Compositing/%s/ep_%s/%s/%s/tk%d' % (parity, ep, sq, sc, tk)

    overWrite = False
    for view in ['left', 'right']:
        if overWrite:
            break
        path = os.path.join(folder, view)
        if os.path.isdir(path):
            filenames = os.listdir(path)
            for filename in filenames:
                if re.compile(r'gt_%s_%s_%s_%s_cp_c%03d\.\d{4}\.tiff$' % (ep, sq, sc, view, tk), re.IGNORECASE).search(filename) != None:
                    if nuke.ask('序列已经存在，是否覆盖？') == False:
                        return
                    overWrite = True
                    break

    overWrite = False
    for view in ['left', 'right']:
        path = os.path.join(folder, view)
        if not os.path.isdir(path):
            os.makedirs(path)

    filename = 'gt_%s_%s_%s_%%V_cp_c%03d.%%04d.tiff' % (ep, sq, sc, tk)
    path = '%s/%%V/%s' % (folder, filename)

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("file_type").setValue("tiff")
    node.knob("datatype").setValue(1)
    node.knob("compression").setValue(0)

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)
# 改自gt


def writeNode_ot():
    if nuke.views() != ['left', 'right']:
        nuke.message(u"请先\"Set up views for stereo\"")
        return

    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message('请选择一个节点')
        return

    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)
    m = re.compile(r'^ot_([^_\.]+)_(Q\d+)_(S\d+)[_\.]', re.IGNORECASE).search(filename)
    if m == None:
        nuke.message('不能从文件名获得镜头号')
        return
    ep = m.group(1)
    sq = m.group(2)
    sc = m.group(3)
    parity = getParity(ep)

    s = nuke.getInput(r'tk num', '1')
    if s == None:
        return
    if re.search('\d{1,3}', s) == None:
        return
    tk = int(s)

    folder = '//file-cluster/GDC/Projects/OTTO/Production/Render/Compositing/%s/ep_%s/%s/%s/tk%d' % (parity, ep, sq, sc, tk)
    overWrite = False
    for view in ['left', 'right']:
        if overWrite:
            break
        path = os.path.join(folder, view)
        if os.path.isdir(path):
            filenames = os.listdir(path)
            for filename in filenames:
                if re.compile(r'ot_%s_%s_%s_%s_cp_c%03d\.\d{4}\.tiff$' % (ep, sq, sc, view, tk), re.IGNORECASE).search(filename) != None:
                    if nuke.ask('序列已经存在，是否覆盖？') == False:
                        return
                    overWrite = True
                    break

    overWrite = False
    for view in ['left', 'right']:
        path = os.path.join(folder, view)
        if not os.path.isdir(path):
            os.makedirs(path)

    filename = 'ot_%s_%s_%s_%%V_cp_c%03d.%%04d.tiff' % (ep, sq, sc, tk)
    path = '%s/%%V/%s' % (folder, filename)

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("file_type").setValue("tiff")
    node.knob("datatype").setValue(1)
    node.knob("compression").setValue(0)

    node.knob("afterRender").setValue('import Ninjago_TK_Version as njtk\nreload(njtk)\nnjtk.copySingleFrame(\"OTTO\")')

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)


def writeNode_eq():
    if nuke.views() != ['left', 'right']:
        nuke.message(u"请先\"Set up views for stereo\"")
        return

    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message('请选择一个节点')
        return

    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)
    m = re.compile(r'^eq_([^_\.]+)_([^_\.]+)[_\.]', re.IGNORECASE).search(filename)
    if m == None:
        nuke.message('不能从文件名获得镜头号')
        return
    ep = m.group(1)
    sq = m.group(2)
    #sc = m.group(3)
    parity = getParity(ep)

    s = '1'
    if s == None:
        return
    if re.search('\d{1,3}', s) == None:
        return
    tk = int(s)

    folder = '//file-cluster/GDC/Projects/Earthquake/Production/Render/Compositing/%s/%s/%s' % (parity, ep, sq)
    overWrite = False
    for view in ['left', 'right']:
        if overWrite:
            break
        path = os.path.join(folder, view)
        if os.path.isdir(path):
            filenames = os.listdir(path)
            for filename in filenames:
                if re.compile(r'eq_%s_%s_%s_cp_c%03d\.\d{4}\.tiff$' % (ep, sq, view, tk), re.IGNORECASE).search(filename) != None:
                    if nuke.ask('序列已经存在，是否覆盖？') == False:
                        return
                    overWrite = True
                    break

    overWrite = False
    for view in ['left', 'right']:
        path = os.path.join(folder, view)
        if not os.path.isdir(path):
            os.makedirs(path)

    filename = 'eq_%s_%s_%%V_cp_c%03d.%%04d.tiff' % (ep, sq, tk)
    path = '%s/%%V/%s' % (folder, filename)

    # for node in nuke.selectedNodes():
    #    node.knob("selected").setValue(False)
    # cropNode=nuke.createNode('Crop')
    #cropNode.knob('box').setValue([160, 16, 2720, 784])
    # cropNode.knob('reformat').setValue('true')
    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("file_type").setValue("tiff")
    node.knob("datatype").setValue(1)
    node.knob("compression").setValue(0)

    node.knob("afterRender").setValue('import Ninjago_TK_Version as njtk\nreload(njtk)\nnjtk.copySingleFrame(\"Earthquake\")')

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)


def writeNode_sk():
    # if nuke.views() != ['left', 'right']:
        #nuke.message(u"请先\"Set up views for stereo\"")
        # return

    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message('请选择一个节点')
        return

    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)
    m = re.compile(r'^sk_(\d+)_(\d+)[_\.]', re.IGNORECASE).search(filename)
    #modify with liangyu
    q = re.compile(r'^sk_(\d+)_(\d+)(\w)[_\.]', re.IGNORECASE).search(filename)
    if m == None and q== None:
        nuke.message('不能从文件名获得镜头号')
        return
    if q!=None:
        m=q
        sq = m.group(2)+m.group(3)                   
    else:        
        sq = m.group(2)          
    ep = m.group(1)
    parity = getParity(ep)
    #modify with liangyu     
    s = nuke.getInput(r'tk num', '1')
    if s == None:
        return
    if re.search('\d{1,3}', s) == None:
        return
    tk = int(s)

    folder = '//file-cluster/GDC/Projects/Strawberry/Production/Render/Compositing/%s/ep_%s/sq_%s/tk%d' % (parity, ep, sq, tk)
    overWrite = False
    # for view in ['left', 'right']:
        # if overWrite:
            # break
    path = os.path.join(folder)
    if os.path.isdir(path):
        filenames = os.listdir(path)
        for filename in filenames:
            if re.compile(r'sk_%s_%s_cp_c%03d\.\d{4}\.tga$' % (ep, sq, tk), re.IGNORECASE).search(filename) != None:
                if nuke.ask('序列已经存在，是否覆盖？') == False:
                    return
                overWrite = True
                break

    overWrite = False
    # for view in ['left', 'right']:
    # for view in ['main']:
    path = os.path.join(folder)
    if not os.path.isdir(path):
        # os.makedirs(path)
        myMd(path)

    filename = 'sk_%s_%s_cp_c%03d.%%04d.tga' % (ep, sq, tk)
    path = '%s/%s' % (folder, filename)

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("file_type").setValue("targa")
    # node.knob("datatype").setValue(1)
    node.knob("compression").setValue("none")

    node.knob("afterRender").setValue('import Ninjago_TK_Version as njtk\nreload(njtk)\nnjtk.copySingleFrame(\"Strawberry\")')

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)


def writeNode_vv(daType=1):
    sel = nuke.selectedNodes()
    if len(sel) != 1:
        nuke.message('请选择一个节点')
        return

    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)
    m = re.compile(r'^((vv_([a-z0-9]+)_([a-z0-9]+)_([a-z0-9]+)_(keylight|lighting|comp))_([0-9]{2}))\.nk', re.IGNORECASE).search(filename)
    if m == None:
        msg = '''文件命名不规范！nuke文件名命名:

VV_集_场次_镜头号_keylight_版本号.nk
VV_集_场次_镜头号_lighting_版本号.nk
VV_集_场次_镜头号_comp_版本号.nk

例如:
VV_CA_040_0010_keylight_01.nk'''
        nuke.message(msg)
        return
    title = m.group(1)
    titleWithoutTk = m.group(2)
    ep = m.group(3)
    sq = m.group(4)
    sc = m.group(5)
    mode = m.group(6)
    version = m.group(7)
    parity = getParity(ep)

    folder = '//file-cluster/GDC/Projects/VickyTheViking/Production/Render/Compositing/%s/EP_%s/SQ_%s/SC_%s/precomp/%s_%s' % (
        parity, ep, sq, sc, titleWithoutTk, datetime.datetime.now().strftime('%y%m%d'))
    if not os.path.isdir(folder):
        myMd(folder)

    filename = '%s.%%04d.tiff' % (title)

    if daType != 1:
        filename = '%s_%s_%s_lighting_v%s.%%04d.tiff' % (ep, sq, sc, version)

    path = '%s/%s' % (folder, filename)

    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("colorspace").setValue("sRGB")
    node.knob("file_type").setValue("tiff")
    node.knob("datatype").setValue(daType)
    node.knob("compression").setValue(0)

#===============================================================================
# for dod3               by zhangben  modefy  20130220
#===============================================================================
#=============modefy by zhangben  add function parameter =20131218=============================


def writeNode_do(drive=u'L:', proj=u'DiveollyDive5', proj_abb=u'do5', tk_fn=''):
    if nuke.views() != ['left', 'right']:
        nuke.message(u"pleaseSet up views for stereo")
        return
    #=================================================================
    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message(u'select a node')
        return

    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)
    m = re.compile(ur'^%s_(\d+[a-z]*)_(\d+[a-z]*)[_\.]' % proj_abb, re.IGNORECASE).search(filename)
    if m == None:
        nuke.message(u'cant')
        return
    ep = m.group(1)
    sc = m.group(2)
    parity = getParity(ep)
    tk = 1

    targetPath = '%s/Projects/%s/Production/Render/Compositing/%s/%s/%s%s' % (drive, proj, parity, ep, sc, tk_fn)
    tk_names = []
    tkPathes = []
    for root, dirs, files in os.walk(targetPath):
        for dir in dirs:
            tkPathes.append(os.path.join(root, dir))
            if dir.rfind("tk") != -1:
                tk_names.append(dir)
                tk_names.sort()
    if len(tk_names) != 0:
        p_num = re.compile("[0-9]+")
        p_num_tail = re.compile("[0-9]+$")
        tk_No = int(p_num_tail.search(tk_names[-1]).group(0))
        tk = tk_No
        new_tk_No = str(int(tk_No) + 1)
        tkOldPath = "%s\\%s" % (targetPath, tk_names[-1])
        tk_path_ltter = p_num_tail.sub("", tkPathes[0])

        tkNewPath = tk_path_ltter + new_tk_No
        if nuke.ask('YES:覆盖原序列 ,TK+1!! NO:TK不变') == True:
            try:
                os.rename(tkOldPath, tkNewPath)
                tk = int(new_tk_No)
                for root, dirs, files in os.walk(tkNewPath):
                    for fileName in files:
                        newFN = fileName.replace("c%03d" % (int(tk_No)), "c%03d" % (int(new_tk_No)))
                        old_fileFullName = os.path.join(root, fileName)
                        new_fileFullName = os.path.join(root, newFN)
                        os.rename(old_fileFullName, new_fileFullName)
            except:
                nuke.message("原序列无法覆盖，将创建新路径")
                tk = int(new_tk_No)
                os.mkdir(tkNewPath)
                for view in ['left', 'right']:
                    path = os.path.join(tkNewPath, view)
                    if not os.path.isdir(path):
                        os.makedirs(path)

    else:
        folder = '%s/Projects/%s/Production/Render/Compositing/%s/%s/%s%s/tk%d' % (drive, proj, parity, ep, sc, tk_fn, tk)
        for view in ['left', 'right']:
            path = os.path.join(folder, view)
            if not os.path.isdir(path):
                os.makedirs(path)

    folder = '%s/Projects/%s/Production/Render/Compositing/%s/%s/%s%s/tk%d' % (drive, proj, parity, ep, sc, tk_fn, tk)

    if tk_fn == "/tk_fn":
        filename = '%s_%s_%s_%%V_cp_fn.%%04d.tiff' % (proj_abb, ep, sc)
    else:
        filename = '%s_%s_%s_%%V_cp_c%03d.%%04d.tiff' % (proj_abb, ep, sc, tk)
    path = '%s/%%V/%s' % (folder, filename)

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("file_type").setValue("tiff")
    node.knob("datatype").setValue(1)
    node.knob("compression").setValue(0)

    #node.knob("afterRender").setValue('import Ninjago_TK_Version as njtk\nreload(njtk)\nnjtk.copySingleFrame(\"%s\")' % proj)

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)
    nuke.scriptSave()

 #=====================================================================================================


def writeNode_Ch():
    if nuke.views() != ['left', 'right']:
        nuke.message(u"请先\"Set up views for stereo\"")
        return

    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message('请选择一个节点')
        return

    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)
    m = re.compile(r'^ch_([^_\.]+)_([^_\.]+)[_\.]', re.IGNORECASE).search(filename)
    if m == None:
        nuke.message('不能从文件名获得镜头号')
        return
    ep = m.group(1)
    sq = m.group(2)
    #sc = m.group(3)
    parity = getParity(ep)

    s = '1'
    if s == None:
        return
    if re.search('\d{1,3}', s) == None:
        return
    tk = int(s)

    folder = '//file-cluster/GDC/Projects/DomesticProject/ChinaImage/Production/Render/Compositing/%s/%s/%s' % (parity, ep, sq)
    overWrite = False
    for view in ['left', 'right']:
        if overWrite:
            break
        path = os.path.join(folder, view)
        if os.path.isdir(path):
            filenames = os.listdir(path)
            for filename in filenames:
                if re.compile(r'ch_%s_%s_%s_cp_c%03d\.\d{4}\.png$' % (ep, sq, view, tk), re.IGNORECASE).search(filename) != None:
                    if nuke.ask('序列已经存在，是否覆盖？') == False:
                        return
                    overWrite = True
                    break

    overWrite = False
    for view in ['left', 'right']:
        path = os.path.join(folder, view)
        if not os.path.isdir(path):
            myMd(path)

    filename = 'ch_%s_%s_%%V_cp_c%03d.%%04d.png' % (ep, sq, tk)
    path = '%s/%%V/%s' % (folder, filename)

    # for node in nuke.selectedNodes():
    #    node.knob("selected").setValue(False)
    # cropNode=nuke.createNode('Crop')
    #cropNode.knob('box').setValue([160, 16, 2720, 784])
    # cropNode.knob('reformat').setValue('true')
    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("file_type").setValue("png")
    node.knob("datatype").setValue("16 bit")
    # node.knob("datatype").setValue(1)
    # node.knob("compression").setValue(0)

    #node.knob("afterRender").setValue('import Ninjago_TK_Version as njtk\nreload(njtk)\nnjtk.copySingleFrame(\"DomesticProject/ChinaImage\")')

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)


#===============================================================================
# for dod3               by zhangben  modefy  20130306
#===============================================================================
#=============modefy by zhangben  add function parameter =20131218=============================
def writeFinalNode_do(drive=u'L:', proj=u'DiveollyDive4', proj_abb=u'do4'):  # ============添加最终16位tiff wirte 节点
    if nuke.views() != ['left', 'right']:
        nuke.message(u"pleaseSet up views for stereo")
        return
    #=================================================================
    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message(u'select a node')
        return

    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)
    m = re.compile(r'^%s_(\d+[a-z]*)_(\d+[a-z]*)[_\.]' % proj_abb, re.IGNORECASE).search(filename)
    if m == None:
        nuke.message(u'cant')
        return
    ep = m.group(1)
    sc = m.group(2)
    parity = getParity(ep)
    tk_final = 'fn'

    folder = u'%s/Projects/%s/Production/Render/Compositing/%s/ep_%s/sc_%s/tk_%s' % (drive, proj, parity, ep, sc, tk_final)
    for view in ['left', 'right']:
        path = os.path.join(folder, view)
        if not os.path.isdir(path):
            os.makedirs(path)
    filename = '%s_%s_%s_%%V_cp_fn.%%04d.tiff' % (proj_abb, ep, sc)
    path = '%s/%%V/%s' % (folder, filename)

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("file_type").setValue("tiff")
    node.knob("datatype").setValue(1)
    node.knob("compression").setValue(0)

    #node.knob("afterRender").setValue(u'import Ninjago_TK_Version as njtk\nreload(njtk)\nnjtk.copySingleFrame(\"%s\")'%(proj))

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)
    nuke.scriptSave()

#============Add For QS Project ===========||||||||||||==================================


def writeNode_qs():
    sel = nuke.selectedNodes()
    if len(sel) != 1:
        nuke.message('please select a node')
        return

    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)
    m = re.compile(r'^((qs_([a-z0-9]+)_([a-z0-9]+)_([a-z0-9]+)_(keylight|lighting|comp))_([0-9]{2}))\.nk', re.IGNORECASE).search(filename)

    m = re.compile(r'^qs_(\d+[a-z]*)_(\d+[a-z]*)[_\.]', re.IGNORECASE).search(filename)

    if m == None:
        msg = '''file name nonstandard'''
        nuke.message(msg)
        return

    sq = m.group(1)
    sc = m.group(2)

    parity = getParity(sq)

    s = nuke.getInput(r'tk num', '1')
    if s == None:
        return
    if re.search('\d{1,3}', s) == None:
        return
    tk = int(s)

    folder = '//file-cluster/GDC/Projects/Qsanguo/Production/Render/Compositing/%s/SQ_%s/SC_%s/tk%d' % (parity, sq, sc, tk)
    if not os.path.isdir(folder):
        myMd(folder)

    writeFN = '%s.%%04d.tiff' % (os.path.splitext(filename)[0])

    path = '%s/%s' % (folder, writeFN)

    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("colorspace").setValue("sRGB")
    node.knob("file_type").setValue("tiff")
    node.knob("datatype").setValue(1)
    node.knob("compression").setValue(2)
    node.knob("afterRender").setValue('import Ninjago_TK_Version as njtk\nreload(njtk)\nnjtk.copySingleFrame(\"Qsanguo\")')
    
    
def writeNode_North():

    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message('请选择一个节点')
        return

    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)
    '''
    m = re.compile(r'^ice_(\d+)_(\d+)[_\.]', re.IGNORECASE).search(filename)
    #modify with liangyu
    q = re.compile(r'^ice_(\d+)_(\d+)(\w)[_\.]', re.IGNORECASE).search(filename)
    if m == None and q== None:
        nuke.message('不能从文件名获得镜头号')
        return
    if q!=None:
        m=q
        sq = m.group(2)+m.group(3)                   
    else:        
        sq = m.group(2)          
    ep = m.group(1)
    '''
    ep=''
    sq=''
    shotInfo = commonGetShotInfo()
    if shotInfo:
        if shotInfo[1]:
            ep=shotInfo[1]
        if shotInfo[2]:
            sq=shotInfo[2]  
    else:
        nuke.message('不能从文件名获得镜头号')
        return         
    parity = getParity(ep)
    #modify with liangyu     
    s = nuke.getInput(r'tk num', '1')
    if s == None:
        return
    if re.search('\d{1,3}', s) == None:
        return
    tk = int(s)

    folder = '//file-cluster/GDC/Projects/North/Production/Render/Compositing/%s/ep_%s/sq_%s/tk%d' % (parity, ep, sq, tk)
    overWrite = False
    # for view in ['left', 'right']:
        # if overWrite:
            # break
    path = os.path.join(folder)
    if os.path.isdir(path):
        filenames = os.listdir(path)
        for filename in filenames:
            if re.compile(r'ice_%s_%s_cp_c%03d\.\d{4}\.tga$' % (ep, sq, tk), re.IGNORECASE).search(filename) != None:
                if nuke.ask('序列已经存在，是否覆盖？') == False:
                    return
                overWrite = True
                break

    overWrite = False

    path = os.path.join(folder)
    if not os.path.isdir(path):
        # os.makedirs(path)
        myMd(path)

    filename = 'ice_%s_%s_cp_c%03d.%%04d.tga' % (ep, sq, tk)
    path = '%s/%s' % (folder, filename)

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("file_type").setValue("targa")
    # node.knob("datatype").setValue(1)
    node.knob("compression").setValue("none")

    node.knob("afterRender").setValue('import Ninjago_TK_Version as njtk\nreload(njtk)\nnjtk.copySingleFrame(\"North\")')

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)
        
        
        
def writeFinalNode_North():
 
    sel = nuke.selectedNodes()
    if(len(sel) != 1):
        nuke.message('请选择一个节点')
        return

    filename = nuke.root().knob('name').value()
    filename = os.path.basename(filename)
    

    ep=''
    sq=''
    shotInfo = commonGetShotInfo()
    if shotInfo:
        if shotInfo[1]:
            ep=shotInfo[1]
        if shotInfo[2]:
            sq=shotInfo[2]  
    else:
        nuke.message('不能从文件名获得镜头号')
        return   
    
    import pyUtil3 as pyUtil
    tk = pyUtil.idmtService("GetTk", "North|rendering|ice_%s_%s_cp" % ( ep, sq ))
    if tk != '1':
        tk = (int(tk) - 1)
    tk=int(tk)                  
    parity = getParity(ep)

    folder = '//file-cluster/GDC/Projects/North/Production/Render/Compositing/%s/ep_%s/sq_%s/final' % (parity, ep, sq )
    overWrite = False
    path = os.path.join(folder)
    if os.path.isdir(path):
        filenames = os.listdir(path)
        for filename in filenames:
            if re.compile(r'ice_sq%s_sc%s_v%03d\.\d{4}\.dpx$' % (ep, sq, tk), re.IGNORECASE).search(filename) != None:
                if nuke.ask('序列已经存在，是否覆盖？') == False:
                    return
                overWrite = True
                break

    overWrite = False

    path = os.path.join(folder)
    if not os.path.isdir(path):
        # os.makedirs(path)
        myMd(path)

    filename = 'ice_sq%s_sc%s_v%03d.%%04d.dpx' % (ep, sq, tk)
    path = '%s/%s' % (folder, filename)

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    node = nuke.createNode("Write")
    node.knob("ypos").setValue(sel[0].knob("ypos").value() + 100)
    node.knob("file").setValue(path)
    node.knob("colorspace").setValue("linear")
    node.knob("file_type").setValue("dpx")
    node.knob("datatype").setValue("16")        
    #nuke.toNode(node.name()).knob(21).setValue(2)  
      
    node.knob("afterRender").setValue('import Ninjago_TK_Version as njtk\nreload(njtk)\nnjtk.copySingleFrame(\"North\")')

    for node in nuke.selectedNodes():
        node.knob("selected").setValue(False)
    for node in sel:
        node.knob("selected").setValue(True)
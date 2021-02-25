# -*- coding: utf-8 -*-
'''
@Title:file_name

Created on 2014年9月18日

@author: zhangben

@Description:todo
'''
import maya.cmds as mc
import re
import os
import maya.mel as mel
from pymel.core import *
import getpass 
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.DOD.scripts import dod_RenderArnoldLayer 
reload(dod_RenderArnoldLayer)
class dod_rnd_kit(object):
    ins_skic = sk_infoConfig.sk_infoConfig()
    ins_dod_arnTools = dod_RenderArnoldLayer.hh_RenderArnold()
    def __init__(self):
        pass
    def do_rnd_expChrLight(self,lightType = u'Chr'):#=================导出上传角色灯,bg灯==========================
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        chr_light_grp = selected()[0]
        try:
            lightChild = [eachChilder.getShape() for eachChilder in chr_light_grp.getChildren() if nodeType(eachChilder.getShape()) in listNodeTypes(u'light')]
        except:
            error(u'================You must export group objects ===================')
        if not lightChild:
            error(u'===============You selected groups has no light in it==================')
        #=============================dispose namespace ================================
        for each_child in chr_light_grp.listRelatives(ad=True,c=True):
            each_nsp = each_child.namespace()
            if each_nsp:
                get_node = Namespace(each_nsp).ls()
                for each_node in get_node:
                    print u'Node %s  namespaceString is %s' % (each_node,each_nsp)
                    each_node.rename(each_node.stripNamespace())
        #==============================================================================
        p_chrLight = re.compile(u'msh_%s_light' % lightType,re.I)
        if not p_chrLight.match(chr_light_grp.name()):
            chr_light_grp.rename(u'MSH_%s_light' % lightType)
        sys_temp = os.environ["TMP"] #
        currentMayaLocation = os.getenv('MAYA_LOCATION')
        my_btch_app_path = os.path.normpath(os.path.join(currentMayaLocation,u'bin/mayabatch.exe'))
        #====================find checkin file==============================================
        light_file_name = ''
        file_path_serv = u'%s/scenes/Animation/episode_%s/scene_%s/%slight' % (serverPath,shotInfo[1],shotInfo[2],lightType)
        if os.path.exists(file_path_serv):
            get_ls = os.listdir(file_path_serv)
            if get_ls:
                for eachFile in get_ls:
                    fullName = os.path.join(file_path_serv,eachFile)
                    if os.path.isfile(fullName) and os.path.splitext(fullName)[-1] in [u'.ma','.mb']:
                        light_file_name = os.path.split(fullName)[-1]
                        checkOut_fileInfo = u'2|%s|%s|%s' % (projectInfo,light_file_name,getpass.getuser() )
                        cmd_str = u'idmtService \"Checkout\" \"%s\"' % checkOut_fileInfo
                        mel.eval(cmd_str)
                        break
            else:
                light_file_name = u'%s_%s_%s_chrlight_c001.mb' % (shotInfo[0],shotInfo[1],shotInfo[2]) 
        else:
            light_file_name = u'%s_%s_%s_chrlight_c001.mb' % (shotInfo[0],shotInfo[1],shotInfo[2]) 
        light_file_name_full = os.path.join(sys_temp,light_file_name)
        exportSelected(light_file_name_full,type=u'mayaBinary',force=True)
        excute_scripts_file = u'//file-cluster/gdc/Resource/Support/Maya/projects/DODV/do_export_chrLight_cmdScript.mel'
        excute_cmd = u"%s -file \"%s\" -script \"%s \"" % (my_btch_app_path,light_file_name_full,excute_scripts_file)
        os.popen(excute_cmd)
    def assign_dis_clr_material():#===========================指定一个用于显示的lambert 材质球======================
        user_sel_objs = mc.ls(sl=True,l=True)
        SG_LS = []
        for eachObj in user_sel_objs:
            shp = mc.listRelatives(eachObj,s=True,f=True,ni=True) 
            if shp and mc.nodeType(shp[0]) == u'mesh':
                SG_node = mc.listConnections(shp[0],t=u'shadingEngine')
                if SG_node[0] in SG_LS:
                    continue
                else:
                    print '==============================%s On work !!===============================' % (eachObj)        
                    material_nd = mc.listConnections(u'%s.surfaceShader' % SG_node[0])
                    if material_nd[0].find('DISLAMBERT') != -1:
                        continue
                    else:              
                        #upstream_tx_Attr = mc.listConnections(u'%s.color'%material_nd[0],p=True)
                        upstream_tx_Attr = mc.listConnections(u'%s.emissionColor'%material_nd[0],p=True) #上游节点输出到emission color 的值,比较接近正确显示的颜色
                        obj_DisClr = mc.getAttr(upstream_tx_Attr)
                        #obj_outClr = mc.getAttr('%s.outColor'%material_nd[0])
                        #obj_clr = mc.getAttr('%s.color'%material_nd[0])
                        #obj_clr = mc.colorAtPoint(eachObj,o='RGB',u=(.5, 0.0), v=(.5, 0.1))
                        #===创建lambert 材质球，用于显示
                        dis_lamb =mc.shadingNode('lambert',asShader =True,n = u'%sDISLAMBERT_'%material_nd[0]) 
                        mc.setAttr(u'%s.color'%dis_lamb,obj_DisClr[0][0],obj_DisClr[0][1],obj_DisClr[0][2])
                        mc.disconnectAttr(u'%s.outColor'%material_nd[0],u'%s.surfaceShader'%SG_node[0])
                        mc.connectAttr(u'%s.outColor'% dis_lamb,u'%s.surfaceShader'%SG_node[0])
                        mc.connectAttr(u'%s.outColor'% material_nd[0],u'%s.aiSurfaceShader'%SG_node[0])
                        SG_LS.append(SG_node[0])
    def export_specialObjects(objs,path,server=0):
        pass
    def op_anim_file(self,projAbbreviation = u'do5'):#========打开指定的动画文件
        scene_num = textField(u'scen_num_tx',q=True,text=True)
        shot_num = textField(u'shotNum_tx',q=True,text=True)
        projName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(projAbbreviation) 
        if not scene_num or not shot_num:
            error(u'==========Type scene number and shot number first')
        servPath = ur'\\file-cluster\gdc\Projects\%s\Project\scenes\Animation' % projName
        scene_folder = u'episode_%s' % scene_num
        shot_folder = u'scene_%s' % shot_num
        episodePath = os.path.join(servPath,scene_folder)
        shotPath = os.path.join(episodePath,shot_folder)
        anim_fileFolder = os.path.join(shotPath,u'anim')
        if not os.path.exists(anim_fileFolder): error(u'请输入正确的场次镜头')
        containmentList = os.listdir(anim_fileFolder)
        if not containmentList: return
        openFile_fn = ''
        for eachOne in containmentList:
            fullName = os.path.join(anim_fileFolder,eachOne)
            if os.path.isfile(fullName) and os.path.splitext(fullName)[-1] in [u'.ma','.mb']:
                openFile_fn = fullName
                break
        openFile(openFile_fn,f=True,loadAllDeferred=True)
        self.ins_dod_arnTools.ArnoldRendererSettings()
        self.ins_dod_arnTools.csl_RefIm()
        select(ls(type=u'mesh',ni=True))
        self.ins_dod_arnTools.ArnoldShaderAssign(u'aiStand')
        if checkBox(u'op_chb',q=True,v=True): mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
#=========================batch eval mel tool====================================================================
    def check_sel_cmdStr2Server(self,pattern = u'shot'):#====把脚本编辑器里选择的mel指令上传到数据库为分层工具调用=====================
        if pattern == u'shot':
            shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0]) 
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            all_cmdSCrField = lsUI(type = "cmdScrollFieldExecuter")
            SelTexts = []
            for eachField in all_cmdSCrField:
                selTextStr =  eachField.getSelectedText()
                if selTextStr: SelTexts.append(selTextStr)
            if len(SelTexts) >1: 
                error(u'==检查脚本编辑器,确保只有一个标签项有被选择的脚本代码用于上传==')
            elif len(SelTexts) == 0:
                warning(u'==当前并没有选择的代码用于上传==’')
            #melStorPath = os.path.join(serverPath,u'mel')
            melStorPath = u'//file-cluster/GDC/Projects/%s/%s_Scratch/mel' % (projectInfo,projectInfo)
            melFilePath = u''
            shotMelPath  = u'%s/episode_%s/scene_%s' % (melStorPath,shotInfo[1],shotInfo[2])
            if not os.path.exists(shotMelPath):
                os.makedirs(shotMelPath)
            melFilePath = u'%s/shot_%s_%s_rndMel.mel' % (shotMelPath,shotInfo[1],shotInfo[2])
            if os.path.exists(melFilePath):
                if uitypes.ConfirmDialog(t = u'Confirm',m = u'脚本文件已存在确认覆盖？',b= [u'Yes',u'Cancel'],db = u'Yes',cb=u'Cancel') == u'Yes':
                    os.remove(melFilePath) 
                    mel_file = file(melFilePath,'a')
                    mel_file.write(SelTexts[0].encode('utf-8'))
                    mel_file.close()
                    
                else:
                    pass
            else:
                mel_file = file(melFilePath,'a')
                mel_file.write(SelTexts[0].encode('utf-8'))
                mel_file.close()
        elif pattern == u'batch':
            do_show_batchEvalMelWin()
    def do_show_batchEvalMelWin(self):
        import idmt.maya.DOD.scripts.dod_rnd_kit as dork
        reload(dork)
        ins_dork = dork.dod_rnd_kit()
        if mc.window(u'do_evalMel_ui',exists=True): mc.deleteUI(u'do_evalMel_ui')
        evalMel_Win = mc.loadUI(uiFile = u'//file-cluster/gdc/Resource/Support/Python/2.6-x64/Lib/site-packages/idmt/maya/DOD/UI/do_batchEvalMel_UI.myuis')
        mc.windowPref(evalMel_Win,topLeftCorner = [100,80])
        mc.showWindow(evalMel_Win)
        self.config_f_tsl()
    def dork_af_btCmd(self):#===============add file button cmd==========================
        baseFilter = "*.ma"    
        addFiles = mc.fileDialog2(fm = 4,caption = 'add file to repatching render',ff="Maya Files (*.ma *.mb)")
        if addFiles != None:
            self.dork_refresh_f_tsl(addFiles)
            #config_f_tsl()
        else:    
            return addFiles
    def dork_refresh_f_tsl(self,fileList): #==============更新fileList=======================
        #fileList = addFiles
        allItemList = mc.textScrollList('f_tsl',q=True,allItems=True)
        if allItemList == None:
            allItemList = []
        for eachFile in fileList:
            if eachFile not in  allItemList:      
                mc.textScrollList('f_tsl',e=True,a=eachFile)            
                allItemList.append(eachFile)
    def brrt_removeItem(self,listContral):#========================================
        itme = mc.textScrollList(listContral,q=True,si=True)
        for eachItem in itme:
            mc.textScrollList(listContral,e=True,ri=eachItem)        
    def config_f_tsl(self):#=========================================
        mc.popupMenu('del_ppm',p='f_tsl',button=3)
        mc.menuItem(l="delete",c = "ins_dork.brrt_removeItem(\'f_tsl\')",p="del_ppm")   
    def paset_scriptsEditorCodes(self):
        all_cmdSCrField = lsUI(type = "cmdScrollFieldExecuter")
        SelTexts = []
        for eachField in all_cmdSCrField:
            selTextStr =  eachField.getSelectedText()
            if selTextStr: SelTexts.append(selTextStr)
        if len(SelTexts) >1: 
            error(u'==检查脚本编辑器,确保只有一个标签项有被选择的脚本代码用于上传==')
        elif len(SelTexts) == 0:
            warning(u'==当前并没有选择的代码用于上传==’')
        codes = SelTexts[0].encode('utf-8')    
        mc.scrollField(u'aa',e=True,text=codes)
    def batchEvalMel_run_BTCMD(self):   
        currentMayaLocation = os.getenv('MAYA_LOCATION')
        my_btch_app_path = os.path.normpath(os.path.join(currentMayaLocation,u'bin/mayabatch.exe'))
        sys_temp = os.environ["TMP"] #
        excute_codes = "%s\nfile -save;" % (scrollField(u'aa',q=True,text=True))
        codes_file = u'%s\\batch_eval_codes.mel' % (sys_temp,)
        if os.path.isfile(codes_file): os.remove(codes_file)
        f_batchEval = open(codes_file,'w')
        f_batchEval.write(excute_codes)
        f_batchEval.close()
        for eachFile in mc.textScrollList(u'f_tsl',q=True,ai=True):
            try:
                excute_cmd = u"%s -file \"%s\" -script \"%s \"" % (my_btch_app_path,eachFile,codes_file)
                os.popen(excute_cmd)  
            except:
                warning(u'==========场景中有物体无法运行代码=================')
                continue
    #=========================================================================================================
    def amendment_shapeLostMaterials(self,server=False):#=====deformed shape nodes, lost material,amendment ===============================
        FileName=mc.file(q=1,sn=1,shn=1)        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0]) 
        userName = os.environ['USERNAME']       
        Project=shotInfo [0]
        fileType=shotInfo[len(shotInfo)-1].split('.')[1]  
        tempath='E:/Info_Temp/temp/RenderLayer/ResetMat/'+shotInfo[1]+'/' 
        mc.sysFile(tempath, makeDir=True)
        non_con_SG = [eachShape for eachShape in ls(u'*:*ShapeDeformed',type = u'mesh',ni=True) if eachShape.listConnections(type=u'shadingEngine') == [] or nt.ShadingEngine(u'initialShadingGroup') in eachShape.listConnections(type=u'shadingEngine')]
        for each_non_mat in non_con_SG:
             sourceShapeNode = [eachShape for eachShape in each_non_mat.getParent().getShapes() if eachShape != each_non_mat]
             if sourceShapeNode:
                 allCon =  each_non_mat.listConnections(type = u'shadingEngine',d=True,p=True,c=True)
                 if allCon:
                     for eachConPair in allCon:
                         if eachConPair[-1].nodeName() == u'initialShadingGroup':eachConPair[0].disconnect()
                 SG_node = sourceShapeNode[0].listConnections(type = u'shadingEngine')
                 if SG_node: 
                     try:    connectAttr(each_non_mat.instObjGroups[0],SG_node[0].dagSetMembers,na=True)
                     except:
                             con_insObjrp = listConnections(each_non_mat.instObjGroups[0],p=True)
                             if con_insObjrp: 
                                 con_insObjrp[0].disconnect()
                                 connectAttr(each_non_mat.instObjGroups[0],SG_node[0].dagSetMembers,na=True)
        mc.file(rename=(tempath+FileName))                
        mc.file(save=1,type = 'mayaBinary',f = 1)
        print u'=====文件保存再%s' % tempath
        if server:
            fileInfo='1|' + projectInfo + '|'  + FileName.split('_c00')[0] +'|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            mel.eval(checkOutCmd) 
            description = u'材质更新文件'
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
        print (u'==========================【%s】材质重置结束==========================' % FileName )       
    def modefy_L2FileCluster(self):
        cfs = ls(type=u'cacheFile')
        for eachCf in cfs:
            pathValue = eachCf.attr(u'cachePath').get()
            eachCf.attr(u'cachePath').set(pathValue.replace(u'L:/',u'\\\\file-cluster\\gdc\\'))
            print u'==============已经修改%s节点的缓存路径到file-cluster=========================' % eachCf
        runtime.saveScene()

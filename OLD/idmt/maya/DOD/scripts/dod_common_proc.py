# -*- coding: utf-8 -*-
'''
@Title:file_name

Created on 2014年10月22日

@author: zhangben

@Description:todo
'''
import maya.cmds as mc
import re
import os
import maya.mel as mel
from pymel.core import *
import pyodbc
import idmt.maya.ShunLiu_common.csl_RenderAutoCommons as csl_RenderAutoCommons
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig;reload(sk_infoConfig)
import idmt.pipeline
class dod_common_proc(object):
    def __init__(self):
        pass
    def setAll2RTNS(self):#=====set all obj to root namespace===================================
        namespace(set = ":")
        nsps = namespaceInfo(lon=True)
        for each in nsps:
            if each not in [u'UI',u'shared']:
                namespace(force=True,mv = (each,u':'))
                Namespace(each).remove()
    def sync_node_attr(self,sourceNode,targetNode,attr_matchStr):#========同步两个节点的某些属性，参数attr_matchStr支持通配符 “ * ”===========
        #attr_matchStr = u'ai*'
        #allAttr = listAttr(sh_node,string = u'ai*')
        #targetNode,sourceNode,eachAttr = sh_def_node,sh_node,allAttr[23]
        list_specAttr = listAttr(sourceNode,string = attr_matchStr)
        for eachAttr in list_specAttr:
            if targetNode.hasAttr(eachAttr):
                try:
                    #print u'++++++++++++++++++Synchronization  %s &&&&  %s \nattribute %s +++++++++++++++++++++++'%(targetNode,sourceNode,eachAttr)
                    sync_attr_str = u'PyNode(\'%s\').%s.set(PyNode(\'%s\').%s.get())'%(targetNode,eachAttr,sourceNode,eachAttr)
                    exec(sync_attr_str)
                except:
                    #print u'====================ATTRIBUTE %s is not a simple value attribute' % eachAttr
                    pass 
    def dod_sync_cacheDriveMesh_Attr(self,*attrDescription):
        ins_cslRAC = csl_RenderAutoCommons.csl_RenderAutoCommons()
        meshchr=ins_cslRAC.csl_meshInfo(meshtype='c')
        meshprp=ins_cslRAC.csl_meshInfo(meshtype='p')
        deformeredObjs =((meshchr + meshprp)[i] for i in range(len(meshchr + meshprp)) if PyNode((meshchr + meshprp)[i]).isIntermediateObject()
                         and (meshchr + meshprp)[i] not in (meshchr + meshprp)[:i]) #select(deformeredObjs())
        p_orig = re.compile(u'shapeorig',re.I)
        for each in deformeredObjs:
            if PyNode(each).isIntermediateObject():
                #each = selected()[0]
                get_meshs = PyNode(each).getShapes()
                sh_node = ''
                sh_def_node = ''
                for eachMesh in get_meshs:
                    if not eachMesh.isIntermediate() and eachMesh.inMesh.isConnected() and eachMesh.name().find(u'Deformed') != -1:
                        sh_def_node = eachMesh
                    elif eachMesh.isIntermediate and not p_orig.search(eachMesh.name()):
                        sh_node = eachMesh
                for eachAttr in attrDescription:
                    try:
                        self.sync_node_attr(sh_node,sh_def_node,eachAttr)
                        #print u'=====%s ai attri sysned==============='%each
                    except:
                        warning(u'==S====OME ISSUE OCCURED WHEN :Sync Node %s Attribute====occur '%each)
                        pass
    #================导入文件指定namespace====不完善，对于在outline里无法显示的一些节点，会继承着不知名的namespace，需要继续完善函数
    def import_file_specialNameSpace(self,im_filePath,spec_ns):#================ == 导入文件，指定namespace
        #im_filePath,spec_ns = tempath+causLightName,u':'
        if os.path.isfile(im_filePath):
            importFile(im_filePath,namespace = u'IM_TEMP_NS')
            Namespace(u'IM_TEMP_NS').setCurrent()
            child_ns = namespaceInfo(lon=True)
            Namespace(child_ns[0]).setCurrent()
            all_im_objs = namespaceInfo(lod=True)
            Namespace(u':').setCurrent()
            if not namespace(exists = spec_ns):
                namespace(add = spec_ns )
            try:
                namespace(mv =[child_ns[0],spec_ns])
            except:
                Namespace(u'IM_TEMP_NS').remove()
                error(u'=========请检查是否已经导入过该文件在场景中======================')
            Namespace(child_ns[0]).remove()
            Namespace(u'IM_TEMP_NS').remove()
        else:
            warning(u'===================没有指定的文件可以导入场景==================')
        
    def dod_listAll_RndMeshes(self):#=====================分别列出场景中CHR,PRP,SET,等且在MODEL组下的meshes=======
        meshes_in_scenes = ls(type = u'mesh',ni=True)
        p_modelGrp = re.compile(u':model',re.I)
        meshes_list_DIC= {}
        for eachMesh in meshes_in_scenes:
        #  eachMesh= selected()[0]
            attributionGrp = eachMesh.getAllParents()[-1]
            if p_modelGrp.search(eachMesh.longName()):
                grp_key_name = attributionGrp.name()
                if not meshes_list_DIC.has_key(grp_key_name):
                    meshes_list_DIC[grp_key_name] = [eachMesh.getParent()]
                else:
                    meshes_list_DIC[grp_key_name].append(eachMesh.getParent())    
        return meshes_list_DIC
    def formatting_fileName_leyerdescrption(self,shotType = 2):
        fileCurName = mc.file(sn=True,q=True)
        fileNmae_spl = os.path.split(fileCurName)
        fileShn = fileNmae_spl[-1]
        fileShn_spl = fileShn.split(u'_')
        #fileShn = u'do5_004_008_l1chrIDP21_lr_c001.mb'
        modefySection = fileShn_spl[shotType+1]
        layerCount = unicode(len([rl for rl in mc.ls(type=u'renderLayer') if not rl.find(u'defaultRenderLayer') > -1]))
        p_num = re.compile(u'[0-9]')
        new_section = p_num.sub(layerCount,modefySection,count=1)
        fileShn_spl[shotType+1] = new_section
        new_fn_shn  = u'_'.join(fileShn_spl)
        new_fn = u'%s/%s' % (fileNmae_spl[0],new_fn_shn)
        if new_fn != fileCurName:
            renameFile(new_fn,rn=True)
            mc.file(save=1,f = 1)
            if os.path.isfile(fileCurName): os.remove(fileCurName)
            return new_fn_shn
        else:
            mc.file(save=1,f = 1)
            return fileShn
    def dod_queryMsSQL_rndInfo(self,project, ep,sc):
        try:
            cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EReader;PWD=123123'%(project))
        except:
            return None
        cursor = cnxn.cursor()
        cmd_sql = '''select PCPE.pcpe_edit5,PCPE.pcpe_edit4,PCPE.pcpe_edit3, PCPE.pcpe_edit1 from dbo.TB_Anim TA  
        left join dbo.TB_Anim_Task TAT on TA.anim_id=TAT.anim_id and TAT.task_mode=\'composite\'
        left join dbo.tb_PageColumnProjectEdit PCPE on TAT.task_id=PCPE.pcpe_taskid and PCPE.pcpe_tasktype=\'anim\'
        where TA.anim_ep=\'%s\' and TA.anim_sc=\'%s\''''%(ep,sc)
        sf_ef = cursor.execute(cmd_sql).fetchone()
        return sf_ef
    def deploy_scens_idpassAttrGrp(self,grp_classify = u'SET'):#========配置指定组内的成员，idp信息，读取数据库存储的idp信息，创建对应的idp属性组，并配置参数=
        fn_sh = os.path.splitext(sceneName().basename())[0]
        shotInfo = fn_sh.split(u'_')
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0]) 
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        idp_info_stor = u'%s/data/RLayerInfo/RGB' % serverPath
        assetRecordFolders = []#=======找到文件中场景对应的idp信息======================
        assetID_list = []
        setNSP = ''
        if shotInfo[-2] in [u'fs',u'sd',u'lr']:
            setMembers = PyNode(u'%s_GRP'%grp_classify).getChildren()
            assetID_list = []
            for eachSet in setMembers:
                setNSP = eachSet.namespace()
                assetID_list.append(re.match(u'[\w]+',(setNSP.split(u'_')[-1])).group())
        elif shotInfo[-1] ==  u'tx':
            setNSP = shotInfo[1]
            assetID_list = [setNSP]
        for root,dirs,files in os.walk(idp_info_stor):
            for eachDir in dirs:
                if eachDir in assetID_list: 
                    assetRecordFolders.append(os.path.join(root,eachDir).replace(u'\\',u'/'))
                    #assetRecordFolders.append(os.path.abspath(os.path.join(root,eachDir)))
        assetRecordFolders.sort(key = lambda x: x.split(u'/')[-2])#排序，只为了添加属性时的视觉规范=============
        for eachRecFolder in assetRecordFolders: 
            idCode = os.path.split(os.path.dirname(eachRecFolder))[-1]
            fileList = [os.path.join(eachRecFolder,eachfile).replace(u'\\',u'/') for eachfile in os.listdir(eachRecFolder)]
            for eachRecFile in fileList:#pass
                idp_mark = eachRecFile.split(u'_')[-2]
                read_f = open(eachRecFile)
                read_f.seek(13)
                for line in read_f:#pass
                    fullName = ''
                    if shotInfo[-2] in [u'fs',u'sd',u'lr']:
                       valid_str = re.match(u'\S+',line).group()
                       str_split = valid_str.split(u'|')
                       for each in str_split[1:]:
                           each_id = str_split.index(each)
                           str_split[each_id] = u'%s%s' % (setNSP,each)
                       fullName = u'|%s_GRP%s' % (grp_classify,u'|'.join(str_split))
                    elif shotInfo[-1] == u'tx': fullName = re.match(u'\S+',line).group()
                    if objExists(fullName):
                        if not PyNode(fullName).hasAttr(idCode):
                            self.add_idpAttr(PyNode(fullName),idCode)
                            print u'OBJ : %s ------idpAttributeGroup added succeed!!!!!' %(fullName)
                        self.set_idpAttr(PyNode(fullName),idCode,idp_mark)
                    else:
                        warning(u'场景里没有: %s' % fullName) 
                read_f.close()
    def add_idpAttr(self,dagNode,attrName):#======add idp attribute on sepecify dagNode object=========
        dagNode.addAttr(attrName,dt =u'string',r=True,w=False,k=False)
        dagNode.attr(attrName).set(u'No')
        dagNode.addAttr(u'%s_clr' % (attrName.upper()),usedAsColor=True, attributeType='float3')
        dagNode.addAttr( '%sRedChannel'%(attrName.upper()),sn=u'%sRCh'%(attrName.upper()), attributeType='float', parent=u'%s_clr' % (attrName.upper()),dv=0.15)
        dagNode.addAttr( '%sGreenChannel'%(attrName.upper()),sn=u'%sGCh'%(attrName.upper()), attributeType='float', parent=u'%s_clr' % (attrName.upper()),dv=0.15)
        dagNode.addAttr( '%sBlueChannel'%(attrName.upper()),sn=u'%sBCh'%(attrName.upper()), attributeType='float', parent=u'%s_clr' % (attrName.upper()),dv=0.15)
    def set_idpAttr(self,dagNode,attrName,attrValue):#==========set idpAttr group values===============
        #attrName,attrValue,dagNode = u'id13',u'R',selected()[0]
        idpAttrCoupleDict = {u'R':(1,0,0),u'G':(0,1,0),u'B':(0,0,1),u'A':(1,1,1),u'M':(0,0,0)}
        dagNode.attr(attrName).set(attrValue)
        attrChannelGrp = [u'%sRCh'%(attrName.upper()),u'%sGCh'%(attrName.upper()),u'%sBCh'%(attrName.upper())]
        for eachChannel in attrChannelGrp:
            channelIndex = attrChannelGrp.index(eachChannel)
            dagNode.attr(u'%s_clr.%s'%(attrName.upper(),attrChannelGrp[channelIndex])).set(idpAttrCoupleDict[attrValue][channelIndex])
    #===========================================================================
    # def VisitDir(self,arg,dirname,names):
    #     for filespath in names: print os.path.join(dirname,filespath)
    #===========================================================================
    def do_set_submarine_VISAttr(self):
        for eachRef in  listReferences():
            if  eachRef.path.namebase in [u'do5_c502001Beth_h_ms_anim',u'do5_c501001Olly_h_ms_anim']:
                PyNode(u'%s:Master'% (eachRef.namespace)).attr(u'VIS').set(1)
    def do_export_refGrpCams_as_anFile(self):#=====针对于动画文件，把参考物体的顶层组，摄像机导出为an文件到E盘临时目录下===================
        storPath = u'E:/Info_Temp/temp/finalLayoutTemp/do5'
        fn_sh = os.path.splitext(sceneName().basename())[0]
        shotInfo = fn_sh.split(u'_')
        save_an_file_dic = u'%s/%s' % (storPath,shotInfo[1])
        if not os.path.isdir(save_an_file_dic):os.makedirs(save_an_file_dic)
        export_fileFullName = u'%s/%s' % (save_an_file_dic,fn_sh)
        p_shotCam =re.compile(u'cam_%s_%s'%(shotInfo[1],shotInfo[2]))
        allRef_grp =[eachRef.refNode.listConnections(type = u'transform') for eachRef in listReferences() if eachRef.refNode.listConnections(type = u'transform')]
        shotCamLs = [PyNode(eachCam).getParent() for eachCam in listCameras() if p_shotCam.search(PyNode(eachCam).name())]
        select(shotCamLs)
        select(allRef_grp,add=True) 
        exportSelected(export_fileFullName,preserveReferences=True,force=True,type=u'mayaBinary')
        print u'===============File Exported Succeeded!!!!!:::%s============================' % export_fileFullName
    def evalMel_queryMsSQL(self,readMsSQL=True,save=False):
        fn_sh = os.path.splitext(sceneName().basename())[0]
        shotInfo = fn_sh.split(u'_')
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0]) 
        rowValue =self.dod_queryMsSQL_rndInfo(projectInfo,shotInfo[1],shotInfo[2])
        if readMsSQL and rowValue and rowValue[3] == '是':
            self.eval_mel_on_file(projectInfo,shotInfo[1],shotInfo[2])
        elif not readMsSQL:
            self.eval_mel_on_file(projectInfo,shotInfo[1],shotInfo[2])
        elif not rowValue:return None
        if save:
            mc.file(save=1,f = 1)
            print u'File saved succeed!!'
    def eval_mel_on_file(self,proj,sceneNum,shotNume):
        rndMel_storDic = u'//file-cluster/gdc/Projects/%s/%s_Scratch/MasterLighting/renderMel' % (proj,proj)
        p_set = re.compile(u'^s\d+[a-zA-Z]+')
        namespace(set = u':')
        set_ns_ls_all = [eachNsp for eachNsp in  namespaceInfo(lon=True) if len(eachNsp.split(u'_'))!=1 and p_set.match(eachNsp.split(u'_')[1])]
        set_ns_ls = []
        if len(set_ns_ls) !=1:
            p_rollerCoaster = re.compile(u'do5_s514001RollerCoaster')
            for eachNS in set_ns_ls_all:#pass
                if p_rollerCoaster.search(eachNS):set_ns_ls.append(eachNS)
        #set_ns_ls = [eachRef.namespace for eachRef in  listReferences() if p_set.match(eachRef.path.namebase.split(u'_')[1])]
        #eachRef = listReferences()[0]
        #assetId = eachRef.path.namebase.split(u'_')[1]
        eval_mel_file = []
        eval_mel_codes = []
        p_shot = re.compile(u'%s_%s' % (sceneNum,shotNume))
        for root,dirs,fileList in os.walk(rndMel_storDic):
            for eachFile in fileList:
                if p_shot.match(eachFile): eval_mel_file.append(os.path.join(root,eachFile).replace(u'\\',u'/'))
        if len(eval_mel_file) == 0 :
            warning(u'服务器上没有这个镜头分层前需要执行的mel')
            return None 
        f_read = open(eval_mel_file[0],'r')
        for eachLine in f_read:
            if eachLine.startswith(u'setAttr'):
                tempLine = eachLine.replace(os.linesep,'')
                modifyLine = tempLine.replace(u'setAttr \"',u'setAttr \"%s:'%(set_ns_ls[0]))
                try:
                    mel.eval(modifyLine)
                    print (u'=====================Attribute setted SUCCEED:%s ===================== '  % modifyLine.split(u'\"')[1])
                except:
                    warning(u'============object %s not exisits ' % modifyLine.split(u'\"')[1])
                    #error(u'============object %s not exisits ' % modifyLine.split(u'\"')[1])
        f_read.close()
    def export_airscrewLocator(self):#=======阿力贝贝螺旋桨定位的locator导出到L盘对应镜头路径下，用于泡泡制作，finalLayout 调用执行===
        fn_sh = os.path.splitext(sceneName().basename())[0]
        shotInfo = fn_sh.split(u'_')
        p_olly = re.compile('c501001Olly')
        p_beth = re.compile('c502001Beth')
        anim = idmt.pipeline.db.GetAnimByFilename(u'%s_%s_%s'%(shotInfo[0],shotInfo[1],shotInfo[2]))
        playbackOptions(min = anim.frmStart-50,e=True)
        namespace(set = u':')
        listNsp = namespaceInfo(lon=True)
        tem_cons_list_1 = []
        for eachNsp in listNsp:
            if p_olly.search(eachNsp):
                try: tem_cons_list_1.extend(self.create_screwLocation(PyNode(u'%s:MSH_c_hi_airscrew_1_ca_' % eachNsp)))
                except: continue
            elif p_beth.search(eachNsp):
                try: tem_cons_list_1.extend(self.create_screwLocation(PyNode(u'%s:MSH_c_hi_screwpropeller_2_ca_' % eachNsp)))
                except: continue
        if tem_cons_list_1  == []: return
        tem_cons_list_2 = [tem_cons_list_1[i] for i in range(len(tem_cons_list_1)) if tem_cons_list_1[i] not in tem_cons_list_1[:i]]
        bakeResults(u'locAirscrew_*',simulation=True,t=(anim.frmStart-50,anim.frmEnd),sampleBy=1,disableImplicitControl=True,preserveOutsideKeys=True,sparseAnimCurveBake=False,controlPoints=False)
        delete(tem_cons_list_2) 
        stro_locator_path = ur'\\file-cluster\gdc\Projects\DiveollyDive5\DiveollyDive5_Scratch\TD\Bubble_locator'
        current_path = ur'%s\%s_%s'%(stro_locator_path,shotInfo[1],shotInfo[2])
        if not os.path.isdir(current_path):os.makedirs(current_path)
        loc_fileNm = ur'%s\airscrewLocator.mb'%(current_path)
        select(PyNode(u'screwLocationGrp'))
        exportSelected(loc_fileNm,force=True,type=u'mayaBinary')
        delete(PyNode(u'screwLocationGrp'))
        print u'shot %s_%s locator output !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' %(shotInfo[1],shotInfo[2])
    def create_screwLocation(self,screwObj):
        if not objExists(u'screwLocationGrp'):group(n=u'screwLocationGrp',em=True)
        p_nsp = re.compile(u'[^_a-z0-9]+[A-Za-z]+$')
        num=['_01','_02','_03','_04','_05','_06','_07','_08','_09']
        nsp_strip = 'XXXX'
#        if screwObj.namespace() : nsp_strip = p_nsp.search(screwObj.namespace().split(u':')[0]).group()
        if screwObj.namespace() : nsp_strip = screwObj.namespace().split(u':')[0]             
        screwLoc = spaceLocator(n=u'locAirscrew_%s'%nsp_strip)
        airscrewPCons = pointConstraint(screwObj,screwLoc,offset=[0,0,0],weight=1)
        screwLoc.setParent(PyNode(u'screwLocationGrp'))
        return PyNode(u'screwLocationGrp').listRelatives(type = u'pointConstraint',ad=True)
    def jayelocator(self):
        cloc = spaceLocator(n = u'bubblestart%02d'%(len(ls(u'bubblestart*',tr=True))),p = [0,0,0])
        return cloc
    def jayecircle(self):
        jcircle = circle(n = u'BubblePostion%02d'%(len(ls(u'BubblePostion*',tr=True))))
        return jcircle[0]
    def hid_specAttr(self,obj,*attr):
        for eachAttr in attr:
            obj.attr(eachAttr).set(keyable=False,l=True)
    def kcParticleAddAttr(self,pt,attrName,datatype):
        if not pt.hasAttr(attrName):
            pt.addAttr(u'%s0'%(attrName),dataType= datatype)
            pt.addAttr(attrName,dataType = datatype,keyable=True)
            print u'Add attribute %s to %s' % (attrName,pt)
    def zb_visitPathGetSpecModeFile(self,thePath,mode,fileFormat="mb"):#========列出指定路径下的有效文件===============
        get_YWantFiles = []
        for root,dirs,files in os.walk(thePath):
            for filePath in files:
               if self.get_fileMode(filePath,fileFormat) ==mode:
                    temp =os.path.join(root,filePath) 
                    if temp.split("\\")[-2] != "history":                
                        get_YWantFiles.append(os.path.normpath(temp))
        return get_YWantFiles
    def get_fileMode(self,fileSHN,fileFM):
        #fileSHN = "xx.ma"
        if os.path.splitext(fileSHN)[-1].rfind(fileFM) !=1:
            return None
        elif len(fileSHN.split("_")) ==1:
            return None
        else:   
            return fileSHN.split("_")[-2]  
    def do_bubbleSetup(self):#新的dod泡泡工具
        #PyNode(u'defaultRenderGlobals').startFrame.get() 
        #playbackOptions(ast=True,q=True)
        #anim = idmt.pipeline.db.GetAnimByFilename(shotID)
        fn_sh = os.path.splitext(sceneName().basename())[0]
        shotInfo = fn_sh.split(u'_')
        stro_locator_path = ur'\\file-cluster\gdc\Projects\DiveollyDive5\DiveollyDive5_Scratch\TD\Bubble_locator'
        current_path = ur'%s\%s_%s'%(stro_locator_path,shotInfo[1],shotInfo[2])
        loc_fileNm = ur'%s\airscrewLocator.mb'%(current_path)
        if not os.path.exists(loc_fileNm): return
        if os.path.exists(loc_fileNm):importFile(loc_fileNm)
        airscrewLoc = PyNode(u'screwLocationGrp').getChildren()
        select(airscrewLoc)
        playMinTime = playbackOptions(min=True,q=True)
        jayestartframe = playMinTime - 50
        jayetime = currentTime(q=True)
        jayeEndFrame = playbackOptions(max=True,q=True)
        #playbackOptions(min=jayestartframe)
        playbackOptions(min = jayestartframe,e=True)
        sl=ls(tr=True,sl=True)
        for i in range(len(sl)):#i = 0
            obj_jayelocator = self.jayelocator()
            obj_jayecircle = self.jayecircle()
            #dir(obj_jayecircle)
            obj_jayelocator.setParent(obj_jayecircle)
            jayegp = group(obj_jayecircle,n=u'BubbleX')
            loc = ls(sl=True,tr=True)
            self.hid_specAttr(obj_jayelocator,u'rx',u'ry',u'rz',u'sx',u'sy',u'sz')
            self.hid_specAttr(jayegp,u'rx',u'ry',u'rz',u'sx',u'sy',u'sz')
            self.hid_specAttr(obj_jayelocator,u'rx',u'ry',u'rz',u'sx',u'sy',u'sz')
            obj_jayelocator.attr('tx').setKey()
            obj_jayelocator.attr('ty').setKey()
            obj_jayelocator.attr('tz').setKey()
            jayepointposition = pointConstraint(sl[i],jayegp,offset = [0,0,0],weight=1)
            jayepointremon = pointConstraint(sl[i],jayegp,e=True,rm=True)
            jayepointcons = pointConstraint(sl[i],jayegp,name="bubblepoint",offset=(0,0,0),weight=0) 
            jayepoinweith = pointConstraint(jayepointcons,weightAliasList=True,q=True)
            #jayepointcons.name()
            #dir(obj_jayelocator.tx.setKey())
            obj_emit = emitter(pos=(0,0,0),type=u'dir',rate=100,spread=0.6,speedRandom=0.3)
            pt = particle()
            connectDynamic(pt[0],em=obj_emit)
            pt[1].particleRenderType.set(7)
            pt[1].lifespanMode.set(3)
            pt[1].startFrame.set(jayestartframe)
            self.kcParticleAddAttr(pt[1],u'radPP','doubleArray')
            self.kcParticleAddAttr(pt[1],u'radiusPP','doubleArray')
            #create ramp node to connect to particle
            amp = arrayMapper(target = pt[1],destAttr = u'radPP',inputV = u'ageNormalized',type = u'ramp')
            con_list = amp.listConnections(s=True,d=False,type = u'ramp')
            ramp = [con_list[i] for i in range(len(con_list)) if con_list[i] not in con_list[:i]]
            ramp[0].colorEntryList[0].position.set(0)
            ramp[0].colorEntryList[0].color.set(0,0,0)
            ramp[0].colorEntryList[1].position.set(0.135)
            ramp[0].colorEntryList[1].color.set(0.25,0.25,0.25)
            ramp[0].colorEntryList[2].position.set(0.48)
            ramp[0].colorEntryList[2].color.set(0.32,0.32,0.32)
            ramp[0].colorEntryList[3].position.set(1)
            ramp[0].colorEntryList[3].color.set(0.28,0.28,0.28)
            amp.minValue.set(0)
            amp.maxValue.set(0.01)
            #create phone ,assign to the particle
            pe = shadingNode(u'blinn',asShader=True)
            blendcolor = shadingNode(u'blendColors',asUtility=True)
            samplerInfo = ''
            ls_sampInf = ls(type=u'samplerInfo')
            if ls_sampInf:samplerInfo = ls_sampInf[0]
            else:samplerInfo = shadingNode(u'samplerInfo',asUtility=True)
            blendcolor.attr(u'output')>>pe.attr(u'transparency') 
            samplerInfo.attr(u'facingRatio')>>blendcolor.attr(u'blender')  
            blendcolor.color1.set(1,1,1)
            blendcolor.color2.set(0.64,0.64,0.64)
            pe.color.set(0.403,0.600,0.699)
            pe.diffuse.set(0.8)
            pe.eccentricity.set(0.1)
            pe.specularRollOff.set(1)    
            #assign material to the particl
            select(pt[0],r=True)    
            hyperShade(assign=pe)
            #add a gravity
            field=u''
            if objExists(u'buoyance') and PyNode(u'buoyance').nodeType() == u'gravityField': field = PyNode(u'buoyance')
            else:field = gravity(name=u'buoyance',pos=(0,0,0),magnitude=3,dx=0,dy=1,dz=0)
            connectDynamic(pt[0],f=field)
            #constraint to the locator
            jayesetpoint = pointConstraint(obj_jayelocator,obj_emit,n=u'bubblepoint',offset=(0,0,0),weight=1)   
            bubble_grp = group(obj_emit,pt[0],n=u'Bubble1')
            self.hid_specAttr(bubble_grp,u'rx',u'ry',u'rz',u'sx',u'sy',u'sz',u'visibility')
            bubble_grp.addAttr(u'rate',at=u'double',dv=100,min=0,max=1000000000,keyable=True)
            bubble_grp.addAttr(u'spread',at=u'double',dv=1,min=0,max=1,keyable=True)
            bubble_grp.addAttr(u'speed',at=u'double',dv=1,min=-1000000000,max=1000000000,keyable=True)
            bubble_grp.addAttr(u'speedRandom',at=u'double',dv=1,min=0,max=1000000000,keyable=True)
            bubble_grp.addAttr(u'lifeSPmin',at=u'double',dv=0.5,min=1,max=1000000000,keyable=True)
            bubble_grp.addAttr(u'lifeSPmax',at=u'double',dv=4.5,min=0,max=1000000000,keyable=True)
            bubble_grp.addAttr(u'radiusPPmin',at=u'double',dv=0.005,min=0,max=1000000000,keyable=True)
            bubble_grp.addAttr(u'radiusPPmax',at=u'double',dv=0.15,min=0,max=1000000000,keyable=True)
            bubble_grp.addAttr(u'turbulence',at=u'double',dv=0.2,min=0,max=1000000000,keyable=True)
            bubble_grp.addAttr(u'bubbleStart',at=u'double',dv=jayestartframe,min=0,max=1000000000,keyable=True)
            bubble_grp.attr(u'rate') >> obj_emit.attr(u'rate')
            bubble_grp.attr(u'spread') >> obj_emit.attr(u'spread')
            bubble_grp.attr(u'speed') >> obj_emit.attr(u'speed')
            bubble_grp.attr(u'speedRandom') >> obj_emit.attr(u'speedRandom')
            #create expressions
            exp_code_cr = u"""if (particleId == 0)\r\n\t\tseed(2.088388129e-009);
            \r\r\tlifespanPP=rand(%s.lifeSPmin,%s.lifeSPmax);
            \r\r\tradiusPP=rand(%s.radiusPPmin,%s.radiusPPmax);"""%(bubble_grp.name(),bubble_grp.name(),bubble_grp.name(),bubble_grp.name())
            dynExpression(pt[0],creation=True,string=exp_code_cr)
            exp_code_run= u"""\tradiusPP=radiusPP+radPP;
            \r\r\tvector $tub = sphrand(<< %s.turbulence,0,%s.turbulence>>);
            \r\r\tposition += <<$tub.x,0,$tub.z>>;"""%(bubble_grp.name(),bubble_grp.name())
            dynExpression(pt[0],runtimeBeforeDynamics=True,string=exp_code_run)
            jayeexp ="if(frame>=%s.bubbleStart)\r\n\t{%s.%s=1;}\r\nelse\r\n\t{%s.%s=0;}"%(bubble_grp.name(),jayepoinweith[0].nodeName(),jayepoinweith[0].longName(),jayepoinweith[0].nodeName(),jayepoinweith[0].longName())
            expression(n='jayeanbubbleantime',s=jayeexp)
            select(loc)
            bubble_grp.attr(u'radiusPPmin').set(0.07)
            bubble_grp.attr(u'radiusPPmax').set(0.35)   
        
    
    
    
    
    
    
    
    
    
    
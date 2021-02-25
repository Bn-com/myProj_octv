# -*- coding: utf-8 -*-
'''
Script Name: Facial_AutoRig_Tool
Created: 2012-10-10 
@Author: Edward.Sun
@Update_Change: Justin.CHan
@LastUpdated: 2015-05-19
@Description:

'''
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
from RIG.edo.general import edo_autoConnectBlendShapeUI
reload(edo_autoConnectBlendShapeUI)
from RIG.edo.general import edo_cl_checkRiggingFileUI
reload(edo_cl_checkRiggingFileUI)
from RIG.commonly.base import SK_hideLockAll
import headfile
AutoRigPath = headfile.__file__.replace('headfile.py','RIG/').replace('\\','/')
#execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_autoConnectBlendShapeUI.py')
#execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_cl_checkRiggingFileUI.py')

class CJW_Facial_AutoRig_Tool():
    def __init__(self):
        pass
    def CJW_facial_rig_ui(self,edition):
        ui = AutoRigPath+'face_BS/CJW_facial_rig_ui_%s.myuis'%(edition)
        WinName = edition + '_facial_rig_ui'
        if cmds.window(WinName, ex=1):
            cmds.deleteUI(WinName)
        mui = cmds.loadUI(f=ui)
        #cmds.window('LOW_facial_rig_ui',title = u'Facial_rigging_LOW(简易表情)', widthHeight=(260, 375),menuBar=0)   
       
        # 导入模版
        cmds.button('importTemplate_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().%s_importFacialTemplate()'%(edition), ann=u'导入面部所需要的模板')
        # check model
        cmds.button('facial_check_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_openDocumentFromPath()', ann=u'打开工具使用前的模型检查文档')
        # 头部模型生成
        cmds.button('facial_meshes_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_getComponentToTextEditor(\'facial_meshes_list\')', ann=u'将头部所有的模型载入到列表中')
        cmds.textScrollList('facial_meshes_list', e=1, ams=1, sc='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_ListEditSelectCmd(\'facial_meshes_list\')')
        #cmds.popupMenu('facial_meshes_list_popm', p='facial_meshes_list', b=3)
        #cmds.menuItem('facial_meshes_list_mi01', label=u'添加MSH_前缀和_后缀', p='facial_meshes_list_popm', c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_Accession_MSH(\'facial_meshes_list\')')        
        cmds.button('create_meshes_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_createAllFcialMeshes(\'MSH_\')', ann=u'生成面部绑定时需要的所有的头部模型')
        # 舌头生成
        cmds.button('finish_tonguerig_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_finishTongueRig()')
        cmds.button('get_tonguemeshes_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_getComponentToTextEditor(\'get_tonguemeshes_line\')')
        # 下巴生成
        cmds.button('get_UpperToothmeshes_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_getComponentToTextEditor(\'get_UpperToothmeshes_line\')')        
        cmds.button('get_LowerToothmeshes_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_getComponentToTextEditor(\'get_LowerToothmeshes_line\')')         
        cmds.button('jaw_mirror_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_mirrorLipJoint()')        
        cmds.button('finish_jaw_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_finishJawRig(\'%s\')'%(edition))
        # 眼球眼皮
        cmds.button('eyeball_autoloc_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_autoLocationEyeballsCenter()', ann=u'选择眼球的圆形虹膜执行,记住：先选择左眼的虹膜，再选择右眼的')
        cmds.button('eyeball_mirror_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_mirrorEyeballsSkeleton()', ann=u'镜像左边的眼球骨骼到右边')
        cmds.button('eyelids_mend_bt', e=1, c='cmds.selectPref( trackSelectionOrder=1 )', ann=u'选择眼皮线段钱，请点击此补丁')     
        cmds.button('lfeyelids_loop_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_getComponentToTextEditor(\'lfeyelids_loop_line\')', ann=u'依次选择左眼从内到外的眼皮线执行,在生成过程中要时刻保持里面有载入进线')
        cmds.button('rteyelids_loop_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_getComponentToTextEditor(\'rteyelids_loop_line\')', ann=u'依次选择右眼从内到外的眼皮线执行,在生成过程中要时刻保持里面有载入进线')
        cmds.button('finish_eyerig_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_finishEyeRig()', ann=u'先将眼皮线载入上面的框后执行')
        # cmds.button('eyelids_autoloc_bt',e=1,c='edo_createEyslids_skeleton()',ann='先将眼皮线载入上面的框后执行')
        cmds.button('mirrorEyelids_blendshape_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().edo_cl_mirrorFacialLfEyelidsDrivenMeshRoRightAndAutoConnections()', ann=u'直接执行此命令可使左眼皮的驱动模型目标体镜像到右边眼皮')
        #cmds.button('check_calimeroRig_bt', e=1, c='edo_cl_checkRiggingFileUI()', ann='calimero控制器规范检查工具')
        # 耳朵设置
        cmds.button('ears_mirror_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_mirrorEarJoint()')        
        cmds.button('finish_ear_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_finishEarRig()')
        # 头部挤压拉伸
        cmds.button('head_stretch_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_Head_Stretch()')         
        cmds.button('head_stretch_jaw_bt', e=1, c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_Head_Stretch_jaw()')         

        cmds.showWindow(mui)


    def CJW_openDocumentFromPath(self):
        # path='Z:/Resource/Support/Maya/extra/Rigging_Simulation/helpDocument/project/calimero/calimero_facial_rigging_tool_model_check.docx.docx'
        DocumentPath = AutoRigPath+'face_BS/facial_rigging_tool_model_chec.docx'
        cmd = "system(\"load " + DocumentPath + "\")"
        mel.eval(cmd)


    def LOW_importFacialTemplate(self):
        templatePath = AutoRigPath + 'face_BS/TemplateFile'
        cmds.file(templatePath + '/LOW_eyeballs_rig.ma', i=1)
        cmds.file(templatePath + '/LOW_pannel_rig.ma', i=1)
        cmds.file(templatePath + '/LOW_jaw_rig.ma', i=1)
        cmds.file(templatePath + '/LOW_tongue_rig.ma', i=1)
        cmds.file(templatePath + '/LOW_frame_rig.ma', i=1)
        cmds.file(templatePath + '/LOW_ear_rig.ma', i=1)

    def NORM_importFacialTemplate(self):
        templatePath = AutoRigPath + 'face_BS/TemplateFile'
        cmds.file(templatePath + '/Norm_eyeballs_rig.ma', i=1)
        cmds.file(templatePath + '/Norm_pannel_rig.ma', i=1)
        cmds.file(templatePath + '/Norm_jaw_rig.ma', i=1)
        cmds.file(templatePath + '/Norm_tongue_rig.ma', i=1)
        cmds.file(templatePath + '/Norm_frame_rig.ma', i=1)
        cmds.file(templatePath + '/Norm_ear_rig.ma', i=1)


    def HIGH_importFacialTemplate(self):
        templatePath = AutoRigPath + 'face_BS/TemplateFile'
        cmds.file(templatePath + '/High_eyeballs_rig.ma', i=1)
        cmds.file(templatePath + '/High_pannel_rig.ma', i=1)
        cmds.file(templatePath + '/High_jaw_rig.ma', i=1)
        cmds.file(templatePath + '/High_tongue_rig.ma', i=1)
        cmds.file(templatePath + '/High_frame_rig.ma', i=1)
        cmds.file(templatePath + '/High_ear_rig.ma', i=1)
        
    def High_importFacialSelectPannel(self):
        templatePath = AutoRigPath + 'face_BS/TemplateFile/Facial_V1'
        cmds.file(templatePath + '/High_selectPannel_rig.ma', i=1)
                
    def edo_chackAllFacialMeshes(self,meshes):
        # meshes=cmds.ls(sl=1)
        for mesh in meshes:
            # mesh=meshes[0]
            if not 'MSH_' in mesh:
                cmds.warning(u'=====所有模型需“MSH_”前缀=====')
                return False
            if not mesh[-1] == '_':
                print mesh
                cmds.warning(u'=====所有模型需“_”后缀=====')
                return False
    

    def CJW_getComponentToTextEditor(self,texteditor):
        cmds.textScrollList(texteditor, e=1, ra=1)
        sels = cmds.ls(orderedSelection=1, fl=1)
        if not sels == None or not sels == []:
            for sel in sels:
                cmds.textScrollList(texteditor, e=1, a=sel)
        if  sels == None or sels == []:
            cmds.warning(u'=====请选择模型=====')

            
    def CJW_ListEditSelectCmd(self,listName):
        sels = cmds.textScrollList(listName, q=1, si=1)
        if not sels == None:
            cmds.select(sels)            

            
    def CJW_Accession_MSH(self,listName):
        sels = cmds.textScrollList(listName, q=1, si=1)
        if not sels == None:
            for sel in sels:
                MSH_Name = cmds.rename(sel,('MSH_'+sel+'_'))
                cmds.textScrollList(listName, q=1, ri=sel)
                cmds.textScrollList(listName, e=1, a=MSH_Name)     

                
    def edo_createAllFcialMeshes(self,mshstr):
        if cmds.objExists('FACIAL_RIG_MESHES_FRAME'):
            self.edo_buildClFacialRigHierarchyNode()
            if cmds.getAttr('FACIAL_RIG_MESHES_FRAME.MESHES_WERE_ALREAD_CREATED') == 1:
                print 'facial meshes have already been created!,do it again that is not safe'
                return False
            bound = cmds.xform('FACIAL_RIG_MESHES_FRAME', q=1, os=1, bb=1)
            h = bound[4] - bound[1]
            cmds.setAttr('FACIAL_RIG_MESHES_FRAME.ty', cmds.getAttr('FACIAL_RIG_MESHES_FRAME.ty') + (h * 1.5))
            cmds.makeIdentity('FACIAL_RIG_MESHES_FRAME', apply=1, t=1, r=1, s=1, n=0)
            allmeshes = cmds.textScrollList('facial_meshes_list', q=1, ai=1)
            if allmeshes:
                check = self.edo_chackAllFacialMeshes(allmeshes)
                if check == False:
                    cmds.confirmDialog(title=u'模型不符合规范', message=u'相关模型有不符合规范问题，详情请看script Editor窗口！', button=['OK'], defaultButton='Yes', cancelButton='No', dismissString='No')
                    return False
                cmds.parent('FACIAL_RIG_MESHES_FRAME', 'GRP_CL_FACIALRIG_DEFORMER')
                self.edo_setLockTransform(allmeshes, 0)
                if not cmds.objExists('GRP_FCIAL_MESHES'):
                    # cmds.delete('GRP_FCIAL_MESHES')
                    facialmeshesgrp = cmds.group(allmeshes, n='GRP_FCIAL_MESHES')
                    rp = cmds.xform(facialmeshesgrp, q=1, ws=1, rp=1)
                    cmds.xform(facialmeshesgrp, ws=1, rp=[0, rp[1], rp[2]], sp=[0, rp[1], rp[2]])
                else:
                    try:
                        cmds.parent(allmeshes, 'GRP_FCIAL_MESHES')
                    except:
                        print 'something is wrong!'
                allorg = []
                # creaet org
                for mesh in allmeshes:
                    # mesh=allmeshes[0]
                    org = cmds.duplicate(mesh, n=mesh.replace(mshstr, mshstr + 'ORIGINAL_'))
                    # bs=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'BLENDSHAPE_'))
                    # fs=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'FACIALSKIN_'))
                    allorg.append(org[0])
                if cmds.objExists('GRP_FCIAL_ORIGINAL_MESHES'):
                    cmds.delete('GRP_FCIAL_ORIGINAL_MESHES')
                prggrp = cmds.group(allorg, n='GRP_FCIAL_ORIGINAL_MESHES')
                rp = cmds.xform(prggrp, q=1, ws=1, rp=1)
                cmds.xform(prggrp, ws=1, rp=[0, rp[1], rp[2]], sp=[0, rp[1], rp[2]])
                cmds.parent(prggrp, 'ORIGINAL_FRAME')
                cmds.delete(cmds.pointConstraint('ORIGINAL_FRAME', prggrp, mo=0))
                # creaet blendshape
                allorg = []
                for mesh in allmeshes:
                    # mesh=allmeshes[0]
                    # org=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'ORIGINAL_'))
                    org = cmds.duplicate(mesh, n=mesh.replace(mshstr, mshstr + 'BLENDSHAPE_'))
                    # fs=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'FACIALSKIN_'))
                    allorg.append(org[0])
                if cmds.objExists('GRP_FCIAL_BLENDSHAPE_MESHES'):
                    cmds.delete('GRP_FCIAL_BLENDSHAPE_MESHES')
                prggrp = cmds.group(allorg, n='GRP_FCIAL_BLENDSHAPE_MESHES')
                rp = cmds.xform(prggrp, q=1, ws=1, rp=1)
                cmds.xform(prggrp, ws=1, rp=[0, rp[1], rp[2]], sp=[0, rp[1], rp[2]])
                cmds.parent(prggrp, 'BLENDSHAPE_FRAME')
                cmds.delete(cmds.pointConstraint('BLENDSHAPE_FRAME', prggrp, mo=0))
                # creaet facial skin
                allorg = []
                for mesh in allmeshes:
                    # mesh=allmeshes[0]
                    # org=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'ORIGINAL_'))
                    # org=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'BLENDSHAPE_'))
                    org = cmds.duplicate(mesh, n=mesh.replace(mshstr, mshstr + 'FACIALSKIN_'))
                    allorg.append(org[0])
                if cmds.objExists('GRP_FCIAL_FACIALSKIN_MESHES'):
                    cmds.delete('GRP_FCIAL_FACIALSKIN_MESHES')
                prggrp = cmds.group(allorg, n='GRP_FCIAL_FACIALSKIN_MESHES')
                rp = cmds.xform(prggrp, q=1, ws=1, rp=1)
                cmds.xform(prggrp, ws=1, rp=[0, rp[1], rp[2]], sp=[0, rp[1], rp[2]])
                cmds.parent(prggrp, 'FACIALSKIN_FRAME')
                cmds.delete(cmds.pointConstraint('FACIALSKIN_FRAME', prggrp, mo=0))
                bs = cmds.blendShape('GRP_FCIAL_BLENDSHAPE_MESHES', 'GRP_FCIAL_FACIALSKIN_MESHES', tc=1, foc=1, n='BS_FACIAL_BLENDSHAPE_OUTPUT')
                cmds.setAttr(bs[0] + '.GRP_FCIAL_BLENDSHAPE_MESHES', 1)
                bs = cmds.blendShape('GRP_FCIAL_FACIALSKIN_MESHES', 'GRP_FCIAL_MESHES', tc=1, foc=1, n='BS_FACIAL_SKIN_OUTPUT')
                cmds.setAttr(bs[0] + '.GRP_FCIAL_FACIALSKIN_MESHES', 1)
                cmds.setAttr('FACIAL_RIG_MESHES_FRAME.MESHES_WERE_ALREAD_CREATED', 1)
                rp = cmds.xform('GRP_FCIAL_FACIALSKIN_MESHES', q=1, ws=1, rp=1)
                tx = cmds.getAttr('FACIAL_RIG_MESHES_FRAME.tx')
                cmds.setAttr('FACIAL_RIG_MESHES_FRAME.tx', tx - rp[0])
                zjnt = cmds.createNode('joint', n='FACIAL_ZERO_JOINT', p='GRP_FCIAL_FACIALSKIN_MESHES')
                cmds.setAttr(zjnt + '.inheritsTransform', 0)
                cmds.parent(zjnt, 'FACIALSKIN_FRAME')
                cmds.delete(cmds.pointConstraint('GRP_FCIAL_FACIALSKIN_MESHES', zjnt, mo=0))
                cmds.setAttr(zjnt + '.v', 0)
                self.edo_setLockTransform([zjnt], 1)
                skmeshes = cmds.listRelatives('GRP_FCIAL_FACIALSKIN_MESHES', c=1, pa=1)
                if skmeshes:
                    for skmesh in skmeshes:
                        # skmesh=skmeshes[0]
                        try:
                            sk = cmds.skinCluster(zjnt, skmesh, rfs=0, tsb=1, mi=10)
                            cmds.setAttr(sk[0] + '.skinningMethod', 1)
                        except:
                            print 'there is something wrong with the  ...  ' + skmesh
                            self.edo_setLockTransform(['FACIAL_RIG_MESHES_FRAME'], 1)


    def edo_setLockTransform(self,list, v):
        for l in list:
            # l='MSH_tongue_'
            cmds.setAttr(l + '.tx', e=1, l=v)
            cmds.setAttr(l + '.ty', e=1, l=v)
            cmds.setAttr(l + '.tz', e=1, l=v)
            cmds.setAttr(l + '.rx', e=1, l=v)
            cmds.setAttr(l + '.ry', e=1, l=v)
            cmds.setAttr(l + '.rz', e=1, l=v)
            cmds.setAttr(l + '.sx', e=1, l=v)
            cmds.setAttr(l + '.sy', e=1, l=v)
            cmds.setAttr(l + '.sz', e=1, l=v)


    def edo_autoLocationEyeballsCenter(self):
        sels = cmds.ls(sl=1)
        if not sels:
            print 'you must select the eyeballs first!'
            return False
        template = 'GRP_EYEBALLS_TEMPLATE'
        mel.eval('newCluster " -envelope 1";')
        clus = cmds.ls(sl=1)[0]
        piv = cmds.xform(clus, q=1, ws=1, rp=1)
        cmds.xform(template, ws=1, t=piv)
        cmds.delete(clus)
        sel = sels[0]
        cmds.select(sel)
        mel.eval('newCluster " -envelope 1";')
        clus = cmds.ls(sl=1)[0]
        piv = cmds.xform(clus, q=1, ws=1, rp=1)
        cmds.delete(clus)
        cmds.xform('Lf_eyeballs_joint0', ws=1, t=piv)
        cmds.xform('Rt_eyeballs_joint0', ws=1, t=[piv[0] * -1, piv[1], piv[2]])


    def edo_mirrorEyeballsSkeleton(self):
        t1 = cmds.xform('Lf_eyeballs_joint0', q=1, ws=1, t=1)
        t2 = cmds.xform('Lf_eyeballs_joint1', q=1, ws=1, t=1)
        t3 = cmds.xform('Lf_eyeballs_highlight_joint1', q=1, os=1, t=1)
        cmds.xform('Rt_eyeballs_joint0', ws=1, t=[t1[0] * -1, t1[1], t1[2]])
        cmds.xform('Rt_eyeballs_joint1', ws=1, t=[t2[0] * -1, t2[1], t2[2]])
        cmds.xform('Rt_eyeballs_highlight_joint1', os=1, t=[t3[0], t3[1], t3[2]])


    def edo_getComponentToTextEditor(self,texteditor):
        # texteditor='lfeyelids_loop_line'
        sels = cmds.ls(orderedSelection=1, fl=1)
        if sels:
            list = ''
            for sel in sels:
                list = list + sel + ','
            list = list[:len(list) - 1]
            cmds.textField(texteditor, e=1, text=list)


    def edo_createEyslids_skeleton(self):
        lfedges = cmds.textField('lfeyelids_loop_line', q=1, tx=1)
        lfedgelist = lfedges.split(',')
        rtedges = cmds.textField('rteyelids_loop_line', q=1, tx=1)
        rtedgelist = rtedges.split(',')
        lfeyelidsjnt = self.edo_createJointRingFromEdge(lfedgelist[0], 'Lf_', 'GRP_EYEBALLS_TEMPLATE')
        rteyelidsjnt = self.edo_createJointRingFromEdge(rtedgelist[0], 'Rt_', 'GRP_EYEBALLS_TEMPLATE')
        if cmds.objExists('eyelids_influence'):
            cmds.delete('eyelids_influence')
        cmds.sets(lfeyelidsjnt + rteyelidsjnt, n='eyelids_influence')


    def edo_createJointRingFromEdge(self,edge, prefix, parentobj):
        jnts = []
        cmds.select(edge, r=1)
        cmds.SelectEdgeLoopSp()
        curve = cmds.polyToCurve(form=2, degree=1, n=prefix + 'eyelids_ring_curve')
        cmds.parent(curve[0], parentobj)
        cmds.delete(curve[1])
        spans = cmds.getAttr(curve[0] + '.spans')
        degree = cmds.getAttr(curve[0] + '.degree')
        cvnum = spans + degree
        for i in range(0, cvnum - 1):
            # i=0
            jnt = cmds.createNode('joint', n=prefix + 'eyelids_jnt' + str(i), p=curve[0])
            cmds.xform(jnt, ws=1, t=cmds.xform(curve[0] + '.cv[' + str(i) + ']', q=1, ws=1, t=1))
            jnts.append(jnt)
        return jnts


    def edo_buildClEyelids_skeleton_drivenMesh(self,edge, prefix, parentobj):
        # edge=Lfedge
        # prefix='Lfeyelids_'
        # parentobj='FACIALSKIN_FRAME'
        cmds.select(edge, r=1)
        cmds.SelectEdgeLoopSp()
        curve = cmds.polyToCurve(form=2, degree=1, n=prefix + '_skeleton_drivenMesh_curve')
        cmds.delete(curve[1])
        dupcurve = cmds.duplicate(curve[0], n=curve[0] + '_OFFSET')
        cmds.setAttr(dupcurve[0] + '.tz', 0.1)
        lofts = cmds.loft(curve[0], dupcurve[0], ch=1, u=1, c=0, ar=1, d=3, ss=1, rn=0, po=1, rsn=1, n=prefix + '_skeleton_dirvenMesh_')
        tess = self.edo_findNodeFromHis(lofts[0], 'nurbsTessellate')
        cmds.setAttr(tess + '.uType', 3)
        cmds.setAttr(tess + '.uNumber', 1)
        cmds.setAttr(tess + '.vType', 3)
        cmds.setAttr(tess + '.vNumber', 1)
        cmds.setAttr(tess + '.polygonType', 1)
        cmds.setAttr(tess + '.format', 2)
        cmds.select(lofts[0], r=1)
        cmds.DeleteHistory()
        cmds.CenterPivot()
        cmds.parent(lofts[0], parentobj)
        rp = cmds.xform(parentobj, q=1, ws=1, rp=1)
        cmds.xform(lofts[0], ws=1, rp=rp, sp=rp)
        cmds.delete(curve[0], dupcurve[0])
        return lofts[0]


    def edo_findNodeFromHis(self,name, type):
        # name='twodline_curve'
        # type='tweak'
        node = ''
        hiss = cmds.listHistory(name)
        for his in hiss:
            if cmds.nodeType(his) == type:
                node = his
        return node


    def edo_buildClFacialRigHierarchyNode(self):
        if not cmds.objExists('GRP_CL_FACIALRIG_DEFORMER'):
            cmds.createNode('transform', n='GRP_CL_FACIALRIG_DEFORMER')
        if not cmds.objExists('GRP_CL_FACIALRIG_FOLLOWHEAD_NODE'):
            cmds.createNode('transform', n='GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
        if not cmds.objExists('GRP_CL_ALL_FACIALRIG_JOINTS'):
            cmds.createNode('transform', n='GRP_CL_ALL_FACIALRIG_JOINTS', p='GRP_CL_FACIALRIG_DEFORMER')
        if not cmds.objExists('GRP_CL_FACIALRIG_FOLLOWBODY_NODE'):
            cmds.createNode('transform', n='GRP_CL_FACIALRIG_FOLLOWBODY_NODE')


    def edo_createEyeballsRig(self,mshstr):
        self.edo_buildClFacialRigHierarchyNode()
        if not cmds.objExists('GRP_EYEBALLS_TEMPLATE'):
            return False
        # createEyeballsRig
        cmds.joint('Lf_eyeballs_joint0', e=1, oj='xyz', sao='yup', zso=1)
        cmds.joint('Rt_eyeballs_joint0', e=1, oj='xyz', sao='yup', zso=1)
        # lf high light driven joint
        cmds.createNode('joint', n='Lf_eyeballs_highlight_DIV_joint0', p='Lf_eyeballs_joint0')
        cmds.xform('Lf_eyeballs_highlight_DIV_joint0', os=1, t=[0, 0, 0])
        # lf high light joint
        cmds.createNode('joint', n='Lf_eyeballs_highlight_joint0', p='Lf_eyeballs_highlight_DIV_joint0')
        cmds.xform('Lf_eyeballs_highlight_joint0', os=1, t=[0, 0, 0])
        cmds.parent('Lf_eyeballs_highlight_joint1', 'Lf_eyeballs_highlight_joint0')
        # rt high light driven joint
        cmds.createNode('joint', n='Rt_eyeballs_highlight_DIV_joint0', p='Rt_eyeballs_joint0')
        cmds.xform('Rt_eyeballs_highlight_DIV_joint0', os=1, t=[0, 0, 0])
        # rt high light joint
        cmds.createNode('joint', n='Rt_eyeballs_highlight_joint0', p='Rt_eyeballs_highlight_DIV_joint0')
        cmds.xform('Rt_eyeballs_highlight_joint0', os=1, t=[0, 0, 0])
        cmds.parent('Rt_eyeballs_highlight_joint1', 'Rt_eyeballs_highlight_joint0')
        # create eyeballs constraint
        uploc = cmds.spaceLocator(n='Loc_eyeballs_upVector', p=cmds.xform('GRP_EYEBALLS_TEMPLATE', q=1, ws=1, t=1))
        cmds.parent(uploc, 'GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
        cmds.aimConstraint('c_Lf_eye_M', 'Lf_eyeballs_joint0', mo=1, aimVector=[1, 0, 0], upVector=[0, 1, 0], worldUpType='objectrotation', worldUpVector=[0, 1, 0], worldUpObject=uploc[0])
        cmds.aimConstraint('c_Rt_eye_M', 'Rt_eyeballs_joint0', mo=1, aimVector=[1, 0, 0], upVector=[0, 1, 0], worldUpType='objectrotation', worldUpVector=[0, 1, 0], worldUpObject=uploc[0])
        # set parent
        cmds.parent('EYE_RIG', 'GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
        cmds.parent('Lf_eyeballs_joint0', 'GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
        cmds.parent('Rt_eyeballs_joint0', 'GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
        # set head follow
        bodyloc = cmds.spaceLocator(n='Loc_body_constraint', p=cmds.xform('GRP_EYEBALLS_TEMPLATE', q=1, ws=1, t=1))
        cmds.parent(bodyloc, 'GRP_CL_FACIALRIG_FOLLOWBODY_NODE')
        cmds.parentConstraint(bodyloc[0], 'EYE_RIG', mo=1)
        cmds.setKeyframe('EYE_RIG.tx')
        cmds.setKeyframe('EYE_RIG.ty')
        cmds.setKeyframe('EYE_RIG.tz')
        cmds.setKeyframe('EYE_RIG.rx')
        cmds.setKeyframe('EYE_RIG.ry')
        cmds.setKeyframe('EYE_RIG.rz')
        revers = cmds.createNode('reverse')
        bl = cmds.listConnections('EYE_RIG.tx', s=1, d=0)
        cmds.connectAttr('c_eye_M.follow', revers + '.inputX', f=1)
        cmds.connectAttr(revers + '.outputX', bl[0] + '.weight', f=1)
        cmds.delete('EYE_RIGShape')
        self.edo_setLockTransform(['c_eye_M'], 0)
        # create high light rig
        cmds.connectAttr('MD_Lf_eyeballs_highlight.outputX', 'Lf_eyeballs_highlight_DIV_joint0.ry', f=1)
        cmds.connectAttr('MD_Lf_eyeballs_highlight.outputY', 'Lf_eyeballs_highlight_DIV_joint0.rz', f=1)
        cmds.connectAttr('MD_Rt_eyeballs_highlight.outputX', 'Rt_eyeballs_highlight_DIV_joint0.ry', f=1)
        cmds.connectAttr('MD_Rt_eyeballs_highlight.outputY', 'Rt_eyeballs_highlight_DIV_joint0.rz', f=1)
        # c_Lf_spec_tempMod_M.tx  Lf_eyeballs_highlight_DIV_joint0
        # c_Rt_spec_tempMod_M.tx  Rt_eyeballs_highlight_DIV_joint0
        #======================================================================================
        # createEyelidsRig
        # lf eyelids
        if cmds.objExists('Lf_eyelids_ring_curve'):
            jnts = cmds.listRelatives('Lf_eyelids_ring_curve', c=1, type='joint', pa=1)
            if jnts:
                cjnt = cmds.createNode('joint', n='Lf_eyelids_all_jnt0', p='Lf_eyeballs_highlight_joint0')
                cmds.xform('Lf_eyelids_all_jnt0', os=1, t=[0, 0, 0])
                cmds.parent('Lf_eyelids_all_jnt0', 'GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
                for jnt in jnts:
                    # jnt=jnts[0]
                    djnt = cmds.createNode('joint', n=jnt.replace('jnt', 'DIV_jnt'), p='Lf_eyelids_all_jnt0')
                    rjnt = cmds.createNode('joint', n=jnt.replace('jnt', 'rotate_jnt'), p=djnt)
                    cmds.parent(jnt, rjnt)
        # Rt eyelids
        if cmds.objExists('Rt_eyelids_ring_curve'):
            jnts = cmds.listRelatives('Rt_eyelids_ring_curve', c=1, type='joint', pa=1)
            if jnts:
                cjnt = cmds.createNode('joint', n='Rt_eyelids_all_jnt0', p='Rt_eyeballs_highlight_joint0')
                cmds.xform('Rt_eyelids_all_jnt0', os=1, t=[0, 0, 0])
                cmds.parent('Rt_eyelids_all_jnt0', 'GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
                for jnt in jnts:
                    # jnt=jnts[0]
                    djnt = cmds.createNode('joint', n=jnt.replace('jnt', 'DIV_jnt'), p='Rt_eyelids_all_jnt0')
                    rjnt = cmds.createNode('joint', n=jnt.replace('jnt', 'rotate_jnt'), p=djnt)
                    cmds.parent(jnt, rjnt)
        if cmds.objExists('GRP_FCIAL_FACIALSKIN_MESHES'):
            self.edo_setLockTransform(['Lf_eyelids_all_jnt0', 'Rt_eyelids_all_jnt0'], 1)
            cmds.parent(['Lf_eyelids_all_jnt0', 'Rt_eyelids_all_jnt0'], 'GRP_FCIAL_FACIALSKIN_MESHES')
            self.edo_setLockTransform(['Lf_eyelids_all_jnt0', 'Rt_eyelids_all_jnt0'], 0)
        # add skin
        Lfedges = cmds.textField('lfeyelids_loop_line', q=1, tx=1)
        Rtedges = cmds.textField('rteyelids_loop_line', q=1, tx=1)
        edges = Lfedges + ',' + Rtedges
        if edges:
            edges = edges.split(',')
            if edges:
                mesh = edges[0].split('.')[0].replace(mshstr, mshstr + 'FACIALSKIN_')
                if not cmds.objExists(mesh):
                    print 'there is no mesh that name is ' + mesh + ' . So the program cound not add skin to it.'
                    return False
                sks = self.edo_findNodeFromHistory(mesh, 'skinCluster')
                if sks:
                    sk = sks[0]
                    # jnts=cmds.ls(sl=1)
                    if not cmds.objExists('eyelids_influence'):
                        print 'there is no set that name is eyelids_influence . So the program cound not add skin to it.'
                        return False
                    jnts = cmds.sets('eyelids_influence', q=1)
                    cmds.skinCluster(sk, e=1, ai=jnts, lw=1, wt=0)
                    # auto compute the skin weight
                    # find all vertex
                    # Left eyelids
                    lfedges = Lfedges.split(',')
                    count = len(lfedges)
                    addw = 1.0 / (count - 1)
                    vtx_cjnt_w = []
                    for i in range(0, count):
                        # i=0
                        w = (count - i - 1) * addw
                        print w
                        cmds.select(lfedges[i], r=1)
                        cmds.SelectEdgeLoopSp()
                        cmds.ConvertSelectionToVertices()
                        alleyelids_vertex = cmds.ls(sl=1, fl=1)
                        # compute weight
                        #
                        for v in alleyelids_vertex:
                            # v=alleyelids_vertex[5]
                            skv = v.replace(mshstr, mshstr + 'FACIALSKIN_')
                            if cmds.objExists(skv):
                                # find closest skeleton
                                vp = cmds.xform(skv, q=1, ws=1, t=1)
                                mixdis = 10000000.0
                                cjnt = ''
                                for jnt in jnts:
                                    # jnt=jnts[0]
                                    jp = cmds.xform(jnt, q=1, ws=1, t=1)
                                    vecter = om.MVector((vp[0] - jp[0]), (vp[1] - jp[1]), (vp[2] - jp[2]))
                                    dis = vecter.length()
                                    if dis < mixdis:
                                        mixdis = dis
                                        cjnt = jnt
                                vtx_cjnt_w.append([skv, cjnt, w])
                                print 'vetex: ' + skv + '  ......  closestJoint: ' + cjnt + '  ......  weight: ' + str(w)
                                cmds.skinPercent(sk, skv, tv=(cjnt, w))
                    # Right eyelids
                    rtedges = Rtedges.split(',')
                    count = len(rtedges)
                    addw = 1.0 / (count - 1)
                    vtx_cjnt_w = []
                    for i in range(0, count):
                        # i=0
                        w = (count - i - 1) * addw
                        print w
                        cmds.select(rtedges[i], r=1)
                        cmds.SelectEdgeLoopSp()
                        cmds.ConvertSelectionToVertices()
                        alleyelids_vertex = cmds.ls(sl=1, fl=1)
                        # compute weight
                        #
                        for v in alleyelids_vertex:
                            # v=alleyelids_vertex[5]
                            skv = v.replace(mshstr, mshstr + 'FACIALSKIN_')
                            if cmds.objExists(skv):
                                # find closest skeleton
                                vp = cmds.xform(skv, q=1, ws=1, t=1)
                                mixdis = 10000000.0
                                cjnt = ''
                                for jnt in jnts:
                                    # jnt=jnts[0]
                                    jp = cmds.xform(jnt, q=1, ws=1, t=1)
                                    vecter = om.MVector((vp[0] - jp[0]), (vp[1] - jp[1]), (vp[2] - jp[2]))
                                    dis = vecter.length()
                                    if dis < mixdis:
                                        mixdis = dis
                                        cjnt = jnt
                                vtx_cjnt_w.append([skv, cjnt, w])
                                print 'vetex: ' + skv + '  ......  closestJoint: ' + cjnt + '  ......  weight: ' + str(w)
                                cmds.skinPercent(sk, skv, tv=(cjnt, w))
                    # add eyelids skeleton dirven mesh
                    Lfedge = Lfedges.split(',')[0].replace(mshstr, mshstr + 'FACIALSKIN_')
                    Rtedge = Rtedges.split(',')[0].replace(mshstr, mshstr + 'FACIALSKIN_')
                    lfmesh = self.edo_buildClEyelids_skeleton_drivenMesh(Lfedge, 'Lfeyelids', 'FACIALSKIN_FRAME')
                    rtmesh = self.edo_buildClEyelids_skeleton_drivenMesh(Rtedge, 'Rteyelids', 'FACIALSKIN_FRAME')
                    lfmeshget = cmds.duplicate(lfmesh, n=lfmesh.replace('Lfeyelids', 'Lfeyelids_getbs'))[0]
                    rtmeshget = cmds.duplicate(rtmesh, n=rtmesh.replace('Rteyelids', 'Rteyelids_getbs'))[0]
                    cmds.setAttr(lfmeshget + '.sx', -1)
                    cmds.setAttr(lfmeshget + '.v', 0)
                    cmds.setAttr(rtmeshget + '.sx', -1)
                    cmds.setAttr(rtmeshget + '.v', 0)
                    wrapcmd = 'CreateWrap;'
                    cmds.select(lfmeshget, r=1)
                    cmds.select(rtmesh, add=1)
                    mel.eval(wrapcmd)
                    cmds.select(rtmeshget, r=1)
                    cmds.select(lfmesh, add=1)
                    mel.eval(wrapcmd)
                    # lfmesh='Lfeyelids_skeleton_dirvenMesh' rtmesh='Rteyelids_skeleton_dirvenMesh'
                    fos = []
                    for jnt in jnts:
                        if 'Lf_' in jnt:
                            fos.append(self.edo_createFollicleToMeshByClosestObj(lfmesh, jnt, 1))
                    for jnt in jnts:
                        if 'Rt_' in jnt:
                            fos.append(self.edo_createFollicleToMeshByClosestObj(rtmesh, jnt, 1))
                    print fos
                    if cmds.objExists('GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE'):
                        cmds.delete('GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE')
                    grp = cmds.group(fos, n='GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE')
                    cmds.parent(grp, 'FACIALSKIN_FRAME')
                    cmds.setAttr('GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE.v', 0)
                    self.edo_setLockTransform(['FACIAL_RIG_MESHES_FRAME', 'FACIALSKIN_FRAME'], 1)
        cmds.delete('GRP_EYEBALLS_TEMPLATE')


    def edo_finishEyeRig(self):
        Lfedges = cmds.textField('lfeyelids_loop_line', q=1, tx=1)
        Rtedges = cmds.textField('rteyelids_loop_line', q=1, tx=1)
        if Lfedges and Rtedges:
            print 'finish eye rig!'
            self.edo_createEyslids_skeleton()
            self.edo_createEyeballsRig('MSH_')
        else:
            cmds.confirmDialog(title='can not find the edges of eyelids', message='can not find the edges of eyelids,you must appoint the edges of eyelids to the textline editor', button=['ok,i got it'], defaultButton='Yes', cancelButton='No', dismissString='No')


    def edo_finishTongueRig(self):
        self.edo_buildClFacialRigHierarchyNode()
        if not cmds.objExists('GRP_TONGUE_TEMPLATE'):
            return False
        ctrls = cmds.ls('c_tongue_joint*')
        for ctrl in ctrls:
            # ctrl=ctrls[0]
            tp = cmds.listRelatives(ctrl, p=1, pa=1)
            if tp:
                rp = cmds.listRelatives(tp[0], p=1, pa=1)
                if rp:
                    if 'move' in rp[0]:
                        cmds.setAttr(rp[0] + '.tx', cmds.getAttr(ctrl + '.tx'))
                        cmds.setAttr(rp[0] + '.ty', cmds.getAttr(ctrl + '.ty'))
                        cmds.setAttr(rp[0] + '.tz', cmds.getAttr(ctrl + '.tz'))
                        cmds.setAttr(rp[0] + '.rx', cmds.getAttr(ctrl + '.rx'))
                        cmds.setAttr(rp[0] + '.ry', cmds.getAttr(ctrl + '.ry'))
                        cmds.setAttr(rp[0] + '.rz', cmds.getAttr(ctrl + '.rz'))
                        # setZero
                        cmds.setAttr(ctrl + '.tx', 0)
                        cmds.setAttr(ctrl + '.ty', 0)
                        cmds.setAttr(ctrl + '.tz', 0)
                        cmds.setAttr(ctrl + '.rx', 0)
                        cmds.setAttr(ctrl + '.ry', 0)
                        cmds.setAttr(ctrl + '.rz', 0)
        if cmds.objExists('tongue_influence'):
            infs = cmds.sets('tongue_influence', q=1)
            meshes = lfedges = cmds.textField('get_tonguemeshes_line', q=1, tx=1)
            meshs = meshes.split(',')
            if meshs:
                for mesh in meshs:
                    # mesh=meshs[0]
                    cmds.skinCluster(infs, mesh, rfs=0, tsb=1, mi=len(infs))
                    if cmds.objExists('tongue_skinMesh'):
                        cmds.copySkinWeights('tongue_skinMesh', mesh, noMirror=1, surfaceAssociation='closestPoint', influenceAssociation='closestJoint')
        # connect to tongue crtl
        if cmds.objExists('GRP_PANNEL_TEMPLATE'):
            cmds.connectAttr('c_tongue_CTRL.rotateWeight', 'Tongue_M.rotateWeight', f=1)
            cmds.connectAttr('c_tongue_CTRL.drivenJoint', 'Tongue_M.drivenJoint', f=1)
            cmds.connectAttr('c_tongue_CTRL.second_vis', 'Tongue_M.vis_second', f=1)
            cmds.connectAttr('c_tongue_CTRL.output_tx', 'Tongue_M.tx', f=1)
            cmds.connectAttr('c_tongue_CTRL.output_ty', 'Tongue_M.ty', f=1)
            cmds.connectAttr('c_tongue_CTRL.output_stretch', 'Tongue_M.tz', f=1)
            cmds.connectAttr('c_tongue_CTRL.output_rx', 'Tongue_M.rx', f=1)
            cmds.connectAttr('c_tongue_CTRL.output_ry', 'Tongue_M.ry', f=1)
            cmds.connectAttr('c_tongue_CTRL.output_rz', 'Tongue_M.rz', f=1)
            cmds.setAttr('Tongue_MShape.v', 0)
        cmds.parent('GRP_tongue_Rig_all', 'GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
        cmds.delete('GRP_TONGUE_TEMPLATE', 'GRP_Tongue_M_moveShape')


    def edo_createFollicleToMeshByClosestObj(self,mesh, obj, addAimConstraint=0):
        # mesh=lfmesh
        # obj=jnt
        # addAimConstraint=1
        cn = cmds.createNode('closestPointOnMesh', n='CL_EYELIDS_CLOSEST_POINT_ON_MESH')
        cmds.connectAttr(mesh + '.outMesh', cn + '.inMesh', f=1)
        rp = cmds.xform(obj, q=1, ws=1, rp=1)
        cmds.setAttr(cn + '.inPositionX', rp[0])
        cmds.setAttr(cn + '.inPositionY', rp[1])
        cmds.setAttr(cn + '.inPositionZ', rp[2])
        # createFollicle
        fot = cmds.createNode('transform', n=obj + '_closestFollicle')
        fo = cmds.createNode('follicle', n=obj + '_closestFollicleShape', p=fot)
        cmds.connectAttr(fo + '.outTranslateX', fot + '.translateX', f=1)
        cmds.connectAttr(fo + '.outTranslateY', fot + '.translateY', f=1)
        cmds.connectAttr(fo + '.outTranslateZ', fot + '.translateZ', f=1)
        cmds.connectAttr(fo + '.outRotateX', fot + '.rotateX', f=1)
        cmds.connectAttr(fo + '.outRotateY', fot + '.rotateY', f=1)
        cmds.connectAttr(fo + '.outRotateZ', fot + '.rotateZ', f=1)
        cmds.connectAttr(mesh + '.outMesh', fo + '.inputMesh', f=1)
        cmds.connectAttr(mesh + '.worldMatrix', fo + '.inputWorldMatrix', f=1)
        cmds.setAttr(fo + '.parameterU', cmds.getAttr(cn + '.parameterU'))
        cmds.setAttr(fo + '.parameterV', cmds.getAttr(cn + '.parameterV'))
        cmds.delete(cn)
        if addAimConstraint == 1:
            ps = cmds.listRelatives(obj, p=1, pa=1)
            if ps:
                ps = cmds.listRelatives(ps[0], p=1, pa=1)
                if ps:
                    cmds.aimConstraint(fot, ps[0], mo=1, aimVector=[1, 0, 0], upVector=[0, 1, 0], worldUpType='scene')
        return fot


    def edo_findNodeFromHistory(self,node, type):
        # node=mesh
        find = []
        his = cmds.listHistory(node)
        for h in his:
            # h=his[0]
            if cmds.nodeType(h) == type:
                find.append(h)
        return find


    def edo_finishJawRig(self,edition):
        self.edo_buildClFacialRigHierarchyNode()
        if not cmds.objExists('GRP_JAW_TEMPLATE') and not cmds.objExists('GRP_PANNEL_TEMPLATE'):
            return False
        # lower connect
        cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_up', 'low_jaw_joint0.up_driven', f=1)
        cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_dn', 'low_jaw_joint0.dn_driven', f=1)
        cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_rt', 'low_jaw_joint0.lf_driven', f=1)
        cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_lf', 'low_jaw_joint0.rt_driven', f=1)
        cmds.connectAttr('c_jaw_dn_CTRL.translateX', 'low_jaw_joint0.twist_driven', f=1)
        # uper connect
        cmds.connectAttr('c_jaw_up_FRAME.fourAxis_up', 'up_jaw_joint0.up_driven', f=1)
        cmds.connectAttr('c_jaw_up_FRAME.fourAxis_dn', 'up_jaw_joint0.dn_driven', f=1)
        cmds.connectAttr('c_jaw_up_FRAME.fourAxis_rt', 'up_jaw_joint0.lf_driven', f=1)
        cmds.connectAttr('c_jaw_up_FRAME.fourAxis_lf', 'up_jaw_joint0.rt_driven', f=1)
        # create Jaw joint
        jnt = cmds.createNode('joint', n='JAW_ALL_JNT', p='GRP_JAW_TEMPLATE')
        cmds.xform('JAW_ALL_JNT', os=1, t=[0, 0, 0])
        cmds.parent('JAW_ALL_JNT', 'GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
        cmds.parent('JAW_ALL_JNT_Ctrl_GRP', 'JAW_ALL_JNT')
    
        cmds.delete('GRP_JAW_TEMPLATE')
        
        # 嘴角骨骼设置
        if edition=='HIGH':
            cmds.group('Left_jaw_joint1',n = ('Left_jaw_joint1_GRP'),parent = 'Left_jaw_joint1_GRP_GRP_GRP',relative = 1)
            cmds.group('Left_jaw_joint1_GRP',n = ('Left_jaw_joint1_GRP_GRP'),parent = 'Left_jaw_joint1_GRP_GRP_GRP',relative = 1)        
            cmds.group('Right_jaw_joint1',n = ('Right_jaw_joint1_GRP'),parent = 'Right_jaw_joint1_GRP_GRP_GRP',relative = 1)
            cmds.group('Right_jaw_joint1_GRP',n = ('Right_jaw_joint1_GRP_GRP'),parent = 'Right_jaw_joint1_GRP_GRP_GRP',relative = 1)        
            cmds.group('middle_jaw_joint1',n = ('middle_jaw_joint1_GRP'),parent = 'middle_jaw_joint1_GRP_GRP_GRP',relative = 1)
            cmds.group('middle_jaw_joint1_GRP',n = ('middle_jaw_joint1_GRP_LfRotate_GRP'),parent = 'middle_jaw_joint1_GRP_GRP_GRP',relative = 1)
            cmds.group('middle_jaw_joint1_GRP_LfRotate_GRP',n = ('middle_jaw_joint1_GRP_RtRotate_GRP'),parent = 'middle_jaw_joint1_GRP_GRP_GRP',relative = 1) 
            cmds.group('middle_jaw_joint1_GRP_RtRotate_GRP',n = ('middle_jaw_joint1_GRP_GRP'),parent = 'middle_jaw_joint1_GRP_GRP_GRP',relative = 1)                            
            LfJaw_PC = cmds.parentConstraint('up_jaw_joint1_locator1', 'low_jaw_joint1_locator1', 'Left_jaw_joint1_GRP_GRP', mo=1)
            RtJaw_PC = cmds.parentConstraint('up_jaw_joint1_locator1', 'low_jaw_joint1_locator1', 'Right_jaw_joint1_GRP_GRP', mo=1)
            MidJaw_PC = cmds.parentConstraint('up_jaw_joint1_locator1', 'low_jaw_joint1_locator1', 'middle_jaw_joint1_GRP_GRP', mo=1)
            SK_hideLockAll('Left_jaw_joint1',1,1,1)
            SK_hideLockAll('Right_jaw_joint1',1,1,1)
            SK_hideLockAll('middle_jaw_joint1',1,1,1)
            cmds.addAttr('middle_jaw_joint1',ln = 'Twist',at = 'double',min = 0,max=100,dv =30)
            cmds.setAttr('middle_jaw_joint1.Twist',k = 1)
            # 加入嘴角控制器约束骨骼动态效果       
            LRM_jaw_setRange = cmds.shadingNode('setRange',name = 'LRM_jaw_setRange',asUtility = 1)
            cmds.setAttr(LRM_jaw_setRange+'.min',0,0,0.325)
            cmds.setAttr(LRM_jaw_setRange+'.max',1,1,0.675)
            cmds.setAttr(LRM_jaw_setRange+'.oldMin',-1,-1,-1)
            cmds.setAttr(LRM_jaw_setRange+'.oldMax',1,1,1)
            LRM_jaw_MD = cmds.createNode('multiplyDivide',n = 'LRM_jaw_MD',ss = True)
            cmds.connectAttr('c_Lf_mouthLip_CTRL.translateY', LRM_jaw_MD+'.input1X', f=1)
            cmds.connectAttr('c_Rt_mouthLip_CTRL.translateY', LRM_jaw_MD+'.input1Y', f=1)            
            #cmds.connectAttr('c_Mid_mouthLip_CTRL.translateY', LRM_jaw_MD+'.input1Z', f=1)
            cmds.connectAttr('c_Lf_mouthLip_CTRL.follow', LRM_jaw_MD+'.input2X', f=1)
            cmds.connectAttr('c_Rt_mouthLip_CTRL.follow', LRM_jaw_MD+'.input2Y', f=1)            
            #cmds.connectAttr('c_Mid_mouthLip_CTRL.follow', LRM_jaw_MD+'.input2Z', f=1)
            cmds.connectAttr(LRM_jaw_MD+'.outputX', LRM_jaw_setRange+'.valueX', f=1)
            cmds.connectAttr(LRM_jaw_MD+'.outputY', LRM_jaw_setRange+'.valueY', f=1)
            #cmds.connectAttr(LRM_jaw_MD+'.outputZ', LRM_jaw_setRange+'.valueZ', f=1)                          
            cmds.connectAttr(LRM_jaw_setRange+'.outValueX ',LfJaw_PC[0]+'.w0')             
            cmds.connectAttr(LRM_jaw_setRange+'.outValueY ',RtJaw_PC[0]+'.w0')
            cmds.connectAttr(LRM_jaw_setRange+'.outValueZ ',MidJaw_PC[0]+'.w0')  
            LRM_jaw_reverse = cmds.createNode('reverse',n = 'LRM_jaw_reverse',ss = True)                                                         
            cmds.connectAttr(LRM_jaw_setRange+'.outValueX ',LRM_jaw_reverse+'.inputX') 
            cmds.connectAttr(LRM_jaw_setRange+'.outValueY ',LRM_jaw_reverse+'.inputY')            
            cmds.connectAttr(LRM_jaw_setRange+'.outValueZ ',LRM_jaw_reverse+'.inputZ')
            cmds.connectAttr(LRM_jaw_reverse+'.outputX ',LfJaw_PC[0]+'.w1')                         
            cmds.connectAttr(LRM_jaw_reverse+'.outputY ',RtJaw_PC[0]+'.w1')             
            cmds.connectAttr(LRM_jaw_reverse+'.outputZ ',MidJaw_PC[0]+'.w1')
            # 加减节点融合左右控制器数值赋予中间骨骼约束的setRange节点Z轴
            LRM_jaw_plusMinusAverage = cmds.createNode('plusMinusAverage',n = 'LRM_jaw_plusMinusAverage',ss = True)
            cmds.setAttr(LRM_jaw_plusMinusAverage+'.operation',3)
            cmds.connectAttr(LRM_jaw_MD+'.outputX', LRM_jaw_plusMinusAverage+'.i1[0]', f=1)
            cmds.connectAttr(LRM_jaw_MD+'.outputY', LRM_jaw_plusMinusAverage+'.i1[1]', f=1)
            cmds.connectAttr(LRM_jaw_plusMinusAverage+'.output1D',LRM_jaw_setRange+'.valueZ', f=1)            
            # 添加中间骨骼旋转驱动
            Mid_jaw_Rotate_MD = cmds.createNode('multiplyDivide',n = 'Mid_jaw_Rotate_MD',ss = True)
            cmds.connectAttr('c_Lf_mouthLip_CTRL.translateY', Mid_jaw_Rotate_MD+'.input1X', f=1)
            cmds.connectAttr('c_Rt_mouthLip_CTRL.translateY', Mid_jaw_Rotate_MD+'.input1Y', f=1)
            cmds.connectAttr('middle_jaw_joint1.Twist', Mid_jaw_Rotate_MD+'.input2X', f=1)
            cmds.connectAttr('middle_jaw_joint1.Twist', Mid_jaw_Rotate_MD+'.input2Y', f=1)
            cmds.connectAttr(Mid_jaw_Rotate_MD+'.outputX', 'middle_jaw_joint1_GRP_LfRotate_GRP.rotateZ', f=1) 
            Mid_jaw_Rotate_reverse = cmds.createNode('reverse',n = 'Mid_jaw_Rotate_reverse',ss = True) 
            cmds.connectAttr(Mid_jaw_Rotate_MD+'.outputY', Mid_jaw_Rotate_reverse+'.inputY', f=1)                                                       
            cmds.connectAttr(Mid_jaw_Rotate_reverse+'.outputY', 'middle_jaw_joint1_GRP_RtRotate_GRP.rotateZ', f=1)                                                                           
        # 添加牙齿设置
        self.CJW_clearGroup(['UpperTooth_Ctrl','LowerTooth_Ctrl'])
        Tooth_secondCtrls =cmds.ls('UpperTooth_second0*_Ctrl','LowerTooth_second0*_Ctrl') 
        self.CJW_clearGroup(Tooth_secondCtrls)
        
        UpToothsMeshes = cmds.textField('get_UpperToothmeshes_line', q=1, tx=1)
        if UpToothsMeshes:
            UpToothsMeshs = UpToothsMeshes.split(',')
            for UpToothsMesh in UpToothsMeshs:
                cmds.skinCluster('UpperTooth_Ctrl_joint1',UpToothsMesh,rfs=0, tsb=1, mi=30,nw=1)
            UpToothWire = cmds.wire( UpToothsMeshs,name='UpperTooth_wire',gw = False ,en = 1 ,ce = 0 , li = 0 ,dds = [(0,10),(1,1)],w = 'UpperTooth_curve')
            cmds.skinCluster('UpperTooth_Ctrl_joint1',UpToothWire[1]+'BaseWire',rfs=0, tsb=1, mi=30,nw=1)            
        LowToothsMeshes = cmds.textField('get_LowerToothmeshes_line', q=1, tx=1)
        if LowToothsMeshes:
            LowToothsMeshs = LowToothsMeshes.split(',')
            for LowToothsMesh in LowToothsMeshs:
                cmds.skinCluster('LowerTooth_Ctrl_joint1',LowToothsMesh,rfs=0, tsb=1, mi=30,nw=1)
            LowToothWire = cmds.wire( LowToothsMeshs,name='LowerTooth_wire',gw = False ,en = 1 ,ce = 0 , li = 0 ,dds = [(0,10),(1,1)],w = 'LowerTooth_curve')
            cmds.skinCluster('LowerTooth_Ctrl_joint1',LowToothWire[1]+'BaseWire',rfs=0, tsb=1, mi=30,nw=1)
                           
        if cmds.objExists('GRP_tongueRig'):
            # cmds.parentConstraint('low_jaw_joint0','GRP_tongueRig',mo=1)
            cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_up', 'c_tongue_joint1.up_driven', f=1)
            cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_dn', 'c_tongue_joint1.dn_driven', f=1)
            cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_rt', 'c_tongue_joint1.lf_driven', f=1)
            cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_lf', 'c_tongue_joint1.rt_driven', f=1)
            cmds.connectAttr('low_jaw_joint0.twist_driven', 'c_tongue_joint1.twist_driven', f=1)
        
        if edition=='LOW':    
            cmds.connectAttr('c_UpperTooth_ctrl.upperTooth_Vis','UpperTooth_Ctrl_GRP.visibility')
            cmds.connectAttr('c_LowerTooth_ctrl.lowerTooth_Vis','LowerTooth_Ctrl_GRP.visibility') 

    def CJW_mirrorLipJoint(self):
        piv = cmds.xform('Left_jaw_joint1', q=1, ws=1, rp=1)
        cmds.xform('Right_jaw_joint1', ws=1, t=[piv[0] * -1, piv[1], piv[2]])
        
        Uptooth01Piv = cmds.xform('UpperTooth_second05_Ctrl', q=1, ws=1, rp=1)
        cmds.xform('UpperTooth_second01_Ctrl', ws=1, t=[Uptooth01Piv[0] * -1, Uptooth01Piv[1], Uptooth01Piv[2]])        
        Uptooth02Piv = cmds.xform('UpperTooth_second04_Ctrl', q=1, ws=1, rp=1)
        cmds.xform('UpperTooth_second02_Ctrl', ws=1, t=[Uptooth02Piv[0] * -1, Uptooth02Piv[1], Uptooth02Piv[2]])
          
        Lowtooth01Piv = cmds.xform('LowerTooth_second05_Ctrl', q=1, ws=1, rp=1)
        cmds.xform('LowerTooth_second01_Ctrl', ws=1, t=[Lowtooth01Piv[0] * -1, Lowtooth01Piv[1], Lowtooth01Piv[2]])        
        Lowtooth02Piv = cmds.xform('LowerTooth_second04_Ctrl', q=1, ws=1, rp=1)
        cmds.xform('LowerTooth_second02_Ctrl', ws=1, t=[Lowtooth02Piv[0] * -1, Lowtooth02Piv[1], Lowtooth02Piv[2]])  
                
    def CJW_finishEarRig(self):
        self.edo_buildClFacialRigHierarchyNode()
        cmds.parent('ear_L_joint0_GRP','ear_R_joint0_GRP','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
        cmds.delete('GRP_EAR_TEMPLATE')  
        cmds.connectAttr('c_Lf_ear_CTRL.translate', 'ear_L_joint0.translate', f=1)
        cmds.connectAttr('c_Lf_ear_CTRL.rotate', 'ear_L_joint0.rotate', f=1)
        cmds.connectAttr('c_Lf_ear_CTRL.scale', 'ear_L_joint0.scale', f=1)
        cmds.connectAttr('c_Lf_ear_CTRL.rotate', 'ear_L_joint1.rotate', f=1)
        
        cmds.connectAttr('c_Rt_ear_CTRL.translate', 'ear_R_joint0.translate', f=1)
        cmds.connectAttr('c_Rt_ear_CTRL.rotate', 'ear_R_joint0.rotate', f=1)
        cmds.connectAttr('c_Rt_ear_CTRL.scale', 'ear_R_joint0.scale', f=1) 
        cmds.connectAttr('c_Rt_ear_CTRL.rotate', 'ear_R_joint1.rotate', f=1)
        
    def CJW_mirrorEarJoint(self):
        EarJointPiv_T = cmds.xform('Lf_ear_TEMPLATE', q=1, ws=1, rp=1)
        EarJointPiv_R = cmds.getAttr('Lf_ear_TEMPLATE.rotate')[0]
        EarJointPiv_S = cmds.getAttr('Lf_ear_TEMPLATE.scale')[0]
        cmds.xform('Rt_ear_TEMPLATE', ws=1, t=[EarJointPiv_T[0]*-1, EarJointPiv_T[1], EarJointPiv_T[2]])
        cmds.setAttr('Rt_ear_TEMPLATE.rotate',EarJointPiv_R[0],EarJointPiv_R[1]*-1,EarJointPiv_R[2]*-1)
        cmds.setAttr('Rt_ear_TEMPLATE.scale',EarJointPiv_S[0],EarJointPiv_S[1],EarJointPiv_S[2])
        
    def CJW_clearGroup(self,Ctrls):
        for Ctrl in Ctrls:
            Ctrl_T = cmds.getAttr(Ctrl+'.translate')[0]
            Ctrl_R= cmds.getAttr(Ctrl+'.rotate')[0]
            Ctrl_S = cmds.getAttr(Ctrl+'.scale')[0]
            cmds.setAttr(Ctrl+'.translate',0,0,0)
            cmds.setAttr(Ctrl+'.rotate',0,0,0)
            cmds.setAttr(Ctrl+'.scale',1,1,1)
            clearGRP = cmds.group(Ctrl,name= Ctrl+'_clearGRP')
            cmds.setAttr(clearGRP+'.translate',Ctrl_T[0],Ctrl_T[1],Ctrl_T[2])
            cmds.setAttr(clearGRP+'.rotate',Ctrl_R[0],Ctrl_R[1],Ctrl_R[2])
            cmds.setAttr(clearGRP+'.scale',Ctrl_S[0],Ctrl_S[1],Ctrl_S[2])
            
        
        
    def edo_cl_mirrorFacialLfEyelidsDrivenMeshRoRightAndAutoConnections(self):
        rtbsmaker = 'Rteyelids_getbs_skeleton_dirvenMesh_'
        if not cmds.objExists(rtbsmaker):
            print 'error ! there is no object what name is ' + rtbsmaker
            return False
        rteyelidsDrivenMesh = 'Rteyelids_skeleton_dirvenMesh_'
        if not cmds.objExists(rteyelidsDrivenMesh):
            print 'error ! there is no object what name is ' + rteyelidsDrivenMesh
            return False
        lfctrl = 'c_Lf_up_eyelids_CTRL'
        if not cmds.objExists(lfctrl):
            print 'error ! there is no object what name is ' + lfctrl
            return False
        rtctrl = 'c_Rt_up_eyelids_CTRL'
        if not cmds.objExists(rtctrl):
            print 'error ! there is no object what name is ' + rtctrl
            return False
        lfdnctrl = 'c_Lf_dn_eyelids_CTRL'
        if not cmds.objExists(lfctrl):
            print 'error ! there is no object what name is ' + lfdnctrl
            return False
        rtdnctrl = 'c_Rt_dn_eyelids_CTRL'
        if not cmds.objExists(rtctrl):
            print 'error ! there is no object what name is ' + rtdnctrl
            return False
        print 'mirror eyelids start...'
        frames = ['c_Lf_up_eyelids_CTRL_up', 'c_Lf_up_eyelids_CTRL_rtup', 'c_Lf_up_eyelids_CTRL_lfup', 'c_Lf_up_eyelids_CTRL_dn', 'c_Lf_up_eyelids_CTRL_rtdn', 'c_Lf_up_eyelids_CTRL_lfdn', 'c_Lf_up_eyelids_CTRL_lf', 'c_Lf_up_eyelids_CTRL_rt']
        for frame in frames:
            # frame=frames[0]
            if cmds.objExists(frame):
                if 'RL_up' == frame[-5:]:
                    print 'make up blendshape'
                    cmds.setAttr(lfctrl + '.ty', 1)
                    cmds.setAttr(lfctrl + '.tx', 0)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfctrl + '.ty', 0)
                if 'RL_dn' == frame[-5:]:
                    print 'make dn blendshape'
                    cmds.setAttr(lfctrl + '.ty', -1)
                    cmds.setAttr(lfctrl + '.tx', 0)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfctrl + '.ty', 0)
                if 'RL_lf' == frame[-5:]:
                    print 'make lf blendshape'
                    cmds.setAttr(lfctrl + '.tx', -1)
                    cmds.setAttr(lfctrl + '.ty', 0)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfctrl + '.tx', 0)
                if 'RL_rt' == frame[-5:]:
                    print 'make rt blendshape'
                    cmds.setAttr(lfctrl + '.tx', 1)
                    cmds.setAttr(lfctrl + '.ty', 0)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfctrl + '.tx', 0)
                if '_lfup' == frame[-5:]:
                    print 'make lfup blendshape'
                    cmds.setAttr(lfctrl + '.tx', -1)
                    cmds.setAttr(lfctrl + '.ty', 1)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfctrl + '.tx', 0)
                    cmds.setAttr(lfctrl + '.ty', 0)
                if '_lfdn' == frame[-5:]:
                    print 'make lfdn blendshape'
                    cmds.setAttr(lfctrl + '.tx', -1)
                    cmds.setAttr(lfctrl + '.ty', -1)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfctrl + '.tx', 0)
                    cmds.setAttr(lfctrl + '.ty', 0)
                if '_rtup' == frame[-5:]:
                    print 'make rtup blendshape'
                    cmds.setAttr(lfctrl + '.tx', 1)
                    cmds.setAttr(lfctrl + '.ty', 1)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfctrl + '.tx', 0)
                    cmds.setAttr(lfctrl + '.ty', 0)
                if '_rtdn' == frame[-5:]:
                    print 'make rtdn blendshape'
                    cmds.setAttr(lfctrl + '.tx', 1)
                    cmds.setAttr(lfctrl + '.ty', -1)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfctrl + '.tx', 0)
                    cmds.setAttr(lfctrl + '.ty', 0)
        # mirror down eyelids blendshape
        frames = ['c_Lf_dn_eyelids_CTRL_up', 'c_Lf_dn_eyelids_CTRL_rtup', 'c_Lf_dn_eyelids_CTRL_lfup', 'c_Lf_dn_eyelids_CTRL_dn', 'c_Lf_dn_eyelids_CTRL_rtdn', 'c_Lf_dn_eyelids_CTRL_lfdn', 'c_Lf_dn_eyelids_CTRL_lf', 'c_Lf_dn_eyelids_CTRL_rt']
        for frame in frames:
            # frame=frames[0]
            if cmds.objExists(frame):
                if 'RL_up' == frame[-5:]:
                    print 'make up blendshape'
                    cmds.setAttr(lfdnctrl + '.ty', 1)
                    cmds.setAttr(lfdnctrl + '.tx', 0)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfdnctrl + '.ty', 0)
                if 'RL_dn' == frame[-5:]:
                    print 'make dn blendshape'
                    cmds.setAttr(lfdnctrl + '.ty', -1)
                    cmds.setAttr(lfdnctrl + '.tx', 0)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfdnctrl + '.ty', 0)
                if 'RL_lf' == frame[-5:]:
                    print 'make lf blendshape'
                    cmds.setAttr(lfdnctrl + '.tx', -1)
                    cmds.setAttr(lfdnctrl + '.ty', 0)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfdnctrl + '.tx', 0)
                if 'RL_rt' == frame[-5:]:
                    print 'make rt blendshape'
                    cmds.setAttr(lfdnctrl + '.tx', 1)
                    cmds.setAttr(lfdnctrl + '.ty', 0)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfdnctrl + '.tx', 0)
                if '_lfup' == frame[-5:]:
                    print 'make lfup blendshape'
                    cmds.setAttr(lfdnctrl + '.tx', -1)
                    cmds.setAttr(lfdnctrl + '.ty', 1)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfdnctrl + '.tx', 0)
                    cmds.setAttr(lfdnctrl + '.ty', 0)
                if '_lfdn' == frame[-5:]:
                    print 'make lfdn blendshape'
                    cmds.setAttr(lfdnctrl + '.tx', -1)
                    cmds.setAttr(lfdnctrl + '.ty', -1)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfdnctrl + '.tx', 0)
                    cmds.setAttr(lfdnctrl + '.ty', 0)
                if '_rtup' == frame[-5:]:
                    print 'make rtup blendshape'
                    cmds.setAttr(lfdnctrl + '.tx', 1)
                    cmds.setAttr(lfdnctrl + '.ty', 1)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfdnctrl + '.tx', 0)
                    cmds.setAttr(lfdnctrl + '.ty', 0)
                if '_rtdn' == frame[-5:]:
                    print 'make rtdn blendshape'
                    cmds.setAttr(lfdnctrl + '.tx', 1)
                    cmds.setAttr(lfdnctrl + '.ty', -1)
                    bs = cmds.duplicate(rtbsmaker)
                    cmds.setAttr(bs[0] + '.v', 1)
                    cmds.setAttr(bs[0] + '.sx', 1)
                    nbs = cmds.rename(bs[0], 'BS__' + rteyelidsDrivenMesh + '__xxxx')
                    self.edo_clearFacialBlendShapeInFrame(frame.replace('Lf', 'Rt'))
                    cmds.parent(nbs, frame.replace('Lf', 'Rt'))
                    cmds.setAttr(lfdnctrl + '.tx', 0)
                    cmds.setAttr(lfdnctrl + '.ty', 0)
        edo_autoConnectBlendShapeUI.edo_opBlendShapeByFacialCtrl(rtctrl)
        edo_autoConnectBlendShapeUI.edo_addBlendShapeAndExpressionsByFacialCtrl(rtctrl)
        edo_autoConnectBlendShapeUI.edo_opBlendShapeByFacialCtrl(rtdnctrl)
        edo_autoConnectBlendShapeUI.edo_addBlendShapeAndExpressionsByFacialCtrl(rtdnctrl)


    def edo_clearFacialBlendShapeInFrame(self,frame):
        # frame='c_Rt_up_eyelids_CTRL_up'
        cs = cmds.listRelatives(frame, c=1, pa=1)
        for c in cs:
            # c=cs[0]
            cc = cmds.listRelatives(c, shapes=1, pa=1)
            if cc:
                cshape = cc[0]
                if cmds.nodeType(cshape) == 'mesh':
                    print 'clear .. ' + frame + ' .. ' + c
                    cmds.delete(c)

    def CJW_Head_Stretch(self):
        selectVtx = cmds.ls(sl=1)
        if selectVtx==None or selectVtx==[]:
            cmds.error(u'=====请选择相关的点=====')
        Head_ffd01 = cmds.lattice(name = 'head_stretch_ffd01',divisions=(4,12,4),objectCentered=True,ldv = (2,2,2))
        cmds.setAttr(Head_ffd01[0]+'.outsideLattice',1)
        Head_squash01 = cmds.nonLinear(Head_ffd01[1],name = 'head_stretch_squash01',type = 'squash',lowBound = 0,highBound = 2) 
        cmds.setAttr((Head_squash01[1]+'.translateY'),cmds.getAttr(Head_squash01[1]+'.translateY') - cmds.getAttr(Head_squash01[1]+'.scaleX'))
        Head_cluster01 = cmds.cluster(Head_ffd01[1],name='head_stretch_cluster01',relative = True,envelope=1)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][0][0]'),v = 0.0)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][0][1]'),v = 0.0)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][0][2]'),v = 0.0)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][0][3]'),v = 0.0)        
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][1][0]'),v = 0.04)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][1][1]'),v = 0.04)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][1][2]'),v = 0.04)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][1][3]'),v = 0.04)        
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][2][0]'),v = 0.1)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][2][1]'),v = 0.1)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][2][2]'),v = 0.1)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][2][3]'),v = 0.1)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][3][0]'),v = 0.2)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][3][1]'),v = 0.2)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][3][2]'),v = 0.2)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][3][3]'),v = 0.2)        
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][4][0]'),v = 0.3)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][4][1]'),v = 0.3)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][4][2]'),v = 0.3)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][4][3]'),v = 0.3)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][5][0]'),v = 0.4)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][5][1]'),v = 0.4)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][5][2]'),v = 0.4)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][5][3]'),v = 0.4)       
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][6][0]'),v = 0.5)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][6][1]'),v = 0.5)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][6][2]'),v = 0.5)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][6][3]'),v = 0.5)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][7][0]'),v = 0.6)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][7][1]'),v = 0.6)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][7][2]'),v = 0.6)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][7][3]'),v = 0.6)        
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][8][0]'),v = 0.7)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][8][1]'),v = 0.7)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][8][2]'),v = 0.7)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][8][3]'),v = 0.7)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][9][0]'),v = 0.8)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][9][1]'),v = 0.8)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][9][2]'),v = 0.8)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][9][3]'),v = 0.8)         
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][10][0]'),v = 0.9)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][10][1]'),v = 0.9)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][10][2]'),v = 0.9)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][10][3]'),v = 0.9)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][11][0]'),v = 1)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][11][1]'),v = 1)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][11][2]'),v = 1)
        cmds.percent(Head_cluster01[0],(Head_ffd01[1]+'.pt[0:3][11][3]'),v = 1)         
        templatePath = AutoRigPath + 'face_BS/TemplateFile'
        cmds.file(templatePath + '/Head_stretch_rig.ma', i=1)
        cmds.setAttr(('head_stretch_Ctrl_GRP.translateY'),cmds.getAttr(Head_ffd01[1]+'.translateY') + cmds.getAttr(Head_squash01[1]+'.scaleX')+4)
        cmds.setAttr(('head_stretch_top_Ctrl_GRP.translateY'),cmds.getAttr(Head_ffd01[1]+'.translateY') + cmds.getAttr(Head_squash01[1]+'.scaleX')+2)
        cmds.setAttr(('head_stretch_bottom_Ctrl_GRP.translateY'),cmds.getAttr(Head_ffd01[1]+'.translateY') - cmds.getAttr(Head_squash01[1]+'.scaleX')-2)        
        cmds.setAttr(('head_stretch_bottom_Ctrl_GRP.translateZ'),2)        
        head_stretch_tXrZ_MD = cmds.createNode('multiplyDivide',n = 'head_stretch_tXrZ_MD',ss = True)
        cmds.connectAttr('head_stretch_Ctrl.translateX', head_stretch_tXrZ_MD+'.input1X', f=1)
        cmds.connectAttr('head_stretch_Ctrl.translateX', head_stretch_tXrZ_MD+'.input1Z', f=1)
        cmds.connectAttr(head_stretch_tXrZ_MD+'.outputX', Head_cluster01[1]+'.translateX', f=1)
        cmds.connectAttr(head_stretch_tXrZ_MD+'.outputZ', Head_cluster01[1]+'.rotateZ', f=1)
        cmds.connectAttr('head_stretch_Ctrl.T', head_stretch_tXrZ_MD+'.input2X', f=1)
        cmds.connectAttr('head_stretch_Ctrl.inverseR', head_stretch_tXrZ_MD+'.input2Z', f=1)
        cmds.connectAttr('head_stretch_Ctrl.translateY', head_stretch_tXrZ_MD+'.input1Y', f=1)
        cmds.connectAttr('head_stretch_Ctrl.squash', head_stretch_tXrZ_MD+'.input2Y', f=1)
        cmds.connectAttr(head_stretch_tXrZ_MD+'.outputY', Head_squash01[0]+'.factor', f=1)
        head_stretch_tZrX_MD = cmds.createNode('multiplyDivide',n = 'head_stretch_tZrX_MD',ss = True)
        cmds.connectAttr('head_stretch_Ctrl.translateZ', head_stretch_tZrX_MD+'.input1Z', f=1)
        cmds.connectAttr('head_stretch_Ctrl.translateZ', head_stretch_tZrX_MD+'.input1X', f=1)
        cmds.connectAttr(head_stretch_tZrX_MD+'.outputZ', Head_cluster01[1]+'.translateZ', f=1)
        cmds.connectAttr(head_stretch_tZrX_MD+'.outputX', Head_cluster01[1]+'.rotateX', f=1)
        cmds.connectAttr('head_stretch_Ctrl.T', head_stretch_tZrX_MD+'.input2Z', f=1)
        cmds.connectAttr('head_stretch_Ctrl.R', head_stretch_tZrX_MD+'.input2X', f=1)
        cmds.connectAttr('head_stretch_Ctrl.rotateY', Head_cluster01[1]+'.rotateY', f=1)
        cmds.connectAttr('head_stretch_Ctrl.scale', Head_cluster01[1]+'.scale', f=1)        
        Head_cluster02 = cmds.cluster(Head_ffd01[1],name='head_stretch_cluster01',relative = True,envelope=1)   
        cmds.percent(Head_cluster02[0],(Head_ffd01[1]+'.pt[0:3][0:3][0:3]'),v = 0.0)
        cmds.percent(Head_cluster02[0],(Head_ffd01[1]+'.pt[0:3][4][0:3]'),v = 0.047)
        cmds.percent(Head_cluster02[0],(Head_ffd01[1]+'.pt[0:3][5][0:3]'),v = 0.125)
        cmds.percent(Head_cluster02[0],(Head_ffd01[1]+'.pt[0:3][6][0:3]'),v = 0.265)
        cmds.percent(Head_cluster02[0],(Head_ffd01[1]+'.pt[0:3][7][0:3]'),v = 0.457)
        cmds.percent(Head_cluster02[0],(Head_ffd01[1]+'.pt[0:3][8][0:3]'),v = 0.674)
        cmds.percent(Head_cluster02[0],(Head_ffd01[1]+'.pt[0:3][9][0:3]'),v = 0.836) 
        cmds.percent(Head_cluster02[0],(Head_ffd01[1]+'.pt[0:3][10][0:3]'),v = 0.938) 
        cmds.percent(Head_cluster02[0],(Head_ffd01[1]+'.pt[0:3][11][0:3]'),v = 1)        
        Head_squash02 = cmds.nonLinear(Head_ffd01[1],type = 'squash',lowBound = 0,highBound = 1.09)
        cmds.createNode('multiplyDivide',n = 'head_stretch_top_tXrZ_MD',ss = True)
        cmds.connectAttr('head_stretch_top_Ctrl.translateX', 'head_stretch_top_tXrZ_MD.input1X', f=1)
        cmds.connectAttr('head_stretch_top_Ctrl.translateX', 'head_stretch_top_tXrZ_MD.input1Z', f=1)
        cmds.connectAttr('head_stretch_top_tXrZ_MD.outputX', Head_cluster02[1]+'.translateX', f=1)
        cmds.connectAttr('head_stretch_top_tXrZ_MD.outputZ', Head_cluster02[1]+'.rotateZ', f=1)
        cmds.connectAttr('head_stretch_top_Ctrl.T', 'head_stretch_top_tXrZ_MD.input2X', f=1)
        cmds.connectAttr('head_stretch_top_Ctrl.inverseR', 'head_stretch_top_tXrZ_MD.input2Z', f=1)
        cmds.connectAttr('head_stretch_top_Ctrl.translateY', 'head_stretch_top_tXrZ_MD.input1Y', f=1)
        cmds.connectAttr('head_stretch_top_Ctrl.squash', 'head_stretch_top_tXrZ_MD.input2Y', f=1)
        cmds.connectAttr('head_stretch_top_tXrZ_MD.outputY', Head_squash02[0]+'.factor', f=1)
        cmds.createNode('multiplyDivide',n = 'head_stretch_top_tZrX_MD',ss = True)
        cmds.connectAttr('head_stretch_top_Ctrl.translateZ', 'head_stretch_top_tZrX_MD.input1Z', f=1)
        cmds.connectAttr('head_stretch_top_Ctrl.translateZ', 'head_stretch_top_tZrX_MD.input1X', f=1)
        cmds.connectAttr('head_stretch_top_tZrX_MD.outputZ', Head_cluster02[1]+'.translateZ', f=1)
        cmds.connectAttr('head_stretch_top_tZrX_MD.outputX', Head_cluster02[1]+'.rotateX', f=1)
        cmds.connectAttr('head_stretch_top_Ctrl.T', 'head_stretch_top_tZrX_MD.input2Z', f=1)
        cmds.connectAttr('head_stretch_top_Ctrl.R', 'head_stretch_top_tZrX_MD.input2X', f=1)
        cmds.connectAttr('head_stretch_top_Ctrl.rotateY', Head_cluster02[1]+'.rotateY', f=1)
        cmds.connectAttr('head_stretch_top_Ctrl.scale', Head_cluster02[1]+'.scale', f=1)
        if not cmds.objExists('GRP_head_stretch_Deformer_GRP'):
            cmds.group(em=True,name = 'GRP_head_stretch_Deformer_GRP')
        cmds.parent(Head_ffd01[1],Head_ffd01[2],Head_squash01[1],Head_cluster01[1],Head_cluster02[1],Head_squash02[1],'GRP_head_stretch_Deformer_GRP')    
        cmds.select(cl=1)
    def CJW_Head_Stretch_jaw(self):
        selectVtx02 = cmds.ls(sl=1)
        if selectVtx02 == None or selectVtx02 == []:
            cmds.error(u'=====请选择相关的点=====')
        Head_ffd02 = cmds.lattice(name = 'head_stretch_jaw_ffd01',divisions=(8,7,6),objectCentered=True,ldv = (2,2,2))
        cmds.setAttr(Head_ffd02[0]+'.outsideLattice',1)
        Head_cluster04 = cmds.cluster(name='head_stretch_jaw_cluster',relative = True,envelope=1)   
        cmds.percent(Head_cluster04[0],(Head_ffd02[1]+'.pt[0:7][0:6][0]'),v = 0.0) 
        cmds.percent(Head_cluster04[0],(Head_ffd02[1]+'.pt[0:7][0:5][1]'),v = 0.24) 
        cmds.percent(Head_cluster04[0],(Head_ffd02[1]+'.pt[0:7][0:5][2]'),v = 0.475) 
        cmds.percent(Head_cluster04[0],(Head_ffd02[1]+'.pt[0:7][0:5][3]'),v = 0.768)
                                            
        cmds.percent(Head_cluster04[0],(Head_ffd02[1]+'.pt[0:7][6][0:5]'),v = 0.0)             
        cmds.percent(Head_cluster04[0],(Head_ffd02[1]+'.pt[0:7][5][1:5]'),v = 0.24)
        cmds.percent(Head_cluster04[0],(Head_ffd02[1]+'.pt[0:7][4][2:5]'),v = 0.475)  
        cmds.percent(Head_cluster04[0],(Head_ffd02[1]+'.pt[0:7][3][3:5]'),v = 0.768)                          
            
        Head_ffd01 = ['head_stretch_ffd01','head_stretch_ffd01Lattice','head_stretch_ffd01Base']
        if  cmds.objExists(Head_ffd01[1]):
            cmds.select(Head_ffd01[1]+'.pt[0:3][1:3][0:3]')
            Head_cluster03 = cmds.cluster(name='head_stretch_jaw_scale_cluster03',relative = True,envelope=1)
            cmds.percent(Head_cluster03[0],(Head_ffd01[1]+'.pt[0:3][1:3][0:1]'),v = 0.0)        
            cmds.percent(Head_cluster03[0],(Head_ffd01[1]+'.pt[0:3][3][2:3]'),v = 0.664)
            cmds.percent(Head_cluster03[0],(Head_ffd01[1]+'.pt[0:3][1][2:3]'),v = 0.664)
            head_stretch_bottom_clamp = cmds.createNode('clamp',n = 'head_stretch_bottom_clamp',ss = True)
            cmds.setAttr(head_stretch_bottom_clamp+'.minR',-10000)
            cmds.setAttr(head_stretch_bottom_clamp+'.minG',0)
            cmds.setAttr(head_stretch_bottom_clamp+'.minB',0)
            cmds.setAttr(head_stretch_bottom_clamp+'.maxR',10000)
            cmds.setAttr(head_stretch_bottom_clamp+'.maxG',10000)
            cmds.setAttr(head_stretch_bottom_clamp+'.maxB',10000)
            cmds.connectAttr('head_stretch_bottom_Ctrl.translateY', head_stretch_bottom_clamp+'.inputR', f=1)
            cmds.connectAttr('head_stretch_bottom_Ctrl.translateY', head_stretch_bottom_clamp+'.inputG', f=1)
            cmds.connectAttr('head_stretch_bottom_Ctrl.translateY', head_stretch_bottom_clamp+'.inputB', f=1)
            head_stretch_bottom_scale_MD = cmds.createNode('multiplyDivide',n = 'head_stretch_bottom_scale_MD',ss = True)
            cmds.setAttr(head_stretch_bottom_scale_MD+'.input2X',-1)
            cmds.setAttr(head_stretch_bottom_scale_MD+'.input2Y',-1)
            cmds.setAttr(head_stretch_bottom_scale_MD+'.input2Z',-1)
            cmds.connectAttr(head_stretch_bottom_clamp+'.output', head_stretch_bottom_scale_MD+'.input1', f=1)
            head_stretch_bottom_reverse = cmds.createNode('reverse',n = 'head_stretch_bottom_reverse',ss = True)
            cmds.connectAttr(head_stretch_bottom_scale_MD+'.output', head_stretch_bottom_reverse+'.input', f=1)
            cmds.connectAttr(head_stretch_bottom_reverse+'.output', Head_cluster03[1]+'.scale', f=1)
            cmds.connectAttr('head_stretch_bottom_Ctrl.squash', Head_cluster03[0]+'.envelope', f=1)                   
            head_stretch_jaw_tXrZ_MD = cmds.createNode('multiplyDivide',n = 'head_stretch_jaw_tXrZ_MD',ss = True)
            cmds.connectAttr('head_stretch_bottom_Ctrl.translateY', head_stretch_jaw_tXrZ_MD+'.input1Y', f=1)
            cmds.connectAttr('head_stretch_bottom_Ctrl.translateX', head_stretch_jaw_tXrZ_MD+'.input1X', f=1)
            cmds.connectAttr('head_stretch_bottom_Ctrl.translateX', head_stretch_jaw_tXrZ_MD+'.input1Z', f=1)
            cmds.connectAttr(head_stretch_jaw_tXrZ_MD+'.outputY', Head_cluster04[1]+'.translateY', f=1)
            cmds.connectAttr(head_stretch_jaw_tXrZ_MD+'.outputX', Head_cluster04[1]+'.translateX', f=1)
            cmds.connectAttr(head_stretch_jaw_tXrZ_MD+'.outputZ', Head_cluster04[1]+'.rotateZ', f=1)
            cmds.connectAttr('head_stretch_bottom_Ctrl.T',head_stretch_jaw_tXrZ_MD+'.input2Y')
            cmds.connectAttr('head_stretch_bottom_Ctrl.T',head_stretch_jaw_tXrZ_MD+'.input2X')
            cmds.connectAttr('head_stretch_bottom_Ctrl.R',head_stretch_jaw_tXrZ_MD+'.input2Z')
            head_stretch_jaw_tZrX_MD = cmds.createNode('multiplyDivide',n = 'head_stretch_jaw_tZrX_MD',ss = True)
            cmds.connectAttr('head_stretch_bottom_Ctrl.translateZ', head_stretch_jaw_tZrX_MD+'.input1X', f=1)
            cmds.connectAttr('head_stretch_bottom_Ctrl.translateZ', head_stretch_jaw_tZrX_MD+'.input1Z', f=1)
            cmds.connectAttr(head_stretch_jaw_tZrX_MD+'.outputZ', Head_cluster04[1]+'.translateZ', f=1)
            cmds.connectAttr(head_stretch_jaw_tZrX_MD+'.outputX', Head_cluster04[1]+'.rotateX', f=1)
            cmds.connectAttr('head_stretch_bottom_Ctrl.T',head_stretch_jaw_tZrX_MD+'.input2Z')
            cmds.connectAttr('head_stretch_bottom_Ctrl.inverseR',head_stretch_jaw_tZrX_MD+'.input2X')            
            cmds.connectAttr('head_stretch_bottom_Ctrl.rotateY',Head_cluster04[1]+'.rotateY', f=1)
            cmds.connectAttr('head_stretch_bottom_Ctrl.scale',Head_cluster04[1]+'.scale', f=1)
            if not cmds.objExists('GRP_head_stretch_Deformer_GRP'):
                cmds.group(em=True,name = 'GRP_head_stretch_Deformer_GRP')
            cmds.parent(Head_ffd02[1],Head_ffd02[2],Head_cluster03[1],Head_cluster04[1],'GRP_head_stretch_Deformer_GRP')                           
            cmds.select(cl=1)
            print u'=====完成====='
            
                                               
              
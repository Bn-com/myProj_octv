# -*- coding: utf-8 -*-

'''
Created on 2016

GDC 常用工具

@author: hanhong
'''

import maya.cmds as mc
import maya.mel as mel

#GDC 常用工具
#@author: hanhong
#Data：2015/9/16
#----------------------------------------------------------------------------------------------------------#
class GDC_Tools(object):
    def __init__(self):
        pass
    #转Vray材质球【通用】
    #@author: hanhong
    #Data：2016/1/20
    #----------------------------------------------------------------------------------------------------------#
    def GDC_ShaderSwitch(self,shadetype='lambert',swi='vray',sl=1):
        if sl==0:
            shaders=mc.ls(type=shadetype,l=1)
        else:
            shaders=[]
            objs=mc.ls(sl=1,l=1)
            for obj in objs:
                if mc.nodeType(obj) == shadetype:
                    shaders.append(obj)
        if shaders:
            for shd in shaders:
                shdNew=''
                if swi=='vray':
                    shdNew='VRayMtl_'+shd
                    if mc.objExists(shdNew):
                        mc.delete(shdNew)
                    mc.shadingNode('VRayMtl', asShader=True,n=shdNew)
                SG=mc.listConnections(shd,s=0,type = 'shadingEngine')
                if SG:
                    try:
                        mc.connectAttr((shdNew+'.outColor'),(SG[0]+'.surfaceShader'),f=1)
                    except:
                        mc.warning(u'=======================【%s】已连接或无法连接SG节点，请检查==============' %shdNew)
                        pass
                cocorcon=mc.listConnections((shd+'.color'),s=1,d=0)
                bumpcon=mc.listConnections((shd+'.normalCamera'),s=1,d=0)
                if mc.ls(cocorcon):
                    try:
                        mc.connectAttr((cocorcon[0]+'.outColor'),(shdNew+'.diffuseColor'),f=1)
                    except:
                        mc.warning(u'=======================【%s】已连接或无法连接color贴图，请检查==============' %shdNew)
                        pass
                else:
                    cor=mc.getAttr(shd+'.color')
                    try:
                        mc.setAttr((shdNew+'.color'),cor[0][0],cor[0][1],cor[0][2],type='double3')
                    except:
                        mc.warning(u'=======================【%s】无法设置color，请检查==============' %shdNew)
                        pass
                if mc.ls(bumpcon):
                    try:
                        mc.connectAttr((bumpcon[0]+'.outNormal'),(shdNew+'.bumpMap'),f=1)
                    except:
                        mc.warning(u'=======================【%s】已连接或无法连接bump贴图，请检查==============' %shdNew)
                        pass
            print(u'=====================【%s】材质球已转为【%s】材质球====================='%(shadetype,swi))
        return 0
    #转Vray材质球【乐高】
    #@author: hanhong
    #Data：2016/1/20
    def nj_ShaderSwitch(self,sl=1):
        self.GDC_ShaderSwitch('lambert','vray',sl)
        self.GDC_ShaderSwitch('blinn','vray',sl)
        self.GDC_ShaderSwitch('phong','vray',sl)
        self.GDC_ShaderSwitch('phongE','vray',sl)
        print u'===============已转材质==========='
        return 0
    #nj项目设置要求（用在fs或动画文件中）
    #@author: hanhong
    #Data：2016/2/26
    def nj_armReturn(self):
        print '================================='
        print '===========start=================='
        print '================================='

        objs=mc.ls(sl=1,tr=1,l=1)
        ctl=[]
        if objs:
            for obj in objs:
                if '_Switch' in obj and mc.ls(mc.listRelatives(obj,s=1,f=1)) and mc.nodeType(mc.listRelatives(obj,s=1,f=1)[0])=='nurbsCurve':
                    ctl.append(obj)
        else:
            mc.warning(u'===============未选择物体，请选择物体===========')
            mc.error(u'===============未选择物体，请选择物体===========')
        if ctl:
            for ct in ctl:
                bas=ct.split('|')[-1].split(':')[0]+':'+ct.split('|')[-1].split(':')[-1].split('_')[0][0]+ct.split('|')[-1].split(':')[-1].split('_')[0][1]
                ani=''
                handJoint=''
                joints=bas+'_handJoint01'
                jointss=mc.ls(joints,l=1)
                if jointss:
                    for jo in jointss:
                        if ct.split('|')[2] in jo and ct.split('|')[3] in jo:
                             handJoint=jo
                else:
                    mc.warning(u'===============缺少【%s】============'%joints)
                    mc.error(u'===============缺少【%s】============'%joints)

                if handJoint=='':
                    mc.warning(u'===============缺少【%s】============'%joints)
                    mc.error(u'===============缺少【%s】============'%joints)

                if mc.objExists(ct+'.IKFK') and mc.getAttr(ct+'.IKFK')==1:
                    anim=bas+'Arm_Wrist_IK'
                    anis=mc.ls(anim,l=1)
                    for an in anis:
                        if ct.split('|')[2] in an and ct.split('|')[3] in an:
                            ani=an
                if mc.objExists(ct+'.IKFK') and mc.getAttr(ct+'.IKFK')==0:
                    anim=bas+'Arm_Wrist_FK'
                    anis=mc.ls(anim,l=1)
                    for an in anis:
                        if ct.split('|')[2] in an and ct.split('|')[3] in an:
                            ani=an
                rx=mc.getAttr(ani+'.rotateX')
                mc.setKeyframe((handJoint+'.rotateX'),v=rx)
                mc.select(handJoint)
                print '================================='
                print u'===========已设置【%s】=================='%(joints+'.rotateX')
                print '================================='
        else:
            mc.warning(u'===============未选择【%s】物体，请重新选择===========' %'Switch')
            mc.error(u'===============未选择【%s】物体，请重新选择==========='%'Switch')

    #nj项目动画要求（用在fs或动画文件中，前期渲染均可使用）
    #按3显示（开或关）
    #@author: hanhong
    #Data：2016/4/29
    def gdc_smoothDisplayMesh(self,dis=2):
        headobjs=mc.ls('*MSH_head_*',tr=1,l=1)+mc.ls('*:MSH_head_*',tr=1,l=1)
        headmeshs=[]
        if headobjs:
            for obj in headobjs:
                meshs=mc.listRelatives(obj, ad=1, ni=1, type='mesh', f=1)
                if meshs:
                    for mesh in meshs:
                        mc.setAttr((mesh+'.displaySmoothMesh'),dis)
        else:
            mc.error(u'=================文件中没有【MSH_head_】,请检查文件================')
        return 0
    def gdc_smoothDisKey(self):
        headobjs=mc.ls('*MSH_head_*',tr=1,l=1)+mc.ls('*:MSH_head_*',tr=1,l=1)
        headmeshs=[]
        if headobjs:
            mesh=mc.listRelatives(headobjs[0], ad=1, ni=1, type='mesh', f=1)
            if mesh:
                dis=mc.getAttr(mesh[0]+'.displaySmoothMesh')
                if dis==0:
                    self.gdc_smoothDisplayMesh(2)
                else:
                    self.gdc_smoothDisplayMesh(0)
        else:
            mc.error(u'=================文件中没有【MSH_head_】,请检查文件================')
        return 0
    #nj项目前期
    #批量修改材质参数
    #@author: hanhong
    #Data：2016/5/17
    def nj_ExrInfo(self):
        #读取表格
        import xlrd
        reload(xlrd)
        path='Z:/Projects/Ninjago/Ninjago_scratch/TD/Exr/Material.xls'
        shotAllData = xlrd.open_workbook(path).sheets()[0]
        rowMax = shotAllData.nrows
        rowID = []
        MatIDS=[]
        Nums=[]
        for i in range(rowMax):
            MatID =shotAllData.row_values(i)[0]
            Num=shotAllData.row_values(i)[1]
            if MatID!='' and Num!='' and MatID not in MatIDS:
                MatIDS.append(MatID)
                Nums.append(Num)
        result=[MatIDS,Nums]
        return result
    def nj_MatApply(self,save=1,server=1):
        #读取表格 修改材质
        VrayMat=mc.ls(type='VRayMtl',l=1)
        MatInfo=self.nj_ExrInfo()
        Mats=MatInfo[0]
        Nums=MatInfo[1]
        s=[]
        dirty = False
        if VrayMat:
            for i in range(len(VrayMat)):
                for j in range(len(Mats)):
                    if Mats[j] in VrayMat[i]:
                        if mc.getAttr(VrayMat[i]+'.reflectionGlossiness') != Nums[j]:
                            dirty = True
                            mc.setAttr((VrayMat[i]+'.reflectionGlossiness'),Nums[j])
                            print u'================【%s】reflectionGlossiness has been modified ===============' %VrayMat[i]
        if dirty:
            if save==1 and server==0:
                filePath=mc.file(save=1,f=1)
            if save==1 and server==1:
                TempPath='D:/TempInfo/Mat/'
                mc.sysFile(TempPath, makeDir=True)
                fileName=mc.file(q=1,sn=1,shn=1)
                mc.file(rename=(TempPath+fileName))
                mc.file(save=1,f=1)
        return 0
    #nj通用渲染
    #关闭多余default渲染层可渲染属性
    #@author: hanhong
    #Data：2016/11/17
    def gdc_RenderClose(self):
        renders=mc.ls(type='renderLayer',l=1)
        for re in renders:
            if 'default' in re:
                mc.setAttr((re+'.renderable'),0)
        return 0

    #--------------------------#
    # 模型层级改名
    def modelGrpRename(self,selGrps,sgValue1,sgValue2,sgValue3,divValue1,divValue2,divValue3):
        if not selGrps:
            selGrps = mc.ls(sl=1,l=1)
        childModify = 0
        checkV1 = mc.checkBox("ddRTSegmentSubRename",q=1,v=1)
        checkV2 = mc.checkBox("ddRTSegmentSubRenameAllLev",q=1,v=1)
        if not sgValue3:
            divValue2 = ''
        if checkV1:
            childModify = 1
        if checkV2:
            childModify = 2
        if childModify == 1:
            for selGrp in selGrps:
                numTemp = 1
                firstValue = sgValue1
                #shapeSel = mc.listRelatives(selGrp,s=1)
                #if not shapeSel:
                #    firstValue = 'GRP'
                newName = mc.rename(selGrp,firstValue + divValue1 + sgValue2 + divValue2 +sgValue3 + divValue3)
                lastInfo = newName[len(firstValue):]
                childGrps = mc.listRelatives(newName,c=1,f=1)
                for childGrp in childGrps:
                    #childShape = mc.listRelatives(childGrp,s=1)
                    firstValue = sgValue1
                    #if childShape:
                    #    firstValue = sgValue1
                    #else:
                    #    firstValue = 'GRP'
                    newTempName = firstValue + lastInfo + '_%s'%numTemp
                    if mc.ls(newTempName):
                        newTempName = firstValue + lastInfo + '_%s'%(numTemp+1)
                    newTempName = newTempName.replace('__','_')
                    mc.rename(childGrp,newTempName)
                    numTemp += 1
        if childModify == 2:
            childDict = {}
            for selGrp in selGrps:
                allChildGrps = mc.listRelatives(selGrp,ad=1,type = 'transform',f=1)
                for checkGrp in allChildGrps:
                    levNum = len(checkGrp.split('|'))
                    if levNum not in childDict.keys():
                        childDict[levNum] = [checkGrp]
                    else:
                        childDict[levNum].append(checkGrp)
            levList = childDict.keys()
            for lev in range(min(levList),max(levList)+1):
                needLev = max(levList) - lev + min(levList)
                checkObjs = childDict[needLev]
                lastInfo = divValue1 + sgValue2 + divValue2 + sgValue3 + divValue3 + '_lv%s_'%needLev
                for indexNum in range(len(checkObjs)):
                    checkObj = checkObjs[indexNum]
                    firstValue = sgValue1
                    #shapeSel = mc.listRelatives(checkObj,s=1)
                    #if not shapeSel:
                    #    firstValue = 'GRP'
                    newName = firstValue + lastInfo + str(indexNum)
                    newName = newName.replace('__','_')
                    mc.rename(checkObj,newName)
    #【通用】
    #root物体
    #@author: hanhong
    #Data：2017/6/9
    def GA_RootLists(self):
        objs=mc.ls(tr=1,l=1)
        roots=[]
        for obj in objs:
            if '|' in obj and len(obj.split('|'))<3:
                roots.append(obj)
        if not roots:
            roots=[]
        return roots
    #【通用】
    #删除多余参考，用于maya2016以上版本
    #@author: hanhong
    #Data：2017/6/9
    def GA_unknownPluginsRemove(self):
        unknownPlugins = mc.unknownPlugin(list = 1, q=1)
        PluginList=[]
        if unknownPlugins:
            for plug in unknownPlugins:
                try:
                    mc.unknownPlugin(plug, r=1)
                    PluginList.append(plug)
                except:
                    mc.warning(u'【%s】unknownPlugin未删除，请检查' %plug)
                    PluginList.append(plug)
                    pass
        return PluginList

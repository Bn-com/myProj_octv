# -*- coding: utf-8 -*-

'''
Created on 2014

@author: hanhong
'''
import maya.cmds as mc
import maya.mel as mel
import re
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

from idmt.maya.py_common import sk_sceneTools
reload(sk_sceneTools)

import idmt.pipeline.db

from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
import os
class GDCAlembicCommon(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    def GDCAlembicCommonUI(self):
    # 窗口
        if mc.window('ABCcrowd', exists=True):
            mc.deleteUI('ABCcrowd')
        mc.window('ABCcrowd', title=u'ABC面板',
                  width=320, height=350, sizeable=True)
         # 面板
        form = mc.formLayout()
         # 切换面板
        tabs = mc.tabLayout('tabArnold',innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout(
            form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
         # tab_渲染工具
        child1 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label=u'创建ABC', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=1)
        mc.intSliderGrp('framemin',label='frammin', field=True, minValue=-1000, maxValue=10000, fieldMinValue=-1000, fieldMaxValue=10000, value=mc.playbackOptions(min=1,q = 1),columnAttach=[(1,'left',40),(2,'left',0),(3,'both',0)],columnWidth3 = (100,60,150))
        mc.intSliderGrp('framemax', label='frammax', field=True, minValue=-1000, maxValue=10000, fieldMinValue=-1000, fieldMaxValue=10000, value=mc.playbackOptions(max=1,q = 1),columnAttach=[(1,'left',40),(2,'left',0),(3,'both',0)],columnWidth3 = (100,60,150))        
        mc.button(label=u'导出alembic', width=130, height=30,
                   command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().GDC_alembicExr(server = 1,cachePre = 0,shotType = 1,ap=1,,UI=1)')               
        mc.button(label=u'alembic属性添加', width=130, height=30,
                 command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().GDC_alembicApply()')  
        
        mc.button(label=u'一键式创建alembic', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().GDC_alembicImp(line="pre",server = 1,shotType = 1)')  
        mc.setParent('..')  
        mc.frameLayout(label=u'Edit(Select)', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=1)
        mc.button(label=u'群组大组整理', width=130, height=30,
                 command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().gdc_clusterGroupR()')          
        mc.rowColumnLayout(numberOfColumns=2)      
 
        mc.intSliderGrp('offset',width=200,label='offset', field=True, minValue=-1000, maxValue=1000, fieldMinValue=-1000, fieldMaxValue=1000, value=0,columnAttach=[(1,'left',10),(2,'left',0),(3,'both',0)],columnWidth3 = (60,60,70))
        mc.button(label=u'set', width=30, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().gdc_clusteroffset(ot=1,sd=0)')         

            
 
        mc.floatSliderGrp('speed',width=280,label='speed', field=True, minValue=0, maxValue=100, fieldMinValue=0, fieldMaxValue=100, value=1,columnAttach=[(1,'left',10),(2,'left',0),(3,'both',0)],columnWidth3 = (60,60,70))
        mc.button(label=u'set', width=30, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().gdc_clusteroffset(ot=0,sd=1)')                 
        #  Tab
        mc.tabLayout(tabs, edit=True, tabLabel=((child1, u'群组插件')))
        mc.showWindow('ABCcrowd') 
    ############################################################################################################################
    #ABC 导出【通用】【适用于前期群组，渲染FS，场景ABC导出】
    #@author 韩虹
    #2015/03/24
    ########################################################################################################################### 
    def GDC_alembicExr(self,server = 1,cachePre = 0,shotType = 1,ap=1,UI=1):
        framemin=''
        framemax=''
        if UI==1:
            framemin=int(mc.intSliderGrp('framemin',q=1,v=1))+int(cachePre)
            framemax=int(mc.intSliderGrp('framemax',q=1,v=1))
        else:
            framemin  =   mc.playbackOptions(min=1,q = 1)
            framemax  =   mc.playbackOptions(max=1,q = 1)
        # 获取alembic临时路径
        localPath = sk_infoConfig.sk_infoConfig().alembicLocalPath(1)
        # 获取alembic服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().alembicServerPath(shotType )
        shotName=sk_infoConfig.sk_infoConfig().checkShotInfo()
        alembicName=''
        if shotType==1 or shotType==2:          
            alembicName=shotName[0]+'_'+shotName[1]+'_'+shotName[2]+'.abc'
        if shotType==3:
            alembicName=shotName[0]+'_'+shotName[1]+'_'+shotName[2]+'_'+shotName[3]+'.abc'
        if ap==1:
            self.GDC_alembicApply()
        abccommon="-frameRange"+' '+ str(framemin)+' '+str(framemax)+' -uvWrite -worldSpace -writeVisibility '+self.GDC_alembicInfo(infotype=1)[0]+' -file'+' '+str(localPath+alembicName)
        mc.select(cl=1)
        self.csl_AttrAction(line='select',attrtype='alembic')    
        mc.AbcExport(j=abccommon)
        if server==1:
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPath+alembicName) + '"' + ' ' + '"' + (serverPath+alembicName) + '"' + ' true'
            mel.eval(updateAnimCMD)
            print u'===[Updating alembic To Server]===传输[%s]完毕==='%alembicName         
           
        return [(localPath+alembicName),(serverPath+alembicName),framemin,framemax]

    ########################################################################################################################### 
    def GDC_shavealembicExr(self,server = 1,shotType = 1,ap=1):
 
        framemin  =   mc.playbackOptions(min=1,q = 1)
        framemax  =   mc.playbackOptions(max=1,q = 1)
        # 获取alembic临时路径
        localPath = sk_infoConfig.sk_infoConfig().alembicLocalPath(1)
        # 获取alembic服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().alembicServerPath(shotType )
        shotName=sk_infoConfig.sk_infoConfig().checkShotInfo()
        alembicName=''
        if shotType==1 or shotType==2:          
            alembicName=shotName[0]+'_'+shotName[1]+'_'+shotName[2]+'curve.abc'
        if shotType==3:
            alembicName=shotName[0]+'_'+shotName[1]+'_'+shotName[2]+'_'+shotName[3]+'curve.abc'
        if ap==1:
            self.GDC_alembicApply()
        abccommon="-frameRange"+' '+ str(framemin)+' '+str(framemax)+' -uvWrite -worldSpace -writeVisibility '+self.GDC_alembicInfo(infotype=1)[0]+' -file'+' '+str(localPath+alembicName)
        mc.select(cl=1)
        self.csl_AttrAction(line='select',attrtype='alembic')    
        mc.AbcExport(j=abccommon)
        if server==1:
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPath+alembicName) + '"' + ' ' + '"' + (serverPath+alembicName) + '"' + ' true'
            mel.eval(updateAnimCMD)
            print u'===[Updating alembic To Server]===传输[%s]完毕==='%alembicName         
           
        return [(localPath+alembicName),(serverPath+alembicName),framemin,framemax]
################################################################
    #ABC属性添加【通用】【输助】【将cacheSet物体添加abc属性】
    #@author 韩虹
    #2015/03/24
    ########################################################################################################################### 
    def GDC_alembicApply(self):
        cacheObjs=self.checkCacheSetObjects(otcGrp = 1)
        mc.select(cacheObjs)
        self.csl_AttrAction(line="add",attrtype="alembic")
        return cacheObjs
    ############################################################################################################################
    #ABC属性添加【通用】【输助】【返回添加ABC属性的物体】
    #@author 韩虹
    #2015/03/24
    #infotype 为1 导出信息，为0 导出信息，为3则为ABC物体信息
    ########################################################################################################################### 
    def GDC_alembicInfo(self,infotype=1):
        self.csl_AttrAction(line='select',attrtype='alembic')
        abcOjbs=mc.ls(sl=1,l=1)
        abcInfo=''
        abcInfos=[]
        if abcOjbs:
            for i in range(len(abcOjbs)):
                if infotype==0:
                    if i==0:
                        abcInfo=abcOjbs[0]
                    else:
                        abcInfo=abcInfo+' '+abcOjbs[i]
                if infotype==1:
                    if i==0:
                        abcInfo=' -root '+abcOjbs[0]
                    else:
                        abcInfo=abcInfo+' -root '+abcOjbs[i]                                                  
                if infotype==3:
                    abcInfos.append(abcOjbs[i])                                         
        else:
            print u'缺少ABC属性物体'
        if infotype==0 or infotype==1:
            abcInfos=[abcInfo]
        else:
            abcInfos=abcInfos
                                
        return abcInfos   

    ############################################################################################################################
    #abc_curve属性物体【通用】【输助】【用在shave curve】
    #@author 韩虹
    ########################################################################################################################### 
    def GDC_shaveInfo(self,infotype=0,type='abc_curve'):
        objs=mc.ls(type='transform',l=1)
        abcInfo=''
        abcInfos=[]
        abcobjs=[]
        if objs:
            for obj in objs:
                if mc.objExists(obj+'.'+type):
                    abcobjs.append(obj)
        if abcobjs:
            for i in range(len(abcobjs)):
                if infotype==0:
                    if i==0:
                        abcInfo=abcobjs[0]
                    else:
                        abcInfo=abcInfo+' '+abcobjs[i]
                if infotype==1:
                    if i==0:
                        abcInfo=' -root '+abcobjs[0]
                    else:
                        abcInfo=abcInfo+' -root '+abcobjs[i]                                                  
                if infotype==3:
                    abcInfos.append(abcobjs[i])                                         
        else:
            print u'缺少ABC属性物体'
        if infotype==0 or infotype==1:
            abcInfos=[abcInfo]
        else:
            abcInfos=abcInfos
                                
        return abcInfos    
 
   ############################################################################################################################
    #ABC属性添加【通用】【核心】【创建并导入abc（前期）】
    #@author 韩虹
    #2015/03/24
    ###########################################################################################################################  
    def GDC_alembicImp(self,line='pre',server = 1,shotType = 1):
    
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        #本机
        FlocalPath=sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        #服务器路径
        FserverPath=sk_infoConfig.sk_infoConfig().checkProjectServerPath()    
        # 获取alembic临时路径
        localPath = sk_infoConfig.sk_infoConfig().alembicLocalPath(shotType)
        # 获取alembic服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().alembicServerPath(shotType )
        if line=='pre':
            alebicName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'.abc'
            filename=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'ABC_h_ms_render.mb'
            rendername=shotInfo[0]+'_'+shotInfo[1]+'_h_ms_render.mb'
            lineName=''
            if shotInfo[1][0] in ['c']:
                lineName='characters'
            if shotInfo[1][0] in ['p']:
                lineName='props'
            if shotInfo[1][0] in ['s', 'S']:
                lineName='sets'          
            mslocalPath=FlocalPath+'ms_render/' 
            mc.sysFile(mslocalPath, makeDir=True)
            msserverPath= FserverPath+'scenes/'+ lineName+'/'+ shotInfo[1]+'/master/'
            
            #创建abc
            self.GDC_alembicApply()
            abcfile=self.GDC_alembicExr(server = server,cachePre = 0,shotType = 1,ap=1,UI=1) 
            mc.file(rename=(mslocalPath+rendername))
            mc.file(save=1,type = 'mayaBinary',f = 1)            
            mc.file( force=True, new=True )
            #打开ms_render文件并导入abc           
            mc.file((msserverPath+rendername),options='v=0',type='mayaBinary',f=1,o=1)
            mc.file(rename=(mslocalPath+rendername))
            mc.file(save=1,type = 'mayaBinary',f = 1)
            #设置帧数
            #开始帧
            mc.playbackOptions(min=int(abcfile[2]))
            preStartFrame = int(abcfile[2]) - 12
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=int(abcfile[3]))
            # 结束预留
            posEndFrame = int(abcfile[3]) + 12
            mc.playbackOptions(animationEndTime=posEndFrame)
            mc.currentTime(int(abcfile[2]))
            self.GDC_alembicApply()
            mc.select(cl=1)
                        
            self.csl_AttrAction(line='select',attrtype='alembic') 
            abcinfo=self.GDC_alembicInfo(0)[0]
            if server ==1:
                mc.AbcImport(abcfile[1],mode='import',connect=abcinfo)
            else:
                mc.AbcImport(abcfile[0],mode='import',connect=abcinfo) 
            try:
                mc.sysFile((mslocalPath+rendername),delete=True)
            except:
                pass 
            mc.file(rename=(mslocalPath+filename))
            mc.file(save=1,type = 'mayaBinary',f = 1)
        if line=='fs':
            frameStart = mc.playbackOptions(q=1, min=1) 
            frameEnd = mc.playbackOptions(q=1, max=1) 
            mc.playbackOptions(min=frameStart - 12, max=frameEnd + 12)
            shotName=''
            if  shotType==2: 
                shotName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]   
            if  shotType==3: 
                shotName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+ shotInfo[3] 
            alebicName=shotName+'.abc'                
            abcinfo=self.GDC_alembicInfo(0)[0]
            if server ==1:
                mc.AbcImport((serverPath+alebicName),mode='import',connect=abcinfo)
            else:
                mc.AbcImport((localPath+alebicName),mode='import',connect=abcinfo)             
            mc.playbackOptions(min=frameStart, max=frameEnd) 
            mc.currentTime(int(frameStart))                                  
        return 0 
   ############################################################################################################################
    #ABC属性【通用】【核心】【创建并导入毛发曲线abc（前期）】
    #@author 韩虹
    #2015/03/24
    ###########################################################################################################################  
    def GDC_curvealembicImp(self,server = 1,shotType = 1):
    
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        #本机
        FlocalPath=sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        #服务器路径
        FserverPath=sk_infoConfig.sk_infoConfig().checkProjectServerPath()    
        # 获取alembic临时路径
        localPath = sk_infoConfig.sk_infoConfig().alembicLocalPath(shotType)
        # 获取alembic服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().alembicServerPath(shotType )
        
        frameStart = mc.playbackOptions(q=1, min=1) 
        frameEnd = mc.playbackOptions(q=1, max=1) 
        mc.playbackOptions(min=frameStart - 12, max=frameEnd + 12)
        shotName=''
        if  shotType==2: 
            shotName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]   
        if  shotType==3: 
            shotName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+ shotInfo[3] 
        alebicName=shotName+'curve.abc'                
        abcinfo=self.GDC_shaveInfo(0,'abc_curve')[0]
        if server ==1:
            mc.AbcImport((serverPath+alebicName),mode='import',connect=abcinfo)
        else:
            mc.AbcImport((localPath+alebicName),mode='import',connect=abcinfo)             
        mc.playbackOptions(min=frameStart, max=frameEnd) 
        mc.currentTime(int(frameStart))                                  
        return 0     
   #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【属性添加工具】
    #  Author  : 韩虹
    #  Data    : 2014_11
    #------------------------------#  
    #添加（删减）物体属性（) 
    def csl_AttrAction(self,line='add',attrtype='GD'):       
        if line=='select':
            objs=mc.ls(type='transform',l=1)
            objList=[] 
            if objs :
                objList=[]
                for obj in objs:
                    if mc.objExists(obj+'.'+attrtype):
                        objList.append(obj)
                try: 
                    mc.select(objList)
                    print u'\n'
                    print u'==========================已选择有【%s】属性的物体==========================' % attrtype
                    print u'\n'
                except:
                    print u'\n'
                    print u'==========================文件中没有【%s】属性的物体==========================' % attrtype
                    print u'\n'
            else:
                mc.warning(u'没有选择物体，请选择物体' )                                         
        else:
            meshList=[]
            objs=mc.ls(sl=1,type='transform',l=1)
            if objs:                     
                for obj in objs:
                     meshcs=mc.listRelatives(obj,ad=1,f=1)
                     if meshcs:
                         for meshc in meshcs: 
                             if mc.nodeType(meshc)=='mesh':
                               meshList.append(meshc)                     
            if meshList:
                for mesh in meshList:
                    objs=mc.listRelatives(mesh,p=1,f=1)
                    if mc.objExists(objs[0]) and  line=='add':
                        try:
                            mc.setAttr((objs[0]+'.'+attrtype),1)             
                        except:
                            mc.addAttr(objs[0],ln=attrtype,at='double',dv=1,k=1)
                    print u'==========================已添加选择物体的【%s】属性==========================' % attrtype 
                    if mc.objExists(objs[0]) and  line=='remove':
                        obj=objs[0]
                        try:
                             mc.deleteAttr(objs[0],at=attrtype)            
                        except:
                             pass                          
            else:
                mc.warning( u'没有选择物体，或者所选择的物体是空组，请选择有效物体' )                             
                       
        return 0           

    #------------------------------#
    # 【辅助】【获取场景中所有cacheSet的物体】
    #------------------------------#   
    # 获取场景中所有cacheSet的物体
    # 为方便修改更新，所有cacheSet物体全部创建cache

#######Cache物体（from）    
    def checkCacheSetObjects(self,otcGrp = 1):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        objsCache = [] 
        for temp in tempSet:
            if 'MESHES' in temp:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                meshes = mc.sets(objSet, q=1)
                if meshes:
                    for mesh in meshes:
                        # 排除otc信息
                        if otcGrp == 1:
                            if '|OTC_GRP|' in mc.ls(mesh,l=1)[0] or '|SET_GRP|' in mc.ls(mesh,l=1)[0] or mc.ls(mesh,l=1)[0].split('|')[-1][3] in ['s', 'S']:
                                pass
                            else:
                                # 不要长名，为shareNodes做准备
                                objsCache.append(mc.ls((mesh), l=0)[0])
                        else:
                            objsCache.append(mc.ls((mesh), l=0)[0])
        if objsCache:
            print (u'[Cache Object]    ' + str(len(objsCache)))
        else:
            print (u'[Cache Object]    0')
        return objsCache
   #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【群组打组整理】
    #  Author  : 韩虹
    #  Data    : 2015_03
    #------------------------------#  
    def gdc_clusterGroupR(self):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRoot = []
        refNodes = []
        for refLeval in refInfos[0]:
            refNodes = refNodes + refLeval
        for refNode in refNodes:
            # 全名处理
            refObjs = mc.referenceQuery(refNode , nodes=1,dagPath = 1)
            # Q,need to test
            if refObjs:
                refRoot.append(refObjs[0])
        # 群组
        if mc.ls('Cluster_GRP'):
            clusterFlowGrp = 'Cluster_GRP'
        else:
            clusterFlowGrp = mc.group(em=1, name='Cluster_GRP')
        # OTC_GRP
        if mc.ls('OTC_GRP'):
            otcGrp = 'OTC_GRP'
        else:
            otcGrp = mc.group(em=1, name='OTC_GRP')
        # 打组
        if otcGrp not in mc.ls(clusterFlowGrp, l=1)[0]:
            mc.parent(clusterFlowGrp, otcGrp)
        # needRoot
        needRoot = ['persp', 'top', 'front', 'side', 'CAM_GRP', 'CHR_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP']
        keepRoot = ['CHR_GRP', 'CAM_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP', 'persp', 'top', 'front', 'side']
        # 开始处理
        # 优先记录：带有namespace的基本GRP
        ogGrp = ['CHR_GRP', 'CAM_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP']
        ogNsGrp = []
        for grp in ogGrp:
            checkGrps = mc.ls(('*:*' + grp + '*'),l=1) + mc.ls(('*:*:*' + grp + '*'),l=1)
            if checkGrps:
                for obj in checkGrps:
                    lastName = obj.split(':')[-1]
                    ogNsGrp.append(obj[0:-1*(len(lastName)+1)])
        ogNsGrp = list(set(ogNsGrp))
        print refRoot
        # 1为参考方式处理
        # 这个方式对VFX会有影响,所以要修正
        for root in refRoot:
            if '_' in root and ':' in root:
                shortName=root.split('_')[1].split(':')[0]
                clusteGrp=shortName+'_cluster'
                if mc.ls(clusteGrp):
                    try:
                        mc.parent(clusteGrp, clusterFlowGrp)
                    except: 
                        pass                                     
                else:
                    clusterG  = mc.group(em=1, name=clusteGrp)
                    mc.parent(clusterG, clusterFlowGrp)            
                # 首先判断是否在VFX_GRP和Cluster_GRP
                if '_cluster' not in mc.ls(root,l=1)[0]:
                    mc.parent(root, clusterG)        
        return 0 
    
   #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【选择的物体abc移帧及改变速度】
    #  Author  : 韩虹
    #  Data    : 2015_03
    #------------------------------#  
    def gdc_clusteroffset(self,ot=1,sd=1):
        offset=int(mc.intSliderGrp('offset',q=1,v=1))          
        speed=float(mc.floatSliderGrp('speed',q=1,v=1))
        objs=mc.ls(sl=1,type='transform',l=1) 
        abcnodes=[]
        if objs:
            for obj in objs:
                shapes=mc.listRelatives(obj,s=1,type='mesh',f=1)  
                if shapes:
                    abcnode=mc.listConnections((shapes[0]+'.inMesh'),s=1,p=0)
                    if mc.ls(abcnode) and abcnode[0] not in abcnodes:
                        abcnodes.append(abcnode[0])
        if abcnodes==[]:
            mc.error(u'no abc,please select polygon with connected abc')
        if abcnodes and  ot==1:
            for abc in abcnodes:
                mc.setAttr((abc+'.offset'),offset) 
        if abcnodes and  sd==1:
            for abc in abcnodes:
                mc.setAttr((abc+'.speed'),speed) 
        return 0

   #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【辅助】【FL文件 ReferenceEdit还原】
    #------------------------------#

    # 处理FINALLAYOUT文件
    def sk_sceneFLRefShaderReset(self , info ):

        # 处理OTC的SET文件，但不载入参考
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
        fileGrpType = '_base_fs_c001'

        needFilePath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath() 
        needFsFile = needFilePath + info[0] + '_' + info[1] + '_' + info[2] + fileGrpType + fileFomat
        
        print needFsFile
        
        # 不加载参考导入
        mc.file(needFsFile , open = 1, loadReferenceDepth = 'none' , force = 1)
        # 处理好所有参考
        sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
        mc.file(save = 1, force = 1)

    #------------------------------#
    # 【辅助】【FL文件Cache上传】
    #------------------------------#

    # finalLayout上传服务器
    def checkFinalLayoutUpdate(self):
        # 获取cacheSet物体
        cacheObjs = self.checkCacheSetObjects()
        if cacheObjs:
            # 上传服务器
            self.checkCacheLocalUpdate(3)
            #print(unicode('=====================【Cache】【服务器端】【输出】完毕=====================', "utf8"))
            print(u'=====================【Cache】【服务器端】【输出】完毕=====================')
        # 最后保存
        mc.file(save=1)

    #----------------------------------------------------------------------------------------------#
    


    def csl_checkCacheReturnMaterial(self, MatLists = [] ,finalLayout = 0,shotType=3 ):
        if finalLayout:
            MatLists = self.csl_checkCacheRecordMaterialImport(shotType)
        keysSG = MatLists.keys()
        for key in keysSG:
            objs = MatLists[key]
            # 必须加objs，不然会断掉
            if objs:
                mc.sets(objs, forceElement = key)
                
    def csl_checkCacheRecordMaterialImport(self,shotType=3):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if shotType == 2:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        fileInfo = 'ShotShaderInfo.txt'
        allInfo = self.checkFileRead(serverDataPath + fileInfo)
        # 分割点
        signKeyIndex = self.checkListSameAllIndex(allInfo,u'********')[0]
        signMeshSplitIndexList = self.checkListSameAllIndex(allInfo,u'--------')
        # 开始还原
        MatLists = dict({})
        # 创建keys
        for i in range(signKeyIndex):
            MatLists[allInfo[i]] = []
        # 每类创建
        for i in range(len(signMeshSplitIndexList)):
            if i == 0:
                meshNum = signMeshSplitIndexList[i] - signKeyIndex - 1
            else:
                meshNum = signMeshSplitIndexList[i] - signMeshSplitIndexList[i-1] - 1
            for j in range(meshNum):
                baseMeshIndex = signMeshSplitIndexList[i] - meshNum
                MatLists[allInfo[i]].append(allInfo[baseMeshIndex + j])
        return MatLists 
#
    def csl_FinalcheckFileWrite(self, path , info , addtion=0):
        print u'>>>>>>[write]'
        print path
        if addtion == 1:
            info = self.csl_FinalcheckFileRead(path) + info
        txt = open(path, 'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()
#
    def csl_FinalcheckFileRead(self, path):
        print u'>>>>>>[read]'
        print path
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result            
#读取smooth信息
    def csl_FinalSmoothMeshRead(self,meshinfo=[],smoothInfo='smooth_2'):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        nsList = refInfos[2][0]
        if 'UI' in nsList:
            nsList.remove('UI')
        if 'shared' in nsList:
            nsList.remove('shared')
        if 'CAM' in nsList:
            nsList.remove('CAM')  
        for ns in nsList:
            #ns='csl_c001001ShunLiuFin'
            if '_' in ns and ":" not in ns:
                assetInfo = ns.split('_')
                Infopath=serverPath+'data/AssetInfos/smoothSetInfo/'+assetInfo[0]+'/'+assetInfo[1]+ '/h/'+smoothInfo+'.txt'
                if Infopath:
                    meshsmooth=self.checkFileRead(Infopath)
                    #mesh='MSH_c_hi_logo_ca_'
                    #mc.select(mesh)
                    #mc.ls(mesh)
                    
                    if meshsmooth:
                        for mesh in meshsmooth:
                            meshShapes=mc.ls(type='mesh',l=1)
                            for i in range(len(meshShapes)):
                                if "|" not in mesh and mesh in meshShapes[i]:
                                    meshinfo.append(meshShapes[i])
                                if "|" in mesh:
                                    mes=mesh.split('|')
                                    if len(mes)==1 and mes[0] in  meshShapes[i]:
                                        meshinfo.append(meshShapes[i])
                                    if len(mes)==2 and mes[0] in  meshShapes[i] and mes[1] in  meshShapes[i]:
                                        meshinfo.append(meshShapes[i])                                    
                                    if len(mes)==3 and mes[0] in  meshShapes[i] and mes[1] in  meshShapes[i] and mes[2] in  meshShapes[i]:
                                        meshinfo.append(meshShapes[i]) 
                                    if len(mes)==4 and mes[0] in  meshShapes[i] and mes[1] in  meshShapes[i] and mes[2] in  meshShapes[i] and mes[3] in  meshShapes[i]:
                                        meshinfo.append(meshShapes[i])
                        break
        return meshinfo
#设置相应smooth 
    def csl_FinalSmoothSet(self,meshinfo=[],smoothInfo='smooth_2'):
        meshinfo=self.csl_FinalSmoothMeshRead(meshinfo=[],smoothInfo=smoothInfo)
        if meshinfo:
            for meshShape in  meshinfo:
                if meshShape!=None and smoothInfo=='smooth_2':
                    mc.setAttr((meshShape+'.aiSubdivType'),1)
                    mc.setAttr((meshShape+'.aiSubdivIterations'),2)
                if meshShape!=None and smoothInfo=='smooth_1':
                    mc.setAttr((meshShape+'.aiSubdivType'),1)
                    mc.setAttr((meshShape+'.aiSubdivIterations'),1)
                if meshShape!=None and smoothInfo=='smooth_0':
                    mc.setAttr((meshShape+'.aiSubdivType'),0)
                    mc.setAttr((meshShape+'.aiSubdivIterations'),0)
                                     
        print(u'=====================【smooth设置完成】【%s】=====================' % (smoothInfo))          
#记录参考场景
    def csl_EnverInfoRecord (self,EnvInfo=[],shotType=3):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refName = refInfos[2][0]
        EnvInfoPath=''
        if shotType==3:
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        if shotType==2:
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'
        mc.sysFile(temimagepath, makeDir=True)            
        if refName:
            for i in range(len(refName)):
                if refName[i].split('_')[1][0] in ['s', 'S']:
                    EnvInfo.append(refName[i])   
        
        self.csl_FinalcheckFileWrite((EnvInfoPath +  'EnvInfo.txt'), EnvInfo)
        return  EnvInfo

#读取场景并导出场景
    def csl_EnverInfoWrite (self,EnvInfo=[],shotType=3):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refName = refInfos[2][0]
        EnvInfoPath=''
        EnvRnInfo=[]
        EnvFileInfo=[]
        EnvNameSpace=[]
        if shotType==3:
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        if shotType==2:
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'
        if refName:
            for i in range(len(refName)):
                if refName[i].split('_')[1][0] in ['s', 'S']:
                    EnvNameSpace.append(refName[i])   
                    EnvRnInfo.append(refInfos[0][0][i])
                    EnvFileInfo.append(refInfos[1][0][i])            
        EnvInfo=EnvRnInfo + [u'----------------']+ EnvFileInfo+ [u'----------------']+  EnvNameSpace     
        self.csl_FinalcheckFileWrite((EnvInfoPath +  'EnvInfo.txt'), EnvInfo) 
        return EnvInfo
    
    def csl_EnverInfoRead (self,EnvFileName='',shotType=3):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        
        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType=3)
        
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refName = refInfos[2][0]    
        EnvName=''
        EnvInfoPath=''
        if shotType==3:
            EnvName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'_env_fs.ma'
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        if shotType==2:
            EnvName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_env_fs.ma'
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'  
        
        EnvFileName=renderFilePathServer+EnvName
           
        EnvInfo=self.csl_FinalcheckFileRead(EnvInfoPath+'EnvInfo.txt')
        EnvExr=[]
        if EnvInfo:
            signKeyIndex = self.checkListSameAllIndex(EnvInfo,u'----------------')[0]
            mc.select(cl=1)
            EnvExr=[]
            for i in range(signKeyIndex):
            #print (ImageInfo[i]+'.....'+ ImageInfo[i+signKeyIndex+1]+'==================')
                EnvRN=EnvInfo[i]
                EnvFile=EnvInfo[i+signKeyIndex+1]
                EnvNamespace=EnvInfo[i+2*signKeyIndex+2]
                EnvFileRender=EnvFile.replace('_ms_anim', '_ms_render')
                mc.file(EnvFileRender,loadReference=EnvRN)
    
                EnvExr.append(EnvNamespace+':SET')
    
        if EnvExr:   
            mc.select(EnvExr)
            mc.file(EnvFileName, force=1, options="v=0" , type='mayaAscii', preserveReferences=1, exportSelected=1)
            return  EnvFileName

#适用于maya2014,修改自sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheRecordMaterial
    def csl_checkCacheRecordMaterial(self, checkObjs = [] , finalLayout = 0 ,cacheMode = 1 ,shotType = 3):
        SG = mc.ls(type='shadingEngine')
        # 选取模式
        if checkObjs:
            needSG = []
            errorObjs = []
            for obj in checkObjs:
                if not mc.ls(obj):
                    errorObjs.append(obj)
            if errorObjs:
                print u'------------------------以下物体不存在------------------------'
                for info in errorObjs:
                    print info
                print u'------------------------以上物体不存在------------------------'
                print(u'------------------------请检测物体清单------------------------')
                mc.error(u'------------------------请检测物体清单------------------------')
            else:
                for obj in checkObjs:
                    meshs = mc.listRelatives(obj,ni=1,type = 'mesh',s =1 )
                    for mesh in meshs:
                        if mc.listConnections(mesh,destination = 1,type = 'shadingEngine'):
                            nodeSG = mc.listConnections(mesh,destination = 1,type = 'shadingEngine')
                            for node in nodeSG:
                                needSG.append(node)
                SG = list(set(needSG))
        # 备份信息
        MatLists = dict({})
        for node in SG:
            connectObjsSG = mc.sets(node, q=1)
            if connectObjsSG:
                MatLists[node] = connectObjsSG
        # finalLayout上传信息
        if finalLayout:
            self.csl_checkCacheRecordMaterialExport(MatLists,shotType)
        return MatLists

    def csl_checkCacheRecordMaterialExport(self,MatLists,shotType = 2):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        if shotType == 2:
            localShaderInfoPath = localPath + 'finalLayoutTemp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            localShaderInfoPath = localPath + 'finalLayoutTemp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        SGKeys = MatLists.keys()
        allInfo = []
        for i in range(len(SGKeys)):
            if i == 0:
                allInfo = SGKeys + [u'********'] + MatLists[SGKeys[i]] + [u'--------']
            else:
                allInfo = allInfo  + MatLists[SGKeys[i]] + [u'--------']
        # 写
        fileInfo = 'ShotShaderInfo.txt'
        mc.sysFile(localShaderInfoPath, makeDir=True)
        self.checkFileWrite((localShaderInfoPath + fileInfo),allInfo)
        # 上传
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if shotType == 2:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localShaderInfoPath + fileInfo) + '"' + ' ' + '"' + (serverDataPath + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating ShotShaderInfo To Server]===传输[%s]完毕==='%fileInfo         

    def csl_cachemeshAdd(self) :
        import re
        meshAdd=[]    
        meshs=mc.ls(type='transform',l=1)
        if meshs:
            for mesh in meshs:
                if 'CHR' in mesh.split('|') and 'MODEL' in mesh.split('|') and re.search('eye_highlight',mesh)!=None:
                    meshAdd.append(mesh)
        if meshAdd:
            return meshAdd 
        else:
            return 0 

    def csl_setattr(self,attrtype='aiStandIn',attr='visibility',num=1):
        objs=mc.ls(type=attrtype ,l=1)
        if objs:
            for obj in objs:
                Arnold=mc.listRelatives(obj,p = 1,f=1)
                if Arnold and mc.nodeType(Arnold[0])=='transform':
                    mc.setAttr((Arnold[0]+'.'+attr),int(num))        

    #-------------------------------------#
    # 检测是否存在render文件
    def sk_FLCheckRenderFile(self,refInfos):
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refPaths:
            errorAsset = []
            for i in range(len(refPaths)):
                refPath = refPaths[i]
                renderFilePath = refPath.replace('_anim.','_render.')
                if os.path.exists(renderFilePath):
                    pass
                else:
                    errorAsset.append(refNodes[i])
            if errorAsset:
                print u'-------------------以下render文件不存在-------------------'
                for info in errorAsset:
                    print info[:-2]
                print u'-------------------以上render文件不存在-------------------'
                print u'==================请先检查shot文件确定参考是否正确=================='
                print u'==================正确后请再和前期协商更新asset文件=================='
                mc.error(u'==================请和前期协商更新asset文件==================')
        else:
            print(u'==================shot文件没有参考下请先检查shot文件确定参考是否正确，请和动画联系==================')
            mc.error(u'==================shot文件没有参考下请先检查shot文件确定参考是否正确，请和动画联系==================')
    
    #-------------------------------------#   

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】【所有约束BK，确保动画及camera正确】
    #  Author  : 沈康
    #  Data    : 2013_06_03
    #------------------------------#  
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def sk_checkBakeConstraints(self):
        constraintsAll = mc.ls(type='constraint')
        nodeTypeConfig = ['transform','joint']
        #约束烘焙
        if  constraintsAll:
            tobake= []
            # 处理非参考的物体
            constraints = [x for x in constraintsAll if not mc.referenceQuery(x,inr=1)]
            for constraint in constraints:
                objs = mc.listHistory(constraint)
                for checkType in nodeTypeConfig:
                    temp = mc.listConnections(constraint,s = 1 ,d=0,type = checkType)
                    if temp:
                        objs = objs + temp
                plugs = []
                for obj in objs:
                    checkState = 0
                    if (mc.nodeType(obj) in nodeTypeConfig) and mc.nodeType(obj) != "constraint":
                        # 不接受cam
                        shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                        if shape:
                            #print shape 
                            #print obj
                            if mc.nodeType(shape[0]) != 'camera':
                                checkState = 1
                        else:
                            checkState = 1
                    if not checkState:
                        continue
                    # 进行属性检测
                    attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                    consState = 0
                    for attr in attrs:
                        cons = mc.listConnections((obj + attr),s=1,d=0)
                        if cons:
                            consState = 1
                            break
                    if consState:
                        plugs.append(mc.ls(obj,l=1)[0])
                plugs = list(set(plugs))
                tobake+= plugs
            io = (mc.playbackOptions(q=1, minTime=1)-10, mc.playbackOptions(q=1, maxTime=1)+10)

            # 处理参考的_ct_an物体
            constraintRefs = [x for x in constraintsAll if mc.referenceQuery(x,inr=1)]
            for constraint in constraintRefs:
                objs = mc.listHistory(constraint)
                for checkType in nodeTypeConfig:
                    temp = mc.listConnections(constraint,s = 1 ,d=0,type = checkType)
                    if temp:
                        objs = objs + temp
                plugs = []
                for obj in objs:
                    checkState = 0
                    if (mc.nodeType(obj) in nodeTypeConfig) and mc.nodeType(obj) != "constraint":
                        # 不接受cam
                        shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                        if shape:
                            if mc.nodeType(shape[0]) != 'camera':
                                if '_ct_an' in obj or mc.ls(obj + '.ct_an'):
                                    checkState = 1
                        else:
                            if '_ct_an' in obj or mc.ls(obj + '.ct_an'):
                                checkState = 1
                    if not checkState:
                        continue
                    # 进行属性检测
                    attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                    consState = 0
                    for attr in attrs:
                        cons = mc.listConnections((obj + attr),s=1,d=0)
                        if cons:
                            consState = 1
                            break
                    if consState:
                        plugs.append(mc.ls(obj,l=1)[0])
                plugs = list(set(plugs))
                tobake+= plugs
            io = (mc.playbackOptions(q=1, minTime=1)-1, mc.playbackOptions(q=1, maxTime=1)+1)

            tobake = list(set(tobake))
            
            # 改进版，不bake，而是给新locator bake
            if tobake:
                # 删除locators
                locators = mc.ls('IDMT_BakeAnim*',type = 'transform')
                if locators:
                    mc.delete(locators)
                '''
                # 老赵bake脚本
                mc.select(tobake)
                mel.eval('source \"zzjUtilityTools\"')
                mel.eval('zzjUtilityTools \"bakeAnim\"')
                '''
                # 数值传递到locators
                locators = []
                constraintTemp = []
                for i in range(len(tobake)):
                    locTemp = mc.spaceLocator()
                    locTemp = mc.rename(locTemp[0] , ('IDMT_BakeAnim_' + str(i)))
                    cons = mc.parentConstraint(tobake[i] , locTemp)
                    constraintTemp.append(cons[0])
                    locators.append(locTemp)
                # 一次烘焙
                mc.bakeResults(locators,  t=io,
                        simulation=1,
                        sampleBy=1,
                        disableImplicitControl=1,
                        preserveOutsideKeys=1,
                        sparseAnimCurveBake=0,
                        removeBakedAttributeFromLayer=0,
                        bakeOnOverrideLayer=0,
                        controlPoints=0,
                        shape=0)
                mc.delete(constraintTemp)

                # 重新约束物体
                attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                #locators = mc.ls('IDMT_BakeAnim*',type = 'transform')
                if locators:
                    for i in range(len(locators)):
                        # 打断t和r属性
                        for attr in attrs:
                            #mel.eval('CBdeleteConnection \"' + tobake[i] + attr + '\"')
                            #self.checkDeleteConnection(tobake[i] + attr)
#修改原因（有的锁定）
                            try:
                               self.checkDeleteConnection(tobake[i] + attr)
                            except:
                                pass    
#
                        locatorGrp = locators[i]
                        #  父子约束 ,cam已经锁住
                        if 'cam_' not in tobake[i]:
                            print u'----------------'
                            print locatorGrp
                            print tobake[i].split('|')[-1]
                            # 位移检测
                            skipTranslateAxis = []
                            checkTAttr = ['.tx','.ty','.tz']
                            for j in range(3):
                                passAttr = ['x','y','z']
                                tState = mc.getAttr((tobake[i] + checkTAttr[j]),settable = 1)

                                if tState:
                                    pass
                                else:
                                    skipTranslateAxis.append(passAttr[j])
                            # 旋转检测
                            skipRotateAxis = []
                            checkRAttr = ['.rx','.ry','.rz']
                            for k in range(3):
                                passAttr = ['x','y','z']
                                rState = mc.getAttr((tobake[i] + checkRAttr[k]),settable = 1)
                                if rState:
                                    pass
                                else:
                                    skipRotateAxis.append(passAttr[k])
                            # 父子约束
                            if skipTranslateAxis and skipRotateAxis == []:
                                mc.parentConstraint(locatorGrp , tobake[i] , skipTranslate = skipTranslateAxis)
                            if skipTranslateAxis == [] and skipRotateAxis:
                                mc.parentConstraint(locatorGrp , tobake[i] , skipRotate = skipRotateAxis)
                            if skipTranslateAxis and skipRotateAxis:
                                print '------'
                                print locatorGrp
                                print tobake[i]
                                # 修正全忽略的问题，全部忽略再去创建约束会报错
                                if (skipTranslateAxis == ['x','y','z']) and (skipRotateAxis == ['x','y','z']):
                                    pass
                                else:
                                    
                                    #mc.parentConstraint(locatorGrp , tobake[i] , skipTranslate = skipTranslateAxis, skipRotate = skipRotateAxis)
                                    #忽略锁定
                                    try:
                                        mc.parentConstraint(locatorGrp , tobake[i] , skipTranslate = skipTranslateAxis, skipRotate = skipRotateAxis)
                                    except:
                                        pass                                          
                            if skipTranslateAxis == [] and skipRotateAxis == []:
                                mc.parentConstraint(locatorGrp , tobake[i])

                    # 二次烘焙
                    mc.bakeResults(tobake,    t=io,
                            simulation=1,
                            sampleBy=1,
                            disableImplicitControl=1,
                            preserveOutsideKeys=1,
                            sparseAnimCurveBake=1,
                            removeBakedAttributeFromLayer=0,
                            bakeOnOverrideLayer=0,
                            controlPoints=0,
                            shape=1)

                    # 删除约束
                    constraintConfigs = [x for x in (constraints + constraintRefs) if not mc.referenceQuery(x,inr=1)]
                    for cons in constraintConfigs:
                        ref = mc.referenceQuery(cons,isNodeReferenced = 1)
                        if not ref:
                            mc.delete(cons)

                    # 删除locators
                    mc.delete(locators)

                    print(u'\n========================【约束】【烘焙】【成功】========================')
                    print u'\n'
        else:
            print(u'\n========================【约束】【烘焙】【失败】========================')
            print u'\n' 

    #------------------------------#
    # 【辅助】完全断开指定属性
    #------------------------------#     
    # 完全断开指定属性
    def checkDeleteConnection(self , attr ):
        # 被输入方
        if mc.connectionInfo(attr , isDestination = 1):
            destination = mc.connectionInfo(attr , getExactDestination = 1)
            srcConn = mc.listConnections(destination, s = 1, d = 0 , type = 'character')
            if srcConn:
                # 断开
                mc.character(destination , e = 1 ,rm = srcConn[0])
#                try:
#                    mc.character(destination , e = 1 ,rm = srcConn[0])
#                except:
#                    pass
            
            sArr = mc.ls(destination , ro = 1)
            if sArr:
                src = mc.connectionInfo(destination , sourceFromDestination = 1)
                if src:
                    mc.disconnectAttr(src , destination)
            else:
                mc.delete(destination , icn = 1)    

  #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】 OTC及SET结构处理
    #  Author  : 沈康
    #  Data    : 2013_07_28
    #------------------------------#
    # OTC结构处理：删除 [更改：otc由mb强制变更ma;删除先删除ma文件，后找mb，若有则删除]
    def sk_sceneGRPDelete(self, fileGRP='OTC' , shotType = 2):
      
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        #fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileFomat = '.ma'
#        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)        
        
        
        baseShotInfo = ''
        if shotType == 2:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
        import os
        if os.path.exists(otcFileServer):
            mc.sysFile( otcFileServer, delete=True)     
#            cmd = 'zwSysFile(\"del\",\"' + otcFileServer + '\",\"\",1)'
#            mel.eval(cmd)
        else:
            fileFomat = '.mb'
            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            if os.path.exists(otcFileServer):
                mc.sysFile( otcFileServer, delete=True)                 
#                cmd = 'zwSysFile(\"del\",\"' + otcFileServer + '\",\"\",1)'
#                mel.eval(cmd)

    #------------------------------#     

    #-------------------------------------#
    # 记录hide输出
    def sk_FL_RefHideObjsRecord(self,server,shotType):
        unDisplayLayerObjs = []
        # 记录：shot文件非参考的隐藏的显示层的物体
        if server:
            displayLayers = mc.ls(type = 'displayLayer')
            if displayLayers:
                for layer in displayLayers:
                    isRef = mc.referenceQuery(layer, isNodeReferenced = 1)
                    if isRef == 0 and layer != 'defaultLayer':
                        viewState  = mc.getAttr(layer + '.visibility')
                        if viewState == False:
                            objs = mc.editDisplayLayerMembers( layer, query=True,fn=1)
                            if objs:
                                unDisplayLayerObjs = unDisplayLayerObjs + objs
            hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
            mc.sysFile(hideObjsServerPath,makeDir = 1)
            self.checkFileWrite((hideObjsServerPath +  'shotHideObjs.txt'), unDisplayLayerObjs)
            print u'\n'
            print(u'=====================【hideObjs】【服务器端】【输出】完毕=====================')
            print u'\n'
        return unDisplayLayerObjs
    
    #-------------------------------------# 

    #-------------------------------------#
    # 不用于cache的参考记录
    def skFLNoNeedRefNodeInfo(self):
        noNeedRefNodeInfo = []
        if mc.ls('OTC_GRP') and mc.ls('SET_GRP'):
            allGrps = []
            if mc.listRelatives('OTC_GRP',ad = 1,f=1):
                allGrps = allGrps +  mc.listRelatives('OTC_GRP',ad = 1,f=1)
            if mc.listRelatives('SET_GRP',ad = 1,f=1):
                allGrps = allGrps + mc.listRelatives('SET_GRP',ad = 1,f=1)
            if allGrps:
                for grp in allGrps:
                    if mc.referenceQuery(grp,isNodeReferenced = 1):
                        refNode = mc.referenceQuery(grp,referenceNode = 1)
                        noNeedRefNodeInfo.append(refNode)
                if noNeedRefNodeInfo:
                    noNeedRefNodeInfo = list(set(noNeedRefNodeInfo))
        return noNeedRefNodeInfo
    
    #-------------------------------------#   

    #-------------------------------------#
    # 输出角色道具信息
    def skFLAssetNeedInfo(self,refInfos,noNeedRefNodeInfo,shotType):
        assetNeedOutputInfo = []    
        rfnLv1 = refInfos[0][0]
        rfnPathLv1 = refInfos[1][0]
        for i in range(len(rfnLv1)):
            ns = refInfos[2][0][i]
            refNode = refInfos[0][0][i]
            if noNeedRefNodeInfo:
                if refNode not in noNeedRefNodeInfo:
                    newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                    assetNeedOutputInfo.append(newPath)
                    assetNeedOutputInfo.append(ns)
            else:
                if '_' not in refNode:
                    continue                
                if refNode.split('_')[1][0] not in ['s', 'S']:
                    newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                    assetNeedOutputInfo.append(newPath)
                    assetNeedOutputInfo.append(ns)
        assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        self.checkFileWrite((assetNeedServerPath +  'assetReference.txt'), assetNeedOutputInfo)
        print u'\n'
        print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')
        print u'\n'
        return assetNeedOutputInfo
    
    #-------------------------------------# 

   #------------------------------#
    # OTC结构处理：导出
    def sk_sceneGRPExport(self, fileGRP='OTC' , server=1 , shotType = 2 ):
        renderFilePath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        fileFomat = '.ma'
        fileTypeFull = 'mayaAscii'
        
        baseShotInfo = ''
        if shotType == 2:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFile = renderFilePath + baseShotInfo + fileGrpType + fileFomat
        
        root = mc.ls(assemblies=True)
        if root:
            if (fileGRP + '_GRP') in root:
                # OTC和SET处理，导出
                mc.select(fileGRP + '_GRP')
                mc.file(otcFile, force=1, options="v=0" , type=fileTypeFull, preserveReferences=1, exportSelected=1)
        mc.select(cl=1)
        
        # 对set进行转参考处理
        if fileGRP == 'SET':
            # ma模式处理
            animRefInfos = sk_infoConfig.sk_infoConfig().checkFileRead(otcFile)
            renderRefInfos = []
            for line in animRefInfos:
                if '_ms_anim.m' in line:
                    line = line.replace('_ms_anim.m','_ms_render.m')
                renderRefInfos.append(line)
            sk_infoConfig.sk_infoConfig().checkFileWrite(otcFile,renderRefInfos)
        print  otcFile          
        # 传至服务器
        if server:
            renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            mc.sysFile(otcFile,copy=otcFileServer)
#            cmd = 'zwSysFile(\"copy\",\"' + otcFile + '\",\"' + otcFileServer + '\",1)'
#            mel.eval(cmd)
            
    #------------------------------#     
    #------------------------------#
    # 【辅助】【获取场景中所有AnimSet的物体】
    #------------------------------#   
    # 获取场景中所有AnimSet的物体
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def checkAnimSetObjects(self,otcGrp = 1):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        objsAnim = []
        for temp in tempSet:
            if 'CTRLS' in temp:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                ctrls = mc.sets(objSet, q=1)
                if ctrls:
                    for ctrl in ctrls:
                        # 排除otc组信息
                        if otcGrp == 1:
                            if 'OTC_GRP' not in mc.ls(ctrl,l=1)[0] and 'SET_GRP' not in mc.ls(ctrl,l=1)[0]:
                                print ctrl
                                objsAnim.append(ctrl)
        if objsAnim:
            print (u'[Anim  Object]    ' + str(len(objsAnim)))
        else:
            print (u'[Anim  Object]    0')
        return objsAnim  

   #------------------------------#
    # 【核心】【动画数据导入导出PYTHON版】
    # 0.动画
    # Author : 沈  康
    # 参考             : 万寿龙
    # Data   : 2013_05_24 - 2013_05_28
    #------------------------------#   
    # 导出信息
    # 增加上传服务器功能
    def checkAnimCurveInfoExport(self, objs, serverFile=1, infoFile='anim' , targetPath = '' , shotType = 2):
        # 前提基本信息
        AnimsInfo = []
        AnimsInfo.append('ImportExportAnimationForSets v 1.0   (Author: wanshoulong)')
        # 版本号
        AnimsInfo.append('mayaVersion  ' + mc.about(v=1) + ';')
        # 单位类型
        AnimsInfo.append('linearUnit  ' + mc.currentUnit(q=1, f=1, l=1) + ';')
        # 角度单位，弧度还是角度
        AnimsInfo.append('angularUnit  ' + mc.currentUnit(q=1, f=1, a=1) + ';')
        # 制式，PAL等
        AnimsInfo.append('timeUnit  ' + mc.currentUnit(q=1, f=1, t=1) + ';')
        # 获取objs
        if objs:
            for obj in objs:
                # 通道盒子里能被K帧的属性
                keys = mc.listAttr(obj, k=1)
                # 通道盒子中无法被K帧的属性
                noKeys = mc.listAttr(obj, cb=1)
                if noKeys:
                    allAttr = keys + noKeys
                else:
                    allAttr = keys
                if allAttr:
                    for attr in allAttr:
                        animCurve = []
                        if mc.objExists(obj + '.' + attr):
                            # 获取属性的动画曲线
                            animCurve = mc.listConnections((obj + '.' + attr), s=1, d=0)
                        # 剔除无法K帧的情况
                        if animCurve:
                            # 判断是否存在及是否animCurve
                            if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                AnimsInfo.append('anim ' + obj + '.' + attr + '\n{')
                                # 更新信息
                                infoAll = self.checkAnimCurveInfoGet(animCurve[0])  
                                for info in infoAll:
                                    AnimsInfo.append(info)
                                AnimsInfo.append('}')
                        else:
                            # 无动画的信息
                            if mc.objExists(obj + '.' + attr):
                                if 'double3' not in mc.getAttr((obj + '.' + attr), type=1) :
                                    value = mc.getAttr(obj + '.' + attr)
                                    AnimsInfo.append('non-anim ' + obj + '.' + attr + ' ' + str(value) + ';')
                # 对曲线K点的处理
                expShapes = mc.listHistory(obj)
                # 显示控制点的判断
                if expShapes and mc.objectType(expShapes[0], isType='nurbsCurve') and mc.getAttr(expShapes[0] + '.dispCV'):
                    pointNum = mc.getAttr(expShapes[0] + '.spans')
                    # 此处和原脚本不一样
                    for j in range(pointNum * 2):
                        if mc.objExists(expShapes[0] + '.cv[' + str(j) + ']'):
                            allAttr = mc.listAttr((expShapes[0] + '.cv[' + str(j) + ']'), k=1)
                            if allAttr:
                                for attr in allAttr:
                                    animCurve = mc.listConnections((expShapes[0] + '.' + attr), type='animCurve', s=1, d=0)
                                    if animCurve:
                                        if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                            AnimsInfo.append('anim ' + expShapes[0] + '.' + attr + '\n{') 
                                            # 更新信息
                                            infoAll = (self.checkAnimCurveInfoGet(animCurve[0]))
                                            for info in infoAll:
                                                AnimsInfo.append(info)
                                            AnimsInfo.append('}')
                                    else:
                                        # 无动画的信息，不过对于点来说基本用不到
                                        if 'double3' not in mc.getAttr((expShapes[0] + '.' + attr), type=1) :             
                                            value = mc.getAttr(expShapes[0] + '.' + attr)
                                            AnimsInfo.append('non-anim ' + expShapes[0] + '.' + attr + ' ' + str(value) + ';')
        # fsMode，指定输出地址
        if targetPath == '':
            # 本地输出
            # shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType)
            mc.sysFile(localPathAnim, makeDir=True)
            self.checkFileWrite((localPathAnim + infoFile + '.sla'), AnimsInfo)
            # 本地输出object信息
            personalObjsFile = localPathAnim + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)
            '''
            if infoFile in ['moveInfo']:
                objsLong = mc.ls(objs,l=1)
                personalObjsFile = localPathAnim + infoFile + '_Lobjs.txt'
                self.checkFileWrite(personalObjsFile, objsLong)
            '''
            if serverFile == 1:
                # 上传服务器
                self.checkAnimInfoUpdate(infoFile,shotType)
        else:
            # 自定义输出地址
            self.checkFileWrite( (targetPath + infoFile + '.sla') , AnimsInfo)
            # 本地输出object信息
            personalObjsFile = targetPath + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)
        
    #------------------------------# 

    #------------------------------#
    # 【辅助】【获取场景中所有cacheSet的物体】
    #------------------------------#   
    # 获取场景中所有cacheSet的物体
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def checkCacheSetObjects(self,otcGrp = 1):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        objsCache = [] 
        for temp in tempSet:
            if 'MESHES' in temp:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                meshes = mc.sets(objSet, q=1)
                if meshes:
                    for mesh in meshes:
                        # 排除otc信息
                        if otcGrp == 1:
                            if '|OTC_GRP|' in mc.ls(mesh,l=1)[0] or '|SET_GRP|' in mc.ls(mesh,l=1)[0] or mc.ls(mesh,l=1)[0].split('|')[-1][3] in ['s', 'S']:
                                pass
                            else:
                                # 不要长名，为shareNodes做准备
                                objsCache.append(mc.ls((mesh), l=0)[0])
                        else:
                            objsCache.append(mc.ls((mesh), l=0)[0])
        if objsCache:
            print (u'[Cache Object]    ' + str(len(objsCache)))
        else:
            print (u'[Cache Object]    0')
        return objsCache 

    #------------------------------#
    # 处理数据，并输出
    def checkCacheVStateExport(self , cacheObjs , shotType = 2 ,server = 1):
        if cacheObjs:
            # 获取时间轴
            startFrame  =   mc.playbackOptions(min=1,q = 1)
            endFrame    =   mc.playbackOptions(max=1,q = 1)
            # 数据创建
            vData = dict()
            for checkObj in cacheObjs:
                vData[checkObj] = []
            # 即时更新
            for i in range(int(endFrame - startFrame + 1)):
                frameNow = int(startFrame + i)
                mc.currentTime(frameNow)
                for checkObj in cacheObjs:
                    # 处理vState
                    vState = self.checkObjVState(checkObj)
                    if vState:
                        needInfo = [1 , frameNow]
                    else:
                        needInfo = [0 , frameNow]
                    # 处理记录与否
                    if vData[checkObj] == []:
                        vData[checkObj].append(needInfo)
                    else:
                        # 不同的数据则记录
                        if vData[checkObj][-1][0] != vState:
                            vData[checkObj].append(needInfo)
            # 进一步处理数据,处理成list
            resultData = []
            for checkObj in cacheObjs:
                resultData.append([checkObj,vData[checkObj]])
            if server:
                # 输出服务器端
                ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
                self.checkFileWrite((ObjsVDataServerPath +  'cacheObjVInfo.txt'), resultData)
            else:
                # 输出本地
                ObjsVDataLocalPath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
                self.checkFileWrite((ObjsVDataLocalPath +  'cacheObjVInfo.txt'), resultData)
            return  resultData
        
    #------------------------------#    

    #------------------------------#
    # 【核心】【检测v属性】
    #  用途：将时间轴内因隐藏大组出现的显示|隐藏记录
    #      FL环节还原cache物体显示|隐藏动画
    #  Author  : 沈  康
    #  Data    : 2014_02_10
    #------------------------------#
    # 核心检测物体
    def checkObjVState(self,checkObj):
        # 物体不存在则返回0
        if not mc.objExists(checkObj):
            return 0
        # 物体v属性是否存在
        if not mc.attributeQuery('visibility',node = checkObj , exists = 1):
            return 0
        result = mc.getAttr(checkObj +'.visibility')
        # intermediate mesh
        if mc.attributeQuery('intermediateObject',node = checkObj , exists = 1):
            checkValue = mc.getAttr(checkObj + '.intermediateObject')
            result = result and (not checkValue)
        # displayLayer
        if mc.attributeQuery('overrideEnabled',node = checkObj , exists = 1) and mc.getAttr(checkObj + '.overrideEnabled'):
            checkValue = mc.getAttr(checkObj + '.overrideVisibility')
            result = result and checkValue
        # 层级
        if result:
            parentNodes = mc.listRelatives(checkObj,p = 1 ,f = 1 )
            if parentNodes:
                result = result and self.checkObjVState(parentNodes[0])
                
        return result
    
    #------------------------------# 
    #------------------------------#
    # 写文件
    def checkFileWrite(self, path , info , addtion=0):
        print u'>>>>>>[write]'
        print path
        if addtion == 1:
            info = self.checkFileRead(path) + info
        #txt = open(path, 'w')
        try:
            txt = open(path,'w')
        except:
            print '----------'
            print path
            txt = open(path,'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close() 

    #------------------------------#
    # 读文件
    def checkFileRead(self, path):
        print u'>>>>>>[read]'
        print path
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result   

    #------------------------------#
    # 【总篇】【经典Cache 本地|服务器端  创建导出】
    #  0.通用
    #  Author  : 沈  康
    #  Data    : 2013_05_28
    #------------------------------#
    # 传递v显示的动画，OK！！！
    # cache，需要开通GeoCache删写权限
    # 处理的分割情况，遵循一个asset输出一套cache
    # 加入上传服务器功能
    #　objsCache     用于输出cache的物体
    # serverFile    服务器端输出
    # cachePre      预算范围，给特效用;默认是前后5帧，给动态模糊做预留
    #　refMode    　 是否一个参考一个cache
    # createType    创建模式，只输出cache不连接还是输出cache并连接
    # shotType      镜头类型，2位定位还是3位定位
    # resetPosition 回归原点输出
    def checkCacheSetCacheExport(self, objsCache, serverFile = 1 ,cachePre = 0 , refMode = 1 ,createType = 1 ,shotType = 2 , resetPosition = 0 ):
        if not objsCache:
            return 0
        
        # 获取时间轴
        frameStart = mc.playbackOptions(q=1, min=1) 
        frameEnd = mc.playbackOptions(q=1, max=1) 
        mc.playbackOptions(min=frameStart - 51, max=frameEnd + 5)
        
        # 镜头信息
        dirInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotType == 2:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_geoCache'
        if shotType == 3:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_' + dirInfo[3] + '_geoCache'

        # mel用path
        localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
        # local_animPath___python用转mel
        localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType).replace('\\', '/')

        # 服务器端Cache及Anim路径
        # server_cachePath___mel用
        serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        # server_animPath___python用转mel
        serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType).replace('\\', '/')
 

        # 清理历史文件
        oldFiles = mc.getFileList(folder=localPathCache)
        for of in oldFiles:
            if of not in ['assetReference.txt' , 'shotHideObjs.txt' , 'cacheObjVInfo.txt'] and '_anim_' not in of:
                mc.sysFile((localPathCache + of), delete=1)

        # 获取cache物体
        # objsCache = self.checkCacheSetObjects()

        # 备份显示隐藏动画
        animVObjs = []
        hideObjs = []
        for obj in objsCache:
            animCurve = mc.listConnections((obj + '.v'), s=1, d=0)
            if animCurve:
                animVObjs.append(obj)
            else:
                if mc.getAttr(obj + '.v') != True:
                    hideObjs.append(obj)
                    
        # 先处理有动画的
        if animVObjs:
            self.checkAnimCurveInfoExport(animVObjs, serverFile = serverFile , infoFile = 'ca_animV' , shotType = shotType )
        else:
            # 输出空信息
            self.checkAnimCurveInfoExport([], serverFile = serverFile , infoFile = 'ca_animV' , shotType = shotType )
        # 处理自身隐藏的
        if hideObjs:
            self.checkAnimCurveInfoExport(hideObjs, serverFile = serverFile , infoFile = 'ca_hideV', shotType = shotType)
        else:
            # 输出空信息
            self.checkAnimCurveInfoExport([], serverFile = serverFile , infoFile = 'ca_hideV', shotType = shotType)
            
        
        # cachePath
        if serverFile:
            cachePath = serverPathCache
        else:
            cachePath = localPathCache
        
        # 清理目录内文件
        # 只清理txt和cache
        files = mc.getFileList(folder = cachePath , filespec = '*.mc') + mc.getFileList(folder = cachePath , filespec = '*.xml') + mc.getFileList(folder = cachePath , filespec = '*.txt')
        if files:
            for one in files:
                if one not in ['assetReference.txt' , 'shotHideObjs.txt' , 'cacheObjVInfo.txt'] and '_anim_' not in one:
                    mc.sysFile( ( cachePath + one ) , delete = 1)
        print '\n'
        print u'=====================历史文件清理完毕====================='
        print '\n'
            
        # 备份材质
        #MatLists = self.checkCacheRecordMaterial()
        
        # 获取namespace信息
        needCacheObjs = dict()
        for obj in objsCache:
            nsInfo = needCacheObjs.keys()
            ns = obj.split(':')[0]
            if nsInfo == []:
                if ns:
                    needCacheObjs[ns] = [obj]
            else:
                if ns in nsInfo:
                    needCacheObjs[ns].append(obj)
                else:
                    needCacheObjs[ns] = [obj]
        nsInfo = needCacheObjs.keys()
        
        # 回归原点处理
        if resetPosition:
            self.checkCacheResetPositionExport(nsInfo , serverFile , shotType)

        # 经典版本cache处理
        mc.select(objsCache)
        # 删除已有的cache
        try:
            mel.eval('deleteCacheFile 3 { "keep", "", "geometry" } ;')
        except:
            pass
        mc.select(cl=1)

        # 经典版本cache处理
        print '\n'
        print u'=====================【cache】【经典模式】【开始创建】====================='
        print '\n'
        
        # 执行缓存创建
        if refMode == 0:
            lenObjs = len(objsCache)
            splitStep = 250
            if lenObjs > splitStep:
                objTemp = []
                if lenObjs % splitStep == 0:
                    grpNum = lenObjs / splitStep
                else:
                    grpNum = lenObjs / splitStep + 1
                for i in range(grpNum):
                    # 判断最后一位的范围
                    if i == (grpNum - 1):
                        objTemp = objsCache[i * splitStep:]
                    else:
                        objTemp = objsCache[i * splitStep : (i + 1) * splitStep]
                    self.checkCacheDoCreate((fileName + '_' + str(i)), objTemp, cachePath , createType , cachePre )
                    # 输出分段物体信息
                    objPath = cachePath + 'cache_objs_' + str(i) + '.txt'
                    self.checkFileWrite(objPath, objTemp)
                # 输出分段信息
                cacheIndexPath = cachePath + 'cache_objsIndex.txt'
                self.checkFileWrite(cacheIndexPath, [str(grpNum)])
            else:
                self.checkCacheDoCreate((fileName + '_0'), objsCache, cachePath , createType , cachePre)
                # 输出分段物体信息
                objPath = cachePath + 'cache_objs_0.txt'
                self.checkFileWrite(objPath, objsCache )
                # 输出分段信息
                cacheIndexPath = cachePath + 'cache_objsIndex.txt'
                self.checkFileWrite(cacheIndexPath, '0')
        
        # 按namespace处理
        if refMode == 1 and nsInfo:
            for i in range(len(nsInfo)):
                ns = nsInfo[i]
                objTemp = needCacheObjs[ns]
                print u'-------------------------'
                print u'处理cache[%s]ing'%ns
                # 创建cache
                self.checkCacheDoCreate((fileName + '_' + str(i)), objTemp, cachePath, createType , cachePre)
                # 输出分段物体信息
                objPath = cachePath + 'cache_objs_' + str(i) + '.txt'
                self.checkFileWrite(objPath, objTemp)
                print u'处理cache[%s]完毕！'%ns
            # 输出分段信息 , 不加[]给str(len(nsInfo))，会把str(len(nsInfo))处理成list，每个单位一个字符,如16为1,6
            cacheIndexPath = cachePath + 'cache_objsIndex.txt'
            self.checkFileWrite(cacheIndexPath, [str(len(nsInfo))])
        
        # 公用cache
        mel.eval('zwOptimizeGeoCache();')

        # 还原时间轴
        mc.playbackOptions(min=frameStart, max=frameEnd)
        
        # 还原材质
        #self.checkCacheReturnMaterial(MatLists,finalLayout = 1, shotType = shotType)
        
        # 烘焙表情贴图
        #self.checkCacheBakeTexAniFiles()
        
        
        # 上传cache及animPath
        #if serverFile == 1:
        #    self.checkCacheLocalUpdate()

    #------------------------------#
    # 【总篇】【经典Cache 本地|服务器端  导入】
    #------------------------------#
    # 导入cache，还原V动画，yes!
    # 需要细看共享节点
    # 增加从服务器读取功能
    def checkCacheSetCacheImport(self, objsCache, serverFile = 1 , shotType = 2,resetPosition = 0):      
        # 获取时间轴
        frameStart = mc.playbackOptions(q=1, min=1) 
        frameEnd = mc.playbackOptions(q=1, max=1) 
        mc.playbackOptions(min=frameStart - 5, max=frameEnd + 5)
        
        # 镜头信息
        dirInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotType == 2:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_geoCache'
        if shotType == 3:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_' + dirInfo[3] + '_geoCache'
        
        # mel用path
        localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
        # server端path
        if serverFile == 1:
            serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
            localPathCache = serverPathCache
        
        if objsCache:
            # 备份材质
            MatLists = self.checkCacheRecordMaterial()
            
            # 经典版本cache处理
            # 删除已有的cache
            try:
                mel.eval('deleteCacheFile 3 { "keep", "", "geometry" } ;')
            except:
                pass
            
            # 导入cache
            # 查看分段信息
            cacheIndexPath = localPathCache + 'cache_objsIndex.txt'
            splitInfo = self.checkFileRead(cacheIndexPath)
            splitNum = int(splitInfo[0])
            if splitNum == 0:
                mc.select(cl=1)
                mc.select(objsCache)
                localCacheFile = localPathCache + fileName + '_0' + '.xml'
                melCacheCMD = 'doImportCacheFile ' + '"' + localCacheFile + '"' + ' "xml" {} {};' 
                mel.eval(melCacheCMD)
                mc.select(cl=1)
            else:
                mc.select(cl=1)
                for num in range(splitNum):
                    cacheObjsPath = localPathCache + 'cache_objs_' + str(num) + '.txt'
                    objs = self.checkFileRead(cacheObjsPath)
                    mc.select(objs)
                    localCacheFile = localPathCache + fileName + '_' + str(num) + '.xml'
                    melCacheCMD = 'doImportCacheFile ' + '"' + localCacheFile + '"' + ' "xml" {} {};' 
                    mel.eval(melCacheCMD)
                    mc.select(cl=1)

            # 还原v状态
            try:
                self.checkAnimCurveInfoImport(serverFile = serverFile, infoFile = 'ca_hideV' , shotType = shotType)
            except:
                pass
            try:
                self.checkAnimCurveInfoImport(serverFile = serverFile, infoFile = 'ca_animV', shotType = shotType)
            except:
                pass

            # 公用cache
            mel.eval('zwOptimizeGeoCache();')
            
            # 控制器还原属性
            try:
                self.checkAnimCurveInfoImport(serverFile = serverFile, infoFile = 'moveInfo' , shotType = shotType)
            except:
                pass

            # 打断所有连接
            #mel.eval('eyRenderRehyperShade')
  
            # 还原材质
            self.checkCacheReturnMaterial(MatLists,finalLayout = serverFile, shotType = shotType)
            
            # 烘焙表情贴图
            self.checkCacheBakeTexAniFiles()

            # 上传cache
            
        # 还原时间轴
        mc.playbackOptions(min=frameStart, max=frameEnd)

    #------------------------------#
    # 【核心】回到原点cache处理，导出信息
    #------------------------------#
    def checkCacheResetPositionExport(self,nsInfo = [],serverFile = 1, shotType = 2):
        # 回归原点处理
        defaultCtrls = ['Master','Character','WORLD','World','Move','move_ctrl']
        needCtrls = []
        if nsInfo:
            # 搜集控制器
            for ns in nsInfo:
                for key in defaultCtrls:
                    if mc.ls(ns + ':' + key):
                        needCtrls.append(ns + ':' + key)
            if not needCtrls:
                return 0
            # 找到核心最内环
            insideCtrls = []
            for ns in nsInfo:
                nsCtrls = []
                for ctrl in needCtrls:
                    if ns in ctrl:
                        nsCtrls.append(ctrl)
                nsPathCtrls = mc.ls(nsCtrls,l = 1)
                nsDepthPath = []
                if not nsPathCtrls:
                    continue
                for ctrl in nsPathCtrls:
                    nsDepthPath.append(len(ctrl.split('|')))
                insideCtrls.append(nsCtrls[nsDepthPath.index(max(nsDepthPath))])
            
            # locator处理
            finalCtrls = []
            if insideCtrls:
                # 配置loc
                for ctrl in insideCtrls:
                    ns = ctrl.split(':')[0]
                    nsLoc = ns + ':Move_Loc'
                    if mc.ls(nsLoc):
                        mc.delete(nsLoc)
                    mc.spaceLocator(name = nsLoc)
                    mc.parentConstraint(ctrl ,nsLoc )
                    finalCtrls.append(nsLoc)
                # bake loc
                frameStart = mc.playbackOptions(q=1, min=1) 
                frameEnd = mc.playbackOptions(q=1, max=1) 
                mc.bakeResults(finalCtrls, t=(frameStart, frameEnd),
                        simulation=1,
                        sampleBy=1,
                        disableImplicitControl=1,
                        preserveOutsideKeys=1,
                        sparseAnimCurveBake=1,
                        removeBakedAttributeFromLayer=0,
                        bakeOnOverrideLayer=0,
                        controlPoints=0,
                        shape=1)
            # 输出
            if finalCtrls:
                self.checkAnimCurveInfoExport(finalCtrls, serverFile = serverFile, infoFile = 'moveInfo',shotType = shotType)
                # 还原原点
                for ctrl in needCtrls:
                    attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                    for i in range(len(attrs)):
                        attr = attrs[i]
                        connectAttr = mc.listConnections(( ctrl + attr), s=1,plugs=1)
                        if connectAttr:
                            mc.disconnectAttr(('%s') % (connectAttr[0]), ('%s') % (ctrl + attr))
                        mc.setAttr((ctrl + attr),0)
            else:
                self.checkAnimCurveInfoExport([], serverFile = serverFile, infoFile = 'moveInfo',shotType = shotType)  

   #------------------------------#
    # 【核心】【动画数据导入导出PYTHON版】
    # 0.动画
    # Author : 沈  康
    # 参考             : 万寿龙
    # Data   : 2013_05_24 - 2013_05_28
    #------------------------------#   
    # 导出信息
    # 增加上传服务器功能
    def checkAnimCurveInfoExport(self, objs, serverFile=1, infoFile='anim' , targetPath = '' , shotType = 2):
        # 前提基本信息
        AnimsInfo = []
        AnimsInfo.append('ImportExportAnimationForSets v 1.0   (Author: wanshoulong)')
        # 版本号
        AnimsInfo.append('mayaVersion  ' + mc.about(v=1) + ';')
        # 单位类型
        AnimsInfo.append('linearUnit  ' + mc.currentUnit(q=1, f=1, l=1) + ';')
        # 角度单位，弧度还是角度
        AnimsInfo.append('angularUnit  ' + mc.currentUnit(q=1, f=1, a=1) + ';')
        # 制式，PAL等
        AnimsInfo.append('timeUnit  ' + mc.currentUnit(q=1, f=1, t=1) + ';')
        # 获取objs
        if objs:
            for obj in objs:
                # 通道盒子里能被K帧的属性
                keys = mc.listAttr(obj, k=1)
                # 通道盒子中无法被K帧的属性
                noKeys = mc.listAttr(obj, cb=1)
                if noKeys:
                    allAttr = keys + noKeys
                else:
                    allAttr = keys
                if allAttr:
                    for attr in allAttr:
                        animCurve = []
                        if mc.objExists(obj + '.' + attr):
                            # 获取属性的动画曲线
                            animCurve = mc.listConnections((obj + '.' + attr), s=1, d=0)
                        # 剔除无法K帧的情况
                        if animCurve:
                            # 判断是否存在及是否animCurve
                            if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                AnimsInfo.append('anim ' + obj + '.' + attr + '\n{')
                                # 更新信息
                                infoAll = self.checkAnimCurveInfoGet(animCurve[0])  
                                for info in infoAll:
                                    AnimsInfo.append(info)
                                AnimsInfo.append('}')
                        else:
                            # 无动画的信息
                            if mc.objExists(obj + '.' + attr):
                                if 'double3' not in mc.getAttr((obj + '.' + attr), type=1) :
                                    value = mc.getAttr(obj + '.' + attr)
                                    AnimsInfo.append('non-anim ' + obj + '.' + attr + ' ' + str(value) + ';')
                # 对曲线K点的处理
                expShapes = mc.listHistory(obj)
                # 显示控制点的判断
                if expShapes and mc.objectType(expShapes[0], isType='nurbsCurve') and mc.getAttr(expShapes[0] + '.dispCV'):
                    pointNum = mc.getAttr(expShapes[0] + '.spans')
                    # 此处和原脚本不一样
                    for j in range(pointNum * 2):
                        if mc.objExists(expShapes[0] + '.cv[' + str(j) + ']'):
                            allAttr = mc.listAttr((expShapes[0] + '.cv[' + str(j) + ']'), k=1)
                            if allAttr:
                                for attr in allAttr:
                                    animCurve = mc.listConnections((expShapes[0] + '.' + attr), type='animCurve', s=1, d=0)
                                    if animCurve:
                                        if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                            AnimsInfo.append('anim ' + expShapes[0] + '.' + attr + '\n{') 
                                            # 更新信息
                                            infoAll = (self.checkAnimCurveInfoGet(animCurve[0]))
                                            for info in infoAll:
                                                AnimsInfo.append(info)
                                            AnimsInfo.append('}')
                                    else:
                                        # 无动画的信息，不过对于点来说基本用不到
                                        if 'double3' not in mc.getAttr((expShapes[0] + '.' + attr), type=1) :             
                                            value = mc.getAttr(expShapes[0] + '.' + attr)
                                            AnimsInfo.append('non-anim ' + expShapes[0] + '.' + attr + ' ' + str(value) + ';')
        # fsMode，指定输出地址
        if targetPath == '':
            # 本地输出
            # shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType)
            mc.sysFile(localPathAnim, makeDir=True)
            self.checkFileWrite((localPathAnim + infoFile + '.sla'), AnimsInfo)
            # 本地输出object信息
            personalObjsFile = localPathAnim + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)
            '''
            if infoFile in ['moveInfo']:
                objsLong = mc.ls(objs,l=1)
                personalObjsFile = localPathAnim + infoFile + '_Lobjs.txt'
                self.checkFileWrite(personalObjsFile, objsLong)
            '''
            if serverFile == 1:
                # 上传服务器
                self.checkAnimInfoUpdate(infoFile,shotType)
        else:
            # 自定义输出地址
            self.checkFileWrite( (targetPath + infoFile + '.sla') , AnimsInfo)
            # 本地输出object信息
            personalObjsFile = targetPath + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)
        
    #------------------------------#   
    # 动画信息更新到服务器
    def checkAnimInfoUpdate(self, infoFile , shotType = 2):
        import os
        # 本地路径转mel用
        localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType).replace('\\', '/')
        # 服务器端路径转mel用
        serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType).replace('\\', '/')
        # 开始上传
        fileInfo = infoFile + '.sla'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        
        fileInfo = infoFile + '_objs.txt'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        
        fileInfo = infoFile + '_Lobjs.txt'
        if os.path.exists(localPathAnim + fileInfo):
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
            mel.eval(updateAnimCMD)   

    #------------------------------#           
    # 模块：记录功能
    def checkAnimCurveInfoGet(self, animCurve):
        #print '-----------------'
        #print animCurve
        # 帧的时间值
        time = mc.keyframe(animCurve, q=1, tc=1)
        #print time
        # 帧的属性值
        value = mc.keyframe(animCurve, q=1, vc=1)
        # 切线 类型
        inputType = mc.keyTangent(animCurve, q=1, itt=1)
        outputType = mc.keyTangent(animCurve, q=1, ott=1)
        # 切线角度
        inputAngle = mc.keyTangent(animCurve, q=1, ia=1)
        outputAngle = mc.keyTangent(animCurve, q=1, oa=1)
        # 权重
        inputWeight = mc.keyTangent(animCurve, q=1, iw=1)
        outputWeight = mc.keyTangent(animCurve, q=1, ow=1)
        # 锁与否
        # lockType = mc.keyTangent(animCurve, q= 1, l=1)
        weightLock = mc.keyTangent(animCurve, q=1, wl=1)
        
        infoW = ''
        infoAll = []
        if time:
            for i in range(len(time)):
                # time  value  inputType   outputType weightLock
                infoW = (' ' + str(time[i]) + ' ' + str(value[i]) + ' ' + str(inputType[i]) + ' ' + str(outputType[i]) + ' ' + str(weightLock[i])) 
                specialFix = ['fixed']
                # 特殊情况补充行
                if inputType[i] in specialFix or outputType[i] in specialFix and weightLock[i]:
                    infoW = infoW + (' ' + str(inputAngle[i]) + ' ' + str(outputAngle[i]))
                else:
                    if inputType[i] in specialFix  or outputType[i] in specialFix  and weightLock[i] != 'True':
                        infoW = infoW + (' ' + str(inputAngle[i]) + ' ' + str(inputWeight[i]) + ' ' + str(outputAngle[i]) + ' ' + str(outputWeight[i]))
                infoAll.append(infoW + ';')
        return infoAll

    #------------------------------# 
    #------------------------------#
    # 处理OTC的SET文件
    def sk_sceneSETRefShaderReset(self , shotInfo , serverModify = 1 , shotType = 2):

        # 处理OTC的SET文件，但不载入参考
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileGrpType = '_set_render'
        
        if serverModify == 0:
            needFilePath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)

        if serverModify == 1:
            needFilePath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
            
        baseShotInfo = ''
        if shotType == 2:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]

        needSetFile = needFilePath + baseShotInfo + fileGrpType + fileFomat
        print needSetFile
        import os
        if os.path.exists(needSetFile):
            # 不加载参考导入
            mc.file(needSetFile , open = 1, loadReferenceDepth = 'none' , force = 1)
            print u'====================开始处理SET_GRP文件===================='
            # 处理好文件
            # 在importOTC之前处理好anim中材质更改的情况
            sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            mc.file(save = 1, force = 1)
        
        if serverModify == 0:
            # 传至服务器
            renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            print otcFileServer
            mc.sysFile(needSetFile,copy=otcFileServer)            
#            cmd = 'zwSysFile(\"copy\",\"' + needSetFile + '\",\"' + otcFileServer + '\",1)'
#            mel.eval(cmd)
        print u'====================SET_GRP更新完毕===================='

    #------------------------------#    

    #------------------------------#
    # OTC结构处理：导入
    def sk_sceneGRPImport(self, fileGRP='OTC' , shotType = 2):

        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
#        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)       
        # ma文件利于文本读取改参考
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        fileFomat = '.ma'
        fileTypeFull = 'mayaAscii'
        
        baseShotInfo = ''
        if shotType == 2:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
        print otcFileServer
        # 判断otcFile存在与否
        import os
        if os.path.exists(otcFileServer):
            # 在则删除OTC_GRP，并import去掉namespace
            # finalLayout阶段是OTC_GRP是空的
            if mc.ls(fileGRP + '_GRP'):
                mc.delete(fileGRP + '_GRP')
            # import 
            # 记录时间
            import time
            timeNow = time.ctime().split(" ")[3].replace(":", "_")
            # 记录毫秒
            import datetime
            msTime = datetime.datetime.now().microsecond
            timeNow = timeNow + str(msTime / 100000)
            #timeMsec = datetime.datetime.now().microsecond
            #timeNow = timeNow + '_' + str(timeMsec)
            ns = 'food' + timeNow
            if fileGRP == 'SET':
                # 导入,必须这里清理
                print '---'
                print otcFileServer
                mc.file(otcFileServer, i=1 , loadReferenceDepth="none", namespace = ns , type=fileTypeFull , preserveReferences=1 , options="v=0")
                sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            if fileGRP == 'OTC':
                # VFX文件采用tx文件做参考，可以直接用于渲染，无需切换参考
                mc.file(otcFileServer, i=1 , namespace=ns , type=fileTypeFull , preserveReferences=1 , options="v=0")
            # 删除namespace
            mc.namespace(force=1 , moveNamespace=[(':' + ns) , ':'])
            mc.namespace(removeNamespace=(':' + ns))
    
    #-------------------------------------# 
    #------------------------------#
    # OTC结构处理：导入
#    def sk_sceneGRPImport(self, fileGRP='OTC' , shotType = 2):
#
##        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
#        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)       
#        # ma文件利于文本读取改参考
#        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
#        fileFomat = '.ma'
#        fileTypeFull = 'mayaAscii'
#        
#        baseShotInfo = ''
#        if shotType == 2:
#            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
#        if shotType == 3:
#            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
#        
#        fileGrpType = '_' + fileGRP.lower() + '_render'
#        otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
#        
#        # 判断otcFile存在与否
#        import os
#        if os.path.exists(otcFileServer):
#            # 在则删除OTC_GRP，并import去掉namespace
#            # finalLayout阶段是OTC_GRP是空的
#            if mc.ls(fileGRP + '_GRP'):
#                mc.delete(fileGRP + '_GRP')
#            # import 
#            # 记录时间
#            import time
#            timeNow = time.ctime().split(" ")[3].replace(":", "_")
#            # 记录毫秒
#            import datetime
#            msTime = datetime.datetime.now().microsecond
#            timeNow = timeNow + str(msTime / 100000)
#            #timeMsec = datetime.datetime.now().microsecond
#            #timeNow = timeNow + '_' + str(timeMsec)
#            ns = 'food' + timeNow
#            if fileGRP == 'SET':
#                # 导入,必须这里清理
#                print '---'
#                print otcFileServer
#                mc.file(otcFileServer, i=1 , loadReferenceDepth="none", namespace = ns , type=fileTypeFull , preserveReferences=1 , options="v=0")
#                sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
#            if fileGRP == 'OTC':
#                # VFX文件采用tx文件做参考，可以直接用于渲染，无需切换参考
#                mc.file(otcFileServer, i=1 , namespace=ns , type=fileTypeFull , preserveReferences=1 , options="v=0")
#            # 删除namespace
#            mc.namespace(force=1 , moveNamespace=[(':' + ns) , ':'])
#            mc.namespace(removeNamespace=(':' + ns))
    
    #-------------------------------------#        
    # 新建参考
    def sk_FLRefRebuild(self,refInfos,noNeedRefNodeInfo):
        rfnLv1 = refInfos[0][0]
        rfnPathLv1 = refInfos[1][0]
        
        print '[Ref Info]'
        print refInfos[0][0]
        print '[NoNeedRef Info]'
        print noNeedRefNodeInfo
        # 导入参考，注意将_ms_anim替换成_ms_render
        # OTC内的参考不参与处理
        # shareNode只能对第一级reference处理。。。
        for i in range(len(rfnLv1)):
            ns = refInfos[2][0][i]
            refNode = refInfos[0][0][i]
            if noNeedRefNodeInfo:
                if refNode not in noNeedRefNodeInfo:
                    # 应清理refNode及namespace
                    if mc.ls(refNode):
                        try:
                            mc.file(rfn=refNode , removeReference=1)
                        except:
                            mc.lockNode(refNode, l=0)
                            mc.delete(refNode)
                    # 清理namespace
                    try:
                        # 使得namespace成为空的namespace
                        mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
                        # 清理空namespace
                        mc.namespace(removeNamespace= (':' + ns))
                    except:
                        pass
                    newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                    # 此处加referenceNode，是必须的，因为部分文件里即便namespace一致但数字1在refNode顺序不一样
                    # 保证强行一致
                    # shareNodes和cache以及ref list edit有冲突？角色道具可以关闭，同时场景已经合并材质节点
                    # mc.file(newPath, r=1, sharedNodes="shadingNetworks", namespace=ns , referenceNode = refNode )
                    mc.file(newPath, r=1, namespace=ns , referenceNode = refNode )
                    print u'\n'
                    print(u'=====================【创建参考】【%s】=====================' % (rfnLv1[i]))
                    print u'\n'
            else:
                if '_' not in refNode:
                    continue                
                if refNode.split('_')[1][0] not in ['s', 'S']:
                    # 应清理refNode及namespace
                    if mc.ls(refNode):
                        try:
                            mc.file(rfn=refNode , removeReference=1)
                        except:
                            mc.lockNode(refNode, l=0)
                            mc.delete(refNode)
                    # 清理namespace
                    try:
                        # 使得namespace成为空的namespace
                        mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
                        # 清理空namespace
                        mc.namespace(removeNamespace= (':' + ns))
                    except:
                        pass
                    newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                    #mc.file(newPath, r=1, sharedNodes="shadingNetworks", namespace=ns)
                    mc.file(newPath, r=1, namespace=ns , referenceNode = refNode )
                    print u'\n'
                    print(u'=====================【创建参考】【%s】=====================' % (rfnLv1[i]))
                    print u'\n'                                                  

    #------------------------------#
    # 【辅助】【备份材质】
    #------------------------------#
    # 备份材质，不处理Set材质
    # 字典真爽/\ /\
    def checkCacheRecordMaterial(self, checkObjs = [] , finalLayout = 0 ,cacheMode = 1 ,shotType = 3):
        SG = mc.ls(type='shadingEngine')
        # 选取模式
        if checkObjs:
            needSG = []
            errorObjs = []
            for obj in checkObjs:
                if not mc.ls(obj):
                    errorObjs.append(obj)
            if errorObjs:
                print u'------------------------以下物体不存在------------------------'
                for info in errorObjs:
                    print info
                print u'------------------------以上物体不存在------------------------'
                print(u'------------------------请检测物体清单------------------------')
                mc.error(u'------------------------请检测物体清单------------------------')
            else:
                for obj in checkObjs:
                    meshsp = mc.listRelatives(obj,ni=1,type = 'mesh',s =1 ,f=True)
                    if meshsp:
                        mesh=meshsp[0]
                        if mc.listConnections(mesh,destination = 1,type = 'shadingEngine'):
                            nodeSG = mc.listConnections(mesh,destination = 1,type = 'shadingEngine')
                            for node in nodeSG:
                                needSG.append(node)
                SG = list(set(needSG))
        # 备份信息
        MatLists = dict({})
        for node in SG:
            connectObjsSG = mc.sets(node, q=1)
            if connectObjsSG:
                MatLists[node] = connectObjsSG
        # finalLayout上传信息
        if finalLayout:
            self.checkCacheRecordMaterialExport(MatLists,3)
        return MatLists 

    #------------------------------#
    # 【辅助】【材质信息备份到服务器端】【拆分用】
    #------------------------------#        
    # 输出材质信息
    def checkCacheRecordMaterialExport(self,MatLists,shotType = 2):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        if shotType == 2:
            localShaderInfoPath = localPath + 'finalLayoutTemp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            localShaderInfoPath = localPath + 'finalLayoutTemp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        SGKeys = MatLists.keys()
        allInfo = []
        for i in range(len(SGKeys)):
            if i == 0:
                allInfo = SGKeys + [u'********'] + MatLists[SGKeys[i]] + [u'--------']
            else:
                allInfo = allInfo  + MatLists[SGKeys[i]] + [u'--------']
        # 写
        fileInfo = 'ShotShaderInfo.txt'
        mc.sysFile(localShaderInfoPath, makeDir=True)     
        self.checkFileWrite((localShaderInfoPath + fileInfo),allInfo)
        # 上传
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if shotType == 2:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        mc.sysFile(serverDataPath, makeDir=True)   
#        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localShaderInfoPath + fileInfo) + '"' + ' ' + '"' + (serverDataPath + fileInfo) + '"' + ' true'
#        mel.eval(updateAnimCMD)
        mc.sysFile((localShaderInfoPath + fileInfo),copy=(serverDataPath + fileInfo))
        mc.sysFile((localShaderInfoPath + fileInfo),delete=True)
        print u'===[Updating ShotShaderInfo To Server]===传输[%s]完毕==='%fileInfo
            
    #------------------------------#
    # 【核心】回到原点cache处理，导入信息
    #------------------------------#
    def checkCacheResetPositionImport(self,serverFile = 1, shotType = 2):
        # 读控制器
        infoFile = 'moveInfo'
        if serverFile:
            path = sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType)
        else:
            path = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType)
        print '---'
        print (path + infoFile + '_objs.txt')
        needCtrls = sk_infoConfig.sk_infoConfig().checkFileRead(path + infoFile + '_objs.txt')
        #pathCtrls = sk_infoConfig.sk_infoConfig().checkFileRead(path + infoFile + '_Lobjs.txt')
        if not needCtrls:
            return 0
        # 创建控制器
        nsInfo = []
        rootCtrlGrp = 'Food_Temp_Ctrls'
        if mc.ls(rootCtrlGrp):
            mc.delete(rootCtrlGrp)
        mc.group(name = rootCtrlGrp,em = 1)
        for ctrl in needCtrls:
            if ':' in ctrl:
                nsInfo.append(ctrl.split(':')[0])
            if mc.ls(ctrl):
                mc.delete(ctrl)
            mc.circle(name = ctrl)
            mc.parent(ctrl,rootCtrlGrp)
        # 整理控制器
        ctrlInfo = []
        for i in range(len(nsInfo)):
            # namespace相关控制器
            ns = nsInfo[i]
            for ctrl in needCtrls:
                if ns in ctrl:
                    ctrlInfo.append(ctrl)
        # 传动画曲线
        self.checkAnimCurveInfoImport(serverFile=serverFile, infoFile='moveInfo' , replace = [] ,targetPath = '' , shotType = shotType)
        if not nsInfo:
            return 0
        # 给MODEL组K帧
        startFrame = mc.playbackOptions(min=1,q = 1)
        startFrame = startFrame - 5
        endFrame   = mc.playbackOptions(max=1,q = 1)
        endFrame   = endFrame + 5
        attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
        for frame in range(int(startFrame),int(endFrame+1)):
            mc.currentTime(frame)
            for j in range(len(nsInfo)):
                ns = nsInfo[j]
                nsctrl = ctrlInfo[j]
                if not nsctrl:
                    continue
                # 读属性写属性
                setObj = ns + ':' + 'MODEL'
                for attr in attrs:
                    value = mc.getAttr(nsctrl + attr)
                    mc.setAttr((setObj + attr),value)
                    mc.setKeyframe(setObj + attr)
        # 清理
        mc.delete(rootCtrlGrp) 

    #------------------------------#   
    # 导入信息
    # 加入从服务器端读取功能
    def checkAnimCurveInfoImport(self, serverFile=1, infoFile='anim' , replace = [] ,targetPath = '' , shotType = 2):
        # 考虑下清理动画
        # 错误信息
        errorInfo = []
        # fsMode，指定路径读取
        if targetPath == '':
            # 本地获取
            if serverFile == 1:
                serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType)
                personalAmimFile = serverPathAnim + infoFile + '.sla'
                personalObjFile = serverPathAnim + infoFile + '_objs.txt'
            else:
                localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType)
                personalAmimFile = localPathAnim + infoFile + '.sla'
                personalObjFile = localPathAnim + infoFile + '_objs.txt'
        else:
            # 自定义读取路径
            personalAmimFile = targetPath + infoFile + '.sla'
            personalObjFile = targetPath + infoFile + '_objs.txt'
        # 动画信息
        AnimsInfo = self.checkFileRead(personalAmimFile)
        # 获取objct信息，检测obj
        nsObjs = self.checkFileRead(personalObjFile)
        print nsObjs
        # 对物体有效性进行处理
        if nsObjs:
            checkNoneName = []
            for obj in nsObjs:
                # 替换物处理
                if replace:
                    obj = obj.replace(replace[0],replace[1])
                    if infoFile == 'proxy':
                        # master传proxy
                        if 'MSH_c_hi_proxy' not in replace[0]:
                            obj = obj + '_'
                        # proxy传master
                        if 'MSH_c_hi_proxy' in replace[0]:
                            obj = obj[0:-1]
                exist = mc.objExists(obj)
                if exist != True:
                    checkNoneName.append(obj)
            # 无错误
            if checkNoneName == []:
                linesInfo = len(AnimsInfo)
                if linesInfo > 5:
                    # 预设置
                    aniID = []
                    nonAnimID = []
                    # 单位
                    # linear = mc.currentUnit(q=1, f=1, l=1) 
                    linearSla = AnimsInfo[2].split(' ')[2][0:-1]
                    mc.currentUnit(linear=linearSla) 
                    # 角度
                    # anglular = mc.currentUnit(q=1, f=1, a=1)
                    anglularSla = AnimsInfo[3].split(' ')[2][0:-1]
                    mc.currentUnit(angle=anglularSla) 
                    # 制式
                    # timeType = mc.currentUnit(q=1, f=1, t=1)
                    timeTypeSla = AnimsInfo[4].split(' ')[2][0:-1]
                    mc.currentUnit(time=timeTypeSla) 
                    # 处理不对信息
                    for i in range(5, linesInfo):
                        # 去掉回车符
                        lineInfo = AnimsInfo[i][0:-1]
                        # 取anim行数信息
                        # maya的python中没有startsWith，换个方法
                        if 'anim ' in lineInfo and 'non-anim' not in lineInfo:
                            aniID.append(i)
                        if 'non-anim'  in lineInfo:
                            nonAnimID.append(i)
                    # 处理anim信息
                    for aid in aniID:
                        lineInfo = AnimsInfo[aid][0:-1]
                        # 获取属性
                        attr = lineInfo.split('.')[-1]
                        # 物体名处理
                        objCtrl = lineInfo.split('.')[0].split(' ')[-1]
                        # 替换
                        if replace:
                            objCtrl = objCtrl.replace(replace[0],replace[1])
                            if infoFile == 'proxy':
                                # master传proxy
                                if 'MSH_c_hi_proxy' not in replace[0]:
                                    objCtrl = objCtrl + '_'
                                # proxy传master
                                if 'MSH_c_hi_proxy' in replace[0]:
                                    objCtrl = objCtrl[0:-1]
                                    
                        key = ''
                        if 'Shape' not in objCtrl:
                            key = objCtrl + '.' + attr
                        else:
                            ctrolPoint = lineInfo.split('.')[-2]
                            key = objCtrl + '.' + ctrolPoint + '.' + attr
                        # key要存在，且只有一个，且可K帧，且没被锁
                        if len(mc.ls(key)) == 1 and mc.getAttr(key, k=1) and mc.getAttr(key, l=1) != 1:
                            # 处理存在的动画曲线
                            existAnim = mc.listConnections(key, s=1, d=0)
                            if existAnim:
                                mc.delete(existAnim)
                            # 获取{}内数据
                            for j in range(1, linesInfo):
                                nextLine = AnimsInfo[aid + j ]
                                if (nextLine != '}') :
                                    if (nextLine != '{'):
                                        # 开始获取属性数据
                                        infoDetails = nextLine.split(' ')
                                        # time
                                        keyFrame = float(infoDetails[1])
                                        # value
                                        keyValue = float(infoDetails[2])
                                        # in & out
                                        keyInput = infoDetails[3]
                                        keyOutput = infoDetails[4]
                                        # weight
                                        infoWeightLock = infoDetails[5]
                                        if infoWeightLock == 'True' and (infoDetails[3] == 'fixed' or infoDetails[4] == 'fixed'):
                                            # in & out angle
                                            keyInputAngle = float(infoDetails[6])
                                            if ';' in infoDetails[7]:
                                                infoDetails[7] = infoDetails[7][0:-1]
                                            keyOutputAngle = float(infoDetails[7])
                                            # 还原帧
                                            mc.setKeyframe(key, t=keyFrame , v=keyValue)
                                            mc.selectKey(key, k=keyFrame, r=1)
                                            mc.keyTangent(e=1, ia=keyInputAngle, iw=1, oa=keyOutputAngle, ow=1)
                                        else:
                                            if infoWeightLock != 'True' and (infoDetails[3] == 'fixed' or infoDetails[4] == 'fixed'):
                                                # in & out angle and weight
                                                keyInputAngle = float(infoDetails[6])
                                                keyInputWeight = float(infoDetails[7])
                                                keyOutputAngle = float(infoDetails[8])
                                                if ';' in infoDetails[9]:
                                                    infoDetails[9] = infoDetails[9][0:-1]
                                                keyOutputWeight = float(infoDetails[9])
                                                # 还原帧
                                                mc.setKeyframe(key, t=keyFrame , v=keyValue)
                                                mc.selectKey(key, k=keyFrame, r=1)
                                                mc.keyTangent(e=1, ia=keyInputAngle, iw=keyInputWeight, oa=keyOutputAngle, ow=keyOutputWeight)
                                            else:
                                                mc.setKeyframe(key, t=keyFrame , v=keyValue, itt=keyInput, ott=keyOutput)
                                else:       
                                    break
                        else:
                            #errorInfo.append(('===============请检查【%s】，是否唯一，是否可K帧，是否解锁===============') % (str(key)))
                            errorInfo.append(u'===============请检查【%s】，是否唯一，是否可K帧，是否解锁===============' % (key))
                    # 处理non-anim信息
                    for nid in nonAnimID:
                        # 获取属性
                        key = AnimsInfo[nid].split(' ')[1]
                        # 替换
                        if replace:
                            key = key.replace(replace[0],replace[1])
                            if infoFile == 'proxy':
                                # master传proxy
                                if 'MSH_c_hi_proxy' not in replace[0]:
                                    key = key + '_'
                                # proxy传master
                                if 'MSH_c_hi_proxy' in replace[0]:
                                    key = key[0:-1]
                        # key要存在，且只有一个，且可K帧，且没被锁
                        # 锁住后无法处理
                        # valueType 1,浮点数 | 0 字符串
                        valueType = 1
                        if len(mc.ls(key)) == 1 and mc.getAttr(key, k=1) and mc.getAttr(key, l=1) != 1:
                            # 处理存在的动画曲线
                            existAnim = mc.listConnections(key, s=1, d=0)
                            if existAnim:
                                mc.delete(existAnim)
                            # 获取属性数据
                            value = AnimsInfo[nid].split(' ')[2][0:-1]
                            if value == 'True':
                                value = float(1.0)
                            if value == 'False':
                                value = float(0.0)
                            if value != 'True' and value != 'False':
                                try:
                                    value = float(value)
                                except:
                                    valueType = 0
                                    value = str(value)
                            if valueType:
                                mc.setAttr(key, value)
                            else:
                                mc.setAttr(key, value,type = 'string')
                else:  
                    #errorInfo.append('=====================【！！！动画信息错误！！！】=====================')
                    errorInfo.append(u'=====================【！！！动画信息错误！！！】=====================')
            # 丢失物体
            else:
                for error in checkNoneName:
                    #errorInfo.append(('=====================【！！！错误！！！】不存在传递物体【%s】=====================') % (error))
                    errorInfo.append(u'=====================【！！！错误！！！】不存在传递物体【%s】=====================' % (error))
                    #errorInfo.append('=====================【！！！动画信息错误！！！】=====================')
                    errorInfo.append(u'=====================【！！！动画信息错误！！！】=====================')
            for i in errorInfo:
                print(i) 

    #------------------------------#
    # v信息导入
    def checkCacheVStateImport(self , shotType = 2):
        vData = self.checkObjsVData(shotType)
        if vData:
            cacheObjs = vData.keys()
            for cacheObj in cacheObjs:
                keyInfo = vData[cacheObj]
                #print '-----'
                #print len(keyInfo)
                #print keyInfo
                # 单帧
                if len(keyInfo) == 1:
                    vState = keyInfo[0][0]
                    mc.setAttr((cacheObj + '.v'),vState)
                # 多帧
                else:
                    for i in range(len(keyInfo)):
                        vState = keyInfo[i][0]
                        frame = keyInfo[i][1]
                        #print vState
                        #print frame
                        mc.currentTime(frame)
                        mc.setAttr((cacheObj + '.v'),vState)
                        mc.setKeyframe((cacheObj + '.v'))

    #------------------------------#                
    #------------------------------#
    # 【辅助】【还原材质】
    #------------------------------#
    # 还原材质
    def checkCacheReturnMaterial(self, MatLists = [] ,finalLayout = 0,shotType = 2):
        if finalLayout:
            MatLists = self.checkCacheRecordMaterialImport(shotType)
        keysSG = MatLists.keys()
        for key in keysSG:
            objs = MatLists[key]
            # 必须加objs，不然会断掉
            if objs:
                mc.sets(objs, forceElement = key)

    #------------------------------#
    # 【辅助】【材质信息导入】【拆分用】
    #------------------------------#    
    # 输出材质信息
    def checkCacheRecordMaterialImport(self,shotType):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if shotType == 2:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        fileInfo = 'ShotShaderInfo.txt'
        allInfo = self.checkFileRead(serverDataPath + fileInfo)
        # 分割点
        signKeyIndex = self.checkListSameAllIndex(allInfo,u'********')[0]
        signMeshSplitIndexList = self.checkListSameAllIndex(allInfo,u'--------')
        # 开始还原
        MatLists = dict({})
        # 创建keys
        for i in range(signKeyIndex):
            MatLists[allInfo[i]] = []
        # 每类创建
        for i in range(len(signMeshSplitIndexList)):
            if i == 0:
                meshNum = signMeshSplitIndexList[i] - signKeyIndex - 1
            else:
                meshNum = signMeshSplitIndexList[i] - signMeshSplitIndexList[i-1] - 1
            for j in range(meshNum):
                baseMeshIndex = signMeshSplitIndexList[i] - meshNum
                MatLists[allInfo[i]].append(allInfo[baseMeshIndex + j])
        return MatLists   

    #----------------------------#
    # 【通用：获取checkList内所有相同元素的编号】
    #----------------------------#
    # 获取list内所有相同元素的编号 ，index number
    def checkListSameAllIndex(self, checkList, checkObj):
        tempList = checkList[:]
        checkAdd = 0
        allIndex = []
        while tempList.count(checkObj) > 0:
            indexNow = tempList.index(checkObj)
            allIndex.append(checkAdd + indexNow)
            tempList.remove(checkObj)
            checkAdd = checkAdd + 1
        return allIndex                     
    #------------------------------#
    # 【辅助】【Bake表情贴图】
    #------------------------------#    
    # bake表情贴图
    def checkCacheBakeTexAniFiles(self):
        # 获取时间轴
        frameStart = mc.playbackOptions(q=1, min=1) 
        frameEnd = mc.playbackOptions(q=1, max=1) 
        files = mc.ls(type='file')
        for f in files:
            cons = mc.listConnections(f + '.frameExtension')
            if cons:
                mc.bakeResults(f + '.frameExtension', sb=1, t=(frameStart, frameEnd))  

    #------------------------------#
    # 【辅助】【本地cache上传处理】
    #------------------------------#
    # 处理上传
    def checkCacheLocalUpdate(self,shotType):
        # 本地Cache及Anim路径
        # local_cachePath___mel用
        localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
        # local_animPath___python用转mel
        localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType).replace('\\', '/')

        # 服务器端Cache及Anim路径
        # server_cachePath___mel用
        serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        # server_animPath___python用转mel
        serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType).replace('\\', '/')
        # cache上传
        cacheInfos = mc.getFileList(folder=localPathCache)
        
        for cacheInfo in cacheInfos:
            fileInfo = cacheInfo
            updateCacheCMD = 'zwSysFile "copy" ' + '"' + (localPathCache + fileInfo) + '"' + ' ' + '"' + (serverPathCache + fileInfo) + '"' + ' true'
            mel.eval(updateCacheCMD)
            print u'===[Updating Cache To Server]===传输[%s]完毕==='%fileInfo
            
        # anim上传
        fileInfo = 'ca_animV_objs.txt'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        fileInfo = 'ca_animV.sla'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        fileInfo = 'ca_hideV_objs.txt'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        fileInfo = 'ca_hideV.sla'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        
        print u'==============缓存及动画数据全部传输完毕==============' 

    #------------------------------#
    # 【核心】执行创建cache
    #------------------------------#
    def checkCacheDoCreate(self, fileName, objs, path , createType = 0 , cachePre = 0):
        # 标准设置
        cacheType = 'OneFilePerFrame'
        # cacheType = 'OneFile'
        cacheFormat = 'mcc'
        # 参数获取
        frameStart = mc.playbackOptions(q=1, min=1)
        frameEnd = mc.playbackOptions(q=1, max=1)
        # 获取shape
        objsShape = []
        for obj in objs:
            # 需要进行甄别
            # 有输出的才有效；OG无效
            mesh = mc.listRelatives( obj ,pa=1,ni=1,s=1,type='mesh')
            if mesh:
                objsShape.append(mesh[0])
            
        # 本函数只创建，不连接
        if createType == 0:
            mc.cacheFile(f = fileName ,singleCache = 1,dir = path , st = (frameStart+cachePre) , et = frameEnd ,points = objsShape)
        
        # 创建并连接，比较慢
        if createType == 1:
            cacheType = 'OneFile'
            mc.select(objs)
            # doCreateGeometryCache 6 { "3", "1", "24", "OneFile", "1", "E:/TD_work/Data/test","0","","0", "add", "0", "1", "1","0","1","mcc","0" } ;
            # doCreateGeometryCache (版本号6) {(), (startFrame), (endFrame), (onFile), (), (path), (‘0‘),  (fileName) ,(‘0‘) ,('add'),(),('1'),('1'),('0').('1').('mcc'),'0'}
            # add后的参数为1时自动覆盖
            cacheCMD = 'doCreateGeometryCache 6 { "3", "%s", "%s", "%s", "1", "%s","0","%s","0", "add", "1", "1", "1","0","1","%s","0" }' % (str(frameStart+cachePre) , str(frameEnd) , cacheType, path , fileName , cacheFormat)
            mel.eval(cacheCMD)
            mc.select(cl = 1)   

    #------------------------------#
    # vData数据结构处理
    def checkObjsVData(self, shotType = 2):
        ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        resultData = self.checkFileRead(ObjsVDataServerPath +  'cacheObjVInfo.txt')
        vData = dict()
        import os
        if os.path.exists(ObjsVDataServerPath +  'cacheObjVInfo.txt'):
            for lineInfo in resultData:
                # obj
                obj = lineInfo.split(', ')[0][3:-1]
                vData[obj] = []
                # frameList
                frameList = lineInfo.split('\', ')[-1]
                # 单帧情况
                if '], ' not in frameList:
                    frameInfo = frameList.split(', ')
                    vState = frameInfo[0][2:]
                    frame = frameInfo[-1][:-3]
                    vData[obj].append([int(vState),int(frame)])
                # 多帧情况
                else:
                    allInfos = frameList.split('], ')
                    needInfo = []
                    for i in range(len(allInfos)):
                        frameInfo = allInfos[i].split(', ')
                        vState = frameInfo[0][1:]
                        frame = frameInfo[-1][:]
                        if i == 0:
                            vState = frameInfo[0][2:]
                        if i == (len(allInfos) - 1):
                            frame = frameInfo[-1][:-3]
                        needInfo.append([int(vState),int(frame)])
                    vData[obj] = needInfo
        return vData

    def csl_refneedInfo(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRN=refInfos[0][0]
        reffile=refInfos[1][0]
        refnamespace=refInfos[2][0]
        refRNneedList=[]
        reffileRNneedList=[]
        refneedList=[]    
        setneed=['s001007ShootingGallery','s001008DormitoryExt','s001009PlayGround','s001010MainBuilding','s001001TrainingGround','s001002TrainingGroundGate']
        for i in range(len(refRN)):
            if 'csl' in refRN[i] and '_' in refRN[i] and refnamespace[i].split('_')[1] in setneed:
                refRNneedList.append(refRN[i])
                reffileRNneedList.append(reffile[i])
                refneedList.append(refnamespace[i])     
    
        return [refRNneedList,reffileRNneedList ,refneedList]  

    def csl_setRefSwitch(self,ID='s001020MilitaryCamp'):
        setinfoList=self.csl_refneedInfo()
        fileshort=mc.file(q=1,shn=1,sn=1)
        temppath='D:/Info_Temp/setswitch/'
        mc.sysFile(temppath, makeDir=True)        
        setrefRN=setinfoList[0]
        if setrefRN:
            for i in range(len(setrefRN)):
                mc.file(rfn = setrefRN[i] , removeReference = 1)
                print u'====已经删除【%s】参考===' % setinfoList[2][i].split('_')[1]
                
            refRNnew='csl_'+ID+'RN'
            refNamespaceN='csl_'+ID+'_h'
            refoldfile=setinfoList[1][0]
            refoldinfo=setinfoList[1][0].split('_')[1]
            refFileN=refoldfile.replace(refoldinfo,ID)
            mc.file(refFileN, r=1, namespace=refNamespaceN , referenceNode = refRNnew) 
            mc.file(rename=(temppath+fileshort))
            mc.file(save=1,type ='mayaBinary',f = 1)
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
            print u'====【%s】场景已经替换===' %    fileshort 
            print u'====文件路径【%s】===' %    temppath
        else:
            print u'===【%s】没有需要替换的场景===='  %    fileshort      
    
    
    #------------------------------#
    # 【通用】【FS后台工具】【核心】(改自Final工具）
    #  Author  : 韩虹
    #  Data    : 2015_03
    #------------------------------#
    def GDC_FinaloutABC(self,server=1,cachePre=-12,shotType=2,shave=0):
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        import os
        #---------------------------#
        # Setup 000  外部操作，
        #---------------------------#
        

        #---------------------------#
        # Setup 001  多级非参考的namespace清理。
        # 某些外包，喜欢做动作模板，然后import进来，这样形成了两级namespace，而在参考是不会记录import的那级参考。
        # 这种情况，要处理掉，不然后面记录参考信息时会出问题
        #---------------------------#
        # 处理非参考的namespace
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
                #---------------------------#
        # Setup 002  判断是否动画shot里的参考是否都有render 版本。如果没有，报错退出
        #---------------------------#
        # 检测参考是否正确，是否有render参考
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        self.sk_FLCheckRenderFile(refInfos)
        #---------------------------#
        # Setup 003  记录基本信息，修正时间轴
        #---------------------------#
        
        # 记录项目，场次，镜头号,文件类型
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfos[0])
        print u'\n'
        print(u'=====================【%s_%s】【FinalLayout】开始处理！！！====================='%(shotInfos[1],shotInfos[2]))
        print(u'=========================================================================')
                
        # 修正时间轴
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame',shotType)        
        #---------------------------#
        # Setup 004  本地另存，备份
        #---------------------------#
        # 获取FS临时路径
        localPath = sk_infoConfig.sk_infoConfig().alembicLocalPath(shotType)
        # 获取FS服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().alembicServerPath(shotType)   

        # 本地另存
        shotName=''
        if shotType==2:
           shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]  
        if shotType==3:
            shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]   
        localFile = localPath + shotName+'_an_c001' + fileFormat
        mc.file(rename = localFile)
        mc.file(save=1,force = 1)                            

        #---------------------------#
        # Setup 005  清理外包残留的playblast表达式
        #---------------------------#
        if mc.ls('zwHeadsUpDisplay',type = 'expression'):
            mc.delete('zwHeadsUpDisplay')
            print u'\n'
            print u'====================【zwHeadsUpDisplay】清理完毕===================='
            print u'\n'                    

        #---------------------------#
        # Setup 006  清理未勾选的参考，清理垃圾节点，更新camera，IKR再启动
        #---------------------------#
        sk_sceneTools.sk_sceneTools().sk_sceneUnloadRefDel(1,0)
        print u'\n'
        print u'========================未勾选参考清理完毕========================'
        print u'\n'

        # 初步清理垃圾节点
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean(unuse=1 , turtle=1)
        # 强制启动IK解算
        mc.ikSystem(e = 1,sol = 1)
        print u'\n'
        print u'=========================IK解算器强制更新========================'
        print u'\n'
        # 更新摄像机           
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfos[0])
        camServerPath=''
        if projectInfo in ['YongTai']:
            camServerPath = 'Z:/Projects/DomesticProject/' + projectInfo + '/Project/scenes/Animation/episode_' + shotInfos[1] + '/episode_camera/'
        else:            
            camServerPath = 'Z:/Projects/' + projectInfo + '/Project/scenes/Animation/episode_' + shotInfos[1] + '/episode_camera/'
        camServerPathN = camServerPath + shotName+ '_cam.ma'
        if os.path.exists(camServerPath):
            pass
        else:
            if server:
                sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1)
                print u'\n'
                print u'==========================camera传输完毕=========================='
                print u'\n'                
 
        #---------------------------#
        # Setup 007  约束烘焙
        #---------------------------#
        #预处理，约束清理
        self.sk_checkBakeConstraints()
        print(u'========================【约束】【烘焙】【成功】========================')                                        

        #---------------------------#
        # Setup 008 清除服务器data目录残留的SET和OTC文件
        # 【注意】 如果有SD环节，酌情清理OTC，SET需要从服务器端参考
        #---------------------------#
        # 清理服务器端旧的SET和OTC文件
        self.sk_sceneGRPDelete('SET')
        self.sk_sceneGRPDelete('OTC')
        
        #---------------------------#
        # Setup 009 文件内部大组归类
        #---------------------------#
        # 处理SET_GRP和OTC_GRP内的参考
        # 处理大组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
        print u'\n'
        print u'==========================文件整理完毕=========================='
        print u'\n'

        #---------------------------#
        # Setup 010 动画文件内，隐藏的物体，记录下来，cache之后恢复隐藏
        #---------------------------#
        if shotType==2:
            unDisplayLayerObjs = self.sk_FL_RefHideObjsRecord(server=1,shotType=2)
        if shotType==3:
            unDisplayLayerObjs = self.sk_FL_RefHideObjsRecord(server=1,shotType=3)  
            
        #---------------------------#
        # Setup 011 获取anim shot的参考信息
        #---------------------------#
        # 获取references信息
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        #---------------------------#
        # Setup 012 默认OTC和SET组内的参考不参与cache及重新参考，这里记录不需要的参考信息
        #---------------------------#
        # 处理大组
        noNeedRefNodeInfo = self.skFLNoNeedRefNodeInfo()
        #---------------------------#
        # Setup 013 本文件asset参考信息导出，给分解步骤用
        # 这里只记录角色和道具
        #---------------------------#
        # 输出需要的角色和道具参考信息
        if server:
            assetNeedOutputInfo = self.skFLAssetNeedInfo(refInfos,noNeedRefNodeInfo,shotType) 
        #---------------------------#
        # Setup 014 OTC和SET组导出
        # 务必使用ma格式，之后会用文本读取方式替换参考，避免打开后又加载参考，提高效率
        #---------------------------#
        # 导出SET_GRP和OTC_GRP文件
        self.sk_sceneGRPExport('SET',server,shotType)
        self.sk_sceneGRPExport('OTC',server,shotType ) 

        print u'\n'
        print(u'=====================【Group】【服务器端】【输出】完毕=====================')
        print u'\n'
        
        print u'\n-------------------------'
        print '[Ref Info]'
        print refInfos[0][0]
        print u'-------------------------' 

        # 判断是否ms_anim文件
        if shotType==2 and shotInfos[3] == 'an':
            #---------------------------#
            # Setup 015 删除set参考，加快速度
            #---------------------------#
            # 首先删除set参考，加快速度
            rfnLv1 = refInfos[0][0]
            rfnPathLv1 = refInfos[1][0]
            if refNodes:
                for ref in refNodes:
                    if '_' not in ref:
                        continue
                    if ref.split('_')[1][0] in ['s', 'S']:
                        # 删除参考
                        mc.file(rfn=ref, removeReference=1)
            print u'\n'
            print(u'=====================【SET类参考】【清理】完毕=====================')
            print u'\n'
        if shotType==3 and shotInfos[4] == 'an':
            #---------------------------#
            # Setup 015 删除set参考，加快速度
            #---------------------------#
            # 首先删除set参考，加快速度
            rfnLv1 = refInfos[0][0]
            rfnPathLv1 = refInfos[1][0]
            if refNodes:
                for ref in refNodes:
                    if '_' not in ref:
                        continue
                    if ref.split('_')[1][0] in ['s', 'S']:
                        # 删除参考
                        mc.file(rfn=ref, removeReference=1)
            print u'\n'
            print(u'=====================【SET类参考】【清理】完毕=====================')
            print u'\n' 

        #---------------------------#
        # Setup 016 输出cache，以及传递动画的控制器动画
        # cache过程中，加入了对隐藏|组K帧物体的检测，记录显示隐藏动画以便还原
        #---------------------------#
        # 输出cache 

        # 输出ABC
 
        cacheObjs = self.GDC_alembicInfo(3)
        if cacheObjs:
            # 输出显示隐藏动画信息
            self.checkCacheVStateExport(cacheObjs,shotType )
            print u'\n'
            print(u'=====================【Cache】【V信息】【服务器端】【输出】完毕=====================')
            print u'\n'
            # 输出cache
            # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
            self.GDC_alembicExr(1,0,shotType,0,0)            
            print u'\n'
            print(u'=====================【alembic】【服务器端】【输出】完毕=====================')
            print u'\n'            
        else:
            print u'\n'
            print(u'=====================【alembic】无物体！！！！！！=====================')
            print u'\n'
        if shave==1:
            curveObjs=self.GDC_shaveInfo(3,'abc_curve')
            if curveObjs:
                self.GDC_shavealembicExr(server,shotType)
                print u'\n'
                print(u'=====================【abc_curve】【服务器端】【输出】完毕=====================')
                print u'\n'
            else:
                print u'\n'
                print(u'=====================【abc_curve】无物体！！！！！！=====================')
                print u'\n'                                  
                
        

        #---------------------------#
        # Setup 017 对动画文件的处理告一段落，这里处理SET和OTC里面的参考替换，同时清理参考材质覆盖
        #---------------------------#
        # 新建文件之前处理好SET_GRP文件 | 后面处理了 |此时处理避免备份时的崩溃
        self.sk_sceneSETRefShaderReset(shotInfos,serverModify = 1 , shotType =shotType) 
        #---------------------------#
        # Setup 018 开始新文件的架构
        #---------------------------#
        # 新建文件,临时文件夹另存
        mc.file(f=1, new=1)
        print '\n'
        print '[Ref Info]'
        print refInfos[0][0]
        print '\n'
        print(u'=========================【创建新文件】=========================')
        print '\n'
        
        # 准备先另存，因为update需要用到文件名
        fileName = shotName +'_base_fs_c001' + fileFormat
        # 本地文件
        localFile = localPath + fileName
        # 服务器端文件
        # serverFile = serverPath + fileName
        # 重命名
        mc.file( rename= localFile )
        mc.file(save = 1 ,force = 1)
        
    
        #---------------------------#
        # Setup 019 先导入OTC及SET，后创建参考。这里OTC和SET默认不加载，提高速度
        #---------------------------#
        # 导入场景
        # 必须先导入OTC，后载入参考，否则容易出错(PORORO经验)
        # 导回SET_GRP和OTC_GRP
        self.sk_sceneGRPImport('SET',shotType)
        self.sk_sceneGRPImport('OTC',shotType)
        print u'\n'
        print(u'=====================【Group】【服务器端】【导入】完毕=====================')
        print u'\n'
        
        #---------------------------#
        # Setup 020 加载需要的角色和道具类的render参考
        #---------------------------#
        # 导入reference及share nodes（新导入场景，后导入参考）
        self.sk_FLRefRebuild(refInfos,noNeedRefNodeInfo)
        
        #---------------------------#
        # Setup 021 参考最终相机
        #---------------------------#
        # 导入cam
        # 导入相机
        if shotType ==2:
            sk_hbExportCam.sk_hbExportCam().camServerReference(info=2)
        if shotType ==3:
            sk_hbExportCam.sk_hbExportCam().camServerReference(info=3)           

        # Setup 022 新建后的文件大组重新处理
        #---------------------------#
        # 处理大组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(1)
        
    
        #---------------------------#
        # Setup 023 动画文件和fl文件的cache list对比，不一致则报错。 
        # 这里不一致一般在两种情况里发生
        # 1,anim文件和render文件cache list不一致;
        # 2.约束bake失败，某些CHR和PROP和SET有约束残留，导出去的时候CHR,PROP进了SET文件，而SET文件是默认不加载的，丢失部分cacheList
        #---------------------------#
        # 检测cache物体列表
        errorObjs = []
        for obj in cacheObjs:
            if mc.ls(obj) == []:
                errorObjs.append(obj)
        if errorObjs:
            print u'-------------------以下物体不存在-------------------'
            for info in errorObjs:
                print info
            print u'-------------------以上物体不存在-------------------'
            mc.error(u'=====================请通知前期检测anim和render版本cache list=====================') 

    
        # 场景搭建完毕
        # 载入anim
#        self.checkAnimCurveInfoImport(serverFile = 1 ,shotType=shotType)
        
        print u'\n'
        print(u'=====================【Anim】【服务器端】【导入】完毕=====================')
        print u'\n'
        # 处理buging 
        # 载入cache及自带的anim
        cacheObjs = self.GDC_alembicInfo(3)          
        if cacheObjs:
            self.GDC_alembicImp('fs',1,shotType)
            # 处理还原物体           
            # 进行参考reload
            for i in range(len(rfnLv1)):
                ns = refInfos[2][0][i]
                refNode = refInfos[0][0][i]
                if noNeedRefNodeInfo:
                    if refNode not in noNeedRefNodeInfo:
                        print u'================='
                        print refNode
                        print noNeedRefNodeInfo
                        print u'================='
                        newPath = mc.referenceQuery(refNode, filename=True)
            # 导入显示隐藏信息
            self.checkCacheVStateImport(shotType )
            if server:
                print u'\n'
                print(u'=====================【Cache】【服务器端】【导入】完毕=====================')
                print u'\n'
            else:
                print u'\n'
                print(u'=====================【Cache】【本地】【导入】完毕=====================')
                print u'\n'
        else:
            print u'\n'
            print(u'=====================【Cache】无物体！！！！！！！=====================')
            print u'\n'
        if shave==1:
            curveObjs=self.GDC_shaveInfo(3,'abc_curve')
            if curveObjs:
                self.GDC_curvealembicImp(server,shotType)
                print u'\n'
                print(u'=====================【abc_curve】【服务器端】【导入】完毕=====================')
                print u'\n'
            else:
                print u'\n'
                print(u'=====================【abc_curve】无物体！！！！！！=====================')
                print u'\n'                 

        # 处理显示层相关物体
        if unDisplayLayerObjs:
            hideObjs = []
            for obj in unDisplayLayerObjs:
                if mc.ls(obj):
                    hideObjs.append(obj)
            # 放到norender层
            if hideObjs:
                if mc.ls('norender',type = 'displayLayer'):
                    pass
                else:
                    mc.createDisplayLayer(empty = 1, name = 'norender')
                mc.setAttr('norender.visibility',0)
                mc.editDisplayLayerMembers('norender',hideObjs , nr = 1)
        print u'\n'
        print(u'=====================【Displayer】隐藏恢复=====================')
        print u'\n' 

        #---------------------------#
        # Setup 025 备份FL文件
        #---------------------------#
        # 本地保存
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfos[0])
        mc.file(force=1, options="v=0", type=fileTypeFull , save=1)
        # 设置时间轴等消息
        # 命令
        shot=''
        if shotType == 2:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType == 3:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]
        
        #---------------------------#
        # Setup 026 镜头信息，时间轴信息处理                    
        #---------------------------#
        # 开始处理
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart

        endFrame = anim.frmEnd
        fpsFrame = anim.fps
        resW = anim.resolutionW
        resH = anim.resolutionH
        # 分辨率
        mc.setAttr(('defaultResolution.width'), resW)
        mc.setAttr(('defaultResolution.height'), resH)
        # FPS
        if fpsFrame == 25:
            mc.currentUnit(time='pal')
        if fpsFrame == 24:
            mc.currentUnit(time='film')
        if fpsFrame == 30:
            mc.currentUnit(time='ntsc')
        # frame
        if startFrame and fpsFrame:
            # 起始帧
            mc.playbackOptions(min=startFrame)
            # 起始预留
            preStartFrame = startFrame - 10
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=endFrame)
            # 结束预留
            posEndFrame = endFrame + 10
            mc.playbackOptions(animationEndTime=posEndFrame)
        # 设置帧播放模式每帧
        mc.playbackOptions(playbackSpeed=0)
            
        # 允许undo
        mc.undoInfo(state=True, infinity=True)
        
        description = 'FinalLayout Base File'  

    

        
        # 烘焙表情贴图
        self.checkCacheBakeTexAniFiles() 

        # Setup 039 由于之前还原了材质，asset的reference edit列表里会有记录，需要在没加载参考的情况下清理
        #---------------------------#
        self.csl_setattr(attrtype='aiStandIn',attr='visibility',num=1)       
        mc.file(save=1, force = 1)

        # 缺少check in baseFile
        mc.sysFile((localPath + shotName+'_an_c001' + fileFormat),delete=True) 
        print '\n'
        print(u'=========================================================================')
        print(u'=====================【%s_%s_%s】【FinalLayout】处理完毕====================='%(shotInfos[1],shotInfos[2],shotInfos[3]))
        print(u'=====================【%s】文件处理完毕====================='%(localPath + shotName+'_base_fs_c001' + fileFormat))                                                               
       #---------------------------#
        # Setup 030 本地备份之后，check in
        #---------------------------#
        # 上传服务器处理
        if server == 1:
            #sk_cacheFinalLayout.sk_cacheFinalLayout().checkFinalLayoutUpdate()
            # 开始提交文件至服务器
            mc.file(save=1,force = 1)
            # 用户名
            userName = os.environ['USERNAME']
            newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(newInfo[0])
            fileInfo=''
            if shotType==3:
                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
            if shotType==2:
                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3]  + '|' + userName                    
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            #print checkOutCmd
            mel.eval(checkOutCmd)
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')
    
        # 缺少check in baseFile
        print '\n'
        print(u'=========================================================================')
        print(u'=====================【%s_%s】【FinalLayout】处理完毕====================='%(shotInfos[1],shotInfos[2]))                                             
                                                                           
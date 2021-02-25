# -*- coding: utf-8 -*-

'''
Created on 2017

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
class GA_Effectalembic(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    def GA_EffectalembicUI(self):
    # 窗口
        if mc.window('ABCEffect', exists=True):
            mc.deleteUI('ABCEffect')
        mc.window('ABCEffect', title=u'ABC面板',
                  width=360, height=350, sizeable=True)
         # 面板
        form = mc.formLayout()
         # 切换面板
        tabs = mc.tabLayout('tabABC',innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout(
            form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
         # tab_渲染工具
        child1 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label=u'创建ABC', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=1)
        mc.intSliderGrp('framemin',label='frammin', field=True, minValue=-1000, maxValue=10000, fieldMinValue=-1000, fieldMaxValue=10000, value=mc.playbackOptions(min=1,q = 1),columnAttach=[(1,'left',40),(2,'left',0),(3,'both',0)],columnWidth3 = (100,60,150))
        mc.intSliderGrp('framemax', label='frammax', field=True, minValue=-1000, maxValue=10000, fieldMinValue=-1000, fieldMaxValue=10000, value=mc.playbackOptions(max=1,q = 1),columnAttach=[(1,'left',40),(2,'left',0),(3,'both',0)],columnWidth3 = (100,60,150))
        mc.rowColumnLayout(numberOfColumns=3)
        mc.button(label=u'alembic01',width=120,bgc=[0.13, 0.15, 0.25],
                   command='from idmt.maya.py_common import GA_Effectalembic\nreload(GA_Effectalembic)\nGA_Effectalembic.GA_Effectalembic().GA_alembicExr(1,0,"alembic01",1)')
        mc.button(label=u'alembic02',width=120, bgc=[0.13, 0.15, 0.25],
                 command='from idmt.maya.py_common import GA_Effectalembic\nreload(GA_Effectalembic)\nGA_Effectalembic.GA_Effectalembic().GA_alembicExr(1,0,"alembic02",1)')

        mc.button(label=u'alembic03', width=120,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GA_Effectalembic\nreload(GA_Effectalembic)\nGA_Effectalembic.GA_Effectalembic().GA_alembicExr(1,0,"alembic03",1)')
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'导入ABC', bgc=[0, 0, 0.0], borderStyle='in', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=3)
        mc.button(label=u'alembic01',width=120,bgc=[0.13, 0.15, 0.25],
                   command='from idmt.maya.py_common import GA_Effectalembic\nreload(GA_Effectalembic)\nGA_Effectalembic.GA_Effectalembic().GA_alembicImp("alembic01")')
        mc.button(label=u'alembic02',width=120, bgc=[0.13, 0.15, 0.25],
                 command='from idmt.maya.py_common import GA_Effectalembic\nreload(GA_Effectalembic)\nGA_Effectalembic.GA_Effectalembic().GA_alembicImp("alembic02")')

        mc.button(label=u'alembic03', width=120,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GA_Effectalembic\nreload(GA_Effectalembic)\nGA_Effectalembic.GA_Effectalembic().GA_alembicImp("alembic03")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=2)

        mc.intSliderGrp('offset',width=200,label='offset', field=True, minValue=-1000, maxValue=1000, fieldMinValue=-1000, fieldMaxValue=1000, value=0,columnAttach=[(1,'left',10),(2,'left',0),(3,'both',0)],columnWidth3 = (60,60,70))
        mc.button(label=u'set', width=30, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().gdc_clusteroffset(ot=1,sd=0)')



        mc.floatSliderGrp('speed',width=280,label='speed', field=True, minValue=0, maxValue=100, fieldMinValue=0, fieldMaxValue=100, value=1,columnAttach=[(1,'left',10),(2,'left',0),(3,'both',0)],columnWidth3 = (60,60,70))
        mc.button(label=u'set', width=30, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().gdc_clusteroffset(ot=0,sd=1)')


        #  Tab
        mc.tabLayout(tabs, edit=True, tabLabel=((child1, u'植物特效插件')))
        mc.showWindow('ABCEffect')

   #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【选择的物体abc移帧及改变速度】
    #  Author  : 韩虹
    #  Data    : 2015_03
    #------------------------------#  
    def GA_clusteroffset(self,ot=1,sd=1):
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
            mc.error(u'no abc')        
        if abcnodes and  ot==1:
            for abc in abcnodes:
                mc.setAttr((abc+'.offset'),offset) 
        if abcnodes and  sd==1:
            for abc in abcnodes:
                mc.setAttr((abc+'.speed'),speed) 
        return 0

    ############################################################################################################################
    #ABC 导出【通用】【适用于特效ABC导出】
    #@author 韩虹
    #2017/06/12
    ###########################################################################################################################
    def GA_alembicExr(self,server = 1,cachePre = 0,idtype='ABC01',UI=1):
        framemin=''
        framemax=''
        objLists=self.GA_objsList()
        if UI==1:
            framemin=int(mc.intSliderGrp('framemin',q=1,v=1))+int(cachePre)
            framemax=int(mc.intSliderGrp('framemax',q=1,v=1))
        else:
            framemin  =   mc.playbackOptions(min=1,q = 1)
            framemax  =   mc.playbackOptions(max=1,q = 1)
        # 获取alembic临时路径
        localPath = sk_infoConfig.sk_infoConfig().alembicLocalPath(1)
        # 获取alembic服务器端路径
        shotName=sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()+'data/alembic/ef/'+shotName[1]+'/'
        alembicName=shotName[1]+'_'+idtype+'.abc'
        abccommon="-frameRange"+' '+ str(framemin)+' '+str(framemax)+' -uvWrite -worldSpace -writeVisibility '+objLists+' -file'+' '+str(localPath+alembicName)
        mc.select(cl=1)
        mc.AbcExport(j=abccommon)
        if server==1:
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPath+alembicName) + '"' + ' ' + '"' + (serverPath+alembicName) + '"' + ' true'
            mel.eval(updateAnimCMD)
            print u'===[Updating alembic To Server]===传输[%s]完毕==='%alembicName

        return [(localPath+alembicName),(serverPath+alembicName),framemin,framemax]
    ############################################################################################################################
    #ABC 导出【通用】【适用于特效ABC导出】
    #@author 韩虹
    #2017/06/12
    ###########################################################################################################################
    def GA_objsList(self):
        objs=mc.ls(sl=1,l=1,tr=1)
        if not objs:
            mc.error(u'====请选择物体=====')
        objLists=[]
        abcInfo=''
        for obj in objs:
            shapes=mc.listRelatives(obj,s=1,type='mesh',f=1)
            if shapes:
                objLists.append(obj)
        if not objLists:
            mc.error(u'====所选择的物体没有Polygon物体，请检查======')
        for i in range(len(objLists)):
            if i==0:
                abcInfo=' -root '+objLists[0]
            else:
                abcInfo=abcInfo+' -root '+objLists[i]
        return abcInfo
    ############################################################################################################################
    #ABC 导入信息【通用】【适用于特效ABC导出】
    #@author 韩虹
    #2017/06/12
    ###########################################################################################################################
    def GA_infoLists(self):
        objs=mc.ls(sl=1,l=1,tr=1)
        IDList=[]
        infoLists=[]
        objsLists=[]
        ctrls=[]
        if not objs:
            mc.error(u'====请选择物体=====')
        for i in range(len(objs)):
            if '_ctrl' in objs[i] and '|' in objs[i] and len(objs[i].split('|'))>2 and objs[i].split('|')[-3] not in ctrls:
                ctrl=objs[i].split('|')
                ctrlL=''
                for j in range(0,len(ctrl)-2):
                    if j==0:
                        ctrlL=ctrl[0]
                    else:
                        ctrlL=ctrlL+'|'+ctrl[j]
                #print 'AAA'

                #print ctrlL
                ctrls.append(ctrlL)
        if not ctrls:
            mc.error(u'=====所选择的物体非植物库物体,或者植物没在组里，请检查============')
        for j in range(len(ctrls)):
            Lists=[]
            meshs=mc.listRelatives(ctrls[j],ad=1,f=1,type='mesh')
            for k in range(len(meshs)):
                obj=mc.listRelatives(meshs[k],p=1,f=1,type='transform')
                if obj and obj[0] not in Lists:
                    Lists.append(obj[0])
            if Lists:
                ctrlshort=ctrls[j].split('|')[-1]
                if ':' in ctrlshort:
                    ctrlshort=ctrlshort.split(':')[-1]
                IDList.append(ctrlshort.split('_')[0])
                objsLists.append(Lists)
        if not objsLists:
            mc.error(u'请检查所选物体是否为植物库物体')
        infoLists=[IDList, objsLists]
        return  infoLists

    # shotMode 1: 每类植物一个abc;  shotMode 2: 每个植物一个abc
    def GA_infoListsInShot(self,shotMode = 1):
        objs=mc.ls(sl=1,l=1,tr=1)
        IDList=[]
        objsLists=[]
        ctrls=[]
        if not objs:
            mc.error(u'====请选择物体=====')
        for i in range(len(objs)):
            if '_ctrl' in objs[i] and len(objs[i].split('|'))>2 :
                ctrls.append(objs[i])
        if not ctrls:
            mc.error(u'=====所选择的物体非植物库物体，请检查============')
        for j in range(len(ctrls)):
            meshes = mc.listRelatives(ctrls[j],ad=1,f=1,type='mesh')
            if not meshes:
                continue
            meshObjs = mc.listRelatives(meshes,p=1,f=1,type = 'transform')
            meshObjs = list(set(meshObjs))
            # 判断id
            ctrlshort = ctrls[j].split('|')[-1]
            print '----y'
            print ctrlshort
            if ':' in ctrlshort:
                needID = ctrlshort.split(':')[-1].split('_')[0]
            else:
                needID = ctrlshort.split('_')[0]
            IDList.append(needID)
            objsLists.append(meshObjs)
        if not objsLists:
            mc.error(u'请检查所选物体是否为植物库物体')
        # 每类一个abc
        if shotMode in [1]:
            tempIDList = []
            tempObjList = []
            for num in range(len(IDList)):
                checkID = IDList[num]
                objList =  objsLists[num]
                if checkID not in tempIDList:
                    tempIDList.append(checkID)
                    tempObjList.append(objList)
                else:
                    checkIndex = tempIDList.index(checkID)
                    tempObjList[checkIndex] += objList
            IDList = tempIDList
            objsLists = tempObjList

        infoLists=[IDList, objsLists]
        return  infoLists

    ############################################################################################################################
    #ABC 导入ABCCACHE【适用于前期】
    #@author 韩虹
    #2017/06/13
    ###########################################################################################################################
    # shotMode 1: 每类植物一个abc;  shotMode 2: 每个植物一个abc
    def GA_alembicImp(self,idtype='alembic01',shotMode = 1):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        #服务器路径
        FserverPath=sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        # 获取alembic服务器端路径
        serverPath = FserverPath+'data/alembic/ef/'
        objs=mc.ls(sl=1,l=1,tr=1)
        if shotMode in [0]:
            infoList=self.GA_infoLists()
        if shotMode in [1,2]:
            # 极大优化获取算法，减少运算并提速
            infoList = self.GA_infoListsInShot(shotMode)
        print shotMode
        for i in range(len(infoList[0])):
            id=infoList[0][i]
            abcinfo=infoList[1][i]
            AlembicName=id+'_'+idtype+'_AlembicNode'
            alebicName=id+'_'+idtype+'.abc'
            alebicPath=serverPath+id+'/'
            roosold =  mc.ls(assemblies=True,l=1)
            if os.path.exists(alebicPath+alebicName)==False:
                if shotMode in [0]:
                    mc.error(u' 缺少【%s】缓存，请检查'%(alebicPath+alebicName))
                if shotMode in [1,2]:
                    continue
            mc.select(cl=1)
            mc.AbcImport((alebicPath+alebicName),mode='import')
            roosnew = mc.ls(assemblies=True,l=1)
            abcObjs=[]
            for obj in roosnew:
                if obj not in roosold:
                    abcObjs.append(obj)
            if not abcObjs:
                mc.error(u'【%s】 ABC缓存导入失败，或缓存为空，请检查'%(alebicPath+alebicName))
            shape = mc.listRelatives(abcObjs[0],s=1,type='mesh',f=1)
            if not shape:
                mc.error(u'导入的ABC缓存有问题，请检查【%s】'%(alebicPath+alebicName))
            abc = mc.listConnections((shape[0]+'.inMesh'),s=1,type='AlembicNode')
            abcInfos = []
            objInfos = []
            if shotMode in [0]:
                for j in range(len(abcinfo)):
                    for k in range(len(abcObjs)):
                        meshInfo=mc.listRelatives(abcinfo[j],s=1,type='mesh',f=1)
                        mesh=mc.listRelatives(abcObjs[k],s=1,type='mesh',f=1)
                        abcOut=mc.listConnections((mesh[0]+'.inMesh'),s=1,p=1,type='AlembicNode')
                        abcObjShort=abcObjs[k].split('|')[-1]
                        abcinfoShort=abcinfo[j].split('|')[-1]
                        if abcObjShort==abcinfoShort:
                            abcInfos.append(abcOut[0])
                            objInfos.append(meshInfo[0])
                print '---------shotMode:%s'%shotMode
                print abcInfos
                print objInfos
                if not abcInfos:
                    mc.error(u'ABC缓存与目前所选择的模型不相符，请检查【%s】'%(alebicPath+alebicName))
                for m in range(len(abcInfos)):
                    if mc.listConnections(objInfos[m]+'.inMesh'):
                        cons=mc.listConnections((objInfos[m]+'.inMesh'),c=1,p=1)
                        try:
                            mc.disconnectAttr(cons[1] ,cons[0])
                        except:
                            pass
                    try:
                        mc.connectAttr(abcInfos[m],(objInfos[m]+'.inMesh'),f=1)
                    except:
                        mc.error(u'【%s】没有正确连接到【%s】' %abcInfos[m] %objInfos[m])
            if shotMode in [1,2]:
                errorObjs = []
                cacheWrongObjs = []
                print '---------shotMode:%s'%shotMode
                for num in range(len(abcinfo)):
                    targetObj = abcinfo[num]
                    print targetObj
                    if ':' in targetObj:
                        needSourceObj = '|%s'%(targetObj.split(':')[-1])
                    else:
                        needSourceObj = '|%s'%(targetObj.split('|')[-1])
                    if needSourceObj not in abcObjs:
                        continue
                    targetMesh = mc.listRelatives(targetObj,s=1,ni=1,f=1)[0]
                    targetAttr = targetMesh+'.inMesh'
                    # 断开连接检测
                    consNow = mc.listConnections(targetAttr,s=1,plugs=1)
                    if consNow:
                        mc.disconnectAttr(consNow[0],targetAttr)
                    consNow = mc.listConnections(targetAttr,s=1,plugs=1)
                    if consNow:
                        errorObjs.append(targetObj)
                        continue
                    # 连接
                    needSourceMesh = mc.listRelatives(needSourceObj,s=1,ni=1,type = 'mesh',f=1)
                    if not needSourceMesh:
                        cacheWrongObjs.append(targetObj)
                    else:
                        needSourceMesh = needSourceMesh[0]
                        consS = mc.listConnections(needSourceMesh+'.inMesh',s=1,plugs=1)
                        if not consS:
                            continue
                        consS = consS[0]
                        mc.connectAttr(consS,targetAttr)
                if cacheWrongObjs or errorObjs:
                    if cacheWrongObjs:
                        print '\n---------Source Cache Error:'
                        for obj in cacheWrongObjs:
                            print obj
                        print '-----Please fix source cache obj\n'
                    if errorObjs:
                        print '\n---------Target Obj Error:'
                        for obj in errorObjs:
                            print obj
                        print '-----Please fix target obj\n'

            mc.delete(abcObjs)
            print u'=====已导入ABC缓存，请检查文件====='
        return 0
    #-------------------------------------#
    # sd文件一次性导入
    #-------------------------------------#
    def shotSdAbcImport(self):
        objs = mc.ls(sl=1,l=1)
        mc.select(cl=1)
        for i in range(3):
            mc.select(objs)
            self.GA_alembicImp(idtype='alembic0%s'%(i+1),shotMode = 1)
        mc.select(cl=1)

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
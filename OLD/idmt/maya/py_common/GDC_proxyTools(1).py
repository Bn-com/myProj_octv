# -*- coding: utf-8 -*-

'''
Created on 2014

GDC 检测上传工具【通用】

@author: hanhong
'''

import maya.cmds as mc
import maya.mel as mel

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)


import idmt.pipeline.db
import os
import idmt.pipeline.service

from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)

from idmt.maya.py_common import GDC_TransInfoProce

reload(GDC_TransInfoProce)


from idmt.maya.py_common import GDC_checkin
reload(GDC_checkin)

#GPUCache上传
#@author: 韩虹
#Data：2015/9/16
#up:2015/5/3
#----------------------------------------------------------------------------------------------------------#
class GDC_proxyTools(object):
    def __init__(self):
        pass
#----------------------------------------------------------------------------------------------------------#
#【通用】代理类型判断
#@author:韩虹
#data：2017-5-3
    #---------------------------------------------------
    def gdc_proxyType(self):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        proxytype=''
        if shotInfo[0] in ['nj']:
            proxytype='vray01'
        if shotInfo[0] in ['csl','mtd']:
            proxytype='arnold01'
        if shotInfo[0] in ['Yak']:
            proxytype='arnold02'
        if shotInfo[0] in ['do6']:
            proxytype='arnold03'
        return proxytype
#----------------------------------------------------------------------------------------------------------#
#【通用】前期文件路径，本机路径，渲染代理路径
#@author:韩虹
#data：2016-6-16
    #---------------------------------------------------
    def gdc_proxyPath(self):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileName=mc.file(q=1,sn=1,shn=1)
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if shotInfo[0]=='nj':
            proxypath=serverPath+'data/proxy/NJ2017/'
        else:
            proxypath=serverPath+'data/proxy/'+shotInfo[1]+'/'
        shotInfos= sk_infoConfig.sk_infoConfig().checkShotInfo()
        chatype=''
        line=''
        if 'c' in shotInfos[1][0]:
            chatype='characters'
        if 'p' in shotInfos[1][0]:
            chatype='props'
        if 's' in shotInfos[1][0]:
            chatype='sets'
        if '.' in shotInfo[-1] and shotInfo[-1].split('.')[0]=='rg':
            line='rigging'
        if '.' in shotInfo[-1] and shotInfo[-1].split('.')[0]=='tx':
            line='texture'
        if shotInfo[3]=='ms':
            line='master'
        asset = idmt.pipeline.db.GetAssetByFilename(fileName)
        if shotInfo[0] in ['nj']:
            EP=asset.code
            serverimagepath= serverPath+'scenes/'+chatype+'/'+EP+'/'+shotInfos[1]+'/'+line+'/'
        else:
            serverimagepath= serverPath+'scenes/'+chatype+'/'+shotInfos[1]+'/'
        temimagepath='D:/Info_Temp/proxy/' + str(shotInfos[1]) + '/'
        mc.sysFile(temimagepath, makeDir=True)
        texpath=[temimagepath,serverimagepath,proxypath]
        return texpath
#----------------------------------------------------------------------------------------------------------#
#【通用】高模 ，低模，渲染代理物体
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyMeshInfo(self):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        meshsH=[]
        meshsL=[]
        meshsP=[]
        ctrlH=shotInfo[1]+'_h_ctrl'
        ctrlL=shotInfo[1]+'_l_ctrl'
        ctrlP=shotInfo[1]+'_proxy'
        meshs=mc.ls(type='mesh',l=1)
        if meshs:
            for mesh in meshs:
                obj=mc.listRelatives(mesh,p=1,type='transform',f=1)
                if obj and ctrlH in obj[0]:
                    meshsH.append(obj[0])
                if obj and ctrlL in obj[0]:
                    meshsL.append(obj[0])
                if obj and ctrlP in obj[0]:
                    meshsP.append(obj[0])
        return [meshsH,meshsL,meshsP]
#----------------------------------------------------------------------------------------------------------#
#【通用】高模 ，低模，渲染代理结构信息
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyGeoInfo(self,typ='p'):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        ctrl=shotInfo[1]+'_'+typ+'_ctrl'
        grp=shotInfo[1]+'_'+typ+'_grp'
        pre=shotInfo[1]+'_'+typ+'_'
        return [ctrl,grp,pre]
#----------------------------------------------------------------------------------------------------------#
#【Vray项目】高模 ，低模，渲染代理结构信息
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def vray_proxyCreatCheckin(self,server=1):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        servpath=sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        fileName=mc.file(q=1,sn=1,shn=1)
        path=self.gdc_proxyPath()
        tempath=path[0]
        serverpath=path[1]
        proxypath=path[2]
        proxyInfo=self.gdc_proxyInfo()
        #Vray 渲染器项目
        vrmesh=shotInfo[1]+'.vrmesh'
        if os.path.exists(proxypath+vrmesh):
            mc.sysFile(proxypath+'/his', makeDir=True)
            mc.sysFile(proxypath+vrmesh, move=proxypath+'/his/'+vrmesh)
        proxyName=shotInfo[1]+'_proxy'
        modelH=shotInfo[0]+'_'+shotInfo[1]+'_h_rg.mb'
        modelL=shotInfo[0]+'_'+shotInfo[1]+'_l_rg.mb'
        modelP=shotInfo[0]+'_'+shotInfo[1]+'_p_rg.mb'
        if shotInfo[0]=='nj' and proxyInfo==1 and shotInfo[2]=='h' and shotInfo[3]=='rg.mb' and os.path.exists(serverpath+modelL):
            mc.file((serverpath+modelL),i=1)
        if shotInfo[0]=='nj' and proxyInfo==1 and shotInfo[2]=='l' and shotInfo[3]=='rg.mb' and os.path.exists(serverpath+modelH):
            mc.file((serverpath+modelH),i=1)
        meshs=self.proxyMeshInfo()
        meshsH=meshs[0]
        meshsL=meshs[1]
        if meshsH and meshsL:
            mc.select(cl=1)
            mc.select(meshsH)
            mc.select(meshsL,add=1)
            cmdPath='vray setConfValue "proxyPath" '+ '"'+ proxypath+'"'
            cmdExport='vray setConfValue "proxyExportType" 1'
            cmdanm='vray setConfValue "proxyAnimOn" 0'
            cmdOver='vray setConfValue "proxyOverwriteExisting" 1'
            cmdLast='vray setConfValue "proxyLastSelectedAsPreview" 1'
            cmdPreview='vray setConfValue "proxyPreviewType" "combined"'
            cmdVertexcolor='vray setConfValue "proxyVertexColorsOn" 0'
            cmdnodeName='textFieldGrp -e -text ' +'"'+proxyName+'" vraycpNewNodeNameCtrl'
            cmdFileName='textFieldGrp -e -text ' +'"'+vrmesh+'" vraycpFileNameCtrl'
            mel.eval(cmdPath)
            mel.eval(cmdExport)
            mel.eval(cmdOver)
            mel.eval(cmdLast)
            mel.eval(cmdPreview)
            mel.eval(cmdVertexcolor)
            mel.eval('vrayCreateCreateProxyWindow()')
            mel.eval(cmdnodeName)
            mel.eval(cmdFileName)
            mc.checkBoxGrp('vraycpAutoCreateCtrl',e=1,v1=1)
            mel.eval('vrayCreateProxyButtonPressed()')
            meshs=self.proxyMeshInfo()
            meshsP=meshs[2]
            proxygeo=self.proxyGeoInfo('p')
            logeo=self.proxyGeoInfo('l')
            ctrll=logeo[0]
            grpl=logeo[1]
            ctrlp=proxygeo[0]
            grpp=proxygeo[1]
            prep=proxygeo[2]
            proxyfinal=prep+'mesh_'
            if mc.objExists(ctrlp):
                mc.delete(ctrlp)
            if mc.objExists(ctrll):
                mc.rename(ctrll,ctrlp)
            if mc.ls(meshsP)==[]:
                mc.error(u'========未生成代理文件，请检查===========')
            if len(meshsP)>1:
                mc.error(u'==========不止一个代理文件，请检查===========')
            if mc.objExists(grpl):
                mc.delete(grpl)
            mc.rename(meshsP[0], proxyfinal)
            mc.group(proxyfinal, n=grpp)
            proxLight=self.proxyLightInfo()
            checklight=proxLight[0]
            treelights=proxLight[1]
            if checklight==1:
                for light in treelights:
                    if (shotInfo[1]+'_h') in light and (shotInfo[1]+'_p') not in light:
                        lightn=light.split('|')[-1].replace((shotInfo[1]+'_h'),(shotInfo[1]+'_p'))
                        lightn=mc.rename(light.split('|')[-1],lightn)
                        mc.parent(lightn,grpp)
            mc.parent(grpp,ctrlp)
            mc.select(ctrlp)
            mc.file((tempath+modelP),options='v=0',f=1,type='mayaBinary',preserveReferences=1,es=1)
            print '==============================='
            print u'==============渲染代理已生成==========='
            print tempath+modelP
            print '==============================='
            if server==1:
                userName = os.environ['USERNAME']
                mc.file((tempath+modelP),options='v=0',type='mayaBinary',f=1,o=1)
                projectInfo = 'Ninjago'
                fileName=mc.file(q=1,sn=1,shn=1)
                fileInfo='1|' + projectInfo + '|' + fileName + '|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'渲染代理'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传渲染代理文件' % fileName))
        else:
            mc.warning(u'===============文件结构不正确请检查===========')
            mc.error(u'===============文件结构不正确请检查===========')
        return 0

#----------------------------------------------------------------------------------------------------------#
#【通用】适用于arnold渲染器，渲染代理创建
#@author:韩虹
#data：2016-6-17
# low=1 针对需要低模的项目，low=0 针对不需要低模的项目
    #---------------------------------------------------
    def gdc_ArnoldProxyCreat(self,meshH,meshL,low):
        path=self.gdc_proxyPath()
        tempath=path[0]
        serverpath=path[1]
        proxypath=path[2]
        import mtoa.core
        #高模连接SG节点
        shape=mc.listRelatives(meshH[0].split('|')[-1],s=1,f=1,type='mesh')
        if not shape:
            pass
        SG=mc.listConnections(shape[0],s=1,p=0,c=0,type='shadingEngine')
        if not SG:
            pass
        meshp=''
        if low!=0:
            meshlshot=meshL.split('|')[-1]
            meshp=meshlshot.replace('_l_','_p_')
        else:
            meshlshot=meshH[0].split('|')[-1]
            meshp=meshlshot.replace('_l_','_h_')
        ass=meshp+'.ass'
        asstoc=meshp+'.asstoc'
        ArnoldName=meshp+'ArnoldStandIn_'
        #记录BBX属性
        bbxInfos=self.GA_BBXinfo(shape[0])
        #导出代理
        # mc.select(meshH[0].split('|')[-1])
        mc.select(meshH, r = True)
        mc.file((tempath+ass),options="-asciiAss;-mask 8;-lightLinks 0;-boundingBox;-shadowLinks 0",f=1,type="ASS Export",preserveReferences=1,es=1)

        mel.eval('source \"zwSysFile\"')
        mel.eval('zwSysFile "copy" \"' + (tempath+ass) + '\" \"' + (proxypath+ass) + '\" 1')
        mel.eval('zwSysFile "copy" \"' + (tempath+asstoc) + '\" \"' + (proxypath+asstoc) + '\" 1')
        #创建代
        standInNode = mtoa.core.createStandIn(path=(proxypath+ass))
        Arnold= standInNode if isinstance(standInNode, unicode) else standInNode.name() #mtoa.core.createStandIn(path=(proxypath+ass)).name()
        #添加arnold 代理不加载（文件打开时不读取，渲染时会自动读取，沈康提醒）
        mc.setAttr(('%s.%s') % (Arnold,'standInDrawOverride'),4)
        #恢复渲染代理BBX值
        print u'bbx值为：'
        print bbxInfos
        if bbxInfos:
            for i in range(3):
                mc.setAttr(Arnold+'.MinBoundingBox'+str(i),bbxInfos[0][i])
                mc.setAttr(Arnold+'.MaxBoundingBox'+str(i),bbxInfos[1][i])
        ArnTR=mc.listRelatives(Arnold,p=1,f=1)
        ArnoldName=mc.rename(ArnTR[0],ArnoldName)
        mc.select(ArnoldName)
        mc.sets(ArnoldName,e = 1 , forceElement = SG[0])
        proxygeo=self.proxyGeoInfo('p')
        ctrlp=proxygeo[0]
        grpp=proxygeo[1]
        if low!=0:
            geol=self.proxyGeoInfo('l')
            ctrll=geol[0]
            grpl=geol[1]
            meshp=mc.rename(meshlshot,meshp)
            meshpShape=mc.listRelatives(meshp,s=1,f=1,type='mesh')
            Attr=['castsShadows','receiveShadows','motionBlur','primaryVisibility','smoothShading','visibleInReflections','visibleInRefractions','aiSelfShadows','aiOpaque',
            'aiVisibleInDiffuse','aiVisibleInGlossy','aiVisibleInDiffuseReflection', 'aiVisibleInSpecularReflection', 'aiVisibleInDiffuseTransmission', 'aiVisibleInSpecularTransmission', 'aiVisibleInVolume']
            if meshpShape:
                for Att in Attr:
                    try:
                        mc.setAttr((meshpShape[0]+'.'+Att),0)
                    except:
                        pass
            mc.parent(ArnoldName,meshp)
            if not mc.ls(ctrlp) and not mc.ls(grpp):
                mc.select(meshp)
                mc.rename(ctrll,ctrlp)
                mc.rename(grpl,grpp)
                #self.proxyCreatGeoAuto()
            else:
                try:
                    mc.parent(meshp,grpp)
                except:
                    print meshp
                    pass
        else:
            geol=self.proxyGeoInfo('h')
            ctrlh=geol[0]
            grph=geol[1]
            for mesh in meshH:
                try:
                    mc.parent(mesh.split('|')[-1],w=1)
                except:
                    pass
            if not mc.ls(ctrlp) and not mc.ls(grpp):
                mc.rename(ctrlh,ctrlp)
                mc.rename(grph,grpp)
            try:
                mc.parent(ArnoldName,grpp)
            except:
                print ArnoldName
                pass
        return 0
#----------------------------------------------------------------------------------------------------------#
#【Arnold项目】高模 ，低模，渲染代理结构信息
#@author:韩虹
#data：2016-6-17
# low=1 针对需要低模的项目，low=0 针对不需要低模的项目
    #---------------------------------------------------
    def arnold_proxyCreatCheckin(self,server=1,low=0):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        servpath=sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        fileNameH=mc.file(q=1,sn=1,shn=1)
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        path=self.gdc_proxyPath()
        fileType=shotInfo[len(shotInfo)-1].split('.')[1]
        proxytype=self.gdc_proxyType()
        if fileType=='mb':
            fileTypeAll='mayaBinary'
        if fileType=='ma':
            fileTypeAll='mayaAscii'
        tempath=path[0]
        serverpath=path[1]
        proxypath=path[2]
        proxyInfo=self.gdc_proxyInfo()
        #Arnold 渲染器项目
        ass=shotInfo[1]+'.ass'
        asstoc=shotInfo[1]+'.asstoc'
        if os.path.exists(proxypath+ass):
            mc.sysFile(proxypath+'/his', makeDir=True)
            mc.sysFile(proxypath+ass, move=proxypath+'/his/'+ass)
            mc.sysFile(proxypath+asstoc, move=proxypath+'/his/'+asstoc)
        mc.file(rename=(tempath+fileNameH))
        mc.file(save=1,type ='mayaBinary',f = 1)
        proxyName=shotInfo[1]+'_proxy'
        modelH=shotInfo[0]+'_'+shotInfo[1]+'_h_rg.mb'
        modelL=shotInfo[0]+'_'+shotInfo[1]+'_l_rg.mb'
        if proxytype !='arnold02':
            modelP=shotInfo[0]+'_'+shotInfo[1]+'_p_rg.mb'
        else:
            modelP=shotInfo[0]+'_'+shotInfo[1]+'_p_tx.mb'
        if low!=0:
            if proxyInfo==1 and shotInfo[2]=='h' and shotInfo[3]=='rg.mb' and os.path.exists(serverpath+'/rigging/'+modelL):
                mc.file((serverpath+'/rigging/'+modelL),i=1)
            if proxyInfo==1 and shotInfo[2]=='l' and shotInfo[3]=='rg.mb' and os.path.exists(serverpath+'/rigging/'+modelH):
                mc.file((serverpath+'/rigging/'+modelH),i=1)
        meshs=self.proxyMeshInfo()
        
        mc.file(rename=(tempath+modelP))
        mc.file(save=1,type ='mayaBinary',f = 1)
        meshsH=meshs[0]
        meshsL=meshs[1]
        if not meshsH:
            mc.error(u'缺少高模物体，请检查高模文件')
        if not meshsL and low!=0:
            mc.error(u'缺少低模物体，请检查低模文件')
        proxyAttr=['proxy01','proxy02','proxy03','proxy04']
        proxyH=[[],[],[],[]]
        proxyL=[[],[],[],[]]
        for i in range(len(proxyAttr)):
            for mesh in meshsH:
                if mc.objExists(mesh+'.'+proxyAttr[i]):
                    proxyH[i].append(mesh)
            for mesl in meshsL:
                if mc.objExists(mesl+'.'+proxyAttr[i]):
                    proxyL[i].append(mesl)
        if  proxyH==[[],[],[],[]] and proxyL==[[],[],[],[]] and low==1 and len(meshsL)<2 :
            self.gdc_ArnoldProxyCreat(meshsH,meshsL[0],low=1)
        if proxyH== [[],[],[],[]]  and low==0:
            for i in range(len(meshsH)):
                self.gdc_ArnoldProxyCreat([meshsH[i]],meshsL,low=0)
        if proxyH==[[],[],[],[]] and len(meshsL)>1 and low!=0:
            mc.error(u'高模没有加代理属性，而且低模不止一个模型')
        if proxyL==[[],[],[],[]] and len(meshsL)>1 and low!=0:
            mc.error(u'低模没有加代理属性，而且低模不止一个模型')
        if proxyH!=[[],[],[],[]] and proxyL!=[[],[],[],[]] and low!=0:
            if GDC_checkin.GDC_checkin().checkInfo() != 0:
                for i in range(len(proxyL)):
                    if proxyL[i] !=[] and proxyH[i] !=[] and len(proxyL[i])==1:
                        self.gdc_ArnoldProxyCreat(proxyH[i],proxyL[i][0],low)
                    if proxyL[i] !=[] and proxyH[i] !=[] and len(proxyL[i])>1:
                        mc.warning(u'========================不止一个低模有【%s】属性========================'%proxyAttr[i])
                        print proxyL[i]
                        mc.error(u'========================不止一个低模有【%s】属性========================'%proxyAttr[i])
                    if proxyL[i] !=[] and proxyH[i] ==[]:
                        mc.warning(u'========================低模有【%s】属性，相应高模无此属性，请检查文件========================'%proxyAttr[i])
                        print proxyL[i]
                        mc.error(u'========================低模有【%s】属性，相应高模无此属性，请检查文件========================'%proxyAttr[i])
                    if proxyH[i] !=[] and proxyL[i] ==[]:
                        mc.warning(u'========================高模有【%s】属性，相应低模无此属性，请检查文件========================'%proxyAttr[i])
                        print proxyH[i]
                        mc.error(u'========================高模有【%s】属性，相应应低模无此属性，请检查文件========================'%proxyAttr[i])
        proxymeshs=[]
        for i in range(len(proxyH)):
            if  proxyH[i]:
                for j in  range(len(proxyH[i])):
                    if proxyH[i][j] !='' and proxyH[i][j] not in proxymeshs:
                        proxymeshs.append(proxyH[i][j])
        if proxyH!= [[],[],[],[]] and low==0 and len(proxymeshs)==len(meshsH):
            for i in range(len(proxyH)):
                if proxyH[i]!=[] and proxyH[i][0]!='':
                    self.gdc_ArnoldProxyCreat(proxyH[i],proxyL[i],low=0)
        if proxyH!= [[],[],[],[]] and low==0 and len(proxymeshs)<len(meshsH):
            meshns=[]
            for k in range(len(meshsH)):
                if meshsH[k] not in proxymeshs and meshsH[k] not in meshns:
                    meshns.append(meshsH[k])
            if meshns:
                for meshn in meshns:
                    self.gdc_ArnoldProxyCreat([meshn],meshsL,low=0)

            for i in range(len(proxyH)):
                if proxyH[i]!=[] and proxyH[i][0]!='':
                    self.gdc_ArnoldProxyCreat(proxyH[i],proxyL[i],low=0)
        proxygeo=self.proxyGeoInfo('p')
        ctrlp=proxygeo[0]
        if mc.ls(ctrlp):
            mc.select(ctrlp)
            mc.file((tempath+modelP),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            print (tempath+modelP)
        else:
            mc.warning(u'渲染代理创建失败，请检查文件')
            mc.error(u'渲染代理创建失败，请检查文件')


        if server==1:
            userName = os.environ['USERNAME']
            mc.file((tempath+modelP),options='v=0',type=fileTypeAll,f=1,o=1)
            fileName=mc.file(q=1,sn=1,shn=1)
            fileInfo='1|' + projectInfo + '|' + fileName + '|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            mel.eval(checkOutCmd)
            description = u'渲染代理'
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传渲染代理文件' %fileName))
        if proxytype =='arnold02' or proxytype =='arnold03':
            mc.file((tempath+fileNameH),options='v=0',type='mayaBinary',f=1,o=1)
        return 0

#----------------------------------------------------------------------------------------------------------#
#【nj2017】自动渲染代理
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyCreatCheckinF(self,proxytype='vray01',server=1):
        

        fileName=mc.file(q=1,sn=1,shn=1)
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        proxyInfo=self.gdc_proxyInfo()
        servpath=sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        path=self.gdc_proxyPath()
        tempath=path[0]
        serverpath=path[1]
        proxypath=path[2]
        #proxytype=self.gdc_proxyType()
        modelH=shotInfo[0]+'_'+shotInfo[1]+'_h_rg.mb'
        modelL=shotInfo[0]+'_'+shotInfo[1]+'_l_rg.mb'
        modelP=shotInfo[0]+'_'+shotInfo[1]+'_p_rg.mb'
        check=0
        if shotInfo[0] not in ['Yak']:
            serverpath=serverpath+'/rigging/'
        if proxyInfo==1 and shotInfo[2]=='h' and shotInfo[3]=='rg.mb' and os.path.exists(serverpath+modelL):
            check=1
        if proxyInfo==1 and shotInfo[2]=='l' and shotInfo[3]=='rg.mb' and os.path.exists(serverpath+modelH):
            check=1
        if check==1:
            mc.file(rename=(tempath+fileName))
            mc.file(save=1,type = 'mayaBinary',f = 1)
            if proxytype =='vray01': # proxyInfo?
                self.vray_proxyCreatCheckin(server)
            if proxytype =='arnold01': # proxyInfo?
                self.arnold_proxyCreatCheckin(server,low=1)
            mc.file((tempath+fileName),options='v=0',type='mayaBinary',f=1,o=1)
        if check==0:
            pass
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】自动创建代理结构
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyCreatGeo(self,typ='h'):
        GeoInfo=self.proxyGeoInfo(typ)
        objs=mc.ls(sl=1,tr=1,l=1)
        ctrl=GeoInfo[0]
        grp=GeoInfo[1]
        pre=GeoInfo[2]
        if not objs:
            mc.error(u'=====未选择模型，请选择=====')
        #打组
        if mc.objExists(grp)==False and mc.objExists(ctrl)==False:
            mc.group(objs, n=grp)
            #重命名
            self.proxyRenameProxy()
            #创建ctrl
            mc.circle(c=(0,0,0),nr=(0,1,0),n=ctrl)
            mc.setAttr((ctrl+'.scaleX'),10)
            mc.setAttr((ctrl+'.scaleY'),10)
            mc.setAttr((ctrl+'.scaleZ'),10)
            mc.select(ctrl)
            mc.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            mc.parent(grp,ctrl)
        else:
            mc.parent(objs,grp)
            self.proxyRenameProxy()
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】自动创建代理结构(根据文件名判断）
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyCreatGeoAuto(self):
        proxyInfo=self.gdc_proxyInfo()
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfo[2]  in ['h','l','p'] and  proxyInfo==1:
            self.proxyCreatGeo(shotInfo[2])
        else:
            mc.error(u'===========请检查文件名,该文件不是渲染代理编号文件============')
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】自动重命名工具（渲染代理文件）
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyRenameProxy(self):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        proxyInfo=self.gdc_proxyInfo()
        GeoInfo=self.proxyGeoInfo(shotInfo[2])
        if shotInfo[2] not in ['h','l','p'] or proxyInfo!=1:
            mc.error(u'========请检查文件名,该文件不是渲染代理编号文件==============')
        objs=mc.ls(sl=1,tr=1,l=1)
        pre=GeoInfo[2]
        if objs:
            for obj in objs:
                chrs=mc.listRelatives(obj, c=1, type='transform', ad=1, f=1)
                objShort=obj.split('|')[-1]
                if pre not in objShort:
                    objPre=obj.split(objShort)[0]
                    objN=pre+objShort
                    mc.rename(objShort,objN)
                if chrs:
                    for chr in chrs:
                        chrShort=chr.split('|')[-1]
                        if pre not in chrShort:
                            chrN=pre+chrShort
                            mc.rename(chrShort,chrN)
        else:
            print(u'============Please Select==============')
            mc.error(u'============Please Select==============')
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】代理灯光信息
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyLightInfo(self):
        objs=mc.ls(tr=1,l=1)
        trees=[]
        lightcheck=0
        for obj in objs:
            if mc.objExists(obj+'.tree') and mc.listRelatives(obj,s=1,f=1) and mc.nodeType(mc.listRelatives(obj,s=1,f=1)[0])=='VRayLightSphereShape'  :
                trees.append(obj)
        if trees:
            lightcheck=1
        return [lightcheck,trees]
#【通用】缺失贴图检测
#@author:韩虹
#data：2016-6-28
    #---------------------------------------------------
    def FileMapCheck(self):
        files=mc.ls(type='file',l=1)
        fileMapN=[]
        if files:
            for fil in files:
                if mc.objExists(fil+'.fileTextureName'):
                    maps=mc.getAttr(fil+'.fileTextureName')
                    if not maps or os.path.isfile(maps)==False:
                        fileMapN.append(fil)
        if fileMapN:
            for fi in fileMapN:
                mc.warning(u'==========【%s】缺失贴图========='%fi)
            mc.error(u'==========文件中有缺失贴图，请查看警告信息=================')
        return 0
#----------------------------------------------------------------------------------------------------------#
#【NJ2017】渲染代理判断
#@author:韩虹
#data：2016-6-15
#---------------------------------------------------
    def gdc_proxyInfo(self,projStyle = 0):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfo[0] in ['nj']:
            path='Z:\Projects\Ninjago\Project\data\proxy\NJ2017\proxyID.txt'
            proxyID=self.checkFileRead(path)
        elif shotInfo[0] in ['csl']:
            otherID=['p000017zhiwu']
            proxyID=self.csl_proxyIDSQL()
            proxyID=proxyID+otherID
        elif shotInfo[0] in ['Yak']:
            s = idmt.pipeline.service.Service()
            proxyID=s.GetAssetsByCaption(projectName = "TheAdventuresOfYak", FullPath = r"props\PlantBank")
        elif shotInfo[0] in ['mtd']:
            s = idmt.pipeline.service.Service()
            proxyID=s.GetAssetsByCaption(projectName = "ManTou", FullPath = r"props\test\plant")
        else:
            proxyID=self.GDC_proxyIDSQL(projStyle = projStyle)
        if shotInfo[1] in proxyID:
            proxyInfo=1
        else:
            proxyInfo=0
        return proxyInfo

#【顺溜】渲染代理ID
#@author:韩虹
#data：2016-10-20
    def csl_proxyIDSQL(self):
        import pyodbc
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=idmt-engine08;DATABASE=idmtPlex_%s;UID=EReader;PWD=123123'%('Shunliu'))

        cursor = cnxn.cursor()
        cmd_sql = "SELECT TB_Asset.asset_name FROM TB_Asset INNER JOIN TB_AssetMap ON TB_Asset.map_id = TB_AssetMap.ID WHERE TB_AssetMap.Fullpath = \'props\\Shunliu2\\vegetation\' ORDER BY TB_Asset.asset_name"
        data = cursor.execute(cmd_sql).fetchall()
        IDS=[]
        if data:
            for i in range(len(data)):
                if data[i][0] !='':
                    IDS.append(data[i][0])
        return IDS
#【通用】渲染代理ID
#@author:韩虹
#data：2017-05-25
# 该死的华强规则
    def GDC_proxyIDSQL(self,projStyle = 0):
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        printSimp = shotInfo[0]
        if projStyle in [2]:
            printSimp = '%s_%s'%(shotInfo[0],shotInfo[1])
        proj=sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(printSimp)
        s = idmt.pipeline.service.Service()
        IDS=s.GetAssetsByCaption(proj, FullPath = r"props\proxyLibrary")
        return IDS
#【通用】读文件
#@author:沈康
    def checkFileRead(self,path):
        import os
        if not os.path.exists(path):
            print path
            print u'Error:    file do not exist'
            mc.error(u'Error:    file do not exist')
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            #print path
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result
#【通用】写文件
#@author:沈康
    def checkFileWrite(self, path , info , addtion=0):
        print u'>>>>>>[write]'
        print path
        mc.sysFile(os.path.dirname(path), makeDir=True)
        if addtion == 1:
            info = self.checkFileRead(path) + info
        txt = open(path, 'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()
#【通用】记录物体BBX信息
#@author:韩虹
    def GA_BBXinfo(self,mesh):
        if mc.nodeType(mesh)!='mesh':
            mc.error(u'请检查【%s】不是mesh物体'%mesh)
        minB=[]
        maxB=[]
        for i in ['X','Y','Z']:
            attrmin=mesh+'.boundingBoxMin'+i
            attrmax=mesh+'.boundingBoxMax'+i
            if mc.objExists(attrmin) and mc.objExists(attrmax):
                minB.append(mc.getAttr(attrmin))
                maxB.append(mc.getAttr(attrmax))
        result=[]
        if minB and maxB:
            result=[minB,maxB]

        return result


#@author:沈康
#【顺溜】修正代理路径指向
#@author:韩虹
    def csl_proxyPathM(self):
        stand=mc.ls(type='aiStandIn',l=1)
        files=[]
        sts=[]
        if not stand:
            mc.warning(u'文件中没有arnold代理文件')
            pass
        for st in stand:
            fil=mc.getAttr(st+'.dso')
            if fil.split('/')[-2][0]=='s':
                sts.append(st)
            if fil.split('/')[-2][0]=='s' and fil not in files:
                files.append(fil)
        IDS=[]
        FilNs=[]
        if not files:
            mc.warning(u'文件中没有在场景路径中的代理')
            pass
        for fi in files:
            shotf=fi.split('/')[-1]
            if '_' in shotf:
                id=shotf.split('_')[0]
            else:
                id=shotf.split('.')[0]
            pathNew=''
            path01='//file-cluster/gdc/Projects/ShunLiu/Project/data/ArnoldStandIn/'+id+'/'+shotf
            path02='//file-cluster/gdc/Projects/ShunLiu/Project/data/proxy/'+id+'/'+shotf
            if os.path.isfile(path02):
                pathNew=path02
            elif not os.path.isfile(path02) and os.path.isfile(path01):
                pathNew=path01
            else:
                mc.warning(u'缺少渲染代理文件【%s】'%id)
                mc.error(u'缺少渲染代理文件【%s】'%id)
            if pathNew!='':
                IDS.append(id)
                FilNs.append(pathNew)
        if not FilNs:
            mc.warning(u'文件中场景中代理，道具路径中没有')
            pass
        for i in range(len(FilNs)):
            for st in sts:
                fil=mc.getAttr(st+'.dso')
                short=fil.split('/')[-1]
                filN=FilNs[i].split('/')[-1]
                if short==filN:
                    filp=FilNs[i].replace('//file-cluster/gdc/Projects','${IDMT_PROJECTS}')
                    mc.setAttr((st+'.dso'),filp,type = 'string')
                    print u'==============【%s】渲染代理路径已修正==============='%st
        return 0
    def GDC_ArnoldMeshSet(self):
        meshs=mc.ls(type='mesh',l=1)
        infos=['.aiVisibleInDiffuse','.aiVisibleInGlossy']
        if meshs:
            for mesh in meshs:
                for i in range(len(infos)):
                    if mc.objExists(mesh+infos[i]):
                        mc.setAttr((mesh+infos[i]),1)
        return 0
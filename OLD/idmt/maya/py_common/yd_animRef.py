# -*- coding: utf-8 -*-
# 【项目工具】【LSW项目】
#  Author : 韩虹
#  Data   : 2015_10_12
# import sys



# SWL项目替换
# A:_ct_an


import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db
import pymel.core as pm
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)



import xlrd
import os
import re
import idmt
import sys


class yd_animRef(object):
    def __init__(self):
        # namespace清理
        pass
        
    #----------------------------------------------------------------------------------------------#
    def FileSwich(self,path):
        # 修改block文件（参考客户前期文件）
        blockfile=self.RefSwich(path,'yd',0)
        # 修改an文件（参考公司数据库文件）
        animfile=self.RefSwich(path,'yd',1)
        # 打开block文件(输出master动画信息，及asset 信息）
        
        print u'\n'
        print u'=====================【%s】文件开始导出数据!!!====================='%blockfile
        print u'\n'
        mc.file(blockfile,options='v=0',loadReferenceDepth='all',f=1,o=1)
        #输出asset信息
        chrinfo=self.grpInfo('Char',3)
        propinfo=self.grpInfo('Prop',3)
        setinfo=self.grpInfo('Set',3)
        fxinfo=self.grpInfo('FX',3)
        #输出动画信息（三个控制环）
        self.animExr(3)
        print u'\n'
        print u'=====================【%s】文件已导出数据!!!====================='%blockfile
        print u'\n'        
        #打开动画文件（整理组，导入动画信息）
        print u'\n'
        print u'=====================【%s】文件开始导入数据!!!====================='%animfile
        print u'\n' 
        mc.file(animfile,options='v=0',loadReferenceDepth='all',f=1,o=1)
        #整理大组
        self.ReorganizeGrp(3)
        #导入动画
        temp=self.animImp(shotType = 3)
        print u'\n'
        print u'=====================【%s】文件已导入数据!!!====================='%animfile
        print u'\n'      
        #删除所有RefProxy
        mel.eval('source zwRemoveAllProxy') 
        mel.eval('zwRemoveAllProxy()')
        mc.file(force=1, options="v=0" , save=1)
        mc.sysFile(temp, delete=True)
        print u'\n'
        print u'=====================文件已处理完毕!!!====================='
        print u'\n'

    def tes(self,path):
        self.RefSwich(path,'yd',0)
        

    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【SWL】【参考】【替换参考工具】【后台】
    #  Author  : 韩虹
    #  Data    : 2015_10_03
    #pro 是项目简写，如'nj'，type=1，是非简模，type=0，是简模
    #------------------------------#
    def RefSwich(self,path,pro,type=1):
        reload(xlrd)
        Excel='Z:/Projects/YODA/Reference/List/GDC LSW2016 Asset list.xls' 
        shotAllData = xlrd.open_workbook(Excel).sheets()[1]
        shotData_colunm = shotAllData.col_values(1)           
        #path=mc.file(query=1, exn=1)
        #shotname=mc.file(query=1, sn=1,shn=1)
        shotname=path.split('/')[-1]
        if type==1:
            newshortname='yd_'+shotname.split('_')[1]+'_'+shotname.split('_')[2]+'_'+shotname.split('_')[3]+'_an_c001.ma'
        else:
            newshortname=shotname.replace('blocking','block')            
        projctpath=''
        tempath=''
        if pro=='yd':
            projctpath='//file-cluster/gdc/Projects/YODA/Project/Scenes/'
            tempath='D:/Info_Temp/YD/anim/'               
        mc.sysFile(tempath, makeDir=True)
        mc.sysFile(path,copy=(tempath+shotname))
        mc.sysFile((tempath+shotname),rename=(tempath+newshortname))
        newpath=tempath+newshortname
        refpathinfo=self.yd_RefInfoRead(path)        
    #        fp=open((tempath+newshortname),'w')  
        refs=[]
        if refpathinfo:     
            for ref in refpathinfo:
                if '/' in ref and 'release' in ref:
                    refs.append(ref)
        else:
            print u'\n'
            print u'=====================【%s】文件是空，请检查文件!!!====================='%path
            print u'\n'
            mc.error(u'文件为空文件')             
        if refs:
            requires = False
            fi = open(path, "r")
            fo = open(newpath, "w")
            while True:
                line = fi.readline()
                if not line:
                    break
                if not requires:
                    if re.search('^requires ', line) != None:
                        requires = True
                    else:
                        m = re.search(r'\"([^\"]+\.m[ab])\"', line, re.IGNORECASE)
                        if m != None:
                            ref = m.group(1)
                            pathNew = ref
                            link=ref.split('release/')[-1].split('/')[0]
                            id=ref.split('release/')[-1].split('/')[1]            
                #                new=shotAllData.col_values(6)
                            rowNum = 0
                            for info in shotData_colunm:
                                if info == id:
                                    rowNum = shotData_colunm.index(info)
                                if rowNum:
                                    continue
                            shotData = shotAllData.row_values(rowNum)
                            if type==1:
                                idNew=  shotData[6]                           
                                modname=pro+'_'+idNew+'_h_mo.mb'
                                if idNew[0]=='s':                
                                    masname=pro+'_'+idNew+'_h_ms_tex.mb'
                                else:
                                    masname=pro+'_'+idNew+'_h_ms_anim.mb'
                                texname=pro+'_'+idNew+'_h_tx.mb' 
                                texnameL=pro+'_'+idNew+'_l_tx.mb'    
                                modpath=''
                                maspath=''
                                assett = idmt.pipeline.db.GetAssetByFilename(modname)
                                asset=assett.asset_type
                                EP=assett.code
                                if EP:        
                                    modpath=projctpath+asset+'/'+EP+'/'+idNew+'/model/'
                                    maspath=projctpath+asset+'/'+EP+'/'+idNew+'/master/'
                                    texpath=projctpath+asset+'/'+EP+'/'+idNew+'/texture/'
                                else:
                                    modpath=projctpath+asset+'/'+idNew+'/model/'
                                    maspath=projctpath+asset+'/'+idNew+'/master/'
                                    texpath=projctpath+asset+'/'+idNew+'/texture/'
                                if os.path.exists(maspath+masname):
                                    pathNew=maspath+masname                                                                                                            
                                
                                #elif os.path.exists(maspath+masname)==False and os.path.exists(texpath+texname):
                                    #pathNew=texpath+texname 
                                #elif os.path.exists(maspath+masname)==False and os.path.exists(texpath+texname)==False and os.path.exists(texpath+texnameL):
                                    #pathNew=texpath+texnameL                                      
                                #elif os.path.exists(maspath+masname)==False and os.path.exists(texpath+texname)==False and os.path.exists(texpath+texnameL)==False and os.path.exists(modpath+modname):
                                    #pathNew=modpath+modname                      
                                
                                else:
                                    print u'\n'
                                    print u'=====================【%s】缺少数据库mod或master文件或tx文件，请检查文件!!!====================='%idNew
                                    print u'\n'
                                    pathNew=ref
                                    #mc.error(u'=====================【%s】缺少数据库mod或master文件，请检查文件!!!====================='%idNew) 
                            if type==0: 
                                '''
                                pathN= shotData[9].split(' ')[0].replace('\\','/')
                                files=[]

                                if os.path.exists(pathN):
                                    files=mc.getFileList(folder=pathN)  
                                else:
                                    pathNew=ref
                                    print shotn
                                    #mc.error(u'=====================【%s】客户简模未提供!!!====================='%shotn)                                                                  
                                shotn=ref.split('/')[-1].split('_v')[0]
                                sname=''
                                if len(files) == 0:
                                    
                                    print u'\n\n'
                                    print u'=====================【%s】缺少客户简模，请检查，并请联系PA!!!====================='%shotData[6] 
                                    pathNew=ref
                                    print shotn
                                    #mc.error(u'=====================【%s】文件夹为空，请检查，并请联系PA!!!====================='%pathN)                                
                                if len(files) > 1 :
                                    for fi1 in files:
                                        if shotn in fi1:
                                            sname=fi1
                                            break
                                    if sname=='' and '_model_' in shotn:
                                        shotn=shotn.replace('_model_','_layout_')
                                        for fi1 in files:
                                            if shotn in fi1:
                                                sname=fi1
                                                break                               
                                if len(files) ==1 :                                   
                                    pathN=pathN+files[0]+'/'
                                    if os.path.exists(pathN):
                                        filesN=mc.getFileList(folder=pathN)
                                        if filesN:                                                                    
                                            for fi1 in filesN:
                                                if shotn in fi1:
                                                    sname=fi1
                                                    break                                                
                                            if sname==''and '_model_' in shotn:
                                                shotn=shotn.replace('_layout_','_model_')
                                                for fi2 in filesN:
                                                    if shotn in fi2 and '.mb' in fi2:
                                                        sname=fi2
                                                        break
                                            if sname=='' and '_model_' in shotn:
                                                shotn=shotn.replace('_model_','_layout_')
                                                for fi2 in filesN:
                                                    if shotn in fi2 and '.mb' in fi2:
                                                        sname=fi2
                                                        break                                                                                                                                            
                                    else:
                                        print u'\n\n'
                                        mc.error(u'=====================【%s】文件夹为空，请检查，并请联系PA!!!====================='%fileV)              
                                '''
                                #之前是读表的路径，现在根据项目要求，改为固定路径，需要注意，客户发来的简模文件，都需要在这里copy一份  
                                pathN='Z:/Projects/YODA/Reference/Handout/Asset from Wilfilm/Yoda_Proxy/'
                                shotn=ref.split('/')[-1].split('_v')[0]
                                sname=''
                                files=mc.getFileList(folder=pathN) 
                                for fil in files:
                                    if '.mb' in fil and shotn in fil:
                                        sname=fil
                                        break                                   
                                if sname=='' and  '_layout_' in shotn:
                                    shotn=shotn.replace('_layout_','_model_')
                                    for fi2 in files:
                                        if shotn in fi2 and '.mb' in fi2:
                                            sname=fi2
                                            break                                    
                                if sname=='' and  '_model_' in shotn:
                                    shotn=shotn.replace('_model_','_layout_')
                                    for fi2 in files:
                                        if shotn in fi2 and '.ma|.mb' in fi2:
                                            sname=fi2
                                            break                                                                                  
                                                            
                                if sname != '':
                                    pathNew= pathN+sname 
                                else:
                                     pathNew= ref 
                                     mc.warning(u'===============缺少【%s】简模==============='%shotn)                                                                                                                                                                                                                                                                                                
                            line = line.replace(ref, pathNew)                                                                                  
                fo.write(line)
            fi.close()
            fo.close()
            print u'\n'
            print u'=====================【%s】文件已创建!!!====================='%newpath
            print u'\n'
            return   newpath             
            
                        
    '''
    【YD：读取客户动画文件中的参考】
    0.通用
    Author: 韩虹
    Data    :2015_10_13
    ''' 
    def yd_RefInfoRead(self,path):
        print u'>>>>>>[read]'
        print path
        txt = open(path, 'r')
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            txt.close()
        result = []
        for info in fileContent:
            if '\t\t' in info and 'Z:/Client/287_tvs_lsw2016/' in info:
                result.append(info.split('\t\t ')[-1]) 
        txt.close()
        return result 
    '''
    【记录文本信息】
    0.通用
    Author: shenkang
    Data    :2014
    addtion=1,添加
    ''' 
    def gdc_infoFileWrite(self, path, info, addtion=0):
        print u'>>>>>>[write]'
        print path
        if addtion == 1:
            info = self.gdc_infoFileRead(path) + info
        txt = open(path, 'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()   
    ''' 
    【读取文本信息】
    0.通用
    Author: shenkang
    Data    :2014
    ''' 
    def gdc_infoFileRead(self, path):
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
    ''' 
        【记录前期文件信息】
        0.通用
        Author: hanhong
        Data    :2015
        '''     
    def grpInfo(self,infotype='Char',shotType = 3):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo() 
        tempath='D:/Info_Temp/YD/info'
        if shotType==2:
            infopath=tempath+'/'+shotInfos[1]+'/'+shotInfos[2]+'/'+'AssInfo'+'/'
        if shotType==3:
            infopath=tempath+'/'+shotInfos[1]+'/'+shotInfos[2]+'/'+shotInfos[3]+'/'+'AssInfo'+'/'
        mc.sysFile(infopath, makeDir=True)    
        grp=infotype+'_Group'
        grpinfo=[]
        grpAss=[]
        grps=mc.ls(grp,tr=1,l=1)
        if grps and len(grps)==1:
            parts=mc.listRelatives(grps[0],c = 1,f=1)
            if parts:
                for part in parts:
                    if 'Asset_Root' in part:
                        grpAss.append(part)
        if  grpAss:
            for gr in grpAss:
                if '|' in gr and ':' in gr:
                    info=gr.split('|')[-1].split(':')[0]
                    grpinfo.append(info)
                
        self.gdc_infoFileWrite((infopath+infotype+'.txt') ,grpinfo) 
        return grpinfo  
    
    
    '''
    
    【YD：读取客户动画文件中的master名称】
    0.通用
    Author: 韩虹
    Data    :2015_10_29
    '''     
    def animExrInfo(self):
        ctrlM=[]
        ctrlMove=[]
        ctrlChr=[]
        ctrls=mc.ls(type='nurbsCurve',l=1)
        cams=[]
        cam=mc.ls(ca=1,l=1)
        for ctr in ctrls:
            ctrp=mc.listRelatives(ctr, p=1, type='transform', f=1)
            if ctrp and 'Char_Group' in ctrp[0] and  ctrp[0].split(':')[-1]=='Master_CTL':
                ctrlM.append(ctrp[0])
            if ctrp and 'Char_Group' in ctrp[0] and ctrp[0].split(':')[-1]=='SuperRoot_CTL':
                ctrlMove.append(ctrp[0])  
            if ctrp and 'Char_Group' in ctrp[0] and ctrp[0].split(':')[-1]=='Root_CTL':
                ctrlChr.append(ctrp[0])  
            if ctrp and 'Prop_Group' in ctrp[0] and  ctrp[0].split(':')[-1]=='Master_CTL':
                ctrlM.append(ctrp[0])
            if ctrp and 'Prop_Group' in ctrp[0] and ctrp[0].split(':')[-1]=='SuperRoot_CTL':
                ctrlMove.append(ctrp[0])  
            if ctrp and 'Prop_Group' in ctrp[0] and ctrp[0].split(':')[-1]=='Root_CTL':
                ctrlChr.append(ctrp[0]) 
        for ca in cam:
            cap=mc.listRelatives(ca, p=1, type='transform', f=1)
            if cap and 'Camera_Group' in cap[0]:
                cams.append(cap[0])
            
        return [ctrlM,ctrlMove,ctrlChr,cams] 
    '''    
    【YD：读取动画文件中的master名称】
    0.通用
    Author: 韩虹
    Data    :2015_10_29
    ''' 
    def animImInfo(self):
        ctrlM=[]
        ctrlMove=[]
        ctrlChr=[]
        ctrls=mc.ls(type='nurbsCurve',l=1)
        cams=[]
        cam=mc.ls(ca=1,l=1)
        for ctr in ctrls:
            ctrp=mc.listRelatives(ctr, p=1, type='transform', f=1)
            if ctrp and 'Char_Group' in ctrp[0] and  ctrp[0].split(':')[-1]=='Master':
                ctrlM.append(ctrp[0])
            if ctrp and 'Char_Group' in ctrp[0] and ctrp[0].split(':')[-1]=='Move_ctrl':
                ctrlMove.append(ctrp[0])  
            if ctrp and 'Char_Group' in ctrp[0] and ctrp[0].split(':')[-1]=='Character':
                ctrlChr.append(ctrp[0])  
            if ctrp and 'Prop_Group' in ctrp[0] and  ctrp[0].split(':')[-1]=='Master':
                ctrlM.append(ctrp[0])
            if ctrp and 'Prop_Group' in ctrp[0] and ctrp[0].split(':')[-1]=='Move_ctrl':
                ctrlMove.append(ctrp[0])  
            if ctrp and 'Prop_Group' in ctrp[0] and ctrp[0].split(':')[-1]=='Character':
                ctrlChr.append(ctrp[0])           
        for ca in cam:
            cap=mc.listRelatives(ca, p=1, type='transform', f=1)
            if cap and 'Camera_Group' in cap[0]:
                cams.append(cap[0])        
        return [ctrlM,ctrlMove,ctrlChr,cams]           

    def animExr(self,shotType = 3): 
        #bake约束
        mc.ikSystem(e = 1,sol = 1)   
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()               
        mastrInfo=self.animExrInfo()[0]
        moveInfo=self.animExrInfo()[1]
        chrInfo=self.animExrInfo()[2]
        camInfo=self.animExrInfo()[3]
        if shotType == 3:
            temppath='D:/Info_Temp/YD/exr/' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]+'/'
        if shotType == 2:
            temppath='D:/Info_Temp/YD/exr/' + shotInfos[1] + '_' + shotInfos[2] + '/'      
        mc.sysFile(temppath, makeDir=True)
        startime=mc.playbackOptions(q=1,min=1)-12
        mass=mastrInfo+moveInfo+chrInfo+camInfo
        io = (mc.playbackOptions(q=1, minTime=1)-12, mc.playbackOptions(q=1, maxTime=1)+12)
        if  mass:
            for mas in mass:
                shortname=mas.split('|')[-1].split(':')[0]
                type=''
                if mas in mastrInfo:
                    type='ms'
                if mas in moveInfo:
                    type='mv'
                if mas in chrInfo:
                    type='cr'
                if mas in camInfo:
                    type='ca'
                fiename=shortname+'_'+type+'.anim'
                mc.currentTime(startime)
                mc.setKeyframe(mas)  
                '''              
                cons=mc.listConnections(mas, s = 0, d = 1,p=1,type='constraint')
                bake=0
                if cons:
                    for con in cons:
                        if 'target' in con:
                            bake=0
                            break
                '''
                bake=0
                if mas in camInfo:
                    cons=mc.listConnections(mas, s = 0, d = 1,p=1,type='constraint')
                    if cons:
                        bake=1
                    else:                    
                        pars=mc.listRelatives(mas, p=1, type='transform', f=1)
                        if pars:
                            cons=mc.listConnections(pars[0], s = 0, d = 1,type='constraint')
                            if cons:
                                bake=1                   
                    
                if bake==1:                   
                    locn=mas.split('|')[-1]+'_locator'
                    if mc.objExists(locn):
                        mc.delete(locn)                               
                    loct=mc.CreateLocator()
                    mc.rename(loct,locn)
                    point=mc.pointConstraint(mas,locn,name=mas.split('|')[-1]+'_pointConstraint')   
                    poinp=mc.parentConstraint(mas,locn,name=mas.split('|')[-1]+'_parentConstraint')                    
                    mc.select(locn)
                    mc.bakeResults(locn,t=io,simulation=1,sampleBy=1,disableImplicitControl=1,preserveOutsideKeys=1,sparseAnimCurveBake=0,removeBakedAttributeFromLayer=0,bakeOnOverrideLayer=0,controlPoints=0,shape=0)
                    mc.select(locn)
                    mc.file((temppath+fiename),options="precision=17;intValue=17;nodeNames=1;verboseUnits=0;whichRange=1;range=0:10;options=keys;hierarchy=below;controlPoints=0;shapes=1;helpPictures=0;useChannelBox=0;copyKeyCmd=-animation objects -option keys -hierarchy below -controlPoints 0 -shape 1 ",f=1,type="animExport",preserveReferences=1,es=1)                      
                else:
                    mc.select(mas)
                    mc.file((temppath+fiename),options="precision=17;intValue=17;nodeNames=1;verboseUnits=0;whichRange=1;range=0:10;options=keys;hierarchy=below;controlPoints=0;shapes=1;helpPictures=0;useChannelBox=0;copyKeyCmd=-animation objects -option keys -hierarchy below -controlPoints 0 -shape 1 ",f=1,type="animExport",preserveReferences=1,es=1)  
        return 0


    def animImp(self,shotType = 3):    
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()               
        mastrInfo=self.animImInfo()[0]
        moveInfo=self.animImInfo()[1]
        chrInfo=self.animImInfo()[2]
        camInfo=self.animImInfo()[3]
        temppath=''
        if shotType == 3:
            temppath='D:/Info_Temp/YD/exr/' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]+'/'
        if shotType == 2:
            temppath='D:/Info_Temp/YD/exr/' + shotInfos[1] + '_' + shotInfos[2] + '/' 
        mass=mastrInfo+moveInfo+chrInfo
        if  mass:
            for mas in mass:
                shortname=mas.split('|')[-1].split(':')[0]
                type=''
                if mas in mastrInfo:
                    type='ms'
                if mas in moveInfo:
                    type='mv'
                if mas in chrInfo:
                    type='cr'                    
                fiename=shortname+'_'+type+'.anim'
                if os.path.exists(temppath+fiename):
                    mc.select(mas)
                    mc.file((temppath+fiename),i=1,pr=1)
        
        if camInfo:
            for cam in camInfo:
                shortname=cam.split('|')[-1].split(':')[0]
                camanim=shortname+'_ca.anim'
                if os.path.exists(temppath+camanim):
                    if len(cam.split('|'))>2 :
                        cam=mc.parent(cam,w=1)
                    mc.select(cam)
                    mc.file((temppath+camanim),i=1,pr=1)                    
                
        return temppath 
    def ReorganizeGrp(self,shotType = 3):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo() 
        tempath='D:/Info_Temp/YD/info'
        if shotType==2:
            infopath=tempath+'/'+shotInfos[1]+'/'+shotInfos[2]+'/'+'AssInfo'+'/'
        if shotType==3:
            infopath=tempath+'/'+shotInfos[1]+'/'+shotInfos[2]+'/'+shotInfos[3]+'/'+'AssInfo'+'/'
        
        charinfo=[]
        prpinfo=[]
        fxinfo=[]
        setinfo=[]
        if os.path.exists(infopath):
            files=mc.getFileList(folder=infopath)
            for fil in files:
                if fil=='Char.txt':
                    charinfo=self.gdc_infoFileRead(infopath+fil)
                if fil=='FX.txt':
                    fxinfo=self.gdc_infoFileRead(infopath+fil)
                if fil=='Prop.txt':
                    prpinfo=self.gdc_infoFileRead(infopath+fil)
                if fil=='Set.txt':
                    setinfo=self.gdc_infoFileRead(infopath+fil) 
        grops=[]
        objs=mc.ls(tr=1,l=1)
        grpZ=['Char_Group','Prop_Group','Set_Group','FX_Group']
        grpn=['Camera_Group','persp','top','front','side']
        for obj in objs:
           if '|' in obj:
               objn=obj.split('|')
               if len(objn)==2 and  objn[1] not in grpZ+grpn:
                   grops.append(obj) 
        if grops:
            for gr in grops:
                if ':' in gr:
                    grinfo=gr.split('|')[-1].split(':')[0]
                    if grinfo in  charinfo:
                           mc.parent(gr,grpZ[0])                    
                    if grinfo in  prpinfo:
                           mc.parent(gr,grpZ[1])                      
                    if grinfo in  fxinfo:
                           mc.parent(gr,grpZ[3]) 
                    if grinfo in  setinfo:
                           mc.parent(gr,grpZ[2])  
        return  0

# -*- coding: utf-8 -*-
# 【通用】【checkin补充工具】
#  Author : 韩虹
#  Data   : 2014_07
#  Mender:韩虹
#  Data  :2014_07
# import sys
# sys.path.append('D:\\food\pyp\common')






import maya.cmds as mc
import maya.mel as mel
import os
import re
import pymel.core as pm
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig;reload(sk_infoConfig)
from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout;reload(sk_cacheFinalLayout)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig;reload(sk_referenceConfig)
class csl_checkin(object):
    def __init__(self):
        # namespace清理
        pass
        
    #----------------------------------------------------------------------------------------------#
    

    #----------------------------------------------------------------------------------------------#
#---------------------------------------------------
#选择变换tx尺寸工具
#------HANHONG------------------------------------------

    def csl_TexsizeSet(self):
    # 窗口
        if mc.window('csl_TexsizeSet', exists=True):
            mc.deleteUI('csl_TexsizeSet')
        mc.window('csl_TexsizeSet', title=u'设置贴图尺寸(选择物体)',
                  width=320, height=350, sizeable=True)
         # 面板
        mc.frameLayout(label=u'设置贴图尺寸（选择物体）', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=1)
        mc.button(label=u'全尺寸', bgc=[0.13, 0.15, 0.25], width=320,height=50, command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeReadF("full",1)')
        mc.button(label=u'半尺寸', bgc=[0.13, 0.15, 0.25], width=320,height=50,command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeReadF("half",1)')
        mc.button(label=u'1/4尺寸', bgc=[0.13, 0.15, 0.25], width=320,height=50, command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeReadF("quarter",1)')
        mc.button(label=u'Quadratic', bgc=[0.13, 0.15, 0.25], width=320,height=50, command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeReadF("quarter",1)')        
        mc.button(label=u'off', bgc=[0.13, 0.15, 0.25], width=320,height=50, command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeReadF("quarter",1)') 
        mc.setParent('..')
        mc.setParent('..')  
        mc.frameLayout(label=u'设置贴图尺寸（All）', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=1)
        mc.button(label=u'全尺寸', bgc=[0.13, 0.15, 0.25],width=320,height=50, command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeReadF("full",0)')
        mc.button(label=u'半尺寸', bgc=[0.13, 0.15, 0.25], width=320,height=50, command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeReadF("half",0)')
        mc.button(label=u'1/4尺寸', bgc=[0.13, 0.15, 0.25], width=320,height=50, command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeReadF("quarter",0)')
        mc.setParent('..')
        mc.setParent('..') 
        
        mc.frameLayout(label=u'设置Filter Type', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=2)
        mc.button(label=u'Quadratic(All)', bgc=[0.13, 0.15, 0.25], width=160,height=50, command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageFilterType("all",4)')        
        mc.button(label=u'off(All)', bgc=[0, 0, 0], width=160,height=50, command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageFilterType("all",0)') 

        mc.button(label=u'Quadratic(select)', bgc=[0.13, 0.15, 0.25], width=160,height=50, command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageFilterType("select",4)')        
        mc.button(label=u'off(select)', bgc=[0, 0, 0], width=160,height=50, command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageFilterType("select",0)') 
        mc.setParent('..')
        mc.setParent('..')         
        mc.showWindow('csl_TexsizeSet')           
     #------------------------------#
    # 【总篇】【checin】【上传工具】【后台】
  
#帖图路径
    def csl_imagePath(self,line='Pre',texpath=[]):
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if line=='Pre':
            shotInfos= sk_infoConfig.sk_infoConfig().checkShotInfo()
            chatype=''
            # if 'c' in shotInfos[1][0].lower():
            #     chatype='characters'
            # if 'p' in shotInfos[1][0].lower():
            #     chatype='props'
            # if 's' in shotInfos[1][0].lower():
            #     chatype='sets'
            #====add by zhangben 2016.12.28 通过文件名获得服务器路径判断asset文件类
            scenes_name = pm.sceneName().basename()#===== start line====================
            path = mc.idmtService("GetAssetPath", scenes_name)
            m = re.search(r'\\scenes\\([^\\]+)\\', path)
            chatype = m.group(1)#===========end line===================
            serverimagepath= serverPath+'sourceimages/'+chatype+'/'+shotInfos[1]+'/'
            temimagepath='D:/Info_Temp/temp/texScale/' + str(shotInfos[1]) + '/'
            texpath=[temimagepath,serverimagepath]
        if line == 'Render':
            temimagepath=[]
            serverimagepath=[]
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNamespace = refInfos[2][0] 
            for ns in refNamespace:
                shotInfos=ns.split('_')
                if shotInfos[0] in ['csl','ice']:
                    chatype=''
                    if 'c' in shotInfos[1][0].lower():
                        chatype='characters'
                    if 'p' in shotInfos[1][0].lower():
                        chatype='props'
                    if 's' in shotInfos[1][0].lower():
                        chatype='sets'
                    serverimgpath=serverPath+'sourceimages/'+chatype+'/'+shotInfos[1]+'/'
                    temimgpath='D:/Info_Temp/temp/texScale/' + str(shotInfos[1]) + '/' 
                    temimagepath.append(temimgpath)
                    serverimagepath.append(serverimgpath)
                    texpath=[temimagepath,serverimagepath]
        return texpath            
                
                   
        
#写信息
    def csl_InfoWrite (self, path , info , addtion=0):
        print u'>>>>>>[write]'
        print path
        if addtion == 1:
            info = self.checkFileRead(path) + info
        temp = path
        if re.search('file-cluster|^L:', path) != None:
            temp = os.path.join(os.getenv('TEMP'), os.path.basename(path))
        txt = open(temp, 'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()
        if temp != path:
            mel.eval('zwSysFile "move" \"' + temp.replace("\\", "/") + '\" \"' + path.replace("\\", "/") + '\" 1')                

#读信息
    def csl_InfoRead(self, path):
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
#贴图尺寸转换并记录相应贴图信息
    def csl_ImageSizeCover(self,type='quarter',server=1):
        import maya.OpenMaya
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        TexsizeCoverName='TexSizeCover_'+shotInfos[1]+'_'+type+'.txt'
        TexSizeCoverPath=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/'+type+'/'
        img = maya.OpenMaya.MImage()
        ScaleRate=''
        if type=='full':
            ScaleRate=float(1)
        if type=='half':
            ScaleRate=float(0.5)
        if type=='quarter':
            ScaleRate=float(0.25)                
        serverimagepath=self.csl_imagePath(line='Pre',texpath=[])[1] 
        temimagepath=self.csl_imagePath(line='Pre',texpath=[])[0] 
        mc.sysFile(temimagepath, makeDir=True)
        Files=mc.ls(type='file')+ mc.ls(type = 'aiImage')
        FileName=[]
        TexName=[]
        if Files:
            for File in Files:
                keyAttr = '.fileTextureName'
                imgNodeType = mc.nodeType(File)
                if imgNodeType in ['aiImage']:
                    keyAttr = '.filename'
                fileTex = File + keyAttr
                if not mc.ls(fileTex):
                    continue
                oldFile = mc.getAttr(fileTex,x=1)
                if oldFile and (('_'+type) not in oldFile):
                    Short= oldFile.split('/')[len(oldFile.split('/'))-1]
                    shortnew=Short.split('.')[0]+'_'+type+'.'+Short.split('.')[1]
                    imagetype=Short.split('.')[1]
                    shorttex01=Short.split('.')[0]+'_'+type+'01.tx'
                    shorttex=Short.split('.')[0]+'_'+type+'.tx'
                    newmap=temimagepath+shortnew
                    txmap01=temimagepath+Short.split('.')[0]+'_'+type+'01.tx'
                    txmap=temimagepath+Short.split('.')[0]+'_'+type+'.tx'
                    newmapserv=serverimagepath+shortnew
                    txmapserv=serverimagepath+Short.split('.')[0]+'_'+type+'.tx'
                    #将贴图copy到本机并修改尺寸
#                        if shortnew  in mc.getFileList(folder=temimagepath):
#                            mc.sysFile(newmap,delete=1)   
                    #mc.sysFile(oldFile,copy=newmap)
                    mel.eval('source \"zwImgcvt\"')
                    img.readFromFile(oldFile)
                    width = maya.OpenMaya.uIntPtr()
                    height = maya.OpenMaya.uIntPtr()
                    img.getSize(width, height)
                    if '.hdr' not in oldFile and not (shotInfos[0] in ['csl'] and (width.value()<=1024 or height.value()<=1024)):
                        print File
                        try:
                            newwidth=int(width.value()*ScaleRate)
                            newheight=int(height.value()*ScaleRate)
                            #print '%dx%d -> 512x512' % (width.value(), height.value())
                            img.resize(newwidth, newheight)
                            textype=imagetype.lower()
                            img.writeToFile(newmap,textype)
                            img.release()
                        except:
                            print '--------error'
                            print oldFile
                            pass
                        #将转好尺寸的贴图转为tx
                        if shorttex in mc.getFileList(folder=temimagepath):
                            mc.sysFile(txmap,delete=1)
                        #mc.sysFile(newmap,copy=txmap01)
                        mel.eval('zwImgcvt \"' + newmap + '\" \"' + txmap + '\"')
                    else:
                        mel.eval('zwImgcvt \"' + oldFile + '\" \"' + txmap + '\"')
#                        if shorttex01 in mc.getFileList(folder=temimagepath):
#                            mc.sysFile(txmap01,delete=1)             
                    if server:
                        mel.eval('source \"zwSysFile\"')
                        mel.eval('zwSysFile "copy" \"' + newmap + '\" \"' + newmapserv + '\" 1')
                        mel.eval('zwSysFile "copy" \"' + txmap + '\" \"' + txmapserv + '\" 1')
                        FileName.append(File)
                        TexName.append(newmapserv)
                        if shortnew in mc.getFileList(folder=temimagepath):
                            mc.sysFile(newmap,delete=1)
                        if shorttex in mc.getFileList(folder=temimagepath):
                            mc.sysFile(txmap,delete=1)
#                            if shorttex01 in mc.getFileList(folder=temimagepath):
#                                mc.sysFile(txmap01,delete=1)
                if ('_'+type) in oldFile:
                    mc.error(u'------------------------请检测贴图，请使用合尺寸贴图------------------------'%TexsizeCoverName)
        TexInfo=[]
        if TexName and server==1:                        
            TexInfo=FileName + [u'----------------']+ TexName
            self.csl_InfoWrite((temimagepath+TexsizeCoverName) , TexInfo)
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (temimagepath+TexsizeCoverName) + '"' + ' ' + '"' + (TexSizeCoverPath + TexsizeCoverName) + '"' + ' true'
            mel.eval(updateAnimCMD)
            print u'===[Updating TexsizeCoverInfo To Server]===传输[%s]完毕==='%TexsizeCoverName
            
        return TexInfo

#记录全尺寸贴图连接信息        
    def csl_FullImageWrite(self,server=1):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        TexsizeCoverName='TexSizeCover_'+shotInfos[1]+'_full.txt'
        TexSizeCoverPath=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/'+'full/'               
        temimagepath=self.csl_imagePath(line='Pre',texpath=[])[0] 
        serverimagepath=self.csl_imagePath(line='Pre',texpath=[])[1] 
        mc.sysFile(temimagepath, makeDir=True)
        Files=mc.ls(type='file')+ mc.ls(type = 'aiImage')
        FileName=[]
        TexName=[]
        if Files:
            for File in Files:
                keyAttr = '.fileTextureName'
                imgNodeType = mc.nodeType(File)
                if imgNodeType in ['aiImage']:
                    keyAttr = '.filename'
                fileTex = File + keyAttr
                if not mc.ls(fileTex):
                    continue
                oldFile = mc.getAttr(fileTex,x=1)
                if oldFile:
                    Short= oldFile.split('/')[len(oldFile.split('/'))-1]
                    serInfo=serverimagepath+Short
                    TexName.append(serInfo)
                    FileName.append(File)
        
        TexInfo=FileName + [u'----------------']+ TexName
        self.csl_InfoWrite((temimagepath+TexsizeCoverName) , TexInfo)
        if  server:
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (temimagepath+TexsizeCoverName) + '"' + ' ' + '"' + (TexSizeCoverPath + TexsizeCoverName) + '"' + ' true'
            mel.eval(updateAnimCMD)
            print u'===[Updating TexsizeCoverInfo To Server]===传输[%s]完毕==='%TexsizeCoverName
#读取贴图尺寸信息，并连接相应尺寸贴图(前期Pre,渲染环节Render）
#    def csl_ImageSizeRead(self,line='Pre',type='quarter',server=1):
#        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
#        if line=='Pre':        
#            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
#            TexsizeCoverName='TexSizeCover_'+shotInfos[1]+'_'+type+'.txt'
#            TexSizeCoverPath=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/'+type+'/'
#            serverimagepath=self.csl_imagePath(line='Pre',texpath=[])[1]
#            ImageInfo=self.csl_InfoRead(TexSizeCoverPath+TexsizeCoverName)
#            #分割点
#            signKeyIndex = sk_cacheFinalLayout.sk_cacheFinalLayout().checkListSameAllIndex(ImageInfo,u'----------------')[0]
#            for i in range(signKeyIndex):
#                #print (ImageInfo[i]+'.....'+ ImageInfo[i+signKeyIndex+1]+'==================')
#                fileTex=ImageInfo[i]+'.fileTextureName'
#                Image=ImageInfo[i+signKeyIndex+1]
#                ImageShort=Image.split('/')[len(Image.split('/'))-1]
#                import re
#                import re
#                for f in mc.getFileList(folder=serverimagepath):
#                    if  ImageShort.lower()== f.lower() :
#                        mc.setAttr(fileTex,Image,type='string')
#                        break 
#            print u'==转换贴图[%s]完毕==='%type 
#检测前期是否上传三种尺寸贴图信息
    def csl_ImageRecordCheck(self,type='quarter',server=1):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()       
        if len(refInfos)==0:
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            TexsizeCoverName='TexSizeCover_'+shotInfos[1]+'_'+type+'.txt'
            TexSizeCoverPath=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/'+type+'/'
            if TexsizeCoverName in mc.getFileList(folder=TexSizeCoverPath) :
                print u'==前期已经上传该文件尺寸贴图信息[%s]==='%(shotInfos[1]+'===='+type)
                 
            else:
                mc.error(u'==前期没有上传该文件尺寸贴图信息[%s]==='%(shotInfos[1]+'===='+type)) 
                
        else:
            refFile = refInfos[1][0] 
            for ref in refFile:
                shotname=ref.split('/')[len(ref.split('/'))-1] 
                shotInfos=shotname.split('_')
                if shotInfos[1][0] in ['c','p','s']:
                    TexsizeCoverName='TexSizeCover_'+shotInfos[1]+'_'+type+'.txt'
                    TexSizeCoverPath=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/'+type+'/'
                    if TexsizeCoverName in mc.getFileList(folder=TexSizeCoverPath) :
                        print u'==前期已经上传该文件尺寸贴图信息[%s]==='%(shotInfos[1]+'===='+type) 
                        
                    else:
                        mc.error(u'==前期没有上传该文件尺寸贴图信息[%s]==='%(shotInfos[1]+'===='+type))
                        
        print  u'==检测完成==='             
                        
                    
                
                     

#读取贴图尺寸信息，并连接相应尺寸贴图(渲染环节,前期环节）
    def csl_ImageSizeRead(self,line='Render',type='quarter',server=1):
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if line=='Pre':        
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            TexsizeCoverName='TexSizeCover_'+shotInfos[1]+'_'+type+'.txt'
            TexSizeCoverPath=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/'+type+'/'
            serverimagepath=self.csl_imagePath(line='Pre',texpath=[])[1]
            ImageInfo=self.csl_InfoRead(TexSizeCoverPath+TexsizeCoverName)
            #分割点
            signKeyIndex = sk_cacheFinalLayout.sk_cacheFinalLayout().checkListSameAllIndex(ImageInfo,u'----------------')[0]
            for i in range(signKeyIndex):
                #print (ImageInfo[i]+'.....'+ ImageInfo[i+signKeyIndex+1]+'==================')
                fileTex=ImageInfo[i]+'.fileTextureName'
                Image=ImageInfo[i+signKeyIndex+1]
                ImageShort=Image.split('/')[len(Image.split('/'))-1]
                import re
                for f in mc.getFileList(folder=serverimagepath):
                    if  ImageShort.lower()== f.lower() :
                        mc.setAttr(fileTex,Image,type='string')
                        break 
            print u'==转换贴图[%s]完毕==='%type 
        if line=='Render': 
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refFile = refInfos[1][0] 
            for ref in refFile:
                shotname=ref.split('/')[len(ref.split('/'))-1] 
                shotInfos=shotname.split('_')
                if shotInfos[1][0] in ['c','p','s']:
                    TexsizeCoverName='TexSizeCover_'+shotInfos[1]+'_'+type+'.txt'
                    TexSizeCoverPath=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/'+type+'/'
                    chatype=''
                    if 'c' in shotInfos[1][0]:
                        chatype='characters'
                    if 'p' in shotInfos[1][0]:
                        chatype='props'
                    if 's' in shotInfos[1][0]:
                        chatype='sets'
                    ImageserverPath=serverPath+'sourceimages/'+chatype+'/'+shotInfos[1]+'/'
                    temimgpath='D:/Info_Temp/temp/texScale/' + str(shotInfos[1]) + '/' 
                    ImageInfo=self.csl_InfoRead(TexSizeCoverPath+TexsizeCoverName)
                    needNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
                    Name=''
                    for ns in needNamespaces:
                        if ns.split('_')[0] in ['csl','ice'] and ns.split(':')[0] in shotname:
                            Name=ns
                            break
                    #分割点
                    signKeyIndex = sk_cacheFinalLayout.sk_cacheFinalLayout().checkListSameAllIndex(ImageInfo,u'----------------')[0]
                    for i in range(signKeyIndex):
                        #print (ImageInfo[i]+'.....'+ ImageInfo[i+signKeyIndex+1]+'==================')
                        fileTex= Name+':'+ImageInfo[i]+'.fileTextureName'
                        Image=ImageInfo[i+signKeyIndex+1]
                        ImageShort=Image.split('/')[len(Image.split('/'))-1]
                        import re
                        imageList=mc.getFileList(folder=ImageserverPath)
                        for f in imageList:
                            if  ImageShort.lower()==f.lower() :
                                print fileTex
                                print Image
                                mc.setAttr(fileTex,Image,type='string')
                                break 
            print u'==转换贴图[%s]完毕==='%type
    def csl_ImageSizeCoverRead(self,Type='quarter',server=1):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        if len(refInfos)>0:
             self.csl_ImageSizeRead(line='Pre',type=Type,server=1) 
        else:
             self.csl_ImageSizeRead(line='Render',type=Type,server=1)    
    def csl_timeRecord(self):
        import time
        print time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))  


#贴图尺寸转换并记录相应贴图信息
    def csl_ImageSizeCoverSpe(self,server=1):
        import maya.OpenMaya
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        TexsizeCoverName01='TexSizeCover_'+shotInfos[1]+'_'+'half.txt'
        TexsizeCoverName02='TexSizeCover_'+shotInfos[1]+'_'+'quarter.txt'        
        TexSizeCoverPath01=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/half/' 
        TexSizeCoverPath02=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/quarter/'        
        img = maya.OpenMaya.MImage()
        ScaleRate01=float(0.5)
        ScaleRate02=float(0.25)                       
        serverimagepath=self.csl_imagePath(line='Pre',texpath=[])[1] 
        temimagepath=self.csl_imagePath(line='Pre',texpath=[])[0] 
        mc.sysFile(temimagepath, makeDir=True)
        Files=mc.ls(type='file')+ mc.ls(type = 'aiImage')
        FileName=[]
        TexName01=[]
        TexName02=[] 
      
        if Files:
            for File in Files:
                keyAttr = '.fileTextureName'
                imgNodeType = mc.nodeType(File)
                if imgNodeType in ['aiImage']:
                    keyAttr = '.filename'
                fileTex = File + keyAttr
                if not mc.ls(fileTex):
                    continue
                oldFile = mc.getAttr(fileTex,x=1)
                if oldFile and (('_half') not in oldFile) and (('_quarter') not in oldFile):
                    Short= oldFile.split('/')[len(oldFile.split('/'))-1]
                    shortx=Short.split('.')[0]+'.tx'
                    shortnew01=Short.split('.')[0]+'_'+'half.'+Short.split('.')[1]
                    shortnew02=Short.split('.')[0]+'_'+'quarter.'+Short.split('.')[1]
                    imagetype=Short.split('.')[1]
                    shorttex01=Short.split('.')[0]+'_'+'half.tx'
                    shorttex02=Short.split('.')[0]+'_'+'quarter.tx'
                    newmap01=temimagepath+shortnew01
                    newmap02=temimagepath+shortnew02

                    txmap=temimagepath+shortx
                    txmap01=temimagepath+shorttex01
                    txmap02=temimagepath+shorttex02

                    newmapserv01=serverimagepath+shortnew01
                    newmapserv02=serverimagepath+shortnew02

                    txmapserv=serverimagepath+shortx
                    txmapserv01=serverimagepath+shorttex01
                    txmapserv02=serverimagepath+shorttex02
                    #将贴图copy到本机并修改尺寸
#                        if shortnew  in mc.getFileList(folder=temimagepath):
#                            mc.sysFile(newmap,delete=1)   
                    #mc.sysFile(oldFile,copy=newmap)
                    img.readFromFile(oldFile)
                    width = maya.OpenMaya.uIntPtr()
                    height = maya.OpenMaya.uIntPtr()
                    img.getSize(width, height)
                    textype=imagetype.lower()
                    if textype not in ['hdr'] and not (shotInfos[0] in ['csl'] and (width.value()<=1024 or height.value()<=1024)):
                        newwidth01=int(width.value()*ScaleRate01)
                        newheight01=int(height.value()*ScaleRate01)
                        newwidth02=int(width.value()*ScaleRate02)
                        newheight02=int(height.value()*ScaleRate02)
                        #print '%dx%d -> 512x512' % (width.value(), height.value())
                        try:
                            img.resize(newwidth01, newheight01)
                            textype=imagetype.lower()
                            img.writeToFile(newmap01,textype)
                            img.release()
                            #转1/4
                            img.readFromFile(newmap01)
                            img.resize(newwidth02, newheight02)
                            img.writeToFile(newmap02,textype)
                            img.release()
                        except:
                            mc.warning(u'[%s]无法转贴图，请检查'%File)
                    #将转好尺寸的贴图转为tx
#                        if shorttex01 in mc.getFileList(folder=temimagepath):
#                            mc.sysFile(txmap01,delete=1)             
                    #mc.sysFile(newmap,copy=txmap01)
                        mel.eval('source \"zwImgcvt\"')
                        mel.eval('zwImgcvt \"' + newmap01 + '\" \"' + txmap01 + '\"')
                        mel.eval('zwImgcvt \"' + newmap02 + '\" \"' + txmap02 + '\"')
                    mel.eval('source \"zwImgcvt\"')
                    mel.eval('zwImgcvt \"' + oldFile + '\" \"' + txmap + '\"')
#                        if shorttex01 in mc.getFileList(folder=temimagepath):
#                            mc.sysFile(txmap01,delete=1)             
                    if server:
                        mel.eval('source \"zwSysFile\"')
                        mel.eval('zwSysFile "copy" \"' + txmap + '\" \"' + txmapserv + '\" 1')
                        if textype not in ['hdr'] and not (shotInfos[0] in ['csl'] and (width.value()<=1024 or height.value()<=1024)):
                            mel.eval('source \"zwSysFile\"')
                            mel.eval('zwSysFile "copy" \"' + newmap01 + '\" \"' + newmapserv01 + '\" 1')
                            mel.eval('zwSysFile "copy" \"' + newmap02 + '\" \"' + newmapserv02 + '\" 1')
                            mel.eval('zwSysFile "copy" \"' + txmap01 + '\" \"' + txmapserv01 + '\" 1')
                            mel.eval('zwSysFile "copy" \"' + txmap02 + '\" \"' + txmapserv02 + '\" 1')
                            FileName.append(File)
                            TexName01.append(newmapserv01)
                            TexName02.append(newmapserv02)
                            if shortnew01 in mc.getFileList(folder=temimagepath):
                                mc.sysFile(newmap01,delete=1)
                            if shortnew02 in mc.getFileList(folder=temimagepath):
                                mc.sysFile(newmap02,delete=1)
                            if shorttex01 in mc.getFileList(folder=temimagepath):
                                mc.sysFile(txmap01,delete=1)
                            if shorttex02 in mc.getFileList(folder=temimagepath):
                                mc.sysFile(txmap02,delete=1)
    #                            if shorttex01 in mc.getFileList(folder=temimagepath):
    #                                mc.sysFile(txmap01,delete=1)

                if '_quarter' in oldFile or'_half' in oldFile:
                    mc.error(u'------------------------请检测贴图，请使用合尺寸贴图------------------------'%TexsizeCoverName01)
                    mc.error(u'------------------------请检测贴图，请使用合尺寸贴图------------------------'%TexsizeCoverName02)
        TexInfo01=[]
        TexInfo02=[]        
        if TexName01 and server==1:                        
            TexInfo01=FileName + [u'----------------']+ TexName01
            TexInfo02=FileName + [u'----------------']+ TexName02            
            self.csl_InfoWrite((TexSizeCoverPath01+TexsizeCoverName01) , TexInfo01)
            print u'===[Updating TexsizeCoverInfo To Server]===传输[%s]完毕==='%TexsizeCoverName01
            self.csl_InfoWrite((TexSizeCoverPath02+TexsizeCoverName02) , TexInfo02)
            print u'===[Updating TexsizeCoverInfo To Server]===传输[%s]完毕==='%TexsizeCoverName02           
    
        return [TexInfo01,TexInfo02] 
        
    def csl_ImageSizeReadTex(self,type='quarter',server=1):
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        TexsizeCoverName='TexSizeCover_'+shotInfos[1]+'_'+type+'.txt'
        TexSizeCoverPath=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/'+type+'/'
        serverimagepath=self.csl_imagePath(line='Pre',texpath=[])[1]
        ImageInfo=self.csl_InfoRead(TexSizeCoverPath+TexsizeCoverName)
        ImageName=[]
        #分割点
        signKeyIndex = sk_cacheFinalLayout.sk_cacheFinalLayout().checkListSameAllIndex(ImageInfo,u'----------------')[0]
        for i in range(signKeyIndex):
            #print (ImageInfo[i]+'.....'+ ImageInfo[i+signKeyIndex+1]+'==================')
            fileTex=ImageInfo[i]+'.fileTextureName'
            Image=ImageInfo[i+signKeyIndex+1]
            ImageShort=Image.split('/')[len(Image.split('/'))-1]
            import re
            for f in mc.getFileList(folder=serverimagepath):
                if  ImageShort.lower()== f.lower() :
                    ImageName.append(f)
                    break 
        return ImageName

        
    def csl_ImageSizeCovercheckin(self,server=1): 
        serverimagepath=self.csl_imagePath(line='Pre',texpath=[])[1] 
        Tex = mc.getAttr(serverimagepath)
#单个
    def csl_ImageSizeCoverOne(self,ImageNameF,server=1):
        import maya.OpenMaya
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        TexsizeCoverName01='TexSizeCover_'+shotInfos[1]+'_'+'half.txt'
        TexsizeCoverName02='TexSizeCover_'+shotInfos[1]+'_'+'quarter.txt'        
        TexSizeCoverPath01=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/half/' 
        TexSizeCoverPath02=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/quarter/'        
        img = maya.OpenMaya.MImage()
        ScaleRate01=float(0.5)
        ScaleRate02=float(0.25)                       
        serverimagepath=self.csl_imagePath(line='Pre',texpath=[])[1] 
        temimagepath=self.csl_imagePath(line='Pre',texpath=[])[0] 
        mc.sysFile(temimagepath, makeDir=True)
        
        short=ImageNameF.split('/')[len(ImageNameF.split('/'))-1]
        imageTx=short.split('.')[0]+'.tx'
        imagetype=short.split('.')[1]
        TexName01=short.split('.')[0]+'_half.'+short.split('.')[1]
        TexName02=short.split('.')[0]+'_quarter.'+short.split('.')[1]
        
        shottx01=short.split('.')[0]+'_half.tx'
        shottx02=short.split('.')[0]+'_quarter.tx'
        
        temtex01=temimagepath+TexName01
        temtex02=temimagepath+TexName02
        
        temtx=temimagepath+imageTx
        temtx01=temimagepath+shottx01
        temtx02=temimagepath+shottx02


        sertex01=serverimagepath+TexName01
        sertex02=serverimagepath+TexName02
        
        serttx=serverimagepath+imageTx
        sertx01=serverimagepath+shottx01
        sertx02=serverimagepath+shottx02
        textype=imagetype.lower()
        if textype not in ['hdr']:
            img.readFromFile(ImageNameF)
            width = maya.OpenMaya.uIntPtr()
            height = maya.OpenMaya.uIntPtr()
            img.getSize(width, height)
            newwidth01=int(width.value()*ScaleRate01)
            newheight01=int(height.value()*ScaleRate01)

            newwidth02=int(width.value()*ScaleRate02)
            newheight02=int(height.value()*ScaleRate02)
            img.resize(newwidth01, newheight01)
            img.writeToFile(temtex01,textype)
            img.release()
            img.readFromFile(temtex01)
            img.resize(newwidth02, newheight02)
            img.writeToFile(temtex02,textype)
            img.release()
            #转tx
            mel.eval('source \"zwImgcvt\"')
            mel.eval('zwImgcvt \"' + temtex01 + '\" \"' + temtx01 + '\"')
            mel.eval('zwImgcvt \"' + temtex02 + '\" \"' + temtx02 + '\"')
        mel.eval('source \"zwImgcvt\"')
        mel.eval('zwImgcvt \"' + ImageNameF + '\" \"' + temtx + '\"')
        print temtx
        #上传
        if server:
            mel.eval('source \"zwSysFile\"')
            mel.eval('zwSysFile "copy" \"' + temtx + '\" \"' + serttx + '\" 1')
            mel.eval('zwSysFile "copy" \"' + temtex01 + '\" \"' + sertex01 + '\" 1') 
            mel.eval('zwSysFile "copy" \"' + temtex02 + '\" \"' + sertex02 + '\" 1')                                              
            mel.eval('zwSysFile "copy" \"' + temtx01 + '\" \"' + sertx01 + '\" 1')
            mel.eval('zwSysFile "copy" \"' + temtx02 + '\" \"' + sertx02 + '\" 1')                                                     
            if imageTx in mc.getFileList(folder=temimagepath):
                mc.sysFile(temtx,delete=1)
            if shottx01 in mc.getFileList(folder=temimagepath):
                mc.sysFile(temtex01,delete=1)
            if shottx01 in mc.getFileList(folder=temimagepath):
                mc.sysFile(temtex02,delete=1)                                
            if shottx01 in mc.getFileList(folder=temimagepath):
                mc.sysFile(temtx01,delete=1) 
            if shottx02 in mc.getFileList(folder=temimagepath):
                mc.sysFile(temtx02,delete=1)
#网络检测
#cov为0时，超过4K，8K的贴图不进行连接小尺寸，为1时，超过4K，8K的贴图均会连接相应2K贴图
    def csl_ImageSizeCoverServer(self,server=1,cov=0):
        import os
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
           
        TexSizeCoverPath01=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/half/' 
        TexSizeCoverPath02=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/quarter/'        
                        
        serverimagepath=self.csl_imagePath(line='Pre',texpath=[])[1]
        
        texs=mc.getFileList(folder=serverimagepath)
#        os.path.isfile(pathz+imagenameN)
        if mc.ls(texs) and '_half' not in texs[0]:
            self.csl_ImageSizeCoverSpe(server=1)
        else:      
            Files=mc.ls(type='file')+ mc.ls(type = 'aiImage')
            if Files:
                for File in Files:
                    keyAttr = '.fileTextureName'
                    imgNodeType = mc.nodeType(File)
                    if imgNodeType in ['aiImage']:
                        keyAttr = '.filename'
                    fileTex = File + keyAttr
                    if not mc.ls(fileTex):
                        continue
                    tex= mc.getAttr(fileTex,x=1)
                    shortfull=tex.split('/')[len(tex.split('/'))-1]
                    if shortfull in texs and '_half' not in tex and '_quarter' not in tex:
                        halftex=tex.split('.')[0]+'_half.'+tex.split('.')[1]
                        shorthalf=shortfull.split('.')[0]+'_half.'+tex.split('.')[1]
                        if shorthalf not in texs:
                            self.csl_ImageSizeCoverOne(tex,server=1)
                        else:
                            statfull=os.stat(tex)
                            stathalf=os.stat(halftex)
                            if statfull.st_mtime > stathalf.st_mtime:
                                self.csl_ImageSizeCoverOne(tex,server=1)
    
        self.csl_ImageCoverInfoWrite(server=1)
        if cov==1:
            self.csl_ImageSizeReadFs()
        return 0

#写三种精度贴图连接 
    def csl_ImageCoverInfoWrite(self,server=1):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        
        TexsizeCoverNamefull='TexSizeCover_'+shotInfos[1]+'_'+'full.txt'
        TexsizeCoverNamehalf='TexSizeCover_'+shotInfos[1]+'_'+'half.txt'
        TexsizeCoverNamequater='TexSizeCover_'+shotInfos[1]+'_'+'quarter.txt'        
        
        TexSizeCoverPathfull=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/full/'
        TexSizeCoverPathhalf=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/half/' 
        TexSizeCoverPathquater=serverPath+'data/TexSizeCover/'+shotInfos[1]+'/'+shotInfos[2]+'/quarter/'        
                            
        serverimagepath=self.csl_imagePath(line='Pre',texpath=[])[1] 
        temimagepath=self.csl_imagePath(line='Pre',texpath=[])[0] 
        mc.sysFile(temimagepath, makeDir=True)
        Files=mc.ls(type='file')+ mc.ls(type = 'aiImage')
        FileName=[]
        TexNameFull=[]
        TexNameHalf=[]
        TexNameQuater=[] 
        FileName=[]       
        if Files:
            for File in Files:
                keyAttr = '.fileTextureName'
                imgNodeType = mc.nodeType(File)
                if imgNodeType in ['aiImage']:
                    keyAttr = '.filename'
                fileTex = File + keyAttr
                if not mc.ls(fileTex):
                    continue
                texFile = mc.getAttr(fileTex,x=1)
                if texFile and (('_half') not in texFile) and (('_quarter') not in texFile):
                    Shortfull= texFile.split('/')[len(texFile.split('/'))-1]
                    shorthalf=Shortfull.split('.')[0]+'_'+'half.'+Shortfull.split('.')[1]
                    shortquater=Shortfull.split('.')[0]+'_'+'quarter.'+Shortfull.split('.')[1]


                    fullserv=serverimagepath+Shortfull
                    halfserv=serverimagepath+shorthalf
                    quarterserv=serverimagepath+shortquater

                    if server:
                        TexNameFull.append(fullserv)
                        TexNameHalf.append(halfserv)
                        TexNameQuater.append(quarterserv)
                        FileName.append(File)
                            
        TexInfoFull=[]
        TexInfoHalf=[]
        TexInfoQuarter=[] 
              
        if TexNameHalf and server==1:                        
            TexInfoFull=FileName + [u'----------------']+ TexNameFull
            TexInfoHalf=FileName + [u'----------------']+ TexNameHalf
            TexInfoQuarter=FileName + [u'----------------']+ TexNameQuater            
            self.csl_InfoWrite((TexSizeCoverPathfull+TexsizeCoverNamefull) , TexInfoFull)
            self.csl_InfoWrite((TexSizeCoverPathhalf+TexsizeCoverNamehalf) , TexInfoHalf)
            self.csl_InfoWrite((TexSizeCoverPathquater+TexsizeCoverNamequater) , TexInfoQuarter)
       
            
        return [TexInfoFull,TexInfoHalf,TexInfoQuarter]
    def csl_MsSwitchTx(self):
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRN=refInfos[0][0]
        refPath=refInfos[1][0]
        for i in range(len(refRN)):
            if 'ms_anim' in refPath[i]:
                newpath=refPath[i].replace('master','texture').replace('ms_anim','tx')
                mc.file(newpath,options="v=0",type="mayaBinary",loadReference=refRN[i])
        return 0 
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【贴图尺寸路径转换】
    #  Author  : 韩虹
    #  Data    : 2015_01_26
    #------------------------------#  
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def csl_ImageSizeReadF(self,sizetype='full',setype=0):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        #if shotInfos[0] not in ['csl','nj','ice','mi','LION','tf']:
        #    mc.error(u'请确认文件名是否正确')
        if shotInfos[0]=='nj' and shotInfos[1][0] in ['c']:
            print(u'\n')
            print(u'+++++++++++++++++++++++')
            print(u'\n')            
            print(u'乐高项目只能转道具及场景贴图，不能转角色贴图')            
            mc.error(u'乐高项目只能转道具及场景贴图，不能转角色贴图')

        Files=[]
        if setype==0:
            Files=mc.ls(type='file')+ mc.ls(type = 'aiImage')
        else:
            mel.eval('source "Z:/Resource/Support/OEM/2013/zwTextureNetwork"')
            Files=mel.eval('zwTextureNetwork()')    
        if Files:
            for fil in Files:
                keyAttr = '.fileTextureName'
                imgNodeType = mc.nodeType(fil)
                if imgNodeType in ['aiImage']:
                    keyAttr = '.filename'
                fileTex = fil + keyAttr
                if not mc.ls(fileTex):
                    continue
                ImageName=mc.getAttr(fileTex,x=1)
                if ImageName and '/' in ImageName and '_' in ImageName and '.' in ImageName:
                    shortName=ImageName.split('/')[-1]
                    path=ImageName.split(shortName)[0]
                    if '//sourceimages' in path:
                        path=path.replace('//sourceimages','/sourceimages')
                    tailname=shortName.split('.')[0].split('_')[-1]
                    fileType=shortName.split('.')[-1]
                    if tailname in ['half','quarter']:
                        basename=shortName.split('_'+tailname)[0]
                    else:
                        basename=shortName.split('.')[0]
                    if sizetype in ['half','quarter']:
                        imagenameN= basename+'_'+sizetype +'.'+fileType
                    else:
                        imagenameN= basename+'.'+fileType
                    pathz=path
                    #if '${IDMT_PROJECTS}' in path:
                    #    pathz=path.replace('${IDMT_PROJECTS}','Z:/Projects')
                    #if '${L_PROJECTS}' in path:
                    #    pathz=path.replace('${L_PROJECTS}','Z:/Projects')
                    if os.path.isfile(pathz+imagenameN):#os.path.exists(pathz) and imagenameN in mc.getFileList(folder=pathz):
                        try:
                            mc.setAttr((fil+'.fileTextureName'),(path+imagenameN),type='string')
                        except:
                            mc.warning (u'============缺少【%s】贴图=======' %(pathz+imagenameN))
                    else:
                        mc.warning (u'============缺少【%s】贴图=======' %(pathz+imagenameN))
        else:
            print u'==============文件内没有材质文件==========='
        print  u'============【%s】贴图转换已完成=======' %sizetype
        return 0   

    def csl_ImageSizeReadFs(self):
        import maya.OpenMaya        
        img = maya.OpenMaya.MImage()
        Files=mc.ls(type='file')+ mc.ls(type = 'aiImage')
        if Files:
            for fil in Files:
                keyAttr = '.fileTextureName'
                imgNodeType = mc.nodeType(fil)
                if imgNodeType in ['aiImage']:
                    keyAttr = '.filename'
                fileTex = fil + keyAttr
                if not mc.ls(fileTex):
                    continue
                ImageName=mc.getAttr(fileTex,x=1)
                img.readFromFile(ImageName)
                width = maya.OpenMaya.uIntPtr()
                height = maya.OpenMaya.uIntPtr()
                img.getSize(width, height)
                widthsize=int(width.value())

                Shortfull= ImageName.split('/')[len(ImageName.split('/'))-1]
                imagepath=ImageName.split(Shortfull)[0]
                shorthalf=Shortfull.split('.')[0]+'_'+'half.'+Shortfull.split('.')[1]
                shortquater=Shortfull.split('.')[0]+'_'+'quarter.'+Shortfull.split('.')[1]
                if widthsize >= 8000 and '_half' not in ImageName and  '_quarter' not in ImageName:
                    try:
                        mc.setAttr((fil+'.fileTextureName'),(imagepath+shortquater),type='string')
                    except:
                        mc.warning (u'============缺少【%s】贴图=======' %(imagepath+shorthalf))
                elif widthsize >=4000 and '_half' not in ImageName and  '_quarter' not in ImageName:
                    try:
                        mc.setAttr((fil+'.fileTextureName'),(imagepath+shorthalf),type='string')
                    except:
                        mc.warning (u'============缺少【%s】贴图=======' %(imagepath+shorthalf))
            print  u'============贴图转换已完成======='
            return 0 
#修改贴图,filter=4,Quartic模式，filter=0,off模式
# HanHong
    def csl_ImageFilterType(self,sel='all',filter=4):
        images=[]
        texs=[]
        if sel=='all':
            texs=mc.ls(type='file',l=1)+ mc.ls(type = 'aiImage',l=1)
        if sel=='select': 
            texs=mc.ls(sl=1,type='file',l=1) + mc.ls(type = 'aiImage',l=1)
        if texs:
            for tex in texs:
                if mc.objExists(tex+'.filterType'):
                    images.append(tex+'.filterType')
        else:
            mc.error(u'请选择相应Image')
        
        if images:
            for img in images:
                mc.setAttr(img,int(filter))
        
        else:
            mc.error(u'no Image')
        
                
        print  u'============FilterType模式转换已完成======='
        return 0
# tf 项目转贴图路径（后台半尺寸，非tf_开关）
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【贴图尺寸路径转换】
    #  Author  : 韩虹
    #  Data    : 2015_01_26
    #------------------------------#
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def tf_ImageSizeReadF(self,sizetype='full',setype=0):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfos[0] not in ['csl','nj','ice','mi','LION','tf']:
            mc.error(u'请确认文件名是否正确')
        if shotInfos[0]=='nj' and shotInfos[1][0] in ['c']:
            print(u'\n')
            print(u'+++++++++++++++++++++++')
            print(u'\n')
            print(u'乐高项目只能转道具及场景贴图，不能转角色贴图')
            mc.error(u'乐高项目只能转道具及场景贴图，不能转角色贴图')

        Files=[]
        if setype==0:
            Files=mc.ls(type='file')+ mc.ls(type = 'aiImage')
        else:
            mel.eval('source "Z:/Resource/Support/OEM/2013/zwTextureNetwork"')
            Files=mel.eval('zwTextureNetwork()')
        if Files:
            for fil in Files:
                keyAttr = '.fileTextureName'
                imgNodeType = mc.nodeType(fil)
                if imgNodeType in ['aiImage']:
                    keyAttr = '.filename'
                fileTex = fil + keyAttr
                if not mc.ls(fileTex):
                    continue
                ImageName=mc.getAttr(fileTex,x=1)
                if ImageName and '/' in ImageName and '_' in ImageName and '.' in ImageName:
                    shortName=ImageName.split('/')[-1]
                    path=ImageName.split(shortName)[0]
                    if '//sourceimages' in path:
                        path=path.replace('//sourceimages','/sourceimages')
                    tailname=shortName.split('.')[0].split('_')[-1]
                    fileType=shortName.split('.')[-1]
                    if tailname in ['half','quarter']:
                        basename=shortName.split('_'+tailname)[0]
                    else:
                        basename=shortName.split('.')[0]
                    if sizetype in ['half','quarter']:
                        imagenameN= basename+'_'+sizetype +'.'+fileType
                    else:
                        imagenameN= basename+'.'+fileType
                    pathz=path
                    if '${IDMT_PROJECTS}' in path:
                        pathz=path.replace('${IDMT_PROJECTS}','Z:/Projects')
                    if '${L_PROJECTS}' in path:
                        pathz=path.replace('${L_PROJECTS}','Z:/Projects')
                    if os.path.isfile(pathz+imagenameN) and 'tf_' in imagenameN:#os.path.exists(pathz) and imagenameN in mc.getFileList(folder=pathz):
                        try:
                            mc.setAttr((fil+'.fileTextureName'),(path+imagenameN),type='string')
                        except:
                            pass

        else:
            print u'==============文件内没有材质文件==========='
        print  u'============【%s】贴图转换已完成=======' %sizetype
        return 0
    
    
    
                                                                                                                                                                                                                                                 
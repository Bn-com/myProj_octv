# -*- coding: utf-8 -*-

'''
Created on 2015

GDC blockin序列拍屏工具【通用】

适用于blocking整集或整场，按相机顺序拍屏为一个avi

@author: hanhong

Data   : 2015_11_16
'''

# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db
import os
import xlrd
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
import sys

#----------------------------------------------------------------------------------------------------------#     
#【通用】相机序列拍屏工具（用于blocking文件连续拍屏）
#@author: hanhong
#Data：2015/11/16

#----------------------------------------------------------------------------------------------------------#    
class GDC_SequencePlayblast(object):
    def __init__(self,pro='nj'):
        self.shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo() 
        if pro=='nj':
            self.Exr='Z:/Projects/Ninjago/Reference/List/Shot List/Ninjago2016/NinjagoPirates/'
            # excel 表（包含帧数等信息）
         #   self.imgPath=self.camPath+'images/'
            self.EPNum=['Clancy','Duobloon','Flintlocke','Intro']
            self.project='Ninjago'
            self.user=['hanhong','xuguojia']
            self.projects=['csl','nj']
            self.proD='NJ'
            self.TempPath='D:/Info_Temp/Playblast/nj/'
            self.width=720
            self.height=505
            self.soundpath='Z:/Projects/Ninjago/Ninjago_scratch/Animation/HalloweenSpecial/mov/'
#----------------------------------------------------------------------------------------------------------#     
    #------------------------------#
    # 【通用】【相】【相机起始，末尾帧信息读取】
    #  Author  : 韩虹
    #  Data    : 2015_10_03
    #
    #------------------------------#              
    def gdc_FrameRead(self):
        reload(xlrd)
        shotInfo=self.shotInfo
        if shotInfo[0] not in self.projects:
            mc.error(u'请检查文件名，不是【%S】项目'%self.project)          
        cams=[]
        ca=mc.ls(ca=1,l=1)

        for cam in ca:
            if shotInfo[1] in cam and shotInfo[2] in cam and '_' in cam and len(cam.split('_'))>3:
                cam=mc.listRelatives(cam,p = 1,f=1)
                if cam:
                    cams.append(cam[0])        
        camInfos=[]
        if cams:    
            for ca in cams:
                project=self.project
                ep=shotInfo[1]
                sq=shotInfo[2]
                sc=ca.split('_')[-1]
                Info=self.GDC_queryMsSQL(project,ep,sq,sc,tp=0)
                if Info:
                    framestar=Info[3]
                    frameend=Info[4]
                    frameRange=Info[5]                                    
                    camInfos.append([ca,framestar,frameend,frameRange])
        else:
            mc.error(u'文件中没有相应场的相机，请检查文件')
        frameInfos=[]
        if camInfos:
            for j in range(len(camInfos)):
                frameNum=camInfos[j][3]
                if j==0:
                    starframe=camInfos[j][1]
                    endframe=camInfos[j][2]
                else:
                    starframe=camInfos[j-1][2]+1
                    endframe=starframe+frameNum-1
                frameInfos.append([camInfos[j][0],starframe,endframe]) 
        else:
            print '\n\n'
            mc.warning(u'【%s】数据库中没有这一场镜头信息，或文件中相机命名不正确，请检查命名，确认正确后请联系TD及PA'%(shotInfo[1]+'_'+shotInfo[2]))
            mc.error(u'【%s】数据库中没有这一场镜头信息，或文件中相机命名不正确，请检查命名，确认正确后请联系TD及PA'%(shotInfo[1]+'_'+shotInfo[2]))
        return frameInfos
    #------------------------------#
    # 【通用】【非核心代码】【删除所有shot】
    #  Author  : 韩虹
    #  Data    : 2015_11_16
    #
    #------------------------------#   
    def gdc_ShotDelete(self):
        shots = mc.ls(type = "shot",l=1)+mc.ls(type='audio',l=1)
        if shots is not None and len(shots) > 0:
            mc.delete(shots)
    #------------------------------#
    # 【通用】【核心代码】【音频信息】
    #  Author  : 韩虹
    #  Data    : 2015_12_16
    #------------------------------#
    def gdc_AudioInfo(self):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        #sounds:
        sounds=mc.ls(type='audio')
        soundT=''
        soundP=''
        soundInfo=''
        if sounds:
            for so in sounds:
                if shotInfo[2].lower() in so.lower():
                    soundP=so
                    soundT=mc.getAttr(so+'.filename')
                    break
        else:
            mc.warning(u'文件缺少音频文件，请检查文件')
            mc.error(u'文件缺少音频文件，请检查文件')
        if soundT!='':
            soundInfo=[soundP,soundT]
        else:
            mc.warning(u'文件中缺少【%s】场音频文件' %(shotInfo[1]+'_'+shotInfo[2]))
        return soundInfo
    #------------------------------#
    # 【通用】【核心代码】【创建相机相应shot，并按顺序，按帧数排列】
    #  Author  : 韩虹
    #  Data    : 2015_11_16
    #------------------------------#       
    def gdc_SequenceSet(self):
        #删除文件中所有原有shot:
        soundT=self.gdc_AudioInfo()[1]
        soundP=self.gdc_AudioInfo()[0]
        soudstartfrme=mc.getAttr(soundP+'.sourceStart')
        self.gdc_ShotDelete()        
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        '''
        soundI=0
        if os.path.exists(self.soundpath+shotInfo[2]+'.wav'):
            soundfile=self.soundpath+shotInfo[2]+'.wav'
            soundI=1
        elif soundI==0 and os.path.exists(self.soundpath+shotInfo[2]+'.WAV'):
            soundfile=self.soundpath+shotInfo[2]+'.WAV' 
            soundI=1
        else:
            mc.warning(u'===============缺少【%s】场音频文件==============='%shotInfo[2])  
            soundI=0
        '''
        #
        #读取相机相应起始，末尾帧，并创建shot

        camInfos=self.gdc_FrameRead()
        shots=[]
        if camInfos and soundT:
            for i in range(len(camInfos)):
                cam=camInfos[i][0]
                startframe=camInfos[i][1]
                endfram=camInfos[i][2]
                shotname=cam.replace('cam','shot').split('|')[-1]
                #Audioname=cam.replace('cam','audio').split('|')[-1]
                mc.shot(shotname,startTime=startframe,endTime=endfram,currentCamera=cam)
                mc.setAttr((shotname+'.sequenceStartFrame'),startframe)
                shots.append(shotname)
        if shots:
            mc.currentTime(soudstartfrme)
            mc.sequenceManager(currentTime=soudstartfrme)
            mc.select(cl=1)
            mc.select(shots)
            mc.sequenceManager(addSequencerAudio=soundT)

        return 0
                              
    #------------------------------#
    # 【通用】【核心代码】【拍屏】
    #  Author  : 韩虹
    #  Data    : 2015_11_16
    #------------------------------#    
    def GDC_SequencePlayblast(self):
        TempPath=self.TempPath
        if os.path.exists(TempPath)==False:
            mc.sysFile(TempPath, makeDir=True)
        fileshot=mc.file(q=1,sn=1,shn=1)
        #读取相机信息，设置序列起始，结尾帧
        camInfos=self.gdc_FrameRead()
        starframe=camInfos[0][1]
        endframe=camInfos[-1][2]
        # 起始帧
        mc.playbackOptions(min=starframe)
        # 起始预留
        preStartFrame = starframe - 12
        mc.playbackOptions(animationStartTime=preStartFrame)
        # 结束帧
        mc.playbackOptions(max=endframe)
        # 结束预留
        posEndFrame = endframe + 12
        mc.playbackOptions(animationEndTime=posEndFrame)
        
        #设置当前帧为起始帧
        mc.currentTime(starframe)
        # mov 名称
        movname=TempPath+fileshot.split('.')[0]+'.avi'
        # 创建shot
        self.gdc_SequenceSet()
        if os.path.exists(movname):
            os.remove(movname)
        #导入声音
        
        #拍屏
        mel.eval('autoUpdateAttrEd')
        mc.lookThru(camInfos[0][0])
        mc.loadModule(scan=1)
        modelPane=mc.getPanel( withFocus=1 )
        mc.setFocus(modelPane)
        mel.eval("zwHeadsUpDisplay 8001")
        mc.playblast(filename=movname,fmt='avi',compression='PVMJPG40',startTime=starframe,endTime=endframe,sequenceTime=1,forceOverwrite=1,widthHeight=[self.width,self.height],percent=100,useTraxSounds=1,quality=70,viewer=1,clearCache=1,showOrnaments=1)
        #mc.playblast(filename=movname,fmt='avi',compression='PVMJPG40',startTime=100,endTime=endframe,sequenceTime=1,forceOverwrite=0,widthHeight=[self.width,self.height],percent=100,useTraxSounds=1,quality=70,viewer=1,clearCache=1,showOrnaments=0)
        mel.eval("zwHeadsUpDisplay 0")
        print 50*'=='
        print u'======================【%s】=====================' %movname
        print 50*'=='
        return 0

     #------------------------------#
    # 【NJ|YD项目】【数据库查询】
    #  Author  : 韩虹
    #  Data    : 2015_11_18
    #  tp==0,查一列，tp=1,查多列
    #------------------------------#    
    def GDC_queryMsSQL(self,project,ep,sq,sc,tp=0):
        import pyodbc
        try:
            cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=idmt-engine08;DATABASE=idmtPlex_%s;UID=EReader;PWD=123123'%(project))       
        except:
            return None     
        cursor = cnxn.cursor()                
        cmd_sql = '''select
        DISTINCT 
        anim_ep=CASE WHEN A.active=0 THEN \'* \'+anim_ep ELSE anim_ep END,
        A.Tag,
        A.anim_sc,
        A.frmStart,
        A.frmEnd,
        A.length,
        Ast.asset_type,
        AFS.fileser
        FROM   dbo.TB_Anim AS A 
        LEFT JOIN dbo.TB_AssetFileSerInAnim AS AFSIA ON A.anim_id = AFSIA.anim_id
        LEFT JOIN dbo.TB_AssetFileSer AS AFS ON AFSIA.fs_id = AFS.fs_id
        LEFT JOIN dbo.TB_Asset Ast ON AFSIA.asset_id = Ast.asset_id
        WHERE A.anim_ep = \'%s\' AND A.Tag = \'%s\' AND A.anim_sc = \'%s\''''%(ep,sq,sc)                       
        if tp==0:
            scInfo = cursor.execute(cmd_sql).fetchone()
        else:
            scInfo = cursor.execute(cmd_sql).fetchall()            
        return scInfo 

            
        
        
        
            
            
                  
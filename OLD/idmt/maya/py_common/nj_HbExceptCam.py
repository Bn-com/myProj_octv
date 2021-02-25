# -*- coding: utf-8 -*-
from maya.cmds import*
import maya.mel as mm
import os
import string
import shutil
import distutils.file_util as dfu
execfile("//file-cluster/GDC/resource/support/maya/python/idmt/yyscripts/yyMImageFunctions.py")
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class nj_HbExceptCam(object):
    def __init__(self):
        # namespace清理
        pass

    def nj_ExceptReCam(self):
        import maya.OpenMaya
        projects=['csl','nj']
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0]) 
        questEP = optionMenu("EP", q = True, v = True)
        getCam=ls(type="camera")
        TheSc=""
        for Cam in getCam:
            if Cam!="frontShape" and Cam!="perspShape" and Cam!="sideShape" and Cam!="topShape":
                if Cam!="frontShape" and Cam!="perspShape" and Cam!="sideShape" and Cam!="topShape":
                        if Cam.find("cam")!=-1:
                            
                            TheFileName=file(q=1,l=1)
                            TheFile=TheFileName[0].split("/")[-1].split(".")
                            
                            if TheFile[-1]=="mb":
                                try:
                                    if shotInfo[0] in projects: #TheFile[0]=="s" and TheFile[1]=="s":
                                        TheSc=TheFile[0][3:]
                                    else:
                                        result=confirmDialog( title='Confirm', message='This is not the  project file!!', button=['Yes'], defaultButton='Yes')
                                        return
                                except:
                                    pass
                            else:
                                result=confirmDialog( title='Confirm', message='Make sure this is .mb file!!', button=['Yes'], defaultButton='Yes')
                                return
                            CamName=Cam.replace("|","").replace("Shape","")
                            CamOver=Cam+".overscan"
                            setAttr(CamOver,1.3)
                            setAttr(Cam+".displayGateMaskColor",0,0,0)
                            setAttr(Cam+".displayGateMaskOpacity",1)
                            ThePath=serverPath+'Set/'+questEP+"/"+TheSc+'/'
                            ThePath2=serverPath+'Set/'+questEP+"/"+TheSc+"/images/"
                            sysFile(ThePath, makeDir=True )
                            sysFile(ThePath2, makeDir=True )
                            select (cl=1)
                            select (CamName)
                            fCam=CamName.split(':')[0]
                            file(ThePath+"/"+fCam+".ma",type="mayaAscii",pr=1,es=1)
                            lookThru (CamName)
                            #playblast( frame=[1001], format="image", viewer=False , w = 1280, h = 720, fo = True, orn = False, cf = ThePath+"/"+CamName+".iff")
                            #yyConvertImageFormat(ThePath+"/"+CamName+".iff", "jpg", 1)
                            temp=internalVar(userTmpDir=True)
                            tempold=getFileList(filespec=(temp + "*.iff"))
                            #修改playblay 为屏渲
                            '''
                            dest=playblast( frame=[101], format="image", viewer=False , w = 1280, h = 720, fo = True, orn = False,percent=100,quality=100, cf = ThePath+"/"+fCam+".iff")

                            tempNew=getFileList(filespec=(temp + "*.iff"))
                            New=list(set(tempNew) - set(tempold))
                            if len(New) ==1:
                                sysFile(dest, delete = True)
                                sysFile(temp+New[0],mov=dest)
                            yyConvertImageFormat(ThePath+"/"+fCam+".iff", "jpg", 1)
                            '''
                            texpath=ThePath+fCam+'.txt'
                            timeinfo=self.nj_timeRecord()
                            startinfo='Start time: '+timeinfo
                            self.nj_checkFileWrite(texpath , startinfo , addtion=0)
                            mm.eval("renderWindowRenderCamera render renderView "+CamName)
                            timeinfo01=self.nj_timeRecord()
                            endinfo='End time: '+timeinfo01
                            self.nj_checkFileWrite(texpath , endinfo , addtion=1)
                            imagename =mm.eval('optionVar -query "renderedImageName"')
                            imgshortName=imagename.split('/')[-1]
                            imgType= imgshortName.split('.')[-1].lower()
                            imgpath=imagename.split(imgshortName)[0]     
                            imgnameN=fCam+'.'+imgType
                            if imgnameN in getFileList(folder=imgpath):
                                sysFile((imgpath+imgnameN),delete=True)
                            sysFile(imagename,rename=(imgpath+imgnameN))
                            if imgnameN in getFileList(folder=ThePath):
                                sysFile((ThePath+imgnameN),delete=True)
                            sysFile((imgpath+imgnameN),move=(ThePath+imgnameN))
                            yyConvertImageFormat((ThePath+imgnameN), "jpg", 1)
                            #
                            imgnameNN=imgnameN.split('.')[0]+'.jpg'
                            if imgnameNN in getFileList(folder=ThePath2):
                                sysFile((ThePath2+imgnameNN),delete=True)
                            sysFile((ThePath+imgnameNN),copy=(ThePath2+imgnameNN))    
                            img = maya.OpenMaya.MImage()
                            img.readFromFile(ThePath2+imgnameNN)        
                            img.resize(128, 72)
                            textype=imgnameNN.split('.')[-1].lower()
                            img.writeToFile((ThePath2+imgnameNN),'jpg')
                            img.release()

                            self.nj_ChangeReSets()
                            #playblast( frame=[1001], format="image", viewer=False , w = 256, h = 144, fo = True, orn = False, cf = ThePath2+"/"+CamName+".iff")
                            '''
                            temp=internalVar(userTmpDir=True)
                            tempold=getFileList(filespec=(temp + "*.iff"))
                            dest=playblast( frame=[101], format="image", viewer=False , w = 256, h = 144, fo = True, orn = False, cf = ThePath2+"/"+fCam+".iff")
                            tempNew=getFileList(filespec=(temp + "*.iff"))
                            New=list(set(tempNew) - set(tempold))
                            if len(New) ==1:
                                sysFile(dest, delete = True)
                                sysFile(temp+New[0],mov=dest)
                            yyConvertImageFormat(ThePath2+"/"+fCam+".iff", "jpg", 1)
                            self.nj_ChangeReSets()
                            '''
    
                        if Cam.find("cam")==-1:
                            result=confirmDialog( title='Confirm', message='The selected object is not camera!!', button=['Yes'], defaultButton='Yes')
                            return
        if TheSc != optionMenu("EP", q = True, v = True):
            optionMenu( "EPNUM",label='SETS',e=1,v=TheSc )
            self.nj_ChangeReSets()
    
    def nj_ExceptSelectReCam(self):
        import maya.OpenMaya
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        questEP = optionMenu("EP", q = True, v = True)
        getCam=ls(sl=1)
        if getCam==[]:
            result=confirmDialog( title='Confirm', message='please select the camera!!', button=['Yes'], defaultButton='Yes')
            return
    
        cFrame=currentTime( q = True )
        TheSc=""
        if getCam!=[]:
            for Cam in getCam:
                if Cam!="frontShape" and Cam!="perspShape" and Cam!="sideShape" and Cam!="topShape":
                    if Cam.find("Shape")==-1:
                        if Cam.find("cam")!=-1:
                            
                            TheFileName=file(q=1,l=1)
                            TheFile=TheFileName[0].split("/")[-1].split(".")
                            if TheFile[-1]=="mb":
                                try:
                                    if TheFile[0].split('_')[0].lower() == 'nj': #TheFile[0]=="s" and TheFile[1]=="s":
                                        TheSc=TheFile[0][3:]
                                    else:
                                        result=confirmDialog( title='Confirm', message='This is not the  project file!!', button=['Yes'], defaultButton='Yes')
                                        return
                                except:
                                    pass
                            else:
                                result=confirmDialog( title='Confirm', message='Make sure this is .mb file!!', button=['Yes'], defaultButton='Yes')
                                return
                            CamName=Cam.replace("|","").replace("Shape","")
                            CamOver=Cam+".overscan"
                            setAttr(CamOver,1.3)
                            setAttr(Cam+".displayGateMaskColor",0,0,0)
                            setAttr(Cam+".displayGateMaskOpacity",1)
                            ThePath=serverPath+'Set/'+questEP+"/"+TheSc+'/'
                            ThePath2=serverPath+'Set/'+questEP+"/"+TheSc+"/images/"
                            sysFile(ThePath, makeDir=True )
                            sysFile(ThePath2, makeDir=True )
                            select (cl=1)
                            select (CamName)
                            fCam=CamName.split(':')[0]
                            file(ThePath+"/"+fCam+".ma",type="mayaAscii",pr=1,es=1)
                            lookThru (CamName)
                            #playblast( frame=[1001], format="image", viewer=False , w = 1280, h = 720, fo = True, orn = False, cf = ThePath+"/"+CamName+".iff")                       

                            texpath=ThePath+fCam+'.txt'
                            timeinfo=self.nj_timeRecord()
                            startinfo='Start time: '+timeinfo
                            self.nj_checkFileWrite(texpath , startinfo , addtion=0)
                            mm.eval("renderWindowRenderCamera render renderView "+CamName)
                            timeinfo=self.nj_timeRecord()
                            endinfo='End time: '+timeinfo
                            self.nj_checkFileWrite(texpath , endinfo , addtion=1)
                            imagename =mm.eval('optionVar -query "renderedImageName"')
                            imgshortName=imagename.split('/')[-1]
                            imgType= imgshortName.split('.')[-1].lower()
                            imgpath=imagename.split(imgshortName)[0]     
                            imgnameN=fCam+'.'+imgType
                            if imgnameN in getFileList(folder=imgpath):
                                sysFile((imgpath+imgnameN),delete=True)
                            sysFile(imagename,rename=(imgpath+imgnameN))
                            if imgnameN in getFileList(folder=ThePath):
                                sysFile((ThePath+imgnameN),delete=True)
                            sysFile((imgpath+imgnameN),move=(ThePath+imgnameN))
                            yyConvertImageFormat((ThePath+imgnameN), "jpg", 1)
                            #
                            imgnameNN=imgnameN.split('.')[0]+'.jpg'
                            if imgnameNN in getFileList(folder=ThePath2):
                                sysFile((ThePath2+imgnameNN),delete=True)
                            sysFile((ThePath+imgnameNN),copy=(ThePath2+imgnameNN))    
                            img = maya.OpenMaya.MImage()
                            img.readFromFile(ThePath2+imgnameNN)        
                            img.resize(128, 72)
                            textype=imgnameNN.split('.')[-1].lower()
                            img.writeToFile((ThePath2+imgnameNN),'jpg')
                            img.release()
                                                      
                            self.nj_ChangeReSets3()
                        
                        if Cam.find("cam")==-1:
                            result=confirmDialog( title='Confirm', message='The selected object is not a camera or name is incorrect !', button=['Yes'], defaultButton='Yes')
                            return
                    if Cam.find("Shape")!=-1:
                        result=confirmDialog( title='Confirm', message='please select the transform node!!', button=['Yes'], defaultButton='Yes')
                        return
            if TheSc != optionMenu("EP", q = True, v = True):
                optionMenu( "EPNUM",label='SETS',e=1,v=TheSc )
                self.nj_ChangeReSets()
    def nj_OpenReCamPath(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        questSets = optionMenu("EPNUM", q = True, v = True)
        
        questEP = optionMenu("EP", q = True, v = True)
    
        if questSets == '' and questEP == '':
            path="explorer"+' '+ serverPath+'Set/'+questEP+"\\"+questSets+"\\"
            os.system(path)
            
        else:
            path="explorer "+serverPath+'Set/'
            os.system(path)
            
    def nj_ImportReCam(self,Name):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        questSets = optionMenu("EPNUM", q = True, v = True)
        questEP = optionMenu("EP", q = True, v = True)
    
        AllObj=ls(sl=1)
        path=serverPath+'Set/'+questEP+"/"+questSets+"/"
        questMat=ls(Name.split(".")[0])
        if len(questMat)==0:
            try:
                file(path +Name.replace(".jpg",".ma"),i = True)
                lookThru (Name.split(".")[0])
            except:
                pass
        if len(questMat)!=0:
            result=confirmDialog( title='Confirm', message='there hase the same camera in the sences', button=['Yes'], defaultButton='Yes')
            return
    def getTheFileName(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        TheSc=""
        TheFileName=file(q=1,l=1)
        for TheFiles in TheFileName:
            if TheFiles.split(".")[-1]=="mb":
                try:
                    TheFile=TheFiles.split("/")[-1].split("_")[1]
                    if TheFile[0]=="s" and TheFile[1]=="s":
                        TheSc=TheFiles
                except:
                    pass
        return TheSc.split("/")[-1]
    
    def nj_ChangeReSets(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        questSets = optionMenu("EPNUM", q = True, v = True)
        questEP = optionMenu("EP", q = True, v = True)
    
    
    
        for m in range(1000):
            menuItem( "TheMenuItem"+str(m),e=1,en=0,label="        ")    
        TheFileList=getFileList( folder=serverPath+'Set/'+questEP+"/" )
        TheFileList.sort()
        if TheFileList!=None:
            for i in range(len(TheFileList)):
                menuItem( "TheMenuItem"+str(i),e=1,en=1,label=TheFileList[i])
    
    
    
        questEP = optionMenu("EP", q = True, v = True)
        questSets = optionMenu("EPNUM", q = True, v = True)
        for m in range(0,100):
            iconTextButton("Temp"+str(m), e=1,visible=0 ,style='iconAndTextVertical', image1="sphere.xpm")
            #popupMenu("ThePopup"+str(m))
            menuItem("TheObMenu"+str(m),e=1)
            menuItem("Cancle"+str(m),e=1)
    
        sysFile(serverPath+'Set/'+questEP+"/"+questSets+"/images/", makeDir=True )
    
        
        TheDateLib=[]
        mm.eval("string $GetName=python(\"optionMenu('EPNUM', q = True, v = True)\");")
        mm.eval("string $GetTheName=\"sk_\"+$GetName+\"_h_ms_tex.ma\";")
        TheScs=mm.eval("idmtService \"GetAnimsInAsset\" $GetTheName;")
        TheSc=TheScs.split("|")
        for Sc in TheSc:
            
            if Sc.split("_")[0]==questEP:
                TheDateLib.append(Sc)
        intField("TheNumber",e=1, value=len(TheDateLib),cc="from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ChangeReSets4()" )    
    
    
    
    
        try:
    
            TheUpDateSc=os.listdir(serverPath+'Set/'+questEP+"/"+questSets+"/images/")
            TheUpDateSc.sort()
            Thejpg=[]
    
    
            for i in range(len(TheUpDateSc)):
                if TheUpDateSc[i].split(".")[-1]=="jpg":
                    Thejpg.append(TheUpDateSc[i])    
            for j in range(len(Thejpg)):
                    theCommand='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ImportReCam(\"'+Thejpg[j]+'\")'
                    theCommand2='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ImageOk(\"'+Thejpg[j]+'\")'
                    theCommand3='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_CancleHook(\"'+Thejpg[j]+'\")'
                    iconTextButton("Temp"+str(j) ,e=1,visible=1,bgc=(1,1,1),style='iconAndTextVertical', image1=serverPath+'Set/'+questEP+"/"+questSets+"/images/"+Thejpg[j], label=Thejpg[j].split(".")[0],c=theCommand )
                    menuItem("TheObMenu"+str(j),e=1,l="This Camera is ok",c=theCommand2 )
                    menuItem("Cancle"+str(j),e=1,l="cancle the hook",c=theCommand3 )
    
            text( "TheNumber",e=1,bgc=(1,0.9,0.9),label=str(len(Thejpg)),align='center')
            questTheNum=intField("TheNumber", q=1,v=1 )
    
            if float(questTheNum)!=0:
                TheStr=str(float(len(Thejpg))/float(questTheNum)*100)+"%"
                text( "part",e=1,bgc=(0,1,0),label=TheStr,align='center')
            if float(questTheNum)==0:
                text( "part",e=1,bgc=(0,1,0),label="erro",align='center')
    
            try:
                    TheOKDateSc=os.listdir(serverPath+'Set/'+questEP+"/"+questSets+"/images/old/")
                    text( "TheOkNumber",e=1,bgc=(1,0.9,0.9),label=len(TheOKDateSc),align='center')
            except:
                    text( "TheOkNumber",e=1,bgc=(1,0.9,0.9),label=0,align='center')
        except:
            pass
        
        self.nj_ShowDateLibSc()
    
    def nj_ChangeReSets3(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        questSets = optionMenu("EPNUM", q = True, v = True)
        questEP = optionMenu("EP", q = True, v = True)
    
    
    
        for m in range(1000):
            menuItem( "TheMenuItem"+str(m),e=1,en=0,label="        ")    
        TheFileList=getFileList( folder=serverPath+'Set/'+questEP+"/" )
    
        if TheFileList!=None:
            for i in range(len(TheFileList)):
                menuItem( "TheMenuItem"+str(i),e=1,en=1,label=TheFileList[i])
    
        try:
            TheFileName=file(q=1,l=1)
            for TheFiles in TheFileName:
                if TheFiles.split(".")[-1]=="mb":
                    try:
                        TheFile=TheFiles.split("/")[-1].split("_")[1]
                        if TheFile[0]=="s" and TheFile[1]=="s":
                            TheSc=TheFile
                            
                    except:
                        pass
    
    
            optionMenu( "EPNUM",label='SETS',e=1,v=TheSc )
    
        except:
            pass
    
        questEP = optionMenu("EP", q = True, v = True)
        questSets = optionMenu("EPNUM", q = True, v = True)
        for m in range(0,100):
            iconTextButton("Temp"+str(m), e=1,visible=0 ,style='iconAndTextVertical', image1="sphere.xpm")
            #popupMenu("ThePopup"+str(m))
            menuItem("TheObMenu"+str(m),e=1)
            menuItem("Cancle"+str(m),e=1)
    
        sysFile(serverPath+'Set/'+questEP+"/"+questSets+"/images/", makeDir=True )
    
        TheDateLib=[]
        mm.eval("string $GetName=python(\"optionMenu('EPNUM', q = True, v = True)\");")
        mm.eval("string $GetTheName=\"sk_\"+$GetName+\"_h_ms_tex.ma\";")
        TheScs=mm.eval("idmtService \"GetAnimsInAsset\" $GetTheName;")
        TheSc=TheScs.split("|")
        for Sc in TheSc:
            
            if Sc.split("_")[0]==questEP:
                TheDateLib.append(Sc)
        intField("TheNumber",e=1, value=len(TheDateLib),cc="from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ChangeReSets4()" )    
    
    
    
        try:
    
            TheUpDateSc=os.listdir(serverPath+'Set/'+questEP+"/"+questSets+"/images/")
            print TheUpDateSc
            Thejpg=[]
    
    
            for i in range(len(TheUpDateSc)):
                if TheUpDateSc[i].split(".")[-1]=="jpg":
                    Thejpg.append(TheUpDateSc[i])    
            for j in range(len(Thejpg)):
                theCommand='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ImportReCam(\"'+Thejpg[j]+'\")'
                theCommand2='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ImageOk(\"'+Thejpg[j]+'\")'
                theCommand3='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_CancleHook(\"'+Thejpg[j]+'\")'
    
                iconTextButton("Temp"+str(j) ,e=1,visible=1,bgc=(1,1,1),style='iconAndTextVertical', image1=serverPath+'Set/'+questEP+"/"+questSets+"/images/"+Thejpg[j], label=Thejpg[j].split(".")[0],c=theCommand )
                #popupMenu("ThePopup"+str(j))
                menuItem("TheObMenu"+str(j),e=1,l="This Camera is ok",c=theCommand2 )
                menuItem("Cancle"+str(j),e=1,l="cancle the hook",c=theCommand3 )
    
            text( "TheNumber",e=1,bgc=(1,0.9,0.9),label=str(len(Thejpg)),align='center')
            questTheNum=intField("TheNumber", q=1,v=1 )
    
            if float(questTheNum)!=0:
                TheStr=str(float(len(Thejpg))/float(questTheNum)*100)+"%"
                text( "part",e=1,bgc=(0,1,0),label=TheStr,align='center')
            if float(questTheNum)==0:
                text( "part",e=1,bgc=(0,1,0),label="erro",align='center')
    
            try:
                TheOKDateSc=os.listdir(serverPath+'Set/'+questEP+"/"+questSets+"/images/old/")
                text( "TheOkNumber",e=1,bgc=(1,0.9,0.9),label=len(TheOKDateSc),align='center')
            except:
                text( "TheOkNumber",e=1,bgc=(1,0.9,0.9),label=0,align='center')
        except:
            pass
            #text( "TheNumber",e=1,bgc=(1,0.9,0.9),label=0,align='center')
    
            #text( "part",e=1,bgc=(0,1,0),label=0,align='center')
    
        self.nj_ShowDateLibSc()    
    
    def nj_ChangeReSets4(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        questSets = optionMenu("EPNUM", q = True, v = True)
        questEP = optionMenu("EP", q = True, v = True)
    
    
    
        for m in range(1000):
            menuItem( "TheMenuItem"+str(m),e=1,en=0,label="        ")    
        TheFileList=getFileList( folder=serverPath+'Set/'+questEP+"/" )
    
        if TheFileList!=None:
            for i in range(len(TheFileList)):
                menuItem( "TheMenuItem"+str(i),e=1,en=1,label=TheFileList[i])
    
    
    
        questEP = optionMenu("EP", q = True, v = True)
        questSets = optionMenu("EPNUM", q = True, v = True)
        for m in range(0,100):
            iconTextButton("Temp"+str(m), e=1,visible=0 ,style='iconAndTextVertical', image1="sphere.xpm")
            #popupMenu("ThePopup"+str(m))
            menuItem("TheObMenu"+str(m),e=1)
            menuItem("Cancle"+str(m),e=1)
    
        sysFile(serverPath+'Set/'+questEP+"/"+questSets+"/images/", makeDir=True )
    
        
    
    
    
    
    
        try:
    
            TheUpDateSc=os.listdir(serverPath+'Set/'+questEP+"/"+questSets+"/images/")
    
            Thejpg=[]
    
    
            for i in range(len(TheUpDateSc)):
                if TheUpDateSc[i].split(".")[-1]=="jpg":
                    Thejpg.append(TheUpDateSc[i])    
            for j in range(len(Thejpg)):
                    theCommand='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ImportReCam(\"'+Thejpg[j]+'\")'
                    theCommand2='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ImageOk(\"'+Thejpg[j]+'\")'
                    theCommand3='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_CancleHook(\"'+Thejpg[j]+'\")'
                    iconTextButton("Temp"+str(j) ,e=1,visible=1,bgc=(1,1,1),style='iconAndTextVertical', image1=serverPath+'Set/'+questEP+"/"+questSets+"/images/"+Thejpg[j], label=Thejpg[j].split(".")[0],c=theCommand )
                    menuItem("TheObMenu"+str(j),e=1,l="This Camera is ok",c=theCommand2 )
                    menuItem("Cancle"+str(j),e=1,l="cancle the hook",c=theCommand3 )
    
            text( "TheNumber",e=1,bgc=(1,0.9,0.9),label=str(len(Thejpg)),align='center')
            questTheNum=intField("TheNumber", q=1,v=1 )
            if float(questTheNum)!=0:
                TheStr=str(float(len(Thejpg))/float(questTheNum)*100)+"%"
                text( "part",e=1,bgc=(0,1,0),label=TheStr,align='center')
            if float(questTheNum)==0:
                text( "part",e=1,bgc=(0,1,0),label="erro",align='center')
    
            try:
                    TheOKDateSc=os.listdir(serverPath+'Set/'+questEP+"/"+questSets+"/images/old/")
                    text( "TheOkNumber",e=1,bgc=(1,0.9,0.9),label=len(TheOKDateSc),align='center')
            except:
                    text( "TheOkNumber",e=1,bgc=(1,0.9,0.9),label=0,align='center')
        except:
            pass
        
    
        self.nj_ShowDateLibSc()
    
    def nj_ChangeReSets2(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        try:
                
            TheSc=""
            TheFileName=file(q=1,l=1)
            for TheFiles in TheFileName:
                if TheFiles.split(".")[-1]=="mb":
                    try:
                        TheFile=TheFiles.split("/")[-1].split("_")[1]
                        if TheFile[0]=="s" and TheFile[1]=="s":
                            TheSc=TheFile
                    except:
                        pass
    
            TheAnFileName=file(q=1,shn=1,sn=1)
            if TheAnFileName.find("an")!=-1:
                questEP=TheAnFileName.split("_")[1]
            if TheAnFileName.find("an")==-1:
                #questEP="201"
                questEP="CA"
            questSets=TheSc
            sysFile("Z:/Projects/Strawberry/Strawberry_Scratch/TD/animation/"+questEP+"/"+questSets+"/images/", makeDir=True )
            optionMenu( "EPNUM",label='SETS',e=1,v=questSets )
            optionMenu( "EP",label='EP',e=1,v=questEP )
            questEP = optionMenu("EP", q = True, v = True)
            questSets = optionMenu("EPNUM", q = True, v = True)
    
        except:
            pass
        self.nj_ChangeReSets()
        self.nj_ShowDateLibSc()
    def getCurrentUser(self):
        curUser = mm.eval("getenv username;")
        return curUser
    
    def nj_ImageOk(self,Name):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        user = self.getCurrentUser()
        print user
        #if user == "huangbi" or user == "qinsaibo" or user == "lishuaiwei":
        if user == "huangbi" or user == "qinsaibo" or user == "lishuaiwei":
            questSets = optionMenu("EPNUM", q = True, v = True)
            questEP = optionMenu("EP", q = True, v = True)
            path=serverPath+'Set/'+questEP+"/"+questSets+"/images/"+Name
            path02=serverPath+'Set/'+questEP+"/"+questSets+"/images/old/"+Name
    
            questFile=os.path.exists(path02)
            if questFile!=1:
                TheOkPath=path.replace("/","\\")+"@"
                print TheOkPath
                TheFile="D:/TheOkImage.txt"
                UPTX=TheOkPath
                try:
                    f = open(TheFile, "w")
                    f.write(UPTX)
                    f.close()
                except:
                    pass
                os.system(r'"Z:\Resource\Support\Maya\projects\Strawberry2\addimage\addimage.exe"')
                self.nj_ChangeReSets()
    def nj_CancleHook(self,Name):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        user = self.getCurrentUser()
        if user == "huangbi" or user == "qinsaibo" or user == "lishuaiwei":
            try:
                questSets = optionMenu("EPNUM", q = True, v = True)
                questEP = optionMenu("EP", q = True, v = True)
                path01=serverPath+'Set/'+questEP+"/"+questSets+"/images/"+Name
                path02=serverPath+'Set/'+questEP+"/"+questSets+"/images/old/"+Name
                questFile=os.path.exists(path02)
                if questFile!=0:
                    os.remove(path01) 
                    dfu.copy_file(path02, path01)
                    os.remove(path02) 
                    self.nj_ChangeReSets()
            except:
                pass
    def nj_ShowDateLibSc(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        questEP = optionMenu("EP", q = True, v = True)
        TheDateLib=[]
        mm.eval("string $GetName=python(\"optionMenu('EPNUM', q = True, v = True)\");")
        mm.eval("string $GetTheName=\"sk_\"+$GetName+\"_h_ms_tex.ma\";")
        TheScs=mm.eval("idmtService \"GetAnimsInAsset\" $GetTheName;")
        TheSc=TheScs.split("|")
        textScrollList("TheDateLibSc",e=1,ra=1)
        for Sc in TheSc:
            
            if Sc.split("_")[0]==questEP:
                TheDateLib.append(Sc)
                textScrollList("TheDateLibSc",e=1,append=Sc)
    
    def nj_ChangeColor(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        getTheSelect=textScrollList("TheDateLibSc",q=1,si=1)
        questSets = optionMenu("EPNUM", q = True, v = True)
        questEP = optionMenu("EP", q = True, v = True)
        path=serverPath+'Set/'+questEP+"/"+questSets+"/images/"
        TheUpDateSc=os.listdir(path)
        Thejpg=[]
    
        
        for i in range(len(TheUpDateSc)):
            if TheUpDateSc[i].split(".")[-1]=="jpg":
                Thejpg.append(TheUpDateSc[i])    
        for j in range(len(Thejpg)):
                theCommand='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ImportReCam(\"'+Thejpg[j]+'\")'
                theCommand2='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ImageOk(\"'+Thejpg[j]+'\")'
                theCommand3='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_CancleHook(\"'+Thejpg[j]+'\")'
                if Thejpg[j].find(getTheSelect[0])==-1:
                    iconTextButton("Temp"+str(j) ,e=1,visible=1,bgc=(1,1,1),style='iconAndTextVertical', image1=serverPath+'Set/'+questEP+"/"+questSets+"/images/"+Thejpg[j], label=Thejpg[j].split(".")[0],c=theCommand )
                if Thejpg[j].find(getTheSelect[0])!=-1:
                    iconTextButton("Temp"+str(j) ,e=1,visible=1,bgc=(1,0,0),style='iconAndTextVertical', image1=serverPath+'Set/'+questEP+"/"+questSets+"/images/"+Thejpg[j], label=Thejpg[j].split(".")[0],c=theCommand )
    
                menuItem("TheObMenu"+str(j),e=1,l="This Camera is ok",c=theCommand2 )
                menuItem("Cancle"+str(j),e=1,l="cancle the hook",c=theCommand3 )
    
    def nj_SkReCamTools(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectTDPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])         
        EPNum=[6055,6065]
        if window ("nj_SkReCamWin",ex=1):
            deleteUI( "nj_SkReCamWin", window=True )
        window("nj_SkReCamWin",title=projectInfo+ "ReCam Tools", iconName="Short Name", widthHeight=(600, 700),menuBar=1)
        menu(l= "Eidt")
        menuItem(l="Reset",command="")
        menuItem(l="",command="")
        menu(l= "Help")
        menuItem(l="Help",command="mm.eval('system(\"loadZ:/Resource/Support/Maya/help/Help_NJExceptCamTools.mht\")')")
        menuItem(l="About",command="")
        form = formLayout()
        rowColumnLayout("ROW",numberOfColumns=6,cw=[(1,80),(2,300),(3,100),(4,100),(5,100),(6,100)])
        optionMenu( "EP",label='EP',cc="nj_ChangeReSets3()" )
        
        for i in range(EPNum[0],EPNum[1]):
            menuItem( i,label=i)
    #    for i in string.uppercase:
    #        menuItem( 'B'+i,label='B'+i)
    #    for i in string.uppercase:
    #        menuItem( 'C'+i,label='C'+i)
        questEP = optionMenu("EP", q = True, v = True)
    
        optionMenu( "EPNUM",label='SETS',cc="nj_ChangeReSets()" )
        TheFileList=getFileList( folder=serverPath+'Set/'+questEP+"/" )
        for m in range(1000):
            menuItem( "TheMenuItem"+str(m),en=0,label="        ")    
        if TheFileList!=None:
            for i in range(len(TheFileList)):
                menuItem( "TheMenuItem"+str(i),e=1,en=1,label=TheFileList[i])
    
    
        button("OKBUTTON",l = "export all cam", c = "from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ExceptReCam()")
    
        button("OKBUTTON02",l = "exp selected cam", c = "from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ExceptSelectReCam()")
        button("OKBUTTON03",l = "open path", c = "from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_OpenReCamPath()")
        intField("TheNumber", value=100,cc="from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ChangeReSets4()" )
    
        questSets = optionMenu("EPNUM", q = True, v = True)
    
        setParent("..")
    
        rowColumnLayout("ROW4",numberOfColumns=1,cw=[(1,80)])
        textScrollList("TheDateLibSc",w=128,h=600,allowMultiSelection=True,numberOfRows=8,selectCommand="from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ChangeColor()")
        setParent("..")
    
    
        sysFile(serverPath+'Set/'+questEP+"/"+questSets+"/images/", makeDir=True )
    
        TheUpDateSc = []
        if os.path.isdir(serverPath+'Set/'+questEP+"/"+questSets+"/images/"):
            TheUpDateSc=os.listdir(serverPath+'Set/'+questEP+"/"+questSets+"/images/")
        TheOKDateSc = [];
        if os.path.isdir(serverPath+'Set/'+questEP+"/"+questSets+"/images/"):
            TheOKDateSc=os.listdir(serverPath+'Set/'+questEP+"/"+questSets+"/images/")
    
        rowColumnLayout("ROW2",numberOfColumns=3,cw=[(1,120),(2,400),(3,120)])
        text( "TheNumber",label='number')
        text( "part",label='part')
        text( "TheOkNumber",label='0')
    
        setParent("..")
    
        rowColumnLayout("ROW3",numberOfColumns=3,cw=[(1,120),(2,400),(3,120)])
        text( "TheNumber1",label="number",align='center')
        text( "part1",label="part",align='center')
        text( "TheOkNumber1",label="ok",align='center')
    
        setParent("..")
    
        scrollLayout("Grid",horizontalScrollBarThickness=16,verticalScrollBarThickness=16)
        rowColumnLayout( numberOfColumns=5 ,columnWidth=[(1, 128), (2, 128), (3, 128), (4, 128), (5, 128)] )
        for m in range(0,300):
            iconTextButton("Temp"+str(m),h=90, visible=0 ,style='iconAndTextVertical', image1="sphere.xpm")
            popupMenu("ThePopup"+str(m))
            menuItem("TheObMenu"+str(m))
            menuItem("Cancle"+str(m))
    
        Thejpg=[]
        for i in range(len(TheUpDateSc)):
            if TheUpDateSc[i].split(".")[-1]=="jpg":
                Thejpg.append(TheUpDateSc[i])    
        for j in range(len(Thejpg)):
            theCommand='nj_ImportReCam(\"'+Thejpg[j]+'\")'
            theCommand2='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_ImageOk(\"'+Thejpg[j]+'\")'
            theCommand3='from idmt.maya.py_common import nj_HbExceptCam\nreload(nj_HbExceptCam)\nnj_HbExceptCam.nj_HbExceptCam().nj_CancleHook(\"'+Thejpg[j]+'\")'
    
            iconTextButton("Temp"+str(j) ,e=1,visible=1,bgc=(1,1,1),style='iconAndTextVertical', image1=serverPath+'Set/'+questEP+"/"+questSets+"/images/"+Thejpg[j], label=Thejpg[j].split(".")[0],c=theCommand )
            popupMenu("ThePopup"+str(j))
            menuItem("TheObMenu"+str(j),e=1,l="This Camera is ok",c=theCommand2 )
            menuItem("Cancle"+str(j),e=1,l="cancle the hook",c=theCommand3 )
    
        text( "TheNumber",e=1,bgc=(1,0.9,0.9),label=str(len(Thejpg)),align='center')
    
        questTheNum=intField("TheNumber", q=1,v=1 )
        if float(questTheNum)!=0:
            TheStr=str(float(len(Thejpg))/float(questTheNum)*100)+"%"
            text( "part",e=1,bgc=(0,1,0),label=TheStr,align='center')
        if float(questTheNum)==0:
            text( "part",e=1,bgc=(0,1,0),label="erro",align='center')
        try:
            TheOKDateSc=os.listdir(serverPath+'Set/'+questEP+"/"+questSets+"/images/old/")
            text( "TheOkNumber",e=1,bgc=(1,0.9,0.9),label=len(TheOKDateSc),align='center')
        except:
            text( "TheOkNumber",e=1,bgc=(1,0.9,0.9),label=0,align='center')
        setParent( ".." )
        formLayout( form, edit=True, 
        attachForm=(("ROW", "top", 0), ("ROW", "left", 0),("ROW4", "top", 100), ("ROW4", "right", 20),("ROW3", "top", 35), ("ROW3", "left", 10),("ROW2", "top", 70), ("ROW2", "left", 10),("Grid","top", 100),("Grid","left", 0),("Grid","right", 0),("Grid","bottom", 0)))
        showWindow( "nj_SkReCamWin" )
        self.nj_ChangeReSets2()
 

    def nj_checkFileWrite(self,path , info , addtion=0):
        print u'>>>>>>[write]'
        print path
        sysFile(os.path.dirname(path), makeDir=True)
        if addtion == 1:
            info = self.nj_checkFileRead(path)[0] + '\r\n'+'   '+'\r\n'+info
        txt = open(path, 'w')
        try:
            txt.writelines(info)
            print('Writing........')
        finally:
            txt.close()

    def nj_checkFileRead(self,path):
        print u'>>>>>>[read]'
        print path
        sysFile(os.path.dirname(path), makeDir=True)
        txt = open(os.path.normpath(path), 'r')
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

    def nj_timeRecord(self):
        import time
        info=time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))     
        return info            

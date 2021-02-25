# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as mo
import os
import shutil
import distutils.file_util as dfu


# projectInfo = 'ZoomWhiteDolphin'

class sk_hbExceptCam(object):
    def __init__(self):
        pass

    def convertImageFormat(self, fileName, outputFormat, delete):
        # function: convert image format in place
        # parse argrument
        try:
            test = fileName.split(".iff")[1]
            fileBaseName = fileName.split(".iff")[0]
        except:
            raise Exception("Format is not iff.")
        
        # open
        image = mo.MImage()
        try:
            image.readFromFile(fileName)
        except:
            try:
                image.readFromFile(fileName)
            except:
                # raise Exception("Read error.")
                #mc.warning(unicode('===【截图创建过程失败，请再试一次】===', 'utf8'))
                mc.warning(u'===【截图创建过程失败，请再试一次】===')
        
        # convert & save
        try:
            image.writeToFile (fileBaseName + "." + outputFormat, "bmp")
        except:
            # raise Exception("Write error.")
            #mc.warning(unicode('===【截图保存过程失败，请再试一次】===', 'utf8'))
            mc.warning(u'===【截图保存过程失败，请再试一次】===', 'utf8')
            
        
        if delete == 1:
            try:
                os.remove(fileName)
            except:
                pass


    # need
    def HbExceptSelectReCam(self, projectInfo, all=0, scrFrame=1001 , batchUpadate = 0 ,camSelect = 0,shotInfo = []):
        # questEP = mc.optionMenu("EP", q = True, v = True)
        if all == 0:
            getCam = mc.ls(sl=1)
        else:
            getCam = mc.listCameras(p=True)
        if getCam == []:
            result = mc.confirmDialog(title='Confirm', message='please select the camera!!', button=['Yes'], defaultButton='Yes')
            return
        if getCam != []:
            for Cam in getCam:
                # cam_aaa_bbb or cam_aaa_bbb_baked
                CamName = ''
                if '_' in Cam and 'cam' in Cam and (len(Cam.split('_')) == 3 or len(Cam.split('_')) == 4 or len(Cam.split('_')) == 5 ) :
                    questEP = Cam.split('_')[1]
                    # Cam = getCam[0]
                    # Cam = getCam[1]
                    if Cam != "frontShape" and Cam != "perspShape" and Cam != "sideShape" and Cam != "topShape":
                        if Cam.find("Shape") == -1:
                            if Cam.find("cam") != -1:
                                # DOD5很慢，似乎没用，屏蔽by黄仲维，20141230
                                #TheSc = ""
                                #TheFileName = mc.file(q=1, l=1)
                                #for TheFiles in TheFileName:
                                #    if TheFiles.split(".")[-1] == "ma":
                                #        try:
                                #            TheFile = TheFiles.split("/")[-1].split("_")[1]
                                #            if TheFile[0] == "s" :
                                #                TheSc = TheFile
                                #        except:
                                #            pass
                                CamName = Cam.replace("|", "").replace("Shape", "")
                TheSc = ''
                if camSelect:
                    CamName = mc.ls(sl = 1,l=1)
                    questEP = str(shotInfo[0])
                    #questEP = CamName[0].split('|')[-1].split('_')[1]
                    TheSc = ''
                    
                CamOver = Cam + ".overscan"
                mc.setAttr(CamOver, 1.3)
                mc.setAttr(Cam + ".displayGateMaskColor", 0, 0, 0)
                mc.setAttr(Cam + ".displayGateMaskOpacity", 1)
                ThePath = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + TheSc
                ThePath2 = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + TheSc + "/images"
                mc.sysFile(ThePath, makeDir=True)
                mc.sysFile(ThePath2, makeDir=True)
                mc.select (cl=1)
                mc.select (CamName)
                if not camSelect:
                    CamName_validCharactor = CamName.split(":")[-1]
                if camSelect:
                    CamName_validCharactor = 'cam_' + str(shotInfo[0]) + '_' + str(shotInfo[1]) + '_baked'
                print '-----'
                print (ThePath + "/" + CamName_validCharactor + ".ma")
                check = mc.file(ThePath + "/" + CamName_validCharactor + ".ma", type="mayaAscii", pr=1, es=1,force = 1)
                # 开始拍照,如果是batch后台模式，则不更新图片
                if batchUpadate == 0:
                    mc.lookThru(CamName)
                    # mc.playblast( frame=[1001], format="image", viewer=False , w = 1280, h = 720, fo = True, orn = False, cf = ThePath+"/"+CamName+".iff")
                    temp = mc.internalVar(userTmpDir=True)
                    tempold = mc.getFileList(filespec=(temp + "*.iff"))
                    dest = mc.playblast(frame=[scrFrame], format="image", viewer=False , w=1280, h=720, fo=True, orn=True, cf=ThePath + "/" + CamName_validCharactor + ".iff")
                    tempNew = mc.getFileList(filespec=(temp + "*.iff"))
                    New = list(set(tempNew) - set(tempold))
                    if len(New) == 1:
                        mc.sysFile(dest, delete=True)
                        mc.sysFile(temp + New[0], mov=dest)
                    self.convertImageFormat(ThePath + "/" + CamName_validCharactor + ".iff", "bmp", 1)
                    # mc.playblast( frame=[1001], format="image", viewer=False , w = 256, h = 144, fo = True, orn = False, cf = ThePath2+"/"+CamName+".iff")
                    temp = mc.internalVar(userTmpDir=True)
                    tempold = mc.getFileList(filespec=(temp + "*.iff"))
                    dest = mc.playblast(frame=[scrFrame], format="image", viewer=False , w=256, h=144, fo=True, orn=True, cf=ThePath2 + "/" + CamName_validCharactor + ".iff")
                    tempNew = mc.getFileList(filespec=(temp + "*.iff"))
                    New = list(set(tempNew) - set(tempold))
                    if len(New) == 1:
                        mc.sysFile(dest, delete=True)
                        mc.sysFile(temp + New[0], mov=dest)
                    self.convertImageFormat(ThePath2 + "/" + CamName_validCharactor + ".iff", "bmp", 1)
                # 更新用
                try:
                    self.HbChangeReSets3(projectInfo, questEP)
                except:
                    pass

            if Cam.find("cam") == -1 and not camSelect:
                result = mc.confirmDialog(title='Confirm', message='The selected object is not camera!!', button=['Yes'], defaultButton='Yes')
                return
        if Cam.find("Shape") != -1:
            result = mc.confirmDialog(title='Confirm', message='please select the transform node!!', button=['Yes'], defaultButton='Yes')
            return

                    
    # need        
    def HbOpenReCamPath(self, projectInfo):
        questSets = mc.optionMenu("EPNUM", q=True, v=True)
        questEP = mc.optionMenu("EP", q=True, v=True)
        path = "explorer \\\\file-cluster\\GDC\\Projects\\" + projectInfo + "\\" + projectInfo + "_Scratch\\TD\\SetCam\\" + questEP + "\\"
        # path="explorer \\\\file-cluster\\GDC\\Projects\\" + projectInfo + "\\" + projectInfo + "_Scratch\\TD\\SetCam\\"+questEP+"\\"+questSets+"\\" 
        os.system(path)
        
    # need
    def HbImportReCam(self, projectInfo, Name):
        questSets = mc.optionMenu("EPNUM", q=True, v=True)
        questEP = mc.optionMenu("EP", q=True, v=True)
    
        AllObj = mc.ls(sl=1)
        path = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/"
        questMat = mc.ls(Name.split(".")[0])
        if len(questMat) == 0:
            try:
                file(path + Name.replace(".bmp", ".mb"), i=True)
                mc.lookThru (Name.split(".")[0])
            except:
                pass
        if len(questMat) != 0:
            result = mc.confirmDialog(title='Confirm', message='there hase the same camera in the sences', button=['Yes'], defaultButton='Yes')
            return
        
        
    def getTheFileName(self, projectInfo):
            TheSc = ""
            TheFileName = file(q=1, l=1)
            for TheFiles in TheFileName:
                # TheFiles = TheFileName[0]
                if TheFiles.split(".")[-1] == "ma":
                    try:
                        TheFile = TheFiles.split("/")[-1].split("_")[1]
                        if TheFile[0] == "s" :
                            TheSc = TheFiles
                    except:
                        pass
            return TheSc.split("/")[-1]
    
    # need
    def HbChangeReSets(self, projectInfo):
        questSets = mc.optionMenu("EPNUM", q=True, v=True)
        questEP = mc.optionMenu("EP", q=True, v=True)
        for m in range(1000):
            mc.menuItem("TheMenuItem" + str(m), e=1, en=0, label="        ")    
        TheFileList = mc.getFileList(folder=("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/"))
    
        if TheFileList != None:
            for i in range(len(TheFileList)):
                mc.menuItem("TheMenuItem" + str(i), e=1, en=1, label=TheFileList[i])
              
    
        questEP = mc.optionMenu("EP", q=True, v=True)
        questSets = mc.optionMenu("EPNUM", q=True, v=True)
        for m in range(0, 100):
            mc.iconTextButton("Temp" + str(m), e=1, visible=0 , style='iconAndTextVertical', image1="sphere.xpm")
            # mc.popupMenu("ThePopup"+str(m))
            mc.menuItem("TheObMenu" + str(m), e=1)
            mc.menuItem("Cancle" + str(m), e=1)

        mc.sysFile("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/", makeDir=True)

        TheDateLib = []

        mel.eval("string $GetName=python(\"mc.optionMenu('EPNUM', q = True, v = True)\");")
        mel.eval("string $GetTheName=\"sk_\"+$GetName+\"_h_ms_tex.mb\";")

        TheScs = mel.eval("idmtService \"GetAnimsInAsset\" $GetTheName;")
        TheSc = TheScs.split("|")
        

        for Sc in TheSc:
        
            if Sc.split("_")[0] == questEP:
                TheDateLib.append(Sc)
        mc.intField("TheNumber", e=1, value=len(TheDateLib), cc="HbChangeReSets4()")    

        try:
    
            TheUpDateSc = os.listdir("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/")
    
            TheBmp = []
    
            for i in range(len(TheUpDateSc)):
                if TheUpDateSc[i].split(".")[-1] == "bmp":
                    TheBmp.append(TheUpDateSc[i])    
            for j in range(len(TheBmp)):
                    theCommand = 'HbImportReCam(\"' + TheBmp[j] + '\")'
                    theCommand2 = 'HbImageOk(\"' + TheBmp[j] + '\")'
                    theCommand3 = 'HbCancleHook(\"' + TheBmp[j] + '\")'
                    mc.iconTextButton("Temp" + str(j) , e=1, visible=1, bgc=(1, 1, 1), style='iconAndTextVertical', image1="Z:/Projects/ZoomWhiteDolphin/ZoomWhiteDolphin_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/" + TheBmp[j], label=TheBmp[j].split(".")[0], c=theCommand)
                    mc.menuItem("TheObMenu" + str(j), e=1, l="This Camera is ok", c=theCommand2)
                    mc.menuItem("Cancle" + str(j), e=1, l="cancle the hook", c=theCommand3)
    
            mc.text("TheNumber", e=1, bgc=(1, 0.9, 0.9), label=str(len(TheBmp)), align='center')
            questTheNum = mc.intField("TheNumber", q=1, v=1)
    
            if float(questTheNum) != 0:
                TheStr = str(float(len(TheBmp)) / float(questTheNum) * 100) + "%"
                mc.text("part", e=1, bgc=(0, 1, 0), label=TheStr, align='center')
            if float(questTheNum) == 0:
                mc.text("part", e=1, bgc=(0, 1, 0), label="erro", align='center')

            try:
                TheOKDateSc = os.listdir("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/old/")
                mc.text("TheOkNumber", e=1, bgc=(1, 0.9, 0.9), label=len(TheOKDateSc), align='center')
            except:
                mc.text("TheOkNumber", e=1, bgc=(1, 0.9, 0.9), label=0, align='center')
        except:
            pass
        self.HbShowDateLibSc(projectInfo)

    
    # need
    def HbChangeReSets3(self, projectInfo, questEP='101'):
        
        # questSets = mc.optionMenu("EPNUM", q=True, v=True)
        questEP = mc.optionMenu("EP", q=True, v=True)
        
        for m in range(1000):
            mc.menuItem("TheMenuItem" + str(m), e=1, en=0, label="        ")    
        TheFileList = mc.getFileList(folder="//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/")
    
        if TheFileList != None:
            for i in range(len(TheFileList)):
                mc.menuItem("TheMenuItem" + str(i), e=1, en=1, label=TheFileList[i])
    
        try:
            TheFileName = file(q=1, l=1)
            for TheFiles in TheFileName:
                if TheFiles.split(".")[-1] == "mb":
                    try:
                        TheFile = TheFiles.split("/")[-1].split("_")[1]
                        if TheFile[0] == "s" and TheFile[1] == "s":
                            TheSc = TheFile
                        else:
                            TheSc = TheFile
                  
                    except:
                        pass
    
            mc.optionMenu("EPNUM", label='SETS', e=1, v=TheSc)
    
        except:
            pass
    
        questEP = mc.optionMenu("EP", q=True, v=True)
        questSets = mc.optionMenu("EPNUM", q=True, v=True)
        for m in range(0, 100):
            mc.iconTextButton("Temp" + str(m), e=1, visible=0 , style='iconAndTextVertical', image1="sphere.xpm")
            # mc.popupMenu("ThePopup"+str(m))
            mc.menuItem("TheObMenu" + str(m), e=1)
            mc.menuItem("Cancle" + str(m), e=1)
    
        mc.sysFile("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/", makeDir=True)
    
        TheDateLib = []
        mel.eval("string $GetName=python(\"mc.optionMenu('EPNUM', q = True, v = True)\");")
        mel.eval("string $GetTheName=\"sk_\"+$GetName+\"_h_ms_tex.mb\";")
        TheScs = mel.eval("idmtService \"GetAnimsInAsset\" $GetTheName;")
        TheSc = TheScs.split("|")
        for Sc in TheSc:
            if Sc.split("_")[0] == questEP:
                TheDateLib.append(Sc)
        mc.intField("TheNumber", e=1, value=len(TheDateLib), cc="HbChangeReSets4()")    

        try:
    
            TheUpDateSc = os.listdir("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/")

            TheBmp = []
    
            for i in range(len(TheUpDateSc)):
                if TheUpDateSc[i].split(".")[-1] == "bmp":
                    TheBmp.append(TheUpDateSc[i])    
            for j in range(len(TheBmp)):
                theCommand = 'HbImportReCam(\"' + TheBmp[j] + '\")'
                theCommand2 = 'HbImageOk(\"' + TheBmp[j] + '\")'
                theCommand3 = 'HbCancleHook(\"' + TheBmp[j] + '\")'
    
                mc.iconTextButton("Temp" + str(j) , e=1, visible=1, bgc=(1, 1, 1), style='iconAndTextVertical', image1=("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/" + TheBmp[j]), label=TheBmp[j].split(".")[0], c=theCommand)
                # popupMenu("ThePopup"+str(j))
                mc.menuItem("TheObMenu" + str(j), e=1, l="This Camera is ok", c=theCommand2)
                mc.menuItem("Cancle" + str(j), e=1, l="cancle the hook", c=theCommand3)
    
            mc.text("TheNumber", e=1, bgc=(1, 0.9, 0.9), label=str(len(TheBmp)), align='center')
            questTheNum = mc.intField("TheNumber", q=1, v=1)
    
            if float(questTheNum) != 0:
                TheStr = str(float(len(TheBmp)) / float(questTheNum) * 100) + "%"
                mc.text("part", e=1, bgc=(0, 1, 0), label=TheStr, align='center')
            if float(questTheNum) == 0:
                mc.text("part", e=1, bgc=(0, 1, 0), label="erro", align='center')
    
            try:
                TheOKDateSc = os.listdir("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/old/")
                mc.text("TheOkNumber", e=1, bgc=(1, 0.9, 0.9), label=len(TheOKDateSc), align='center')
            except:
                mc.text("TheOkNumber", e=1, bgc=(1, 0.9, 0.9), label=0, align='center')
        except:
            pass
            # text( "TheNumber",e=1,bgc=(1,0.9,0.9),label=0,align='center')
    
            # text( "part",e=1,bgc=(0,1,0),label=0,align='center')
    
        self.HbShowDateLibSc(projectInfo)   
         
    # need
    def HbChangeReSets4(self, projectInfo):
        questSets = mc.optionMenu("EPNUM", q=True, v=True)
        questEP = mc.optionMenu("EP", q=True, v=True)
    
        for m in range(1000):
            mc.menuItem("TheMenuItem" + str(m), e=1, en=0, label="        ")    
        TheFileList = mc.getFileList(folder="//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/")
    
        if TheFileList != None:
            for i in range(len(TheFileList)):
                mc.menuItem("TheMenuItem" + str(i), e=1, en=1, label=TheFileList[i])
    
        questEP = mc.optionMenu("EP", q=True, v=True)
        questSets = mc.optionMenu("EPNUM", q=True, v=True)
        for m in range(0, 100):
            mc.iconTextButton("Temp" + str(m), e=1, visible=0 , style='iconAndTextVertical', image1="sphere.xpm")
            # popupMenu("ThePopup"+str(m))
            mc.menuItem("TheObMenu" + str(m), e=1)
            mc.menuItem("Cancle" + str(m), e=1)
    
        mc.sysFile("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/", makeDir=True)
    
        try:
    
            TheUpDateSc = os.listdir("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/")
            TheBmp = []
    
            for i in range(len(TheUpDateSc)):
                if TheUpDateSc[i].split(".")[-1] == "bmp":
                    TheBmp.append(TheUpDateSc[i])    
            for j in range(len(TheBmp)):
                theCommand = 'HbImportReCam(\"' + TheBmp[j] + '\")'
                theCommand2 = 'HbImageOk(\"' + TheBmp[j] + '\")'
                theCommand3 = 'HbCancleHook(\"' + TheBmp[j] + '\")'
                mc.iconTextButton("Temp" + str(j) , e=1, visible=1, bgc=(1, 1, 1), style='iconAndTextVertical', image1=("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/" + TheBmp[j]), label=TheBmp[j].split(".")[0], c=theCommand)
                mc.menuItem("TheObMenu" + str(j), e=1, l="This Camera is ok", c=theCommand2)
                mc.menuItem("Cancle" + str(j), e=1, l="cancle the hook", c=theCommand3)
    
            mc.text("TheNumber", e=1, bgc=(1, 0.9, 0.9), label=str(len(TheBmp)), align='center')
            questTheNum = mc.intField("TheNumber", q=1, v=1)
            if float(questTheNum) != 0:
                TheStr = str(float(len(TheBmp)) / float(questTheNum) * 100) + "%"
                mc.text("part", e=1, bgc=(0, 1, 0), label=TheStr, align='center')
            if float(questTheNum) == 0:
                mc.text("part", e=1, bgc=(0, 1, 0), label="erro", align='center')
    
            try:
                TheOKDateSc = os.listdir("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/old/")
                mc.text("TheOkNumber", e=1, bgc=(1, 0.9, 0.9), label=len(TheOKDateSc), align='center')
            except:
                mc.text("TheOkNumber", e=1, bgc=(1, 0.9, 0.9), label=0, align='center')
        except:
            pass
    
        self.HbShowDateLibSc(projectInfo)
    
    # need
    def HbChangeReSets2(self, projectInfo):
        try:
            TheSc = ""
            TheFileName = mc.file(q=1, l=1)
            for TheFiles in TheFileName:
                if TheFiles.split(".")[-1] == "mb":
                    try:
                        TheFile = TheFiles.split("/")[-1].split("_")[1]
                        if TheFile[0] == "s" and TheFile[1] == "s":
                            TheSc = TheFile
                        else:
                            TheSc = TheFile
                    except:
                        pass
            TheAnFileName = mc.file(q=1, shn=1, sn=1)
            if TheAnFileName.find("an") != -1:
                questEP = TheAnFileName.split("_")[1]
            if TheAnFileName.find("an") == -1:
                # questEP="201"
                questEP = "301"
            questSets = TheSc

            mc.sysFile("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/", makeDir=True)
            mc.optionMenu("EPNUM", label='SETS', e=1, v=questSets)
            mc.optionMenu("EP", label='EP', e=1, v=questEP)
            questEP = mc.optionMenu("EP", q=True, v=True)

            questSets = mc.optionMenu("EPNUM", q=True, v=True)
        except:
            pass

        self.HbChangeReSets(projectInfo)
        self.HbShowDateLibSc(projectInfo)

        
    # need
    def getCurrentUser(self, projectInfo):
        curUser = mel.eval("getenv username;")
        return curUser
    
    # need
    def HbImageOk(self, projectInfo, Name):
        user = self.getCurrentUser()

        if user == "huangbi" or user == "qinsaibo" or user == "lishuaiwei":
            questSets = mc.optionMenu("EPNUM", q=True, v=True)
            questEP = mc.optionMenu("EP", q=True, v=True)
            path = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/" + Name
            path02 = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/old/" + Name
    
            questFile = os.path.exists(path02)
            if questFile != 1:
                TheOkPath = path.replace("/", "\\") + "@"

                TheFile = "D:/TheOkImage.txt"
                UPTX = TheOkPath
                try:
                    f = open(TheFile, "w")
                    f.write(UPTX)
                    f.close()
                except:
                    pass
                os.system(r'"Z:\Resource\Support\Maya\projects\Strawberry2\addimage\addimage.exe"')
                self.HbChangeReSets(projectInfo)
    
    # need
    def HbCancleHook(self, projectInfo, Name):
        user = self.getCurrentUser()
        if user == "huangbi" or user == "qinsaibo" or user == "lishuaiwei":
            try:
                questSets = mc.optionMenu("EPNUM", q=True, v=True)
                questEP = mc.optionMenu("EP", q=True, v=True)
                path01 = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/" + Name
                path02 = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/old/" + Name
                questFile = os.path.exists(path02)
                if questFile != 0:
                    os.remove(path01) 
                    dfu.copy_file(path02, path01)
                    os.remove(path02) 
                    self.HbChangeReSets(projectInfo)
            except:
                pass
    # need
    def HbShowDateLibSc(self, projectInfo):
        questEP = mc.optionMenu("EP", q=True, v=True)

        TheDateLib = []
        mel.eval("string $GetName=python(\"mc.optionMenu('EPNUM', q = True, v = True)\");")
        mel.eval("string $GetTheName=\"sk_\"+$GetName+\"_h_ms_tex.mb\";")
        TheScs = mel.eval("idmtService \"GetAnimsInAsset\" $GetTheName;")
        TheSc = TheScs.split("|")

        mc.textScrollList("TheDateLibSc", e=1, ra=1)
        for Sc in TheSc:
            if Sc.split("_")[0] == questEP:
                TheDateLib.append(Sc)
                mc.textScrollList("TheDateLibSc", e=1, append=Sc)

    
    # need
    def HbChangeColor(self, projectInfo):
        getTheSelect = mc.textScrollList("TheDateLibSc", q=1, si=1)
        questSets = mc.optionMenu("EPNUM", q=True, v=True)
        questEP = mc.optionMenu("EP", q=True, v=True)
        path = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/"
        TheUpDateSc = os.listdir(path)
        TheBmp = []
    
        
        for i in range(len(TheUpDateSc)):
            if TheUpDateSc[i].split(".")[-1] == "bmp":
                TheBmp.append(TheUpDateSc[i])    
        for j in range(len(TheBmp)):
                theCommand = 'HbImportReCam(\"' + TheBmp[j] + '\")'
                theCommand2 = 'HbImageOk(\"' + TheBmp[j] + '\")'
                theCommand3 = 'HbCancleHook(\"' + TheBmp[j] + '\")'
                if TheBmp[j].find(getTheSelect[0]) == -1:
                    mc.iconTextButton("Temp" + str(j) , e=1, visible=1, bgc=(1, 1, 1), style='iconAndTextVertical', image1="Z:/Projects/ZoomWhiteDolphin/ZoomWhiteDolphin_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/" + TheBmp[j], label=TheBmp[j].split(".")[0], c=theCommand)
                if TheBmp[j].find(getTheSelect[0]) != -1:
                    mc.iconTextButton("Temp" + str(j) , e=1, visible=1, bgc=(1, 0, 0), style='iconAndTextVertical', image1="Z:/Projects/ZoomWhiteDolphin/ZoomWhiteDolphin_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/" + TheBmp[j], label=TheBmp[j].split(".")[0], c=theCommand)
    
                mc.menuItem("TheObMenu" + str(j), e=1, l="This Camera is ok", c=theCommand2)
                mc.menuItem("Cancle" + str(j), e=1, l="cancle the hook", c=theCommand3)
    
    # need
    def HbSkReCamTools(self, projectInfo , scrFrame=1001):
    
        if mc.window ("HbSkReCamWin", ex=1):
            mc.deleteUI("HbSkReCamWin", window=True)
        mc.window("HbSkReCamWin", title="Project Camera Tools", iconName="Short Name", widthHeight=(600, 600), menuBar=0)
        # mc.menu(l="Eidt")
        # mc.menuItem(l="Reset", command="")
        # mc.menuItem(l="", command="")
        # mc.menu(l="Help")
        # mc.menuItem(l="Help", command="")
        # mc.menuItem(l="About", command="")
        
        form = mc.formLayout()

        mc.rowColumnLayout("ROW", numberOfColumns=6, cw=[(1, 80), (2, 150), (3, 100), (4, 100), (5, 100), (6, 30)])
        # check ok
        
        cmd = 'sk_hbExceptCam.sk_hbExceptCam().HbChangeReSets3(\"' + projectInfo + '\")'
        mc.optionMenu("EP", label='EP', cc=cmd)
        
        # for i in range(201,214):
        # EP Num
        for i in range(101, 153):
            mc.menuItem("SetDressTemp" + str(i), label=self.paddNum(projectInfo, i, 3))
        
        questEP = mc.optionMenu("EP", q=True, v=True)

        # check ok
        cmd = 'sk_hbExceptCam.sk_hbExceptCam().HbChangeReSets(\"' + projectInfo + '\")'
        mc.optionMenu("EPNUM", label='SETS', cc=cmd)
        TheFileList = mc.getFileList(folder="//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/")
        for m in range(1000):
            mc.menuItem("TheMenuItem" + str(m), en=0, label="        ")    
        if TheFileList != None:
            for i in range(len(TheFileList)):
                mc.menuItem("TheMenuItem" + str(i), e=1, en=1, label=TheFileList[i])

        # check ok
        cmd = 'sk_hbExceptCam.sk_hbExceptCam().HbExceptSelectReCam(\"' + projectInfo + '\",1)'
        mc.button("OKBUTTON" , bgc=[0.6, 0.1, 0.1], l="export all cam" , c=cmd)
        # check ok
        cmd = 'sk_hbExceptCam.sk_hbExceptCam().HbExceptSelectReCam(\"' + projectInfo + '\")'
        mc.button("OKBUTTON02", bgc=[0.1, 0.6, 0.1], l="exp selected cam", c=cmd)
        # check ok 
        cmd = 'sk_hbExceptCam.sk_hbExceptCam().HbOpenReCamPath(\"' + projectInfo + '\")'
        mc.button("OKBUTTON03", bgc=[0.1, 0.1, 0.1], l="open path", c=cmd)
        # check ok
        cmd = 'sk_hbExceptCam.sk_hbExceptCam().HbChangeReSets4(\"' + projectInfo + '\")'
        mc.intField("TheNumber", value=100, cc=cmd)
    
        questSets = mc.optionMenu("EPNUM", q=True, v=True)
    
        mc.setParent("..")

        mc.rowColumnLayout("ROW4", numberOfColumns=1, cw=[(1, 80)])
        mc.textScrollList("TheDateLibSc", w=128, h=600, allowMultiSelection=True, numberOfRows=8, selectCommand="HbChangeColor()")
        mc.setParent("..")
    
        mc.sysFile("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/", makeDir=True)
    
        TheUpDateSc = []
        if os.path.isdir("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/"):
            TheUpDateSc = os.listdir("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/")
        TheOKDateSc = [];
        if os.path.isdir("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/"):
            TheOKDateSc = os.listdir("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/")
    
        mc.rowColumnLayout("ROW2", numberOfColumns=3, cw=[(1, 120), (2, 400), (3, 120)])
        mc.text("TheNumber", label='number')
        mc.text("part", label='part')
        mc.text("TheOkNumber", label='0')

        mc.setParent("..")
    
        mc.rowColumnLayout("ROW3", numberOfColumns=3, cw=[(1, 120), (2, 400), (3, 120)])
        mc.text("TheNumber1", label="number", align='center')
        mc.text("part1", label="part", align='center')
        mc.text("TheOkNumber1", label="ok", align='center')
    
        mc.setParent("..")

        mc.scrollLayout("Grid", horizontalScrollBarThickness=16, verticalScrollBarThickness=16)
        mc.rowColumnLayout(numberOfColumns=5 , columnWidth=[(1, 128), (2, 128), (3, 128), (4, 128), (5, 128)])
        for m in range(0, 300):
            mc.iconTextButton("Temp" + str(m), h=90, visible=0 , style='iconAndTextVertical', image1="sphere.xpm")
            mc.popupMenu("ThePopup" + str(m))
            mc.menuItem("TheObMenu" + str(m))
            mc.menuItem("Cancle" + str(m))
    
        TheBmp = []
        for i in range(len(TheUpDateSc)):
            if TheUpDateSc[i].split(".")[-1] == "bmp":
                TheBmp.append(TheUpDateSc[i])    
        for j in range(len(TheBmp)):
            # check ok
            theCommand = 'sk_hbExceptCam.sk_hbExceptCam().HbImportReCam(projectInfo,\"' + TheBmp[j] + '\")'
            # check ok
            theCommand2 = 'sk_hbExceptCam.sk_hbExceptCam().HbImageOk(projectInfo,\"' + TheBmp[j] + '\")'
            # check ok
            theCommand3 = 'sk_hbExceptCam.sk_hbExceptCam().HbCancleHook(projectInfo,\"' + TheBmp[j] + '\")'
            
            mc.iconTextButton("Temp" + str(j) , e=1, visible=1, bgc=(1, 1, 1), style='iconAndTextVertical', image1="//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/" + TheBmp[j], label=TheBmp[j].split(".")[0], c=theCommand)
            mc.popupMenu("ThePopup" + str(j))
            mc.menuItem("TheObMenu" + str(j), e=1, l="This Camera is ok", c=theCommand2)
            mc.menuItem("Cancle" + str(j), e=1, l="cancle the hook", c=theCommand3)
    
        mc.text("TheNumber", e=1, bgc=(1, 0.9, 0.9), label=str(len(TheBmp)), align='center')

        questTheNum = mc.intField("TheNumber", q=1, v=1)
        if float(questTheNum) != 0:
            TheStr = str(float(len(TheBmp)) / float(questTheNum) * 100) + "%"
            mc.text("part", e=1, bgc=(0, 1, 0), label=TheStr, align='center')
        if float(questTheNum) == 0:
            mc.text("part", e=1, bgc=(0, 1, 0), label="erro", align='center')
        try:
            TheOKDateSc = os.listdir("//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + questEP + "/" + questSets + "/images/old/")
            mc.text("TheOkNumber", e=1, bgc=(1, 0.9, 0.9), label=len(TheOKDateSc), align='center')
        except:
            mc.text("TheOkNumber", e=1, bgc=(1, 0.9, 0.9), label=0, align='center')
        mc.setParent("..")
        mc.formLayout(form, edit=True,
        attachForm=(("ROW", "top", 0), ("ROW", "left", 0), ("ROW4", "top", 100), ("ROW4", "right", 20), ("ROW3", "top", 35), ("ROW3", "left", 10), ("ROW2", "top", 70), ("ROW2", "left", 10), ("Grid", "top", 100), ("Grid", "left", 0), ("Grid", "right", 0), ("Grid", "bottom", 0)))
        mc.showWindow("HbSkReCamWin")
        
        self.HbChangeReSets2(projectInfo)

        
    
    def paddNum(self, projectInfo, num, length):
        numStr = str(num)
        while(len(numStr) < length):
            numStr = "0" + numStr
        return numStr

    # 补充：新增处理相机到Z盘路径
    def sceneCamPublish(self):
        import sk_infoConfig
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        camName = 'cam_' + shotInfo[1] + '_' + shotInfo[2]
        camList = mc.ls(camName,l=1)
        needCam = ''
        if camList:
            for cam in camList:
                if mc.listRelatives(cam,s=1,ni=1,type = 'camera'):
                    needCam = cam
        else:
            mc.error(u'=============找不到对应镜头的CAM=============')
        # 开始check in
        mc.select(needCam)
        mel.eval('source \"zwCameraImportExport.mel\"')
        mel.eval('zwBakeCamera')
        mel.eval('zwCheckinCamera')
        
    # 获取服务器Cam地址
    # info 2 为 cl_xxx_xxx模式 | 3 为 yd_xxx_xxx_xxx模式 
    def camServerReference(self,info = 2):
        import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        # serve目录
        camServerPath = sk_infoConfig.sk_infoConfig().checkCameraServerPath()
        #camServerPath = "//file-cluster/GDC/Projects/"+ projectInfo + "/Project/scenes/Animation/episode_" + shotInfo[1] + "/episode_camera/" 
        if info == 2:
            camServerFilePath = camServerPath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_cam.ma'
        if info == 3:
            camServerFilePath = camServerPath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '_cam.ma'
        # 开始参考
        refPaths = mc.file(reference = 1,q=1)
        camIn = 0
        for refPath in refPaths:
            if camServerFilePath in refPath:
                camIn =1
        # 无则导入参考相机
        if camIn == 0:
            mc.file(camServerFilePath,reference = 1,ignoreVersion=1,namespace='CAM')
        # 有则重载入相机
        if camIn == 1:
            refNode = mc.referenceQuery(camServerFilePath,referenceNode=1)
            # 清除
            mc.file(rfn=refNode , removeReference=1)
            #载入
            mc.file(camServerFilePath,reference = 1,ignoreVersion=1,namespace='CAM')




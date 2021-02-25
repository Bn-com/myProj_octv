#modify by xuweijian
from maya.cmds import *
import maya.mel as mm
import os
import tempfile
import json
import maya.cmds as mc



class EasyAnimation():
    className=''
    def __init__(self):
        self.className=self.__class__

    def EAGetProjectRepository(self):
        #get the config file and pare the path
        currentSceneName = file(q=True, sn = True, shn =True)
        try:
            projectID = currentSceneName.split("_")[0]
        except:
            projectID = "general"

        #print projectID

        if projectID == "ey":
            return "//file-cluster/GDC/Projects/Enyo/Enyo_Scratch/animation/animCurveLib"
        elif projectID == "fnl":
            return "//file-cluster/GDC/Projects/Jonalu/Jonalu_Scratch/animation/animCurveLib"
        elif projectID == "bu":
            return "//file-cluster/GDC/Projects/BubbleGuppies/BubbleGuppies_Scratch/animation/animCurveLib"
        elif projectID == "do2":
            return "//cq-file10/dod2_scratch/Animation/animCurveLib"
        elif projectID == "lv":
            return "//file-cluster/GDC/Projects/Lionelville/Lionelville_Scratch/Animation/animCurveLib"
        elif projectID == "sk":
            return "//file-cluster/GDC/Projects/Strawberry/Strawberr_Scratch/animation/animCurveLib"
        elif projectID == "ot":
            return "//file-cluster/GDC/Projects/Strawberry/Strawberr_Scratch/Animation/animCurveLib"
        else:
            return "//file-cluster/GDC/Projects/Enyo/Enyo_Scratch/animation/animCurveLib"

    def yyEAExportWrapper(self):

        isExportJnt = mc.checkBox("yyEAExportJnt", q = True, v = True)
        optionMode = mc.radioCollection("yyEARC", q = True, sl = True)
        #yyEAHi yyEASl yyEACh
        if optionMode == "yyEAHi":
            self.yyAutoSelectWithACInHi(isExportJnt)

        selObj = mc.ls(sl = True)
        if selObj != []:
            #fileDirectory
            thisWorkspace=mc.workspace(q=1,fn=1)
            storePath=thisWorkspace+'/data/*.GDCAN'
            fileName = mc.fileDialog(m = 1, dm = storePath)
            filePath = fileName
            if fileName.find(".GDCAN") < 0:
                filePath = fileName+".GDCAN"


            startTime = mc.intField("yyEAStartIF01", q = True, v = True)
            endTime = mc.intField("yyEAEndIF01", q = True, v = True)
            isInfinity = mc.checkBox("yyEAIsInfinity", q = True, v = True)
            if isInfinity == 1:
                print "export infinity"
                startTime = -5000000
                endTime = 5000000
            dict = self.yyEAExport(startTime, endTime)


            if filePath.find(".") != 0:
                try:
                    f = open(filePath, "w")
                    json.dump(dict,f)
                    f.flush()
                    f.close()
                    print "file havs been saved in \"" + filePath + "\"."
                except:
                    pass
            else:
                print "Operation has been cancelled."


    def yyEAExport(self,tStart = 0, tEnd = 0):

        #wirte content list
        channelInfoTotal = ""
        AllObjDict={}
        selObj = mc.ls(sl = True)
        for obj in selObj:
            objDict={}
            channels = mc.listConnections(obj, t = "animCurve", c = True)
            if channels != [] and channels != None:
                for j in range(len(channels)/2):
                    j = j*2
                    channelDict={}
                    #channelDict['attrName']=str(channels[j])
                    channelDict['wt']=mc.getAttr(channels[j+1] + ".weightedTangents")
                    channelDict['preI']=mc.getAttr(channels[j+1] + ".preInfinity")
                    channelDict['postI']=mc.getAttr(channels[j+1] + ".postInfinity")


                    #animCurve: channels[j+1]
                    #channelInfo.append(str(channels[j+1]))

                    #is weighted tangent

                    #postIninity

                    #each key infomation
                    keys = mc.keyframe(channels[j+1], q = True, t = (tStart, tEnd))
                    #print channels[j+1]
                    #print keys
                    values = mc.keyframe(channels[j+1], q = True, vc = True, t = (tStart, tEnd))
                    inTan = mc.keyTangent(channels[j+1], q = True, itt = True, t = (tStart, tEnd))
                    outTan = mc.keyTangent(channels[j+1], q = True, ott = True, t = (tStart, tEnd))
                    tanLock = mc.keyTangent(channels[j+1], q = True, lock = True, t = (tStart, tEnd))
                    inAngle = mc.keyTangent(channels[j+1], q = True, inAngle = True, t = (tStart, tEnd))
                    outAngle = mc.keyTangent(channels[j+1], q = True, outAngle = True, t = (tStart, tEnd))
                    inWeight = mc.keyTangent(channels[j+1], q = True, inWeight = True, t = (tStart, tEnd))
                    outWeight = mc.keyTangent(channels[j+1], q = True, outWeight = True, t = (tStart, tEnd))

                    breakDown = mc.keyframe(channels[j+1], q = True, breakdown = True, t = (tStart, tEnd))

                    #each key information

                    keyInfo=[]
                    try:
                        for k in range(len(keys)):
                            keyInfoDict={}
                            keyInfoDict['key']=keys[k]
                            keyInfoDict['value']=values[k]
                            keyInfoDict['tanLock']=tanLock[k]
                            keyInfoDict['inTan']=inTan[k]
                            keyInfoDict['outTan']=outTan[k]
                            keyInfoDict['inAngle']=inAngle[k]
                            keyInfoDict['outAngle']=outAngle[k]
                            keyInfoDict['inWeight']=inWeight[k]
                            keyInfoDict['outWeight']=outWeight[k]
                            keyInfo.append(keyInfoDict)
                    except:
                        pass


                    attrName=channels[j].split('.')[1]
                    channelDict['keyInfo']=keyInfo
                    channelDict['breakdown']=breakDown
                    objDict[str(attrName)]=channelDict
                AllObjDict[obj]=objDict


                    #sum them together

        return AllObjDict

    def yyEAImportWrapper(self):
        #extract namespace
        selObj = mc.ls(sl = True)
        if selObj == []:
            namespace = "noNamespaceExist"
        else:
            chd = selObj[0].split("|")
            chd = chd[len(chd)-1]
            seq = chd.split(":")
            if seq[0] == selObj[0]:
                namespace = ""
            else:
                namespace = ""
                for i in range(len(seq)-1):
                    namespace += seq[i]+":"

        #get file path:
        thisWorkspace=mc.workspace(q=1,fn=1)
        storePath=thisWorkspace+'/data/*.GDCAN'
        #filePath = fileDialog2(startingDirectory=storePath,dialogStyle=2, ff = "*.GDCAN")[0]
        filePath = mc.fileDialog(m = 0, dm = storePath)
        #directoryMask='/usr/u/bozo/myFiles/*.ma'
        #get blackhole
        timeOffset = mc.intField("yyEAOffsetIF01", q = True, v = True)

        #get Wormhole
        timeScale = mc.floatField("yyEATimeIF01", q = True, v = True)

        #make sure whether replace
        isReplace = mc.checkBox("yyEAIsReplace", q = True, v = True)


        if os.access(filePath, 0):
            self.yyEAImport(namespace, filePath, timeOffset, timeScale, isReplace)

    def yyEATransferWrapper(self):
        selObj = mc.ls(sl = True)
        try:
            ns2 = selObj[1].split(":")[0]
        except:
            raise Exception("Select source then target. Make sure namespace correctly")

        isJnt = mc.checkBox("yyEATransferJnt", q = True, v = True)
        self.yyAutoSelectWithNS(isJnt)
        isReplace = mc.checkBox("yyEATransferIsReplace", q = True, v = True)

        contents = self.yyEAExport(tStart = -500000, tEnd = 510000)
        tempDir = tempfile.gettempdir()
        try:
            f = open(tempDir + "/yyEACurveFile.yyea", "w")
            f.write(contents)
            f.close()
            print tempDir + "/yyEACurveFile.yyea"
        except:
            raise Exception("IO error")

        #yyAutoSelectWithNS(??)
        self.yyEAImport(ns2 + ":", tempDir + "/yyEACurveFile.yyea", 0, 1, isReplace)



    def yyEAImport(self,namespace, filePath, timeOffset, timeScale, isReplace):
        #print namespace
        #print filePath
        #print timeOffset
        #print timeScale

        #grab the txt file (.yyea ext)
        try:
            f = open(filePath, "r")
            dict = json.load(f)
            f.close()
        except:
            mc.confirmDialog(t = "Error", m = "IOError, access deny of no such file on hard drive!")

        #input analysis
        '''
        *****Pseudo***** (formatting input string)
        splite("#")
        if find "{}" or == "" (pass this string)
        split "{{" :
                1 before: target attribute and channel attribute
                2 after: split "}{":
                        1 before: keys information (split " ")
                        2 after: break down: if find "None":  split "[" grab after, then split "]" grab before, then split " "

        '''
        objList=dict.keys()
        #channelList = contents.split("#")
        #for each channel (separated by "#" in txt file)


        #----------------progressing win
        progressWin = mc.window(title = "animCurv Importing")
        mc.columnLayout(adj = True)
        pointsNum = len(objList)
        progressControl = mc.progressBar(maxValue = pointsNum, width=300)
        mc.setParent("..")
        mc.showWindow( progressWin )
        #---------------- progressing win



        for obj in objList:
            #for skipping blank key and ""
            if obj != "":
                if namespace == "noNamespaceExist":
                    #no any object selected
                    newObj=obj
                else:
                    temp1 = obj.split("|")
                    temp2 = temp1[len(temp1)-1]
                    temp3 = temp2.split(":")
                    orgNamespace=''
                    for j in range(len(temp3)-1):
                        orgNamespace += temp3[j] + ":"
                    newObj=obj.replace(orgNamespace,namespace)
                attrs=dict[obj].keys()
                if attrs != None:

                    for attr in attrs:
                        if isReplace == 1:
                            try:
                                animNodePre = mc.listConnections('%s.%s'%(newObj,attr), t = "animCurveTL")[0]
                            except:
                                animNodePre = None
                            try:
                                if animNodePre != None:
                                    mc.delete(animNodePre)
                            except:
                                pass
                            try:
                                animNodePre = mc.listConnections('%s.%s'%(newObj,attr), t = "animCurveTA")[0]
                            except:
                                animNodePre = None
                            try:
                                if animNodePre != None:
                                    mc.delete(animNodePre)
                            except:
                                pass
                            try:
                                animNodePre = mc.listConnections('%s.%s'%(newObj,attr), t = "animCurveTU")[0]
                            except:
                                animNodePre = None
                            try:
                                if animNodePre != None:
                                    mc.delete(animNodePre)
                            except:
                                pass
                        keyTime=[]
                        keyValue=[]
                        tanLock=[]
                        inTan=[]
                        outTan=[]
                        inAngle=[]
                        outAngle=[]
                        inWeight=[]
                        outWeight=[]
                        wt=dict[obj][attr]['wt']
                        preI=dict[obj][attr]['preI']
                        postI=dict[obj][attr]['postI']

                        keyInfo=dict[obj][attr]['keyInfo']

                        for onekey in keyInfo:
                            keyTime.append(timeOffset + float(onekey['key']) * timeScale)
                            #keyTime.append(onekey['key'])
                            keyValue.append(onekey['value'])
                            tanLock.append(onekey['tanLock'])
                            inTan.append(onekey['inTan'])
                            outTan.append(onekey['outTan'])
                            inAngle.append(onekey['inAngle'])
                            outAngle.append(onekey['outAngle'])
                            inWeight.append(onekey['inWeight'])
                            outWeight.append(onekey['outWeight'])

                        for i in range(len(keyTime)):
                            try:
                                mc.setKeyframe('%s.%s'%(newObj,attr), time = keyTime[i], v = keyValue[i])
                            except:
                                print 'error in %s.%s setkey'%(obj,attr)


                        try:
                            animNode = mc.listConnections('%s.%s'%(newObj,attr), t = "animCurve")[0]
                            #move this to the top of import
                            mc.setAttr(animNode + ".weightedTangents", wt)
                            mc.setAttr(animNode + ".preInfinity", preI)
                            mc.setAttr(animNode + ".postInfinity", postI)
                        except:
                            print newObj + ' no animationNode'

                        if wt==True:
                            print inAngle
                            print outAngle
                            for j in range(len(keyTime)):
                                try:

                                    #in/out tangent type
                                    mc.keyTangent('%s.%s'%(newObj,attr), e = True, itt = inTan[j], time = (keyTime[j], keyTime[j]))
                                    print inTan[j]

                                    mc.keyTangent('%s.%s'%(newObj,attr), e = True, ott = outTan[j], time = (keyTime[j], keyTime[j]))
                                    print outTan[j]

                                    mc.keyTangent('%s.%s'%(newObj,attr), e = True, lock = 0, time = (keyTime[j], keyTime[j]))
                                    print '-----1'
                                    #in/out angle
                                    print inAngle[j]
                                    mc.keyTangent('%s.%s'%(newObj,attr), e = True, ia = inAngle[j], time = (keyTime[j], keyTime[j]))

                                    print '-----2'
                                    mc.keyTangent('%s.%s'%(newObj,attr), e = True, oa = outAngle[j], time = (keyTime[j], keyTime[j]))
                                    print '-----3'
                                    #in/out angle weight
                                    mc.keyTangent('%s.%s'%(newObj,attr), e = True, iw = inWeight[j], time = (keyTime[j], keyTime[j]))
                                    mc.keyTangent('%s.%s'%(newObj,attr), e = True, ow = outWeight[j], time = (keyTime[j], keyTime[j]))
                                    print '-----4'
                                    #apply the lock, make sure the same as txt file
                                    mc.keyTangent('%s.%s'%(newObj,attr), e = True, lock = tanLock[j], time = (keyTime[j], keyTime[j]))
                                    print '-----5'

                                except:
                                    print 'error in set %s.%s keyTangent '%(newObj,attr)

            mc.progressBar(progressControl, edit=True, step=1)
        mc.deleteUI(progressWin)


    def yyEARefresh(self):
        self.yyEAGUI()
    def yyEAAbout(self):
        mc.confirmDialog(t = "About Easy Animation 2.0", m = "Yeah.Y Presents\nCurrent Verion: 2.0\nGDC-IDMT(2009). All Rights Reserved(C)")
    def yyEAExit(self):
        try:
            mc.deleteUI("easyAnimGUI")
        except:
            pass
    def yyEASureExportJoint(self):
        stat = mc.confirmDialog(t = "Export Note!", m = "Are you sure you wanna export animCurve on joints", b = ["Sure","No"])
        if stat == "No":
            mc.checkBox("yyEAExportJnt", e = True, v = 0)

    def yyEASureTransferJoint(self):
        stat = mc.confirmDialog(t = "Transfer Note!", m = "Are you sure you wanna transfer animCurve on joints", b = ["Sure","No"])
        if stat == "No":
            mc.checkBox("yyEATransferJnt", e = True, v = 0)

    def yyEADiableTimeRange(self):
        mc.text("yyEATextFrame", e = True, en = False)
        mc.intField("yyEAStartIF01", e = True, en = False)
        mc.text("yyEATestTo", e = True, en = False)
        mc.intField("yyEAEndIF01", e = True, en = False)

    def yyEAEnableTimeRange(self):
        mc.text("yyEATextFrame", e = True, en = True)
        mc.intField("yyEAStartIF01", e = True, en = True)
        mc.text("yyEATestTo", e = True, en = True)
        mc.intField("yyEAEndIF01", e = True, en = True)


    def yyEAAbout(self):
        mc.confirmDialog(t = "About Easy Animation 2.0", m = "Yeah.Y Presents\nCurrent Verion: 2.2\nGDC-IDMT(2009). All Rights Reserved(C)")
    def yyEAHelp(self):
        mayaCmd = 'system("load //file-cluster/GDC/Resource/Support/Maya/Python/IDMT/yyScripts/doc/yyEasyAnimation.mht" );'
        mm.eval(mayaCmd)



    def yyEAChangeCreature(self):
        selection = self.yyEAGetOptionItemFP01()
        #print selection
        for i in range(100):
            stri = str(i)
            try:
                mc.deleteUI("yyEA_mi02"+stri)
            except:
                break

        repositoryPath = self.yyEAGetProjectRepository()
        creaturePath = self.yyEAGetOptionItemFP01()
        yyeaListTemp = os.listdir(repositoryPath + "/" + creaturePath)
        yyeaList = []
        for i in range(len(yyeaListTemp)):
            if yyeaListTemp[i].find(".")<0:
                yyeaList.append(yyeaListTemp[i].split(".")[0])

        for i in range(len(yyeaList)):
            stri = str(i)
            mc.menuItem("yyEA_mi02"+stri, p = "yyEA_om02", l = yyeaList[i])
        try:
            mc.optionMenu("yyEA_om02", e=True, select = 1)
        except:
            pass
        self.yyEAChangeGenre()


    def yyEAChangeGenre(self):
        selection = self.yyEAGetOptionItemFP02()
        #print selection
        for i in range(100):
            stri = str(i)
            try:
                mc.deleteUI("yyEA_mi03"+stri)
            except:
                break

        repositoryPath = self.yyEAGetProjectRepository()
        creaturePath = self.yyEAGetOptionItemFP01()
        genrePath = self.yyEAGetOptionItemFP02()
        yyeaListTemp = os.listdir(repositoryPath + "/" + creaturePath + "/" + genrePath)
        yyeaList = []
        for i in range(len(yyeaListTemp)):
            if yyeaListTemp[i].find(".yyea") > 0:
                yyeaList.append(yyeaListTemp[i].split(".")[0])

        for i in range(len(yyeaList)):
            stri = str(i)
            mc.menuItem("yyEA_mi03"+stri, p = "yyEA_om03", l = yyeaList[i])
        try:
            mc.optionMenu("yyEA_om03", e=True, select = 1)
        except:
            pass


    def yyEAGetFeedInFilePath(self):
        repository = self.yyEAGetProjectRepository()
        creature = self.yyEAGetOptionItemFP01()
        genre = self.yyEAGetOptionItemFP02()
        curve = self.yyEAGetOptionItemFP03()
        feedinPath = repository + "/" + creature + "/" + genre + "/" + curve + ".yyea"

        return feedinPath

    def yyEAWatchExampleVideoClip(self):
        repository = self.yyEAGetProjectRepository()
        creature = self.yyEAGetOptionItemFP01()
        genre = self.yyEAGetOptionItemFP02()
        curve = self.yyEAGetOptionItemFP03()
        feedinPath1 = repository + "/" + creature + "/" + genre + "/" + curve + ".avi"
        feedinPath2 = repository + "/" + creature + "/" + genre + "/" + curve + ".mov"
        if os.access(feedinPath1, os.R_OK) == 1:
            mayaCmd = 'system("load ' + feedinPath1 + '" );'
            mm.eval(mayaCmd)

        elif os.access(feedinPath2, os.R_OK) == 1:
            mayaCmd = 'system("load ' + feedinPath2 + '" );'
            mm.eval(mayaCmd)

        else:
            mc.confirmDialog(t = "Note", m = "No such movie clip")

    def yyEAFeedInWrapper(self):

        feedinFile = self.yyEAGetFeedInFilePath()
        times = mc.intField("feedinTimes",q = True, v = True)
        scale = mc.floatField("feedinScale", q = True, v = True)
        jumpJump = mc.intField("yyEAJump", q = True, v = True)
        isStop = mc.checkBox("yyEAIsStop2", q = True, v = True)
        stopTime = mc.intField("yyEAStopTime2", q = True, v = True)

        #*****************************
        #change above parameters
        #is replace always 0
        #add jumpJump for sperating circle anime
        #add stop time for appending animation
        #*****************************

        #--------------------------------- derived from yyEAImportWrapper --------
        #extract namespace
        selObj = mc.ls(sl = True)
        if selObj == []:
            namespace = "noNamespaceExist"
        else:
            chd = selObj[0].split("|")
            chd = chd[len(chd)-1]
            seq = chd.split(":")
            if seq[0] == selObj[0]:
                namespace = ""
            else:
                namespace = ""
                for i in range(len(seq)-1):
                    namespace += seq[i]+":"

        #get file path:
        filePath = feedinFile

        #get blackhole
        #get current time

        #get Wormhole
        timeScale = scale

        #make sure whether replace
        isReplace = 0


        if os.access(filePath, 0):
            jump = 0
            for i in range(times):
                timeOffset = mc.currentTime(q = True)
                if jump == 0:
                    jump = self.yyEAFeedIn(namespace, filePath, timeOffset, timeScale, isReplace, isStop, stopTime)
                else:
                    currentKeyTime = timeOffset + (jump + jumpJump) * i
                    self.yyEAFeedIn(namespace, filePath, currentKeyTime, timeScale, isReplace, isStop, stopTime)



    def yyEAFeedIn(namespace, filePath, timeOffset, timeScale, isReplace, isStop, stopTime):

        firstFrame = 100000
        lastFrame = 0

        #*************************
        #jump to the key time (done) lastFrame and first frame tracker
        #trun off the infinity (done) 0 for pre and post
        #turn off replace (done)
        #*************************

        #print namespace
        #print filePath
        #print timeOffset
        #print timeScale

        #grab the txt file (.yyea ext)
        try:
            f = open(filePath, "r")
            contents = f.read()
            f.close()
        except:
            mc.confirmDialog(t = "Error", m = "IOError, access deny of no such file on hard drive!")

        #input analysis
        '''
        *****Pseudo***** (formatting input string)
        splite("#")
        if find "{}" or == "" (pass this string)
        split "{{" :
                1 before: target attribute and channel attribute
                2 after: split "}{":
                        1 before: keys information (split " ")
                        2 after: break down: if find "None":  split "[" grab after, then split "]" grab before, then split " "

        '''

        channelList = contents.split("#")
        #for each channel (separated by "#" in txt file)


        #----------------progressing win
        progressWin = mc.window(title = "animCurv Feeding in")
        mc.columnLayout(adj = True)
        pointsNum = len(channelList)
        progressControl = mc.progressBar(maxValue = pointsNum, width=300)
        mc.setParent("..")
        mc.showWindow( progressWin )
        #---------------- progressing win


        for i in range(len(channelList)):
            #for skipping blank key and ""
            if channelList[i] != "" and channelList[i].find("{}") < 0:
                channelNKeys = channelList[i].split("{{")
                channelAttributes = channelNKeys[0]
                keysInfo = channelNKeys[1]

                #channel info
                channelAttributeListTemp = channelAttributes.split(" ")

                #key info
                keyInfoList = keysInfo.split("}{") #each key, last on with break down
                lastKeyNBreakdown = keyInfoList[len(keyInfoList)-1].split("}}")
                keyInfoListTemp = []
                for i in range(len(keyInfoList)-1):
                    keyInfoListTemp.append(keyInfoList[i])
                keyInfoListTemp.append(lastKeyNBreakdown[0])
                breakdownTemp = lastKeyNBreakdown[1]

                #by now, get the raw infomation
                    #|_channelAttributeListTemp
                    #|_keyInfoListTemp
                    #|_breakdownTemp

                #step 1: channel informations
                #weightedTangent
                wt = float(channelAttributeListTemp[1])
                #preInfinity
                preI = float(channelAttributeListTemp[2])
                #postIninity
                postI = float(channelAttributeListTemp[3])


                '''
                *****Pseudo***** (namespace intelligence)
                #####specify channel name (channelName)
                no any selected: use the original namespace
                have seleceted: use current select namespace (parm: namespace)
                        have namespace inside the .txt file (just substitute)
                        no namespace inside the .txt file(adding)
                                    "|object1"
                                    "objectRoot|object1"
                '''
                if namespace == "noNamespaceExist":
                    #no any object selected
                    channelName = channelAttributeListTemp[0]
                else:
                    #have selected object
                    if channelAttributeListTemp[0].find(":") >= 0:
                        #parse orgNamespace for substitution
                        temp1 = channelAttributeListTemp[0].split("|")
                        temp2 = temp1[len(temp1)-1]
                        temp3 = temp2.split(":")
                        orgNamespace = ""
                        for j in range(len(temp3)-1):
                            orgNamespace += temp3[j] + ":"
                        #print orgNamespace + " replaced by " + namespace
                        channelName = channelAttributeListTemp[0].replace(orgNamespace, namespace)
                    else:
                        #add namespace
                        if channelAttributeListTemp[0].find("|") == 0:
                            #in complex hierarchy: condition1 "|sphere"
                            channelNameBlank = channelAttributeListTemp[0].split("|")
                            channelName = "|" + namespace + channelNameBlank[1]
                        elif channelAttributeListTemp[0].find("|") > 0:
                            #in complex hierarchy: condition1 "sphere2|sphere"
                            channelNamePieces = channelAttributeListTemp[0].split("|")
                            channelName = ""
                            for j in range(len(channelNamePieces)):
                                if j != len(channelNamePieces)-1:
                                    channelName += namespace + channelNamePieces[j] + "|"
                                else:
                                    channelName += namespace + channelNamePieces[j]
                        else:
                            channelName = namespace + channelAttributeListTemp[0]

                #step 2: parse the keys information
                #storage variables:
                keyTime = []
                keyValue = []
                tanLock = []
                inTan = []
                outTan = []
                inAngle = []
                outAngle = []
                inWeight = []
                outWeight = []

                for j in range(len(keyInfoListTemp)):
                    keyInfoTemp1 = keyInfoListTemp[j].split(" ")

                    #blackhole and wormhole effect
                    keyTime.append(int(timeOffset + float(keyInfoTemp1[1]) * timeScale))
                    keyValue.append(float(keyInfoTemp1[2]))
                    tanLock.append(float(keyInfoTemp1[3]))
                    inTan.append(keyInfoTemp1[4])
                    outTan.append(keyInfoTemp1[5])
                    inAngle.append(float(keyInfoTemp1[6]))
                    outAngle.append(float(keyInfoTemp1[7]))
                    inWeight.append(float(keyInfoTemp1[8]))
                    outWeight.append(float(keyInfoTemp1[9]))


                #step 3: parse the breakdown (also with timeOffset and timeScale)
                if breakdownTemp.find("None") < 0 :
                    breakdownListTemp = breakdownTemp.split(" ")
                    breakdownList = []
                    for j in range(len(breakdownListTemp) - 2):
                        j += 1
                        breakdownList.append((float(breakdownListTemp[j]) + timeOffset) * timeScale)
                else:
                    breakdownList = []

                #step 4: feed in animation (handle exceptions)
                #make sure is replace or adding
                #find the animCurve node if it's exist in
                if isReplace == 1:
                    #find the channel feeding nodes and try to delete them
                    try:
                        animNodePre = mc.listConnections(channelName, t = "animCurve")[0]
                    except:
                        animNodePre = None
                    try:
                        if animNodePre != None:
                            mc.delete(animNodePre)
                    except:
                        pass


                #no matter whether delete, just add.
                for j in range(len(keyTime)):
                    try:
                        #attention: in/out tangent type must in final order. (after tangent lock)

                        #create the key frame no matter whether the channel exist.
                        if isStop == 1:
                            if keyTime[j] < stopTime:
                                mc.setKeyframe(channelName, time = keyTime[j], v = keyValue[j])
                            else:
                                break
                        else:
                            mc.setKeyframe(channelName, time = keyTime[j], v = keyValue[j])

                    except:
                        pass
                        #print channelName + ' cannot key'
                    if lastFrame < keyTime[j]:
                        lastFrame = keyTime[j]
                    if firstFrame > keyTime[j]:
                        firstFrame = keyTime[j]

                #deal with breakdown
                if breakdownList != []:
                    for k in range(len(breakdownList)):
                        try:
                            mc.keyframe(channelName, e = True, bd = True, time = (breakdownList[k], breakdownList[k]))
                        except:
                            pass

                #check animCurve node again for add some attributes;
                try:
                    animNode = mc.listConnections(channelName, t = "animCurve")[0]
                    mc.setAttr(animNode + ".weightedTangents", wt)
                    mc.setAttr(animNode + ".preInfinity", 0)
                    mc.setAttr(animNode + ".postInfinity", 0)
                except:
                    #print channelName + ' no keys'
                    pass

                for j in range(len(keyTime)):
                    try:
                        #attention: in/out tangent type must in final order. (after tangent lock)
                        #create the key frame no matter whether the channel exist.
                        if isStop == 1:
                            if keyTime[j] < stopTime:

                                #unlock the tangent
                                mc.keyTangent(channelName, e = True, lock = 0, time = (keyTime[j], keyTime[j]))

                                #in/out angle
                                mc.keyTangent(channelName, e = True, ia = inAngle[j], time = (keyTime[j], keyTime[j]))
                                mc.keyTangent(channelName, e = True, oa = outAngle[j], time = (keyTime[j], keyTime[j]))
                                #in/out angle weight
                                mc.keyTangent(channelName, e = True, iw = inWeight[j], time = (keyTime[j], keyTime[j]))
                                mc.keyTangent(channelName, e = True, ow = outWeight[j], time = (keyTime[j], keyTime[j]))

                                #apply the lock, make sure the same as txt file
                                mc.keyTangent(channelName, e = True, lock = tanLock[j], time = (keyTime[j], keyTime[j]))

                                #in/out tangent type
                                mc.keyTangent(channelName, e = True, itt = inTan[j], time = (keyTime[j], keyTime[j]))
                                mc.keyTangent(channelName, e = True, ott = outTan[j], time = (keyTime[j], keyTime[j]))
                            else:
                                break
                        else:

                            #unlock the tangent
                            mc.keyTangent(channelName, e = True, lock = 0, time = (keyTime[j], keyTime[j]))

                            #in/out angle
                            mc.keyTangent(channelName, e = True, ia = inAngle[j], time = (keyTime[j], keyTime[j]))
                            mc.keyTangent(channelName, e = True, oa = outAngle[j], time = (keyTime[j], keyTime[j]))
                            #in/out angle weight
                            mc.keyTangent(channelName, e = True, iw = inWeight[j], time = (keyTime[j], keyTime[j]))
                            mc.keyTangent(channelName, e = True, ow = outWeight[j], time = (keyTime[j], keyTime[j]))

                            #apply the lock, make sure the same as txt file
                            mc.keyTangent(channelName, e = True, lock = tanLock[j], time = (keyTime[j], keyTime[j]))

                            #in/out tangent type
                            mc.keyTangent(channelName, e = True, itt = inTan[j], time = (keyTime[j], keyTime[j]))
                            mc.keyTangent(channelName, e = True, ott = outTan[j], time = (keyTime[j], keyTime[j]))
                    except:
                        pass

            mc.progressBar(progressControl, edit=True, step=1)
        mc.deleteUI(progressWin)

        return lastFrame - firstFrame

    def yyEAGetOptionItemFP01(self):
        okay = mc.optionMenu("yyEA_om01",q = True, select = True)
        stri = str(okay-1)
        si = mc.menuItem("yyEA_mi01"+stri, q=True,l=True)
        return si

    def yyEAGetOptionItemFP02(self):
        okay = mc.optionMenu("yyEA_om02",q = True, select = True)
        stri = str(okay-1)
        si = mc.menuItem("yyEA_mi02"+stri, q=True,l=True)
        return si

    def yyEAGetOptionItemFP03(self):
        okay = mc.optionMenu("yyEA_om03",q = True, select = True)
        stri = str(okay-1)
        si = mc.menuItem("yyEA_mi03"+stri, q=True,l=True)
        return si

    ##----Roll Line----#
    #yyEAGUI()
    ##----Roll Line----#





    ###################################
    # add to common function


    def yyAutoSelectWithACInHi(self,withJnt = 0):

        try:
            selObj = mc.ls(sl = True)
            access = 1
        except:
            access = 0
            pass

        if access == 1:
            allCurve = mc.ls(type = "animCurve")

            #filter TA, TU, TL
            realAC = []
            for curve in allCurve:
                if mc.nodeType(curve) == "animCurveTL" or mc.nodeType(curve) == "animCurveTA" or mc.nodeType(curve) == "animCurveTU":
                    realAC.append(curve)


            #extract Transform node with curve
            #selectable for joint, include or exclude
            animObj = []
            for i in range(len(realAC)):
                try:
                    animObjTemp = mc.listConnections(realAC[i])[0]
                    if withJnt !=1:
                        if mc.nodeType(animObjTemp) == "joint":
                            continue
                    animObj.append(animObjTemp)
                except:
                    pass

            #clear the redundance
            mc.select(animObj)
            animObj = mc.ls(sl = True) #explicity names for parsing whether in hierachy
            target = []
            ##In hierachy and same name
            for i in range(len(selObj)):
                for j in range(len(animObj)):
                    if self.isThatInDagHi(selObj[i], animObj[j]) == 1:
                        target.append(animObj[j])

            try:
                mc.select(target)
            except:
                pass

        else:
            mc.confirmDialog(t = "Error", m = "No any object selected.")


    def yyAutoSelectWithNS(self,withJnt = 0):
        try:
            selObj = mc.ls(sl = True)[0]
        except:
            raise Exception("Please Select an Object")
        try:
            namespace = selObj.split(":")[0]
        except:
            raise Exception("No namespace detected, please check that object")
        allCurve = mc.ls(type = "animCurve")
        #filter TA, TU, TL
        realAC = []
        for curve in allCurve:
            if mc.nodeType(curve) == "animCurveTL" or mc.nodeType(curve) == "animCurveTA" or mc.nodeType(curve) == "animCurveTU":

                realAC.append(curve)

        if realAC == []:
            raise Exception("No Animation Detected")

        #extract Transform node with curve
        #selectable for joint, include or exclude
        animObj = []
        for i in range(len(realAC)):
            try:
                animObjTemp = mc.listConnections(realAC[i])[0]
                if withJnt !=1:
                    if mc.nodeType(animObjTemp) == "joint":
                        continue
                animObj.append(animObjTemp)
            except:
                pass

        nsObj = []
        for i in range(len(animObj)):
            try:
                thisNS = animObj[i].split(":")[0]
                if thisNS == namespace:
                    nsObj.append(animObj[i])
            except:
                pass
        mc.select(nsObj)

    def yyAutoSelectWithAC(self,withJnt = 0):

        allCurve = mc.ls(type = "animCurve")

        #filter TA, TU, TL
        realAC = []
        for curve in allCurve:
            if mc.nodeType(curve) == "animCurveTL" or mc.nodeType(curve) == "animCurveTA" or mc.nodeType(curve) == "animCurveTU":
                realAC.append(curve)

        #extract Transform node with curve
        #selectable for joint, include or exclude
        animObj = []
        for i in range(len(realAC)):
            try:
                animObjTemp = mc.listConnections(realAC[i])[0]
                if withJnt !=1:
                    if mc.nodeType(animObjTemp) == "joint":
                        continue
                animObj.append(animObjTemp)
            except:
                pass

        try:
            mc.select(animObj)
            target = mc.ls(sl = True) #implicity names for excluding some channels
            #exclude TSM session
            targetWithoutTSM = []
            try:
                for i in range(len(target)):
                    if target[i].find("RightLeg_polevector") < 0 and target[i].find("LeftLeg_polevector") < 0 and target[i].find("LeftLeg_isolater") < 0 and target[i].find("RightLeg_isolater")<0 and target[i].find("Head_isolatecalculate")<0:
                        targetWithoutTSM.append(target[i])
            except:
                pass

            try:
                mc.select(targetWithoutTSM)
            except:
                mc.select(clear = True)
                mc.confirmDialog(t = "Note", m = "No Animation Found in Hierachy")

            #constrain warnning
        except:
            mc.confirmDialog(t = "Note", m = "No found any animation exsit in current scene.")

    def yyEADeleteAnimCurveWrapper(self):
        stat = mc.confirmDialog(t = "Warning!!", m = "Are you sure delete animation?\nThis process possibly cannot be undone.", b = ["Yes","No"])
        if stat == "Yes":
            option = mc.radioCollection("yyEADARC", q = True, sl = True)
            if option == "yyEADASl":
                self.yyDeleteSelectAnimCurve()
            else:
                self.yyDeleteSelectAllAnimCurve()


    def yyDeleteSelectAnimCurve(self):
        deleted = 0
        try:
            selObj = mc.ls(sl = True)
            for i in range(len(selObj)):
                acTL = mc.listConnections(selObj[i], type = "animCurveTL")
                try:
                    for j in range(len(acTL)):
                        try:
                            mc.delete(acTL[j])
                            deleted = 1
                        except:
                            pass
                except:
                    pass

                acTU = mc.listConnections(selObj[i], type = "animCurveTU")
                try:
                    for j in range(len(acTU)):
                        try:
                            mc.delete(acTU[j])
                            deleted = 1
                        except:
                            pass
                except:
                    pass

                acTA = mc.listConnections(selObj[i], type = "animCurveTA")
                try:
                    for j in range(len(acTA)):
                        try:
                            mc.delete(acTA[j])
                            deleted = 1
                        except:
                            pass
                except:
                    pass
        except:
            mc.confirmDialog(t = "Note!", m = "Nothing to be deleted!")
        if deleted == 1:
            mc.confirmDialog(t = "Note", m = "Delete animation, done.")

    def yyDeleteSelectAllAnimCurve(self):

        ta = mc.ls(type = "animCurveTA")
        tu = mc.ls(type = "animCurveTU")
        tl = mc.ls(type = "animCurveTL")

        c = ta
        for i in range(len(c)):
            try:
                mc.delete(c[i])
            except:
                pass
        c = tu
        for i in range(len(c)):
            try:
                mc.delete(c[i])
            except:
                pass
        c = tl
        for i in range(len(c)):
            try:
                mc.delete(c[i])
            except:
                pass

        mc.confirmDialog(t = "Note", m = "Delete animation, done.")

    def yyNonAnimChannelChecker(self):
        selObj = mc.ls(sl = True)
        objWithNonAnimChannel = []
        if selObj != []:
            for i in range(len(selObj)):
                connections = mc.listConnections(selObj[i], s = True, d = False)
                if connections != [] and connections != None:
                    for j in range(len(connections)):
                        nType = mc.nodeType(connections[j])
                        if nType.find("animCurveU") >=0 or nType.find("Constraint") >=0 or nType.find("pairBlend") >=0 :
                            objWithNonAnimChannel.append(selObj[i])
            if objWithNonAnimChannel == []:
                mc.confirmDialog(t = "Note", m = "No found any object with non-animation channel(s).")
            else:
                mc.confirmDialog(t = "Non-Anim Channel Detected", m = "Object(s) with non-animation channel(s) have been selected by system.")
                try:
                    mc.select(objWithNonAnimChannel)
                except:
                    pass

        else:
            mc.confirmDialog(t = "Wrong!", m = "Please Select the Object(s).")


    def isThatInDagHi(self,root, obj):
        allChild = mc.ls(root, dag = True, type = "transform")
        if allChild != [] and allChild != None:
            for i in range(len(allChild)):
                if allChild[i] == obj:
                    return 1
        return 0

    def isThisHaveConstraintOutConns(self):

        #no namespace constraints
        noNsCns = []

        conns = mc.ls(type = "aimConstraint")
        if conns != [] and conns != None:
            for i in range(len(conns)):
                if mc.referenceQuery(conns[i], inr = True) == 0:
                    noNsCns.append(conns[i])

        conns = mc.ls(type = "orientConstraint")
        if conns != [] and conns != None:
            for i in range(len(conns)):
                if mc.referenceQuery(conns[i], inr = True) == 0:
                    noNsCns.append(conns[i])

        conns = mc.ls(type = "parentConstraint")
        if conns != [] and conns != None:
            for i in range(len(conns)):
                if mc.referenceQuery(conns[i], inr = True) == 0:
                    noNsCns.append(conns[i])

        conns = mc.ls(type = "pointConstraint")
        if conns != [] and conns != None:
            for i in range(len(conns)):
                if mc.referenceQuery(conns[i], inr = True) == 0:
                    noNsCns.append(conns[i])

        conns = mc.ls(type = "scaleConstraint")
        if conns != [] and conns != None:
            for i in range(len(conns)):
                if mc.referenceQuery(conns[i], inr = True) == 0:
                    noNsCns.append(conns[i])

        if noNsCns != []:
            for i in range(len(noNsCns)):
                print "ok"

        #for backup
        #"geometryConstraint"
        #"tangentConstraint"
        #"normalConstraint"

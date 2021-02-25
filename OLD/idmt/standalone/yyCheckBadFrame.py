#!/usr/bin/env python

import sys
import os
import math
import tkMessageBox
import pymssql

def getProjectNameFromID(projectID):
    
    if projectID.lower() == "do2":
        return "DiveOllyDive2"
    
    elif projectID.lower() == "lv":
        return "Lionelville"
    
    elif projectID.lower() == "sk":
        return "Strawberry"
    
    elif projectID.lower() == "ey":
        return "Enyo"

def yyCheckBadFramePath(fileName):
    
    match = fileName.split(".mb")[0] + "_"
    print match
    
    ESS = fileName.split("_")
    projectID = ESS[0]
    episode = ESS[1]
    shot = ESS[2]
    
    orgEp = episode
    episode = episode[0] + episode[1] + episode[2]
    
    print "Episode: " + episode
    
    if int(episode)%2 == 1:
        server = "Odd"
    else:
        server = "Even"
        
    episode = orgEp
    
    projectName = getProjectNameFromID(projectID)

    path = "//file-cluster/gdc/netrender/scenes/"+projectName + "/" + server + "/ep_" + episode + "/sc_" + shot
    try:
        layers = os.listdir(path)
    except:
        pathNew = path.replace("//file-cluster/gdc", "z:")
        tkMessageBox.showwarning(title = "Note.", message = "Below path not exist, check it.\nCheck: " + pathNew)
        raise
    
    if layers == []:
        tkMessageBox.showwarning(title = "Note.", message = "No found specific render layer.")
        raise
    
    print path
    
    thisLayer = []
    checkPointList = []
    imagesList = []
    images = []
    if layers != []:
        for i in range(len(layers)):
            print layers[i]
            if layers[i].find(".")>=0:
                continue
            images = []
            images = os.listdir(path + "/" + layers[i])
            
            if len(images) != 0:

                gotIt = 0
                imagesNew = []
                for j in range(len(images)):
                    if images[j].find(match) >= 0:
                        imagesNew.append(images[j])
                        gotIt += 1
                        
                images = imagesNew
                if images == []:
                    continue
                
                tmp1 = images[0].split(".")[0]
                tmp2 = tmp1.split("c0")[1]
                tmp3 = tmp2.split("_")
                segment = ""
                
                for j in range(len(tmp3)-1):
                    j = j+1
                    if j != len(tmp3)-1:
                        segment += tmp3[j] + "_"
                    else:
                        segment += tmp3[j]
                
                if gotIt != 0 and segment == layers[i]:
                    thisLayer.append(layers[i])
                    checkPointList.append(path + "/" + layers[i])
                    imagesList.append(images)
                    continue
    
    returnContents = []
    returnContents.append(checkPointList)
    returnContents.append(imagesList)
    returnContents.append(projectName)
    returnContents.append(episode)
    returnContents.append(shot)
    
    return returnContents

def yyCheckBadFrameCheck(contents):
    checkPointList = contents[0]
    imagesList = contents[1]
    
    badFrameTotal = []
    
    #read from database
    startNEndFrame = yyGetStartNEndFrame(contents[2], contents[3], contents[4])
    print "Database Frame:"
    print startNEndFrame
    
    for i in range(len(checkPointList)):
        
        images = imagesList[i]
        checkPoints = checkPointList[i]
        
        #init
        badFrame = []
        
        #check integreting
        endFrame = startNEndFrame[1]
        
        imageInfo = []
        temp = images[0].split(".")[0]
        
        #if 1 frame only found, and size less than 10 KB: bad frame
        if len(images) == 1 and os.path.getsize(checkPoints + "/" + images[0]) < 10000:
            badFrame.append(1001)
            badFrameTotal.append(badFrame)
            continue
        
        #if 1 frame only found, and size greater than 10 KB, okay
        elif len(images) == 1 and os.path.getsize(checkPoints + "/" + images[0]) >= 10000:
            #badFrame.append(-1)
            badFrameTotal.append("N/A")
            continue
        
        #compare to database for checking bad frame
        for j in range(endFrame - 1000):
            strJ1001 = str(j+1001)
            thisFile = temp + "." + strJ1001 + ".iff"
            
            if thisFile in images:
                imageInfo.append(checkPoints + "/" + thisFile)
                imageInfo.append(os.path.getsize(checkPoints + "/" + thisFile))
                imageInfo.append(strJ1001)
            else:
                badFrame.append(j+1001)
        
        ##check size, less than 10KB: bad frame
        for j in range(len(imageInfo)/3):
            currentSize = imageInfo[j*3+1]
            if currentSize <10000:
                badFrame.append(int(imageInfo[j*3+2]))
                continue
            
        #badFrame.sort()
        
        badFrameInt = []
        for j in range(len(badFrame)):
            badFrameInt.append(int(badFrame[j]))
        badFrameInt.sort()
        badFrameFormat = yyFormattingSequenceNumber(badFrameInt)
            
        badFrameTotal.append(badFrameFormat)
        
    return badFrameTotal

def yyGetStartNEndFrame(project, episode, shot):
    
    startNEndFrame = []

    conn = pymssql.connect(host='192.168.168.16', user='ECAUser', password='hk#$G#324f', database='idmtPlex_' + project)
    cur = conn.cursor()
    sqlCmd = 'SELECT frmStart, frmEnd FROM TB_Anim WHERE (anim_ep = \''+ episode +'\') AND (anim_sc = \''+ shot +'\')'
    cur.execute(sqlCmd)
    for row in cur:
        startNEndFrame.append(row[0])
        startNEndFrame.append(row[1])
    
    return startNEndFrame

def yyFormatList(badFrameTotal):
    
    returnContentsList = []
    for k in range(len(badFrameTotal)):
        badFrame = badFrameTotal[k]
        badFrame.sort()
        returnContents = ""
        
        for i in range(len(badFrame)):
            if i != len(badFrame)-1:
                returnContents += str(badFrame[i]) + ","
            else:
                returnContents += str(badFrame[i])

        if returnContents == "-1":
            returnContents = "N/A"
        returnContentsList.append(returnContents)

    return returnContentsList
    
def yyFormattingSequenceNumber(a):
    adjStat = []
    result = ""
    if len(a) >= 2:
        for i in range(len(a)-1):
            if a[i+1] - a[i] == 1:
                adjStat.append(1)
            else:
                adjStat.append(0)
            if i == len(a)-2:
                if a[i] - a[i-1] == 1:
                    adjStat.append(1)
                else:
                    adjStat.append(0)

    startSet = []
        
    currentStat = 0
    for i in range(len(adjStat)):
        if adjStat[i] == 1 and currentStat == 0:
            startSet.append(i)
            currentStat = 1
        elif currentStat == 1 and i == len(adjStat)-1:
            startSet.append(i)
        elif adjStat[i]==0 and currentStat == 1:
            startSet.append(i)
            currentStat = 0
    
    if startSet != []:
        inBound = 0
        count = 0
        for i in range(len(a)):
            if count > len(startSet) -1:
                count = len(startSet) -1
            if startSet[count] != i and inBound == 0:
                result += str(a[i]) + ","
            elif startSet[count] == i and inBound == 0 and i == len(a)-1 :
                result += str(a[i])
            elif startSet[count] == i and inBound == 0:
                result += str(a[i]) + "-"
                count += 1
                inBound = 1
            elif startSet[count] != i and inBound == 1:
                continue
            elif startSet[count] == i and inBound == 1:
                result += str(a[i]) + ","
                inBound = 0
                count +=1

    else:
        for i in range(len(a)):
            if i != len(a)-1:
                result += str(a[i]) + ","
            else:
                result += str(a[i])
    
    resultNew = ""
    if result[-1] == ",":
        for i in range(len(result)-1):
            resultNew += result[i]
        return resultNew
    else:
        return result


def yyCheckBadFrameWrapper(fileName):
    
    checkPointList = yyCheckBadFramePath(fileName)
    badFrameTotal = yyCheckBadFrameCheck(checkPointList)
    
    returnList = []
    returnList.append(checkPointList[0])
    returnList.append(badFrameTotal)
    
    print returnList
    if returnList == [[],[]]:
        tkMessageBox.showwarning(title = "Note.", message = "No found any rendered bad images of this file")
    
    return returnList


#yyCheckBadFrameWrapper("lv_011_001a_l1bgrgba_lr_c001.mb")
#yyCheckBadFrameWrapper("lv_025_014_l1ZWao_lr_c001.mb")
#yyCheckBadFrameWrapper("lv_010a_107_l1bg_lr_c001.mb")
#yyCheckBadFrameWrapper("do2_201_133_l1bg_c002_color_bg.mb")
#yyCheckBadFrameWrapper("do2_201_133_l3ocean_ef_c001_ocean.mb")
#yyCheckBadFrameWrapper("do2_201_003_l4test_ef_c008.mb")
#do2_201_133_l3ocean_ef_c001_ocean.mb

#381 354 998 013 015 3749
    










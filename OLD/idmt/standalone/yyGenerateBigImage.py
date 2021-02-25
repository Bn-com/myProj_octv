#!/usr/bin/env python
import os
import sys
import distutils.file_util as dfu
import PIL
import Image
import ImageDraw
import tkMessageBox
import tempfile
import re


##------------------------------- for debug
#import pymssql


#def yyGenerateGetExactFile(project, episode):
#    
#    epID = episode[0] + episode[1] + episode[2]
#    epIDInt = int(epID)
#    
#    if epIDInt % 2 == 1:
#        server = "ODD"
#    else:
#        server = "EVEN"
#        
#    path = getRepository(project) + "/Production/Render/Compositing/" + server + "/ep_" + epID
#    
#    accessPath = os.access(path, os.R_OK)
#    if accessPath != True:
#        raise Exception("path error")
#    
#    allFolders = os.listdir(path)
#    if allFolders == []:
#        raise Exception("blank folder")
#    
#    #need hard core programming
#    showImages = []
#    for i in range(len(allFolders)):
#        allImages = os.listdir(path + "/" + allFolders[i])
#        if allImages == []:
#            continue
#        showImages.append(path + "/" + allFolders[i] + "/" + allImages[0])
#        
#        
#    return showImages

#pase images and get file

def getRepository(project):
	repository = ""
	if project == "MonsterHigh":
		repository = "//file-cluster/GDC/Projects/SideProjects/TestProjects/%s" % project
	else:
		repository = "//file-cluster/GDC/Projects/%s" % project
	return repository

def yyGenerateGetNewFile(project, episode):
    
    #cam path
    episodeStr = episode[0] + episode[1] + episode[2]
    epInt = int(episodeStr)
    server = "EVEN"
    if epInt % 2 == 1:
        server = "ODD"
    
    repositoryFolder = getRepository(project)
    camPath = ''
    for str in ['ep_', '']:
        camPath = repositoryFolder + "/Production/Render/Compositing/" + server + "/" + str + episode
        if os.path.isdir(camPath):
            break

    #print camPath

    if os.access(camPath, os.R_OK) == False:
        raise Exception("no shot found")
        
    #all cameras
    allCam = os.listdir(camPath)
    #print allCam
    camIDs = []
    for i in range(len(allCam)):
        if allCam[i].find("_")>0:
            camIDs.append(allCam[i].split("_")[1])
        else:
            camIDs.append(allCam[i])
            
    camIDs.sort()
    #print camIDs
    
    #scratch dir
    if project.lower() == "strawberry":
        projectScratch = "Strawberr_Scratch"
    else:
        projectScratch = project + "_Scratch"
    
    #image blueprint
    donePath = r'\\file-cluster\GDC\Netrender\Maya_Even'
    if not os.path.isdir(donePath):
	donePath = r'\\file-cluster\GDC\Netrender\maya'
    donePath = donePath + "/T150/Projects/" + projectScratch + "/TD/Episode Picture Blueprint/" + episode
    if not os.path.isdir(donePath):
        os.makedirs(donePath)
    
    #image infoFile path
    infoFile = donePath + "/imageInfo.txt"
    
    #database dbInfoFile path
    dbInfoFile = donePath + "/dbInfo.txt"
    
    #1: get camIDs, all folder in render/compositing.
    #2: if there are no any file and image, create a blank dbInfo and imageInfo
    #3: get database info and compare to dbInfo, if not the same, just redo whole sequence
    #4: from imageInfo and dbInfo, and camPath we can figure out image to add, order
    #5: figure out which of them should be updated. and add them to list
    
    #--------------create new file
    if os.access(dbInfoFile, os.R_OK) == False:
        try:
            f = open(dbInfoFile, "w")
            f.write("")
            f.close()
        except:
            raise Exception("create dbInfoFile error")
    if os.access(infoFile, os.R_OK) == False:
        try:
            f = open(infoFile, "w")
            f.write("")
            f.close()
        except:
            raise Exception("create infoFile error")
        
    try:
        f = open(dbInfoFile, "r")
        dbInfoFileContents = f.read()
        f.close()
    except:
        raise Exception("read dbinfo file error")
    
    
    #get db info
    dbInfo = yyGetEPShot(project, episode)
    #get db order files
    try:
        dbInfo.sort()
    except:
        raise Exception("database error")
    

    #redo for testing wether db change
    redo = False
    dbInfoStr = ""
    for i in range(len(dbInfo)):
        dbInfoStr += dbInfo[i]
        
    if dbInfoFileContents != dbInfoStr:
        redo = True
    
    try:
        f = open(dbInfoFile, "w")
        f.write(dbInfoStr)
        f.close()
    except:
        raise Exception("write dbinfo file error")
    
    
    #get ready to add:
    if redo != True:
        try:
            f = open(infoFile, "r")
            infoFileContents = f.read()
            f.close()
        except:
            raise Exception("image info file read error")
    else:
        try:
            f = open(infoFile, "w")
            infoFileContents = f.write("")
            f.close()
        except:
            raise Exception("image info file write error")
        infoFileContents = ""
    
    
    #extract string to list:
    if infoFileContents != "":
        infoFileList = []
        
        infoFileContentsTemp = infoFileContents.replace("\r", "")
        
        infoFileListTemp = infoFileContentsTemp.split('\n')
        for i in range(len(infoFileListTemp) - 1):
            infoFileList.append(infoFileListTemp[i].split("@")[0])
    else:
        infoFileList = []
    
    
    #real compare stage:
    readyToAdd = []
    order = []

    for i in range(len(dbInfo)):
        if dbInfo[i] in camIDs:
            readyToAdd.append(dbInfo[i])
            order.append(i+1)
            
    #readyToAdd = []
    #order = []
    #
    #if readyToAddTemp != []:
    #    for i in range(len(readyToAddTemp)):
    #        if readyToAddTemp[i] in camIDs:
    #            readyToAdd.append(readyToAddTemp[i])
    #            order.append(orderTemp[i])
                
    paste = True
    #print readyToAdd
    if readyToAdd == []:
        paste = False
      
    #db path
    dbInfoLen = len(dbInfo)
    
    row = dbInfoLen / 4 + 1
    #blank 1200(300 * 4) by 200 * row
    #image 256 by 144
    height = row * 300
    width = 1650
    
    imageSize = [width, height]
    
    
    #--------------------------...
    #above get: camPath, camIDs, camInfo, donePath, infoFile, imageSize
    #--------------------------...
    #compare get the new one
    #get the new size
    
    info = []
    info.append(imageSize)
    info.append(readyToAdd)
    info.append(order)
    info.append(redo)
    info.append(server)
    info.append(infoFile)
    info.append(donePath + "/blueprint.jpg")
    info.append(dbInfo)
    info.append(paste)
    info.append(infoFileContents)
    
    return info
    
#read from database SQL(SELECT anim_sc FROM TB_Anim WHERE (anim_ep = '<episode>'))
def yyGetEPShot(project, episode):
    
    try:
        startNEndFrame = []
        
        conn = pymssql.connect(host='192.168.168.16', user='ECAUser', password='hk#$G#324f', database='idmtPlex_' + project)
        cur = conn.cursor()
        sqlCmd = 'SELECT anim_sc FROM TB_Anim WHERE (anim_ep = \''+ episode +'\')'
        cur.execute(sqlCmd)
        for row in cur:
            startNEndFrame.append(row[0])
        
        return startNEndFrame
    except:
        return False

#this function can list all file in one folder with filter <keywords>
def listAllFiles(directory, keywords = ""):
    files = os.listdir(directory)
    fileList = []
    if keywords != "":
        for i in range(len(files)):
            if files[i].find(keywords) >= 0:
                fileList.append(files[i])
        return fileList
    else:
        return files
    
#this function can grab an image form disk, naming convention: <shot>\tk<n>
def getAnImage(server, imageID, project, episode):
	img = ''

	parityFolder = getRepository(project) + "/Production/Render/Compositing/" + server

	episodeFolder = ''
	for str in ['ep_', '']:
		episodeFolder = parityFolder + '/' + str + episode
		if os.path.isdir(episodeFolder):
			break
	if not os.path.isdir(episodeFolder):
		return img

	shotFolder = ''
	for str in ['sc_', '', 'sh_']:	# sh_ for SportLets project
		shotFolder = episodeFolder + '/' + str + imageID
		if os.path.isdir(shotFolder):
			break
	if not os.path.isdir(shotFolder):
		return img

	for root, dirs, files in os.walk(shotFolder):
		if re.compile(r'[/\\](right|old)[/\\]|[/\\](right|old)$', re.IGNORECASE).search(root) == None:
			if files != []:
				str = root + "/" + files[int(len(files)* .618)]
				if re.compile(r'\.tga$', re.IGNORECASE).search(str) != None:
					img = str

	return img
    
    
def getThePosition(order):
    
    X = order % 4 * 410 + 20
    Y = order / 4 * 300 + 15
    
    return (X,Y)

def yyGenerateNewFile(info, project, episode):    
        
    blueprint = info[6]
    redo = info[3]
    dbInfo = info[7]
    paste = info[8]
    if redo == True:
        print "creating..."
        finalImg = Image.new("RGB", (info[0][0], info[0][1]), 0)
        #draw a text title
        draw = ImageDraw.Draw(finalImg)
        draw.text( (50,50), project + "-" + episode + " auto generated.")
        
        #draw ep text here
        for i in range(len(dbInfo)):
            draw = ImageDraw.Draw(finalImg)
            position = getThePosition(i+1)
            draw.text( (position[0], position[1] - 10), episode + "_" + dbInfo[i])
        
    elif paste == False:
        print "bypass..."
        pass
    else:
        #need modify
        print "updating..."
        finalImg = Image.open(blueprint)
        pass
    
    server = info[4]
    contents = info[9]
  
    tempContents = contents.replace("\r", "")
    contents = tempContents
    
    addContents = ""
    length = len(info[1])
    doIt = 0
    for i in range(length):
        print "Finish: " + str(int(float(i) / length * 100)) + " %"
        imageID = info[1][i]
        order = info[2][i]

        try:
            imagePath = getAnImage(server, imageID, project, episode)
        except:
            continue
        
        if imagePath.find(".tga") < 0:
            continue
	   
        print imagePath

        modTime = str(os.path.getmtime(imagePath))
        modTimeStr = str(modTime)
        
        #find same mod time
        if contents != "":
            if contents.find(imageID + "@") >=0:
                tmp1 = contents.split(imageID + "@")[1]
                timeStr = tmp1.split("\n")[0]
                if timeStr == modTimeStr:
                    addContents += str(imageID) + "@" + modTime + "\n"
                    continue
                else:
                    print "updating " + imageID
        
        position = getThePosition(order)
        
        a = os.access(imagePath, os.R_OK)
        
        temp = Image.open(imagePath)
        tempSmall = temp.resize((384,216))
        try:
            finalImg.paste(tempSmall, position)
        except:
            print "bypass " + imageID
        addContents += str(imageID) + "@" + modTime + "\n"
        doIt +=1
    
    print "Finish: 100% Done."
    
    if doIt == 0:
        paste = False
        print "Bypass pasting..."

    if paste == True and addContents != "":
        finalImg.save(blueprint, "JPEG", quality = 100)
        print "Copy done"
        
        try:
            f = open(info[5], "w")
            f.write(addContents)
            f.close()
        except:
            pass

    dfu.copy_file(blueprint, tempfile.gettempdir() + "/" + project + "_" + episode + ".jpg")
    
    
def yyGenerateImageWrapper(project, episode):    
    #get new images
    
    info = yyGenerateGetNewFile(project, episode)
    
    #update it
    yyGenerateNewFile(info, project, episode)
    ie = Dispatch("InternetExplorer.Application")
    ie.visible = 1

    ie.navigate(tempfile.gettempdir() + "/" + project + "_" + episode + ".jpg")

def yyOpenImage(project, episode):
    
    tempFolder = tempfile.gettempdir()
    #scratch dir
    if project.lower() == "strawberry":
        projectScratch = "Strawberr_Scratch"
    else:
        projectScratch = project + "_Scratch"
    
    #image blueprint
    imageOnline = r'\\file-cluster\GDC\Netrender\Maya_Even'
    if not os.path.isdir(imageOnline):
	imageOnline = r'\\file-cluster\GDC\Netrender\maya'
    imageOnline = imageOnline + "/T150/Projects/" + projectScratch + "/TD/Episode Picture Blueprint/" + episode + "/blueprint.jpg"
    imageLocal = tempFolder + "/" + project + "_" + episode + ".jpg"
    
    if os.access(imageOnline, os.R_OK) != True:
        tkMessageBox.showwarning(title = "Error", message = "No found online, please update it firstly")
        raise
    
    t1 = os.path.getmtime(imageOnline)
    try:
        t2 = os.path.getmtime(imageLocal)
    except:
        t2 = 0
    
    if os.access(imageLocal, os.R_OK) == True and t2 == t1:
        ie = Dispatch("InternetExplorer.Application")
        ie.visible = 1
        ie.navigate(tempFolder + "/" + project + "_" + episode + ".jpg")
        
    else:
        dfu.copy_file(imageOnline, tempFolder + "/" + project + "_" + episode + ".jpg")
        ie = Dispatch("InternetExplorer.Application")
        ie.visible = 1

        ie.navigate(tempFolder + "/" + project + "_" + episode + ".jpg")
    
    
#yyGenerateImageWrapper("Strawberry", "107")

#after write recode to info file
#database change ,redo = true, and images = all
#copy to local and open


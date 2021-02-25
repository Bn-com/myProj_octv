# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.

__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2013-02-27'

from cal_check_gdc import *
import datetime
import os
import time
import zipfile
import maya.cmds
import maya.OpenMaya

class my_cal_scene_checker_gdc(cal_scene_checker_gdc):
    def publish_scene(self):
        print "#" * 100
        print ""

        if self.maFolder == "":
            print "Error : Can't find model in Z:/Projects/Calimero/Common_Sync/CAL_MAYA/2013/python/teamto/hierarchy.txt. Be sure the text file is in the good place and is updated."
            return

        publishPath = self.projectFolder + self.maFolder + self.modelName.lower() + self.step + "000.ma"

        print "Publishing scene", self.scenePathName, "to", publishPath

        if not os.path.isdir(self.projectFolder + self.maFolder):
            print "Creating path", self.projectFolder + self.maFolder
            os.makedirs(self.projectFolder + self.maFolder)

        #publishSucceeded = False
        #if os.path.exists(publishPath):
        #    if self.override:
        #        shutil.copy2(self.scenePathName, publishPath)
        #        publishSucceeded = True
        #        print "Success"
        #    else:
        #        print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
        #else:
        #    shutil.copy2(self.scenePathName, publishPath)
        #    publishSucceeded = True
        #    print "Success"

        #if publishSucceeded:
        #    f = open(publishPath, 'r')
        #    content = f.read()
        #    f.close()
        #    if 'setAttr ".ftn"' in content:
        content = ""
        f = open(self.scenePathName.replace('/', '\\'), 'r')
        fo = open(publishPath.replace('/', '\\'), 'w')
        for line in f:
            if 'setAttr ".ftn"' in line:
                line = re.sub('setAttr ".ftn" -type "string" ".*/sourceimages/', 'setAttr ".ftn" -type "string" "sourceimages/', line)
                lineSplit = line.split('sourceimages/')
                name = lineSplit[1].split('/')[-1]
                newLine = lineSplit[0] + self.maFolder.replace('scenes/', 'sourceimages/') + name
                if self.step == "_tx_":
                    newLine = newLine.replace('/publish/', '/work/')
                ### TODO : verifier
                else:
                    newLine = newLine.replace('.map', '.png')
                ###
                content = newLine
            else:
                content = line
            fo.write(content)
        f.close()
        fo.close()

        try:
            rsync = publishPath.replace(self.projectFolder, '/')
            Rsynclist = datetime.datetime.now().strftime(r'\\file-cluster\GDC\Projects\Calimero\Calimero_scratch\Rsync  list\%Y%m%d.txt')
            find = False
            if os.path.isfile(Rsynclist):
                f = open(Rsynclist, 'r')
                for line in f:
                    if line.strip() == rsync:
                        find = True
                        break
                f.close()
            if not find:
                f = open(Rsynclist, 'a')
                f.write(rsync)
                f.write('\r\n')
                f.close()
        except:
            pass

        files = cmds.ls(type="file")
        for f in files:
            if cmds.attributeQuery("fileTextureName", node=f, exists=True):
                originalPath = cmds.getAttr(f + ".fileTextureName")
                originalPath = originalPath.replace('${IDMT_PROJECTS}', '//file-cluster/GDC/Projects').replace('${idmt_projects}', '//file-cluster/GDC/Projects')
                copyPath = self.maFolder.replace('scenes/', 'sourceimages/') + os.path.basename(originalPath)
                if self.step == "_tx_":
                    copyPath = copyPath.replace('/publish/', '/work/')
                if copyPath:
                    if not os.path.exists(self.projectFolder + os.path.dirname(copyPath)):
                        os.makedirs(self.projectFolder + os.path.dirname(copyPath))

                    if self.step == "_layout_" or self.step == "_anim_":
                        if os.path.isfile(originalPath):
                            print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                            if os.path.exists(self.projectFolder + copyPath):
                                if self.override:
                                    if cmds.getAttr(f + '.useFrameExtension'):
                                        startNumber = originalPath.split('.')[-2]
                                        number = int(startNumber)
                                        nDigits = len(startNumber)

                                        while os.path.isfile(originalPath):
                                            print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                            shutil.copy2(originalPath, self.projectFolder + copyPath)
                                            originalPath = originalPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                            copyPath = copyPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                            number += 1
                                    else:
                                        shutil.copy2(originalPath, self.projectFolder + copyPath)
                                    
                                    print "Success"
                                else:
                                    print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
                            else:
                                if cmds.getAttr(f + '.useFrameExtension'):
                                    startNumber = originalPath.split('.')[-2]
                                    number = int(startNumber)
                                    nDigits = len(startNumber)

                                    while os.path.isfile(originalPath):
                                        print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                        shutil.copy2(originalPath, self.projectFolder + copyPath)
                                        originalPath = originalPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                        copyPath = copyPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                        number += 1
                                else:
                                    shutil.copy2(originalPath, self.projectFolder + copyPath)
                                print "Success"
                    else:
                        if os.path.splitext(originalPath)[1] == '.map':
                            # Copy zip textures
                            if os.path.isfile(originalPath):
                                zipPath = copyPath.replace('.map', '.zip')
                                print 'Ziping', originalPath,  'to', self.projectFolder + zipPath
                                if os.path.exists(self.projectFolder + zipPath):
                                    if self.override:
                                        z = zipfile.ZipFile(self.projectFolder + zipPath, "w", zipfile.ZIP_DEFLATED) 
                                        z.write(originalPath, os.path.basename(originalPath))
                                        z.close()
                                        print "Success"
                                    else:
                                        print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
                                else:
                                    z = zipfile.ZipFile(self.projectFolder + zipPath, "w", zipfile.ZIP_DEFLATED) 
                                    z.write(originalPath, os.path.basename(originalPath))
                                    z.close()
                                    print "Success"
                            # Copy png textures
                            originalPath = originalPath.replace('.map', '.png')
                            copyPath = copyPath.replace('.map', '.png')
                            if os.path.isfile(originalPath):
                                print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                if os.path.exists(self.projectFolder + copyPath):
                                    if self.override:
                                        shutil.copy2(originalPath, self.projectFolder + copyPath)
                                        print "Success"
                                    else:
                                        print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
                                else:
                                    shutil.copy2(originalPath, self.projectFolder + copyPath)
                                    print "Success"

                        if os.path.splitext(originalPath)[1] == '.tga':
                            # Copy tga textures
                            firstOriginalPath = originalPath
                            firstCopyPath = copyPath
                            if os.path.isfile(originalPath):
                                print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                if os.path.exists(self.projectFolder + copyPath):
                                    if self.override:
                                        if cmds.getAttr(f + '.useFrameExtension'):
                                            startNumber = originalPath.split('.')[-2]
                                            number = int(startNumber)
                                            nDigits = len(startNumber)

                                            while os.path.isfile(originalPath):
                                                print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                                shutil.copy2(originalPath, self.projectFolder + copyPath)
                                                originalPath = originalPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                                copyPath = copyPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                                number += 1
                                        else:
                                            shutil.copy2(originalPath, self.projectFolder + copyPath)
                                        print "Success"
                                    else:
                                        print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
                                else:
                                    if cmds.getAttr(f + '.useFrameExtension'):
                                        startNumber = originalPath.split('.')[-2]
                                        number = int(startNumber)
                                        nDigits = len(startNumber)

                                        while os.path.isfile(originalPath):
                                            print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                            shutil.copy2(originalPath, self.projectFolder + copyPath)
                                            originalPath = originalPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                            copyPath = copyPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                            number += 1
                                    else:
                                        shutil.copy2(originalPath, self.projectFolder + copyPath)
                                    print "Success"

                            # Copy png textures
                            originalPath = firstOriginalPath.replace('.tga', '.png')
                            copyPath = firstCopyPath.replace('.tga', '.png')
                            if os.path.isfile(originalPath):
                                print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                if os.path.exists(self.projectFolder + copyPath):
                                    if self.override:
                                        if cmds.getAttr(f + '.useFrameExtension'):
                                            startNumber = originalPath.split('.')[-2]
                                            number = int(startNumber)
                                            nDigits = len(startNumber)

                                            while os.path.isfile(originalPath):
                                                print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                                shutil.copy2(originalPath, self.projectFolder + copyPath)
                                                originalPath = originalPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                                copyPath = copyPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                                number += 1
                                        else:
                                            shutil.copy2(originalPath, self.projectFolder + copyPath)
                                        print "Success"
                                    else:
                                        print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
                                else:
                                    if cmds.getAttr(f + '.useFrameExtension'):
                                        startNumber = originalPath.split('.')[-2]
                                        number = int(startNumber)
                                        nDigits = len(startNumber)

                                        while os.path.isfile(originalPath):
                                            print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                            shutil.copy2(originalPath, self.projectFolder + copyPath)
                                            originalPath = originalPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                            copyPath = copyPath.replace('.' + str(number).zfill(nDigits) + '.', '.' + str(number + 1).zfill(nDigits) + '.')
                                            number += 1
                                    else:
                                        shutil.copy2(originalPath, self.projectFolder + copyPath)
                                    print "Success"

def publish(modelName, p=True):
	obj = my_cal_scene_checker_gdc(modelName, publish=p, override=True)

	if obj.val:
		for logLvl, logMsg in obj.val:
			if logLvl == "error":
				return False

	if p:
		f = open('Z:/Projects/Calimero/Common_Sync/CAL_MAYA/2013/python/teamto/hierarchy.txt', 'r')
		projectFolder = "Z:/Projects/Calimero/Common_Sync/CAL_MAYA/"
		maFolder = ""
		for line in f:
			if '|' + obj.modelName + '|' in line:
				maFolder = line.replace('|', '/').replace('\r', '').replace('\n', '').replace('MODELS/', 'scenes/')
				maFolder += 'publish/'
		f.close()
		if maFolder == "":
			return False;

		publishPath = projectFolder + maFolder + obj.modelName.lower() + obj.step + "000.ma"
		if not os.path.isfile(publishPath):
			return False

		statinfo = os.stat(publishPath)
		if time.time() -  statinfo.st_mtime > 14400:
			return False

	return True

def makePng(source, dest):
	image = maya.OpenMaya.MImage()
	image.readFromFile(source)
	image.resize(256, 256)
	image.writeToFile(dest, "png") 
	image.release()
	maya.cmds.idmtFile(source, dest, copyModified = True)

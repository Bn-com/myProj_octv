# -*- coding: utf-8 -*-
import datetime
import hashlib
import os
import re
import zipfile
import rarfile
#import maya.mel

def isGdc(asset):
    rs = False
    f = open(r'\\file-cluster\GDC\Netrender\Maya_Even\N196\hierarchy.txt', 'r')
    for line in f:
        if '|' + asset + '|' in line:
            rs = True
            break
    f.close()
    return rs

def GetFileMd5(filename):
    myhash = hashlib.md5()
    f = file(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest().upper() 

def myMove(source, temp, dest):
    cmd = r'move "%s" "%s"' % (temp, dest)
    print cmd
    os.system(r'\\file-cluster\GDC\Resource\Support\bin\checkinClient ' + cmd)
    if os.path.isfile(temp):
        os.remove(temp)

    Rsynclist = datetime.datetime.now().strftime(r'\\file-cluster\GDC\Projects\Calimero\Common_Sync\CAL_MAYA\sourceimages\log\%Y%m%d.txt')
    f = open(Rsynclist, 'a')
    f.write('%s -> %s\r\n' % (source, dest))
    f.close()

def myCopy(source, dest):
    cmd = r'copy "%s" "%s"' % (source, dest)
    print cmd
    os.system(r'\\file-cluster\GDC\Resource\Support\bin\checkinClient ' + cmd)

    Rsynclist = datetime.datetime.now().strftime(r'\\file-cluster\GDC\Projects\Calimero\Common_Sync\CAL_MAYA\sourceimages\log\%Y%m%d.txt')
    f = open(Rsynclist, 'a')
    f.write('%s -> %s\r\n' % (source, dest))
    f.close()

def syncFolder(sourceFolder, destFolder):
    if not os.path.isdir(sourceFolder):
        return
    files = os.listdir(sourceFolder)
    for file in files:
        source = os.path.join(sourceFolder, file)
        if not os.path.isfile(source):
            continue
        if re.compile(r'\.zip$', re.IGNORECASE).search(file) != None:
            map = re.compile(r'\.zip$', re.IGNORECASE).sub('.map', file)
            dest = os.path.join(destFolder, map)
            try:
                zip = zipfile.ZipFile(source, 'r')
                for info in zip.infolist():
                    if re.search(r'[\\/]', info.filename) != None:
                        continue
                    dest = os.path.join(destFolder, info.filename)
                    isLatest = False
                    if os.path.isfile(dest):
                        statDest = os.stat(dest)
                        timeDest = datetime.datetime.fromtimestamp(statDest.st_mtime)
                        timeSource = datetime.datetime(info.date_time[0], info.date_time[1], info.date_time[2], info.date_time[3], info.date_time[4], int(info.date_time[5]))
                        #if timeDest > timeSource:
                        delta = timeDest - timeSource
                        if delta > datetime.timedelta(seconds = -4):
                            isLatest = True
                    if not isLatest:
                        temp = os.path.join(os.getenv('TEMP'), info.filename)
                        zip.extract(info.filename, os.getenv('TEMP'))
                        myMove(source, temp, dest)
                zip.close()
            except:
                try:
                    rar = rarfile.RarFile(source, 'r')
                    for info in rar.infolist():
                        if re.search(r'[\\/]', info.filename) != None:
                            continue
                        dest = os.path.join(destFolder, info.filename)
                        isLatest = False
                        if os.path.isfile(dest):
                            statDest = os.stat(dest)
                            timeDest = datetime.datetime.fromtimestamp(statDest.st_mtime)
                            timeSource = datetime.datetime(info.mtime[0], info.mtime[1], info.mtime[2], info.mtime[3], info.mtime[4], int(info.mtime[5]))
                            #if timeDest > timeSource:
                            delta = timeDest - timeSource
                            if delta > datetime.timedelta(seconds = -4):
                                isLatest = True
                        if not isLatest:
                            temp = os.path.join(os.getenv('TEMP'), info.filename)
                            rar.extract(info.filename, os.getenv('TEMP'))
                            myMove(source, temp, dest)
                    rar.close()
                except:
                    pass
        else:
            dest = os.path.join(destFolder, file)
            isLatest = False
            if os.path.isfile(dest):
                statSource = os.stat(source)
                statDest = os.stat(dest)
                if statDest.st_mtime - statSource.st_mtime > -4:
                    isLatest = True
                #else:
                #    md5Source = GetFileMd5(source)
                #    md5Dest = GetFileMd5(dest)
                #    if md5Source == md5Dest:
                #        isLatest = True
            if not isLatest:
                myCopy(source, dest)

def syncSourceimages():
    RS = r'\\file-cluster\GDC\Projects\Calimero\Common_Sync\CAL_MAYA\sourceimages'
    GDC = r'\\file-cluster\GDC\Projects\Calimero\Project\sourceimages'
    assetTypes = os.listdir(RS)
    for assetType in assetTypes:
        typeFolder = os.path.join(RS, assetType)
        if not os.path.isdir(typeFolder):
            continue
        assetMaps = os.listdir(typeFolder)
        for assetMap in assetMaps:
            mapFolder = os.path.join(typeFolder, assetMap)
            if not os.path.isdir(mapFolder):
                continue
            assets = os.listdir(mapFolder)
            for asset in assets:
                assetFolder = os.path.join(mapFolder, asset)
                if not os.path.isdir(assetFolder):
                    continue
                if not isGdc(asset):
                    continue
                destFolder = os.path.join(GDC, assetType, asset)
                #if not os.path.isdir(destFolder):
                #    #continue
                #    cmd = r'md "%s"' % (destFolder)
                #    print cmd
                #    os.system(r'\\file-cluster\GDC\Resource\Support\bin\idmtCheckin ' + cmd)
                #    #os.makedirs(destFolder)
                sourceFolder = os.path.join(assetFolder, 'publish')
                syncFolder(sourceFolder, destFolder)
                sourceFolder = os.path.join(assetFolder, 'work')
                syncFolder(sourceFolder, destFolder)

if __name__ == "__main__":
    syncSourceimages()
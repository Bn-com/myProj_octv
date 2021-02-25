'''
Created on Mar 25, 2013

@author: wanshoulong
'''
# coding=utf-8
import os
import re
import shutil  

def copytree(src, dst, symlinks=False):  
    names = os.listdir(src)  
    if not os.path.isdir(dst):  
        os.makedirs(dst)  
    errors = []  
    for name in names:  
        srcname = os.path.join(src, name)  
        dstname = os.path.join(dst, name)  
        try:  
            if symlinks and os.path.islink(srcname):  
                linkto = os.readlink(srcname)  
                os.symlink(linkto, dstname)  
            elif os.path.isdir(srcname):  
                copytree(srcname, dstname, symlinks)  
            else:  
                if os.path.isdir(dstname):  
                    os.rmdir(dstname)  
                elif os.path.isfile(dstname):  
                    os.remove(dstname)  
                shutil.copy2(srcname, dstname)  
            # XXX What about devices, sockets etc.?  
        except (IOError, os.error) as why:  
            errors.append((srcname, dstname, str(why)))  
        # catch the Error from the recursive copytree so that we can  
        # continue with other files  
        except OSError as err:  
            errors.extend(err.args[0])  
    try:  
        shutil.copystat(src, dst)  
    except WindowsError:  
        # can't copy file access times on Windows  
        pass  
    except OSError as why:  
        errors.extend((src, dst, str(why)))  
    if errors:  
        raise Error(errors)

def maPublishCacheFromFile(folder):
    children=os.listdir(folder)
    for item in children :
        if os.path.isfile(folder+'/'+item):
            print '-----start------'
            print item
            buff=item.split('_')
            episode=buff[1]
            sequence=buff[2]
            shot=buff[3]
            sourcePath='Y:/005_EPISODES_Caches/'
            destPath=folder+'/005_EPISODES_Caches/'
            allcache=os.listdir(sourcePath)
            for cf in allcache :
                if re.match(episode+'_',cf):
                    sourcePath=sourcePath+cf+'/'
                    destPath=destPath+cf+'/'
                    break
            sourcePath=sourcePath+sequence+'/'+shot
            destPath=destPath+sequence+'/'+shot
            

            
            if os.path.isdir(sourcePath):
                print sourcePath
                print unicode(destPath,'cp936')
                print '-----end-------'
                copytree(sourcePath,destPath)
                
    print 'Copy Cache is OK!!!!!!!!!!!!!!!!!!!!'
            
            
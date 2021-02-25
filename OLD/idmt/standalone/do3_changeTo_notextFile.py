# -*- coding: utf-8 -*-
'''
Created on 2012-12-72012

@author: zhangben
'''
import os ,re 
import os.path
import sys


def do3_ref_switch_TX_NOTX(filePath,wantTo="_notex"):
    if wantTo =="_tex":
        usedStyle = "_notex"
    else:
        usedStyle = "_tex"
    
    savePath = "D:\No_text_AutoSave\\"
    fileName = os.path.split(filePath)
    
    newFile = savePath + fileName[-1]
    
    if os.path.exists(savePath) != True:
        os.mkdir(savePath)  
    if os.path.isfile(newFile):
         os.remove(newFile)
    
    p = re.compile(usedStyle)
    openFile = open(filePath,'r')
    writeFile = open(newFile,'w')
    for eachLine in openFile.readlines():
        if startWith(eachLine,"\W*(//file-cluster)"):
            newLine = p.sub(wantTo,eachLine)
            writeFile.write(newLine)
        else:
            writeFile.write(eachLine)
    
    openFile.close() 
    writeFile.close()
    #print "file :%s was saved"%(newFile)       
def startWith(sourceStr,mathLetter):
#mathLetter = "\W*file"
    p = re.compile(mathLetter)
    if p.match(sourceStr) !=None :
        return True
    else:
        return False

if __name__ =="__main__":
    fileName = sys.argv[1]
    do3_ref_switch_TX_NOTX(fileName)

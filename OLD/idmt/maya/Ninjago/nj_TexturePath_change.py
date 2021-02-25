# -*- coding: utf-8 -*-
import os
import re
import shutil
import sys

path = sys.argv[1]
txt = open(path, 'r');
try:
    fileContent = txt.readlines()
    print('Loading........')
finally:
    txt.close()
for i in range(len(fileContent)):
    if len(fileContent[i].split('\r\n')) > 1:
        temp = fileContent[i].split('\r\n')
        fileContent[i] = temp[0]            
readInfos = fileContent
    

    
needIndexs = []
for i in range(len(readInfos)):  
    if 'Read {' in readInfos[i]:
        needIndexs.append(i)
            
   
    
for j in needIndexs:
    for k in range(j,j+100):
        checkState = 0
        if 'file' in readInfos[k]:
            newLineInfo = readInfos[k].replace('Z:/Projects/Ninjago/Ninjago_scratch/lighting&compositing/2015','Z:/Projects/Ninjago/Reference/picturereference/MasterLighting/2015')
            readInfos[k] = newLineInfo
            checkState = 1
        if checkState:
            break

txt = open(path, 'w')
try:
    txt.writelines(str(a) + '\r\n' for a in readInfos)
    print('Writing........')
finally:
    txt.close()



#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-9-122013

@author: zhangben

'''
import re,os,sys

def modefyRF_mayaFile_save_another(ma_filePath,sourStr,subStr,ma2mb=True,varAlt=True):
    ma_filePath_shn = os.path.basename(ma_filePath)
 #========UNUSED===========   
    ma_filePath_shn_spl= os.path.splitext(os.path.basename(ma_filePath))[0].split(u'_')
    sq_num = ma_filePath_shn_spl[1]
    sc_num = ma_filePath_shn_spl[2]
    mode = ma_filePath_shn_spl[3]
    ves_numStr = ma_filePath_shn_spl[4]
 #==================================   
    fileFolder = os.path.dirname(ma_filePath) 
    
    newStorFolder = u'%s/modefiedFolder'%fileFolder
    newStorFolder = newStorFolder.replace(u'\\',u'/')
    
    if not os.path.isdir(newStorFolder):
        os.mkdir(newStorFolder)
    
    
    newFilePath = u'%s/%s'%(newStorFolder,ma_filePath_shn)
    read_mf = open(ma_filePath,'r')
    write_mf = open(newFilePath,'w')
    for el in read_mf:
        write_mf.write(modefy_maFile_contait(el,sourStr,subStr,ma2mb))
         
    read_mf.close()
    write_mf.close()       
   
def modefy_maFile_contait(lineContant,sourceChar,substituteChar,ma2mb = False,changeVariable= True):
    modefiedContant = lineContant.replace(sourceChar,substituteChar)
    if changeVariable == True:
        modefiedContant = modefiedContant.replace(u"${IDMT_PROJECTS}",u"//file-cluster/GDC/Projects")
    if ma2mb == True:
        modefiedContant = modefiedContant.replace(u'.ma\";',u'.mb\";')
    return modefiedContant


if __name__ =="__main__":
    fileName = sys.argv[1]
    sourceChar = u"DiveollyDive4_Scratch/Modeling&Texture/toLayout/car/car_vison03.mb"
    substituteChar = u"Project/scenes/props/p407001TractorShovel/master/do4_p407001TractorShovel_h_ms_anim.mb"
    modefyRF_mayaFile_save_another(fileName,sourceChar,substituteChar,True,True)

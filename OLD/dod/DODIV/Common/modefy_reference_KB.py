#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-92013

@author: zhangben
'''
import re,os,sys
import idmt.maya.DOD.DODIV.Common.modefy_maFileReference as mmfr

def blankProc():
    pass



def findExactFile(searchPath,fileName,resourceFilePath):#==================找到正确的参考文件===若找不到记录==================
    p_ex = re.compile('%s_h'%(descriptionChar),re.I)
    p_ms = re.compile('_ms_anim')
    fileStor = []
    for root,dirs,files in os.walk(searchPath):
        for filePath in files:
            if p_ex.search(filePath) != None and p_ms.search(filePath) != None and root.find('history') == -1:
                fileStor.append(os.path.join(root,filePath))
    if len(fileStor) == 1:
        return fileStor
    else:
        rec_filePath = r"\\file-cluster\GDC\Projects\Qsanguo\Qsanguo_Scratch\TD\documente\rec_refFile_info.txt"
        resourceFileName = os.path.basename(resourceFilePath)  #===========找不到的参考文件名字
        rec_infor = '%s : %s'%(fileName,resourceFileName)           #===========记录 镜头文件 与 参考文件 的信息===========
        record_fileInformation(rec_filePath,rec_infor)                      #====写入文件=====================
        return None



if __name__ =="__main__":
    fileName = sys.argv[1]
    sourceChar = u"//192.168.1.7/software/GDC"
    substituteChar = u"L:"
    mmfr.modefyRF_mayaFile_save_another(fileName,sourceChar,substituteChar,False,True)




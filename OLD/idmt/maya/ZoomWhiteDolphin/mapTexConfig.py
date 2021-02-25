# -*- coding: utf-8 -*-
import maya.cmds as mc
'''
【通用：修正map后缀中存在多种.格式的情况】
统一更改贴图，考虑到不是所有人有权限改服务器端，则临时放入D盘指定temp
上传后手动清理D盘temp文件
Author: 沈  康
Data    :2013_04_27
'''
def sk_mapTexConfig():    
    #创建目录
    tempPath = 'D:/Info_Temp/temp/texTemp'
    mc.sysFile(tempPath ,makeDir = 1)
    #获取贴图节点
    texNames = mc.ls(type = 'file')
    for i in range(len(texNames)):
        #获取贴图路径
        sysPath = mc.getAttr((texNames[i] + '.fileTextureName'))
        #获取最终文件名
        tempSplit = sysPath.split('/')[-1]
        tempNames = tempSplit.split('.')
        finalName = tempNames[0]+'.'+tempNames[-1]
        #复制，改名
        mc.sysFile(sysPath ,copy = (tempPath + '/' + tempSplit))
        mc.sysFile((tempPath + '/' + tempSplit) , rename = (tempPath + '/' +finalName) )
        #重新更改路径
        mc.setAttr((texNames[i] + '.fileTextureName'),(tempPath + '/' +finalName),type = 'string')



    

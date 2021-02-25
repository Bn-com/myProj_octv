#-*- coding: utf-8 -*-
#u删除选中角色的所有缓存节点
__author__ = 'ZhangXiaoYun'

import  maya.cmds as mc
import  maya.mel  as  mel
def doHairNclothCache():
    obj = mc.ls(sl = 1)
    allCacheShape = []
    allHairShape = mc.ls(type = 'hairSystem')
    allClothShape = mc.ls(type = 'nCloth')

    for  eleObj  in obj:
        bigGroup = eleObj.split(':')[0]
        for hairShape in allHairShape:
            if bigGroup  in hairShape:
                allCacheShape.append(hairShape)
        for clothShape in allClothShape:
            if bigGroup  in clothShape:
                allCacheShape.append(clothShape)
    try:
        mc.select(allCacheShape)
    except:
        mc.error(u'===please  selet  anything==')

    mel.eval('performDeleteNclothCache 1')
#doHairNclothCache()
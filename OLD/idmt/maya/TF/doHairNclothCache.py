# -*- coding: utf-8 -*-
__author__ = 'ZhangXiaoYun'

import  maya.cmds as mc
import  maya.mel  as  mel
import idmt.pipeline.db
#弹框选择是否检查缓存，选是：查出哪些角色的缓存有问题，弹（delete）并error删除这些角色的缓存
def  TF_checkCaches():
    charName = []
    worngCache = 0
    cachefile = mc.ls(type = 'cacheFile')
    for  eachfile in cachefile :
        number = eachfile[-1]
        if  int(number) != 1 and eachfile.split('_')[1] not in charName :
            char = eachfile.split('_')[1]
            charName.append(char)
            worngCache = 1
    for  char in charName:
        #char = 'c003001Twinkle'
        try:
            Name = '*%s:*'%char
            hair = mc.ls(Name,type = 'hairSystem')
            worngCache = mc.select(hair,add = 1)
            cloth = mc.ls(Name,type = 'nCloth')
            mc.select(cloth,add = 1)
        except:
            print 'wrong'
    if worngCache != 0:
        mel.eval('performDeleteNclothCache 1')
        mc.error(label=u'做过多次缓存，请删除框中所有显示的缓存文件，再做缓存')
    else:
        showResult = mc.window(iconName='showresult')
        mc.columnLayout( adjustableColumn=True )
        mc.text(label=u'恭喜，没有重复缓存，缓存生成正确！')
        mc.button(label=u'关闭', command=('mc.deleteUI(\"' + showResult + '\", window=True)') )
    mc.showWindow()

def TF_doHairNclothCache():
    obj = mc.ls(sl = 1)
    allCacheShape = []
    allHairShape = mc.ls(type = 'hairSystem')
    allClothShape = mc.ls(type = 'nCloth')
    shotName = mc.file(q=1,sn=1,shn=1)
    anim = idmt.pipeline.db.GetAnimByFilename(shotName)
    startFrame = anim.frmStart
    endFrame = anim.frmEnd
    for  eleObj  in obj:
        bigGroup = eleObj.split(':')[0]
        hairDym = bigGroup+':hair_con.HairDynamicCtrlClock'
        clothDym = bigGroup+':hair_con.cloth_DynamicCtrlCloak'
        try:
            hairDymValue = mc.getAttr(hairDym)
            hairDymFrame = mc.getAttr('%s:hair_con.HairStartFrame'%bigGroup)
        except:
            mc.error(bigGroup+u'===头发解算控制器或起始帧命名错误==')
        try:
            clothDymValue = mc.getAttr(clothDym)
            clothDymFrame = mc.getAttr('%s:hair_con.cloth_StartFrame'%bigGroup)
        except:
            mc.error(bigGroup+u'===布料解算控制器或起始帧数命名错误==')
        if  hairDymValue :
            for hairShape  in allHairShape:
                if bigGroup  in hairShape:
                    allCacheShape.append(hairShape)
            if hairDymFrame >endFrame:
                mc.error(bigGroup+u'===需要解算头发的起始帧数太大，请修改==')
        if  clothDymValue :
            for clothShape  in allClothShape:
                if bigGroup  in clothShape:
                    allCacheShape.append(clothShape)
            if clothDymFrame >endFrame:
                mc.error(bigGroup+u'===需要解算布料的起始帧数太大，请修改==')

    mel.eval('performCreateNclothCache 1 "add"')
    try:
        mc.select(allCacheShape)
    except:
        mc.error(u'===please  selet  anything==')

    mel.eval('optionVar -iv nclothCacheTimeRange 3')
    mel.eval('floatFieldGrp -e -enable true nclothCacheStartEndTime')
    mel.eval('optionVar -floatValue  nclothCacheStartTime 950')
    mel.eval('zwQueryCameraTime "defaultRenderGlobals"')
    mel.eval('int $EndTimes = `getAttr "defaultRenderGlobals.endFrame"`')
    mel.eval('optionVar -floatValue nclothCacheEndTime $EndTimes')
    mel.eval('floatFieldGrp -e -v1 `optionVar -query nclothCacheStartTime` -v2 `optionVar -query nclothCacheEndTime` nclothCacheStartEndTime')
    mel.eval('optionVar -stringValue nclothCacheFormat "mcx"')
    mel.eval('optionMenuGrp -e -v "mcx" formatMenu')
    mel.eval('string $distrib = "OneFile"')
    mel.eval('optionVar -intValue nclothCacheDistrib 2')
    mel.eval('optionVar -intValue nclothRefresh 1')
    mel.eval('optionVar -stringValue nclothCacheName "Automatic"')
    mel.eval('optionVar -intValue nclothCacheUsePrefix 0')
    mel.eval('string $directory = `zwCacheSetDirectory "nClothCache" "cacheSetDirectory"`')
    mel.eval('optionVar -intValue nclothCachePerGeometry 1')
    mel.eval('checkBoxGrp -edit -value1 `optionVar -query nclothCachePerGeometry` cachePerGeometry')
    mel.eval('radioButtonGrp -e -sl 1 nclothCacheDist2')
    mel.eval('radioButtonGrp -e -sl 1 nclothCacheTimeRange3')
    mel.eval('zwQueryCameraTime "defaultRenderGlobals"')

    checkwidow = mc.window( title=u"检测缓存", iconName='checkcache', widthHeight=(200, 55) )
    mc.columnLayout( adjustableColumn=True )
    mc.text( label=u'请在制作完缓存后使用这个窗口' )
    commandString = 'checkCaches();mc.deleteUI(\"' + checkwidow + '\", window=True)'
    mc.button( label=u'检测缓存',command =commandString )
    mc.button( label=u'不检测并关闭', command=('mc.deleteUI(\"' + checkwidow + '\", window=True)') )
    mc.showWindow(checkwidow)


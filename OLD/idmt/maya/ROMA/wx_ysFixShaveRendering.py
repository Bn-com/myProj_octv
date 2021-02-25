# -*- coding: gbk -*-
import os, sys, re
import maya.cmds as cmd
import maya.mel as mel

mel.eval('source "D:/Alias/MAYA8.5/2013/others/showEditor.mel"')
mel.eval('source "//file-cluster/GDC/Resource/Support/AnimalLogic/mayaman2.0.7/mel/AEMayaManCustomShaderTemplate.mel"')
mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/2013/zjRemoveNamespace.mel"')
mel.eval('zjRemoveNamespace;')
animalName = cmd.file(query=True, ns=True)


def updatemmShdr():
    mmShdr = cmd.ls(type='MayaManCustomShader')
    try:
        mmShdr = cmd.ls(type='MayaManCustomShader')
        for item in mmShdr:
            mel.eval('showEditor("'+item+'")')
            mel.eval('callCSUpdateCustomShader("'+item+'", "'+item+'.ShaderFile")')
    except:
        pass
    return mmShdr
    
def removeDeformedShape():
    shaveGrp = []
    transGrp = cmd.ls(type='transform')
    mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/2013/zjMakeLightLinks.mel"')
    for item in transGrp:
        if re.search('shaveDisplayGroup', item) or re.search('shave_importArchive_group', item):
            try:
                meshShapes = cmd.listRelatives(item, type='mesh', ad=1)
                for item in meshShapes:
                    try:
                        cmd.setAttr(item+'.intermediateObject', 0)
                        if re.search('Deformed', item):
                            cmd.delete(item)
                    except:
                        pass
            except:
                print "There is one empty Shave Group at least!"
            
        if re.search('shave', item) and cmd.nodeType(item) == 'transform':
            shaveGrp.append(item)
           
    lights = cmd.ls(lights=True) 
    cmd.select(lights, r=True)
    cmd.select(shaveGrp, tgl=True)
    mel.eval('zjMakeLightLinks;')
    cmd.select(cl=True)   
       
def fixLostTexture():
    shaveGrp = re.compile('^shave_importArchive_group*', re.I)
    shaveImportGrp = [item for item in cmd.ls(type='transform') if shaveGrp.match(item) != None]
    if len(shaveImportGrp) > 1:
        cmd.confirmDialog(title='confirmDialog', message=u'请删除多余的shave_importArchive_group', button='OK')
        return
    
    mmShdr = updatemmShdr()
    try:
        mmNode = cmd.ls(type='MayaManAttributes')
        isLightSeted = (item+'.mmma_LightSet' for item in mmNode\
                    if cmd.listConnections(item+'.mmma_LightSet', s=1, d=0)!=None)
        for item in isLightSeted:
          lightSet = cmd.listConnections(item, s=1, d=0)
          cmd.disconnectAttr(lightSet[0]+'.message', item)
    except:
        pass  
            
    if animalName.count('peg') != 0:        
        for item in mmShdr:
            if re.search('SHD_shaveHairBodynew_fur', item) or re.search('SHD_shaveHairHeadnew_fur', item) or re.search('SHD_shaveHairLegsnew_fur', item):
                cmd.setAttr(item+'.roottexture', '//Serverone/CONTENT_4_GLOBAL/PRJ_winxII/MC_winxII/sourceimages/characters/animals/peg/default/2k/animals_peg_default_shave_color_2k.iff', type='string')
                cmd.setAttr(item+'.tiptexture', '//Serverone/CONTENT_4_GLOBAL/PRJ_winxII/MC_winxII/sourceimages/characters/animals/peg/default/2k/animals_peg_default_shave_color_2k.iff', type='string')
                cmd.setAttr(item+".convertRoottexture", 1)
                cmd.setAttr(item+".convertTiptexture", 1)
    if animalName.count('kiko') != 0:
        for item in mmShdr:
            if re.search('SHD_shave_body', item):
                cmd.setAttr(item+'.roottexture', '//Serverone/CONTENT_4_GLOBAL/PRJ_winxII/MC_winxII/sourceimages/characters/animals/kiko/default/2k/animals_kiko_default_body_color_2k.iff', type='string')
                cmd.setAttr(item+'.tiptexture', '//Serverone/CONTENT_4_GLOBAL/PRJ_winxII/MC_winxII/sourceimages/characters/animals/kiko/default/2k/animals_kiko_default_body_color_2k.iff', type='string')
                cmd.setAttr(item+".convertRoottexture", 1)
                cmd.setAttr(item+".convertTiptexture", 1)
    if animalName.count('unicorn') != 0:
        for item in mmShdr:
            if re.search('SHD_shave_body', item) or ('SHD_shave_head', item) or ('SHD_shave_legs', item):
                cmd.setAttr(item+'.roottexture', '//Serverone/CONTENT_4_GLOBAL/PRJ_winxII/MC_winxII/sourceimages/characters/animals/unicorn/default/2k/animals_unicorn_default_shave_color_2k.iff', type='string')
                cmd.setAttr(item+'.tiptexture', '//Serverone/CONTENT_4_GLOBAL/PRJ_winxII/MC_winxII/sourceimages/characters/animals/unicorn/default/2k/animals_unicorn_default_shave_color_2k.iff', type='string')
                cmd.setAttr(item+".convertRoottexture", 1)
                cmd.setAttr(item+".convertTiptexture", 1)
    if animalName.count('believix') != 0:        
        for item in mmShdr:
            if re.search('SHD_shaveHairBodynew_fur', item) or re.search('SHD_shaveHairHeadnew_fur', item) or re.search('SHD_shaveHairLegsnew_fur', item):
                cmd.setAttr(item+'.roottexture', '//Serverone/CONTENT_4_GLOBAL/PRJ_winxII/MC_winxII/sourceimages/characters/animals/peg/believix/4k/animals_peg_believix_shave_color_4k.iff', type='string')
                cmd.setAttr(item+'.tiptexture', '//Serverone/CONTENT_4_GLOBAL/PRJ_winxII/MC_winxII/sourceimages/characters/animals/peg/believix/4k/animals_peg_believix_shave_color_4k.iff', type='string')
                cmd.setAttr(item+".convertRoottexture", 1)
                cmd.setAttr(item+".convertTiptexture", 1)

    removeDeformedShape()
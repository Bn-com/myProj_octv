#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
from pymel.core import *
import re
sys.path.append('//file-cluster/gdc/Resource/Support/Maya/projects/VickytheViking/')
from vv_deleteTurtleNodes import *

import idmt.maya.DOD.DODIV.Maya.commonProperties as docp
reload(docp)


def layerNameByCheck():

    layerNames = ''
    version = ''
    contentName = ''
    layerNamesList = []
    sepSn = []
    sn = mc.file(sceneName=True, q=True, shortName=True)
    if sn.find('lr') >= 0:
        sepSn = sn.split('lr')

    charName = mc.textFieldGrp('charNameText', q=True, text=True)
    versionName = mc.textFieldGrp('VersionText', q=True, text=True)
    contentName = charName + versionName

    if mc.radioButtonGrp('fileType', q=True, select=True) == 2 and sepSn[1][-3:] == '.ma':
        sepSn[1] = sepSn[1].replace('.ma', '.mb')
    elif mc.radioButtonGrp('fileType', q=True, select=True) == 1 and sepSn[1][-3:] == '.mb':
        sepSn[1] = sepSn[1].replace('.mb', '.ma')

    if mc.checkBoxGrp('l1', q=True, v1=True):
        layerNames = layerNames + 'Clr'
        layerNamesList.append(sepSn[0] + contentName + 'Clr' + '_lr' + sepSn[1])

    if mc.checkBoxGrp('l1', q=True, v2=True):
        layerNames = layerNames + 'Occ'
        layerNamesList.append(sepSn[0] + contentName + 'Occ' + '_lr' + sepSn[1])

    if mc.checkBoxGrp('l2', q=True, v1=True):
        layerNames = layerNames + 'Shw'
        layerNamesList.append(sepSn[0] + contentName + 'Shw' + '_lr' + sepSn[1])

    if mc.checkBoxGrp('l2', q=True, v2=True):
        layerNames = layerNames + 'Nor'
        layerNamesList.append(sepSn[0] + contentName + 'Nor' + '_lr' + sepSn[1])

    if mc.checkBoxGrp('l3', q=True, v1=True):
        layerNames = layerNames + 'Zdp'
        layerNamesList.append(sepSn[0] + contentName + 'Zdp' + '_lr' + sepSn[1])

    if mc.checkBoxGrp('l3', q=True, v2=True):
        layerNames = layerNames + 'Fsl'
        layerNamesList.append(sepSn[0] + contentName + 'Fsl' + '_lr' + sepSn[1])

    if mc.checkBoxGrp('l4', q=True, v1=True):
        layerNames = layerNames + 'Idp'
        layerNamesList.append(sepSn[0] + contentName + 'Idp' + '_lr' + sepSn[1])

    if mc.checkBoxGrp('l4', q=True, v2=True):
        layerNames = layerNames + 'Cao'
        layerNamesList.append(sepSn[0] + contentName + 'Cao' + '_lr' + sepSn[1])

    if mc.checkBoxGrp('l5', q=True, v1=True):
        layerNames = layerNames + 'Cau'
        layerNamesList.append(sepSn[0] + contentName + 'Cau' + '_lr' + sepSn[1])

    if mc.checkBoxGrp('l5', q=True, v2=True):
        layerNames = layerNames + 'Arn'
        layerNamesList.append(sepSn[0] + contentName + 'Arn' + '_lr' + sepSn[1])

    layerNames = sepSn[0] + contentName + layerNames + '_lr' + sepSn[1]
    return [layerNames, layerNamesList]


def changeLayrNameText():
    sn = mc.file(sceneName=True, q=True, shortName=True)
    if sn.find('lr') < 0:
        mc.text('fileNameResult', edit=True, label=u'Confirm lr', bgc=[1, 0, 0])
    else:
        if mc.radioButtonGrp('checkLayer', q=True, select=True) == 2:
            ln = layerNameByCheck()[0]
            mc.text('fileNameResult', edit=True, label=ln, bgc=[0, .5, 0])
        else:
            lns = layerNameByCheck()[1]
            if len(lns):
                fileNameResult = ''
                num = len(lns)
                for i in range(num):
                    if i < num - 1:
                        fileNameResult = fileNameResult + lns[i] + '\n'
                    else:
                        fileNameResult = fileNameResult + lns[i]

                mc.text('fileNameResult', edit=True, label=fileNameResult, bgc=[0, .5, 0])
            else:
                mc.text('fileNameResult', edit=True, label='', bgc=[.3, .3, .3])


def expLayerFiles():

    execfile(r'//file-cluster/gdc/Resource/Support/Maya/projects/VickytheViking/vv_sop.py')

    if len(mc.ls(sl=True)) == 0:
        mc.confirmDialog(title='Confirm', message=u'please select you need objects', defaultButton='Yes')
        return

    cam = docp.config_shotFile_cameraParameter()
    select(cam, add=True)

    nr_dl = get_noRnd_DL()
    if nr_dl:
        select(nr_dl, add=True)
    savePath = mc.workspace(q=True, fn=True) + '/scenes/'
    sn = mc.file(sceneName=True, q=True, shortName=True)
    if mc.radioButtonGrp('checkLayer', q=True, select=True) == 2:
        if sn.find('lr') > -1:
            if mc.textFieldGrp('charNameText', q=True, text=True) == '':
                mc.text('fileNameResult', edit=True, label=u'Charactor Name Blank!!!!', bgc=[1, 0, 0])
                return
            ln = layerNameByCheck()[0]
            expFile = 'file -force -options "v=0" -typ "mayaAscii" -pr -es "' + savePath + ln + '"'
            if mc.radioButtonGrp('fileType', q=True, select=True) == 2:
                expFile = 'file -force -options "v=0" -typ "mayaBinary" -pr -es "' + savePath + ln + '"'

            mel.eval(expFile)
            mc.confirmDialog(title='Confirm', message=u'congratulation,Exported!!!', defaultButton='Yes')
        else:
            mc.confirmDialog(title='Confirm', message=u'Please confirm This is a LR file  with \'lr\'!!!', defaultButton='Yes')
    else:
        if sn.find('lr') > -1:
            if mc.textFieldGrp('charNameText', q=True, text=True) == '':
                mc.text('fileNameResult', edit=True, label=u'Charactor Name Blank!!!!', bgc=[1, 0, 0])
                return
            lns = layerNameByCheck()[1]
            for n in lns:
                expFile = 'file -force -options "v=0" -typ "mayaAscii" -pr -es "' + savePath + n + '"'
                sn = mc.file(sceneName=True, q=True, shortName=True)
                if mc.radioButtonGrp('fileType', q=True, select=True) == 2:
                    expFile = 'file -force -options "v=0" -typ "mayaBinary" -pr -es "' + savePath + n + '"'
                mel.eval(expFile)
            mc.confirmDialog(title='Confirm', message=u'congratulation，Exported!!!', defaultButton='Yes')
        else:
            mc.confirmDialog(title='Confirm', message=u'Please confirm This is a LR file  with \'lr\'!!!', defaultButton='Yes')


def setCharNameTxt(name):
    mc.textFieldGrp('charNameText', e=True, text=name)
    changeLayrNameText()


def setVerionTxt(name):
    mc.textFieldGrp('VersionText', e=True, text=name)
    changeLayrNameText()


def do_seperateFile():
    arnd_lodState = u''
    if mc.pluginInfo('mtoa', l=True, q=True):
        mc.unloadPlugin(u'mtoa', f=True)
        arnd_lodState = u'\n原本加载的arnold 已经卸载了'
    if mc.window('mainWin', exists=True):
        mc.deleteUI('mainWin')
    mc.window('mainWin', title=u'DiveollyDive4 -- Exprot The Selected Objects For Auto Layer', width=460, height=180, sizeable=False)
    mc.columnLayout(rowSpacing=2, columnAttach=['both', 5], columnWidth=460)
    mc.text(label='         ')
    mc.text(label=u'            根据所选择的物体，选择文件内容（角色|场景），以及所需分层%s' % arnd_lodState)
    mc.separator(height=20, style='out')
    mc.text('fileNameResult', label=' ', fn='fixedWidthFont', align='center')
    mc.columnLayout(columnAttach=['left', 10])
    mc.radioButtonGrp('checkLayer', label=u'File', labelArray2=[u'One Layer One File', u'All Layer in One file'], numberOfRadioButtons=2, select=1, cc='changeLayrNameText()')
    mc.checkBoxGrp('l1', label=u'Layers:', labelArray2=['Color ( clr )', 'Occ ( occ )'], numberOfCheckBoxes=2, cc='changeLayrNameText()')
    mc.checkBoxGrp('l2', label=u'', labelArray2=['Shadow ( shw )', 'Normal ( nor )'], numberOfCheckBoxes=2, cc='changeLayrNameText()')
    mc.checkBoxGrp('l3', label=u'', labelArray2=['Zdepth ( zdp )', 'Fresnel ( fsl )'], numberOfCheckBoxes=2,  cc='changeLayrNameText()')
    mc.checkBoxGrp('l4', label='', labelArray2=['RGBA ( idp )', 'ContactOcc( cao )'], numberOfCheckBoxes=2,  cc='changeLayrNameText()')
    mc.checkBoxGrp('l5', label='', labelArray2=['Caustic ( caus )', 'Arnold Occ | Normal( arnold )'], numberOfCheckBoxes=2,  cc='changeLayrNameText()')

    mc.rowLayout(numberOfColumns=2)
    mc.textFieldGrp('charNameText', label=u'Charactor Name (RB select) :', editable=False, columnWidth2=[180, 60], cc='changeLayrNameText()')
    mc.popupMenu()
    mc.menuItem(label=u'Chars ', c='setCharNameTxt("Chars")')
    mc.menuItem(label=u'Sc ', c='setCharNameTxt("Sc")')
    mc.menuItem(label=u'ArnCh ', c='setCharNameTxt("ArnCh")')
    mc.menuItem(label=u'ArnSc ', c='setCharNameTxt("ArnSc")')
    mc.menuItem(label=u'TdSc ', c='setCharNameTxt("TdSc")')
    #===========================================================================
    # mainChars = []
    # for char in mainChars:
    #   mc.menuItem( label = char, c = 'setCharNameTxt("' + char + '")')
    #===========================================================================

    mc.textFieldGrp('VersionText', label='', editable=False, columnWidth2=[0, 50], cc='changeLayrNameText()')
    mc.popupMenu()
    for num in range(1, 11):
        versionName = "%02d" % num
        mc.menuItem(label=versionName, c='setVerionTxt("' + versionName + '")')
    mc.menuItem(label=u'TD', c='setVerionTxt("TD")')
    mc.setParent('..')
    mc.radioButtonGrp('fileType', label=u'File Type:', labelArray2=[u'.ma', u'.mb'], numberOfRadioButtons=2, select=2, cc='changeLayrNameText()')
    mc.setParent('..')

    mc.separator(height=10, style='out')
    mc.button(label='            Export The Selected Objects', backgroundColor=[0.44, 0.67, .9], c='expLayerFiles()')
    mc.text(label='         ')
    mc.showWindow('mainWin')
    changeLayrNameText()


def get_noRnd_DL():
    p_nr = re.compile(u'norender', re.I)

    DLM = [each_dlm for each_dlm in mc.ls(type=u'displayLayerManager') if not mc.referenceQuery(each_dlm, inr=True)]
    NR_DL = [each_DL for each_DL in mc.listConnections(DLM[0], type=u'displayLayer') if p_nr.search(each_DL)]
    if NR_DL != []:
        return NR_DL
    else:
        return None


if __name__ == "__main__":
    do_seperateFile()

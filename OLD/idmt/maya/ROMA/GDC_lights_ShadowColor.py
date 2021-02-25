# -*- coding: gbk -*-
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as OpenMaya
import xlrd


def GDC_lights_color_xls_Path():
##zzj       ▲xls文件的路径`
	#return r'\\file-cluster\GDC\Resource\Support\Maya\Import\iRender\RenderInfo\ROMA\GDC_lights_ShadowColor.xls'
	return r'\\file-cluster\GDC\Projects\ROMA\ROMA_Scratch\Lighting&Comp\RenderInfo\GDC_lights_ShadowColor.xls'

def xlrdGetAllDataFromCol():
##zzj       ▲读所有数值`
#   this function return all data from xls
    book = xlrd.open_workbook(GDC_lights_color_xls_Path(),
                        formatting_info = 1)
    sheet = book.sheet_by_index(0)
    numRows = sheet.nrows
    numCols = sheet.ncols

    readFromXlrd = []
    for i in range(numCols):
        readFromXlrd.append(sheet.col_values(i))
    return readFromXlrd



def xlrdGetPosFromKeyWord(keyword):
##zzj       ▲关键字所在位置`

#        *****************************
#        *    a    *   b    *    c   *
#        *****************************
#        *    d    *   e    *    f   *
#        *****************************
#        xlrdGetPosFromKeyWord('c'):   # Result: [2, 0] #

    allString=xlrdGetAllDataFromCol()
    columnRow = []
    rolNum = -1
    for i in range(len(allString)):
        try:
            rolNum = allString[i].index(keyword)
            columnRow=[i,rolNum]
            continue
        except:
            pass
    return columnRow



##zzj ==========================================

def ChangeColor():
##zzj   ▲读取GDC_lights_color.xls的信息
    allData=xlrdGetAllDataFromCol()
    fileNum=xlrdGetPosFromKeyWord(u'maya文件名')[0]
    lightNum=xlrdGetPosFromKeyWord(u'灯光名')[0]
    attributeNum=xlrdGetPosFromKeyWord(u'属性名')[0]
    valueNum=xlrdGetPosFromKeyWord(u'数值')[0]

##zzj       ▲maya文件名分离
#   quary the file name
    currentFileName = cmds.file(query = 1,sn = 1,shn = 1)
    fileSplit = currentFileName.split("_")

##zzj       ▲AllLights记录所有灯光Shape的名字
    AllLights = cmds.ls(type='light')

##zzj       ▲查找xls表中的.mb的那个完整名字
#   lighting_xxx_xxx_xxxx_xxxx_bloomDefault_hairs_RM.mb
    mbName=''
    for a in allData[fileNum]:
        if (a.find('.mb') != -1):
            mbName=a
            break
##zzj       ▲如果名字不对，弹出错误的提示

    #if len(fileSplit)<8 or fileSplit[0]!='lighting':
    if len(fileSplit)<6 or fileSplit[0]!='lighting':
        cmds.confirmDialog( title = u'请注意', message = u'文件名不符合规范', button = [u'确认'],dismissString = 'No' )

##zzj       ▲关键部分
    #if mbName.find(fileSplit[6])!=-1:
    if mbName.find(fileSplit[4])!=-1:
        id=[]
        for i in range(len(allData[lightNum])):

            for b in AllLights:
#                print allData[lightNum][i].split('_')
                if len(allData[lightNum][i].split('_'))==2:
                    if b.find(allData[lightNum][i].split('_')[1])!=-1:
                        id.append(i)
        id=list(set(id))

        if len(id)>1:
            button=[]
            buttonDic={}
            finalID=-1

            for a in id:
                button.append(allData[lightNum][a])
                buttonDic[allData[lightNum][a]]=a
            keyword=cmds.confirmDialog( title = u'角色信息有重复，请选择' , button = button  ,dismissString = 'No'  )
            if keyword!='No':
                finalID=buttonDic[keyword]
                values=allData[valueNum][finalID].split(',')
                for b in AllLights:
                    if len(values)==3:
                        #cmds.setAttr((b+'.'+allData[attributeNum][finalID]),float(values[0]),float(values[1]),float(values[2]),type='double3')
                        valuesRGB = mel.eval(r'hsv_to_rgb(<<%s, %s, %s>>)' % (float(values[0]) / 360.0, values[1], values[2]))
                        OpenMaya.MGlobal.executeCommand(r'setAttr "%s.%s" -type double3 %s %s %s' % (b, allData[attributeNum][finalID], valuesRGB[0], valuesRGB[1], valuesRGB[2]), True)
                    if len(values)==1 and values[0]!='':
                        #cmds.setAttr((b+'.'+allData[attributeNum][finalID]),float(values[0]))
			OpenMaya.MGlobal.executeCommand(r'setAttr "%s.%s" %s %s %s' % (b, allData[attributeNum][finalID], values[0]), True)

        if len(id)==1:
            values=allData[valueNum][id[0]].split(',')
            for b in AllLights:
                if len(values)==3:
		    #cmds.setAttr((b+'.'+allData[attributeNum][id[0]]),float(values[0]),float(values[1]),float(values[2]),type='double3')
		    valuesRGB = mel.eval(r'hsv_to_rgb(<<%s, %s, %s>>)' % (float(values[0]) / 360.0, values[1], values[2]))
		    OpenMaya.MGlobal.executeCommand(r'setAttr "%s.%s" -type double3 %s %s %s' % (b, allData[attributeNum][id[0]], valuesRGB[0], valuesRGB[1], valuesRGB[2]), True)
                if len(values)==1 and values[0]!='':
                    #cmds.setAttr((b+'.'+allData[attributeNum][id[0]]),float(values[0]))
		    OpenMaya.MGlobal.executeCommand(r'setAttr "%s.%s" %s %s %s' % (b, allData[attributeNum][id[0]], values[0]), True)

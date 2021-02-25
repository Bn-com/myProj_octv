# -*- coding: gbk -*-
import maya.cmds as cmds
import maya.mel as mel
import xlrd



def xlrdGetAllData():
##zzj       ▲读所有数值`
#   this function return all data from xls
    book = xlrd.open_workbook(r'\\file-cluster\GDC\Resource\Support\Maya\Import\iRender\RenderInfo\ROMA\lighting_parameter.xls',
                        formatting_info = 1)
    sheet = book.sheet_by_index(0)
    numRows = sheet.nrows
    numCols = sheet.ncols

#   all data in table：readFromXlrd
    readFromXlrd = []
    for i in range(numRows):
        readFromXlrd.append(sheet.row_values(i))
    return readFromXlrd



def xlrdGetBoundingBoxFromKeyWord(keyword):
##zzj       ▲获得关键字的范围（BoundingBox）`
#   this function return the length of the quryed keyword like this:['0', '1', '2', '14']
    book = xlrd.open_workbook(r'\\file-cluster\GDC\Resource\Support\Maya\Import\iRender\RenderInfo\ROMA\lighting_parameter.xls',
                        formatting_info = 1)
    sheet = book.sheet_by_index(0)

    All_Merged_Cells = sheet.merged_cells

#   所有合并的单元格里的value：All_Merged_Cells_value
#   [[u'mentalRay', '', '', '', ...], [u'softWare', '', ...], [u'GDC', '', '', ...], [u'lighting_xxx_xxx_xxxx_xxxx_env_GDCbeauty_MR.mb', '']]

    for a in All_Merged_Cells:
        rlo, rhi, clo, chi = a
        for i in xrange(rlo,rhi):
            tmp = sheet.row_values(i,start_colx = clo, end_colx = chi)
            for b in tmp:
                if b==(keyword):
                    return a
                    #   "a" maybe ['0', '1', '2', '14']


def xlrdGetColorFromCell(a,b):
##zzj       ▲单元格颜色`
    book = xlrd.open_workbook(r'\\file-cluster\GDC\Resource\Support\Maya\Import\iRender\RenderInfo\ROMA\lighting_parameter.xls',
                        formatting_info = 1)
    sheet = book.sheet_by_index(0)

    xfIndex = sheet.cell_xf_index(a,b)

    xf = book.xf_list[xfIndex]

    pIndex=xf.background.pattern_colour_index
#   cIndex=xf.background.background_colour_index

    finalColor=book.colour_map[pIndex]
    return finalColor



def xlrdConvert255To1(tupleType):
##zzj       ▲将0-255转换成0-1
    if  type(tupleType)==tuple:
        if  type(tupleType[0])==int and \
            type(tupleType[1])==int and \
            type(tupleType[2])==int :
            new=(float(tupleType[0])/255,float(tupleType[1])/255,float(tupleType[2])/255)
            return new




def xlrdGetColorFromSheet():
##zzj       ▲表格颜色`
    book = xlrd.open_workbook(r'\\file-cluster\GDC\Resource\Support\Maya\Import\iRender\RenderInfo\ROMA\lighting_parameter.xls',
                        formatting_info = 1)
    sheet = book.sheet_by_index(0)

    nr=sheet.nrows
    nc=sheet.ncols

    AllColors={}

    for a in range(nr):
        for b in range(nc):
            xfIndex = sheet.cell_xf_index(a,b)
            xf = book.xf_list[xfIndex]
            pIndex=xf.background.pattern_colour_index
            finalColor=book.colour_map[pIndex]
            AllColors[str(a)+','+str(b)]=finalColor
    return AllColors



def xlrdGetColumnNumFromKeyWord(keyword):
##zzj       ▲关键字所在列`
    allString=xlrdGetAllData()
    returnValue = []
    num = 10000
    for a in allString:
        try:
            num = a.index(keyword)
            continue
        except:
            pass
    return (num)



##zzj ==========================================


def get_suited_Data():
##zzj  ★①申明一个变量yy存储最终匹配的数据`
    yy = []
##zzj  ★②申明一个变量rowNum存储匹配的行号`
    rowNum=[]

##zzj       ▲表格中所有数据
    allString=xlrdGetAllData()

##zzj       ▲maya文件名分离
#   quary the file name
    currentFileName = cmds.file(query = 1,sn = 1,shn = 1)
    fileSplit = currentFileName.split("_")

##zzj       ▲读表格中'maya文件名'的那一列，放入变量mayaFileNameInXls中
    mayaFNColNum = xlrdGetColumnNumFromKeyWord(u'maya文件名')
    mayaFileNameInXls = []
    for b in allString:
        mayaFileNameInXls.append(b[mayaFNColNum])


##zzj       ▲返回所有找到的数据到suitedName里
    suitedName = []
    for a in mayaFileNameInXls:
        if type(a) != unicode:
            continue
        if a.find(fileSplit[6]) != -1:
            suitedName.append(a)

##zzj       ▲判断（当前maya文件名）对应（表格中maya文件名）是否唯一
    if len(suitedName) == 0:
        cmds.confirmDialog( title = u'请注意', message = u'文件名不符合规范', button = [u'确认'],dismissString = 'No' )

    if len(suitedName)>1:
        for a in suitedName:
            tmpName = fileSplit[5]
            if (tmpName != 'chr')and(tmpName != 'env'):
                tmpName = 'bloomDefault'
            if a.find(tmpName) != -1:
                suitedName = []
                suitedName.append(a)

    if len(suitedName) == 1:
        num = 10000
        for a in allString:
            try:
                num = a.index(u'maya文件名')
                continue
            except:
                pass
        ctNameIndex = mayaFileNameInXls.index(suitedName[0])
##zzj  ★①向变量yy中追加数据`
        yy.append(allString[ctNameIndex])
##zzj  ★②向变量rowNum中追加行号`
        rowNum.append(ctNameIndex)

##zzj       ▲判断（表格中maya文件名）对应的（渲染层名）是否有多行数据
        for i in range(1,10):
            if allString[ctNameIndex+i][num] == '' and allString[ctNameIndex+i][num+1] != '':
##zzj  ★①向变量yy中追加数据`
                yy.append(allString[ctNameIndex+i])
##zzj  ★②向变量rowNum中追加行号`
                rowNum.append(ctNameIndex+i)
            else:
                break

##zzj       ▲对表格中初始为bloomDefault的数据进行替换
        for i in range(len(yy)):
            yy[i] = list(yy[i])         #   set yy[i] to list
            for j in range(len(yy[i])):
                if type(yy[i][j]) == unicode:
                    b = yy[i][j].replace('bloomDefault',fileSplit[5])
                    yy[i][j] = b

#   "yy" maybe [['', u'lighting_xxx_xxx_xxxx_xxxx_bloomRoyalBalldress_GDCexlights_MR.mb', u'bloomRoyalBalldress_GDCextra', u'\u51e0\u4f55\u4f53\u3001\u706f\u5149', u'sq_xxx_sc_xxx_bloomRoyalBalldress_GDCextra.####.iff', u'2048*872', 0.0, 1.0, 7.0, 1.0, 1.0, 0.0, 2.0, 2.0, 2.0, 2.0, 1.0, 2.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.0, 2.0, 1.0, 0.0, 2.0, 1.0, 1.0, 1.0, 1.0, 10.0, 0.0, 1.0, 2.0, 8.0, 1.0, 4.0, 0.4, 0.3, 0.6, 10.0, 10.0, 10.0]]




##zzj       ▲对lights部分的数据进行追加处理
##zzj           ▲获得lights部分的宽度`
    bb=xlrdGetBoundingBoxFromKeyWord(u'lights')
#    print bb
    color=xlrdGetColorFromSheet()


    for d in range(len(yy)):
#        print bb[2],bb[3]:  55-98
        for i in range(bb[2],bb[3]):
#            print i
#            i: 55-97
##zzj           ▲如果对应的数值为空，则查看颜色值`
#            print yy[d][i]


#            print yy[d][97]

            if yy[d][i]=="":
                t=str(rowNum[d])+','+str(i)
#                print color[t]
#                print t:    5,56   5,96   6,56   6,96
#                print type(color[t])

#                print 'zzz'
                if type(color[t])==tuple:
#                    print 'adsfaeasdsdewfadsf'
#                    print color[t]
                    yy[d][i]=str(xlrdConvert255To1(color[t]))[1:-1]
#                    print yy[d][i]
#                    print type(color[t])
#    print yy

    return yy








##zzj ==========================================


def createLayer():
    allString=xlrdGetAllData()
    currentFileName = cmds.file(query = 1,sn = 1,shn = 1)

#    if currentFileName.find('GDC') == -1:
#        mel.eval("py_autoSetForRendering()")

    if currentFileName.find('GDC') != -1:
        fileSplit = currentFileName.split("_")

        suitedName = []
        num = xlrdGetColumnNumFromKeyWord(u'maya文件名')
        mayaFileNameInXls = []
        for a in allString:
            mayaFileNameInXls.append(a[num])

        for a in mayaFileNameInXls:
            if type(a) != unicode:
                continue
            if a.find(fileSplit[6]) != -1:
#                print a
                suitedName.append(a)
        if len(suitedName) == 0:
            cmds.confirmDialog( title = u'请注意', message = u'文件名不符合规范', button = [u'确认'],dismissString = 'No' )
        else:
##zzj   ▲删除所有渲染层`
            cmds.editRenderLayerGlobals(currentRenderLayer = "defaultRenderLayer")
            mel.eval("layerEditorLayerButtonSelect 0 \"defaultRenderLayer\"")

            allLayers = cmds.ls(type = "renderLayer")
            defaultRL = cmds.ls('*:defaultRenderLayer','defaultRenderLayer',type = "renderLayer")
            for a in defaultRL:
                allLayers.remove(a)
            if len(allLayers) != 0:
                try :
                    cmds.delete(allLayers)
                except:
                    pass

##zzj   ▲分层`
            yy = get_suited_Data()
            for a in yy:
##zzj       ▲创建渲染层`
                numX = xlrdGetColumnNumFromKeyWord(u'渲染层名')
                mel.eval("createRenderLayer -name "+a[numX]+"")
    #   change currentRenderLayer
                cmds.editRenderLayerGlobals(currentRenderLayer  = a[2])

##zzj       ▲层内物体`
                numC = xlrdGetColumnNumFromKeyWord(u'层内物体')
                allLayers = cmds.ls(type = "renderLayer")
                allLayers.remove("defaultRenderLayer")

                selected = None

                if a[numC] == u'当前选择物体':
                    selected = cmds.ls(sl = 1)

                if a[numC] == u'选择的几何体':
                    selected = cmds.ls(sl = 1,dag = 1,geometry = 1)

                if a[numC] == u'选择的几何体、灯光':
                    selected = cmds.ls(sl = 1,dag = 1,geometry = 1,lights = 1)

                if a[numC] == u'几何体、灯光':
                    selected = cmds.ls(lights = 1,geometry = 1)

                cmds.editRenderLayerMembers( a[numX],selected)

##zzj       ▲输出素材名`
    #   sq_xxx_sc_xxx_bloomRoyalBalldress_GDClgt.####.iff

    #   set imageFilePrefix
                tmp = a[numX].split('_')
                imagePath = "sq_"+fileSplit[1]+"/sc_"+fileSplit[2]+"/"+tmp[0]+"/"+tmp[1]+"/"    +    "sq_"+fileSplit[1]+"_sc_"+fileSplit[2]+"_"+"<Layer>"
                cmds.editRenderLayerAdjustment("defaultRenderGlobals.imageFilePrefix")
                cmds.setAttr("defaultRenderGlobals.imageFilePrefix",imagePath,type = "string")

##zzj       ▲输出alpha`
                numA = xlrdGetColumnNumFromKeyWord(u'alpha')
                cams = cmds.listCameras(perspective = 1)
                orAlpha = a[numA]
                for cam in cams:
                    if cmds.getAttr(cam+".renderable"):
                        cmds.editRenderLayerAdjustment(cam+".mask")
                        cmds.setAttr((cam + ".mask"),orAlpha)

##zzj       ▲分辨率
                numA = xlrdGetColumnNumFromKeyWord(u'分辨率')
                resolution = a[numA]
                tmp = resolution.split('*')
                cmds.editRenderLayerAdjustment("defaultResolution.width")
                cmds.setAttr("defaultResolution.width",int(tmp[0]))
                cmds.editRenderLayerAdjustment("defaultResolution.height")
                cmds.setAttr("defaultResolution.height",int(tmp[1]))


##zzj       ▲mentalRay
                numMR = xlrdGetColumnNumFromKeyWord(u'mentalRay')
                length = xlrdGetBoundingBoxFromKeyWord(u'mentalRay')
                #   length:(0,1,7,40)
                if fileSplit[7][0:2] == 'MR':

                    cmds.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
                    cmds.setAttr('defaultRenderGlobals.currentRenderer','mentalRay',type = 'string')

                    cmds.editRenderLayerAdjustment("defaultRenderGlobals.imageFormat")
                    cmds.editRenderLayerAdjustment("miDefaultFramebuffer.premultiply")
                    cmds.editRenderLayerAdjustment("miDefaultFramebuffer.datatype")


                    cmds.setAttr('defaultRenderGlobals.imageFormat',        a[numMR])
                    cmds.setAttr('miDefaultFramebuffer.premultiply',        a[numMR+1])
                    cmds.setAttr('miDefaultFramebuffer.datatype',           a[numMR+2])

                    for i in range(length[2]+3,length[3]):
                        attri = 'miDefaultOptions.'+allString[length[1]][i]
                        cmds.editRenderLayerAdjustment(attri)
                        cmds.setAttr(attri,a[i])

##zzj       ▲softWare
                numSW = xlrdGetColumnNumFromKeyWord(u'softWare')
                length = xlrdGetBoundingBoxFromKeyWord(u'softWare')

                if fileSplit[7][0:2] == 'MS':
#                    print 'hahahaha'
                    cmds.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
                    cmds.setAttr('defaultRenderGlobals.currentRenderer','mayaSoftware',type = 'string')

                    cmds.editRenderLayerAdjustment("defaultRenderGlobals.imageFormat")
                    cmds.editRenderLayerAdjustment("defaultRenderGlobals.composite")

                    cmds.setAttr('defaultRenderGlobals.imageFormat',            a[numSW])
#                    print a[numSW]
                    cmds.setAttr('defaultRenderGlobals.composite',      a[numSW+1])
#                    print a[numSW+1]

                    for i in range(length[2]+3,length[3]):
                        attri = 'defaultRenderQuality.'+allString[length[1]][i]
#                        print attri
                        cmds.editRenderLayerAdjustment(attri)
                        cmds.setAttr(attri,a[i])

##zzj       ▲mayaMan





##zzj       ▲灯光
                numMR = xlrdGetColumnNumFromKeyWord(u'lights')
#                print numMR
                length = xlrdGetBoundingBoxFromKeyWord(u'lights')
#                print length
                #   length:(0, 1, 55, 98)
##zzj       ▲分类
                lightTypes=[]
                for i in range(length[2],length[3]):
#                    print i
                    if allString[length[1]][i]!='':
                        lightTypes.append(allString[length[1]][i])
#                print lightTypes
                #   lightTypes:[u'chr_keyLight', u'chr_fillLight', u'chr_bounceLight', u'chr_ambientLight', u'rim', u'aks_Light', u'env_keyLight', u'env_fillLight', u'env_bounceLight', u'env_ambientLight']

##zzj           ▲分属性

                allLightsInMaya=cmds.ls(type='light')
                for h in allLightsInMaya:
#                    print h
                    for t in lightTypes:
                        if h.find(t)!=-1:

                            attBB=xlrdGetBoundingBoxFromKeyWord(t)
#                            print attBB
#                           print attBB:(1, 2, 55, 61)
                            lightAtt=[]
#                           print '=============='
                            for g in range(attBB[2],attBB[3]):
                                lightAttName=allString[attBB[1]][g]
#                                print lightAttName
#                                print "======="


#                                print type(a[g])
#                                continue
                                if a[g]==None:
                                    continue
                                else:
##zzj               ▲建层override
#                                    print (h+'.'+lightAttName)
                                    try:
                                        cmds.editRenderLayerAdjustment(h+'.'+lightAttName)
                                    except:
                                        pass

                                    tmp=str(a[g])
#                                    print type(tmp)

                                    tmpSp=tmp.split(',')
#                                    print tmpSp
                                    if tmpSp==['']:
                                        continue
                                    else:
#                                        print tmpSp
##zzj               ▲设置参数
                                        try:
                                            if len(tmpSp)==3:
#                                                print tmpSp[0],tmpSp[1],tmpSp[2]
                                                cmds.setAttr((h+'.'+lightAttName),float(tmpSp[0]),float(tmpSp[1]),float(tmpSp[2]),type='double3')
                                            if len(tmpSp)==1:
#                                                print type(tmpSp[0])
                                                cmds.setAttr((h+'.'+lightAttName),float(tmpSp[0]))
                                        except:
                                            pass


##zzj       ▲关闭defaultRenderLayer的可渲染属性
                array=cmds.listConnections("renderLayerManager.renderLayerId")
                for item in array:
                    if item.find("defaultRenderLayer") !=-1:
                        cmds.setAttr((item + ".renderable") ,0)

##zzj   ▲fix
        fix()



def fix():
##zzj       ▲单独处理GDCrfl层
    currentFileName=cmds.file(query=1,sn=1,shn=1)
    fileSplit=currentFileName.split("_")
    if fileSplit[6].find("GDCrfl")!=-1:
        selects=cmds.ls(sl=1,dag=1,geometry=1)
        if selects==None or selects==[]:
            cmds.confirmDialog(m=u"请选择反射物体",button=u"确认")
        else:
            allLayers=cmds.ls(type="renderLayer")
            allLayers.remove("defaultRenderLayer")

            objShape=cmds.ls(geometry=1)
            allLights=cmds.ls(lights=1)

            selects=cmds.ls(sl=1,dag=1,geometry=1)
            for sel in selects:
                objShape.remove(sel)
            ref=cmds.shadingNode('useBackground',asShader=1,name="reflection")
            cmds.setAttr ((ref + ".reflectivity") ,1)
            cmds.setAttr ((ref + ".reflectionLimit"), 2)
            cmds.setAttr ((ref + ".shadowMask") ,0)

            refSG = cmds.sets(renderable=1,noSurfaceShader=1,empty=1,name=(ref+"SG"))
            cmds.connectAttr((ref +".outColor"), (refSG +".surfaceShader"))

    #   Setup objects which is in reflection by turn off primary visibility
            for sel in objShape:
                cmds.setAttr((sel + ".primaryVisibility"),0)
            for sel in selects:
                cmds.setAttr((sel + ".primaryVisibility"),1)
    #   Assign reflection shader to objects
            cmds.select(selects)
            cmds.hyperShade(assign=ref )


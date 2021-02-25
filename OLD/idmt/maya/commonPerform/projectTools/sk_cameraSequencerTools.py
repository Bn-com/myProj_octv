# -*- coding: utf-8 -*-
#  Author : 沈康
#  Data   : 2015_04_01

import maya.cmds as mc
import maya.mel as mel

import os
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
from idmt.maya.commonCore.core_baseCommon import sk_infoCore
reload(sk_infoCore)
from idmt.maya.commonCore.core_mayaCommon import sk_camMatrixScene
reload(sk_camMatrixScene)

# cameraSequencer 处理工具集
class sk_cameraSequencerTools(object):
    def __init__(self):
        self.modifySeq = 1
        mel.eval('optionVar -intValue seqDoubleClickMayaFrameRange true')
    # UI
    def sk_cameraSequencerToolsUI(self,ds = 'mi_010'):

        # 窗口
        if mc.window ("sk_camSeqTools", ex=1):
            mc.deleteUI("sk_camSeqTools", window=True)
        mc.window("sk_camSeqTools", title="CamSeq Tools", widthHeight=(420, 380), menuBar=0,sizeable = 1)
        columnLayout = mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',0])
        '''
        # 输入载入信息
        mc.frameLayout(l = u'[ 请输入载入信息 | Please Imput Sequence Info ]' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        # 输入
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',0])
        mc.text(label = '' , height = 3)
        mc.rowColumnLayout(numberOfColumns = 9)
        mc.text(label = '' , width = 10)
        mc.textField('sk_camSeqImput',text = ds,width = 150)
        mc.text(label = '' , width = 5)
        mc.button(l=u'查询|Search',width = 80,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqGetXmlPath()')
        mc.text(label = '' , width = 5)
        mc.button(l=u'fix',width = 40,bgc = [0.3,0.5,0.3],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqFileFix()')
        mc.text(label = '' , width = 5)
        mc.button(l=u'导入|Import',width = 85,bgc = [0.3,0.6,0.8],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqImportPerform()')
        mc.text(label = '' , width = 10)
        mc.text(label = '' , height = 3)
        mc.setParent()
        mc.setParent(columnLayout)

        # 调整透明度
        mc.frameLayout(l = u'[ 调整背景图透明度 | Adjust ImagePlane Alpha Gain ]' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        # 输入
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',0])
        mc.text(label = '' , height = 3)
        mc.rowColumnLayout(numberOfColumns = 5)
        mc.text(label = '' , width = 10)
        mc.floatSlider('sk_camSeqImgSliderAlpha',value = 0.25,minValue = -1 , maxValue = 1,width = 100,changeCommand = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqImgPlaneAlphaPerform(2)')
        mc.text(label = '' , width = 5)
        #mc.button(l=u'选取更改|Apply to Selected',width = 150,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqImgPlaneAlphaPerform(1)')
        #mc.text(label = '' , width = 5)
        #mc.button(l=u'全部更改|Apply to all',width = 150,bgc = [0.3,0.6,0.8],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqImgPlaneAlphaPerform(0)')
        mc.radioButtonGrp('sk_camSeqImgSelMode',numberOfRadioButtons  = 2,labelArray2 = [u'选改|Apply to Selected',u'全改|Apply to all'] ,width = 240,columnWidth2 = [140,100],select = 2)
        mc.text(label = '' , width = 10)
        mc.text(label = '' , height = 3)
        mc.setParent()
        mc.setParent(columnLayout)

        # cam 分割线 完整版
        camROT = mc.frameLayout(l = u'[ 三分构图线 | Rule Of Thirds ]' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        # 输入
        mc.columnLayout(adjustableColumn = 0 , columnOffset = ['both',0])
        mc.text(label = '' , height = 3)
        mc.rowColumnLayout(numberOfColumns = 9)
        mc.text(label = '' , width = 10)
        mc.floatField('sk_camSeqImgROTLenthScale',value = 1.0,width = 60)
        mc.text(label = '' , width = 5)
        mc.button(l = u'长度缩放|Lenth Scale',width = 120,bgc =  [0.1,0.42,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqROTPerform(1,dsInfo = "%s")'%ds)
        mc.text(label = '' , width = 5)
        mc.floatField('sk_camSeqImgROTThickScale',value = 1.0,width = 60)
        mc.text(label = '' , width = 5)
        mc.button(l = u'粗细缩放|Thick Scale',width = 120,bgc =  [0.1,0.42,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqROTPerform(2,dsInfo = "%s")'%ds)
        mc.text(label = '' , width = 10)
        mc.setParent(camROT)

        #mc.columnLayout()
        mc.columnLayout(adjustableColumn = 0 , columnOffset = ['both',10])
        mc.rowColumnLayout(numberOfColumns = 7)
        mc.button(l = u'ImgPlane ON / OFF',width = 90,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqImageOnOff(dsInfo = "%s")'%ds)
        mc.text(label = '' , width = 5)
        mc.button(l = u'显示开关|ON / OFF',width = 90,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqROTPerform(3,dsInfo = "%s")'%ds)
        mc.text(label = '' , width = 5)
        mc.button(l = u'重建 | Rebuild',width = 90,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqROTPerform(4,dsInfo = "%s")'%ds)
        mc.text(label = '' , width = 5)
        mc.button(l = u'选建 | Sel Rebuild',width = 90,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqROTPerform(4,dsInfo = "%s",selMode = 1)'%ds)
        mc.setParent(camROT)
        
        mc.columnLayout(adjustableColumn = 0 , columnOffset = ['both',10])
        mc.rowColumnLayout(numberOfColumns = 7)
        mc.button(l = u'Mov Sel ON',width = 90,bgc = [0.1,0.1,0.5],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqMovOnOff(selMode=1,onMode=1)')
        mc.text(label = '' , width = 5)
        mc.button(l = u'Mov All ON',width = 90,bgc = [0.1,0.1,0.5],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqMovOnOff(selMode=0,onMode=1)')
        mc.text(label = '' , width = 5)
        mc.button(l = u'Mov Sel OFF',width = 90,bgc = [0.1,0.5,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqMovOnOff(selMode=1,onMode=0)')
        mc.text(label = '' , width = 5)
        mc.button(l = u'Mov All OFF',width = 90,bgc = [0.1,0.5,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqMovOnOff(selMode=0,onMode=0)')
        mc.text(label = '' , height = 3)
        mc.setParent(camROT)

        mc.setParent(columnLayout)
        '''

        # 创建
        mc.frameLayout(l = u'[ 三分线创建| GoldLine Create ]' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        # 输入
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',10])
        mc.text(label = '' , height = 3)
        mc.rowColumnLayout(numberOfColumns = 7)
        mc.button(l = u'重建 | Rebuild',width = 180,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqROTPerform(4,dsInfo = "%s")'%ds)
        mc.text(label = '' , width = 5)
        mc.button(l = u'选建 | Sel Rebuild',width = 180,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqROTPerform(4,dsInfo = "%s",selMode = 1)'%ds)
        mc.text(label = '' , width = 5)
        mc.setParent()
        mc.setParent(columnLayout)

        # 切换三分线
        mc.frameLayout(l = u'[ 三分线切换开关| GoldLine ON/OFF ]' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        # 输入
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',10])
        mc.text(label = '' , height = 3)
        mc.rowColumnLayout(numberOfColumns = 7)
        mc.button(l = u'三分线切换开 | GoldLine Switch On',width = 180,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().applyGoldenLineShowSwitch(mode = 1)')
        mc.text(label = '' , width = 5)
        mc.button(l = u'三分线切换关 | GoldLine Switch Off',width = 180,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().applyGoldenLineShowSwitch(mode = 0)')
        mc.text(label = '' , width = 5)
        mc.setParent()
        mc.setParent(columnLayout)

        # 调整黄金线透明度
        mc.frameLayout(l = u'[ 调整黄金线透明度 | Adjust GoldLine Alpha Gain ]' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        # 输入
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',0])
        mc.text(label = '' , height = 3)
        mc.rowColumnLayout(numberOfColumns = 3)
        mc.text(label = '' , width = 10)
        mc.floatSlider('sk_camSeqGoldLineSliderAlpha',value = 0.872,minValue = 0 , maxValue = 1,width = 365,changeCommand = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqGoldLineAlphaPerform()')
        mc.text(label = '' , width = 10)
        mc.text(label = '' , height = 3)
        mc.setParent()
        mc.setParent(columnLayout)

        # 三分线调整粗细
        mc.frameLayout(l = u'[ 三分线调整粗细| GoldLine Modify ]' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        # 输入
        mc.columnLayout(adjustableColumn = 0 , columnOffset = ['both',0])
        mc.text(label = '' , height = 3)
        mc.rowColumnLayout(numberOfColumns = 9)
        mc.text(label = '' , width = 10)
        mc.floatField('sk_camSeqImgROTLenthScale',value = 5.0,width = 60)
        mc.text(label = '' , width = 5)
        mc.button(l = u'长度缩放|Lenth Scale',width = 115,bgc =  [0.1,0.42,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqROTPerform(1,dsInfo = "%s")'%ds)
        mc.text(label = '' , width = 5)
        mc.floatField('sk_camSeqImgROTThickScale',value = 5.0,width = 60)
        mc.text(label = '' , width = 5)
        mc.button(l = u'粗细缩放|Thick Scale',width = 115,bgc =  [0.1,0.42,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqROTPerform(2,dsInfo = "%s")'%ds)
        mc.text(label = '' , width = 10)
        mc.setParent(columnLayout)

        # camera批量改属性
        camApply = mc.frameLayout(l = u'[ cam批量改属性 | Apply to Cams ]' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        # 输入
        mc.columnLayout(adjustableColumn = 0 , columnOffset = ['both',0])
        mc.rowColumnLayout(numberOfColumns = 7)
        mc.text(label = '' , width = 10)
        mc.checkBox('sk_camSeqApplyFilmGate',label = 'Display Safe Title',value = 0)
        mc.text(label = '' , width = 20)
        mc.checkBox('sk_camSeqApplyResGate',label = 'Display Resolution',value = 0)
        mc.text(label = '' , width = 20)
        mc.checkBox('sk_camSeqApplyGateMask',label = 'Display Gate Mask',value = 0)
        mc.text(label = '' , width = 10)
        mc.setParent(camApply)
        
        mc.setParent(columnLayout)
        
        camApply = mc.frameLayout(l = u'[ cam批量改属性 | Apply to Cams ]' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        
        mc.columnLayout(adjustableColumn = 0 , columnOffset = ['both',10])
        mc.rowColumnLayout(numberOfColumns = 7)
        mc.button(l = u'应用所选Cam | Apply to Selected',width = 180,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().applyCameraAttrs(mode = 1)')
        mc.text(label = '' , width = 5)
        mc.button(l = u'应用所有Cam | Apply to All ',width = 180,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().applyCameraAttrs(mode = 2)')
        mc.text(label = '' , width = 5)
        mc.setParent(camApply)
        
        mc.setParent(columnLayout)
        '''
        # 显示服务器端xml路径
        mc.frameLayout(l = u'[ 服务器端xml路径显示 | Server sequence xml path ]' ,collapse = 1,collapsable = 1,borderStyle = 'etchedIn')
        
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',0])
        mc.text(label = '' , height = 3)
        mc.rowColumnLayout(numberOfColumns = 5)
        mc.text(label = '' , width = 10)
        mc.textField('sk_camSeqXmlPath',text = '',width = 255)
        mc.text(label = '' , width = 5)
        mc.button(l = u'复制|Copy',width = 100)
        mc.text(label = '' , width = 10)
        mc.text(label = '' , height = 3)
        mc.setParent()
        mc.setParent(columnLayout)

        # 整体时间轴偏移
        fOff = mc.frameLayout(l = u'[ 整体帧偏移 | Whole Frames Offset ]' ,collapse = 1,collapsable = 1,borderStyle = 'etchedIn')
        mc.columnLayout(adjustableColumn = 0 , columnOffset = ['both',0])
        mc.text(label = '' , height = 3)
        mc.rowColumnLayout(numberOfColumns = 5)
        mc.text(label = '' , width = 10)
        mc.floatField('sk_camSeqShotOffset',value = 10.0,width = 70)
        mc.text(label = '' , width = 5)
        mc.button(l = u'选取起始shot节点后开始偏移 | Select Start Shot Then Offset',width = 300,bgc =  [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqFrameExchange()')
        mc.text(label = '' , width = 10)
        mc.setParent()
        mc.setParent(columnLayout)
        
        # assetImport
        mc.frameLayout(l = u'[ 镜头Assets参考 | Server Assets Reference ]' ,collapse = 1,collapsable = 1,borderStyle = 'etchedIn')
        
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',10])
        mc.text(label = '' , height = 3)
        mc.button(l = u'选取shot的Asset参考导入 | Import Assets From The Shot Seleted',width = 320,height = 30 ,bgc = [0.1,0.6,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_assetsReferencePerform(1)')
        mc.text(label = '' , height = 3)
        mc.button(l = u'所有shot的Asset参考导入 | Import Assets From All Shot Of The File',width = 320,height = 30,bgc = [0.1,0.6,0.8],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_assetsReferencePerform(0)')
        mc.text(label = '' , height = 3)
        mc.setParent()
        mc.setParent(columnLayout)
        
        # Split Files 手动版
        splitLayoutByHand = mc.frameLayout(l = u'[ 手动分割 | Break Out By Hands ]' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')

        mc.columnLayout(adjustableColumn = 0 , columnOffset = ['both',10])
        
        mc.text(label = u'', height = 6)
        mc.text(label = u'【注意】分割前备份好源文件；分割后勿覆盖；分割过程中会断掉一些连接。',bgc = [0.1,0.6,0.1], height = 26)
        mc.text(label = u'', height = 6)
        
        mc.rowColumnLayout(numberOfColumns = 7)
        mc.textField('sk_camSeqBreakOutGetShot',width = 70)
        mc.text(label = '' , width = 5)
        mc.button(l = u'Fix Shot',width = 55,bgc = [0.1,0.3,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqFixShotName()')
        mc.text(label = '' , width = 5)
        mc.button(l = u'Get Shot',width = 55,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqGetSelShot()')
        mc.text(label = '' , width = 5)
        mc.button(l = u'选取参考导出 | Select Assets Export',width = 180,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqBreakOutByHands()')
        mc.setParent(splitLayoutByHand)
        mc.setParent(columnLayout)
        
        # Split Files
        splitLayout = mc.frameLayout(l = u'[ 分割成单个镜头文件 | Break Out Single Layout Files ]' ,collapse = 1,collapsable = 1,borderStyle = 'etchedIn')
        
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',10])
        mc.text(label = '' , height = 3)
        mc.button(l = u'分割选取的shot | Break Out The Shot Selected',width = 320,height = 30 ,bgc = [0.1,0.6,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqSplitPerform(1)')
        mc.text(label = '' , height = 3)
        mc.button(l = u'分割所有的shot | Break Out All Shot Of The File ',width = 320,height = 30,bgc = [0.1,0.6,0.8],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().sk_camSeqSplitPerform(0)')
        mc.text(label = '' , height = 3)
        mc.setParent(splitLayout)
        mc.setParent(columnLayout)

        # fix Split Files
        fixLayout = mc.frameLayout(l = u'[ 处理分割后的文件 | Fix Files After Breaking Out ]' ,collapse = 1,collapsable = 1,borderStyle = 'etchedIn')
        
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',10])
        mc.rowColumnLayout(numberOfColumns = 4)
        mc.button(l = u'修正时间轴 | Fix Time and Animation',width = 190,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().fixTimeLineAnimation()')
        mc.text(label = '' , width = 5)
        mc.button(l = u'删除多余动画 | Delete  Keyframes',width = 190,bgc = [0.1,0.1,0.1],c = 'reload(sk_cameraSequencerTools)\nsk_cameraSequencerTools.sk_cameraSequencerTools().cleanMoreTimeRange()')
        mc.text(label = '' , height = 10)
        mc.setParent(fixLayout)
        mc.setParent(columnLayout)
        '''
        mc.showWindow("sk_camSeqTools")

    # buttonImport
    def sk_camSeqImportPerform(self):
        seqInfos = mc.textField('sk_camSeqImput',q = 1 , text = 1)
        shotInfos = seqInfos.split('_')
        # 修正文件
        self.sk_shotDefaultConfig(shotInfos[0])
        # 更新mov
        self.sk_camMovCopy(seqInfos)
        # 获取xml路径
        xmlServerPath = self.sk_camSeqGetXmlPath()
        # 导入
        shotNodes = mc.ls(type = 'shot')
        if shotNodes:
            # 报错
            return 
        import maya.app.edl.importExport as EDL
        EDL.doImport(xmlServerPath,0,1)
        # 修正imageplane数据
        self.sk_camImgSetting(xmlServerPath)
        # 加载音频
        self.sk_camImgImportAudio(xmlServerPath)
        # 校正cam
        self.sk_camSetting(shotInfos[0])
        # 校正时间轴
        self.sk_timeLineConfig()
        # 自动加载seq到内存
        # 开启窗口
        self.sk_camSeqConfig(shotInfos[0])
        # imgPlanes
        imageShapes = mc.ls(type = 'imagePlane')
        for imgShape in imageShapes:
            mc.setAttr((imgShape+'.fit'),1)
            mel.eval('AEinvokeFitRezGate %s %s'%(( imgShape + '.sizeX'),( imgShape + '.sizeY')))
        
    # button fix
    def sk_camSeqFileFix(self):
        shotNodes = mc.ls(type = 'shot')
        if not shotNodes:
            return
        shotInfos = shotNodes[0].split('_')
        xmlServerPath = self.sk_camSeqGetXmlPath(shotInfos)
        # 修正imageplane数据
        self.sk_camImgSetting(xmlServerPath)
        # 加载音频
        self.sk_camImgImportAudio(xmlServerPath)
        # 校正cam
        self.sk_camSetting(shotInfos[0],goldenLine = 0)
        # 校正时间轴
        self.sk_timeLineConfig()
        # 开启窗口
        self.sk_camSeqConfig(shotInfos[0])
        
    # getXmlPath
    def sk_camSeqGetXmlPath(self,shotInfos = []):
        if not shotInfos:
            seqInfos = mc.textField('sk_camSeqImput',q = 1 , text = 1)
            shotInfos = seqInfos.split('_')
        fileDictInfo = sk_infoConfig.sk_infoConfig().checkGetShotDict(shotInfos=shotInfos)
        shotID = sk_infoConfig.sk_infoConfig().checkGetShotIDInfo(shotInfos)
        sgState = sk_infoConfig.sk_infoConfig().checkSGState(shotInfos[0])
        xmlName = shotID
        if shotID[-1] in ['_']:
            xmlName = shotID[:-1]
        needPath = fileDictInfo['sequence']
        if fileDictInfo['reel']:
            needPath = '%s/%s'%(fileDictInfo['reel'],fileDictInfo['sequence'])
        projectPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath(shotInfos = shotInfos,productionMode = 2,mayaMode = 0)
        layoutFolder = 'Previsualization'
        targetPath= '%sPreProduction/%s/bgprevis/%s/%s_bv/%s.xml'%(projectPath,layoutFolder,needPath,xmlName,xmlName)
        if sgState:
            targetPath = 'Z:/Shotgun/projects/%s/animatic/seq%s/%s_%s_sb.xml'%(fileDictInfo['showShortname'],fileDictInfo['sequence'],fileDictInfo['showShortname'],fileDictInfo['sequence'])
        winPath = targetPath.replace('/','\\')
        mc.textField('sk_camSeqXmlPath',text = winPath,e = 1)
        return targetPath

    # button switch goldenLine :１开启 0 关闭
    def applyGoldenLineShowSwitch(self,mode = 1):
        #import seq_cam_keeper
        #reload(seq_cam_keeper)
        goldGrp = 'goldLine_Grp'
        if mode:
            if mc.ls(goldGrp):
                mc.setAttr('%s.v'%goldGrp,1)
            # 打开
            #seq_cam_keeper.open_seq_cam_keeper()
        else:
            # 关闭
            #seq_cam_keeper.close_seq_cam_keeper()
            if mc.ls(goldGrp):
                mc.setAttr('%s.v'%goldGrp,0)

    # button alpha gain
    def sk_camSeqImgPlaneAlphaPerform(self,selMode = 0):
        imgPlanes = []
        if selMode in [2]:
            selValue = mc.radioButtonGrp('sk_camSeqImgSelMode',select = 1,q = 1)
            if selValue == 1:
                shotNodes = mc.ls(sl = 1,type = 'shot')
            if selValue == 2:
                shotNodes = mc.ls(type = 'shot')
            alphaValue = mc.floatSlider('sk_camSeqImgSliderAlpha',value=1,q=1)
        for shotNode in shotNodes:
            imgPlane = mc.listConnections(shotNode,s= 1,d= 0, type = 'imagePlane')
            if not imgPlane:
                continue
            imgPlanes = imgPlanes + imgPlane
        for imgPlane in imgPlanes:
            mc.setAttr((imgPlane + '.alphaGain'),alphaValue)

    # button goldline alpha
    def sk_camSeqGoldLineAlphaPerform(self):
        goldLineShader = 'camGoldenLineShader'
        if not mc.ls(goldLineShader):
            return
        alphaValue = mc.floatSlider('sk_camSeqGoldLineSliderAlpha',value=1,q=1)
        alphaValue = 1-alphaValue
        mc.setAttr('%s.transparency'%goldLineShader,alphaValue,alphaValue,alphaValue,type = 'double3')

    # button get ShotNode
    def sk_camSeqGetSelShot(self):
        errorInfo = '\n-----------Please Select Valueable Shot Node!!!-----------'
        objs = mc.ls(sl = 1)
        if not objs:
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        needObj = []
        for obj in objs:
            nodeType = mc.nodeType(obj)
            if nodeType not in ['shot']:
                continue
            needObj.append(obj)
        if not needObj:
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        mc.textField('sk_camSeqBreakOutGetShot',e = 1 ,text = needObj[0])

    # button fix shot
    def sk_camSeqFixShotName(self):
        seqInfo = mc.file(exn=1,q=1).split('/')[-1].split('_')[1]
        shotNodes = mc.ls(type= 'shot')
        for checkShotNode in shotNodes:
            if '_' not in checkShotNode:
                errorInfo = '-----[AAS Error]-----\n-----某些shot的名字不合法,没有镜头信息,请改名！-----\n'
                print errorInfo
                mc.error()
            seqNow = checkShotNode.split('_')[1]
            if seqInfo == seqNow:
                continue
            # camName
            camCons = mc.listConnections('%s.currentCamera'%checkShotNode)
            if camCons:
                camCons = camCons[0]
                camConsInfos = camCons.split('_')
                camPre = camConsInfos[0]
                camNow = camConsInfos[1]
                camAft = camCons[(len(camPre) + len(camNow) + 2):]
                camNew = '%s_%s_%s'%(camPre,seqInfo,camAft)
                mc.rename(camCons,camNew)
            # shotNode
            checkInfos = checkShotNode.split('_')
            seqPre = checkInfos[0]
            seqAft = checkShotNode[(len(seqPre) + len(seqNow) + 2):]
            newShotName = '%s_%s_%s'%(seqPre,seqInfo,seqAft)
            mc.rename(checkShotNode,newShotName)

    # button ROT | lenth scale 1 | thick scale 2 | onoff  3  | 4 重建
    # selMode 选取模式
    def sk_camSeqROTPerform(self,mode = 0,dsInfo = '',selMode = 0):
        selValue = 0
        if mode in [1,2]:
            selMode = 1
            if mc.ls('sk_camSeqImgSelMode'):
                selValue = mc.radioButtonGrp('sk_camSeqImgSelMode',select = 1,q = 1)
            else:
                selValue = 2
        # 获取camera
        fixCamList = []
        if selValue == 1:
            camera = self.sk_camGetViewCamera()[0]
            fixCamList.append(camera)
        if selValue in [0,2]:
            fixCamList = self.sk_camGetAllInShotCamera()
        selCamList = []
        selGrps = mc.ls(sl = 1)
        for grp in selGrps:
            nodeType = mc.nodeType(grp)
            if nodeType in ['camera']:
                grp = mc.listRelatives(grp,p=1,type = 'transform')
                if not grp:
                    continue
                grp = grp[0]
            selCamList.append(grp)
        if selMode:
            fixCamList = selCamList
        # 获取缩放类型
        if mode == 1:
            scaleValue = mc.floatField('sk_camSeqImgROTLenthScale',q = 1, value= 1)
            for cam in fixCamList:
                sk_camMatrixScene.cameraTools().camGoldenLineCreate(cam ,viewState = 1,lenthScale = scaleValue)
            if fixCamList:
                mc.select(fixCamList)
        if mode == 2:
            scaleValue = mc.floatField('sk_camSeqImgROTThickScale',q = 1, value= 1)
            for cam in fixCamList:
                sk_camMatrixScene.cameraTools().camGoldenLineCreate(cam ,viewState = 1,thickScale = scaleValue)
            if fixCamList:
                mc.select(fixCamList)
        if mode == 3:
            goldLineRootGrp = 'goldLine_Grp'
            if not mc.ls(goldLineRootGrp):
                mc.group(em=1,name=goldLineRootGrp)
            if fixCamList:
                goldGrp = 'goldenTemp_%s'%(fixCamList[0])
                vState  = mc.getAttr(goldGrp + '.v')
                for cam in fixCamList:
                    if vState == 0:
                        sk_camMatrixScene.cameraTools().camGoldenLineCreate(cam ,viewState = 1)
                    if vState == 1:
                        sk_camMatrixScene.cameraTools().camGoldenLineCreate(cam ,viewState = 0)
            else:
                checkGrps = mc.listRelatives(goldLineRootGrp,c=1,type = 'transform',f=1)
                vState = mc.getAttr(checkGrps[0] + '.v')
                for camGrp in checkGrps:
                    if vState == 0:
                        mc.setAttr((camGrp + '.v'),1)
                    if vState == 1:
                        mc.jihasetAttr((camGrp + '.v'),0)
        if mode == 4:
            projSimp = mc.file(exn=1,q=1).split('/')[-1].split('_')[0]
            for cam in fixCamList:
                sk_camMatrixScene.cameraTools().camGoldenLineCreate(cam ,projSimp = projSimp,rebuild = 1)
    
    # button camera属性统一修正 mode: 1 选取 | 2 所有
    def applyCameraAttrs(self,mode = 1):
        # 获取camera
        needCamShapes = []
        if mode == 1:
            objs = mc.ls(sl = 1,l=1)
            for obj in objs:
                nodeType = mc.nodeType(obj)
                if nodeType not in ['camera']:
                    obj = mc.listRelatives(obj,s=1,type = 'camera',f=1)
                    if not obj:
                        continue
                    obj = obj[0]
                needCamShapes.append(obj)
        if mode == 2:
            needCamShapes = mc.ls(type = 'camera')
        # 获取状态
        filmGateState = mc.checkBox('sk_camSeqApplyFilmGate',q= 1, value = 1)
        if filmGateState:
            filmGateState = 1
        else:
            filmGateState = 0
        ResGateState = mc.checkBox('sk_camSeqApplyResGate',q= 1, value = 1)
        if ResGateState:
            ResGateState = 1
        else:
            ResGateState = 0
        getMaskState = mc.checkBox('sk_camSeqApplyGateMask',q= 1, value = 1)
        if getMaskState:
            getMaskState = 1
        else:
            getMaskState = 0
        # 应用
        for cam in needCamShapes:
            mc.setAttr((cam + '.displaySafeTitle'),filmGateState)
            mc.setAttr((cam + '.displayResolution'),ResGateState)
            mc.setAttr((cam + '.displayGateMask'),getMaskState)

        
    # button 修正时间轴和动画
    def fixTimeLineAnimation(self):
        fileName = mc.file(exn = 1 , q = 1).split('|')[-1]
        frameStart = mc.playbackOptions(min = 1, q = 1)
        frameEnd = mc.playbackOptions(max = 1, q = 1)
        newStart = sk_infoConfig.sk_infoConfig().checkProjectStartFrame(fileName.split('_')[0])
        newEnd   = frameEnd - frameStart + newStart
        offsetValue = newStart - frameStart
        # 曲线偏移
        animCurves = mc.ls(type = 'animCurve')
        needList = []
        for animCurve in animCurves:
            isRef = mc.referenceQuery (animCurve,inr = 1)
            if isRef:
                continue
            needList.append(animCurve)
        mc.keyframe(needList,iub = 1 ,r = 1, o = 'over' , tc = offsetValue)
        # 时间轴
        mc.playbackOptions(min = newStart)
        mc.playbackOptions(max = newEnd)
        # 偏移音频
        audios = mc.ls(type = 'audio')
        for au in audios:
            oldValue = mc.getAttr(au + '.offset')
            mc.setAttr((au + '.offset'),(oldValue + offsetValue))
    
    # button 清理时间轴外的动画信息
    def cleanMoreTimeRange(self):
        animCurves = mc.ls(type = 'animCurve')
        needAnimCurves = []
        for info in animCurves:
            isRef = mc.referenceQuery(info,inr = 1)
            if isRef:
                continue
            needAnimCurves.append(info)
        from idmt.maya.commonCore.core_finalLayout import sk_animCurveCore
        reload(sk_animCurveCore)
        sk_animCurveCore.sk_animCurveCore().checkAnimCleanNoneTimeRange(needAnimCurves)
    
    # ImagePlane On Off
    def sk_camSeqImageOnOff(self,dsInfo = ''):
        # selType
        selValue = mc.radioButtonGrp('sk_camSeqImgSelMode',select = 1,q = 1)
        # 获取camera
        fixCamList = []
        if selValue == 1:
            camera = self.sk_camGetViewCamera()[0]
            fixCamList.append(camera)
        if selValue == 2:
            fixCamList = self.sk_camGetAllInShotCamera()
        # imgNode
        imgList = []
        for cam in fixCamList:
            cameraShape = mc.listRelatives(cam,s= 1, type = 'camera')
            if not cameraShape:
                continue
            cameraShape = cameraShape[0]
            imgNodes = mc.listConnections(cameraShape,s = 1 ,d = 0 ,type = 'imagePlane')
            if not imgNodes:
                continue
            imgList = imgList + imgNodes
        # 处理
        if not imgList:
            return
        mode = mc.getAttr(imgList[0] + '.v')
        switchState = 0
        if mode == 0:
            switchState = 1
        if mode == 1:
            switchState = 0
        for imgNode in imgList:
            mc.setAttr((imgNode + '.v'),switchState)
            
    # mov on off
    def sk_camSeqMovOnOff(self,selMode = 1 , onMode = 1 ):
        imgNodes = []
        if not selMode:
            imgNodes = mc.ls(type = 'imagePlane')
        else:
            selObjs = mc.ls(sl = 1,l=1)
            if not selObjs:
                return
            for selObj in selObjs:
                nodeType = mc.nodeType(selObj)
                if nodeType in ['imagePlane']:
                    imgNodes.append(selObj)
                if nodeType in ['transform']:
                    shape = mc.listRelatives(selObj , s=1, type = 'camera',f=1)
                    if not shape:
                        continue
                    nodeType = 'camera'
                    selObj = shape[0]
                if nodeType in ['shot','camera']:
                    needNodes = mc.listConnections(selObj,s=1,d=0,type = 'imagePlane')
                    if not needNodes:
                        continue
                    imgNodes = imgNodes + needNodes
        print '--------imgNodes'
        print imgNodes
        attr = '.foodPath'
        for imgNode in imgNodes:
            if onMode:
                if not mc.ls(imgNode + attr):
                    continue
                movPath = mc.getAttr(imgNode + attr)
                mc.setAttr((imgNode + '.imageName'),movPath , type = 'string')
            else:
                mc.setAttr((imgNode + '.imageName'),'' , type = 'string')

    # 获取当前面板的camera
    def sk_camGetViewCamera(self):
        viewPanel = mc.getPanel(withFocus = 1)
        panelType = mc.getPanel(typeOf = viewPanel)
        camNeed = '' 
        errorState = 0
        if panelType not in ['modelPanel']:
            panleNew = mel.eval('getCustomViewEditorFromPanel %s'%viewPanel)
            camNeed = mc.stereoCameraView(panleNew,exists = 1,q=1)
            if not camNeed:
                errorState = 1
        else:
            camNeed = mc.modelEditor(viewPanel ,q = 1, camera = 1)
        if errorState:
            errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(107)
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        if mc.nodeType(camNeed) == 'camera':
            camGrp = mc.listRelatives(camNeed,p=1,type = 'transform')[0]
        else:
            camGrp = camNeed
        return [camGrp,viewPanel]

    # 获取镜头内所有camera
    def sk_camGetAllInShotCamera(self):
        fixCamList = []
        shotNodes = mc.ls(type = 'shot')
        if shotNodes:
            for shotNode in shotNodes:
                camera = mc.listConnections(shotNode,s = 1,d = 0 , type = 'camera')
                if not camera:
                    continue
                camera = camera[0]
                if mc.nodeType(camera) in ['transform']:
                    fixCamList.append(camera)
                if mc.nodeType(camera) in ['camera']:
                    camGrp = mc.listRelatives(camera,p=1,type = 'transform')[0]
                    fixCamList.append(camGrp)
        else:
            fixCamList = sk_sceneTools.sk_sceneTools().sk_getProjNeedCamera()
        return fixCamList

    # maya camseq tools config
    def sk_camSeqConfig(self,projSimp):
        mel.eval('SequenceEditor')
        resInfos  = sk_infoConfig.sk_infoConfig().checkAASDb(args = '--qres %s'%projSimp)
        resW = resH = 0
        if resInfos:
            resInfos = resInfos.split('|')[1]
            resW = int(resInfos.split('x')[0])
            resH = int(resInfos.split('x')[1])
        mel.eval('optionVar -intValue  playblastSequenceResW %s'%str(resW))
        mel.eval('optionVar -intValue  playblastSequenceResH %s'%str(resH))
        mel.eval('optionVar -stringValue playblastFormat "qt"')
        mel.eval('optionVar -stringValue playblastCompression "PNG"')
        mel.eval('optionVar -intValue playblastViewerOn 1')
        
    # button Frame Exchange
    def sk_camSeqFrameExchange(self):
        frameOffset = mc.floatField('sk_camSeqShotOffset',q=1,v=1)
        shotNodes = mc.ls(sl=1,type = 'shot')
        allShotNodes = mc.ls(type = 'shot')
        franeMin = 0
        frameMax = 0
        firstNode = ''
        firstEnd = 0
        for checkNode in shotNodes:
            checkS = mc.getAttr(checkNode + '.startFrame')
            checkE = mc.getAttr(checkNode + '.endFrame')
            index = shotNodes.index(checkNode)
            if index == 0:
                franeMin = checkS
                frameMax = checkE
            if checkS <= franeMin:
                franeMin = checkS
                firstNode = checkNode
                firstEnd = checkE
            if checkE >= franeMin:
                frameMax = checkE
        # 后续列表
        needList = shotNodes
        for checkNode in allShotNodes:
            frameEnd = mc.getAttr(checkNode + '.endFrame')
            if frameEnd > frameMax and checkNode not in needList:
                needList.append(checkNode)
        # 偏移shot节点
        for checkNode in needList:
            checkS = mc.getAttr(checkNode + '.startFrame')
            checkE = mc.getAttr(checkNode + '.endFrame')
            seqS   = mc.getAttr(checkNode + '.sequenceStartFrame')
            mc.setAttr((checkNode + '.endFrame'),checkE + frameOffset)
            if checkNode == firstNode:
                continue
            mc.setAttr((checkNode + '.startFrame'),checkS + frameOffset)
            mc.setAttr((checkNode + '.sequenceStartFrame'),seqS + frameOffset)
        # 偏移曲线
        frameRange = (firstEnd,99999999)
        animCurves = mc.ls(type = 'animCurve')
        temps = []
        for animCurve in animCurves:
            isRef = mc.referenceQuery(animCurve ,inr = 1)
            if isRef:
                continue
            temps.append(animCurve)
        animCurves = temps
        mc.keyframe(animCurves,e = 1 ,iub=True , o = 'over',time = frameRange,r = 1 , tc = frameOffset)
        '''
        # rangeMode
        sourceInfos = mc.floatFieldGrp ('sk_camSeqFOSourceRange',q= 1, value = 1)
        targetInfos = mc.floatFieldGrp ('sk_camSeqFOTargetRange',q= 1, value = 1)
        sourceFrameStart = sourceInfos[0]
        sourceFrameEnd = sourceInfos[1]
        targetFrameStart = targetInfos[0]
        targetFrameEnd = targetInfos[1]
        # animCurvs
        animCurves = mc.ls(type = 'animCurve')
        temps = []
        for animCurve in animCurves:
            isRef = mc.referenceQuery(animCurve ,inr = 1)
            if isRef:
                continue
            temps.append(animCurve)
        animCurves = temps
        # 偏移至临时范围
        sourceOffset = -5000
        sourceFrameRange = (sourceFrameStart,sourceFrameEnd)
        sk_sceneTools.sk_sceneTools().checkSceneAnimOffsetPerform(animCurves,offsetValue = sourceOffset , frameRange = sourceFrameRange)
        targetOffset = -8000
        targetFrameRange = (targetFrameStart,targetFrameEnd)
        sk_sceneTools.sk_sceneTools().checkSceneAnimOffsetPerform(animCurves,offsetValue = targetOffset , frameRange = targetFrameRange)
        # 偏移至目标范围
        sourceOffsetNew    =  targetFrameStart - (sourceFrameStart + sourceOffset)
        sourceFrameRangeNew = ((sourceFrameStart + sourceOffset),(sourceFrameEnd + sourceOffset))
        sk_sceneTools.sk_sceneTools().checkSceneAnimOffsetPerform(animCurves,offsetValue = sourceOffsetNew , frameRange = sourceFrameRangeNew)
        targetOffsetNew    =  sourceFrameStart - (targetFrameStart + targetOffset)
        targetFrameRangeNew = ((targetFrameStart + targetOffset),(targetFrameEnd + targetOffset))
        sk_sceneTools.sk_sceneTools().checkSceneAnimOffsetPerform(animCurves,offsetValue = targetOffsetNew , frameRange = targetFrameRangeNew)
        '''
    #-------------------------------------------------------------------------------------#
    # import perform配套工具集
    #-------------------------------------#
    # 更新最新版本mov
    def sk_camMovCopy(self,seqInfos):
        filename = '%s_bv'%(seqInfos)
        shotInfos = filename.split('_')
        shotType = sk_infoConfig.sk_infoConfig().checkShotType(shotInfos[0])
        projectPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath(shotInfos = shotInfos,productionMode = 2,mayaMode = 0)
        productionPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath(shotInfos = shotInfos,productionMode = 1,mayaMode = 0)
        layoutFolder = 'Previsualization'
        sourcePath = '%sshots/%s/000/bgPrevis/%s'%(productionPath,shotInfos[1],filename)
        targetPath= '%sPreProduction/%s/bgPrevis/%s/%s'%(projectPath,layoutFolder,shotInfos[1],filename)
        if shotType == 3:
            sourcePath = '%sshots/%s/%s/000/bgPrevis/%s'%(productionPath,shotInfos[1],shotInfos[2],filename)
        pySysFile.pySysFile('copy',[sourcePath],[targetPath])
    
    #---------------------------#
    # 修正图路径
    def sk_camImgSetting(self,xmlServerPath):
        xmlServerFolder = xmlServerPath[:-1*(len(xmlServerPath.split('/')[-1]))]
        imageShapes = mc.ls(type = 'imagePlane')
        attr = '.foodPath'
        for imgShape in imageShapes:
            pathOld  = mc.getAttr(imgShape + '.imageName')
            if not pathOld:
                shotNodes = mc.listConnections(imgShape,s=0,d=1,type = 'shot')
                pathOld = '%s.mov'%(shotNodes[0])
            newPath = '%s%s'%(xmlServerFolder,pathOld.split('/')[-1])
            if not mc.ls(imgShape + attr):
                mc.addAttr(imgShape, ln=attr.split('.')[-1] , dt='string')
            #mc.setAttr((imgShape + '.imageName'),'',type = 'string')
            mc.setAttr((imgShape + attr),newPath,type = 'string')
            #mc.setAttr((imgShape + '.imageName'),newPath,type = 'string')
            
    #---------------------------#
    # 加载音频
    def sk_camImgImportAudio(self,xmlPath):
        audioPath = xmlPath.replace('.xml','_au.wav')
        if not os.path.exists(audioPath):
            return
        # 校正
        audioNodes = mc.ls(type = 'audio')
        if not audioNodes:
            return
        for node in audioNodes:
            mc.setAttr((node + '.filename'),audioPath,type = 'string')
        
    #----------------------------#
    # 校正camera
    def sk_camSetting(self,projSimp,goldenLine = 1):
        # 修正文件
        self.sk_shotDefaultConfig(projSimp)
        resInfos = sk_infoConfig.sk_infoConfig().checkProjCamSetting(projSimp)
        # 处理camera
        cameraShapes  = mc.ls(type = 'camera')
        for cameraShape in cameraShapes:
            camGrp = mc.listRelatives(cameraShape,p = 1 ,type = 'transform')[0]
            if '_' not in camGrp:
                continue
            # 控制器创建
            camInfos = camGrp.split('_')
            preName = '%s_%s_%s'%(camInfos[0],camInfos[1],camInfos[2])
            sk_sceneTools.sk_sceneTools().sk_createCamCtrls(camGrp,preName)
            camKey = 'Camera'
            mc.setAttr(cameraShape + '.displayGateMaskColor',0,0,0,type = 'double3')
            mc.setAttr(cameraShape + '.displayGateMaskOpacity',1)
            mc.setAttr(cameraShape + '.displayResolution',1)
            mc.setAttr(cameraShape + '.overscan',resInfos[2])
            mc.setAttr(cameraShape + '.horizontalFilmAperture',resInfos[0])
            mc.setAttr(cameraShape + '.verticalFilmAperture',resInfos[1])
            mc.setAttr(cameraShape + '.lensSqueezeRatio',resInfos[3])
            if camKey in camGrp:
                newCameName = 'cam%s'%(camGrp.split(camKey)[0][len(camGrp.split(camKey)[0].split('_')[0]):])
                mc.rename(camGrp,newCameName)
            else:
                newCameName = camGrp
            checkKeys = ['_sb']
            for checkKey in checkKeys:
                if checkKey not in newCameName:
                    continue
                tempNew = newCameName.split(checkKey)[0]
                mc.rename(newCameName,tempNew)
                newCameName = tempNew
            # goldenLine
            if goldenLine:
                sk_camMatrixScene.cameraTools().camGoldenLineCreate(newCameName ,projSimp = projSimp,viewState = 1)
        # 处理图片
        imageShapes = mc.ls(type = 'imagePlane')
        for imgShape in imageShapes:
            mc.setAttr( imgShape + '.sizeX',resInfos[0])
            mc.setAttr( imgShape + '.sizeY',resInfos[1])
            mc.setAttr((imgShape+'.fit'),1)
            mel.eval('AEinvokeFitRezGate %s %s'%(( imgShape + '.sizeX'),( imgShape + '.sizeY')))

    #----------------------------#
    # 校正时间轴
    def sk_timeLineConfig(self):
        shotNodes = mc.ls(type = 'shot')
        stFrame = []
        edFrame = []
        for shotNode in shotNodes:
            stFrame.append(mc.getAttr(shotNode + '.startFrame'))
            edFrame.append(mc.getAttr(shotNode + '.endFrame'))
        if stFrame:
            minFrame = min(stFrame)
            if minFrame > int(minFrame):
                minFrame = int(minFrame) - 1
            else:
                minFrame = int(minFrame)
            maxFrame = max(edFrame)
            if maxFrame > int(maxFrame):
                maxFrame = int(maxFrame) + 1
            else:
                maxFrame = int(maxFrame)
        else:
            minFrame = 1
            maxFrame = 2
        mc.playbackOptions(min=minFrame)
        mc.playbackOptions(max=maxFrame)
            
    # 动画曲线平移
    def sk_animCurveMove(self,animCurves,value):
        for animCurve in animCurves:
            mc.keyframe(animCurve,iub = 1 ,r = 1, o = 'over' , tc = value)
            
    # 修正fps
    def sk_shotDefaultConfig(self,projSimp, checkMode = 0):
        # FPS
        fpsFrame   = sk_infoConfig.sk_infoConfig().checkAASDb(args = '--qfps %s'%projSimp)
        if fpsFrame:
            fpsFrame = int(fpsFrame.split('|')[1])
        timeName = ['game','film','pal','ntsc','show','palf','ntscf']
        timeSpeed= [15,     24,    25,   30,    48,    50,   60]
        fpsFrameName = timeName[timeSpeed.index(fpsFrame)]
        if checkMode:
            speedMode = mc.currentUnit(time = 1,q=1)
            if  speedMode != fpsFrameName:
                errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(100)
                print errorInfo
                sk_infoConfig.errorCode = errorInfo
                mc.error()
        if fpsFrame:
            mc.currentUnit(time = fpsFrameName)
        # res
        sgState = sk_infoConfig.sk_infoConfig().checkSGState(projSimp)
        resW = resH = 0
        if not sgState:
            resInfos  = sk_infoConfig.sk_infoConfig().checkAASDb(args = '--qres %s'%projSimp)
            if resInfos:
                resInfos = resInfos.split('|')[1]
        if sgState:
            from idmt.maya.commonPerform.shotgun import sgBase
            reload(sgBase)
            sg = sgBase.sgBase().shotgunCons(1)
            projDict = sgBase.sgBase().getProjInfos(sg,projSimp=projSimp)
            resInfos = projDict['sg_resolutionrender']
        resW = int(resInfos.split('x')[0])
        resH = int(resInfos.split('x')[1])
        mc.setAttr(('defaultResolution.width'), resW)
        mc.setAttr(('defaultResolution.height'), resH)
        ratio = resW / (resH + float('.0'))
        mc.setAttr(('defaultResolution.deviceAspectRatio'), ratio)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)

    #-------------------------------------------------------------------------------------#
    # asset 参考工具集
    #-------------------------------------#
    # assets reference
    def sk_assetsReferencePerform(self,selMode = 0):
        shotNodes = []
        if selMode:
            shotNodes = mc.ls(sl = 1 , type = 'shot')
        else:
            shotNodes = mc.ls(type = 'shot')
        if not shotNodes:
            return
        # 开始查询
        assetDict = self.sk_getShotAssetListDictInfo(shotNodes)
        projSimp = shotNodes[0].split('_')[0]
        # 对比文件存在的参考
        assetListInFile = self.sk_collectFileAssetsList()
        needAssetList = dict()
        if not assetListInFile:
            needAssetList = assetDict
        else:
            checkKeys = assetDict.keys()
            fileKeys  = assetListInFile.keys()
            for key in checkKeys:
                if key not in fileKeys:
                    needAssetList[key] = assetDict[key]
                else:
                    allValue = assetDict[key]
                    fileValue = assetListInFile[key]
                    if allValue > fileValue:
                        needAssetList[key] = allValue - fileValue
        print '--------'
        print needAssetList
        # 执行参考
        self.sk_referenceNeedAssetList(projSimp,needAssetList)
        
    # 获取shot asset list dict
    def sk_getShotAssetListDictInfo(self,shotList):
        assetDict = dict()
        for shotNode in shotList:
            dataGet = os.popen('%s --qlist %s'%(self.dbpy,shotNode))
            getInfo = dataGet.read()
            # 这里需要检测
            assetList = getInfo.split('|')[1:]
            # 收集本镜数量
            checkAssetDict = self.sk_assetListConfig(assetList)
            checkKeys = checkAssetDict.keys()
            assetKeys = assetDict.keys()
            if not checkKeys:
                continue
            # 扩充总信息量
            for key in checkKeys:
                if key not in assetKeys:
                    assetDict[key] = 1
                else:
                    needValue = max(assetDict[key],checkAssetDict[key])
                    assetDict[key] = needValue
        return assetDict

    # 筛选物体List
    def sk_assetListConfig(self,assetList):
        checkAssetDict = dict()
        for asset in assetList:
            if '\n' in asset:
                asset = asset.split('\n')[0]
            assetKeys = checkAssetDict.keys()
            if asset not in assetKeys:
                checkAssetDict[asset] = 1
            else:
                checkAssetDict[asset] = checkAssetDict[asset] + 1
        return checkAssetDict
    
    # 统计文件内参考信息
    def sk_collectFileAssetsList(self):
        refList = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNs = refList[2][0]
        assetList = dict()
        for ns in refNs:
            if not ns:
                continue
            assetKeys = assetList.keys()
            if '_' not in ns:
                continue
            assetID = ns.split('_')[1]
            if assetID not in assetKeys:
                assetList[assetID] = 1
            else:
                assetList[assetID] = assetList[assetID] + 1
        return assetList
    
    # 批量参考指定asset的参考
    def sk_referenceNeedAssetList(self,projSimp,needAssetList,defualtType = 'l'):
        assetIDs = needAssetList.keys()
        missAssets  = []
        for assetID in assetIDs:
            shotInfos = [projSimp,assetID,defualtType,'ani']
            assetServerPath = sk_infoConfig.sk_infoConfig().checkProjectServerFilePath(shotInfos)
            refPerform = 1
            needRefPath = ''
            if os.path.exists(assetServerPath):
                needRefPath = assetServerPath
            else:
                needRefPath = assetServerPath.replace('_l_','_t_')
                if not os.path.exists(needRefPath):
                    needRefPath = assetServerPath.replace('_l_','_h_')
                    if not os.path.exists(needRefPath):
                        refPerform = 0
                        missAssets.append(assetID)
            # 参考
            if refPerform:
                try:
                    mc.file(needRefPath,r = 1 ,namespace = ':%s_%s'%(projSimp,assetID))
                except:
                    pass
        # 校正namespace
        sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig()
        # 返回数据
        return assetIDs

    #-------------------------------------------------------------------------------------#
    # 拆分工具集
    #-------------------------------------#
    # 分拆文件,ly shot , ly seq都需要上传
    def sk_camSeqSplitPerform(self, selMode = 0 , needShotNodes = [] ,needObjs = [],printMode = 1):
        # 整理文件
        if printMode: print '------------001'
        sk_sceneTools.sk_sceneTools().checkDonotNodeCleanBase(0)
        sgState = sk_infoConfig.sk_infoConfig().checkSGState()
        self.sk_camSeqFixSameNameCamera()
        if not needShotNodes:
            if selMode:
                shotNodes = mc.ls(sl = 1 , type = 'shot')
            else:
                shotNodes = mc.ls(type = 'shot')
        else:
            shotNodes = needShotNodes
        if printMode: print '------------002'
        filePath = mc.file(exn = 1, q = 1)
        fileFolder = filePath[:-1*len(filePath.split('/')[-1])]
        shotNodeType = '_sb'
        # 分解导出
        splitFiles = []
        changeFrames = []
        newStart = []
        newEnd   = []
        oldStart = []
        oldEnd   = []
        # seqName
        if printMode: print '------------003'
        checkShotInfos = shotNodes[0].split('_')
        checkShotType = sk_infoConfig.sk_infoConfig().checkShotType()
        splitFolder = '%s%s_%s'%(fileFolder,checkShotInfos[0],checkShotInfos[1])
        if checkShotType == 3:
            splitFolder = '%s%s_%s_%s'%(fileFolder,checkShotInfos[0],checkShotInfos[1],checkShotInfos[2])
        if not os.path.exists(splitFolder):
            os.makedirs(splitFolder)
        if printMode: print '------------005'
        # 分割
        layoutKey = 'ly'
        if sgState:
            layoutKey = 'lay_v001'
        for shotNode in shotNodes:
            if printMode: print '=========001'
            shotName = self.sk_camSeqGetRealShotName(shotNode)
            projSimp = shotNode.split('_')[0]
            # 处理camera
            #camOgInfos = self.sk_camSeqCam2RigCam(shotNode)
            cameraNow = self.sk_camSeqGetShotNodeCamera(shotNode)
            # 导出
            if shotNodeType not in shotName:
                shotName = '%s_%s'%(shotName,shotNodeType)
            if shotNodeType in shotNode:
                splitFileName = '%s.ma'%(shotName.replace(shotNodeType,layoutKey))
            else:
                splitFileName = '%s%s.ma'%(shotName,layoutKey)
            if printMode: print '=========002'
            splitFilePath = '%s/%s'%(splitFolder,splitFileName)
            # 获取物体
            if not needObjs:
                shotObjs = self.sk_getShotObjs(shotNode,shotNodeType)
            else:
                shotObjs = needObjs
            if cameraNow not in shotObjs:
                shotObjs.append(cameraNow)
            goldenLineGrp = sk_camMatrixScene.cameraTools().getGoldenGrpFromCam(cameraNow)
            if goldenLineGrp and goldenLineGrp not in shotObjs:
                shotObjs.append(goldenLineGrp)
            if printMode: print '=========003'
            # 处理信息
            #if mc.ls('cam_World'):
            #    shotObjs = shotObjs + ['cam_World']
            mc.select(shotObjs)
            if printMode: print '=========005'
            mc.file(splitFilePath, force=1, options="v=0" , type='mayaAscii', preserveReferences=1, exportSelected=1)
            splitFiles.append(splitFilePath)
            if printMode: print '=========006'
            # bkCamera
            # 记录偏移时间
            startFrame = mc.getAttr(shotNode + '.startFrame')
            endFrame = mc.getAttr(shotNode + '.endFrame')
            oldStart.append(startFrame)
            oldEnd.append(endFrame)
            defaultStart = sk_infoConfig.sk_infoConfig().checkProjectStartFrame(projSimp)
            changeFrames.append(int(defaultStart) - int(startFrame))
            newStart.append(defaultStart)
            newEndFrame = int(defaultStart)  + endFrame - int(startFrame)
            if printMode: print '=========007'
            if newEndFrame > int(newEndFrame):
                newEndFrame = int(newEndFrame) + 1
            else:
                newEndFrame = int(newEndFrame)
            newEnd.append(newEndFrame)
            # bkCamera
            mc.playbackOptions(min = startFrame)
            mc.playbackOptions(max = endFrame)
            newShotInfo = splitFileName.split('_')
            print newShotInfo
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(batchUpadate = 1 ,shotInfo = newShotInfo,abcExport = 0)
            if printMode: print '=========008'
            # 还原camera
            #if camOgInfos[0]:
            #    mc.delete(camOgInfos[1])
            #    mc.rename(camOgInfos[0],camOgInfos[1])
            #    mc.delete('cam_World')
            if printMode: print '=========009'
        # 处理动画曲线
        for i in range(len(splitFiles)):
            splitFile = splitFiles[i]
            changeFrame = changeFrames[i]
            sFrame = newStart[i]
            eFrame = newEnd[i]
            oldSFrame = oldStart[i]
            oldEFrame = oldEnd[i]
            print '--------------frames'
            print oldSFrame
            print oldEFrame
            # 修正时间轴
            self.sk_fixTimeLineByReadMa(splitFile,oldSFrame,oldEFrame,offset = 0)
            # 修正动画曲线
            #self.sk_fixAnimInfosByReadMa(splitFile,changeFrame)
        print '--------------Split Folder:'
        print splitFolder

    #----------------------------#
    # button breakOut by hands
    def sk_camSeqBreakOutByHands(self):
        shotNode = mc.textField('sk_camSeqBreakOutGetShot',q = 1 , text = 1)
        if not shotNode or not mc.ls(shotNode):
            errorInfo = u'-----------No Shot Node to Target-----------'
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        selObjs = mc.ls(sl = 1,l = 1,type = 'transform')
        if not selObjs:
            errorInfo = u'-----------No Assets Selected !!!-----------'
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        audioFile = mc.ls(type = 'audio')
        selObjs = selObjs + audioFile
        print '------------shotNode'
        print shotNode
        print selObjs
        self.sk_camSeqSplitPerform(0,[shotNode],selObjs)

    #-----------------------------#
    # 获取shotNode的camera
    def sk_camSeqGetShotNodeCamera(self,shotNode):
        cameraNow = mc.listConnections(shotNode,s = 1 ,d = 0 , type = 'camera')
        if not cameraNow:
            errorInfo = u'-----------No camera for Shot:[%s]-----------'%(shotNode)
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        camGrpNow = mc.ls(cameraNow[0],l=1)[0]
        nodeType = mc.nodeType(camGrpNow)
        if nodeType == 'camera':
            camGrpNow = mc.listRelatives(camGrpNow,p=1,type = 'transform',f = 1)[0]
        return camGrpNow

    #-----------------------------#
    # cam转rgCam
    def sk_camSeqCam2RigCam(self,shotNode):
        camOg = ''
        cameraNow = mc.listConnections(shotNode,s = 1 ,d = 0 , type = 'camera')
        if not cameraNow:
            errorInfo = u'-----------No camera for Shot:[%s]-----------'%(shotNode)
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()
        camGrpNow = mc.ls(cameraNow[0],l=1)[0]
        nodeType = mc.nodeType(camGrpNow)
        if nodeType == 'camera':
            camGrpNow = mc.listRelatives(camGrpNow,p=1,type = 'transform',f = 1)[0]
        camCheck = shotNode.replace(shotNode.split('_')[0],'cam')
        camNeed = ''
        # 备份重名cam
        if mc.ls(camCheck):
            if camGrpNow.split('|')[-1] == camCheck:
                camNeed = mc.rename(camCheck,'%s_FoodTemp'%camCheck)
                camOg = camNeed
            else:
                camOg = mc.rename(camCheck,'%s_FoodTemp'%camCheck)
                camNeed = camGrpNow
        else:
            camNeed = camGrpNow
        # 导入
        camServerBase = sk_infoConfig.sk_infoConfig().checkProjectServerPath(shotInfos = shotNode.split('_'),productionMode = 1,mayaMode = 0)
        camServerFile = '%s%s/CamBase/cam_rig.ma'%(camServerBase,sk_infoConfig.sk_infoConfig().serverDataFolder)
        nsTemp = 'foodCamTemp'
        try:
            self.sk_deleteNamespace(nsTemp)
        except:
            pass
        mc.file(camServerFile,i=1,f=1,ns= nsTemp)
        self.sk_deleteNamespace(nsTemp)
        mc.rename('cam_base',camCheck)
        tarGetGrp = camCheck
        # 转移连接
        # transform
        for attr in ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz','.v']:
            mc.setAttr((tarGetGrp + attr),mc.getAttr(camNeed + attr))
        consInfos = mc.listConnections(camNeed,s=1,d=0,c=1,plugs= 1)
        if not consInfos:
            consInfos = []
        for num in range(len(consInfos)/2):
            targetAttr   = consInfos[2*num]
            sourceAttr = consInfos[2*num+1]
            mc.connectAttr(sourceAttr,'%s.%s'%(tarGetGrp,targetAttr.split('.')[-1]),f=1)
        # shape
        targetShape = mc.listRelatives(tarGetGrp,s=1,type = 'camera')[0]
        sourceShape = mc.listRelatives(camNeed,s=1,type='camera')[0]
        listAttrs = mc.listAttr(targetShape,keyable = 1)
        listAttrs = listAttrs + ['nearClipPlane','farClipPlane','displayResolution','displayGateMask','displayGateMaskOpacity','overscan']
        for attr in listAttrs:
            if attr[:2] in ['mr','ai']:
                continue
            mc.setAttr((targetShape +'.' + attr),mc.getAttr(sourceShape + '.'+ attr))
        mc.setAttr((targetShape + '.displayGateMaskColor'),0,0,0,type = 'double3')
        consShapeInfos = mc.listConnections(sourceShape,s=1,d=0,c=1,plugs= 1)
        if not consShapeInfos:
            consShapeInfos = []
        for num in range(len(consShapeInfos)/2):
            targetAttr   = consShapeInfos[2*num]
            sourceTarget = consShapeInfos[2*num+1]
            mc.connectAttr(sourceTarget,'%s.%s'%(targetShape,targetAttr.split('.')[-1]),f=1)
        consShapeOutPuts = mc.listConnections(sourceShape,s=0,d=1,c=1,plugs= 1) 
        if not consShapeOutPuts:
            consShapeOutPuts = []
        for num in range(len(consShapeOutPuts)/2):
            sourceAttr   = consShapeOutPuts[2*num]
            targetAttr = consShapeOutPuts[2*num+1]
            mc.disconnectAttr(sourceAttr,targetAttr)
            mc.connectAttr('%s.%s'%(targetShape,sourceAttr.split('.')[-1]),targetAttr,f=1)
        return [camOg,camCheck]

    # 收集shot物体信息
    # chooseAssetMode  0 默认顺序级  | 1 镜头解算
    # scanMode         0 优先数据库  | 1 镜头扫描
    def sk_getShotObjs(self,shotNode,shotNodeType = '',chooseAssetMode = 1,scanMode = 0):
        # cam
        projSimp = shotNode.split('_')[0]
        if shotNodeType in shotNode and shotNodeType:
            shotName = shotNode.split(shotNodeType)[0]
        else:
            shotName = shotNode
        shotName = self.sk_camSeqGetRealShotName(shotNode)
        camName = shotName.replace(projSimp,'cam')
        # ref list组
        refGrps = []
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refNsList   = refInfos[2][0]
        # 获取asset的namespace
        if scanMode == 0:
            assetList = self.sk_getShotAssetListDictInfo([shotNode])
            assetKeys = assetList.keys()
            allAssetList = self.sk_collectFileAssetsList()
            needAssetRefNode = []
            numList = range(100)
            for assetID in assetKeys:
                nsKey = '%s_%s'%(projSimp,assetID)
                if assetID not in allAssetList.keys():
                    errorInfo = u'-----Lost Asset in the Shot,please Check the Shot Asset List in Database-----'
                    print errorInfo
                    sk_infoConfig.errorCode = errorInfo
                    mc.error()
                if allAssetList[assetID] == 1:
                    for ns in refNsList:
                        if nsKey not in ns:
                            continue
                        if ns.split('_')[-1] in numList:
                            continue
                        needAssetRefNode.append(refNodes[refNsList.index(ns)])
                        break
                else:
                    # 多个asset
                    if chooseAssetMode == 0:
                        for ns in refNsList:
                            if nsKey not in ns:
                                continue
                            if ns.split('_')[-1] not in numList:
                                # 记录标准的
                                needAssetRefNode.append(refNodes[refNsList.index(ns)])
                            else:
                                # 记录前标准位
                                if int(ns.split('_')[-1]) in range(assetList[assetID]):
                                    needAssetRefNode.append(refNodes[refNsList.index(ns)])
                    if chooseAssetMode == 1:
                        allCheckObjs = []
                        for ns in refNsList:
                            if nsKey not in ns:
                                continue
                            nsRootGrp = mc.referenceQuery(refNodes[refNsList.index(ns)],nodes = 1)[0]
                            nsMeshes = mc.listRelatives(nsRootGrp,ad = 1 ,type = 'mesh',f = 1)
                            for mesh in nsMeshes:
                                nsGrp = mc.listRelatives(mesh,p=1,type = 'transform',f = 1)[0]
                                if nsGrp in allCheckObjs:
                                    continue
                                allCheckObjs.append(nsGrp)
                        from idmt.maya.commonCore.core_mayaCommon import sk_camMatrixScene
                        reload(sk_camMatrixScene)
                        checkSFrame = mc.getAttr(shotNode + '.startFrame')
                        if int(checkSFrame) < checkSFrame:
                            checkSFrame = int(checkSFrame) + 1
                        checkEFrame = int(mc.getAttr(shotNode + '.endFrame'))
                        camName = 'cam_%s'%(shotName[(len(shotName.split('_')[0])+1):])
                        checkInfos = sk_camMatrixScene.sk_camMatrixScene().sk_sceneMeshCamMatrixCheckSequence(checkSFrame,checkEFrame,camName,allCheckObjs,4,1)
                        needNsList = []
                        for obj in checkInfos[0]:
                            tempGrp = obj.split('|')[-1]
                            ns =  tempGrp[:-1*(len(tempGrp.split(':')[-1])+1)]
                            if ns in needNsList:
                                continue
                            needNsList.append(ns)
                            needAssetRefNode.append(refNodes[refNsList.index(ns)])
                        print '-----------------checkAssets'
                        print needNsList
        if scanMode == 1:
            allCheckObjs = []
            for ns in refNsList:
                nsRootGrp = mc.referenceQuery(refNodes[refNsList.index(ns)],nodes = 1)[0]
                nsMeshes = mc.listRelatives(nsRootGrp,ad = 1 ,type = 'mesh',f = 1)
                for mesh in nsMeshes:
                    nsGrp = mc.listRelatives(mesh,p=1,type = 'transform',f = 1)[0]
                    if nsGrp in allCheckObjs:
                        continue
                    allCheckObjs.append(nsGrp)
            from idmt.maya.commonCore.core_mayaCommon import sk_camMatrixScene
            reload(sk_camMatrixScene)
            checkSFrame = mc.getAttr(shotNode + '.startFrame')
            if int(checkSFrame) < checkSFrame:
                checkSFrame = int(checkSFrame) + 1
            checkEFrame = int(mc.getAttr(shotNode + '.endFrame'))
            camName = 'cam_%s'%(shotName[(len(shotName.split('_')[0])+1):])
            checkInfos = sk_camMatrixScene.sk_camMatrixScene().sk_sceneMeshCamMatrixCheckSequence(checkSFrame,checkEFrame,camName,allCheckObjs,0,1)
            needNsList = []
            for obj in checkInfos:
                tempGrp = obj.split('|')[-1]
                ns =  tempGrp[:-1*(len(tempGrp.split(':')[-1])+1)]
                if ns in needNsList:
                    continue
                needNsList.append(ns)
                needAssetRefNode.append(refNodes[refNsList.index(ns)])
                
        # 获取指定ns的组
        for refNode in needAssetRefNode:
            grps = mc.referenceQuery(refNode,nodes = 1)
            if not grps:
                continue
            refGrps.append(grps[0])
        return ([camName] + refGrps)
    
    # 读取ma文件修正动画曲线时间轴
    def sk_fixAnimInfosByReadMa(self,maFile,offsetFrame):
        fileInfos = sk_infoConfig.sk_infoConfig().checkFileRead(maFile)
        print '----------Statr:'
        print maFile
        animCurveKey = 'createNode animCurve'
        animPointKey = '.ktv['
        animLineIDs = []
        for lineInfo in fileInfos:
            if animCurveKey not in lineInfo:
                continue
            animLineIDs.append(fileInfos.index(lineInfo))
        
        for i in range(len(animLineIDs)):
            soureFrame = animLineIDs[i]
            if animLineIDs[i] == animLineIDs[-1]:
                targetFrame= animLineIDs[i] + 10
            else:
                targetFrame= animLineIDs[i+1]
            for j in range(soureFrame,targetFrame):
                lineInfo = fileInfos[j]
                if animPointKey not in lineInfo:
                    continue
                needInfos = lineInfo.split(']')[-1].split(' ')
                addTemp = 0
                if ';' not in needInfos[-1]:
                    addTemp = 1
                    needInfos = needInfos + fileInfos[j+2].split(' ')
                ttIndex = 0
                if '\t\t' in needInfos:
                    ttIndex = needInfos.index('\t\t')
                    needInfos.remove('\t\t')
                needNums = []
                newNums = []
                for m in range(2,len(needInfos)):
                    id = needInfos.index(needInfos[m])
                    if id == ttIndex - 1:
                        needInfos[m] = needInfos[m].split('\n')[0]
                    if id%2 != 0:
                        newNums.append(needInfos[m])
                        continue
                    if ';' in needInfos[m]:
                        needInfos[m] = needInfos[m].split(';')[0]
                    if '.' in needInfos[m]:
                        oldFrame = float(needInfos[m])
                    else:
                        oldFrame = int(needInfos[m])
                    needNums.append(oldFrame)
                    newFrame = oldFrame + offsetFrame
                    newNums.append(newFrame)
                newLineInfo = '%s]" '%lineInfo.split(']')[0]
                for newInfo in newNums:
                    if ';' in str(newInfo):
                        newLineInfo = newLineInfo + str(newInfo)
                    else:
                        newLineInfo = newLineInfo + str(newInfo) + ' '
                newLineInfo = newLineInfo.replace('\t\t','')
                #print '-------------------------------u'
                #print newLineInfo
                fileInfos[j] = newLineInfo
                if addTemp:
                    fileInfos[j+2] = ''
        print '----------End:'
        print maFile
        resultInfos = []
        for info in fileInfos:
            if not info:
                continue
            if info == '\n':
                continue
            resultInfos.append(info)
        fileInfos = resultInfos
        sk_infoConfig.sk_infoConfig().checkFileWrite(maFile,fileInfos)
        
    # 修正时间轴起始点
    def sk_fixTimeLineByReadMa(self,maFile,stFrame,edFrame,offset = 0):
        fileInfos = sk_infoConfig.sk_infoConfig().checkFileRead(maFile)
    
        createNodeKey = 'createNode '
        timeLineKey = 'createNode script -n "sceneConfigurationScriptNode"'
        playOptionKey = 'playbackOptions'
        nodeLineList = []
        addInfo = '%s -min %s -max %s -ast %s -aet %s ";'%(playOptionKey,str(stFrame),str(edFrame),str(stFrame - offset),str(edFrame + offset))
        hasTimeInfo = 0
        
        for lineInfo in fileInfos:
            if createNodeKey not in lineInfo:
                continue
            if timeLineKey in lineInfo:
                hasTimeInfo = fileInfos.index(lineInfo)
            nodeLineList.append(fileInfos.index(lineInfo))
        
        if hasTimeInfo:
            for i in range(hasTimeInfo,hasTimeInfo + 10):
                lineInfo = fileInfos[i]
                if playOptionKey not in lineInfo:
                    continue
                lastInfo = '%s%s'%(lineInfo.split(playOptionKey)[0],addInfo)
                fileInfos[i] = lastInfo
        else:
            addInfos = ['createNode script -n "sceneConfigurationScriptNode";','    setAttr ".b" -type "string" "%s -min %s -max %s -ast %s -aet %s ";'%(playOptionKey,str(stFrame),str(edFrame),str(stFrame - offset),str(edFrame + offset)),'    setAttr ".st" 6;']
            tempInfos = fileInfos[:nodeLineList[-1]] + addInfos + fileInfos[nodeLineList[-1]:]
            fileInfos = tempInfos
        sk_infoConfig.sk_infoConfig().checkFileWrite(maFile,fileInfos)
        
    #-----------------------------------------#
    # playblast 
    #-----------------------------------------#
    # 0 选取playblast | 1 全部 shot | 3 sequence
    def sk_camSeqPlayblast(self,mode = 1):
        pass
    
    #-----------------------------------------#
    # 获取真实shotName
    def sk_camSeqGetRealShotName(self,shotNode):
        checkShotInfos = shotNode.split('_')
        shotType = sk_infoConfig.sk_infoConfig().checkShotType(checkShotInfos[0])
        needShotNode = '%s_%s_%s'%(checkShotInfos[0],checkShotInfos[1],checkShotInfos[2])
        if shotType == 3:
            needShotNode = '%s_%s_%s_%s'%(checkShotInfos[0],checkShotInfos[1],checkShotInfos[2],checkShotInfos[3])
        return needShotNode
    
    #-----------------------------------------#
    # 清理namespace
    def sk_deleteNamespace(self,namespace):
        ns = namespace
        # 使得namespace成为空的namespace
        mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
        # 清理空namespace
        mc.namespace(removeNamespace= (':' + ns))
    
    #-----------------------------------------#
    # 修正重名camera
    def sk_camSeqFixSameNameCamera(self):
        cameras = mc.ls(type = 'camera',l=1)
        cameraGrps = mc.listRelatives(cameras,p=1,type = 'transform',f = 1)
        # 获取简称
        camSims = []
        for cam in cameraGrps:
            camSims.append(cam.split('|')[-1])
            # 重命名Shape
            shapeNode = mc.listRelatives(cam,s=1,type = 'camera',f = 1)
            try:
                mc.rename(shapeNode[0],'%s_Shape'%(cam.split('|')[-1]))
            except:
                pass
        # 获取重名
        from idmt.mayacommonCore.core_mayaCommon import sk_pyCommon
        reload(sk_pyCommon)
        for cam in cameraGrps:
            if not mc.ls(cam):
                continue
            checkInfo = cam.split('|')[-1]
            sameNum = camSims.count(checkInfo)
            if sameNum == 1:
                continue
            # rename
            indexList = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(camSims, checkInfo)
            for i in range(len(indexList)):
                if i == 0:
                    continue
                oldCam = cameraGrps[indexList[i]]
                newCam = '%s_%s'%(oldCam.split('|')[-1],str(i))
                mc.rename(oldCam,newCam)

    #-----------------------------------------#
    # 获取camera golden line grp
    def sk_camSeqGetNeedGoldenLineGrps(self,shotNode = '',turnOn = 0):
        keepCam = ''
        if shotNode:
            camCons = mc.listConnections('%s.currentCamera'%shotNode)
            if camCons:
                keepCam = camCons[0]
        allShotNodes = mc.ls(type = 'shot')
        for checkShotNode in allShotNodes:
            camCons = mc.listConnections('%s.currentCamera'%checkShotNode)
            if not camCons:
                continue
            camGrp = camCons[0]
            goldLineGrp = sk_camMatrixScene.cameraTools().getGoldenGrpFromCam(camGrp)
            if camGrp == keepCam :
                mc.setAttr('%s.v'%goldLineGrp,1)
            else:
                mc.setAttr('%s.v'%goldLineGrp,turnOn)

    # 隐藏camera
    def sk_camSeqHideShotCamera(self,shotNode = '',turnOn = 0):
        keepCam = ''
        if shotNode:
            camCons = mc.listConnections('%s.currentCamera'%shotNode)
            if camCons:
                keepCam = camCons[0]
        allShotNodes = mc.ls(type = 'shot')
        for checkShotNode in allShotNodes:
            camCons = mc.listConnections('%s.currentCamera'%checkShotNode)
            if not camCons:
                continue
            camGrp = camCons[0]
            if camGrp == keepCam :
                mc.setAttr('%s.v'%camGrp,1)
            else:
                mc.setAttr('%s.v'%camGrp,turnOn)

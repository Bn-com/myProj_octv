# -*- coding: utf-8 -*-

'''
Created on 2013-10-11

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel

class sk_ripple2DMaya(object):
    def __init__(self):
        # namespace清理
        print ''
    '''
            界面核心
    '''
    def sk_waveCircle2DMayaUI(self):
        # 窗口
        if mc.window ("sk_waveCircle2DMayaUI", ex=1):
            mc.deleteUI("sk_waveCircle2DMayaUI", window=True)
        mc.window("sk_waveCircle2DMayaUI", title="Wave2DTools", widthHeight=(170, 460), menuBar=0)
        
        # 获取源物
        mc.frameLayout(label=u'源物体选取', borderStyle='etchedOut' , width=265, height=50)
        mc.rowLayout(numberOfColumns=2, columnWidth2=(180, 90))
        mc.textField('sk_waveMoveSourceField', text='', width=180, height=25)
        mc.button(l=u'获取运动源物体', bgc=[0.1, 0.1, 0.1], width=90, height=25 , c='from idmt.maya.FxTools import sk_ripple2DMaya\nreload(sk_ripple2DMaya)\nsk_ripple2DMaya.sk_ripple2DMaya().sk_waveUIGetObj(\"move\")')
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=2, columnWidth2=(180, 90))
        mc.textField('sk_waveOceanSourceField', text='', width=180, height=25)
        mc.button(l=u'获取Ocean平面', bgc=[0.1, 0.1, 0.1], width=90, height=25, c='from idmt.maya.FxTools import sk_ripple2DMaya\nreload(sk_ripple2DMaya)\nsk_ripple2DMaya.sk_ripple2DMaya().sk_waveUIGetObj(\"ocean\")')
        mc.setParent('..')
        mc.setParent('..')

        # 面板开始
        mc.paneLayout(configuration='single', w=250, h=300)
        mc.scrollLayout()

        # 创建基础属性
        mc.frameLayout(label=u'基础设置', borderStyle='etchedOut' , width=250)
        # 半径
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'Mask半径', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveMRadiusField', v=5, width=50, height=20)
        mc.button(l=u'Wave半径', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveWRadiusField', v=7, width=50, height=20)
        mc.setParent('..')
        # 半径变量
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'M半径随机', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveMRadiusRandomField', v=0, width=50, height=20)
        mc.button(l=u'W半径随机', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveWRadiusRandomField', v=0, width=50, height=20)
        mc.setParent('..')
        # 分段数
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'Mask分段', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.intField('sk_waveMSegXField', v=50, width=50, height=20)
        mc.button(l=u'Wave分段', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.intField('sk_waveWSegXField', v=50, width=50, height=20)
        mc.setParent('..')
        mc.setParent('..')
        
        # noise变形
        mc.frameLayout(label=u'Noise变形参数', borderStyle='etchedOut' , width=250)
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'设置noise算法', width=70, height=20,bgc=[0.4, 0.4, 0.4])
        mc.intField('sk_waveNoiseTypeField', v=1, width=50, height=20)
        mc.button(l=u'', width=70, height=20)
        mc.button(l=u'', width=50, height=20)
        mc.setParent('..')
        # Type01
        mc.frameLayout(label=u'Noise 算法A', borderStyle='etchedOut' , width=250 , bgc=[0.2, 0.2, 0.2])
        # 半径
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'M最小随机', width=70, height=20 , bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveNoiseT1MinField', v=-0.1, width=50, height=20)
        mc.button(l=u'W最小随机', width=70, height=20 , bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveNoiseT1MinWField', v=-0.1, width=50, height=20)
        mc.setParent('..')
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'M最大随机', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveNoiseT1MaxField', v=0.3, width=50, height=20)
        mc.button(l=u'W最大随机', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveNoiseT1MaxWField', v=0.3, width=50, height=20)
        mc.setParent('..')
        mc.setParent('..')
        # Type02
        mc.frameLayout(label=u'Noise 算法B', cll=1, cl=1, borderStyle='etchedIn' , width=250 , bgc=[0.2, 0.2, 0.2])
        # 半径
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'M差异最小', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveNoiseT2MinScaleField', v=-0.1, width=50, height=20)
        mc.button(l=u'W差异最小', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveNoiseT2MinScaleWField', v=-0.1, width=50, height=20)
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'M差异最大', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveNoiseT2MaxScaleField', v=0.2, width=50, height=20)
        mc.button(l=u'W差异最大', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveNoiseT2MaxScaleWField', v=0.2, width=50, height=20)
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'M差异倍数', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveNoiseT2RandScaleField', v=2.0, width=50, height=20)
        mc.button(l=u'W差异倍数', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveNoiseT2RandScaleWField', v=2.0, width=50, height=20)
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'M浪纹缩放', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveNoiseT2NoiseScaleField', v=3, width=50, height=20)
        mc.button(l=u'W浪纹缩放', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveNoiseT2NoiseScaleWField', v=3, width=50, height=20)
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'M浪纹最小', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveNoiseT2NoiseScaleVMinField', v=0.1, width=50, height=20)
        mc.button(l=u'W浪纹最小', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveNoiseT2NoiseScaleVMinWField', v=0.1, width=50, height=20)
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'M浪纹最大', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveNoiseT2NoiseScaleVMaxField', v=0.2, width=50, height=20)
        mc.button(l=u'W浪纹最大', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveNoiseT2NoiseScaleVMaxWField', v=0.2, width=50, height=20)
        mc.setParent('..')
        mc.setParent('..')

        # 动画属性
        mc.frameLayout(label=u'泡泡参数', borderStyle='etchedOut' , width=250)
        mc.setParent('..')
        
        # 动画属性
        mc.frameLayout(label=u'动画设置', borderStyle='etchedOut',collapsable=1 , width=250)
        # 发射速率
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'波纹0|泡沫1', width=70, height=20,bgc=[0.0, 0.0, 0.0])
        mc.intField('sk_waveAnimTypeField', v=0, width=50, height=20)
        mc.button(l=u'发射间隔', width=70, height=20 ,bgc=[0.4, 0.4, 0.4])
        mc.floatField('sk_waveFrameRateField', v=2, width=50, height=20)
        mc.setParent('..')
        # 动画范围
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'起始帧', width=70, height=20 ,bgc=[0.4, 0.4, 0.4])
        mc.floatField('sk_waveFrameStartField', v=1, width=50, height=20)
        mc.button(l=u'结束帧', width=70, height=20 ,bgc=[0.4, 0.4, 0.4])
        mc.floatField('sk_waveFrameEndField', v=25, width=50, height=20)
        mc.setParent('..')
        # 范围偏移
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'X轴偏移Min', width=70, height=20,bgc=[0.4, 0.4, 0.4])
        mc.floatField('sk_waveXRandomMinField', v=1, width=50, height=20)
        mc.button(l=u'Z轴偏移Min', width=70, height=20,bgc=[0.4, 0.4, 0.4])
        mc.floatField('sk_waveZRandomMinField', v=1, width=50, height=20)
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'X轴偏移Max', width=70, height=20,bgc=[0.4, 0.4, 0.4])
        mc.floatField('sk_waveXRandomMaxField', v=5, width=50, height=20)
        mc.button(l=u'Z轴偏移Max', width=70, height=20,bgc=[0.4, 0.4, 0.4])
        mc.floatField('sk_waveZRandomMaxField', v=5, width=50, height=20)
        mc.setParent('..')
        # 成长时间
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'M基础高度', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveBaseHeightTypeField', v=0, width=50, height=20)
        mc.button(l=u'W基础高度', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveBaseHeightTypeWField', v=0, width=50, height=20)
        mc.setParent('..')
        # 成长时间
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'Mask变化', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveMGrowField', v=30, width=50, height=20)
        mc.button(l=u'Wave变化', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveWGrowField', v=10, width=50, height=20)
        mc.setParent('..')
        # 滞留时间
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'Mask滞留', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveMStayField', v=6, width=50, height=20)
        mc.button(l=u'Wave滞留', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveWStayField', v=5, width=50, height=20)
        mc.setParent('..')
        # 缩放值
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'Mask缩放', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveMScaleField', v=1.75, width=50, height=20)
        mc.button(l=u'Wave缩放', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveWScaleField', v=1.15, width=50, height=20)
        mc.setParent('..')
        # 停滞缩放值
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'Mask滞缩放', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveMStayScaleField', v=1.75, width=50, height=20)
        mc.button(l=u'Wave滞缩放', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveWStayScaleField', v=1.15, width=50, height=20)
        mc.setParent('..')
        mc.setParent('..')
        
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')

	#简单设置面板
	#新添加/hh
        mc.frameLayout(label=u'locator面板', borderStyle='etchedOut' ,collapsable=1, width=250)
	mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
	mc.button(l=u'Mask半径', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveMRadiusField01', v=50, width=50, height=20)
	mc.button(l=u'Wave半径', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveWRadiusField01', v=70, width=50, height=20)
	mc.setParent('..')
	# 动画范围
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'起始帧', width=70, height=20 ,bgc=[0.4, 0.4, 0.4])
        mc.floatField('sk_waveFrameStartField01', v=-20, width=50, height=20)
        mc.button(l=u'结束帧', width=70, height=20 ,bgc=[0.4, 0.4, 0.4])
        mc.floatField('sk_waveFrameEndField01', v=25, width=50, height=20)
        mc.setParent('..')
	mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'Mask变化', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveMGrowField01', v=30, width=50, height=20)
        mc.button(l=u'Wave变化', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveWGrowField01', v=10, width=50, height=20)
        mc.setParent('..')
        # 滞留时间
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'Mask滞留', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveMStayField01', v=6, width=50, height=20)
        mc.button(l=u'Wave滞留', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveWStayField01', v=5, width=50, height=20)
        mc.setParent('..')
        # 缩放值
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'Mask缩放', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveMScaleField01', v=1.75, width=50, height=20)
        mc.button(l=u'Wave缩放', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveWScaleField01', v=1.15, width=50, height=20)
        mc.setParent('..')
        # 停滞缩放值
        mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
        mc.button(l=u'Mask滞缩放', width=70, height=20, bgc=[0.1, 0.1, 0.1])
        mc.floatField('sk_waveMStayScaleField01', v=1.75, width=50, height=20)
        mc.button(l=u'Wave滞缩放', width=70, height=20, bgc=[0.3, 0.3, 0.3])
        mc.floatField('sk_waveWStayScaleField01', v=1.15, width=50, height=20)
	mc.setParent('..')
	mc.rowLayout(numberOfColumns=4, columnWidth4=(70 , 50, 70, 50))
	mc.button(label=u'参数设置' , bgc=[0.6, 0.1, 0.1], width=110 , height=30, c='from idmt.maya.FxTools import sk_ripple2DMaya\nreload(sk_ripple2DMaya)\nsk_ripple2DMaya.sk_ripple2DMaya().sk_waveLocator()')
	mc.setParent('..')
        mc.setParent('..')
        
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')

        # 执行按钮属性
        mc.frameLayout(label=u'==================================', borderStyle='etchedOut' , width=250 , height=70)
        mc.rowLayout(numberOfColumns=4, columnWidth4=(65, 65, 65, 65))
        mc.button(label=u'重建Noise' , width=65 , height=25, c='from idmt.maya.FxTools import sk_ripple2DMaya\nreload(sk_ripple2DMaya)\nsk_ripple2DMaya.sk_ripple2DMaya().sk_waveNoiseRebuild()')
        mc.button(label=u'清除选取系统' , width=65 , height=25 , c='from idmt.maya.FxTools import sk_ripple2DMaya\nreload(sk_ripple2DMaya)\nsk_ripple2DMaya.sk_ripple2DMaya().sk_waveCircleClean()')
        mc.button(label=u'输出浪纹方案' , width=65 , height=25, c='from idmt.maya.FxTools import sk_ripple2DMaya\nreload(sk_ripple2DMaya)\nsk_ripple2DMaya.sk_ripple2DMaya().sk_waveUIButtonCMD(-1,1,0)')
        mc.button(label=u'导入浪纹方案' , width=65 , height=25 , c='from idmt.maya.FxTools import sk_ripple2DMaya\nreload(sk_ripple2DMaya)\nsk_ripple2DMaya.sk_ripple2DMaya().sk_waveUIButtonCMD(-1,0,1)')
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=3, columnWidth3=(110 , 50 , 110))
        mc.button(label=u'平面2D涟漪创建' , bgc=[0.1, 0.5, 0.1], width=110 , height=30, c='from idmt.maya.FxTools import sk_ripple2DMaya\nreload(sk_ripple2DMaya)\nsk_ripple2DMaya.sk_ripple2DMaya().sk_waveUIButtonCMD(0)')
        mc.button(label=u'高度归零' , bgc=[0.3, 0.7, 0.1], width=50 , height=30, c='from idmt.maya.FxTools import sk_ripple2DMaya\nreload(sk_ripple2DMaya)\nsk_ripple2DMaya.sk_ripple2DMaya().sk_waveHeightClean()')
        mc.button(label=u'起伏2D涟漪创建' , bgc=[0.1, 0.4, 0.8], width=110 , height=30, c='from idmt.maya.FxTools import sk_ripple2DMaya\nreload(sk_ripple2DMaya)\nsk_ripple2DMaya.sk_ripple2DMaya().sk_waveUIButtonCMD(1)')
        mc.setParent('..')
        mc.setParent('..')
        
        mc.showWindow("sk_waveCircle2DMayaUI")
        
        
    # 获取物体
    def sk_waveUIGetObj(self, sourceType=''):
        obj = mc.ls(sl=1)[0]
        if sourceType == 'move':
            mc.textField('sk_waveMoveSourceField', text=obj, e=1)
        if sourceType == 'ocean':
            mc.textField('sk_waveOceanSourceField', text=obj, e=1)
            
    # 执行
    def sk_waveUIButtonCMD(self, animType=0 , export=0 , im=0):
        # 参数处理
        # 物体获取
        objMove = mc.textField('sk_waveMoveSourceField', text=1, q=1)
        objOcean = mc.textField('sk_waveOceanSourceField', text=1, q=1)
        
        # 创建设置
        radiusM = mc.floatField('sk_waveMRadiusField', v=1, q=1)
        radiusW = mc.floatField('sk_waveWRadiusField', v=1, q=1)
        radiusMrandom = mc.floatField('sk_waveMRadiusRandomField', v=1, q=1)
        radiusWrandom = mc.floatField('sk_waveWRadiusRandomField', v=1, q=1)
        segM = mc.intField('sk_waveMSegXField', v=1, q=1)
        segW = mc.intField('sk_waveWSegXField', v=1, q=1)

        # noise参数
        noiseType = mc.intField('sk_waveNoiseTypeField', v=1 , q=1)
        t1Min = mc.floatField('sk_waveNoiseT1MinField', v=1, q=1)
        t1Max = mc.floatField('sk_waveNoiseT1MaxField', v=1, q=1)
        t1MinW = mc.floatField('sk_waveNoiseT1MinWField', v=1, q=1)
        t1MaxW = mc.floatField('sk_waveNoiseT1MaxWField', v=1, q=1)
        t2MinScale = mc.floatField('sk_waveNoiseT2MinScaleField', v=1, q=1)
        t2MaxScale = mc.floatField('sk_waveNoiseT2MaxScaleField', v=1, q=1)
        t2RandScale = mc.floatField('sk_waveNoiseT2RandScaleField', v=1, q=1)
        t2NoiseScale = mc.floatField('sk_waveNoiseT2NoiseScaleField', v=1, q=1)
        t2NoiseScaleVMin = mc.floatField('sk_waveNoiseT2NoiseScaleVMinField', v=1, q=1)
        t2NoiseScaleVMax = mc.floatField('sk_waveNoiseT2NoiseScaleVMaxField', v=1, q=1)
        t2MinScaleW = mc.floatField('sk_waveNoiseT2MinScaleWField', v=1, q=1)
        t2MaxScaleW = mc.floatField('sk_waveNoiseT2MaxScaleWField', v=1, q=1)
        t2RandScaleW = mc.floatField('sk_waveNoiseT2RandScaleWField', v=1, q=1)
        t2NoiseScaleW = mc.floatField('sk_waveNoiseT2NoiseScaleWField', v=1, q=1)
        t2NoiseScaleVMinW = mc.floatField('sk_waveNoiseT2NoiseScaleVMinWField', v=1, q=1)
        t2NoiseScaleVMaxW = mc.floatField('sk_waveNoiseT2NoiseScaleVMaxWField', v=1, q=1)
        
        # 动画参数
        animRate = mc.floatField('sk_waveFrameRateField', v=1, q=1)
        frameStart = mc.floatField('sk_waveFrameStartField', v=1, q=1)
        frameEnd = mc.floatField('sk_waveFrameEndField', v=1, q=1)
        XrandMin = mc.floatField('sk_waveXRandomMinField', v=1, q=1)
        XrandMax = mc.floatField('sk_waveXRandomMaxField', v=1, q=1)
        ZrandMin = mc.floatField('sk_waveZRandomMinField', v=1, q=1)
        ZrandMax = mc.floatField('sk_waveZRandomMaxField', v=1, q=1)
        growTimeM = mc.floatField('sk_waveMGrowField', v=1, q=1)
        growTimeW = mc.floatField('sk_waveWGrowField', v=1, q=1)
        stayTimeM = mc.floatField('sk_waveMStayField', v=1, q=1)
        stayTimeW = mc.floatField('sk_waveWStayField', v=1, q=1)
        scaleM = mc.floatField('sk_waveMScaleField', v=1, q=1)
        scaleW = mc.floatField('sk_waveWScaleField', v=1, q=1)
        stayScaleM = mc.floatField('sk_waveMStayScaleField', v=1, q=1)
        stayScaleW = mc.floatField('sk_waveWStayScaleField', v=1, q=1)
        baseHeight = mc.floatField('sk_waveBaseHeightTypeField', v=1, q=1)
        baseHeightW = mc.floatField('sk_waveBaseHeightTypeWField', v=1, q=1)
        
        # 波纹|泡沫
        createType = mc.intField('sk_waveAnimTypeField' , v=1 , q=1)
        if createType == 0:
            animInfoTxt = '_wave_'
        if createType == 1:
            animInfoTxt = '_foam_'   
        
        # info
        objInfo = [objMove, objOcean]
        circleInfo = [[radiusM, radiusMrandom, segM], [radiusW, radiusWrandom, segW]]
        noiseInfo = [noiseType, [[t1Min, t1Max], [t1MinW, t1MaxW]], [[t2RandScale, t2MinScale, t2MaxScale, t2NoiseScale, t2NoiseScaleVMin, t2NoiseScaleVMax], [t2RandScaleW, t2MinScaleW, t2MaxScaleW, t2NoiseScaleW, t2NoiseScaleVMinW, t2NoiseScaleVMaxW]]]
        animInfo = [[[XrandMin, XrandMax], [ZrandMin, ZrandMax]], growTimeM, growTimeW, stayTimeM, stayTimeW, scaleM, scaleW, stayScaleM, stayScaleW, [baseHeight, baseHeightW]]
        frameInfo = [animRate, frameStart, frameEnd]
        if animType == 0:
            self.sk_waveSceneAnimPlane(objInfo , animInfo , frameInfo, circleInfo, noiseInfo , createType)
        if animType == 1:
            self.sk_waveSceneAnimMayaOcean(objOcean)
        if export == 1:
            if objMove:
                from idmt.maya.py_common import sk_checkCommon
                reload(sk_checkCommon)
                animInfo.append(createType)
                allInfo = [objInfo, circleInfo, noiseInfo, animInfo, frameInfo]
                local2DRippleInfoPath = ('D:/Info_Temp/2DRippleInfo/')
                mc.sysFile(local2DRippleInfoPath, makeDir=True)
                sk_checkCommon.sk_checkTools().checkFileWrite((local2DRippleInfoPath + objMove + animInfoTxt + '_2DSYS.txt'), allInfo)
                print u'===================System【%s】成功导出===================' % objMove
            else:
                print u'===================没有源运动物体，无法导出==================='
        if im == 1:
            if objMove:
                from idmt.maya.py_common import sk_checkCommon
                reload(sk_checkCommon)
                local2DRippleInfoPath = ('D:/Info_Temp/2DRippleInfo/')
                import os
                if os.path.exists(local2DRippleInfoPath + objMove + animInfoTxt + '_2DSYS.txt'):
                    allInfo = sk_checkCommon.sk_checkTools().checkFileRead((local2DRippleInfoPath + objMove + animInfoTxt + '_2DSYS.txt'))
                    # oceanObj
                    objOcean = allInfo[0].split(',')[1]
                    if objOcean[2] == '\'':
                        objOcean = ''
                    else:
                        objOcean = objOcean[2:-1]
                    mc.textField('sk_waveOceanSourceField', text=objOcean, e=1)
                    # circleInfo
                    circleMInfo = allInfo[1].split('], [')[0][2:]
                    circleWInfo = allInfo[1].split('], [')[1][0:-2]
                    radiusM = circleMInfo.split(', ')[0]
                    radiusMrandom = circleMInfo.split(', ')[1]
                    segM = circleMInfo.split(', ')[2]
                    mc.floatField('sk_waveMRadiusField', v=float(radiusM), e=1)
                    mc.floatField('sk_waveMRadiusRandomField', v=float(radiusMrandom), e=1)
                    mc.intField('sk_waveMSegXField', v=float(segM), e=1)
                    radiusW = circleWInfo.split(', ')[0]
                    radiusWrandom = circleWInfo.split(', ')[1]
                    segW = circleWInfo.split(', ')[2]
                    mc.floatField('sk_waveWRadiusField', v=float(radiusM), e=1)
                    mc.floatField('sk_waveWRadiusRandomField', v=float(radiusMrandom), e=1)
                    mc.intField('sk_waveWSegXField', v=float(segM), e=1)
                    # noiseInfo
                    noiseInfo = allInfo[2].split(', ')
                    noiseType = noiseInfo[0][1:]
                    mc.intField('sk_waveNoiseTypeField', v=int(noiseType) , e=1)
                    t1MinM = noiseInfo[1][2:]
                    t1MaxM = noiseInfo[2][0:-1]
                    t1MinW = noiseInfo[3][1:]
                    t1MaxW = noiseInfo[4][0:-2]
                    mc.floatField('sk_waveNoiseT1MinField', v=float(t1MinM), e=1)
                    mc.floatField('sk_waveNoiseT1MaxField', v=float(t1MaxM), e=1)
                    mc.floatField('sk_waveNoiseT1MinWField', v=float(t1MinW), e=1)
                    mc.floatField('sk_waveNoiseT1MaxWField', v=float(t1MaxW), e=1)
                    t2RandScaleM = noiseInfo[5][2:]
                    t2MinScaleM = noiseInfo[6]
                    t2MaxScaleM = noiseInfo[7]
                    t2NoiseScaleM = noiseInfo[8]
                    t2NoiseScaleVMinM = noiseInfo[6]
                    t2NoiseScaleVMaxM = noiseInfo[10][0:-1]
                    t2RandScaleW = noiseInfo[11][1:]
                    t2MinScaleW = noiseInfo[12]
                    t2MaxScaleW = noiseInfo[13]
                    t2NoiseScaleW = noiseInfo[14]
                    t2NoiseScaleVMinW = noiseInfo[15]
                    t2NoiseScaleVMaxW = noiseInfo[16][0:-3]
                    mc.floatField('sk_waveNoiseT2MinScaleField', v=float(t2MinScaleM), e=1)
                    mc.floatField('sk_waveNoiseT2MaxScaleField', v=float(t2MaxScaleM), e=1)
                    mc.floatField('sk_waveNoiseT2RandScaleField', v=float(t2RandScaleM), e=1)
                    mc.floatField('sk_waveNoiseT2NoiseScaleField', v=float(t2NoiseScaleM), e=1)
                    mc.floatField('sk_waveNoiseT2NoiseScaleVMinField', v=float(t2NoiseScaleVMinM), e=1)
                    mc.floatField('sk_waveNoiseT2NoiseScaleVMaxField', v=float(t2NoiseScaleVMaxM), e=1)
                    mc.floatField('sk_waveNoiseT2MinScaleWField', v=float(t2MinScaleW), e=1)
                    mc.floatField('sk_waveNoiseT2MaxScaleWField', v=float(t2MaxScaleW), e=1)
                    mc.floatField('sk_waveNoiseT2RandScaleWField', v=float(t2RandScaleW), e=1)
                    mc.floatField('sk_waveNoiseT2NoiseScaleWField', v=float(t2NoiseScaleW), e=1)
                    mc.floatField('sk_waveNoiseT2NoiseScaleVMinWField', v=float(t2NoiseScaleVMinW), e=1)
                    mc.floatField('sk_waveNoiseT2NoiseScaleVMaxWField', v=float(t2NoiseScaleVMaxW), e=1)
                    # animInfo 
                    animInfo = allInfo[3].split(', ')
                    XrandMin = animInfo[0][3:]
                    XrandMax = animInfo[1][:-1]
                    ZrandMin = animInfo[2][1:]
                    ZrandMax = animInfo[3][:-2]
                    growTimeM = animInfo[4]
                    growTimeW = animInfo[5]
                    stayTimeM = animInfo[6]
                    stayTimeW = animInfo[7]
                    scaleM = animInfo[8]
                    scaleW = animInfo[9]
                    stayScaleM = animInfo[10]
                    stayScaleW = animInfo[11]
                    baseHeight = animInfo[12][1:]
                    baseHeightW = animInfo[13][:-1]
                    animType = animInfo[14][:-1]
                    mc.floatField('sk_waveXRandomMinField', v=float(XrandMin), e=1)
                    mc.floatField('sk_waveXRandomMaxField', v=float(XrandMax), e=1)
                    mc.floatField('sk_waveZRandomMinField', v=float(ZrandMax), e=1)
                    mc.floatField('sk_waveZRandomMaxField', v=float(stayTimeW), e=1)
                    mc.floatField('sk_waveMGrowField', v=float(growTimeM), e=1)
                    mc.floatField('sk_waveWGrowField', v=float(growTimeW), e=1)
                    mc.floatField('sk_waveMStayField', v=float(stayTimeM), e=1)
                    mc.floatField('sk_waveWStayField', v=float(stayTimeW), e=1)
                    mc.floatField('sk_waveMScaleField', v=float(scaleM), e=1)
                    mc.floatField('sk_waveWScaleField', v=float(scaleW), e=1)
                    mc.floatField('sk_waveMStayScaleField', v=float(stayScaleM), e=1)
                    mc.floatField('sk_waveWStayScaleField', v=float(stayScaleW), e=1)
                    mc.floatField('sk_waveBaseHeightTypeField', v=float(baseHeight), e=1)
                    mc.floatField('sk_waveBaseHeightTypeWField', v=float(baseHeightW), e=1)
                    mc.intField('sk_waveAnimTypeField', v=int(animType), e=1)
                    # frameInfo
                    frameInfo = allInfo[4].split(', ')
                    animRate = frameInfo[0][1:]
                    frameStart = frameInfo[1]
                    frameEnd = frameInfo[2][0:-1]
                    mc.floatField('sk_waveFrameRateField', v=float(animRate), e=1)
                    mc.floatField('sk_waveFrameStartField', v=float(frameStart), e=1)
                    mc.floatField('sk_waveFrameEndField', v=float(frameEnd), e=1)
                    print u'===================System【%s】成功导入===================' % objMove
                else:
                    print u'===================该系统信息文件不存在==================='
            else:
                print u'===================没有源运动物体，无法导入==================='
    
    
    # 高度归零
    def sk_waveHeightClean(self):
        shapes = mc.ls(type = 'clusterHandle')
        for shape in shapes:
            if 'FoodWaveCluster' in shape or 'FoodFoamCluster' in shape:
                obj = mc.listRelatives(shape,p=1,type = 'transform')
                if obj:
                    obj = obj[0]
                    mc.setAttr((obj + '.ty'),0)
        
        
        
    # 重建noise效果
    def sk_waveNoiseRebuild(self):
        objMove = mc.textField('sk_waveMoveSourceField', text=1, q=1)
        noiseType = mc.intField('sk_waveNoiseTypeField', v=1 , q=1)
        t1Min = mc.floatField('sk_waveNoiseT1MinField', v=1, q=1)
        t1Max = mc.floatField('sk_waveNoiseT1MaxField', v=1, q=1)
        t1MinW = mc.floatField('sk_waveNoiseT1MinWField', v=1, q=1)
        t1MaxW = mc.floatField('sk_waveNoiseT1MaxWField', v=1, q=1)
        t2MinScale = mc.floatField('sk_waveNoiseT2MinScaleField', v=1, q=1)
        t2MaxScale = mc.floatField('sk_waveNoiseT2MaxScaleField', v=1, q=1)
        t2RandScale = mc.floatField('sk_waveNoiseT2RandScaleField', v=1, q=1)
        t2NoiseScale = mc.floatField('sk_waveNoiseT2NoiseScaleField', v=1, q=1)
        t2NoiseScaleVMin = mc.floatField('sk_waveNoiseT2NoiseScaleVMinField', v=1, q=1)
        t2NoiseScaleVMax = mc.floatField('sk_waveNoiseT2NoiseScaleVMaxField', v=1, q=1)
        t2MinScaleW = mc.floatField('sk_waveNoiseT2MinScaleWField', v=1, q=1)
        t2MaxScaleW = mc.floatField('sk_waveNoiseT2MaxScaleWField', v=1, q=1)
        t2RandScaleW = mc.floatField('sk_waveNoiseT2RandScaleWField', v=1, q=1)
        t2NoiseScaleW = mc.floatField('sk_waveNoiseT2NoiseScaleWField', v=1, q=1)
        t2NoiseScaleVMinW = mc.floatField('sk_waveNoiseT2NoiseScaleVMinWField', v=1, q=1)
        t2NoiseScaleVMaxW = mc.floatField('sk_waveNoiseT2NoiseScaleVMaxWField', v=1, q=1)
      
        noiseT1Setting = [[t1Min, t1Max], [t1MinW, t1MaxW]]
        noiseT2Setting = [[t2RandScale, t2MinScale, t2MaxScale, t2NoiseScale, t2NoiseScaleVMin, t2NoiseScaleVMax], [t2RandScaleW, t2MinScaleW, t2MaxScaleW, t2NoiseScaleW, t2NoiseScaleVMinW, t2NoiseScaleVMaxW]]
        # 获取系统物体
        objsM = []
        objsW = []

        if mc.objExists('FoodWave_' + objMove + '_SYS'):
            if mc.objExists('FoodWave_M_' + objMove + '_GRP'):
                objs = mc.listRelatives(('FoodWave_M_' + objMove + '_GRP'), c=1, type='transform')
                if objs:
                    for obj in objs:
                        if 'FoodWaveMesh' in obj:
                            objsM.append(obj)
            if mc.objExists('FoodWave_W_' + objMove + '_GRP'):
                objs = mc.listRelatives(('FoodWave_W_' + objMove + '_GRP'), c=1, type='transform')
                if objs:
                    for obj in objs:
                        if 'FoodWaveMesh' in obj:
                            objsW.append(obj)
        if objsM:
            for obj in objsM:
                clusterObjM = obj.replace('Mesh', 'Cluster')[0:-1]
                sx = mc.getAttr(clusterObjM + '.sx')
                sy = mc.getAttr(clusterObjM + '.sy')
                sz = mc.getAttr(clusterObjM + '.sz')
                mc.setAttr((clusterObjM + '.sx'), 1)
                mc.setAttr((clusterObjM + '.sy'), 1)
                mc.setAttr((clusterObjM + '.sz'), 1)
                self.sk_waveCircleNoise(obj, noiseType, noiseT1Setting, noiseT2Setting)
                mc.setAttr((clusterObjM + '.sx'), sx)
                mc.setAttr((clusterObjM + '.sy'), sy)
                mc.setAttr((clusterObjM + '.sz'), sz)
        if objsW:
            for obj in objsW:
                clusterObjW = obj.replace('Mesh', 'Cluster')[0:-1]
                sx = mc.getAttr(clusterObjW + '.sx')
                sy = mc.getAttr(clusterObjW + '.sy')
                sz = mc.getAttr(clusterObjW + '.sz')
                mc.setAttr((clusterObjW + '.sx'), 1)
                mc.setAttr((clusterObjW + '.sy'), 1)
                mc.setAttr((clusterObjW + '.sz'), 1)
                self.sk_waveCircleNoise(obj, noiseType, noiseT1Setting, noiseT2Setting)
                mc.setAttr((clusterObjW + '.sx'), sx)
                mc.setAttr((clusterObjW + '.sy'), sy)
                mc.setAttr((clusterObjW + '.sz'), sz)

    
    # 删除选取源系统
    def sk_waveCircleClean(self):
        objMove = mc.textField('sk_waveMoveSourceField', text=1, q=1)
        if mc.objExists('FoodWave_' + objMove + '_SYS'):
            mc.delete('FoodWave_' + objMove + '_SYS')
    
    '''
            创建状态核心,mask存活时间要比wave时间长
    '''
    # 核心，圆盘
    def sk_waveCircleCreate(self , id , radius=10 , radiusRand=0 , segX=40 , createType=0 , randInfo=[0, 0]):
        # 创建
        import random
        # createType
        if createType == 0:
            preInfo = 'FoodWaveMesh_'
            preInfoC = 'FoodWaveCluster_'
            preInfoCNew = 'FoodWaveC_'
        if createType == 1:
            preInfo = 'FoodFoamMesh_'
            preInfoC = 'FoodFoamCluster_'
            preInfoCNew = 'FoodFoamC_'
            
        randomInfo = 0
        if radiusRand:
            if randInfo[0] == 0:
                randomInfo = random.uniform(0, radiusRand)
            if randInfo[0] == 1:
                randomInfo = randInfo[1]
            obj = mc.polyCylinder(r=(radius + randomInfo) , sx=segX , sy=1 , sz=1, h=0)
        else:
            obj = mc.polyCylinder(r=(radius) , sx=segX , sy=1 , sz=1, h=0)
        obj = obj[0]
        mc.delete(obj + '.f[0:' + str(segX * 2 - 1) + ']')
        # 重命名
        newName = preInfo + id
        if mc.objExists(newName):
            mc.delete(newName)
        mc.rename(obj, newName)
        # 删历史
        mc.select(newName)
        mel.eval('DeleteHistory')
        mc.select(cl=1)
        # smooth显示
        mc.setAttr((mc.listRelatives(newName, s=1, ni=1, type='mesh')[0] + '.displaySmoothMesh'), 2)
        # 创建簇      
        if mc.objExists(preInfoC + id):
            mc.delete(preInfoC + id)
        mc.select(newName)
        mc.cluster(name=(preInfoCNew + id))
        clusterNewName = (preInfoC + id)[0:-1]
        mc.rename((preInfoCNew + id + 'Handle'), clusterNewName)
        mc.setAttr((clusterNewName + '.v'), 0)
        mc.select(cl=1)
        return randomInfo
        
    # 核心，物体与水面交界处的线
    # 。。。这个物体还是手动创建吧
    # 第一帧创建，然后获取master大环的值进行位移，旋转
    def sk_waveMasterCreate(self):   
        startFrame = mc.playbackOptions(q=1, min=1) 
        mc.currentTime(startFrame)
        
    
    # 核心，圆圈noise
    def sk_waveCircleNoise(self, sourceCircle, noiseType=1, setT1=[] , setT2=[]):
        import math
        import random
        # 获取点信息，除了最后一点，其他都是需要处理的
        pointNum = mc.polyEvaluate(sourceCircle, vertex=1)
        # noise方案1
        if noiseType == 1:
            t1RandMin = setT1[0]
            t1RandMax = setT1[1]
            centerPointOG = mc.pointPosition((sourceCircle + '.pt[' + str(pointNum - 1) + ']'), w=1)
            for i in range(pointNum - 1):
                # 获取点信息
                pointOG = mc.pointPosition((sourceCircle + '.pt[' + str(i) + ']'), w=1)
                # 进行扭曲
                baseNoise = random.uniform(t1RandMin, t1RandMax)
                tx = (pointOG[0] - centerPointOG[0]) * baseNoise + pointOG[0]
                baseNoise = random.uniform(t1RandMin, t1RandMax)
                tz = (pointOG[2] - centerPointOG[2]) * baseNoise + pointOG[2]
                # move算法
                mc.select(sourceCircle + '.pt[' + str(i) + ']')
                mc.move(tx, 0, tz)
                # 这里的set是属性额外增加
                # mc.setAttr((sourceCircle + '.pt[' + str(i) + ']'), tx, 0, tz, type='double3')
            mc.select(cl=1)
        
        # noise方案2
        if noiseType == 2:
            # 浪纹差异起始值
            t2RandScale = setT2[0]
            # 浪纹差异
            t2RandMin = setT2[1]
            t2RandMax = setT2[2]
            # 浪纹间隔
            t2NoiseScale = setT2[3]
            # 浪纹深度
            t2NoiseScaleVMin = setT2[4]
            t2NoiseScaleVMax = setT2[5]
            # 获取index
            centerPointOG = mc.pointPosition((sourceCircle + '.pt[' + str(pointNum - 1) + ']'), w=1)
            indexRand = t2RandScale * random.uniform(t2RandMin, t2RandMax)
            print indexRand
            for i in range(pointNum - 1):
                # 获取点信息
                pointOG = mc.pointPosition((sourceCircle + '.pt[' + str(i) + ']'), w=1)
                t2NoiseScaleV = random.uniform(t2NoiseScaleVMin, t2NoiseScaleVMax)
                # 进行扭曲
                baseNoise = t2NoiseScaleV * mel.eval('noise(' + str((indexRand + t2NoiseScale * i) / t2RandScale) + ')')
                tx = (pointOG[0] - centerPointOG[0]) * baseNoise + pointOG[0]
                tz = (pointOG[2] - centerPointOG[2]) * baseNoise + pointOG[2]
                # move算法
                mc.select(sourceCircle + '.pt[' + str(i) + ']')
                mc.move(tx, 0, tz)
                # 这里的set是属性额外增加
                # mc.setAttr((sourceCircle + '.pt[' + str(i) + ']'), tx, pointOG[1], tz, type='double3')
            mc.select(cl=1)
                
    # 创建材质球
    def sk_waveShaderCreate(self):
        # wave
        if mc.objExists('SHD_FoodWave'):
            mc.delete('SHD_FoodWave')
        if mc.objExists('SHD_FoodWave_SG'):
            mc.delete('SHD_FoodWave_SG')
        waveShader = mc.shadingNode ('surfaceShader', asShader=True, name='SHD_FoodWave')    
        mc.setAttr(('%s.outColor') % (waveShader), 1, 1, 1, type="double3")
        waveSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='SHD_FoodWave_SG')
        mc.connectAttr(('%s.%s') % (waveShader , 'outColor') , ('%s.%s') % (waveSG , 'surfaceShader'), f=True)
        # foam
        if mc.objExists('SHD_FoodFoam'):
            mc.delete('SHD_FoodFoam')
        if mc.objExists('SHD_FoodFoam_SG'):
            mc.delete('SHD_FoodFoam_SG')
        waveShader = mc.shadingNode ('surfaceShader', asShader=True, name='SHD_FoodFoam')    
        mc.setAttr(('%s.outColor') % (waveShader), 0.8, 0.8, 0.8, type="double3")
        waveSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='SHD_FoodFoam_SG')
        mc.connectAttr(('%s.%s') % (waveShader , 'outColor') , ('%s.%s') % (waveSG , 'surfaceShader'), f=True)
        # mask
        if mc.objExists('SHD_FoodMask'):
            mc.delete('SHD_FoodMask')
        if mc.objExists('SHD_FoodMask_SG'):
            mc.delete('SHD_FoodMask_SG')
        maskShader = mc.shadingNode ('surfaceShader', asShader=True, name='SHD_FoodMask')    
        mc.setAttr(('%s.outColor') % (maskShader), 0, 0, 0, type="double3")
        maskSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='SHD_FoodMask_SG')
        mc.connectAttr(('%s.%s') % (maskShader , 'outColor') , ('%s.%s') % (maskSG , 'surfaceShader'), f=True)
    
    # 着色
    def sk_waveShader2Objs(self):
        maskObjs = mc.ls('*FoodWaveMesh_M_*', type='transform')
        if maskObjs:
            if mc.objExists('SHD_FoodMask_SG'):
                mc.sets(maskObjs, e=1, forceElement='SHD_FoodMask_SG')    
        waveObjs = mc.ls('*FoodWaveMesh_W_*', type='transform')
        if waveObjs:
            if mc.objExists('SHD_FoodWave_SG'):
                mc.sets(waveObjs, e=1, forceElement='SHD_FoodWave_SG')  
        MaskObjs = mc.ls('*FoodFoamMesh_M_*', type='transform')
        if MaskObjs:
            if mc.objExists('SHD_FoodMask_SG'):
                mc.sets(MaskObjs, e=1, forceElement='SHD_FoodMask_SG')    
        foamObjs = mc.ls('*FoodFoamMesh_W_*', type='transform')
        if foamObjs:
            if mc.objExists('SHD_FoodFoam_SG'):
                mc.sets(foamObjs, e=1, forceElement='SHD_FoodFoam_SG')  

    '''
            创建动画核心
    '''
                
    # 发射器
    # frameInfo      [发射频率，起始帧，结束帧]
    # circleInfo     [半径，半径随机值，分段数]
    def sk_waveSceneEmitter(self, systemID, frameInfo=[1, 1, 20], circleInfoM=[10, 0, 40], circleInfoW=[12, 0, 40], noiseInfo=[1, [[-0.1, 0.3], [-0.1, 0.3]], [[], []]] , createType=0):
        import math
        # 参数分解
        # frameInfo
        waveRate = frameInfo[0]
        frameStart = frameInfo[1]
        frameEned = frameInfo[2]
        # circleInfoM
        circleRadiusM = circleInfoM[0]
        cirCleRadiusRandomM = circleInfoM[1]
        circleSegmentM = circleInfoM[2]
        # circleInfoW
        circleRadiusW = circleInfoW[0]
        cirCleRadiusRandomW = circleInfoW[1]
        circleSegmentW = circleInfoW[2]
        # noiseInfo
        noiseType = noiseInfo[0]
        t1SettingM = noiseInfo[1][0]
        t1SettingW = noiseInfo[1][1]
        t2SettingM = noiseInfo[2][0]
        t2SettingW = noiseInfo[2][1]
        # createType
        if createType == 0:
            preInfoM = 'FoodWave_M_'
            preInfoW = 'FoodWave_W_'
            preInfoMeshM = 'FoodWaveMesh_M_'
            preInfoMeshW = 'FoodWaveMesh_W_'
            preInfoFoamM = 'FoodWaveCluster_M_'
            preInfoFoamW = 'FoodWaveCluster_W_'
        if createType == 1:
            preInfoM = 'FoodFoam_M_'
            preInfoW = 'FoodFoam_W_'
            preInfoMeshM = 'FoodFoamMesh_M_'
            preInfoMeshW = 'FoodFoamMesh_W_'
            preInfoFoamM = 'FoodFoamCluster_M_'
            preInfoFoamW = 'FoodFoamCluster_W_'
        # 分组
        self.sk_waveAddVFXGrp(systemID , createType)

        MGrp = (preInfoM + systemID + '_GRP')
        WGrp = (preInfoW + systemID + '_GRP')
        # 创建物体
        waveNum = math.ceil((frameEned - frameStart + 1) / waveRate)
        for i in range(waveNum):
            if createType == 0:
                # 创建
                self.sk_waveCircleCreate(('M_' + str(i) + '_' + systemID + '_'), circleRadiusM, cirCleRadiusRandomM, circleSegmentM)
                mc.parent((preInfoMeshM + str(i) + '_' + systemID + '_'), MGrp)
                self.sk_waveCircleCreate(('W_' + str(i) + '_' + systemID + '_'), circleRadiusW, cirCleRadiusRandomW, circleSegmentW)
                mc.parent((preInfoMeshW + str(i) + '_' + systemID + '_'), WGrp)
            if createType == 1:
                randomInfo = self.sk_waveCircleCreate(('M_' + str(i) + '_' + systemID + '_'), radius=circleRadiusM, radiusRand=cirCleRadiusRandomM, segX=circleSegmentM , createType=1)
                mc.parent((preInfoMeshM + str(i) + '_' + systemID + '_'), MGrp)
                self.sk_waveCircleCreate(('W_' + str(i) + '_' + systemID + '_'), radius=circleRadiusW, segX=circleSegmentW, createType=1 , randInfo=[1, randomInfo])
                mc.parent((preInfoMeshW + str(i) + '_' + systemID + '_'), WGrp)
            # noise
            self.sk_waveCircleNoise((preInfoMeshM + str(i) + '_' + systemID + '_'), noiseType, t1SettingM, t2SettingM)
            self.sk_waveCircleNoise((preInfoMeshW + str(i) + '_' + systemID + '_'), noiseType, t1SettingW, t2SettingW)
        # 让polygon在一起
        for i in range(waveNum):
            mc.parent((preInfoFoamM + str(i) + '_' + systemID), MGrp)
            mc.parent((preInfoFoamW + str(i) + '_' + systemID), WGrp)
        
    # 处理VFX组
    def sk_waveAddVFXGrp(self, systemID , createType=0):
        if createType == 0:
            preInfoM = 'FoodWave_M_'
            preInfoW = 'FoodWave_W_'
            preInfoSys = 'FoodWave_'
        if createType == 1:
            preInfoM = 'FoodFoam_M_'
            preInfoW = 'FoodFoam_W_'
            preInfoSys = 'FoodFoam_'
        
        # 分组
        if mc.objExists(preInfoSys + systemID + '_SYS'):
            mc.delete(preInfoSys + systemID + '_SYS')
        waveSys = mc.group(name=(preInfoSys + systemID + '_SYS'), em=1)
        if mc.objExists(preInfoM + systemID + '_GRP'):
            mc.delete(preInfoM + systemID + '_GRP')
        MGrp = mc.group(name=(preInfoM + systemID + '_GRP'), em=1)
        if mc.objExists(preInfoW + systemID + '_GRP'):
            mc.delete(preInfoW + systemID + '_GRP')
        WGrp = mc.group(name=(preInfoW + systemID + '_GRP'), em=1)
        # 检测VFX和OTCGRP
        # VFX_GRP
        if mc.objExists('VFX_GRP'):
            vfxGrp = 'VFX_GRP'
        else:
            vfxGrp = mc.group(em=1, name='VFX_GRP')
        # OTC_GRP
        if mc.objExists('OTC_GRP'):
            otcGrp = 'OTC_GRP'
        else:
            otcGrp = mc.group(em=1, name='OTC_GRP')
        # 打组
        if otcGrp not in mc.ls(vfxGrp, l=1)[0]:
            mc.parent(vfxGrp, otcGrp)
        if vfxGrp not in mc.ls(waveSys, l=1)[0]:
            mc.parent(waveSys, vfxGrp)
        if waveSys not in mc.ls(MGrp, l=1)[0]:
            mc.parent(MGrp, waveSys)
        if waveSys not in mc.ls(WGrp, l=1)[0]:
            mc.parent(WGrp, waveSys)
            
    # wave跟随动画
    def sk_waveSceneAnimPlane(self, objInfo=['followObj', 'oceanObj'] , animInfo=[[[0, 0], [0, 0]], 30, 20, 7, 5, 1.5, 1.15, 1.5, 1.15, [0, 0]] , frameInfo=[2, 1, 50], circleInfo=[[4, 0, 40], [6, 0, 40]], noiseInfo=[1, [[-0.1, 0.3], [-0.1, 0.3]], [[], []]] , createType=0):
        # 获取信息
        # obj信息
        followObj = objInfo[0]
        oceanObj = objInfo[1]
        # frameInfo
        waveRate = frameInfo[0]
        frameStart = frameInfo[1]
        frameEned = frameInfo[2]
        # circleInfo
        circleRadiusM = circleInfo[0][0]
        cirCleRadiusRandomM = circleInfo[0][1]
        circleSegmentM = circleInfo[0][2]
        circleRadiusW = circleInfo[1][0]
        cirCleRadiusRandomW = circleInfo[1][1]
        circleSegmentW = circleInfo[1][2]
        # noiseInfo
        noiseType = noiseInfo[0]
        t1Setting = noiseInfo[1]
        t2Setting = noiseInfo[2]
        # animInfo
        # 存活时间,帧数
        XrandMin = animInfo[0][0][0]
        XrandMax = animInfo[0][0][1]
        ZrandMin = animInfo[0][1][0]
        ZrandMax = animInfo[0][1][1]
        print ZrandMax
        growTimeM = animInfo[1]
        growTimeW = animInfo[2]
        stayTimeM = animInfo[3]
        stayTimeW = animInfo[4]
        scaleMaxM = animInfo[5]
        scaleMaxW = animInfo[6]
        stayeScaleMaxM = animInfo[7]
        stayeScaleMaxW = animInfo[8]
        heightInfo = animInfo[9][0]
        heightInfoW = animInfo[9][1]
        # 创建好物体
        self.sk_waveSceneEmitter(followObj, frameInfo, circleInfo[0], circleInfo[1], noiseInfo , createType)
        # 材质及着色
        self.sk_waveShaderCreate()
        self.sk_waveShader2Objs()
        # 前缀名
        if createType == 0:
            preCtrlM = 'FoodWaveCluster_M_'
            preCtrlW = 'FoodWaveCluster_W_'
            preMeshM = 'FoodWaveMesh_M_'
            preMeshW = 'FoodWaveMesh_W_'
        if createType == 1:
            preCtrlM = 'FoodFoamCluster_M_'
            preCtrlW = 'FoodFoamCluster_W_'
            preMeshM = 'FoodFoamMesh_M_'
            preMeshW = 'FoodFoamMesh_W_'
        # 开始动画
        import math
        import random
        waveNum = math.ceil((frameEned - frameStart + 1) / waveRate)
        for i in range(int(waveNum)):
            mc.currentTime(frameStart + i * waveRate)
            Xrand = random.uniform(XrandMin, XrandMax)
            Zrand = random.uniform(ZrandMin, ZrandMax)
            #--------------------------------------------------------------#
            # W位移匹配
            # W_t
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.tx'), (mc.getAttr(followObj + '.tx') + Xrand))
            mc.setKeyframe( preCtrlW+ str(i) + '_' + followObj + '.tx')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.ty'), heightInfoW)
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.tz'), (mc.getAttr(followObj + '.tz') + Zrand))
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.tz')
            # W_r
            # mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.rx'), mc.getAttr(followObj + '.rx'))
            # mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.rx')
            # mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.ry'), mc.getAttr(followObj + '.ry'))
            # mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.ry')
            # mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.rz'), mc.getAttr(followObj + '.rz'))
            # mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.rz')
            # W_s
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sx'), mc.getAttr(followObj + '.sx'))
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sy'), mc.getAttr(followObj + '.sy'))
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sz'), mc.getAttr(followObj + '.sz'))
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sz')
            # W隐藏K帧
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sx'), 0)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sy'), 0)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sz'), 0)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sz')
            mc.setAttr(( preMeshW + str(i) + '_' + followObj + '_.v'), 0)
            mc.setKeyframe( preMeshW + str(i) + '_' + followObj + '_.v')
            # M位移匹配
            # W_t
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.tx'), (mc.getAttr(followObj + '.tx') + Xrand))
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.tx')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.ty'), heightInfo)
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.tz'), (mc.getAttr(followObj + '.tz') + Zrand))
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.tz')
            # M_r
            # mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.rx'), mc.getAttr(followObj + '.rx'))
            # mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.rx')
            # mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.ry'), mc.getAttr(followObj + '.ry'))
            # mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.ry')
            # mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.rz'), mc.getAttr(followObj + '.rz'))
            # mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.rz')
            # M_s
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sx'), mc.getAttr(followObj + '.sx'))
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sy'), mc.getAttr(followObj + '.sy'))
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sz'), mc.getAttr(followObj + '.sz'))
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sz')
            # M隐藏K帧
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sx'), 0)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sy'), 0)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sz'), 0)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sz')
            mc.setAttr(( preMeshM + str(i) + '_' + followObj + '_.v'), 0)
            mc.setKeyframe( preMeshM + str(i) + '_' + followObj + '_.v')
            if waveRate > 1:
                mc.currentTime(frameStart + (i + 1) * waveRate - 1)
                # W隐藏K帧
                mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sx'), 0)
                mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sx')
                mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sy'), 0)
                mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sy')
                mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sz'), 0)
                mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sz')
                mc.setAttr(( preMeshW + str(i) + '_' + followObj + '_.v'), 0)
                mc.setKeyframe( preMeshW + str(i) + '_' + followObj + '_.v')
                # M隐藏K帧
                mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sx'), 0)
                mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sx')
                mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sy'), 0)
                mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sy')
                mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sz'), 0)
                mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sz')
                mc.setAttr(( preMeshM + str(i) + '_' + followObj + '_.v'), 0)
                mc.setKeyframe( preMeshM + str(i) + '_' + followObj + '_.v')
            #--------------------------------------------------------------#
            # 开始生长
            mc.currentTime(frameStart + (i + 1) * waveRate)
            # W隐藏K帧
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sx'), 1)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sy'), 1)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sz'), 1)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sz')
            mc.setAttr(( preMeshW + str(i) + '_' + followObj + '_.v'), 1)
            mc.setKeyframe( preMeshW + str(i) + '_' + followObj + '_.v')
            # M隐藏K帧
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sx'), 1)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sy'), 1)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sz'), 1)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sz')
            mc.setAttr(( preMeshM + str(i) + '_' + followObj + '_.v'), 1)
            mc.setKeyframe( preMeshM + str(i) + '_' + followObj + '_.v')
            #--------------------------------------------------------------#
            # W生长
            # W生长结束
            mc.currentTime(frameStart + (i + 1) * waveRate + growTimeW)
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sx'), scaleMaxW)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sy'), scaleMaxW)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sz'), scaleMaxW)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sz')
            # W生长消失前一帧
            mc.currentTime(frameStart + (i + 1) * waveRate + growTimeW + stayTimeW - 1)
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sx'), scaleMaxW)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sy'), scaleMaxW)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sz'), scaleMaxW)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sz')
            # W消失
            mc.currentTime(frameStart + (i + 1) * waveRate + growTimeW + stayTimeW)
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sx'), 0)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sy'), 0)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlW + str(i) + '_' + followObj + '.sz'), 0)
            mc.setKeyframe( preCtrlW + str(i) + '_' + followObj + '.sz')
            mc.setAttr(( preMeshW + str(i) + '_' + followObj + '_.v'), 0)
            mc.setKeyframe( preMeshW + str(i) + '_' + followObj + '_.v')
            #--------------------------------------------------------------#
            # M生长
            # M生长结束
            mc.currentTime(frameStart + (i + 1) * waveRate + growTimeM)
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sx'), scaleMaxM)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sy'), scaleMaxM)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sz'), scaleMaxM)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sz')
            # M生长消失前一帧
            mc.currentTime(frameStart + (i + 1) * waveRate + growTimeM + stayTimeM - 1)
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sx'), scaleMaxM)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sy'), scaleMaxM)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sz'), scaleMaxM)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sz')
            # M消失
            mc.currentTime(frameStart + (i + 1) * waveRate + growTimeM + stayTimeM)
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sx'), 0)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sx')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sy'), 0)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sy')
            mc.setAttr(( preCtrlM + str(i) + '_' + followObj + '.sz'), 0)
            mc.setKeyframe( preCtrlM + str(i) + '_' + followObj + '.sz')
            mc.setAttr(( preMeshM + str(i) + '_' + followObj + '_.v'), 0)
            mc.setKeyframe( preMeshM + str(i) + '_' + followObj + '_.v')

    # 跟随动画
    def sk_waveSceneAnimMayaOcean(self, oceanObj):
        # 获取信息
        # obj信息
        oceanObj = oceanObj
        # 获取oceanShader
        oceanShape = mc.listRelatives(oceanObj, s=1, ni=1)
        if oceanShape:
            oceanShape = oceanShape[0]
            oceanSG = mc.listConnections('oceanPlaneShape1', type='shadingEngine')
            if oceanSG:
                oceanSG = oceanSG[0]
                oceanShader = mc.listConnections(oceanSG + '.displacementShader')
                if oceanShader:
                    oceanShader = oceanShader[0]
                    # 赋予SG节点置换
                    displacementShader = mc.connectionInfo(('SHD_FoodWave_Mask_SG.displacementShader'), sourceFromDestination=1)
                    print displacementShader
                    if displacementShader:
                        mc.disconnectAttr(displacementShader, ('SHD_FoodWave_Mask_SG.displacementShader'))
                    else:
                        mc.connectAttr((oceanShader + '.displacement'), ('SHD_FoodWave_Mask_SG.displacementShader'))
                    displacementShader = mc.connectionInfo(('SHD_FoodWave_Wave_SG.displacementShader'), sourceFromDestination=1)
                    if displacementShader:
                        mc.disconnectAttr(displacementShader, ('SHD_FoodWave_Wave_SG.displacementShader'))
                    else:
                        mc.connectAttr((oceanShader + '.displacement'), ('SHD_FoodWave_Wave_SG.displacementShader'))
 #locator
    def sk_waveLocator(self):
        
	#获得Locator面板调节值

	radiusM01 = mc.floatField('sk_waveMRadiusField01', v=1, q=1)
        radiusW01 = mc.floatField('sk_waveWRadiusField01', v=1, q=1)

        frameStart01 = mc.floatField('sk_waveFrameStartField01', v=1, q=1)
        frameEnd01 = mc.floatField('sk_waveFrameEndField01', v=1, q=1)
      
        growTimeM01 = mc.floatField('sk_waveMGrowField01', v=1, q=1)
        growTimeW01 = mc.floatField('sk_waveWGrowField01', v=1, q=1)
        stayTimeM01 = mc.floatField('sk_waveMStayField01', v=1, q=1)
        stayTimeW01 = mc.floatField('sk_waveWStayField01', v=1, q=1)
        scaleM01 = mc.floatField('sk_waveMScaleField01', v=1, q=1)
        scaleW01 = mc.floatField('sk_waveWScaleField01', v=1, q=1)
        stayScaleM01 = mc.floatField('sk_waveMStayScaleField01', v=1, q=1)
        stayScaleW01 = mc.floatField('sk_waveWStayScaleField01', v=1, q=1)
	#设置
	mc.floatField('sk_waveMRadiusField', v=radiusM01, e=1)
	#Mask半径
	mc.floatField('sk_waveWRadiusField', v=radiusW01, e=1)
	#Wave半径
	mc.floatField('sk_waveFrameStartField', v=frameStart01, e=1)
	#起始帧
        mc.floatField('sk_waveFrameEndField', v=frameEnd01, e=1)
	#结束帧
      
        mc.floatField('sk_waveMGrowField', v=growTimeM01, e=1)
	#Mask变化
        mc.floatField('sk_waveWGrowField', v=growTimeW01, e=1)
	#Wave变化
        mc.floatField('sk_waveMStayField', v=stayTimeM01, e=1)
	#Mask滞留
        mc.floatField('sk_waveWStayField', v=stayTimeW01, e=1)
	#Wave滞留
        mc.floatField('sk_waveMScaleField', v=scaleM01, e=1)
	#Mask缩放
        mc.floatField('sk_waveWScaleField', v=scaleW01, e=1)
	#Wave缩放
        mc.floatField('sk_waveMStayScaleField', v=stayScaleM01, e=1)
	#Mask滞缩放
        mc.floatField('sk_waveWStayScaleField', v=stayScaleW01, e=1)
	#Wave滞缩放

	#其余默认参数设置
	mc.floatField('sk_waveBaseHeightTypeField', v=5, e=1)
	#M基础高度
	mc.floatField('sk_waveMRadiusRandomField', v=0.5, e=1)
	#M半径随机
        mc.floatField('sk_waveWRadiusRandomField', v=0.5, e=1)
	#W半径随机
        mc.intField('sk_waveMSegXField', v=30, e=1)
	#Mask分段
        mc.intField('sk_waveWSegXField', v=30, e=1)
	#Wave分段

        # noise参数
	mc.intField('sk_waveNoiseTypeField', v=2 , e=1)
	#设置noise算法
        mc.floatField('sk_waveNoiseT2MinScaleField', v=-0.1, e=1)
	#M差异最小
	mc.floatField('sk_waveNoiseT2MaxScaleField', v=0.4, e=1)
	#M差异最大
        mc.floatField('sk_waveNoiseT2RandScaleField', v=2, e=1)
	#差异倍数
        mc.floatField('sk_waveNoiseT2NoiseScaleField', v=3, e=1)
	#W差异倍数
        mc.floatField('sk_waveNoiseT2NoiseScaleVMinField', v=-0.1, e=1)
	#M浪纹最小
        mc.floatField('sk_waveNoiseT2NoiseScaleVMaxField', v=0.2, e=1)
	#M浪纹最大
        mc.floatField('sk_waveNoiseT2MinScaleWField', v=-0.1, e=1)
	#W差异最小
        mc.floatField('sk_waveNoiseT2MaxScaleWField', v=0.4, e=1)
	#W差异最大
        mc.floatField('sk_waveNoiseT2RandScaleWField', v=2, e=1)
	#W差异倍数
        mc.floatField('sk_waveNoiseT2NoiseScaleWField', v=3, e=1)
	#W浪纹缩放
        mc.floatField('sk_waveNoiseT2NoiseScaleVMinWField', v=-0.1, e=1)
	#W浪纹最小
	mc.floatField('sk_waveNoiseT2NoiseScaleVMaxWField', v=0.2, e=1)
	#W浪纹最大
        
        # 动画参数
        mc.floatField('sk_waveFrameRateField', v=1, e=1)
	#发射间隔
        mc.floatField('sk_waveXRandomMinField', v=0, e=1)
	#X轴偏移Min
        mc.floatField('sk_waveXRandomMaxField', v=0, e=1)
	#X轴偏移Max
        mc.floatField('sk_waveZRandomMinField', v=0, e=1)
        mc.floatField('sk_waveZRandomMaxField', v=0, e=1)
    

       
  
        
        # 波纹|泡沫
        mc.intField('sk_waveAnimTypeField' , v=1 , e=1)
  
	

# -*- coding: utf-8 -*-
__author__ = 'xuweijian'

import maya.cmds as mc
import sys
from functools import partial

class MirrorWindow():
    #thisClass='idmt.maya.xwjModule.MirrorTool.MirrorWindow.MirrorWindow()'
    def MirrorWindowUI(self):
        winName = "MirrorToolGUI"
        if mc.window(winName, q = True, ex = True):
            mc.deleteUI(winName)
        mc.window(winName, w= 280, h= 200, title = "Mirror Tool", rtf = True, menuBar = True)

        form = mc.formLayout()
        tabs = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
        #---------------------------- easyAnimCurve IO -------------------------#
        child0 = mc.columnLayout('MirroPose',adj = True)
        mc.separator(h = 10)
        mc.text(l = u"选择模式:",fn = "smallBoldLabelFont", align = "left")
        mc.rowColumnLayout(nc = 2, cw = [(1, 100),(2,120)])
        mc.radioCollection("mirrorPoseRC")
        mc.radioButton("radioWhole", label=u'镜像全身')
        mc.radioButton("radioSelect", label=u'镜像选中的控制器')
        #radioButton("yyEACh", label='Character Set', en = False)
        mc.radioCollection("mirrorPoseRC", e = True, select = "radioWhole")
        mc.setParent("..")
        #cmd=self.thisClass+'.beginMirrorPose()'
        mc.button(l = ">>>Start Mirror<<<", h = 30, c =partial(self.beginMirrorPose))
        #mc.checkBox("yyEAExportJnt", l = "Enclude Joint Animation", v = 0, align  = "left", onc = "yyEASureExportJoint()")
        #mc.checkBox("yyEAIsInfinity", l = "Export Entire AnimCurve", v = 0, align = "left", onc = "yyEADiableTimeRange()", ofc = "yyEAEnableTimeRange()")
        mc.setParent("..")

        child1 = mc.columnLayout('MirroAnim',adj = True)
        mc.separator(h = 10)
        mc.text(l = u"选择模式:",fn = "smallBoldLabelFont", align = "left")
        mc.rowColumnLayout(nc = 2, cw = [(1, 100),(2,120)])
        mc.radioCollection("mirrorAnimRC")
        mc.radioButton("radioWhole", label=u'镜像全身')
        mc.radioButton("radioSelect", label=u'镜像选中的控制器')
        mc.radioCollection("mirrorAnimRC", e = True, select = "radioWhole")
        mc.setParent("..")
        #cmd=self.thisClass+'.beginMirrorAnim()'
        mc.button(l = ">>>Start Mirror<<<", h = 30, c =partial(self.beginMirrorAnim))
        mc.setParent("..")


        mc.showWindow(winName)



    def beginMirrorPose(self,UI=False):
        selectCtrl=mc.ls(sl=1)
        if selectCtrl!=[] or selectCtrl!=None:
            from idmt.maya.xwjModule.MirrorTool import MirrorPose
            reload(MirrorPose)
            optionMode = mc.radioCollection("mirrorPoseRC", q = True, sl = True)
            if optionMode=='radioWhole':
                ctrl=self.getSelect(1)
                MirrorPose.MirrorPose().wholeMirror(ctrl)
            else:
                ctrl=self.getSelect()
                for oneCtrl in ctrl:
                    MirrorPose.MirrorPose().mirrorPose(oneCtrl,1)
    def beginMirrorAnim(self,UI=False):
        selectCtrl=mc.ls(sl=1)
        if selectCtrl!=[] or selectCtrl!=None:
            from idmt.maya.xwjModule.MirrorTool import MirrorAnimation
            reload(MirrorAnimation)
            optionMode = mc.radioCollection("mirrorAnimRC", q = True, sl = True)
            if optionMode=='radioWhole':
                ctrl=self.getSelect(1)
                MirrorAnimation.MirrorAnimation().wholeMirror(ctrl)
            else:
                ctrl=self.getSelect()
                for oneCtrl in ctrl:
                    MirrorAnimation.MirrorAnimation().mirrorAnim(oneCtrl)

    #type参数0为选中控制器模式,1为全身复制模式(全身模式只执行第一个选中的控制器)
    def getSelect(self,type=0):
        if len(mc.ls(sl=1))==0:
            mc.confirmDialog( title='WARNING', message=u'请选择一个角色控制器', button=['OK'], cancelButton='No')
            print u'脚本准备结束'
            sys.exit()
        else:
            if type==1:
                selectObj=(mc.ls(sl=1)[0])
            else:
                selectObj=mc.ls(sl=1)
            print selectObj
        return selectObj
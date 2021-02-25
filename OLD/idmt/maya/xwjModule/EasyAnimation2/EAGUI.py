__author__ = 'xuweijian'
import maya.cmds as mc
import os



def yyEAGUI():
    winName = "easyAnimGUI"
    if mc.window(winName, q = True, ex = True):
        mc.deleteUI(winName)
    mc.window(winName, w= 280, h= 480, title = "Easy Animation v2.3", rtf = True, menuBar = True)

    mc.menu( label='Edit')
    mc.menuItem( label='Refresh', c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEARefresh()")
    mc.menuItem( divider=True )

    mc.menuItem( label='Exit', c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEAExit()")

    mc.menu( label='About')
    mc.menuItem( label='Help', c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEAHelp()")
    mc.menuItem( divider=True )

    mc.menuItem( label='About' , c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEAAbout()")

    form = mc.formLayout()
    tabs = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    mc.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

    #---------------------------- easyAnimCurve IO -------------------------#
    child0 = mc.columnLayout(adj = True)

    mc.separator(h = 10)
    mc.text(l = "Export (first specific mode):",fn = "smallBoldLabelFont", align = "left")
    mc.rowColumnLayout(nc = 3, cw = [(1, 76),(2,74),(3, 84)])
    mc.radioCollection("yyEARC")
    mc.radioButton("yyEAHi", label='Hierarchy')
    mc.radioButton("yyEASl", label='Selection')
    mc.radioButton("yyEACh", label='Character Set', en = False)
    mc.radioCollection("yyEARC", e = True, select = "yyEAHi")
    mc.setParent("..")


    mc.checkBox("yyEAExportJnt", l = "Enclude Joint Animation", v = 0, align  = "left", onc = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEASureExportJoint()")
    mc.checkBox("yyEAIsInfinity", l = "Export Entire AnimCurve", v = 0, align = "left", onc = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEADiableTimeRange()", ofc = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEAEnableTimeRange()")

    ##--------------- play back range --------------##
    mc.rowColumnLayout(nc = 4, cw = [(1, 40),(2,80),(3, 30),(4,80)])
    startTime = mc.playbackOptions(q = True, min = True)
    endTime = mc.playbackOptions(q = True, max = True)
    mc.text("yyEATextFrame", l = "Frame")
    mc.intField("yyEAStartIF01", v = startTime)
    mc.text("yyEATestTo", l = "To", align = "center")
    mc.intField("yyEAEndIF01", v = endTime)
    mc.setParent("..")
    ##--------------- play back range --------------##
    #cmd='from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEAExportWrapper()'
    mc.button(l = "animCurve Export>>>>>", h = 30, c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEAExportWrapper()")
    mc.separator(h = 10)
    ##--------------- import options --------------##
    mc.text(l = "Import:",fn = "smallBoldLabelFont", align = "left")
    mc.checkBox("yyEAIsReplace", l = "Replace Exist animCurve", v = 1, align  = "left")
    mc.rowColumnLayout(nc = 4, cw = [(1, 40),(2,60),(3, 60),(4,80)])
    mc.text(l = "Offset")
    mc.intField("yyEAOffsetIF01", v = 0)
    mc.text(l = "Time Scale", align = "center")
    mc.floatField("yyEATimeIF01", v = 1)
    mc.setParent("..")

    mc.rowColumnLayout(nc = 3, cw = [(1,60),(2,60),(3,60)])
    mc.checkBox("yyEAIsStop1", l = " isStop?", v = 0)
    mc.text(l = "Stop Time:")
    mc.intField("yyEAStopTime1", v = 1000)
    mc.setParent("..")

    ##--------------- import  --------------##
    mc.button(l = ">>>>>animCurve Import", h = 30, c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEAImportWrapper()")
    mc.separator(h = 10)
    ##--------------- Transfer by namespace --------------##
    mc.text(l = "Transfer:",fn = "smallBoldLabelFont", align = "left")
    mc.text(l = "First select source, then target.", align = "left")
    mc.checkBox("yyEATransferJnt", l = "Enclude Joint Animation", v = 0, align  = "left", onc = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEASureTransferJoint()")
    mc.checkBox("yyEATransferIsReplace", l = "Is Replace?", v = 1, align = "left")
    mc.button(l = ">>>animCurve Transfer>>>", h = 30, c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEATransferWrapper()")


    mc.text(l = "-----------------------")
    mc.text(l = "GDC-IDMT 2009 (C)\n")
    mc.setParent( '..' )


    #---------------------------  EA Feeding  ---------------------------#
    child2 = mc.columnLayout(adj = True)
    mc.separator(h = 10)
    try:
        mc.text(l = "Hint:",fn = "smallBoldLabelFont",align = "left")
        mc.text(l = "Auto recognize namespace from your selection", align = "left")
        mc.separator(h = 10)
        repositoryPath = ea1.yyEAGetProjectRepository()
        mc.text(l = "Creature Name:", align = "left")
        try:
            creatureNodeList = os.listdir(repositoryPath)
        except:
            creatureNodeList = []
        mc.optionMenu("yyEA_om01", cc = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEAChangeCreature()",w =120)
        try:
            for i in range(len(creatureNodeList)):
                stri = str(i)
                mc.menuItem("yyEA_mi01"+stri,label=creatureNodeList[i])
        except:
            pass
        try:
            mc.optionMenu("yyEA_om01", e=True, select = 1)
        except:
            pass

        creaturePath = ea1.yyEAGetOptionItemFP01()
        try:
            yyeaListTemp = os.listdir(repositoryPath + "/" + creaturePath)
        except:
            yyeaListTemp = []
        yyeaList = []
        for i in range(len(yyeaListTemp)):
            if yyeaListTemp[i].find(".") < 0:
                yyeaList.append(yyeaListTemp[i].split(".")[0])


        mc.text(l = "Genre Name:", align = "left")
        mc.optionMenu("yyEA_om02", cc = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEAChangeGenre()")
        try:
            for i in range(len(yyeaList)):
                stri = str(i)
                mc.menuItem("yyEA_mi02"+stri,label=yyeaList[i])
        except:
            pass
        try:
            mc.optionMenu("yyEA_om02", e=True, select = 1)
        except:
            pass

        genrePath = ea1.yyEAGetOptionItemFP02()
        try:
            yyeaListTemp = os.listdir(repositoryPath + "/" + creaturePath + "/" + genrePath)
            #print yyeaListTemp
        except:
            yyeaListTemp = []
        yyeaList = []
        for i in range(len(yyeaListTemp)):
            if yyeaListTemp[i].find(".yyea") > 0:
                yyeaList.append(yyeaListTemp[i].split(".")[0])


        mc.text(l = "Feedin Curve Name:", align = "left")
        mc.optionMenu("yyEA_om03")
        try:
            for i in range(len(yyeaList)):
                stri = str(i)
                mc.menuItem("yyEA_mi03"+stri,label=yyeaList[i])
        except:
            pass
        try:
            mc.optionMenu("yyEA_om03", e=True, select = 1)
        except:
            pass


    except:
        mc.text(l = "no found repository")


    mc.rowColumnLayout(nc = 4, cw = [(1,40),(2,70),(3,40),(4,70)])
    mc.text(l = "Times:", align = "left")
    mc.intField("feedinTimes", v = 1)
    mc.text(l = "Scale:", align = "left")
    mc.floatField("feedinScale", v = 1)
    mc.text(l = "Jump:")
    mc.intField("yyEAJump", v = 0)
    mc.setParent("..")
    mc.rowColumnLayout(nc = 3, cw = [(1,60),(2,60),(3,60)])
    mc.checkBox("yyEAIsStop2", l = " isStop?", v = 0)
    mc.text(l = "Stop Time:")
    mc.intField("yyEAStopTime2", v = 1000)
    mc.setParent("..")
    mc.button(l = "Easy Anim Feed In", h = 30, c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEAFeedInWrapper()")
    mc.button(l = "Watch Example Video", h = 30, c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEAWatchExampleVideoClip()")


    mc.text(l = "-----------------------")
    mc.text(l = "GDC-IDMT 2009 (C)\n")
    mc.setParent( '..' )


    #---------------------------  Extra functions  ---------------------------#
    child1 = mc.columnLayout(adj = True)
    mc.separator(h = 10)
    mc.text(l = "Hint:",fn = "smallBoldLabelFont",align = "left")
    mc.text(l = "For Checking Animation Info:", w = 220, align = "left")

    ##--------------- animation checker --------------##
    mc.separator(h = 10)
    mc.text(l = "Animation Detector", w = 220, align = "left", fn = "smallBoldLabelFont")
    mc.button(l = "Auto Select Objects with Anim (Whole Scene)", h = 30, c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyAutoSelectWithAC(1)")
    mc.button(l = "Auto Select Objects with Anim (in Hierarchy)", h = 30, c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyAutoSelectWithACInHi(1)")
    mc.button(l = "Auto Select Objects with Anim (by Namespace)", h = 30, c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyAutoSelectWithNS(1)")
    mc.separator(h = 10)
    ##--------------- animation cleanser --------------##
    mc.text(l = "Animation Cleanser", w = 220, align = "left", fn = "smallBoldLabelFont")
    mc.rowColumnLayout(nc = 3, cw = [(1,88),(2, 80),(3,50)])
    mc.text(l = "Operation Mode:")
    mc.radioCollection("yyEADARC")
    mc.radioButton("yyEADASl", label='Selections')
    mc.radioButton("yyEADAAll", label='All')
    mc.radioCollection("yyEADARC", e = True, select = "yyEADASl")
    mc.setParent("..")
    mc.button(l = "Delete Animation", h = 30, c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyEADeleteAnimCurveWrapper()")
    mc.separator(h = 10)

    ##------------- non-animation channels ------------##
    mc.text(l = "Non-animation Channel Channels:", w = 240, align = "left", fn = "smallBoldLabelFont")
    mc.button(l = "Check Non-animation Channels", h = 30, c = "from idmt.maya.xwjModule.EasyAnimation2 import EasyAnimation\nreload(EasyAnimation)\nEasyAnimation.EasyAnimation().yyNonAnimChannelChecker()")
    mc.button(l = "Bake Non-animation Channels", h = 30, en = False)
    mc.separator(h = 10)

    mc.text(l = "-----------------------")
    mc.text(l = "GDC-IDMT 2009 (C)\n")

    mc.setParent( '..' )

    mc.tabLayout( tabs, edit=True, tabLabel=((child0,"animCurve IO"),(child2, "EA-Feedin"), (child1, 'Accessories')))

    mc.showWindow(winName)

#def yyEAExportWrapper():
    #print '------------------'
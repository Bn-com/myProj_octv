__author__ = 'xuweijian'
# -*- coding: utf-8 -*-
import maya.cmds as mc
class AOV():
    def __init__(self,projectName):
        self.projectName=projectName
    def creatAOV(self,aovName):
        if not mc.pluginInfo('mtoa.mll',q=1,loaded = 1):
            mc.loadPlugin('mtoa.mll')
        import mtoa
        mtoa.core.createOptions()
        import mtoa.cmds.registerArnoldRenderer
        mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
        self.aovName=aovName
        aovListSize = mc.getAttr('defaultArnoldRenderOptions.aovList',s=1)

        for checkNum in range(aovListSize):
            cons = mc.listConnections('defaultArnoldRenderOptions.aovList[%s]'%str(checkNum),s=1,d=0)
            if not cons:
                aovListSize = checkNum
                break
        if mc.ls(aovName):
            mc.error('Aov already existed')
        customAOV = mc.createNode('aiAOV',n=aovName, skipSelect=True)
        mc.setAttr(customAOV+'.name',customAOV,type='string')
        mc.connectAttr(customAOV+'.message','defaultArnoldRenderOptions.aovList[%s]'%aovListSize,f=1)
        mc.connectAttr('defaultArnoldDriver.message',customAOV+'.outputs[0].driver', f=1)
        mc.connectAttr('defaultArnoldFilter.message',customAOV+'.outputs[0].filter', f=1)



    def RGB(self,objR=[],objG=[],objB=[]):
        #---------aiUserData------------------
        RColor='R_aiColor_%s'%self.projectName
        GColor='G_aiColor_%s'%self.projectName
        BColor='B_aiColor_%s'%self.projectName

        if not mc.ls(RColor):
            self.RColor=mc.shadingNode('aiUserDataColor', asShader=1,name = RColor)
            mc.setAttr(self.RColor+'.defaultValue',1,0,0,typ='double3')
        if not mc.ls(GColor):
            self.GColor=mc.shadingNode('aiUserDataColor', asShader=1,name = GColor)
            mc.setAttr(self.GColor+'.defaultValue',0,1,0,typ='double3')
        if not mc.ls(BColor):
            self.BColor=mc.shadingNode('aiUserDataColor', asShader=1,name = BColor)
            mc.setAttr(self.BColor+'.defaultValue',0,0,1,typ='double3')

        #----------tripleShadingSwith-------------
        tSwitch='RGB_tSwitch_%s'%self.aovName

        if mc.ls(tSwitch):
            mc.delete(tSwitch)
        tSwitch = mc.shadingNode('tripleShadingSwitch',au=1,name = tSwitch)
        mc.setAttr(tSwitch+'.default',0,0,0,typ='double3')

        #----------aiUtility----------------
        aiUshader='RGB_aiUtility_%s'%self.aovName
        if mc.ls(aiUshader):
            mc.delete(aiUshader)
        aiUshader = mc.shadingNode('aiUtility', asShader=1,name = aiUshader)
        mc.setAttr('%s.shadeMode'%aiUshader,2)




        #----------连接节点------------------
        mc.connectAttr(aiUshader+'.outColor',self.aovName+'.defaultValue',f=1)
        mc.connectAttr(tSwitch+'.output', aiUshader+'.color',f=1)
        if objR  and objR!=[u'']:
            meshR = mc.listRelatives(objR,ad=1,type = 'mesh',ni=1)
            if meshR:
                print meshR
                for one in meshR:
                    inNum = mc.getAttr(tSwitch+'.input',s=1)
                    mc.connectAttr(one+'.instObjGroups[0]',tSwitch+'.input['+str(inNum)+'].inShape',f=1)
                    mc.connectAttr(RColor+'.outColor','%s.input[%s].inTriple'%(tSwitch,inNum),f=1)

        if objG and objG!=[u'']:
            meshG = mc.listRelatives(objG,ad=1,type = 'mesh',ni=1)
            if meshG:
                print meshG
                for one in meshG:
                    inNum = mc.getAttr(tSwitch+'.input',s=1)
                    mc.connectAttr(one+'.instObjGroups[0]',tSwitch+'.input['+str(inNum)+'].inShape',f=1)
                    mc.connectAttr(GColor+'.outColor','%s.input[%s].inTriple'%(tSwitch,inNum),f=1)

        if objB and objB!=[u'']:
            meshB = mc.listRelatives(objB,ad=1,type = 'mesh',ni=1)
            if meshB:
                for one in meshB:
                    inNum = mc.getAttr(tSwitch+'.input',s=1)
                    mc.connectAttr(one+'.instObjGroups[0]',tSwitch+'.input['+str(inNum)+'].inShape',f=1)
                    mc.connectAttr(BColor+'.outColor','%s.input[%s].inTriple'%(tSwitch,inNum),f=1)






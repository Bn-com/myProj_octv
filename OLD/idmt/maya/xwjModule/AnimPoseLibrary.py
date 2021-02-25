#-*- coding: utf-8 -*-
__author__ = 'xuweijian'


import maya.cmds as mc
import os
from functools import partial


class AnimPoseLibrary(object):


    #currentPath=''
    #allPath='//file-cluster/GDC/Projects/'

    def APLibUI(self):
        if mc.window('AnimPoseLibraryWin',exists=1):
            mc.deleteUI('AnimPoseLibraryWin')
        mc.window('AnimPoseLibraryWin',rtf=1)
        mc.columnLayout(adj=1)
        mc.rowLayout(numberOfColumns=2,cw1=10,cat=[1,'both',0])
        folders=mc.getFileList(fld='//file-cluster/GDC/Projects/')
        mc.optionMenuGrp('projectsGRp',label='projects')
        for folder in folders:
            mc.menuItem(label=folder)
        mc.optionMenuGrp('privateOrPublic',label='private or public')
        mc.menuItem(label='public')
        mc.menuItem(label='private')
        mc.setParent('..')

        form2=mc.formLayout()
        tabs = mc.tabLayout()
        mc.formLayout( form2, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
        form2Width=mc.formLayout( form2, q=1,w=1)
        print 'width='+str(form2Width)
        tabAn=mc.rowLayout(numberOfColumns=2,cw=[1,100])#--------------3



        mc.textScrollList('charScrolList',numberOfRows=8,allowMultiSelection=0,)







        mc.formLayout('flofAnim')#-------2
        mc.shelfLayout('shelfOfAnim',cwh=[80,80],w=400,h=400,p='flofAnim')
        mc.formLayout('flofAnim',e=1,attachForm=(('shelfOfAnim', 'top', 0), ('shelfOfAnim', 'left', 0), ('shelfOfAnim', 'bottom', 0), ('shelfOfAnim', 'right', 0)))
        #mc.iconTextRadioCollection( 'itRadCollection',p='shelfOfAnim')
        #mc.iconTextRadioButton( st='textOnly', i1='sphere.png', l='sphere',si='M:/test/TeethLess_walk.bmp')
        #mc.iconTextRadioButton( st='iconOnly', i1='spotlight.png', l='spotlight' )
        #mc.iconTextRadioButton( st='iconAndTextHorizontal', i1='cone.png', l='cone' )
        #mc.iconTextRadioButton( st='iconAndTextVertical', i1='cube.png', l='cube' )
        #mc.iconTextRadioButton( st='iconOnly', i1='M:/test/TeethLess_walk.bmp', l='test',mw=10,mh=10,si='A')
        #mc.iconTextRadioButton( st='iconAndTextCentered', i1='M:/test/TeethLess_walk.bmp', l='test',mw=10,mh=10)
        mc.setParent('..')#----------1
        mc.setParent('..')#----------2




        mc.setParent('..')#------------3





        tabPose=mc.rowLayout(numberOfColumns=2)
        mc.formLayout('flofPose')
        mc.shelfLayout('shelfOfPose',cwh=[80,80],w=400,h=400)
        mc.formLayout('flofPose',e=1,attachForm=(('shelfOfPose', 'top', 0), ('shelfOfPose', 'left', 0), ('shelfOfPose', 'bottom', 0), ('shelfOfPose', 'right', 0)))
        #mc.iconTextRadioCollection( 'itRadCollection2' )
        #mc.iconTextRadioButton( st='textOnly', i1='sphere.png', l='sphere',si='M:/test/TeethLess_walk.bmp')
        #mc.iconTextRadioButton( st='iconOnly', i1='spotlight.png', l='spotlight' )
        #mc.iconTextRadioButton( st='iconAndTextHorizontal', i1='cone.png', l='cone' )
        #mc.iconTextRadioButton( st='iconAndTextVertical', i1='cube.png', l='cube' )
        #mc.iconTextRadioButton( st='iconOnly', i1='M:/test/TeethLess_walk.bmp', l='test',mw=10,mh=10,si='A')
        #mc.iconTextRadioButton( st='iconAndTextCentered', i1='M:/test/TeethLess_walk.bmp', l='test',mw=10,mh=10)
        mc.setParent('..')
        mc.setParent('..')


        mc.setParent('..')

        mc.tabLayout( tabs, edit=True, tabLabel=((tabAn, 'Anmiation'), (tabPose, 'Pose')) )
        mc.setParent('..')
        mc.setParent('..')



        mc.rowLayout(numberOfColumns=2,adj=1)
        mc.button(l='import',c='print project')
        mc.button(l='export',w=100)
        mc.setParent('..')


        mc.tabLayout( tabs, edit=True, tabLabel=((tabAn, 'Anmiation'), (tabPose, 'Pose')) )
        mc.optionMenuGrp('projectsGRp',e=1,cc=partial(self.getCharList))
        #mc.optionMenuGrp('projectsGRp',e=1,cc="from idmt.maya.xwjModule import AnimPoseLibrary\nreload(AnimPoseLibrary)\nAnimPoseLibrary.AnimPoseLibrary().getCharList()")
        #mc.optionMenuGrp('projectsGRp',e=1,cc="AnimPoseLibrary.AnimPoseLibrary().getCharList()")
        #mc.optionMenuGrp('projectsGRp',e=1,cc=AnimPoseLibrary().getCharList())
        mc.showWindow()



    def getCharList(self,project):
        print 'run getCharList'
        print 'test:'+project
        #project=mc.optionMenuGrp('projectsGRp',q=1,v=1)
        #print project
        projectPath='//file-cluster/GDC/Projects/'+project+'/%s_Scratch/'%project+u'Animation/动作库/'
        #self.currentPath=projectPath
        #print 'currentPath:'+self.currentPath

        if os.path.exists(projectPath):
            files=os.listdir(projectPath)
            if files != None or files!=[]:
                mc.textScrollList('charScrolList',e=1,ra=1)
                for one in files:
                    if os.path.isdir(os.path.join(projectPath, one)):
                        #mc.textScrollList('charScrolList',e=1,a=one,sc='reload(AnimPoseLibrary)\nAnimPoseLibrary.AnimPoseLibrary().getAnimLibrary()')
                        mc.textScrollList('charScrolList',e=1,a=one,sc=partial(self.getAnimLibrary,projectPath))
                        #mc.textScrollList('charScrolList',e=1,a=one,sc='from idmt.maya.xwjModule.AnimPoseLibrary.AnimPoseLibrary().getAnimLibrary() import getAnimLibrary()\ngetAnimLibrary()')
        else:
            print projectPath+' not exist'




    def getAnimLibrary(self,path):
        print path
        #print 'currentPath:'+self.currentPath
        charName=mc.textScrollList('charScrolList',q=1,si=1)[0]
        #AnimLibraryPath=projectPath+charName+'/'
        AnimLibraryPath=path+charName+'/'
        print AnimLibraryPath
        imageFile=mc.getFileList(fld=AnimLibraryPath,fs='*.bmp')
        print imageFile
        childs=mc.shelfLayout('shelfOfAnim',q=1,ca=1)
        print childs
        if childs!=None:
            mc.deleteUI(childs)
        mc.iconTextRadioCollection('itRadCollection',p='shelfOfAnim')
        mc.iconTextRadioButton(st='iconAndTextCentered', i1='M:/test/TeethLess_walk.bmp', l='test',mw=10,mh=10)
        mc.setParent('shelfOfAnim')
        #charPath=projectPath+'/'+charName
        #print charPath



        #charList=mc.getFileList(fld=projectPath,filespec='folder')
        #print charList



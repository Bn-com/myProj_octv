__author__ = 'xuweijian'

import maya.cmds as mc
class getInfoByName():
    def getInfoByScene(self):
        dict={}
        fileName = mc.file(q=1, sn=1,shn=1)
        SceneName=fileName
        info=SceneName.split('_')
        SCinfo=[info[1][1:3],info[1][4:7]]
        dict['project']=info[0]
        dict['scene']=SCinfo[0]
        dict['camera']=SCinfo[1]
        dict['part']=info[2]
        return dict
    def getInfoByAsset(self):
        dict={}
        fileName = mc.file(q=1, sn=1,shn=1)
        SceneName=fileName
        info=SceneName.split('_')
        SCinfo=[info[1][1:2],info[1][4:6]]
        dict['project']=info[0]
        dict['type']=info[1]
        dict['name']=info[2]
        dict['part']=info[3]
        return dict
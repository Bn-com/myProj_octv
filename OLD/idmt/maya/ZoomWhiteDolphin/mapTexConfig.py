# -*- coding: utf-8 -*-
import maya.cmds as mc
'''
��ͨ�ã�����map��׺�д��ڶ���.��ʽ�������
ͳһ������ͼ�����ǵ�������������Ȩ�޸ķ������ˣ�����ʱ����D��ָ��temp
�ϴ����ֶ�����D��temp�ļ�
Author: ��  ��
Data    :2013_04_27
'''
def sk_mapTexConfig():    
    #����Ŀ¼
    tempPath = 'D:/Info_Temp/temp/texTemp'
    mc.sysFile(tempPath ,makeDir = 1)
    #��ȡ��ͼ�ڵ�
    texNames = mc.ls(type = 'file')
    for i in range(len(texNames)):
        #��ȡ��ͼ·��
        sysPath = mc.getAttr((texNames[i] + '.fileTextureName'))
        #��ȡ�����ļ���
        tempSplit = sysPath.split('/')[-1]
        tempNames = tempSplit.split('.')
        finalName = tempNames[0]+'.'+tempNames[-1]
        #���ƣ�����
        mc.sysFile(sysPath ,copy = (tempPath + '/' + tempSplit))
        mc.sysFile((tempPath + '/' + tempSplit) , rename = (tempPath + '/' +finalName) )
        #���¸���·��
        mc.setAttr((texNames[i] + '.fileTextureName'),(tempPath + '/' +finalName),type = 'string')



    

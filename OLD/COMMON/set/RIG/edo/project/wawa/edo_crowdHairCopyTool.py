#-*- coding: utf-8 -*-
import maya.cmds as cmds
def edo_crowdHairCopyTool():
    sels=cmds.ls(sl=1)
    if sels==None:
        cmds.confirmDialog(title='ѡ�����', message='��ѡ��Master���������й�������', button='֪����!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    for sel in sels:
        #sel=sels[0]
        if not 'Master' in sel:
            cmds.confirmDialog(title='ѡ�����', message='��ѡ��Master���������й�������', button='���Լ���!',defaultButton='Yes', cancelButton='No', dismissString='No')
            continue
        sp=sel.split(':')
        if not len(sp)==1:
            cmds.confirmDialog(title='ѡ�����', message='   �����ƿռ䣬��ѡ��������Ƶ�Master������ִ�нű�', button='֪����!',defaultButton='Yes', cancelButton='No', dismissString='No')
            continue
        list=cmds.listRelatives(sel,c=1)
        Master=sel
        PFX=edo_findGroupFromString(list,'GRP_paintEffects')
        if PFX=='':
            PFX=edo_findGroupFromString(list,'GRP_PaintEffects')
            if PFX=='':
                cmds.confirmDialog(title='��Ⱦ���岻����', message='   �㼶����Ⱦ���岻����', button='���Լ���!',defaultButton='Yes', cancelButton='No', dismissString='No')
                continue
        chs=cmds.listRelatives(PFX,c=1,f=1)
        for ch in chs:
            #ch=chs[0]
            chShapes=cmds.listRelatives(ch,s=1)
            if chShapes==None:
                cmds.confirmDialog(title='û���νڵ�', message='   û���νڵ�', button='���Լ���!',defaultButton='Yes', cancelButton='No', dismissString='No')
                continue
            if not len(chShapes)==1:
                cmds.confirmDialog(title='����νڵ�', message='   �ж���νڵ�', button='���Լ���!',defaultButton='Yes', cancelButton='No', dismissString='No')
                continue
            type=cmds.nodeType(chShapes[0])
            if not type=='pfxHair':
                cmds.confirmDialog(title='�νڵ㲻��ȷ', message='   ���νڵ㲻��pfxHair', button='���Լ���!',defaultButton='Yes', cancelButton='No', dismissString='No')
                continue
            newch=cmds.createNode('pfxHair')
            trs=cmds.listRelatives(newch,p=1)
            cmds.rename(trs[0],ch)
            newch=cmds.ls(sl=1,type='pfxHair')
            newpfx=cmds.listRelatives(newch,p=1,f=1)
            input=cmds.listConnections(chShapes[0]+'.renderHairs',s=1,d=0,p=1)
            if input==None:
                cmds.confirmDialog(title='ԭʼͷ�����Ӳ���ȷ', message='   û�б�hairsystem����', button='���Լ���!',defaultButton='Yes', cancelButton='No', dismissString='No')
                continue
            cmds.connectAttr(input[0],newpfx[0]+'.renderHairs',f=1)
            cmds.setAttr(newpfx[0]+'.tx',l=1)
            cmds.setAttr(newpfx[0]+'.ty',l=1)
            cmds.setAttr(newpfx[0]+'.tz',l=1)
            cmds.setAttr(newpfx[0]+'.rx',l=1)
            cmds.setAttr(newpfx[0]+'.ry',l=1)
            cmds.setAttr(newpfx[0]+'.rz',l=1)
            cmds.setAttr(newpfx[0]+'.sx',l=1)
            cmds.setAttr(newpfx[0]+'.sy',l=1)
            cmds.setAttr(newpfx[0]+'.sz',l=1)
            cmds.parent(newpfx[0],Master)
    
def edo_findGroupFromString(list,name):
     group=''     
     for l in list:
         if name in l:
             group=l
     return group

edo_crowdHairCopyTool()

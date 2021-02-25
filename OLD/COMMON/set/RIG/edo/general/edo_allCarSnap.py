import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaAnim as oma
import sys
sys.path.append("//File-cluster/GDC/Resource/Support/Maya/Python/IDMT/RR")
import RR_ysAniTools as ANT
reload(ANT)

def edo_allCarSnap():
    bt=cmds.confirmDialog( title='dialog', message='which MIS control you want to snap?', button=['only select MIS','all truck MIS'],defaultButton='Yes', cancelButton='No', dismissString='No')
    if (bt=='only select MIS'):
        ANT.attachCarOnGround()
    if (bt=='all truck MIS'):
        ma=oma.MAnimControl()
        st=ma.minTime().value()
        et=ma.maxTime().value()
        nameSpace=''
        sels=cmds.ls(sl=1)
        if not sels==None:
            cv=sels[1]
            fround=sels[2]
            nameSpace=sels[0].split(':')[0]
            set=nameSpace+':'+'snapCtrl_set'
            cvshape=cmds.listRelatives(cv,s=1)[0]
            if cmds.objExists(nameSpace+'_curveInfo'):
                cmds.delete(nameSpace+'_curveInfo')
            cmds.createNode('curveInfo',n=nameSpace+'_curveInfo')
            cmds.connectAttr(cvshape+'.worldSpace',nameSpace+'_curveInfo.inputCurve',f=1)
            arclen=cmds.getAttr(nameSpace+'_curveInfo.arcLength')
            if cmds.objExists(set):
                ctrl=cmds.sets(set,q=1)
                for c in ctrl:
                    #c=ctrl[0]
                    cmds.select(c,cv,fround,r=1)
                    ANT.attachCarOnGround()
                    snapc=c.replace('_MIS','_Path_Car_Grp')
                    mp=cmds.listConnections(snapc+'.ry',d=0,s=1)[0]
                    anim=cmds.listConnections(mp+'.uValue',d=0,s=1)[0]
                    if not anim==None:
                        if 'animCurve' in cmds.nodeType(anim):
                            cmds.delete(anim)
                    if not cmds.attributeQuery('go',node=c,ex=1):
                        cmds.addAttr(c,ln='go',at='double',min=0,max=1)
                        cmds.setAttr(c+'.go',keyable=True)
                    cmds.connectAttr(c+'.go',mp+'.uValue',f=1)
                cmds.cycleCheck(e=0)
                for i in range(-1,-len(ctrl)-1,-1):
                    #i=-1
                    dis=cmds.getAttr(ctrl[i]+'.distance')
                    indis=cmds.getAttr(ctrl[i]+'.inverse_distance')
                    cmds.setKeyframe(ctrl[i]+'.go',t=st,v=(dis/arclen))
                    cmds.setKeyframe(ctrl[i]+'.go',t=et,v=1-(indis/arclen))
import maya.cmds as cmds
def edo_setQSKparts():
    sels=cmds.ls(sl=1)
    for sela in sels:
        #sela=sels[0]
        sel=sela.split('|')[-1] 
        if sel[0:3]=='QKS':
            continue
        qsk=cmds.rename(sela,'QKS_'+sel)
        shs=cmds.listRelatives(qsk,s=1,pa=1)
        if shs:
            sh=shs[0]
            print 'setAttr ... '+sh+'.connectionCtrlName  ...  '+sel+'\n'
            cmds.setAttr(sh+'.connectionCtrlName',sel,type='string')

def edo_setMultiplyQSKparts():
    sels=cmds.ls(sl=1)
    mqsk=sels[0]
    sels=sels[1:]
    tx=''
    for i in sels:
        #i=sels[0]
        t=cmds.getAttr(i+'.connectionCtrlName')
        if t[-1]==' ':
            t=t[:-1]
        tx=tx+t+' '
    print tx
    shs=cmds.listRelatives(mqsk,s=1,pa=1)
    if shs:
        sh=shs[0]
        print 'setAttr ... '+sh+'.connectionCtrlName  ...  '+tx+'\n'
        cmds.setAttr(sh+'.connectionCtrlName',tx,type='string')

def edo_addMultiplyQSKparts():
    sels=cmds.ls(sl=1)
    mqsk=sels[0]
    sels=sels[1:]
    tx=cmds.getAttr(mqsk+'.connectionCtrlName')
    for i in sels:
        #i=sels[6]
        t=cmds.getAttr(i+'.connectionCtrlName')
        ts=t.split(' ')
        for tt in ts:
            if not tt in tx:
                tx=tx+tt+' '
    print tx
    shs=cmds.listRelatives(mqsk,s=1,pa=1)
    if shs:
        sh=shs[0]
        print 'setAttr ... '+sh+'.connectionCtrlName  ...  '+tx+'\n'
        cmds.setAttr(sh+'.connectionCtrlName',tx,type='string')
        
def edo_setQSKpartsAsSelectedCtrls():
    sels=cmds.ls(sl=1)
    mqsk=sels[0]
    sels=sels[1:]
    tx=''
    for i in sels:
        #i=sels[0]
        tx=tx+i+' '
    print tx
    shs=cmds.listRelatives(mqsk,s=1,pa=1)
    if shs:
        sh=shs[0]
        print 'setAttr ... '+sh+'.connectionCtrlName  ...  '+tx+'\n'
        cmds.setAttr(sh+'.connectionCtrlName',tx,type='string')

def edo_limitAllQSK(v=1):
    #cmds.select(sels)
    sels=cmds.ls(type='reSelectLocator')
    for sel in sels:
        print sel
        #sel='QSK_c_eye_MShape'
        p=cmds.listRelatives(sel,p=1,pa=1)[0]
        cmds.setAttr(p+'.tx',e=1,k=0)
        cmds.setAttr(p+'.ty',e=1,k=0)
        cmds.setAttr(p+'.tz',e=1,k=0)
        cmds.setAttr(p+'.rx',e=1,k=0)
        cmds.setAttr(p+'.ry',e=1,k=0)
        cmds.setAttr(p+'.rz',e=1,k=0)
        cmds.setAttr(p+'.sx',e=1,k=0)
        cmds.setAttr(p+'.sy',e=1,k=0)
        cmds.setAttr(p+'.sz',e=1,k=0)
        cmds.setAttr(p+'.tx',e=1,cb=1)
        cmds.setAttr(p+'.ty',e=1,cb=1)
        cmds.setAttr(p+'.tz',e=1,cb=1)
        cmds.setAttr(p+'.rx',e=1,cb=1)
        cmds.setAttr(p+'.ry',e=1,cb=1)
        cmds.setAttr(p+'.rz',e=1,cb=1)
        cmds.setAttr(p+'.sx',e=1,cb=1)
        cmds.setAttr(p+'.sy',e=1,cb=1)
        cmds.setAttr(p+'.sz',e=1,cb=1)
        cmds.setAttr(p+'.v',e=1,k=0)
        cmds.setAttr(p+'.v',e=1,l=1)
        cmds.setAttr(p+'.mxtl',cmds.getAttr(p+'.tx'),cmds.getAttr(p+'.ty'),cmds.getAttr(p+'.tz'),type='double3')
        cmds.setAttr(p+'.mntl',cmds.getAttr(p+'.tx'),cmds.getAttr(p+'.ty'),cmds.getAttr(p+'.tz'),type='double3')
        cmds.setAttr(p+'.mxrl',cmds.getAttr(p+'.rx'),cmds.getAttr(p+'.ry'),cmds.getAttr(p+'.rz'),type='double3')
        cmds.setAttr(p+'.mnrl',cmds.getAttr(p+'.rx'),cmds.getAttr(p+'.ry'),cmds.getAttr(p+'.rz'),type='double3')
        cmds.setAttr(p+'.mxsl',cmds.getAttr(p+'.sx'),cmds.getAttr(p+'.sy'),cmds.getAttr(p+'.sz'),type='double3')
        cmds.setAttr(p+'.mnsl',cmds.getAttr(p+'.sx'),cmds.getAttr(p+'.sy'),cmds.getAttr(p+'.sz'),type='double3')
        cmds.setAttr(p+'.mtxe',v)
        cmds.setAttr(p+'.mtye',v)
        cmds.setAttr(p+'.mtze',v)
        cmds.setAttr(p+'.xtxe',v)
        cmds.setAttr(p+'.xtye',v)
        cmds.setAttr(p+'.xtze',v)
        cmds.setAttr(p+'.mrxe',v)
        cmds.setAttr(p+'.mrye',v)
        cmds.setAttr(p+'.mrze',v)
        cmds.setAttr(p+'.xrxe',v)
        cmds.setAttr(p+'.xrye',v)
        cmds.setAttr(p+'.xrze',v)
        cmds.setAttr(p+'.msxe',v)
        cmds.setAttr(p+'.msye',v)
        cmds.setAttr(p+'.msze',v)
        cmds.setAttr(p+'.xsxe',v)
        cmds.setAttr(p+'.xsye',v)
        cmds.setAttr(p+'.xsze',v)
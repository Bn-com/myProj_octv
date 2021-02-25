import maya.cmds as cmds

def edo_addSkinCtrlCmd():
    mid='_'
    ctrlName=cmds.textField('edo_skinCtrlUItextField',q=1,text=1)
    if not ctrlName=='':
        if ctrlName[len(ctrlName)-1]=='_':
            mid=''
        cmds.delete(cmds.circle(nr=(0,1,0),r=1.5,n=ctrlName+mid+'CTRL')[1])
        cmds.createNode('joint',n=ctrlName+mid+'JNT',p=ctrlName+mid+'CTRL')
        cmds.group(ctrlName+mid+'CTRL',n='GRP_'+ctrlName+mid+'CTRL')
        cmds.setAttr(ctrlName+mid+'CTRLShape.overrideEnabled',1)
        cmds.setAttr(ctrlName+mid+'CTRLShape.ovc',6)
        return 1
    else:
        sels=cmds.ls(sl=1)
        for sel in sels:
            ##sel=sels[0]
            if '|' in sel:
                cmds.confirmDialog( title='name error', message='this object\'s name is not only,it has nameSpace!,please use the other mode to create control!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
                continue
            if not 'MSH_' in sel:
                button=cmds.confirmDialog( title='name error', message='this object('+sel+')\'s name have not prefix \'MSH_\',click pass and tell modeling rename this object or click create igron it!', button=['create','pass'],defaultButton='Yes', cancelButton='No', dismissString='No')
                if button=='pass':           
                    continue
            bb=cmds.xform(sel,q=1,ws=1,bb=1)
            centerX=(bb[0]+bb[3])*0.5
            centerY=(bb[1]+bb[4])*0.5
            centerZ=(bb[2]+bb[5])*0.5
            if sel[len(sel)-1]=='_':
                mid=''
            cmds.delete(cmds.circle(nr=(0,1,0),r=1.5,n=sel.replace('MSH_','')+mid+'CTRL')[1])
            cmds.createNode('joint',n=sel.replace('MSH_','')+mid+'JNT',p=sel.replace('MSH_','')+mid+'CTRL')
            cmds.group(sel.replace('MSH_','')+mid+'CTRL',n='GRP_'+sel.replace('MSH_','')+mid+'CTRL')
            cmds.setAttr(sel.replace('MSH_','')+mid+'CTRLShape.overrideEnabled',1)
            cmds.setAttr(sel.replace('MSH_','')+mid+'CTRLShape.ovc',6)
            cmds.setAttr('GRP_'+sel.replace('MSH_','')+mid+'CTRL.tx',centerX)
            cmds.setAttr('GRP_'+sel.replace('MSH_','')+mid+'CTRL.ty',centerY)
            cmds.setAttr('GRP_'+sel.replace('MSH_','')+mid+'CTRL.tz',centerZ)   
            
def edo_skinCtrlUI():
    if cmds.window('edo_skinCtrlUI',ex=1):
        cmds.deleteUI('edo_skinCtrlUI')
    cmds.window('edo_skinCtrlUI',t='add CtrlUI',w=400,h=100)
    cmds.columnLayout('edo_skinCtrlUILayout',adjustableColumn=True,rs=10)
    cmds.text('edo_skinCtrlUIText',l='filed the ctrl name:')
    cmds.textField('edo_skinCtrlUItextField')
    cmds.button('edo_skinCtrlUIButton',l='create',c='edo_addSkinCtrlCmd()')
    cmds.showWindow('edo_skinCtrlUI')
    cmds.window('edo_skinCtrlUI',e=1,w=300,h=100)
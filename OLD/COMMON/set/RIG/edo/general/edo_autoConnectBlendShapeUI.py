#-*- coding: utf-8 -*-
import maya.cmds as cmds
import headfile
AutoRigPath = headfile.__file__.replace('headfile.py','RIG/').replace('\\','/')


def edo_autoConnectBlendShapeUI():
    if cmds.window('edo_autoConnectBlendShapeUI',q=1,ex=1):
        cmds.deleteUI('edo_autoConnectBlendShapeUI')
    ui=cmds.loadUI(f=AutoRigPath+'edo/general/edo_autoConnectBlendShapeUI.myuis')
    cmds.showWindow(ui)
    cmds.button('edo_autoConnectBlendShapeUI_BT01',e=1,c='edo_renameBlendShapeMesh()')
    cmds.button('edo_autoConnectBlendShapeUI_BT02',e=1,c='edo_opBlendShapeByFacialCtrl(cmds.ls(sl=1)[0])')
    cmds.button('edo_autoConnectBlendShapeUI_BT03',e=1,c='edo_addBlendShapeAndExpressionsByFacialCtrl(cmds.ls(sl=1)[0])')
    cmds.button('edo_autoConnectBlendShapeUI_BT04',e=1,c='edo_addFollicelPlane()')


def edo_targetIsInBlendShapeWeightId(target,bsnode):
    #target='BS__pSphere1__test_CTRL_up'
    #bsnode='pSphere1__BLENDSHAPE'
    bswc=cmds.blendShape(bsnode,q=1,wc=1)
    for i in range(0,bswc):
        #i=0
        bsattr=cmds.aliasAttr(bsnode+'.weight['+str(i)+']',q=1)
        if bsattr==target:
            return i
    return -1

#edo_addBlendShapeAndExpressionsByFacialCtrl('test_CTRL')
def edo_addBlendShapeAndExpressionsByFacialCtrl(ctrlName):
    #ctrlName='testA_CTRL'
    endstr=ctrlName.split('_')[-1]
    allMeshes=[]
    if endstr=='CTRL':
        upmeshes=cmds.listRelatives(ctrlName+'_up',c=1,type='transform',pa=1)
        dnmeshes=cmds.listRelatives(ctrlName+'_dn',c=1,type='transform',pa=1)
        lfmeshes=cmds.listRelatives(ctrlName+'_lf',c=1,type='transform',pa=1)
        lfupmeshes=cmds.listRelatives(ctrlName+'_lfup',c=1,type='transform',pa=1)
        lfdnmeshes=cmds.listRelatives(ctrlName+'_lfdn',c=1,type='transform',pa=1)
        rtmeshes=cmds.listRelatives(ctrlName+'_rt',c=1,type='transform',pa=1)
        rtupmeshes=cmds.listRelatives(ctrlName+'_rtup',c=1,type='transform',pa=1)
        rtdnmeshes=cmds.listRelatives(ctrlName+'_rtdn',c=1,type='transform',pa=1)
        fourAxisupmeshes=cmds.listRelatives(ctrlName+'_fourAxisup',c=1,type='transform',pa=1)
        fourAxisdnmeshes=cmds.listRelatives(ctrlName+'_fourAxisdn',c=1,type='transform',pa=1)
        fourAxislfmeshes=cmds.listRelatives(ctrlName+'_fourAxislf',c=1,type='transform',pa=1)
        fourAxisrtmeshes=cmds.listRelatives(ctrlName+'_fourAxisrt',c=1,type='transform',pa=1)
        edo_combineAllList(allMeshes,upmeshes)
        edo_combineAllList(allMeshes,dnmeshes)
        edo_combineAllList(allMeshes,lfmeshes)
        edo_combineAllList(allMeshes,rtmeshes)
        edo_combineAllList(allMeshes,lfupmeshes)
        edo_combineAllList(allMeshes,rtupmeshes)
        edo_combineAllList(allMeshes,lfdnmeshes)
        edo_combineAllList(allMeshes,rtdnmeshes)
        edo_combineAllList(allMeshes,fourAxisupmeshes)
        edo_combineAllList(allMeshes,fourAxisdnmeshes)
        edo_combineAllList(allMeshes,fourAxislfmeshes)
        edo_combineAllList(allMeshes,fourAxisrtmeshes)
        if allMeshes==[] or allMeshes==None:
            return False
    else:
        allMeshes=cmds.listRelatives(ctrlName,c=1,type='transform',pa=1)
    bsnodes=[]
    targetMesh=''
    for m in allMeshes:
        #m=allMeshes[0]
        print m
        if 'connectCurve' in m:
            continue
        targetMesh=m.split('__')[1]+'_'
        if cmds.objExists(targetMesh):
            BSname=targetMesh+'_BLENDSHAPE'
            if not BSname in bsnodes:
                bsnodes.append(BSname)
            if not cmds.objExists(BSname):
                bsnode=cmds.blendShape(targetMesh,frontOfChain=1,n=BSname)
            wc=cmds.blendShape(BSname,q=1,wc=1)
            output=cmds.listConnections(m+'.worldMesh[0]',s=0,d=1,type='blendShape')
            if not output==None:
                if not BSname in cmds.listConnections(m+'.worldMesh[0]',s=0,d=1,type='blendShape'):
                    cmds.blendShape(BSname,e=1,t=[targetMesh,wc,m,1.0])
            else:
                id=edo_targetIsInBlendShapeWeightId(m,BSname)
                if id==-1:
                    cmds.blendShape(BSname,e=1,t=[targetMesh,wc,m,1.0])
                else:
                    cmds.blendShape(BSname,e=1,ib=True,t=[targetMesh,id,m,1.0])
    print 'get expression...'
    for bsnode in bsnodes:
        #bsnode=bsnodes[0]
        exname=ctrlName+'__'+bsnode.replace('_BLENDSHAPE','_EXPRESSION')
        extext='//'+exname+'\n'
        extext+='//don\'t write custom expression in here!,the script will delete this scirpt first before create a new expression\n\n'
        if cmds.objExists(exname):
            cmds.delete(exname)
        bsattrlen=cmds.blendShape(bsnode,q=1,wc=1)
        for i in range(0,bsattrlen):
            #i=1
            print i
            ctrlattrname=''
            if endstr=='CTRL':
                bsattr=cmds.aliasAttr(bsnode+'.weight['+str(i)+']',q=1)
                m=bsattr
                bsattrname=bsnode+'.'+m
                print m
                if not ctrlName in m or '___' in m:
                    print m+' ... pass'
                    continue
                else:
                    print m+' ... addex'
                    ctrlattrname=m.split('__')[len(m.split('__'))-1]
                    ctrlattrname=ctrlattrname.replace('CTRL_','FRAME.')
                    ctrlattrname=ctrlattrname.replace('fourAxis','fourAxis_')
                    extext+=bsattrname+'='+ctrlattrname+';\n'
            else:
                bsattr=cmds.aliasAttr(bsnode+'.weight['+str(i)+']',q=1)
                m=bsattr
                bsattrname=bsnode+'.'+m
                print m
                if not ctrlName in m:
                    print m+' ... pass'
                    continue
                else:
                    print m+' ... addex'
                    tmp=m.split('___')
                    st=tmp[0].split('__')[-1]
                    tmp.remove(tmp[0])
                    ctrlattrname=st
                    for t in tmp:
                        ctrlattrname+=('___'+t)
                    ctrlattrname=ctrlattrname+'.multiplyValue'
                    extext+=bsattrname+'='+ctrlattrname+';\n'
        print 'add expression'
        print exname+' : \n'+extext+'\n'
        cmds.expression(n=exname,s=extext)

def edo_combineAllList(finalList,combineList):
    if combineList==None or combineList==[]:
        return finalList
    finalList+=combineList

def edo_attrIsInBlendShape(bsname,attrname):
    #bsname='MSH_body_new__BLENDSHAPE'
    #attrname='BS__MSH_body_new__Lfeyebrows_CTRL_rtup'
    wc=cmds.blendShape(bsname,q=1,wc=1)
    for i in range(0,wc):
        #i=0
        atname=bsname+'.weight['+str(i)+']'
        atlname=cmds.aliasAttr(atname,q=1)
        if atlname==attrname:
            return i
    return -1
    
    

def edo_renameBlendShapeMesh():
    sels=cmds.ls(sl=1)
    if sels==None:
        return False
    tn=sels[len(sels)-1]
    if not tn[len(tn)-1]=='_':
        cmds.confirmDialog( title='Ŀ��ģ���������淶', message='Ŀ��ģ�ͺ�׺û��\'_\',��֪ͨģ�����!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    sels.remove(tn)
    for s in sels:
        en=tn.split('|')[len(tn.split('|'))-1]
        nn=cmds.rename(s,'BS__'+en+'_xxxx')
        print 'rename  ...  '+s+'  ...  to  ...  '+nn+'\n'
     
#edo_opBlendShapeByFacialCtrl(cmds.ls(sl=1)[0])
def edo_opBlendShapeByFacialCtrl(ctrlName):
    #ctrlName='Lfmouth_CTRL_fourAxis_dn___Lfdnmouth_sneer_CTRL_dn'
    endstr=ctrlName.split('_')[-1]
    if endstr=='CTRL':
        edo_setBlendShapeMeshTransform(ctrlName+'_up')
        edo_setBlendShapeMeshTransform(ctrlName+'_dn')
        edo_setBlendShapeMeshTransform(ctrlName+'_lf')
        edo_setBlendShapeMeshTransform(ctrlName+'_rt')
        edo_setBlendShapeMeshTransform(ctrlName+'_lfup')
        edo_setBlendShapeMeshTransform(ctrlName+'_lfdn')
        edo_setBlendShapeMeshTransform(ctrlName+'_rtup')
        edo_setBlendShapeMeshTransform(ctrlName+'_rtdn')
        edo_setBlendShapeMeshTransform(ctrlName+'_fourAxisup')
        edo_setBlendShapeMeshTransform(ctrlName+'_fourAxisdn')
        edo_setBlendShapeMeshTransform(ctrlName+'_fourAxislf')
        edo_setBlendShapeMeshTransform(ctrlName+'_fourAxisrt')
        #
        edo_renameBlendShapeMeshByFrame(ctrlName+'_up')
        edo_renameBlendShapeMeshByFrame(ctrlName+'_dn')
        edo_renameBlendShapeMeshByFrame(ctrlName+'_lf')
        edo_renameBlendShapeMeshByFrame(ctrlName+'_rt')
        edo_renameBlendShapeMeshByFrame(ctrlName+'_lfup')
        edo_renameBlendShapeMeshByFrame(ctrlName+'_lfdn')
        edo_renameBlendShapeMeshByFrame(ctrlName+'_rtup')
        edo_renameBlendShapeMeshByFrame(ctrlName+'_rtdn')
        edo_renameBlendShapeMeshByFrame(ctrlName+'_fourAxisup')
        edo_renameBlendShapeMeshByFrame(ctrlName+'_fourAxisdn')
        edo_renameBlendShapeMeshByFrame(ctrlName+'_fourAxislf')
        edo_renameBlendShapeMeshByFrame(ctrlName+'_fourAxisrt')
    else:
        edo_setBlendShapeMeshTransform(ctrlName)
        edo_renameBlendShapeMeshByFrame(ctrlName)
    cmds.select(ctrlName,r=1)
        

def edo_renameBlendShapeMeshByFrame(frameName):
    #frameName='Lfmouth_sneer_CTRL_up___Lfmouth_CTRL_rt'
    if not cmds.objExists('GRP_wrongNameBlendShapes'):
        cmds.createNode('transform',n='GRP_wrongNameBlendShapes')
    childs=cmds.listRelatives(frameName,s=0,c=1,pa=1,type='transform')
    if childs==None:
        return False
    for c in childs:
        #c=childs[1]
        if c.split('_')[-1]=='connectCurve':
            print 'pass connectCurve'
            continue
        if cmds.nodeType(c)=='transform':
            tc=c.split('|')[-1]
            objname=tc.split('__')[1]
            if not cmds.objExists(objname+'_'):
                cmds.parent(c,'GRP_wrongNameBlendShapes')
                continue
            newname=edo_removeLastStr(c,'__')+frameName
            nn=newname.split('|')[len(newname.split('|'))-1]
            cmds.rename(c,nn)

                
def edo_removeLastStr(name,flag='_'):
    #name='face_CTRL_up|BS__MSH_facial__xxxx'
    #flag='__'
    sn=name.split(flag)
    rn=''
    for i in range(0,len(sn)-1):
        rn+=sn[i]+flag
    return rn
        
        
    
def edo_setBlendShapeMeshTransform(frameName):
    #frameName='Lfmouth_CTRL_fourAxis_dn___Lfdnmouth_sneer_CTRL_dn'
    po=cmds.xform(frameName,q=1,ws=1,t=1)
    if not cmds.objExists('GRP_wrongNameBlendShapes'):
        cmds.createNode('transform',n='GRP_wrongNameBlendShapes')
    childs=cmds.listRelatives(frameName,type='transform',c=1,pa=1)
    if childs==None:
        return False
    for c in childs:
        #c=childs[2]
        if c.split('_')[-1]=='connectCurve':
            print 'pass connectCurve'
            continue
        if cmds.nodeType(c)=='transform':
            tc=c.split('|')[-1]
            oc=tc.split('__')
            if not cmds.objExists(oc[1]+'_'):
                cmds.parent(c,'GRP_wrongNameBlendShapes')
                continue
            if 'BS__' in c:
                cmds.xform(c,ws=1,t=po)
            else:
                cmds.parent(c,'GRP_wrongNameBlendShapes')


def edo_addFollicelPlane():
    sels=cmds.ls(sl=1)
    if sels:
        for s in sels:
            #s=sels[0]
            mesh=cmds.polyPlane(n='FCM_'+s,sw=1,sh=1)
            #cmds.delete(mesh[1])
            #f=cmds.createNode('follicle',n=mesh[0]+'_follicleShape')
            #fo=cmds.listRelatives(f,p=1,pa=1)[0]
            #cmds.rename(fo,mesh[0]+'_follicle')
            #cmds.connectAttr(mesh[0]+'.outMesh',f+'.inputMesh',f=1)
            #cmds.connectAttr(mesh[0]+'.worldMatrix',f+'.inputWorldMatrix',f=1)
            #cmds.connectAttr(f+'.outTranslate',mesh[0]+'_follicle.translate',f=1)
            #cmds.connectAttr(f+'.outRotate',mesh[0]+'_follicle.rotate',f=1)
            #cmds.setAttr(f+'.parameterU',0.5)
            #cmds.setAttr(f+'.parameterV',0.5)
            cmds.delete(cmds.parentConstraint(s,mesh[0],mo=0))
            cmds.makeIdentity(mesh[0],apply=1,t=1,r=1,s=1,n=0)
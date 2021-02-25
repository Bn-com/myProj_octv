import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om

execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_facialCtrl.py')
execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_autoConnectBlendShapeUI.py')

def edo_autoConnectBlendshapesInbetweenUI():
    ui='F:/autoConnectBlendshapes.myuis'
    if cmds.window('edo_autoConnectBlendshapesInbetweenUI',ex=1):
        cmds.deleteUI('edo_autoConnectBlendshapesInbetweenUI')
    mui=cmds.loadUI(f=ui)
    cmds.showWindow(mui)
    cmds.button('createCtrlBt',e=1,c='edo_addFacialCtrlCmd(\'\')')
    cmds.button('addMultiplyFrameBt',e=1,c='edo_addMultiplyFrame(cmds.ls(sl=1))')
    cmds.button('renameBt',e=1,c='edo_renameBlendShapeMeshInbetween()')
    cmds.button('autoConnectBt',e=1,c='edo_autoConnectBlendshapes()')
    cmds.button('attachMeshBt',e=1,c='edo_addFollicelPlane()')
    cmds.button('blendshapeNameBt',e=1,c='edo_getSelectedBlendshape()')
    cmds.textScrollList('blendshapeListLw',e=1,sc='edo_getBlendshapeAttrInbetweenList()')
    cmds.button('pickupSelectedBlendshapeBt',e=1,c='edo_pickupSelectedBlendshape()')
    cmds.button('pickupAllBlendshapeBt',e=1,c='edo_pickupSelectedBlendshape(1)')

def edo_autoConnectBlendshapes():
    sels=cmds.ls(sl=1)
    if not sels:
        cmds.confirmDialog( title='��Ҫѡ�������', message='��Ҫѡ���������ִ������', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    edo_opBlendShapeByFacialCtrlInbetween(sels[0])
    edo_addBlendShapeAndExpressionsByFacialCtrlInbetween(sels[0])
    
def edo_renameBlendShapeMeshInbetween():
    sels=cmds.ls(sl=1)
    if sels:
        #cmds.objectTypeUI('inbetweenDsb')
        inbetween=str(int(float(cmds.textField('inbetweenDsb',q=1,tx=1))*1000+5000))
        if sels==None:
            return False
        tn=sels[len(sels)-1]
        if not tn[len(tn)-1]=='_':
            cmds.confirmDialog( title='Ŀ��ģ���������淶', message='Ŀ��ģ�ͺ�׺û��\'_\',��֪ͨģ�����!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        sels.remove(tn)
        for s in sels:
            #s=sels[0]
            en=tn.split('|')[len(tn.split('|'))-1]
            nn=cmds.rename(s,'BS__'+en+'_'+inbetween+'__xxxx')
            print 'rename  ...  '+s+'  ...  to  ...  '+nn+'\n'
        
def edo_opBlendShapeByFacialCtrlInbetween(ctrlName):
    #ctrlName='aaa_CTRL'
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
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_up')
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_dn')
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_lf')
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_rt')
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_lfup')
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_lfdn')
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_rtup')
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_rtdn')
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_fourAxisup')
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_fourAxisdn')
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_fourAxislf')
        edo_renameBlendShapeMeshByFrameInbetween(ctrlName+'_fourAxisrt')
    else:
        edo_setBlendShapeMeshTransform(ctrlName)
        edo_renameBlendShapeMeshByFrame(ctrlName)
    cmds.select(ctrlName,r=1)
    
def edo_renameBlendShapeMeshByFrameInbetween(frameName):
    #frameName=ctrlName+'_up'
    if not cmds.objExists('GRP_wrongNameBlendShapes'):
        cmds.createNode('transform',n='GRP_wrongNameBlendShapes')
    childs=cmds.listRelatives(frameName,s=0,c=1,pa=1,type='transform')
    if childs==None:
        return False
    for c in childs:
        #c=childs[0]
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
            
#edo_addBlendShapeAndExpressionsByFacialCtrl('test_CTRL')
def edo_addBlendShapeAndExpressionsByFacialCtrlInbetween(ctrlName):
    #ctrlName='aaa_CTRL'
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
    for mm in allMeshes:
        #mm=allMeshes[1]
        if 'connectCurve' in mm:
            continue
        targetMesh=mm.split('__')[1]+'_'
        targetCtrl=mm.split('__')[-1]
        if cmds.objExists(targetMesh) and cmds.objExists(targetCtrl):
            BSname=targetMesh+'_BLENDSHAPE'
            m=cmds.rename(mm,edo_splitBlendshapeWeightStr(mm,'6000'))
            print m
            if m[-1].lower()==m[-1].upper():
                print m+'... is a wrong named target,passed...'
                continue
            if len(m.split('__'))==4 and m.split('__')[2].upper()==m.split('__')[2].lower():
                print 'add inbetween...'
                if not BSname in bsnodes:
                    bsnodes.append(BSname)
                if not cmds.objExists(BSname):
                    bsnode=cmds.blendShape(targetMesh,frontOfChain=1,n=BSname)
                wc=cmds.blendShape(BSname,q=1,wc=1)
                attrname=edo_splitBlendshapeWeightStr(m,m.split('__')[2])
                id=edo_targetIsInBlendShapeWeightId(attrname,BSname)
                wv=(float(m.split('__')[2])-5000)/1000
                output=cmds.listConnections(m+'.worldMesh[0]',s=0,d=1,type='blendShape')
                if not output==None:
                    if not BSname in cmds.listConnections(m+'.worldMesh[0]',s=0,d=1,type='blendShape'):
                        if id==-1:
                            cmds.blendShape(BSname,e=1,t=[targetMesh,wc,m,wv])
                        else:
                            cmds.blendShape(BSname,e=1,ib=True,t=[targetMesh,id,m,mv])
                        try:
                            cmds.aliasAttr(attrname,BSname+'.weight['+str(wc)+']')
                        except:
                            print 'pass aliasAttr...'
                else:
                    if id==-1:
                        cmds.blendShape(BSname,e=1,t=[targetMesh,wc,m,wv])
                    else:
                        cmds.blendShape(BSname,e=1,ib=True,t=[targetMesh,id,m,wv])
                    try:
                        cmds.aliasAttr(attrname,BSname+'.weight['+str(wc)+']')
                    except:
                        print 'pass aliasAttr...'
            else:
                if not BSname in bsnodes:
                    bsnodes.append(BSname)
                if not cmds.objExists(BSname):
                    bsnode=cmds.blendShape(targetMesh,frontOfChain=1,n=BSname)
                #attrname=edo_splitBlendshapeWeightStr(m,m.split('__')[2])
                id=edo_targetIsInBlendShapeWeightId(m,BSname)
                wc=cmds.blendShape(BSname,q=1,wc=1)
                output=cmds.listConnections(m+'.worldMesh[0]',s=0,d=1,type='blendShape')
                if not output==None:
                    if not BSname in cmds.listConnections(m+'.worldMesh[0]',s=0,d=1,type='blendShape'):
                        cmds.blendShape(BSname,e=1,t=[targetMesh,wc,m,1.0])
                else:
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
        
def edo_splitBlendshapeWeightStr(bsmesh,weight):
    #bsmesh='BS__pSphere1__6000__aaa_CTRL_up'
    sp=bsmesh.split('__')
    rbsmesh=''
    if not sp[2]==weight:
        rbsmesh=bsmesh
        return rbsmesh
    for t in range(0,len(sp)):
        if t==2:
            continue
        rbsmesh=rbsmesh+sp[t]+'__'
    print rbsmesh[:-2]
    return rbsmesh[:-2]
    
def edo_getSelectedBlendshape():
    sels=cmds.ls(sl=1,type='blendShape')
    if sels:
        sel=sels[0]
        cmds.textField('blendshapeNameLe',e=1,tx=sel)
        edo_getBlendshapeAttrList(sel)
        
def edo_getBlendshapeAttrList(blendshape):
    #blendshape='pSphere1__BLENDSHAPE'
    wc=cmds.blendShape(blendshape,q=1,wc=1)
    attrlist=[]
    cmds.textScrollList('blendshapeListLw',e=1,ra=1)
    for w in range(0,wc):
        #w=0
        attr=blendshape+'.weight['+str(w)+']'
        aattr=cmds.aliasAttr(attr,q=1)
        if not aattr in attrlist:
            attrlist.append(aattr)
            cmds.textScrollList('blendshapeListLw',e=1,a=aattr)
            
def edo_getBlendshapeAttrInbetweenList():
    print 'getBlendshapeAttrInbetweenList...'
    bsname=cmds.textField('blendshapeNameLe',q=1,tx=1)
    cmds.textScrollList('inbetweenListLw',e=1,ra=1)
    #bsname='pSphere1__BLENDSHAPE'
    sis=cmds.textScrollList('blendshapeListLw',q=1,si=1)
    if sis:
        si=sis[0]
        id=edo_targetIsInBlendShapeWeightId(si,bsname)
        #.inputTarget[0].inputTargetGroup[0].inputTargetItem[6000].inputGeomTarget
        attrname=bsname+'.inputTarget[0].inputTargetGroup['+str(id)+'].inputTargetItem'
        attrlist=cmds.getAttr(attrname,mi=1)
    for a in attrlist:
        cmds.textScrollList('inbetweenListLw',e=1,a=str(a)+':'+str(((float(a)-5000)/1000)))
        
def edo_pickupSelectedBlendshape(all=0):
    sels=cmds.ls(sl=1,type='transform')
    if not sels:
        return False
    sel=sels[0]
    cb=cmds.checkBox('keepConnectionCb',q=1,v=1)
    bsname=cmds.textField('blendshapeNameLe',q=1,tx=1)
    selectAttrs=''
    selectAttrs=cmds.textScrollList('blendshapeListLw',q=1,si=1)
    if all==1:
        print 'get all blendshape...'
        selectAttrs=cmds.textScrollList('blendshapeListLw',q=1,ai=1)
    if selectAttrs:
        for si in selectAttrs:
            #si=selectAttrs[0]
            cmds.textScrollList('blendshapeListLw',e=1,si=si)
            edo_getBlendshapeAttrInbetweenList()
            inbetweenList=cmds.textScrollList('inbetweenListLw',q=1,ai=1)
            input=cmds.listConnections(bsname+'.'+si,d=0,s=1,p=1)
            if input:
                cmds.disconnectAttr(input[0],bsname+'.'+si)
            id=edo_targetIsInBlendShapeWeightId(si,bsname)
            attrname=bsname+'.inputTarget[0].inputTargetGroup['+str(id)+'].inputTargetItem'
            for ib in inbetweenList:
                #ib=inbetweenList[0]
                t=ib.split(':')
                p=t[0]
                w=float(t[1])
                cmds.setAttr(bsname+'.'+si,w)
                mname=si.replace(sel,sel+'_'+p+'_')
                tm=cmds.duplicate(sel,n=mname)[0]
                cmds.setAttr(bsname+'.'+si,0.0)
                frame=tm.split('__')[-1]
                if frame==tm:
                    tm=cmds.rename(tm,sel+'_'+p)
                if cmds.objExists(frame):
                    cmds.parent(tm,frame)
                    edo_setBlendShapeMeshTransform(frame)
                else:
                    try:
                        cmds.parent(tm,w=1)
                    except:
                        print tm+'... has already parent in world!'
                    bb=cmds.xform(sel,q=1,os=1,bb=1)
                    print bb
                    h=bb[4]-bb[1]
                    print h
                    cmds.move(0,h*1.2,0,tm,r=1,os=1,ws=1)
                if cb==1:
                    cmds.connectAttr(tm+'.worldMesh[0]',bsname+'.inputTarget[0].inputTargetGroup['+str(id)+'].inputTargetItem['+p+'].inputGeomTarget',f=1)
            if input:
                cmds.connectAttr(input[0],bsname+'.'+si,f=1)
  
edo_autoConnectBlendshapesInbetweenUI()
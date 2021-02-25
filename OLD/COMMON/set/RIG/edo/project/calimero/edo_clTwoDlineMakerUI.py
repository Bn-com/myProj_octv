import maya.cmds as cmds
import maya.mel as mel

global edp_2dcurvePositions

def edo_loadSlectedAttribute(lineedit):
    sels=cmds.ls(sl=1)
    if sels==None or sels==[]:
        cmds.confirmDialog( title='error', message='please select something!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    sel=sels[0]
    attr=cmds.channelBox('MayaWindow|MainChannelsLayersLayout|ChannelsLayersPaneLayout|ChannelBoxForm|menuBarLayout1|frameLayout1|mainChannelBox',q=1,sma=1)
    if attr==None:
        cmds.confirmDialog( title='error', message='please select something and its attribute in channelbox!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if not len(attr)==1:
        cmds.confirmDialog( title='error', message='please select only one attribute!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    attrname=sel+'.'+attr[0]
    cmds.textField(lineedit,e=1,text=attrname)

def edo_loadSlectedObject(lineedit):
    sels=cmds.ls(sl=1)
    if sels==None or sels==[]:
        cmds.confirmDialog( title='error', message='please select something!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    sel=sels[0]
    attr=cmds.channelBox('MayaWindow|MainChannelsLayersLayout|ChannelsLayersPaneLayout|ChannelBoxForm|menuBarLayout1|frameLayout1|mainChannelBox',q=1,sma=1)
    if attr==None:
        cmds.textField(lineedit,e=1,text=sel)
        return True
    if not len(attr)==1:
        cmds.confirmDialog( title='error', message='please select only one attribute!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    attrname=sel+'.'+attr[0]
    cmds.textField(lineedit,e=1,text=attrname)

def edo_findAllcurve():
    cmds.textScrollList('twodcurvelist',e=1,ra=1)
    if not cmds.objExists('twoDline_curve'):
        cmds.textScrollList('twodcurvelist',e=1,a='set is not exists')
        return False
    curves=cmds.sets('twoDline_curve',q=1)
    if curves==None:
        return False
    for c in curves:
        cmds.textScrollList('twodcurvelist',e=1,a=c)
        
        
def edo_findAllstroke():
    cmds.textScrollList('twodstrokelist',e=1,ra=1)
    if not cmds.objExists('twoDline_stroke'):
        cmds.textScrollList('twodstrokelist',e=1,a='set is not exists')
        return False
    curves=cmds.sets('twoDline_stroke',q=1)
    if curves==None:
        return False
    for c in curves:
        cmds.textScrollList('twodstrokelist',e=1,a=c)
        

def edo_updataTheList():
    edo_findAllcurve()
    edo_findAllstroke()
    
def edo_clTwoDlineMakerSelectCurveCmd():
    cmds.select(cl=1)
    sels=cmds.textScrollList('twodcurvelist',q=1,si=1)
    try:
        cmds.select(sels,add=1)
    except:
        print "no object"
        
        
def edo_clTwoDlineMakerSelectStrokeCmd():
    cmds.select(cl=1)
    sels=cmds.textScrollList('twodstrokelist',q=1,si=1)
    try:
        cmds.select(sels,add=1)
    except:
        print "no object"
        
        
def edo_clTwoDlineMakerSelectAnimCmd():
    cmds.select(cl=1)
    sels=cmds.textScrollList('animcurvelist',q=1,si=1)
    try:
        cmds.select(sels,add=1)
    except:
        print "no object"
        
    
def edo_createCurveSet():
    sels=cmds.ls(sl=1)
    if sels==[] or sels==None:
        cmds.confirmDialog( title='error', message='please select all the two D line curves!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    if not cmds.objExists('twoDline_curve'):
        cmds.createNode('objectSet',n='twoDline_curve')
    cmds.sets(sels,include='twoDline_curve')
    
def edo_createStrokeSet():
    strokes=[]
    if not cmds.objExists('twoDline_curve'):
        cmds.confirmDialog( title='error', message='the twoDline_curve set can not find,please create this set first!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    curves=cmds.sets('twoDline_curve',q=1)
    if curves==None or curves==[]:
        return False
    for c in curves:
        t=0
        #c=curves[0]
        sts=cmds.listConnections(c+'.worldSpace[0]',s=0,d=1,p=1)
        if not sts==None:
            for st in sts:
                #st=sts[0]
                st=st.split('.')[0]
                if cmds.nodeType(st)=='stroke':
                    print 'pass this curve'
                    t=1
        if t==1:
            continue
        #cmds.createNode('brush',n=c+'_brush')
        #cmds.createNode('transform',n=c+'_stroke')
        #cmds.createNode('stroke',n=c+'_strokeShape',p=c+'_stroke')
        #cmds.connectAttr(c+'_brush.outBrush',c+'_strokeShape.brush',f=1)
        #cmds.connectAttr(c+'.worldSpace[0]',c+'_strokeShape.pathCurve[0].curve',f=1)
        #cmds.connectAttr('time1.outTime',c+'_brush.time',f=1)
        cmds.select(c,r=1)
        mel.eval('AttachBrushToCurves')
        sel=cmds.ls(sl=1)[0]
        cmds.rename(sel,c+'_stroke')
        cmds.setAttr(c+'_stroke'+".pressureScale[0].pressureScale_Interp",2)
        cmds.setAttr(c+'_stroke'+".pressureScale[0].pressureScale_Position",0)
        cmds.setAttr(c+'_stroke'+".pressureScale[0].pressureScale_FloatValue",0)
        cmds.setAttr(c+'_stroke'+".pressureScale[1].pressureScale_Interp",2)
        cmds.setAttr(c+'_stroke'+".pressureScale[1].pressureScale_Position",0.5)
        cmds.setAttr(c+'_stroke'+".pressureScale[1].pressureScale_FloatValue",1)
        cmds.setAttr(c+'_stroke'+".pressureScale[2].pressureScale_Interp",2)
        cmds.setAttr(c+'_stroke'+".pressureScale[2].pressureScale_Position",1)
        cmds.setAttr(c+'_stroke'+".pressureScale[2].pressureScale_FloatValue",0)
        br=cmds.listConnections(c+'_stroke'+'.brush',s=1,d=0)[0]
        cmds.setAttr(br+'.forwardTwist',1)
        mel.eval('setAttr "'+br+'.color1" -type double3 1 1 1 ;')
        if not cmds.attributeQuery('brush_start',n=c+'_stroke',ex=1):
            cmds.addAttr(c+'_stroke',ln='brush_start',sn='bs',at='double',min=0,max=1)
        if not cmds.attributeQuery('key_start',n=c+'_stroke',ex=1):
            cmds.addAttr(c+'_stroke',ln='key_start',sn='ks',at='double',min=-1,max=1) 
        cmds.setAttr(c+'_stroke.bs',e=1,k=1)
        cmds.setAttr(c+'_stroke.bs',1)
        cmds.setAttr(c+'_stroke.ks',e=1,k=1)
        cmds.setAttr(c+'_stroke.ks',0)
        stplug=cmds.createNode('plusMinusAverage',n='PG_'+c+'_stroke_start')
        stmd=cmds.createNode('multiplyDivide',n='MD_'+c+'_stroke_start')
        cmds.connectAttr(c+'_stroke.bs',stplug+'.input3D[0].input3Dx',f=1)
        cmds.setAttr(stplug+'.input3D[1].input3Dx',1)
        cmds.setAttr(stplug+'.operation',2)
        cmds.connectAttr(stplug+'.output3D.output3Dx',stmd+'.input1X',f=1)
        cmds.setAttr(stmd+'.input2X',-0.5)
        ksplug=cmds.createNode('plusMinusAverage',n='PG_'+c+'_key_start')
        cmds.connectAttr(stmd+'.outputX',ksplug+'.input3D[0].input3Dx',f=1)
        cmds.connectAttr(c+'_stroke.ks',ksplug+'.input3D[1].input3Dx',f=1)
        cmds.connectAttr(ksplug+'.output3D.output3Dx',c+'_stroke.minClip',f=1)
        if not cmds.attributeQuery('brush_end',n=c+'_stroke',ex=1):
            cmds.addAttr(c+'_stroke',ln='brush_end',sn='be',at='double',min=0,max=1)
        if not cmds.attributeQuery('key_end',n=c+'_stroke',ex=1):
            cmds.addAttr(c+'_stroke',ln='key_end',sn='ke',at='double',min=-1,max=1) 
        cmds.setAttr(c+'_stroke.be',e=1,k=1)
        cmds.setAttr(c+'_stroke.be',1)
        cmds.setAttr(c+'_stroke.ke',e=1,k=1)
        cmds.setAttr(c+'_stroke.ke',0)
        edmd=cmds.createNode('multiplyDivide',n='MD_'+c+'_stroke_end')
        cmds.connectAttr(c+'_stroke.be',edmd+'.input1X',f=1)
        cmds.setAttr(edmd+'.input2X',0.5)
        edplug=cmds.createNode('plusMinusAverage',n='PG_'+c+'_stroke_end')
        cmds.connectAttr(edmd+'.outputX',edplug+'.input3D[0].input3Dx',f=1)
        cmds.setAttr(edplug+'.input3D[1].input3Dx',0.5)
        keplug=cmds.createNode('plusMinusAverage',n='PG_'+c+'_key_end')
        cmds.connectAttr(edplug+'.output3D.output3Dx',keplug+'.input3D[0].input3Dx',f=1)
        cmds.connectAttr(c+'_stroke.ke',keplug+'.input3D[1].input3Dx',f=1)
        cmds.connectAttr(keplug+'.output3D.output3Dx',c+'_stroke.maxClip',f=1)
        strokes.append(c+'_stroke')
    print strokes
    if not strokes==[]:
        if not cmds.objExists('twoDline_stroke'):
            cmds.createNode('objectSet',n='twoDline_stroke')
        cmds.sets(strokes,include='twoDline_stroke')

def edo_dirvenAll():
    driven=cmds.textField('lineEdit',q=1,text=1)
    if driven=='':
        cmds.confirmDialog( title='error', message='set the driver attribute first,please!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    curves=cmds.sets('twoDline_curve',q=1)
    strokes=cmds.sets('twoDline_stroke',q=1)
    for c in curves:
        #c=curves[0]
        tw=edo_findtweak(c)
        cmds.select(c,r=1)
        mel.eval('SelectCurveCVsAll')
        cvs=cmds.ls(sl=1)[0]
        cvs=cmds.ls(cvs,fl=1)
        cvnum=len(cvs)
        for i in range(0,cvnum):
            #i=0
            twx=tw+'.plist[0].controlPoints['+str(i)+'].xValue'
            twy=tw+'.plist[0].controlPoints['+str(i)+'].yValue'
            twz=tw+'.plist[0].controlPoints['+str(i)+'].zValue'
            cmds.setDrivenKeyframe(twx,cd=driven)
            cmds.setDrivenKeyframe(twy,cd=driven)
            cmds.setDrivenKeyframe(twz,cd=driven)
    for s in strokes:
        #s=strokes[0]
        smin=s+'.bs'
        smax=s+'.be'
        cmds.setDrivenKeyframe(smin,cd=driven)
        cmds.setDrivenKeyframe(smax,cd=driven)


def edo_findNodeFromHis(name,type):
    #name='twodline_curve'
    #type='tweak'
    node=''
    hiss=cmds.listHistory(name)
    for his in hiss:
        if cmds.nodeType(his)==type:
            node=his
    return node

#edo_findtweak('twodline_curve2')
def edo_findtweak(name):
    #name='twodline_curve'
    orgs=cmds.listRelatives(name,s=1,ni=0)
    if orgs==None:
        print 'no org node'
    org=orgs[1]
    tw=cmds.listConnections(org+'.worldSpace[0]',s=0,d=1)[0]
    tw=cmds.listConnections(tw+'.outputGeometry',s=0,d=1)[0]
    return tw
    
    
def edo_createTwoDcurveWrap():
    sels=[]
    sels=cmds.ls(sl=1)
    if sels==None or sels==[]:
        cmds.confirmDialog( title='error', message='you need select a mesh of the character\'s head!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    if not len(sels)==1:
        cmds.confirmDialog( title='error', message='you can select only one mesh!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    curves=cmds.sets('twoDline_curve',q=1)
    cmds.select(curves,r=1)
    cmds.select(sels[0],add=1)
    mel.eval('CreateWrap')
    
    
def edo_mirrorTweak():
    sels=cmds.ls(sl=1)
    if sels==None or sels==[]:
        cmds.confirmDialog( title='error', message='select the source curve,then select add the destination curve!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    st=sels[0]
    dt=sels[1]
    cmds.select(st,r=1)
    mel.eval('SelectCurveCVsAll')
    stcvs=cmds.ls(sl=1)[0]
    stcvs=cmds.ls(stcvs,fl=1)
    stcvnum=len(stcvs)
    cmds.select(dt,r=1)
    mel.eval('SelectCurveCVsAll')
    dtcvs=cmds.ls(sl=1)[0]
    dtcvs=cmds.ls(dtcvs,fl=1)
    dtcvnum=len(dtcvs)
    if not stcvnum==dtcvnum:
        cmds.confirmDialog( title='error', message='the source curve\'s cvpoint number is defferent with the destination curve,please check it!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    stw=edo_findtweak(st)
    dtw=edo_findtweak(dt)
    for i in range(0,stcvnum):
        #i=0
        x=cmds.getAttr(stw+'.plist[0].controlPoints['+str(i)+'].xValue')*-1
        y=cmds.getAttr(stw+'.plist[0].controlPoints['+str(i)+'].yValue')
        z=cmds.getAttr(stw+'.plist[0].controlPoints['+str(i)+'].zValue')
        cmds.setAttr(dtw+'.plist[0].controlPoints['+str(i)+'].xValue',x)
        cmds.setAttr(dtw+'.plist[0].controlPoints['+str(i)+'].yValue',y)
        cmds.setAttr(dtw+'.plist[0].controlPoints['+str(i)+'].zValue',z)
    cmds.select(sels)


def edo_saveCvPosition():
    global edp_2dcurvePositions
    xs=[]
    ys=[]
    zs=[]
    sel=cmds.ls(sl=1)[0]
    tw=edo_findtweak(sel)
    mel.eval('SelectCurveCVsAll')
    cvs=cmds.ls(sl=1)[0]
    cvs=cmds.ls(cvs,fl=1)
    cvnum=len(cvs)
    for i in range(0,cvnum):
        xs.append(cmds.getAttr(tw+'.plist[0].controlPoints['+str(i)+'].xValue'))
        ys.append(cmds.getAttr(tw+'.plist[0].controlPoints['+str(i)+'].yValue'))
        zs.append(cmds.getAttr(tw+'.plist[0].controlPoints['+str(i)+'].zValue'))
    positions=[xs,ys,zs]
    print positions
    edp_2dcurvePositions=positions
        
        
def edo_loadCvPosition():
    global edp_2dcurvePositions
    xs=edp_2dcurvePositions[0]
    ys=edp_2dcurvePositions[1]
    zs=edp_2dcurvePositions[2]
    sel=cmds.ls(sl=1)[0]
    tw=edo_findtweak(sel)
    mel.eval('SelectCurveCVsAll')
    cvs=cmds.ls(sl=1)[0]
    cvs=cmds.ls(cvs,fl=1)
    cvnum=len(cvs)
    if not cvnum==len(xs):
        cmds.confirmDialog( title='error', message='the data is defferent with select curve!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    for i in range(0,cvnum):
        cmds.setAttr(tw+'.plist[0].controlPoints['+str(i)+'].xValue',xs[i])
        cmds.setAttr(tw+'.plist[0].controlPoints['+str(i)+'].yValue',ys[i])
        cmds.setAttr(tw+'.plist[0].controlPoints['+str(i)+'].zValue',zs[i])
        
        
def edo_selectStrokFromCurve():
    sels=cmds.textScrollList('twodcurvelist',q=1,si=1)
    cmds.textScrollList('twodstrokelist',e=1,da=1)
    cmds.textScrollList('twodcurvelist',q=1,da=1)
    cmds.select(cl=1)
    for sel in sels:
        #sel=sels[0]
        sel=sel+'_stroke'
        cmds.textScrollList('twodstrokelist',e=1,si=sel)
        cmds.select(sel,add=1)
        
def edo_selectCurveFromStroke():
    sels=cmds.textScrollList('twodstrokelist',q=1,si=1)
    cmds.textScrollList('twodcurvelist',e=1,da=1)
    cmds.textScrollList('twodstrokelist',q=1,da=1)
    cmds.select(cl=1)
    for sel in sels:
        #sel=sels[0]
        sel=sel.replace('_stroke','')
        cmds.textScrollList('twodcurvelist',e=1,si=sel)
        cmds.select(sel,add=1)
        
def edo_mirrorStroke():
    sels=cmds.ls(sl=1)
    if sels==None or sels==[]:
        cmds.confirmDialog( title='error', message='select the source curve,then select add the destination curve!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    st=sels[0]+'_stroke'
    dt=sels[1]+'_stroke'
    cmds.setAttr(dt+'.bs',cmds.getAttr(st+'.bs'))
    cmds.setAttr(dt+'.be',cmds.getAttr(st+'.be'))
    
def edo_convertCurveWarpTarget():
    sels=cmds.ls(sl=1)
    if sels==None or sels==[]:
        cmds.confirmDialog( title='error', message='select the source curve,then select add the destination curve!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    st=sels[1]
    dt=sels[0]
    #===createWrap===
    #warp=edo_findNodeFromHis(st,'wrap')
    #wmesh=cmds.listConnections(warp+'.driverPoints',s=1,d=0)
    #cmds.select(dt)
    #cmds.select(wmesh[0],add=1)
    #nwarp=mel.eval('CreateWrap')
    #nwarp=edo_findNodeFromHis(dt,'wrap')
    #================
    tw=edo_findtweak(st)
    cmds.select(st)
    mel.eval('SelectCurveCVsAll')
    stcvs=cmds.ls(sl=1)[0]
    stcvs=cmds.ls(stcvs,fl=1)
    stcvnum=len(stcvs)
    id=0
    for stcv in stcvs:
        #stcv=stcvs[3]
        dtcv=stcv.replace(st,dt)
        stcvp=cmds.xform(stcv,q=1,ws=1,t=1)
        dtcvp=cmds.xform(dtcv,q=1,ws=1,t=1)
        addp=[dtcvp[0]-stcvp[0],dtcvp[1]-stcvp[1],dtcvp[2]-stcvp[2]]
        cmds.setAttr(tw+'.plist[0].controlPoints['+str(id)+'].xValue',(cmds.getAttr(tw+'.plist[0].controlPoints['+str(id)+'].xValue')+addp[0]))
        cmds.setAttr(tw+'.plist[0].controlPoints['+str(id)+'].yValue',(cmds.getAttr(tw+'.plist[0].controlPoints['+str(id)+'].yValue')+addp[1]))
        cmds.setAttr(tw+'.plist[0].controlPoints['+str(id)+'].zValue',(cmds.getAttr(tw+'.plist[0].controlPoints['+str(id)+'].zValue')+addp[2]))
        id=id+1
    cmds.delete(dt)

def edo_findAnimationCurveFormAttribute():
    sattr=cmds.textField('lineEdit_4',q=1,text=1)
    cattr=cmds.textField('lineEdit_3',q=1,text=1)
    if sattr==None and cattr==None:
        cmds.confirmDialog( title='error', message='you must load the control attribute and the driven attirbute!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    lens=len(sattr.split('.'))
    node=sattr.split('.')[0]
    shape=cmds.listRelatives(node,s=1,ni=1)
    type=cmds.nodeType(shape)
    acs=[]
    cmds.textScrollList('animcurvelist',e=1,ra=1)
    if type=='nurbsCurve':
        tw=edo_findtweak(node)
        if lens==1:
            bws=cmds.listConnections(tw,s=1,d=0,t='blendWeighted')
            if bws==None or bws==[]:
                cmds.confirmDialog( title='error', message='target attribute has not input node,please check it thanks a lot!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
                return False
            for bw in bws:
                #bw=bws[1]
                print bw
                animcurves=cmds.listConnections(bw,s=1,d=0,type='animCurve')
                for ac in animcurves:
                    #ac='animCurveUU498'
                    input=cmds.listConnections(ac+'.input',s=1,d=0,p=1,scn=1)[0]
                    input=input.replace('.translateX','.tx')
                    input=input.replace('.translateY','.ty')
                    input=input.replace('.translateZ','.tz')
                    input=input.replace('.rotateX','.rx')
                    input=input.replace('.rotateY','.ry')
                    input=input.replace('.rotateZ','.rz')
                    input=input.replace('.scaleX','.sx')
                    input=input.replace('.scaleY','.sy')
                    input=input.replace('.scaleZ','.sz')
                    if input==cattr:
                        acs.append(ac)
                        cmds.textScrollList('animcurvelist',e=1,a=ac)
        if lens==2:
            id=sattr.split('.')[1].replace('cv','')
            twp=tw+'.plist[0].controlPoints'+id
            bwsx=cmds.listConnections(twp+'.xValue',s=1,d=0,t='blendWeighted')
            bwsy=cmds.listConnections(twp+'.yValue',s=1,d=0,t='blendWeighted')
            bwsz=cmds.listConnections(twp+'.zValue',s=1,d=0,t='blendWeighted')
            bws=[]
            bws.append(bwsx)
            bws.append(bwsy)
            bws.append(bwsz)
            if bws==None or bws==[]:
                cmds.confirmDialog( title='error', message='target attribute has not input node,please check it thanks a lot!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
                return False
            for bw in bws:
                #bw=bws[0]
                print bw
                animcurves=cmds.listConnections(bw,s=1,d=0,type='animCurve')
                for ac in animcurves:
                    #ac='animCurveUU498'
                    input=cmds.listConnections(ac+'.input',s=1,d=0,p=1,scn=1)[0]
                    input=input.replace('.translateX','.tx')
                    input=input.replace('.translateY','.ty')
                    input=input.replace('.translateZ','.tz')
                    input=input.replace('.rotateX','.rx')
                    input=input.replace('.rotateY','.ry')
                    input=input.replace('.rotateZ','.rz')
                    input=input.replace('.scaleX','.sx')
                    input=input.replace('.scaleY','.sy')
                    input=input.replace('.scaleZ','.sz')
                    if input==cattr:
                        acs.append(ac)
                        cmds.textScrollList('animcurvelist',e=1,a=ac)
        if lens==4:
            id=sattr.split('.')[1].replace('cv','')
            ax=sattr.split('.')[3].replace('v','Value')
            twpc=tw+'.plist[0].controlPoints'+id+'.'+ax
            bws=cmds.listConnections(twpc,s=1,d=0,t='blendWeighted')
            if bws==None or bws==[]:
                cmds.confirmDialog( title='error', message='target attribute has not input node,please check it thanks a lot!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
                return False
            for bw in bws:
                #bw=bws[0]
                print bw
                animcurves=cmds.listConnections(bw,s=1,d=0,type='animCurve')
                for ac in animcurves:
                    #ac='animCurveUU498'
                    input=cmds.listConnections(ac+'.input',s=1,d=0,p=1,scn=1)[0]
                    input=input.replace('.translateX','.tx')
                    input=input.replace('.translateY','.ty')
                    input=input.replace('.translateZ','.tz')
                    input=input.replace('.rotateX','.rx')
                    input=input.replace('.rotateY','.ry')
                    input=input.replace('.rotateZ','.rz')
                    input=input.replace('.scaleX','.sx')
                    input=input.replace('.scaleY','.sy')
                    input=input.replace('.scaleZ','.sz')
                    if input==cattr:
                        acs.append(ac)
                        cmds.textScrollList('animcurvelist',e=1,a=ac)
        return acs
    bws=cmds.listConnections(sattr,s=1,d=0,t='blendWeighted')
    if bws==None or bws==[]:
        cmds.confirmDialog( title='error', message='target attribute has not input node,please check it thanks a lot!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    for bw in bws:
        #bw=bws[1]
        print bw
        animcurves=cmds.listConnections(bw,s=1,d=0,type='animCurve')
        for ac in animcurves:
            #ac='animCurveUU498'
            input=cmds.listConnections(ac+'.input',s=1,d=0,p=1,scn=1)[0]
            input=input.replace('.translateX','.tx')
            input=input.replace('.translateY','.ty')
            input=input.replace('.translateZ','.tz')
            input=input.replace('.rotateX','.rx')
            input=input.replace('.rotateY','.ry')
            input=input.replace('.rotateZ','.rz')
            input=input.replace('.scaleX','.sx')
            input=input.replace('.scaleY','.sy')
            input=input.replace('.scaleZ','.sz')
            if input==cattr:
                acs.append(ac)
                cmds.textScrollList('animcurvelist',e=1,a=ac)
    print acs
    return acs


def edo_setAllStrokeTransformCannotSelected():
    stros=cmds.ls(type='stroke')
    for s in stros:
        #s=stros[0]
        ssh=cmds.listRelatives(s,p=1)[0]
        cmds.setAttr(s+'.overrideEnabled',1)
        cmds.setAttr(s+'.overrideDisplayType',0)
        cmds.setAttr(ssh+'.overrideEnabled',1)
        cmds.setAttr(ssh+'.overrideDisplayType',2)


def edo_changeDrivenAttribute(orgattr,changeattr):
    #orgattr='FV_CTRL.tx'
    #changeattr='FV_FRAME.rt'
    outputs=cmds.listConnections(orgattr,s=0,d=1,p=1)
    for output in outputs:
        #output = outputs[10]
        if 'animCurve' in cmds.nodeType(output):
            print 'connect .. '+changeattr+' .. to .. '+output
            cmds.connectAttr(changeattr,output,f=1)

def edo_clTwoDlineMakerUI():
    if cmds.window('clTwoDlineMakerUI',ex=1):
        cmds.deleteUI('clTwoDlineMakerUI')
    dialog1 = cmds.loadUI(f='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/project/calimero/edo_clTwoDlineMakerUI.myuis')
    cmds.showWindow(dialog1)
    #cmds.window(dialog1,e=1,w=480,h=610)
    cmds.textScrollList('twodcurvelist',e=1,sc='edo_clTwoDlineMakerSelectCurveCmd()',ams=1)
    cmds.popupMenu(b=3,p='twodcurvelist')
    cmds.menuItem(l='find stroke',c='edo_selectStrokFromCurve()')
    cmds.textScrollList('twodstrokelist',e=1,sc='edo_clTwoDlineMakerSelectStrokeCmd()',ams=1)
    cmds.popupMenu(b=3,p='twodstrokelist')
    cmds.menuItem(l='find 2d curve',c='edo_selectCurveFromStroke()')
    cmds.textScrollList('animcurvelist',e=1,sc='edo_clTwoDlineMakerSelectAnimCmd()',ams=1)
    edo_updataTheList()
    edo_setAllStrokeTransformCannotSelected()
edo_clTwoDlineMakerUI()
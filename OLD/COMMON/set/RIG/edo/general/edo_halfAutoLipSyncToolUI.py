import maya.cmds as cmds
import maya.mel as mel
def edo_halfAutoLipSyncToolUI():
    filename=cmds.optionVar(q='edo_halfAutoLipSyncUserSetup')
    edo_halfAutoLipSyncToolUICmd()
    edo_loadhalfAutoLipSyncUserSetup(filename)

def edo_halfAutoLipSyncToolUICmd():
    nameSpace=cmds.optionVar(q='edo_halfAutoLipSyncToolUINameSpace')
    if cmds.window('edo_halfAutoLipSyncToolUI',ex=1):
        cmds.deleteUI('edo_halfAutoLipSyncToolUI')
    dialog1=cmds.loadUI(f='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_halfAutoLipSyncToolUI.myuis')
    cmds.showWindow(dialog1)
    cmds.window(dialog1,e=1,w=300,h=470)
    cmds.button('importvoiceBt',e=1,c='edo_importVoiceCmd()')
    cmds.popupMenu('nameSpacePopupMenu',p='nameSpaceTf')
    cmds.menuItem('nameSpacePopupMenuItem01',p='nameSpacePopupMenu',label='load nameSpace',c='edo_loadNaneSpaceCmd()')
    cmds.textField('nameSpaceTf',e=1,tx=nameSpace)
    cmds.button('addBt',e=1,c='edo_addLipShapeList()')
    cmds.button('subBt',e=1,c='edo_removeLipShapeList()')
    cmds.button('renBt',e=1,c='edo_renameLipShapeList()',vis=0)
    cmds.popupMenu('lipShapeListPopupMenu',p='lipShapeList')
    cmds.menuItem('lipShapeListPopupMenuItem01',p='lipShapeListPopupMenu',label='add  all  select  animCurve',c='edo_addAllSelectAnimCurveToList()')
    cmds.button('saveBt',e=1,c='edo_savehalfAutoLipSyncUserSetup()')
    cmds.button('loadBt',e=1,c='edo_loadhalfAutoLipSyncUserSetupCmd()')
    cmds.button('setKeyFrameBt',e=1,c='edo_setKeyFrameCmd()')
    cmds.button('deleteKeyFrameBt',e=1,c='edo_deleteKeyFrame()')
    cmds.textScrollList('lipShapeList',e=1,sc='edo_lipShapeListChangeCmd()')
    
def edo_deleteKeyFrame():
    bc=edo_loadNaneSpace()
    if bc==False:
        return False
    nameSpace=bc+':'
    allAnimCurve=edo_findAllAnimCurveFromList()
    if allAnimCurve==False:
        return False
    if allAnimCurve==None:
        return False
    for ac in allAnimCurve:
        #ac=allAnimCurve[0]
        acn=nameSpace+ac
        if cmds.objExists(acn):
            ct=cmds.currentTime(query=True)
            cmds.cutKey(acn,clear=True,time=(ct,ct))

def edo_loadNaneSpace():
    sels=cmds.ls(sl=1)
    if sels==None or sels==[]:
        return False
    sel=sels[0]
    tmp=sel.split(':')
    if len(tmp)>1:
        nameSpace=tmp[0]
        return nameSpace

def edo_loadNaneSpaceCmd():
    bc=edo_loadNaneSpace()
    if bc==False:
        return False
    nameSpace=bc+':'
    if not nameSpace==None:
        cmds.textField('nameSpaceTf',e=1,tx=nameSpace)
        cmds.optionVar(sv=('edo_halfAutoLipSyncToolUINameSpace',nameSpace))

def edo_importVoice(filename):
    #filename='Z:/Resource/Groups/Production/Rigging_Simulation/Projects/riggingGroupProject/lipSync/testVoice/test1.wav'
    cmds.file(filename,i=1)
    mel.eval('setPlaybackRangeToSound()')
    
def edo_importVoiceCmd():
    filename=cmds.fileDialog2(dialogStyle=1,fm=1)
    if not filename==None:
        filename=filename[0]
        edo_importVoice(filename)
        
def edo_addLipShapeList():
    newLipShapeDialog=cmds.promptDialog(title='create new lipShape',message='write a new lipShape name',button=['OK', 'Cancel'])
    if newLipShapeDialog=='Cancel':
        return False
    if newLipShapeDialog=='OK':
        texts=cmds.promptDialog(query=True, text=True)
    alllist=cmds.textScrollList('lipShapeList',q=1,ai=1)
    if not alllist==None:
        if texts in alllist:
            cmds.confirmDialog( title='error', message=texts+' is already in this list!,don\'t add this text again!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
            print texts+' is already in this list!,don\'t add this text again!'
            return False
    edo_addLipShapeListCmd(texts)

def edo_addLipShapeListCmd(texts):     
    if not texts=='':
        cmds.textScrollList('lipShapeList',e=1,a=texts)
        cmds.textScrollList('lipShapeList',e=1,si=texts)
        cmds.setParent('animationCurveRow')
        cmds.textScrollList(texts+'_animCurveList',vis=0,sc='edo_animCurveListChangeCmd()')
        cmds.popupMenu(texts+'_animCurveListPopupMenu',p=texts+'_animCurveList')
        cmds.menuItem(texts+'_animCurveListPopupMenuItem01',p=texts+'_animCurveListPopupMenu',label='load animCurve key value from current',c='edo_loadAnimCurveKeyValueFromCurrent()')
    edo_lipShapeListChangeCmd()
        
     
def edo_loadAnimCurveKeyValueFromCurrent():
    #print 'edo_loadAnimCurveKeyValueFromCurrent()'
    nameSpace=cmds.textField('nameSpaceTf',q=1,tx=1)
    lssel=cmds.textScrollList('lipShapeList',q=1,si=1)[0]
    alllist=cmds.textScrollList(lssel+'_animCurveList',q=1,ai=1)
    for l in alllist:
        #l=alllist[0]
        tmp=l.split('_')
        obj=''
        for i in range(len(tmp)-1):
            obj+=tmp[i]+'_'
        obj=nameSpace+obj[:len(obj)-1]
        output=obj+'.'+tmp[-1]
        if cmds.objExists(obj):
            cv=cmds.getAttr(output)
            maxfield=lssel+'_'+l+'_maxFiled'
            if cmds.floatField(maxfield,q=1,ex=1):
                cmds.floatField(maxfield,e=1,v=cv)
        
def edo_lipShapeListChangeCmd():
    alllist=cmds.textScrollList('lipShapeList',q=1,ai=1)
    si=cmds.textScrollList('lipShapeList',q=1,si=1)[0]
    if len(alllist)==0:
        cmds.textScrollList('animCurveList',e=1,vis=1)
    else:
        cmds.textScrollList('animCurveList',e=1,vis=0)
    for l in alllist:
        cmds.textScrollList(l+'_animCurveList',e=1,vis=0)
    cmds.textScrollList(si+'_animCurveList',e=1,vis=1)
    edo_animCurveListChangeCmd()


def edo_removeLipShapeList():
    siis=cmds.textScrollList('lipShapeList',q=1,sii=1)
    if siis==None:
        return False
    sii=siis[0]
    si=cmds.textScrollList('lipShapeList',q=1,si=1)[0]
    alllist=cmds.textScrollList(si+'_animCurveList',q=1,ai=1)
    if not alllist==None:
        for l in alllist:
            cmds.deleteUI(si+'_'+l+'_minFiled')
            cmds.deleteUI(si+'_'+l+'_maxFiled')
    cmds.deleteUI(si+'_animCurveList')
    cmds.textScrollList('lipShapeList',e=1,rii=sii)
    edo_lipShapeListChangeCmd()
    
def edo_renameLipShapeList():
    renameShapeDialog=cmds.promptDialog(title='rename the lipShape name',message='write a new lipShape name',button=['OK', 'Cancel'])
    if renameShapeDialog=='OK': 
        texts=cmds.promptDialog(query=True, text=True)
    sii=cmds.textScrollList('lipShapeList',q=1,sii=1)[0]
    alllist=cmds.textScrollList('lipShapeList',q=1,ai=1)
    cmds.textScrollList('lipShapeList',e=1,ra=1)
    for i in range(0,len(alllist)):
        l=alllist[i]
        if i==sii-1:
            cmds.textScrollList('lipShapeList',e=1,a=texts)
            continue
        cmds.textScrollList('lipShapeList',e=1,a=l)
        
def edo_addAllSelectAnimCurveToList():
    #print 'add all selected animationCurve to right list'
    sels=cmds.ls(sl=1)
    if sels==None or sels==[]:
        cmds.confirmDialog( title='error', message='you must select some object', button=['god it'], defaultButton='Yes', cancelButton='No', dismissString='No')
        return
    kb=''
    sels=cmds.ls(sl=1,type='animCurve')
    if sels==[] or sels==None:
        b=cmds.confirmDialog( title='error', message='you must select some animationCurve node', button=['auto find from select objects!','god it'], defaultButton='Yes', cancelButton='No', dismissString='No')
        if b=='god it':
            return False
        if b=='auto find from select objects!':
            if kb=='':
                kb=cmds.confirmDialog( title='error', message='select Object has no keyframe,do you want auto key it?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            if kb=='No':
                return False
            if kb=='Yes':
                sels=cmds.ls(sl=1)
                edo_findLostAnimCurveFromSelect(sels)
                cmds.setKeyframe(sels,shape=0,controlPoints=0,hierarchy='none',breakdown=0)
                sels=selectAnimCurveNodeFromSelectObject()
    edo_addAllSelectAnimCurveToListCmd(sels)
    edo_loadAnimCurveKeyValueFromCurrent()

def edo_findLostAnimCurveFromSelect(sels):
    for sel in sels:
        #sel='cp_c009001daipa:IY_M'
        keys=cmds.listAttr(sel,k=1)
        for k in keys:
            #k=keys[1]
            ac=sel+'_'+k
            oa=sel+'.'+k
            if cmds.objExists(ac):
                if cmds.listConnections(ac+'.output',s=0,d=1)==None:
                    cmds.connectAttr(ac+'.output',oa,f=1)
            else:
                cmds.cutKey(oa,clear=1)
                cmds.setKeyframe(oa,shape=0,controlPoints=0,hierarchy='none',breakdown=0)

def selectAnimCurveNodeFromSelectObject():
    allAnimCurves=[]
    sels=cmds.ls(sl=1)
    if sels==None:
        cmds.confirmDialog( title='error', message='you must select something', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    for sel in sels:
        #sel=sels[0]
        attrs=cmds.listAttr(sel,k=1)
        if not attrs==None:
            for a in attrs:
                #a=attrs[0]
                animCurves=cmds.listConnections(sel+'.'+a,s=1,d=0,p=0,t='animCurve')
                if not animCurves==None:
                    for ac in animCurves:
                        allAnimCurves.append(ac)
    return allAnimCurves
            
        
def edo_addAllSelectAnimCurveToListCmd(sels):
    sis=cmds.textScrollList('lipShapeList',q=1,si=1)
    if sis==None:
        return False
    si=sis[0]
    alllist=cmds.textScrollList(si+'_animCurveList',q=1,ai=1)
    if not alllist==None:
        for l in alllist:
            if cmds.floatField(si+'_'+l+'_minFiled',q=1,ex=1)==True:
                cmds.deleteUI(si+'_'+l+'_minFiled')
            if cmds.floatField(si+'_'+l+'_maxFiled',q=1,ex=1)==True:
                cmds.deleteUI(si+'_'+l+'_maxFiled')
    cmds.textScrollList(si+'_animCurveList',e=1,ra=1)
    for sel in sels:
        #sel=sels[0]
        tmp=sel.split(':')
        if len(tmp)>1:
            sel=tmp[len(tmp)-1]
        cmds.textScrollList(si+'_animCurveList',e=1,a=sel)
        cmds.setParent('minMaxRow')
        if cmds.floatField(si+'_'+sel+'_minFiled',q=1,ex=1)==False:
            cmds.floatField(si+'_'+sel+'_minFiled',precision=3,step=.01,vis=0)
        if cmds.floatField(si+'_'+sel+'_maxFiled',q=1,ex=1)==False:
            cmds.floatField(si+'_'+sel+'_maxFiled',precision=3,step=.01,v=1.0,vis=0)
    cmds.textScrollList(si+'_animCurveList',e=1,sii=1)
    selanim=cmds.textScrollList(si+'_animCurveList',q=1,si=1)[0]
    cmds.floatField(si+'_'+selanim+'_minFiled',e=1,vis=1)
    cmds.floatField(si+'_'+selanim+'_maxFiled',e=1,vis=1)
    edo_animCurveListChangeCmd()
    
def edo_animCurveListChangeCmd():
    lsalllist=cmds.textScrollList('lipShapeList',q=1,ai=1)
    for lsl in lsalllist:
        #lsl=lsalllist[0]
        alllist=cmds.textScrollList(lsl+'_animCurveList',q=1,ai=1)
        if not alllist==None and not alllist==[]:
            for l in alllist:
                if cmds.floatField(lsl+'_'+l+'_minFiled',q=1,ex=1):
                    cmds.floatField(lsl+'_'+l+'_minFiled',e=1,vis=0)
                if cmds.floatField(lsl+'_'+l+'_maxFiled',q=1,ex=1):
                    cmds.floatField(lsl+'_'+l+'_maxFiled',e=1,vis=0)
    lssi=cmds.textScrollList('lipShapeList',q=1,si=1)[0]
    sis=cmds.textScrollList(lssi+'_animCurveList',q=1,si=1)
    if not sis==None:
        si=sis[0]
        cmds.floatField(lssi+'_'+si+'_minFiled',e=1,vis=1)
        cmds.floatField(lssi+'_'+si+'_maxFiled',e=1,vis=1)
        
def edo_savehalfAutoLipSyncUserSetup():
    print 'save......'
    filename=cmds.fileDialog2(dialogStyle=1,fm=0)
    if not filename==None:
        filename=filename[0].replace('*','lps')
        fobj=open(filename,'w')
        fobj.writelines('//this file use to save the lip shape and the animationCurve data!\n')
        lsalllist=cmds.textScrollList('lipShapeList',q=1,ai=1)
        if lsalllist==None:
            fobj.writelines('//theEnd')
            fobj.close()
            return False
        for lsl in lsalllist:
            #lsl=lsalllist[0]
            acalllist=cmds.textScrollList(lsl+'_animCurveList',q=1,ai=1)
            texts=''
            mins=''
            maxs=''
            if acalllist==None:
                continue
            for acl in acalllist:
                #acl=acalllist[0]
                texts+=acl+' '
                minfield=lsl+'_'+acl+'_minFiled'
                maxfield=lsl+'_'+acl+'_maxFiled'
                if cmds.floatField(minfield,q=1,ex=1):
                    mins+=str(cmds.floatField(minfield,q=1,v=1))+' '
                if cmds.floatField(maxfield,q=1,ex=1):
                    maxs+=str(cmds.floatField(maxfield,q=1,v=1))+' '
            ptext=lsl+':'+texts+':'+mins+':'+maxs+'\n'
            print ptext
            fobj.writelines(ptext)
        fobj.writelines('//theEnd')
        fobj.close()
        
def edo_loadhalfAutoLipSyncUserSetupCmd():
    filename=cmds.fileDialog2(dialogStyle=1,fm=1)
    if not filename==None:
        edo_halfAutoLipSyncToolUICmd()
        edo_loadhalfAutoLipSyncUserSetup(filename[0])
        cmds.optionVar(sv=('edo_halfAutoLipSyncUserSetup',filename[0]))
    
def edo_loadhalfAutoLipSyncUserSetup(filename):
    print 'load......'
    #fileName=
    if not filename==None:
        filename=filename.replace('*','lps') 
        fobj=open(filename,'r')
        t=fobj.readline()
        if t[:66]=='//this file use to save the lip shape and the animationCurve data!':
            texts=''
            while(not texts=='//theEnd'):
                texts=fobj.readline()
                if texts=='//theEnd':
                    break
                #print texts
                lipshape=texts.split(':')[0]
                #print lipshape+'\n'
                animcurves=texts.split(':')[1].split(' ')
                animcurves=animcurves[:len(animcurves)-1]
                #print animcurves
                mins=texts.split(':')[2].split(' ')
                mins=mins[:len(mins)-1]
                maxs=texts.split(':')[3].split(' ')
                maxs=maxs[:len(maxs)-1]
                edo_addLipShapeListCmd(lipshape)
                edo_addAllSelectAnimCurveToListCmd(animcurves)
                id=0
                for ac in animcurves:
                    #ac=animcurves[0]
                    minfield=lipshape+'_'+ac+'_minFiled'
                    minv=float(mins[id])
                    if cmds.floatField(minfield,q=1,ex=1):
                        cmds.floatField(minfield,e=1,v=minv)
                    maxfield=lipshape+'_'+ac+'_maxFiled'
                    maxv=float(maxs[id])
                    if cmds.floatField(maxfield,q=1,ex=1):
                        cmds.floatField(maxfield,e=1,v=maxv)
                    id+=1
        fobj.close()

def edo_findAllAnimCurveFromList():
    allanim=[]
    lsalllist=cmds.textScrollList('lipShapeList',q=1,ai=1)
    if lsalllist==None:
        return False
    for lsl in lsalllist:
        #lsl=lsalllist[0]
        alllist=cmds.textScrollList(lsl+'_animCurveList',q=1,ai=1)
        if alllist==None:
            continue
        for l in alllist:
            if not l in allanim:
                allanim.append(l)
    print allanim
    return allanim
    
    
#ex:edo_getAnimCurveTotalValue('AHH_M_translateZ')
def edo_getAnimCurveTotalValue(animCurve,minOrMax='min'):
    #animCurve='AHH_M_translateZ'
    #minOrMax='max'
    total=0.0
    lsalllist=cmds.textScrollList('lipShapeList',q=1,ai=1)
    for lsl in lsalllist:
        #lsl=lsalllist[0]
        alllist=cmds.textScrollList(lsl+'_animCurveList',q=1,ai=1)
        for l in alllist:
            #l=alllist[0]
            if l==animCurve:
                if minOrMax=='min':
                    minfield=lsl+'_'+l+'_minFiled'
                    if cmds.floatField(minfield,q=1,ex=1):
                        v=cmds.floatField(minfield,q=1,v=1)
                        total+=v
                if minOrMax=='max':
                    maxfield=lsl+'_'+l+'_maxFiled'
                    if cmds.floatField(maxfield,q=1,ex=1):
                        v=cmds.floatField(maxfield,q=1,v=1)
                        total+=v
    #print total
    return total
    
def edo_findAllKeyAttr():
    bc=edo_loadNaneSpace()
    if bc==False:
        return False
    nameSpace=bc+':'
    keyAttr=[]
    aac=edo_findAllAnimCurveFromList()
    for ac in aac:
        #ac=aac[0]
        nac=nameSpace+ac
        tmp=nac.split('_')
        obj=''
        for i in range(0,len(tmp)-1):
            t=tmp[i]
            tx=t+'_'
            obj+=tx
        #print obj
        keyAttr.append(obj[:len(obj)-1]+'.'+tmp[-1])
    return keyAttr
        
def edo_setAllAminCurveMinKey():
    nameSpace=cmds.textField('nameSpaceTf',q=1,tx=1)
    animCurves=edo_findAllAnimCurveFromList()
    if animCurves==False:
        return False
    for a in animCurves:
        #a=animCurves[0]
        min=edo_getAnimCurveTotalValue(a)
        na=nameSpace+a
        if not cmds.objExists(na):
            ak=edo_findAllKeyAttr()
            for k in ak:
                #k=ak[0]
                if not cmds.objExists(k):
                    print 'nameSpace may be wrong!'
                    cmds.confirmDialog( title='error', message='nameSpace may be wrong!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
                    return False
                if cmds.listConnections(k,s=1,d=0,t='animCurve')==None or not cmds.listConnections(k,s=1,d=0,t='animCurve')==k.replace('.','_'):
                    cmds.cutKey(k,clear=1)
                    cmds.setKeyframe(k,v=min)
        cmds.setKeyframe(na,v=min)
        if cmds.listConnections(na+'.output',s=0,d=1)==None:
            tmp=na.split('_')
            obj=''
            for i in range(0,len(tmp)-1):
                t=tmp[i]
                tx=t+'_'
                obj+=tx
            objattr=obj[:len(obj)-1]+'.'+tmp[-1]
            cmds.connectAttr(na+'.output',objattr,f=1)
        #print obj
        print 'set animCurve keyframe    ['+na+']   to   '+str(min)
        
def edo_setCurrentAnimCurveMaxKey():
    nameSpace=cmds.textField('nameSpaceTf',q=1,tx=1)
    current=cmds.textScrollList('lipShapeList',q=1,si=1)[0]
    alllist=cmds.textScrollList(current+'_animCurveList',q=1,ai=1)
    for l in alllist:
        #l=alllist[0]
        nl=nameSpace+l
        maxfield=current+'_'+l+'_maxFiled'
        if cmds.floatField(maxfield,q=1,ex=1):
            v=cmds.floatField(maxfield,q=1,v=1)
            if not cmds.objExists(nl):
                cmds.confirmDialog( title='error', message=nl+' has not keyframe,please key it first!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
                return False
            cmds.setKeyframe(nl,v=v)
            print 'set animCurve keyframe    ['+nl+']   to   '+str(v)
            
def edo_setKeyFrameCmd():
    stat=edo_setAllAminCurveMinKey()
    if stat==False:
        return False
    edo_setCurrentAnimCurveMaxKey()
edo_halfAutoLipSyncToolUI()
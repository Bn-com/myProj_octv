import maya.cmds as cmds
import os
global gpath
import maya.mel as mel
import subprocess
def edo_noLightingToolsUI():
    ui='f:/noLightingToolsUI.myuis'
    if cmds.window('noLightingToolsUI',ex=1):
        cmds.deleteUI('noLightingToolsUI')
    mui=cmds.loadUI(f=ui)
    cmds.showWindow(mui)
    cmds.textField('project_le',e=1,cc='edo_textFieldChangeCmd()')
    cmds.textField('scenes_le',e=1,cc='edo_textFieldChangeCmd()')
    cmds.textField('shot_le',e=1,cc='edo_textFieldChangeCmd()')
    cmds.textField('first_le',e=1,cc='edo_textFieldChangeCmd()')
    cmds.textField('second_le',e=1,cc='edo_textFieldChangeCmd()')
    cmds.textField('third_le',e=1,cc='edo_textFieldChangeCmd()')
    cmds.textScrollList('search_list',e=1,ams=1)
    cmds.textScrollList('pickup_list',e=1,ams=1)
    cmds.popupMenu('pickup_list_popm',p='pickup_list',b=3)
    cmds.menuItem('pickup_list_mi',label='delete selected',parent='pickup_list_popm')
    cmds.menuItem('pickup_list_mi',e=1,c='edo_deleteSelectedMiCmd()')
    cmds.menuItem('pickup_list_mi1',label='delete all',parent='pickup_list_popm')
    cmds.menuItem('pickup_list_mi1',e=1,c='edo_deleteSelectedMi1Cmd()')
    cmds.menuItem('pickup_list_mi2',label='open and optimize',parent='pickup_list_popm')
    cmds.menuItem('pickup_list_mi2',e=1,c='edo_openCmd()')
    cmds.menuItem('pickup_list_mi3',label='optimize all and auto save',parent='pickup_list_popm')
    cmds.menuItem('pickup_list_mi3',e=1,c='edo_doitCmd()')
    cmds.menuItem('pickup_list_mi4',label='open avi',parent='pickup_list_popm')
    cmds.menuItem('pickup_list_mi4',e=1,c='openSelectedShotAvi("pickup_list")')
    cmds.popupMenu('search_list_popm',p='search_list',b=3)
    cmds.menuItem('pickup_list_mi5',label='open avi',parent='search_list_popm')
    cmds.menuItem('pickup_list_mi5',e=1,c='openSelectedShotAvi("search_list")')
    cmds.button('pickup_bt',e=1,bgc=[0.8,0.6,0.2],c='edo_pickUpFilesCmd()')
    #cmds.button('doit_bt',e=1,bgc=[0.5,0.7,0.3],c='edo_doitCmd()')
    cmds.button('save_bt',e=1,bgc=[0.8,0.4,0.2],c='edo_saveRenderingFiles()')
    edo_textFieldChangeCmd()
edo_noLightingToolsUI()


def openSelectedShotAvi(listname):
    global gpath
    #listname='pickup_list'
    allfiles=cmds.textScrollList(listname,q=1,si=1)
    if allfiles:
        f=allfiles[0]
        scence=f.split('_')[1]
        shots=f.split('_')[2]
        stage=f.split('_')[3]
        scencename='episode_'+scence
        shotname='scene_'+shots
        stagename=''
        if stage=='ly':
            stagename='layout'
        if stage=='an':
            stagename='anim'
        if stage=='dy':
            stagename='dynamic'
        if stage=='sd':
            stagename='setdressing'
        print stagename
        filepath=gpath+scencename+'/'+shotname+'/'+stagename+'/'+f
        avipath=filepath.replace('.ma','.0001.avi').replace('.mb','.0001.avi')
        if os.path.exists(avipath):
            print 'opening...'
            cmd='start '+avipath.replace('/','\\')
            b=subprocess.Popen(cmd, shell=True)
            b.wait()

def edo_saveRenderingFiles():
    print 'save rendering files'
    global gpath
    savepath=cmds.textField('path_le',q=1,text=1)
    savepath=savepath.replace('\\','/')
    if not savepath[-1]=='/':
        savepath=savepath+'/'
    print savepath
    failpath=savepath+'failed/'
    okpathname=savepath+f
    if not os.path.exists(savepath):
        cmds.error('this save path is not existed.')
        return False
    if not os.path.exists(failpath):
        os.mkdir(failpath)
    cmds.file(rn=okpathname)

def edo_openCmd():
    global gpath
    allfiles=cmds.textScrollList('pickup_list',q=1,si=1)
    if allfiles:
        f=allfiles[0]
        scence=f.split('_')[1]
        shots=f.split('_')[2]
        stage=f.split('_')[3]
        scencename='episode_'+scence
        shotname='scene_'+shots
        stagename=''
        if stage=='ly':
            stagename='layout'
        if stage=='an':
            stagename='anim'
        if stage=='dy':
            stagename='dynamic'
        if stage=='sd':
            stagename='setdressing'
        print stagename
        filepath=gpath+scencename+'/'+shotname+'/'+stagename+'/'+f
        failpathname=failpath+f
        okpathname=savepath+f
        cmds.file(f=True,new=True)
        cmds.file(filepath,o=1,f=1)
        try:
            edo_opScene()
        except:
            cmds.error('something was failed')
            print 'failed'

def edo_doitCmd():
    global gpath
    savepath=cmds.textField('path_le',q=1,text=1)
    if savepath=='':
        cmds.error('you need field a path into the save path of the UI')
        return False
    savepath=savepath.replace('\\','/')
    if not savepath[-1]=='/':
        savepath=savepath+'/'
    print savepath
    failpath=savepath+'failed/'
    if not os.path.exists(savepath):
        cmds.error('this save path is not existed.')
        return False
    if not os.path.exists(failpath):
        os.mkdir(failpath)
    allfiles=cmds.textScrollList('pickup_list',q=1,si=1)
    for f in allfiles:
        #f=allfiles[0]
        scence=f.split('_')[1]
        shots=f.split('_')[2]
        stage=f.split('_')[3]
        scencename='episode_'+scence
        shotname='scene_'+shots
        stagename=''
        if stage=='ly':
            stagename='layout'
        if stage=='an':
            stagename='anim'
        if stage=='dy':
            stagename='dynamic'
        if stage=='sd':
            stagename='setdressing'
        print stagename
        filepath=gpath+scencename+'/'+shotname+'/'+stagename+'/'+f
        failpathname=failpath+f
        okpathname=savepath+f
        cmds.file( f=True, new=True )
        cmds.file(filepath,o=1,f=1)
        cmds.file(rn=okpathname)
        try:
            edo_opScene()
        except:
            cmds.file(rn=failpathname)
        cmds.file(s=1,f=1)

def edo_opScene():
    print 'import all reference'
    edo_importAllReference()
    print 'rename defualt render layer'
    execfile('//file-cluster/gdc/Resource/Support/Maya/projects/DODIII/edo_renameDefualtRenderLayerName.py')
    #print 'delete all shader'
    #melcmd='source "zzjUtilityTools.mel";lighting_DeleteUnusedNode();'
    #mel.eval(melcmd)
    print 'optimize: set all facial Controler'
    edo_setAllFacialCtrls()
    print 'optimize: hide all DEFORMER group'
    edo_hideNoModelGrp()
    print 'optimize: delete all unused groupParts and group Id'
    execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_clearUpScene.py')
    edo_clearUpScenes()
    print 'delete unknown nodes'
    execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_deleteUnknownNodes.py')
    edo_deleteUnknownNodes()
    #print 'optimize: set camera'
    #cmds.modelPanel('modelPanel11',e=1,cam='persp')
    print 'optimize: set model render attribute'
    edo_setModelAllRender()
    print 'optimize: set render options'
    edo_setRenderOptions()
    print 'optimize: delete all GDC rigging node'
    edo_deleteAllGDCriggingScriptNode()

def edo_deleteAllGDCriggingScriptNode():
    gdcsns1=cmds.ls('*:GDC_BODYRIG2009_SCRIPTNODE*')
    gdcsns2=cmds.ls('*GDC_BODYRIG2009_SCRIPTNODE')
    gdcsns3=cmds.ls('*GDC_BODYRIG2009_SCRIPTNODE*')
    gdcsns=gdcsns1+gdcsns2+gdcsns3
    if not gdcsns==[] and not gdcsns==None:
        cmds.delete(gdcsns)


def edo_setRenderOptions():
    if cmds.objExists('defaultRenderGlobals'):
        cmds.setAttr('defaultRenderGlobals.currentRenderer','mentalRay',type='string')
    if cmds.objExists('miDefaultOptions.finalGather'):
        cmds.setAttr('miDefaultOptions.finalGather',0)
    if cmds.objExists('miDefaultOptions.globalIllum'):
        cmds.setAttr('miDefaultOptions.globalIllum',0)
    cams=cmds.ls(type='camera')
    for ca in cams:
        cmds.setAttr(ca+'.renderable',0)
    scams=cmds.ls(type='stereoRigCamera')
    for scam in scams:
        #scam=scams[0]
        pa=cmds.listRelatives(scam,p=1,pa=1)[0]
        cs=cmds.listRelatives(pa,c=1,shapes=0,pa=1)
        for c in cs:
            if cmds.objExists(c+'.renderable'):
                cmds.setAttr(c+'.renderable',1)
        
    
    
def edo_setModelAllRender():
    mods=cmds.ls('*:MODEL')
    mshas=cmds.ls('*:MSH_all')
    amods=mods+mshas
    for mod in amods:
        #mod=mods[0]
        cmds.select(mod,hi=1)
        mss=cmds.ls(sl=1,type='mesh')
        for ms in mss:
            #ms=mss[0]
            msv=cmds.getAttr(ms+'.v')
            pms=cmds.listRelatives(ms,p=1,pa=1)[0]
            pmsv=cmds.getAttr(pms+'.v')
            if pmsv==1 and msv==1:
                cmds.setAttr(ms+'.castsShadows',1)
                cmds.setAttr(ms+'.receiveShadows',1)
                cmds.setAttr(ms+'.motionBlur',1)
                cmds.setAttr(ms+'.primaryVisibility',1)
                cmds.setAttr(ms+'.smoothShading',1)
                cmds.setAttr(ms+'.visibleInReflections',1)
                cmds.setAttr(ms+'.visibleInRefractions',1)
                cmds.setAttr(ms+'.doubleSided',1)
    cmds.select(cl=1)

def edo_hideNoModelGrp():
    defs=cmds.ls('*:DEFORMERS')
    cmds.hide(defs)
    defs=cmds.ls('*:RIG')
    cmds.hide(defs)
    defs=cmds.ls('*:PROX')
    cmds.hide(defs)
    defs=cmds.ls(type='light')
    cmds.hide(defs)
    
def edo_setAllFacialCtrls():
    fcs=[]
    mas=[]
    try:
        fcs=cmds.ls('*:Facial_CTRL_FRAME',type='transform')
    except:
        print 'facial ls error'
    if fcs:
        for fc in fcs:
            #fc=fcs[0]
            fca=fc+'.facialSecondaryCtrl'
            inps=cmds.listConnections(fca,s=1,d=0,p=1)
            if inps:
                cmds.disconnectAttr(inps[0],fca)
            cmds.setAttr(fca,1)
    try:
        mas=cmds.ls('*:Master',type='transform')
    except:
        print 'master ls error'
    if mas:
        for ma in mas:
            #ma=mas[0]
            maaH=ma+'.model_view'
            maaE=ma+'.expressions'
            if cmds.objExists(maaH):
                inps=cmds.listConnections(maaH,s=1,d=0,p=1)
                if inps:
                    cmds.disconnectAttr(inps[0],maaH)
                cmds.setAttr(maaH,0)
            if cmds.objExists(maaE):
                inps=cmds.listConnections(maaE,s=1,d=0,p=1)
                if inps:
                    cmds.disconnectAttr(inps[0],maaE)
                cmds.setAttr(maaE,0)

def edo_importAllReference():
    refs=cmds.ls(type='reference')
    path=''
    for ref in refs:
        #ref=refs[0]
        try:
            path=cmds.referenceQuery(ref,f=1)
            print 'import  ... '+ path +' ... form reference'
            cmds.file(path,ir=1)
        except:
            continue

def edo_deleteSelectedMi1Cmd():
    sels=cmds.textScrollList('pickup_list',e=1,ra=1)

def edo_deleteSelectedMiCmd():
    sels=cmds.textScrollList('pickup_list',q=1,si=1)
    alin=cmds.textScrollList('pickup_list',q=1,ai=1)
    for s in sels:
        if s in alin:
            cmds.textScrollList('pickup_list',e=1,ri=s)
            

def edo_pickUpFilesCmd():
    sels=cmds.textScrollList('search_list',q=1,si=1)
    alin=cmds.textScrollList('pickup_list',q=1,ai=1)
    for s in sels:
        #s=sels[0]
        if not alin:
            cmds.textScrollList('pickup_list',e=1,a=s)
            continue
        if not s in alin:
            cmds.textScrollList('pickup_list',e=1,a=s)

def edo_textFieldChangeCmd():
    global gpath
    zpath='Z:/Projects/'
    fsc=cmds.textField('first_le',q=1,text=1)
    ssc=cmds.textField('second_le',q=1,text=1)
    tsc=cmds.textField('third_le',q=1,text=1)
    projectname=cmds.textField('project_le',q=1,text=1)
    scenesname=cmds.textField('scenes_le',q=1,text=1)
    shotname=cmds.textField('shot_le',q=1,text=1)
    if projectname=='':
        return False
    if scenesname=='':
        return False
    if shotname=='':
        return False
    animationPath=zpath+projectname+'/project/scenes/Animation/'
    gpath=animationPath
    scenesname='episode_'+scenesname
    scenesPath=animationPath+scenesname+'/'
    shotlist=[]
    if '-' in shotname:
        sp=shotname.split('-')
        shotlist_int=range(int(sp[0]),int(sp[1])+1)
        for s in shotlist_int:
            #s=shotlist_int[0]
            ss=edo_addIntPrefix(s)
            shotlist.append(ss)
    else:
        shotlist.append(shotname)
    #print shotlist
    alldirs=os.listdir(scenesPath)
    dirlist=[]
    for dir in alldirs:
        #dir=alldirs[2]
        if 'scene_' in dir:
            sid=dir.split('_')[-1]
            while len(sid)>3:
                sid=sid[:-1]
            if sid in shotlist:
                dirlist.append(dir)
    #print dirlist
    allfiles=[]
    for dir in dirlist:
        #dir=dirlist[1]
        dirpath=scenesPath+dir+'/'
        indir=os.listdir(dirpath)
        atfiles=[]
        for id in indir:
            #id=indir[0]
            #print dir+ '  ...  ' + id
            p=dirpath+id+'/'
            fs=os.listdir(p)
            for f in fs:
                #f=fs[1]
                if '.ma' in f or '.mb' in f:
                    atfiles.append(f)
        #print atfiles
        pickup=''
        if pickup=='' and not fsc=='':
            for f in atfiles:
                #f=atfiles[0]
                if fsc in f:
                    pickup=f
        if pickup=='' and not ssc=='':
            for f in atfiles:
                #f=atfiles[0]
                if ssc in f:
                    pickup=f
        if pickup=='' and not tsc=='':
            for f in atfiles:
                #f=atfiles[0]
                if tsc in f:
                    pickup=f
        if not pickup=='':
            allfiles.append(pickup)
    cmds.textScrollList('search_list',e=1,ra=1)
    if allfiles:
        print allfiles
        for f in allfiles:
            cmds.textScrollList('search_list',e=1,a=f)
    

        
def edo_addIntPrefix(i,n=3):
    #i=15
    #n=3
    si=str(i)
    while len(si)<n:
        si='0'+si
    #print si
    return si
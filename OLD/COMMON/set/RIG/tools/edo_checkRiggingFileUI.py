#-*- coding: utf-8 -*-
import maya.cmds as cmds
def edo_checkRiggingFileUI():
    if cmds.window('checkRiggingFileUI',ex=1):
        cmds.deleteUI('checkRiggingFileUI')
    cmds.window('checkRiggingFileUI',w=400,h=800)
    cmds.columnLayout('checkRiggingFileUI_CL01',adj=1)
    cmds.frameLayout('checkRiggingFileUI_FR01',l=u'检查控制器',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_BT00',l=u'清除设置垃圾节点',c='edo_clearGarbageNodes()')
    cmds.button('checkRiggingFileUI_BT01',l=u'检查重名控制器',c='edo_checkCtrlMoreThanOneNameCmd()')
    cmds.textScrollList('checkRiggingFileUI_TL01',ams=1,h=200,sc='edo_checkRiggingFileUI_TL01_ccCmd()')
    cmds.popupMenu('checkRiggingFileUI_PPM01',b=3)
    cmds.menuItem('checkRiggingFileUI_MIT01',l=u'选择所有相同名称物体',c='edo_selectSameNameControlCmd()')
    cmds.setParent('checkRiggingFileUI_CL01')
    cmds.frameLayout('checkRiggingFileUI_FR02',l=u'检查SET',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_BT02',l=u'检查没放入SET的控制器',c='edo_checkCtrlSetCmd()')
    cmds.textScrollList('checkRiggingFileUI_TL02',ams=1,h=200,sc='edo_checkRiggingFileUI_TL02_ccCmd()')
    cmds.popupMenu('checkRiggingFileUI_PPM02',b=3)
    cmds.menuItem('checkRiggingFileUI_MIT02',l=u'加入_BodySet',c='edo_addSelectToBodySetCmd(\'BodySet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0201',l=u'加入_Lf_ArmSet',c='edo_addSelectToBodySetCmd(\'Lf_ArmSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0202',l=u'加入_Rt_ArmSet',c='edo_addSelectToBodySetCmd(\'Rt_ArmSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0203',l=u'加入_Lf_LegSet',c='edo_addSelectToBodySetCmd(\'Lf_LegSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0204',l=u'加入_Rt_LegSet',c='edo_addSelectToBodySetCmd(\'Rt_LegSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0205',l=u'加入_Lf_FingerSet',c='edo_addSelectToBodySetCmd(\'Lf_FingerSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0206',l=u'加入_Rt_FingerSet',c='edo_addSelectToBodySetCmd(\'Rt_FingerSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0207',l=u'加入_Lf_ToesSet',c='edo_addSelectToBodySetCmd(\'Lf_ToesSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0208',l=u'加入_Rt_ToesSet',c='edo_addSelectToBodySetCmd(\'Rt_ToesSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT03',l=u'加入_BrowsSet',c='edo_addSelectToFacialSetCmd(\'BrowsSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0301',l=u'加入_LipsSet',c='edo_addSelectToFacialSetCmd(\'LipsSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0302',l=u'加入_LookSet',c='edo_addSelectToFacialSetCmd(\'LookSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0303',l=u'加入_MouthSet',c='edo_addSelectToFacialSetCmd(\'MouthSet\')')
    cmds.menuItem('checkRiggingFileUI_MIT0304',l=u'加入_OtherSet',c='edo_addSelectToFacialSetCmd(\'OtherSet\')')
    cmds.setParent('checkRiggingFileUI_CL01')
    cmds.frameLayout('checkRiggingFileUI_FR03',l=u'检查控制器数值和key帧',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_BT03',l=u'检查是否存在Transform不是默认值以及被key帧的控制器',c='edo_checkCtrlChannel()')
    cmds.columnLayout('checkRiggingFileUI_CL02',adj=1)
    cmds.rowLayout('checkRiggingFileUI_RW01',numberOfColumns=3,columnWidth3=[133,133,133])
    cmds.columnLayout('checkRiggingFileUI_CL03',adj=1)
    cmds.text(l=u'以下列表中为',bgc=[0.7,0.25,0.1])
    cmds.text(l=u'被key帧的控制器',bgc=[0.7,0.25,0.1])
    cmds.textScrollList('checkRiggingFileUI_TL03',ams=1,w=133,h=200,sc='edo_checkRiggingFileUI_TL03_ccCmd()')
    cmds.setParent('checkRiggingFileUI_RW01')
    cmds.columnLayout('checkRiggingFileUI_CL04',adj=1)
    cmds.text(l=u'以下列表中为',bgc=[0.78,0.75,0.72])
    cmds.text(l=u'Transform有数值的控制器',bgc=[0.78,0.75,0.72])
    cmds.textScrollList('checkRiggingFileUI_TL04',ams=1,w=133,h=200,sc='edo_checkRiggingFileUI_TL04_ccCmd()')
    cmds.setParent('checkRiggingFileUI_RW01')
    cmds.columnLayout('checkRiggingFileUI_CL05',adj=1)
    cmds.text(l=u'以下列表中为被隐藏的曲线',bgc=[0.28,0.2,0.12])
    cmds.text(l=u'请检查其中有误隐藏的控制器',bgc=[0.28,0.2,0.12])
    cmds.textScrollList('checkRiggingFileUI_TL05',ams=1,w=133,h=200,sc='edo_checkRiggingFileUI_TL05_ccCmd()')
    cmds.showWindow('checkRiggingFileUI')
    cmds.window('checkRiggingFileUI',e=1,w=400,h=800)

#edo_clearUpScenes()
def edo_clearUpScenes(types=['groupParts','groupId','polyNormal']):
    cmds.undoInfo(state=False)
    for t in types:
        #t=types[0]
        Nodes=cmds.ls(type=t)
        if not Nodes:
            cmds.undoInfo(state=True)
            return False
        print t+' ... total is ... '+str(len(Nodes))
        clearNodes=[]
        for n in Nodes:
            #n=Nodes[1]
            out=cmds.listConnections(n,s=0,d=1)
            if not out:
                #print 'delete   ...  '+n
                #cmds.delete(gp)
                #print 'serching no output groupId'
                clearNodes.append(n)
                cmds.delete(n)
                if len(clearNodes)%1000==0 and len(clearNodes)>0:
                    print str(len(clearNodes))
            else:
                if t=='groupId':
                    #print 'serching shadding groupId'
                    isshadding=0
                    for o in out:
                        #o=out[1]
                        if cmds.nodeType(o)=='shadingEngine':
                            isshadding=1
                        else:
                            isshadding=0
                            break
                    if isshadding==1:
                        clearNodes.append(n)
                        cmds.delete(n)
                    if len(clearNodes)%1000==0 and len(clearNodes)>0:
                        print str(len(clearNodes))
        cl=len(clearNodes)
        #if cl>0:
        #    cmds.delete(clearNodes)
        print 'cleared ... '+str(cl)+'  of  '+t+'  ...  nodes'
    cmds.undoInfo(state=True)
    return True

def edo_deleteGDCriggingScriptNode():
    gdcsns=[]
    allnodes=cmds.ls(type='script')
    for n in allnodes:
        if 'GDC_BODYRIG2009_SCRIPTNODE' in n:
            if not n=='GDC_BODYRIG2009_SCRIPTNODE':
                gdcsns.append(n)
    print 'delete script:'
    print gdcsns
    if gdcsns:
        cmds.delete(gdcsns)

def edo_clearGarbageNodes():
    print 'clear scriptNodes'
    edo_deleteGDCriggingScriptNode()
    print 'clear useless group parts node, groupId node and polynormal node'
    edo_clearUpScenes()

def edo_checkCtrlMoreThanOneNameCmd():
    print 'check more than one name control'
    cmds.textScrollList('checkRiggingFileUI_TL01',e=1,ra=1)
    curveShapes=cmds.ls(type='nurbsCurve',ap=1,ni=1)
    curveTransforms=[]
    for c in curveShapes:
        t=cmds.listRelatives(c,p=1,pa=1)[0]
        if cmds.nodeType(t)=='transform' or cmds.nodeType(t)=='joint':
            if '|' in t:
                if not t in curveTransforms:
                    curveTransforms.append(t)
    print curveTransforms
    for ct in curveTransforms:
        shape=cmds.listRelatives(ct,s=1,ni=1,pa=1,type='nurbsCurve')[0]
        if edo_getCurveIsHided(shape)=='hided':
            print ct+' is  hided,pass this nurbs curve..\n'
        else:
            cmds.textScrollList('checkRiggingFileUI_TL01',e=1,a=ct)
    
    
def edo_checkRiggingFileUI_TL01_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL01',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_checkRiggingFileUI_TL02_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL02',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_checkRiggingFileUI_TL03_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL03',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_checkRiggingFileUI_TL04_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL04',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_checkRiggingFileUI_TL05_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL05',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_selectSameNameControlCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL01',q=1,si=1)
    cmds.select(cl=1)
    for s in selText:
        ts=s.split('|')
        ctn=ts[len(ts)-1]
        cmds.select('*'+ctn,add=1)
    allsel=cmds.ls(sl=1,ni=1,ap=1)
    cmds.textScrollList('checkRiggingFileUI_TL01',e=1,si=allsel)
    
def edo_checkCtrlSetCmd():
    cmds.select(all=1)
    grp=cmds.ls(sl=1,ni=1,type='transform')
    cmds.select(cl=1)
    if len(grp)>1:
        click=cmds.confirmDialog( title=u'设置文件还不够规范', message=u'设置文件最终只能有1个大组，现在又多个，请整理。',button=['yes,god it!','ignore'],defaultButton='YES',cancelButton='YES', dismissString='YES')
        if click=='yes,god it!':
            return 0
    if cmds.objExists('*CHR'):
        print 'it\'s character file\n'
        if not cmds.objExists('CtrlSet') or not cmds.objExists('All_BodySet') or not cmds.objExists('All_FacialSet'):
            click=cmds.confirmDialog( title=u'设置文件还不够规范', message=u'角色文件种必须有All_BodySet和All_FacialSet，放入CtrlSet并分别将控制器分类放入其中,是否需要自动创建',button=['auto create,BodySet','auto create,FacialSet','not at all,create it by my self!'],defaultButton='YES',cancelButton='YES', dismissString='YES')
            if click=='not at all,create it by my self!':
                return 0
            if click=='auto create,BodySet':
                from RIG.commonly.sets import CJW_createCtrlSets
                CJW_createCtrlSets()  
            if click=='auto create,FacialSet':
                from RIG.commonly.sets import CJW_createFacialCtrlSets
                CJW_createFacialCtrlSets()                
        #curveShapes=cmds.ls(type='nurbsCurve',ap=1,ni=1)
        curveShapes = cmds.listRelatives('RIG',allDescendents=1,type = 'nurbsCurve',fullPath=1)
        curveTransforms=[]
        for c in curveShapes:
            #c='c_Lf_up_eyelids_CTRL_dn|curveShape74'
            #print c
            t=cmds.listRelatives(c,p=1,pa=1)[0]
            if cmds.nodeType(t)=='transform' or cmds.nodeType(t)=='joint':
                bset=cmds.listSets(o=t)
                if not bset==None:
                    if not 'BodySet' in cmds.listSets(o=t) and not 'Lf_ArmSet' in cmds.listSets(o=t) and not 'Lf_FingerSet' in cmds.listSets(o=t) and not 'Lf_LegSet' in cmds.listSets(o=t) and not 'Lf_ToesSet' in cmds.listSets(o=t) and not 'Rt_ArmSet' in cmds.listSets(o=t)and not 'Rt_FingerSet' in cmds.listSets(o=t) and not 'Rt_LegSet' in cmds.listSets(o=t) and not 'Rt_ToesSet' in cmds.listSets(o=t) and not 'BrowsSet' in cmds.listSets(o=t) and not 'LipsSet' in cmds.listSets(o=t) and not 'LookSet' in cmds.listSets(o=t) and not 'MouthSet' in cmds.listSets(o=t) and not 'OtherSet' in cmds.listSets(o=t):
                        if not t in curveTransforms:
                            curveTransforms.append(t)
                else:
                    if not t in curveTransforms:
                        curveTransforms.append(t)
        #print curveTransforms
        cmds.textScrollList('checkRiggingFileUI_TL02',e=1,ra=1)
        for ct in curveTransforms:
            #ct='c_Lf_up_eyelids_CTRL_fourAxisup'
            shape=cmds.listRelatives(ct,s=1,ni=1,pa=1,type='nurbsCurve')[0]
            if edo_getCurveIsHided(shape)=='hided':
                print ct+' is  hided,pass this nurbs curve..\n'
            else:
                channelBoxAttr=cmds.listAttr(ct,k=1,se=1,u=1)
                if not channelBoxAttr==None:
                    if ct[-3:]=='_dn' or ct[-3:]=='_up' or ct[-3:]=='_lf' or ct[-3:]=='_rt' or ct[-5:]=='_lfup' or ct[-5:]=='_lfdn' or ct[-5:]=='_rtup' or ct[-5:]=='_rtdn' or ct[-11:]=='_fourAxisup' or ct[-11:]=='_fourAxisdn' or ct[-11:]=='_fourAxislf' or ct[-11:]=='_fourAxisrt':
                        print ct+'   is  a  blendshape target box...pass...'
                        continue
                    cmds.textScrollList('checkRiggingFileUI_TL02',e=1,a=ct)
    if cmds.objExists('*PROP'):
        print 'it\'s prop file\n'
    if cmds.objExists('*SET'):
        print 'it\'s set file\n'
    if not cmds.objExists('*SET') and not cmds.objExists('*CHR') and not cmds.objExists('*PROP'):
        click=cmds.confirmDialog( title=u'文件超出工具检查范围', message=u'此工具只检查角色（根部组名为CHR），道具（根部组名为PROP），场景（根部组名为SET）设置文件',button='yes,god it!',defaultButton='YES',cancelButton='YES', dismissString='YES')
    return 1
    
def edo_addSelectToBodySetCmd(SetName):
    print 'add the select to bodySet now...\n'
    selText=cmds.textScrollList('checkRiggingFileUI_TL02',q=1,si=1)
    cmds.sets(selText,include=SetName)
    
def edo_addSelectToFacialSetCmd(SetName):
    print 'add the select to facialSet now...\n'
    selText=cmds.textScrollList('checkRiggingFileUI_TL02',q=1,si=1)
    cmds.sets(selText,include=SetName)

def edo_checkCtrlChannel():
    print 'check control value'
    bc=None
    fc=None
    if cmds.objExists('bodySet'):
        bc=cmds.sets('bodySet',q=True)
    if cmds.objExists('facialSet'):
        fc=cmds.sets('facialSet',q=True)
    tctrls=[]
    if not bc==None and fc==None:
        tctrls=bc
    if not fc==None and bc==None:
        tctrls=fc
    if not bc==None and not fc==None:
        tctrls=bc+fc
    if bc==None and fc==None:
        return 0
    tf=cmds.ls(tctrls,type='transform')
    jn=cmds.ls(tctrls,type='joint')
    ctrls=tf+jn
    keyctrl=[]
    transformCtrl=[]
    visCtrl=[]
    cmds.textScrollList('checkRiggingFileUI_TL03',e=1,ra=1)
    cmds.textScrollList('checkRiggingFileUI_TL04',e=1,ra=1)
    cmds.textScrollList('checkRiggingFileUI_TL05',e=1,ra=1)
    for c in ctrls:
        #c='Lf_elbow_display'
        #print c
        channelBoxAttr=cmds.listAttr(c,k=1,se=1,u=1)
        vis=None
        shape=cmds.listRelatives(c,s=1,ni=1,pa=1,type='nurbsCurve')[0]
        if edo_getCurveIsHided(shape)=='hided':
            vis=True
        else:
            vis=False
        if not channelBoxAttr==None:
            for a in channelBoxAttr:
                #a='translateY'
                #print c+'.'+a
                inputNode=cmds.listConnections(c+'.'+a,s=1,d=0)
                if not inputNode==None and not c in keyctrl:
                    if 'animCurveT' in cmds.nodeType(inputNode):
                        keyctrl.append(c)
                        cmds.textScrollList('checkRiggingFileUI_TL03',e=1,a=c)
                value=int((cmds.getAttr(c+'.'+a)+0.0005)*1000)
                if inputNode==None and not c in transformCtrl:
                    if vis==False:
                        if a=='translateX' and not value==0:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='translateY' and not value==0:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='translateZ' and not value==0:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='rotateX' and not value==0:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='rotateY' and not value==0:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='rotateZ' and not value==0:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='scaleX' and not value==1000:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='scaleY' and not value==1000:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='scaleZ' and not value==1000:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
        if not c in visCtrl:
            #value=cmds.getAttr(c+'.'+a)
            if vis==True:
                visCtrl.append(c)
                cmds.textScrollList('checkRiggingFileUI_TL05',e=1,a=c)
    #print keyctrl
    #print transformCtrl
    #print visCtrl
    
def edo_getCurveIsHided(curveObj):
    #curveObj='Lf_elbow_displayShape'
    iso=0
    state='special'
    if not cmds.listConnections(curveObj+'.v',s=1,d=0)==None or not cmds.listConnections(curveObj+'.template',s=1,d=0)==None:
        return 'connected'
    if cmds.getAttr(curveObj+'.v')==False or cmds.getAttr(curveObj+'.template')==True:
        return 'hided'
    nt=cmds.nodeType(curveObj)
    if nt=='transform' or nt=='joint':
        if cmds.getAttr(curveObj+'.overrideEnabled')==True and cmds.getAttr(curveObj+'.overrideDisplayType')==0:
            if iso==0:
                state='normal'
        else:
            iso=1
            if cmds.getAttr(curveObj+'.overrideEnabled')==True and not cmds.getAttr(curveObj+'.overrideDisplayType')==0 and state=='special':
                return 'hided'
    else:
        if cmds.getAttr(curveObj+'.overrideEnabled')==True and not cmds.getAttr(curveObj+'.overrideDisplayType')==0:
            return 'hided'
    parent=''
    while not parent==None:
        parent=cmds.listRelatives(curveObj,p=1,pa=1)
        if not parent==None:
            curveObj=parent[0]
            if not cmds.listConnections(curveObj+'.v',s=1,d=0)==None or not cmds.listConnections(curveObj+'.template',s=1,d=0)==None:
                return 'connected'
            if cmds.getAttr(curveObj+'.v')==False or cmds.getAttr(curveObj+'.template')==True:
                return 'hided'
            nt=cmds.nodeType(curveObj)
            if nt=='transform' or nt=='joint':
                if cmds.getAttr(curveObj+'.overrideEnabled')==True and cmds.getAttr(curveObj+'.overrideDisplayType')==0:
                    if iso==0:
                        state='normal'
                else:
                    iso=1
                    if cmds.getAttr(curveObj+'.overrideEnabled')==True and not cmds.getAttr(curveObj+'.overrideDisplayType')==0 and state=='special':
                        return 'hided'
                    continue
        #print parent
    return 'nothing'

edo_checkRiggingFileUI()
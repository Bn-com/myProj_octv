#-*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel

def edo_modelNameCheckinList():
    if cmds.window('edo_mnclu_ui',ex=1):
        cmds.deleteUI('edo_mnclu_ui')
    ui=cmds.loadUI(f='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_modelNameCheckinList.myuis')
    cmds.showWindow(ui)
    #cmds.control('edo_mnclu_group01',e=1,vis=1)
    #cmds.control('edo_mnclu_group02',e=1,vis=0)
    cmds.menuItem('MODEL',p='edo_mnclu_opm01')
    cmds.menuItem('MS_CACHE',p='edo_mnclu_opm01')
    cmds.optionMenu('edo_mnclu_opm01',e=1,w=120,h=30,sl=1)
    cmds.button('edo_mnclu_bt01',e=1,bgc=[0.75,0.52,0.15],c='edo_modelNameCheckinList_BT01()')
    cmds.button('edo_mnclu_bt02',e=1,bgc=[0.25,0.52,0.12],c='edo_checkNoZeorVertexMeshes()')
    cmds.textScrollList('edo_mnclu_list01',e=1,ams=1,sc='edo_ListEditSelectCmd(\'edo_mnclu_list01\')')
    cmds.textScrollList('edo_mnclu_list02',e=1,ams=1,sc='edo_ListEditSelectCmd(\'edo_mnclu_list02\')')
    cmds.textScrollList('edo_mnclu_list03',e=1,ams=1,sc='edo_ListEditSelectCmd(\'edo_mnclu_list03\')')
    cmds.textScrollList('edo_mnclu_list04',e=1,ams=1,sc='edo_ListEditSelectCmd(\'edo_mnclu_list04\')')
    cmds.textScrollList('edo_mnclu_list05',e=1,ams=1,sc='edo_ListEditSelectCmd(\'edo_mnclu_list05\')')
    cmds.textScrollList('edo_mnclu_list06',e=1,ams=1,sc='edo_ListEditSelectCmd(\'edo_mnclu_list06\')')
    cmds.textScrollList('edo_mnclu_list07',e=1,ams=1,sc='edo_ListEditSelectCmd(\'edo_mnclu_list07\')',dcc='edo_ListEditDccCmd(\'edo_mnclu_list07\')')
    cmds.textScrollList('edo_mnclu_list08',e=1,ams=1,sc='edo_ListEditSelectCmd(\'edo_mnclu_list08\')')
    cmds.textScrollList('edo_mnclu_list09',e=1,ams=1,sc='edo_ListEditSelectCmd(\'edo_mnclu_list09\')')
    cmds.textScrollList('edo_mnclu_list10',e=1,ams=1,sc='edo_ListEditSelectCmd(\'edo_mnclu_list10\')')
    cmds.popupMenu('edo_mnclu_list01_popm',p='edo_mnclu_list01',b=3)
    cmds.menuItem('edo_mnclu_list01_popm_mi01',label='�����ѡ��Ŀ���',p='edo_mnclu_list01_popm',c='edo_clearSelectObjInList(\'edo_mnclu_list01\')')
    cmds.popupMenu('edo_mnclu_list02_popm',p='edo_mnclu_list02',b=3)
    cmds.menuItem('edo_mnclu_list02_popm_mi01',label='�����ѡ���������ʷ',p='edo_mnclu_list02_popm',c='edo_deleteObjectHistoryFromList(\'edo_mnclu_list02\')')
    cmds.popupMenu('edo_mnclu_list03_popm',p='edo_mnclu_list03',b=3)
    cmds.menuItem('edo_mnclu_list03_popm_mi01',label='�����ѡ��Ķ���original�ڵ�',p='edo_mnclu_list03_popm',c='edo_clearSelectObjInList(\'edo_mnclu_list03\')')
    cmds.popupMenu('edo_mnclu_list04_popm',p='edo_mnclu_list04',b=3)
    cmds.menuItem('edo_mnclu_list04_popm_mi01',label='���������׺_',p='edo_mnclu_list04_popm',c='edo_addEndNameFromList(\'edo_mnclu_list04\')')
    cmds.popupMenu('edo_mnclu_list05_popm',p='edo_mnclu_list05',b=3)
    cmds.menuItem('edo_mnclu_list05_popm_mi01',label='�����������νڵ�',p='edo_mnclu_list05_popm',c='edo_renameShapeNameFromList(\'edo_mnclu_list05\')')
    cmds.popupMenu('edo_mnclu_list06_popm',p='edo_mnclu_list06',b=3)
    cmds.menuItem('edo_mnclu_list06_popm_mi01',label='������original�ڵ�',p='edo_mnclu_list06_popm',c='edo_renameOriginalNameFromList(\'edo_mnclu_list06\')')
    cmds.popupMenu('edo_mnclu_list09_popm',p='edo_mnclu_list09',b=3)
    cmds.menuItem('edo_mnclu_list09_popm_mi01',label='���ѡ��ģ�͵ĵ�λ��',p='edo_mnclu_list09_popm',c='edo_freezeVertexOfMeshesFromList(\'edo_mnclu_list09\')')
    cmds.popupMenu('edo_mnclu_list10_popm',p='edo_mnclu_list10',b=3)
    cmds.menuItem('edo_mnclu_list10_popm_mi01',label='�ر�inVisibleFace����',p='edo_mnclu_list10_popm',c='edo_turnOffVisibleFaceFromList(\'edo_mnclu_list10\')')
    cmds.window(ui,e=1,w=550,h=900)
    
def edo_edo_mnclu_opm01_changeCmd():
    v=cmds.optionMenu('edo_mnclu_opm01',q=1,v=1)
    if v=='MODEL':
        cmds.control('edo_mnclu_group01',e=1,vis=1)
        cmds.control('edo_mnclu_group02',e=1,vis=0)
    if v=='MS_CACHE':
        cmds.control('edo_mnclu_group01',e=1,vis=0)
        cmds.control('edo_mnclu_group02',e=1,vis=1)

def edo_modelNameCheckinList_BT01():
    print 'checkin model\'s name now...'
    rt=edo_check_MODEL_Group()
    if rt==False:
        return False
    edo_check_allModel_history()
    edo_check_empty_group()
    edo_checkUnusedOriginalNode()
    edo_checkEndNameFlag()
    edo_checkShapeNodeName()
    edo_checkOrignalShapeNodeName()
    edo_checkNameSpaceMesh()
    edo_check_instanceObj()
    edo_checkInVisibleFace()
    
def edo_check_instanceObj():
    inss=[]
    meshes=cmds.ls(type='mesh',ni=1)
    if not meshes==None:
        for mesh in meshes:
            #mesh='aaa2_Shape'
            tss=cmds.listRelatives(mesh,ap=1,pa=1)
            if len(tss)>1:
                #mesh=mesh.split('|')[len(mesh.split('|'))-1]
                if not mesh in inss:
                    inss.append(mesh)
    print inss
    edo_fildTextsToListEdit(inss,'edo_mnclu_list08')
    return inss
            
def edo_check_allModel_history():
    hismesh=[]
    meshes=cmds.ls(type='mesh',ni=1)
    if not meshes==None:
        for mesh in meshes:
            #mesh='polySurfaceShape1'
            his=cmds.listConnections(mesh+'.inMesh',s=1,d=0,scn=True,sh=1)
            if not his==None:
                for hi in his:
                    #hi=his[0]
                    if not cmds.nodeType(hi)=='mesh' and not mesh in hismesh:
                        outs=cmds.listConnections(hi,s=0,d=1,p=1)
                        for out in outs:
                            #out=outs[0]
                            if mesh+'.inMesh' in out:
                                hismesh.append(mesh)
    print hismesh
    edo_fildTextsToListEdit(hismesh,'edo_mnclu_list02')
    return hismesh
    
def edo_check_MODEL_Group():
    cmds.select(ado=1)
    all=cmds.ls(sl=1)
    if all==[] or all==None:
        cmds.confirmDialog( title='�ļ����淶', message='���������κ�ģ�������壬����', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if len(all)==0:
        cmds.confirmDialog( title='�ļ����淶', message='���������κ�ģ�������壬����', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if len(all)>1:
        cmds.confirmDialog( title='�ļ����淶', message='������ֻ����һ����Ϊ MODEL ���飬������Ӧ�÷���MODEL֮�£�����ɢ�����⣬������', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    msa=cmds.ls("*MODEL")
    if len(msa)==0:
        cmds.confirmDialog( title='�ļ����淶', message='���������ϲ����Ӧ������Ϊ MODEL , ����', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if len(msa)>1:
        cmds.confirmDialog( title='�ļ����淶', message='�������ж������Ϊ MODEL , ����', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if not all[0]=='MODEL':
        cmds.confirmDialog( title='�ļ����淶', message='���������ϲ����Ӧ������Ϊ MODEL , ����', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    cmds.select(cl=1)
        
def edo_fildTextsToListEdit(list,listName):
    #listName='edo_mnclu_list01'
    cmds.textScrollList(listName,e=1,ra=1)
    if not list==None or not list==[]:
        for l in list:
            cmds.textScrollList(listName,e=1,a=l)



def edo_ListEditSelectCmd(listName):
    #listName='edo_mnclu_list01'
    sels=cmds.textScrollList(listName,q=1,si=1)
    if not sels==None:
        cmds.select(sels)
        
def edo_clearSelectObjInList(listName):
    #listName='edo_mnclu_list01'
    sels=cmds.textScrollList(listName,q=1,si=1)
    if not sels==None:
        cmds.delete(sels)
    edo_modelNameCheckinList_BT01()
    
def edo_ListEditDccCmd(listName):
    #listName='edo_mnclu_list01'
    sels=cmds.textScrollList(listName,q=1,si=1)
    if not sels==None:
        bt=cmds.promptDialog(title='������',message='д��������',button=['OK','Cancel'])
        if bt=='OK':
            newname=cmds.promptDialog(query=True,text=True)
            if not newname=='':
                cmds.rename(sels[0],newname)
            else:
                return False
        else:
            return False
    edo_modelNameCheckinList_BT01()
                
def edo_addEndNameFromList(listName):
    #listName='edo_mnclu_list04'
    sels=cmds.textScrollList(listName,q=1,si=1)
    if not sels==None:
        for sel in sels:
            #sel=sels[0] 
            cmds.rename(sel,sel.split('|')[len(sel.split('|'))-1]+'_')
    edo_modelNameCheckinList_BT01()
    
def edo_renameShapeNameFromList(listName):
    #listName='edo_mnclu_list05'
    sels=cmds.textScrollList(listName,q=1,si=1)
    if not sels==None:
        for sel in sels:
            #sel=sels[0] 
            ts=cmds.listRelatives(sel,p=1,pa=1)[0]
            cmds.rename(sel,ts.split('|')[len(ts.split('|'))-1]+'Shape')
    edo_modelNameCheckinList_BT01()
    
def edo_renameOriginalNameFromList(listName):
    #listName='edo_mnclu_list06'
    sels=cmds.textScrollList(listName,q=1,si=1)
    if not sels==None:
        for sel in sels:
            #sel=sels[0] 
            ts=cmds.listRelatives(sel,p=1,pa=1)[0]
            cmds.rename(sel,ts.split('|')[len(ts.split('|'))-1]+'ShapeOrig')
    edo_modelNameCheckinList_BT01()
    
def edo_turnOffVisibleFaceFromList(listName):
    #listName='edo_mnclu_list10'
    sels=cmds.textScrollList(listName,q=1,si=1)
    if not sels==None:
        for sel in sels:
            #sel=sels[0] 
            cmds.setAttr(sel+'.displayInvisibleFaces',0)
    edo_modelNameCheckinList_BT01()
    
def edo_deleteObjectHistoryFromList(listName):
    #listName='edo_mnclu_list02'
    sels=cmds.textScrollList(listName,q=1,si=1)
    if not sels==None:
        cmds.DeleteHistory()
    edo_modelNameCheckinList_BT01()
    
def edo_freezeVertexOfMeshesFromList(listName):
    #listName='edo_mnclu_list09'
    sels=cmds.textScrollList(listName,q=1,si=1)
    if not sels==None:
        cmds.deformer(type='cluster')
        cmds.DeleteHistory()
    edo_checkNoZeorVertexMeshes()
    
def edo_check_empty_group():
    epg=[]
    trans=cmds.ls(type='transform')
    for t in trans:
        #print t
        #t='group16'
        if edo_find_empty_group(t)==None:
            epg.append(t)
    print epg
    edo_fildTextsToListEdit(epg,'edo_mnclu_list01')
    return epg

def edo_find_empty_group(grp):
    #grp='group16'
    #print grp
    shapes=cmds.listRelatives(grp,s=1)
    if not shapes==None:
        return True
    childs=cmds.listRelatives(grp,c=1,pa=1)
    if childs==None:
        return None
    for c in childs:
        #c=childs[0]
        rt=edo_find_empty_group(c)
        if rt==True:
           return True

def edo_checkUnusedOriginalNode():
    orgs=[]
    meshes=cmds.ls(type='mesh',ni=0)
    if not meshes==None:
        for mesh in meshes:
            #mesh=meshes[2]
            io=cmds.getAttr(mesh+'.io')
            if io==True:
                outs=cmds.listConnections(mesh+'.worldMesh[0]',s=0,d=1,sh=1)
                if outs==None:
                    orgs.append(mesh)
                else:
                    for out in outs:
                        #out=outs[0]
                        if cmds.nodeType(out)=='mesh':
                            if mesh not in orgs:
                                orgs.append(mesh)        
    print orgs
    edo_fildTextsToListEdit(orgs,'edo_mnclu_list03')
    return orgs

def edo_checkEndNameFlag():
    wnms=[]
    meshes=cmds.ls(type='mesh',ni=1)
    if not meshes==None:
        for mesh in meshes:
            #mesh=meshes[0]
            ts=cmds.listRelatives(mesh,p=1,pa=1)[0]
            if not ts[len(ts)-1]=='_':
                if ts not in wnms:
                    wnms.append(ts)
    print wnms
    edo_fildTextsToListEdit(wnms,'edo_mnclu_list04')
    return wnms

def edo_checkShapeNodeName():
    wsns=[]
    meshes=cmds.ls(type='mesh',ni=1)
    if not meshes==None:
        for mesh in meshes:
            #mesh=meshes[1]
            ts=cmds.listRelatives(mesh,p=1,pa=1)[0]
            if not '|' in ts:
                if not ts+'Shape' in mesh:
                    if mesh not in wsns:
                        wsns.append(mesh)
            else:
                if not ts+'|'+ts.split('|')[len(ts.split('|'))-1]+'Shape' in mesh:
                    if mesh not in wsns:
                        wsns.append(mesh)          
    print wsns
    edo_fildTextsToListEdit(wsns,'edo_mnclu_list05')
    return wsns

def edo_checkOrignalShapeNodeName():
    orgs=[]
    worgs=[]
    meshes=cmds.ls(type='mesh',ni=0)
    if not meshes==None:
        for mesh in meshes:
            #mesh=meshes[2]
            io=cmds.getAttr(mesh+'.io')
            if io==True:
                orgs.append(mesh)
    print orgs
    if not orgs==None or not orgs==[]:
        for org in orgs:
            #org=orgs[2]
            ts=cmds.listRelatives(org,p=1)[0]
            fn=ts+'ShapeOrig'
            if not fn in org:
                if org not in worgs:   
                    worgs.append(org)
    print worgs
    edo_fildTextsToListEdit(worgs,'edo_mnclu_list06')
    return worgs

def edo_checkNameSpaceMesh():
    nsms=[]
    meshes=cmds.ls(type='mesh',ni=1)
    if not meshes==None:
        for mesh in meshes:
            #mesh=meshes[0]
            ts=cmds.listRelatives(mesh,p=1,pa=1)[0]
            if '|' in ts:
                if not ts in nsms:
                    nsms.append(ts)
    print nsms
    edo_fildTextsToListEdit(nsms,'edo_mnclu_list07')
    return nsms
    
def edo_checkNoZeorVertexMeshes():
    nzvms=[]
    meshes=cmds.ls(type='mesh',ni=1)
    if not meshes==None:
        for mesh in meshes:
            #mesh='MSH_eye_L_1_Shape'
            #print mesh
            num=cmds.polyEvaluate(mesh,v=1)
            po=0.0
            for n in range(0,num):
                #n=1
                #print n
                vertex=mesh+'.pnts['+str(n)+']'
                po+=(cmds.getAttr(vertex+'.pntx')+cmds.getAttr(vertex+'.pnty')+cmds.getAttr(vertex+'.pntz'))
            if not po==0.0 and not mesh in nzvms:
                nzvms.append(mesh)
    print nzvms
    edo_fildTextsToListEdit(nzvms,'edo_mnclu_list09')
    return nzvms
    
def edo_checkInVisibleFace():
    invisfs=[]
    meshes=cmds.ls(type='mesh',ni=1)
    if not meshes==None:
        for m in meshes:
            #m=meshes[0]
            if cmds.getAttr(m+'.displayInvisibleFaces'):
                invisfs.append(m) 
    print invisfs
    edo_fildTextsToListEdit(invisfs,'edo_mnclu_list10')
    return invisfs
                       
edo_modelNameCheckinList()
import maya.cmds as cmds
global edo_geometryComputer_compute

def edo_mathBlendShapeUI():
    global edo_geometryComputer_compute
    edo_geometryComputer_compute=1
    cmds.loadPlugin('geometryComputer',qt=1)
    if cmds.window('edo_mathBlendShapeUI',ex=1):
        cmds.deleteUI('edo_mathBlendShapeUI')
    cmds.window('edo_mathBlendShapeUI')
    cmds.columnLayout('edo_mathBlendShapeUI_CL01',w=380,h=300,rs=10)
    cmds.text(l='   1,field you source mesh,blendshape meshes and target mesh.')
    cmds.text(l='   2,select the math method.')
    cmds.optionMenu('edo_mathBlendShapeUI_OM01' ,label='      MATH   METHOD: ',cc='edo_mathBlendShape_OM01_ccmd()')
    cmds.menuItem( label='+' )
    cmds.menuItem( label='-' )
    cmds.menuItem( label='SkinCluster_inverse')
    cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG01',label='BASE_MESH',text='',buttonLabel='    Load    ',cw3=[100,200,100],bc='edo_loadTextListToTF(\'edo_mathBlendShapeUI_TFBG01\',\'mesh\')')
    cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG02',label='BLENDSHAPE_A',text='',buttonLabel='    Load    ',cw3=[100,200,100],bc='edo_loadTextListToTF(\'edo_mathBlendShapeUI_TFBG02\',\'mesh\')')
    cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG03',label='BLENDSHAPE_B',text='',buttonLabel='    Load    ',cw3=[100,200,100],bc='edo_loadTextListToTF(\'edo_mathBlendShapeUI_TFBG03\',\'mesh\')')
    cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG04',label='TARGET_MESH',text='',buttonLabel='    Load    ',cw3=[100,200,100],bc='edo_loadTextListToTF(\'edo_mathBlendShapeUI_TFBG04\',\'mesh\')')
    cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG05',label='TWEAK',text='',buttonLabel='    Load    ',cw3=[100,200,100],bc='edo_loadTextListToTF(\'edo_mathBlendShapeUI_TFBG05\',\'tweak\')',vis=0)
    cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG06',label='SKINCLUSTER',text='',buttonLabel='    Load    ',cw3=[100,200,100],bc='edo_loadTextListToTF(\'edo_mathBlendShapeUI_TFBG06\',\'skinCluster\')',vis=0)
    cmds.setParent('edo_mathBlendShapeUI_CL01')
    cmds.button('edo_mathBlendShapeUI_BT01',label=' MATH THE BLENDSHAPES ',w=380,h=30,bgc=[0.83,0.67,0.28],c='edo_mathBlendShapeBT01_cmd()')
    cmds.button('edo_mathBlendShapeUI_BT02',label=' stop compute ',w=380,h=30,bgc=[0.83,0.17,0.18],c='edo_mathBlendShapeUI_BT02_cmd()',vis=1)
    cmds.showWindow('edo_mathBlendShapeUI')
    cmds.window('edo_mathBlendShapeUI',e=1,w=380,h=300)

def edo_mathBlendShapeUI_BT02_cmd():
    global edo_geometryComputer_compute
    print edo_geometryComputer_compute
    if edo_geometryComputer_compute==1:
        print 'turn off\n'
        edo_geometryComputer_compute=0
        cmds.button('edo_mathBlendShapeUI_BT02',e=1,bgc=[0.18,0.83,0.17],label=' start compute ')
        edo_setAllGeometryComputerNodeState(edo_geometryComputer_compute)
        return True
    if edo_geometryComputer_compute==0:
        print 'turn on\n'
        edo_geometryComputer_compute=1
        cmds.button('edo_mathBlendShapeUI_BT02',e=1,bgc=[0.83,0.17,0.18],label=' stop compute ')   
        edo_setAllGeometryComputerNodeState(edo_geometryComputer_compute)
        return True

def edo_setAllGeometryComputerNodeState(onoff):
    #onoff=0
    gcnodes=cmds.ls(type='geometryComputer')
    if not gcnodes==None and not gcnodes==[] :
        for gcnode in gcnodes:
            #gcnode=gcnodes[0]
            if onoff==0:
                cmds.setAttr(gcnode+'.nodeState',9)
            if onoff==1:
                cmds.setAttr(gcnode+'.nodeState',0)

def edo_mathBlendShape_OM01_ccmd():
    mathMethod=cmds.optionMenu('edo_mathBlendShapeUI_OM01',q=1,v=1)
    if mathMethod=='SkinCluster_inverse':
        cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG03',e=1,vis=0)
        cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG01',e=1,vis=0)
        cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG05',e=1,vis=1)
        cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG06',e=1,vis=1)
        cmds.window('edo_mathBlendShapeUI',e=1,w=380,h=300)
    if mathMethod=='+' or mathMethod=='-':
        cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG03',e=1,vis=1)
        cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG01',e=1,vis=1)
        cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG05',e=1,vis=0)
        cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG06',e=1,vis=0)
        cmds.window('edo_mathBlendShapeUI',e=1,w=380,h=300)

def edo_mathBlendShapeBT01_cmd():
    mathMethod=cmds.optionMenu('edo_mathBlendShapeUI_OM01',q=1,v=1)
    base=cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG01',q=1,text=1)
    target=cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG04',q=1,text=1)
    amesh=cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG02',q=1,text=1)
    bmesh=cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG03',q=1,text=1)
    tweak=cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG05',q=1,text=1)
    skincluster=cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG06',q=1,text=1)
    edo_mathBlendShape(base,target,amesh,bmesh,mathMethod,tweak,skincluster)

    
    

def edo_loadTextListToTF(tfname,type):
    #tfname='edo_mathBlendShapeUI_TFBG02'
    #type='mesh'
    sels=cmds.ls(sl=1)
    if sels==None:
        cmds.confirmDialog( title='error', message='you must select something', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    nodes=[]
    for sel in sels:
        if cmds.nodeType(sel)==type:
            nodes.append(sel)
            continue
        shape=cmds.listRelatives(sel,s=1,ni=1)
        if not shape==None:
            if cmds.nodeType(shape[0])==type:
                nodes.append(sel)
    print nodes
    list=''
    for node in nodes:
        list=list+node+','
    list=list[:len(list)-1]
    cmds.textFieldButtonGrp(tfname,e=1,text=list)


#edo_mathBlendShape('MSH_body5','target','MSH_body4','MSH_body2','-')
def edo_mathBlendShape(org,target,bsa,bsb,math,tweak,skincluster):
    #org='pSphere1'
    #target='pSphere6'
    #bsa='pSphere5'
    #bsb='pSphere3'
    #math='+'
    #tweak='tweak1'
    #skincluster='skinCluster1'
    print 'create deformer now\n'
    if not cmds.objExists(target):
        cmds.warning('deform object is not enough!\n')
        return False
    gcnode=cmds.deformer(target,type='geometryComputer')[0]
    if math=='-':
        print "method is -"
        if not cmds.objExists(org) or not cmds.objExists(bsa) or not cmds.objExists(bsb):
            cmds.warning('deform object is not enough!\n')
            return False
        cmds.setAttr(gcnode+'.computeMethod',1)
        cmds.connectAttr(org+'.outMesh',gcnode+'.baseGeometry',f=1)
        cmds.connectAttr(bsa+'.outMesh',gcnode+'.targetX',f=1)
        cmds.connectAttr(bsb+'.outMesh',gcnode+'.targetY',f=1)
    if math=='+':
        print "method is +"
        if not cmds.objExists(org) or not cmds.objExists(bsa) or not cmds.objExists(bsb):
            cmds.warning('deform object is not enough!\n')
            return False
        cmds.setAttr(gcnode+'.computeMethod',0)
        cmds.connectAttr(org+'.outMesh',gcnode+'.baseGeometry',f=1)
        cmds.connectAttr(bsa+'.outMesh',gcnode+'.targetX',f=1)
        cmds.connectAttr(bsb+'.outMesh',gcnode+'.targetY',f=1)     
    if math=='SkinCluster_inverse':
        print "method is SkinCluster_inverse"
        if not cmds.objExists(tweak) or not cmds.objExists(bsa) or not cmds.objExists(skincluster):
            cmds.warning('deform object is not enough!\n')
            return False
        cmds.setAttr(gcnode+'.computeMethod',2)
        cmds.connectAttr(bsa+'.outMesh',gcnode+'.convertTarget',f=1)
        cmds.connectAttr(tweak+'.message',gcnode+'.tweakMessage',f=1)
        cmds.connectAttr(skincluster+'.message',gcnode+'.skinClusterMessage',f=1)
        cmds.connectAttr(skincluster+'.outputGeometry[0]',gcnode+'.geometryUpdata',f=1)
    print "done.."
    return True

#example:
#edo_findNodeFromHis('object','skinCluster')
#return 'skinCluster1'

def edo_findNodeFromHis(name,type):
    #name='twodline_curve'
    #type='tweak'
    node=''
    hiss=cmds.listHistory(name)
    for his in hiss:
        if cmds.nodeType(his)==type:
            node=his
    return node

edo_mathBlendShapeUI()
import maya.cmds as cmds
import maya.OpenMaya as om
global edo_g_selectBlendShape

#edo_namesOfArrayAttr('blendShape1','weight','attr')
def edo_namesOfArrayAttr(name,attr):
    #name='blendShape1'
    #attr='weight'
    attrs=[]
    obj=om.MObject()
    msel=om.MSelectionList()
    mg=om.MGlobal()
    cmds.select(name)
    mg.getActiveSelectionList(msel)
    msel.getDependNode(0,obj)
    mfndg=om.MFnDependencyNode()
    mfndg.setObject(obj)
    plug=mfndg.findPlug(attr)
    num=plug.numElements()
    for n in range(0,num):
        #n=0
        p=plug.elementByLogicalIndex(n)
        attrname=p.name()
        lens=len(attrname.split('.'))
        attrname=attrname.split('.')[lens-1]
        attrs.append(attrname)
    return attrs
        

def edo_findNodeFromHis(name,type):
    #name='twodline_curve'
    #type='tweak'
    nodes=[]
    hiss=cmds.listHistory(name)
    for his in hiss:
        if cmds.nodeType(his)==type:
            nodes.append(his)
    return nodes

def edo_makeBlendShapeWeightNormalizePaintable():
    global edo_g_selectBlendShape
    sels=cmds.ls(sl=1)
    sourcemesh=''
    if sels==None:
        cmds.confirmDialog( title='error', message='please select the source mesh!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    if '.vtx[' in sels[0]:
        sourcemesh=sels[0].split('.')[0]
    else:
        if not len(sels)==1:
            cmds.confirmDialog( title='error', message='you can select only one mesh!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
            return False
        sourcemesh=sels[0]
    bs=''
    bss=edo_findNodeFromHis(sourcemesh,'blendShape')
    if len(bss)==1:
        bs=bss[0]
    else:
        bs=cmds.confirmDialog( title='error', message='more than blendshape find,select one!', button=bss, defaultButton='Yes', cancelButton='No', dismissString='No' )
    if bs=='':
        cmds.confirmDialog( title='error', message='can not find blendShape node!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    targets=edo_namesOfArrayAttr(bs,'weight')
    skins=edo_findNodeFromHis(sourcemesh,'skinCluster')
    joints=[]
    if not skins==[]:
        bb=cmds.confirmDialog( title='error', message='more than skinCluster find,select one!', button=['create New One','transfer To Old'], defaultButton='Yes', cancelButton='No', dismissString='No' )
    if skins==[] or bb=='create New One':
        for t in targets:
            #t=targets[0]
            po=[0,0,0]
            if cmds.objExists(t):
                po=cmds.xform(t,q=1,ws=1,rp=1)
            joints.append(cmds.createNode('joint',n=t+'_bsweight'))
            cmds.xform(joints[(len(joints)-1)],ws=1,t=po)
        cmds.select(joints)
        cmds.select(sourcemesh,add=1)
        cmds.skinCluster(sourcemesh,joints,tsb=True)
        skin=edo_findNodeFromHis(sourcemesh,'skinCluster')[0]
    else:
        if len(skins)==1:
            skin=skins[0]
            joints=cmds.skinCluster(skin,q=1,inf=1)
        else:
            skin=cmds.confirmDialog( title='error', message='more than skinCluster find,select one!', button=skins, defaultButton='Yes', cancelButton='No', dismissString='No' )
            joints=cmds.skinCluster(skin,q=1,inf=1)
    wl=edo_namesOfArrayAttr(skin,'weightList')
    for s in range(0,len(wl)):
        #s=0
        w=wl[s]
        for i in range(0,len(targets)):
            #i=1
            onput=skin+'.'+w+'.weights['+str(i)+']'
            input=bs+'.it[0].itg['+str(i)+'].tw['+str(s)+']'
            cmds.setAttr(input,cmds.getAttr(onput))
    cmds.select(sels)
    
def edo_BlendShapeListUIBT1cmd():
    global edo_g_selectBlendShape
    edo_g_selectBlendShape=cmds.textScrollList('edo_BlendShapeListUITSL01',q=1,si=1)
    print edo_g_selectBlendShape
    cmds.deleteUI('edo_BlendShapeListUI')

def edo_makeBlendShapeWeightNormalizePaintableUI():
    if cmds.window("edo_makeBlendShapeWeightNormalizePaintableUI",ex=1):
        cmds.deleteUI("edo_makeBlendShapeWeightNormalizePaintableUI")
    cmds.window("edo_makeBlendShapeWeightNormalizePaintableUI",title="edo_makeBlendShapeWeightNormalizePaintableUI")
    cmds.columnLayout( columnAttach=('both', 5), rowSpacing=5, columnWidth=190)
    cmds.button('edo_makeBlendShapeWeightNormalizePaintableUIBT1',label='transfer blendshape weights',h=27,bgc=(0.1,0.9,0.7),c='edo_makeBlendShapeWeightNormalizePaintable()')
    cmds.button('edo_makeBlendShapeWeightNormalizePaintableUIBT2',label='get all blendshape target',h=27,bgc=(0.8,0.7,0.2),c='edo_getNewTargetWithBlendShapeNode()')
    cmds.showWindow("edo_makeBlendShapeWeightNormalizePaintableUI")


def edo_getNewTargetWithBlendShapeNode():
    sel=cmds.ls(sl=1)[0]
    shape=cmds.listRelatives(sel,s=1,ni=1)[0]
    nodes=cmds.listHistory(shape)
    bss=edo_findNodeFromList(nodes,'blendShape')
    bs=''
    if len(bss)==1:
        bs=bss[0]
    else:
        bs=cmds.confirmDialog( title='error', message='more than blendshape find,select one!', button=bss, defaultButton='Yes', cancelButton='No', dismissString='No' )
    if bs=='':
        cmds.confirmDialog( title='error', message='can not find blendShape node!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return False
    print ('get the target from '+bs[0])+'  :'
    attr=cmds.blendShape(bs,q=1,weight=1)
    num=len(attr)
    if not cmds.objExists('GRP_'+bs+'_newBlendShape'):
        cmds.createNode('transform',n='GRP_'+bs+'_newBlendShape')
    for u in range(0,num):
        attrname=bs+'.weight['+str(u)+']'
        cmds.setAttr(attrname,0)
    for n in range(0,num):
        #n=0
        attrname=bs+'.weight['+str(n)+']'
        longname=cmds.aliasAttr(attrname,q=1)
        print 'get '+longname+'  ...'
        cmds.setAttr(attrname,1)
        dup=cmds.duplicate(sel,n='new_'+longname)
        cmds.parent(dup,'GRP_'+bs+'_newBlendShape')
        cmds.setAttr(attrname,0)

def edo_findNodeFromList(nodes,type):
    bc=[]
    for node in nodes:
        if cmds.nodeType(node)==type:
            bc.append(node)
            print node
    return bc

edo_makeBlendShapeWeightNormalizePaintableUI()
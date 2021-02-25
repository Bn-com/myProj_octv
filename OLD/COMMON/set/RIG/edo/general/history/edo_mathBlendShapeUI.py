import maya.cmds as cmds


def edo_mathBlendShapeUI():
    if cmds.window('edo_mathBlendShapeUI',ex=1):
        cmds.deleteUI('edo_mathBlendShapeUI')
    cmds.window('edo_mathBlendShapeUI')
    cmds.columnLayout('edo_mathBlendShapeUI_CL01',w=380,h=290,rs=10)
    cmds.text(l='   1,field you source mesh,blendshape meshes and target mesh.')
    cmds.text(l='   2,select the math method.')
    cmds.text(l='   fianl=target+((A-base)+/-(B-base)).')
    cmds.optionMenu('edo_mathBlendShapeUI_OM01' ,label='      MATH   METHOD: ',cc='edo_mathBlendShape_OM01_ccmd()')
    cmds.menuItem( label='+' )
    cmds.menuItem( label='-' )
    cmds.menuItem( label='inverse')
    cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG01',label='BASE_MESH',text='',buttonLabel='    Load    ',cw3=[100,200,100],bc='edo_loadTextListToTF(\'edo_mathBlendShapeUI_TFBG01\',\'mesh\')')
    cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG02',label='BLENDSHAPE_A',text='',buttonLabel='    Load    ',cw3=[100,200,100],bc='edo_loadTextListToTF(\'edo_mathBlendShapeUI_TFBG02\',\'mesh\')')
    cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG03',label='BLENDSHAPE_B',text='',buttonLabel='    Load    ',cw3=[100,200,100],bc='edo_loadTextListToTF(\'edo_mathBlendShapeUI_TFBG03\',\'mesh\')')
    cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG04',label='TARGET_MESH',text='',buttonLabel='    Load    ',cw3=[100,200,100],bc='edo_loadTextListToTF(\'edo_mathBlendShapeUI_TFBG04\',\'mesh\')')
    cmds.setParent('edo_mathBlendShapeUI_CL01')
    cmds.button('edo_mathBlendShapeUI_BT01',label=' MATH THE BLENDSHAPES ',w=380,h=30,bgc=[0.83,0.67,0.28],c='edo_mathBlendShapeBT01_cmd()')
    cmds.showWindow('edo_mathBlendShapeUI')
    cmds.window('edo_mathBlendShapeUI',e=1,w=380,h=290)


def edo_mathBlendShape_OM01_ccmd():
    mathMethod=cmds.optionMenu('edo_mathBlendShapeUI_OM01',q=1,v=1)
    if mathMethod=='inverse':
        cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG03',e=1,vis=0)
        cmds.window('edo_mathBlendShapeUI',e=1,w=380,h=250)
    if mathMethod=='+' or mathMethod=='-':
        cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG03',e=1,vis=1)
        cmds.window('edo_mathBlendShapeUI',e=1,w=380,h=290)

def edo_mathBlendShapeBT01_cmd():
    mathMethod=cmds.optionMenu('edo_mathBlendShapeUI_OM01',q=1,v=1)
    base=cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG01',q=1,text=1)
    target=cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG04',q=1,text=1)
    amesh=cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG02',q=1,text=1)
    bmesh=cmds.textFieldButtonGrp('edo_mathBlendShapeUI_TFBG03',q=1,text=1)
    edo_mathBlendShape(base,target,amesh,bmesh,mathMethod)

    
    

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
def edo_mathBlendShape(org,target,bsa,bsb,math):
    #org='MSH_body_3'
    #target='MSH_body_3'
    #bsa='math_MSH_body_4'
    #bsb='pSphere3'
    #math='inverse'
    orgvtx=cmds.polyListComponentConversion(org,toVertex=1)
    orgvertex=cmds.ls(orgvtx,fl=1)
    mathmesh=cmds.duplicate(target,n='math_'+target)[0]
    #deform=[]
    if math=='-':
        print "method is -"
        for orgvtx in orgvertex:
            #orgvtx=orgvertex[0]
            bsavtx=orgvtx.replace(org,bsa)
            bsbvtx=orgvtx.replace(org,bsb)
            mathvtx=orgvtx.replace(org,mathmesh)
            orgvtxpo=cmds.xform(orgvtx,q=1,os=1,t=1)
            bsavtxpo=cmds.xform(bsavtx,q=1,os=1,t=1)
            bsbvtxpo=cmds.xform(bsbvtx,q=1,os=1,t=1)
            mathvtxpo=cmds.xform(mathvtx,q=1,os=1,t=1)
            deforma=[bsavtxpo[0]-orgvtxpo[0],bsavtxpo[1]-orgvtxpo[1],bsavtxpo[2]-orgvtxpo[2]]
            deformb=[bsbvtxpo[0]-orgvtxpo[0],bsbvtxpo[1]-orgvtxpo[1],bsbvtxpo[2]-orgvtxpo[2]]
            finaldeform=[mathvtxpo[0]+(deforma[0]-deformb[0]),(mathvtxpo[1]+deforma[1]-deformb[1]),(mathvtxpo[2]+deforma[2]-deformb[2])]
            cmds.xform(mathvtx,os=1,t=finaldeform)
            #deform.append(finaldeform)
    if math=='+':
        print "method is +"
        for orgvtx in orgvertex:
            #orgvtx=orgvertex[0]
            bsavtx=orgvtx.replace(org,bsa)
            bsbvtx=orgvtx.replace(org,bsb)
            mathvtx=orgvtx.replace(org,mathmesh)
            orgvtxpo=cmds.xform(orgvtx,q=1,os=1,t=1)
            bsavtxpo=cmds.xform(bsavtx,q=1,os=1,t=1)
            bsbvtxpo=cmds.xform(bsbvtx,q=1,os=1,t=1)
            mathvtxpo=cmds.xform(mathvtx,q=1,os=1,t=1)
            deforma=[bsavtxpo[0]-orgvtxpo[0],bsavtxpo[1]-orgvtxpo[1],bsavtxpo[2]-orgvtxpo[2]]
            deformb=[bsbvtxpo[0]-orgvtxpo[0],bsbvtxpo[1]-orgvtxpo[1],bsbvtxpo[2]-orgvtxpo[2]]
            finaldeform=[mathvtxpo[0]+(deforma[0]+deformb[0]),(mathvtxpo[1]+deforma[1]+deformb[1]),(mathvtxpo[2]+deforma[2]+deformb[2])]
            cmds.xform(mathvtx,os=1,t=finaldeform)
    if math=='inverse':
        print "method is inverse"
        for orgvtx in orgvertex:
            #orgvtx=orgvertex[0]
            bsavtx=orgvtx.replace(org,bsa)
            mathvtx=orgvtx.replace(org,mathmesh)
            orgvtxpo=cmds.xform(orgvtx,q=1,os=1,t=1)
            bsavtxpo=cmds.xform(bsavtx,q=1,os=1,t=1)
            mathvtxpo=cmds.xform(mathvtx,q=1,os=1,t=1)
            deforma=[(bsavtxpo[0]-orgvtxpo[0])*-1,(bsavtxpo[1]-orgvtxpo[1])*-1,(bsavtxpo[2]-orgvtxpo[2])*-1]
            finaldeform=[mathvtxpo[0]+deforma[0],mathvtxpo[1]+deforma[1],mathvtxpo[2]+deforma[2]]
            cmds.xform(mathvtx,os=1,t=finaldeform)
            #deform.append(finaldeform)
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
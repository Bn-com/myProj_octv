import maya.cmds as cmds
global jointList
global positionList
global rotationList
global scaleList
global joList

#edo_gdcfrig2012_createFacialJoint(3,3,3,3,7)
def edo_gdcfrig2012_createFacialJoint(lipnum,eyelidnum,nosenum,earnum,tonguenum):
    #lipnum=3
    #eyelidnum=5
    #nosenum=4
    #earnum=3
    #tonguenum=8
    if cmds.objExists('D_head_driven'):
        cmds.delete('D_head_driven')
    cmds.createNode('joint',n='D_head_driven')
    cmds.createNode('joint',n='D_jaw_driven',p='D_head_driven')
    cmds.createNode('joint',n='D_jaw_skin',p='D_jaw_driven')
    cmds.xform('D_jaw_skin',os=1,t=[0,-1,3])
    cmds.xform('D_jaw_driven',os=1,t=[0,2,1])
    cmds.createNode('joint',n='D_nose_driven',p='D_head_driven')
    cmds.xform('D_nose_driven',os=1,t=[0,4,2])
    cmds.createNode('joint',n='D_eyelid_l_driven',p='D_head_driven')
    cmds.xform('D_eyelid_l_driven',os=1,t=[2,6,2])
    cmds.createNode('joint',n='D_ear_l_driven',p='D_head_driven')
    cmds.xform('D_ear_l_driven',os=1,t=[4,4,0])
    cmds.createNode('joint',n='D_tongue_driven',p='D_jaw_driven')
    cmds.xform('D_tongue_driven',os=1,t=[0,0,1])
    cmds.createNode('joint',n='D_upteeth_driven',p='D_jaw_driven')
    cmds.xform('D_upteeth_driven',os=1,t=[0,0.5,2])
    cmds.createNode('joint',n='D_dnteeth_driven',p='D_jaw_driven')
    cmds.xform('D_dnteeth_driven',os=1,t=[0,-0.5,2])
    for i in range(0,lipnum):
        #i=1
        if i==0:
            cmds.createNode('joint',n='D_uplip_m_skin',p='D_jaw_driven')
            cmds.xform('D_uplip_m_skin',os=1,t=[0,0.2,2.8])
            cmds.createNode('joint',n='D_dnlip_m_skin',p='D_jaw_driven')
            cmds.xform('D_dnlip_m_skin',os=1,t=[0,-0.2,2.8])
        else:
            cmds.createNode('joint',n='D_uplip_l_'+str(i)+'_skin',p='D_jaw_driven')
            cmds.xform('D_uplip_l_'+str(i)+'_skin',os=1,t=[i*0.3,0.2,2.8])
            cmds.createNode('joint',n='D_dnlip_l_'+str(i)+'_skin',p='D_jaw_driven')
            cmds.xform('D_dnlip_l_'+str(i)+'_skin',os=1,t=[i*0.3,-0.2,2.8])
    e=-int(eyelidnum/2)
    for i in range(0,eyelidnum):
        #i=0
        cmds.createNode('joint',n='D_uplid_l_'+str(i)+'_skin',p='D_eyelid_l_driven')
        cmds.xform('D_uplid_l_'+str(i)+'_skin',os=1,t=[e+i,0.5,1])
        cmds.createNode('joint',n='D_dnlid_l_'+str(i)+'_skin',p='D_eyelid_l_driven')
        cmds.xform('D_dnlid_l_'+str(i)+'_skin',os=1,t=[e+i,-0.5,1])
    parentJoint='D_nose_driven'
    for i in range(0,nosenum):
        tmp=cmds.createNode('joint',n='D_nose_'+str(i)+'_skin',p=parentJoint)
        cmds.xform('D_nose_'+str(i)+'_skin',os=1,t=[0,0,0.2])
        parentJoint=tmp
    parentJoint='D_ear_l_driven'
    for i in range(0,earnum):
        parentJoint=cmds.createNode('joint',n='D_ear_l_'+str(i)+'_skin',p=parentJoint)
        cmds.xform('D_ear_l_'+str(i)+'_skin',os=1,t=[0.2,0,0])
    parentJoint='D_tongue_driven'
    for i in range(0,tonguenum):
        parentJoint=cmds.createNode('joint',n='D_tongue_'+str(i)+'_skin',p=parentJoint)
        cmds.xform('D_tongue_'+str(i)+'_skin',os=1,t=[0,0,0.2])

#edo_gdcfrig2012_refreshFacialJoint(1,3,3,3,3,7)
def edo_gdcfrig2012_refreshFacialJoint(keepposition,lipnum,eyelidnum,nosenum,earnum,tonguenum):
    jointList=[]
    positionList=[]
    rotationList=[]
    scaleList=[]
    joList=[]
    if not cmds.objExists('D_head_driven'):
        return False
    cmds.select('D_head_driven')
    cmds.select(hi=1)
    alljoints=cmds.ls(sl=1)
    for jnt in alljoints:
        #jnt=alljoints[0]
        print jnt
        position=[cmds.getAttr(jnt+'.tx'),cmds.getAttr(jnt+'.ty'),cmds.getAttr(jnt+'.tz')]
        rotation=[cmds.getAttr(jnt+'.rx'),cmds.getAttr(jnt+'.ry'),cmds.getAttr(jnt+'.rz')]
        scales=[cmds.getAttr(jnt+'.sx'),cmds.getAttr(jnt+'.sy'),cmds.getAttr(jnt+'.sz')]
        jo=[cmds.getAttr(jnt+'.jointOrientX'),cmds.getAttr(jnt+'.jointOrientY'),cmds.getAttr(jnt+'.jointOrientZ')]
        jointList.append(jnt)
        positionList.append(position)
        rotationList.append(rotation)
        scaleList.append(scales)
        joList.append(jo)
    print positionList
    edo_gdcfrig2012_createFacialJoint(lipnum,eyelidnum,nosenum,earnum,tonguenum)
    if keepposition==1:
        for i in range(0,len(jointList)):
            #i=0
            jnt=jointList[i]
            position=positionList[i]
            rotation=rotationList[i]
            scales=scaleList[i]
            jo=joList[i]
            if cmds.objExists(jnt):
                cmds.setAttr(jnt+'.tx',position[0])
                cmds.setAttr(jnt+'.ty',position[1])
                cmds.setAttr(jnt+'.tz',position[2])
                cmds.setAttr(jnt+'.rx',rotation[0])
                cmds.setAttr(jnt+'.ry',rotation[1])
                cmds.setAttr(jnt+'.rz',rotation[2])
                cmds.setAttr(jnt+'.sx',scales[0])
                cmds.setAttr(jnt+'.sy',scales[1])
                cmds.setAttr(jnt+'.sz',scales[2])
                cmds.setAttr(jnt+'.jointOrientX',jo[0])
                cmds.setAttr(jnt+'.jointOrientY',jo[1])
                cmds.setAttr(jnt+'.jointOrientZ',jo[2])          
                
def edo_gdcfrig2012_separateJoint():
    if not cmds.objExists('D_head_driven'):
        return False
    cmds.select('D_head_driven')
    cmds.select(hi=1)
    cmds.parent(w=1)

def edo_gdcfrig2012_mirrorFacialJoint():
    if cmds.objExists('D_eyelid_l_driven'):
        if cmds.objExists('D_eyelid_r_driven'):
            cmds.delete('D_eyelid_r_driven')
        cmds.mirrorJoint('D_eyelid_l_driven',mirrorYZ=True,searchReplace=['_l_','_r_'])
    if cmds.objExists('D_ear_l_driven'):
        if cmds.objExists('D_ear_r_driven'):
            cmds.delete('D_ear_r_driven')
        cmds.mirrorJoint('D_ear_l_driven',mirrorBehavior=True,mirrorYZ=True,searchReplace=['_l_','_r_'])
    lf_lips=cmds.ls('D_*lip_l_*_skin',type='joint')
    for l in lf_lips:
        if cmds.objExists(l.replace('_l_','_r_')):
            cmds.delete(l.replace('_l_','_r_'))
        cmds.mirrorJoint(l,mirrorYZ=True,searchReplace=['_l_','_r_'])  
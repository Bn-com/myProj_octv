import maya.cmds as cmds
def edo_addTooManyInbetweenBlendShape():
    sels=cmds.ls(sl=1)
    m=sels[len(sels)-1]
    sels.remove(m)
    l=len(sels)
    print 'createInbetween blendShape:\n'
    for i in range(0,l/2):
        #i=0
        n=l/2+i
        print sels[i]+'    ....    '+sels[n]
        cmds.select(sels[i],r=1)
        cmds.select(sels[n],add=1)
        cmds.select(m,add=1)
        edo_edo_addInbetweenBlendShape()
edo_addTooManyInbetweenBlendShape()
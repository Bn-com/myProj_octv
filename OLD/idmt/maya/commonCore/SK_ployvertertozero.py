objGrp=mc.ls(sl=1)        
if objGrp:             
    for obj in objGrp:
        mesh=mc.listRelatives(obj,s=1,ni=1,f=1)
        if mesh:
            mesh=mesh[0]
            edgeNum=mc.polyEvaluate(mesh,edge=1)
        if edgeNum:
            for num in range(edgeNum):
                mc.setAttr((mesh+'.pnts['+str(num)+'].pntx'),0)
                mc.setAttr((mesh+'.pnts['+str(num)+'].pnty'),0)
                mc.setAttr((mesh+'.pnts['+str(num)+'].pntz'),0)
else:
    mc.confirmDialog(title=u'警告', message=u'请选择物体', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No') 
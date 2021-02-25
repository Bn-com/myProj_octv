
import maya.cmds as mc
ui='//file-cluster/GDC/Resource/Support/Python/2.6-x64/Lib/site-packages/idmt/maya/norch/QT/Nor_renderTools.myuis'
if mc.window('Nor_renderTools',ex=1):
    mc.deleteUI('Nor_renderTools')
mui=mc.loadUI(f=ui)

mc.window("Nor_renderTools",e=1,tlc=(10,10))
mc.showWindow(mui)
mc.button("creatproject",e=1,c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/Strawberry4/sk4_SetProject.mel"\')\nmel.eval(\"skSetProject\")')
mc.button("deleteLayer",e=1,c='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldALLDelete(nodetype="renderLayer")')  

mc.button("hmesh_exr",e=1,c='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().NorH_meshCreate()')  
mc.button("Amesh_exr",e=1,c='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().NorA_MeshCreate()')  
mc.button("humanIDP",e=1,c='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().Nor_IDPCreate(\'CHR\')')  
mc.button("animalIDP",e=1,c ='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().Nor_IDPCreate(\'AN\')')   
mc.button("Afur_tif",e=1,c ='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().NorA_FurCreate()')  
mc.button("Hfur_tif",e=1,c='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().NorH_FurCreate()')  

mc.button("save_ligntingfile",e=1,c='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().Nor_filelightingSave()')  
mc.button("save_Hfile",e=1,c='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().Nor_SeprateFileSave(\'CHR\')')  
mc.button("save_Afile",e=1,c='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().Nor_SeprateFileSave(\'AN\')')  
mc.button("import_Hlight",e=1,c='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().norlightingImp(\'CHR\')')  
mc.button("import_Alight",e=1,c='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().norlightingImp(\'AN\')')  

mc.button("ALL_IDP",e=1,c ='from idmt.maya.norch import north_renderLayer\nreload(north_renderLayer)\nnorth_renderLayer.north_renderLayer().ALLRGBCreate()') 


mc.button("shadow",e=1,c ='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign(\'Shadow\',0)')
mc.button("occ",e=1,c ='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign(\'AO\',0)')
mc.button("refrection",e=1,c ='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign(\'reflection\',0)')

mc.button('R',e=1,command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpR")')
mc.button('G',e=1,command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpG")')
mc.button('B',e=1,command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpB")')
mc.button('M',e=1,command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpM")')
mc.button('Y',e=1,command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpY")') 
mc.button('C',e=1,command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpC")') 
mc.button('K',e=1,command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpK")')  
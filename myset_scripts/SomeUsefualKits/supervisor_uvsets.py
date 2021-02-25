import pymel.core as pm
import maya.api.OpenMaya as om2

iffy = None
def check_uv(model):  
    model = pm.selected()[0]
    mSel = om2.MSelectionList()
    
    mSel.add(model.name())
    mDag = mSel.getDagPath(0)
    mFnMesh= om2.MFnMesh(mDag)
    UVSets_lst = mFnMesh.getUVSetNames()
    if not 'map1' in UVSets_lst:
        iffy = True
        return  
    
    Ucods,Vcods = mFnMesh.getUVs('map1')
    if not (Ucods.__len__() or Vcods.__len__()):
       iffy = True 

    #uv_counts, uvIDs = MFnMesh.getAssignedUVs(uvset)
import maya.cmds as cmds

def _listGeoTransforms():
    """ Return transforms of geometry nodes only """
    return list(set(cmds.listRelatives([mesh for mesh in cmds.ls(type='mesh')], p=True)))

def _listGeoParentedToBillCtrl():
    """ Return transforms of geometry nodes prented to c_BIL_ controlers """
    geoLs = []
    for ctrl in cmds.ls("c_BIL_*", type='transform'):
        for child in cmds.listRelatives(ctrl, ad=True, f=True):
            if cmds.nodeType(child) == 'mesh':
                geoLs.append(cmds.listRelatives(child, p=True)[0])
    return geoLs

def addMiLabel(trLs, value=0, log=False):
    """ Add miLabel attribute on a given list """
    if not trLs:
        # --- Get selection if no input
        trLs = cmds.ls(sl=True, type='transform')
        if not trLs:
            cmds.warning('Invalid selection. Please select geometry transforms')
            return False
    count = 0
    crCount = 0
    for tr in trLs:
        if not cmds.attributeQuery('miLabel', n=tr, ex=True):
            cmds.addAttr(tr, ln='miLabel', at='double')
            cmds.setAttr(tr+'.miLabel', k=True, cb=True)
            count += 1
        cmds.setAttr(tr+'.miLabel', 1)

        crCount += 1
    # --- Print
    if log and crCount:
        print '# miLabel created: %s' %crCount
    if log and count:
        print '# miLabel set to %s: %s' %(value, count)
    return True
def delMiLabel(trLs=None, log=False):
    if not trLs:
        trLs = _listGeoTransforms()
    count = 0
    for tr in trLs:
        if cmds.attributeQuery('miLabel', n=tr, ex=True):
            cmds.deleteAttr(tr+'.miLabel')
            count += 1
    # --- Print
    if log and count:
        print '# miLabels deleted: %s' %count

def setAoIndex(log=False):
    """
    Set inclexcl index of AO texture nodes
    -5 for Billboards
    -1 for other nodes
    """
    bilCount = 0
    count = 0    
    for aoTex in cmds.ls(type='mib_amb_occlusion'):
        if 'AO' in aoTex:
            if 'BIL' in aoTex:
                cmds.setAttr(aoTex+'.id_inclexcl', -5)
                bilCount += 1
            else:
                cmds.setAttr(aoTex+'.id_inclexcl', -1)
                count += 1
    # --- Print
    if log and bilCount:
        print '# Billboard AO texture inclexcl index set to -5: %s' %bilCount
    if log and count:
        print '# Regular AO texture inclexcl index set to -1: %s' %count

def configMiLabel(recreate=False, log=False):
    """ Configure miLabel attributes in the whole scene """
    if recreate:
        # --- Delete all miLabels
        delMiLabel(log=log)
    result=addMiLabel(filter(lambda x: 'msh_BIL_' in x, _listGeoTransforms()) + _listGeoParentedToBillCtrl(), value=1, log=log)
    setAoIndex(log=log)
    log_final=""
    if result == True:
        log_final = "- msh_BIL MiLabel -1 : DONE ! \n- AO shaders Id Inclexcl -1 : DONE !" 
    else:
        log_final = "- AO shaders Id Inclexcl -1 : DONE !"
    result = cmds.confirmDialog(title='Finished', message= log_final, button=['Close'])

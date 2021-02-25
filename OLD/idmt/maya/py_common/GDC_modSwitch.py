def csl_switchMode():
    mode = ''
    dt = radioButtonGrp('csl_dt', q = True, select = True )
    modeInt = radioButtonGrp('csl_mode', q = True, select = True )
    selType = radioButtonGrp('csl_selType', q = True, select = True )
    if modeInt == 2:
	    mode = '_p'
    elif modeInt == 3:
        mode = '_l'

    elif modeInt == 1:
        mode = '_h'

    sels = ls( sl = True)
    
    if selType == 2:
        if len(sels) == 1:
            ctrl = csl_getMiscCtrl(sels[0])
            print ctrl
            if ctrl:
                objectName = csl_returnMiscName(ctrl)
                allMisc = ls(objectName + '*', type = 'transform')
                del sels[:]
                for m in allMisc:
                    if csl_getMiscCtrl(m):
                        sels.append(csl_getMiscCtrl(m))
        else:
            return 0
            
    sels = list(set(sels))
   
    for sel in sels:
        ctrl = csl_getMiscCtrl(sel)
        
        objectName = csl_returnMiscName(ctrl)
    
        if not objectName:
            return 0
            
        if objectName.find(':') > -1:
            objectName = objectName.split(':')[1]
        
        
        if not objExists(objectName + mode + '_ctrl_MiscType'):
           
            newCtrl = csl_importMisc( objectName,mode )
            if newCtrl:
                rename(newCtrl, objectName + mode + '_ctrl_MiscType')
   
            
    for sel in sels:
        ctrl = csl_getMiscCtrl(sel)
        
        objectName = csl_returnMiscName(ctrl)
            
        if not objectName:
            return 0
                
        if objectName.find(':') > -1:
            objectName = objectName.split(':')[1]
        
        newCtrl = ''
        miscObj = objectName + mode + '_ctrl_MiscType'
          
        if objExists(miscObj):
            #if dt == 1:
                #newCtrl = duplicate(miscObj, n = objectName + mode + '_ctrl_#' )[0]
            #else:
            newCtrl = duplicate(miscObj, instanceLeaf  = True, n = objectName + mode + '_ctrl_#' )[0]
            
            if ctrl.getParent():
                parent(newCtrl,ctrl.getParent())
            csl_copyKeyWith2Obj(ctrl,newCtrl)
            try:
                mc.setAttr(ctrl + '.visibility', 0)
                delete(ctrl)
            except:
                mc.setAttr(ctrl + '.visibility', 0)
        
    allMiscType = ls('*_ctrl_MiscType')
    if allMiscType:
        try:
            for misc in allMiscType:
                mc.setAttr(misc + '.visibility', 0)
            delete(allMiscType)
        except:
            for misc in allMiscType:
                mc.setAttr(misc + '.visibility', 0)
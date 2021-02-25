# --- Create Custom Visibility: tt_visibility
# --- 1.0
import maya.cmds as mc
for ctrlLg in filter(lambda y: not y.rpartition('|')[-1].startswith('c_LGT_') and not y.rpartition('|')[-1].startswith('c_BIL_'), sorted(mc.ls('c_*', tr=True, l=True), key = lambda x: len(x.split('|')), reverse=True)):
    ctrl = ctrlLg.rpartition('|')[-1]
    
    if not mc.attributeQuery('tt_visibility', ex=True, n=ctrlLg):
        
        # --- Add Custom Vis attribute
        mc.addAttr(ctrlLg, ln='tt_visibility', at='enum', en='visible:hidden:primary_off')
        mc.setAttr(ctrlLg+'.tt_visibility', e=True, k=True)
        mc.setAttr(ctrlLg+'.visibility', k=False, cb=False)
    
        # --- Create Vis Group hierarchy
        visGrp = mc.group(em=True, n=ctrl.replace('c_', 'vis_'))
        ctrlPos = mc.xform(ctrlLg, q=True, ws=True, t=True)
        ctrlPiv = mc.xform(ctrlLg, q=True, r=True, piv=True)
        ctrlRot = mc.xform(ctrlLg, q=True, ws=True, ro=True)
        mc.xform(visGrp, ws=True, t=ctrlPos[:3])
        mc.xform(visGrp, ws=True, ro=ctrlRot)
        mc.xform(visGrp, r=True, piv=ctrlPiv[:3])
        childrenLs = mc.listRelatives(ctrlLg, c=True, typ='transform', f=True)
        mc.parent(visGrp, ctrlLg)
        mc.parent(childrenLs, visGrp)
        
        # --- Plug Condition node
        cdNode = mc.createNode('condition', n=ctrl.replace('c_', 'cond_'))
        mc.setAttr(cdNode + '.operation', 2)
        mc.connectAttr(ctrlLg+'.tt_visibility', cdNode+'.firstTerm')
        mc.connectAttr(cdNode+'.outColorR', visGrp+'.visibility')
        
        # --- Print
        print 'Custom Visibility has been added to: %s' %ctrl
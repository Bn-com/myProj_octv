def smoothSetBuild(self , projType = 1):
# smoothLeval
if projType == 1:
    smoothLeval_0 = 'smooth_0'
    smoothLeval_1 = 'smooth_1'
    smoothLeval_2 = 'smooth_2'
else:
    smoothLeval_0 = 'smooth_0_lv'
    smoothLeval_1 = 'smooth_1_lv'
    smoothLeval_2 = 'smooth_2_lv'



# 创建默认Set
if mc.objExists('SMOOTH_SET'):    pass
else:
    mc.createNode('objectSet', n='SMOOTH_SET')
# smooth_0
smoothObjs_lv0 = []
if mc.objExists(smoothLeval_0):
    smoothObjs_lv0 = mc.sets(smoothLeval_0 , q = 1)
    mc.delete(smoothLeval_0)
mc.createNode('objectSet', n= smoothLeval_0 )
mc.sets(smoothLeval_0, e=1, addElement='SMOOTH_SET')   
if smoothObjs_lv0:
    mc.sets(smoothObjs_lv0 , e=1 , addElement= smoothLeval_0) 
# smooth_1
smoothObjs_lv1 = []       
if mc.objExists(smoothLeval_1):
    smoothObjs_lv1 = mc.sets(smoothLeval_1 , q = 1)
    mc.delete(smoothLeval_1)
mc.createNode('objectSet', n= smoothLeval_1 )
mc.sets(smoothLeval_1, e=1, addElement='SMOOTH_SET')    
if smoothObjs_lv1:
    mc.sets(smoothObjs_lv1 , e=1 , addElement= smoothLeval_1) 
# smooth_2
smoothObjs_lv2 = []       
if mc.objExists(smoothLeval_2):
    smoothObjs_lv2 = mc.sets(smoothLeval_2 , q = 1)
    mc.delete(smoothLeval_2)
mc.createNode('objectSet', n= smoothLeval_2 )
mc.sets(smoothLeval_2, e=1, addElement='SMOOTH_SET')
if smoothObjs_lv2:
    mc.sets(smoothObjs_lv2 , e=1 , addElement= smoothLeval_2) 
mc.select(cl = 1)
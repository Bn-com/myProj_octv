##################################
#    Script Name: YJcreateCtrl   #
#    Author:  YeJun              #
#    Last Updated:  2009/08/17   #
##################################

from maya.cmds import *

def YJcreateCtrl():
    if window('testwindow',q=True,ex=True):
        deleteUI('testwindow')
    window('testwindow',title="Auto Add Control Window",menuBar = True)
    menu(label = "help")
    menuItem(label="help")
    frameLayout('tab1',labelVisible=0,bs = "etchedOut",mh = 5,mw =5)
    columnLayout(adj=1)
    radioButtonGrp("seltypeRB", numberOfRadioButtons=3, label='select Method:', 
			labelArray3=['select','hierarchy','all'] , select = 1 , cw4 = [85,65,65,65])                                 
    radioButtonGrp("addtypeRB", numberOfRadioButtons=3, label='add Method:', 
			labelArray3=['self','parent','constrain'] , select = 1 , cw4 = [85,65,65,65])                                
    radioButtonGrp("constraintypeRB", numberOfRadioButtons=3, label='Constrain:', 
			labelArray3=['Point','Orient','Parent'] , select = 3 , cw4 = [85,65,65,65])					     										
    separator(h=5,style = 'in')
    floatFieldGrp("directionRFG",label='ctrl Direction:', numberOfFields=3 , value1=1,value2=0 ,value3=0,cw4 = [85,60,60,60])    
    #floatFieldGrp("radiusRFG",label='radius:', value1=1 ,cw2 = [60,60])
    floatSliderGrp("radiusFSG", label='CV Radius:',extraLabel="", field=True, minValue=0, maxValue=10.0, 
			fieldMinValue=0, fieldMaxValue=100.0, value=1 ,cw4= [85,60,120,1],columnAttach4=["both","both","both","both"])  

    separator(h=5,style = 'in')
    #radioButtonGrp("colorRB", numberOfRadioButtons=3, label='color Method:', 
			#labelArray3=['None','select','auto'] , select = 1 , cw4 = [85,65,65,65])                                     
    #colorIndexSliderGrp("colorISG" , label='Color:', min=0, max=32, value=0 ,cw4 = [85,60,120,1])                                   

    separator(h=10,style = 'in')
    button(label='add cv control',h = 30 ,command = "createCvCtrl()")
    separator(h=8,style = 'in')
    button(label='delete cv shape',h = 30 ,command = "deleteCVshape()")
    separator(h=10,style = 'in')
    window('testwindow',edit = True,w=300,h=250)
    showWindow('testwindow')


def createCvCtrl():
	addtype = radioButtonGrp("addtypeRB",q=True,select = True )
	if addtype == 1:
		createCvShapeCtr()
	if addtype == 2:
		createParentCtrl()
	if addtype == 3:
		createConstrainCtrl()



def createCvShapeCtr():
    seltype = radioButtonGrp("seltypeRB",q=True,select = True )
    addtype = radioButtonGrp("addtypeRB",q=True,select = True )
    cvradius = floatSliderGrp("radiusFSG",q=True, value=True )
    directionX= floatFieldGrp("directionRFG",q=True, value1=True )
    directionY= floatFieldGrp("directionRFG",q=True, value2=True )
    directionZ= floatFieldGrp("directionRFG",q=True, value3=True )
    #colorIndex =  colorIndexSliderGrp("colorISG" , q=True, value=True )
    if seltype == 1 and addtype == 1 :
		selectObj = ls(sl=True)
		sel = ""
		for eachselect1 in selectObj:
			cv = circle(ch = 0,nr =[directionX,directionY,directionZ],r=cvradius,name=(eachselect1 + "_curve"))
			pickWalk(d='down')
			select(eachselect1 ,add=True)
			parent(r=True,shape=True)
			delete(cv)
			lockTranslate(eachselect1)
			lockScale(eachselect1)
			lockVis(eachselect1)
			lockRadius(eachselect1)
                                                                                                         
    if seltype == 2 and addtype == 1 :
       selparent = ls(sl=True)
       selchild = listRelatives(selparent,allDescendents=True,type = "joint")
       sel = selparent + selchild 
    if seltype == 3 and addtype == 1 :
    	sel = ls(type = 'joint')
    for eachsel in sel:
	checksel = listRelatives(eachsel,c=True )
	try:
		if len(checksel) != 0:
    			cv = circle(ch = 0,nr =[directionX,directionY,directionZ],r=cvradius,name=(eachsel + "_curve"))
    			pickWalk(d='down')
    			select(eachsel,add=True)
    			parent(r=True,shape=True)
    			delete(cv)
			lockTranslate(eachsel)
			lockScale(eachsel)
			lockVis(eachsel)
			lockRadius(eachsel)
	except:
		pass


def createConstrainCtrl():
    seltype = radioButtonGrp("seltypeRB",q=True,select = True )
    addtype = radioButtonGrp("addtypeRB",q=True,select = True )
    cvradius = floatSliderGrp("radiusFSG",q=True, value=True )
    directionX= floatFieldGrp("directionRFG",q=True, value1=True )
    directionY= floatFieldGrp("directionRFG",q=True, value2=True )
    directionZ= floatFieldGrp("directionRFG",q=True, value3=True )
    #colorIndex =  colorIndexSliderGrp("colorISG" , q=True, value=True )
    constraintype = radioButtonGrp("constraintypeRB", q=True,select = True)	
    if seltype == 1 and addtype == 3 :
		selectObj = ls(sl=True)
		sel = ""
		for eachselect1 in selectObj:
			cv = circle(ch = 0,nr =[directionX,directionY,directionZ],r=cvradius,name=(eachselect1 + "_ctrl"))
			group(name=(eachselect1 + "_grp"))
			pConstraint = parentConstraint( eachselect1 , (eachselect1 + "_grp"),  w=1 )
			delete(pConstraint )
			if constraintype == 1 :
				pConstraint = pointConstraint( (eachselect1 + "_ctrl"), eachselect1 ,mo = True, w=1 )
				lockRotate((eachselect1 + "_ctrl"))
				lockScale((eachselect1 + "_ctrl"))
			if constraintype == 2 :
				pConstraint = orientConstraint( (eachselect1 + "_ctrl"), eachselect1 ,mo = True, w=1 )
				lockTranslate((eachselect1 + "_ctrl"))
				lockScale((eachselect1 + "_ctrl"))
			if constraintype == 3 :
				pConstraint = parentConstraint( (eachselect1 + "_ctrl"), eachselect1 ,mo = True, w=1 )
				lockScale((eachselect1 + "_ctrl"))

		for eachselect2 in selectObj:
			parentNode = listRelatives(eachselect2 ,parent=True)
			try:
				parentJoint = nodeType(parentNode[0])
				if parentJoint == "joint":
					parent((eachselect2 +"_grp"), (parentNode[0]+"_ctrl"))
			except:
				pass

                                                                                                         
    if seltype == 2 and addtype == 3 :
       selparent = ls(sl=True)
       selchild = listRelatives(selparent,allDescendents=True,type = "joint")
       sel = selparent + selchild 
    if seltype == 3 and addtype == 3 :
    	sel = ls(type = 'joint')
    for eachsel in sel:
	checksel = listRelatives(eachsel,c=True )
	try:
		if len(checksel) != 0:
			cv = circle(ch = 0,nr =[directionX,directionY,directionZ],r=cvradius,name=(eachsel + "_ctrl"))
			group(name=(eachsel + "_grp"))
			pConstraint = parentConstraint( eachsel , (eachsel + "_grp"),  w=1 )
			delete(pConstraint )
			if constraintype == 1 :
				pConstraint = pointConstraint( (eachsel + "_ctrl"), eachsel ,mo = True, w=1 )
				lockRotate((eachsel + "_ctrl"))
				lockScale((eachsel + "_ctrl"))
			if constraintype == 2 :
				pConstraint = orientConstraint( (eachsel + "_ctrl"), eachsel ,mo = True, w=1 )
				lockTranslate((eachsel + "_ctrl"))
				lockScale((eachsel + "_ctrl"))
			if constraintype == 3 :
				pConstraint = parentConstraint( (eachsel + "_ctrl"), eachsel ,mo = True, w=1 )
				lockScale((eachsel + "_ctrl"))

	except:
		pass

    for eachsel1 in sel:
	parentNode = listRelatives(eachsel1 ,parent=True)
	try:
		parentJoint = nodeType(parentNode[0])
		if parentJoint == "joint":
			parent((eachsel1 +"_grp"), (parentNode[0]+"_ctrl"))
	except:
		pass



def createParentCtrl():
    seltype = radioButtonGrp("seltypeRB",q=True,select = True )
    addtype = radioButtonGrp("addtypeRB",q=True,select = True )
    cvradius = floatSliderGrp("radiusFSG",q=True, value=True )
    directionX= floatFieldGrp("directionRFG",q=True, value1=True )
    directionY= floatFieldGrp("directionRFG",q=True, value2=True )
    directionZ= floatFieldGrp("directionRFG",q=True, value3=True )
    #colorIndex =  colorIndexSliderGrp("colorISG" , q=True, value=True )
    constraintype = radioButtonGrp("constraintypeRB", q=True,select = True)	
    if seltype == 1 and addtype == 2 :
		selectObj = ls(sl=True)
		sel = ""
		for eachselect1 in selectObj:
			cv = circle(ch = 0,nr =[directionX,directionY,directionZ],r=cvradius,name=(eachselect1 + "_ctrl"))
			group(name=(eachselect1 + "_grp"))
			pConstraint = parentConstraint( eachselect1 , (eachselect1 + "_grp"),  w=1 )
			delete(pConstraint )
			eachParent = listRelatives(eachselect1 ,parent=True)
			try:
				parent((eachselect1 + "_grp"),eachParent[0])
			except:
				pass
			parent(eachselect1 ,(eachselect1 + "_ctrl"))
	

                                                                                                         
    if seltype == 2 and addtype == 2 :
       selparent = ls(sl=True)
       selchild = listRelatives(selparent,allDescendents=True,type = "joint")
       sel = selparent + selchild 
    if seltype == 3 and addtype == 2 :
    	sel = ls(type = 'joint')
    for eachsel in sel:
	checksel = listRelatives(eachsel,c=True )
	try:
		if len(checksel) != 0:
			cv = circle(ch = 0,nr =[directionX,directionY,directionZ],r=cvradius,name=(eachsel + "_ctrl"))
			group(name=(eachsel + "_grp"))
			pConstraint = parentConstraint( eachsel, (eachsel + "_grp"),  w=1 )
			delete(pConstraint )
			eachParent = listRelatives(eachsel,parent=True)
			try:
				parent((eachsel + "_grp"),eachParent[0])
			except:
				pass
			parent(eachsel,(eachsel + "_ctrl"))

	except:
		pass



def deleteCVshape():
	selObj = ls(sl=True)
	for eachObj in selObj:
		if nodeType(eachObj)=="joint":
			allshape = listRelatives(eachObj,s=True)
			delete(allshape)
		else:
			print(eachObj + " is not joint type;")
deleteCVshape()



def lockTranslate(lockTranslateObj):
	setAttr(lockTranslateObj+".tx",keyable=False,lock=True)
	setAttr(lockTranslateObj+".ty",keyable=False,lock=True)
	setAttr(lockTranslateObj+".tz",keyable=False,lock=True)

def lockRotate(lockRotateObj):
	setAttr(lockRotateObj+".rx",keyable=False,lock=True)
	setAttr(lockRotateObj+".ry",keyable=False,lock=True)
	setAttr(lockRotateObj+".rz",keyable=False,lock=True)

def lockScale(lockScaleObj):
	setAttr(lockScaleObj+".sx",keyable=False,lock=True)
	setAttr(lockScaleObj+".sy",keyable=False,lock=True)
	setAttr(lockScaleObj+".sz",keyable=False,lock=True)

def lockVis(lockScaleObj):
	setAttr(lockScaleObj+".visibility",keyable=False,lock=True)

def lockRadius(lockScaleObj):
	setAttr(lockScaleObj+".radius",keyable=False,channelBox=False )

def addObjColor(objName,colorIndex):
	setAttr(objName+".overrideEnabled",1)
	setAttr(objName+".overrideColor",colorIndex)










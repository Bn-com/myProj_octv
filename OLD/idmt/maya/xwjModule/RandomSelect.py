import maya.cmds as mc
import random
global SLSsets
SLSsets=[]
def selectSetWindow():
    if (mc.window("selectSetWindow", ex = 1 ) ) : mc.deleteUI("selectSetWindow", window = 1)
    if(mc.windowPref("selectSetWindow", ex = 1) ) : mc.windowPref("selectSetWindow", remove = 1)

    mc.window ( "selectSetWindow",
				title = "Random Select",
				width = 360,
				height = 280,
				menuBar = 1,
				rtf = 0
			)

    base = mc.formLayout(numberOfDivisions = 100)

    baseObj = mc.textFieldButtonGrp(label = 'Objects: ',
                                      cw3 = (90,200,50),
                                      buttonLabel = '<<<')

    mc.textFieldButtonGrp(baseObj,  e=1,
                                      buttonCommand = "fillTextField('"+baseObj+"')")

    mc.formLayout(base,
                  e=1,
                  attachForm = [(baseObj,"left",5),(baseObj,"top",5)])
    subdivisions = mc.intSliderGrp(
				label = "Subdivisions:",
				field=True,
				cw3 = (80,40, 200),
				fmn=1,
				min =1,
                max =10,
                v = 3
			)

    mc.formLayout (base,
				e = 1,
				attachForm  = [(subdivisions,"left", 5),(subdivisions, "top", 50)]
			)

    setList = mc.textScrollList(
				numberOfRows=8,
                allowMultiSelection=True,
                width = 150,
		        height = 150

			)

    mc.formLayout (base,
				e = 1,
				attachForm  = [(setList,"left", 5),(setList, "top", 100)]
			)
    ButtonRandom = mc.button  (
		label = "Random",

		command = "getSet('"+  baseObj+"','"+ subdivisions + "','"+ setList+"')",

		width = 150,
		height = 40,
		bgc = [255,241,67],
		)

    mc.formLayout(base,
			e = 1,
 		   attachForm  = [(ButtonRandom, "left", 180),(ButtonRandom, "top", 120)]
	   )

    ButtonSelect = mc.button  (
		label = "Select",

		command = "selectSet('"+ setList+"')",

		width = 150,
		height = 40,
		bgc = [255,241,67],
		)

    mc.formLayout(base,
			e = 1,
 		   attachForm  = [(ButtonSelect, "left", 180),(ButtonSelect, "top", 200)]
	   )

    mc.showWindow("selectSetWindow")

def fillTextField(buttonc) :
    listObj = mc.ls(sl = 1)

    listObjConcat =""
    for i, obj in enumerate(listObj) :
        if (i == (len(listObj) - 1)) :
			listObjConcat += obj
        else :
            listObjConcat += obj + " "

    if len(listObj) == 0 :
        return
    mc.textFieldButtonGrp(buttonc, e = 1, text = listObjConcat )

def getSet(baseObj,subdivisions,setList):
    global SLSsets
    SLSsets=[]
    base = mc.textFieldButtonGrp(baseObj, q=1, text= 1)
    subdivisions = mc.intSliderGrp(subdivisions, q=1, value = 1)
    mc.textScrollList( setList,e=1,ra=1)
    baseList=base.split()
    for j in range(subdivisions):
        mc.textScrollList( setList,e=1,append=['Set0'+str(j+1)] ,selectItem='Set01', showIndexedItem=1)
        SLSsets.append([])
    for obj in baseList:
        print obj
        index=random.randint(0,subdivisions-1)
        SLSsets[index].append(obj)
    if (len(base) == 0):
        return

	return SLSsets

def selectSet(setList):
    indexs = mc.textScrollList(setList, q=1, sii=1)
    mc.select(cl=1)
    for index in indexs:
        mc.select(SLSsets[index-1],add=1)
selectSetWindow()

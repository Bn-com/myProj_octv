# -*- coding: utf-8 -*-

import maya.cmds as mc
import os.path
import os
import fnmatch
import pickle
import string
from struct import pack
import struct

# ------------------------------------
# ------------------------------------
#	Builds python script to
#	assign the MDDs in Modo
# ------------------------------------
# ------------------------------------
def outputAssignmentScript(directory, outputMDDS) :
	script = []
	script.append('#python')
	script.append(' ')
	script.append('import lx')
	script.append('import string')
	script.append('import os.path')
	script.append('from struct import pack')
	script.append('import sys')
	script.append(' ')
	script.append('def momoMapLayers():')
	script.append('    layers = lx.eval("query layerservice layers ? all")')
	script.append('    layerMapping = {}')
	script.append('    if ( layers == 1 ) :')
	script.append('        cmd = ( "query layerservice layer.name ? " + str(layers) )')
	script.append('        name = lx.eval(cmd)')
	script.append('        layerMapping[name] = layers')
	script.append('    else :')
	script.append('        for layer in layers :')
	script.append('            cmd = ( "query layerservice layer.name ? " + str(layer) )')
	script.append('            name = lx.eval(cmd)')
	script.append('            layerMapping[name] = layer')
	script.append('    return layerMapping')
	script.append(' ')
	script.append('def applyMDD(mdds, layers):')
	script.append('    for layer in layers.keys() :')
	script.append('        if mdds.has_key(layer) :')
	script.append('            mdd = mdds[layer]')
	script.append('            layerNum = layers[layer]')
	script.append('            lx.eval("select.layer " + str(layerNum) + " set")')
	script.append('            cmd = ("deform.mddAdd \\"" + os.path.abspath(mdd) + "\\"")')
	script.append('            lx.eval(cmd)')
	script.append(' ')
	script.append('mdds = {}')
	
	for obj in outputMDDS.keys():	    
		NamNw=newObjNma(str(obj))
		outFile = outputMDDS[str(obj)]
		outFile = string.replace(outFile, '\\', '/')
		script.append('mdds[\'' + str(NamNw)+ '\'] = \'' + outFile + '\''  )
	
	script.append('applyMDD(mdds, momoMapLayers())')

	pyScript = os.path.abspath( directory + '/mddApply.py' )
	f = open(pyScript, 'w')
	for line in script :
		f.write(line + '\n')
	f.close()

# ------------------------------------
# ------------------------------------
#	Get the framerate and
#	return as a float
# ------------------------------------
# ------------------------------------
def util_getFPS() :
	fpsString = mc.currentUnit( q=True, time=True )
	fps = -1
	
	if fpsString == "ntsc" :
   		fps = 30.0
	if fpsString == "film" :
   		fps = 24.0
	if fpsString == "game" :
   		fps = 15.0
	if fpsString == "pal" :
   		fps = 25.0
	if fpsString == "show" :
   		fps = 48.0
	if fpsString == "palf" :
   		fps = 50.0
	if fpsString == "ntscf" :
   		fps = 60.0
	return fps

# ------------------------------------
# ------------------------------------
#	Turn the pickle files
#	into valid '.mdd' files
# ------------------------------------
# ------------------------------------
def compileMDD( data, directory ):
	framerate = util_getFPS()
	startFrame = 0
	endFrame = 0
	
	outputMDDS = {}

	for obj in data.keys() :
		vertCount = 0
		objData = data[obj]
		
		for info in objData.keys():
			frange = objData['range']
			startFrame = frange[0]
			endFrame = frange[1]
			vertCount = objData['vCount']
			fileList = objData['fileList']
		
		deformation = {}
		for frameFile in fileList:
			frame = os.path.basename(frameFile)
			frame = string.split(frame, ".")
			frame = int(frame[1])
			
			if not deformation.has_key(frame):
				deformation[frame] = {}
			
			f = open(frameFile, 'r')
			frameData = pickle.load(f)
			f.close()

			for vert in range(0,vertCount):
				deformation[frame][vert] = {}
				deformation[frame][vert] = frameData[vert]

		animLength = ( ( endFrame - startFrame ) + 1 )
		mdd = os.path.abspath(( directory + "/" + obj + ".mdd" ))
		
		outputMDDS[obj] = mdd
		
		f = open(mdd, 'wb')
		f.seek(0)
		f.write(pack('>L', animLength))
		f.write(pack('>L', vertCount))
		
		x = 1.0

		while x <= animLength :
			n = ( x / framerate )
			f.write(pack('>f', n))
			x = ( x + 1 )
		
		for vert in range(0, vertCount) :
			position = deformation[startFrame][vert]
			f.write(pack('>f', position[0]))
			f.write(pack('>f', position[1]))
			f.write(pack('>f', position[2]))

		for frame in range(startFrame, (endFrame+1)) :
			for vert in range(0, vertCount) :
				position = deformation[frame][vert]
				f.write(pack('>f', position[0]))
				f.write(pack('>f', position[1]))
				f.write(pack('>f', position[2]))

		f.close()
		for frameFile in fileList:
			os.remove(os.path.abspath(frameFile))
			
	outputAssignmentScript(directory, outputMDDS)

# ------------------------------------
# ------------------------------------
#	Export out pickle files
#	1 per object per frame
#	allows low mem computers to
#	export complex scenes
# ------------------------------------
# ------------------------------------
def exportIntermediateFiles(objs, startFrame, endFrame, outDir):
	if not os.path.exists(outDir):
		os.mkdir(outDir)
	
	tempDir = outDir + '\mmtmp'
	
	if not os.path.exists(tempDir):
		os.mkdir(tempDir)
		
	massdata = {}
		
	for frame in range(startFrame, (endFrame+1)):
		for obj in objs:
			vertCount = 0
			fileList = []
			if massdata.has_key(obj) :
				vertCount = massdata[obj]['vCount']
				fileList = massdata[obj]['fileList']
			else :
				vertCount = mc.polyEvaluate(obj, v=True)	
			
			mc.currentTime(frame)
			mc.dgdirty(a=True)
		
			outFile = os.path.abspath(( tempDir + "/" + obj + "." + str(frame) + ".mmFrame" ))
			fileList.append(outFile)
			
			print '------------------------'
			print outFile
			print '------------------------'
		
			f = open(outFile, 'wb')
			data = {}
			for vert in range( 0, vertCount ):
				vertName = ( obj + ".vtx[" + str(vert) + "]" )
				pos = mc.xform(vertName, q=True, worldSpace=True, translation=True)
				x = pos[0]
				y = pos[1]
				z = ( pos[2] * (-1) )
				pos = x,y,z
				if not data.has_key(vert):
					data[vert] = pos

			pickle.dump(data,f)
			f.close()
			
			raw = {}
			raw['vCount'] = vertCount
			raw["range"] = (startFrame, endFrame)
			raw['fileList'] = fileList
			massdata[obj] = raw
	return massdata

# ------------------------------------
# ------------------------------------
#	A simple trick to remove
#	duplicate entries from a
#	string array
# ------------------------------------
# ------------------------------------
def removeListDuplicates( rawList ):
	u = {}
	try:
		for x in rawList:
			u[x] = 1
	except TypeError:
		del u  # move on to the next method
	else:
		return u.keys()
		
# ------------------------------------
# ------------------------------------
#	Get a list of all the
#	cameras in the scene, ignores
#	the default cameras
# ------------------------------------
# ------------------------------------
def mdd_FindCameras() :
	camShapes = mc.ls( type = 'camera' )
	cams = []

	for shape in camShapes :
		if shape != 'topShape':
			if shape != 'frontShape':
				if shape != 'sideShape':
					if shape != 'perspShape':
						raw = mc.listRelatives( shape, p=1, type = 'transform' )
						cams.append(raw[0])
	cams = sorted(cams)
	cams.append('  -----  No Camera Export  -----  ')
	return cams

# ------------------------------------
# ------------------------------------
#	Get a list of all the
#	mdd Groups in
#	scene
# ------------------------------------
# ------------------------------------
def mdd_GetGroups() :
	groups = []
	raw = mc.ls(type = 'mesh')
	
	if raw :
		for mesh in raw :
			lr = mc.listRelatives( mesh, p=1, type = 'transform' )
			if lr :
				for r in lr :
					if mc.attributeQuery('mddGroup', node = r, exists=1):
						group = mc.getAttr(( r + '.mddGroup' ))
						groups.append(group)
	
	groups = removeListDuplicates(sorted(groups))
	return groups

# ------------------------------------
# ------------------------------------
#	Find all polyMesh transforms
#	in the scene without a group
#	tag.
# ------------------------------------
# ------------------------------------
def mdd_FindUntaggedGeometry( group ) :
	untaggedList = []
	raw = mc.ls(type = 'mesh')
	
	if raw :
		for mesh in raw :
			lr = mc.listRelatives( mesh, p=1, type = 'transform' )
			if lr :
				for r in lr :
					if not mc.attributeQuery('mddGroup', node = r, exists=1):
						untaggedList.append(r)
	
	untaggedList = removeListDuplicates(sorted(untaggedList))
	return untaggedList

# ------------------------------------
# ------------------------------------
#	Find all polyMesh transforms
#	in the scene with a group
#	tag.
# ------------------------------------
# ------------------------------------
def mdd_FindTaggedGeometry( group ) :
	taggedList = []
	raw = mc.ls(type = 'mesh')
	
	if raw :
		for mesh in raw :
			lr = mc.listRelatives( mesh, p=1, type = 'transform' )
			if lr :
				for r in lr :
					if mc.attributeQuery('mddGroup', node = r, exists=1):
						if mc.getAttr(( r + '.mddGroup' )) == group:
							taggedList.append(r)
	
	taggedList = removeListDuplicates(sorted(taggedList))
	return taggedList

# ------------------------------------
# ------------------------------------
#	Add group tag 'group' to
#	object 'obj'
# ------------------------------------
# ------------------------------------
def mdd_TagGeometry( obj, group ) :
	mc.addAttr( obj, ln='mddGroup', dt='string' )
	mc.setAttr( ( obj + '.mddGroup' ), group, type = 'string' )
	mc.setAttr( ( obj + '.mddGroup' ), lock = 1 )

# ------------------------------------
# ------------------------------------
#	Remove group tag 'group'
#	from object 'obj'
# ------------------------------------
# ------------------------------------
def mdd_UntagGeometry( obj, group ) :
	mc.setAttr( ( obj + '.mddGroup' ), lock = 0 )
	mc.deleteAttr( obj + '.mddGroup' )

# ------------------------------------
# ------------------------------------
#	UI Update Callback
# ------------------------------------
# ------------------------------------
def mdd_TagGeometryCB( gtsl, utsl, ttsl ) :
	raw = mc.textScrollList(gtsl, q=1, selectItem=1 ) 
	group = raw[0]
	raw = mc.textScrollList(utsl, q=1, selectItem=1 )

	for geo in raw :
		mdd_TagGeometry( geo, group )
		mc.textScrollList( utsl, e=1, removeItem = geo )
		mc.textScrollList( ttsl, e=1, append = geo )

# ------------------------------------
# ------------------------------------
#	UI Update Callback
# ------------------------------------
# ------------------------------------
def mdd_UntagGeometryCB( gtsl, utsl, ttsl ) :
	raw = mc.textScrollList(gtsl,  q=1, selectItem=1 ) 
	group = raw[0]
	raw = mc.textScrollList(ttsl,  q=1, selectItem=1 )

	for geo in raw :
		mdd_UntagGeometry( geo, group )
		mc.textScrollList( ttsl, e=1, removeItem = geo )
		mc.textScrollList( utsl, e=1, append = geo )


# ------------------------------------
# ------------------------------------
#	UI Callback Creating
#	a new Tag Group
# ------------------------------------
# ------------------------------------
def mdd_CreateGroupCB( tslist ) :
	name = ''
	result = mc.promptDialog( title = 'Create mdd Group', message='Enter Group Name :', button= ['Create' , 'Cancel'], defaultButton = 'Create', cancelButton = 'Cancel', dismissString = 'Cancel' )
	
	if result == 'Create' :
		name = mc.promptDialog(q=1, text=1)
		mc.textScrollList( tslist, e=1, append=name )		

# ------------------------------------
# ------------------------------------
#	Deletes a group from the Tagger
# ------------------------------------
# ------------------------------------
def mdd_DeleteGroupCB( tsl, ttsl ) :
	raw = mc.textScrollList( tsl, q = 1, selectItem = 1 )
	group = raw[0]

	c = mc.confirmDialog( title='Confirm', message = 'Are you sure?', button = [ 'Totally','Whoops!'], defaultButton = 'Totally', cancelButton = 'Whoops!', dismissString= 'Whoops!' )
	if c == "Totally" :
		ig = mdd_FindTaggedGeometry(group)
		mc.textScrollList(tsl, e=1, removeItem = group )
		mc.textScrollList( ttsl , e=1, removeAll=1 )
		for each in ig :
			mdd_UntagGeometry(each, group)

def mdd_HighlightGroup( gtsl, utsl, ttsl ) :
	raw = mc.textScrollList( gtsl, q=1, selectItem=1 )
	group =	raw[0]
	ugeo = mdd_FindUntaggedGeometry( group )
	tgeo = mdd_FindTaggedGeometry( group )

	mc.textScrollList( utsl, e=1, removeAll = 1 )
	mc.textScrollList( ttsl, e=1, removeAll = 1 )

	if ugeo:
		for geo in ugeo :
			mc.textScrollList( utsl, e=1, append=geo )

	if tgeo:
		print tgeo
		for geo in tgeo :
			mc.textScrollList( ttsl, e=1, append=geo )

# ------------------------------------
# ------------------------------------
#	Change the export directory
# ------------------------------------
# ------------------------------------
def mdd_ChangeExportDirCB( tf ) :
	selected = mc.fileDialog( mode= 1 )
	if selected :
		directory = os.path.abspath(os.path.dirname(selected))
		mc.text(tf, e=1, label=directory, ann=selected )

# ------------------------------------
# ------------------------------------
#	Builds the command from the
#	Export UI and executes
# ------------------------------------
# ------------------------------------
def mdd_ExportCB(form, frange, camMenu, outDirText ) :
	raw = mc.formLayout( form, q=1, childArray=1)
	groups = []

	for check in raw :
		check = ( form + '|' + check )
		
		if mc.checkBox( check, q = 1, v = 1 ) :
			groups.append(mc.checkBox( check, q=1, l=1 ))

	sf = mc.intFieldGrp(frange, q = 1, v1 = 1 ) 
	ef = mc.intFieldGrp(frange, q = 1, v2 = 1 )
	cam = mc.optionMenu( camMenu, q = 1, v = 1 )
	selCam = mc.optionMenu( camMenu, q = 1, select = 1 )
	camCount = mc.optionMenu( camMenu, q = 1, numberOfItems = 1 )
	outdir = os.path.abspath(mc.text( outDirText, q = 1,  label = 1 ))
	exportCam = ''
	
	if selCam != camCount :
		exportCam = cam

	if outdir :
		mdd(groups, sf, ef, outdir, 1 )

# ------------------------------------
# ------------------------------------
#	Build the Tagger Window
# ------------------------------------
# ------------------------------------
def mdd_Tagger() :
	existingGroups = mdd_GetGroups()
	
	windowName = 'mdd_Tagging_Window'
	windowWidth = 800
	windowHeight = 650

	if mc.window(windowName, exists = 1):
		mc.deleteUI(windowName)

	window = mc.window(windowName,w=windowWidth, h=windowHeight,  t='mdd Tagger')
	masterForm = mc.formLayout(parent=window)
	groupsForm = mc.formLayout(parent=masterForm)
	possibleForm = mc.formLayout(parent=masterForm)
	inForm = mc.formLayout(parent=masterForm)
	attrForm = mc.formLayout(parent=masterForm)
	
	margin = 3

	#-------------------------------------
	#
	#	Group Management
	#
	# ------------------------------------
	
	groupsTSL = mc.textScrollList( allowMultiSelection = 0, parent = groupsForm )
	addGroup = mc.button( label= 'Add Group', parent = groupsForm )
	delGroup = mc.button( label = 'Delete Group', parent = groupsForm )
	groupsLabel = mc.text( label = 'mdd Groups', font = 'boldLabelFont', align = 'center', parent = groupsForm )
	mc.formLayout( groupsForm, edit = 1, attachForm = [( delGroup , 'left' , margin ), ( delGroup , 'bottom' , margin ), ( delGroup , 'right' , margin ), ( addGroup , 'left' , margin ), ( addGroup , 'right' , margin ), ( groupsLabel , 'top' , margin ), ( groupsLabel , 'left' , margin ), ( groupsLabel , 'right' , margin ), ( groupsTSL , 'left' , margin ), ( groupsTSL , 'right' , margin )], attachNone = [( addGroup, 'top' ), ( groupsLabel, 'bottom' ), ( delGroup, 'top' )], attachControl = [( addGroup , 'bottom' , margin , delGroup ), ( groupsTSL , 'top' , margin , groupsLabel ), (groupsTSL , 'bottom' , margin , addGroup )] )
	
	untaggedTSL = mc.textScrollList( allowMultiSelection = 1, parent = possibleForm )
	tag = mc.button( label = 'Tag Selected', parent = possibleForm )
	untaggedLabel = mc.text( label= 'Untagged Geometry', font = 'boldLabelFont', align = 'center', parent = possibleForm )
	mc.formLayout(possibleForm, edit = 1, attachNone = [ ( tag, 'top' ), ( untaggedLabel, 'bottom' ) ],attachForm = [( tag , 'left' , margin ),( tag , 'bottom' , margin ),( tag , 'right' , margin ),( untaggedLabel , 'top' , margin ),( untaggedLabel , 'left' , margin ),( untaggedLabel , 'right' , margin ),( untaggedTSL , 'left' , margin ),( untaggedTSL , 'right' , margin )],attachControl = [( untaggedTSL, 'top', margin, untaggedLabel ),( untaggedTSL, 'bottom', margin, tag ) ] )
	
	taggedTSL = mc.textScrollList( allowMultiSelection = 1,  parent = inForm )
	untag = mc.button( label = 'Untag Selected' , parent = inForm )
	taggedLabel = mc.text( label = 'Tagged Geometry', font= 'boldLabelFont', align = 'center', parent = inForm )

	mc.formLayout( inForm, edit = 1, attachNone = [ ( untag, 'top' ), ( taggedLabel, 'bottom' ) ], attachForm = [( untag, 'left', margin ), ( untag, 'bottom', margin ), ( untag, 'right', margin ), ( taggedLabel, 'top', margin ), ( taggedLabel, 'left', margin ), ( taggedLabel, 'right', margin ), ( taggedTSL, 'left', margin ), ( taggedTSL, 'right', margin ) ], attachControl = [( taggedTSL, 'top', margin, taggedLabel ),( taggedTSL, 'bottom', margin, untag )] )

	#-------------------------------------
	#
	#	add commands to controls
	#
	# ------------------------------------

	mc.button( addGroup, e = 1,  c =  ( 'mdd.mdd_CreateGroupCB( \'' + groupsTSL + '\')') )
	mc.textScrollList( groupsTSL, e=1,  selectCommand = ( 'mdd.mdd_HighlightGroup(\''+ groupsTSL + '\', \'' + untaggedTSL + '\', \'' + taggedTSL	+ '\')' ) )

	mc.textScrollList( untaggedTSL, e=1, doubleClickCommand = ( 'mdd.mdd_TagGeometryCB(\'' + groupsTSL + '\', \'' + untaggedTSL + '\', \'' + taggedTSL + '\')' ) )
	mc.textScrollList( taggedTSL, e=1, doubleClickCommand=( 'mdd.mdd_UntagGeometryCB(\'' + groupsTSL + '\', \'' + untaggedTSL + '\', \'' + taggedTSL + '\')' ) )

	mc.button( tag, e=1, c = ( 'mdd.mdd_TagGeometryCB(\'' + groupsTSL + '\', \'' + untaggedTSL + '\', \'' + taggedTSL + '\')' ) )
	mc.button( untag, e=1, c = ( 'mdd.mdd_UntagGeometryCB(\'' + groupsTSL + '\', \'' + untaggedTSL + '\', \'' + taggedTSL + '\')' ) )

	mc.button( delGroup, e=1, c = ('mdd.mdd_DeleteGroupCB(\'' + groupsTSL+ '\', \'' + taggedTSL + '\')') )

	for group in existingGroups :
		mc.textScrollList( groupsTSL, e=1, append = group ) 

	mc.formLayout(masterForm, edit=1, attachForm =[ ( groupsForm, 'top', margin ), ( groupsForm, 'left', margin ), ( groupsForm, 'bottom', margin ), ( possibleForm, 'top', margin ), ( possibleForm, 'bottom', margin ), ( inForm, 'top', margin ), ( inForm, 'bottom', margin ), ( inForm, 'right', margin )], attachPosition= [ ( groupsForm, 'right', margin, 33 ), ( possibleForm, 'right', margin, 66 ) ], attachControl =[ ( possibleForm, 'left', margin, groupsForm ), ( inForm, 'left', margin, possibleForm )] )

	mc.showWindow(window)
	

# ------------------------------------
# ------------------------------------
#	Build the Group Exporter UI
# ------------------------------------
# ------------------------------------
def mdd_Exporter() :
	groups = mdd_GetGroups()

	windowName = 'mdd_Export_Window'
	windowWidth = 500
	windowHeight = 350

	if mc.window( windowName, exists=1 ) :
		mc.deleteUI(windowName)

	window = mc.window( w=windowWidth, h=windowHeight, t= 'mdd Exporter' )

	masterForm = mc.formLayout(parent=window)

	margin = 6

	groupListFL = mc.frameLayout( label = 'Select Groups to Export', labelAlign = 'top', borderStyle = 'etchedIn', li = 10, parent = masterForm )
	gaForm = mc.formLayout( parent = groupListFL )

	gChecks = []

	for group in groups :
		gChecks.append(mc.checkBox( v=1, l = group, annotation = group, parent = gaForm ) )

	aff = []
	anf = []
	acf = []
	
	for i in range(0, len(groups)):
		if i == 0:
			aff.append( ( gChecks[i] , 'top' , ( margin * 1.5 ) ) )
		else:
			acf.append( ( gChecks[i], 'top', ( margin * 1.5 ), gChecks[(i-1)] ) )
		aff.append( ( gChecks[i], 'left' , margin ) )
		anf.append( ( gChecks[i], 'bottom' ) )
		anf.append( ( gChecks[i], 'right' ) )	
	
	mc.formLayout( gaForm, edit = 1, attachForm = aff, attachNone=anf, attachControl=acf )

	cameraFL = mc.frameLayout( label = 'Select Camera to Export', labelAlign = 'top', borderStyle = 'etchedIn', li = 10, parent = masterForm )
	camForm = mc.formLayout( parent = cameraFL )

	cams = mdd_FindCameras()

	camMenu = mc.optionMenu( label='', enable = 0, parent = camForm )

	for cam in cams :
		mc.menuItem( label = cam, parent = camMenu)

	mc.formLayout( camForm, edit = 1, attachForm = [( camMenu, 'top', margin ),( camMenu, 'bottom', margin ),( camMenu, 'right', margin )], attachNone = [( camMenu, 'left' )] )

	frangeSettingsFL = mc.frameLayout( label = ' Frame Range Settings ', labelAlign = 'top', borderStyle = 'etchedIn', li = 10, parent = masterForm )
	frangeForm = mc.formLayout( parent = frangeSettingsFL )

	sf = mc.playbackOptions( q = 1, min = 1 )
	ef = mc.playbackOptions( q = 1, max = 1 )

	frange = mc.intFieldGrp( numberOfFields = 2, label = 'Start / End',  value1 = sf,  value2 = ef,  parent = frangeForm )

	mc.formLayout( frangeForm, edit = 1, attachForm = [( frange, 'top', margin ), ( frange, 'bottom', margin ), ( frange, 'right', margin )], attachNone = [( frange, 'left' )] )
	outputFL = mc.frameLayout( label = 'Output Path', labelAlign = 'top', borderStyle = 'etchedIn', li = 10, parent = masterForm )
	outputForm = mc.formLayout( parent = outputFL )

	ws = mc.workspace(q=True, act=True)
	path = mc.workspace(ws, q=True, lfw=True)
	path = os.path.abspath(path[0] + '/data')
	
	outputDirLabel = mc.text( label = path, align = 'center', parent = outputForm )
	outDirButton = mc.button( label = 'Change Directory', parent = outputForm )

	mc.button( outDirButton, e=1, c = ('mdd.mdd_ChangeExportDirCB(\'' + outputDirLabel + '\')' ))

	mc.formLayout( outputForm, edit = 1, attachForm = [ ( outputDirLabel, 'top', margin ), ( outputDirLabel, 'left', margin ), ( outputDirLabel, 'right', margin ), ( outDirButton, 'left', ( margin * 15 ) ), ( outDirButton, 'right', ( margin * 15 ) ) ], attachControl = [ ( outDirButton, 'top', ( margin + 10 ), outputDirLabel ) ], attachNone = [ ( outputDirLabel, 'bottom' ), ( outDirButton, 'bottom' ) ] )

	exportButton = mc.button( label = 'Export', parent = masterForm )

	mc.formLayout( masterForm, edit = 1, attachNone =[( cameraFL, 'top' ), ( frangeSettingsFL, 'bottom' ), ( outputFL, 'bottom' )], attachPosition=[( cameraFL, 'right', margin, 40 ), ( groupListFL, 'right', margin, 40 ), ( exportButton, 'top', margin, 80 )], attachForm=[( cameraFL, 'left', margin ), ( cameraFL, 'bottom', margin ), ( groupListFL, 'top', margin ), ( groupListFL, 'left', margin ), ( exportButton, 'bottom', margin ), ( exportButton, 'right', margin ), ( frangeSettingsFL, 'top', margin ), ( frangeSettingsFL, 'right', margin ), ( outputFL, 'right', margin )], attachControl = [ ( groupListFL, 'bottom', margin, cameraFL  ), ( exportButton, 'left', margin, groupListFL ), ( frangeSettingsFL, 'left', margin, groupListFL ), ( outputFL, 'top', margin, frangeSettingsFL ), ( outputFL, 'left', margin, groupListFL )] )

	mc.button( exportButton, e = 1,  c = ('mdd.mdd_ExportCB(\'' + gaForm + '\', \'' + frange + '\', \'' + camMenu + '\', \'' + outputDirLabel + '\')' ) )
	
	mc.showWindow(window)
	
# ------------------------------------
# ------------------------------------
#	Main Function - you can use
#	this directly via scripting
# ------------------------------------
# ------------------------------------
def mdd( groups, sf, ef, outDir, mode=0 ) :
	outDir = ( outDir + '/' )
	
	geo = []

	for group in groups :
		for item in mdd_FindTaggedGeometry(group) :
			geo.append(item)

	mc.waitCursor( state=True )
	compileMDD(exportIntermediateFiles(geo, sf, ef, outDir), outDir)
	mc.waitCursor( state=False )
	
	if mode:
		mc.confirmDialog( title = 'Export Complete', message = ( 'Completed Export to ' + os.path.abspath(outDir) ), button = 'OK', defaultButton = 'OK' )

# ------------------------------------
# ------------------------------------
#	Quick Export of Selected Geo
# ------------------------------------
# ------------------------------------
def mddQuickExport() :
	from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
	reload(sk_infoConfig)
	
	shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

	meshes = []	
	sf = int(mc.playbackOptions( q = 1, min = 1 ))
	ef = int(mc.playbackOptions( q = 1, max = 1 ))
	
	selected=mc.ls(sl=1)
	if selected:
		for each in selected :
			if mc.listRelatives(each, ad=1, ni=1, type='mesh',f=1) :
				meshes.append(each)
	else:
		mc.confirmDialog(title=u'警告', message=u'请选择ToRig组下需要做mdd cache的物体', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
	
	directory = ('\\\\file-cluster\\GDC\\Projects\\North\\Project\\data\\MDDCache\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
	mc.sysFile(directory, makeDir=True)
	mc.waitCursor( state=True )
	compileMDD(exportIntermediateFiles(meshes, sf, ef, directory), directory)
	mc.waitCursor( state=False )


# ------------------------------------
# ------------------------------------
#	get object info
# ------------------------------------
# ------------------------------------
def newObjNma(obj):
    if ':' in obj:
        flePreFix=os.path.basename(mc.referenceQuery(obj, f = True)).split('.')[0].replace('_mst','_tex')
        getObjNam=(obj.split(':')[1].split('_',2)[2]+'Shape (')+flePreFix+')'
        return getObjNam





	
	
	
	
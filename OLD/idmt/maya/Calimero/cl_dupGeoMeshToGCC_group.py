
import maya.cmds as mc
import re

def cl_dupGeoMeshToGCC_group ():
	
	start_Frame = (mc.playbackOptions(q=True,min=True)) -1
	if (mc.currentTime(q=True)!= start_Frame):
	  mc.currentTime(start_Frame)
	selectMeshes = mc.ls(sl=1,l=1)
	#print selectMeshes
	chrDic={}

	for i in range(len(selectMeshes)):
	  #i=0
	  temp = selectMeshes[i].rsplit("|")
	  groupName = temp[1]
	  p = re.compile("[^0-9]+[0-9]+[a-z]+[^A-Z]*")
	  chrName = p.findall(groupName)
	  
	  #shapeLists = mc.listRelatives(selectMeshes[i],c=1,ni=1,s=1,f=1)
	  mc.select(selectMeshes[i],r=1)
	  mc.duplicate(selectMeshes[i],st=1)
	  dupMeshListe = mc.ls(sl=1,l=1)
	  
	  #================add particle set gole target=====================
	  softParticle = mc.soft(dupMeshListe[0],c=1)
	  attrName = softParticle[0]+".startFrame"
	  mc.setAttr(attrName,start_Frame)	
	  mc.goal(w=1,utr = 0,g = selectMeshes[i])
		
	  meshList = [dupMeshListe[0]]
	  if (chrDic.has_key(chrName[0])):
		chrDic[chrName[0]].extend(meshList)
	  else:
		chrDic.setdefault(chrName[0],meshList)

	chrLis = chrDic.keys()
	geoCacheChaGroups = []
	for eaChr in chrLis:
	  geoCacheChaGroups.extend([mc.group(chrDic[eaChr],w=1,n=("GEO_CACHE_CHA_" + eaChr))])

	return geoCacheChaGroups

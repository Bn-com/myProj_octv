import sys
import os
import re
import shutil
import string
import maya.cmds as cmds
import maya.mel as mel
import unicodedata
import math
import zipfile

displayPrints = False


def getTransformByShape(shape):
    try:
        if cmds.nodeType(shape) == "transform":
            return shape
        else:
            parents = cmds.listRelatives(shape, fullPath=False, parent=True)
            return parents[0]
    except:
        return False


def getShapes(xform):
    shapes = [""]
    shapes[0] = xform
    if(cmds.nodeType(xform) == "transform"):
        shapes = cmds.listRelatives(xform, fullPath=True, type="shape")
    return shapes

##################################################################################################
# CHECK TOOLBOX
##################################################################################################


class check_toolbox_gdc():
    scenePathName = ""

    def __init__(self, projName):
        print "check_toolbox init"
        self.checkStartTimerX = cmds.timerX()

        self.val = []
        self.valNodes = []
        self.errorsInfos = {}

        self.objRoot = None
        self.refRoot = None
        self.allNodes = None
        self.allNodesInfos = None
        self.fileNodeInfos = None
        self.defaultCams = ["persp", "front", "side", "top", "CAMERA:CAMERA"]
        self.defaultMaterials = ["lambert1", "particleCloud1"]
        self.animCurvesT = ["animCurveTA", "animCurveTL", "animCurveTU"]
        self.checkReportWindow = "checkPublishabilityReport"
        self.correctsGeoGroups = ["GEO", "SKINNED_GEO", "DEFORMABLE_GEO", "DEFORMED_GEO", "geo"]

        defs = dir(self)
        checks = []
        for d in defs:
            if "check_" in d:
                checks.append(len(d))
        self.defsMaxLenght = max(checks)

        self.__defineStep()

    def __defineStep(self):
        # determination du type de model ( char, props, sets )
        self.scenePathName = cmds.file(loc=True, q=True)
        if("_mo_" in self.scenePathName or "_mo." in self.scenePathName):
            self.lisaStep = "MODELING"
            self.stepShort = "_mo_"
        elif("_rg_" in self.scenePathName or "_rg." in self.scenePathName):
            self.lisaStep = "RIGGING"
            self.stepShort = "_rg_"
        elif("_px_" in self.scenePathName):
            self.lisaStep = "PROXY"
            self.stepShort = "_px_"
        elif("_tx_rgb_" in self.scenePathName or "_tx." in self.scenePathName):
            self.lisaStep = "SHADING"
            self.stepShort = "_tx_rgb_"
        elif "_render_" in self.scenePathName or "_render." in self.scenePathName:
            self.lisaStep = "SHADING"
            self.stepShort = "_render_"
        else:
            self.lisaStep = ""
            self.stepShort = ""

    def checkReport(self, error_type, message, nodes=[]):
        if displayPrints:
            print "\t", message
        self.val.append([error_type, message])
        self.valNodes.append(nodes)

        type = "warning" if error_type == "warning" else "ERROR"
        if type not in self.errorsInfos:
            self.errorsInfos[type] = {}
        self.errorsInfos[type][message] = nodes

    def checkReportTimerX(self):
        print "check elapsed time :", cmds.timerX(startTime=self.checkStartTimerX)

    def checkNodeNameByHierarchicalLevel(self, name, level):
        ok = False
        currentLevel = None
        ls = cmds.ls(name, l=1)
        if ls and len(ls) == 1:
            if "|" in ls[0]:
                currentLevel = ls[0].count("|")
                if currentLevel == level+1:
                    ok = True

        return ok, ls, currentLevel

    def check_valid_nodes(self, error_type, nonValidTypes):
        if displayPrints:
            print "* check_valid_nodes".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : Control all the existing node in the scene, not permitted : "+", ".join(nonValidTypes)
        message = "ok"
        nodes = cmds.ls()

        for node in nodes:
            if cmds.referenceQuery(node, inr=1) == False and node.find("default") == -1 and node.find("Default") == -1 and node.find("initial") == -1:
                type = cmds.objectType(node)
                if type in nonValidTypes:
                    if node != "sceneConfigurationScriptNode" and node != "uiConfigurationScriptNode" and node != "vectorRenderGlobals":
                        message = "The node : "+node+" with type "+type+" should not be in the scene"
                        self.checkReport(error_type, message)

    def check_mesh_nomencl(self, error_type):
        if displayPrints:
            print "* check_mesh_nomencl : all mesh transform must start by 'msh_'."
        meshs = cmds.ls(type="mesh", sn=True)
        for mesh in meshs:
            transform = getTransformByShape(mesh)
            if not transform.startswith("msh_"):
                message = "mesh " + transform + " doesn't start with 'msh_'"
                self.checkReport(error_type, message)

    def check_group_nomencl(self, error_type):
        if displayPrints:
            print "* check_group_nomencl : group transform must not start by 'msh_'."
        print 'DEBUG : error type : ' + error_type
        transforms = cmds.ls(type="transform", sn=True)
        for transform in transforms:
            shapes = getShapes(transform)
            if not shapes and transform.lower().startswith("msh_"):
                message = "group " + transform + " start with 'msh_'"
                self.checkReport(error_type, message)

            #CALIMERO specific
            if "VALID" in transform:
                message = "group " + transform + " contain 'VALID'"
                self.checkReport(error_type, message)

    def check_main_group_position(self, error_type):
        if displayPrints:
            print "* check_main_group_position"

        objs = cmds.ls(['|*', 'WORLD'])
        objs = [x for x in objs if x not in self.defaultCams]
        if objs:
            for obj in objs:
                if self.stepShort == "_tx_rgb_" and obj == "CAM":
                    continue
                transl = cmds.getAttr(obj+".t")
                if transl != [(0.0, 0.0, 0.0)]:
                    self.val.append([error_type, "object " + obj + " should have a translate value of 0,0,0"])
                rotate = cmds.getAttr(obj+".r")
                if rotate != [(0.0, 0.0, 0.0)]:
                    self.val.append([error_type, "object " + obj + " should have a rotate value of 0,0,0"])
                scale = cmds.getAttr(obj+".s")
                if scale != [(1.0, 1.0, 1.0)]:
                    self.val.append([error_type, "object " + obj + " should have a scale value of 1,1,1"])

    def check_occurences(self, error_type):
        if displayPrints:
            print "* check_occurences"
        names = cmds.ls(["c_*", 'msh_*'])
        shortNames = []
        for name in names:
            if name.count("|"):
                shortNames.append(name.split('|')[-1])
            else:
                shortNames.append(name)

        multipleOccurences = set([])
        for name in shortNames:
            if shortNames.count(name) > 1:
                multipleOccurences.add(name)

        if multipleOccurences:
            message = "objects with same name found : " + ", ".join(multipleOccurences)
            self.checkReport(error_type, message)

    def check_clean_topology(self, error_type):
        if displayPrints:
            print "* check_clean_topology".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : Control all meshs for a correct topology : nsided, holed, zeroAreaFace , zeroLengthEdge, nonMannifold, lamina"
        meshs = cmds.ls(type="mesh", l=1)

        isCharacter = False
        if "/characters/" in self.scenePathName.replace("\\", '/').lower():
            isCharacter = True

        toChecks = []
        noVtx = []

        if meshs:
            for m in meshs:
                vtx = cmds.polyEvaluate(m, v=1)
                if vtx != 0:
                    if m not in toChecks:
                        toChecks.append(m)
                else:
                    if m not in noVtx:
                        noVtx.append(m)
        if noVtx:
            for nv in noVtx:
                message = "mesh with no vertex: " + nv
                self.checkReport(error_type, message, nodes=noVtx)

        if toChecks:
            cmds.select(toChecks, r=1)
            errors = mel.eval('polyCleanupArgList 3 { "0","2","1","0","1","0","1","0","1","1e-005","1","1e-005","0","1e-005","0","1","1" }')
            if errors:
                for it in errors:
                    message = "mesh with incorrect topology: " + it
                    if isCharacter:
                        self.checkReport("warning", message, nodes=noVtx)
                    else:
                        self.checkReport(error_type, message, nodes=errors)

    def check_texture_path(self, error_type, inScene=1, inRef=0):
        if displayPrints:
            print "* check_texture_path".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : the textures path must be on the source images folder correspondant of the object"

        dirName = os.path.dirname(cmds.file(loc=True, q=True))

        sourceOK = dirName.lower().replace("/scenes", "/sourceimages").replace("/texture", "").replace("/master", "")

        filesNodeInfos = {}
        files = cmds.ls(type="file")
        for f in files:
            if cmds.attributeQuery("fileTextureName", node=f, exists=True):
                path = cmds.getAttr(f+".fileTextureName").lower().replace('${idmt_projects}', '//file-cluster/GDC/Projects')
                if path:
                    if filesNodeInfos.has_key(path):
                        filesNodeInfos[path].append(f)
                    else:
                        filesNodeInfos[path] = [f]
        if len(filesNodeInfos):
            for path in filesNodeInfos:
                pathOK = unicodedata.normalize("NFKD", path).encode("ascii", "ignore")

                message = None
                if path.find(" ") != -1 or pathOK != path or path.find(":") != -1:
                    message = path + " contain a white space, or illegal(s) character(s), or is in local"
                else:
                    #pathTest = path.replace(path.split("/")[2],self.project.SERVER_NAME)
                    pathTest = path.replace("\\", "/")
                    filePath = pathTest.replace(os.path.basename(path), "")

                    if "sourceimages/" not in filePath.lower():  # texture dans le mauvais dossier
                        message = "Wrong directory : texture " + path + " should be in " + sourceOK
                    if not os.path.isfile(path):  # le fichier texture n'existe pas
                        message = path + " doesn't exists"

                if message:
                    self.checkReport(error_type, message, nodes=filesNodeInfos[path])
                    print "\t\ton node(s)", ", ".join(filesNodeInfos[path])

    def check_texture_format(self, error_type, maFolder=""):
        if displayPrints:
            print "* check_texture_format".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : the texture must be a tga."

        correctTypesByMode = {"_mo_": ["png", "tga"], "_rg_": ["png", "tga"], "_px_": ["tga", "png"], "_tx_rgb_": ["tga"], "_render_": ["map", "png", "tga"]}

        step = self.stepShort

        fileNodes = cmds.ls(type="file")
        if fileNodes and len(fileNodes):
            for fileNode in fileNodes:
                filePathName = cmds.getAttr(fileNode + ".fileTextureName")
                if filePathName:
                    filePathNameL = filePathName.lower()
                    if step in correctTypesByMode:
                        ext = filePathNameL.split(".")[-1]
                        if not ext in correctTypesByMode[step]:
                            message = "texture " + filePathName + " must be a "+",".join(correctTypesByMode[step])+" file"
                            self.checkReport(error_type, message, nodes=fileNode)
                            #print "\t\ton node(s)",", ".join(fileNode)
                        if step == "_render_":
                            message = ""
                            for checkExt in correctTypesByMode[step]:
                                # if checkExt == "zip" and maFolder != "":
                                #     checkPath = filePathName.replace("." + ext, '.' + checkExt)
                                #     checkPath = maFolder.replace('scenes/', 'sourceimages/') + os.path.basename(checkPath)
                                #     if not os.path.isfile(checkPath):
                                #         message += checkPath + ", "
                                if checkExt != "map":
                                    checkPath = filePathName.replace("." + ext, '.' + checkExt).replace('${IDMT_PROJECTS}', '//file-cluster/GDC/Projects').replace('${idmt_projects}', '//file-cluster/GDC/Projects')
                                    if not os.path.isfile(checkPath):
                                        message += checkPath + ", "
                            if message:
                                self.checkReport(error_type, message + "is missing.", nodes=fileNode)

    def check_valid_names(self, error_type, forbidden=[" "]):
        if displayPrints:
            print "* check_valid_names".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : check the nodes name: no space and no illegal characters(accents)"
        errors = []

        allNodes = cmds.ls()
        refs = cmds.ls(type="reference")

        for t in allNodes:
            if not refs:
                forbidden.append(":")

            for f in forbidden:
                if f in t:
                    errors.append(t)
                    break
            OK = unicodedata.normalize("NFKD", t).encode("ascii", "ignore")
            if OK != t:
                errors.append(t)

        if len(errors):
            message = 'Some nodes have illegal(s) chararcter(s) : "' + '", "'.join(errors) + '"'
            self.checkReport(error_type, message, nodes=errors)
            if displayPrints:
                print "(\" \",\":\" for non references objects or accentued and special characters)"

    def check_smoothSet_integrity(self, error_type):
        if displayPrints:
            print "* check_smoothSet_integrity".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : check that an object is not assigned to multiple smooth sets"

        smoothSets = cmds.ls("smooth*", "Smooth*", type="objectSet")

        if smoothSets and len(smoothSets) > 1:
            i = 0
            for i in range(len(smoothSets)-1):
                cmds.select(smoothSets[i], hierarchy=True)
                membersI = cmds.ls(sl=True, l=True)
                for j in range(i+1, len(smoothSets)):
                    cmds.select(smoothSets[j], hierarchy=True)
                    members = cmds.ls(sl=True, l=True)
                    for memberI in membersI:
                        if memberI in members:
                            message = memberI + " is in several smoothSets"
                            self.checkReport(error_type, message)

        elif not smoothSets:
            message = "No smooth set found"
            self.checkReport(error_type, message)

        cmds.select(cl=True)

    def check_mesh_in_smooth_set(self, error_type):
        if displayPrints:
            print "* check_mesh_in_smooth_set \t : all msh_ has to be in a smooth set."
        meshSet = set(cmds.ls('msh_*', type='transform'))
        try:
            smoothSetMeshSet = set(cmds.sets("smooth*", q=True))
            for mesh in (meshSet - smoothSetMeshSet):
                message = mesh + " is not in a smooth set"
                self.checkReport(error_type, message)
        except:
            pass

    def check_null_transforms(self, error_type):
        if displayPrints:
            print "* check_null_transforms".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : Control that there is no transforms without his shape"
        animable = ["c_", "a_", "pose_", "p_", "WORLD"]
        attributesStd = ["visibility", "translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ", "scaleX", "scaleY", "scaleZ"]
        transforms = cmds.ls(exactType="transform", l=1)

        isCharacter = False
        if "CHR_" in self.scenePathName:
            isCharacter = True

        for tr in transforms:
            childs = cmds.listRelatives(tr, ad=1)
            if childs == None:
                okNode = 0
                for ani in animable:
                    if ani in tr:
                        okNode = 1
                        break

                if okNode == 0:
                    okAttr = 0
                    attrs = cmds.listAttr(tr, k=1)
                    if attrs:
                        for attr in attrs:
                            if attr not in attributesStd:
                                okAttr = 1
                                break
                    if okAttr == 0 and not isCharacter:
                        message = tr+" is a transform with no shape and have no special attribute"
                        self.checkReport(error_type, message, nodes=tr)
                    elif not isCharacter:
                        message = tr+" is a transform with no shape but have special(s) attribute(s) and is not a controller"
                        self.checkReport(error_type, message, nodes=tr)

    def check_shapes_history(self, error_type, permitedTypes=["transform", "displayLayer", "shadingEngine", "groupId", "mesh", "mentalraySubdivApprox"]):
        if displayPrints:
            print "* check_shapes_history".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : control the history of shapes"

        nbMeshConcerned = 0
        allShapes = cmds.ls(exactType="subdiv", ni=True, r=True, l=True)+cmds.ls(exactType="mesh", ni=True, r=True, l=True)+cmds.ls(exactType="nurbsSurface", ni=True, r=True, l=True)
        allShapes = [x for x in allShapes if "eyeball" not in x and "iris" not in x and "pulpil" not in x and "cornea" not in x]
        allErrorShapes = []
        if allShapes and len(allShapes):
            for shp in allShapes:
                history = []
                errors = []
                his = cmds.listHistory(shp, ag=1, future=0)
                for h in his:
                    type = cmds.objectType(h)
                    if type not in permitedTypes:
                        errors.append(h)

                if len(errors):
                    nbMeshConcerned += 1
                    allErrorShapes.append(shp)
                    print "\t", cmds.ls(shp)[0], "have contruction history :", ", ".join(errors)

        if nbMeshConcerned:
            message = str(nbMeshConcerned) + " objects have contruction history."
            self.checkReport(error_type, message, nodes=allErrorShapes)

    def check_anim_default_cams(self, error_type):
        if displayPrints:
            print "* check_anim_default_cams".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : The default camera should not have animation"

        self.defaultCams += ["cam_GUI", "cam_facePanel", "CAMERA:CAMERA"]

        attrs = ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ", "scaleX", "scaleY", "scaleZ"]

        cams = [cmds.pickWalk(x, direction="up")[0] for x in cmds.ls(cameras=True)]

        for cam in cams:
            if self.stepShort == "_tx_rgb_" and cam == "CAM":
                continue
            message = "ok"
            ok = 0
            for defCam in self.defaultCams:
                if defCam in defCam:
                    ok = 1
                    break
            if not ok:
                message = cam+" must not be in the scene"
                self.checkReport(error_type, message, nodes=cam)
            elif ok and cam != "CAMERA:CAMERA":
                for attr in attrs:
                    conns = cmds.listConnections(cam+"."+attr)
                    if conns and len(conns):
                        message = cam+"."+attr+" has animation"
                        self.checkReport(error_type, message, nodes=cam)

    def check_shaders_nomenclature(self, error_type):
        if displayPrints:
            print "* check_shaders_nomenclature".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : shaders must be called \"shd_\""

        errors = []
        materials = [x for x in cmds.ls(mat=True) if x not in self.defaultMaterials]
        for material in materials:
            if ":" not in material:
                if not material.lower().startswith("shd_"):
                    errors.append(material)

        if len(errors):
            msg = "Some shader(s) should starts with \"shd_\" : " + ", ".join(errors)
            self.checkReport(error_type, msg)

    def check_lambert1_unassigned(self, error_type):
        if displayPrints:
            print "* check_lambert1_unassigned".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : Control that the default lambert1 is not assigned"

        assigments = cmds.sets("initialShadingGroup", q=1)
        if assigments and len(assigments):
            ni = cmds.ls(assigments, ni=1, ut=1, v=1)
            if ni and len(ni):
                message = "lambert1 assigned to : " + ",".join(ni)
                self.checkReport(error_type, message, nodes=ni)

    def check_assignment_by_face(self, error_type):
        if displayPrints:
            print "* check_assignment_by_face".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : face assigment is forbidden"

        errors = {}
        SES = cmds.ls(type="shadingEngine")
        for SE in SES:
            assigments = cmds.sets(SE, q=1)
            if assigments:
                for assigment in assigments:
                    if ".f[" in assigment:
                        aS = assigment.split(".")
                        if SE not in errors:
                            errors[SE] = [aS[0]]
                        elif aS[0] not in errors[SE]:
                            errors[SE].append(aS[0])

        if len(errors):
            for e in errors:
                message = e+" is assigned to faces of "+",".join(errors[e])
                self.checkReport(error_type, message, nodes=e)

    def check_negative_scale(self, error_type):
        transforms = cmds.ls(type="transform")
        meshHierarchies = cmds.ls(type='mesh', l=True)
        meshGroupList = []
        for meshHierarchy in meshHierarchies:
            groups = meshHierarchy.split("|")
            for group in groups[1:len(groups)-1]:
                meshGroupList.append(group)
        negativeScaleNodes = []
        for transform in set(transforms) & set(meshGroupList):
            if cmds.attributeQuery("s", node=transform, ex=True):
                scale = cmds.getAttr(transform + ".s")
                if scale and (scale[0][0] < 0 or scale[0][1] < 0 or scale[0][2] < 0):
                    negativeScaleNodes.append(transform)
        if negativeScaleNodes:
            message = "Negative scale found on : " + ", ".join(negativeScaleNodes)
            self.checkReport(error_type, message)

    def check_nodes_nomencl(self, error_type, modelName):
        # on recupere le nom de l'objet dans la base de donnees via la classe lisa_getter (elle meme heritiere de TT_lisa_basics)
        if modelName:
            nomModele = modelName
            nomModele = nomModele.upper()
            if displayPrints:
                print "* CHECK for model : '" + nomModele + "'"
                print "* check_nodes_nomenclature".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : control if root node name is the same as in Lisa"
            ok, ls, level = self.checkNodeNameByHierarchicalLevel(modelName.upper(), 0)
            if not ok:
                message = None
                if not ls:
                    message = nomModele + " root node not found"
                else:
                    message = "wrong root node name : " + ",".join(ls)

                if message:
                    self.checkReport(error_type, message)
        else:
            message = "can't check the nodes nomenclature (local scene or no LISA connection)."
            self.checkReport(error_type, message)

    def check_ctrl_value(self, error_type):
        """
        test si les controleur sont bien a l'identite (0 ou 1)
        """
        if displayPrints:
            print "* check_ctrl_value".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : check if the controleurs have the transform to identity (0 for translate ant rotate and 1 for scale)"
        ctrls = cmds.ls("c_*", et="transform", l=1, r=1)
        axis = ["X", "Y", "Z"]
        zeroAttrs3 = ["translate", "rotate"]
        oneAttrs3 = ["scale"]
        errors = {}

        if ctrls:
            for c in ctrls:
                for a in zeroAttrs3:
                    label = []
                    values = []
                    er = False
                    for axe in axis:
                        v = cmds.getAttr(c+"."+a+axe)
                        locked = cmds.getAttr(c + "." + a + axe, lock=True)
                        if math.fabs(round(v, 3)) != 0.0 and locked != True and cmds.listConnections(c + "." + a + axe) == None:
                            label.append(a + axe)
                            values.append(str(v))
                            er = True
                    if er == True:
                        if c not in errors:
                            errors[c] = {}
                        if a not in errors[c]:
                            errors[c][",".join(label)] = ",".join(values)

                for a in oneAttrs3:
                    label = []
                    values = []
                    er = False
                    for axe in axis:
                        v = cmds.getAttr(c+"."+a+axe)
                        locked = cmds.getAttr(c+"."+a+axe, lock=True)
                        if math.fabs(round(v, 3)) != 1.0 and locked != True and cmds.listConnections(c+"."+a+axe) == None:
                            label.append(a+axe)
                            values.append(str(v))
                            er = True
                    if er == True:
                        if c not in errors:
                            errors[c] = {}
                        if a not in errors[c]:
                            errors[c][",".join(label)] = ",".join(values)
            if errors:
                for n in errors.keys():
                    message = cmds.ls(n)[0]+" should have identity transform, found : "
                    for a in errors[n].keys():
                        message += a + ": " + errors[n][a] + "; "
                    self.checkReport(error_type, message[:-2], nodes=n)

    def check_ctrl_setup(self, error_type):
        """
        test si le controleur sont bien sur des transforms
        """
        if displayPrints:
            print "* check_ctrl_setup".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : the nodes starting by \"c_\" must be transform nodes"
        ctrls = cmds.ls("c_*")
        if ctrls:
            for ctrl in ctrls:
                # on test si c'est un transform
                if not cmds.objectType(ctrl, isType='transform') and not cmds.objectType(ctrl, isType='file') and not cmds.objectType(ctrl, isType='nurbsCurve') and not cmds.objectType(ctrl, isType='aimConstraint') and not cmds.objectType(ctrl, isType='joint') and not cmds.objectType(ctrl, isType='animCurveUU') and not cmds.objectType(ctrl, isType='animCurveUL') and not cmds.objectType(ctrl, isType='softModHandle'):
                    message = ctrl + " type is not a transform but a " + cmds.objectType(ctrl)
                    self.checkReport(error_type, message, nodes=ctrl)

    def check_visibility(self, error_type):
        if displayPrints:
            print "* check_visibility".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : All objects must be visible"

        isCharacter = False
        if "CHR_" in self.scenePathName:
            isCharacter = True

        if "_stp_" in self.scenePathName:
            transfs = cmds.ls(type="mesh", sn=True)  # self.returnTypedNodesByNS("mesh",None)
        else:
            transfs = cmds.ls(type="transform", sn=True)  # self.returnTypedNodesByNS("transform",None)
            transfs = [x for x in transfs if x.replace("|", "") not in self.defaultCams]

        if transfs:
            for transf in transfs:
                if cmds.attributeQuery("visibility", node=transf, ex=True):
                    vis = cmds.getAttr(transf + ".visibility")
                if not vis and not isCharacter:
                    message = transf + " should not be hidden"
                    self.checkReport(error_type, message, nodes=transf)

                if "_stp_" in self.scenePathName:
                    parent = cmds.listRelatives(transf, parent=True, type="transform", path=True)
                    if parent:
                        parent = parent[0]
                        if cmds.attributeQuery("visibility", node=parent, ex=True):
                            vis = cmds.getAttr(parent + ".visibility")
                        if not vis and not isCharacter:
                            message = transf + " should not be hidden"
                            self.checkReport(error_type, message, nodes=transf)

    def check_hierarchy(self, error_type, modelName):
        if modelName:
            nomModele = modelName
            nomModele = nomModele.lower()

            worlds = cmds.ls("WORLD", long=True)

            for world in worlds:
                if not world.split('|')[-2].lower() == nomModele:
                    message = "wrong WORLD group parent :" + world
                    self.checkReport(error_type, message)

            geos = cmds.ls("GEO", long=True)

            for geo in geos:
                if not geo.split('|')[-2] == 'WORLD':
                    message = "wrong GEO group parent :" + geo
                    self.checkReport(error_type, message)

            deformed_geos = cmds.ls("DEFORMED_GEO", long=True)

            for deformed_geo in deformed_geos:
                if not deformed_geo.split('|')[-2].lower() == nomModele:
                    message = "wrong DEFORMED_GEO group parent :" + deformed_geo
                    self.checkReport(error_type, message)

            if len(geos) + len(deformed_geos) == 0:
                message = "GEO group is not existing."
                self.checkReport(error_type, message)

            if len(geos) > 1:
                message = "GEO group is not unique."
                self.checkReport(error_type, message)

            if len(deformed_geos) > 1:
                message = "DEFORMED_GEO group is not unique."
                self.checkReport(error_type, message)

            if len(worlds) != 1:
                message = "WORLD group is not unique or not existing."
                self.checkReport(error_type, message)
        else:
            message = "can't check the hierarchy (local scene or no LISA connection)."
            self.checkReport(error_type, message)

    def check_TTvisibility(self, modelType, error_type):
        if displayPrints:
            print "* check_TTvisibility".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : TTvisibility attribute on every controller except c_BIL and c_LGT or if it's a character model"
        if modelType and modelType != 'CHARACTERS':
            allCtrls = cmds.ls("c_*", et="transform", r=1)
            for ctrl in allCtrls:
                if cmds.attributeQuery("vis", node=ctrl, ex=True):
                    msg = ctrl + " has .vis attribute."
                    self.checkReport(error_type, msg, nodes=ctrl)
                if not cmds.attributeQuery("tt_visibility", node=ctrl, ex=True) and not 'c_BIL' in ctrl and not 'c_LGT' in ctrl:
                    msg = ctrl + " doesn't have .tt_visibility attribute."
                    self.checkReport(error_type, msg, nodes=ctrl)

    def check_limits_and_lock(self, error_type):
        if displayPrints:
            print "* check_limits_and_lock".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : Check limits and lock on all trasnforms"
        transforms = cmds.ls(typ='transform')
        limitedTransforms = []
        for transform in transforms:
            etx = cmds.transformLimits(transform, q=True, etx=True)
            ety = cmds.transformLimits(transform, q=True, ety=True)
            etz = cmds.transformLimits(transform, q=True, etz=True)
            erx = cmds.transformLimits(transform, q=True, erx=True)
            ery = cmds.transformLimits(transform, q=True, ery=True)
            erz = cmds.transformLimits(transform, q=True, erz=True)
            esx = cmds.transformLimits(transform, q=True, esx=True)
            esy = cmds.transformLimits(transform, q=True, esy=True)
            esz = cmds.transformLimits(transform, q=True, esz=True)

            limits = etx + ety + etz + erx + ery + erz + esx + esy + esz

            if True in limits:
                limitedTransforms.append(transform)

        if limitedTransforms:
            msg = ', '.join(limitedTransforms) + " have limits."
            self.checkReport(error_type, msg, nodes=limitedTransforms)

    def check_calimero_shading(self, scenePathName, modelType, error_type):
        if displayPrints:
            print "* check_calimero_shading".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : Differents controls for Camilero shading"

        # No PINK color (1,0,1) set or connected in writeToColorBuffer nodes
        colorIDs = cmds.ls('*ColorID*', typ='writeToColorBuffer')

        for colorID in colorIDs:
            colorR = cmds.getAttr(colorID + '.colorR')
            colorG = cmds.getAttr(colorID + '.colorG')
            colorB = cmds.getAttr(colorID + '.colorB')
            if colorR == 1.0 and colorG == 0.0 and colorB == 1.0:
                message = colorID + " shouldn't be pink."
                self.checkReport(error_type, message, nodes=colorID)

        # writeToColorBuffer named colorID3 set to BLUE (0, 0, 1) and connected to <name>_LIGHT shaders if the shader name contains 'window' and 'glass'
        colorIDs = cmds.ls('*ColorID3*', typ='writeToColorBuffer')

        for colorID in colorIDs:
            if colorID.count('glass') or colorID.count('Glass'):
                colorR = cmds.getAttr(colorID + '.colorR')
                colorG = cmds.getAttr(colorID + '.colorG')
                colorB = cmds.getAttr(colorID + '.colorB')
                if not (colorR == 0.0 and colorG == 0.0 and colorB == 1.0):
                    message = colorID + " have to be blue."
                    self.checkReport(error_type, message, nodes=colorID)

                if not cmds.objExists('SHD_' + colorID.split('_ColorID3')[0] + '_LIGHT') or not cmds.isConnected('SHD_' + colorID.split('_ColorID3')[0] + '_LIGHT.outColor', colorID + '.evaluationPassThrough'):
                    message = 'SHD_' + colorID.split('_ColorID3')[0] + '_LIGHT.outColor have to be connected to ' + colorID + '.evaluationPassThrough.'
                    self.checkReport(error_type, message, nodes=colorID)

        # If a shader is suffixed <name>_RGBA two corresponding shaders suffixed <name>_LIGHT and <name>_ZDEPTH have to exist
        rgbaShaders = cmds.ls('SHD*RGBA')

        for rgbaShader in rgbaShaders:
            if not cmds.objExists(rgbaShader.replace('_RGBA', '_LIGHT')):
                message = rgbaShader.replace('_RGBA', '_LIGHT') + ' have to exist.'
                self.checkReport(error_type, message, nodes=rgbaShader)
            if not cmds.objExists(rgbaShader.replace('_RGBA', '_ZDEPTH')):
                message = rgbaShader.replace('_RGBA', '_ZDEPTH') + ' have to exist.'
                self.checkReport(error_type, message, nodes=rgbaShader)

        # A miLabel attribute have to exist for every meshes prefixed msh_BIL_* and have to be set to 1
        bilboards = []
        for ctrl in cmds.ls("c_BIL_*", type='transform'):
            for child in cmds.listRelatives(ctrl, ad=True, f=True):
                if cmds.nodeType(child) == 'mesh':
                    bilboards.append(cmds.listRelatives(child, p=True)[0])

        bilboards += cmds.ls('msh_BIL*', typ='transform')

        message = ''
        for bilboard in bilboards:
            miLabelCheck = False
            if cmds.attributeQuery('miLabel', node=bilboard, ex=True):
                if cmds.getAttr(bilboard + '.miLabel') == 1:
                    miLabelCheck = True

            if not miLabelCheck:
                message = "miLabel attribute doesn't exists for some bilboards."

        if message:
            self.checkReport(error_type, message, nodes=bilboard)

        # All AO_BIL* indexcl is set to 5 and all AO except AO_BIL* indexcl is set to -1
        for aoTex in cmds.ls(type='mib_amb_occlusion'):
            if 'AO' in aoTex:
                if 'BIL' in aoTex:
                    if cmds.getAttr(aoTex+'.id_inclexcl') != -5:
                        message = "id_inclexcl attribute have to be -5 for " + aoTex + "."
                        self.checkReport(error_type, message, nodes=aoTex)
                else:
                    if cmds.getAttr(aoTex+'.id_inclexcl') != -1:
                        message = "id_inclexcl attribute have to be -1 for " + aoTex + "."
                        self.checkReport(error_type, message, nodes=aoTex)

        ###
        # For characters:
        # - For every <name>_RGB (ou RGBA) shader, two corresponding writeToColorBuffer nodes <name>_ColorID and <name>_ColorID_CHR have to exist
        # - writeToColorBuffer colorID have to be RED (1, 0, 0)
        #
        # For props:
        #- For every <name>_RGB (ou RGBA), a corresponding writeToColorBuffer nodes <name>_ColorID have to exist
        #- writeToColorBuffer colorID have to be BLUE (0, 0, 1)
        #
        #For sets:
        #- For every <name>_RGB (ou RGBA), a corresponding writeToColorBuffer nodes <name>_ColorID have to exist
        ###

        shaders = cmds.ls('SHD*RGBA') + cmds.ls('SHD*RGB')
        for shader in shaders:
            message = ''
            colorIDExists = True
            colorID = shader.replace('_RGBA', '_ColorID').replace('_RGB', '_ColorID').replace('SHD_', '')
            if not cmds.objExists(colorID):
                message += colorID + ' have to exist.\n'
                colorIDExists = False

            if modelType == "CHARACTERS":
                if not cmds.objExists(shader.replace('_RGBA', '_ColorID_CHR').replace('_RGB', '_ColorID_CHR').replace('SHD_', '')):
                    message += shader.replace('_RGBA', '_ColorID_CHR').replace('_RGB', '_ColorID_CHR').replace('SHD_', '') + ' have to exist.\n'

                if 'Glass' in colorID or 'glass' in colorID:
                    colorID = shader.replace('_RGBA', '_ID_ColorIDA').replace('_RGB', '_ID_ColorIDA')
                if not cmds.objExists(colorID):
                    message += colorID + ' have to exist.\n'
                    colorIDExists = False

                if colorIDExists:
                    colorAttr = '.color'
                    if 'Glass' in colorID or 'glass' in colorID:
                        colorAttr = '.outColor'
                    colorR = cmds.getAttr(colorID + colorAttr + 'R')
                    colorG = cmds.getAttr(colorID + colorAttr + 'G')
                    colorB = cmds.getAttr(colorID + colorAttr + 'B')
                    if not (colorR == 1.0 and colorG == 0.0 and colorB == 0.0):
                        message += colorID + ' have to be red.\n'

            elif modelType == "PROPS":
                if 'prp_' in scenePathName or 'veh_' in scenePathName:
                    if colorIDExists:
                        colorR = cmds.getAttr(colorID + '.colorR')
                        colorG = cmds.getAttr(colorID + '.colorG')
                        colorB = cmds.getAttr(colorID + '.colorB')
                        if colorR == 0.0 and colorG == 1.0 and colorB == 0.0:
                            connectedEngines = cmds.listConnections(shader, s=False, t='shadingEngine')
                            if connectedEngines:
                                se = connectedEngines[0]
                                meshes = cmds.listConnections(se, d=False, t='mesh')
                                if meshes == None:
                                    meshes = []
                                for mesh in meshes:
                                    parents = cmds.listRelatives(mesh, p=True, f=True)
                                    if parents.lower().count('vegetation') or parents.lower().count('planter'):
                                        break
                                else:
                                    message += colorID + ' have to be blue.\n'
                        elif not (colorR == 0.0 and colorG == 0.0 and colorB == 1.0):
                            message += colorID + ' have to be blue.\n'
                elif 'col_' in scenePathName and not (colorR == 0.0 and colorG == 0.0 and colorB == 0.0):
                    message += colorID + ' have to be black.\n'

            if message:
                self.checkReport(error_type, message, nodes=shader)

    def check_calimero_lighting(self, modelName, error_type):
        if displayPrints:
            print "* check_calimero_lighting".ljust(self.defsMaxLenght)+" ("+error_type.center(9)+") : Check hierarchy and position for lighting"

        for light in cmds.ls(typ='light', l=True):
            if not light.startswith('|' + modelName.upper() + '|WORLD|LIGHTING|'):
                msg = light + " is outside of the group |" + modelName.upper() + "|WORLD|LIGHTING|."
                self.checkReport(error_type, msg, nodes=light)

        for light in [light for light in cmds.ls(typ='light') if not 'LGT_PREVIEW_ONLY' in light]:
            if not (light.startswith('LGT_') and ('BOUNCE' in light or 'KEY' in light or 'EXTRA' in light)):
                msg = light + " need to be named correctly."
                self.checkReport(error_type, msg, nodes=light)

        grp = cmds.ls('LIGHTING', typ='transform', l=True)
        if grp:
            grp = grp[0]

            if grp != '|' + modelName.upper() + '|WORLD|LIGHTING':
                msg = grp + " should be under |" + modelName.upper() + "|WORLD."
                self.checkReport(error_type, msg, nodes=grp)

            msg = []
            transl = cmds.getAttr(grp+".t")
            if transl != [(0.0, 0.0, 0.0)]:
                msg.append([error_type, "object " + grp + " should have a translate value of 0,0,0"])
            rotate = cmds.getAttr(grp+".r")
            if rotate != [(0.0, 0.0, 0.0)]:
                msg.append([error_type, "object " + grp + " should have a rotate value of 0,0,0"])
            scale = cmds.getAttr(grp+".s")
            if scale != [(1.0, 1.0, 1.0)]:
                msg.append([error_type, "object " + grp + " should have a scale value of 1,1,1"])

            if msg:
                msg = '\n'.join(msg)
                self.checkReport(error_type, msg, nodes=grp)

##################################################################################################
# END CHECK TOOLBOX
##################################################################################################


def cal_check_modeling_gdc(modelName, modelType, local):
    print "CAL CHECK MODELING"

    test = check_toolbox_gdc("CALIMERO")
    e, w = "error", "warning"

    # Errors
    test.check_nodes_nomencl(e, modelName)
    test.check_hierarchy(e, modelName)
    test.check_ctrl_value(e)
    test.check_main_group_position(e)
    test.check_occurences(e)
    test.check_valid_names(e)
    test.check_smoothSet_integrity(e)
    test.check_mesh_in_smooth_set(e)
    test.check_negative_scale(e)
    # TODO : test.check_ligth_names(e)
    test.check_mesh_nomencl(e)
    test.check_group_nomencl(e)
    test.check_TTvisibility(modelType, e)
    test.check_calimero_lighting(modelName, e)
    test.check_limits_and_lock(e)

    if local:
        test.check_valid_nodes(e, ['unknown', 'lookAt', 'audio', 'nucleus', 'MelodyGlobals', 'VersionTracker', 'reference', 'ilrOptionsNode', 'ilrUIOptionsNode', 'ilrBakeLayerManager', 'ilrBakeLayer'])
        test.check_valid_nodes(w, ['renderLayer'])
        test.check_texture_path(w)
        test.check_texture_format(w)
    else:
        test.check_valid_nodes(e, ['unknown', 'lookAt', 'audio', 'renderLayer', 'nucleus', 'MelodyGlobals', 'VersionTracker', 'reference', 'ilrOptionsNode', 'ilrUIOptionsNode', 'ilrBakeLayerManager', 'ilrBakeLayer'])
        test.check_texture_path(e)
        test.check_texture_format(e)

    if modelType == "CHARACTERS":
        test.check_clean_topology(w)
    else:
        test.check_clean_topology(e)

    # Warnings
    test.check_null_transforms(w)
    test.check_shapes_history(w)
    test.check_valid_nodes(w, ["light", "animCurveTA", "animCurveTL", "animCurveTU"])
    test.check_anim_default_cams(w)
    test.check_shaders_nomenclature(w)
    test.check_lambert1_unassigned(w)
    test.check_assignment_by_face(w)

    test.checkReportTimerX()

    return test.val


def cal_check_setup_gdc(modelName, modelType, local):
    print "CAL CHECK SETUP"

    test = check_toolbox_gdc("CALIMERO")
    e, w = "error", "warning"

    # Errors
    test.check_nodes_nomencl(e, modelName)
    test.check_hierarchy(e, modelName)
    test.check_main_group_position(e)
    test.check_ctrl_value(e)
    test.check_valid_names(e)
    test.check_ctrl_setup(e)
    test.check_occurences(e)
    test.check_smoothSet_integrity(e)
    test.check_mesh_in_smooth_set(e)
    test.check_anim_default_cams(e)
    #test.check_node_presence(e, ["light","audio","renderLayer"])
    test.check_negative_scale(e)
    test.check_clean_topology(e)

    # TODO : test.check_ligth_names(e)
    test.check_mesh_nomencl(e)
    test.check_group_nomencl(e)
    test.check_TTvisibility(modelType, e)
    test.check_calimero_lighting(modelName, e)

    if local:
        test.check_texture_path(w)
        test.check_valid_nodes(e, ['unknown', 'lookAt', 'audio', 'MelodyGlobals', 'VersionTracker', 'reference', 'ilrOptionsNode', 'ilrUIOptionsNode', 'ilrBakeLayerManager', 'ilrBakeLayer'])
        test.check_valid_nodes(w, ['renderLayer'])
        test.check_texture_format(w)
    else:
        test.check_texture_path(e)
        test.check_valid_nodes(e, ['unknown', 'lookAt', 'audio', 'MelodyGlobals', 'renderLayer', 'VersionTracker', 'reference', 'ilrOptionsNode', 'ilrUIOptionsNode', 'ilrBakeLayerManager', 'ilrBakeLayer'])
        test.check_texture_format(e)

    # Warnings
    test.check_visibility(w)
    #test.check_shapes_history(w)
    test.check_null_transforms(w)
    test.check_shaders_nomenclature(w)
    test.check_assignment_by_face(w)
    test.check_lambert1_unassigned(w)

    test.checkReportTimerX()

    return test.val


def cal_check_shading_gdc(scenePathName, modelName, modelType, maFolder, local, txStep=False):
    print "CAL CHECK SHADING"

    test = check_toolbox_gdc("CALIMERO")
    e, w = "error", "warning"

    # Errors
    test.check_nodes_nomencl(e, modelName)
    test.check_hierarchy(e, modelName)
    test.check_main_group_position(e)
    test.check_ctrl_value(e)
    test.check_valid_names(e)
    test.check_ctrl_setup(e)
    test.check_occurences(e)
    test.check_smoothSet_integrity(e)
    test.check_mesh_in_smooth_set(e)
    test.check_anim_default_cams(e)
    test.check_negative_scale(e)
    test.check_clean_topology(e)
    # TODO : test.check_ligth_names(e)
    test.check_mesh_nomencl(e)
    test.check_assignment_by_face(e)
    test.check_shaders_nomenclature(e)
    test.check_lambert1_unassigned(e)
    test.check_calimero_shading(scenePathName, modelType, e)
    test.check_TTvisibility(modelType, e)

    if local:
        test.check_valid_nodes(e, ['unknown', 'lookAt', 'audio', 'nucleus', 'MelodyGlobals', 'VersionTracker', 'reference', 'ilrOptionsNode', 'ilrUIOptionsNode', 'ilrBakeLayerManager', 'ilrBakeLayer'])
        test.check_valid_nodes(w, ['renderLayer'])
        test.check_texture_path(w)
        test.check_texture_format(w)
        test.check_group_nomencl(w)
    elif txStep:
        test.check_valid_nodes(e, ['unknown', 'lookAt', 'audio', 'nucleus', 'MelodyGlobals', 'VersionTracker', 'reference', 'ilrOptionsNode', 'ilrUIOptionsNode', 'ilrBakeLayerManager', 'ilrBakeLayer'])
        test.check_valid_nodes(w, ['renderLayer'])
        test.check_texture_path(e)
        test.check_texture_format(e)
        test.check_group_nomencl(w)
    else:
        test.check_calimero_lighting(modelName, e)
        test.check_valid_names(e, forbidden=["VALID"])
        test.check_valid_nodes(e, ['unknown', 'lookAt', 'audio', 'renderLayer', 'nucleus', 'MelodyGlobals', 'VersionTracker', 'reference', 'ilrOptionsNode', 'ilrUIOptionsNode', 'ilrBakeLayerManager', 'ilrBakeLayer'])
        test.check_texture_path(e)
        test.check_texture_format(e, maFolder)
        test.check_group_nomencl(e)

    # Warnings
    test.check_visibility(w)
    test.check_shapes_history(w)
    test.check_valid_nodes(w, ["reference", "animCurveTA", "animCurveTL", "animCurveTU"])
    test.check_null_transforms(w)

    test.checkReportTimerX()

    return test.val


class cal_scene_checker_gdc():
    def __init__(self, modelName, publish=False, override=False, local=False):

        if publish and local:
            print "Error : if you want to publish, you need to set local to False"
            return

        self.scenePathName = cmds.file(loc=True, q=True)
        self.modelName = modelName
        self.publish = publish
        self.override = override
        self.val = []

        f = open('Z:/Projects/Calimero/Common_Sync/CAL_MAYA/2013/python/teamto/hierarchy.txt', 'r')
        self.projectFolder = "Z:/Projects/Calimero/Common_Sync/CAL_MAYA/"
        self.maFolder = ""
        for line in f:
            if '|' + self.modelName + '|' in line:
                self.maFolder = line.replace('|', '/').replace('\r', '').replace('\n', '').replace('MODELS/', 'scenes/')
                self.maFolder += 'publish/'

        f.close()

        self.test_steps(local)

    def test_steps(self, local):
        """
        en fonction du step on execute un check different
        """
        sls = cmds.ls(sl=1)
        check = []

        self.step = ""

        if self.scenePathName != "unknown" and not "_presentation_" in self.scenePathName:
            print "*" * 10
            print self.scenePathName
            print "*" * 10

            self.modelType = None
            if("characters/" in self.scenePathName.lower()):
                self.modelType = "CHARACTERS"
            elif("sets/" in self.scenePathName.lower()):
                self.modelType = "SETS"
            elif ("props/" in self.scenePathName.lower()):
                self.modelType = "PROPS"
            else:
                print "unknow model type for this scene"

            if "_mo_" in self.scenePathName or "_mo." in self.scenePathName or "_layout_" in self.scenePathName or "_layout." in self.scenePathName:
                print 'DEBUG : step LAYOUT'
                self.step = "_layout_"
                check = cal_check_modeling_gdc(self.modelName, self.modelType, local)
            elif "_rg_" in self.scenePathName or "_rg." in self.scenePathName or "_anim_" in self.scenePathName or "_anim." in self.scenePathName:
                print 'DEBUG : step ANIM'
                self.step = "_anim_"
                check = cal_check_setup_gdc(self.modelName, self.modelType, local)
            elif "_tx_" in self.scenePathName or "_tx." in self.scenePathName:
                print 'DEBUG : step TX'
                self.step = "_tx_"
                check = cal_check_shading_gdc(self.scenePathName.lower(), self.modelName, self.modelType, self.projectFolder + self.maFolder, local, txStep=True)
            elif "_render_" in self.scenePathName or "_render." in self.scenePathName:
                print 'DEBUG : step RENDER'
                self.step = "_render_"
                check = cal_check_shading_gdc(self.scenePathName.lower(), self.modelName, self.modelType, self.projectFolder + self.maFolder, local)
            else:
                print "unknow step for this scene"

        if check:
            self.val = check

        if len(sls):
            cmds.select(sls, r=1)

        cmds.select(cl=True)
        print "* DONE\n"

        print "#" * 100

        errors = ""
        warnings = ""

        if self.val:
            for logLvl, logMsg in self.val:
                if logLvl == "error":
                    errors += "\t- " + logMsg + "\n"

            for logLvl, logMsg in self.val:
                if logLvl == "warning":
                    warnings += "\t- " + logMsg + "\n"

        if errors:
            print "Errors found :"
            print errors
            if warnings:
                print "\n\nWarnings found :"
                print warnings
        else:
            if warnings:
                print "\n\nWarnings found :"
                print warnings

            if self.publish:
                self.publish_scene()

        print "#" * 100

    def publish_scene(self):
        print "#" * 100
        print ""

        if self.maFolder == "":
            print "Error : Can't find model in Z:/Projects/Calimero/Common_Sync/CAL_MAYA/2013/python/teamto/hierarchy.txt. Be sure the text file is in the good place and is updated."
            return

        publishPath = self.projectFolder + self.maFolder + self.modelName.lower() + self.step + "000.ma"

        print "Publishing scene", self.scenePathName, "to", publishPath

        if not os.path.isdir(self.projectFolder + self.maFolder):
            print "Creating path", self.projectFolder + self.maFolder
            os.makedirs(self.projectFolder + self.maFolder)

        publishSucceeded = False
        if os.path.exists(publishPath):
            if self.override:
                shutil.copy2(self.scenePathName, publishPath)
                publishSucceeded = True
                print "Success"
            else:
                print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
        else:
            shutil.copy2(self.scenePathName, publishPath)
            publishSucceeded = True
            print "Success"

        if publishSucceeded:
            f = open(publishPath, 'r')
            content = f.read()
            f.close()
            if 'setAttr ".ftn"' in content:
                content = ""
                f = open(publishPath, 'r')
                for line in f:
                    if 'setAttr ".ftn"' in line:
                        line = re.sub('setAttr ".ftn" -type "string" ".*/sourceimages/', 'setAttr ".ftn" -type "string" "sourceimages/', line)
                        lineSplit = line.split('sourceimages/')
                        name = lineSplit[1].split('/')[-1]
                        newLine = lineSplit[0] + self.maFolder.replace('scenes/', 'sourceimages/') + name
                        if self.step == "_tx_":
                            newLine = newLine.replace('/publish/', '/work/')
                        ### TODO : verifier
                        else:
                            newLine = newLine.replace('.map', '.png')
                        ###
                        content += newLine
                    else:
                        content += line
                f.close()
                f = open(publishPath, 'w')
                f.write(content)
                f.close()

        files = cmds.ls(type="file")
        for f in files:
            if cmds.attributeQuery("fileTextureName", node=f, exists=True):
                originalPath = cmds.getAttr(f + ".fileTextureName")
                originalPath = originalPath.replace('${IDMT_PROJECTS}', '//file-cluster/GDC/Projects').replace('${idmt_projects}', '//file-cluster/GDC/Projects')
                copyPath = self.maFolder.replace('scenes/', 'sourceimages/') + os.path.basename(originalPath)
                if self.step == "_tx_":
                    copyPath = copyPath.replace('/publish/', '/work/')
                if copyPath:
                    if not os.path.exists(self.projectFolder + os.path.dirname(copyPath)):
                        os.makedirs(self.projectFolder + os.path.dirname(copyPath))

                    if self.step == "_layout_" or self.step == "_anim_":
                        if os.path.isfile(originalPath):
                            print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                            if os.path.exists(self.projectFolder + copyPath):
                                if self.override:
                                    shutil.copy2(originalPath, self.projectFolder + copyPath)
                                    print "Success"
                                else:
                                    print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
                            else:
                                shutil.copy2(originalPath, self.projectFolder + copyPath)
                                print "Success"
                    else:
                        if os.path.splitext(originalPath)[1] == '.map':
                            # Copy zip textures
                            if os.path.isfile(originalPath):
                                zipPath = copyPath.replace('.map', '.zip')
                                print 'Ziping', originalPath,  'to', self.projectFolder + zipPath
                                if os.path.exists(self.projectFolder + zipPath):
                                    if self.override:
                                        z = zipfile.ZipFile(self.projectFolder + zipPath, "w", zipfile.ZIP_DEFLATED) 
                                        z.write(originalPath, os.path.basename(originalPath))
                                        z.close()
                                        print "Success"
                                    else:
                                        print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
                                else:
                                    z = zipfile.ZipFile(self.projectFolder + zipPath, "w", zipfile.ZIP_DEFLATED) 
                                    z.write(originalPath, os.path.basename(originalPath))
                                    z.close()
                                    print "Success"
                            # Copy png textures
                            originalPath = originalPath.replace('.map', '.png')
                            copyPath = copyPath.replace('.map', '.png')
                            if os.path.isfile(originalPath):
                                print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                if os.path.exists(self.projectFolder + copyPath):
                                    if self.override:
                                        shutil.copy2(originalPath, self.projectFolder + copyPath)
                                        print "Success"
                                    else:
                                        print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
                                else:
                                    shutil.copy2(originalPath, self.projectFolder + copyPath)
                                    print "Success"

                        if os.path.splitext(originalPath)[1] == '.tga':
                            # Copy tga textures
                            if os.path.isfile(originalPath):
                                print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                if os.path.exists(self.projectFolder + copyPath):
                                    if self.override:
                                        shutil.copy2(originalPath, self.projectFolder + copyPath)
                                        print "Success"
                                    else:
                                        print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
                                else:
                                    shutil.copy2(originalPath, self.projectFolder + copyPath)
                                    print "Success"

                            # Copy png textures
                            originalPath = originalPath.replace('.tga', '.png')
                            copyPath = copyPath.replace('.tga', '.png')
                            if os.path.isfile(originalPath):
                                print 'Copying', originalPath,  'to', self.projectFolder + copyPath
                                if os.path.exists(self.projectFolder + copyPath):
                                    if self.override:
                                        shutil.copy2(originalPath, self.projectFolder + copyPath)
                                        print "Success"
                                    else:
                                        print "Error : a publication of this file already exists. If you want to publish, you need to set the override parameter to True"
                                else:
                                    shutil.copy2(originalPath, self.projectFolder + copyPath)
                                    print "Success"

"""
Usage :

import sys
sys.path.append('Z:/Projects/Calimero/Common_Sync/CAL_MAYA/2013/python/teamto')
from cal_check_gdc import *

cal_scene_checker_gdc("<modelName>", publish=<boolean>, override=<boolean>, local=<boolean>)



Exemple for Calimero :
- check only:
cal_scene_checker_gdc("CALI")

- local check only:
cal_scene_checker_gdc("CALI", local=True)

- check and publish without overriding if file exists:
cal_scene_checker_gdc("CALI", publish=True)

- check and publish even if the file exists:
cal_scene_checker_gdc("CALI", publish=True, override=True)
"""

from maya import cmds
import maya.OpenMaya as OpenMaya
  
class Plane(object):
    def __init__(self, normalisedVector):
        self.vector = normalisedVector
        self.distance = 0.0
  
    def relativeToPlane(self, point):
        # converting the point as a vector from the origin to its position
        pointVec = OpenMaya.MVector(point.x, point.y, point.z)
        val = (self.vector * pointVec) + self.distance
        if (val > 0.0):
            return False
        elif (val < 0.0):
            return True
  
class Frustrum(object):
    def __init__(self, cameraName, overscan):
        # initialising selected transforms into its associated dagPaths 
        selectionList = OpenMaya.MSelectionList()
        objDagPath = OpenMaya.MDagPath()
        selectionList.add(cameraName)
        selectionList.getDagPath(0, objDagPath)
        self.camera = OpenMaya.MFnCamera(objDagPath)
  
        self.nearClip = self.camera.nearClippingPlane()
        self.farClip =  self.camera.farClippingPlane()
        self.aspectRatio = self.camera.aspectRatio()
  
        left_util= OpenMaya.MScriptUtil()
        left_util.createFromDouble(0.0)
        ptr0= left_util.asDoublePtr()
  
        right_util = OpenMaya.MScriptUtil()
        right_util.createFromDouble(0.0)
        ptr1 = right_util.asDoublePtr()
  
        bot_util = OpenMaya.MScriptUtil()
        bot_util.createFromDouble(0.0)
        ptr2 = bot_util.asDoublePtr()
  
        top_util = OpenMaya.MScriptUtil()
        top_util.createFromDouble(0.0)
        ptr3 = top_util.asDoublePtr()
  
        stat = self.camera.getViewingFrustum(self.aspectRatio, ptr0, ptr1, ptr2, ptr3, overscan, True)  
        planes = []
  
        left = left_util.getDoubleArrayItem(ptr0, 0)
        right = right_util.getDoubleArrayItem(ptr1, 0)
        bottom = bot_util.getDoubleArrayItem(ptr2, 0)
        top = top_util.getDoubleArrayItem(ptr3, 0)
  
        # planeA = right plane
        a = OpenMaya.MVector(right, top, -self.nearClip)
        b = OpenMaya.MVector(right, bottom, -self.nearClip)
        c = (a ^ b).normal() ## normal of plane = cross product of vectors a and b
        planeA = Plane(c)
        planes.append(planeA)
  
        # planeB = left plane
        a = OpenMaya.MVector(left, bottom, -self.nearClip)
        b = OpenMaya.MVector(left, top, -self.nearClip)
        c = (a ^ b).normal()
        planeB = Plane(c)
        planes.append(planeB)
  
        # planeC = bottom plane
        a = OpenMaya.MVector(right, bottom, -self.nearClip)
        b = OpenMaya.MVector(left, bottom, -self.nearClip)
        c = (a ^ b).normal()
        planeC = Plane(c)
        planes.append(planeC)
  
        # planeD = top plane
        a = OpenMaya.MVector(left, top, -self.nearClip)
        b = OpenMaya.MVector(right, top, -self.nearClip)
        c = (a ^ b).normal()
        planeD = Plane(c)
        planes.append(planeD)
  
        # planeE = far plane
        c = OpenMaya.MVector(0, 0, 1)
        planeE = Plane(c)
        planeE.distance = self.farClip
        planes.append(planeE)
  
        # planeF = near plane
        c = OpenMaya.MVector(0, 0, -1)
        planeF = Plane(c)
        planeF.distance = self.nearClip
        planes.append(planeF)
  
        self.planes = planes
        self.numPlanes = 6
  
    def relativeToFrustum(self, pointsArray):
        numInside = 0
        numPoints = len(pointsArray)
  
        for j in range(0, 6):
          numBehindThisPlane = 0
          for i in range(0, numPoints):
            if self.planes[j].relativeToPlane(pointsArray[i]):
                numBehindThisPlane += 1
            if numBehindThisPlane == numPoints:
            # all points were behind the same plane
                # return 'OUTSIDE'
                return False
            elif (numBehindThisPlane==0):
                numInside += 1
  
        if (numInside == self.numPlanes):
            # return 'INSIDE'
            return True
        # return 'INTERSECTS'
        return True
  
class DkbObjectsInCameraView():
    def __init__(self, cameraName, node, overscan):
        selectionList = OpenMaya.MSelectionList()
        camDagPath = OpenMaya.MDagPath()
        selectionList.add(cameraName)
        selectionList.getDagPath(0, camDagPath)
        self.cameraName = cameraName
        self.cameraDagPath = OpenMaya.MFnCamera(camDagPath)
  
        self.camInvWorldMtx = camDagPath.inclusiveMatrixInverse()
  
        self.node = node
        self.overscan = overscan
  
    def processNode(self):        
        fnCam = Frustrum(self.cameraName, self.overscan)
        points = []
  
        # for node in self.objectList:
        selectionList = OpenMaya.MSelectionList()
        objDagPath = OpenMaya.MDagPath()
        selectionList.add(self.node)
        selectionList.getDagPath(0, objDagPath)
  
        fnDag = OpenMaya.MFnDagNode(objDagPath)
        obj = objDagPath.node()
  
        dWorldMtx = objDagPath.exclusiveMatrix()
        bbox = fnDag.boundingBox()
  
        minx = bbox.min().x 
        miny = bbox.min().y 
        minz = bbox.min().z 
        maxx = bbox.max().x 
        maxy = bbox.max().y 
        maxz = bbox.max().z
  
        # Getting points relative to the cameras transmformation matrix
        points.append(bbox.min() * dWorldMtx * self.camInvWorldMtx)
        points.append(OpenMaya.MPoint(maxx, miny, minz) * dWorldMtx * self.camInvWorldMtx)
        points.append(OpenMaya.MPoint(maxx, miny, maxz) * dWorldMtx * self.camInvWorldMtx)
        points.append(OpenMaya.MPoint(minx, miny, maxz) * dWorldMtx * self.camInvWorldMtx)
        points.append(OpenMaya.MPoint(minx, maxy, minz) * dWorldMtx * self.camInvWorldMtx)
        points.append(OpenMaya.MPoint(maxx, maxy, minz) * dWorldMtx * self.camInvWorldMtx)
        points.append(bbox.max() * dWorldMtx * self.camInvWorldMtx)
        points.append(OpenMaya.MPoint(minx, maxy, maxz) * dWorldMtx * self.camInvWorldMtx)
  
        value = fnCam.relativeToFrustum(points)
  
        return value
  
def process(camera, node, overscan=False):
    if not camera:
        raise UserWarning('camera not found!')
    if not node:
        raise UserWarning('nodes not found!')
  
    obj = DkbObjectsInCameraView(camera, node, overscan)
    if obj.processNode():
        return True
    if not obj.processNode():
        return False
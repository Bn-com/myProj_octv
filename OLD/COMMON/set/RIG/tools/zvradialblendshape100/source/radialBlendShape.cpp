#include <math.h>

#include <maya/MPxDeformerNode.h>
#include <maya/MItGeometry.h>

#include <maya/MTypeId.h> 
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>

#include <maya/MFnNumericAttribute.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MFnMatrixAttribute.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnPlugin.h>
#include <maya/MFnMesh.h>

#include <maya/MPoint.h>
#include <maya/MVector.h>
#include <maya/MPointArray.h>
#include <maya/MVectorArray.h>
#include <maya/MMatrix.h>

#include <vector>

using std::vector;

#define PI 3.14159265
#define TWOPI 6.2831853

#define McheckErr(stat, msg)		\
	if (MS::kSuccess != stat) {		\
		cerr << msg;				\
		return MS::kFailure;		\
	}


// radialBlendShape class definition
class radialBlendShape : public MPxDeformerNode {
public:
	radialBlendShape();
	virtual ~radialBlendShape();

	static void* creator();
	static MStatus initialize();

	// deformation function
	//
    virtual MStatus deform(MDataBlock& block, MItGeometry& iter, const MMatrix& mat, unsigned int multiIndex);

public:
	// radialBlendShape attributes
	//
	static MObject inputTargetAttr;
	static MObject weightsAttr;
	static MObject inMeshAttr;
	static MObject inMatrixAttr;
	static MObject blendAttr;
	static MObject twistAttr;
	static MObject curvatureAttr;
	static MObject rbsWeightsAttr;
	static MObject rbsWeightListAttr;
	static MTypeId id;

private:
	MVectorArray defVectors;
	MPointArray origPoints;

	void toCartesian(MPoint& point, MPoint& outPoint);
	void toCilindrical(MPoint& point, MPoint& outPoint);
	void cilindricalBlend(MPoint& p1, MPoint& p2, double blend, MPoint& outPoint);

};

MTypeId radialBlendShape::id(0x58804);

// radialBlendShape attributes
MObject radialBlendShape::inputTargetAttr;
MObject radialBlendShape::inMeshAttr;
MObject radialBlendShape::inMatrixAttr;
MObject radialBlendShape::blendAttr;
MObject radialBlendShape::twistAttr;
MObject radialBlendShape::curvatureAttr;
MObject radialBlendShape::weightsAttr;
MObject radialBlendShape::rbsWeightsAttr;
MObject radialBlendShape::rbsWeightListAttr;


radialBlendShape::radialBlendShape() { 
}

radialBlendShape::~radialBlendShape() {
}

void* radialBlendShape::creator() {
	return new radialBlendShape();
}

// Attributes
MStatus radialBlendShape::initialize() {
	// target mesh
	MFnTypedAttribute tAttr;
	inMeshAttr = tAttr.create("inMesh", "i", MFnData::kMesh);
	addAttribute(inMeshAttr);
	
	// matrix of the center
	MFnMatrixAttribute mAttr;
	inMatrixAttr = mAttr.create("inMatrix", "m");
	addAttribute(inMatrixAttr);
	
	// blend value
	MFnNumericAttribute nAttr;
	blendAttr = nAttr.create("blend", "b", MFnNumericData::kDouble, -1000.0);
	nAttr.setArray(true);
	nAttr.setUsesArrayDataBuilder(true);
	nAttr.setKeyable(true);
	addAttribute(blendAttr);

	// twist value
	twistAttr = nAttr.create("twist", "t", MFnNumericData::kDouble, -1000.0);
	nAttr.setArray(true);
	nAttr.setUsesArrayDataBuilder(true);
	nAttr.setKeyable(true);
	addAttribute(twistAttr);

	// curvature value
	curvatureAttr = nAttr.create("curvature", "c", MFnNumericData::kDouble, -1000.0);
	nAttr.setArray(true);
	nAttr.setUsesArrayDataBuilder(true);
	nAttr.setKeyable(true);
	addAttribute(curvatureAttr); 

	// weights array
	weightsAttr = nAttr.create("targetWeights", "tw", MFnNumericData::kFloat, -1000.0);
	nAttr.setMin(0.0);
	nAttr.setMax(1.0);
	nAttr.setArray(true);
	nAttr.setReadable(true);
	nAttr.setUsesArrayDataBuilder(true);
	addAttribute(weightsAttr);

	// input target compound attr
	MFnCompoundAttribute cAttr;
	inputTargetAttr = cAttr.create("inputTarget", "it");
	cAttr.setArray(true);

	cAttr.addChild(inMeshAttr);
	cAttr.addChild(inMatrixAttr);
	cAttr.addChild(weightsAttr);

	cAttr.setUsesArrayDataBuilder(true);
	addAttribute(inputTargetAttr);

	// paintable weights array
	rbsWeightsAttr = nAttr.create("radialWeights", "rw", MFnNumericData::kFloat, -1000.0);
	nAttr.setMin(0.0);
	nAttr.setMax(1.0);
	nAttr.setArray(true);
	nAttr.setUsesArrayDataBuilder(true);
	addAttribute(rbsWeightsAttr);

	// paintable weights array list
	rbsWeightListAttr = cAttr.create("radialWeightList", "rwl");
	cAttr.setHidden(true);
	cAttr.setArray(true);

	cAttr.addChild(rbsWeightsAttr);
	cAttr.setReadable(true);
	cAttr.setUsesArrayDataBuilder(true);
	addAttribute(rbsWeightListAttr);

	// affects
    attributeAffects(blendAttr, outputGeom);
    attributeAffects(twistAttr, outputGeom);
    attributeAffects(curvatureAttr, outputGeom);
    attributeAffects(inputTargetAttr, outputGeom);

	return MS::kSuccess;
}

// Deformation function
MStatus radialBlendShape::deform(MDataBlock& block, MItGeometry& iter, const MMatrix& mat, unsigned int) {
	MStatus status = MS::kSuccess;
	
	// envelope
	MDataHandle numDH = block.inputValue(envelope, &status);
	float envelope = numDH.asFloat();

	// input target attribute
	MArrayDataHandle inputTargetADH = block.inputArrayValue(inputTargetAttr, &status);

	unsigned int targetCount = inputTargetADH.elementCount();

	// exit if none
	if (envelope == 0.0f || targetCount == 0) {
		return status;
	}

	// blend, twist, curvature arrays
	MArrayDataHandle blendADH = block.inputArrayValue(blendAttr, &status);
	MArrayDataHandle twistADH = block.inputArrayValue(twistAttr, &status);
	MArrayDataHandle curvatureADH = block.inputArrayValue(curvatureAttr, &status);

	// variables
	MObject meshObj;
	MMatrix invGeoMatrix, matrix, invMatrix;
	double blend, twist, curvature;

	int tidx, idx;
	unsigned int t, i, pointCount;
	MDataHandle dh, vdh, cdh;

	MStatus elemStatus;
	MPoint targetPoint, origPointLS, targetPointLS, blendedPointLS, origPointLSCil, targetPointLSCil, blendedPointLSCil;
	MVector tmpVector;
	MVector* finalVector;
	MPoint* origPoint;
	double localBlend;
	float weight;

	// store the geo's inverse matrix
	invGeoMatrix = mat.inverse();

	// store the original points
	iter.allPositions(origPoints, MSpace::kObject);
	pointCount = origPoints.length();

	// resize the array if needed
	if (defVectors.length() != pointCount)
		defVectors.setLength(iter.count());

	// zero out the deformation vectors
	for (i = 0; i < pointCount; i++)
		defVectors[i] = MVector::zero;
	
	// loop through the connected or stored meshes (radial blend shape targets)
	for (t=0; t<targetCount; inputTargetADH.next(), t++) {
		tidx = inputTargetADH.elementIndex();

		dh = inputTargetADH.inputValue();

		// target mesh
		cdh = dh.child(inMeshAttr);
		meshObj = cdh.asMesh();

		MFnMesh mesh(meshObj);

		// if no points continue
		if (mesh.numVertices() == 0)
			continue;

		// matrix (locator's matrix relative to the geo's transform)
		cdh = dh.child(inMatrixAttr);
		matrix = cdh.asMatrix();
		matrix *= invGeoMatrix;
		invMatrix = matrix.inverse();

		// weights array
		cdh = dh.child(weightsAttr);
		MArrayDataHandle weightsADH(cdh);

		// blend
		blendADH.jumpToElement(tidx);
		vdh = blendADH.inputValue(&elemStatus);
		blend = (elemStatus == MS::kSuccess)? vdh.asDouble() : 0.0;

		// twist
		twistADH.jumpToElement(tidx);
		vdh = twistADH.inputValue(&elemStatus);
		twist = (elemStatus == MS::kSuccess)? vdh.asDouble() : 0.0;

		// curvature
		curvatureADH.jumpToElement(tidx);
		vdh = curvatureADH.inputValue(&elemStatus);
		curvature = (elemStatus == MS::kSuccess)? vdh.asDouble() : 0.0;

		// loop through the affected points
		for (i=0; !iter.isDone(); i++, iter.next()) {
			idx = iter.index();

			origPoint = &origPoints[i];
			finalVector = &defVectors[i];
			mesh.getPoint(idx, targetPoint, MSpace::kObject);
			
			// if the target point is not equal to the original point than do the blend calculation
			if (targetPoint != (*origPoint)) {
				// get the weight
				if (weightsADH.jumpToArrayElement(idx) == MStatus::kSuccess) {
					weight = weightsADH.inputValue().asFloat();
					if (weight == 0.0)
						continue;
				}
				else {
					weight = 1.0;
				}

				// points in locator space
				origPointLS = (*origPoint)*invMatrix;
				targetPointLS = targetPoint*invMatrix;
				
				// get the blend value for this particular point
				localBlend = (blend + (curvature*origPointLS.x + twist)*origPointLS.x)*weight;

				// convert to cilindrical coordinates
				toCilindrical(origPointLS, origPointLSCil);
				toCilindrical(targetPointLS, targetPointLSCil);

				// get the blended point
				cilindricalBlend(origPointLSCil, targetPointLSCil, localBlend, blendedPointLSCil);

				// convert the blended point to cartesian (locator space)
				toCartesian(blendedPointLSCil, blendedPointLS);

				// get the offset from the original position
				tmpVector = blendedPointLS - origPointLS;

				// convert the offset to object space
				tmpVector *= matrix;

				// sum this offset to the other target offsets
				(*finalVector) += tmpVector;
			}
		}
		iter.reset();
	}

	// envelope blending pass
	for (i=0; i < pointCount; i++) {
		finalVector = &defVectors[i];

		// set the final position of this point
		(*finalVector) *= envelope;
		origPoints[i] += (*finalVector);
	}

	// set the final positions
	iter.setAllPositions(origPoints, MSpace::kObject);

	return status;
}

// Convert from cartesian to cilindrical coordinates
void radialBlendShape::toCilindrical(MPoint& point, MPoint& outPoint) {
	// radius
	outPoint.x = sqrt(point.z*point.z + point.y*point.y);
	// angle
	outPoint.y = atan2(point.y, point.z);
	// h
	outPoint.z = point.x;
}

// Convert from cilindrical to cartesian coordinates
void radialBlendShape::toCartesian(MPoint& point, MPoint& outPoint) {
	outPoint.x = point.z;
	outPoint.y = point.x*sin(point.y);
	outPoint.z = point.x*cos(point.y);
}

// Blend two cilindrical coordinates in the shortest path
void radialBlendShape::cilindricalBlend(MPoint& p1, MPoint& p2, double blend, MPoint& outPoint) {
	outPoint.x = (p2.x - p1.x)*blend + p1.x;

	double diff = p2.y - p1.y;
	if (diff > PI)
		diff -= TWOPI;
	else if (diff < -PI)
		diff += TWOPI;

	outPoint.y = diff*blend + p1.y;
	outPoint.z = (p2.z - p1.z)*blend + p1.z;
}

// Initialize
MStatus initializePlugin(MObject obj) {
	MStatus result;
	MFnPlugin plugin(obj, "Paolo Dominici (paolodominici@gmail.com)", "1.0", "Any");
	result = plugin.registerNode("radialBlendShape", radialBlendShape::id, radialBlendShape::creator, radialBlendShape::initialize, MPxNode::kDeformerNode);
	return result;
}

// Uninitialize
MStatus uninitializePlugin(MObject obj) {
	MStatus result;
	MFnPlugin plugin(obj);
	result = plugin.deregisterNode(radialBlendShape::id);
	return result;
}

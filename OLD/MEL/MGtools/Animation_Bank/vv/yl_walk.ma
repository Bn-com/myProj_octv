//Maya ASCII 2012 scene
//Name: yl_walk.ma
//Last modified: Thu, Aug 23, 2012 06:58:28 PM
//Codeset: 936
requires maya "2012";
requires "Mayatomr" "2012.0m - 3.9.1.48 ";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t pal;
fileInfo "application" "maya";
fileInfo "product" "Maya 2012";
fileInfo "version" "2012 x64";
fileInfo "cutIdentifier" "201201172029-821146";
fileInfo "osv" "Microsoft Windows XP Professional x64 Edition Service Pack 2 (Build 3790)\n";
createNode transform -n "MG_outPutAnimBank";
	addAttr -ci true -sn "ns" -ln "ns" -dt "string";
	addAttr -ci true -sn "range" -ln "range" -dt "string";
	addAttr -ci true -sn "num" -ln "num" -at "long";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".ns" -type "string" "ylva_original";
	setAttr ".range" -type "string" "\"1:34\"";
	setAttr ".num" 73;
	setAttr ".nts" -type "string" (
		"ylva_original:hair_ex_ctrl; ylva_original:head_squash_ctrl; ylva_original:l_armA_thumb_02_ctrl; ylva_original:l_armA_thumb_03_ctrl; ylva_original:l_eye_ctrl; ylva_original:l_legA_ankle_ctrl; ylva_original:l_legA_foot_IK_ctrl; ylva_original:l_legA_heel_IK_ctrl; ylva_original:l_legA_knee_IK_ctrl; ylva_original:l_legA_pelvis_ctrl; ylva_original:l_teethBtmA_ctrl; ylva_original:l_teethTopA_ctrl; ylva_original:m_armA_shoulder_ctrl; ylva_original:m_bothEye_ctrl; ylva_original:m_eye_ctrl; ylva_original:m_jaw_ctrl; ylva_original:m_spineA_body_ctrl; ylva_original:m_spineA_chest_ctrl; ylva_original:m_spineA_head_ctrl; ylva_original:m_spineA_hip_ctrl; ylva_original:m_spineA_neck_01_ctrl; ylva_original:m_spineA_neck_02_ctrl; ylva_original:m_spineA_neck_03_ctrl; ylva_original:m_spineA_torso_ctrl; ylva_original:m_spineA_waistFree_ctrl; ylva_original:m_spineA_waist_ctrl; ylva_original:m_teethBtmA_ctrl; ylva_original:m_teethBtmB_ctrl; ylva_original:m_teethTopA_ctrl; ylva_original:m_teethTopB_ctrl; ylva_original:r_armA_hand_IK_ctrl; ylva_original:r_armA_index_02_ctrl; ylva_original:r_armA_index_03_ctrl; ylva_original:r_armA_index_04_ctrl; ylva_original:r_armA_middle_02_ctrl; ylva_original:r_armA_middle_03_ctrl; ylva_original:r_armA_middle_04_ctrl; ylva_original:r_armA_ring_02_ctrl; ylva_original:r_armA_ring_03_ctrl; ylva_original:r_armA_ring_04_ctrl; ylva_original:r_armA_thumb_01_ctrl; ylva_original:r_armA_thumb_02_ctrl; ylva_original:r_armA_thumb_03_ctrl; ylva_original:r_eye_ctrl; ylva_original:r_legA_ankle_ctrl; ylva_original:r_legA_foot_IK_ctrl; ylva_original:r_legA_heel_IK_ctrl; ylva_original:r_legA_knee_IK_ctrl; ylva_original:r_legA_pelvis_ctrl; ylva_original:r_teethBtmA_ctrl; ylva_original:r_teethTopA_ctrl; ylva_original:skirt_lwrwire_1_ctrl; ylva_original:skirt_lwrwire_2_ctrl; ylva_original:skirt_lwrwire_3_ctrl; ylva_original:skirt_lwrwire_4_ctrl; ylva_original:skirt_lwrwire_5_ctrl; ylva_original:skirt_lwrwire_6_ctrl; ylva_original:skirt_lwrwire_7_ctrl; ylva_original:skirt_lwrwire_8_ctrl; ylva_original:skirt_midwire_1_ctrl; ylva_original:skirt_midwire_2_ctrl; ylva_original:skirt_midwire_3_ctrl; ylva_original:skirt_midwire_4_ctrl; ylva_original:skirt_midwire_5_ctrl; ylva_original:skirt_midwire_6_ctrl; ylva_original:skirt_midwire_7_ctrl; ylva_original:skirt_midwire_8_ctrl; ylva_original:tongueCon_ctrl; ylva_original:top_ctrl; ylva_original:l_armA_elbow_FK_ctrl; ylva_original:l_armA_uprarm_FK_ctrl; ylva_original:r_armA_uprarm_FK_ctrl; ylva_original:r_armA_elbow_FK_ctrl; ");
createNode transform -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "subCtrl" -ln "subCtrl" -at "long";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k on ".subCtrl";
	setAttr ".ObjName" -type "string" "ylva_original:hair_ex_ctrl";
createNode locator -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1Shape" -p "ylva_original:hair_ex_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:head_squash_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:head_squash_ctrl";
createNode locator -n "ylva_original:head_squash_ctrl_outPutAnimBank_1Shape" -p "ylva_original:head_squash_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_thumb_02_ctrl";
createNode locator -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_thumb_03_ctrl";
createNode locator -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_eye_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "crossEyeFix" -ln "crossEyeFix" -at "double";
	addAttr -ci true -sn "crossEyeRate" -ln "crossEyeRate" -at "double";
	addAttr -ci true -sn "Iris_Size" -ln "Iris_Size" -at "double";
	addAttr -ci true -sn "Pupil_Size" -ln "Pupil_Size" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".crossEyeFix";
	setAttr -k on ".crossEyeRate";
	setAttr -k on ".Iris_Size";
	setAttr -k on ".Pupil_Size";
	setAttr ".ObjName" -type "string" "ylva_original:l_eye_ctrl";
createNode locator -n "ylva_original:l_eye_ctrl_outPutAnimBank_1Shape" -p "ylva_original:l_eye_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "FK_2_IK" -ln "FK_2_IK" -at "double";
	addAttr -ci true -sn "globalIK_2_localIK" -ln "globalIK_2_localIK" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".FK_2_IK";
	setAttr -k on ".globalIK_2_localIK";
	setAttr ".ObjName" -type "string" "ylva_original:l_legA_ankle_ctrl";
createNode locator -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1Shape" -p "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "footHeight" -ln "footHeight" -at "double";
	addAttr -ci true -sn "footRoll" -ln "footRoll" -at "double";
	addAttr -ci true -sn "toeBend" -ln "toeBend" -at "double";
	addAttr -ci true -sn "heelTurn" -ln "heelTurn" -at "double";
	addAttr -ci true -sn "toeTurn" -ln "toeTurn" -at "double";
	addAttr -ci true -sn "footSide" -ln "footSide" -at "double";
	addAttr -ci true -sn "thighStretch" -ln "thighStretch" -at "double";
	addAttr -ci true -sn "shankStretch" -ln "shankStretch" -at "double";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -at "double";
	addAttr -ci true -sn "preferredAngle" -ln "preferredAngle" -at "double";
	addAttr -ci true -sn "kneeTwist" -ln "kneeTwist" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".footHeight";
	setAttr -k on ".footRoll";
	setAttr -k on ".toeBend";
	setAttr -k on ".heelTurn";
	setAttr -k on ".toeTurn";
	setAttr -k on ".footSide";
	setAttr -k on ".thighStretch";
	setAttr -k on ".shankStretch";
	setAttr -k on ".autoStretch";
	setAttr -k on ".preferredAngle";
	setAttr -k on ".kneeTwist";
	setAttr ".ObjName" -type "string" "ylva_original:l_legA_foot_IK_ctrl";
createNode locator -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:l_legA_heel_IK_ctrl";
createNode locator -n "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "followBody_2_followFoot" -ln "followBody_2_followFoot" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".followBody_2_followFoot";
	setAttr ".ObjName" -type "string" "ylva_original:l_legA_knee_IK_ctrl";
createNode locator -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:l_legA_pelvis_ctrl";
createNode locator -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:l_teethBtmA_ctrl";
createNode locator -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1Shape" -p "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:l_teethTopA_ctrl";
createNode locator -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1Shape" -p "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "followBody" -ln "followBody" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".followBody";
	setAttr ".ObjName" -type "string" "ylva_original:m_armA_shoulder_ctrl";
createNode locator -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "l_eye_offset" -ln "l_eye_offset" -at "double";
	addAttr -ci true -sn "r_eye_offset" -ln "r_eye_offset" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".l_eye_offset";
	setAttr -k on ".r_eye_offset";
	setAttr ".ObjName" -type "string" "ylva_original:m_bothEye_ctrl";
createNode locator -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_bothEye_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_eye_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "l_eyePSD_tx" -ln "l_eyePSD_tx" -at "double";
	addAttr -ci true -sn "l_eyePSD_sc" -ln "l_eyePSD_sc" -at "double";
	addAttr -ci true -sn "bothEye_offset" -ln "bothEye_offset" -at "double";
	addAttr -ci true -sn "irisSize_temp" -ln "irisSize_temp" -at "double";
	addAttr -ci true -sn "pupilSize_temp" -ln "pupilSize_temp" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k on ".l_eyePSD_tx";
	setAttr -k on ".l_eyePSD_sc";
	setAttr -k on ".bothEye_offset";
	setAttr -k on ".irisSize_temp";
	setAttr -k on ".pupilSize_temp";
	setAttr ".ObjName" -type "string" "ylva_original:m_eye_ctrl";
createNode locator -n "ylva_original:m_eye_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_eye_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:m_jaw_ctrl";
createNode locator -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_jaw_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:m_spineA_body_ctrl";
createNode locator -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "wide" -ln "wide" -at "double";
	addAttr -ci true -sn "thick" -ln "thick" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".rpy";
	setAttr -k on ".wide";
	setAttr -k on ".thick";
	setAttr ".ObjName" -type "string" "ylva_original:m_spineA_chest_ctrl";
createNode locator -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "orbit" -ln "orbit" -at "double";
	addAttr -ci true -sn "nod" -ln "nod" -at "double";
	addAttr -ci true -sn "side" -ln "side" -at "double";
	addAttr -ci true -sn "twist" -ln "twist" -at "double";
	addAttr -ci true -sn "neckStretch" -ln "neckStretch" -at "double";
	addAttr -ci true -sn "compensation" -ln "compensation" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".orbit";
	setAttr -k on ".nod";
	setAttr -k on ".side";
	setAttr -k on ".twist";
	setAttr -k on ".neckStretch";
	setAttr -k on ".compensation";
	setAttr ".ObjName" -type "string" "ylva_original:m_spineA_head_ctrl";
createNode locator -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "wide" -ln "wide" -at "double";
	addAttr -ci true -sn "thick" -ln "thick" -at "double";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".rpy";
	setAttr -k on ".wide";
	setAttr -k on ".thick";
	setAttr -k on ".autoStretch";
	setAttr ".ObjName" -type "string" "ylva_original:m_spineA_hip_ctrl";
createNode locator -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:m_spineA_neck_01_ctrl";
createNode locator -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:m_spineA_neck_02_ctrl";
createNode locator -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:m_spineA_neck_03_ctrl";
createNode locator -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:m_spineA_torso_ctrl";
createNode locator -n "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1" 
		-p "MG_outPutAnimBank";
	addAttr -ci true -sn "wide" -ln "wide" -at "double";
	addAttr -ci true -sn "thick" -ln "thick" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".wide";
	setAttr -k on ".thick";
	setAttr ".ObjName" -type "string" "ylva_original:m_spineA_waistFree_ctrl";
createNode locator -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".rpy";
	setAttr ".ObjName" -type "string" "ylva_original:m_spineA_waist_ctrl";
createNode locator -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:m_teethBtmA_ctrl";
createNode locator -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:m_teethBtmB_ctrl";
createNode locator -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:m_teethTopA_ctrl";
createNode locator -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:m_teethTopB_ctrl";
createNode locator -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "uprarmStretch" -ln "uprarmStretch" -at "double";
	addAttr -ci true -sn "forearmStretch" -ln "forearmStretch" -at "double";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -at "double";
	addAttr -ci true -sn "elbowTwist" -ln "elbowTwist" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".uprarmStretch";
	setAttr -k on ".forearmStretch";
	setAttr -k on ".autoStretch";
	setAttr -k on ".elbowTwist";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_hand_IK_ctrl";
createNode locator -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_index_02_ctrl";
createNode locator -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_index_03_ctrl";
createNode locator -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_index_04_ctrl";
createNode locator -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_middle_02_ctrl";
createNode locator -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_middle_03_ctrl";
createNode locator -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_middle_04_ctrl";
createNode locator -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_ring_02_ctrl";
createNode locator -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_ring_03_ctrl";
createNode locator -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_ring_04_ctrl";
createNode locator -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_thumb_01_ctrl";
createNode locator -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_thumb_02_ctrl";
createNode locator -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_thumb_03_ctrl";
createNode locator -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_eye_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "crossEyeFix" -ln "crossEyeFix" -at "double";
	addAttr -ci true -sn "crossEyeRate" -ln "crossEyeRate" -at "double";
	addAttr -ci true -sn "Iris_Size" -ln "Iris_Size" -at "double";
	addAttr -ci true -sn "Pupil_Size" -ln "Pupil_Size" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".crossEyeFix";
	setAttr -k on ".crossEyeRate";
	setAttr -k on ".Iris_Size";
	setAttr -k on ".Pupil_Size";
	setAttr ".ObjName" -type "string" "ylva_original:r_eye_ctrl";
createNode locator -n "ylva_original:r_eye_ctrl_outPutAnimBank_1Shape" -p "ylva_original:r_eye_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "FK_2_IK" -ln "FK_2_IK" -at "double";
	addAttr -ci true -sn "globalIK_2_localIK" -ln "globalIK_2_localIK" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".FK_2_IK";
	setAttr -k on ".globalIK_2_localIK";
	setAttr ".ObjName" -type "string" "ylva_original:r_legA_ankle_ctrl";
createNode locator -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1Shape" -p "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "footHeight" -ln "footHeight" -at "double";
	addAttr -ci true -sn "footRoll" -ln "footRoll" -at "double";
	addAttr -ci true -sn "toeBend" -ln "toeBend" -at "double";
	addAttr -ci true -sn "heelTurn" -ln "heelTurn" -at "double";
	addAttr -ci true -sn "toeTurn" -ln "toeTurn" -at "double";
	addAttr -ci true -sn "footSide" -ln "footSide" -at "double";
	addAttr -ci true -sn "thighStretch" -ln "thighStretch" -at "double";
	addAttr -ci true -sn "shankStretch" -ln "shankStretch" -at "double";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -at "double";
	addAttr -ci true -sn "preferredAngle" -ln "preferredAngle" -at "double";
	addAttr -ci true -sn "kneeTwist" -ln "kneeTwist" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".footHeight";
	setAttr -k on ".footRoll";
	setAttr -k on ".toeBend";
	setAttr -k on ".heelTurn";
	setAttr -k on ".toeTurn";
	setAttr -k on ".footSide";
	setAttr -k on ".thighStretch";
	setAttr -k on ".shankStretch";
	setAttr -k on ".autoStretch";
	setAttr -k on ".preferredAngle";
	setAttr -k on ".kneeTwist";
	setAttr ".ObjName" -type "string" "ylva_original:r_legA_foot_IK_ctrl";
createNode locator -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:r_legA_heel_IK_ctrl";
createNode locator -n "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "followBody_2_followFoot" -ln "followBody_2_followFoot" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".followBody_2_followFoot";
	setAttr ".ObjName" -type "string" "ylva_original:r_legA_knee_IK_ctrl";
createNode locator -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:r_legA_pelvis_ctrl";
createNode locator -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:r_teethBtmA_ctrl";
createNode locator -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1Shape" -p "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:r_teethTopA_ctrl";
createNode locator -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1Shape" -p "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_lwrwire_1_ctrl";
createNode locator -n "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_lwrwire_2_ctrl";
createNode locator -n "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_lwrwire_3_ctrl";
createNode locator -n "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_lwrwire_4_ctrl";
createNode locator -n "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_lwrwire_5_ctrl";
createNode locator -n "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_lwrwire_6_ctrl";
createNode locator -n "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_lwrwire_7_ctrl";
createNode locator -n "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_lwrwire_8_ctrl";
createNode locator -n "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_midwire_1_ctrl";
createNode locator -n "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_midwire_2_ctrl";
createNode locator -n "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_midwire_3_ctrl";
createNode locator -n "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_midwire_4_ctrl";
createNode locator -n "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_midwire_5_ctrl";
createNode locator -n "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_midwire_6_ctrl";
createNode locator -n "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_midwire_7_ctrl";
createNode locator -n "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:skirt_midwire_8_ctrl";
createNode locator -n "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:tongueCon_ctrl";
createNode locator -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1Shape" -p "ylva_original:tongueCon_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:top_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "globalScale" -ln "globalScale" -at "double";
	addAttr -ci true -sn "bodyRes" -ln "bodyRes" -at "long";
	addAttr -ci true -sn "ribbonCtrl_grp" -ln "ribbonCtrl_grp" -at "long";
	addAttr -ci true -sn "hairCtrl" -ln "hairCtrl" -at "long";
	addAttr -ci true -sn "clothCtrl" -ln "clothCtrl" -at "long";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".globalScale";
	setAttr -k on ".bodyRes";
	setAttr -k on ".ribbonCtrl_grp";
	setAttr -k on ".hairCtrl";
	setAttr -k on ".clothCtrl";
	setAttr ".ObjName" -type "string" "ylva_original:top_ctrl";
createNode locator -n "ylva_original:top_ctrl_outPutAnimBank_1Shape" -p "ylva_original:top_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "twistBlend" -ln "twistBlend" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".twistBlend";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_elbow_FK_ctrl";
createNode locator -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "twistBlend" -ln "twistBlend" -at "double";
	addAttr -ci true -sn "compensation" -ln "compensation" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".twistBlend";
	setAttr -k on ".compensation";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_uprarm_FK_ctrl";
createNode locator -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "twistBlend" -ln "twistBlend" -at "double";
	addAttr -ci true -sn "compensation" -ln "compensation" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".twistBlend";
	setAttr -k on ".compensation";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_uprarm_FK_ctrl";
createNode locator -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "twistBlend" -ln "twistBlend" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".twistBlend";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_elbow_FK_ctrl";
createNode locator -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 5;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
	setAttr -s 9 ".kit[0:8]"  9 9 9 9 9 9 9 9 
		1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
createNode animCurveTL -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -0.00020660770125248418 5 0.0097666868753931435
		 9 0.0072539516938125454 13 0.0089601117883126424 17 0.0026520814025220284 21 0.0081417048777622878
		 25 0.0078682617197761932 29 0.0075254381637327164 33 -0.00020660770125248418;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTL -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -0.041676805968393363 5 1.8956386840202946
		 9 1.4065410342469002 13 1.7267976867026198 17 0.49095375078321624 21 1.5526234790842668
		 25 1.5023698604400733 29 1.4449566669972211 33 -0.041676805968393363;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTL -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.67757697999640476 5 0.69797939790337882
		 9 0.66276502847335717 13 0.72130422499467317 17 0.81485119330438471 21 0.74333491345093761
		 25 0.71420438548563236 29 0.65192777097335641 33 0.67757697999640476;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTA -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTA -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTA -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_subCtrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
	setAttr -s 9 ".kot[0:8]"  5 5 5 5 5 5 5 5 
		5;
createNode animCurveTL -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 17 0 33 0;
createNode animCurveTL -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 17 0 33 0;
createNode animCurveTL -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 17 0 33 0;
createNode animCurveTA -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -8.132716 9 -8.8134584010190249 17 -8.132716
		 25 -8.776884651632276 33 -8.132716;
createNode animCurveTA -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -17.427749 9 -13.024108270537573 17 -17.427749
		 25 -13.26917508460329 33 -17.427749;
createNode animCurveTA -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 9.21258 9 8.5641211718598402 17 9.21258
		 25 8.6016137970053013 33 9.21258;
createNode animCurveTU -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 17 1 33 1;
createNode animCurveTU -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 17 1 33 1;
createNode animCurveTU -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 17 1 33 1;
createNode animCurveTL -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 17 0 33 0;
createNode animCurveTL -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 17 0 33 0;
createNode animCurveTL -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 17 0 33 0;
createNode animCurveTA -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 23.514925 9 23.251570443929271 17 23.514925
		 25 23.2695174332063 33 23.514925;
createNode animCurveTA -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 26.591115000000002 9 30.637033742844004
		 17 26.591115000000002 25 30.41104504869816 33 26.591115000000002;
createNode animCurveTA -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 2.856867 9 4.6033754135370009 17 2.856867
		 25 4.5065404133648839 33 2.856867;
createNode animCurveTU -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 17 1 33 1;
createNode animCurveTU -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 17 1 33 1;
createNode animCurveTU -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 17 1 33 1;
createNode animCurveTL -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_crossEyeFix";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_crossEyeRate";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.5 5 0.5 9 0.5 13 0.5 17 0.5 21 0.5 25 0.5
		 29 0.5 33 0.5;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_Iris_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_Pupil_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 -0.085919060734705482 5 -0.087668223383194618
		 13 -0.11562952124030068 17 -0.13002531744795462 21 -0.13002531744795462 25 -0.13002531744795462
		 29 -0.085919060734705482 33 -0.085919060734705482;
createNode animCurveTL -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -2.4318292522439604 5 -2.7078354354591934
		 9 -1.1034313503902844 13 1.2597352260348578 17 1.0996653890580981 33 -2.4318292522439604;
	setAttr -s 6 ".kit[3:5]"  1 9 9;
	setAttr -s 6 ".kot[3:5]"  1 9 9;
	setAttr -s 6 ".kix[3:5]"  0.53901690244674683 0.21179409325122833 
		0.17832174897193909;
	setAttr -s 6 ".kiy[3:5]"  0.84229499101638794 -0.97731435298919678 
		-0.98397225141525269;
	setAttr -s 6 ".kox[3:5]"  0.53901684284210205 0.21179409325122833 
		0.17832174897193909;
	setAttr -s 6 ".koy[3:5]"  0.84229499101638794 -0.97731435298919678 
		-0.98397225141525269;
createNode animCurveTA -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0.4911933786510469 9 1.3319133794360785
		 13 2.0783644126717227 17 -24.185653423397245 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0.42328955543559466 9 1.0449817019489069
		 13 0.41068358224466051 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[1:8]"  1 18 1 18 18 18 18 18;
	setAttr -s 9 ".kot[1:8]"  1 18 1 18 18 18 18 18;
	setAttr -s 9 ".kix[1:8]"  0.14203673601150513 1 0.15218028426170349 
		1 1 1 1 1;
	setAttr -s 9 ".kiy[1:8]"  0.98986136913299561 0 -0.98835277557373047 
		0 0 0 0 0;
	setAttr -s 9 ".kox[1:8]"  0.14203676581382751 1 0.15218028426170349 
		1 1 1 1 1;
	setAttr -s 9 ".koy[1:8]"  0.98986142873764038 0 -0.98835277557373047 
		0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 29.8 5 66.445253993387567 9 27.908076870529904
		 13 2.5479443606817185 17 0 21 0 25 0 29 14.899991673977549 33 29.8;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 1.079976827431788 9 3.2349537848171597
		 13 6.544145882935485 17 8.6 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footSide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTL -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_followBody";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTL -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 -0.0011297796595487668;
createNode animCurveTL -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.36315789473684218 5 0.36315789473684218
		 9 0.36315789473684218 13 0.36315789473684218 17 0.36315789473684218 21 0.36315789473684218
		 25 0.36315789473684218 29 0.36315789473684218 33 0.36315789473684218;
createNode animCurveTL -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_l_eye_offset";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_r_eye_offset";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -0.00020244999999999999 5 -0.00020244999999999999
		 9 -0.00020244999999999999 13 -0.00020244999999999999 17 -0.00020244999999999999 21 -0.00020244999999999999
		 25 -0.00020244999999999999 29 -0.00020244999999999999 33 -0.00020244999999999999;
createNode animCurveTL -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 16.290981800000001 5 16.290981800000001
		 9 16.290981800000001 13 16.290981800000001 17 16.290981800000001 21 16.290981800000001
		 25 16.290981800000001 29 16.290981800000001 33 16.290981800000001;
createNode animCurveTL -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1.68490439 5 1.68490439 9 1.68490439 13 1.68490439
		 17 1.68490439 21 1.68490439 25 1.68490439 29 1.68490439 33 1.68490439;
createNode animCurveTA -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -3.7000000000000006 5 -3.7000000000000006
		 9 -3.7000000000000006 13 -3.7000000000000006 17 -3.7000000000000006 21 -3.7000000000000006
		 25 -3.7000000000000006 29 -3.7000000000000006 33 -3.7000000000000006;
createNode animCurveTA -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_tx";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.18 5 0.18 9 0.18 13 0.18 17 0.18 21 0.18
		 25 0.18 29 0.18 33 0.18;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_sc";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1.215 5 1.215 9 1.215 13 1.215 17 1.215
		 21 1.215 25 1.215 29 1.215 33 1.215;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_bothEye_offset";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 8 5 8 9 8 13 8 17 8 21 8 25 8 29 8 33 8;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_irisSize_temp";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -2.5 5 -2.5 9 -2.5 13 -2.5 17 -2.5 21 -2.5
		 25 -2.5 29 -2.5 33 -2.5;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_pupilSize_temp";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -5 5 -5 9 -5 13 -5 17 -5 21 -5 25 -5 29 -5
		 33 -5;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
	setAttr -s 9 ".kot[0:8]"  5 5 5 5 5 5 5 5 
		5;
createNode animCurveTL -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTL -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 9 -0.065936801642300757 25 0.1181646979690007
		 33 0;
	setAttr -s 4 ".kit[0:3]"  1 18 18 18;
	setAttr -s 4 ".kot[0:3]"  1 18 18 18;
	setAttr -s 4 ".kix[0:3]"  1 1 1 1;
	setAttr -s 4 ".kiy[0:3]"  0 0 0 0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -0.0031952045507457633 5 -0.11663531512351262
		 9 -0.0031952045507457633 13 0.14279418179463488 17 -0.0031952045507457633 21 -0.11701782786264786
		 25 -0.0031952045507457633 29 0.14317669453376314 33 -0.0031952045507457633;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 1 0.77679133415222168 1 0.7763371467590332 
		1 0.77588313817977905 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0.62975805997848511 0 -0.63031786680221558 
		0 0.63087666034698486 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 0.7767912745475769 1 0.7763371467590332 
		1 0.77588307857513428 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0.62975805997848511 0 -0.63031792640686035 
		0 0.63087671995162964 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0.099999995343387174 9 0.2 13 0.099999981373546917
		 17 0 21 0.099999972060322156 25 0.2 29 0.1000000558793453 33 0;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 0.84799832105636597 1 0.84799832105636597 
		1 0.84799832105636597 1 0.84799832105636597 1;
	setAttr -s 9 ".kiy[0:8]"  0 0.52999889850616455 0 -0.52999895811080933 
		0 0.52999895811080933 0 -0.52999889850616455 0;
	setAttr -s 9 ".kox[0:8]"  1 0.84799832105636597 1 0.84799826145172119 
		1 0.84799826145172119 1 0.84799832105636597 1;
	setAttr -s 9 ".koy[0:8]"  0 0.52999889850616455 0 -0.52999889850616455 
		0 0.52999889850616455 0 -0.52999883890151978 0;
createNode animCurveTA -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -3.3831616727896914 5 -2.5507104113128105
		 9 -1.8355023180601413 13 -2.5453463985648659 17 -3.2299027811631982 21 -2.5453463985648659
		 25 -1.7892691998741701 29 -2.5453463985648659 33 -3.3831616727896914;
	setAttr -s 9 ".kit[0:8]"  9 18 18 18 18 18 18 18 
		9;
	setAttr -s 9 ".kot[0:8]"  9 18 18 18 18 18 18 18 
		9;
createNode animCurveTA -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 2.88 17 -2.88 33 2.88;
	setAttr -s 3 ".kit[0:2]"  1 18 18;
	setAttr -s 3 ".kot[0:2]"  1 18 18;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -1.4400000592054472 9 -1.4954013063304537
		 25 -0.46038792418476787 33 -1.4400000592054472;
	setAttr -s 4 ".kit[0:3]"  1 18 18 18;
	setAttr -s 4 ".kot[0:3]"  1 18 18 18;
	setAttr -s 4 ".kix[0:3]"  1 1 1 1;
	setAttr -s 4 ".kiy[0:3]"  0 0 0 0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 13.444808004063752 5 9.8167153109126541
		 9 7.2801626172575986 13 13.053269707095597 17 17.792146439951679 21 14.639179527565112
		 25 8.5206715706206193 29 8.8642885534077767 33 13.444808004063752;
	setAttr -s 9 ".kit[2:8]"  18 1 18 18 1 9 9;
	setAttr -s 9 ".kot[2:8]"  18 1 18 18 1 9 9;
	setAttr -s 9 ".kix[3:8]"  0.69779336452484131 1 0.89239031076431274 
		0.86039847135543823 0.96577578783035278 0.8945499062538147;
	setAttr -s 9 ".kiy[3:8]"  0.71629911661148071 0 -0.45126438140869141 
		-0.50962191820144653 0.2593783438205719 0.44696804881095886;
	setAttr -s 9 ".kox[3:8]"  0.69779336452484131 1 0.89239037036895752 
		0.86039841175079346 0.96577578783035278 0.8945499062538147;
	setAttr -s 9 ".koy[3:8]"  0.71629911661148071 0 -0.45126441121101379 
		-0.50962203741073608 0.2593783438205719 0.44696804881095886;
createNode animCurveTA -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -3.3034280152266424 5 -0.83136623520579056
		 9 0.55290026450072738 17 -1.5081114084722762 25 -5.3236534971926313 29 -4.5829167569429021
		 33 -3.3034280152266424;
	setAttr -s 7 ".kit[2:6]"  1 1 1 9 9;
	setAttr -s 7 ".kot[2:6]"  1 1 1 9 9;
	setAttr -s 7 ".kix[2:6]"  1 0.3200000524520874 1 0.99398428201675415 
		0.99040001630783081;
	setAttr -s 7 ".kiy[2:6]"  0 -0.076923906803131104 0 0.10952334105968475 
		0.13823062181472778;
	setAttr -s 7 ".kox[2:6]"  1 0.3200000524520874 1 0.99398428201675415 
		0.99040001630783081;
	setAttr -s 7 ".koy[2:6]"  0 -0.076923921704292297 0 0.10952334105968475 
		0.13823062181472778;
createNode animCurveTA -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 3.7522415842757768 9 3.56519873061769
		 25 4.1489755985843502 33 3.7522415842757768;
	setAttr -s 4 ".kit[0:3]"  9 18 18 9;
	setAttr -s 4 ".kot[0:3]"  9 18 18 9;
createNode animCurveTL -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_wide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_thick";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_orbit";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_nod";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_side";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_twist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_neckStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_compensation";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0.16769909392025262 13 0 17 0
		 21 0 25 -0.17841323395200429 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 3.7430167064782145 5 -2.013051001803408
		 9 -7.1326226525899337 13 -10.414864932066521 25 6.2143248749920375 29 10.954415772548607
		 33 3.7430167064782145;
	setAttr -s 7 ".kit[0:6]"  9 18 18 18 1 18 9;
	setAttr -s 7 ".kot[0:6]"  9 18 18 18 1 18 9;
	setAttr -s 7 ".kix[4:6]"  0.76970702409744263 1 0.78596431016921997;
	setAttr -s 7 ".kiy[4:6]"  0.63839733600616455 0 -0.61827188730239868;
	setAttr -s 7 ".kox[4:6]"  0.76970702409744263 1 0.78596431016921997;
	setAttr -s 7 ".koy[4:6]"  0.63839727640151978 0 -0.61827188730239868;
createNode animCurveTA -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 3.3319139621625506 9 0.98642395776861214
		 17 -1.3307616178031196 25 0.98454247017432162 33 3.3319139621625506;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_wide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_thick";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTL -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -6.9955561142875871 9 -10.784265462572247
		 17 -6.0089160271586968 25 -10.784265419499745 33 -6.9955561142875871;
	setAttr -s 5 ".kix[0:4]"  1 0.3200000524520874 1 0.3200000524520874 
		1;
	setAttr -s 5 ".kiy[0:4]"  0 0.012915099039673805 0 -0.012915086001157761 
		0;
	setAttr -s 5 ".kox[0:4]"  1 0.31999996304512024 1 0.3200000524520874 
		1;
	setAttr -s 5 ".koy[0:4]"  0 0.01291508786380291 0 -0.012915100902318954 
		0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -0.90990290056691991 5 -0.90990290056691991
		 9 -0.90990290056691991 13 -0.90990290056691991 17 -0.90990290056691991 21 -0.90990290056691991
		 25 -0.90990290056691991 29 -0.90990290056691991 33 -0.90990290056691991;
createNode animCurveTL -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 33 0;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 33 0;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 33 0;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -3.7544516299264443 5 -2.7758798968444531
		 13 1.4974266959095139 17 2.5200001036095903 21 1.5390736593847962 29 -2.7322374222196917
		 33 -3.7544516299264443;
	setAttr -s 7 ".kit[0:6]"  1 18 18 18 18 18 18;
	setAttr -s 7 ".kot[0:6]"  1 18 18 18 18 18 18;
	setAttr -s 7 ".kix[0:6]"  1 0.98225045204162598 0.9819597601890564 
		1 0.98224806785583496 0.98197543621063232 1;
	setAttr -s 7 ".kiy[0:6]"  0 0.18757417798042297 0.18908973038196564 
		0 -0.18758656084537506 -0.18900863826274872 0;
	setAttr -s 7 ".kox[0:6]"  1 0.98225045204162598 0.9819597601890564 
		1 0.98224806785583496 0.98197543621063232 1;
	setAttr -s 7 ".koy[0:6]"  0 0.18757417798042297 0.18908973038196564 
		0 -0.18758656084537506 -0.18900863826274872 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 1.7354913552686182 5 1.5766608130939432
		 9 1.547968618199862 13 1.5047287293741158 21 1.8401244296838686 25 1.8702136545924795
		 29 1.8742417296940026 33 1.7354913552686182;
	setAttr -s 8 ".kit[0:7]"  1 18 1 18 18 3 18 1;
	setAttr -s 8 ".kot[0:7]"  1 18 1 18 18 3 18 1;
	setAttr -s 8 ".kix[0:7]"  1 0.99995583295822144 1 1 0.99995148181915283 
		1 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 -0.0093890838325023651 0 0 0.0098461965098977089 
		0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 0.99995595216751099 1 1 0.99995148181915283 
		1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 -0.0093890847638249397 0 0 0.0098461965098977089 
		0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -0.33331210587907417 5 -0.63896039458885745
		 9 0.38668475163125854 13 1.2899579184727399 17 0.4393613639070949 21 -0.42718804106723485
		 25 0.38094861686183318 29 1.2566939102929029 33 -0.33331210587907417;
	setAttr -s 9 ".kit[0:8]"  9 9 1 1 18 18 1 1 
		1;
	setAttr -s 9 ".kot[0:8]"  9 9 1 1 18 18 1 1 
		1;
	setAttr -s 9 ".kix[2:8]"  0.99056392908096313 0.99962723255157471 
		0.99564296007156372 1 0.99395978450775146 0.99934965372085571 0.99518758058547974;
	setAttr -s 9 ".kiy[2:8]"  0.13705149292945862 0.027301695197820663 
		-0.093247726559638977 0 0.10974561423063278 -0.036056756973266602 -0.09798826277256012;
	setAttr -s 9 ".kox[2:8]"  0.99056392908096313 0.99962723255157471 
		0.99564296007156372 1 0.99395978450775146 0.99934965372085571 0.99518758058547974;
	setAttr -s 9 ".koy[2:8]"  0.13705149292945862 0.027301687747240067 
		-0.093247726559638977 0 0.10974561423063278 -0.036056756973266602 -0.09798826277256012;
createNode animCurveTU -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 33 1;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 33 1;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 33 1;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 5.4484707031578976 5 5.4576079623788081
		 9 5.4484707031578976 13 5.4484707031578976 17 5.4484707031578976 21 5.4484707031578976
		 25 5.4534440694580733 29 5.4484707031578976 33 5.4484707031578976;
createNode animCurveTA -n "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1.1275925557962823 5 0.56477803337850607
		 9 0.63427081263540841 25 2.8759971980333754 33 1.1275925557962823;
	setAttr -s 5 ".kit[0:4]"  9 18 18 18 9;
	setAttr -s 5 ".kot[0:4]"  9 18 18 18 9;
createNode animCurveTA -n "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 9 1.1516430593421059 25 -0.42127582832542232
		 33 0;
createNode animCurveTL -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_wide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_thick";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -1.9714028018730632 5 -2.8136317108083695
		 9 -4.0375610611220543 13 -5.1543440843723545 17 -5.7757815758058051 21 -5.1909627325869314
		 25 -4.0009424129074755 29 -2.8136317108083664 33 -1.9714028018730632;
	setAttr -s 9 ".kit[8]"  3;
	setAttr -s 9 ".kot[8]"  3;
createNode animCurveTA -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTU -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTU -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTL -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 2.4651903290000001e-031;
createNode animCurveTA -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTU -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTU -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTL -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTU -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTU -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTL -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 2.4651903290000001e-031;
createNode animCurveTA -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTU -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTU -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
createNode animCurveTL -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 5.3884375039849237 9 5.2768921672488407
		 17 5.2323476158606672 21 5.2728916418942795 25 5.3687500624684983 29 5.4236085358749122
		 33 5.3884375039849237;
	setAttr -s 7 ".kit[0:6]"  1 9 9 18 9 18 1;
	setAttr -s 7 ".kot[0:6]"  1 9 9 18 9 18 1;
	setAttr -s 7 ".kix[0:6]"  0.97668153047561646 0.97152304649353027 
		0.99996531009674072 0.91991394758224487 0.90467852354049683 1 0.97668153047561646;
	setAttr -s 7 ".kiy[0:6]"  -0.21469299495220184 -0.23694519698619843 
		-0.0083341393619775772 0.39212039113044739 0.42609480023384094 0 -0.21469299495220184;
	setAttr -s 7 ".kox[0:6]"  0.97668153047561646 0.97152304649353027 
		0.99996531009674072 0.9199138879776001 0.90467852354049683 1 0.97668153047561646;
	setAttr -s 7 ".koy[0:6]"  -0.21469299495220184 -0.23694519698619843 
		-0.0083341393619775772 0.392120361328125 0.42609480023384094 0 -0.21469299495220184;
createNode animCurveTL -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.019194205050613852 9 -0.10627883256133305
		 17 -0.020122590502903479 25 -0.10708636717352205 33 -0.019194205050613852;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 1;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 1;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 3.724905494998664 9 3.7302944003990208
		 17 3.723475652746159 25 3.7304263411615475 33 3.724905494998664;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 1;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 1;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 15.930736187693636 5 18.312816814901446
		 9 15.930736187693636 13 18.492770080835136 17 15.815037077609496 21 18.430641519851552
		 29 16.748834349416658 33 15.930736187693636;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 18 18 18 1;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 1;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 1 0.99589407444000244 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 -0.090525887906551361 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 1 0.99589413404464722 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 -0.090525887906551361 0;
createNode animCurveTA -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -28.488900732413182 9 -28.488900732413182
		 17 -26.459975985352035 21 -26.306060417382088 33 -28.488900732413182;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 1;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 1;
	setAttr -s 5 ".kix[0:4]"  1 1 0.99873387813568115 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0.050304986536502838 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 0.99873387813568115 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0.050304990261793137 0 0;
createNode animCurveTA -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 177.41288469407277 9 177.41288469407277
		 17 177.28348470163243 21 177.36275807359698 33 177.41288469407277;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 1;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 1;
	setAttr -s 5 ".kix[0:4]"  1 1 1 0.99999374151229858 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0.0035288152284920216 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 0.99999380111694336 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0.0035288152284920216 0;
createNode animCurveTU -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_uprarmStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 9 0 17 0 33 0;
	setAttr -s 4 ".kit[0:3]"  1 18 18 1;
	setAttr -s 4 ".kot[0:3]"  1 18 18 1;
	setAttr -s 4 ".kix[0:3]"  1 1 1 1;
	setAttr -s 4 ".kiy[0:3]"  0 0 0 0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_forearmStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 9 0 17 0 33 0;
	setAttr -s 4 ".kit[0:3]"  1 18 18 1;
	setAttr -s 4 ".kot[0:3]"  1 18 18 1;
	setAttr -s 4 ".kix[0:3]"  1 1 1 1;
	setAttr -s 4 ".kiy[0:3]"  0 0 0 0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 9 0 17 0 33 0;
	setAttr -s 4 ".kit[0:3]"  1 18 18 1;
	setAttr -s 4 ".kot[0:3]"  1 18 18 1;
	setAttr -s 4 ".kix[0:3]"  1 1 1 1;
	setAttr -s 4 ".kiy[0:3]"  0 0 0 0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_elbowTwist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 70 9 70 17 70 33 70;
	setAttr -s 4 ".kit[0:3]"  1 18 18 1;
	setAttr -s 4 ".kot[0:3]"  1 18 18 1;
	setAttr -s 4 ".kix[0:3]"  1 1 1 1;
	setAttr -s 4 ".kiy[0:3]"  0 0 0 0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTL -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -9.965483 9 -8.8926586494998716 17 -9.965483
		 25 -8.8926586494998716 33 -9.965483;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -23.037399 9 -28.518340833634863 17 -23.037399
		 25 -28.518340833634863 33 -23.037399;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 10.832392 9 11.725723978744869 17 10.832392
		 25 11.725723978744869 33 10.832392;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 1.7038996424677977 17 0 25 1.7038996424677977
		 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 20.346534 9 20.670843256646894 17 20.346534
		 25 20.670843256646894 33 20.346534;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -45.124291 9 -36.711862684973426 17 -45.124291
		 25 -36.711862684973426 33 -45.124291;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -3.7797989999999997 9 -0.62933801277243739
		 17 -3.7797989999999997 25 -0.62933801277243739 33 -3.7797989999999997;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -5.283565 9 -5.6869248315484233 17 -5.283565
		 25 -5.6869248315484233 33 -5.283565;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -24.844699 9 -28.338945812730483 17 -24.844699
		 25 -28.338945812730483 33 -24.844699;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -6.793381 9 -6.4599694182166028 17 -6.793381
		 25 -6.4599694182166028 33 -6.793381;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 1.454060385744113 17 0 25 1.454060385744113
		 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 13.356869 9 13.490112513601584 17 13.356869
		 25 13.490112513601584 33 13.356869;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -55.686955 9 -46.955478754617822 17 -55.686955
		 25 -46.955478754617822 33 -55.686955;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -1.916453 9 0.17137722323600246 17 -1.916453
		 25 0.17137722323600246 33 -1.916453;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -19.303798 9 -19.763089003386735 17 -19.303798
		 25 -19.763089003386735 33 -19.303798;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -25.876552 9 -27.65558389744146 17 -25.876552
		 25 -27.65558389744146 33 -25.876552;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -15.264991999999998 9 -14.655175512673075
		 17 -15.264991999999998 25 -14.655175512673075 33 -15.264991999999998;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 -1.0257000926969486 17 0 25 -1.0257000926969486
		 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 3.7676139606318864 17 0 25 3.7676139606318864
		 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0.50437912844297139 17 0 25 0.50437912844297139
		 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 4.389862 9 5.2726703743171282 17 4.389862
		 25 5.2726703743171282 33 4.389862;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -45.324833 9 -36.337252197677664 17 -45.324833
		 25 -36.337252197677664 33 -45.324833;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -6.00415 9 -5.2466013430911653 17 -6.00415
		 25 -5.2466013430911653 33 -6.00415;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
createNode animCurveTA -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 23.021074 9 24.966765968304813 17 23.021074
		 25 24.133163261941672 33 23.021074;
createNode animCurveTA -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -5.745265 9 -4.0762666605235092 17 -5.745265
		 25 -4.3751966710517802 33 -5.745265;
createNode animCurveTA -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -6.519954 9 -4.987431327949178 17 -6.519954
		 25 -3.6440953422548517 33 -6.519954;
createNode animCurveTU -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
createNode animCurveTU -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
createNode animCurveTU -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
createNode animCurveTL -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -12.988475000000001 9 -13.81928410008995
		 17 -12.988475000000001 25 -13.81928410008995 33 -12.988475000000001;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 15.455663 9 12.130052271765889 17 15.455663
		 25 12.130052271765889 33 15.455663;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -14.846536 9 -14.078918946506681 17 -14.846536
		 25 -14.078918946506681 33 -14.846536;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 9 0 17 0 25 0 33 0;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 7.1765560000000006 9 3.008830490295086
		 17 7.1765560000000006 25 0.96886042162021158 33 7.1765560000000006;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 12.048683 9 8.068927356470736 17 12.048683
		 25 2.3854971120553325 33 12.048683;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -20.251916 9 -20.926713896358571 17 -20.251916
		 25 -21.111095089281026 33 -20.251916;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 9 1 17 1 25 1 33 1;
	setAttr -s 5 ".kit[3:4]"  1 18;
	setAttr -s 5 ".kot[3:4]"  1 18;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[3:4]"  1 1;
	setAttr -s 5 ".koy[3:4]"  0 0;
createNode animCurveTL -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_crossEyeFix";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_crossEyeRate";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.5 5 0.5 9 0.5 13 0.5 17 0.5 21 0.5 25 0.5
		 29 0.5 33 0.5;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_Iris_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_Pupil_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0.37448559556786692 5 0.37448559556786692
		 9 0.37448559556786692 13 0.33270085213307621 17 0.27909031753899982 21 0.33760366241927742
		 29 0.37448559556786692 33 0.37448559556786692;
	setAttr -s 8 ".kit[5:7]"  1 18 18;
	setAttr -s 8 ".kot[5:7]"  1 18 18;
	setAttr -s 8 ".kix[5:7]"  0.92373055219650269 1 1;
	setAttr -s 8 ".kiy[5:7]"  0.3830428421497345 0 0;
	setAttr -s 8 ".kox[5:7]"  0.92373067140579224 1 1;
	setAttr -s 8 ".koy[5:7]"  0.38304269313812256 0 0;
createNode animCurveTL -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1.3338451859217482 13 -2.6454997026308322
		 17 -3.5472821369023522 29 -0.067527890693139137 33 1.3338451859217482;
	setAttr -s 5 ".kit[0:4]"  9 1 3 1 9;
	setAttr -s 5 ".kot[0:4]"  9 1 3 1 9;
	setAttr -s 5 ".kix[1:4]"  0.12852658331394196 1 0.10619177669286728 
		0.11343683302402496;
	setAttr -s 5 ".kiy[1:4]"  -0.99170607328414917 0 0.99434572458267212 
		0.99354517459869385;
	setAttr -s 5 ".kox[1:4]"  0.12852658331394196 1 0.10619177669286728 
		0.11343683302402496;
	setAttr -s 5 ".koy[1:4]"  -0.99170607328414917 0 0.99434566497802734 
		0.99354517459869385;
createNode animCurveTA -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -17.258833266631726 5 0 9 0 13 0 17 0
		 21 0 25 0 29 -6.4793980568070539 33 -17.258833266631726;
createNode animCurveTA -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0.801 21 1.9000000000000001
		 25 0.9468816842105261 29 0.1681515789473691 33 0;
	setAttr -s 9 ".kit[6:8]"  1 18 18;
	setAttr -s 9 ".kot[6:8]"  1 18 18;
	setAttr -s 9 ".kix[6:8]"  0.1283513605594635 0.3201625645160675 1;
	setAttr -s 9 ".kiy[6:8]"  -0.99172878265380859 -0.94736260175704956 
		0;
	setAttr -s 9 ".kox[6:8]"  0.12835134565830231 0.32016259431838989 
		1;
	setAttr -s 9 ".koy[6:8]"  -0.99172878265380859 -0.94736260175704956 
		0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 36.987656428027066 17 56.513702261754048
		 21 53.239204030659181 25 35.420087163354211 29 7.6923285194972078 33 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -5 5 -2.5000001164153209 9 0 13 0 17 0
		 21 0 25 0 29 -2.4999986030163668 33 -5;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footSide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTL -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -0.041993683149036891 5 -0.0017484992919791758
		 9 0 13 0 17 0 21 0 25 0 29 -0.020996829841620837 33 -0.041993683149036891;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 0.99946302175521851 1 1 1 1 1 0.99149894714355469 
		1;
	setAttr -s 9 ".kiy[0:8]"  0 0.032766755670309067 0 0 0 0 0 -0.13011464476585388 
		0;
	setAttr -s 9 ".kox[0:8]"  1 0.99946302175521851 1 1 1 1 1 0.99149894714355469 
		1;
	setAttr -s 9 ".koy[0:8]"  0 0.032766755670309067 0 0 0 0 0 -0.13011464476585388 
		0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.32679917939198777 5 0.70116406264244979
		 9 0 13 0 17 0 21 0 25 0 29 0.1633994983893729 33 0.32679917939198777;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 0.69963502883911133 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0.71450042724609375 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 0.69963502883911133 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0.71450036764144897 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1.8700975999528717 5 1.2794546604212502
		 9 0 13 0 17 0 21 0 25 0 29 0.93504827747728814 33 1.8700975999528717;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 0.1686626672744751 1 1 1 1 1 0.1686626672744751 
		1;
	setAttr -s 9 ".kiy[0:8]"  0 -0.98567378520965576 0 0 0 0 0 0.98567378520965576 
		0;
	setAttr -s 9 ".kox[0:8]"  1 0.1686626672744751 1 1 1 1 1 0.1686626672744751 
		1;
	setAttr -s 9 ".koy[0:8]"  0 -0.98567384481430054 0 0 0 0 0 0.98567378520965576 
		0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 -0.67318417398760733 17 -1.3840591312279851
		 21 -0.56950541693286261 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0.28501338504460882 17 0.4689460279613315
		 21 0.80727982129248677 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 1.2764588774970294 17 2.262707441952633
		 21 1.6737054648004794 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 8.8817841970012523e-016 5 0 9 0 13 0 17 0
		 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 2.7755575615628914e-017 5 0 9 0 13 0 17 0
		 21 0 25 0 29 0 33 0;
createNode animCurveTL -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 -2.7755575620000002e-016;
createNode animCurveTL -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 -0.23682148550000001;
createNode animCurveTL -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 -0.32291556739999999;
createNode animCurveTA -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTA -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
	setAttr -s 9 ".kot[0:8]"  5 5 5 5 5 5 5 5 
		5;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_globalScale";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_bodyRes";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_ribbonCtrl_grp";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_hairCtrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_clothCtrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTA -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 11.263577383043829 5 6.650568152316608
		 9 13.857424203629867 13 19.51870746186178 17 15.910426486855656 21 7.5184754848758697
		 25 0.80095809841776744 29 5.4966049956663943 33 11.263577383043829;
	setAttr -s 9 ".kit[0:8]"  9 18 9 18 18 1 9 18 
		9;
	setAttr -s 9 ".kot[0:8]"  9 18 9 18 18 1 9 18 
		9;
	setAttr -s 9 ".kix[5:8]"  0.79777967929840088 0.99397450685501099 
		0.86853528022766113 0.84644299745559692;
	setAttr -s 9 ".kiy[5:8]"  -0.60294902324676514 -0.10961146652698517 
		0.49562728404998779 0.53247934579849243;
	setAttr -s 9 ".kox[5:8]"  0.79777967929840088 0.99397450685501099 
		0.86853528022766113 0.84644299745559692;
	setAttr -s 9 ".koy[5:8]"  -0.60294902324676514 -0.10961146652698517 
		0.49562728404998779 0.53247934579849243;
createNode animCurveTA -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -1.2976772372595378 5 -1.1745935295530927
		 9 -1.3407297144169459 13 -1.5763603311392831 17 -3.7596950268475542 21 -2.2702387097247869
		 25 -1.8896003509863812 29 -1.26579184991286 33 -1.2976772372595378;
createNode animCurveTA -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -10.905855008574376 5 -15.621653411119429
		 9 -13.935114020415524 13 -7.8059881509255149 17 0.29005743871420325 21 2.4370756052855116
		 25 -5.5380819784699264 29 -13.819247464359023 33 -10.905855008574376;
	setAttr -s 9 ".kit[0:8]"  9 18 18 18 1 1 18 18 
		9;
	setAttr -s 9 ".kot[0:8]"  9 18 18 18 1 1 18 18 
		9;
	setAttr -s 9 ".kix[4:8]"  0.78412669897079468 0.83153194189071655 
		0.74824243783950806 1 0.95303040742874146;
	setAttr -s 9 ".kiy[4:8]"  0.62060087919235229 -0.55547702312469482 
		-0.66342532634735107 0 0.30287462472915649;
	setAttr -s 9 ".kox[4:8]"  0.7841266393661499 0.83153188228607178 
		0.74824243783950806 1 0.95303040742874146;
	setAttr -s 9 ".koy[4:8]"  0.62060087919235229 -0.5554770827293396 
		-0.66342532634735107 0 0.30287462472915649;
createNode animCurveTU -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.5 5 0.5 9 0.5 13 0.5 17 0.5 21 0.5 25 0.5
		 29 0.5 33 0.5;
createNode animCurveTA -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 20.299250345905993 5 28.215135891562173
		 17 10.412805477882802 25 5.4063785582016068 33 20.299250345905993;
	setAttr -s 5 ".kit[1:4]"  3 1 18 9;
	setAttr -s 5 ".kot[1:4]"  3 1 18 9;
	setAttr -s 5 ".kix[2:4]"  0.85136747360229492 1 0.77619755268096924;
	setAttr -s 5 ".kiy[2:4]"  -0.52456974983215332 0 0.6304897665977478;
	setAttr -s 5 ".kox[2:4]"  0.8513675332069397 1 0.77619755268096924;
	setAttr -s 5 ".koy[2:4]"  -0.52456974983215332 0 0.6304897665977478;
createNode animCurveTA -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 29.404085525811347 17 24.463583227996818
		 33 29.404085525811347;
	setAttr -s 3 ".kit[2]"  1;
	setAttr -s 3 ".kot[2]"  1;
	setAttr -s 3 ".kix[2]"  1;
	setAttr -s 3 ".kiy[2]"  0;
	setAttr -s 3 ".kox[2]"  1;
	setAttr -s 3 ".koy[2]"  0;
createNode animCurveTA -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -12.494502779291107 17 8.1258531264233298
		 33 -12.494502779291107;
	setAttr -s 3 ".kit[2]"  1;
	setAttr -s 3 ".kot[2]"  1;
	setAttr -s 3 ".kix[2]"  1;
	setAttr -s 3 ".kiy[2]"  0;
	setAttr -s 3 ".kox[2]"  1;
	setAttr -s 3 ".koy[2]"  0;
createNode animCurveTU -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 17 1 33 1;
	setAttr -s 3 ".kit[2]"  1;
	setAttr -s 3 ".kot[2]"  1;
	setAttr -s 3 ".kix[2]"  1;
	setAttr -s 3 ".kiy[2]"  0;
	setAttr -s 3 ".kox[2]"  1;
	setAttr -s 3 ".koy[2]"  0;
createNode animCurveTU -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 17 0 33 0;
	setAttr -s 3 ".kit[2]"  1;
	setAttr -s 3 ".kot[2]"  1;
	setAttr -s 3 ".kix[2]"  1;
	setAttr -s 3 ".kiy[2]"  0;
	setAttr -s 3 ".kox[2]"  1;
	setAttr -s 3 ".koy[2]"  0;
createNode animCurveTU -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_compensation";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 17 1 33 1;
	setAttr -s 3 ".kit[2]"  1;
	setAttr -s 3 ".kot[2]"  1;
	setAttr -s 3 ".kix[2]"  1;
	setAttr -s 3 ".kiy[2]"  0;
	setAttr -s 3 ".kox[2]"  1;
	setAttr -s 3 ".koy[2]"  0;
createNode animCurveTA -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -29.164051219249846 5 -8.3594209098098595
		 9 -7.9634031938512662 13 -7.3652164042578194 17 -6.9945142148694286 21 -7.3168032663937161
		 25 -7.8052489916874519 29 -8.2603356375188177 33 -29.164051219249846;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTA -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 31.93251473459139 5 30.289510619562677
		 9 30.117452059522265 13 30.237686934551746 17 30.455545267751305 21 30.9542527857379
		 25 30.89844017586185 29 30.063915547916437 33 31.93251473459139;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTA -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 13.367530431039494 5 1.9344115041370813
		 9 0.050977583143847705 13 0.081616561317362585 17 0.29608931093406243 21 4.6702744721925349
		 25 5.2657373861248491 29 4.6913133503816846 33 13.367530431039494;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 5 0 9 0 13 0 17 0 21 0 25 0 29 0 33 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_compensation";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTA -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.97518236670197411 5 1.5180568962864964
		 9 2.6459158129045557 13 4.49523661462809 17 5.655056955611597 21 4.8853719748557332
		 25 3.3398827443293477 29 1.78461148270794 33 0.97518236670197411;
createNode animCurveTA -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.90218842177802949 5 0.73562000027241126
		 9 0.56905156325389916 13 0.97560514635377527 17 1.3821585780006547 21 1.5985221678290111
		 25 1.2263286626957162 29 0.73399168155535777 33 0.90218842177802949;
createNode animCurveTA -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -12.279657241035416 5 -8.4470803840697908
		 9 -4.6145031701676187 13 -12.587315512591012 17 -20.56012488491066 21 -22.611711307727646
		 25 -17.803278994597967 29 -5.6780938008418786 33 -12.279657241035416;
createNode animCurveTU -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 5 1 9 1 13 1 17 1 21 1 25 1 29 1 33 1;
createNode animCurveTU -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.5 5 0.5 9 0.5 13 0.5 17 0.5 21 0.5 25 0.5
		 29 0.5 33 0.5;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr ".unw" 1;
lockNode -l 1 ;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 50 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
lockNode -l 1 ;
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 13 ".dsm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -s 9 ".gn";
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -cb on ".mica";
	setAttr -cb on ".micw";
	setAttr -cb on ".mirw";
lockNode -l 1 ;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -cb on ".mica";
	setAttr -av -cb on ".micw";
	setAttr -cb on ".mirw";
lockNode -l 1 ;
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 50 ".s";
select -ne :defaultTextureList1;
	setAttr -s 88 ".tx";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 337 ".u";
select -ne :defaultRenderingList1;
	setAttr -s 3 ".r";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".macc";
	setAttr -k on ".macd";
	setAttr -k on ".macq";
	setAttr -k on ".mcfr" 25;
	setAttr -cb on ".ifg";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr -k on ".edl";
	setAttr -cb on ".ren";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -cb on ".imfkey";
	setAttr -k on ".gama";
	setAttr -k on ".an";
	setAttr -cb on ".ar";
	setAttr -k on ".fs";
	setAttr -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -k on ".be";
	setAttr -cb on ".ep";
	setAttr -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -k on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -k on ".pff";
	setAttr -cb on ".peie";
	setAttr -k on ".ifp";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -k on ".afp";
	setAttr -k on ".pfb";
	setAttr -k on ".pram" -type "string" "";
	setAttr -k on ".poam";
	setAttr -k on ".prlm";
	setAttr -k on ".polm";
	setAttr -cb on ".prm";
	setAttr -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -k on ".ubc";
	setAttr -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -k on ".udbx";
	setAttr -k on ".smc";
	setAttr -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -k on ".ope";
	setAttr -k on ".oppf";
	setAttr -cb on ".hbl";
select -ne :defaultLightSet;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultObjectSet;
	setAttr ".ro" yes;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k off ".ctrs" 256;
	setAttr -av -k off ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr" 25;
select -ne :defaultHardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".rp";
	setAttr -k on ".cai";
	setAttr -k on ".coi";
	setAttr -cb on ".bc";
	setAttr -av -k on ".bcb";
	setAttr -av -k on ".bcg";
	setAttr -av -k on ".bcr";
	setAttr -k on ".ei";
	setAttr -k on ".ex";
	setAttr -av -k on ".es";
	setAttr -av -k on ".ef";
	setAttr -av -k on ".bf";
	setAttr -k on ".fii";
	setAttr -av -k on ".sf";
	setAttr -k on ".gr";
	setAttr -k on ".li";
	setAttr -k on ".ls";
	setAttr -k on ".mb";
	setAttr -k on ".ti";
	setAttr -k on ".txt";
	setAttr -k on ".mpr";
	setAttr -k on ".wzd";
	setAttr -k on ".fn" -type "string" "im";
	setAttr -k on ".if";
	setAttr -k on ".res" -type "string" "ntsc_4d 646 485 1.333";
	setAttr -k on ".as";
	setAttr -k on ".ds";
	setAttr -k on ".lm";
	setAttr -k on ".fir";
	setAttr -k on ".aap";
	setAttr -k on ".gh";
	setAttr -cb on ".sd";
select -ne :characterPartition;
	setAttr -s 16 ".st";
select -ne :ikSystem;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".gsn";
	setAttr -k on ".gsv";
	setAttr -s 8 ".sol";
connectAttr "ylva_original:hair_ex_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:hair_ex_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:hair_ex_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:hair_ex_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:hair_ex_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:hair_ex_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:hair_ex_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:hair_ex_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:hair_ex_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:hair_ex_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:hair_ex_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:hair_ex_ctrl_outPutAnimBank_1_subCtrl.o" "ylva_original:hair_ex_ctrl_outPutAnimBank_1.subCtrl"
		;
connectAttr "ylva_original:head_squash_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:head_squash_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:head_squash_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:head_squash_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:head_squash_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_eye_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_eye_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_eye_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_eye_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_eye_ctrl_outPutAnimBank_1_crossEyeFix.o" "ylva_original:l_eye_ctrl_outPutAnimBank_1.crossEyeFix"
		;
connectAttr "ylva_original:l_eye_ctrl_outPutAnimBank_1_crossEyeRate.o" "ylva_original:l_eye_ctrl_outPutAnimBank_1.crossEyeRate"
		;
connectAttr "ylva_original:l_eye_ctrl_outPutAnimBank_1_Iris_Size.o" "ylva_original:l_eye_ctrl_outPutAnimBank_1.Iris_Size"
		;
connectAttr "ylva_original:l_eye_ctrl_outPutAnimBank_1_Pupil_Size.o" "ylva_original:l_eye_ctrl_outPutAnimBank_1.Pupil_Size"
		;
connectAttr "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK.o" "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1.FK_2_IK"
		;
connectAttr "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK.o" "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1.globalIK_2_localIK"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.footHeight"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.footRoll"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.toeBend"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.heelTurn"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.toeTurn"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footSide.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.footSide"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.thighStretch"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.shankStretch"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.autoStretch"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.preferredAngle"
		;
connectAttr "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist.o" "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.kneeTwist"
		;
connectAttr "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot.o" "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.followBody_2_followFoot"
		;
connectAttr "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_followBody.o" "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1.followBody"
		;
connectAttr "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_bothEye_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_bothEye_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_bothEye_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_bothEye_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_l_eye_offset.o" "ylva_original:m_bothEye_ctrl_outPutAnimBank_1.l_eye_offset"
		;
connectAttr "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_r_eye_offset.o" "ylva_original:m_bothEye_ctrl_outPutAnimBank_1.r_eye_offset"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_tx.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.l_eyePSD_tx"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_sc.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.l_eyePSD_sc"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_bothEye_offset.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.bothEye_offset"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_irisSize_temp.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.irisSize_temp"
		;
connectAttr "ylva_original:m_eye_ctrl_outPutAnimBank_1_pupilSize_temp.o" "ylva_original:m_eye_ctrl_outPutAnimBank_1.pupilSize_temp"
		;
connectAttr "ylva_original:m_jaw_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:m_jaw_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_jaw_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_jaw_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_jaw_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_jaw_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_jaw_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_jaw_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_jaw_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_jaw_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:m_jaw_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotatePivotY.o" "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1.rpy"
		;
connectAttr "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_wide.o" "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1.wide"
		;
connectAttr "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_thick.o" "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1.thick"
		;
connectAttr "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_orbit.o" "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1.orbit"
		;
connectAttr "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_nod.o" "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1.nod"
		;
connectAttr "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_side.o" "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1.side"
		;
connectAttr "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_twist.o" "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1.twist"
		;
connectAttr "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_neckStretch.o" "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1.neckStretch"
		;
connectAttr "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_compensation.o" "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1.compensation"
		;
connectAttr "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotatePivotY.o" "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1.rpy"
		;
connectAttr "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_wide.o" "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1.wide"
		;
connectAttr "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_thick.o" "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1.thick"
		;
connectAttr "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_autoStretch.o" "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1.autoStretch"
		;
connectAttr "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_wide.o" "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.wide"
		;
connectAttr "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_thick.o" "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.thick"
		;
connectAttr "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotatePivotY.o" "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1.rpy"
		;
connectAttr "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_uprarmStretch.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.uprarmStretch"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_forearmStretch.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.forearmStretch"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_autoStretch.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.autoStretch"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_elbowTwist.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.elbowTwist"
		;
connectAttr "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_eye_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_eye_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_eye_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_eye_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_eye_ctrl_outPutAnimBank_1_crossEyeFix.o" "ylva_original:r_eye_ctrl_outPutAnimBank_1.crossEyeFix"
		;
connectAttr "ylva_original:r_eye_ctrl_outPutAnimBank_1_crossEyeRate.o" "ylva_original:r_eye_ctrl_outPutAnimBank_1.crossEyeRate"
		;
connectAttr "ylva_original:r_eye_ctrl_outPutAnimBank_1_Iris_Size.o" "ylva_original:r_eye_ctrl_outPutAnimBank_1.Iris_Size"
		;
connectAttr "ylva_original:r_eye_ctrl_outPutAnimBank_1_Pupil_Size.o" "ylva_original:r_eye_ctrl_outPutAnimBank_1.Pupil_Size"
		;
connectAttr "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK.o" "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1.FK_2_IK"
		;
connectAttr "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK.o" "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1.globalIK_2_localIK"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.footHeight"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.footRoll"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.toeBend"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.heelTurn"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.toeTurn"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footSide.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.footSide"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.thighStretch"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.shankStretch"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.autoStretch"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.preferredAngle"
		;
connectAttr "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist.o" "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.kneeTwist"
		;
connectAttr "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot.o" "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1.followBody_2_followFoot"
		;
connectAttr "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:tongueCon_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:tongueCon_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:tongueCon_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:tongueCon_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:tongueCon_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:tongueCon_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:top_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_globalScale.o" "ylva_original:top_ctrl_outPutAnimBank_1.globalScale"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_bodyRes.o" "ylva_original:top_ctrl_outPutAnimBank_1.bodyRes"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_ribbonCtrl_grp.o" "ylva_original:top_ctrl_outPutAnimBank_1.ribbonCtrl_grp"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_hairCtrl.o" "ylva_original:top_ctrl_outPutAnimBank_1.hairCtrl"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_clothCtrl.o" "ylva_original:top_ctrl_outPutAnimBank_1.clothCtrl"
		;
connectAttr "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_twistBlend.o" "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1.twistBlend"
		;
connectAttr "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_twistBlend.o" "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.twistBlend"
		;
connectAttr "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_compensation.o" "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.compensation"
		;
connectAttr "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_twistBlend.o" "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.twistBlend"
		;
connectAttr "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_compensation.o" "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.compensation"
		;
connectAttr "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_twistBlend.o" "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1.twistBlend"
		;
// End of yl_walk.ma

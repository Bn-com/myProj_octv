//Maya ASCII 2012 scene
//Name: vk_walk.ma
//Last modified: Mon, Sep 03, 2012 02:14:15 PM
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
	setAttr ".ns" -type "string" "vicky_original";
	setAttr ".range" -type "string" "\"100:117\"";
	setAttr ".num" 87;
	setAttr ".nts" -type "string" (
		"vicky_original:m_spineA_waistFree_ctrl; vicky_original:m_spineA_chest_ctrl; vicky_original:m_spineA_waist_ctrl; vicky_original:m_spineA_hip_ctrl; vicky_original:m_spineA_torso_ctrl; vicky_original:m_spineA_body_ctrl; vicky_original:l_legA_heel_IK_ctrl; vicky_original:l_legA_knee_IK_ctrl; vicky_original:l_legA_foot_IK_ctrl; vicky_original:r_legA_heel_IK_ctrl; vicky_original:r_legA_knee_IK_ctrl; vicky_original:r_legA_foot_IK_ctrl; vicky_original:l_legA_pelvis_ctrl; vicky_original:r_legA_pelvis_ctrl; vicky_original:l_armA_shoulder_ctrl; vicky_original:r_armA_shoulder_ctrl; vicky_original:m_armA_shoulder_ctrl; vicky_original:l_armA_thumb_03_ctrl; vicky_original:l_armA_thumb_02_ctrl; vicky_original:l_armA_thumb_01_ctrl; vicky_original:l_armA_index_04_ctrl; vicky_original:l_armA_index_03_ctrl; vicky_original:l_armA_index_02_ctrl; vicky_original:l_armA_index_01_ctrl; vicky_original:l_armA_middle_04_ctrl; vicky_original:l_armA_middle_03_ctrl; vicky_original:l_armA_middle_02_ctrl; vicky_original:l_armA_middle_01_ctrl; vicky_original:l_armA_ring_04_ctrl; vicky_original:l_armA_ring_03_ctrl; vicky_original:l_armA_ring_02_ctrl; vicky_original:l_armA_ring_01_ctrl; vicky_original:l_armA_wrist_ctrl; vicky_original:r_armA_thumb_03_ctrl; vicky_original:r_armA_thumb_02_ctrl; vicky_original:r_armA_thumb_01_ctrl; vicky_original:r_armA_index_04_ctrl; vicky_original:r_armA_index_03_ctrl; vicky_original:r_armA_index_02_ctrl; vicky_original:r_armA_index_01_ctrl; vicky_original:r_armA_middle_04_ctrl; vicky_original:r_armA_middle_03_ctrl; vicky_original:r_armA_middle_02_ctrl; vicky_original:r_armA_middle_01_ctrl; vicky_original:r_armA_ring_04_ctrl; vicky_original:r_armA_ring_03_ctrl; vicky_original:r_armA_ring_02_ctrl; vicky_original:r_armA_ring_01_ctrl; vicky_original:r_armA_wrist_ctrl; vicky_original:m_spineA_head_ctrl; vicky_original:m_spineA_neck_03_ctrl; vicky_original:m_spineA_neck_02_ctrl; vicky_original:m_spineA_neck_01_ctrl; vicky_original:l_armA_elbow_FK_ctrl; vicky_original:l_armA_uprarm_FK_ctrl; vicky_original:r_armA_elbow_FK_ctrl; vicky_original:r_armA_uprarm_FK_ctrl; vicky_original:l_legA_ankle_ctrl; vicky_original:r_legA_ankle_ctrl; vicky_original:l_hornLong_ctrl; vicky_original:r_hornLong_ctrl; vicky_original:m_helmet_ctrl; vicky_original:l_hair_ex_ctrl; vicky_original:m_hair_ex_ctrl; vicky_original:r_hair_ex_ctrl; vicky_original:r_foreHair_ex_ctrl; vicky_original:l_foreHair_ex_ctrl; vicky_original:hair_ex_ctrl; vicky_original:mov_ctrl; vicky_original:top_ctrl; vicky_original:tongoueA_Rot_Ctrl; vicky_original:tongoueB_Rot_Ctrl; vicky_original:tongoueC_Rot_Ctrl; vicky_original:tongueIn1_Ctrl; vicky_original:m_tongueTip_Ctrl; vicky_original:m_tongue_subC_Ctrl; vicky_original:m_tongue_subB_Ctrl; vicky_original:m_tongue_subA_Ctrl; vicky_original:tongueCon_ctrl; vicky_original:tongueCurve; vicky_original:m_jaw_ctrl; vicky_original:l_pupilRadz_end; vicky_original:l_eye_ctrl; vicky_original:r_eye_ctrl; vicky_original:m_bothEye_ctrl; vicky_original:m_eye_ctrl; vicky_original:head_squash_ctrl; ");
createNode transform -n "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1" 
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
	setAttr ".ObjName" -type "string" "vicky_original:m_spineA_waistFree_ctrl";
createNode locator -n "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:m_spineA_chest_ctrl";
createNode locator -n "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".rpy";
	setAttr ".ObjName" -type "string" "vicky_original:m_spineA_waist_ctrl";
createNode locator -n "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:m_spineA_hip_ctrl";
createNode locator -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:m_spineA_torso_ctrl";
createNode locator -n "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:m_spineA_body_ctrl";
createNode locator -n "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:l_legA_heel_IK_ctrl";
createNode locator -n "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:l_legA_knee_IK_ctrl";
createNode locator -n "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:l_legA_foot_IK_ctrl";
createNode locator -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:r_legA_heel_IK_ctrl";
createNode locator -n "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:r_legA_knee_IK_ctrl";
createNode locator -n "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:r_legA_foot_IK_ctrl";
createNode locator -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:l_legA_pelvis_ctrl";
createNode locator -n "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:r_legA_pelvis_ctrl";
createNode locator -n "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_shoulder_ctrl";
createNode locator -n "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_shoulder_ctrl";
createNode locator -n "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "followBody" -ln "followBody" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".followBody";
	setAttr ".ObjName" -type "string" "vicky_original:m_armA_shoulder_ctrl";
createNode locator -n "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_thumb_03_ctrl";
createNode locator -n "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_thumb_02_ctrl";
createNode locator -n "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_thumb_01_ctrl";
createNode locator -n "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_index_04_ctrl";
createNode locator -n "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_index_03_ctrl";
createNode locator -n "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_index_02_ctrl";
createNode locator -n "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_index_01_ctrl";
createNode locator -n "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_middle_04_ctrl";
createNode locator -n "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_middle_03_ctrl";
createNode locator -n "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_middle_02_ctrl";
createNode locator -n "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_middle_01_ctrl";
createNode locator -n "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_ring_04_ctrl";
createNode locator -n "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_ring_03_ctrl";
createNode locator -n "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_ring_02_ctrl";
createNode locator -n "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_ring_01_ctrl";
createNode locator -n "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "keepOrientation" -ln "keepOrientation" -at "double";
	addAttr -ci true -sn "FK_2_IK" -ln "FK_2_IK" -at "double";
	addAttr -ci true -sn "globalIK_2_localIK" -ln "globalIK_2_localIK" -at "double";
	addAttr -ci true -sn "neutral" -ln "neutral" -at "double";
	addAttr -ci true -sn "fist" -ln "fist" -at "double";
	addAttr -ci true -sn "relax" -ln "relax" -at "double";
	addAttr -ci true -sn "curl" -ln "curl" -at "double";
	addAttr -ci true -sn "spread" -ln "spread" -at "double";
	addAttr -ci true -sn "splay" -ln "splay" -at "double";
	addAttr -ci true -sn "break" -ln "break" -at "double";
	addAttr -ci true -sn "flex" -ln "flex" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".keepOrientation";
	setAttr -k on ".FK_2_IK";
	setAttr -k on ".globalIK_2_localIK";
	setAttr -k on ".neutral";
	setAttr -k on ".fist";
	setAttr -k on ".relax";
	setAttr -k on ".curl";
	setAttr -k on ".spread";
	setAttr -k on ".splay";
	setAttr -k on ".break";
	setAttr -k on ".flex";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_wrist_ctrl";
createNode locator -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_thumb_03_ctrl";
createNode locator -n "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_thumb_02_ctrl";
createNode locator -n "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_thumb_01_ctrl";
createNode locator -n "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_index_04_ctrl";
createNode locator -n "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_index_03_ctrl";
createNode locator -n "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_index_02_ctrl";
createNode locator -n "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_index_01_ctrl";
createNode locator -n "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_middle_04_ctrl";
createNode locator -n "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_middle_03_ctrl";
createNode locator -n "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_middle_02_ctrl";
createNode locator -n "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_middle_01_ctrl";
createNode locator -n "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_ring_04_ctrl";
createNode locator -n "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_ring_03_ctrl";
createNode locator -n "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_ring_02_ctrl";
createNode locator -n "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_ring_01_ctrl";
createNode locator -n "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "keepOrientation" -ln "keepOrientation" -at "double";
	addAttr -ci true -sn "FK_2_IK" -ln "FK_2_IK" -at "double";
	addAttr -ci true -sn "globalIK_2_localIK" -ln "globalIK_2_localIK" -at "double";
	addAttr -ci true -sn "neutral" -ln "neutral" -at "double";
	addAttr -ci true -sn "fist" -ln "fist" -at "double";
	addAttr -ci true -sn "relax" -ln "relax" -at "double";
	addAttr -ci true -sn "curl" -ln "curl" -at "double";
	addAttr -ci true -sn "spread" -ln "spread" -at "double";
	addAttr -ci true -sn "splay" -ln "splay" -at "double";
	addAttr -ci true -sn "break" -ln "break" -at "double";
	addAttr -ci true -sn "flex" -ln "flex" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".keepOrientation";
	setAttr -k on ".FK_2_IK";
	setAttr -k on ".globalIK_2_localIK";
	setAttr -k on ".neutral";
	setAttr -k on ".fist";
	setAttr -k on ".relax";
	setAttr -k on ".curl";
	setAttr -k on ".spread";
	setAttr -k on ".splay";
	setAttr -k on ".break";
	setAttr -k on ".flex";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_wrist_ctrl";
createNode locator -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:m_spineA_head_ctrl";
createNode locator -n "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:m_spineA_neck_03_ctrl";
createNode locator -n "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:m_spineA_neck_02_ctrl";
createNode locator -n "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:m_spineA_neck_01_ctrl";
createNode locator -n "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "twistBlend" -ln "twistBlend" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".twistBlend";
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_elbow_FK_ctrl";
createNode locator -n "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1" -p
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
	setAttr ".ObjName" -type "string" "vicky_original:l_armA_uprarm_FK_ctrl";
createNode locator -n "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "twistBlend" -ln "twistBlend" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".twistBlend";
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_elbow_FK_ctrl";
createNode locator -n "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1" -p
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
	setAttr ".ObjName" -type "string" "vicky_original:r_armA_uprarm_FK_ctrl";
createNode locator -n "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1Shape" 
		-p "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:l_legA_ankle_ctrl";
createNode locator -n "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:r_legA_ankle_ctrl";
createNode locator -n "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "followHead" -ln "followHead" -at "float";
	addAttr -ci true -sn "displayGeo" -ln "displayGeo" -at "long";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k on ".followHead";
	setAttr -k on ".displayGeo";
	setAttr ".ObjName" -type "string" "vicky_original:l_hornLong_ctrl";
createNode locator -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1Shape" -p "vicky_original:l_hornLong_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "followHead" -ln "followHead" -at "float";
	addAttr -ci true -sn "displayGeo" -ln "displayGeo" -at "long";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k on ".followHead";
	setAttr -k on ".displayGeo";
	setAttr ".ObjName" -type "string" "vicky_original:r_hornLong_ctrl";
createNode locator -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1Shape" -p "vicky_original:r_hornLong_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "followHead" -ln "followHead" -at "float";
	addAttr -ci true -sn "displayGeo" -ln "displayGeo" -at "long";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k on ".followHead";
	setAttr -k on ".displayGeo";
	setAttr ".ObjName" -type "string" "vicky_original:m_helmet_ctrl";
createNode locator -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1Shape" -p "vicky_original:m_helmet_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_hair_ex_ctrl";
createNode locator -n "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1Shape" -p "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:m_hair_ex_ctrl";
createNode locator -n "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1Shape" -p "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_hair_ex_ctrl";
createNode locator -n "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1Shape" -p "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:r_foreHair_ex_ctrl";
createNode locator -n "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:l_foreHair_ex_ctrl";
createNode locator -n "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "subCtrl" -ln "subCtrl" -at "long";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k on ".subCtrl";
	setAttr ".ObjName" -type "string" "vicky_original:hair_ex_ctrl";
createNode locator -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1Shape" -p "vicky_original:hair_ex_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:mov_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:mov_ctrl";
createNode locator -n "vicky_original:mov_ctrl_outPutAnimBank_1Shape" -p "vicky_original:mov_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:top_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "globalScale" -ln "globalScale" -at "double";
	addAttr -ci true -sn "headRes" -ln "headRes" -at "long";
	addAttr -ci true -sn "bodyRes" -ln "bodyRes" -at "long";
	addAttr -ci true -sn "shoe" -ln "shoe" -at "long";
	addAttr -ci true -sn "helmetCtrl" -ln "helmetCtrl" -at "double";
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
	setAttr -k on ".headRes";
	setAttr -k on ".bodyRes";
	setAttr -k on ".shoe";
	setAttr -k on ".helmetCtrl";
	setAttr -k on ".hairCtrl";
	setAttr -k on ".clothCtrl";
	setAttr ".ObjName" -type "string" "vicky_original:top_ctrl";
createNode locator -n "vicky_original:top_ctrl_outPutAnimBank_1Shape" -p "vicky_original:top_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:tongoueA_Rot_Ctrl";
createNode locator -n "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:tongoueB_Rot_Ctrl";
createNode locator -n "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:tongoueC_Rot_Ctrl";
createNode locator -n "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "vicky_original:tongueIn1_Ctrl";
createNode locator -n "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1Shape" -p "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ratio" -ln "ratio" -at "double";
	addAttr -ci true -sn "roll" -ln "roll" -at "double";
	addAttr -ci true -sn "Sub_Ctrl" -ln "Sub_Ctrl" -at "long";
	addAttr -ci true -sn "ExtraDeformers" -ln "ExtraDeformers" -at "long";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sz";
	setAttr -k on ".ratio";
	setAttr -k on ".roll";
	setAttr -k on ".Sub_Ctrl";
	setAttr -k on ".ExtraDeformers";
	setAttr ".ObjName" -type "string" "vicky_original:m_tongueTip_Ctrl";
createNode locator -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1Shape" -p "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:m_tongue_subC_Ctrl";
createNode locator -n "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:m_tongue_subB_Ctrl";
createNode locator -n "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:m_tongue_subA_Ctrl";
createNode locator -n "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1Shape" -p
		 "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:tongueCon_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:tongueCon_ctrl";
createNode locator -n "vicky_original:tongueCon_ctrl_outPutAnimBank_1Shape" -p "vicky_original:tongueCon_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:tongueCurve_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "vicky_original:tongueCurve";
createNode locator -n "vicky_original:tongueCurve_outPutAnimBank_1Shape" -p "vicky_original:tongueCurve_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "vicky_original:m_jaw_ctrl";
createNode locator -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1Shape" -p "vicky_original:m_jaw_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_pupilRadz_end_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "vicky_original:l_pupilRadz_end";
createNode locator -n "vicky_original:l_pupilRadz_end_outPutAnimBank_1Shape" -p "vicky_original:l_pupilRadz_end_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:l_eye_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:l_eye_ctrl";
createNode locator -n "vicky_original:l_eye_ctrl_outPutAnimBank_1Shape" -p "vicky_original:l_eye_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:r_eye_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:r_eye_ctrl";
createNode locator -n "vicky_original:r_eye_ctrl_outPutAnimBank_1Shape" -p "vicky_original:r_eye_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_bothEye_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:m_bothEye_ctrl";
createNode locator -n "vicky_original:m_bothEye_ctrl_outPutAnimBank_1Shape" -p "vicky_original:m_bothEye_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:m_eye_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "vicky_original:m_eye_ctrl";
createNode locator -n "vicky_original:m_eye_ctrl_outPutAnimBank_1Shape" -p "vicky_original:m_eye_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "vicky_original:head_squash_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "vicky_original:head_squash_ctrl";
createNode locator -n "vicky_original:head_squash_ctrl_outPutAnimBank_1Shape" -p "vicky_original:head_squash_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode animCurveTL -n "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 17 ".ktv[0:16]"  100 -0.011457540299999999 101 -0.026827806919999999
		 102 -0.068896994219999994 103 -0.18486257380000001 104 -0.20888378339999999 105 -0.065916283249999999
		 106 -0.02038001305 107 -0.0088270167609999992 108 -0.011457540299999999 109 -0.026827806919999999
		 110 -0.068896994219999994 111 -0.18486257380000001 112 -0.20888378339999999 113 -0.065916283249999999
		 114 -0.02038001305 115 -0.0088270167609999992 116 -0.011457540299999999;
	setAttr -s 17 ".kit[0:16]"  1 9 9 9 9 9 9 1 
		1 9 9 9 9 9 9 1 1;
	setAttr -s 17 ".kot[0:16]"  1 9 9 9 9 9 9 1 
		1 9 9 9 9 9 9 1 1;
	setAttr -s 17 ".kix[0:16]"  0.99139225482940674 0.81230640411376953 
		0.45164570212364197 0.49617385864257813 0.55808788537979126 0.39066830277442932 0.81399267911911011 
		0.99911582469940186 0.98345655202865601 0.81230640411376953 0.45164570212364197 0.49617385864257813 
		0.55808788537979126 0.39066830277442932 0.8139910101890564 0.99911582469940186 0.98345655202865601;
	setAttr -s 17 ".kiy[0:16]"  -0.13092531263828278 -0.58323103189468384 
		-0.8921973705291748 -0.86822313070297241 0.82978183031082153 0.9205315113067627 0.58087515830993652 
		0.042042691260576248 -0.18114428222179413 -0.58323103189468384 -0.8921973705291748 
		-0.86822313070297241 0.82978183031082153 0.9205315113067627 0.58087742328643799 0.042042691260576248 
		-0.18114428222179413;
	setAttr -s 17 ".kox[0:16]"  0.99139225482940674 0.81230640411376953 
		0.45164570212364197 0.49617385864257813 0.55808788537979126 0.39066830277442932 0.81399267911911011 
		0.99911582469940186 0.98345655202865601 0.81230640411376953 0.45164570212364197 0.49617385864257813 
		0.55808788537979126 0.39066830277442932 0.8139910101890564 0.99911582469940186 0.98345655202865601;
	setAttr -s 17 ".koy[0:16]"  -0.13092531263828278 -0.58323103189468384 
		-0.8921973705291748 -0.86822313070297241 0.82978183031082153 0.9205315113067627 0.58087515830993652 
		0.04204270988702774 -0.18114438652992249 -0.58323103189468384 -0.8921973705291748 
		-0.86822313070297241 0.82978183031082153 0.9205315113067627 0.58087742328643799 0.04204270988702774 
		-0.18114438652992249;
createNode animCurveTL -n "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 2.9580326119999998 102 2.362701688 105 -2.196391733
		 107 -2.9576913120000001 110 -2.3176958120000002 113 2.0768632239999998 115 2.9940169179999998
		 116 2.9580326119999998;
	setAttr -s 8 ".kit[0:7]"  3 1 1 9 1 9 3 9;
	setAttr -s 8 ".kot[3:7]"  9 1 9 3 9;
	setAttr -s 8 ".kix[1:7]"  0.079544536769390106 0.046376097947359085 
		0.99994397163391113 0.053577248007059097 0.9072689414024353 1 0.99987679719924927;
	setAttr -s 8 ".kiy[1:7]"  -0.017397988587617874 -0.017434513196349144 
		-0.010585169307887554 0.01742822490632534 0.42055076360702515 0 -0.015699194744229317;
	setAttr -s 8 ".kox[0:7]"  1 0.079544536769390106 0.046376120299100876 
		0.99994397163391113 0.053577248007059097 0.9072689414024353 1 0.99987679719924927;
	setAttr -s 8 ".koy[0:7]"  0 -0.017397988587617874 -0.017434513196349144 
		-0.010585169307887554 0.01742822490632534 0.42055076360702515 0 -0.015699194744229317;
createNode animCurveTU -n "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_wide";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_thick";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  100 -0.62342823790000002 101 -0.77851875810000004
		 102 -0.41918434030000001 104 1.408502033 106 1.4194075420000001 108 -0.62342823790000002
		 109 -0.77851875810000004 110 -0.41918434030000001 112 1.408502033 114 1.4194075420000001
		 116 -0.62342823790000002;
	setAttr -s 11 ".kit[2:10]"  9 9 1 1 1 9 9 1 
		1;
	setAttr -s 11 ".kot[2:10]"  9 9 1 1 1 9 9 1 
		1;
	setAttr -s 11 ".kix[0:10]"  0.10511631518602371 0.49094325304031372 
		0.95295113325119019 0.98047500848770142 0.059585843235254288 0.12197047472000122 
		0.49094325304031372 0.95295113325119019 0.98047500848770142 0.059585843235254288 
		0.12197047472000122;
	setAttr -s 11 ".kiy[0:10]"  -0.017356600612401962 0.015205160714685917 
		0.3031238317489624 0.19664353132247925 -0.017422281205654144 -0.017322981730103493 
		0.015205160714685917 0.3031238317489624 0.19664353132247925 -0.017422281205654144 
		-0.017322981730103493;
	setAttr -s 11 ".kox[0:10]"  0.10511631518602371 0.4909433126449585 
		0.95295113325119019 0.98047500848770142 0.059585843235254288 0.12197047472000122 
		0.4909433126449585 0.95295113325119019 0.98047500848770142 0.059585843235254288 0.12197047472000122;
	setAttr -s 11 ".koy[0:10]"  -0.017356600612401962 0.015205159783363342 
		0.3031238317489624 0.19664353132247925 -0.017422281205654144 -0.017322981730103493 
		0.015205159783363342 0.3031238317489624 0.19664353132247925 -0.017422281205654144 
		-0.017322981730103493;
createNode animCurveTA -n "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  100 10.17052889 102 8.0330656309999995 106 -7.4027962180000006
		 108 -9.9803514539999991 110 -7.8134991430000005 114 7.0652936140000007 116 10.17052889;
	setAttr -s 7 ".kit[0:6]"  3 1 1 9 1 9 3;
	setAttr -s 7 ".kot[3:6]"  9 1 9 3;
	setAttr -s 7 ".kix[1:6]"  0.023562196642160416 0.013710969127714634 
		0.99899798631668091 0.015845192596316338 0.60740774869918823 1;
	setAttr -s 7 ".kiy[1:6]"  -0.017448447644710541 -0.017451651394367218 
		-0.044755760580301285 0.017451100051403046 0.79439014196395874 0;
	setAttr -s 7 ".kox[0:6]"  1 0.023562196642160416 0.013710985891520977 
		0.99899798631668091 0.015845203772187233 0.60740774869918823 1;
	setAttr -s 7 ".koy[0:6]"  0 -0.017448447644710541 -0.017451651394367218 
		-0.044755760580301285 0.017451100051403046 0.79439014196395874 0;
createNode animCurveTA -n "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 -2.0365930909999999 101 -2.0180201449999999
		 102 -1.613915094 106 1.775445766 107 1.8878323300000002 109 1.9471271779999999 110 1.7869995620000003
		 114 -1.81079108 116 -2.0365930919999999;
	setAttr -s 9 ".kit[0:8]"  18 9 9 1 1 3 1 1 
		18;
	setAttr -s 9 ".kot[1:8]"  9 9 1 1 3 1 1 18;
	setAttr -s 9 ".kix[3:8]"  0.18670320510864258 0.54277193546295166 
		1 0.14167517423629761 0.17360657453536987 1;
	setAttr -s 9 ".kiy[3:8]"  0.017146401107311249 0.014658673666417599 
		0 -0.017277244478464127 -0.017188265919685364 0;
	setAttr -s 9 ".kox[0:8]"  1 0.99577528238296509 0.94933372735977173 
		0.18670320510864258 0.54277193546295166 1 0.1416754275560379 0.17360644042491913 
		1;
	setAttr -s 9 ".koy[0:8]"  0 0.091824539005756378 0.31426998972892761 
		0.017146401107311249 0.014658673666417599 0 -0.017277244478464127 -0.017188267782330513 
		0;
createNode animCurveTL -n "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_wide";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_thick";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 -3.434366126 101 -3.2881632559999998
		 103 -2.881317879 105 -2.7939762890000002 108 -3.434366126 109 -3.2881632559999998
		 111 -2.881317879 113 -2.7939762890000002 116 -3.434366126;
	setAttr -s 9 ".kit[0:8]"  1 9 9 9 3 9 9 9 
		3;
	setAttr -s 9 ".kot[0:8]"  1 9 9 9 3 9 9 9 
		3;
	setAttr -s 9 ".kix[0:8]"  0.90258830785751343 0.99678051471710205 
		0.99855011701583862 0.99883741140365601 1 0.99678051471710205 0.99855011701583862 
		0.99883741140365601 1;
	setAttr -s 9 ".kiy[0:8]"  0.0075137247331440449 0.080178715288639069 
		0.05382932722568512 -0.048206385225057602 0 0.080178715288639069 0.05382932722568512 
		-0.048206500709056854 0;
	setAttr -s 9 ".kox[0:8]"  0.90258830785751343 0.99678051471710205 
		0.99855011701583862 0.99883741140365601 1 0.99678051471710205 0.99855011701583862 
		0.99883741140365601 1;
	setAttr -s 9 ".koy[0:8]"  0.0075137247331440449 0.080178715288639069 
		0.05382932722568512 -0.048206385225057602 0 0.080178715288639069 0.05382932722568512 
		-0.048206500709056854 0;
createNode animCurveTA -n "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 -1.4811938330000003 101 -1.5170865739999999
		 103 -1.363359988 107 1.3673807680000001 109 1.4997661419999999 110 1.505324543 111 1.3761660180000002
		 115 -1.359514189 116 -1.4811938570000001;
	setAttr -s 9 ".kit[0:8]"  18 9 1 1 1 3 1 1 
		18;
	setAttr -s 9 ".kot[1:8]"  9 1 1 1 3 1 1 18;
	setAttr -s 9 ".kix[2:8]"  0.18888059258460999 0.24247616529464722 
		0.93399226665496826 1 0.13662895560264587 0.22584682703018188 1;
	setAttr -s 9 ".kiy[2:8]"  0.017139134928584099 0.016932440921664238 
		0.0062359422445297241 0 -0.017289621755480766 -0.017002347856760025 0;
	setAttr -s 9 ".kox[0:8]"  1 0.99985313415527344 0.18888047337532043 
		0.24247616529464722 0.93399226665496826 1 0.13662900030612946 0.22584664821624756 
		1;
	setAttr -s 9 ".koy[0:8]"  0 0.017135737463831902 0.017139134928584099 
		0.016932440921664238 0.0062359445728361607 0 -0.017289621755480766 -0.017002347856760025 
		0;
createNode animCurveTL -n "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  100 0 105 0 108 0 110 0 112 0 116 0;
	setAttr -s 6 ".kot[0:5]"  1 9 9 9 9 9;
	setAttr -s 6 ".kox[0:5]"  1 1 1 1 1 1;
	setAttr -s 6 ".koy[0:5]"  0 0 0 0 0 0;
createNode animCurveTA -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  100 0 105 0 108 0 110 0 112 0 116 0;
	setAttr -s 6 ".kot[0:5]"  1 9 9 9 9 9;
	setAttr -s 6 ".kox[0:5]"  1 1 1 1 1 1;
	setAttr -s 6 ".koy[0:5]"  0 0 0 0 0 0;
createNode animCurveTA -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 -1.4688870350000001 101 0.11813630109999998
		 104 4.0696293839999997 106 4.0696293839999997 109 0.11813630109999998 112 -3.870837088
		 114 -4.0132225500000001 116 -1.455563742;
	setAttr -s 8 ".kit[0:7]"  18 1 1 1 9 9 1 18;
	setAttr -s 8 ".kot[4:7]"  9 9 1 18;
	setAttr -s 8 ".kix[1:7]"  0.031256634742021561 0.065133653581142426 
		0.0468938909471035 0.86598938703536987 0.94072854518890381 0.092080540955066681 1;
	setAttr -s 8 ".kiy[1:7]"  0.017444763332605362 0.017416231334209442 
		-0.017434092238545418 -0.50006246566772461 -0.33916032314300537 0.017379144206643105 
		0;
	setAttr -s 8 ".kox[0:7]"  1 0.031256634742021561 0.065133653581142426 
		0.0468938909471035 0.86598938703536987 0.94072854518890381 0.092080540955066681 1;
	setAttr -s 8 ".koy[0:7]"  0 0.017444763332605362 0.017416231334209442 
		-0.017434092238545418 -0.50006246566772461 -0.33916032314300537 0.017379144206643105 
		0;
createNode animCurveTL -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_wide";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_thick";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 -0.044314489489999997 102 0.0074595961839999999
		 104 0.051583491170000002 106 0.059626526050000003 108 0.037845040060000001 110 -0.022942391270000001
		 112 -0.058177441619999999 114 -0.060482103269999997 116 -0.044314489489999997;
	setAttr -s 9 ".kit[0:8]"  1 9 9 9 9 9 9 9 
		1;
	setAttr -s 9 ".kot[0:8]"  1 9 9 9 9 9 9 9 
		1;
	setAttr -s 9 ".kix[0:8]"  0.97687000036239624 0.85773384571075439 
		0.95074200630187988 0.99633383750915527 0.88864755630493164 0.85743951797485352 0.97356253862380981 
		0.99626749753952026 0.96176326274871826;
	setAttr -s 9 ".kiy[0:8]"  0.21383415162563324 0.51409393548965454 
		0.30998340249061584 -0.085550352931022644 -0.45859074592590332 -0.51458472013473511 
		-0.22842057049274445 0.08632013201713562 0.27388200163841248;
	setAttr -s 9 ".kox[0:8]"  0.97687000036239624 0.85773384571075439 
		0.95074200630187988 0.99633383750915527 0.88864755630493164 0.85743951797485352 0.97356253862380981 
		0.99626749753952026 0.96176326274871826;
	setAttr -s 9 ".koy[0:8]"  0.21383410692214966 0.51409393548965454 
		0.30998340249061584 -0.085550352931022644 -0.45859074592590332 -0.51458472013473511 
		-0.22842057049274445 0.08632013201713562 0.27388200163841248;
createNode animCurveTL -n "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 17 ".ktv[0:16]"  100 -0.15837416139999999 101 -0.36054364480000001
		 102 -0.4291757692 103 -0.39499227570000001 104 -0.1511829724 105 -0.085368319060000003
		 106 -0.07303851754 107 -0.07828721424 108 -0.15837416139999999 109 -0.36054364480000001
		 110 -0.4291757692 111 -0.39499227570000001 112 -0.1511829724 113 -0.085368319060000003
		 114 -0.07303851754 115 -0.07828721424 116 -0.15837416139999999;
	setAttr -s 17 ".kit[0:16]"  9 1 18 1 9 1 9 1 
		1 1 18 1 9 1 9 1 1;
	setAttr -s 17 ".kot[2:16]"  18 1 9 1 9 1 1 1 
		18 1 9 1 9 1 1;
	setAttr -s 17 ".kix[1:16]"  0.24987503886222839 1 0.47982630133628845 
		0.25016230344772339 0.86672651767730713 0.99610549211502075 0.89582842588424683 0.22959631681442261 
		0.24987503886222839 1 0.47982630133628845 0.25016230344772339 0.86672651767730713 
		0.99610549211502075 0.89582842588424683 0.22959631681442261;
	setAttr -s 17 ".kiy[1:16]"  -0.96827811002731323 0 0.87736350297927856 
		0.96820396184921265 0.49878349900245667 0.08816865086555481 -0.44440007209777832 
		-0.973285973072052 -0.96827811002731323 0 0.87736350297927856 0.96820396184921265 
		0.49878349900245667 0.088169179856777191 -0.44440007209777832 -0.973285973072052;
	setAttr -s 17 ".kox[0:16]"  0.19409114122390747 0.24987503886222839 
		1 0.47982639074325562 0.25016230344772339 0.86672651767730713 0.99610549211502075 
		0.89582842588424683 0.22959624230861664 0.24987503886222839 1 0.47982639074325562 
		0.25016230344772339 0.86672651767730713 0.99610549211502075 0.89582842588424683 0.22959624230861664;
	setAttr -s 17 ".koy[0:16]"  -0.98098349571228027 -0.96827811002731323 
		0 0.87736344337463379 0.96820396184921265 0.49878358840942383 0.08816865086555481 
		-0.44440007209777832 -0.97328603267669678 -0.96827811002731323 0 0.87736344337463379 
		0.96820396184921265 0.49878358840942383 0.088169179856777191 -0.44440007209777832 
		-0.97328603267669678;
createNode animCurveTL -n "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 13 ".ktv[0:12]"  100 8.1358177289999993 101 7.7741603900000005
		 102 8.2843857950000004 103 9.3469788190000003 104 10.032154 107 8.6593068750000004
		 108 8.1358177289999993 109 7.7741603900000005 110 8.2843857950000004 111 9.3469788190000003
		 112 10.032154 115 8.6593068750000004 116 8.1358177289999993;
	setAttr -s 13 ".kit[0:12]"  1 9 9 9 1 9 1 9 
		9 9 1 9 1;
	setAttr -s 13 ".kot[0:12]"  1 9 9 9 1 9 1 9 
		9 9 1 9 1;
	setAttr -s 13 ".kix[0:12]"  0.20823286473751068 0.99947518110275269 
		0.9458649754524231 0.93437838554382324 0.57570827007293701 0.97926795482635498 0.09418816864490509 
		0.99947518110275269 0.9458649754524231 0.93437838554382324 0.57570827007293701 0.97926783561706543 
		0.09418816864490509;
	setAttr -s 13 ".kiy[0:12]"  -0.017070705071091652 0.032395545393228531 
		0.32456040382385254 0.35628244280815125 -0.014270773157477379 -0.20256920158863068 
		-0.017375702038407326 0.032395545393228531 0.32456040382385254 0.35628244280815125 
		-0.014270773157477379 -0.20256976783275604 -0.017375702038407326;
	setAttr -s 13 ".kox[0:12]"  0.20823287963867188 0.99947518110275269 
		0.9458649754524231 0.93437838554382324 0.57570844888687134 0.97926795482635498 0.09418816864490509 
		0.99947518110275269 0.9458649754524231 0.93437838554382324 0.57570844888687134 0.97926783561706543 
		0.09418816864490509;
	setAttr -s 13 ".koy[0:12]"  -0.017070703208446503 0.032395545393228531 
		0.32456040382385254 0.35628244280815125 -0.014270773157477379 -0.20256920158863068 
		-0.017375702038407326 0.032395545393228531 0.32456040382385254 0.35628244280815125 
		-0.014270773157477379 -0.20256976783275604 -0.017375702038407326;
createNode animCurveTA -n "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  100 -2.0049866519999999 102 -1.4561965589999999
		 106 1.3742018549999999 108 1.9470446460000002 110 1.3742018549999999 114 -1.4561965589999999
		 116 -2.0049866519999999;
	setAttr -s 7 ".kit[0:6]"  3 18 9 9 9 9 3;
	setAttr -s 7 ".kot[0:6]"  1 18 9 9 9 9 3;
	setAttr -s 7 ".kox[0:6]"  1 0.97110766172409058 0.97071295976638794 
		1 0.97071284055709839 0.97110772132873535 1;
	setAttr -s 7 ".koy[0:6]"  0 0.23864169418811798 0.24024216830730438 
		0 -0.2402426153421402 -0.23864170908927917 0;
createNode animCurveTA -n "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  100 -0.44089346680000002 103 -0.51011138659999999
		 108 0.37750506449999999 111 0.46666201220000003 116 -0.44089346680000002;
	setAttr -s 5 ".kit[0:4]"  1 9 9 1 9;
	setAttr -s 5 ".kot[0:4]"  1 9 9 1 9;
	setAttr -s 5 ".kix[0:4]"  0.3953547477722168 0.99900525808334351 
		0.99858391284942627 0.66133964061737061 0.99687838554382324;
	setAttr -s 5 ".kiy[0:4]"  -0.016031347215175629 0.044592291116714478 
		0.053199253976345062 -0.013091480359435081 -0.078952006995677948;
	setAttr -s 5 ".kox[0:4]"  0.3953547477722168 0.99900525808334351 
		0.99858391284942627 0.66133999824523926 0.99687838554382324;
	setAttr -s 5 ".koy[0:4]"  -0.016031347215175629 0.044592291116714478 
		0.053199253976345062 -0.013091474771499634 -0.078952006995677948;
createNode animCurveTA -n "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 0 108 0 114 0 116 0;
	setAttr -s 4 ".kit[1:3]"  9 3 18;
	setAttr -s 4 ".kot[0:3]"  1 9 3 18;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTL -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  9 18;
	setAttr -s 3 ".kot[0:2]"  1 9 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 1.800436573 108 -2.5 109 -2.899003913
		 110 -3.0267659500000001 112 -1.708268991 114 0.65412235569999999 115 1.7216979370000001
		 116 1.800436573;
	setAttr -s 8 ".kit[1:7]"  2 9 1 1 9 18 1;
	setAttr -s 8 ".kot[1:7]"  10 9 1 1 9 18 1;
	setAttr -s 8 ".kix[0:7]"  0.98670029640197754 0.074205935001373291 
		0.15014828741550446 0.59195190668106079 0.038223683834075928 0.034964337944984436 
		0.16695959866046906 0.98670029640197754;
	setAttr -s 8 ".kiy[0:7]"  0.16255001723766327 -0.99724292755126953 
		-0.9886634349822998 0.80597323179244995 0.99926918745040894 0.99938857555389404 0.98596376180648804 
		0.16255001723766327;
	setAttr -s 8 ".kox[0:7]"  0.074205897748470306 0.076381109654903412 
		0.15014828741550446 0.59195202589035034 0.038223683834075928 0.034964337944984436 
		0.16695959866046906 1;
	setAttr -s 8 ".koy[0:7]"  -0.99724292755126953 -0.99707871675491333 
		-0.9886634349822998 0.80597317218780518 0.99926918745040894 0.99938857555389404 0.98596376180648804 
		0;
createNode animCurveTA -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 0 102 0 108 0 109 0 110 0 111 0.62567041459999995
		 112 1.2350569600000003 114 0.56957725069999998 116 0;
	setAttr -s 9 ".kit[0:8]"  3 9 9 3 3 9 9 9 
		3;
	setAttr -s 9 ".kot[0:8]"  1 9 9 3 3 9 9 9 
		3;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 0.96556317806243896 0.99996674060821533 
		0.99104636907577515 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0.26016896963119507 -0.0081581566482782364 
		-0.13351768255233765 0;
createNode animCurveTA -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 14.711819959999998 102 9.9192801880000001
		 108 9.9192801880000001 109 9.9192801880000001 110 11.300913270000001 112 15.737361529999999
		 114 17.000149759999999 116 14.711819959999998;
	setAttr -s 8 ".kit[1:7]"  3 9 3 9 9 3 9;
	setAttr -s 8 ".kot[0:7]"  1 3 9 3 9 9 3 9;
	setAttr -s 8 ".kox[0:7]"  0.016690270975232124 1 1 1 0.76336652040481567 
		0.84925895929336548 1 0.89470028877258301;
	setAttr -s 8 ".koy[0:7]"  -0.017450861632823944 0 0 0 0.64596563577651978 
		0.52797651290893555 0 -0.44666710495948792;
createNode animCurveTA -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 0 108 0 109 0 116 0;
	setAttr -s 4 ".kit[0:3]"  18 9 9 18;
	setAttr -s 4 ".kot[0:3]"  1 9 9 18;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTU -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  100 0 102 0 108 0 109 0 110 1.204203661
		 111 2.2001581589999999 113 1.407305517 114 0.5560899212 115 0.21441977849999999 116 0;
	setAttr -s 10 ".kit[0:9]"  3 3 9 3 1 9 9 9 
		1 3;
	setAttr -s 10 ".kot[0:9]"  1 3 9 3 1 9 9 9 
		1 3;
	setAttr -s 10 ".kix[4:9]"  0.030012939125299454 0.50868266820907593 
		0.072795949876308441 0.066913887858390808 0.27135056257247925 1;
	setAttr -s 10 ".kiy[4:9]"  0.99954956769943237 0.86095410585403442 
		-0.99734681844711304 -0.99775880575180054 -0.96248054504394531 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 0.030012939125299454 0.50868266820907593 
		0.072795949876308441 0.066913887858390808 0.27135053277015686 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0.99954956769943237 0.86095410585403442 
		-0.99734681844711304 -0.99775880575180054 -0.96248054504394531 0;
createNode animCurveTU -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 15 ".ktv[0:14]"  100 -19.144541579999999 101 -4.602238882
		 102 0 102.00416666666666 0 104 0 105 4.6950874000000002 106 13.527303209999999 107 25.1785812
		 108 38.186822329999998 109 58.040818340000001 110 64.026131539999994 112 48.533094460000001
		 114 6.9616123029999999 115 -15.33144223 116 -19.144541579999999;
	setAttr -s 15 ".kit[2:14]"  3 9 3 9 1 9 1 9 
		18 9 18 9 9;
	setAttr -s 15 ".kot[0:14]"  1 9 3 9 3 9 1 9 
		1 9 18 9 18 9 9;
	setAttr -s 15 ".kix[6:14]"  0.003893199609592557 0.0032441825605928898 
		0.0023529399186372757 0.0030960401054471731 1 0.0028038299642503262 0.0018789718160405755 
		0.0030643942300230265 0.010489567182958126;
	setAttr -s 15 ".kiy[6:14]"  0.99999243021011353 0.99999475479125977 
		0.99999719858169556 0.99999517202377319 0 -0.99999606609344482 -0.99999821186065674 
		-0.99999535083770752 -0.99994498491287231;
	setAttr -s 15 ".kox[0:14]"  0.0027505827601999044 0.0041786963120102882 
		1 1 1 0.0059138559736311436 0.003893199609592557 0.0032441825605928898 0.0023529399186372757 
		0.0030960401054471731 1 0.0028038299642503262 0.0018789718160405755 0.0030643942300230265 
		0.010489567182958126;
	setAttr -s 15 ".koy[0:14]"  0.99999618530273438 0.99999123811721802 
		0 0 0 0.99998247623443604 0.99999243021011353 0.99999475479125977 0.99999719858169556 
		0.99999517202377319 0 -0.99999606609344482 -0.99999821186065674 -0.99999535083770752 
		-0.99994498491287231;
createNode animCurveTU -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  100 25.139861079999999 101 30.461951160000002
		 102 0 108 0 109 0 110 -7.0352354359999998 111 -8.5076647609999991 112 -8.5228934400000007
		 114 -6.7061563749999999 115 11.721700719999999 116 25.139861079999999;
	setAttr -s 11 ".kit[1:10]"  1 18 9 3 9 9 3 1 
		9 9;
	setAttr -s 11 ".kot[0:10]"  1 1 18 9 3 9 9 3 
		1 9 9;
	setAttr -s 11 ".kix[1:10]"  0.018124548718333244 1 1 1 0.0094028608873486519 
		0.053698159754276276 1 0.025783447548747063 0.0025120778009295464 0.0029810182750225067;
	setAttr -s 11 ".kiy[1:10]"  -0.99983572959899902 0 0 0 -0.99995583295822144 
		-0.99855720996856689 0 0.99966752529144287 0.9999968409538269 0.99999552965164185;
	setAttr -s 11 ".kox[0:10]"  0.0075156246311962605 0.018124548718333244 
		1 1 1 0.0094028608873486519 0.053698159754276276 1 0.02578343078494072 0.0025120778009295464 
		0.0029810182750225067;
	setAttr -s 11 ".koy[0:10]"  0.99997180700302124 -0.99983572959899902 
		0 0 0 -0.99995583295822144 -0.99855720996856689 0 0.99966752529144287 0.9999968409538269 
		0.99999552965164185;
createNode animCurveTU -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 0 108 0 109 0 116 0;
	setAttr -s 4 ".kit[0:3]"  18 9 9 18;
	setAttr -s 4 ".kot[0:3]"  1 9 9 18;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTU -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 0 108 0 109 0 116 0;
	setAttr -s 4 ".kit[0:3]"  18 9 9 18;
	setAttr -s 4 ".kot[0:3]"  1 9 9 18;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTU -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footSide";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 0 108 0 109 0 116 0;
	setAttr -s 4 ".kit[0:3]"  18 9 9 18;
	setAttr -s 4 ".kot[0:3]"  1 9 9 18;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTU -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 0 108 0 109 0 116 0;
	setAttr -s 4 ".kit[0:3]"  18 9 9 18;
	setAttr -s 4 ".kot[0:3]"  1 9 9 18;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTU -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 0 108 0 109 0 116 0;
	setAttr -s 4 ".kit[0:3]"  18 9 9 18;
	setAttr -s 4 ".kot[0:3]"  1 9 9 18;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTU -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 0 108 0 109 0 116 0;
	setAttr -s 4 ".kit[0:3]"  18 9 9 18;
	setAttr -s 4 ".kot[0:3]"  1 9 9 18;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTU -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 1 108 1 109 1 116 1;
	setAttr -s 4 ".kit[0:3]"  18 9 9 18;
	setAttr -s 4 ".kot[0:3]"  1 9 9 18;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTU -n "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 0 108 0 109 0 116 0;
	setAttr -s 4 ".kit[0:3]"  18 9 9 18;
	setAttr -s 4 ".kot[0:3]"  1 9 9 18;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTA -n "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 106 0 116 0;
	setAttr -s 3 ".kit[1:2]"  3 9;
	setAttr -s 3 ".kot[0:2]"  1 3 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kit[0:1]"  3 9;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 -2.5 101 -2.899003913 102 -3.0267659500000001
		 104 -1.708268991 106 0.65412235569999999 107 1.7216979370000001 108 1.800436573 116 -2.5;
	setAttr -s 8 ".kit[0:7]"  9 9 1 1 9 18 1 2;
	setAttr -s 8 ".kot[1:7]"  9 1 1 9 18 1 10;
	setAttr -s 8 ".kix[2:7]"  0.59195190668106079 0.038223683834075928 
		0.034964472055435181 0.16695959866046906 0.98670029640197754 0.074205823242664337;
	setAttr -s 8 ".kiy[2:7]"  0.80597323179244995 0.99926918745040894 
		0.99938851594924927 0.98596376180648804 0.16255001723766327 -0.99724292755126953;
	setAttr -s 8 ".kox[0:7]"  0.099749557673931122 0.15014828741550446 
		0.59195202589035034 0.038223683834075928 0.034964472055435181 0.16695959866046906 
		0.074205890297889709 0.074205823242664337;
	setAttr -s 8 ".koy[0:7]"  -0.99501258134841919 -0.9886634349822998 
		0.80597317218780518 0.99926918745040894 0.99938851594924927 0.98596376180648804 -0.99724292755126953 
		-0.99724292755126953;
createNode animCurveTA -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 0 101 0 102 0 103 0.62567041459999995
		 104 1.2350569600000003 106 0.56957725069999998 108 0 110 0 116 0;
	setAttr -s 9 ".kit[0:8]"  3 3 3 9 9 9 3 9 
		9;
	setAttr -s 9 ".kot[0:8]"  1 3 3 9 9 9 3 9 
		9;
	setAttr -s 9 ".kox[0:8]"  1 1 1 0.96556317806243896 0.99996674060821533 
		0.9910464882850647 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0.26016896963119507 -0.0081581566482782364 
		-0.13351729512214661 0 0 0;
createNode animCurveTA -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 -9.9817521510000002 101 -9.9817521510000002
		 102 -11.203563730000001 104 -15.126822300000001 106 -16.24353649 108 -14.219911059999999
		 110 -9.9817521510000002 116 -9.9817521510000002;
	setAttr -s 8 ".kit[1:7]"  3 9 9 3 9 3 9;
	setAttr -s 8 ".kot[0:7]"  1 3 9 9 3 9 3 9;
	setAttr -s 8 ".kox[0:7]"  1 1 0.80064487457275391 0.87629866600036621 
		1 0.82575231790542603 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 -0.59913927316665649 -0.48176819086074829 
		0 0.56403285264968872 0 0;
createNode animCurveTA -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 101 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  100 0 101 0 102 1.204203661 103 2.2001581589999999
		 105 1.407305517 106 0.5560899212 107 0.21441977849999999 108 0.101564218 110 0 116 0;
	setAttr -s 10 ".kit[1:9]"  3 1 9 9 9 1 1 3 
		9;
	setAttr -s 10 ".kot[0:9]"  1 3 1 9 9 9 1 1 
		3 9;
	setAttr -s 10 ".kix[2:9]"  0.030012939125299454 0.50868266820907593 
		0.072795949876308441 0.066914282739162445 0.27135056257247925 0.4235152006149292 
		1 1;
	setAttr -s 10 ".kiy[2:9]"  0.99954956769943237 0.86095410585403442 
		-0.99734681844711304 -0.99775868654251099 -0.96248054504394531 -0.90588903427124023 
		0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 0.030012939125299454 0.50868266820907593 
		0.072795949876308441 0.066914282739162445 0.27135053277015686 0.42351508140563965 
		1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0.99954956769943237 0.86095410585403442 
		-0.99734681844711304 -0.99775868654251099 -0.96248054504394531 -0.90588897466659546 
		0 0;
createNode animCurveTU -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 14 ".ktv[0:13]"  100 38.186822329999998 101 58.040818340000001
		 102 64.026131539999994 104 48.533094460000001 106 6.9616123029999999 107 -15.33144223
		 108 -19.144541579999999 109 -4.602238882 110 0 110.00416666666666 0 112 0 114 13.527303209999999
		 115 25.1785812 116 38.186822329999998;
	setAttr -s 14 ".kit[2:13]"  18 9 18 9 9 9 3 9 
		3 1 9 1;
	setAttr -s 14 ".kot[0:13]"  1 9 18 9 18 9 9 9 
		3 9 3 1 9 1;
	setAttr -s 14 ".kix[11:13]"  0.0047442824579775333 0.0032441630028188229 
		0.0023529399186372757;
	setAttr -s 14 ".kiy[11:13]"  0.99998879432678223 0.99999475479125977 
		0.99999719858169556;
	setAttr -s 14 ".kox[0:13]"  0.0020147017203271389 0.0030960401054471731 
		1 0.0028038299642503262 0.0018789794994518161 0.0030644126236438751 0.0074560707435011864 
		0.0041786963120102882 1 1 1 0.0047442824579775333 0.0032441630028188229 0.0023529399186372757;
	setAttr -s 14 ".koy[0:13]"  0.99999797344207764 0.99999517202377319 
		0 -0.99999606609344482 -0.99999821186065674 -0.99999535083770752 0.99997222423553467 
		0.99999123811721802 0 0 0 0.99998879432678223 0.99999475479125977 0.99999719858169556;
createNode animCurveTU -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  100 0 101 0 102 -7.0352354359999998 103 -8.5076647609999991
		 104 -8.5228934400000007 106 -6.7061563749999999 107 11.721700719999999 108 25.139861079999999
		 109 30.461951160000002 110 0 116 0;
	setAttr -s 11 ".kit[0:10]"  3 3 9 9 3 1 9 9 
		1 18 9;
	setAttr -s 11 ".kot[0:10]"  1 3 9 9 3 1 9 9 
		1 18 9;
	setAttr -s 11 ".kix[5:10]"  0.025783447548747063 0.0025120929349213839 
		0.0042688432149589062 0.018124548718333244 1 1;
	setAttr -s 11 ".kiy[5:10]"  0.99966752529144287 0.9999968409538269 
		0.99999088048934937 -0.99983572959899902 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 0.0094028608873486519 0.053698159754276276 
		1 0.02578343078494072 0.0025120929349213839 0.0042688432149589062 0.018124548718333244 
		1 1;
	setAttr -s 11 ".koy[0:10]"  0 0 -0.99995583295822144 -0.99855720996856689 
		0 0.99966752529144287 0.9999968409538269 0.99999088048934937 -0.99983572959899902 
		0 0;
createNode animCurveTU -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 101 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 101 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footSide";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 101 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 101 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 101 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 101 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 1 101 1 116 1;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 101 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 -10.154627050000002 102 -7.993661007
		 104 -3.7731789280000005 106 -9.2931646459999993 109 -9.6231411330000007 112 -2.8517186680000002
		 114 -5.4395768609999999 116 -10.154627050000002;
	setAttr -s 8 ".kit[0:7]"  1 9 9 9 9 9 1 1;
	setAttr -s 8 ".kot[0:7]"  1 9 9 9 9 9 1 1;
	setAttr -s 8 ".kix[0:7]"  0.061700843274593353 0.82072955369949341 
		0.99010181427001953 0.89065343141555786 0.90556859970092773 0.93935561180114746 0.025024218484759331 
		0.043396782130002975;
	setAttr -s 8 ".kiy[0:7]"  -0.01742003858089447 0.57131695747375488 
		-0.14035087823867798 -0.454682856798172 0.42419975996017456 0.34294483065605164 -0.017447825521230698 
		-0.01743684895336628;
	setAttr -s 8 ".kox[0:7]"  0.061700768768787384 0.82072955369949341 
		0.99010181427001953 0.89065343141555786 0.90556859970092773 0.93935561180114746 0.025024205446243286 
		0.043396800756454468;
	setAttr -s 8 ".koy[0:7]"  -0.01742003858089447 0.57131695747375488 
		-0.14035087823867798 -0.454682856798172 0.42419975996017456 0.34294483065605164 -0.017447825521230698 
		-0.01743684895336628;
createNode animCurveTA -n "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  100 8.7141240310000008 102 9.1370877630000003
		 104 2.880057732 106 -8.15658554 108 -12.88318306 110 -12.41977243 116 8.7141240310000008;
	setAttr -s 7 ".kit[2:6]"  9 9 9 1 1;
	setAttr -s 7 ".kot[2:6]"  9 9 9 1 1;
	setAttr -s 7 ".kix[0:6]"  0.082938522100448608 0.11966083198785782 
		0.46836021542549133 0.50272983312606812 0.90674734115600586 0.021687515079975128 
		0.07321641594171524;
	setAttr -s 7 ".kiy[0:6]"  0.017393160611391068 -0.017327886074781418 
		-0.88353759050369263 -0.86444360017776489 -0.42167431116104126 0.017449187114834785 
		0.017406448721885681;
	setAttr -s 7 ".kox[0:6]"  0.082938522100448608 0.11966090649366379 
		0.46836021542549133 0.50272983312606812 0.90674734115600586 0.021687515079975128 
		0.07321641594171524;
	setAttr -s 7 ".koy[0:6]"  0.017393160611391068 -0.017327886074781418 
		-0.88353759050369263 -0.86444360017776489 -0.42167431116104126 0.017449187114834785 
		0.017406448721885681;
createNode animCurveTL -n "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  9 18;
	setAttr -s 3 ".kot[0:2]"  1 9 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  9 18;
	setAttr -s 3 ".kot[0:2]"  1 9 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  9 18;
	setAttr -s 3 ".kot[0:2]"  1 9 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 -10.274734130000001 101 -9.6231411330000007
		 104 -2.8517186680000002 106 -5.4395768609999999 108 -10.154627050000002 110 -7.993661007
		 112 -3.7731789280000005 114 -9.2931646459999993 116 -10.274734309999999;
	setAttr -s 9 ".kit[0:8]"  18 9 9 1 1 9 9 9 
		18;
	setAttr -s 9 ".kot[0:8]"  1 9 9 1 1 9 9 9 
		18;
	setAttr -s 9 ".kix[3:8]"  0.025024218484759331 0.043396782130002975 
		0.82072955369949341 0.99010181427001953 0.81568688154220581 1;
	setAttr -s 9 ".kiy[3:8]"  -0.017447825521230698 -0.01743684895336628 
		0.57131695747375488 -0.14035087823867798 -0.57849359512329102 0;
	setAttr -s 9 ".kox[0:8]"  1 0.77716797590255737 0.93935561180114746 
		0.025024205446243286 0.043396800756454468 0.82072955369949341 0.99010181427001953 
		0.81568688154220581 1;
	setAttr -s 9 ".koy[0:8]"  0 0.62929320335388184 0.34294483065605164 
		-0.017447825521230698 -0.01743684895336628 0.57131695747375488 -0.14035087823867798 
		-0.57849359512329102 0;
createNode animCurveTA -n "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  100 -12.88318306 102 -12.41977243 108 8.7141240310000008
		 110 9.1370877630000003 112 2.880057732 114 -8.15658554 116 -12.88318306;
	setAttr -s 7 ".kit[0:6]"  9 1 1 1 9 9 9;
	setAttr -s 7 ".kot[4:6]"  9 9 9;
	setAttr -s 7 ".kix[1:6]"  0.021687515079975128 0.07321641594171524 
		0.11966083198785782 0.46836021542549133 0.50272870063781738 0.69616860151290894;
	setAttr -s 7 ".kiy[1:6]"  0.017449187114834785 0.017406448721885681 
		-0.017327886074781418 -0.88353759050369263 -0.86444425582885742 -0.71787834167480469;
	setAttr -s 7 ".kox[0:6]"  0.1701166033744812 0.021687515079975128 
		0.07321641594171524 0.11966090649366379 0.46836021542549133 0.50272870063781738 0.69616860151290894;
	setAttr -s 7 ".koy[0:6]"  0.017198892310261726 0.017449187114834785 
		0.017406448721885681 -0.017327886074781418 -0.88353759050369263 -0.86444425582885742 
		-0.71787834167480469;
createNode animCurveTL -n "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_followBody";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 -15.853047410000002 102 -18.65251336
		 104 -19.577395970000001 106 -15.516626829999998 108 -11.587481049999999 110 -8.1615083540000004
		 111 -5.5041864550000001 114 -0.27179297019999998 116 -15.853047410000002;
	setAttr -s 9 ".kit[0:8]"  3 9 9 9 18 9 1 9 
		3;
	setAttr -s 9 ".kot[0:8]"  1 9 9 9 18 9 1 9 
		3;
	setAttr -s 9 ".kix[6:8]"  0.015832962468266487 0.74214565753936768 
		1;
	setAttr -s 9 ".kiy[6:8]"  0.017451105639338493 -0.6702386736869812 
		0;
	setAttr -s 9 ".kox[0:8]"  1 0.92646217346191406 0.94617354869842529 
		0.75385940074920654 0.77998626232147217 0.74893534183502197 0.015832962468266487 
		0.74214565753936768 1;
	setAttr -s 9 ".koy[0:8]"  0 -0.37638804316520691 0.32365992665290833 
		0.6570357084274292 0.62579655647277832 0.66264313459396362 0.017451105639338493 -0.6702386736869812 
		0;
createNode animCurveTA -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 -39.600324880000002 102 -25.955080679999998
		 104 11.03310078 106 16.367632100000002 108 -9.6088123319999994 110 -34.809888919999999
		 111 -35.941293260000002 114 -17.91012855 116 -39.600324880000002;
	setAttr -s 9 ".kit[0:8]"  1 9 1 9 9 9 9 9 
		1;
	setAttr -s 9 ".kot[0:8]"  1 9 1 9 9 9 9 9 
		1;
	setAttr -s 9 ".kix[0:8]"  0.003700225381180644 0.17815619707107544 
		0.0025756573304533958 0.40588554739952087 0.17632183432579041 0.25263327360153198 
		0.47681704163551331 0.95261448621749878 0.0034934207797050476;
	setAttr -s 9 ".kiy[0:8]"  -0.01745317317545414 0.98400217294692993 
		0.017453234642744064 -0.91392397880554199 -0.98433256149291992 -0.96756207942962646 
		0.87900251150131226 -0.3041803240776062 -0.017453186213970184;
	setAttr -s 9 ".kox[0:8]"  0.003700220724567771 0.17815619707107544 
		0.0025756573304533958 0.40588554739952087 0.17632183432579041 0.25263327360153198 
		0.47681704163551331 0.95261448621749878 0.0034934161230921745;
	setAttr -s 9 ".koy[0:8]"  -0.01745317317545414 0.98400217294692993 
		0.017453234642744064 -0.91392397880554199 -0.98433256149291992 -0.96756207942962646 
		0.87900251150131226 -0.3041803240776062 -0.017453186213970184;
createNode animCurveTA -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 -0.11334237989999998 102 20.931521 104 29.581596699999995
		 106 28.212268049999999 108 -3.4111135290000001 110 -24.775765570000001 111 -29.459523679999997
		 114 -18.28376209 116 -0.11334237989999998;
	setAttr -s 9 ".kit[1:8]"  18 1 1 9 9 9 1 1;
	setAttr -s 9 ".kot[1:8]"  18 1 1 9 9 9 1 1;
	setAttr -s 9 ".kix[0:8]"  0.0036990137305110693 0.29497963190078735 
		0.015691269189119339 0.0080085834488272667 0.1704753190279007 0.25520980358123779 
		0.81608796119689941 0.007825843058526516 0.004183243028819561;
	setAttr -s 9 ".kiy[0:8]"  0.01745317317545414 0.95550346374511719 
		0.017451144754886627 -0.017452733591198921 -0.98536199331283569 -0.96688568592071533 
		0.57792770862579346 0.017452757805585861 0.017453141510486603;
	setAttr -s 9 ".kox[0:8]"  0.0036990088410675526 0.29497963190078735 
		0.015691263601183891 0.0080085787922143936 0.1704753190279007 0.25520980358123779 
		0.81608796119689941 0.007825843058526516 0.004183243028819561;
	setAttr -s 9 ".koy[0:8]"  0.01745317317545414 0.95550346374511719 
		0.017451144754886627 -0.017452733591198921 -0.98536199331283569 -0.96688568592071533 
		0.57792770862579346 0.017452757805585861 0.017453141510486603;
createNode animCurveTU -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_keepOrientation";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_neutral";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_fist";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_relax";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_curl";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_spread";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_splay";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_break";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_flex";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 -11.587481049999999 102 -8.1615083540000004
		 103 -5.5041864550000001 106 -0.27179297019999998 108 -15.853047410000002 110 -18.65251336
		 112 -19.577395970000001 114 -15.516626829999998 116 -11.587481049999999;
	setAttr -s 9 ".kit[0:8]"  18 9 1 9 3 9 9 9 
		18;
	setAttr -s 9 ".kot[0:8]"  1 9 1 9 3 9 9 9 
		18;
	setAttr -s 9 ".kix[2:8]"  0.015832962468266487 0.74214643239974976 
		1 0.92646217346191406 0.94617354869842529 0.75385844707489014 1;
	setAttr -s 9 ".kiy[2:8]"  0.017451105639338493 -0.67023777961730957 
		0 -0.37638804316520691 0.32365992665290833 0.65703690052032471 0;
	setAttr -s 9 ".kox[0:8]"  1 0.74893534183502197 0.015832962468266487 
		0.74214643239974976 1 0.92646217346191406 0.94617354869842529 0.75385844707489014 
		1;
	setAttr -s 9 ".koy[0:8]"  0 0.66264313459396362 0.017451105639338493 
		-0.67023777961730957 0 -0.37638804316520691 0.32365992665290833 0.65703690052032471 
		0;
createNode animCurveTA -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 -9.6088123319999994 102 -34.809888919999999
		 103 -35.941293260000002 106 -17.91012855 108 -39.600324880000002 110 -25.955080679999998
		 112 11.03310078 114 16.367632100000002 116 -9.6088123319999994;
	setAttr -s 9 ".kit[4:8]"  1 9 1 9 9;
	setAttr -s 9 ".kot[0:8]"  1 9 9 9 1 9 1 9 
		9;
	setAttr -s 9 ".kix[4:8]"  0.0034934207797050476 0.17815619707107544 
		0.0025756573304533958 0.40588453412055969 0.17376987636089325;
	setAttr -s 9 ".kiy[4:8]"  -0.017453186213970184 0.98400217294692993 
		0.017453234642744064 -0.91392433643341064 -0.9847862720489502;
	setAttr -s 9 ".kox[0:8]"  0.0031744486186653376 0.25263327360153198 
		0.47681704163551331 0.95261460542678833 0.0034934161230921745 0.17815619707107544 
		0.0025756573304533958 0.40588453412055969 0.17376987636089325;
	setAttr -s 9 ".koy[0:8]"  -0.017453204840421677 -0.96756207942962646 
		0.87900251150131226 -0.30417963862419128 -0.017453186213970184 0.98400217294692993 
		0.017453234642744064 -0.91392433643341064 -0.9847862720489502;
createNode animCurveTA -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 -3.4111135290000001 102 -24.775765570000001
		 103 -29.459523679999997 106 -18.28376209 108 -0.11334237989999998 110 20.931521 112 29.581596699999995
		 114 28.212268049999999 116 -3.4111135290000001;
	setAttr -s 9 ".kit[0:8]"  9 9 9 1 1 18 1 1 
		9;
	setAttr -s 9 ".kot[1:8]"  9 9 1 1 18 1 1 9;
	setAttr -s 9 ".kix[3:8]"  0.007825843058526516 0.004183243028819561 
		0.29497963190078735 0.015691269189119339 0.0080085834488272667 0.1434461921453476;
	setAttr -s 9 ".kiy[3:8]"  0.017452757805585861 0.017453141510486603 
		0.95550346374511719 0.017451144754886627 -0.017452733591198921 -0.98965805768966675;
	setAttr -s 9 ".kox[0:8]"  0.0037444727495312691 0.25520980358123779 
		0.81608796119689941 0.007825843058526516 0.004183243028819561 0.29497963190078735 
		0.015691263601183891 0.0080085787922143936 0.1434461921453476;
	setAttr -s 9 ".koy[0:8]"  -0.017453169450163841 -0.96688568592071533 
		0.57792770862579346 0.017452757805585861 0.017453141510486603 0.95550346374511719 
		0.017451144754886627 -0.017452733591198921 -0.98965805768966675;
createNode animCurveTU -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_keepOrientation";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_neutral";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 1 108 1 116 1;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_fist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_relax";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 1 108 1 116 1;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_curl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_spread";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_splay";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_break";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_flex";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_orbit";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_nod";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_side";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_twist";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_neckStretch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_compensation";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 17 ".ktv[0:16]"  100 1.97087985 101 1.5873515220000003 102 1.0082479040000001
		 103 0.34125606200000003 104 -0.21871968829999999 105 -0.52072718380000005 106 -0.66457400749999995
		 107 -0.63164719439999994 108 -0.42839829260000001 109 -0.11392165779999999 110 0.37519536489999999
		 111 0.91755979160000001 112 1.392701534 113 1.7781541830000001 114 2.110818444 115 2.1570364450000001
		 116 1.9711527959999999;
	setAttr -s 17 ".kot[0:16]"  1 18 18 18 18 18 18 18 
		18 18 18 18 18 18 18 18 18;
	setAttr -s 17 ".kox[0:16]"  1 0.97865080833435059 0.96497690677642822 
		0.96599012613296509 0.98277312517166138 0.99530249834060669 1 0.99907249212265015 
		0.99368149042129517 0.98497742414474487 0.97560250759124756 0.97623592615127563 0.98282724618911743 
		0.98794883489608765 0.99817496538162231 1 1;
	setAttr -s 17 ".koy[0:16]"  0 -0.20553027093410492 -0.26233488321304321 
		-0.25857919454574585 -0.1848161518573761 -0.096813485026359558 0 0.043060649186372757 
		0.11223661154508591 0.17268338799476624 0.21954426169395447 0.21671034395694733 0.18452851474285126 
		0.15478090941905975 0.060388866811990738 0 0;
createNode animCurveTA -n "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 17 ".ktv[0:16]"  100 -2.9024296829999998 101 -4.047992442
		 102 -4.5870026089999998 103 -4.3293676640000003 104 -3.3931973329999998 105 -1.6928348769999999
		 106 0.27176867719999998 107 2.1546530320000001 108 3.684083292 109 4.506575636 110 4.6011794259999999
		 111 3.8450974720000004 112 2.6082736629999999 113 1.2142178379999999 114 -0.016595895100000001
		 115 -1.5167278500000001 116 -2.902454766;
	setAttr -s 17 ".kot[0:16]"  1 18 18 18 18 18 18 18 
		18 18 18 18 18 18 18 18 18;
	setAttr -s 17 ".kox[0:16]"  1 0.938618004322052 1 0.9677167534828186 
		0.86683028936386108 0.78103166818618774 0.76593583822250366 0.80213266611099243 0.88971269130706787 
		0.99241936206817627 1 0.91706925630569458 0.86729228496551514 0.8677830696105957 
		0.85908049345016479 0.8462451696395874 1;
	setAttr -s 17 ".koy[0:16]"  0 -0.34495821595191956 0 0.25204005837440491 
		0.4986032247543335 0.62449127435684204 0.64291691780090332 0.59714591503143311 0.45652085542678833 
		0.1228974387049675 0 -0.39872795343399048 -0.49779924750328064 -0.4969431459903717 
		-0.5118405818939209 -0.53279370069503784 0;
createNode animCurveTA -n "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 17 ".ktv[0:16]"  100 -9.3374728339999997 101 -10.563801809999999
		 102 -11.79749616 103 -11.92098552 104 -10.96673271 105 -9.2181272189999994 106 -8.1445917909999999
		 107 -8.2855692600000008 108 -9.3474775349999994 109 -10.56309486 110 -11.788803240000002
		 111 -11.916193010000001 112 -10.972578990000001 113 -9.2248096149999999 114 -8.1381332660000005
		 115 -8.2729099450000003 116 -9.3370801879999998;
	setAttr -s 17 ".kot[0:16]"  1 18 18 18 18 18 18 18 
		18 18 18 18 18 18 18 18 18;
	setAttr -s 17 ".kox[0:16]"  1 0.88112026453018188 0.98718565702438354 
		1 0.86139261722564697 0.85153990983963013 1 0.98339593410491943 0.8955422043800354 
		0.88261604309082031 0.98638010025024414 1 0.8623356819152832 0.85051888227462769 
		1 0.98479163646697998 1;
	setAttr -s 17 ".koy[0:16]"  0 -0.47289225459098816 -0.1595759391784668 
		0 0.50793975591659546 0.52428990602493286 0 -0.18147298693656921 -0.44497653841972351 
		-0.47009465098381042 -0.16448181867599487 0 0.50633704662322998 0.52594447135925293 
		0 -0.17373934388160706 0;
createNode animCurveTU -n "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 -6.2598829269999996 116 -6.2598829269999996;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 0 102 0 109 0 116 0;
	setAttr -s 4 ".kit[0:3]"  3 9 9 3;
	setAttr -s 4 ".kot[0:3]"  1 9 9 3;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTA -n "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  100 0 102 0 109 0 116 0;
	setAttr -s 4 ".kit[0:3]"  3 9 9 3;
	setAttr -s 4 ".kot[0:3]"  1 9 9 3;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTA -n "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  100 -23.96747345 102 7.1050482190000004
		 104 8.5422437819999999 106 -23.035496179999999 109 -43.973820910000001 110 -47.447139069999999
		 116 -23.96747345;
	setAttr -s 7 ".kit[5:6]"  1 1;
	setAttr -s 7 ".kot[0:6]"  1 9 9 9 9 1 1;
	setAttr -s 7 ".kix[5:6]"  0.017906760796904564 0.0046762875281274319;
	setAttr -s 7 ".kiy[5:6]"  -0.017450492829084396 0.01745310053229332;
	setAttr -s 7 ".kox[0:6]"  0.002574611222371459 0.27140280604362488 
		0.29099041223526001 0.21318699419498444 0.35155969858169556 0.017906753346323967 
		0.0046762875281274319;
	setAttr -s 7 ".koy[0:6]"  0.017453234642744064 0.96246582269668579 
		-0.95672595500946045 -0.97701144218444824 -0.936165452003479 -0.017450492829084396 
		0.01745310053229332;
createNode animCurveTU -n "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0.5 116 0.5;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 6.8737701020000008 102 13.490784039999999
		 106 25.399111380000001 108 28.188377760000002 110 28.58289916 111 25.965529880000002
		 113 8.4671068409999997 114 5.3541715669999999 116 6.8737701020000008;
	setAttr -s 9 ".kit[1:8]"  9 1 1 1 18 9 9 1;
	setAttr -s 9 ".kot[1:8]"  9 1 1 1 18 9 9 1;
	setAttr -s 9 ".kix[0:8]"  0.025338374078273773 0.59602487087249756 
		0.020428454503417015 0.053124867379665375 0.066896110773086548 0.32342526316642761 
		0.3164362907409668 0.97418320178985596 0.014859428629279137;
	setAttr -s 9 ".kiy[0:8]"  0.017447687685489655 0.80296593904495239 
		0.017449650913476944 0.017428645864129066 -0.017414197325706482 -0.94625377655029297 
		-0.94861376285552979 -0.22575883567333221 0.017451366409659386;
	setAttr -s 9 ".kox[0:8]"  0.025338374078273773 0.59602487087249756 
		0.020428461953997612 0.053124867379665375 0.066896125674247742 0.32342526316642761 
		0.3164362907409668 0.97418320178985596 0.014859428629279137;
	setAttr -s 9 ".koy[0:8]"  0.017447687685489655 0.80296593904495239 
		0.017449650913476944 0.017428645864129066 -0.017414197325706482 -0.94625377655029297 
		-0.94861376285552979 -0.22575883567333221 0.017451366409659386;
createNode animCurveTA -n "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  100 25.97107553 102 27.635681900000005 103 26.32852579
		 106 18.421989020000002 109 13.590503350000001 114 24.486072709999998 116 25.97107553;
	setAttr -s 7 ".kit[1:6]"  18 18 9 1 9 1;
	setAttr -s 7 ".kot[1:6]"  18 18 9 1 9 1;
	setAttr -s 7 ".kix[0:6]"  0.021925985813140869 1 0.70532047748565674 
		0.7336113452911377 0.44757452607154846 0.79167020320892334 0.024940924718976021;
	setAttr -s 7 ".kiy[0:6]"  0.017449097707867622 0 -0.70888864994049072 
		-0.6795693039894104 0.015607547946274281 0.61094874143600464 0.017447862774133682;
	setAttr -s 7 ".kox[0:6]"  0.021925985813140869 1 0.70532041788101196 
		0.7336113452911377 0.44757437705993652 0.79167020320892334 0.024940924718976021;
	setAttr -s 7 ".koy[0:6]"  0.017449097707867622 0 -0.70888859033584595 
		-0.6795693039894104 0.015607548877596855 0.61094874143600464 0.017447862774133682;
createNode animCurveTA -n "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 50.613044449999997 102 15.974210180000002
		 103 -3.3951540019999999 106 -44.785837630000003 108 -48.917888230000003 110 -32.996003170000002
		 114 45.194132250000003 116 50.613044449999997;
	setAttr -s 8 ".kit[0:7]"  1 9 1 9 9 9 9 1;
	setAttr -s 8 ".kot[0:7]"  1 9 1 9 9 9 9 1;
	setAttr -s 8 ".kix[0:7]"  0.034734692424535751 0.12628529965877533 
		0.002353231655433774 0.24410896003246307 0.61383515596389771 0.14457769691944122 
		0.16228727996349335 0.010578734800219536;
	setAttr -s 8 ".kiy[0:7]"  -0.017442760989069939 -0.99199396371841431 
		-0.01745324395596981 -0.96974784135818481 0.78943425416946411 0.98949348926544189 
		0.98674356937408447 -0.017452316358685493;
	setAttr -s 8 ".kox[0:7]"  0.034734692424535751 0.12628529965877533 
		0.0023532269988209009 0.24410896003246307 0.61383515596389771 0.14457769691944122 
		0.16228727996349335 0.010578740388154984;
	setAttr -s 8 ".koy[0:7]"  -0.017442760989069939 -0.99199396371841431 
		-0.01745324395596981 -0.96974784135818481 0.78943425416946411 0.98949348926544189 
		0.98674356937408447 -0.017452316358685493;
createNode animCurveTU -n "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 1 115 1 116 1;
	setAttr -s 3 ".kit[2]"  9;
	setAttr -s 3 ".kot[0:2]"  1 3 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_compensation";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 3;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  100 0 101 0 108 0 110 0 116 0;
	setAttr -s 5 ".kit[0:4]"  18 9 3 9 18;
	setAttr -s 5 ".kot[0:4]"  1 9 3 9 18;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTA -n "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  100 0 101 0 108 0 110 0 116 0;
	setAttr -s 5 ".kit[0:4]"  18 9 3 9 18;
	setAttr -s 5 ".kot[0:4]"  1 9 3 9 18;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTA -n "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 -38.167009059999998 101 -43.973820910000001
		 102 -47.447139069999999 108 -23.96747345 110 7.1050482190000004 112 8.5422437819999999
		 114 -23.035496179999999 116 -38.167004630000001;
	setAttr -s 8 ".kit[0:7]"  18 9 1 1 9 9 9 18;
	setAttr -s 8 ".kot[0:7]"  1 9 1 1 9 9 9 18;
	setAttr -s 8 ".kix[2:7]"  0.017906760796904564 0.0046762875281274319 
		0.27140280604362488 0.29099041223526001 0.19258925318717957 1;
	setAttr -s 8 ".kiy[2:7]"  -0.017450492829084396 0.01745310053229332 
		0.96246582269668579 -0.95672595500946045 -0.98127949237823486 0;
	setAttr -s 8 ".kox[0:7]"  1 0.44284850358963013 0.017906753346323967 
		0.0046762875281274319 0.27140280604362488 0.29099041223526001 0.19258925318717957 
		1;
	setAttr -s 8 ".koy[0:7]"  0 -0.89659643173217773 -0.017450492829084396 
		0.01745310053229332 0.96246582269668579 -0.95672595500946045 -0.98127949237823486 
		0;
createNode animCurveTU -n "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 1 108 1 116 1;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0.5 108 0.5 116 0.5;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  100 28.188377760000002 102 28.58289916 103 25.965529880000002
		 105 8.4671068409999997 106 5.3541715669999999 108 6.8737701020000008 110 13.490784039999999
		 114 25.399111380000001 116 28.188377760000002;
	setAttr -s 9 ".kit[2:8]"  18 9 9 1 9 1 1;
	setAttr -s 9 ".kot[2:8]"  18 9 9 1 9 1 1;
	setAttr -s 9 ".kix[0:8]"  0.053124867379665375 0.066896110773086548 
		0.32342526316642761 0.3164362907409668 0.97418344020843506 0.014859428629279137 0.59602487087249756 
		0.020428454503417015 0.053124867379665375;
	setAttr -s 9 ".kiy[0:8]"  0.017428645864129066 -0.017414197325706482 
		-0.94625377655029297 -0.94861376285552979 -0.22575798630714417 0.017451366409659386 
		0.80296593904495239 0.017449650913476944 0.017428645864129066;
	setAttr -s 9 ".kox[0:8]"  0.053124867379665375 0.066896125674247742 
		0.32342526316642761 0.3164362907409668 0.97418344020843506 0.014859428629279137 0.59602487087249756 
		0.020428461953997612 0.053124867379665375;
	setAttr -s 9 ".koy[0:8]"  0.017428645864129066 -0.017414197325706482 
		-0.94625377655029297 -0.94861376285552979 -0.22575798630714417 0.017451366409659386 
		0.80296593904495239 0.017449650913476944 0.017428645864129066;
createNode animCurveTA -n "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 14.33581242 101 13.590503350000001 106 24.486072709999998
		 108 25.97107553 110 27.635681900000005 111 26.32852579 114 18.421989020000002 116 14.335813220000002;
	setAttr -s 8 ".kit[1:7]"  1 9 1 18 18 9 18;
	setAttr -s 8 ".kot[0:7]"  1 1 9 1 18 18 9 18;
	setAttr -s 8 ".kix[1:7]"  0.44757452607154846 0.79167068004608154 
		0.024940924718976021 1 0.70532047748565674 0.69084018468856812 1;
	setAttr -s 8 ".kiy[1:7]"  0.015607547946274281 0.61094802618026733 
		0.017447862774133682 0 -0.70888864994049072 -0.72300750017166138 0;
	setAttr -s 8 ".kox[0:7]"  1 0.44757437705993652 0.79167068004608154 
		0.024940924718976021 1 0.70532041788101196 0.69084018468856812 1;
	setAttr -s 8 ".koy[0:7]"  0 0.015607548877596855 0.61094802618026733 
		0.017447862774133682 0 -0.70888859033584595 -0.72300750017166138 0;
createNode animCurveTA -n "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 -48.917888230000003 102 -32.996003170000002
		 106 45.194132250000003 108 50.613044449999997 110 15.974210180000002 111 -3.3951540019999999
		 114 -44.785837630000003 116 -48.917888230000003;
	setAttr -s 8 ".kit[3:7]"  1 9 1 9 9;
	setAttr -s 8 ".kot[0:7]"  1 9 9 1 9 1 9 9;
	setAttr -s 8 ".kix[3:7]"  0.010578734800219536 0.12628529965877533 
		0.002353231655433774 0.2441084086894989 0.74274939298629761;
	setAttr -s 8 ".kiy[3:7]"  -0.017452316358685493 -0.99199396371841431 
		-0.01745324395596981 -0.96974796056747437 -0.66956961154937744;
	setAttr -s 8 ".kox[0:7]"  0.0050244624726474285 0.14457769691944122 
		0.16228759288787842 0.010578740388154984 0.12628529965877533 0.0023532269988209009 
		0.2441084086894989 0.74274939298629761;
	setAttr -s 8 ".koy[0:7]"  0.017453072592616081 0.98949348926544189 
		0.9867435097694397 -0.017452316358685493 -0.99199396371841431 -0.01745324395596981 
		-0.96974796056747437 -0.66956961154937744;
createNode animCurveTU -n "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 108 0 116 0;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_compensation";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 1 108 1 116 1;
	setAttr -s 3 ".kit[1:2]"  3 18;
	setAttr -s 3 ".kot[0:2]"  1 3 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 9;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_followHead";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_displayGeo";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_followHead";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_displayGeo";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  100 -0.78826787259999997 104 -0.29388055569999999
		 107 0.5596324238 108 0.76510452819999997 116 -0.78826787259999997;
	setAttr -s 5 ".kit[1:4]"  9 9 1 1;
	setAttr -s 5 ".kot[1:4]"  9 9 1 1;
	setAttr -s 5 ".kix[0:4]"  0.22539511322975159 0.99648904800415039 
		0.99339395761489868 0.42697605490684509 0.25644925236701965;
	setAttr -s 5 ".kiy[0:4]"  -0.017004175111651421 0.083723865449428558 
		0.11475400626659393 0.015782365575432777 -0.016869613900780678;
	setAttr -s 5 ".kox[0:4]"  0.22539511322975159 0.99648904800415039 
		0.99339395761489868 0.42697605490684509 0.25644925236701965;
	setAttr -s 5 ".koy[0:4]"  -0.017004175111651421 0.083723865449428558 
		0.11475400626659393 0.015782365575432777 -0.016869613900780678;
createNode animCurveTA -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  100 -0.87645283370000004 101 -0.41256533150000008
		 103 0.38056234410000001 104 0.51725931189999996 107 -0.95269540520000007 109 -0.41256533150000008
		 111 0.38056234410000001 112 0.51725931189999996 115 -0.95269540520000007 116 -0.87645300640000001;
	setAttr -s 10 ".kit[0:9]"  18 9 9 1 9 1 9 1 
		9 18;
	setAttr -s 10 ".kot[0:9]"  1 9 9 1 9 1 9 1 
		9 18;
	setAttr -s 10 ".kix[3:9]"  0.91472983360290527 0.99672418832778931 
		0.067718423902988434 0.99097895622253418 0.91472983360290527 0.9886399507522583 1;
	setAttr -s 10 ".kiy[3:9]"  0.0070522814057767391 -0.080876581370830536 
		0.017413226887583733 0.13401764631271362 0.0070522814057767391 -0.15030349791049957 
		0;
	setAttr -s 10 ".kox[0:9]"  1 0.98369503021240234 0.99097895622253418 
		0.91472983360290527 0.99672418832778931 0.067718520760536194 0.99097895622253418 
		0.91472983360290527 0.9886399507522583 1;
	setAttr -s 10 ".koy[0:9]"  0 0.17984466254711151 0.13401764631271362 
		0.0070522814057767391 -0.080876581370830536 0.017413226887583733 0.13401764631271362 
		0.0070522814057767391 -0.15030349791049957 0;
createNode animCurveTU -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1_followHead";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_helmet_ctrl_outPutAnimBank_1_displayGeo";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 15 ".ktv[0:14]"  100 0.31827907439999997 101 0.4049676995
		 102 0.4530718172 103 0.29581375970000001 104 0.077894175349999997 105 0.066552093919999999
		 106 0.1086999993 108 0.31827907439999997 109 0.4049676995 110 0.4530718172 111 0.29581375970000001
		 112 0.077894175349999997 113 0.066552093919999999 114 0.1086999993 116 0.31827907439999997;
	setAttr -s 15 ".kit[2:14]"  1 9 1 9 1 9 9 1 
		9 1 9 1 9;
	setAttr -s 15 ".kot[0:14]"  1 9 1 9 1 9 1 9 
		9 1 9 1 9 1 9;
	setAttr -s 15 ".kix[2:14]"  0.9911806583404541 0.20854379236698151 
		0.76428687572479248 0.93320244550704956 0.5256914496421814 0.37541449069976807 0.51038181781768799 
		0.9911806583404541 0.20854379236698151 0.71677029132843018 0.93320244550704956 0.5256914496421814 
		0.35661917924880981;
	setAttr -s 15 ".kiy[2:14]"  -0.13251763582229614 -0.97801297903060913 
		-0.64487648010253906 0.35935121774673462 0.85067540407180786 0.92685705423355103 
		0.85994786024093628 -0.13251763582229614 -0.97801297903060913 -0.69730931520462036 
		0.35935121774673462 0.85067540407180786 0.9342498779296875;
	setAttr -s 15 ".kox[0:14]"  0.41897034645080566 0.51038181781768799 
		0.99118059873580933 0.20854379236698151 0.76428687572479248 0.93320244550704956 0.52569115161895752 
		0.37541449069976807 0.51038181781768799 0.99118059873580933 0.20854379236698151 0.71677041053771973 
		0.93320244550704956 0.52569115161895752 0.35661917924880981;
	setAttr -s 15 ".koy[0:14]"  0.90799993276596069 0.85994786024093628 
		-0.13251775503158569 -0.97801297903060913 -0.64487648010253906 0.35935121774673462 
		0.85067546367645264 0.92685705423355103 0.85994786024093628 -0.13251775503158569 
		-0.97801297903060913 -0.69730913639068604 0.35935121774673462 0.85067546367645264 
		0.9342498779296875;
createNode animCurveTL -n "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  100 -0.09964276926 101 -0.32984209869999997
		 102 -0.37283814479999999 104 -0.12622477639999999 106 -0.056659925280000002 108 -0.09964276926
		 109 -0.32984209869999997 110 -0.37283814479999999 112 -0.12622477639999999 114 -0.056659925280000002
		 116 -0.09964276926;
	setAttr -s 11 ".kot[0:10]"  1 9 9 9 9 9 9 9 
		9 9 9;
	setAttr -s 11 ".kox[0:10]"  0.17119701206684113 0.28102916479110718 
		0.50772720575332642 0.4515221118927002 0.98647850751876831 0.40217754244804382 0.28102916479110718 
		0.50772720575332642 0.4515221118927002 0.98647838830947876 0.88090300559997559;
	setAttr -s 11 ".koy[0:10]"  -0.98523682355880737 -0.95969921350479126 
		0.86151790618896484 0.89225995540618896 0.1638907790184021 -0.91556167602539063 -0.95969921350479126 
		0.86151790618896484 0.89225995540618896 0.1638912707567215 -0.47329691052436829;
createNode animCurveTA -n "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  100 0.13781582519999999 101 -0.0057802024590000002
		 103 0.076445086300000006 105 0.47617037340000001 107 0.31218795799999999 109 -0.0057802024590000002
		 111 0.076445086300000006 113 0.47617037340000001 115 0.31218795799999999 116 0.13781589029999999;
	setAttr -s 10 ".kit[0:9]"  18 9 9 1 9 9 9 3 
		9 18;
	setAttr -s 10 ".kot[0:9]"  1 9 9 1 9 9 9 3 
		9 18;
	setAttr -s 10 ".kix[3:9]"  0.72200191020965576 0.31507575511932373 
		0.56157702207565308 0.31507492065429688 1 0.33425796031951904 1;
	setAttr -s 10 ".kiy[3:9]"  -0.6918911337852478 -0.94906651973724365 
		-0.82742446660995483 0.94906681776046753 0 -0.94248157739639282 0;
	setAttr -s 10 ".kox[0:9]"  1 0.89032202959060669 0.31507492065429688 
		0.72200191020965576 0.31507575511932373 0.56157702207565308 0.31507492065429688 1 
		0.33425796031951904 1;
	setAttr -s 10 ".koy[0:9]"  0 -0.45533141493797302 0.94906681776046753 
		-0.6918911337852478 -0.94906651973724365 -0.82742446660995483 0.94906681776046753 
		0 -0.94248157739639282 0;
createNode animCurveTA -n "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 15 ".ktv[0:14]"  100 -0.38534927400000002 101 -0.50266245539999999
		 102 -0.56776035120000001 103 -0.35494762060000001 104 -0.0600434195 105 -0.044694512370000002
		 106 -0.1017320402 108 -0.38534927400000002 109 -0.50266245539999999 110 -0.56776035120000001
		 111 -0.35494762060000001 112 -0.0600434195 113 -0.044694512370000002 114 -0.1017320402
		 116 -0.38534927400000002;
	setAttr -s 15 ".kit[2:14]"  1 9 1 9 1 9 9 1 
		9 1 9 1 9;
	setAttr -s 15 ".kot[0:14]"  1 9 1 9 1 9 1 9 
		9 1 9 1 9 1 9;
	setAttr -s 15 ".kix[2:14]"  0.98402369022369385 0.1556476354598999 
		0.6588369607925415 0.88681423664093018 0.41538801789283752 0.28673672676086426 0.40164071321487427 
		0.98402369022369385 0.1556476354598999 0.60486799478530884 0.88681423664093018 0.41538801789283752 
		0.27147689461708069;
	setAttr -s 15 ".kiy[2:14]"  0.17803733050823212 0.98781263828277588 
		0.75228571891784668 -0.462126225233078 -0.90964430570602417 -0.95800936222076416 
		-0.91579735279083252 0.17803733050823212 0.98781263828277588 0.79632580280303955 
		-0.462126225233078 -0.90964430570602417 -0.96244490146636963;
	setAttr -s 15 ".kox[0:14]"  0.32272329926490784 0.40164071321487427 
		0.98402369022369385 0.1556476354598999 0.6588369607925415 0.88681423664093018 0.41538774967193604 
		0.28673672676086426 0.40164071321487427 0.98402369022369385 0.1556476354598999 0.60486805438995361 
		0.88681423664093018 0.41538774967193604 0.27147689461708069;
	setAttr -s 15 ".koy[0:14]"  -0.94649332761764526 -0.91579735279083252 
		0.17803762853145599 0.98781263828277588 0.75228577852249146 -0.462126225233078 -0.90964436531066895 
		-0.95800936222076416 -0.91579735279083252 0.17803762853145599 0.98781263828277588 
		0.79632568359375 -0.462126225233078 -0.90964436531066895 -0.96244490146636963;
createNode animCurveTL -n "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 104 0 116 0;
	setAttr -s 3 ".kit[1:2]"  9 18;
	setAttr -s 3 ".kot[0:2]"  1 9 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  100 -0.09964276926 101 -0.32984209869999997
		 102 -0.37283814479999999 104 -0.12622477639999999 106 -0.056659925280000002 108 -0.09964276926
		 109 -0.32984209869999997 110 -0.37283814479999999 112 -0.12622477639999999 114 -0.056659925280000002
		 116 -0.09964276926;
	setAttr -s 11 ".kot[0:10]"  1 9 9 9 9 9 9 9 
		9 9 9;
	setAttr -s 11 ".kox[0:10]"  0.17119701206684113 0.28102916479110718 
		0.50772720575332642 0.4515221118927002 0.98647850751876831 0.40217754244804382 0.28102916479110718 
		0.50772720575332642 0.4515221118927002 0.98647838830947876 0.88090300559997559;
	setAttr -s 11 ".koy[0:10]"  -0.98523682355880737 -0.95969921350479126 
		0.86151790618896484 0.89225995540618896 0.1638907790184021 -0.91556167602539063 -0.95969921350479126 
		0.86151790618896484 0.89225995540618896 0.1638912707567215 -0.47329691052436829;
createNode animCurveTA -n "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  100 0.0022790569489999999 101 0.0077029587559999998
		 104 0.020078635139999999 107 0.016190423410000002 109 -0.0038040820919999999 112 -0.017655130929999999
		 116 0.0022790569489999999;
	setAttr -s 7 ".kit[0:6]"  18 1 9 9 9 9 18;
	setAttr -s 7 ".kot[0:6]"  1 1 9 9 9 9 18;
	setAttr -s 7 ".kix[1:6]"  0.99478626251220703 0.99937528371810913 
		0.99294561147689819 0.98598134517669678 0.99976414442062378 1;
	setAttr -s 7 ".kiy[1:6]"  0.10198240727186203 0.035342305898666382 
		-0.11857102066278458 -0.1668555736541748 0.021720392629504204 0;
	setAttr -s 7 ".kox[0:6]"  1 0.99478626251220703 0.99937528371810913 
		0.99294561147689819 0.98598134517669678 0.99976414442062378 1;
	setAttr -s 7 ".koy[0:6]"  0 0.10198240727186203 0.035342305898666382 
		-0.11857102066278458 -0.1668555736541748 0.021720392629504204 0;
createNode animCurveTL -n "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  100 -0.00070179403619999997 101 0.0049434774550000003
		 104 0.019861748620000001 107 0.0157471333 109 -0.002905452919 112 -0.017730314260000001
		 116 -0.00070179403619999997;
	setAttr -s 7 ".kit[0:6]"  18 1 9 9 9 9 18;
	setAttr -s 7 ".kot[0:6]"  1 1 9 9 9 9 18;
	setAttr -s 7 ".kix[1:6]"  0.99322038888931274 0.99898833036422729 
		0.99358290433883667 0.98627835512161255 0.9999690055847168 1;
	setAttr -s 7 ".kiy[1:6]"  0.11624634265899658 0.044969644397497177 
		-0.11310534924268723 -0.16509056091308594 0.0078699737787246704 0;
	setAttr -s 7 ".kox[0:6]"  1 0.99322038888931274 0.99898833036422729 
		0.99358290433883667 0.98627835512161255 0.9999690055847168 1;
	setAttr -s 7 ".koy[0:6]"  0 0.11624634265899658 0.044969644397497177 
		-0.11310534924268723 -0.16509056091308594 0.0078699737787246704 0;
createNode animCurveTL -n "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  100 0 102 0 103 0 106 0 107 0 108 0 110 0
		 116 0;
	setAttr -s 8 ".kit[4:7]"  9 3 3 3;
	setAttr -s 8 ".kot[0:7]"  1 3 3 3 9 3 3 3;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 13 ".ktv[0:12]"  100 -0.25987531429999999 102 -0.45320522289999998
		 104 -0.34096804780000001 105 -0.045147052719999997 106 0.03799707544 107 -0.034840934160000003
		 108 -0.25987531429999999 110 -0.45320522289999998 112 -0.34096804780000001 113 -0.045147052719999997
		 114 0.03799707544 115 -0.034840934160000003 116 -0.25987531429999999;
	setAttr -s 13 ".kit[0:12]"  1 9 9 9 9 9 1 9 
		9 9 9 9 1;
	setAttr -s 13 ".kot[0:12]"  1 9 9 9 9 9 1 9 
		9 9 9 9 1;
	setAttr -s 13 ".kix[0:12]"  0.25843057036399841 0.89197707176208496 
		0.28212904930114746 0.20654888451099396 0.99180376529693604 0.25938084721565247 0.22504289448261261 
		0.89197707176208496 0.28212904930114746 0.20654888451099396 0.99180364608764648 0.25937941670417786 
		0.22504289448261261;
	setAttr -s 13 ".kiy[0:12]"  -0.9660298228263855 -0.45208081603050232 
		0.95937645435333252 0.97843629121780396 0.12776996195316315 -0.96577507257461548 
		-0.97434884309768677 -0.45208081603050232 0.95937645435333252 0.97843629121780396 
		0.12777069211006165 -0.96577554941177368 -0.97434884309768677;
	setAttr -s 13 ".kox[0:12]"  0.25843054056167603 0.89197707176208496 
		0.28212904930114746 0.20654888451099396 0.99180376529693604 0.25938084721565247 0.22504289448261261 
		0.89197707176208496 0.28212904930114746 0.20654888451099396 0.99180364608764648 0.25937941670417786 
		0.22504289448261261;
	setAttr -s 13 ".koy[0:12]"  -0.9660298228263855 -0.45208081603050232 
		0.95937645435333252 0.97843629121780396 0.12776996195316315 -0.96577507257461548 
		-0.97434884309768677 -0.45208081603050232 0.95937645435333252 0.97843629121780396 
		0.12777069211006165 -0.96577554941177368 -0.97434884309768677;
createNode animCurveTL -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  100 -0.02000457445 101 -0.01356203773 103 0.0077274893529999996
		 105 0.0069961254499999997 107 -0.0069559523630000003 108 -0.02019223874 110 -0.01356203773
		 112 0.0077274893529999996 114 0.0069961254499999997 116 -0.02;
	setAttr -s 10 ".kit[0:9]"  18 9 9 9 9 1 9 9 
		9 1;
	setAttr -s 10 ".kot[0:9]"  18 9 9 9 9 1 9 9 
		9 1;
	setAttr -s 10 ".kix[5:9]"  0.99057894945144653 0.98511421680450439 
		0.99184614419937134 0.9853140115737915 0.9905167818069458;
	setAttr -s 10 ".kiy[5:9]"  -0.13694293797016144 0.1719009131193161 
		0.12744095921516418 -0.17075194418430328 -0.13739201426506042;
	setAttr -s 10 ".kox[5:9]"  0.99057894945144653 0.98511421680450439 
		0.99184614419937134 0.9853140115737915 0.9905167818069458;
	setAttr -s 10 ".koy[5:9]"  -0.13694293797016144 0.1719009131193161 
		0.12744095921516418 -0.17075194418430328 -0.13739213347434998;
createNode animCurveTA -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 107 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 107 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 107 0 116 0;
	setAttr -s 3 ".kot[0:2]"  1 9 9;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  100 1.0184959570000001 101 1.0045322400000001
		 103 0.94844042959999997 104 0.95049219190000001 107 1.0134599959999999 108 1.0184959570000001
		 109 1.0045322400000001 111 0.94844042959999997 112 0.95049219190000001 115 1.0134599959999999
		 116 1.0184959570000001;
	setAttr -s 11 ".kit[0:10]"  3 9 9 9 9 9 9 9 
		9 9 9;
	setAttr -s 11 ".kot[0:10]"  3 9 9 9 9 9 9 9 
		9 9 9;
createNode animCurveTU -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  100 1.0184959570000001 101 1.0045322400000001
		 103 0.94844042959999997 104 0.95049219190000001 107 1.0134599959999999 108 1.0184959570000001
		 109 1.0045322400000001 111 0.94844042959999997 112 0.95049219190000001 115 1.0134599959999999
		 116 1.0184959570000001;
	setAttr -s 11 ".kit[0:10]"  3 9 9 9 9 9 9 9 
		9 9 9;
	setAttr -s 11 ".kot[0:10]"  3 9 9 9 9 9 9 9 
		9 9 9;
createNode animCurveTU -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  100 1.0184959570000001 101 1.0045322400000001
		 103 0.94844042959999997 104 0.95049219190000001 107 1.0134599959999999 108 1.0184959570000001
		 109 1.0045322400000001 111 0.94844042959999997 112 0.95049219190000001 115 1.0134599959999999
		 116 1.0184959570000001;
	setAttr -s 11 ".kit[0:10]"  3 9 9 9 9 9 9 9 
		9 9 9;
	setAttr -s 11 ".kot[0:10]"  3 9 9 9 9 9 9 9 
		9 9 9;
createNode animCurveTU -n "vicky_original:hair_ex_ctrl_outPutAnimBank_1_subCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  100 0 107 0 116 0;
	setAttr -s 3 ".kit[2]"  18;
	setAttr -s 3 ".kot[0:2]"  1 9 18;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "vicky_original:mov_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  100 0;
createNode animCurveTL -n "vicky_original:mov_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  100 0;
createNode animCurveTL -n "vicky_original:mov_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  100 0;
createNode animCurveTA -n "vicky_original:mov_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  100 0;
createNode animCurveTA -n "vicky_original:mov_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  100 0;
createNode animCurveTA -n "vicky_original:mov_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  100 0;
createNode animCurveTU -n "vicky_original:top_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "vicky_original:top_ctrl_outPutAnimBank_1_globalScale";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:top_ctrl_outPutAnimBank_1_headRes";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:top_ctrl_outPutAnimBank_1_bodyRes";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:top_ctrl_outPutAnimBank_1_shoe";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:top_ctrl_outPutAnimBank_1_helmetCtrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:top_ctrl_outPutAnimBank_1_hairCtrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:top_ctrl_outPutAnimBank_1_clothCtrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_ratio";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_roll";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_Sub_Ctrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_ExtraDeformers";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:tongueCon_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:tongueCon_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:tongueCon_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongueCon_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongueCon_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:tongueCon_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:tongueCurve_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_jaw_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_pupilRadz_end_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "vicky_original:l_pupilRadz_end_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 90 116 90;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_pupilRadz_end_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:l_pupilRadz_end_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_pupilRadz_end_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 9.9999999999999998e-013 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_pupilRadz_end_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 9.9999999999999998e-013 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_pupilRadz_end_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 9.9999999999999998e-013 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 -0.086068930269999996 116 -0.086068930269999996;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:l_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 -0.15266249330000001 116 -0.15266249330000001;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_eye_ctrl_outPutAnimBank_1_crossEyeFix";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_eye_ctrl_outPutAnimBank_1_crossEyeRate";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0.5 116 0.5;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_eye_ctrl_outPutAnimBank_1_Iris_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:l_eye_ctrl_outPutAnimBank_1_Pupil_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0.086 116 0.086;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:r_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 -0.153 116 -0.153;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_eye_ctrl_outPutAnimBank_1_crossEyeFix";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_eye_ctrl_outPutAnimBank_1_crossEyeRate";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0.5 116 0.5;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_eye_ctrl_outPutAnimBank_1_Iris_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:r_eye_ctrl_outPutAnimBank_1_Pupil_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_l_eye_offset";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_r_eye_offset";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 9.591906153 116 9.591906153;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1.0646416519999999 116 1.0646416519999999;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 2.145436664 116 2.145436664;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 2.145436664 116 2.145436664;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 2.145436664 116 2.145436664;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_tx";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0.009 116 0.009;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_sc";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_bothEye_offset";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 14.17 116 14.17;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_irisSize_temp";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 -1.7 116 -1.7;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:m_eye_ctrl_outPutAnimBank_1_pupilSize_temp";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 -0.5 116 -0.5;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "vicky_original:head_squash_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 1 116 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "vicky_original:head_squash_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:head_squash_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "vicky_original:head_squash_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  100 0 116 0;
	setAttr -s 2 ".kot[0:1]"  1 18;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
select -ne :time1;
	setAttr ".o" 116;
	setAttr ".unw" 116;
select -ne :renderPartition;
	setAttr -s 58 ".st";
select -ne :initialShadingGroup;
	setAttr -s 336 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 6 ".gn";
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -s 58 ".s";
select -ne :defaultTextureList1;
	setAttr -s 168 ".tx";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 564 ".u";
select -ne :defaultRenderingList1;
	setAttr -s 7 ".r";
select -ne :renderGlobalsList1;
select -ne :defaultRenderGlobals;
	setAttr ".mcfr" 25;
	setAttr ".an" yes;
	setAttr ".ep" 4;
	setAttr ".pff" yes;
	setAttr ".ifp" -type "string" "<Layer>/<Scene>_<Layer>";
	setAttr ".pram" -type "string" "";
select -ne :defaultRenderQuality;
	setAttr ".eaa" 0;
	setAttr ".ufil" yes;
	setAttr ".ss" 2;
select -ne :defaultResolution;
	setAttr ".w" 1280;
	setAttr ".h" 720;
	setAttr ".pa" 1;
	setAttr ".dar" 1.7779999971389771;
	setAttr ".ldar" yes;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr ".hwfr" 25;
select -ne :defaultHardwareRenderGlobals;
	setAttr ".fn" -type "string" "im";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
select -ne :characterPartition;
	setAttr -s 24 ".st";
select -ne :ikSystem;
	setAttr -s 14 ".sol";
connectAttr "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_wide.o" "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.wide"
		;
connectAttr "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_thick.o" "vicky_original:m_spineA_waistFree_ctrl_outPutAnimBank_1.thick"
		;
connectAttr "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotatePivotY.o" "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1.rpy"
		;
connectAttr "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_wide.o" "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1.wide"
		;
connectAttr "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1_thick.o" "vicky_original:m_spineA_chest_ctrl_outPutAnimBank_1.thick"
		;
connectAttr "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotatePivotY.o" "vicky_original:m_spineA_waist_ctrl_outPutAnimBank_1.rpy"
		;
connectAttr "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotatePivotY.o" "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1.rpy"
		;
connectAttr "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_wide.o" "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1.wide"
		;
connectAttr "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_thick.o" "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1.thick"
		;
connectAttr "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1_autoStretch.o" "vicky_original:m_spineA_hip_ctrl_outPutAnimBank_1.autoStretch"
		;
connectAttr "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_spineA_body_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot.o" "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.followBody_2_followFoot"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.footHeight"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.footRoll"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.toeBend"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.heelTurn"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.toeTurn"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footSide.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.footSide"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.thighStretch"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.shankStretch"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.autoStretch"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.preferredAngle"
		;
connectAttr "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist.o" "vicky_original:l_legA_foot_IK_ctrl_outPutAnimBank_1.kneeTwist"
		;
connectAttr "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_legA_heel_IK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot.o" "vicky_original:r_legA_knee_IK_ctrl_outPutAnimBank_1.followBody_2_followFoot"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.footHeight"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.footRoll"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.toeBend"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.heelTurn"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.toeTurn"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footSide.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.footSide"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.thighStretch"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.shankStretch"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.autoStretch"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.preferredAngle"
		;
connectAttr "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist.o" "vicky_original:r_legA_foot_IK_ctrl_outPutAnimBank_1.kneeTwist"
		;
connectAttr "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_legA_pelvis_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_legA_pelvis_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_shoulder_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_shoulder_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1_followBody.o" "vicky_original:m_armA_shoulder_ctrl_outPutAnimBank_1.followBody"
		;
connectAttr "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_thumb_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_thumb_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_index_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_index_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_index_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_index_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_middle_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_middle_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_middle_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_middle_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_ring_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_ring_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_ring_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_armA_ring_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_keepOrientation.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.keepOrientation"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_FK_2_IK.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.FK_2_IK"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_globalIK_2_localIK.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.globalIK_2_localIK"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_neutral.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.neutral"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_fist.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.fist"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_relax.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.relax"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_curl.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.curl"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_spread.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.spread"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_splay.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.splay"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_break.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.break"
		;
connectAttr "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1_flex.o" "vicky_original:l_armA_wrist_ctrl_outPutAnimBank_1.flex"
		;
connectAttr "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_thumb_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_thumb_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_thumb_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_index_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_index_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_index_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_index_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_middle_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_middle_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_middle_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_middle_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_ring_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_ring_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_ring_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_armA_ring_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_keepOrientation.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.keepOrientation"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_FK_2_IK.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.FK_2_IK"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_globalIK_2_localIK.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.globalIK_2_localIK"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_neutral.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.neutral"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_fist.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.fist"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_relax.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.relax"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_curl.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.curl"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_spread.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.spread"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_splay.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.splay"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_break.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.break"
		;
connectAttr "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1_flex.o" "vicky_original:r_armA_wrist_ctrl_outPutAnimBank_1.flex"
		;
connectAttr "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_orbit.o" "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1.orbit"
		;
connectAttr "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_nod.o" "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1.nod"
		;
connectAttr "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_side.o" "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1.side"
		;
connectAttr "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_twist.o" "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1.twist"
		;
connectAttr "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_neckStretch.o" "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1.neckStretch"
		;
connectAttr "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1_compensation.o" "vicky_original:m_spineA_head_ctrl_outPutAnimBank_1.compensation"
		;
connectAttr "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:m_spineA_neck_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_spineA_neck_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_spineA_neck_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_twistBlend.o" "vicky_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1.twistBlend"
		;
connectAttr "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_twistBlend.o" "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.twistBlend"
		;
connectAttr "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_compensation.o" "vicky_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1.compensation"
		;
connectAttr "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_twistBlend.o" "vicky_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1.twistBlend"
		;
connectAttr "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_twistBlend.o" "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.twistBlend"
		;
connectAttr "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_compensation.o" "vicky_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1.compensation"
		;
connectAttr "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK.o" "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1.FK_2_IK"
		;
connectAttr "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK.o" "vicky_original:l_legA_ankle_ctrl_outPutAnimBank_1.globalIK_2_localIK"
		;
connectAttr "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK.o" "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1.FK_2_IK"
		;
connectAttr "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK.o" "vicky_original:r_legA_ankle_ctrl_outPutAnimBank_1.globalIK_2_localIK"
		;
connectAttr "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_hornLong_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_hornLong_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_hornLong_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_hornLong_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_hornLong_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_hornLong_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_hornLong_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_hornLong_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_hornLong_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_followHead.o" "vicky_original:l_hornLong_ctrl_outPutAnimBank_1.followHead"
		;
connectAttr "vicky_original:l_hornLong_ctrl_outPutAnimBank_1_displayGeo.o" "vicky_original:l_hornLong_ctrl_outPutAnimBank_1.displayGeo"
		;
connectAttr "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_hornLong_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_hornLong_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_hornLong_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_hornLong_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_hornLong_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_hornLong_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_hornLong_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_hornLong_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_hornLong_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_followHead.o" "vicky_original:r_hornLong_ctrl_outPutAnimBank_1.followHead"
		;
connectAttr "vicky_original:r_hornLong_ctrl_outPutAnimBank_1_displayGeo.o" "vicky_original:r_hornLong_ctrl_outPutAnimBank_1.displayGeo"
		;
connectAttr "vicky_original:m_helmet_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_helmet_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_helmet_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_helmet_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_helmet_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_helmet_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_helmet_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_helmet_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_helmet_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_helmet_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_helmet_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_helmet_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_helmet_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:m_helmet_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:m_helmet_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:m_helmet_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:m_helmet_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:m_helmet_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:m_helmet_ctrl_outPutAnimBank_1_followHead.o" "vicky_original:m_helmet_ctrl_outPutAnimBank_1.followHead"
		;
connectAttr "vicky_original:m_helmet_ctrl_outPutAnimBank_1_displayGeo.o" "vicky_original:m_helmet_ctrl_outPutAnimBank_1.displayGeo"
		;
connectAttr "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_hair_ex_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:m_hair_ex_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_hair_ex_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:r_foreHair_ex_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:l_foreHair_ex_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:hair_ex_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:hair_ex_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:hair_ex_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:hair_ex_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:hair_ex_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:hair_ex_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:hair_ex_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:hair_ex_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:hair_ex_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:hair_ex_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:hair_ex_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:hair_ex_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:hair_ex_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:hair_ex_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:hair_ex_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:hair_ex_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:hair_ex_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:hair_ex_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:hair_ex_ctrl_outPutAnimBank_1_subCtrl.o" "vicky_original:hair_ex_ctrl_outPutAnimBank_1.subCtrl"
		;
connectAttr "vicky_original:mov_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:mov_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:mov_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:mov_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:mov_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:mov_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:mov_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:mov_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:mov_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:mov_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:mov_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:mov_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:top_ctrl_outPutAnimBank_1_visibility.o" "vicky_original:top_ctrl_outPutAnimBank_1.v"
		;
connectAttr "vicky_original:top_ctrl_outPutAnimBank_1_globalScale.o" "vicky_original:top_ctrl_outPutAnimBank_1.globalScale"
		;
connectAttr "vicky_original:top_ctrl_outPutAnimBank_1_headRes.o" "vicky_original:top_ctrl_outPutAnimBank_1.headRes"
		;
connectAttr "vicky_original:top_ctrl_outPutAnimBank_1_bodyRes.o" "vicky_original:top_ctrl_outPutAnimBank_1.bodyRes"
		;
connectAttr "vicky_original:top_ctrl_outPutAnimBank_1_shoe.o" "vicky_original:top_ctrl_outPutAnimBank_1.shoe"
		;
connectAttr "vicky_original:top_ctrl_outPutAnimBank_1_helmetCtrl.o" "vicky_original:top_ctrl_outPutAnimBank_1.helmetCtrl"
		;
connectAttr "vicky_original:top_ctrl_outPutAnimBank_1_hairCtrl.o" "vicky_original:top_ctrl_outPutAnimBank_1.hairCtrl"
		;
connectAttr "vicky_original:top_ctrl_outPutAnimBank_1_clothCtrl.o" "vicky_original:top_ctrl_outPutAnimBank_1.clothCtrl"
		;
connectAttr "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:tongoueA_Rot_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:tongoueB_Rot_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:tongoueC_Rot_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_translateX.o" "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_translateY.o" "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:tongueIn1_Ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_ratio.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.ratio"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_roll.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.roll"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_Sub_Ctrl.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.Sub_Ctrl"
		;
connectAttr "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1_ExtraDeformers.o" "vicky_original:m_tongueTip_Ctrl_outPutAnimBank_1.ExtraDeformers"
		;
connectAttr "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:m_tongue_subC_Ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:m_tongue_subB_Ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:m_tongue_subA_Ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:tongueCon_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:tongueCon_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:tongueCon_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:tongueCon_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:tongueCon_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:tongueCon_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:tongueCon_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:tongueCon_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:tongueCon_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:tongueCon_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:tongueCon_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:tongueCon_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:tongueCurve_outPutAnimBank_1_visibility.o" "vicky_original:tongueCurve_outPutAnimBank_1.v"
		;
connectAttr "vicky_original:m_jaw_ctrl_outPutAnimBank_1_visibility.o" "vicky_original:m_jaw_ctrl_outPutAnimBank_1.v"
		;
connectAttr "vicky_original:m_jaw_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_jaw_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_jaw_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_jaw_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_jaw_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_jaw_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_jaw_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_jaw_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_jaw_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_jaw_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_jaw_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_jaw_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_jaw_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:m_jaw_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:m_jaw_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:m_jaw_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:m_jaw_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:m_jaw_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_pupilRadz_end_outPutAnimBank_1_visibility.o" "vicky_original:l_pupilRadz_end_outPutAnimBank_1.v"
		;
connectAttr "vicky_original:l_pupilRadz_end_outPutAnimBank_1_rotateX.o" "vicky_original:l_pupilRadz_end_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_pupilRadz_end_outPutAnimBank_1_rotateY.o" "vicky_original:l_pupilRadz_end_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_pupilRadz_end_outPutAnimBank_1_rotateZ.o" "vicky_original:l_pupilRadz_end_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:l_pupilRadz_end_outPutAnimBank_1_scaleX.o" "vicky_original:l_pupilRadz_end_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:l_pupilRadz_end_outPutAnimBank_1_scaleY.o" "vicky_original:l_pupilRadz_end_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:l_pupilRadz_end_outPutAnimBank_1_scaleZ.o" "vicky_original:l_pupilRadz_end_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:l_eye_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_eye_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_eye_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_eye_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_eye_ctrl_outPutAnimBank_1_crossEyeFix.o" "vicky_original:l_eye_ctrl_outPutAnimBank_1.crossEyeFix"
		;
connectAttr "vicky_original:l_eye_ctrl_outPutAnimBank_1_crossEyeRate.o" "vicky_original:l_eye_ctrl_outPutAnimBank_1.crossEyeRate"
		;
connectAttr "vicky_original:l_eye_ctrl_outPutAnimBank_1_Iris_Size.o" "vicky_original:l_eye_ctrl_outPutAnimBank_1.Iris_Size"
		;
connectAttr "vicky_original:l_eye_ctrl_outPutAnimBank_1_Pupil_Size.o" "vicky_original:l_eye_ctrl_outPutAnimBank_1.Pupil_Size"
		;
connectAttr "vicky_original:r_eye_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:r_eye_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:r_eye_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:r_eye_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:r_eye_ctrl_outPutAnimBank_1_crossEyeFix.o" "vicky_original:r_eye_ctrl_outPutAnimBank_1.crossEyeFix"
		;
connectAttr "vicky_original:r_eye_ctrl_outPutAnimBank_1_crossEyeRate.o" "vicky_original:r_eye_ctrl_outPutAnimBank_1.crossEyeRate"
		;
connectAttr "vicky_original:r_eye_ctrl_outPutAnimBank_1_Iris_Size.o" "vicky_original:r_eye_ctrl_outPutAnimBank_1.Iris_Size"
		;
connectAttr "vicky_original:r_eye_ctrl_outPutAnimBank_1_Pupil_Size.o" "vicky_original:r_eye_ctrl_outPutAnimBank_1.Pupil_Size"
		;
connectAttr "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_bothEye_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_bothEye_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_bothEye_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_bothEye_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_l_eye_offset.o" "vicky_original:m_bothEye_ctrl_outPutAnimBank_1.l_eye_offset"
		;
connectAttr "vicky_original:m_bothEye_ctrl_outPutAnimBank_1_r_eye_offset.o" "vicky_original:m_bothEye_ctrl_outPutAnimBank_1.r_eye_offset"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_scaleX.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_scaleY.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_scaleZ.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_tx.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.l_eyePSD_tx"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_sc.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.l_eyePSD_sc"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_bothEye_offset.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.bothEye_offset"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_irisSize_temp.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.irisSize_temp"
		;
connectAttr "vicky_original:m_eye_ctrl_outPutAnimBank_1_pupilSize_temp.o" "vicky_original:m_eye_ctrl_outPutAnimBank_1.pupilSize_temp"
		;
connectAttr "vicky_original:head_squash_ctrl_outPutAnimBank_1_visibility.o" "vicky_original:head_squash_ctrl_outPutAnimBank_1.v"
		;
connectAttr "vicky_original:head_squash_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:head_squash_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:head_squash_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:head_squash_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:head_squash_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:head_squash_ctrl_outPutAnimBank_1.tz"
		;
// End of vk_walk.ma

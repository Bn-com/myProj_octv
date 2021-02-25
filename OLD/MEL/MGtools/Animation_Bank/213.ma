//Maya ASCII 2012 scene
//Name: 213.ma
//Last modified: Thu, Sep 06, 2012 06:04:52 PM
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
	setAttr ".range" -type "string" "\"282:373\"";
	setAttr ".num" 171;
	setAttr ".nts" -type "string" (
		"ylva_original:m_spineA_waistFree_ctrl; ylva_original:m_spineA_chest_ctrl; ylva_original:m_spineA_waist_ctrl; ylva_original:m_spineA_hip_ctrl; ylva_original:l_armA_elbow_IK_ctrl; ylva_original:r_armA_elbow_IK_ctrl; ylva_original:m_spineA_torso_ctrl; ylva_original:m_spineA_body_ctrl; ylva_original:l_legA_heel_IK_ctrl; ylva_original:l_legA_knee_IK_ctrl; ylva_original:l_legA_foot_IK_ctrl; ylva_original:r_legA_heel_IK_ctrl; ylva_original:r_legA_knee_IK_ctrl; ylva_original:r_legA_foot_IK_ctrl; ylva_original:l_legA_pelvis_ctrl; ylva_original:r_legA_pelvis_ctrl; ylva_original:l_armA_hand_IK_ctrl; ylva_original:r_armA_hand_IK_ctrl; ylva_original:l_armA_shoulder_ctrl; ylva_original:r_armA_shoulder_ctrl; ylva_original:m_armA_shoulder_ctrl; ylva_original:l_armA_thumb_03_ctrl; ylva_original:l_armA_thumb_02_ctrl; ylva_original:l_armA_thumb_01_ctrl; ylva_original:l_armA_index_04_ctrl; ylva_original:l_armA_index_03_ctrl; ylva_original:l_armA_index_02_ctrl; ylva_original:l_armA_index_01_ctrl; ylva_original:l_armA_middle_04_ctrl; ylva_original:l_armA_middle_03_ctrl; ylva_original:l_armA_middle_02_ctrl; ylva_original:l_armA_middle_01_ctrl; ylva_original:l_armA_ring_04_ctrl; ylva_original:l_armA_ring_03_ctrl; ylva_original:l_armA_ring_02_ctrl; ylva_original:l_armA_ring_01_ctrl; ylva_original:l_armA_wrist_ctrl; ylva_original:r_armA_thumb_03_ctrl; ylva_original:r_armA_thumb_02_ctrl; ylva_original:r_armA_thumb_01_ctrl; ylva_original:r_armA_index_04_ctrl; ylva_original:r_armA_index_03_ctrl; ylva_original:r_armA_index_02_ctrl; ylva_original:r_armA_index_01_ctrl; ylva_original:r_armA_middle_04_ctrl; ylva_original:r_armA_middle_03_ctrl; ylva_original:r_armA_middle_02_ctrl; ylva_original:r_armA_middle_01_ctrl; ylva_original:r_armA_ring_04_ctrl; ylva_original:r_armA_ring_03_ctrl; ylva_original:r_armA_ring_02_ctrl; ylva_original:r_armA_ring_01_ctrl; ylva_original:r_armA_wrist_ctrl; ylva_original:m_spineA_head_ctrl; ylva_original:m_spineA_neck_03_ctrl; ylva_original:m_spineA_neck_02_ctrl; ylva_original:m_spineA_neck_01_ctrl; ylva_original:RgtOuterBrow; ylva_original:RgtMidBrow; ylva_original:LftMidBrow; ylva_original:LftOuterBrow; ylva_original:rgtHappyBrow; ylva_original:rgtMadBrow; ylva_original:rgtSadBrow; ylva_original:rgtBoredBrow; ylva_original:lftHappyBrow; ylva_original:lftMadBrow; ylva_original:lftSadBrow; ylva_original:lftBoredBrow; ylva_original:RgtTopLid; ylva_original:LftTopLid; ylva_original:RgtBtmLid; ylva_original:LftBtmLid; ylva_original:eyeDarts; ylva_original:JawRock; ylva_original:MouthEmotion; ylva_original:MouthSlide; ylva_original:UprLip; ylva_original:LwrLip; ylva_original:rgtCheekInOut; ylva_original:lftCheekInOut; ylva_original:TongueB; ylva_original:TongueA; ylva_original:teethClench; ylva_original:teethUpSharp; ylva_original:teethDownSharp; ylva_original:mouthAa; ylva_original:mouthOo; ylva_original:mouthUu; ylva_original:mouthMm; ylva_original:mouthSurprised; ylva_original:scared; ylva_original:angry; ylva_original:bigMouth; ylva_original:nose; ylva_original:noseTip; ylva_original:nosetril; ylva_original:RgtbigEye; ylva_original:LftbigEye; ylva_original:RgteyeSquint; ylva_original:LfteyeSquint; ylva_original:RgtUpEyeLid; ylva_original:RgtDownEyeLid; ylva_original:LftUpEyeLid; ylva_original:LftDownEyeLid; ylva_original:mouthWideNarrow; ylva_original:openHappy; ylva_original:openSad; ylva_original:facialCtrlVis; ylva_original:rottenTeeth; ylva_original:faceGui; ylva_original:l_legA_ankle_ctrl; ylva_original:r_legA_ankle_ctrl; ylva_original:skirt_midwire_1_ctrl; ylva_original:skirt_midwire_2_ctrl; ylva_original:skirt_midwire_3_ctrl; ylva_original:skirt_midwire_4_ctrl; ylva_original:skirt_midwire_5_ctrl; ylva_original:skirt_midwire_6_ctrl; ylva_original:skirt_midwire_7_ctrl; ylva_original:skirt_midwire_8_ctrl; ylva_original:skirt_lwrwire_1_ctrl; ylva_original:skirt_lwrwire_2_ctrl; ylva_original:skirt_lwrwire_3_ctrl; ylva_original:skirt_lwrwire_4_ctrl; ylva_original:skirt_lwrwire_5_ctrl; ylva_original:skirt_lwrwire_6_ctrl; ylva_original:skirt_lwrwire_7_ctrl; ylva_original:skirt_lwrwire_8_ctrl; ylva_original:hair_curve_jt_7_fk_ctrl; ylva_original:hair_curve_jt_6_fk_ctrl; ylva_original:hair_curve_jt_4_ctrl; ylva_original:hair_curve_jt_5_ctrl; ylva_original:hair_curve_jt_6_ctrl; ylva_original:hair_curve_jt_7_ctrl; ylva_original:hair_curve_jt_8_ctrl; ylva_original:hair_curve_jt_9_ctrl; ylva_original:hair_curve_jt_10_ctrl; ylva_original:hair_curve_jt_11_ctrl; ylva_original:hair_ex_ctrl; ylva_original:mov_ctrl; ylva_original:top_ctrl; ylva_original:tongoueA_Rot_Ctrl; ylva_original:tongoueB_Rot_Ctrl; ylva_original:tongoueC_Rot_Ctrl; ylva_original:tongueIn1_Ctrl; ylva_original:m_tongueTip_Ctrl; ylva_original:m_tongue_subC_Ctrl; ylva_original:m_tongue_subB_Ctrl; ylva_original:m_tongue_subA_Ctrl; ylva_original:tongueCon_ctrl; ylva_original:tongueCurve; ylva_original:m_jaw_ctrl; ylva_original:l_eye_ctrl; ylva_original:r_eye_ctrl; ylva_original:m_bothEye_ctrl; ylva_original:m_eye_ctrl; ylva_original:l_mouth_ctrl; ylva_original:m_mouthTop_ctrl; ylva_original:m_mouthBtm_ctrl; ylva_original:r_mouth_ctrl; ylva_original:m_mouth_root_ctrl; ylva_original:l_teethBtmA_ctrl; ylva_original:r_teethBtmA_ctrl; ylva_original:m_teethBtmB_ctrl; ylva_original:m_teethBtmA_ctrl; ylva_original:l_teethTopA_ctrl; ylva_original:r_teethTopA_ctrl; ylva_original:m_teethTopB_ctrl; ylva_original:m_teethTopA_ctrl; ylva_original:head_squash_ctrl; ");
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
createNode transform -n "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_elbow_IK_ctrl";
createNode locator -n "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_elbow_IK_ctrl";
createNode locator -n "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1";
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
createNode transform -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_hand_IK_ctrl";
createNode locator -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1";
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
createNode transform -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_shoulder_ctrl";
createNode locator -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_shoulder_ctrl";
createNode locator -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1";
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
createNode transform -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_thumb_03_ctrl";
createNode locator -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_thumb_02_ctrl";
createNode locator -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_thumb_01_ctrl";
createNode locator -n "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_index_04_ctrl";
createNode locator -n "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_index_03_ctrl";
createNode locator -n "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_index_02_ctrl";
createNode locator -n "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_index_01_ctrl";
createNode locator -n "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_middle_04_ctrl";
createNode locator -n "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_middle_03_ctrl";
createNode locator -n "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_middle_02_ctrl";
createNode locator -n "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_middle_01_ctrl";
createNode locator -n "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_ring_04_ctrl";
createNode locator -n "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_ring_03_ctrl";
createNode locator -n "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_ring_02_ctrl";
createNode locator -n "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_ring_01_ctrl";
createNode locator -n "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_wrist_ctrl";
createNode locator -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1Shape" -p "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_thumb_03_ctrl";
createNode locator -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_thumb_02_ctrl";
createNode locator -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_thumb_01_ctrl";
createNode locator -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_index_04_ctrl";
createNode locator -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_index_03_ctrl";
createNode locator -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_index_02_ctrl";
createNode locator -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_index_01_ctrl";
createNode locator -n "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_middle_04_ctrl";
createNode locator -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_middle_03_ctrl";
createNode locator -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_middle_02_ctrl";
createNode locator -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_middle_01_ctrl";
createNode locator -n "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_ring_04_ctrl";
createNode locator -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_ring_03_ctrl";
createNode locator -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_ring_02_ctrl";
createNode locator -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_ring_01_ctrl";
createNode locator -n "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "ylva_original:r_armA_wrist_ctrl";
createNode locator -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1Shape" -p "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1";
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
createNode transform -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:m_spineA_neck_03_ctrl";
createNode locator -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1";
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
createNode transform -n "ylva_original:RgtOuterBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:RgtOuterBrow";
createNode locator -n "ylva_original:RgtOuterBrow_outPutAnimBank_1Shape" -p "ylva_original:RgtOuterBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:RgtMidBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:RgtMidBrow";
createNode locator -n "ylva_original:RgtMidBrow_outPutAnimBank_1Shape" -p "ylva_original:RgtMidBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:LftMidBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:LftMidBrow";
createNode locator -n "ylva_original:LftMidBrow_outPutAnimBank_1Shape" -p "ylva_original:LftMidBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:LftOuterBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:LftOuterBrow";
createNode locator -n "ylva_original:LftOuterBrow_outPutAnimBank_1Shape" -p "ylva_original:LftOuterBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:rgtHappyBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:rgtHappyBrow";
createNode locator -n "ylva_original:rgtHappyBrow_outPutAnimBank_1Shape" -p "ylva_original:rgtHappyBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:rgtMadBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:rgtMadBrow";
createNode locator -n "ylva_original:rgtMadBrow_outPutAnimBank_1Shape" -p "ylva_original:rgtMadBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:rgtSadBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:rgtSadBrow";
createNode locator -n "ylva_original:rgtSadBrow_outPutAnimBank_1Shape" -p "ylva_original:rgtSadBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:rgtBoredBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:rgtBoredBrow";
createNode locator -n "ylva_original:rgtBoredBrow_outPutAnimBank_1Shape" -p "ylva_original:rgtBoredBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:lftHappyBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:lftHappyBrow";
createNode locator -n "ylva_original:lftHappyBrow_outPutAnimBank_1Shape" -p "ylva_original:lftHappyBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:lftMadBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:lftMadBrow";
createNode locator -n "ylva_original:lftMadBrow_outPutAnimBank_1Shape" -p "ylva_original:lftMadBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:lftSadBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:lftSadBrow";
createNode locator -n "ylva_original:lftSadBrow_outPutAnimBank_1Shape" -p "ylva_original:lftSadBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:lftBoredBrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:lftBoredBrow";
createNode locator -n "ylva_original:lftBoredBrow_outPutAnimBank_1Shape" -p "ylva_original:lftBoredBrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:RgtTopLid_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:RgtTopLid";
createNode locator -n "ylva_original:RgtTopLid_outPutAnimBank_1Shape" -p "ylva_original:RgtTopLid_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:LftTopLid_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:LftTopLid";
createNode locator -n "ylva_original:LftTopLid_outPutAnimBank_1Shape" -p "ylva_original:LftTopLid_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:RgtBtmLid_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:RgtBtmLid";
createNode locator -n "ylva_original:RgtBtmLid_outPutAnimBank_1Shape" -p "ylva_original:RgtBtmLid_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:LftBtmLid_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:LftBtmLid";
createNode locator -n "ylva_original:LftBtmLid_outPutAnimBank_1Shape" -p "ylva_original:LftBtmLid_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:eyeDarts_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:eyeDarts";
createNode locator -n "ylva_original:eyeDarts_outPutAnimBank_1Shape" -p "ylva_original:eyeDarts_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:JawRock_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "mouthHold" -ln "mouthHold" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".mouthHold";
	setAttr ".ObjName" -type "string" "ylva_original:JawRock";
createNode locator -n "ylva_original:JawRock_outPutAnimBank_1Shape" -p "ylva_original:JawRock_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:MouthEmotion_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:MouthEmotion";
createNode locator -n "ylva_original:MouthEmotion_outPutAnimBank_1Shape" -p "ylva_original:MouthEmotion_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:MouthSlide_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:MouthSlide";
createNode locator -n "ylva_original:MouthSlide_outPutAnimBank_1Shape" -p "ylva_original:MouthSlide_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:UprLip_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:UprLip";
createNode locator -n "ylva_original:UprLip_outPutAnimBank_1Shape" -p "ylva_original:UprLip_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:LwrLip_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:LwrLip";
createNode locator -n "ylva_original:LwrLip_outPutAnimBank_1Shape" -p "ylva_original:LwrLip_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:rgtCheekInOut_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:rgtCheekInOut";
createNode locator -n "ylva_original:rgtCheekInOut_outPutAnimBank_1Shape" -p "ylva_original:rgtCheekInOut_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:lftCheekInOut_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:lftCheekInOut";
createNode locator -n "ylva_original:lftCheekInOut_outPutAnimBank_1Shape" -p "ylva_original:lftCheekInOut_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:TongueB_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:TongueB";
createNode locator -n "ylva_original:TongueB_outPutAnimBank_1Shape" -p "ylva_original:TongueB_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:TongueA_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:TongueA";
createNode locator -n "ylva_original:TongueA_outPutAnimBank_1Shape" -p "ylva_original:TongueA_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:teethClench_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:teethClench";
createNode locator -n "ylva_original:teethClench_outPutAnimBank_1Shape" -p "ylva_original:teethClench_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:teethUpSharp_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:teethUpSharp";
createNode locator -n "ylva_original:teethUpSharp_outPutAnimBank_1Shape" -p "ylva_original:teethUpSharp_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:teethDownSharp_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:teethDownSharp";
createNode locator -n "ylva_original:teethDownSharp_outPutAnimBank_1Shape" -p "ylva_original:teethDownSharp_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:mouthAa_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:mouthAa";
createNode locator -n "ylva_original:mouthAa_outPutAnimBank_1Shape" -p "ylva_original:mouthAa_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:mouthOo_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:mouthOo";
createNode locator -n "ylva_original:mouthOo_outPutAnimBank_1Shape" -p "ylva_original:mouthOo_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:mouthUu_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:mouthUu";
createNode locator -n "ylva_original:mouthUu_outPutAnimBank_1Shape" -p "ylva_original:mouthUu_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:mouthMm_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:mouthMm";
createNode locator -n "ylva_original:mouthMm_outPutAnimBank_1Shape" -p "ylva_original:mouthMm_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:mouthSurprised_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:mouthSurprised";
createNode locator -n "ylva_original:mouthSurprised_outPutAnimBank_1Shape" -p "ylva_original:mouthSurprised_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:scared_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:scared";
createNode locator -n "ylva_original:scared_outPutAnimBank_1Shape" -p "ylva_original:scared_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:angry_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:angry";
createNode locator -n "ylva_original:angry_outPutAnimBank_1Shape" -p "ylva_original:angry_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:bigMouth_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:bigMouth";
createNode locator -n "ylva_original:bigMouth_outPutAnimBank_1Shape" -p "ylva_original:bigMouth_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:nose_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:nose";
createNode locator -n "ylva_original:nose_outPutAnimBank_1Shape" -p "ylva_original:nose_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:noseTip_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:noseTip";
createNode locator -n "ylva_original:noseTip_outPutAnimBank_1Shape" -p "ylva_original:noseTip_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:nosetril_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:nosetril";
createNode locator -n "ylva_original:nosetril_outPutAnimBank_1Shape" -p "ylva_original:nosetril_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:RgtbigEye_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:RgtbigEye";
createNode locator -n "ylva_original:RgtbigEye_outPutAnimBank_1Shape" -p "ylva_original:RgtbigEye_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:LftbigEye_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:LftbigEye";
createNode locator -n "ylva_original:LftbigEye_outPutAnimBank_1Shape" -p "ylva_original:LftbigEye_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:RgteyeSquint_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:RgteyeSquint";
createNode locator -n "ylva_original:RgteyeSquint_outPutAnimBank_1Shape" -p "ylva_original:RgteyeSquint_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:LfteyeSquint_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:LfteyeSquint";
createNode locator -n "ylva_original:LfteyeSquint_outPutAnimBank_1Shape" -p "ylva_original:LfteyeSquint_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:RgtUpEyeLid_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:RgtUpEyeLid";
createNode locator -n "ylva_original:RgtUpEyeLid_outPutAnimBank_1Shape" -p "ylva_original:RgtUpEyeLid_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:RgtDownEyeLid_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:RgtDownEyeLid";
createNode locator -n "ylva_original:RgtDownEyeLid_outPutAnimBank_1Shape" -p "ylva_original:RgtDownEyeLid_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:LftUpEyeLid_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:LftUpEyeLid";
createNode locator -n "ylva_original:LftUpEyeLid_outPutAnimBank_1Shape" -p "ylva_original:LftUpEyeLid_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:LftDownEyeLid_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:LftDownEyeLid";
createNode locator -n "ylva_original:LftDownEyeLid_outPutAnimBank_1Shape" -p "ylva_original:LftDownEyeLid_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:mouthWideNarrow_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:mouthWideNarrow";
createNode locator -n "ylva_original:mouthWideNarrow_outPutAnimBank_1Shape" -p "ylva_original:mouthWideNarrow_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:openHappy_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:openHappy";
createNode locator -n "ylva_original:openHappy_outPutAnimBank_1Shape" -p "ylva_original:openHappy_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:openSad_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:openSad";
createNode locator -n "ylva_original:openSad_outPutAnimBank_1Shape" -p "ylva_original:openSad_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:facialCtrlVis_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".tx";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:facialCtrlVis";
createNode locator -n "ylva_original:facialCtrlVis_outPutAnimBank_1Shape" -p "ylva_original:facialCtrlVis_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:rottenTeeth_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:rottenTeeth";
createNode locator -n "ylva_original:rottenTeeth_outPutAnimBank_1Shape" -p "ylva_original:rottenTeeth_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:faceGui_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:faceGui";
createNode locator -n "ylva_original:faceGui_outPutAnimBank_1Shape" -p "ylva_original:faceGui_outPutAnimBank_1";
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
createNode transform -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1" 
		-p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:hair_curve_jt_7_fk_ctrl";
createNode locator -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1" 
		-p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:hair_curve_jt_6_fk_ctrl";
createNode locator -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:hair_curve_jt_4_ctrl";
createNode locator -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:hair_curve_jt_5_ctrl";
createNode locator -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:hair_curve_jt_6_ctrl";
createNode locator -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:hair_curve_jt_7_ctrl";
createNode locator -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:hair_curve_jt_8_ctrl";
createNode locator -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:hair_curve_jt_9_ctrl";
createNode locator -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:hair_curve_jt_10_ctrl";
createNode locator -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1" -p
		 "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:hair_curve_jt_11_ctrl";
createNode locator -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1Shape" 
		-p "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:hair_ex_ctrl";
createNode locator -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1Shape" -p "ylva_original:hair_ex_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:mov_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:mov_ctrl";
createNode locator -n "ylva_original:mov_ctrl_outPutAnimBank_1Shape" -p "ylva_original:mov_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:top_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "globalScale" -ln "globalScale" -at "double";
	addAttr -ci true -sn "bodyRes" -ln "bodyRes" -at "long";
	addAttr -ci true -sn "faceGuiCtrl" -ln "faceGuiCtrl" -at "long";
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
	setAttr -k on ".faceGuiCtrl";
	setAttr -k on ".ribbonCtrl_grp";
	setAttr -k on ".hairCtrl";
	setAttr -k on ".clothCtrl";
	setAttr ".ObjName" -type "string" "ylva_original:top_ctrl";
createNode locator -n "ylva_original:top_ctrl_outPutAnimBank_1Shape" -p "ylva_original:top_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:tongoueA_Rot_Ctrl";
createNode locator -n "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1Shape" -p "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:tongoueB_Rot_Ctrl";
createNode locator -n "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1Shape" -p "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:tongoueC_Rot_Ctrl";
createNode locator -n "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1Shape" -p "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:tongueIn1_Ctrl";
createNode locator -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1Shape" -p "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "ylva_original:m_tongueTip_Ctrl";
createNode locator -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:m_tongue_subC_Ctrl";
createNode locator -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:m_tongue_subB_Ctrl";
createNode locator -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:m_tongue_subA_Ctrl";
createNode locator -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1";
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
createNode transform -n "ylva_original:tongueCurve_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:tongueCurve";
createNode locator -n "ylva_original:tongueCurve_outPutAnimBank_1Shape" -p "ylva_original:tongueCurve_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:m_jaw_ctrl";
createNode locator -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_jaw_ctrl_outPutAnimBank_1";
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
createNode transform -n "ylva_original:l_mouth_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:l_mouth_ctrl";
createNode locator -n "ylva_original:l_mouth_ctrl_outPutAnimBank_1Shape" -p "ylva_original:l_mouth_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:m_mouthTop_ctrl";
createNode locator -n "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:m_mouthBtm_ctrl";
createNode locator -n "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_mouth_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:r_mouth_ctrl";
createNode locator -n "ylva_original:r_mouth_ctrl_outPutAnimBank_1Shape" -p "ylva_original:r_mouth_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:m_mouth_root_ctrl";
createNode locator -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1";
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
createNode transform -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:r_teethBtmA_ctrl";
createNode locator -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1Shape" -p "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:m_teethBtmB_ctrl";
createNode locator -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:m_teethBtmA_ctrl";
createNode locator -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "ylva_original:l_teethTopA_ctrl";
createNode locator -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1Shape" -p "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1";
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
createNode transform -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:m_teethTopB_ctrl";
createNode locator -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr ".ObjName" -type "string" "ylva_original:m_teethTopA_ctrl";
createNode locator -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1Shape" -p "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1";
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
createNode animCurveTL -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_wide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_thick";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 0 285 0 289 0 293 0 297 0 302 0 314 0
		 325 0 333 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 0 285 0 289 0 293 0 297 0 302 0 314 0
		 325 0 333 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 0 285 0 289 0 293 0 297 0 302 0 314 0
		 325 0 333 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 7.7056775110000011 284 0.89322675789999995
		 286 -0.86775519170000004 289 2.004371994 293 18.398667639999999 297 7.254601826 299 0.68457132549999999
		 302 -0.79269784983621105 308 13.070368966410273 314 18.425187703051968 325 19.317657492492248
		 333 13.338621066284407;
	setAttr -s 12 ".kit[0:11]"  9 18 3 9 18 1 1 1 
		10 1 10 10;
	setAttr -s 12 ".kot[1:11]"  18 3 9 18 1 1 1 10 
		1 10 10;
	setAttr -s 12 ".kix[5:11]"  0.016713559627532959 0.016653690487146378 
		1 0.81970095634460449 0.99529457092285156 1 0.95072448253631592;
	setAttr -s 12 ".kiy[5:11]"  -0.017450854182243347 -0.017450872808694839 
		0 0.5727916955947876 0.09689534455537796 0 -0.31003710627555847;
	setAttr -s 12 ".kox[0:11]"  0.011742383241653442 0.73036855459213257 
		1 0.63989019393920898 1 0.016713570803403854 0.016653662547469139 1 0.81970095634460449 
		0.99529457092285156 1 0.95072448253631592;
	setAttr -s 12 ".koy[0:11]"  -0.017452089115977287 -0.68305331468582153 
		0 0.7684662938117981 0 -0.017450854182243347 -0.017450872808694839 0 0.5727916955947876 
		0.09689534455537796 0 -0.31003710627555847;
createNode animCurveTA -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 -6.609776997 289 -5.9717531209999999
		 293 -5.813685489 302 -3.6715516355284077 308 -1.8089412950670454 314 -2.1167492614611074
		 325 -0.94503537010895178 333 -1.9662885127060585;
	setAttr -s 8 ".kit[0:7]"  9 9 18 10 10 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 9 18 10 10 1 10 10;
	setAttr -s 8 ".kix[5:7]"  0.99193048477172852 1 1;
	setAttr -s 8 ".kiy[5:7]"  0.12678287923336029 0 0;
	setAttr -s 8 ".kox[0:7]"  0.40186089277267456 0.99950182437896729 
		0.99866479635238647 1 1 0.99193048477172852 1 1;
	setAttr -s 8 ".koy[0:7]"  0.015981992706656456 0.031562451273202896 
		0.051658496260643005 0 0 0.12678287923336029 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 2.189117977 285 2.598353012 289 0.42156676859999997
		 293 -1.3925539549999999 297 -0.022311845029999999 302 1.2669270080384587 308 0.97753929536265793
		 314 -0.8029439293026871 325 -1.0996911334135779 333 -1.7198295538620221;
	setAttr -s 10 ".kit[0:9]"  3 18 9 9 18 10 10 1 
		10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 9 9 18 10 10 1 
		10 10;
	setAttr -s 10 ".kix[7:9]"  0.99947649240493774 1 1;
	setAttr -s 10 ".kiy[7:9]"  -0.032353177666664124 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 0.97711986303329468 0.99970704317092896 
		0.9917900562286377 1 1 0.99947649240493774 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 -0.21268944442272186 -0.024202754721045494 
		0.12787684798240662 0 0 -0.032353177666664124 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 0 285 0 289 0 293 0 297 0 302 0 314 0
		 325 0 333 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_wide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 0 285 0 289 0 293 0 297 0 302 0 314 0
		 325 0 333 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_thick";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 0 285 0 289 0 293 0 297 0 302 0 314 0
		 325 0 333 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 10 
		10;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 -3.3819916480000001 289 -1.432735466
		 293 -3.7749619430000001 297 -3.3818193230000002 302 -3.3132450560062243 308 1.9310842544426801
		 314 -1.5591175952934395 325 -2.1408179035827937 333 -8.2688242348708307;
	setAttr -s 9 ".kit[0:8]"  9 18 9 9 10 10 1 10 
		10;
	setAttr -s 9 ".kot[0:8]"  1 18 9 9 10 10 1 10 
		10;
	setAttr -s 9 ".kix[6:8]"  0.9979928731918335 1 0.94842755794525146;
	setAttr -s 9 ".kiy[6:8]"  -0.063326351344585419 0 -0.31699410080909729;
	setAttr -s 9 ".kox[0:8]"  0.14218546450138092 1 0.99439692497253418 
		0.99974960088729858 1 0.99797207117080688 0.9979928731918335 1 0.94842755794525146;
	setAttr -s 9 ".koy[0:8]"  0.017275966703891754 0 -0.10571049153804779 
		0.022379083558917046 0 0.063652463257312775 -0.063326351344585419 0 -0.31699410080909729;
createNode animCurveTA -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 287 0 289 0 293 0 297 0 302 2.2024755464197638
		 308 3.0789980595780526 314 4.5265455814142932 325 6.0060200885266477 333 4.8159175103299621;
	setAttr -s 11 ".kit[7:10]"  10 1 10 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 10 
		1 10 10;
	setAttr -s 11 ".kix[8:10]"  0.98722636699676514 1 1;
	setAttr -s 11 ".kiy[8:10]"  0.15932430326938629 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 0.99262410402297974 1 0.98722636699676514 
		1 1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0.12123256921768188 0 0.15932430326938629 
		0 0;
createNode animCurveTA -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 0.99267490030000005 287 2.582808376
		 289 2.908429967 297 0.3147319281 302 -1.8067601296633702 308 -1.9247842280894396
		 314 -7.3981939185586301 325 -8.3104288669701614 333 -8.5125523236221206;
	setAttr -s 9 ".kit[0:8]"  9 18 18 1 18 10 1 10 
		10;
	setAttr -s 9 ".kot[0:8]"  1 18 18 1 18 10 1 10 
		10;
	setAttr -s 9 ".kix[3:8]"  0.084203667938709259 0.9996686577796936 
		1 0.99508541822433472 1 1;
	setAttr -s 9 ".kiy[3:8]"  -0.017391307279467583 -0.025740357115864754 
		0 -0.099020428955554962 0 0;
	setAttr -s 9 ".kox[0:8]"  0.12479228526353836 0.99294543266296387 
		1 0.084203660488128662 0.9996686577796936 1 0.99508541822433472 1 1;
	setAttr -s 9 ".koy[0:8]"  0.017316859215497971 0.1185724064707756 
		0 -0.017391307279467583 -0.025740357115864754 0 -0.099020428955554962 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 0 285 0 289 0 293 0 297 0 302 0 314 0
		 325 0 333 0;
	setAttr -s 9 ".kit[7:8]"  10 10;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 10 
		10;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 313 0 325 0 333 0;
	setAttr -s 10 ".kit[7:9]"  1 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 1 
		10 10;
	setAttr -s 10 ".kix[7:9]"  1 1 1;
	setAttr -s 10 ".kiy[7:9]"  0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 313 0 325 0 333 0;
	setAttr -s 10 ".kit[7:9]"  1 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 1 
		10 10;
	setAttr -s 10 ".kix[7:9]"  1 1 1;
	setAttr -s 10 ".kiy[7:9]"  0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 313 0 325 0 333 0;
	setAttr -s 10 ".kit[7:9]"  1 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 1 
		10 10;
	setAttr -s 10 ".kix[7:9]"  1 1 1;
	setAttr -s 10 ".kiy[7:9]"  0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 0 285 0.066794718350000004 289 0.16769909390000001
		 293 0.11520989439999998 297 0.00064003003370000002 305 -0.178413234 313 0 325 0 333 0;
	setAttr -s 9 ".kit[6:8]"  1 10 10;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 1 10 
		10;
	setAttr -s 9 ".kix[6:8]"  1 1 1;
	setAttr -s 9 ".kiy[6:8]"  0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 0.99994534254074097 1 0.99995845556259155 
		0.99994301795959473 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0.010452622547745705 0 -0.0091112889349460602 
		-0.010675840079784393 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  282 12.91264758 285 6.226786165 295 -16.297959410000001
		 297 -14.913093009999999 313 12.91264758 325 12.91264758 333 0;
	setAttr -s 7 ".kit[0:6]"  9 18 18 18 1 10 10;
	setAttr -s 7 ".kot[0:6]"  1 18 18 18 1 10 10;
	setAttr -s 7 ".kix[4:6]"  0.016119463369250298 1 0.81758600473403931;
	setAttr -s 7 ".kiy[4:6]"  -0.017451025545597076 0 -0.57580649852752686;
	setAttr -s 7 ".kox[0:6]"  0.017945416271686554 0.71406126022338867 
		1 0.81612014770507813 0.016119455918669701 1 0.81758600473403931;
	setAttr -s 7 ".koy[0:6]"  -0.01745048351585865 -0.70008325576782227 
		0 0.57788228988647461 -0.017451025545597076 0 -0.57580649852752686;
createNode animCurveTA -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 4.4743048649999997 285 10.52475664 287 12.842135669999999
		 293 11.701911429999999 297 1.8030222789999999 301 -4.6928253059999996 305 -6.6576316059999998
		 313 4.4743048649999997 325 4.4743048649999997 333 0;
	setAttr -s 10 ".kit[0:9]"  9 18 1 1 18 18 18 1 
		10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 1 1 18 18 18 1 
		10 10;
	setAttr -s 10 ".kix[2:9]"  0.090200521051883698 0.041691355407238007 
		0.74544203281402588 0.90798735618591309 1 0.021975602954626083 1 0.97149056196212769;
	setAttr -s 10 ".kiy[2:9]"  0.017382146790623665 -0.017438117414712906 
		-0.66657054424285889 -0.41899758577346802 0 0.017449077218770981 0 -0.23707838356494904;
	setAttr -s 10 ".kox[0:9]"  0.019829310476779938 0.80759787559509277 
		0.090200521051883698 0.041691351681947708 0.74544203281402588 0.90798735618591309 
		1 0.021975606679916382 1 0.97149056196212769;
	setAttr -s 10 ".koy[0:9]"  0.017449859529733658 0.5897335410118103 
		0.017382146790623665 -0.017438117414712906 -0.66657054424285889 -0.41899758577346802 
		0 0.01744907908141613 0 -0.23707838356494904;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 313 0 325 0 333 0;
	setAttr -s 10 ".kit[7:9]"  1 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 1 
		10 10;
	setAttr -s 10 ".kix[7:9]"  1 1 1;
	setAttr -s 10 ".kiy[7:9]"  0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_wide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 313 0 325 0 333 0;
	setAttr -s 10 ".kit[7:9]"  1 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 1 
		10 10;
	setAttr -s 10 ".kix[7:9]"  1 1 1;
	setAttr -s 10 ".kiy[7:9]"  0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_thick";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 313 0 325 0 333 0;
	setAttr -s 10 ".kit[7:9]"  1 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 1 
		10 10;
	setAttr -s 10 ".kix[7:9]"  1 1 1;
	setAttr -s 10 ".kiy[7:9]"  0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 313 1 325 1 333 1;
	setAttr -s 10 ".kit[7:9]"  1 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 1 
		10 10;
	setAttr -s 10 ".kix[7:9]"  1 1 1;
	setAttr -s 10 ".kiy[7:9]"  0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  326 -4.282602393052807 333 2.7193208429822993;
createNode animCurveTL -n "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  326 -7.0027470728877983 333 -4.5119167802358975;
createNode animCurveTL -n "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  326 5.8175639528373635 333 14.350800075552453;
createNode animCurveTL -n "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  333 -3.6987873428103342;
createNode animCurveTL -n "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  333 -2.3716937158302143;
createNode animCurveTL -n "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  333 14.858079586276393;
createNode animCurveTA -n "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 9.9518836589999999 293 9.9518836589999999
		 297 9.9518836589999999 301 9.9518836589999999 309 9.9518836589999999 313 9.9518836589999999
		 314 9.9518836589999999 325 9.9518836589999999 333 9.9518836589999999;
	setAttr -s 9 ".kit[5:8]"  1 1 10 10;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 1 1 10 
		10;
	setAttr -s 9 ".kix[5:8]"  1 0.039999961853027344 1 1;
	setAttr -s 9 ".kiy[5:8]"  0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 0.39999961853027344 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 1.127592556 289 2.360984245 297 1.1203575100000003
		 305 -0.1202692247 313 1.127592556 314 1.3174451374623688 325 1.3174451374623688 333 1.3174451374623688;
	setAttr -s 8 ".kit[0:7]"  9 18 18 18 1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[4:7]"  0.23503921926021576 0.039999961853027344 
		1 1;
	setAttr -s 8 ".kiy[4:7]"  0.016964353621006012 0.00367343844845891 
		0 0;
	setAttr -s 8 ".kox[0:7]"  0.22138382494449615 1 0.99771851301193237 
		1 0.23503939807415009 0.23999977111816406 1 1;
	setAttr -s 8 ".koy[0:7]"  0.017020219936966896 0 -0.067511379718780518 
		0 0.016964353621006012 0.022040639072656631 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 -0.77060319740000005 289 -0.1907232951
		 297 -0.76399878440000002 305 -1.3372742740000001 313 -0.77060319740000005 314 -0.6823240616604308
		 325 -0.6823240616604308 333 -0.6823240616604308;
	setAttr -s 8 ".kit[0:7]"  9 18 18 18 1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[4:7]"  0.46365895867347717 0.039999961853027344 
		1 1;
	setAttr -s 8 ".kiy[4:7]"  0.015463857911527157 0.0017156661488115788 
		0 0;
	setAttr -s 8 ".kox[0:7]"  0.43482294678688049 1 0.99951159954071045 
		1 0.46365910768508911 0.23999977111816406 1 1;
	setAttr -s 8 ".koy[0:7]"  0.015716968104243279 0 -0.031252086162567139 
		0 0.015463855117559433 0.01029399037361145 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0.361987858 285 0.1021813276 289 -0.2438214155
		 293 -0.33312675609999998 295 -0.29110113459999998 297 -0.21272166410000001 307 0.70129736253659836
		 313 0.19267594589461856 325 0.10790570978762196 333 0.59405790550640269;
	setAttr -s 10 ".kit[7:9]"  1 10 10;
	setAttr -s 10 ".kot[7:9]"  1 10 10;
	setAttr -s 10 ".kix[7:9]"  0.9046938419342041 0.89380860328674316 
		0.54981160163879395;
	setAttr -s 10 ".kiy[7:9]"  -0.42606210708618164 0.44844874739646912 
		0.8352886438369751;
	setAttr -s 10 ".kox[7:9]"  0.9046938419342041 0.89380860328674316 
		0.54981166124343872;
	setAttr -s 10 ".koy[7:9]"  -0.42606210708618164 0.44844874739646912 
		0.83528870344161987;
createNode animCurveTL -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 13 ".ktv[0:12]"  282 -0.2013334111 285 -0.36122346979999997
		 286 -0.37737733169999998 288 -0.30479066490000001 293 0.17240659320000001 295 0.1174380164
		 297 -0.19666500109999999 299 -0.3564480498 301 -0.37479956689999999 307 -0.1130359878275493
		 313 0.13291520128406981 325 0.17390706613600632 333 0.19106137291423034;
	setAttr -s 13 ".kit[10:12]"  1 10 10;
	setAttr -s 13 ".kot[10:12]"  1 10 10;
	setAttr -s 13 ".kix[10:12]"  0.97503578662872314 1 1;
	setAttr -s 13 ".kiy[10:12]"  0.22204761207103729 0 0;
	setAttr -s 13 ".kox[10:12]"  0.97503578662872314 1 1;
	setAttr -s 13 ".koy[10:12]"  0.22204761207103729 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  282 -0.75278262549999997 297 -0.75278262549999997
		 307 -0.4370777644091976 313 -0.51285866455354334 325 -0.52548881457760099 333 -0.44984848403468342;
	setAttr -s 6 ".kit[3:5]"  1 10 10;
	setAttr -s 6 ".kot[3:5]"  1 10 10;
	setAttr -s 6 ".kix[3:5]"  0.99754726886749268 1 0.97318190336227417;
	setAttr -s 6 ".kiy[3:5]"  -0.069995462894439697 0 0.23003709316253662;
	setAttr -s 6 ".kox[3:5]"  0.99754726886749268 1 0.97318190336227417;
	setAttr -s 6 ".koy[3:5]"  -0.069995462894439697 0 0.23003709316253662;
createNode animCurveTA -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 -7.0432063579999999 286 -4.7209816660000001
		 289 -5.7124186850000003 293 -10.065588910000001 299 -5.8701508450000013 301 -4.613412587
		 307 0.033370891779512427 313 -5.0944757659148658 325 -5.9491168755305956 333 -1.2287369776012085;
	setAttr -s 10 ".kit[7:9]"  1 10 10;
	setAttr -s 10 ".kot[7:9]"  1 10 10;
	setAttr -s 10 ".kix[7:9]"  0.99658399820327759 1 0.96841955184936523;
	setAttr -s 10 ".kiy[7:9]"  -0.082585327327251434 0 0.2493264228105545;
	setAttr -s 10 ".kox[7:9]"  0.99658399820327759 1 0.96841955184936523;
	setAttr -s 10 ".koy[7:9]"  -0.082585327327251434 0 0.2493264228105545;
createNode animCurveTA -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  282 2.88 297 2.88 307 -2.0705810962042035
		 313 -7.7571621535335584 325 -8.7049256630884511 333 -50.789503124989864;
	setAttr -s 6 ".kit[2:5]"  1 1 10 10;
	setAttr -s 6 ".kot[2:5]"  1 1 10 10;
	setAttr -s 6 ".kix[2:5]"  0.9375755786895752 0.99580395221710205 
		1 0.39940369129180908;
	setAttr -s 6 ".kiy[2:5]"  -0.34778165817260742 -0.091512210667133331 
		0 -0.91677510738372803;
	setAttr -s 6 ".kox[2:5]"  0.9375755786895752 0.99580395221710205 
		1 0.39940372109413147;
	setAttr -s 6 ".koy[2:5]"  -0.34778162837028503 -0.091512210667133331 
		0 -0.9167751669883728;
createNode animCurveTA -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  282 -0.60350934389999999 289 -1.495401306
		 307 -1.0687093312029243 313 -0.43340903699094069 325 -0.32752565462227667 333 3.8561631816595128;
	setAttr -s 6 ".kit[3:5]"  1 10 10;
	setAttr -s 6 ".kot[3:5]"  1 10 10;
	setAttr -s 6 ".kix[3:5]"  0.99994724988937378 1 0.97494024038314819;
	setAttr -s 6 ".kiy[3:5]"  0.010266209952533245 0 0.22246679663658142;
	setAttr -s 6 ".kox[3:5]"  0.99994724988937378 1 0.97494029998779297;
	setAttr -s 6 ".koy[3:5]"  0.010266209952533245 0 0.22246681153774261;
createNode animCurveTA -n "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 -0.085919060729999996 299 -0.11329603150636558
		 300 -0.099574073142093766 301 -0.085919060729999996 302 -0.080988518936919718 303 -0.091000506173486428
		 304 -0.11800205314079903 305 -0.15917881204040896 325 -0.15917881204040896 330 -0.15917881204040896
		 333 0.18012991198979328;
	setAttr -s 11 ".kit[0:10]"  18 10 10 10 10 10 10 10 
		10 10 10;
	setAttr -s 11 ".kot[0:10]"  1 10 10 10 10 10 10 10 
		10 10 10;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 1 0.33342257142066956;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0.94277751445770264;
createNode animCurveTL -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 15 ".ktv[0:14]"  282 0 285 0.0033667084960000001 289 0.44028352939999998
		 293 0 297 0 299 -0.081074144569655004 300 -0.042352719561179697 301 0 302 0.044547812486356975
		 303 0.0899776122123086 304 0.13514580523300879 305 0.17906930292336654 325 0.17906930292336654
		 330 0.17906930292336654 333 0;
	setAttr -s 15 ".kit[0:14]"  18 18 18 18 18 10 10 18 
		10 10 10 18 10 10 10;
	setAttr -s 15 ".kot[0:14]"  1 18 18 18 18 10 10 18 
		10 10 10 18 10 10 10;
	setAttr -s 15 ".kox[0:14]"  1 0.99647659063339233 1 1 1 1 1 0.6772923469543457 
		1 1 1 1 1 1 0.55669099092483521;
	setAttr -s 15 ".koy[0:14]"  0 0.083871237933635712 0 0 0 0 0 0.73571401834487915 
		0 0 0 0 0 0 -0.8307197093963623;
createNode animCurveTL -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 15 ".ktv[0:14]"  282 -4.565 283 -4.9818964980000002 286 -6.0653450500000003
		 295 1.194142115 297 1.4564144459999999 299 0.28992000722905686 300 0.21939335749857491
		 301 0.1131767293 302 -0.018354229325950655 303 -0.16344964746190271 304 -0.30952605929337551
		 305 -0.44437557088940594 325 -0.44437557088940594 330 -0.44437557088940594 333 -0.65762053781669561;
	setAttr -s 15 ".kit[0:14]"  9 9 3 18 1 18 10 18 
		10 10 10 18 10 10 10;
	setAttr -s 15 ".kot[0:14]"  1 9 3 18 1 18 10 18 
		10 10 10 18 10 10 10;
	setAttr -s 15 ".kix[4:14]"  0.89417445659637451 0.18576309084892273 
		0.41235882043838501 0.31892001628875732 0.277814120054245 0.26493379473686218 0.27388343214988708 
		1 1 1 0.49041518568992615;
	setAttr -s 15 ".kiy[4:14]"  -0.44771859049797058 -0.98259454965591431 
		-0.91102153062820435 -0.94778168201446533 -0.96063482761383057 -0.96426659822463989 
		-0.96176284551620483 0 0 0 -0.87148892879486084;
	setAttr -s 15 ".kox[0:14]"  0.095508374273777008 0.10604076087474823 
		1 0.10115387290716171 0.89417445659637451 0.18576309084892273 0.41235882043838501 
		0.31892001628875732 0.277814120054245 0.26493379473686218 0.27388343214988708 1 1 
		1 0.49041518568992615;
	setAttr -s 15 ".koy[0:14]"  -0.99542856216430664 -0.99436181783676147 
		0 0.99487078189849854 -0.44771856069564819 -0.98259454965591431 -0.91102153062820435 
		-0.94778168201446533 -0.96063482761383057 -0.96426659822463989 -0.96176284551620483 
		0 0 0 -0.87148892879486084;
createNode animCurveTA -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 15 ".ktv[0:14]"  282 0 285 0.49119337869999996 289 2.175277742
		 293 -0.048711200099999998 297 -12.04303298 299 0.04469700703018905 300 0.022649143488919596
		 301 0 302 -0.014692879266425651 303 -0.018717293879025987 304 -0.015138875171511116
		 305 -0.011190695984865962 325 -0.011190695984865962 330 -0.011190695984865962 333 0;
	setAttr -s 15 ".kit[6:14]"  10 18 10 10 10 18 10 10 
		10;
	setAttr -s 15 ".kot[0:14]"  1 18 18 18 18 18 10 18 
		10 10 10 18 10 10 10;
	setAttr -s 15 ".kox[0:14]"  1 0.99093228578567505 1 0.80853348970413208 
		1 1 1 0.99996685981750488 1 1 1 1 1 1 1;
	setAttr -s 15 ".koy[0:14]"  0 0.13436216115951538 0 -0.58845019340515137 
		0 0 0 -0.0081465030089020729 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 15 ".ktv[0:14]"  282 0 285 0 289 0 293 0 297 0 299 -3.9892736511832516
		 300 -0.76423331467917532 301 4.0340076526842559 302 9.9334365175473369 303 16.461991555595468
		 304 23.147618682039287 305 29.518328424821963 325 29.518328424821963 330 29.518328424821963
		 333 -8.0064897273056594;
	setAttr -s 15 ".kit[0:14]"  18 18 18 18 18 10 10 18 
		10 10 10 18 10 10 10;
	setAttr -s 15 ".kot[0:14]"  1 18 18 18 18 10 10 18 
		10 10 10 18 10 10 10;
	setAttr -s 15 ".kox[0:14]"  1 1 1 1 1 0.99387907981872559 0.49605134129524231 
		0.39384251832962036 0.34603285789489746 0.32771819829940796 0.33124774694442749 1 
		1 1 0.18022485077381134;
	setAttr -s 15 ".koy[0:14]"  0 0 0 0 0 -0.11047297716140747 0.86829322576522827 
		0.91917794942855835 0.93822240829467773 0.94477552175521851 0.94354379177093506 0 
		0 0 -0.98362547159194946;
createNode animCurveTA -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 15 ".ktv[0:14]"  282 0 285 0 289 0 293 0 297 0 299 -0.073548499744261392
		 300 -0.038153047592133033 301 0 302 0.026023297021038228 303 0.030245792053531718
		 304 0.0084408523034309978 305 -0.039024422498392435 325 -0.039024422498392435 330 -0.039024422498392435
		 333 -0.032141015946140938;
	setAttr -s 15 ".kit[0:14]"  18 18 18 18 18 10 10 18 
		10 10 10 18 10 10 10;
	setAttr -s 15 ".kot[0:14]"  1 18 18 18 18 10 10 18 
		10 10 10 18 10 10 10;
	setAttr -s 15 ".kox[0:14]"  1 1 1 1 1 1 1 0.99990200996398926 1 1 1 
		1 1 1 1;
	setAttr -s 15 ".koy[0:14]"  0 0 0 0 0 0 0 0.013999748043715954 0 0 
		0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0.003192287722 286 1.27774403 289 2.1042589500000002
		 293 1.247603486 295 0.47592524959999999 297 0.1685320173 301 0 305 0 325 0 330 0
		 333 0;
	setAttr -s 11 ".kit[0:10]"  3 1 9 1 18 1 18 18 
		10 10 10;
	setAttr -s 11 ".kot[2:10]"  9 1 18 1 18 18 10 10 
		10;
	setAttr -s 11 ".kix[1:10]"  0.10732927173376083 0.99425619840621948 
		0.080437660217285156 0.14667190611362457 0.30019819736480713 1 1 1 1 1;
	setAttr -s 11 ".kiy[1:10]"  0.99422359466552734 -0.10702624171972275 
		-0.99675965309143066 -0.98918521404266357 -0.95387691259384155 0 0 0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 0.10732919722795486 0.99425619840621948 
		0.080437667667865753 0.14667190611362457 0.30019837617874146 1 1 1 1 1;
	setAttr -s 11 ".koy[0:10]"  0 0.99422353506088257 -0.10702624171972275 
		-0.99675965309143066 -0.98918521404266357 -0.953876793384552 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 41.414402590000002 285 70.513791449999999
		 289 64.298113889999996 293 26.237062760000001 295 10.424500220000001 297 0 301 0
		 305 0 325 0 330 0 333 0;
	setAttr -s 11 ".kit[0:10]"  9 1 1 18 18 18 18 18 
		10 10 10;
	setAttr -s 11 ".kot[0:10]"  1 1 1 18 18 18 18 18 
		10 10 10;
	setAttr -s 11 ".kix[1:10]"  0.014670044183731079 0.0053559695370495319 
		0.0044548227451741695 0.0060981246642768383 1 1 1 1 1 1;
	setAttr -s 11 ".kiy[1:10]"  0.99989241361618042 -0.99998563528060913 
		-0.99999010562896729 -0.99998146295547485 0 0 0 0 0 0;
	setAttr -s 11 ".kox[0:10]"  0.0041237589903175831 0.014670048840343952 
		0.0053559695370495319 0.0044548227451741695 0.0060981246642768383 1 1 1 1 1 1;
	setAttr -s 11 ".koy[0:10]"  0.99999147653579712 0.99989235401153564 
		-0.99998563528060913 -0.99999010562896729 -0.99998146295547485 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 285 0 289 -31.924829389999999 293 -7.1517914290000002
		 295 0.055656294910000001 297 13.07270244 299 4.0954804329999996 301 0 305 0 325 0
		 330 0 333 0;
	setAttr -s 12 ".kit[2:11]"  1 1 18 18 18 18 18 10 
		10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 1 1 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kix[2:11]"  0.023057013750076294 0.016495378687977791 
		0.0079109445214271545 1 0.012238316237926483 1 1 1 1 1;
	setAttr -s 12 ".kiy[2:11]"  -0.99973410367965698 0.99986392259597778 
		0.99996870756149292 0 -0.99992507696151733 0 0 0 0 0;
	setAttr -s 12 ".kox[0:11]"  1 1 0.023057019338011742 0.016495382413268089 
		0.0079109445214271545 1 0.012238316237926483 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 -0.99973410367965698 0.99986392259597778 
		0.99996870756149292 0 -0.99992507696151733 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 325 0 330 0 333 0;
	setAttr -s 10 ".kit[7:9]"  10 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 10 
		10 10;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 325 0 330 0 333 0;
	setAttr -s 10 ".kit[7:9]"  10 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 10 
		10 10;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footSide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 325 0 330 0 333 0;
	setAttr -s 10 ".kit[7:9]"  10 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 10 
		10 10;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 325 0 330 0 333 13.8;
	setAttr -s 10 ".kit[7:9]"  10 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 10 
		10 10;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.0086953146383166313;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0.9999622106552124;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 325 0 330 0 333 0;
	setAttr -s 10 ".kit[7:9]"  10 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 10 
		10 10;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 325 0 330 0 333 0;
	setAttr -s 10 ".kit[7:9]"  10 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 10 
		10 10;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 325 1 330 1 333 1;
	setAttr -s 10 ".kit[7:9]"  10 10 10;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 10 
		10 10;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 293 -10.31487242 297 -8.9962971659999997
		 299 -5.8739142219999998 301 -2.7093336099999998 325 -2.7093336099999998 330 -2.7093336099999998
		 333 -2.7093336099999998;
	setAttr -s 8 ".kit[4:7]"  9 10 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 9 10 10 10;
	setAttr -s 8 ".kox[0:7]"  1 1 0.053963597863912582 0.025441225618124008 
		0.31220996379852295 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0.9985429048538208 0.99967634677886963 
		0.95001310110092163 0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  282 0.62420995400000001 285 0.62420995400000001
		 289 0.62420995400000001 309 0.56761523515575696 325 0.56761523515575696 329 0.89633202605680395
		 333 0.89633202605680395;
	setAttr -s 7 ".kit[0:6]"  18 18 3 10 10 10 10;
	setAttr -s 7 ".kot[0:6]"  1 18 3 10 10 10 10;
	setAttr -s 7 ".kox[0:6]"  1 1 1 1 1 1 1;
	setAttr -s 7 ".koy[0:6]"  0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0.099499536370000002 285 0 289 0 293 0
		 297 0 300 0.088533124929999998 301 0.1942462392 305 0.1015264707 309 0 325 0 329 0.23056437481359676
		 333 0.23056437481359676;
	setAttr -s 12 ".kit[0:11]"  9 18 18 18 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kox[0:11]"  0.76979756355285645 1 1 1 1 0.635783851146698 
		1 0.85483413934707642 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  -0.63828808069229126 0 0 0 0 0.77186715602874756 
		0 -0.51890146732330322 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 1.5815872099999999 284 0.79755553800000001
		 293 -2.7214534910000001 297 -4.2860892399999999 300 -5.4711722739999997 309 -0.75403020745072236
		 325 -0.75403020745072236 329 -2.3637400345470132 333 -2.3637400345470132;
	setAttr -s 9 ".kit[0:8]"  1 1 1 9 18 10 10 10 
		10;
	setAttr -s 9 ".kot[0:8]"  1 1 1 9 18 10 10 10 
		10;
	setAttr -s 9 ".kix[0:8]"  0.10172288119792938 0.10134435445070267 
		0.10317977517843246 0.10130463540554047 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  -0.99481284618377686 -0.99485135078430176 
		-0.99466276168823242 -0.99485540390014648 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  0.10172288119792938 0.10134438425302505 
		0.10317979007959366 0.10130463540554047 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  -0.99481284618377686 -0.99485146999359131 
		-0.99466276168823242 -0.99485540390014648 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 13 ".ktv[0:12]"  282 -8.4569858730000007 284 0 285 0 289 0
		 293 0 297 0 300 0 301 0 305 -4.8862788029999997 309 0 325 0 329 10.553454122744823
		 333 10.553454122744823;
	setAttr -s 13 ".kit[0:12]"  9 18 18 18 18 18 18 18 
		18 1 10 10 10;
	setAttr -s 13 ".kot[0:12]"  1 18 18 18 18 18 18 18 
		18 1 10 10 10;
	setAttr -s 13 ".kix[9:12]"  0.048467140644788742 1 1 1;
	setAttr -s 13 ".kiy[9:12]"  -0.017432780936360359 0 0 0;
	setAttr -s 13 ".kox[0:12]"  0.0094592031091451645 1 1 1 1 1 1 1 1 0.048467148095369339 
		1 1 1;
	setAttr -s 13 ".koy[0:12]"  0.017452511936426163 0 0 0 0 0 0 0 0 -0.017432780936360359 
		0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 285 0 289 0 293 0 297 0 300 0 301 0
		 305 0 309 -10.485742557380572 325 -10.485742557380572 329 -53.102934721195425 333 -53.102934721195425;
	setAttr -s 12 ".kit[9:11]"  10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 285 0 289 0 293 0 297 0 300 0 301 0
		 305 0 309 0 325 0 329 -14.917379087945164 333 -14.917379087945164;
	setAttr -s 12 ".kit[9:11]"  10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 285 0 289 0 293 0 297 0 300 0.23635545299999999
		 303 1.425899974 305 1.963392238 309 0 325 0 329 0 333 0;
	setAttr -s 12 ".kit[6:11]"  1 9 18 10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 1 9 
		18 10 10 10;
	setAttr -s 12 ".kix[6:11]"  0.10409232974052429 0.16597992181777954 
		1 1 1 1;
	setAttr -s 12 ".kiy[6:11]"  0.99456769227981567 -0.98612916469573975 
		0 0 0 0;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 0.16686376929283142 0.10409232974052429 
		0.16597992181777954 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0.98597997426986694 0.99456769227981567 
		-0.98612916469573975 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 285 0 289 0 293 4.9608091429999996
		 297 31.66800654 300 65.267643879999994 303 82.625477059999994 305 70.459951700000005
		 309 0 325 0 329 0 333 0;
	setAttr -s 12 ".kit[0:11]"  18 18 18 9 1 9 9 9 
		18 10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 9 1 9 9 9 
		18 10 10 10;
	setAttr -s 12 ".kix[4:11]"  0.0052968976087868214 0.0047097532078623772 
		0.038489937782287598 0.002904658205807209 1 1 1 1;
	setAttr -s 12 ".kiy[4:11]"  0.99998599290847778 0.99998891353607178 
		0.99925893545150757 -0.99999582767486572 0 0 0 0;
	setAttr -s 12 ".kox[0:11]"  1 1 1 0.010104309767484665 0.0052968976087868214 
		0.0047097532078623772 0.038489937782287598 0.002904658205807209 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0.99994897842407227 0.99998599290847778 
		0.99998891353607178 0.99925893545150757 -0.99999582767486572 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 14 ".ktv[0:13]"  282 21.312941129999999 284 6.2 285 0 289 0
		 293 0 297 0 300 -4.1878059470000002 301 -12.34735145 303 -35.094081780000003 305 -57.227426819999998
		 309 0 325 0 329 0 333 0;
	setAttr -s 14 ".kit[0:13]"  3 1 18 18 18 18 18 18 
		18 3 9 10 10 10;
	setAttr -s 14 ".kot[0:13]"  1 1 18 18 18 18 18 18 
		18 3 9 10 10 10;
	setAttr -s 14 ".kix[1:13]"  0.003119621891528368 1 1 1 1 0.01295714545994997 
		0.0038826735690236092 0.0035650304052978754 1 0.013977949507534504 1 1 1;
	setAttr -s 14 ".kiy[1:13]"  -0.99999511241912842 0 0 0 0 -0.99991607666015625 
		-0.99999243021011353 -0.99999362230300903 0 0.99990230798721313 0 0 0;
	setAttr -s 14 ".kox[0:13]"  1 0.003119621891528368 1 1 1 1 0.012957144528627396 
		0.0038826735690236092 0.0035650304052978754 1 0.013977949507534504 1 1 1;
	setAttr -s 14 ".koy[0:13]"  0 -0.99999511241912842 0 0 0 0 -0.99991607666015625 
		-0.99999243021011353 -0.99999362230300903 0 0.99990230798721313 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 285 0 289 0 293 0 297 0 300 0 301 0
		 305 0 309 0 325 0 329 0 333 0;
	setAttr -s 12 ".kit[9:11]"  10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 285 0 289 0 293 0 297 0 300 0 301 0
		 305 0 309 0 325 0 329 0 333 0;
	setAttr -s 12 ".kit[9:11]"  10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footSide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 285 0 289 0 293 0 297 0 300 0 301 0
		 305 0 309 0 325 0 329 0 333 0;
	setAttr -s 12 ".kit[9:11]"  10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 285 0 289 0 293 0 297 0 300 0 301 0
		 305 0 309 0 325 0 329 0 333 0;
	setAttr -s 12 ".kit[9:11]"  10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 285 0 289 0 293 0 297 0 300 0 301 0
		 305 0 309 0 325 0 329 0 333 0;
	setAttr -s 12 ".kit[9:11]"  10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 285 0 289 0 293 0 297 0 300 0 301 0
		 305 0 309 0 325 0 329 0 333 0;
	setAttr -s 12 ".kit[9:11]"  10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 1 285 1 289 1 293 1 297 1 300 1 301 1
		 305 1 309 1 325 1 329 1 333 1;
	setAttr -s 12 ".kit[9:11]"  10 10 10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 10 10 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  282 -13.556659460000001 284 -8.7023436729999997
		 297 0 309 -7.6186707250000003 325 -7.6186707250000003 329 -7.6186707250000003 333 -7.6186707250000003;
	setAttr -s 7 ".kit[0:6]"  18 1 18 1 10 10 10;
	setAttr -s 7 ".kot[0:6]"  1 1 18 1 10 10 10;
	setAttr -s 7 ".kix[1:6]"  0.024968948215246201 1 0.040281467139720917 
		1 1 1;
	setAttr -s 7 ".kiy[1:6]"  0.99968820810317993 0 -0.99918836355209351 
		0 0 0;
	setAttr -s 7 ".kox[0:6]"  1 0.024968948215246201 1 0.04028145968914032 
		1 1 1;
	setAttr -s 7 ".koy[0:6]"  0 0.99968820810317993 0 -0.99918836355209351 
		0 0 0;
createNode animCurveTL -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 16 ".ktv[0:15]"  282 -4.640281409 283 -4.7183069729999998
		 284 -4.7972636719999997 285 -4.877574385 286 -4.9656633079999999 287 -5.0593355789999999
		 288 -5.1464944040000002 293 -5.2732487960718313 300 -5.1310386027778643 302 -4.7285781526967581
		 305 -4.5858980496340429 309 -4.7627993788656626 312 -5.2323970751977669 315 -5.2741954885618085
		 326 -5.3702955110007959 333 -2.1101222113771168;
	setAttr -s 16 ".kit[9:15]"  10 10 10 10 18 18 10;
	setAttr -s 16 ".kot[0:15]"  1 18 18 18 18 18 18 18 
		18 10 10 10 10 18 18 10;
	setAttr -s 16 ".kox[0:15]"  1 0.45405119657516479 0.44885662198066711 
		0.42910102009773254 0.40284410119056702 0.40458166599273682 0.7465139627456665 1 
		0.55139374732971191 0.3444291353225708 0.99261391162872314 0.39742836356163025 1 
		0.97099387645721436 1 0.085569910705089569;
	setAttr -s 16 ".koy[0:15]"  0 -0.89097559452056885 -0.89360374212265015 
		-0.90325653553009033 -0.9152686595916748 -0.91450178623199463 -0.66536968946456909 
		0 0.83424520492553711 0.93881231546401978 -0.12131606042385101 -0.91763323545455933 
		0 -0.23910436034202576 0 0.99633216857910156;
createNode animCurveTL -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 16 ".ktv[0:15]"  282 0.20825323979999999 283 0.12607619610000001
		 284 0.039166316110000002 285 -0.041524018750000002 286 -0.084050807830000004 287 -0.09999287187
		 288 -0.040151352129999998 293 0.91676928149995773 300 -0.17568421398610917 302 0.076776210735390538
		 305 0.20855381979291085 309 0.1915882413635045 312 0.2727110715258973 315 0.1133550164518168
		 326 0.11188302044159537 333 2.3593300913918434;
	setAttr -s 16 ".kit[9:15]"  10 10 10 10 18 18 10;
	setAttr -s 16 ".kot[0:15]"  1 18 18 18 18 18 18 18 
		18 10 10 10 10 18 18 10;
	setAttr -s 16 ".kox[0:15]"  1 0.42767640948295593 0.43076866865158081 
		0.54455184936523438 0.80735564231872559 1 0.22973091900348663 1 1 0.46170890331268311 
		1 1 0.95076239109039307 0.99994963407516479 1 0.12362992018461227;
	setAttr -s 16 ".koy[0:15]"  0 -0.90393191576004028 -0.90246236324310303 
		-0.83872717618942261 -0.59006506204605103 0 0.97325420379638672 0 0 0.88703149557113647 
		0 0 -0.3099207878112793 -0.01003583986312151 0 0.99232840538024902;
createNode animCurveTL -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 16 ".ktv[0:15]"  282 3.08538405 283 3.1122877309999999 284 3.1417021699999998
		 285 3.164565117 286 3.1719671379999999 287 3.1687384249999999 288 3.1571515809999999
		 293 2.9343247914472474 300 3.3076089964556865 302 3.7085131524502679 305 3.909451676065502
		 309 3.8250541465304142 312 3.285456929334015 315 3.3401790158699947 326 3.3199687236711535
		 333 6.3605992440425103;
	setAttr -s 16 ".kit[9:15]"  10 10 10 10 18 18 10;
	setAttr -s 16 ".kot[0:15]"  1 18 18 18 18 18 18 18 
		18 10 10 10 10 18 18 10;
	setAttr -s 16 ".kox[0:15]"  1 0.81770116090774536 0.83711463212966919 
		0.9353066086769104 1 0.98328077793121338 0.75481921434402466 1 0.42164605855941772 
		0.31535568833351135 0.92322391271591187 0.40939429402351379 0.44360664486885071 1 
		1 0.091698102653026581;
	setAttr -s 16 ".koy[0:15]"  0 0.57564294338226318 0.547027587890625 
		0.35383814573287964 0 -0.18209615349769592 -0.65593290328979492 0 0.90676051378250122 
		0.94897353649139404 0.38426259160041809 -0.9123576283454895 -0.89622151851654053 
		0 0 0.99578684568405151;
createNode animCurveTA -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 -74.227128469999997 283 -74.587271799999996
		 284 -75.013273859999998 285 -75.457116350000021 286 -75.870071659999994 287 -76.202724790000005
		 288 -76.405209929999998 293 -74.043590140000006 300 -72.768381950000006 315 -74.627133872354349
		 326 -74.627133872354349 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 0.98560881614685059 0.98246568441390991 
		0.98297452926635742 0.9870266318321228 0.99325394630432129 1 0.99136942625045776 
		1 1 1 0.21017129719257355;
	setAttr -s 12 ".koy[0:11]"  0 -0.16904224455356598 -0.18644332885742188 
		-0.1837419867515564 -0.16055634617805481 -0.11596018821001053 0 0.13109762966632843 
		0 0 0 0.97766458988189697;
createNode animCurveTA -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 -145.97571919999999 283 -146.1348691
		 284 -146.32446519999999 285 -146.5235323 286 -146.7101332 287 -146.86141 288 -146.95390829999999
		 293 -145.8950159 300 -145.34194189999999 315 -146.16129004039286 326 -146.16129004039286
		 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 0.99711805582046509 0.99642437696456909 
		0.99647891521453857 0.99729418754577637 0.99858886003494263 1 0.9982866644859314 
		1 1 1 0.10910570621490479;
	setAttr -s 12 ".koy[0:11]"  0 -0.075865373015403748 -0.08449004590511322 
		-0.083843521773815155 -0.073514096438884735 -0.053107846528291702 0 0.058512385934591293 
		0 0 0 0.9940301775932312;
createNode animCurveTA -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 -25.457694430000004 283 -25.64421845
		 284 -25.862927880000001 285 -26.088579110000001 286 -26.296495620000002 287 -26.462557740000005
		 288 -26.563017729999999 293 -25.362063729999999 300 -24.686946299999999 315 -25.652321377872418
		 326 -25.652321377872418 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 0.99611479043960571 0.99533379077911377 
		0.99555617570877075 0.9966881275177002 0.99831384420394897 1 0.99768131971359253 
		1 1 1 0.5302390456199646;
	setAttr -s 12 ".koy[0:11]"  0 -0.088064819574356079 -0.096492186188697815 
		-0.094169557094573975 -0.081319347023963928 -0.058047425001859665 0 0.068057775497436523 
		0 0 0 0.84784817695617676;
createNode animCurveTU -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_uprarmStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 -2.113338926 283 -2.1438466479999998
		 284 -2.1611618429999999 285 -2.1751789069999998 286 -2.1957922380000001 287 -2.232896218
		 288 -2.2963852720000002 293 -6.7620621139999999 300 -5.4133389259999998 315 -5.1920538614167535
		 326 -5.1920538614167535 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 0.85832983255386353 0.93113237619400024 
		0.91770720481872559 0.8109697699546814 0.62244588136672974 0.20553107559680939 1 
		0.67052578926086426 1 1 0.053850263357162476;
	setAttr -s 12 ".koy[0:11]"  0 -0.51309841871261597 -0.36468136310577393 
		-0.39725741744041443 -0.58508801460266113 -0.78266286849975586 -0.97865062952041626 
		0 0.74188625812530518 0 0 0.99854904413223267;
createNode animCurveTU -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_forearmStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 -2.113338926 283 -2.1438466479999998
		 284 -2.1611618429999999 285 -2.1751789069999998 286 -2.1957922380000001 287 -2.232896218
		 288 -2.2963852720000002 293 -6.7620621139999999 300 -5.4133389259999998 315 -5.1920538614167535
		 326 -5.1920538614167535 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 0.85832983255386353 0.93113237619400024 
		0.91770720481872559 0.8109697699546814 0.62244588136672974 0.20553107559680939 1 
		0.67052578926086426 1 1 0.053850263357162476;
	setAttr -s 12 ".koy[0:11]"  0 -0.51309841871261597 -0.36468136310577393 
		-0.39725741744041443 -0.58508801460266113 -0.78266286849975586 -0.97865062952041626 
		0 0.74188625812530518 0 0 0.99854904413223267;
createNode animCurveTU -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 283 0 284 0 285 0 286 0 287 0 288 0
		 293 0 300 0 315 0 326 0 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_elbowTwist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 71.7 283 71.7 284 71.7 285 71.7 286 71.7
		 287 71.7 288 71.7 293 71.7 300 71.7 315 71.7 326 71.7 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 0.0039051270578056574;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 -0.99999237060546875;
createNode animCurveTL -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 16 ".ktv[0:15]"  282 5.4243174749999996 283 5.3462110669999996
		 284 5.2671606960000004 285 5.1867546280000001 286 5.0985790230000001 287 5.0048383440000004
		 288 4.9176384950000003 293 4.7913918739281689 300 4.9339034342221355 302 5.3362750573162963
		 305 5.4786011195326685 309 5.3012815536379732 312 4.8316524922993898 315 4.7898854439418264
		 326 4.693785421502839 333 0.5832925526155982;
	setAttr -s 16 ".kit[9:15]"  10 10 10 10 18 18 10;
	setAttr -s 16 ".kot[0:15]"  1 18 18 18 18 18 18 18 
		18 10 10 10 10 18 18 10;
	setAttr -s 16 ".kox[0:15]"  1 0.45365080237388611 0.4484315812587738 
		0.42872282862663269 0.40255632996559143 0.4043770432472229 0.74723541736602783 1 
		0.55124402046203613 0.34467595815658569 0.99228066205978394 0.3971957266330719 1 
		0.97100645303726196 0.83643978834152222 0.06796080619096756;
	setAttr -s 16 ".koy[0:15]"  0 -0.89117956161499023 -0.89381706714630127 
		-0.90343606472015381 -0.91539520025253296 -0.914592444896698 -0.66455948352813721 
		0 0.83434414863586426 0.93872183561325073 -0.12401217967271805 -0.91773390769958496 
		0 -0.23905305564403534 -0.54805880784988403 -0.99768805503845215;
createNode animCurveTL -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 16 ".ktv[0:15]"  282 0.00086434227310000001 283 -0.078808866820000004
		 284 -0.16275476320000001 285 -0.2403546533 286 -0.28000419720000003 287 -0.29362738249999998
		 288 -0.2323739302 293 0.70810510439995766 300 -0.39319295070610916 302 -0.13970100338866043
		 305 -0.0038120702733902946 309 -0.015920769905996029 312 0.065202060256396827 315 -0.094153994817683703
		 326 -0.095625990827905141 333 3.4022506528813703;
	setAttr -s 16 ".kit[9:15]"  10 10 10 10 18 18 10;
	setAttr -s 16 ".kot[0:15]"  1 18 18 18 18 18 18 18 
		18 10 10 10 10 18 18 10;
	setAttr -s 16 ".kox[0:15]"  1 0.43924719095230103 0.44378000497817993 
		0.56361150741577148 0.83234095573425293 1 0.23299193382263184 1 1 0.45689049363136292 
		1 1 0.95076239109039307 0.99994963407516479 1 0.079793252050876617;
	setAttr -s 16 ".koy[0:15]"  0 -0.89836621284484863 -0.89613568782806396 
		-0.82603996992111206 -0.55426394939422607 0 0.97247868776321411 0 0 0.88952291011810303 
		0 0 -0.3099207878112793 -0.01003583986312151 0 0.99681144952774048;
createNode animCurveTL -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 16 ".ktv[0:15]"  282 2.8573279180000002 283 2.8827422930000002
		 284 2.9104221369999999 285 2.9315088610000002 286 2.9372865159999999 287 2.9327689939999999
		 288 2.9204062159999999 293 2.7070357464472474 300 3.0858018094556865 302 3.486020222663424
		 305 3.6844454737548324 309 3.5970923732714639 312 3.0572734787747939 315 3.1122172426110444
		 326 3.0920069504122032 333 -4.3276566404231565;
	setAttr -s 16 ".kit[9:15]"  10 10 10 10 18 18 10;
	setAttr -s 16 ".kot[0:15]"  1 18 18 18 18 18 18 18 
		18 10 10 10 10 18 18 10;
	setAttr -s 16 ".kox[0:15]"  1 0.83319771289825439 0.85386192798614502 
		0.94797807931900024 1 0.97845596075057983 0.73329943418502808 1 0.41950803995132446 
		0.31687209010124207 0.929534912109375 0.40766569972038269 0.44360664486885071 1 0.99063897132873535 
		0.037710685282945633;
	setAttr -s 16 ".koy[0:15]"  0 0.55297529697418213 0.52049946784973145 
		0.31833583116531372 0 -0.20645561814308167 -0.67990577220916748 0 0.90775161981582642 
		0.94846826791763306 0.36873406171798706 -0.9131312370300293 -0.89622151851654053 
		0 -0.13650766015052795 -0.99928873777389526;
createNode animCurveTA -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 -75.888045520000006 283 -76.143164290000001
		 284 -76.444317440000006 285 -76.757388950000006 286 -77.048056840000001 287 -77.281781960000004
		 288 -77.423870469999997 293 -75.757842030000006 300 -74.849546040000007 315 -76.167309264595048
		 326 -76.167309264595048 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 0.99271631240844727 0.99114072322845459 
		0.99143677949905396 0.99351930618286133 0.99665576219558716 1 0.99564754962921143 
		1 1 1 0.20610372722148895;
	setAttr -s 12 ".koy[0:11]"  0 -0.12047586590051651 -0.13281598687171936 
		-0.13058772683143616 -0.11366348713636398 -0.081714726984500885 0 0.093197755515575409 
		0 0 0 0.9785301685333252;
createNode animCurveTA -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 136.4998013 283 136.53053980000001 284 136.56839909999999
		 285 136.60955870000001 286 136.64941279999999 287 136.6826015 288 136.7032743 293 136.48458590000004
		 300 136.38735689999999 315 136.54376293219252 326 136.54376293219252 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 0.99988806247711182 0.99985140562057495 
		0.99984383583068848 0.99987310171127319 0.9999309778213501 1 0.99993401765823364 
		1 1 1 0.11668937653303146;
	setAttr -s 12 ".koy[0:11]"  0 0.014964057132601738 0.017236704006791115 
		0.017671704292297363 0.015933459624648094 0.011749816127121449 0 -0.011486333794891834 
		0 0 0 -0.99316847324371338;
createNode animCurveTA -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 7.6456983840000001 283 7.922237288999999
		 284 8.2480450750000003 285 8.5859944610000003 286 8.8990463260000006 287 9.1502547510000003
		 288 9.3027413570000004 293 7.5043799240000002 300 6.5153214349999997 315 7.9443726103792702
		 326 7.9443726103792702 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 0.99147570133209229 0.98967725038528442 
		0.99006432294845581 0.99250787496566772 0.99614417552947998 1 0.99490296840667725 
		1 1 1 0.89614170789718628;
	setAttr -s 12 ".koy[0:11]"  0 0.13029159605503082 0.1433146595954895 
		0.14061544835567474 0.12218032032251358 0.087732039391994476 0 -0.10083694010972977 
		0 0 0 -0.44376805424690247;
createNode animCurveTU -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_uprarmStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 283 -0.052058481810000001 284 -0.1863145665
		 285 -0.36988921279999998 286 -0.56990341649999998 287 -0.75347802610000003 288 -0.88773412920000005
		 293 -0.061470093929999997 300 2.8 315 5.0778132881456397 326 5.0778132881456397 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 0.39454761147499084 0.24409244954586029 
		0.2041635662317276 0.20416358113288879 0.24409520626068115 1 0.12907232344150543 
		0.16877380013465881 1 1 0.055058155208826065;
	setAttr -s 12 ".koy[0:11]"  0 -0.91887545585632324 -0.96975195407867432 
		-0.97893679141998291 -0.97893679141998291 -0.96975123882293701 0 0.99163514375686646 
		0.98565483093261719 0 0 -0.99848318099975586;
createNode animCurveTU -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_forearmStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 283 -0.052058481810000001 284 -0.1863145665
		 285 -0.36988921279999998 286 -0.56990341649999998 287 -0.75347802610000003 288 -0.88773412920000005
		 293 -0.061470093929999997 300 2.8 315 5.0778132881456397 326 5.0778132881456397 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 0.39454761147499084 0.24409244954586029 
		0.2041635662317276 0.20416358113288879 0.24409520626068115 1 0.12907232344150543 
		0.16877380013465881 1 1 0.055058155208826065;
	setAttr -s 12 ".koy[0:11]"  0 -0.91887545585632324 -0.96975195407867432 
		-0.97893679141998291 -0.97893679141998291 -0.96975123882293701 0 0.99163514375686646 
		0.98565483093261719 0 0 -0.99848318099975586;
createNode animCurveTU -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 0 283 0 284 0 285 0 286 0 287 0 288 0
		 293 0 300 0 315 0 326 0 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_elbowTwist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  282 52.4 283 52.4 284 52.4 285 52.4 286 52.4
		 287 52.4 288 52.4 293 52.4 300 52.4 315 52.4 326 52.4 333 0;
	setAttr -s 12 ".kit[11]"  10;
	setAttr -s 12 ".kot[0:11]"  1 18 18 18 18 18 18 18 
		18 18 18 10;
	setAttr -s 12 ".kox[0:11]"  1 1 1 1 1 1 1 1 1 1 1 0.0053434297442436218;
	setAttr -s 12 ".koy[0:11]"  0 0 0 0 0 0 0 0 0 0 0 -0.99998575448989868;
createNode animCurveTL -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 299 0 306 0 313 0 314 0 325 0
		 333 0;
	setAttr -s 8 ".kit[1:7]"  18 1 18 1 1 10 10;
	setAttr -s 8 ".kot[1:7]"  18 1 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.23999977111816406 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 299 0 306 0 313 0 314 0 325 0
		 333 0;
	setAttr -s 8 ".kit[1:7]"  18 1 18 1 1 10 10;
	setAttr -s 8 ".kot[1:7]"  18 1 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.23999977111816406 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 299 0 306 0 313 0 314 0 325 0
		 333 0;
	setAttr -s 8 ".kit[1:7]"  18 1 18 1 1 10 10;
	setAttr -s 8 ".kot[1:7]"  18 1 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.23999977111816406 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 -6.9047346379999999 288 -8.0845871380000016
		 292 -6.9350196130376371 299 -7.9936450660000009 306 -10.021306969999999 313 -6.9047346379999999
		 314 -6.9700908989329458 325 -6.9700908989329458 333 15.383860048090559;
	setAttr -s 9 ".kit[1:8]"  18 10 1 18 1 1 10 10;
	setAttr -s 9 ".kot[1:8]"  18 10 1 18 1 1 10 10;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 0.039999961853027344 1 0.63417041301727295;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 -0.0021612816490232944 0 0.77319324016571045;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 0.23999977111816406 1 0.63417047262191772;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 -0.012967753224074841 0 0.77319329977035522;
createNode animCurveTA -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 10.78330369 288 6.6964874730000004 292 -6.871281459430846
		 299 10.00718633 306 8.1907503970000004 313 10.78330369 314 10.556920284393586 325 10.556920284393586
		 333 -0.15710469165010174;
	setAttr -s 9 ".kit[1:8]"  18 10 1 18 1 1 10 10;
	setAttr -s 9 ".kot[1:8]"  18 10 1 18 1 1 10 10;
	setAttr -s 9 ".kix[0:8]"  1 0.79220467805862427 0.99148690700531006 
		1 1 1 0.039999961853027344 1 0.86339288949966431;
	setAttr -s 9 ".kiy[0:8]"  0 -0.61025547981262207 0.13020622730255127 
		0 0 0 -0.007486383430659771 0 -0.50453227758407593;
	setAttr -s 9 ".kox[0:8]"  1 0.79220473766326904 0.99148690700531006 
		1 1 1 0.23999977111816406 1 0.86339288949966431;
	setAttr -s 9 ".koy[0:8]"  0 -0.61025547981262207 0.13020622730255127 
		0 0 0 -0.044918186962604523 0 -0.50453227758407593;
createNode animCurveTA -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 -23.75261175 288 -26.53387141 292 -24.079382617017099
		 299 -29.781918740000002 306 -26.756168769999999 313 -23.75261175 314 -23.85745686353275
		 325 -23.85745686353275 333 -29.531661894717264;
	setAttr -s 9 ".kit[1:8]"  18 10 9 18 1 1 10 10;
	setAttr -s 9 ".kot[1:8]"  18 10 9 18 1 1 10 10;
	setAttr -s 9 ".kix[0:8]"  1 1 1 0.99653816223144531 0.98279857635498047 
		1 0.039999961853027344 1 0.95529764890670776;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 -0.083137579262256622 0.18468044698238373 
		0 -0.0035199010744690895 0 -0.29564568400382996;
	setAttr -s 9 ".kox[0:8]"  1 1 1 0.99653816223144531 0.98279863595962524 
		1 0.23999977111816406 1 0.95529764890670776;
	setAttr -s 9 ".koy[0:8]"  0 0 0 -0.083137579262256622 0.18468046188354492 
		0 -0.021119464188814163 0 -0.29564568400382996;
createNode animCurveTL -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 299 0 306 0 313 0 314 0 325 0
		 333 0;
	setAttr -s 8 ".kit[4:7]"  1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[4:7]"  1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[4:7]"  0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.23999977111816406 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 299 0 306 0 313 0 314 0 325 0
		 333 0;
	setAttr -s 8 ".kit[4:7]"  1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[4:7]"  1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[4:7]"  0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.23999977111816406 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 299 0 306 0 313 0 314 0 325 0
		 333 0;
	setAttr -s 8 ".kit[4:7]"  1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[4:7]"  1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[4:7]"  0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.23999977111816406 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 9.3944530240000006 288 9.5564404090000004
		 292 10.084392790556597 299 9.3944530240000006 306 10.06496566 313 9.3944530240000006
		 314 9.4034260861428578 325 9.4034260861428578 333 0;
	setAttr -s 9 ".kit[2:8]"  10 18 18 1 1 10 10;
	setAttr -s 9 ".kot[0:8]"  1 18 10 18 18 1 1 10 
		10;
	setAttr -s 9 ".kix[5:8]"  1 0.039999961853027344 1 0.88979673385620117;
	setAttr -s 9 ".kiy[5:8]"  0 0.00029675493715330958 0 -0.45635703206062317;
	setAttr -s 9 ".kox[0:8]"  1 0.99954718351364136 1 1 1 1 0.23999977111816406 
		1 0.88979679346084595;
	setAttr -s 9 ".koy[0:8]"  0 0.030090628191828728 0 0 0 0 0.001780410879291594 
		0 -0.45635706186294556;
createNode animCurveTA -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 24.10832602 288 26.17604729 292 11.173207437573755
		 299 24.10832602 306 19.046087920000002 313 24.10832602 314 24.597030816770665 325 24.597030816770665
		 333 0;
	setAttr -s 9 ".kit[2:8]"  10 18 18 1 1 10 10;
	setAttr -s 9 ".kot[0:8]"  1 18 10 18 18 1 1 10 
		10;
	setAttr -s 9 ".kix[5:8]"  0.078300744295120239 0.039999961853027344 
		1 0.59763705730438232;
	setAttr -s 9 ".kiy[5:8]"  0.017399707809090614 0.0081412931904196739 
		0 -0.80176669359207153;
	setAttr -s 9 ".kox[0:8]"  1 1 0.99665325880050659 1 1 0.078301176428794861 
		0.23999977111816406 1 0.5976371169090271;
	setAttr -s 9 ".koy[0:8]"  0 0 -0.081744998693466187 0 0 0.017399705946445465 
		0.048848092555999756 0 -0.80176675319671631;
createNode animCurveTA -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 -17.38942699 288 -17.008223279999999
		 292 -20.971927045108806 299 -17.38942699 306 -13.90833561 313 -17.38942699 314 -17.368310749504374
		 325 -17.368310749504374 333 0;
	setAttr -s 9 ".kit[2:8]"  10 18 18 1 1 10 10;
	setAttr -s 9 ".kot[0:8]"  1 18 10 18 18 1 1 10 
		10;
	setAttr -s 9 ".kix[5:8]"  1 0.039999961853027344 1 0.72597920894622803;
	setAttr -s 9 ".kiy[5:8]"  0 0.00069829018320888281 0 0.68771666288375854;
	setAttr -s 9 ".kox[0:8]"  1 1 0.9998856782913208 0.97661399841308594 
		1 1 0.23999977111816406 1 0.72597920894622803;
	setAttr -s 9 ".koy[0:8]"  0 0 -0.015119330957531929 0.21499989926815033 
		0 0 0.004189775325357914 0 0.68771666288375854;
createNode animCurveTL -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0 325 0 333 0;
createNode animCurveTL -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0 325 0 333 0;
createNode animCurveTL -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0 325 0 333 0;
createNode animCurveTA -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0 325 0 333 0;
createNode animCurveTA -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0 325 0 333 0;
createNode animCurveTA -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0 325 0 333 0;
createNode animCurveTU -n "ylva_original:m_armA_shoulder_ctrl_outPutAnimBank_1_followBody";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 1 325 1 333 1;
createNode animCurveTL -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -16.438895 347 0;
createNode animCurveTA -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 19.558546 347 0;
createNode animCurveTA -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -14.202342 347 0;
createNode animCurveTU -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_thumb_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 5.73649;
createNode animCurveTA -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 2.032196;
createNode animCurveTA -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -8.134621;
createNode animCurveTU -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_thumb_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -8.214251 347 0;
createNode animCurveTA -n "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 9.286062 347 0;
createNode animCurveTA -n "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 12.330358000000002 347 0;
createNode animCurveTU -n "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -26.12546 347 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -18.633547 347 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -0.22801100000000002 347 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -2.01014 347 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 0.11595500000000002 347 0;
createNode animCurveTU -n "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -5.793319 347 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -16.416886 347 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -2.840173 347 0;
createNode animCurveTU -n "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -31.151217 347 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -0.557562 347 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 1.513605 347 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -13.119081 347 0;
createNode animCurveTU -n "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTA -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 29.226087059999998 313 29.226087059999998
		 314 29.226087059999998 326 29.226087059999998 333 0;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 0.48119217157363892;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 -0.87661510705947876;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 0.48119217157363892;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 -0.87661510705947876;
createNode animCurveTA -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 4.2510370130000004 313 4.2510370130000004
		 314 4.2510370130000004 326 4.2510370130000004 333 0;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 0.96663933992385864;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 -0.25614100694656372;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 0.96663945913314819;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 -0.25614103674888611;
createNode animCurveTA -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 -0.82589306750000002 313 -0.82589306750000002
		 314 -0.82589306750000002 326 -0.82589306750000002 333 0;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_keepOrientation";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 1 326 1 333 1;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  282 1 326 1 333 0 347 1;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 0 313 0 314 0 326 0 333 0;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_neutral";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 1 313 1 314 1 326 1 333 1;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_fist";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 0.4 313 0.4 314 0.4 326 0.4 333 0.4;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_relax";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 0 313 0 314 0 326 0 333 0;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_curl";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 0 313 0 314 0 326 0 333 0;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_spread";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 0 313 0 314 0 326 0 333 0;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_splay";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 0 313 0 314 0 326 0 333 0;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_break";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 0 313 0 314 0 326 0 333 0;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_flex";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 0 313 0 314 0 326 0 333 0;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -6.527843;
createNode animCurveTA -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -0.105422;
createNode animCurveTA -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -16.908326000000002;
createNode animCurveTU -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_thumb_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -22.429684;
createNode animCurveTA -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 6.872709;
createNode animCurveTA -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -16.862834;
createNode animCurveTU -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_thumb_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 26.442174;
createNode animCurveTA -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 2.724606;
createNode animCurveTA -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1.8388970000000002;
createNode animCurveTU -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_thumb_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 6.833799;
createNode animCurveTA -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -37.553707;
createNode animCurveTA -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0.354347;
createNode animCurveTU -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_index_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 7.1336920000000008;
createNode animCurveTA -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -25.42722;
createNode animCurveTA -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 5.05311;
createNode animCurveTU -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_index_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -14.922301;
createNode animCurveTA -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -22.308327;
createNode animCurveTA -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 7.8126400000000009;
createNode animCurveTU -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_index_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1.9789469999999998;
createNode animCurveTA -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -6.4326250000000007;
createNode animCurveTA -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -0.93047100000000016;
createNode animCurveTU -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_middle_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -39.204499;
createNode animCurveTA -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_middle_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -7.855638;
createNode animCurveTA -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -12.355324000000001;
createNode animCurveTA -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -6.130316;
createNode animCurveTU -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_middle_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 4.037581;
createNode animCurveTA -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -27.788193;
createNode animCurveTA -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -0.319069;
createNode animCurveTU -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_ring_04_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -23.713701;
createNode animCurveTA -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_ring_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -31.667669000000004;
createNode animCurveTA -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -11.375659;
createNode animCurveTA -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -18.117976;
createNode animCurveTU -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_ring_02_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTL -n "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTA -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 15.056219889999999 313 15.056219889999999
		 314 15.056219889999999 326 15.056219889999999 333 -157.44489946070146;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 0.092601552605628967;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 -0.99570322036743164;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 0.092601560056209564;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 -0.99570327997207642;
createNode animCurveTA -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 0.84392198100000015 313 0.84392198100000015
		 314 0.84392198100000015 326 0.84392198100000015 333 -8.1412081994142849;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 0.8724791407585144;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 -0.48865142464637756;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 0.8724791407585144;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 -0.48865142464637756;
createNode animCurveTA -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  282 6.086156635 313 6.086156635 314 6.086156635
		 326 6.086156635 333 1.2328648305067906;
	setAttr -s 5 ".kit[3:4]"  10 10;
	setAttr -s 5 ".kot[3:4]"  10 10;
	setAttr -s 5 ".kix[0:4]"  1 1 0.039999961853027344 1 0.95715945959091187;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 -0.28956124186515808;
	setAttr -s 5 ".kox[0:4]"  1 1 1.1999988555908203 1 0.95715951919555664;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 -0.28956127166748047;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_keepOrientation";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 1 326 1 333 1;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 1 326 1 333 1;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 297 0 306 0 313 0 314 0 326 0
		 333 0;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.19999980926513672 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_neutral";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 1 288 1 297 1 306 1 313 1 314 1 326 1
		 333 1;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.19999980926513672 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_fist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0.4 288 0.4 297 0.4 306 0.4 313 0.4
		 314 0.4 326 0.4 333 0.4;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.19999980926513672 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_relax";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 297 0 306 0 313 0 314 0 326 0
		 333 0;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.19999980926513672 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_curl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 297 0 306 0 313 0 314 0 326 0
		 333 0;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.19999980926513672 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_spread";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 297 0 306 0 313 0 314 0 326 0
		 333 0;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.19999980926513672 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_splay";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 297 0 306 0 313 0 314 0 326 0
		 333 0;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.19999980926513672 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_break";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 297 0 306 0 313 0 314 0 326 0
		 333 0;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.19999980926513672 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_flex";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 288 0 297 0 306 0 313 0 314 0 326 0
		 333 0;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 1 1 10 10;
	setAttr -s 8 ".kix[0:7]"  1 1 1 1 1 0.039999961853027344 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 0 0 0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 0.19999980926513672 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_orbit";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_nod";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_side";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_twist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_neckStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_compensation";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0 324 0 333 0;
	setAttr -s 3 ".kit[0:2]"  1 10 10;
	setAttr -s 3 ".kot[0:2]"  1 10 10;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0 324 0 333 0;
	setAttr -s 3 ".kit[0:2]"  1 10 10;
	setAttr -s 3 ".kot[0:2]"  1 10 10;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0 324 0 333 0;
	setAttr -s 3 ".kit[0:2]"  1 10 10;
	setAttr -s 3 ".kot[0:2]"  1 10 10;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 -6.5903558020000004 285 -6.8476641210000002
		 287 -6.947952538 289 -7.1495964480000005 291 -7.0891161760000001 294 -18.690407016977439
		 302 -14.094483503367545 308 -15.361272927705077 315 -31.701252071342068 324 -34.424581928614906
		 333 -4.3155092063812006;
	setAttr -s 11 ".kit[0:10]"  1 18 18 9 18 18 10 18 
		1 10 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 9 18 18 10 18 
		1 10 10;
	setAttr -s 11 ".kix[0:10]"  0.43804526329040527 0.99951344728469849 
		0.99945807456970215 0.99988150596618652 1 1 1 0.96386677026748657 0.94917213916778564 
		1 0.56516003608703613;
	setAttr -s 11 ".kiy[0:10]"  -0.015689689666032791 -0.031191049143671989 
		-0.032917696982622147 -0.01539666298776865 0 0 0 -0.26638469099998474 -0.31475734710693359 
		0 0.82498133182525635;
	setAttr -s 11 ".kox[0:10]"  0.43804538249969482 0.99951344728469849 
		0.99945807456970215 0.99988150596618652 1 1 1 0.96386682987213135 0.94917213916778564 
		1 0.56516003608703613;
	setAttr -s 11 ".koy[0:10]"  -0.015689687803387642 -0.03119104728102684 
		-0.032917693257331848 -0.01539666298776865 0 0 0 -0.26638469099998474 -0.31475734710693359 
		0 0.82498133182525635;
createNode animCurveTA -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 2.3080151680000003 285 0.87457588980000001
		 287 0.25331928310000001 289 0.1731109217 291 1.1767559599999999 294 -7.1612871566419756
		 302 -4.3738817360372915 308 -7.7913730244971093 315 -12.724628677968433 324 -13.546837953546985
		 333 -16.71356317875232;
	setAttr -s 11 ".kit[0:10]"  9 18 18 1 18 18 10 3 
		1 10 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 1 18 18 10 3 
		1 10 10;
	setAttr -s 11 ".kix[3:10]"  1 1 1 1 1 0.99502551555633545 1 0.98841899633407593;
	setAttr -s 11 ".kiy[3:10]"  0 0 0 0 0 -0.099620133638381958 0 -0.15174931287765503;
	setAttr -s 11 ".kox[0:10]"  0.083422854542732239 0.98430216312408447 
		0.99862492084503174 1 1 1 1 1 0.99502551555633545 1 0.9884190559387207;
	setAttr -s 11 ".koy[0:10]"  -0.017392454668879509 -0.17649149894714355 
		-0.052423488348722458 0 0 0 0 0 -0.099620133638381958 0 -0.15174932777881622;
createNode animCurveTA -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 -0.035720683529999998 286 -3.183407055
		 291 1.11496353 294 0.391628815169629 302 2.9890440188233547 308 9.3959520053726333
		 315 6.4228658874348916 324 5.9273515344452683 333 -3.4837608652417171;
	setAttr -s 9 ".kit[0:8]"  9 18 18 18 10 10 1 10 
		10;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 10 10 1 10 
		10;
	setAttr -s 9 ".kix[6:8]"  0.9981846809387207 1 0.90977656841278076;
	setAttr -s 9 ".kiy[6:8]"  -0.060227889567613602 0 -0.41509833931922913;
	setAttr -s 9 ".kox[0:8]"  0.050765395164489746 1 1 1 1 0.99342381954193115 
		0.9981846809387207 1 0.90977656841278076;
	setAttr -s 9 ".koy[0:8]"  -0.017430787906050682 0 0 0 0 0.11449486017227173 
		-0.060227889567613602 0 -0.41509833931922913;
createNode animCurveTU -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 1 324 1 333 1;
	setAttr -s 3 ".kit[0:2]"  1 10 10;
	setAttr -s 3 ".kot[0:2]"  1 10 10;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 1 324 1 333 1;
	setAttr -s 3 ".kit[0:2]"  1 10 10;
	setAttr -s 3 ".kot[0:2]"  1 10 10;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 1 324 1 333 1;
	setAttr -s 3 ".kit[0:2]"  1 10 10;
	setAttr -s 3 ".kot[0:2]"  1 10 10;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  282 0 297 0 313 0 314 0;
	setAttr -s 4 ".kit[0:3]"  18 18 1 1;
	setAttr -s 4 ".kot[1:3]"  18 1 1;
	setAttr -s 4 ".kix[2:3]"  1 0.039999961853027344;
	setAttr -s 4 ".kiy[2:3]"  0 0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 0.55999946594238281;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  282 0 297 0 313 0 314 0;
	setAttr -s 4 ".kit[0:3]"  18 18 1 1;
	setAttr -s 4 ".kot[1:3]"  18 1 1;
	setAttr -s 4 ".kix[2:3]"  1 0.039999961853027344;
	setAttr -s 4 ".kiy[2:3]"  0 0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 0.55999946594238281;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  282 0 297 0 313 0 314 0;
	setAttr -s 4 ".kit[0:3]"  18 18 1 1;
	setAttr -s 4 ".kot[1:3]"  18 1 1;
	setAttr -s 4 ".kix[2:3]"  1 0.039999961853027344;
	setAttr -s 4 ".kiy[2:3]"  0 0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 0.55999946594238281;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  282 0 297 0 313 0 314 0;
	setAttr -s 4 ".kit[0:3]"  9 9 1 1;
	setAttr -s 4 ".kot[1:3]"  9 1 1;
	setAttr -s 4 ".kix[2:3]"  1 0.039999961853027344;
	setAttr -s 4 ".kiy[2:3]"  0 0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 0.55999946594238281;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  282 0 289 -1.567426234 297 0.40483984960000002
		 305 2.3771059330000002 313 0 314 -0.25133643213735246;
	setAttr -s 6 ".kit[0:5]"  9 18 18 18 1 1;
	setAttr -s 6 ".kot[0:5]"  1 18 18 18 1 1;
	setAttr -s 6 ".kix[4:5]"  0.17585298418998718 0.039999961853027344;
	setAttr -s 6 ".kiy[4:5]"  -0.017181308940052986 -0.0047854357399046421;
	setAttr -s 6 ".kox[0:5]"  0.1758534163236618 1 0.99426400661468506 
		1 0.17585298418998718 0.23999977111816406;
	setAttr -s 6 ".koy[0:5]"  -0.017181305214762688 0 0.10695350170135498 
		0 -0.017181307077407837 -0.028712613508105278;
createNode animCurveTA -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  282 0 286 -3.5201430349999998 293 1.796839283
		 301 -3.3974993750000002 309 1.8968434569999999 313 0 314 -0.93090308395920296;
	setAttr -s 7 ".kit[0:6]"  9 18 18 18 18 1 1;
	setAttr -s 7 ".kot[0:6]"  1 18 18 18 18 1 1;
	setAttr -s 7 ".kix[5:6]"  0.058970749378204346 0.039999961853027344;
	setAttr -s 7 ".kiy[5:6]"  -0.017422918230295181 -0.019495336338877678;
	setAttr -s 7 ".kox[0:6]"  0.045405779033899307 1 1 1 1 0.058970749378204346 
		0.11999988555908203;
	setAttr -s 7 ".koy[0:6]"  -0.017435291782021523 0 0 0 0 -0.017422918230295181 
		-0.058486003428697586;
createNode animCurveTL -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[0:9]"  1 1 1 1 1 1 1 1 1 0.039999961853027344;
	setAttr -s 10 ".kiy[0:9]"  0 0 0 0 0 0 0 0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[0:9]"  1 1 1 1 1 1 1 1 1 0.039999961853027344;
	setAttr -s 10 ".kiy[0:9]"  0 0 0 0 0 0 0 0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[0:9]"  1 1 1 1 1 1 1 1 1 0.039999961853027344;
	setAttr -s 10 ".kiy[0:9]"  0 0 0 0 0 0 0 0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[0:9]"  1 1 1 1 1 1 1 1 1 0.039999961853027344;
	setAttr -s 10 ".kiy[0:9]"  0 0 0 0 0 0 0 0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[0:9]"  1 1 1 1 1 1 1 1 1 0.039999961853027344;
	setAttr -s 10 ".kiy[0:9]"  0 0 0 0 0 0 0 0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0 313 0 314 0;
	setAttr -s 3 ".kit[0:2]"  9 1 1;
	setAttr -s 3 ".kix[1:2]"  1 0.039999961853027344;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1.1999988555908203;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "ylva_original:RgtOuterBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtOuterBrow_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 -0.49775790440000001;
createNode animCurveTL -n "ylva_original:RgtOuterBrow_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTA -n "ylva_original:RgtOuterBrow_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:RgtMidBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtMidBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTL -n "ylva_original:RgtMidBrow_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 -0.18317128050000001;
createNode animCurveTA -n "ylva_original:RgtMidBrow_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:LftMidBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftMidBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTL -n "ylva_original:LftMidBrow_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 -0.18317128050000001;
createNode animCurveTA -n "ylva_original:LftMidBrow_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:LftOuterBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftOuterBrow_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 -0.49775790440000001;
createNode animCurveTA -n "ylva_original:LftOuterBrow_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:rgtHappyBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:rgtHappyBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:rgtMadBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:rgtMadBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:rgtSadBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:rgtSadBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0.69098946569999997;
createNode animCurveTU -n "ylva_original:rgtBoredBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:rgtBoredBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:lftHappyBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:lftHappyBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:lftMadBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:lftMadBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:lftSadBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:lftSadBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0.69098946569999997;
createNode animCurveTU -n "ylva_original:lftBoredBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:lftBoredBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:RgtTopLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtTopLid_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 -0.30152130780000003;
createNode animCurveTU -n "ylva_original:LftTopLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftTopLid_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 -0.30152130780000003;
createNode animCurveTU -n "ylva_original:RgtBtmLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtBtmLid_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:LftBtmLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftBtmLid_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:eyeDarts_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:eyeDarts_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTL -n "ylva_original:eyeDarts_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:JawRock_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:JawRock_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:JawRock_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:JawRock_outPutAnimBank_1_mouthHold";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:MouthEmotion_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:MouthEmotion_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 -0.01432669837087147 345 0
		 347 0 351 0;
createNode animCurveTL -n "ylva_original:MouthEmotion_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 -0.83769746919999999 291 -0.83769746919999999
		 294 0 297 -0.35225426985413683 299 -1 302 -0.89178790402181174 304 0 306 0 308 -1
		 310 -1 312 -0.33698435655984837 313 0 315 -0.20918180045326168 316 -0.20780741545912321
		 318 -0.62628486251939275 319 -1 321 -1 322 0 323 0 324 -0.42084951898085327 325 -0.54279259291723014
		 327 -0.96020350080108652 329 0 331 0 333 -0.33069597473919149 335 0 336 0 338 0.12858448114620535
		 339 0 341 0 343 -0.66590545753580344 345 -1 347 -0.88014284401610032 351 -0.83769746919999999;
createNode animCurveTU -n "ylva_original:MouthSlide_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:MouthSlide_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 -0.22006997140000001 291 -0.22006997140000001
		 294 0 297 0 299 0 302 0 304 0 306 0 308 0 310 0 312 1.776356839e-015 313 1.776356839e-015
		 315 0.069556914036281475 316 0.1440599112532597 318 0.2585690714802083 319 0.2585690714802083
		 321 0.2585690714802083 322 0.2158235998128572 323 0.2158235998128572 324 0.26044559042378823
		 325 0.26192128326155562 327 0.2585690714802083 329 0.2585690714802083 331 0.2585690714802083
		 333 0.2585690714802083 335 0.30063612353630764 336 0.30063612353630764 338 0.25856907148021008
		 339 0.25856907148021008 341 0.30223133770379795 343 0.2585690714802083 345 0.2585690714802083
		 347 0.2585690714802083 351 0.29953076124010614;
createNode animCurveTL -n "ylva_original:MouthSlide_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 -0.0080647164359999995 291 -0.0080647164359999995
		 294 0 297 -0.086206650901691162 299 0 302 0 304 0 306 0 308 0 310 0 312 7.1054273579999998e-015
		 313 7.1054273579999998e-015 315 0 316 0 318 0.12754050227835761 319 0 321 0 322 7.1054273579999998e-015
		 323 7.1054273579999998e-015 324 7.1054273579999998e-015 325 7.1054273579999998e-015
		 327 0 329 0 331 0 333 0 335 7.1054273579999998e-015 336 7.1054273579999998e-015 338 0
		 339 0 341 0 343 0 345 0.12583707215602782 347 0 351 -0.0080647164359999995;
createNode animCurveTU -n "ylva_original:UprLip_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:UprLip_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1.776356839e-015 291 1.776356839e-015
		 294 0 297 0 299 0 302 0 304 0 306 0 308 0 310 0 312 1.776356839e-015 313 1.776356839e-015
		 315 0 316 0 318 0 319 0 321 0 322 1.776356839e-015 323 1.776356839e-015 324 1.776356839e-015
		 325 1.776356839e-015 327 0 329 0 331 0 333 0 335 1.776356839e-015 336 1.776356839e-015
		 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:UprLip_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 7.1054273579999998e-015 291 7.1054273579999998e-015
		 294 0 297 0 299 0 302 0 304 0 306 0 308 0 310 0 312 7.1054273579999998e-015 313 7.1054273579999998e-015
		 315 0 316 0 318 0 319 0 321 0 322 7.1054273579999998e-015 323 7.1054273579999998e-015
		 324 7.1054273579999998e-015 325 7.1054273579999998e-015 327 0 329 0 331 0 333 0 335 7.1054273579999998e-015
		 336 7.1054273579999998e-015 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:LwrLip_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:LwrLip_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:LwrLip_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 -0.14463631399999999 291 -0.14463631399999999
		 294 0 297 0 299 -0.3358369913 302 -0.3358369913 304 0 306 0 308 -0.3358369913 310 -0.3358369913
		 312 7.1054273579999998e-015 313 7.1054273579999998e-015 315 0 316 0 318 0 319 -0.3358369913
		 321 -0.3358369913 322 7.1054273579999998e-015 323 7.1054273579999998e-015 324 7.1054273579999998e-015
		 325 7.1054273579999998e-015 327 0 329 0 331 0 333 0 335 7.1054273579999998e-015 336 7.1054273579999998e-015
		 338 0 339 0 341 0 343 -0.3358369913 345 -0.25138161982441004 347 -0.3358369913 351 -0.14463631399999999;
createNode animCurveTU -n "ylva_original:rgtCheekInOut_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:rgtCheekInOut_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0.25 291 0.25 294 0 297 0 299 0 302 0
		 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0
		 325 0 327 0 329 0 331 0.25 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0
		 351 0.25;
createNode animCurveTU -n "ylva_original:lftCheekInOut_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:lftCheekInOut_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0.25 291 0.25 294 0 297 0 299 0 302 0
		 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0
		 325 0 327 0 329 0 331 0.25 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0
		 351 0.25;
createNode animCurveTU -n "ylva_original:TongueB_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:TongueB_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:TongueB_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 -0.6376713812499113 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0
		 323 0 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0
		 347 0 351 0;
createNode animCurveTU -n "ylva_original:TongueA_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1 327 1
		 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 33 ".kot[0:32]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:TongueA_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  289 0 291 0 294 0.50775143899999997 297 0.50775143899999997
		 299 0.031788062030000001 302 0.031788062030000001 304 -0.21123377860000001 306 -0.21123377860000001
		 308 0.031788062030000001 310 0.031788062030000001 312 0 313 0 315 0.50775143899999997
		 318 0 319 0.031788062030000001 321 0.031788062030000001 322 0 323 0 324 0.50775143899999997
		 325 0.50775143899999997 327 0 329 -0.21123377860000001 331 0 333 0.50775143899999997
		 335 0 336 0 338 0.13142201945865309 339 0.13142201945865309 341 -0.21123377860000001
		 343 0.031788062030000001 345 0 347 0.031788062030000001 351 0;
createNode animCurveTL -n "ylva_original:TongueA_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0.40613753720000001 297 0.40613753720000001
		 299 -0.3510012669 302 -0.3510012669 304 -0.56532674400000005 306 -0.56532674400000005
		 308 -0.3510012669 310 -0.17960858070786037 312 0 313 0 315 0.40613753720000001 316 0.0060556374197313634
		 318 0 319 -0.3510012669 321 -0.3510012669 322 0 323 0 324 0.40613753720000001 325 0.40613753720000001
		 327 0 329 -0.56532674400000005 331 0 333 0.40613753720000001 335 0 336 0 338 -0.029415440822790982
		 339 -0.029415440822790982 341 -0.56532674400000005 343 -0.3510012669 345 0 347 -0.3510012669
		 351 0;
createNode animCurveTU -n "ylva_original:teethClench_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:teethClench_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:teethUpSharp_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:teethUpSharp_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:teethDownSharp_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:teethDownSharp_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:mouthAa_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:mouthAa_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0.46363956989999999 297 0
		 299 0.25217419396463203 302 0.015771813260413256 304 0 306 0.16987417351015735 308 0.072010263808758607
		 310 0.40775046529701359 312 0 313 0 315 0.46363956989999999 316 0.59195486759742533
		 318 0 319 0.28446989549881019 321 0.070440623661445712 322 0 323 0 324 0.29269306354644536
		 325 0.46363956989999999 327 0 329 0.13112537980115885 331 0.087975020567995887 333 0.37569187998534281
		 335 0 336 0 338 0.15522084911994971 339 0.15522084911994971 341 0 343 0.24299363009917893
		 345 0 347 0.067061618961617442 351 0.21731794126874335;
createNode animCurveTU -n "ylva_original:mouthOo_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:mouthOo_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0.64702047279928332 339 0.64538114547433212
		 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:mouthUu_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:mouthUu_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0.70834807830000002
		 306 0.70834807830000002 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0
		 323 0 324 0 325 0 327 0 329 0.6254972129640104 331 0 333 0.132814474145587 335 0
		 336 0 338 0 339 0 341 0.70834807830000002 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:mouthMm_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:mouthMm_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0.25558794495178472 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0.34665089121045445
		 347 0 351 0;
createNode animCurveTU -n "ylva_original:mouthSurprised_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:mouthSurprised_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:scared_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:scared_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:scared_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:angry_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:angry_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:angry_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:bigMouth_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:bigMouth_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:bigMouth_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:nose_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 28 ".ktv[0:27]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 315 1 316 1 318 1 319 1 321 1 323 1 324 1 325 1 327 1 329 1
		 331 1 333 1 336 1 338 1 339 1 341 1 345 1;
	setAttr -s 28 ".kot[0:27]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5;
createNode animCurveTL -n "ylva_original:nose_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 28 ".ktv[0:27]"  289 1 291 1 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 315 0 316 0 318 0 319 0 321 0 323 0 324 0 325 0 327 0 329 0
		 331 0 333 0 336 0 338 0 339 0 341 0 345 0;
createNode animCurveTL -n "ylva_original:nose_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 28 ".ktv[0:27]"  289 -1.4210854720000001e-014 291 -1.4210854720000001e-014
		 294 0 297 0 299 0 302 0 304 0 306 0 308 0 310 0 312 0 315 0 316 0 318 0 319 0 321 0
		 323 0 324 0 325 0 327 0 329 0 331 0 333 0 336 0 338 0 339 0 341 0 345 0;
createNode animCurveTU -n "ylva_original:noseTip_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 315 1 316 1 318 1 319 1 321 1 323 1 324 1 325 1 327 1 329 1
		 331 1 333 1 336 1 338 1 339 1 341 1 345 1 351 1;
	setAttr -s 29 ".kot[0:28]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5;
createNode animCurveTL -n "ylva_original:noseTip_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 315 0 316 0 318 0 319 0 321 0 323 0 324 0 325 0 327 0 329 0
		 331 0 333 0 336 0 338 0 339 0 341 0 345 0 351 0;
createNode animCurveTL -n "ylva_original:noseTip_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 315 0 316 0 318 0 319 0 321 0 323 0 324 0 325 0 327 0 329 0
		 331 0 333 0 336 0 338 0 339 0 341 0 345 0 351 0;
createNode animCurveTU -n "ylva_original:nosetril_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 315 1 316 1 318 1 319 1 321 1 323 1 324 1 325 1 327 1 329 1
		 331 1 333 1 336 1 338 1 339 1 341 1 345 1 351 1;
	setAttr -s 29 ".kot[0:28]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5;
createNode animCurveTL -n "ylva_original:nosetril_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 315 0 316 0 318 0 319 0 321 0 323 0 324 0 325 0 327 0 329 0
		 331 0 333 0 336 0 338 0 339 0 341 0 345 0 351 0;
createNode animCurveTL -n "ylva_original:nosetril_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 315 0 316 0 318 0 319 0 321 0 323 0 324 0 325 0 327 0 329 0
		 331 0 333 0 336 0 338 0 339 0 341 0 345 0 351 0;
createNode animCurveTU -n "ylva_original:RgtbigEye_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtbigEye_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0.25;
createNode animCurveTU -n "ylva_original:LftbigEye_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftbigEye_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0.25;
createNode animCurveTU -n "ylva_original:RgteyeSquint_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgteyeSquint_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:LfteyeSquint_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LfteyeSquint_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:RgtUpEyeLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtUpEyeLid_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0.25;
createNode animCurveTU -n "ylva_original:RgtDownEyeLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtDownEyeLid_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:LftUpEyeLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftUpEyeLid_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0.25;
createNode animCurveTU -n "ylva_original:LftDownEyeLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftDownEyeLid_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0;
createNode animCurveTU -n "ylva_original:mouthWideNarrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:mouthWideNarrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:mouthWideNarrow_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0.50215116989999997 291 0.50215116989999997
		 294 0 297 0 299 0.16956752802895325 302 0.35255327011759219 304 0 306 0 308 0.25859250111548177
		 310 0.16951805838332423 312 7.1054273579999998e-015 313 7.1054273579999998e-015 315 0
		 316 0 318 0.20976409881513791 319 0.2097754104238288 321 0.16952415243977295 322 7.1054273579999998e-015
		 323 7.1054273579999998e-015 324 -0.12927572266006679 325 -0.29368609357522396 327 0
		 329 0 331 0 333 0 335 7.1054273579999998e-015 336 7.1054273579999998e-015 338 0 339 0
		 341 0 343 0.20807083546990121 345 0.30220253807816233 347 0 351 0.1631043145610454;
createNode animCurveTU -n "ylva_original:openHappy_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:openHappy_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:openHappy_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:openSad_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:openSad_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:openSad_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:facialCtrlVis_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:facialCtrlVis_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
createNode animCurveTU -n "ylva_original:rottenTeeth_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 1 291 1 294 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 345 1 347 1 351 1;
	setAttr -s 34 ".kot[0:33]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:rottenTeeth_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  289 0 291 0 294 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 345 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:faceGui_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:faceGui_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  298 5.4 312 5.1588050362281992;
createNode animCurveTL -n "ylva_original:faceGui_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  298 13.62705487 312 14.768576553250206;
createNode animCurveTL -n "ylva_original:faceGui_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  298 -1.065814104e-016 312 -0.14954046830393894;
createNode animCurveTA -n "ylva_original:faceGui_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  298 0 312 -0.8897079644215472;
createNode animCurveTA -n "ylva_original:faceGui_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  298 0 312 12.041812186054015;
createNode animCurveTA -n "ylva_original:faceGui_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  298 0 312 14.727357504263829;
createNode animCurveTU -n "ylva_original:faceGui_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0.3;
createNode animCurveTU -n "ylva_original:faceGui_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0.3;
createNode animCurveTU -n "ylva_original:faceGui_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  298 0.3;
createNode animCurveTA -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 8.881784197e-016 285 0 289 0 293 0 297 0
		 301 0 305 0 309 0;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 2.7755575619999998e-017 285 0 289 0
		 293 0 297 0 301 0 305 0 309 0;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0.84381747200000001 285 0.84381747200000001
		 289 0.84381747200000001 293 0.84381747200000001 297 0.84381747200000001 301 0.84381747200000001
		 305 0.84381747200000001 309 0.84381747200000001 313 0.84381747200000001 314 0.84381747200000001;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0.84381747200000001 285 0.84381747200000001
		 289 0.84381747200000001 293 0.84381747200000001 297 0.84381747200000001 301 0.84381747200000001
		 305 0.84381747200000001 309 0.84381747200000001 313 0.84381747200000001 314 0.84381747200000001;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0.84381747200000001 285 0.84381747200000001
		 289 0.84381747200000001 293 0.84381747200000001 297 0.84381747200000001 301 0.84381747200000001
		 305 0.84381747200000001 309 0.84381747200000001 313 0.84381747200000001 314 0.84381747200000001;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0.84381747200000001 285 0.84381747200000001
		 289 0.84381747200000001 293 0.84381747200000001 297 0.84381747200000001 301 0.84381747200000001
		 305 0.84381747200000001 309 0.84381747200000001 313 0.84381747200000001 314 0.84381747200000001;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0.84381747200000001 285 0.84381747200000001
		 289 0.84381747200000001 293 0.84381747200000001 297 0.84381747200000001 301 0.84381747200000001
		 305 0.84381747200000001 309 0.84381747200000001 313 0.84381747200000001 314 0.84381747200000001;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  282 0.33245434489999998 285 0.72585223060000004
		 289 0.3721959634 293 0 297 0 301 -0.23631996899999999 303 -0.58487564749999998 305 -0.34510126029999999
		 309 -0.020996829840000002;
	setAttr -s 9 ".kit[0:8]"  9 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kox[0:8]"  0.29176256060600281 1 0.40339931845664978 
		1 1 0.37962508201599121 1 0.39162608981132507 1;
	setAttr -s 9 ".koy[0:8]"  0.95649075508117676 0 -0.9150240421295166 
		0 0 -0.925140380859375 0 0.92012447118759155 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 1.8010942400000001 285 1.814653123 289 1.5607597
		 293 0.84381747200000001 297 0.84381747200000001 301 0.84381747200000001 305 0.84381747200000001
		 309 1.00721697;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kix[0:7]"  0.96448999643325806 1 0.31304648518562317 
		1 1 1 1 1;
	setAttr -s 8 ".kiy[0:7]"  0.26411926746368408 0 -0.94973772764205933 
		0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  0.96448999643325806 1 0.31304651498794556 
		1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0.26411926746368408 0 -0.94973784685134888 
		0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 2.0197492810000002 285 1.95990453 289 0.47571592979999999
		 293 0 297 0 301 0 305 0 309 0.93504827749999997;
	setAttr -s 8 ".kit[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kix[0:7]"  1 0.55569487810134888 0.16113986074924469 
		1 1 1 1 1;
	setAttr -s 8 ".kiy[0:7]"  0 -0.83138632774353027 -0.98693156242370605 
		0 0 0 0 0;
	setAttr -s 8 ".kox[0:7]"  1 0.55569487810134888 0.16113986074924469 
		1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 -0.83138632774353027 -0.98693156242370605 
		0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 -0.67318417399999997
		 297 -1.3840591310000001 301 -0.93307459989999997 305 0 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 0.22526147961616516 1 0.22526147961616516 
		1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 -0.97429835796356201 0 0.97429835796356201 
		0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0.84381747200000001 285 0.84381747200000001
		 289 0.84381747200000001 293 1.1288308570000001 297 1.3127635 301 1.929247921 305 0.84381747200000001
		 309 0.84381747200000001 313 0.84381747200000001 314 0.84381747200000001;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 0.56365394592285156 0.37122350931167603 
		1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0.826011061668396 0.92854350805282593 
		0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 1.276458877 297 2.262707442
		 301 1.6737054650000001 305 0 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 0.14002995193004608 1 0.14002995193004608 
		1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0.99014723300933838 0 -0.99014723300933838 
		0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0.84381747200000001 285 0.84381747200000001
		 289 0.84381747200000001 293 0.84381747200000001 297 0.84381747200000001 301 0.84381747200000001
		 305 0.84381747200000001 309 0.84381747200000001;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0;
	setAttr -s 8 ".kot[0:7]"  1 18 18 18 18 18 18 18;
	setAttr -s 8 ".kox[0:7]"  1 1 1 1 1 1 1 1;
	setAttr -s 8 ".koy[0:7]"  0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTL -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTL -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTU -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTL -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTL -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 0;
createNode animCurveTU -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -1.1368683772167429e-013;
createNode animCurveTL -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -8.5265128291255719e-014;
createNode animCurveTL -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -0.43513428515256708;
createNode animCurveTA -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 2.2737367544322118e-013;
createNode animCurveTL -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 2.842170943040266e-014;
createNode animCurveTL -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -0.46590324197811761;
createNode animCurveTA -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 1 338 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 0 338 0;
createNode animCurveTL -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 4.2632564145603954e-014 338 4.2632564145603954e-014;
createNode animCurveTL -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -0.69221533267156088 338 -0.69221533267156088;
createNode animCurveTA -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 0 338 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 0 338 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 0 338 0;
createNode animCurveTU -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 1 338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 1 338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 1 338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 1 338 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 0 338 0;
createNode animCurveTL -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 4.2632564145603954e-014 338 4.2632564145603954e-014;
createNode animCurveTL -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -0.69221533267156088 338 -0.69221533267156088;
createNode animCurveTA -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 0 338 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 0 338 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 0 338 0;
createNode animCurveTU -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 1 338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 1 338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 1 338 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1.1368683772156013e-013;
createNode animCurveTL -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1.8932661725304283e-029;
createNode animCurveTL -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -0.43726535785869014;
createNode animCurveTA -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -1.1368683772163012e-013;
createNode animCurveTL -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -5.6843418860815058e-014;
createNode animCurveTL -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -0.31570570893113015;
createNode animCurveTA -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -1.1368683772160528e-013;
createNode animCurveTL -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -1.4210854715200659e-014;
createNode animCurveTL -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -0.17881511222570351;
createNode animCurveTA -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTL -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTA -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
createNode animCurveTU -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -0.00020660770129999999;
	setAttr ".kot[0]"  1;
	setAttr ".kox[0]"  1;
	setAttr ".koy[0]"  0;
createNode animCurveTL -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 -0.041676805970000001;
	setAttr ".kot[0]"  1;
	setAttr ".kox[0]"  1;
	setAttr ".koy[0]"  0;
createNode animCurveTL -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0.31281998781038012;
	setAttr ".kot[0]"  1;
	setAttr ".kox[0]"  1;
	setAttr ".koy[0]"  0;
createNode animCurveTA -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
	setAttr ".kot[0]"  1;
	setAttr ".kox[0]"  1;
	setAttr ".koy[0]"  0;
createNode animCurveTA -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
	setAttr ".kot[0]"  1;
	setAttr ".kox[0]"  1;
	setAttr ".koy[0]"  0;
createNode animCurveTA -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 0;
	setAttr ".kot[0]"  1;
	setAttr ".kox[0]"  1;
	setAttr ".koy[0]"  0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
	setAttr ".kot[0]"  1;
	setAttr ".kox[0]"  1;
	setAttr ".koy[0]"  0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
	setAttr ".kot[0]"  1;
	setAttr ".kox[0]"  1;
	setAttr ".koy[0]"  0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
	setAttr ".kot[0]"  1;
	setAttr ".kox[0]"  1;
	setAttr ".koy[0]"  0;
createNode animCurveTL -n "ylva_original:mov_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 -108.95479357390597 298 -106.36406586327269
		 306 -106.35008672800502;
createNode animCurveTL -n "ylva_original:mov_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 107.57001756102362 298 107.17026440991708
		 306 106.83499959576503;
createNode animCurveTL -n "ylva_original:mov_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 1995.892584170736 298 1990.3957083465905
		 306 1990.3976898535718;
createNode animCurveTA -n "ylva_original:mov_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0.37349974356299492 298 0.37349974356299492
		 306 0.81065442189985715;
createNode animCurveTA -n "ylva_original:mov_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 154.9385663306507 298 154.9385663306507
		 306 114.66883758964285;
createNode animCurveTA -n "ylva_original:mov_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 2.5458229730219415 298 2.5458229730219415
		 306 3.1242893246130818;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 5;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[0:9]"  9 9 9 9 9 9 9 9 
		1 9;
	setAttr -s 10 ".kix[8:9]"  1 1;
	setAttr -s 10 ".kiy[8:9]"  0 0;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_globalScale";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_bodyRes";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_faceGuiCtrl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  282 1;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_ribbonCtrl_grp";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  282 0 333 1 358 0;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_hairCtrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_clothCtrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 314 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 314 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 314 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 315 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 315 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 315 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 315 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 315 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 315 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 314 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 314 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 314 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 314 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 314 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 0 285 0 289 0 293 0 297 0 300 0 305 0
		 309 0 313 0 314 0 338 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 1 285 1 289 1 293 1 297 1 300 1 305 1
		 309 1 313 1 314 1 338 1;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 1 285 1 289 1 293 1 297 1 300 1 305 1
		 309 1 313 1 314 1 338 1;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 1 285 1 289 1 293 1 297 1 300 1 305 1
		 309 1 313 1 314 1 338 1;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[0:10]"  1 18 18 18 18 18 18 18 
		1 1 10;
	setAttr -s 11 ".kix[8:10]"  1 0.039999961853027344 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
	setAttr -s 11 ".kox[0:10]"  1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1;
	setAttr -s 11 ".koy[0:10]"  0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 316 0 320 0 322 0 323 0 324 0
		 325 0 326 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 32 ".kit[0:31]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kot[0:31]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kix[15:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".kiy[15:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 32 ".kox[0:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".koy[0:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 316 -0.31317697919364662 317 -0.019961678507759248
		 320 -0.12837671106972567 322 0 323 0 324 -0.28629560146254579 325 0 326 -0.011259695375420457
		 331 0 333 0 335 0 336 0 338 -0.47056794556875475 341 -0.20694433006414117 343 0 345 0
		 349 0;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[15:32]"  1 0.99230712652206421 0.65455573797225952 
		0.99505603313446045 1 1 1 1 1 1 1 1 1 0.69494056701660156 0.39115461707115173 1 1 
		1;
	setAttr -s 33 ".kiy[15:32]"  0 -0.1238008439540863 0.75601375102996826 
		0.099315032362937927 0 0 0 0 0 0 0 0 0 -0.7190672755241394 0.92032492160797119 0 
		0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.99230712652206421 
		0.65455573797225952 0.99505603313446045 1 1 1 1 1 1 1 1 1 0.69494056701660156 0.39115461707115173 
		1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.1238008439540863 
		0.75601375102996826 0.099315032362937927 0 0 0 0 0 0 0 0 0 -0.7190672755241394 0.92032492160797119 
		0 0 0;
createNode animCurveTL -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 316 -0.66551082693191399 320 -0.39146891800125705
		 322 0 323 0 324 -0.515732120496605 325 -0.93609133046525206 326 -0.68249193002891873
		 331 0 333 0 335 0 336 0 338 -0.39440955580819781 341 -0.40796492422626046 343 -0.76784893818933975
		 345 0 349 -0.46882493882289594;
	setAttr -s 32 ".kit[0:31]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kot[0:31]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kix[15:31]"  1 0.58175957202911377 0.33923980593681335 
		1 1 0.085151270031929016 0.43253427743911743 0.24835240840911865 1 1 1 1 1 1 0.36511442065238953 
		0.62593561410903931 0.32298707962036133;
	setAttr -s 32 ".kiy[15:31]"  0 -0.81336081027984619 0.94069993495941162 
		0 0 -0.99636805057525635 -0.90161752700805664 0.96866977214813232 0 0 0 0 0 0 0.93096262216567993 
		0.77987474203109741 -0.9464033842086792;
	setAttr -s 32 ".kox[0:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.58175957202911377 
		0.33923980593681335 1 1 0.085151270031929016 0.43253427743911743 0.24835240840911865 
		1 1 1 1 1 1 0.36511442065238953 0.62593561410903931 0.32298707962036133;
	setAttr -s 32 ".koy[0:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.81336081027984619 
		0.94069993495941162 0 0 -0.99636805057525635 -0.90161752700805664 0.96866977214813232 
		0 0 0 0 0 0 0.93096262216567993 0.77987474203109741 -0.9464033842086792;
createNode animCurveTA -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 316 0 320 0 322 0 323 0 324 -7.7065419757617519
		 325 0 326 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 32 ".kit[0:31]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kot[0:31]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kix[15:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".kiy[15:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 32 ".kox[0:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".koy[0:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 316 0 320 0 322 0 323 0 324 0
		 325 0 326 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 32 ".kit[0:31]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kot[0:31]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kix[15:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".kiy[15:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 32 ".kox[0:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".koy[0:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 316 0 320 0 322 0 323 0 324 0
		 325 0 326 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 32 ".kit[0:31]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kot[0:31]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kix[15:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".kiy[15:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 32 ".kox[0:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".koy[0:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  282 1 285 1 289 1 293 1 295 1 297 1 298 1
		 299 1 300 1 303 1 305 1 307 1 309 1 311 1 312 1 313 1 316 1 320 1 322 1 323 1 324 1
		 325 1 326 1 331 1 333 1 335 1 336 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 32 ".kit[0:31]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kot[0:31]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kix[15:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".kiy[15:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 32 ".kox[0:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".koy[0:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  282 1 285 1 289 1 293 1 295 1 297 1 298 1
		 299 1 300 1 303 1 305 1 307 1 309 1 311 1 312 1 313 1 316 1 320 1 322 1 323 1 324 1
		 325 1 326 1 331 1 333 1 335 1 336 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 32 ".kit[0:31]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kot[0:31]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kix[15:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".kiy[15:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 32 ".kox[0:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".koy[0:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_ratio";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 316 0 320 0 322 0 323 0 324 0
		 325 0 326 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 32 ".kit[0:31]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kot[0:31]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kix[15:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".kiy[15:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 32 ".kox[0:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".koy[0:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_roll";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 316 0 320 0 322 0 323 0 324 0
		 325 0 326 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 32 ".kit[0:31]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kot[0:31]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kix[15:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".kiy[15:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 32 ".kox[0:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".koy[0:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_Sub_Ctrl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 316 0 320 0 322 0 323 0 324 0
		 325 0 326 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 32 ".kit[0:31]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kot[0:31]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kix[15:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".kiy[15:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 32 ".kox[0:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".koy[0:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_ExtraDeformers";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 316 0 320 0 322 0 323 0 324 0
		 325 0 326 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 32 ".kit[0:31]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kot[0:31]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10;
	setAttr -s 32 ".kix[15:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".kiy[15:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 32 ".kox[0:31]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 32 ".koy[0:31]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0.25135932909999997
		 297 0 298 0.25135932909999997 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0
		 315 0.25135932909999997 317 0.25135932909999997 320 0 322 0 323 0 324 0.25135932909999997
		 325 0.25135932909999997 326 0.25135932909999997 331 0 333 0 335 0 336 0 337 0 338 0
		 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 1 285 1 289 1 293 1 295 1 297 1 298 1
		 299 1 300 1 303 1 305 1 307 1 309 1 311 1 312 1 313 1 315 1 317 1 320 1 322 1 323 1
		 324 1 325 1 326 1 331 1 333 1 335 1 336 1 337 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 1 285 1 289 1 293 1 295 1 297 1 298 1
		 299 1 300 1 303 1 305 1 307 1 309 1 311 1 312 1 313 1 315 1 317 1 320 1 322 1 323 1
		 324 1 325 1 326 1 331 1 333 1 335 1 336 1 337 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0.24106017029999999
		 297 0 298 0.24106017029999999 299 0 300 -0.068791639979999999 303 -0.068791639979999999
		 305 0 307 0 309 -0.068791639979999999 311 -0.068791639979999999 312 0 313 0 315 0.24106017029999999
		 317 0.24106017029999999 320 -0.068791639979999999 322 -0.068791639979999999 323 0
		 324 0.24106017029999999 325 0.24106017029999999 326 0.24106017029999999 331 0 333 0
		 335 0 336 0 337 0 338 0 341 0 343 0 345 -0.068791639979999999 349 -0.068791639979999999;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 0.2499898374080658 
		1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0.96824848651885986 0 0 0 0 0 
		0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 0.2499898374080658 1 1 1 
		1 1 1 1 1 0.079999923706054688 1 1 1 0.2499898374080658 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 -0.96824848651885986 0 0 
		0 0 0 0 0 0 0 0 0 0 0.96824848651885986 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 2.647590645e-016 295 0
		 297 2.647590645e-016 298 0 299 2.647590645e-016 300 0 303 2.647590645e-016 305 2.647590645e-016
		 307 2.647590645e-016 309 2.647590645e-016 311 2.647590645e-016 312 0 313 0 315 0
		 317 0 320 0 322 0 323 0 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 2.647590645e-016
		 343 2.647590645e-016 345 2.647590645e-016 349 2.647590645e-016;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 1 285 1 289 1 293 1 295 1 297 1 298 1
		 299 1 300 1 303 1 305 1 307 1 309 1 311 1 312 1 313 1 315 1 317 1 320 1 322 1 323 1
		 324 1 325 1 326 1 331 1 333 1 335 1 336 1 337 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 1 285 1 289 1 293 1 295 1 297 1 298 1
		 299 1 300 1 303 1 305 1 307 1 309 1 311 1 312 1 313 1 315 1 317 1 320 1 322 1 323 1
		 324 1 325 1 326 1 331 1 333 1 335 1 336 1 337 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 300 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 320 0 322 0 323 0
		 324 0 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 1 285 1 289 1 293 1 295 1 297 1 298 1
		 299 1 300 1 303 1 305 1 307 1 309 1 311 1 312 1 313 1 314 1 316 1 320 1 322 1 323 1
		 324 1 325 1 326 1 331 1 333 1 335 1 336 1 337 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 34 ".ktv[0:33]"  282 1 285 1 289 1 293 1 295 1 297 1 298 1
		 299 1 300 1 303 1 305 1 307 1 309 1 311 1 312 1 313 1 314 1 316 1 320 1 322 1 323 1
		 324 1 325 1 326 1 331 1 333 1 335 1 336 1 337 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 34 ".kit[0:33]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kot[0:33]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10;
	setAttr -s 34 ".kix[15:33]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".kiy[15:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 34 ".kox[0:33]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 34 ".koy[0:33]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 7.3725747729999992e-018
		 295 0 297 7.3725747729999992e-018 298 0 299 7.3725747729999992e-018 301 0 303 0 305 7.3725747729999992e-018
		 307 7.3725747729999992e-018 309 0 311 0 312 0 313 0 314 0 316 0 321 0 323 0 324 0
		 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 7.3725747729999992e-018 343 7.3725747729999992e-018
		 345 0 349 0;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[15:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[15:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 -0.39720608930000001
		 295 -0.4755822307 297 -0.39720608930000001 298 -0.4755822307 299 -0.17994771800000001
		 301 0 303 0 305 -0.17994771800000001 307 -0.17994771800000001 309 0 311 0 312 0 313 0
		 314 -0.4755822307 316 -0.4755822307 321 0 323 0 324 -0.4755822307 325 -0.4755822307
		 326 -0.4755822307 331 -0.17994771800000001 333 0 335 0 336 0 337 0 338 0 341 -0.17994771800000001
		 343 -0.17994771800000001 345 0 349 0;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[15:32]"  1 0.039999961853027344 1 1 1 1 1 1 0.50735056400299072 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[15:32]"  0 0 0 0 0 0 0 0 0.86173975467681885 0 0 
		0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 0.4505273699760437 1 1 0.34554320573806763 
		0.2446541041135788 1 1 1 1 1 1 1 1 0.079999923706054688 1 1 1 1 1 1 0.50735056400299072 
		1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 -0.89276254177093506 0 0 0.93840283155441284 
		0.96961051225662231 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.86173975467681885 0 0 0 0 0 0 
		0 0 0;
createNode animCurveTL -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 -0.29541459520000002
		 295 -0.089735859119999997 297 -0.29541459520000002 298 -0.089735859119999997 299 0
		 301 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 -0.089735859119999997 316 -0.089735859119999997
		 321 0 323 0 324 -0.089735859119999997 325 -0.089735859119999997 326 -0.089735859119999997
		 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[15:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[15:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 0.26139053702354431 1 1 1 1 
		1 1 1 1 1 0.079999923706054688 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0.96523308753967285 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 0 295 -2.9248583020000001
		 297 0 298 -2.9248583020000001 299 0 301 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0
		 314 -2.9248583020000001 316 -2.9248583020000001 321 0 323 0 324 -2.9248583020000001
		 325 -2.9248583020000001 326 -2.9248583020000001 331 0 333 0 335 0 336 0 337 0 338 0
		 341 0 343 0 345 0 349 0;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[15:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[15:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 301 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 321 0 323 0 324 0
		 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[15:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[15:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 0 295 0 297 0 298 0
		 299 0 301 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 321 0 323 0 324 0
		 325 0 326 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 18 10 10 
		18 10 18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[15:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[15:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:tongueCurve_outPutAnimBank_1_visibility";
	setAttr ".tan" 5;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  282 1 285 1 289 1 293 1 297 1 300 1 305 1
		 309 1 313 1 315 1 338 1;
	setAttr -s 11 ".kit[0:10]"  9 9 9 9 9 9 9 9 
		1 9 9;
	setAttr -s 11 ".kix[8:10]"  1 1 1;
	setAttr -s 11 ".kiy[8:10]"  0 0 0;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 5;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 1 285 1 289 1 293 1 295 1 298 1 300 1
		 303 1 305 1 307 1 309 1 311 1 312 1 313 1 315 1 317 1 320 1 322 1 323 1 324 1 325 1
		 326 1 327 1 331 1 333 1 335 1 336 1 337 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 33 ".kit[0:32]"  9 9 9 9 9 9 9 9 
		9 9 9 9 9 1 9 9 9 9 9 9 9 9 9 9 9 
		9 9 9 9 9 9 9 9;
	setAttr -s 33 ".kix[13:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[13:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 0 295 0 298 0 300 0
		 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0 324 0 325 0
		 326 0 327 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[13:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[13:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 0 295 0.0069616983879999999
		 298 0.0069616983879999999 300 0 303 0 305 0.0025561906870000001 307 0.0025561906870000001
		 309 0 311 0 312 0 313 0 315 0.0069616983879999999 317 0.0069616983879999999 320 0
		 322 0 323 0 324 0.0069616983879999999 325 0.0069616983879999999 326 0.0069616983879999999
		 327 0.0069616983879999999 331 0.0025561906870000001 333 0 335 0 336 0 337 0 338 0
		 341 0.0025561906870000001 343 0.0025561906870000001 345 0 349 0;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[13:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[13:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 0.1205231231 295 -0.017917696909999999
		 298 -0.017917696909999999 300 -0.1015476532 303 -0.1015476532 305 0.040736272060000002
		 307 0.040736272060000002 309 -0.1015476532 311 -0.1015476532 312 -0.2465084438 313 -0.2465084438
		 315 -0.017917696909999999 317 -0.017917696909999999 320 -0.1015476532 322 -0.2465084438
		 323 -0.2465084438 324 -0.017917696909999999 325 -0.017917696909999999 326 -0.017917696909999999
		 327 -0.017917696909999999 331 0.040736272060000002 333 0 335 -0.2465084438 336 -0.2465084438
		 337 -0.2465084438 338 -0.2465084438 341 0.040736272060000002 343 0.040736272060000002
		 345 -0.1015476532 349 -0.1015476532;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[13:32]"  1 0.039999961853027344 1 0.65847271680831909 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[13:32]"  0 0 0 -0.75260460376739502 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 0.65847271680831909 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.75260460376739502 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 35 ".ktv[0:34]"  282 0 285 0 289 0 293 0 295 4.5083775519999998
		 298 4.5083775519999998 300 0 303 0 305 -3.590587814 307 -3.590587814 309 0 311 0
		 312 0 313 0 315 4.5083775519999998 317 4.5083775519999998 319 3.1368063744662349
		 320 0 322 0 323 0 324 4.5083775519999998 325 4.5083775519999998 326 4.5083775519999998
		 327 3.8013770816381611 329 4.0401260849634442 331 -1.1714808785686963 333 0 335 0
		 336 0 337 0 338 0 341 -3.590587814 343 -3.590587814 345 2.9547929649254407 349 0;
	setAttr -s 35 ".kit[0:34]"  18 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10 10;
	setAttr -s 35 ".kot[0:34]"  1 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10 10 10;
	setAttr -s 35 ".kix[13:34]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1 0.96755921840667725 0.95178157091140747;
	setAttr -s 35 ".kiy[13:34]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0.25264438986778259 -0.30677655339241028;
	setAttr -s 35 ".kox[0:34]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.96755921840667725 0.95178157091140747;
	setAttr -s 35 ".koy[0:34]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0.25264438986778259 -0.30677655339241028;
createNode animCurveTA -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 0 295 0 298 0 300 0
		 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0 324 0 325 0
		 326 0 327 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[13:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[13:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 0 285 0 289 0 293 0 295 0 298 0 300 0
		 303 0 305 0 307 0 309 0 311 0 312 0 313 0 315 0 317 0 320 0 322 0 323 0 324 0 325 0
		 326 0 327 0 331 0 333 0 335 0 336 0 337 0 338 0 341 0 343 0 345 0 349 0;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[13:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[13:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 1 285 1 289 1 293 1 295 1 298 1 300 1
		 303 1 305 1 307 1 309 1 311 1 312 1 313 1 315 1 317 1 320 1 322 1 323 1 324 1 325 1
		 326 1 327 1 331 1 333 1 335 1 336 1 337 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[13:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[13:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 1 285 1 289 1 293 1 295 1 298 1 300 1
		 303 1 305 1 307 1 309 1 311 1 312 1 313 1 315 1 317 1 320 1 322 1 323 1 324 1 325 1
		 326 1 327 1 331 1 333 1 335 1 336 1 337 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[13:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[13:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 33 ".ktv[0:32]"  282 1 285 1 289 1 293 1 295 1 298 1 300 1
		 303 1 305 1 307 1 309 1 311 1 312 1 313 1 315 1 317 1 320 1 322 1 323 1 324 1 325 1
		 326 1 327 1 331 1 333 1 335 1 336 1 337 1 338 1 341 1 343 1 345 1 349 1;
	setAttr -s 33 ".kit[0:32]"  18 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kot[0:32]"  1 18 18 18 10 10 18 10 
		18 10 18 10 10 1 1 10 10 10 10 10 10 10 10 10 10 
		10 10 10 10 10 10 10 10;
	setAttr -s 33 ".kix[13:32]"  1 0.039999961853027344 1 1 1 1 1 1 1 1 
		1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".kiy[13:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 33 ".kox[0:32]"  1 1 1 1 1 1 1 1 1 1 1 1 1 1 0.079999923706054688 
		1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr -s 33 ".koy[0:32]"  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_crossEyeFix";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_crossEyeRate";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0.5 285 0.5 289 0.5 293 0.5 297 0.5
		 301 0.5 305 0.5 309 0.5 313 0.5 314 0.5;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_Iris_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_Pupil_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_crossEyeFix";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_crossEyeRate";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0.5 285 0.5 289 0.5 293 0.5 297 0.5
		 301 0.5 305 0.5 309 0.5 313 0.5 314 0.5;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_Iris_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_Pupil_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  282 -0.17688379123203335 314 -0.31514522507245268;
	setAttr -s 2 ".kit[1]"  1;
	setAttr -s 2 ".kot[1]"  1;
	setAttr -s 2 ".kix[1]"  0.039999961853027344;
	setAttr -s 2 ".kiy[1]"  0;
	setAttr -s 2 ".kox[1]"  0.079999923706054688;
	setAttr -s 2 ".koy[1]"  0;
createNode animCurveTL -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  314 0.022554526977359712;
	setAttr ".kix[0]"  0.039999961853027344;
	setAttr ".kiy[0]"  0;
	setAttr ".kox[0]"  0.079999923706054688;
	setAttr ".koy[0]"  0;
createNode animCurveTL -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  314 0;
	setAttr ".kix[0]"  0.039999961853027344;
	setAttr ".kiy[0]"  0;
	setAttr ".kox[0]"  0.079999923706054688;
	setAttr ".koy[0]"  0;
createNode animCurveTA -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  314 0;
	setAttr ".kix[0]"  0.039999961853027344;
	setAttr ".kiy[0]"  0;
	setAttr ".kox[0]"  0.079999923706054688;
	setAttr ".koy[0]"  0;
createNode animCurveTU -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_l_eye_offset";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  314 0;
	setAttr ".kix[0]"  0.039999961853027344;
	setAttr ".kiy[0]"  0;
	setAttr ".kox[0]"  0.079999923706054688;
	setAttr ".koy[0]"  0;
createNode animCurveTU -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_r_eye_offset";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  314 0;
	setAttr ".kix[0]"  0.039999961853027344;
	setAttr ".kiy[0]"  0;
	setAttr ".kox[0]"  0.079999923706054688;
	setAttr ".koy[0]"  0;
createNode animCurveTL -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 -0.00020244999999999999 285 -0.00020244999999999999
		 289 -0.00020244999999999999 293 -0.00020244999999999999 297 -0.00020244999999999999
		 301 -0.00020244999999999999 305 -0.00020244999999999999 309 -0.00020244999999999999
		 313 -0.00020244999999999999 314 -0.00020244999999999999;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 16.290981800000001 285 16.290981800000001
		 289 16.290981800000001 293 16.290981800000001 297 16.290981800000001 301 16.290981800000001
		 305 16.290981800000001 309 16.290981800000001 313 16.290981800000001 314 16.290981800000001;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 -3.8045691326260567e-005 
		0;
createNode animCurveTL -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1.68490439 285 1.68490439 289 1.68490439
		 293 1.68490439 297 1.68490439 301 1.68490439 305 1.68490439 309 1.68490439 313 1.68490439
		 314 1.68490439;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 -3.7000000000000006 285 -3.7000000000000006
		 289 -3.7000000000000006 293 -3.7000000000000006 297 -3.7000000000000006 301 -3.7000000000000006
		 305 -3.7000000000000006 309 -3.7000000000000006 313 -3.7000000000000006 314 -3.7000000000000006;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_tx";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0.18 285 0.18 289 0.18 293 0.18 297 0.18
		 301 0.18 305 0.18 309 0.18 313 0.18 314 0.18;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_sc";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1.215 285 1.215 289 1.215 293 1.215
		 297 1.215 301 1.215 305 1.215 309 1.215 313 1.215 314 1.215;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_bothEye_offset";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 8 285 8 289 8 293 8 297 8 301 8 305 8
		 309 8 313 8 314 8;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_irisSize_temp";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 -2.5 285 -2.5 289 -2.5 293 -2.5 297 -2.5
		 301 -2.5 305 -2.5 309 -2.5 313 -2.5 314 -2.5;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_pupilSize_temp";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 -5 285 -5 289 -5 293 -5 297 -5 301 -5
		 305 -5 309 -5 313 -5 314 -5;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_mouth_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 -0.16011547379999999 297 -0.16011547379999999
		 299 0 302 0 304 0 306 0 308 0 310 0 312 0.041737993029999997 313 0.041737993029999997
		 315 -0.16011547379999999 316 -0.16011547379999999 318 0 319 0 321 0 322 0.041737993029999997
		 323 0.041737993029999997 324 -0.16011547379999999 325 -0.16011547379999999 327 0
		 329 0 331 -0.14456282279999999 333 -0.16011547379999999 335 0.041737993029999997
		 336 0.041737993029999997 338 -0.16011547379999999 341 1.232595164e-032 343 0 347 0
		 351 0;
createNode animCurveTL -n "ylva_original:l_mouth_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 -0.096487450279999998 297 -0.096487450279999998
		 299 0 302 0 304 0 306 0 308 0 310 0 312 0.086936221529999996 313 0.086936221529999996
		 315 -0.096487450279999998 316 -0.096487450279999998 318 0 319 0 321 0 322 0.086936221529999996
		 323 0.086936221529999996 324 -0.096487450279999998 325 -0.096487450279999998 327 0
		 329 0 331 -0.087365106129999995 333 -0.096487450279999998 335 0.086936221529999996
		 336 0.086936221529999996 338 -0.096487450279999998 341 0 343 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:l_mouth_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 -0.23253049510000001 313 -0.23253049510000001 315 0 316 0 318 0 319 0
		 321 0 322 -0.23253049510000001 323 -0.23253049510000001 324 0 325 0 327 0 329 -0.0026166254400529429
		 331 -0.199 333 0 335 -0.23253049510000001 336 -0.23253049510000001 338 0 341 0 343 0
		 347 0 351 0;
createNode animCurveTA -n "ylva_original:l_mouth_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 0.28316976919999998 313 0.28316976919999998 315 0 316 0 318 0 319 0
		 321 0 322 0.28316976919999998 323 0.28316976919999998 324 0 325 0 327 0 329 0 331 0
		 333 0 335 0.28316976919999998 336 0.28316976919999998 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:l_mouth_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 -4.9919953809999997 313 -4.9919953809999997 315 0 316 0 318 0 319 0
		 321 0 322 -4.9919953809999997 323 -4.9919953809999997 324 0 325 0 327 0 329 0 331 0
		 333 0 335 -4.9919953809999997 336 -4.9919953809999997 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:l_mouth_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 5.9222418049999996
		 302 5.9222418049999996 304 0 306 0 308 5.9222418049999996 310 5.9222418049999996
		 312 -3.250739238 313 -3.250739238 315 0 316 0 318 0 319 5.9222418049999996 321 5.9222418049999996
		 322 -3.250739238 323 -3.250739238 324 0 325 0 327 0 329 0 331 0 333 0 335 -3.250739238
		 336 -3.250739238 338 0 341 0 343 5.9222418049999996 347 5.9222418049999996 351 0;
createNode animCurveTL -n "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 -0.0023742676630000002 313 -0.0023742676630000002 315 0 316 0 318 0
		 319 0 321 0 322 -0.0023742676630000002 323 -0.0023742676630000002 324 0 325 0 327 0
		 329 0 331 0 333 0 335 -0.0023742676630000002 336 -0.0023742676630000002 338 0 341 0
		 343 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 -0.024937341790000001
		 306 -0.024937341790000001 308 0 310 0 312 0.2085774171 313 0.2085774171 315 0 316 0
		 318 0 319 0 321 0 322 0.2085774171 323 0.2085774171 324 0 325 0 327 0 329 -0.024937341790000001
		 331 0 333 0 335 0.2085774171 336 0.2085774171 338 0 341 -0.024937341790000001 343 0
		 347 0 351 0;
createNode animCurveTL -n "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0.052992384949999999
		 306 0.052992384949999999 308 0 310 0 312 -0.089968818340000006 313 -0.089968818340000006
		 315 0 316 0 318 0 319 0 321 0 322 -0.089968818340000006 323 -0.089968818340000006
		 324 0 325 0 327 0 329 0.052992384949999999 331 0 333 0 335 -0.089968818340000006
		 336 -0.089968818340000006 338 0 341 0.052992384949999999 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 -27.6301557
		 306 -27.6301557 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 -27.6301557 331 0 333 0 335 0 336 0 338 0 341 -27.6301557 343 0
		 347 0 351 0;
createNode animCurveTA -n "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0 327 0
		 329 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0 327 0
		 329 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0 327 0
		 329 -0.11648564495947628 331 0 333 0 335 0 336 0 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0.071916993750000005 297 0.071916993750000005
		 299 0 302 0 304 -0.010027178100000001 306 -0.010027178100000001 308 0 310 0 312 -0.025705504349999998
		 313 -0.025705504349999998 315 0.071916993750000005 316 0.071916993750000005 318 0
		 319 0 321 0 322 -0.025705504349999998 323 -0.025705504349999998 324 0.071916993750000005
		 325 0.071916993750000005 327 0 329 -0.010027178100000001 331 0 333 0.071916993750000005
		 335 -0.025705504349999998 336 -0.025705504349999998 338 0.071916993750000005 341 -0.010027178100000001
		 343 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0.029950868709999998
		 306 0.029950868709999998 308 0 310 0 312 0.043458591220000002 313 0.043458591220000002
		 315 0 316 0 318 0 319 0 321 0 322 0.043458591220000002 323 0.043458591220000002 324 0
		 325 0 327 0 329 0.029950868709999998 331 0 333 0 335 0.043458591220000002 336 0.043458591220000002
		 338 0 341 0.029950868709999998 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 18.509904769999999
		 306 18.509904769999999 308 0 310 0 312 32.066914480000001 313 32.066914480000001
		 315 0 316 0 318 0 319 0 321 0 322 32.066914480000001 323 32.066914480000001 324 0
		 325 0 327 0 329 18.509904769999999 331 0 333 0 335 32.066914480000001 336 32.066914480000001
		 338 0 341 18.509904769999999 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0 327 0
		 329 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0 327 0
		 329 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:r_mouth_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 -0.16011547379999999 297 -0.16011547379999999
		 299 0 302 0 304 0 306 0 308 0 310 0 312 0.083295461139999999 313 0.083295461139999999
		 315 -0.16011547379999999 316 -0.16011547379999999 318 0 319 0 321 0 322 0.083295461139999999
		 323 0.083295461139999999 324 -0.16011547379999999 325 -0.16011547379999999 327 0
		 329 0 331 -0.14456282279999999 333 -0.16011547379999999 335 0.083295461139999999
		 336 0.083295461139999999 338 -0.16011547379999999 341 1.232595164e-032 343 0 347 0
		 351 0;
createNode animCurveTL -n "ylva_original:r_mouth_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 -0.096487450279999998 297 -0.096487450279999998
		 299 0 302 0 304 0 306 0 308 0 310 0 312 0.086936221529999996 313 0.086936221529999996
		 315 -0.096487450279999998 316 -0.096487450279999998 318 0 319 0 321 0 322 0.086936221529999996
		 323 0.086936221529999996 324 -0.096487450279999998 325 -0.096487450279999998 327 0
		 329 0 331 -0.087365106129999995 333 -0.096487450279999998 335 0.086936221529999996
		 336 0.086936221529999996 338 -0.096487450279999998 341 0 343 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:r_mouth_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 0.2320325121 313 0.2320325121 315 0 316 0 318 0 319 0 321 0 322 0.2320325121
		 323 0.2320325121 324 0 325 0 327 0 329 0 331 0.1988513781 333 0 335 0.2320325121
		 336 0.2320325121 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:r_mouth_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 -0.28316976919999998 313 -0.28316976919999998 315 0 316 0 318 0 319 0
		 321 0 322 -0.28316976919999998 323 -0.28316976919999998 324 0 325 0 327 0 329 0 331 0
		 333 0 335 -0.28316976919999998 336 -0.28316976919999998 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:r_mouth_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 0 302 0 304 0 306 0
		 308 0 310 0 312 4.9919953809999997 313 4.9919953809999997 315 0 316 0 318 0 319 0
		 321 0 322 4.9919953809999997 323 4.9919953809999997 324 0 325 0 327 0 329 0 331 0
		 333 0 335 4.9919953809999997 336 4.9919953809999997 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:r_mouth_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  291 0 294 0 297 0 299 5.9222418049999996
		 302 5.9222418049999996 304 0 306 0 308 5.9222418049999996 310 5.9222418049999996
		 312 -3.250739238 313 -3.250739238 315 0 316 0 318 0 319 5.9222418049999996 321 5.9222418049999996
		 322 -3.250739238 323 -3.250739238 324 0 325 0 327 0 329 0 331 0 333 0 335 -3.250739238
		 336 -3.250739238 338 0 341 0 343 5.9222418049999996 347 5.9222418049999996 351 0;
createNode animCurveTU -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  291 1 293 1 295 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 341 1 343 1 347 1 351 1;
	setAttr -s 32 ".kot[0:31]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  291 0 293 0 295 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  291 0 293 0 295 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  291 0 293 0 295 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  291 0 293 1.9163006930000002 295 -3.3464752170000001
		 297 1.9163006930000002 299 -1.0629834170000001 302 0 304 -1.0629834170000001 306 -1.0629834170000001
		 308 0 310 0 312 0 313 0 315 -3.3464752170000001 316 -3.3464752170000001 318 0 319 0
		 321 0 322 0 323 0 324 -3.3464752170000001 325 -3.3464752170000001 327 0 329 -1.0629834170000001
		 331 -3.6815017889999995 333 -3.3464752170000001 335 0 336 0 338 -3.3464752170000001
		 341 -1.0629834170000001 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  291 0 293 0 295 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  291 0 293 0 295 0 297 0 299 0 302 0 304 0
		 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0 324 0 325 0
		 327 0 329 0 331 0 333 0 335 0 336 0 338 0 341 0 343 0 347 0 351 0;
createNode animCurveTU -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  291 1 293 1 295 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 341 1 343 1 347 1 351 1;
createNode animCurveTU -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  291 1 293 1 295 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 341 1 343 1 347 1 351 1;
createNode animCurveTU -n "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 32 ".ktv[0:31]"  291 1 293 1 295 1 297 1 299 1 302 1 304 1
		 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1 324 1 325 1
		 327 1 329 1 331 1 333 1 335 1 336 1 338 1 341 1 343 1 347 1 351 1;
createNode animCurveTL -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 -0.0044317438500000002 297 0 298 -0.0044317438500000002
		 299 0 301 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 -0.0044317438500000002
		 316 -0.0044317438500000002 321 0 323 0 324 -0.0044317438500000002 325 -0.0044317438500000002
		 326 -0.0044317438500000002 331 0 333 0 335 0 336 0 337 0 338 0 340 -0.0044317438500000002
		 341 0 343 0 345 0 349 0;
createNode animCurveTL -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 -0.2500608372 297 0 298 -0.2500608372
		 299 0 301 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 -0.2500608372 316 -0.2500608372
		 321 0 323 0 324 -0.2500608372 325 -0.2500608372 326 -0.2500608372 331 0 333 0 335 0
		 336 0 337 0 338 0 340 -0.2500608372 341 0 343 0 345 0 349 0;
createNode animCurveTL -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 -0.0098637586409999999 297 0 298 -0.0098637586409999999
		 299 0 301 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 -0.0098637586409999999
		 316 -0.0098637586409999999 321 0 323 0 324 -0.0098637586409999999 325 -0.0098637586409999999
		 326 -0.0098637586409999999 331 0 333 0 335 0 336 0 337 0 338 0 340 -0.0098637586409999999
		 341 0 343 0 345 0 349 0;
createNode animCurveTA -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 -14.70090046 297 0 298 -14.70090046
		 299 0 301 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 -14.70090046 316 -14.70090046
		 321 0 323 0 324 -14.70090046 325 -14.70090046 326 -14.70090046 331 0 333 0 335 0
		 336 0 337 0 338 0 340 -14.70090046 341 0 343 0 345 0 349 0;
createNode animCurveTA -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 -2.402422042 297 0 298 -2.402422042
		 299 0 301 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 -2.402422042 316 -2.402422042
		 321 0 323 0 324 -2.402422042 325 -2.402422042 326 -2.402422042 331 0 333 0 335 0
		 336 0 337 0 338 0 340 -2.402422042 341 0 343 0 345 0 349 0;
createNode animCurveTA -n "ylva_original:l_teethBtmA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 -9.2249763960000006 297 0 298 -9.2249763960000006
		 299 0 301 0 303 0 305 0 307 0 309 0 311 0 312 0 313 0 314 -9.2249763960000006 316 -9.2249763960000006
		 321 0 323 0 324 -9.2249763960000006 325 -9.2249763960000006 326 -9.2249763960000006
		 331 0 333 0 335 0 336 0 337 0 338 0 340 -9.2249763960000006 341 0 343 0 345 0 349 0;
createNode animCurveTL -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  293 0 295 0.0068809756469999997 296 0 297 0.0068809756469999997
		 298 0 300 0 302 0 304 0 306 0 308 0 310 0 312 0 313 0 314 0.0068809756469999997 319 0
		 321 0 322 0 323 0 324 0.0068809756469999997 325 0.0068809756469999997 329 0 331 0
		 333 0.0068809756469999997 335 0 336 0 338 0.0068809756469999997 341 0 343 0 347 0;
createNode animCurveTL -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  293 0 295 -0.2419497524 296 0 297 -0.2419497524
		 298 0 300 0 302 0 304 0 306 0 308 0 310 0 312 0 313 0 314 -0.2419497524 319 0 321 0
		 322 0 323 0 324 -0.2419497524 325 -0.2419497524 329 0 331 0 333 -0.2419497524 335 0
		 336 0 338 -0.2419497524 341 0 343 0 347 0;
createNode animCurveTL -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  293 0 295 0.028381991959999998 296 0 297 0.028381991959999998
		 298 0 300 0 302 0 304 0 306 0 308 0 310 0 312 0 313 0 314 0.028381991959999998 319 0
		 321 0 322 0 323 0 324 0.028381991959999998 325 0.028381991959999998 329 0 331 0 333 0.028381991959999998
		 335 0 336 0 338 0.028381991959999998 341 0 343 0 347 0;
createNode animCurveTA -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  293 0 295 6.8533877109999999 296 0 297 6.8533877109999999
		 298 0 300 0 302 0 304 0 306 0 308 0 310 0 312 0 313 0 314 6.8533877109999999 319 0
		 321 0 322 0 323 0 324 6.8533877109999999 325 6.8533877109999999 329 0 331 0 333 6.8533877109999999
		 335 0 336 0 338 6.8533877109999999 341 0 343 0 347 0;
createNode animCurveTA -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  293 0 295 -3.87576345 296 0 297 -3.87576345
		 298 0 300 0 302 0 304 0 306 0 308 0 310 0 312 0 313 0 314 -3.87576345 319 0 321 0
		 322 0 323 0 324 -3.87576345 325 -3.87576345 329 0 331 0 333 -3.87576345 335 0 336 0
		 338 -3.87576345 341 0 343 0 347 0;
createNode animCurveTA -n "ylva_original:r_teethBtmA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 29 ".ktv[0:28]"  293 0 295 -22.120116280000001 296 0 297 -22.120116280000001
		 298 0 300 0 302 0 304 0 306 0 308 0 310 0 312 0 313 0 314 -22.120116280000001 319 0
		 321 0 322 0 323 0 324 -22.120116280000001 325 -22.120116280000001 329 0 331 0 333 -22.120116280000001
		 335 0 336 0 338 -22.120116280000001 341 0 343 0 347 0;
createNode animCurveTL -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTL -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTL -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTA -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTA -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTA -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTU -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTU -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTU -n "ylva_original:m_teethBtmB_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTL -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTL -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0.1162631979 296 0 297 0.1162631979
		 298 0 300 0 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0.1162631979 316 0.1162631979
		 318 0 319 0 321 0 322 0 323 0 324 0.1162631979 325 0.1162631979 327 0 329 0.1383736240360349
		 331 0 333 0.1162631979 335 0 336 0 338 0.1162631979 339 0.1162631979 341 0 343 0
		 344 0 347 0 351 0;
createNode animCurveTL -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 -0.050170615199999997 295 -0.055024243090000001
		 296 -0.050170615199999997 297 -0.055024243090000001 298 0 300 0 302 0 304 0 306 0
		 308 0 310 0 312 0 313 0 315 -0.055024243090000001 316 -0.055024243090000001 318 0
		 319 0 321 0 322 0 323 0 324 -0.055024243090000001 325 -0.055024243090000001 327 0
		 329 0 331 0 333 -0.055024243090000001 335 0 336 0 338 -0.055024243090000001 339 -0.055024243090000001
		 341 0 343 0 344 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 5.2199547400000004 296 0
		 297 5.2199547400000004 298 0 300 0 302 0 304 0 306 -5.3295636257068271 308 0 310 0
		 312 0 313 0 315 5.2199547400000004 316 5.2199547400000004 318 0 319 0 321 0 322 0
		 323 0 324 5.2199547400000004 325 5.2199547400000004 327 0 329 0 331 0 333 5.2199547400000004
		 335 0 336 0 338 5.2199547400000004 339 5.2199547400000004 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTA -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTA -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTU -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTU -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTU -n "ylva_original:m_teethBtmA_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTU -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 1 295 1 297 1 298 1 299 1 301 1 303 1
		 305 1 307 1 309 1 311 1 312 1 313 1 314 1 316 1 321 1 323 1 324 1 325 1 326 1 331 1
		 333 1 335 1 336 1 337 1 338 1 340 1 341 1 343 1 345 1 349 1;
	setAttr -s 31 ".kot[0:30]"  5 5 5 5 5 5 5 5 
		5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
		5 5 5 5 5 5;
createNode animCurveTL -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 297 0 298 0 299 0 301 0 303 0
		 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 321 0 323 0 324 0 325 0 326 0 331 0
		 333 0 335 0 336 0 337 0 338 0 340 0 341 0 343 0 345 0 349 0;
createNode animCurveTL -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 297 0 298 0 299 0 301 0 303 0
		 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 321 0 323 0 324 0 325 0 326 0 331 0
		 333 0 335 0 336 0 337 0 338 0 340 0 341 0 343 0 345 0 349 0;
createNode animCurveTL -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 297 0 298 0 299 0 301 0 303 0
		 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 321 0 323 0 324 0 325 0 326 0 331 0
		 333 0 335 0 336 0 337 0 338 0 340 0 341 0 343 0 345 0 349 0;
createNode animCurveTA -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 297 0 298 0 299 0 301 0 303 0
		 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 321 0 323 0 324 0 325 0 326 0 331 0
		 333 0 335 0 336 0 337 0 338 0 340 0 341 0 343 0 345 0 349 0;
createNode animCurveTA -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 297 0 298 0 299 0 301 0 303 0
		 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 321 0 323 0 324 0 325 0 326 0 331 0
		 333 0 335 0 336 0 337 0 338 0 340 0 341 0 343 0 345 0 349 0;
createNode animCurveTA -n "ylva_original:l_teethTopA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 297 0 298 0 299 0 301 0 303 0
		 305 0 307 0 309 0 311 0 312 0 313 0 314 0 316 0 321 0 323 0 324 0 325 0 326 0 331 0
		 333 0 335 0 336 0 337 0 338 0 340 0 341 0 343 0 345 0 349 0;
createNode animCurveTL -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 296 0 297 0 298 0 300 0 302 0
		 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 319 0 321 0 322 0 323 0 324 0 325 0
		 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 347 0;
createNode animCurveTL -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 296 0 297 0 298 0 300 0 302 0
		 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 319 0 321 0 322 0 323 0 324 0 325 0
		 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 347 0;
createNode animCurveTL -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 296 0 297 0 298 0 300 0 302 0
		 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 319 0 321 0 322 0 323 0 324 0 325 0
		 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 347 0;
createNode animCurveTA -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 296 0 297 0 298 0 300 0 302 0
		 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 319 0 321 0 322 0 323 0 324 0 325 0
		 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 347 0;
createNode animCurveTA -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 296 0 297 0 298 0 300 0 302 0
		 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 319 0 321 0 322 0 323 0 324 0 325 0
		 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 347 0;
createNode animCurveTA -n "ylva_original:r_teethTopA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 31 ".ktv[0:30]"  293 0 295 0 296 0 297 0 298 0 300 0 302 0
		 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 319 0 321 0 322 0 323 0 324 0 325 0
		 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 347 0;
createNode animCurveTL -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTL -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTL -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTA -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTA -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTA -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTU -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTU -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTU -n "ylva_original:m_teethTopB_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTL -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTL -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 -0.07983343792 295 -0.039669278529999998
		 296 -0.07983343792 297 -0.039669278529999998 298 0 300 -0.0087741055960000001 302 -0.0087741055960000001
		 304 0 306 0 308 -0.0087741055960000001 310 -0.0087741055960000001 312 0 313 0 315 -0.039669278529999998
		 316 -0.039669278529999998 318 0 319 -0.0087741055960000001 321 -0.0087741055960000001
		 322 0 323 0 324 -0.039669278529999998 325 -0.039669278529999998 327 0 329 0 331 0
		 333 -0.039669278529999998 335 0 336 0 338 -0.039669278529999998 339 -0.039669278529999998
		 341 0 343 -0.0087741055960000001 344 0 347 -0.0087741055960000001 351 0;
createNode animCurveTL -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTA -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 -14.935976615474166 339 -14.935976615474166
		 341 0 343 0 344 0 347 0 351 0;
createNode animCurveTA -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTA -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 0 293 0 295 0 296 0 297 0 298 0 300 0
		 302 0 304 0 306 0 308 0 310 0 312 0 313 0 315 0 316 0 318 0 319 0 321 0 322 0 323 0
		 324 0 325 0 327 0 329 0 331 0 333 0 335 0 336 0 338 0 339 0 341 0 343 0 344 0 347 0
		 351 0;
createNode animCurveTU -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTU -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTU -n "ylva_original:m_teethTopA_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 36 ".ktv[0:35]"  291 1 293 1 295 1 296 1 297 1 298 1 300 1
		 302 1 304 1 306 1 308 1 310 1 312 1 313 1 315 1 316 1 318 1 319 1 321 1 322 1 323 1
		 324 1 325 1 327 1 329 1 331 1 333 1 335 1 336 1 338 1 339 1 341 1 343 1 344 1 347 1
		 351 1;
createNode animCurveTU -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 5;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 1 285 1 289 1 293 1 297 1 301 1 305 1
		 309 1 313 1 314 1;
	setAttr -s 10 ".kit[0:9]"  9 9 9 9 9 9 9 9 
		1 9;
	setAttr -s 10 ".kix[8:9]"  1 1;
	setAttr -s 10 ".kiy[8:9]"  0 0;
createNode animCurveTL -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  282 0 285 0 289 0 293 0 297 0 301 0 305 0
		 309 0 313 0 314 0;
	setAttr -s 10 ".kit[8:9]"  1 1;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		1 1;
	setAttr -s 10 ".kix[8:9]"  1 0.039999961853027344;
	setAttr -s 10 ".kiy[8:9]"  0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 0.079999923706054688;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
select -ne :time1;
	setAttr ".o" 282;
	setAttr ".unw" 282;
select -ne :renderPartition;
	setAttr -s 49 ".st";
select -ne :initialShadingGroup;
	setAttr -s 6596 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 9 ".gn";
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -s 49 ".s";
select -ne :defaultTextureList1;
	setAttr -s 87 ".tx";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 335 ".u";
select -ne :defaultRenderingList1;
	setAttr -s 4 ".r";
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
	setAttr -s 16 ".st";
select -ne :ikSystem;
	setAttr -s 8 ".sol";
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
connectAttr "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotatePivotY.o" "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1.rpy"
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
connectAttr "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_elbow_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_elbow_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1.rz"
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
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_uprarmStretch.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.uprarmStretch"
		;
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_forearmStretch.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.forearmStretch"
		;
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_autoStretch.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.autoStretch"
		;
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_elbowTwist.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.elbowTwist"
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
connectAttr "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1.rz"
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
connectAttr "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_thumb_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_index_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_index_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_index_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_index_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_middle_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_middle_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_middle_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_middle_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_ring_04_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_ring_03_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_ring_02_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:l_armA_ring_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_keepOrientation.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.keepOrientation"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_FK_2_IK.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.FK_2_IK"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_globalIK_2_localIK.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.globalIK_2_localIK"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_neutral.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.neutral"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_fist.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.fist"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_relax.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.relax"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_curl.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.curl"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_spread.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.spread"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_splay.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.splay"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_break.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.break"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_flex.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.flex"
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
connectAttr "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_index_01_ctrl_outPutAnimBank_1.sz"
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
connectAttr "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_middle_01_ctrl_outPutAnimBank_1.sz"
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
connectAttr "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:r_armA_ring_01_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_keepOrientation.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.keepOrientation"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_FK_2_IK.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.FK_2_IK"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_globalIK_2_localIK.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.globalIK_2_localIK"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_neutral.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.neutral"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_fist.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.fist"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_relax.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.relax"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_curl.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.curl"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_spread.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.spread"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_splay.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.splay"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_break.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.break"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_flex.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.flex"
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
connectAttr "ylva_original:RgtOuterBrow_outPutAnimBank_1_visibility.o" "ylva_original:RgtOuterBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:RgtOuterBrow_outPutAnimBank_1_translateY.o" "ylva_original:RgtOuterBrow_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:RgtOuterBrow_outPutAnimBank_1_translateZ.o" "ylva_original:RgtOuterBrow_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:RgtOuterBrow_outPutAnimBank_1_rotateZ.o" "ylva_original:RgtOuterBrow_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:RgtMidBrow_outPutAnimBank_1_visibility.o" "ylva_original:RgtMidBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:RgtMidBrow_outPutAnimBank_1_translateX.o" "ylva_original:RgtMidBrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:RgtMidBrow_outPutAnimBank_1_translateY.o" "ylva_original:RgtMidBrow_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:RgtMidBrow_outPutAnimBank_1_rotateZ.o" "ylva_original:RgtMidBrow_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:LftMidBrow_outPutAnimBank_1_visibility.o" "ylva_original:LftMidBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:LftMidBrow_outPutAnimBank_1_translateX.o" "ylva_original:LftMidBrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:LftMidBrow_outPutAnimBank_1_translateY.o" "ylva_original:LftMidBrow_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:LftMidBrow_outPutAnimBank_1_rotateZ.o" "ylva_original:LftMidBrow_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:LftOuterBrow_outPutAnimBank_1_visibility.o" "ylva_original:LftOuterBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:LftOuterBrow_outPutAnimBank_1_translateY.o" "ylva_original:LftOuterBrow_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:LftOuterBrow_outPutAnimBank_1_rotateZ.o" "ylva_original:LftOuterBrow_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:rgtHappyBrow_outPutAnimBank_1_visibility.o" "ylva_original:rgtHappyBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:rgtHappyBrow_outPutAnimBank_1_translateX.o" "ylva_original:rgtHappyBrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:rgtMadBrow_outPutAnimBank_1_visibility.o" "ylva_original:rgtMadBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:rgtMadBrow_outPutAnimBank_1_translateX.o" "ylva_original:rgtMadBrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:rgtSadBrow_outPutAnimBank_1_visibility.o" "ylva_original:rgtSadBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:rgtSadBrow_outPutAnimBank_1_translateX.o" "ylva_original:rgtSadBrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:rgtBoredBrow_outPutAnimBank_1_visibility.o" "ylva_original:rgtBoredBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:rgtBoredBrow_outPutAnimBank_1_translateX.o" "ylva_original:rgtBoredBrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:lftHappyBrow_outPutAnimBank_1_visibility.o" "ylva_original:lftHappyBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:lftHappyBrow_outPutAnimBank_1_translateX.o" "ylva_original:lftHappyBrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:lftMadBrow_outPutAnimBank_1_visibility.o" "ylva_original:lftMadBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:lftMadBrow_outPutAnimBank_1_translateX.o" "ylva_original:lftMadBrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:lftSadBrow_outPutAnimBank_1_visibility.o" "ylva_original:lftSadBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:lftSadBrow_outPutAnimBank_1_translateX.o" "ylva_original:lftSadBrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:lftBoredBrow_outPutAnimBank_1_visibility.o" "ylva_original:lftBoredBrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:lftBoredBrow_outPutAnimBank_1_translateX.o" "ylva_original:lftBoredBrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:RgtTopLid_outPutAnimBank_1_visibility.o" "ylva_original:RgtTopLid_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:RgtTopLid_outPutAnimBank_1_translateY.o" "ylva_original:RgtTopLid_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:LftTopLid_outPutAnimBank_1_visibility.o" "ylva_original:LftTopLid_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:LftTopLid_outPutAnimBank_1_translateY.o" "ylva_original:LftTopLid_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:RgtBtmLid_outPutAnimBank_1_visibility.o" "ylva_original:RgtBtmLid_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:RgtBtmLid_outPutAnimBank_1_translateY.o" "ylva_original:RgtBtmLid_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:LftBtmLid_outPutAnimBank_1_visibility.o" "ylva_original:LftBtmLid_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:LftBtmLid_outPutAnimBank_1_translateY.o" "ylva_original:LftBtmLid_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:eyeDarts_outPutAnimBank_1_visibility.o" "ylva_original:eyeDarts_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:eyeDarts_outPutAnimBank_1_translateX.o" "ylva_original:eyeDarts_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:eyeDarts_outPutAnimBank_1_translateY.o" "ylva_original:eyeDarts_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:JawRock_outPutAnimBank_1_visibility.o" "ylva_original:JawRock_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:JawRock_outPutAnimBank_1_translateX.o" "ylva_original:JawRock_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:JawRock_outPutAnimBank_1_translateY.o" "ylva_original:JawRock_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:JawRock_outPutAnimBank_1_mouthHold.o" "ylva_original:JawRock_outPutAnimBank_1.mouthHold"
		;
connectAttr "ylva_original:MouthEmotion_outPutAnimBank_1_visibility.o" "ylva_original:MouthEmotion_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:MouthEmotion_outPutAnimBank_1_translateX.o" "ylva_original:MouthEmotion_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:MouthEmotion_outPutAnimBank_1_translateY.o" "ylva_original:MouthEmotion_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:MouthSlide_outPutAnimBank_1_visibility.o" "ylva_original:MouthSlide_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:MouthSlide_outPutAnimBank_1_translateX.o" "ylva_original:MouthSlide_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:MouthSlide_outPutAnimBank_1_translateY.o" "ylva_original:MouthSlide_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:UprLip_outPutAnimBank_1_visibility.o" "ylva_original:UprLip_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:UprLip_outPutAnimBank_1_translateX.o" "ylva_original:UprLip_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:UprLip_outPutAnimBank_1_translateY.o" "ylva_original:UprLip_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:LwrLip_outPutAnimBank_1_visibility.o" "ylva_original:LwrLip_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:LwrLip_outPutAnimBank_1_translateX.o" "ylva_original:LwrLip_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:LwrLip_outPutAnimBank_1_translateY.o" "ylva_original:LwrLip_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:rgtCheekInOut_outPutAnimBank_1_visibility.o" "ylva_original:rgtCheekInOut_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:rgtCheekInOut_outPutAnimBank_1_translateY.o" "ylva_original:rgtCheekInOut_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:lftCheekInOut_outPutAnimBank_1_visibility.o" "ylva_original:lftCheekInOut_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:lftCheekInOut_outPutAnimBank_1_translateY.o" "ylva_original:lftCheekInOut_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:TongueB_outPutAnimBank_1_visibility.o" "ylva_original:TongueB_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:TongueB_outPutAnimBank_1_translateX.o" "ylva_original:TongueB_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:TongueB_outPutAnimBank_1_translateY.o" "ylva_original:TongueB_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:TongueA_outPutAnimBank_1_visibility.o" "ylva_original:TongueA_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:TongueA_outPutAnimBank_1_translateX.o" "ylva_original:TongueA_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:TongueA_outPutAnimBank_1_translateY.o" "ylva_original:TongueA_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:teethClench_outPutAnimBank_1_visibility.o" "ylva_original:teethClench_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:teethClench_outPutAnimBank_1_translateX.o" "ylva_original:teethClench_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:teethUpSharp_outPutAnimBank_1_visibility.o" "ylva_original:teethUpSharp_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:teethUpSharp_outPutAnimBank_1_translateX.o" "ylva_original:teethUpSharp_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:teethDownSharp_outPutAnimBank_1_visibility.o" "ylva_original:teethDownSharp_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:teethDownSharp_outPutAnimBank_1_translateX.o" "ylva_original:teethDownSharp_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:mouthAa_outPutAnimBank_1_visibility.o" "ylva_original:mouthAa_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:mouthAa_outPutAnimBank_1_translateX.o" "ylva_original:mouthAa_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:mouthOo_outPutAnimBank_1_visibility.o" "ylva_original:mouthOo_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:mouthOo_outPutAnimBank_1_translateX.o" "ylva_original:mouthOo_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:mouthUu_outPutAnimBank_1_visibility.o" "ylva_original:mouthUu_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:mouthUu_outPutAnimBank_1_translateX.o" "ylva_original:mouthUu_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:mouthMm_outPutAnimBank_1_visibility.o" "ylva_original:mouthMm_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:mouthMm_outPutAnimBank_1_translateX.o" "ylva_original:mouthMm_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:mouthSurprised_outPutAnimBank_1_visibility.o" "ylva_original:mouthSurprised_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:mouthSurprised_outPutAnimBank_1_translateX.o" "ylva_original:mouthSurprised_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:scared_outPutAnimBank_1_visibility.o" "ylva_original:scared_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:scared_outPutAnimBank_1_translateX.o" "ylva_original:scared_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:scared_outPutAnimBank_1_translateY.o" "ylva_original:scared_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:angry_outPutAnimBank_1_visibility.o" "ylva_original:angry_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:angry_outPutAnimBank_1_translateX.o" "ylva_original:angry_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:angry_outPutAnimBank_1_translateY.o" "ylva_original:angry_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:bigMouth_outPutAnimBank_1_visibility.o" "ylva_original:bigMouth_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:bigMouth_outPutAnimBank_1_translateX.o" "ylva_original:bigMouth_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:bigMouth_outPutAnimBank_1_translateY.o" "ylva_original:bigMouth_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:nose_outPutAnimBank_1_visibility.o" "ylva_original:nose_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:nose_outPutAnimBank_1_translateX.o" "ylva_original:nose_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:nose_outPutAnimBank_1_translateY.o" "ylva_original:nose_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:noseTip_outPutAnimBank_1_visibility.o" "ylva_original:noseTip_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:noseTip_outPutAnimBank_1_translateX.o" "ylva_original:noseTip_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:noseTip_outPutAnimBank_1_translateY.o" "ylva_original:noseTip_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:nosetril_outPutAnimBank_1_visibility.o" "ylva_original:nosetril_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:nosetril_outPutAnimBank_1_translateX.o" "ylva_original:nosetril_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:nosetril_outPutAnimBank_1_translateY.o" "ylva_original:nosetril_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:RgtbigEye_outPutAnimBank_1_visibility.o" "ylva_original:RgtbigEye_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:RgtbigEye_outPutAnimBank_1_translateY.o" "ylva_original:RgtbigEye_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:LftbigEye_outPutAnimBank_1_visibility.o" "ylva_original:LftbigEye_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:LftbigEye_outPutAnimBank_1_translateY.o" "ylva_original:LftbigEye_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:RgteyeSquint_outPutAnimBank_1_visibility.o" "ylva_original:RgteyeSquint_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:RgteyeSquint_outPutAnimBank_1_translateY.o" "ylva_original:RgteyeSquint_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:LfteyeSquint_outPutAnimBank_1_visibility.o" "ylva_original:LfteyeSquint_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:LfteyeSquint_outPutAnimBank_1_translateY.o" "ylva_original:LfteyeSquint_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:RgtUpEyeLid_outPutAnimBank_1_visibility.o" "ylva_original:RgtUpEyeLid_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:RgtUpEyeLid_outPutAnimBank_1_translateX.o" "ylva_original:RgtUpEyeLid_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:RgtDownEyeLid_outPutAnimBank_1_visibility.o" "ylva_original:RgtDownEyeLid_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:RgtDownEyeLid_outPutAnimBank_1_translateX.o" "ylva_original:RgtDownEyeLid_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:LftUpEyeLid_outPutAnimBank_1_visibility.o" "ylva_original:LftUpEyeLid_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:LftUpEyeLid_outPutAnimBank_1_translateX.o" "ylva_original:LftUpEyeLid_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:LftDownEyeLid_outPutAnimBank_1_visibility.o" "ylva_original:LftDownEyeLid_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:LftDownEyeLid_outPutAnimBank_1_translateX.o" "ylva_original:LftDownEyeLid_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:mouthWideNarrow_outPutAnimBank_1_visibility.o" "ylva_original:mouthWideNarrow_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:mouthWideNarrow_outPutAnimBank_1_translateX.o" "ylva_original:mouthWideNarrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:mouthWideNarrow_outPutAnimBank_1_translateY.o" "ylva_original:mouthWideNarrow_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:openHappy_outPutAnimBank_1_visibility.o" "ylva_original:openHappy_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:openHappy_outPutAnimBank_1_translateX.o" "ylva_original:openHappy_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:openHappy_outPutAnimBank_1_translateY.o" "ylva_original:openHappy_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:openSad_outPutAnimBank_1_visibility.o" "ylva_original:openSad_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:openSad_outPutAnimBank_1_translateX.o" "ylva_original:openSad_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:openSad_outPutAnimBank_1_translateY.o" "ylva_original:openSad_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:facialCtrlVis_outPutAnimBank_1_visibility.o" "ylva_original:facialCtrlVis_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:facialCtrlVis_outPutAnimBank_1_translateY.o" "ylva_original:facialCtrlVis_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:rottenTeeth_outPutAnimBank_1_visibility.o" "ylva_original:rottenTeeth_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:rottenTeeth_outPutAnimBank_1_translateX.o" "ylva_original:rottenTeeth_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:faceGui_outPutAnimBank_1_visibility.o" "ylva_original:faceGui_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:faceGui_outPutAnimBank_1_translateX.o" "ylva_original:faceGui_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:faceGui_outPutAnimBank_1_translateY.o" "ylva_original:faceGui_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:faceGui_outPutAnimBank_1_translateZ.o" "ylva_original:faceGui_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:faceGui_outPutAnimBank_1_rotateX.o" "ylva_original:faceGui_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:faceGui_outPutAnimBank_1_rotateY.o" "ylva_original:faceGui_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:faceGui_outPutAnimBank_1_rotateZ.o" "ylva_original:faceGui_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:faceGui_outPutAnimBank_1_scaleX.o" "ylva_original:faceGui_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:faceGui_outPutAnimBank_1_scaleY.o" "ylva_original:faceGui_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:faceGui_outPutAnimBank_1_scaleZ.o" "ylva_original:faceGui_outPutAnimBank_1.sz"
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
connectAttr "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:hair_curve_jt_7_fk_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:hair_curve_jt_6_fk_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:hair_curve_jt_4_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:hair_curve_jt_5_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:hair_curve_jt_6_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:hair_curve_jt_7_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:hair_curve_jt_8_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:hair_curve_jt_9_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:hair_curve_jt_10_ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:hair_curve_jt_11_ctrl_outPutAnimBank_1.sz"
		;
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
connectAttr "ylva_original:mov_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:mov_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:mov_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:mov_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:mov_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:mov_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:mov_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:mov_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:mov_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:mov_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:mov_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:mov_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:top_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_globalScale.o" "ylva_original:top_ctrl_outPutAnimBank_1.globalScale"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_bodyRes.o" "ylva_original:top_ctrl_outPutAnimBank_1.bodyRes"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_faceGuiCtrl.o" "ylva_original:top_ctrl_outPutAnimBank_1.faceGuiCtrl"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_ribbonCtrl_grp.o" "ylva_original:top_ctrl_outPutAnimBank_1.ribbonCtrl_grp"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_hairCtrl.o" "ylva_original:top_ctrl_outPutAnimBank_1.hairCtrl"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_clothCtrl.o" "ylva_original:top_ctrl_outPutAnimBank_1.clothCtrl"
		;
connectAttr "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_translateX.o" "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_translateY.o" "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1.sz"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_ratio.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.ratio"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_roll.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.roll"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_Sub_Ctrl.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.Sub_Ctrl"
		;
connectAttr "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_ExtraDeformers.o" "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1.ExtraDeformers"
		;
connectAttr "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1.sy"
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
connectAttr "ylva_original:tongueCurve_outPutAnimBank_1_visibility.o" "ylva_original:tongueCurve_outPutAnimBank_1.v"
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
connectAttr "ylva_original:l_mouth_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:l_mouth_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:l_mouth_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:l_mouth_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:l_mouth_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:l_mouth_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:l_mouth_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_mouth_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_mouth_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_mouth_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_mouth_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_mouth_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_mouthTop_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_mouthBtm_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:r_mouth_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:r_mouth_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:r_mouth_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:r_mouth_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:r_mouth_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:r_mouth_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:r_mouth_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_mouth_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_mouth_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_mouth_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_mouth_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_mouth_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_scaleX.o" "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1.sx"
		;
connectAttr "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_scaleY.o" "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1.sy"
		;
connectAttr "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1_scaleZ.o" "ylva_original:m_mouth_root_ctrl_outPutAnimBank_1.sz"
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
connectAttr "ylva_original:head_squash_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:head_squash_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateX.o" "ylva_original:head_squash_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateY.o" "ylva_original:head_squash_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateZ.o" "ylva_original:head_squash_ctrl_outPutAnimBank_1.tz"
		;
// End of 213.ma

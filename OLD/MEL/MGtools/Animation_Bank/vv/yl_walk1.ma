//Maya ASCII 2012 scene
//Name: yl_walk1.ma
//Last modified: Fri, Aug 31, 2012 03:56:04 PM
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
	setAttr ".range" -type "string" "\"1:33\"";
	setAttr ".num" 102;
	setAttr ".nts" -type "string" (
		"ylva_original:m_spineA_waistFree_ctrl; ylva_original:m_spineA_chest_ctrl; ylva_original:m_spineA_waist_ctrl; ylva_original:m_spineA_hip_ctrl; ylva_original:m_spineA_torso_ctrl; ylva_original:m_spineA_body_ctrl; ylva_original:l_legA_heel_IK_ctrl; ylva_original:l_legA_knee_IK_ctrl; ylva_original:l_legA_foot_IK_ctrl; ylva_original:r_legA_heel_IK_ctrl; ylva_original:r_legA_knee_IK_ctrl; ylva_original:r_legA_foot_IK_ctrl; ylva_original:l_legA_pelvis_ctrl; ylva_original:r_legA_pelvis_ctrl; ylva_original:l_armA_hand_IK_ctrl; ylva_original:r_armA_hand_IK_ctrl; ylva_original:l_armA_shoulder_ctrl; ylva_original:r_armA_shoulder_ctrl; ylva_original:l_armA_wrist_ctrl; ylva_original:r_armA_wrist_ctrl; ylva_original:m_spineA_head_ctrl; ylva_original:m_spineA_neck_03_ctrl; ylva_original:m_spineA_neck_02_ctrl; ylva_original:m_spineA_neck_01_ctrl; ylva_original:RgtOuterBrow; ylva_original:RgtMidBrow; ylva_original:LftMidBrow; ylva_original:LftOuterBrow; ylva_original:rgtHappyBrow; ylva_original:rgtMadBrow; ylva_original:rgtSadBrow; ylva_original:rgtBoredBrow; ylva_original:lftHappyBrow; ylva_original:lftMadBrow; ylva_original:lftSadBrow; ylva_original:lftBoredBrow; ylva_original:RgtTopLid; ylva_original:LftTopLid; ylva_original:RgtBtmLid; ylva_original:LftBtmLid; ylva_original:eyeDarts; ylva_original:MouthEmotion; ylva_original:MouthSlide; ylva_original:RgtbigEye; ylva_original:LftbigEye; ylva_original:RgteyeSquint; ylva_original:LfteyeSquint; ylva_original:RgtUpEyeLid; ylva_original:RgtDownEyeLid; ylva_original:LftUpEyeLid; ylva_original:LftDownEyeLid; ylva_original:mouthWideNarrow; ylva_original:facialCtrlVis; ylva_original:faceGui; ylva_original:l_armA_elbow_FK_ctrl; ylva_original:l_armA_uprarm_FK_ctrl; ylva_original:r_armA_elbow_FK_ctrl; ylva_original:r_armA_uprarm_FK_ctrl; ylva_original:l_legA_ankle_ctrl; ylva_original:r_legA_ankle_ctrl; ylva_original:skirt_midwire_1_ctrl; ylva_original:skirt_midwire_2_ctrl; ylva_original:skirt_midwire_3_ctrl; ylva_original:skirt_midwire_4_ctrl; ylva_original:skirt_midwire_5_ctrl; ylva_original:skirt_midwire_6_ctrl; ylva_original:skirt_midwire_7_ctrl; ylva_original:skirt_midwire_8_ctrl; ylva_original:skirt_lwrwire_1_ctrl; ylva_original:skirt_lwrwire_2_ctrl; ylva_original:skirt_lwrwire_3_ctrl; ylva_original:skirt_lwrwire_4_ctrl; ylva_original:skirt_lwrwire_5_ctrl; ylva_original:skirt_lwrwire_6_ctrl; ylva_original:skirt_lwrwire_7_ctrl; ylva_original:skirt_lwrwire_8_ctrl; ylva_original:hair_ex_ctrl; ylva_original:top_ctrl; ylva_original:tongoueA_Rot_Ctrl; ylva_original:tongoueB_Rot_Ctrl; ylva_original:tongoueC_Rot_Ctrl; ylva_original:tongueIn1_Ctrl; ylva_original:m_tongueTip_Ctrl; ylva_original:m_tongue_subC_Ctrl; ylva_original:m_tongue_subB_Ctrl; ylva_original:m_tongue_subA_Ctrl; ylva_original:tongueCon_ctrl; ylva_original:tongueCurve; ylva_original:m_jaw_ctrl; ylva_original:l_eye_ctrl; ylva_original:r_eye_ctrl; ylva_original:m_bothEye_ctrl; ylva_original:m_eye_ctrl; ylva_original:l_teethBtmA_ctrl; ylva_original:r_teethBtmA_ctrl; ylva_original:m_teethBtmB_ctrl; ylva_original:m_teethBtmA_ctrl; ylva_original:l_teethTopA_ctrl; ylva_original:r_teethTopA_ctrl; ylva_original:m_teethTopB_ctrl; ylva_original:m_teethTopA_ctrl; ylva_original:head_squash_ctrl; ");
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
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".uprarmStretch";
	setAttr -k on ".forearmStretch";
	setAttr ".ObjName" -type "string" "ylva_original:l_armA_hand_IK_ctrl";
createNode locator -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1Shape" -p
		 "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "uprarmStretch" -ln "uprarmStretch" -at "double";
	addAttr -ci true -sn "forearmStretch" -ln "forearmStretch" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".uprarmStretch";
	setAttr -k on ".forearmStretch";
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
createNode transform -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
createNode transform -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
createNode transform -n "ylva_original:faceGui_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr ".ObjName" -type "string" "ylva_original:faceGui";
createNode locator -n "ylva_original:faceGui_outPutAnimBank_1Shape" -p "ylva_original:faceGui_outPutAnimBank_1";
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
createNode transform -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "subCtrl" -ln "subCtrl" -at "long";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k on ".subCtrl";
	setAttr ".ObjName" -type "string" "ylva_original:hair_ex_ctrl";
createNode locator -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1Shape" -p "ylva_original:hair_ex_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "ylva_original:top_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "globalScale" -ln "globalScale" -at "double";
	addAttr -ci true -sn "bodyRes" -ln "bodyRes" -at "long";
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
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_wide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_spineA_waistFree_ctrl_outPutAnimBank_1_thick";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
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
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
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
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.38720380897010459 8 0.41279622623430268
		 16 -0.38720380897010459 24 0.41279622623430268 32 -0.38720380897010459;
createNode animCurveTA -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -3.0000000000000004 16 3.0000000000000004
		 32 -3.0000000000000004;
createNode animCurveTA -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 2.1891179769295692 4 2.598353012362367
		 8 0.42156676857938929 12 -1.3925539550453607 16 -0.022311845028931399 24 5.4814434221354116
		 28 4.0633205402564911 32 2.1891179769295692;
	setAttr -s 8 ".kit[0:7]"  3 18 9 9 18 3 9 3;
	setAttr -s 8 ".kot[0:7]"  3 18 9 9 18 3 9 3;
createNode animCurveTL -n "ylva_original:m_spineA_chest_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
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
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
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
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kot[0:8]"  1 3 3 18 18 18 18 18 
		1;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.3 8 0.3 16 -0.3 24 0.3 32 -0.3;
	setAttr -s 5 ".kit[1:4]"  18 3 18 3;
	setAttr -s 5 ".kot[1:4]"  18 3 18 3;
createNode animCurveTA -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -3.0000000000000004 16 3.0000000000000004
		 32 -3.0000000000000004;
createNode animCurveTA -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0.99267490033858952 6 2.5828083758632898
		 8 2.9084299665680287 16 0.31473192812793244 20 -1.6817461322160387 22 -2.8223677502608635
		 24 -3.3028021228298541 32 0.99267490033858952;
	setAttr -s 8 ".kit[0:7]"  9 18 18 1 18 18 1 1;
	setAttr -s 8 ".kot[0:7]"  9 18 18 1 18 18 1 1;
	setAttr -s 8 ".kix[3:7]"  0.97932994365692139 0.97495055198669434 
		0.98472291231155396 0.99937975406646729 0.95783686637878418;
	setAttr -s 8 ".kiy[3:7]"  -0.20226943492889404 -0.22242163121700287 
		-0.17412836849689484 -0.035217531025409698 0.28731262683868408;
	setAttr -s 8 ".kox[3:7]"  0.97932994365692139 0.97495055198669434 
		0.98472291231155396 0.99937969446182251 0.95783686637878418;
	setAttr -s 8 ".koy[3:7]"  -0.20226944983005524 -0.22242161631584167 
		-0.17412836849689484 -0.035217531025409698 0.28731259703636169;
createNode animCurveTL -n "ylva_original:m_spineA_waist_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTA -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 32 0;
	setAttr -s 2 ".kit[1]"  1;
	setAttr -s 2 ".kot[1]"  1;
	setAttr -s 2 ".kix[1]"  1;
	setAttr -s 2 ".kiy[1]"  0;
	setAttr -s 2 ".kox[1]"  1;
	setAttr -s 2 ".koy[1]"  0;
createNode animCurveTA -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 2 16 -2 32 2;
createNode animCurveTA -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 4.4743048653888264 32 4.4743048653888264;
createNode animCurveTL -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_rotatePivotY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_wide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_thick";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:m_spineA_hip_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTA -n "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0.81288084234791869 12 0.81288084234791869
		 16 0.81288084234791869 20 0.81288084234791869 28 0.81288084234791869 32 0.81288084234791869;
createNode animCurveTA -n "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 0 32 0;
createNode animCurveTA -n "ylva_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.77060319741122807 8 -0.19072329505950317
		 16 -0.76399878443065694 24 -1.3372742738018109 32 -0.77060319741122807;
	setAttr -s 5 ".kit[0:4]"  9 18 18 18 9;
	setAttr -s 5 ".kot[0:4]"  9 18 18 18 9;
createNode animCurveTL -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 9 -0.1 24 0.1 32 0;
	setAttr -s 4 ".kit[0:3]"  9 18 18 9;
	setAttr -s 4 ".kot[0:3]"  9 18 18 9;
createNode animCurveTL -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0.1 8 -0.16555369606621473 16 0.1 24 -0.1699236195184991
		 32 0.1;
createNode animCurveTL -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -0.50583301366222033 16 -0.50583301366222033
		 28 -0.50583301366222033 32 -0.50583301366222033;
	setAttr -s 4 ".kit[0:3]"  1 18 18 1;
	setAttr -s 4 ".kot[0:3]"  1 18 18 1;
	setAttr -s 4 ".kix[0:3]"  1 1 1 1;
	setAttr -s 4 ".kiy[0:3]"  0 0 0 0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0.015203441248335156 7 0.14722723373054999
		 15 0.012702166880896001 23 0.14068334196372256 32 0.015203441248335156;
	setAttr -s 5 ".kit[0:4]"  3 18 18 18 3;
	setAttr -s 5 ".kot[0:4]"  3 18 18 18 3;
createNode animCurveTA -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 5 16 -5 32 5;
	setAttr -s 3 ".kit[1:2]"  18 1;
	setAttr -s 3 ".kot[1:2]"  18 1;
	setAttr -s 3 ".kix[2]"  1;
	setAttr -s 3 ".kiy[2]"  0;
	setAttr -s 3 ".kox[2]"  1;
	setAttr -s 3 ".koy[2]"  0;
createNode animCurveTA -n "ylva_original:m_spineA_body_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -0.60350934387587796 8 -1.4954013063304537
		 22 0.89436151132663255 32 -0.60350934387587796;
	setAttr -s 4 ".kit[0:3]"  1 18 18 1;
	setAttr -s 4 ".kot[0:3]"  1 18 18 1;
	setAttr -s 4 ".kix[0:3]"  0.99571740627288818 1 1 0.99359291791915894;
	setAttr -s 4 ".kiy[0:3]"  -0.092449329793453217 0 0 -0.11301867663860321;
	setAttr -s 4 ".kox[0:3]"  0.99571740627288818 1 1 0.99359291791915894;
	setAttr -s 4 ".koy[0:3]"  -0.092449337244033813 0 0 -0.11301866918802261;
createNode animCurveTA -n "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTL -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 -0.085919060734705482 4 -0.087668223383194618
		 12 -0.35377533588209775 16 -0.64924349797461467 18 -0.64924349797461467 20 -0.64924349797461467
		 24 -0.64924349797461467 32 -0.085919060734705482;
	setAttr -s 8 ".kit[2:7]"  1 3 3 3 18 18;
	setAttr -s 8 ".kot[2:7]"  1 3 3 3 18 18;
	setAttr -s 8 ".kix[2:7]"  0.38890179991722107 1 1 1 1 1;
	setAttr -s 8 ".kiy[2:7]"  -0.92127925157546997 0 0 0 0 0;
	setAttr -s 8 ".kox[2:7]"  0.38890182971954346 1 1 1 1 1;
	setAttr -s 8 ".koy[2:7]"  -0.9212791919708252 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 -4.565 2 -4.7159591259731632 5 -3.5411648594746188
		 14 1.0813588471408542 16 1.4564144457377299 18 0.89572944966462076 20 0.1131767293193594
		 24 -1.5055043113437923 28 -3.0424600257444387 32 -4.5645561502928835;
	setAttr -s 10 ".kit[0:9]"  9 9 9 18 9 18 18 18 
		18 9;
	setAttr -s 10 ".kot[0:9]"  9 9 9 18 2 18 18 18 
		18 9;
createNode animCurveTA -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0 4 0.4911933786510469 8 2.1752777423465424
		 12 4.9765423601109973 16 -12.043032977502373 18 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0.57253997459411154 4 0.80278291035388194
		 8 1.0449817019489069 12 0.97895526476442041 14 0.39335304589440556 16 0.1418975153172726
		 20 0 24 0 28 0.24914563735939732 32 0.57253997459411154;
	setAttr -s 10 ".kit[0:9]"  9 9 1 9 18 18 18 18 
		1 9;
	setAttr -s 10 ".kot[0:9]"  9 9 1 9 18 18 18 18 
		1 9;
	setAttr -s 10 ".kix[2:9]"  0.70015716552734375 0.34561187028884888 
		0.18774665892124176 0.52084559202194214 1 1 0.41966003179550171 0.44344654679298401;
	setAttr -s 10 ".kiy[2:9]"  0.7139887809753418 -0.9383774995803833 
		-0.98221749067306519 -0.85365080833435059 0 0 0.90768140554428101 0.8963007926940918;
	setAttr -s 10 ".kox[2:9]"  0.70015716552734375 0.34561187028884888 
		0.18774665892124176 0.52084565162658691 1 1 0.41966003179550171 0.44344654679298401;
	setAttr -s 10 ".koy[2:9]"  0.7139887809753418 -0.9383774995803833 
		-0.98221749067306519 -0.85365086793899536 0 0 0.90768134593963623 0.8963007926940918;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 63.799090421368483 2 67.043154558932585
		 4 62.421435214247495 8 27.908076870529904 12 2.5479443606817185 14 -6.8815070991188279
		 15 -5.2407497042168663 16 0 20 0 24 0 28 37.300917730674435 32 63.799090421368483;
	setAttr -s 12 ".kit[0:11]"  9 18 18 18 18 18 18 18 
		18 18 18 9;
	setAttr -s 12 ".kot[0:11]"  9 18 18 18 18 18 18 18 
		18 18 18 9;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0 4 1.079976827431788 8 3.2349537848171597
		 12 6.544145882935485 16 8.6 18 7.0210526315789448 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_footSide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:l_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:r_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:r_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTL -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0.62420995401175094 4 0.62420995401175094
		 8 0.62420995401175094 12 0.41278110064475521 16 0.27909031753899982 20 0.3004215283673542
		 28 0.5369127697159306 32 0.62420995401175094;
	setAttr -s 8 ".kit[2:7]"  3 18 18 1 1 18;
	setAttr -s 8 ".kot[2:7]"  3 18 18 1 1 18;
	setAttr -s 8 ".kix[5:7]"  0.94188469648361206 0.78090327978134155 
		1;
	setAttr -s 8 ".kiy[5:7]"  0.33593642711639404 0.62465202808380127 
		0;
	setAttr -s 8 ".kox[5:7]"  0.94188475608825684 0.78090327978134155 
		1;
	setAttr -s 8 ".koy[5:7]"  0.33593630790710449 0.62465202808380127 
		0;
createNode animCurveTL -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 1.3338451859217482 3 0.5498135144410865
		 12 -2.9691955145654831 16 -4.4502108238845466 19 -4.8262571834470034 20 -4.7182701090247985
		 32 1.3338451859217482;
	setAttr -s 7 ".kit[3:6]"  9 18 9 9;
	setAttr -s 7 ".kot[3:6]"  9 18 9 9;
	setAttr -s 7 ".kix[0:6]"  0.10172287374734879 0.07999999076128006 
		0.10317978262901306 0.14909069240093231 1 0.084115020930767059 0.07906283438205719;
	setAttr -s 7 ".kiy[0:6]"  -0.99481278657913208 -0.78532344102859497 
		-0.99466276168823242 -0.9888235330581665 0 0.99645602703094482 0.99686962366104126;
	setAttr -s 7 ".kox[0:6]"  0.10172288864850998 0.35999998450279236 
		0.10317977517843246 0.14909069240093231 1 0.084115020930767059 0.07906283438205719;
	setAttr -s 7 ".koy[0:6]"  -0.99481284618377686 -3.5339550971984863 
		-0.99466270208358765 -0.9888235330581665 0 0.99645602703094482 0.99686962366104126;
createNode animCurveTA -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 -17.258833266631726 3 0 4 0 8 0 12 0 16 0
		 20 0 24 2.8885836730467829 28 -3.4453342954906017 32 -17.258833266631726;
	setAttr -s 10 ".kit[0:9]"  9 18 18 18 18 18 18 18 
		18 9;
	setAttr -s 10 ".kot[0:9]"  9 18 18 18 18 18 18 18 
		18 9;
createNode animCurveTA -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footHeight";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0.27599999999999997 16 1.203
		 20 1.9000000000000001 24 1.2588816842105259 28 0.32115157894736907 32 0;
	setAttr -s 9 ".kit[6:8]"  1 18 18;
	setAttr -s 9 ".kot[6:8]"  1 18 18;
	setAttr -s 9 ".kix[6:8]"  0.1283513605594635 0.24635924398899078 
		1;
	setAttr -s 9 ".kiy[6:8]"  -0.99172878265380859 -0.96917861700057983 
		0;
	setAttr -s 9 ".kox[6:8]"  0.12835134565830231 0.24635924398899078 
		1;
	setAttr -s 9 ".koy[6:8]"  -0.99172878265380859 -0.96917861700057983 
		0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footRoll";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 24.690352493674517 16 48.907867397980922
		 20 53.239204030659181 24 35.420087163354211 28 17.115244808912422 32 0;
	setAttr -s 9 ".kit[3:8]"  1 1 1 18 18 18;
	setAttr -s 9 ".kot[3:8]"  1 1 1 18 18 18;
	setAttr -s 9 ".kix[3:8]"  0.0048649776726961136 0.010498322546482086 
		0.040163282305002213 0.0088580390438437462 0.0090340524911880493 1;
	setAttr -s 9 ".kiy[3:8]"  0.99998819828033447 0.99994492530822754 
		-0.99919319152832031 -0.99996072053909302 -0.99995917081832886 0;
	setAttr -s 9 ".kox[3:8]"  0.0048649776726961136 0.010498320683836937 
		0.040163282305002213 0.0088580381125211716 0.0090340524911880493 1;
	setAttr -s 9 ".koy[3:8]"  0.99998819828033447 0.99994492530822754 
		-0.99919313192367554 -0.99996072053909302 -0.99995917081832886 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeBend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -5 3 6.93439145491533 8 0 12 0 16 0 20 0
		 24 0 28 -14.399998603016368 32 -5;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_heelTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_toeTurn";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_footSide";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_thighStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_shankStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_autoStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_preferredAngle";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:r_legA_foot_IK_ctrl_outPutAnimBank_1_kneeTwist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:l_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:r_legA_pelvis_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_uprarmStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -4.4133389264914147 16 -5.4133389264914147
		 32 -4.4133389264914147;
	setAttr -s 3 ".kit[0:2]"  9 18 18;
	setAttr -s 3 ".kot[0:2]"  9 18 18;
createNode animCurveTU -n "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_forearmStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -4.4133389264914147 16 -5.4133389264914147
		 32 -4.4133389264914147;
	setAttr -s 3 ".kit[0:2]"  9 18 18;
	setAttr -s 3 ".kot[0:2]"  9 18 18;
createNode animCurveTU -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_uprarmStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 2.8000000000000003 32 0;
createNode animCurveTU -n "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_forearmStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 2.8000000000000003 32 0;
createNode animCurveTL -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 8 0 16 0 25 0 32 0;
	setAttr -s 5 ".kit[0:4]"  1 18 1 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 1 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 8 0 16 0 25 0 32 0;
	setAttr -s 5 ".kit[0:4]"  1 18 1 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 1 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTL -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 8 0 16 0 25 0 32 0;
	setAttr -s 5 ".kit[0:4]"  1 18 1 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 1 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 -6.9047346378331662 32 -6.9047346378331662;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 3.0644068880266877 32 3.0644068880266877;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "ylva_original:l_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -28.426078232613779 16 -27.594692922574403
		 32 -28.426078232613779;
	setAttr -s 3 ".kit[1:2]"  9 18;
	setAttr -s 3 ".kot[1:2]"  9 18;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 8 0 16 0 25 0 32 0;
createNode animCurveTL -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 8 0 16 0 25 0 32 0;
createNode animCurveTL -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 8 0 16 0 25 0 32 0;
createNode animCurveTA -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 9.3944530238280244 32 9.3944530238280244;
createNode animCurveTA -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 16.71104991868253 32 16.71104991868253;
createNode animCurveTA -n "ylva_original:r_armA_shoulder_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -20.242096630654078 16 -21.132985808614727
		 32 -20.242096630654078;
createNode animCurveTA -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 29.226087056547055 32 29.226087056547055;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 4.2510370129013992 32 4.2510370129013992;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 -0.82589306750555125 32 -0.82589306750555125;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 32 0;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_neutral";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 32 1;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_fist";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0.4 32 0.4;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_relax";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 32 0;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_curl";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 32 0;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_spread";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 32 0;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_splay";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 32 0;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_break";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 32 0;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_flex";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 32 0;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 15.056219893716531 32 15.056219893716531;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0.84392198096090587 32 0.84392198096090587;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 6.0861566353577388 32 6.0861566353577388;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
	setAttr -s 2 ".kix[0:1]"  1 1;
	setAttr -s 2 ".kiy[0:1]"  0 0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 16 0 25 0 32 0;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_neutral";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 7 1 16 1 25 1 32 1;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_fist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0.4 7 0.4 16 0.4 25 0.4 32 0.4;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_relax";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 16 0 25 0 32 0;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_curl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 16 0 25 0 32 0;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_spread";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 16 0 25 0 32 0;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_splay";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 16 0 25 0 32 0;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_break";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 16 0 25 0 32 0;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_flex";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 16 0 25 0 32 0;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_orbit";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_nod";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_side";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_twist";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_neckStretch";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:m_spineA_head_ctrl_outPutAnimBank_1_compensation";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTL -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 0 32 0;
	setAttr -s 3 ".kit[1:2]"  18 1;
	setAttr -s 3 ".kot[1:2]"  18 1;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 0 32 0;
	setAttr -s 3 ".kit[1:2]"  18 1;
	setAttr -s 3 ".kot[1:2]"  18 1;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 0 32 0;
	setAttr -s 3 ".kit[1:2]"  18 1;
	setAttr -s 3 ".kot[1:2]"  18 1;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -4.5776862708926469 16 5.7795272670209199
		 32 -4.5776862708926469;
	setAttr -s 3 ".kit[1:2]"  10 3;
	setAttr -s 3 ".kot[1:2]"  10 3;
createNode animCurveTA -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 0 32 0;
	setAttr -s 3 ".kit[1:2]"  10 3;
	setAttr -s 3 ".kot[1:2]"  10 3;
createNode animCurveTA -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 4.8373799099558141 3 4.27487991062437
		 10 6.3975264906454807 18 4.27487991062437 26 6.3975264906454807 32 4.8373803107155586;
	setAttr -s 6 ".kit[1:5]"  3 10 10 1 1;
	setAttr -s 6 ".kot[1:5]"  3 10 10 1 1;
	setAttr -s 6 ".kix[0:5]"  0.9869343638420105 1 1 1 0.99999850988388062 
		0.98497283458709717;
	setAttr -s 6 ".kiy[0:5]"  -0.1611228883266449 0 0 0 0.0017210611840710044 
		-0.1727093905210495;
	setAttr -s 6 ".kox[0:5]"  0.98693442344665527 1 1 1 0.99999850988388062 
		0.98497289419174194;
	setAttr -s 6 ".koy[0:5]"  -0.1611228734254837 0 0 0 0.0017210603691637516 
		-0.17270936071872711;
createNode animCurveTU -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 16 1 32 1;
	setAttr -s 3 ".kit[1:2]"  18 1;
	setAttr -s 3 ".kot[1:2]"  18 1;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 16 1 32 1;
	setAttr -s 3 ".kit[1:2]"  18 1;
	setAttr -s 3 ".kot[1:2]"  18 1;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "ylva_original:m_spineA_neck_03_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 16 1 32 1;
	setAttr -s 3 ".kit[1:2]"  18 1;
	setAttr -s 3 ".kot[1:2]"  18 1;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 0 32 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 0 32 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 0 32 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 0 32 0;
	setAttr -s 3 ".kit[2]"  1;
	setAttr -s 3 ".kot[2]"  1;
	setAttr -s 3 ".kix[2]"  1;
	setAttr -s 3 ".kiy[2]"  0;
	setAttr -s 3 ".kox[2]"  1;
	setAttr -s 3 ".koy[2]"  0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 8 -1.5674262342569811 16 0.40483984956098146
		 24 2.3771059333789442 32 0;
	setAttr -s 5 ".kit[0:4]"  9 18 18 18 1;
	setAttr -s 5 ".kot[0:4]"  9 18 18 18 1;
	setAttr -s 5 ".kix[4]"  0.99526101350784302;
	setAttr -s 5 ".kiy[4]"  -0.097239665687084198;
	setAttr -s 5 ".kox[4]"  0.99526101350784302;
	setAttr -s 5 ".koy[4]"  -0.097239665687084198;
createNode animCurveTA -n "ylva_original:m_spineA_neck_02_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 32 0;
createNode animCurveTL -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
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
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
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
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
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
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
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
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 1 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0 0;
createNode animCurveTA -n "ylva_original:m_spineA_neck_01_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 32 0;
createNode animCurveTU -n "ylva_original:RgtOuterBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtOuterBrow_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.49988739700000001;
createNode animCurveTL -n "ylva_original:RgtOuterBrow_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:RgtOuterBrow_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:RgtMidBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtMidBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:RgtMidBrow_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.49988739700000001;
createNode animCurveTA -n "ylva_original:RgtMidBrow_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:LftMidBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftMidBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:LftMidBrow_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.49988739700000001;
createNode animCurveTA -n "ylva_original:LftMidBrow_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:LftOuterBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftOuterBrow_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.49988739700000001;
createNode animCurveTA -n "ylva_original:LftOuterBrow_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:rgtHappyBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTU -n "ylva_original:rgtMadBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:rgtMadBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:rgtSadBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:rgtSadBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.39123053969999999;
createNode animCurveTU -n "ylva_original:rgtBoredBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:rgtBoredBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:lftHappyBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTU -n "ylva_original:lftMadBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:lftMadBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:lftSadBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:lftSadBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.39123053969999999;
createNode animCurveTU -n "ylva_original:lftBoredBrow_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:lftBoredBrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:RgtTopLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtTopLid_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 -0.1068386088;
createNode animCurveTU -n "ylva_original:LftTopLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftTopLid_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 -0.1068386088;
createNode animCurveTU -n "ylva_original:RgtBtmLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtBtmLid_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.20906160082099096;
createNode animCurveTU -n "ylva_original:LftBtmLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftBtmLid_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.20906160082099096;
createNode animCurveTU -n "ylva_original:eyeDarts_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:eyeDarts_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:eyeDarts_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:MouthEmotion_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTL -n "ylva_original:MouthEmotion_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTL -n "ylva_original:MouthSlide_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTL -n "ylva_original:MouthSlide_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTU -n "ylva_original:RgtbigEye_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtbigEye_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.25;
createNode animCurveTU -n "ylva_original:LftbigEye_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftbigEye_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.25;
createNode animCurveTU -n "ylva_original:RgteyeSquint_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgteyeSquint_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:LfteyeSquint_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LfteyeSquint_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:RgtUpEyeLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtUpEyeLid_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.25;
createNode animCurveTU -n "ylva_original:RgtDownEyeLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:RgtDownEyeLid_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:LftUpEyeLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftUpEyeLid_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.25;
createNode animCurveTU -n "ylva_original:LftDownEyeLid_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:LftDownEyeLid_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTL -n "ylva_original:mouthWideNarrow_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTL -n "ylva_original:mouthWideNarrow_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTU -n "ylva_original:facialCtrlVis_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:facialCtrlVis_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:faceGui_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "ylva_original:faceGui_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 5.4;
createNode animCurveTL -n "ylva_original:faceGui_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 13.62705487;
createNode animCurveTL -n "ylva_original:faceGui_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 -1.065814104e-016;
createNode animCurveTA -n "ylva_original:faceGui_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:faceGui_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTA -n "ylva_original:faceGui_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0;
createNode animCurveTU -n "ylva_original:faceGui_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.3;
createNode animCurveTU -n "ylva_original:faceGui_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.3;
createNode animCurveTU -n "ylva_original:faceGui_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  33 0.3;
createNode animCurveTA -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 10.015407826155226 7 18.741227791410473
		 16 10.971856909099325 25 2.3145723487510717 32 10.015407826155226;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 0.9290543794631958 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 -0.3699432909488678 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 0.92905431985855103 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 -0.36994326114654541 0 0;
createNode animCurveTA -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -6.1763878855464602 7 4.2012601329174082
		 16 -3.8269729830485049 25 -1.3565494156501641 32 -6.1763878855464602;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -32.027334356261264 7 -32.346288067788045
		 16 -30.736621596377738 25 -16.959511758262234 32 -32.027334356261264;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 0.97367227077484131 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0.2279527336359024 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 0.97367227077484131 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0.2279527336359024 0 0;
createNode animCurveTU -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 16 1 32 1;
	setAttr -s 3 ".kit[0:2]"  1 18 18;
	setAttr -s 3 ".kot[0:2]"  1 18 18;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_elbow_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 0 32 0;
	setAttr -s 3 ".kit[0:2]"  1 18 18;
	setAttr -s 3 ".kot[0:2]"  1 18 18;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 88.98097630641503 7 82.571190091048649
		 16 84.020194423361133 25 99.093166406471909 32 48.218836410732038;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 0.97850579023361206 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0.20621925592422485 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 0.97850584983825684 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0.20621927082538605 0 0;
createNode animCurveTA -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 42.584652956475274 7 42.61884435659428
		 16 42.887395732794644 25 48.83781076484231 32 49.907010103148259;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 0.99997216463088989 0.99923807382583618 
		0.98216593265533447 1;
	setAttr -s 5 ".kiy[0:4]"  0 0.0074591985903680325 0.039029452949762344 
		0.18801631033420563 0;
	setAttr -s 5 ".kox[0:4]"  1 0.99997216463088989 0.99923807382583618 
		0.98216593265533447 1;
	setAttr -s 5 ".koy[0:4]"  0 0.0074591985903680325 0.039029456675052643 
		0.18801631033420563 0;
createNode animCurveTA -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -21.228297371209457 7 -23.847591060008405
		 16 -24.338376340139693 25 -31.121138893420579 32 -26.330061365359157;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 0.99746203422546387 0.99746197462081909 
		1 1;
	setAttr -s 5 ".kiy[0:4]"  0 -0.071200661361217499 -0.071200661361217499 
		0 0;
	setAttr -s 5 ".kox[0:4]"  1 0.99746197462081909 0.99746197462081909 
		1 1;
	setAttr -s 5 ".koy[0:4]"  0 -0.071200661361217499 -0.071200661361217499 
		0 0;
createNode animCurveTU -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 16 1 32 1;
	setAttr -s 3 ".kit[0:2]"  1 18 18;
	setAttr -s 3 ".kot[0:2]"  1 18 18;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 16 0 32 0;
	setAttr -s 3 ".kit[0:2]"  1 18 18;
	setAttr -s 3 ".kot[0:2]"  1 18 18;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "ylva_original:l_armA_uprarm_FK_ctrl_outPutAnimBank_1_compensation";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 16 1 32 1;
	setAttr -s 3 ".kit[0:2]"  1 18 18;
	setAttr -s 3 ".kot[0:2]"  1 18 18;
	setAttr -s 3 ".kix[0:2]"  1 1 1;
	setAttr -s 3 ".kiy[0:2]"  0 0 0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTA -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 30.80768981073706 7 23.709999286375712
		 11 27.091710073004105 16 31.022666999999995 20 29.654362368345417 25 28.161365514684775
		 32 30.80768981073706;
	setAttr -s 7 ".kit[0:6]"  1 18 18 18 18 18 18;
	setAttr -s 7 ".kot[0:6]"  1 18 18 18 18 18 18;
	setAttr -s 7 ".kix[0:6]"  1 1 0.94251996278762817 1 0.99051505327224731 
		1 1;
	setAttr -s 7 ".kiy[0:6]"  0 0 0.33414986729621887 0 -0.13740405440330505 
		0 0;
	setAttr -s 7 ".kox[0:6]"  1 1 0.94251996278762817 1 0.99051511287689209 
		1 1;
	setAttr -s 7 ".koy[0:6]"  0 0 0.33414986729621887 0 -0.13740406930446625 
		0 0;
createNode animCurveTA -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 8.8658636603465784 7 11.72643806886733
		 11 14.46437617368335 16 14.310361000000002 20 13.239567140085793 25 10.021706521391891
		 32 8.8658636603465784;
	setAttr -s 7 ".kit[0:6]"  1 18 18 18 18 18 18;
	setAttr -s 7 ".kot[0:6]"  1 18 18 18 18 18 18;
	setAttr -s 7 ".kix[0:6]"  1 0.97143560647964478 1 0.9991881251335144 
		0.97906118631362915 0.98758929967880249 1;
	setAttr -s 7 ".kiy[0:6]"  0 0.23730343580245972 0 -0.040288344025611877 
		-0.20356623828411102 -0.15705865621566772 0;
	setAttr -s 7 ".kox[0:6]"  1 0.971435546875 1 0.99918806552886963 
		0.97906112670898438 0.98758929967880249 1;
	setAttr -s 7 ".koy[0:6]"  0 0.23730343580245972 0 -0.040288344025611877 
		-0.20356622338294983 -0.15705864131450653 0;
createNode animCurveTA -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -29.119333980287962 7 -26.237402565550816
		 11 -26.58169477013832 16 -30.255995 20 -27.219121557094592 25 -29.186991179128007
		 32 -29.119333980287962;
	setAttr -s 7 ".kit[0:6]"  1 18 18 18 18 18 18;
	setAttr -s 7 ".kot[0:6]"  1 18 18 18 18 18 18;
	setAttr -s 7 ".kix[0:6]"  1 1 0.99371254444122314 1 1 1 1;
	setAttr -s 7 ".kiy[0:6]"  0 0 -0.11196095496416092 0 0 0 0;
	setAttr -s 7 ".kox[0:6]"  1 1 0.99371260404586792 1 1 1 1;
	setAttr -s 7 ".koy[0:6]"  0 0 -0.11196096241474152 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 7 1 16 1 25 1 32 1;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_elbow_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0.5 7 0.5 16 0.5 25 0.5 32 0.5;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTA -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 75.125186150896326 7 77.506467051065087
		 16 79.832278 25 79.978163921696762 32 75.125186150896326;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 0.99075579643249512 0.99977493286132813 
		1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0.13565799593925476 0.02121347188949585 
		0 0;
	setAttr -s 5 ".kox[0:4]"  1 0.99075573682785034 0.99977493286132813 
		1 1;
	setAttr -s 5 ".koy[0:4]"  0 0.13565801084041595 0.02121347188949585 
		0 0;
createNode animCurveTA -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 49.206526636322735 7 52.63374436236316
		 16 53.577124 25 53.826992162385977 32 49.206526636322735;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 0.99201500415802002 0.99958193302154541 
		1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0.12612034380435944 0.028913049027323723 
		0 0;
	setAttr -s 5 ".kox[0:4]"  1 0.99201500415802002 0.99958193302154541 
		1 1;
	setAttr -s 5 ".koy[0:4]"  0 0.12612035870552063 0.028913049027323723 
		0 0;
createNode animCurveTA -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -37.45636356887546 7 -34.983422658685264
		 16 -35.703798 25 -35.739913532821461 32 -37.45636356887546;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 0.99998617172241211 0.99998623132705688 
		1;
	setAttr -s 5 ".kiy[0:4]"  0 0 -0.0052527184598147869 -0.0052527189254760742 
		0;
	setAttr -s 5 ".kox[0:4]"  1 1 0.99998623132705688 0.99998617172241211 
		1;
	setAttr -s 5 ".koy[0:4]"  0 0 -0.0052527189254760742 -0.0052527184598147869 
		0;
createNode animCurveTU -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 7 1 16 1 25 1 32 1;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_twistBlend";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 16 0 25 0 32 0;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTU -n "ylva_original:r_armA_uprarm_FK_ctrl_outPutAnimBank_1_compensation";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1 7 1 16 1 25 1 32 1;
	setAttr -s 5 ".kit[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kot[0:4]"  1 18 18 18 18;
	setAttr -s 5 ".kix[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".kiy[0:4]"  0 0 0 0 0;
	setAttr -s 5 ".kox[0:4]"  1 1 1 1 1;
	setAttr -s 5 ".koy[0:4]"  0 0 0 0 0;
createNode animCurveTA -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:l_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_FK_2_IK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:r_legA_ankle_ctrl_outPutAnimBank_1_globalIK_2_localIK";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_1_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_2_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_3_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_4_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_5_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_6_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_7_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 8.8817841970012523e-016 4 0 8 0 12 0 16 0
		 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_midwire_8_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 2.7755575615628914e-017 4 0 8 0 12 0 16 0
		 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.84381747202947199 4 0.84381747202947199
		 8 0.84381747202947199 12 0.84381747202947199 16 0.84381747202947199 20 0.84381747202947199
		 24 0.84381747202947199 28 0.84381747202947199 32 0.84381747202947199;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_1_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.84381747202947199 4 0.84381747202947199
		 8 0.84381747202947199 12 0.84381747202947199 16 0.84381747202947199 20 0.84381747202947199
		 24 0.84381747202947199 28 0.84381747202947199 32 0.84381747202947199;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_2_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.84381747202947199 4 0.84381747202947199
		 8 0.84381747202947199 12 0.84381747202947199 16 0.84381747202947199 20 0.84381747202947199
		 24 0.84381747202947199 28 0.84381747202947199 32 0.84381747202947199;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_3_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.84381747202947199 4 0.84381747202947199
		 8 0.84381747202947199 12 0.84381747202947199 16 0.84381747202947199 20 0.84381747202947199
		 24 0.84381747202947199 28 0.84381747202947199 32 0.84381747202947199;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_4_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.84381747202947199 4 0.84381747202947199
		 8 0.84381747202947199 12 0.84381747202947199 16 0.84381747202947199 20 0.84381747202947199
		 24 0.84381747202947199 28 0.84381747202947199 32 0.84381747202947199;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_5_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0.33245434488063336 2 0.72309304772050687
		 4 -0.0017484992919791758 8 0 12 0 16 0 20 0 24 0 28 -0.020996829841620837 32 0.33245434488063336;
	setAttr -s 10 ".kit[0:9]"  1 18 18 18 18 18 18 18 
		18 18;
	setAttr -s 10 ".kot[0:9]"  1 18 18 18 18 18 18 18 
		18 18;
	setAttr -s 10 ".kix[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".kiy[0:9]"  0 0 0 0 0 0 0 0 0 0;
	setAttr -s 10 ".kox[0:9]"  1 1 1 1 1 1 1 1 1 1;
	setAttr -s 10 ".koy[0:9]"  0 0 0 0 0 0 0 0 0 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1.5235499628425113 4 1.5449815346719218
		 8 0.84381747202947199 12 0.84381747202947199 16 0.84381747202947199 20 0.84381747202947199
		 24 0.84381747202947199 28 1.0072169704188449 32 1.5235499628425113;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 1 1 1 1 1 1 0.42593422532081604 1;
	setAttr -s 9 ".kiy[0:8]"  0 0 0 0 0 0 0 0.9047541618347168 0;
	setAttr -s 9 ".kox[0:8]"  1 1 1 1 1 1 1 0.42593419551849365 1;
	setAttr -s 9 ".koy[0:8]"  0 0 0 0 0 0 0 0.9047541618347168 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_6_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 2.0197492809282682 4 1.2794546604212502
		 8 0 12 0 16 0 20 0 24 0 28 0.93504827747728814 32 2.0197492809282682;
	setAttr -s 9 ".kit[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kot[0:8]"  1 18 18 18 18 18 18 18 
		18;
	setAttr -s 9 ".kix[0:8]"  1 0.13731783628463745 1 1 1 1 1 0.15648366510868073 
		1;
	setAttr -s 9 ".kiy[0:8]"  0 -0.99052709341049194 0 0 0 0 0 0.98768055438995361 
		0;
	setAttr -s 9 ".kox[0:8]"  1 0.13731782138347626 1 1 1 1 1 0.15648366510868073 
		1;
	setAttr -s 9 ".koy[0:8]"  0 -0.99052703380584717 0 0 0 0 0 0.98768055438995361 
		0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 -0.67318417398760733 16 -1.3840591312279851
		 20 -0.56950541693286261 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.84381747202947199 4 0.84381747202947199
		 8 0.84381747202947199 12 1.1288308570740808 16 1.3127634999908036 20 1.6510972933219588
		 24 0.84381747202947199 28 0.84381747202947199 32 0.84381747202947199;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_7_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 1.2764588774970294 16 2.262707441952633
		 20 1.6737054648004794 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.84381747202947199 4 0.84381747202947199
		 8 0.84381747202947199 12 0.84381747202947199 16 0.84381747202947199 20 0.84381747202947199
		 24 0.84381747202947199 28 0.84381747202947199 32 0.84381747202947199;
createNode animCurveTL -n "ylva_original:skirt_lwrwire_8_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 5;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
	setAttr -s 9 ".kit[0:8]"  9 9 9 9 9 9 9 9 
		1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
createNode animCurveTL -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -0.00020660770125248418 4 0.0097666868753931435
		 8 0.0072539516938125454 12 0.0089601117883126424 16 0.0026520814025220284 20 0.0081417048777622878
		 24 0.0078682617197761932 28 0.0075254381637327164 32 -0.00020660770125248418;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTL -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -0.041676805968393363 4 1.8956386840202946
		 8 1.4065410342469002 12 1.7267976867026198 16 0.49095375078321624 20 1.5526234790842668
		 24 1.5023698604400733 28 1.4449566669972211 32 -0.041676805968393363;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTL -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.67757697999640476 4 0.69797939790337882
		 8 0.66276502847335717 12 0.72130422499467317 16 0.81485119330438471 20 0.74333491345093761
		 24 0.71420438548563236 28 0.65192777097335641 32 0.67757697999640476;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTA -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTA -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTA -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:hair_ex_ctrl_outPutAnimBank_1_subCtrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
	setAttr -s 9 ".kit[8]"  1;
	setAttr -s 9 ".kot[8]"  1;
	setAttr -s 9 ".kix[8]"  1;
	setAttr -s 9 ".kiy[8]"  0;
	setAttr -s 9 ".kox[8]"  1;
	setAttr -s 9 ".koy[8]"  0;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
	setAttr -s 9 ".kot[0:8]"  5 5 5 5 5 5 5 5 
		5;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_globalScale";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_bodyRes";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_hairCtrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:top_ctrl_outPutAnimBank_1_clothCtrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTA -n "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongoueA_Rot_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongoueB_Rot_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongoueC_Rot_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:tongueIn1_Ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTL -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_ratio";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_roll";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_Sub_Ctrl";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_tongueTip_Ctrl_outPutAnimBank_1_ExtraDeformers";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:m_tongue_subC_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTL -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.9999999999999889 4 0.9999999999999889
		 8 0.9999999999999889 12 0.9999999999999889 16 0.9999999999999889 20 0.9999999999999889
		 24 0.9999999999999889 28 0.9999999999999889 32 0.9999999999999889;
createNode animCurveTU -n "ylva_original:m_tongue_subB_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.9999999999999889 4 0.9999999999999889
		 8 0.9999999999999889 12 0.9999999999999889 16 0.9999999999999889 20 0.9999999999999889
		 24 0.9999999999999889 28 0.9999999999999889 32 0.9999999999999889;
createNode animCurveTL -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:m_tongue_subA_Ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTL -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 -0.23682148550000001;
createNode animCurveTL -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 -0.32291556739999999;
createNode animCurveTA -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:tongueCon_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:tongueCurve_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
	setAttr -s 9 ".kot[0:8]"  5 5 5 5 5 5 5 5 
		5;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
	setAttr -s 9 ".kot[0:8]"  5 5 5 5 5 5 5 5 
		5;
createNode animCurveTL -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:m_jaw_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTL -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_crossEyeFix";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_crossEyeRate";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.5 4 0.5 8 0.5 12 0.5 16 0.5 20 0.5 24 0.5
		 28 0.5 32 0.5;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_Iris_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:l_eye_ctrl_outPutAnimBank_1_Pupil_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_crossEyeFix";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_crossEyeRate";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.5 4 0.5 8 0.5 12 0.5 16 0.5 20 0.5 24 0.5
		 28 0.5 32 0.5;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_Iris_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:r_eye_ctrl_outPutAnimBank_1_Pupil_Size";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 -0.0011297796595487668;
createNode animCurveTL -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.36315789473684218 4 0.36315789473684218
		 8 0.36315789473684218 12 0.36315789473684218 16 0.36315789473684218 20 0.36315789473684218
		 24 0.36315789473684218 28 0.36315789473684218 32 0.36315789473684218;
createNode animCurveTL -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_l_eye_offset";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_bothEye_ctrl_outPutAnimBank_1_r_eye_offset";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -0.00020244999999999999 4 -0.00020244999999999999
		 8 -0.00020244999999999999 12 -0.00020244999999999999 16 -0.00020244999999999999 20 -0.00020244999999999999
		 24 -0.00020244999999999999 28 -0.00020244999999999999 32 -0.00020244999999999999;
createNode animCurveTL -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 16.290981800000001 4 16.290981800000001
		 8 16.290981800000001 12 16.290981800000001 16 16.290981800000001 20 16.290981800000001
		 24 16.290981800000001 28 16.290981800000001 32 16.290981800000001;
createNode animCurveTL -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1.68490439 4 1.68490439 8 1.68490439 12 1.68490439
		 16 1.68490439 20 1.68490439 24 1.68490439 28 1.68490439 32 1.68490439;
createNode animCurveTA -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -3.7000000000000006 4 -3.7000000000000006
		 8 -3.7000000000000006 12 -3.7000000000000006 16 -3.7000000000000006 20 -3.7000000000000006
		 24 -3.7000000000000006 28 -3.7000000000000006 32 -3.7000000000000006;
createNode animCurveTA -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTA -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_tx";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.18 4 0.18 8 0.18 12 0.18 16 0.18 20 0.18
		 24 0.18 28 0.18 32 0.18;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_l_eyePSD_sc";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1.215 4 1.215 8 1.215 12 1.215 16 1.215
		 20 1.215 24 1.215 28 1.215 32 1.215;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_bothEye_offset";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 8 4 8 8 8 12 8 16 8 20 8 24 8 28 8 32 8;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_irisSize_temp";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -2.5 4 -2.5 8 -2.5 12 -2.5 16 -2.5 20 -2.5
		 24 -2.5 28 -2.5 32 -2.5;
createNode animCurveTU -n "ylva_original:m_eye_ctrl_outPutAnimBank_1_pupilSize_temp";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -5 4 -5 8 -5 12 -5 16 -5 20 -5 24 -5 28 -5
		 32 -5;
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
createNode animCurveTU -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 1 4 1 8 1 12 1 16 1 20 1 24 1 28 1 32 1;
	setAttr -s 9 ".kot[0:8]"  5 5 5 5 5 5 5 5 
		5;
createNode animCurveTL -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
createNode animCurveTL -n "ylva_original:head_squash_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 12 0 16 0 20 0 24 0 28 0 32 0;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr ".unw" 1;
lockNode -l 1 ;
select -ne :sequenceManager1;
	setAttr ".o" 18;
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
lockNode -l 1 ;
select -ne :defaultTextureList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 88 ".tx";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
lockNode -l 1 ;
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
lockNode -l 1 ;
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
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -k on ".w" 1280;
	setAttr -k on ".h" 720;
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar" 1.7769999504089355;
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
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
lockNode -l 1 ;
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
lockNode -l 1 ;
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
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_uprarmStretch.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.uprarmStretch"
		;
connectAttr "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1_forearmStretch.o" "ylva_original:l_armA_hand_IK_ctrl_outPutAnimBank_1.forearmStretch"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_uprarmStretch.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.uprarmStretch"
		;
connectAttr "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1_forearmStretch.o" "ylva_original:r_armA_hand_IK_ctrl_outPutAnimBank_1.forearmStretch"
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
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:l_armA_wrist_ctrl_outPutAnimBank_1.rz"
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
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateX.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateY.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1_rotateZ.o" "ylva_original:r_armA_wrist_ctrl_outPutAnimBank_1.rz"
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
connectAttr "ylva_original:MouthEmotion_outPutAnimBank_1_translateX.o" "ylva_original:MouthEmotion_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:MouthEmotion_outPutAnimBank_1_translateY.o" "ylva_original:MouthEmotion_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:MouthSlide_outPutAnimBank_1_translateX.o" "ylva_original:MouthSlide_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:MouthSlide_outPutAnimBank_1_translateY.o" "ylva_original:MouthSlide_outPutAnimBank_1.ty"
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
connectAttr "ylva_original:mouthWideNarrow_outPutAnimBank_1_translateX.o" "ylva_original:mouthWideNarrow_outPutAnimBank_1.tx"
		;
connectAttr "ylva_original:mouthWideNarrow_outPutAnimBank_1_translateY.o" "ylva_original:mouthWideNarrow_outPutAnimBank_1.ty"
		;
connectAttr "ylva_original:facialCtrlVis_outPutAnimBank_1_visibility.o" "ylva_original:facialCtrlVis_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:facialCtrlVis_outPutAnimBank_1_translateY.o" "ylva_original:facialCtrlVis_outPutAnimBank_1.ty"
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
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_visibility.o" "ylva_original:top_ctrl_outPutAnimBank_1.v"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_globalScale.o" "ylva_original:top_ctrl_outPutAnimBank_1.globalScale"
		;
connectAttr "ylva_original:top_ctrl_outPutAnimBank_1_bodyRes.o" "ylva_original:top_ctrl_outPutAnimBank_1.bodyRes"
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
// End of yl_walk1.ma
